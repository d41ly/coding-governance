#!/usr/bin/env python3
"""retired_edits.py — the fixture of TOOL-dSafePassage-9: what `update` does with a withdrawn hook
fragment, an edited file gov stopped shipping, and an edited render.

    python <this kit>/fixtures/retired_edits.py --plant <case> [--stub <name>]
                                                 [--write-withdrawals] [--rerender-off]

Each plant builds a scratch gov holding a copy of this kit's `govkit.py`, gov's policy kit beside it
and one `demo` kit (an engine file, a seed, a rendered file with a `[[regenerate]]` argv and a hook
fragment) plus a `settings-merge` entry; installs a target from it, stages the case, runs
`update --write`, and prints each verdict, order, settings entry and receipt role it observed beside
what the case expects. `--stub <name>` stages one named break in the scratch copy, loaded as a module
before its `main` runs, so each red the spec names is seen and the tree is never touched.

Exit 0 every observation matched · 1 one missed its case · 2 the plant could not be built or observed.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import govkit  # noqa: E402 — the deployer itself, for its tool root, its slug and its dispatch tables
from fixture_target import build_scratch_gov, build_target  # noqa: E402 — the scratch repositories' factory

PFX = govkit.derive_tool_root(govkit.repo_root())
PLANTS = ("fragment-withdrawn", "fragment-rollback", "edited-gone", "edited-row", "keep",
          "seed-retired-edited", "seed-retired-clean", "render-edited", "render-clean",
          "render-edited-no-oid", "render-eol-no-oid", "dispatch-gap", "edited-reshipped",
          "edited-rolled-back", "render-edited-kill", "render-filter-broken")
# Each stub is one statement over the scratch module `m`, run after it loads and before its `main`.
STUBS = {
    "forked": 'm.UPDATE_ROLE["retired-edited"] = m.UPDATE_ROLE["forked"]',
    "report-omits": 'm.render_retired_edited_line = lambda *a, **k: ""',
    "today": "m.check_render_edited = lambda *a, **k: False",
    "seed-override": 'm.SEED_KEPT_VERDICTS = ("missing", "renamed")',
    # TOOL-dSafePassage-63: a row with no `oid` graded False, as the check did before its fallback.
    "oid-only": ("m.check_render_edited = lambda t, r, f=m.check_render_edited: "
                 "bool(r.get('oid')) and f(t, r)"),
}
LOADER = ("import importlib.util, sys\n"
          "path, stub, argv = sys.argv[1], sys.argv[2], sys.argv[3:]\n"
          "spec = importlib.util.spec_from_file_location('govkit', path)\n"
          "m = importlib.util.module_from_spec(spec)\n"
          "sys.modules['govkit'] = m\n"
          "spec.loader.exec_module(m)\n"
          "exec(stub, {'m': m})\n"
          "sys.stdout.reconfigure(encoding='utf-8')\n"
          "sys.exit(m.main(argv))\n")
DEMO = "demo"
KIT = ('id = "demo"\nhome = "demo"\nversion_from = { none = "fixture" }\n\n'
       '[check]\nargv = ["bash", "{kit}/check.sh"]\n\n'
       '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
       '[[files]]\ninclude = ["seed.md"]\nrole = "seed"\nto = "docs/seed.md"\n\n'
       '[[files]]\ninclude = ["tpl.md"]\nrole = "rendered"\nto = "docs/out.md"\n\n'
       '[[regenerate]]\nargv = ["bash", "{kit}/gen.sh"]\n\n'
       '[adopt]\nargv = ["bash", "{kit}/gen.sh"]\nmutates_index = false\n')
SM_KIT = ('id = "settings-merge"\nhome = "sm"\nversion_from = { none = "fixture" }\n\n'
          '[check]\nnone = "fixture"\n\n[[files]]\ninclude = "**"\nrole = "engine"\n\n'
          '[adopt]\nargv = []\nmutates_index = false\n')
FILES = {
    "eng.txt": "v1\n",
    "gone.txt": "gov's line\n",
    "seed.md": "seed\n",
    "tpl.md": "tpl v1\n",
    "gen.sh": 'd="$(dirname "$0")"\nmkdir -p docs\ncat "$d/tpl.md" > docs/out.md\n',
    "check.sh": 'if grep -q red "$(dirname "$0")/eng.txt"; then exit 1; fi\nexit 0\n',
    "fixture-hook.js": "// the fixture's hook\n",
    "hook.fragment.json": json.dumps({"name": "fixture-hook", "event": "Stop", "matcher": "*",
                                      "marker": "fixture-hook.js",
                                      "hook_path": "{here}/fixture-hook.js"}) + "\n",
}
FRAG = "hook.fragment.json"
MARKER = "fixture-hook.js"


def resolve_kit_path(*parts: str) -> str:
    """A repo-relative path under the scratch gov's (and target's) tool root."""
    return "/".join(p for p in (PFX, *parts) if p)


def run_git(root: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", env=read_clean_env())


def read_clean_env(extra: dict | None = None) -> dict:
    """The caller's environment without git's location variables or the two knobs `update` reads,
    so an exported GOVKIT_RERENDER or GOV_SETTINGS_JSON cannot move a plant."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")
           and k not in ("GOVKIT_RERENDER", "GOV_SETTINGS_JSON")}
    env["GOVKIT_NO_REMOTE_PROBE"] = "1"
    env.update(extra or {})
    return env


def write_commit(root: pathlib.Path, msg: str) -> None:
    run_git(root, "add", "-A")
    p = run_git(root, "-c", "core.hooksPath=/dev/null", "commit", "-qm", msg)
    if p.returncode != 0 and "nothing to commit" not in p.stdout + p.stderr:
        raise OSError(f"git commit in {root.as_posix()} failed: {p.stderr.strip()}")


def write_gov_files(g: pathlib.Path, files: dict, drop: tuple = ()) -> None:
    for rel, body in files.items():
        (g / resolve_kit_path(DEMO, rel)).write_bytes(body.encode("utf-8"))
    for rel in drop:
        (g / resolve_kit_path(DEMO, rel)).unlink()


def build_retired_gov(tmp: pathlib.Path) -> pathlib.Path:
    """A gov holding a copy of this kit's deployer, gov's policy kit, a settings-merge entry and the
    demo kit, committed once, in the scratch repository `fixture_target`'s factory makes."""
    g = build_scratch_gov(tmp / "gov")
    gk = g / resolve_kit_path(govkit.GOVKIT_DIR.name)
    gk.mkdir(parents=True)
    for name in ("govkit.py", "adopters.toml", "upgrade_steps.py"):
        shutil.copy2(govkit.GOVKIT_DIR / name, gk / name)
    (gk / govkit.REGISTRY_NAME).write_text(
        '[surface]\nglobs = ["{prefix}/*"]\n\n[selection]\ndefault = ["demo", "settings-merge"]\n\n'
        '[[entry]]\nid = "demo"\ndescriptor = "{prefix}/demo/kit.toml"\n\n'
        '[[entry]]\nid = "settings-merge"\ndescriptor = "{prefix}/sm/kit.toml"\n\n'
        f'[[exempt]]\npath = "{{prefix}}/{govkit.GOVKIT_DIR.name}"\nwhy = "the deployer itself"\n\n'
        '[[exempt]]\npath = "{prefix}/policy"\nwhy = "the policy reader update runs"\n',
        encoding="utf-8", newline="\n")
    shutil.copytree(govkit.resolve_kit_dir("policy", "policy.py", govkit.GOVKIT_DIR),
                    g / resolve_kit_path("policy"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.test.sh", "legacy-homes.txt"))
    sm = g / resolve_kit_path("sm")
    sm.mkdir(parents=True)
    shutil.copy2(govkit.GOVKIT_DIR.parent / "settings-merge.py", sm / "settings-merge.py")
    (sm / "kit.toml").write_text(SM_KIT, encoding="utf-8", newline="\n")
    (g / resolve_kit_path(DEMO)).mkdir(parents=True)
    (g / resolve_kit_path(DEMO, "kit.toml")).write_text(KIT, encoding="utf-8", newline="\n")
    write_gov_files(g, FILES)
    write_commit(g, "A")
    return g


def build_retired_target(tmp: pathlib.Path) -> pathlib.Path:
    """The adopter target `tmp/t`, through `fixture_target`'s factory (TOOL-dSafePassage-26 S19)."""
    return build_target(tmp, f'gov_source = "local"\nprefix = "{PFX}"\nkits = ["demo", "settings-merge"]\n', "t")


def run_govkit(g: pathlib.Path, t: pathlib.Path, *args: str, stub: str = "",
               rerender_off: bool = False) -> subprocess.CompletedProcess:
    """The scratch gov's deployer over the target, loaded as a module with `stub` run first."""
    path = (g / resolve_kit_path(govkit.GOVKIT_DIR.name, "govkit.py")).as_posix()
    return subprocess.run([sys.executable, "-c", LOADER, path, stub, args[0], "--target", str(t),
                           *args[1:]], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", stdin=subprocess.DEVNULL,
                          env=read_clean_env({"GOVKIT_RERENDER": "0"} if rerender_off else None))


def read_verdict(out: str, path: str) -> str:
    """The verdict word of `path`'s classification line, `  <verdict> [<role>] <path>`."""
    for ln in out.splitlines():
        if ln.startswith("  ") and "]" in ln and ln.split("]", 1)[1].strip() == path:
            return ln[:ln.index("[")].strip()
    return "(no row)"


def read_role(t: pathlib.Path, path: str) -> str:
    rec = json.loads((t / ".governance" / "install.json").read_text(encoding="utf-8"))
    return next((str(f.get("role")) for f in rec.get("files", []) if f.get("path") == path), "(no row)")


def read_orders(t: pathlib.Path, kind: str, path: str | None = None) -> list[str]:
    box = t / ".governance" / "outbox"
    want = f"update-{kind}-" + (govkit.render_order_slug(path) + ".md" if path else "")
    return sorted(p.name for p in box.glob("*.md") if p.name.startswith(want)) if box.is_dir() else []


def read_bytes(t: pathlib.Path, path: str) -> bytes | None:
    return (t / path).read_bytes() if (t / path).is_file() else None


def read_wired(t: pathlib.Path) -> str:
    s = t / ".claude" / "settings.json"
    return "wired" if s.is_file() and MARKER in s.read_text(encoding="utf-8") else "gone"


def run_update(g, t, *flags, stub="", rerender_off=False) -> str:
    p = run_govkit(g, t, "update", "--write", *flags, stub=stub, rerender_off=rerender_off)
    out = p.stdout + p.stderr
    print(f"retired-edits fixture: update --write {' '.join(flags)} exited {p.returncode}")
    for ln in out.splitlines():
        if ln.startswith("  ") or "hooks:" in ln or "HELD BACK" in ln or "ROLLED BACK" in ln:
            print(f"    | {ln}")
    return out


def run_plant(tmp: pathlib.Path, plant: str, stub: str, write_withdrawals: bool,
              rerender_off: bool) -> list[tuple[str, str, str]]:
    g, t = build_retired_gov(tmp), build_retired_target(tmp)
    p = run_govkit(g, t, "apply")
    if p.returncode != 0:
        raise OSError(f"the scratch install refused (exit {p.returncode}): {(p.stdout + p.stderr)[-900:]}")
    write_commit(t, "the install")
    frag, eng = resolve_kit_path(DEMO, FRAG), resolve_kit_path(DEMO, "eng.txt")
    gone, seed, out_md = resolve_kit_path(DEMO, "gone.txt"), "docs/seed.md", "docs/out.md"
    obs: list[tuple[str, str, str]] = [("the install wired the fragment", read_wired(t), "wired")]
    if plant in ("fragment-withdrawn", "fragment-rollback"):
        rollback = plant == "fragment-rollback"
        write_gov_files(g, {"eng.txt": "red\n"} if rollback else {}, drop=(FRAG,))
        write_commit(g, "B")
        ww = ("--write-withdrawals",) if write_withdrawals else ()
        out = run_update(g, t, *ww, stub=stub, rerender_off=rerender_off)
        obs.append(("verdict " + frag, read_verdict(out, frag), "withdrawn"))
        obs.append(("withdrawn order", str(len(read_orders(t, "withdrawn", frag))), "1"))
        if rollback:
            obs += [("unwired during the run",
                     str(f"hooks: {frag} unwired, gov no longer ships it" in out), "True"),
                    ("the kit rolled back", (read_bytes(t, eng) or b"").decode(), "v1\n"),
                    ("settings entry after the rollback", read_wired(t), "wired")]
        elif rerender_off:
            obs += [("settings entry", read_wired(t), "wired"),
                    ("fragment file", "present" if read_bytes(t, frag) else "gone", "present"),
                    ("the line naming the switch",
                     str(sum(f"hooks: {frag} left WIRED — GOVKIT_RERENDER=0" in ln
                             for ln in out.splitlines())), "1")]
        else:
            obs += [("settings entry", read_wired(t), "gone"),
                    ("fragment file", "present" if read_bytes(t, frag) else "gone",
                     "gone" if write_withdrawals else "present")]
        return obs
    if plant in ("edited-gone", "edited-row", "keep", "edited-reshipped", "edited-rolled-back"):
        edited = b"gov's line\nthe target's edit\n"
        (t / gone).write_bytes(edited)
        write_commit(t, "the target edits a gov file")
        write_gov_files(g, {}, drop=("gone.txt",))
        write_commit(g, "B")
        out = run_update(g, t, "--write-withdrawals", stub=stub if plant == "edited-gone" else "")
        if plant != "edited-gone":
            obs.append(("first run's verdict", read_verdict(out, gone), "retired-edited"))
            write_commit(t, "the first update")
            # The first run's order is cleared, so an order seen after the second is that run's.
            for o in read_orders(t, "retired-edited"):
                (t / ".governance" / "outbox" / o).unlink()
            if plant == "keep":
                (t / ".governance" / "policy.toml").write_text(
                    '[install]\nretired-edits = "keep"\n', encoding="utf-8", newline="\n")
            write_commit(t, "the first order cleared" + (", retired edits kept" if plant == "keep" else ""))
            obs.append(("role before the second run", read_role(t, gone), "retired-edited"))
            if plant in ("edited-reshipped", "edited-rolled-back"):
                if plant == "edited-reshipped":
                    # TOOL-dSafePassage-64: gov ships the file again with the bytes it held at `A`.
                    write_gov_files(g, {"gone.txt": FILES["gone.txt"]})
                    write_commit(g, "C")
                    out = run_update(g, t, stub=stub)
                else:
                    # TOOL-dSafePassage-65: back to `A`, whose descriptor pools the file as `engine`,
                    # with the scratch gov's working tree still at `B`, which pools no such file.
                    a = run_git(g, "rev-parse", "HEAD~1").stdout.strip()
                    out = run_update(g, t, "--rollback", "--to", a, stub=stub)
                return obs + [("verdict " + gone, read_verdict(out, gone), "patched"),
                              ("receipt role", read_role(t, gone), "engine"),
                              ("retired-edited orders", str(len(read_orders(t, "retired-edited"))), "0"),
                              ("the edited bytes", "kept" if read_bytes(t, gone) == edited else "lost",
                               "kept")]
            out = run_update(g, t, stub=stub)
        obs.append(("verdict " + gone, read_verdict(out, gone), "retired-edited"))
        if plant == "keep":
            obs += [("the line naming keep", str(any(
                        gone in ln and "kept, no order (install.retired-edits = keep)" in ln
                        for ln in out.splitlines())), "True"),
                    ("retired-edited orders", str(len(read_orders(t, "retired-edited"))), "0")]
        else:
            obs += [("retired-edited orders", str(len(read_orders(t, "retired-edited", gone))), "1"),
                    ("the order line", str(any(ln.startswith("  ordered ") and gone in ln
                                               for ln in out.splitlines())), "True")]
        obs += [("receipt role", read_role(t, gone), "retired-edited"),
                ("the edited bytes", "kept" if read_bytes(t, gone) == edited else "lost", "kept"),
                ("a forked line", str(any("forked" in ln and gone in ln for ln in out.splitlines())),
                 "False")]
        return obs
    if plant in ("seed-retired-edited", "seed-retired-clean"):
        clean = plant == "seed-retired-clean"
        copy = read_bytes(t, seed) if clean else b"seed\nthe target's own line\n"
        if not clean:
            (t / seed).write_bytes(copy)
            write_commit(t, "the target edits its seeded copy")
        write_gov_files(g, {}, drop=("seed.md",))
        write_commit(g, "B")
        out = run_update(g, t, *(("--write-withdrawals",) if clean else ()), stub=stub)
        obs.append(("verdict " + seed, read_verdict(out, seed), "withdrawn" if clean else "retired-edited"))
        obs.append(("retired-edited orders", str(len(read_orders(t, "retired-edited", seed))),
                    "0" if clean else "1"))
        if clean:
            obs += [("the reported-only line", str(any(ln.startswith("  reported only") and seed in ln
                                                       for ln in out.splitlines())), "True"),
                    ("orders for the seed", str(len([o for o in os.listdir(t / ".governance" / "outbox")
                                                     if govkit.render_order_slug(seed) in o])), "0")]
        else:
            obs.append(("receipt role", read_role(t, seed), "retired-edited"))
        obs.append(("the seeded copy", "kept" if read_bytes(t, seed) == copy else "changed", "kept"))
        return obs
    if plant in ("render-edited-no-oid", "render-eol-no-oid"):
        # TOOL-dSafePassage-63: the render `apply` left, with no update between, so its row carries
        # `output_sha256` and no `oid`; then gov moves the template.
        rec = json.loads((t / ".governance" / "install.json").read_text(encoding="utf-8"))
        obs.append(("the render's recorded oid", "present" if any(
            f.get("path") == out_md and f.get("oid") for f in rec.get("files", [])) else "absent", "absent"))
        eol = plant == "render-eol-no-oid"
        edited = (read_bytes(t, out_md) or b"").replace(b"\n", b"\r\n") if eol else b"tpl v1\nthe target's edit\n"
        (t / out_md).write_bytes(edited)
        write_commit(t, "the target rewrites the render's line endings" if eol else "the target edits the render")
        write_gov_files(g, {"tpl.md": "tpl v2\n"})
        write_commit(g, "B")
        out = run_update(g, t, stub=stub)
        if eol:
            return obs + [("verdict " + out_md, read_verdict(out, out_md), "re-rendered"),
                          ("render-edited orders", str(len(read_orders(t, "render-edited"))), "0")]
        return obs + [("verdict " + out_md, read_verdict(out, out_md), "render-edited"),
                      ("the HELD BACK line", str(f"HELD BACK {DEMO}:" in out), "True"),
                      ("render-edited orders", str(len(read_orders(t, "render-edited", out_md))), "1"),
                      ("the edited bytes", "kept" if read_bytes(t, out_md) == edited else "overwritten",
                       "kept")]
    # render-edited, render-clean: a first update renders and stamps the row's `oid`, then gov moves
    # the template and the engine again over an edited or an untouched render.
    write_gov_files(g, {"tpl.md": "tpl v2\n", "eng.txt": "v2\n"})
    write_commit(g, "B")
    run_update(g, t)
    write_commit(t, "the first update")
    rec = json.loads((t / ".governance" / "install.json").read_text(encoding="utf-8"))
    obs.append(("the render's recorded oid", "present" if any(
        f.get("path") == out_md and f.get("oid") for f in rec.get("files", [])) else "absent", "present"))
    edited = b"tpl v2\nthe target's edit\n"
    if plant in ("render-edited", "render-edited-kill", "render-filter-broken"):
        (t / out_md).write_bytes(edited)
        write_commit(t, "the target edits the render")
    if plant == "render-filter-broken":
        # TOOL-dSafePassage-76 S6: the render mapped to a required clean filter that fails, so git
        # cannot hash it and no clean hash can prove it unedited.
        (t / ".gitattributes").write_text(f"{out_md} filter=broken\n", encoding="utf-8", newline="\n")
        run_git(t, "config", "filter.broken.clean", "false")
        run_git(t, "config", "filter.broken.required", "true")
    write_gov_files(g, {"tpl.md": "tpl v3\n", "eng.txt": "v3\n"})
    us = govkit.upgrade_steps
    if plant == "render-edited-kill":
        # TOOL-dSafePassage-66: C also ships step `fx/s1`, which blocks after its first write; the
        # update is killed there, so only what ran before the walk is on disk.
        gk = g / resolve_kit_path(govkit.GOVKIT_DIR.name)
        (gk / "steps").mkdir(exist_ok=True)
        (gk / "steps" / "fx.py").write_text(us.FIXTURE_WALK_STEP, encoding="utf-8", newline="\n")
        (gk / us.STEPS_FILE).write_text(us.render_fixture_row("s1"), encoding="utf-8", newline="\n")
    write_commit(g, "C")
    if plant == "render-edited-kill":
        reports = t.with_name(t.name + ".fx")
        reports.mkdir()
        (reports / "s1.block-after").touch()
        path = (g / resolve_kit_path(govkit.GOVKIT_DIR.name, "govkit.py")).as_posix()
        why = us.run_killed([sys.executable, "-c", LOADER, path, stub, "update", "--target", str(t),
                             "--write"], reports, "s1", read_clean_env())
        if why:
            raise OSError(f"the kill was not staged: {why}")
        rec = json.loads((t / ".governance" / "install.json").read_text(encoding="utf-8"))
        row = next((f for f in rec.get("files", []) if f.get("path") == eng), {})
        step = next((s for s in rec.get("steps") or [] if s.get("id") == "fx/s1"), {})
        sha_b = run_git(g, "rev-parse", "HEAD~1").stdout.strip()
        return obs + [("the demo kit's eng.txt", (read_bytes(t, eng) or b"").decode(), "v2\n"),
                      ("its receipt row's commit",
                       "B" if row.get("commit") == sha_b else str(row.get("commit")), "B"),
                      ("fx/s1", f"{step.get('state')} · {str(step.get('failure', '')).split(' ', 1)[0]}",
                       "failed · interrupted:")]
    out = run_update(g, t, stub=stub)
    if plant == "render-clean":
        return obs + [("verdict " + out_md, read_verdict(out, out_md), "re-rendered"),
                      ("render-edited orders", str(len(read_orders(t, "render-edited"))), "0"),
                      ("the render", (read_bytes(t, out_md) or b"").decode(), "tpl v3\n")]
    rb = t / ".governance" / "outbox" / f"update-rollback-{DEMO}.md"
    rb_lines = rb.read_text(encoding="utf-8").splitlines() if rb.is_file() else []
    obs += [("verdict " + out_md, read_verdict(out, out_md), "render-edited"),
            ("the HELD BACK line", str(f"HELD BACK {DEMO}:" in out), "True"),
            ("render-edited orders", str(len(read_orders(t, "render-edited", out_md))), "1"),
            ("the edited bytes", "kept" if read_bytes(t, out_md) == edited else "overwritten", "kept")]
    if plant == "render-filter-broken":
        return obs  # TOOL-dSafePassage-76 AC6: the hold, not what its rollback restores
    return obs + [
                  # TOOL-dSafePassage-66 S2: put back before the walk, and still named by the order.
                  ("the demo kit's eng.txt", (read_bytes(t, eng) or b"").decode(), "v2\n"),
                  ("the order's restored line", str(f"restored  {eng}" in rb_lines), "True")]


def run_dispatch_gap() -> list[tuple[str, str, str]]:
    copy = {k: v for k, v in govkit.UPDATE_ROLE.items() if k != "retired-edited"}
    gaps = govkit.derive_dispatch_gaps(copy, govkit.UNLANDED_REASON, govkit.LANDABLE_ROLES,
                                       govkit.VERDICT_GRID)
    own = govkit.derive_dispatch_gaps(govkit.UPDATE_ROLE, govkit.UNLANDED_REASON,
                                      govkit.LANDABLE_ROLES, govkit.VERDICT_GRID)
    for line in gaps + own:
        print(f"    | {line}")
    return [("messages over the copy", str(len(gaps)), "1"),
            ("the message names the role", str(bool(gaps) and "'retired-edited'" in gaps[0]), "True"),
            ("messages over the module's own tables", str(len(own)), "0")]


def run_fixture(plant: str, stub: str | None, write_withdrawals: bool, rerender_off: bool) -> int:
    print(f"retired-edits fixture: plant {plant}" + (f" · stub {stub}" if stub else "")
          + (" · --write-withdrawals" if write_withdrawals else "")
          + (" · --rerender-off" if rerender_off else ""))
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="rte-"))
    try:
        obs = (run_dispatch_gap() if plant == "dispatch-gap" else
               run_plant(tmp, plant, STUBS.get(stub or "", ""), write_withdrawals, rerender_off))
    except (govkit.Refusal, LookupError, OSError, ValueError) as exc:
        print(f"retired-edits fixture: cannot observe: {exc}")
        return 2
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    bad = 0
    for name, seen, want in obs:
        bad += seen != want
        print(f"  {name}: {seen!r} · expects {want!r} · {'ok' if seen == want else 'MISS'}")
    print(f"retired-edits fixture: {len(obs) - bad} of {len(obs)} observation(s) matched")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="retired_edits.py")
    ap.add_argument("--plant", choices=PLANTS, required=True)
    ap.add_argument("--stub", choices=sorted(STUBS))
    ap.add_argument("--write-withdrawals", action="store_true")
    ap.add_argument("--rerender-off", action="store_true")
    args = ap.parse_args(argv)
    return run_fixture(args.plant, args.stub, args.write_withdrawals, args.rerender_off)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    raise SystemExit(main(sys.argv[1:]))
