#!/usr/bin/env python3
"""upgrade_walk.py — the `upgrade-walk` leg: every declared upgrade step walked over release-0 (TOOL-dSafePassage-5).

    python <prefix>/govkit/upgrade_walk.py                     # the leg: every case, then every arm
    python <prefix>/govkit/upgrade_walk.py --list              # the pin, the landed ref, the rows
    python <prefix>/govkit/upgrade_walk.py --case <case> [--step <id>] [--inject <name> ...] [--pin <rev>]

RELEASE-0 is an adopter tree of the pinned vintage, generated, never copied: a `--no-tags` scratch
clone of gov checked out at the pin (`fixtures/release-0/pin.txt`) runs its OWN `govkit.py apply`
into a target `fixture_target.build_target` makes from `fixtures/release-0/deploy.toml` and the
`seed/` project layer. The plants of `plants.toml` are committed onto it, the target's own policy
adopter is re-run as its install-day remedy asks, and the clone then walks to its tip, HEAD's
commit plus the `[[gov_plant]]` commits, as an adopter's `update` does.

THE CASES, each over a fresh copy of the planted release-0: `up`, `down`, `reup`, `plants`, `skip`,
`kill`, `fail`, `shims` and `isolation` (help/upgrade-steps.md, "How gov proves a step before you
meet it"). A walk runs in a child process that rebinds `run_step_isolated` and `read_steps` in the
clone's `upgrade_steps` module, so no shipped code carries a test switch. Every compare reads the
tree as `derive_tree_digest` states. The arms of `arms.toml` join only under `--inject`, and the
leg runs each after its real cases: an arm whose case stays green, or goes red naming no `needle`
of its row, is a red. Every invocation first runs `check_graders` (TOOL-dSafePassage-77 S7).

    Exit 0 green · 1 a red · 2 nothing measured: the pin fails, release-0 does not apply clean, a
    plant's path is absent at release-0, no step is declared, or an engine file under this
    directory or its sibling `lib` differs from HEAD outside the leg's own files.
"""
from __future__ import annotations

import ast
import hashlib
import inspect
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
import tomllib

HERE = pathlib.Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "release-0"
CASES = ("up", "down", "reup", "plants", "skip", "kill", "fail", "shims", "isolation")
PER_STEP = ("skip", "kill", "fail", "isolation")
SCHEMA_STEP = "govkit/receipt-schema-4"
RECEIPT, SUMS, OUTBOX = ".governance/install.json", ".governance/install.sums", ".governance/outbox"
# S4: the keys a record re-derives on every run, so a compare reads them as their owners declare.
CARRY_KEY = "carry"  # DEPL-dCarriedReceipt-9 S2
RENDERED_KEYS = ("sha256", "oid", "gov_oid", "commit", "version")  # DEPL-dRemeasuredRender-1 S1
CHILD_TIMEOUT_S = 1800
# The pinned clone's remote, named here and removed once the landed ref is fetched.
CLONE_REMOTE = "gk-walk-source"
OK = {"verdict": "ok", "rc": 0, "tail": ""}
# TOOL-dSafePassage-77 S3: the files the leg reads from the working tree, relative to HERE
LEG_OWN = (pathlib.Path(__file__).name, "fixture_target.py", "fixtures/release-0")


class Stop(Exception):
    """Nothing measured: exit 2 with the reason."""


def print_line(line: str) -> None:
    print(f"upgrade-walk: {line}", flush=True)


def run_git(cwd, *args: str, check: bool = True) -> str:
    """`git -C <cwd> <args>`'s stdout, with no `GIT_*` name a calling hook exported."""
    env = {k: v for k, v in os.environ.items() if not k.upper().startswith("GIT_")}
    p = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env, stdin=subprocess.DEVNULL)
    if check and p.returncode:
        raise Stop(f"git {' '.join(args)} in {pathlib.Path(cwd).as_posix()}: {p.stderr.strip()}")
    return p.stdout.strip()


def write_commit(tree, msg: str) -> None:
    """Stage everything and commit it, as an adopter commits a run; an empty run commits empty."""
    run_git(tree, "add", "-A")
    run_git(tree, "-c", "user.email=t@e", "-c", "user.name=t", "commit", "-q", "--allow-empty", "-m", msg)


def remove_tree(path) -> None:
    shutil.rmtree(path, onexc=lambda f, q, _e: (os.chmod(q, 0o700), f(q)))


def load_engine():
    """gov's own `upgrade_steps` and `shims`, by path, so `govkit` binds the one `Refusal`."""
    sys.path.insert(0, str(HERE))
    import govkit  # noqa: E402
    import shims  # noqa: E402
    return govkit.upgrade_steps, shims, govkit


# ------------------------------------------------------------------------------------------ the pin
def read_release_pin(fixture=FIXTURE) -> str:
    return (pathlib.Path(fixture) / "pin.txt").read_text(encoding="utf-8").strip()


def check_release_pin(gov_root, pin: str) -> list[str]:
    """S1: one problem per way `pin` is not release-0's commit: not 40 hex, no commit, not on HEAD's
    first-parent line, or a tree carrying an `[[upgrade]]` row, each row named."""
    if len(pin) != 40 or any(c not in "0123456789abcdef" for c in pin):
        return [f"the pin {pin!r} is not one full sha"]
    if run_git(gov_root, "cat-file", "-t", pin, check=False) != "commit":
        return [f"the pin {pin} names no commit in gov"]
    out = []
    if pin not in run_git(gov_root, "rev-list", "--first-parent", "HEAD").split():
        out.append(f"the pin {pin[:8]} is not a first-parent ancestor of HEAD")
    hits = run_git(gov_root, "grep", "-n", "-E", r"^\[\[upgrade\]\]", pin, "--", ":(glob)**/*.toml", check=False)
    out += [f"the pin {pin[:8]} carries an [[upgrade]] row at {h.split(':', 1)[1].rsplit(':', 1)[0]}"
            for h in hits.splitlines() if h]
    return out


# ----------------------------------------------------------------------------------------- the rows
def read_fixture_rows(kind: str, fixture=FIXTURE) -> list[dict]:
    """The `kind` rows, each `path`, and a nested plant's `path` and shim's `from` and `to`, spelled
    `{prefix}/…` and resolved here against the tool root, the pinned clone's as gov's own: the walk
    runs the clone's engine at HERE's own relative path (TOOL-dSafePassage-82 S3)."""
    name = {"plant": "plants.toml", "gov_plant": "plants.toml", "condition": "plants.toml", "arm": "arms.toml"}[kind]
    gk = load_engine()[2]
    troot = gk.derive_tool_root(gk.repo_root())
    fix = lambda r: {k: gk.resolve_prefix_token(v, troot) if k in ("path", "from", "to") and isinstance(v, str)
                     else fix(v) if isinstance(v, dict) else v for k, v in r.items()}
    rows = tomllib.loads((pathlib.Path(fixture) / name).read_text(encoding="utf-8")).get(kind) or []
    return [fix(r) if isinstance(r, dict) else r for r in rows]


def read_plant_rows(fixture=FIXTURE) -> list[dict]:
    """TOOL-dSafePassage-77 S1: an `ordered` plant with no `order` kind is a Stop naming it."""
    rows = read_fixture_rows("plant", fixture)
    for r in rows:
        if r.get("expect") == "ordered" and not r.get("order"):
            raise Stop(f"plant {r.get('id')}: expects ordered and names no `order` kind")
    return rows


def read_condition_rows(fixture=FIXTURE) -> list[dict]:
    return read_fixture_rows("condition", fixture)


def read_arm_rows(fixture=FIXTURE) -> list[dict]:
    """TOOL-dSafePassage-77 S2: an arm with no `needle` is a Stop naming it."""
    rows = read_fixture_rows("arm", fixture)
    for r in rows:
        if not r.get("needle"):
            raise Stop(f"arm {r.get('name')}: names no `needle`, the text its case's red must hold")
    return rows


def write_plant_edits(tree, rows: list[dict]) -> None:
    """Apply each plant-shaped row's edit to `tree`: `append` its `text`, `replace` `old` by `new`
    once, `create` the file holding `text`. An `append` or `replace` path the tree lacks is a Stop."""
    tree = pathlib.Path(tree)
    for r in rows:
        f = tree / r["path"]
        if r["edit"] == "remove":  # a [[gov_plant]]'s: gov stops shipping a file
            if not f.is_file():
                raise Stop(f"plant {r['id']}: {r['path']} is absent")
            f.unlink()
            continue
        if r["edit"] == "create":
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(r["text"], encoding="utf-8", newline="\n")
            continue
        if not f.is_file():
            raise Stop(f"plant {r['id']}: {r['path']} is absent at release-0")
        text = f.read_text(encoding="utf-8", newline="")
        if r["edit"] == "append":
            text += r["text"]
        elif r["edit"] == "replace":
            if r["old"] not in text:
                raise Stop(f"plant {r['id']}: {r['path']} holds no {r['old']!r} to replace")
            text = text.replace(r["old"], r["new"], 1)
        else:
            raise Stop(f"plant {r['id']}: edit {r['edit']!r} is none of append, replace, create")
        f.write_text(text, encoding="utf-8", newline="")


# ------------------------------------------------------------------------------------ release-0
def build_release_tree(gov_root, root, pin: str, plants: list[dict], gov_plants: list[dict],
                       with_target: bool = True) -> dict:
    """S2: the scratch clone at the pin, its landed ref gov's own, release-0 applied by its own
    `apply`, planted and committed, the policy adopter re-run and committed, and the clone moved to
    its tip. Returns the run's context; a release-0 that does not apply clean is a Stop."""
    us, _shims, gk = load_engine()
    gov_root, root = pathlib.Path(gov_root), pathlib.Path(root)
    head = run_git(gov_root, "rev-parse", "HEAD")
    landed = us.resolve_landed_ref(gov_root)
    if not landed:
        raise Stop("gov names no landed ref, so no step's introducing commit can be derived")
    clone = root / "gov"
    # PINNED, not inherited: a Windows git install sets core.autocrlf=true system-wide, and the clone
    # would check out its engine bytes by the machine running the leg (fixture-inherits-ambient-machine-state)
    run_git(root, "clone", "-q", "--no-tags", "--origin", CLONE_REMOTE, "-c", "core.autocrlf=false", gov_root.as_posix(), clone.as_posix())
    run_git(clone, "-c", "advice.detachedHead=false", "checkout", "-q", "--detach", pin)
    full = run_git(gov_root, "rev-parse", "--symbolic-full-name", landed) or landed
    run_git(clone, "fetch", "-q", "--no-tags", gov_root.as_posix(), f"+{full}:refs/heads/main")
    run_git(clone, "remote", "remove", CLONE_REMOTE)
    rel = HERE.relative_to(gov_root.resolve()).as_posix()
    ctx = {"root": root, "gov_root": gov_root, "clone": clone, "pin": pin, "head": head,
           "landed": run_git(gov_root, "rev-parse", landed), "govkit": f"{rel}/govkit.py", "tip": head}
    if with_target:
        deploy = gk.resolve_prefix_token((FIXTURE / "deploy.toml").read_text(encoding="utf-8"),
                                         gk.derive_tool_root(clone)).replace("{scratch}", root.as_posix())
        sys.path.insert(0, str(HERE))
        from fixture_target import build_target  # noqa: E402 — S12, the one factory
        t = build_target(root / "r0", deploy)
        shutil.copytree(FIXTURE / "seed", t, dirs_exist_ok=True)
        p = subprocess.run([sys.executable, str(clone / ctx["govkit"]), "apply", "--target", str(t)],
                           cwd=str(clone), capture_output=True, text=True, encoding="utf-8", errors="replace",
                           stdin=subprocess.DEVNULL)
        if p.returncode:
            bad = [ln for ln in (p.stdout + p.stderr).splitlines() if "FAIL" in ln or "refus" in ln or "error" in ln.lower()]
            raise Stop(f"release-0's apply exited {p.returncode}: " + (" | ".join(bad[:40]) or p.stderr[-2000:]))
        write_commit(t, "release-0")
        schema = json.loads((t / RECEIPT).read_text(encoding="utf-8")).get("schema")
        print_line(f"release-0 applied by the pinned clone's own apply over the fixture's kits line · exit 0 · "
            f"receipt schema {schema}")
        write_plant_edits(t, plants)
        write_commit(t, "plants")
        adopter = "adopt-policy.sh"
        p = subprocess.run([gk.resolve_bash(), (gk.resolve_kit_dir("policy", adopter, t / gk.derive_tool_root(clone)) / adopter).as_posix(), "--scaffold", "--target", t.as_posix()],
                           cwd=str(t), capture_output=True, text=True, encoding="utf-8", errors="replace",
                           stdin=subprocess.DEVNULL)
        if p.returncode:
            raise Stop(f"release-0's policy adopter re-run exited {p.returncode}: {(p.stdout + p.stderr)[-1000:]}")
        write_commit(t, "policy adopter re-run")
        print_line("release-0 · the policy adopter's re-run committed "
            + (".governance/policy.json" if (t / ".governance/policy.json").is_file() else "no policy mirror"))
        ctx["r0"] = t
    run_git(clone, "-c", "advice.detachedHead=false", "checkout", "-q", "--detach", head)
    if gov_plants:
        # `update --to` refuses a commit no ref names, as it would an adopter's, so the tip is a branch
        run_git(clone, "checkout", "-q", "-b", "upgrade-walk-tip")
        write_plant_edits(clone, gov_plants)
        run_git(clone, "add", "-A")
        run_git(clone, "-c", "user.email=uw@e", "-c", "user.name=uw", "commit", "-qm", "upgrade-walk: gov plants")
        ctx["tip"] = run_git(clone, "rev-parse", "HEAD")
    return ctx


# ---------------------------------------------------------------------------------------- the digest
def derive_tree_digest(tree, pin_modes: dict[str, str], unvia: str | None = None) -> dict[str, str]:
    """S4: `{path: sha256}` over every file outside `.git/` and the outbox, and `{":index " + path:
    "mode oid stage"}` over the index there. The receipt is read without `carry` in its `files` rows
    and without RENDERED_KEYS in its `rendered` rows, the sidecar without the lines naming a
    rendered row, and an `engine` row's index mode through `resolve_landed_mode` against gov's mode
    at the pin (`pin_modes`, source path to mode), as the records owning each declare them. The
    receipt's and sidecar's own index entries are read by mode and stage: their blob ids hash the
    contents compared above, so a blob compare would read those records' fields raw. `unvia`, a
    step id, reads that step's `steps` row without `via` (AC7: the killed step's mark)."""
    _us, _shims, gk = load_engine()
    tree = pathlib.Path(tree)
    out: dict[str, str] = {}
    receipt, rendered_paths, engine_src = None, set(), {}
    try:
        receipt = json.loads((tree / RECEIPT).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        pass
    if isinstance(receipt, dict):
        for row in receipt.get("files") or []:
            if not isinstance(row, dict):
                continue
            row.pop(CARRY_KEY, None)
            if row.get("role") == "engine":
                engine_src[row.get("path")] = row.get("source")
            elif row.get("role") == "rendered":
                rendered_paths.add(row.get("path"))
                for k in RENDERED_KEYS:
                    row.pop(k, None)
        for row in receipt.get("steps") or []:
            if unvia and isinstance(row, dict) and row.get("id") == unvia:
                row.pop("via", None)
    for dp, dn, fn in os.walk(tree):
        rel = pathlib.Path(dp).relative_to(tree).as_posix()
        if rel == ".git" or rel.startswith(".git/") or rel == OUTBOX or rel.startswith(OUTBOX + "/"):
            dn[:] = []
            continue
        for f in fn:
            path = f if rel == "." else f"{rel}/{f}"
            data = (tree / path).read_bytes()
            if path == RECEIPT and isinstance(receipt, dict):
                data = json.dumps(receipt, sort_keys=True).encode("utf-8")
            elif path == SUMS:
                data = b"\n".join(ln for ln in data.splitlines()
                                  if not any(p and ln.endswith((" " + p).encode("utf-8")) for p in rendered_paths))
            out[path] = hashlib.sha256(data).hexdigest()
    for ln in run_git(tree, "ls-files", "--stage", "-z").split("\0"):
        if not ln:
            continue
        meta, path = ln.split("\t", 1)
        if path == OUTBOX or path.startswith(OUTBOX + "/"):
            continue
        mode, oid, stage = meta.split()
        if path in engine_src:
            mode = gk.resolve_landed_mode(mode, pin_modes.get(engine_src[path]))
        # the receipt's and sidecar's blobs hash the very contents read above, so by mode and stage
        out[f":index {path}"] = f"{mode} {stage}" if path in (RECEIPT, SUMS) else f"{mode} {oid} {stage}"
    return out


def check_walk_exit(rc: int, out: str, ordered: set, stops: int = 0) -> list[str]:
    """§4 "The walk's exit": [] when the run returned, else its problems. Returned is exit 0 with no
    stop expected, or exit 1 whose count line `govkit: <n> problem(s)` counts exactly its `kit '<eid>'
    was HELD BACK: this run refused <paths> of it` lines, every path of each (split on `, `) an
    `ordered` plant's, plus the `stops` problems a case expecting its walk to stop adds."""
    if rc == 0 and not stops:
        return []
    lines = out.splitlines()
    at = next((i for i in range(len(lines) - 1, -1, -1) if re.fullmatch(r"govkit: \d+ problem\(s\)", lines[i])), None)
    n = int(lines[at].split()[1]) if at is not None else 0
    # Report.emit prints the problems straight above the count line, notes above them
    problems = [ln[len("govkit: "):] for ln in lines[max(0, at - n):at]] if at is not None else []
    held = [m.group(1) for p in problems
            if (m := re.match(r"kit '[^']+' was HELD BACK: this run refused (.+?) of it, so", p))]
    stray = sorted({p for paths in held for p in paths.split(", ") if p not in ordered})
    if rc == 1 and at is not None and n == len(held) + stops and not stray:
        return []
    return [f"exit {rc}"] + [f"a held path no ordered plant names: {', '.join(stray)}"] * bool(stray) + [
        p[:300] for p in problems if " was HELD BACK: " not in p or stray]


def derive_digest_diff(a: dict, b: dict) -> list[str]:
    return sorted(k for k in a.keys() | b.keys() if a.get(k) != b.get(k))


# ----------------------------------------------------------------------------------- the first write
def derive_first_write(before: dict[str, bytes], shadow, image: str) -> list[str]:
    """The paths a shadow run changed against `before` (path to bytes), the first write first:
    `image`, the step's before-image path, where it is among them, since the step contract writes it
    first; else the one changed path; else by modification time. A tie between the two earliest, or
    a removed path among several (it has no time of its own), is a Stop naming them, `first write
    undetermined`. A write inside one file is not split."""
    shadow = pathlib.Path(shadow)
    after = read_tree_bytes(shadow)
    changed = sorted(p for p in before.keys() | after.keys() if before.get(p) != after.get(p))
    if image in changed:
        return [image] + [p for p in changed if p != image]
    if len(changed) < 2:
        return changed
    gone = [p for p in changed if p not in after]
    if gone:
        raise Stop(f"first write undetermined: {', '.join(gone)} removed among {len(changed)} changed paths")
    timed = sorted(changed, key=lambda p: ((shadow / p).stat().st_mtime_ns, p))
    if (shadow / timed[0]).stat().st_mtime_ns == (shadow / timed[1]).stat().st_mtime_ns:
        raise Stop(f"first write undetermined: {timed[0]} and {timed[1]} share one modification time")
    return timed


def read_tree_bytes(tree) -> dict[str, bytes]:
    tree, out = pathlib.Path(tree), {}
    for dp, dn, fn in os.walk(tree):
        if pathlib.Path(dp) == tree and ".git" in dn:
            dn.remove(".git")
        for f in fn:
            p = pathlib.Path(dp) / f
            out[p.relative_to(tree).as_posix()] = p.read_bytes()
    return out


# ------------------------------------------------------------------------------------------ the child
CHILD = r'''
import importlib.util, json, os, pathlib, runpy, shutil, sys
cfg = json.loads(sys.argv[1])
gk_path = pathlib.Path(cfg["govkit"])
spec = importlib.util.spec_from_file_location("upgrade_steps", gk_path.parent / "upgrade_steps.py")
us = importlib.util.module_from_spec(spec)
sys.modules["upgrade_steps"] = us
spec.loader.exec_module(us)
spec = importlib.util.spec_from_file_location("upgrade_walk_leg", cfg["leg"])
uw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(uw)
real_run, real_read = us.run_step_isolated, us.read_steps
step, mode, first = cfg.get("step"), cfg.get("mode"), [True]
extra = [us.StepRow(**r) for r in cfg.get("inject", [])]


def run(row, phase, target, gov_root, *args, **kwargs):
    if row.id == step:
        if phase == "witness" and first[0]:
            first[0] = False
            if mode == "skip":
                return dict(uw.OK)
            got = real_run(row, phase, target, gov_root, *args, **kwargs)
            if got["verdict"] != "ok":
                return got
            print(f"upgrade-walk: forced {row.id}", flush=True)
            return {"verdict": "failed", "rc": 1, "tail": "upgrade-walk: forced"}
        if phase in ("up", "resume") and mode == "fail":
            return {"verdict": "failed", "rc": 1, "tail": "upgrade-walk: planted exit 1"}
        if phase in ("up", "resume") and mode == "kill":
            target, shadow = pathlib.Path(target), pathlib.Path(cfg["shadow"])
            before = uw.read_tree_bytes(target)
            shutil.copytree(target, shadow, symlinks=True)
            real_run(row, phase, shadow, gov_root, *args, **kwargs)
            image = us.derive_image_path(shadow, row.id).relative_to(shadow).as_posix()
            try:
                changed = uw.derive_first_write(before, shadow, image)
            except uw.Stop as e:
                print(f"upgrade-walk: {row.id} · {e}", flush=True)
                os._exit(3)
            if changed:
                src, dst = shadow / changed[0], target / changed[0]
                if src.is_file():
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    dst.write_bytes(src.read_bytes())
                else:
                    dst.unlink()
            print(f"upgrade-walk: killed {row.id} after " + (changed[0] if changed else "its end, no write"), flush=True)
            os._exit(137)
    return real_run(row, phase, target, gov_root, *args, **kwargs)


def read(root, rev, landed_ref, *args, **kwargs):
    rows = real_read(root, rev, landed_ref, *args, **kwargs)
    if extra and us.resolve_rev(root, rev or "HEAD") == cfg["tip"]:
        rows = rows + [r._replace(introduced=cfg["tip"] if landed_ref is not None else None) for r in extra]
    return rows


us.run_step_isolated, us.read_steps = run, read
sys.argv = [str(gk_path), *cfg["argv"]]
runpy.run_path(str(gk_path), run_name="__main__")
'''


def check_child_forwarding(us, child: str = CHILD) -> list[str]:
    """TOOL-dSafePassage-68 S2: one problem per way a stand-in `child` rebinds on `us` fails to take
    and pass on every parameter of the real function it replaces, read live by `inspect.signature`.
    It reads the shape of the forwarding, never what a stand-in's branches do with the values."""
    tree = ast.parse(child)
    stand, real = {}, {}
    for node in tree.body:
        if not (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Tuple) and isinstance(node.value, ast.Tuple)):
            continue
        for t, v in zip(node.targets[0].elts, node.value.elts):
            if isinstance(t, ast.Attribute) and isinstance(t.value, ast.Name) and t.value.id == "us" \
                    and isinstance(v, ast.Name):
                stand[t.attr] = v.id
            elif isinstance(t, ast.Name) and isinstance(v, ast.Attribute) and isinstance(v.value, ast.Name) \
                    and v.value.id == "us":
                real[v.attr] = t.id
    if not stand:
        return ["the child rebinds nothing on `us`"]
    defs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    out = []
    for attr in sorted(stand):
        name, rname = stand[attr], real.get(attr)
        fn = defs.get(name)
        if fn is None or rname is None or not hasattr(us, attr):
            out.append(f"{attr}: no stand-in def or real binding found")
            continue
        names = list(inspect.signature(getattr(us, attr)).parameters)
        own = [a.arg for a in fn.args.posonlyargs + fn.args.args]
        va, kw = fn.args.vararg and fn.args.vararg.arg, fn.args.kwarg and fn.args.kwarg.arg
        if own != names[:len(own)] or not va or not kw:
            out.append(f"{attr}: stand-in {name}({', '.join(own)}) does not take and pass on ({', '.join(names)})")
        calls = sorted((c for c in ast.walk(fn) if isinstance(c, ast.Call)
                        and isinstance(c.func, ast.Name) and c.func.id == rname), key=lambda c: c.lineno)
        if not calls:
            out.append(f"{attr}: {name} never calls {rname}")
        for c in calls:
            pos, last = c.args[:-1], c.args[-1:]
            if not (len(pos) == len(own) and not any(isinstance(a, ast.Starred) for a in pos)
                    and last and isinstance(last[0], ast.Starred) and isinstance(last[0].value, ast.Name)
                    and last[0].value.id == va
                    and any(k.arg is None and isinstance(k.value, ast.Name) and k.value.id == kw
                            for k in c.keywords)):
                out.append(f"{attr}: CHILD line {c.lineno} calls {rname} without passing on "
                           f"*{va or 'args'}, **{kw or 'kwargs'}")
    return out


def run_child_walk(ctx: dict, target, argv: list[str], mode: str | None = None, step: str | None = None,
                   inject: list | None = None, path_first: str | None = None) -> tuple[int, str]:
    """S5: the clone's `govkit.py` run as `main` in a fresh Python process that first imports the
    clone's `upgrade_steps` and rebinds `run_step_isolated` (`mode` `skip`, `kill` or `fail` at
    `step`) and `read_steps` (the `inject` rows, introduced at the tip). Returns (exit, output)."""
    cfg = {"govkit": str(ctx["clone"] / ctx["govkit"]), "leg": str(pathlib.Path(__file__).resolve()),
           "argv": [a if a != "{target}" else str(target) for a in argv], "mode": mode, "step": step,
           "tip": ctx["tip"], "shadow": str(ctx["root"] / "shadow"),
           "inject": [r._asdict() for r in (inject or [])]}
    if (ctx["root"] / "shadow").exists():
        remove_tree(ctx["root"] / "shadow")
    env = dict(os.environ)
    if path_first:
        env["PATH"] = path_first + os.pathsep + env.get("PATH", "")
    p = subprocess.run([sys.executable, "-I", "-c", CHILD, json.dumps(cfg)], cwd=str(ctx["clone"]),
                       capture_output=True, text=True, encoding="utf-8", errors="replace", env=env,
                       stdin=subprocess.DEVNULL, timeout=CHILD_TIMEOUT_S)
    return p.returncode, p.stdout + p.stderr


# ------------------------------------------------------------------------------------------ the cases
def check_plant_rows(ctx: dict, tree, rows: list[dict]) -> list[str]:
    """S3 over a walked, committed tree: one red per `[[plant]]` neither carried by its observation
    nor, expecting `ordered`, named by an order of its `order` kind under the outbox: the file
    gov's one order writer names by `render_row_order_key` (TOOL-dSafePassage-77 S1). Prints one
    line per plant."""
    _us, _shims, gk = load_engine()
    tree, reds = pathlib.Path(tree), []
    sha = run_git(tree, "rev-parse", "HEAD")
    for r in rows:
        f, got, why = tree / r["path"], None, ""
        if r["expect"] == "ordered":
            name = gk.render_row_order_key(r["order"], r["path"]) + ".md"
            got = "ordered" if (tree / OUTBOX / name).is_file() else None
            why = f"no {r['order']} order {name} is under the outbox"
        elif "contains" in r:
            got = "carried" if f.is_file() and r["contains"] in f.read_text(encoding="utf-8", errors="replace") else None
            why = f"the walked file does not hold {r['contains']!r}"
        elif r.get("unchanged"):
            planted = (ctx["r0"] / r["path"]).read_bytes()
            got = "carried" if f.is_file() and f.read_bytes() == planted else None
            why = "the walked bytes differ from the bytes as planted"
        elif "policy" in r:
            pol = r["policy"]
            reader = "policy.py"
            kit = gk.resolve_kit_dir("policy", reader, ctx["clone"] / pathlib.Path(ctx["govkit"]).parent)
            p = subprocess.run([sys.executable, str(kit / reader), "get", pol["key"], "--rev", sha],
                               cwd=str(tree), capture_output=True, text=True, encoding="utf-8", errors="replace",
                               stdin=subprocess.DEVNULL)
            value = p.stdout.strip()
            held = [a for a in pol.get("absent", []) if subprocess.run(
                ["git", "-C", str(tree), "cat-file", "-e", f"{sha}:{a}"], capture_output=True).returncode == 0]
            if p.returncode == 2:
                why = "policy.py get exited 2: " + next((ln for ln in (p.stdout + p.stderr).splitlines()
                                                         if "policy: refused" in ln), p.stderr.strip()[-300:])
            elif value != pol["value"] or held:
                why = f"{pol['key']} reads {value!r}, expected {pol['value']!r}" + (
                    f", and the walked commit still holds {', '.join(held)}" if held else "")
            else:
                got = f"carried · {pol['key']} reads {value}"
        if got:
            print_line(f"plants · {r['id']} · {got}")
        else:
            reds.append(f"plants · {r['id']} · {r['path']}: expected {r['expect']}, {why}")
            print_line(reds[-1] + " · RED")
    return reds


def check_shim_paths(ctx: dict, tree, extra_rows: list[dict]) -> tuple[list[str], int]:
    """S11 over the walked tree: the clone holds no tag, `read_releases` returns none, every shim row
    `read_shim_rows` reads is held by `check_shim_windows`, and each row whose `from` the receipt
    installs has its forwarder in the tree. Returns (reds, rows counted)."""
    _us, shims, _gk = load_engine()
    reds, tree = [], pathlib.Path(tree)
    tags = run_git(ctx["clone"], "tag")
    print_line("shims · the clone holds " + ("no tag" if not tags else f"tags {tags.split()}"))
    if tags:
        reds.append("shims · the --no-tags clone holds a tag")
    releases = shims.read_releases(ctx["clone"])
    print_line(f"shims · read_releases returned {'none' if not releases else len(releases)}")
    rows = shims.read_shim_rows(ctx["clone"])
    held = {ln.split()[1] for ln in shims.check_shim_windows(ctx["clone"], releases)}
    for r in rows:
        if r["closed"] and r["id"] not in held:
            reds.append(f"shims · {r['id']} reads closable with {len(releases)} release(s) cut")
    installed = {row.get("path") for row in json.loads((tree / RECEIPT).read_text(encoding="utf-8")).get("files") or []
                 if isinstance(row, dict)}
    for r in rows + extra_rows:
        if r["from"] in installed and not (tree / r["from"]).is_file():
            reds.append(f"shims · {r['id']} · its forwarder {r['from']} is gone from the walked target")
    for x in reds:
        print_line(x + " · RED")
    if not rows + extra_rows:
        print_line("shims: 0 declared")
    return reds, len(rows + extra_rows)


def check_step_isolation(ctx: dict, row) -> tuple[str, str]:
    """S10: `check_needs_target` for `row` over a scratch copy of release-0, its verdict and line."""
    import contextlib
    import io
    us, _shims, _gk = load_engine()
    scratch = ctx["root"] / "iso"
    if scratch.exists():
        remove_tree(scratch)
    shutil.copytree(ctx["r0"], scratch, symlinks=True)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        verdict = us.check_needs_target(row, scratch, ctx["clone"])
    remove_tree(scratch)
    return verdict, buf.getvalue().strip()


def run_walk_case(ctx: dict, case: str, steps: list | None = None, inject: tuple = ()) -> list[str]:
    """One case over fresh copies of the planted release-0; its lines printed, its reds returned.
    `steps` limits a per-step case; `inject` names the arms joining the walk."""
    us, _shims, _gk = load_engine()
    arms = {a["name"]: a for a in ctx["arms"]}
    inj_rows = [ctx["arm_rows"][n] for n in inject if n in ctx["arm_rows"]]
    rows = ctx["rows"] + inj_rows
    reds: list[str] = []
    walk = ["update", "--target", "{target}", "--to", ctx["tip"], "--write"]
    back = ["update", "--target", "{target}", "--rollback", "--to", ctx["pin"], "--write"]
    arm_plants = [arms[n]["plant"] for n in inject if "plant" in arms.get(n, {})]

    def build_case_tree(name: str, src=None) -> pathlib.Path:
        dst = ctx["root"] / "cases" / name
        if dst.exists():
            remove_tree(dst)
        shutil.copytree(src or ctx["r0"], dst, symlinks=True)
        if src is None and arm_plants:
            # TOOL-dSafePassage-77 S6: an injected plant arm joins release-0's plants by their writer
            write_plant_edits(dst, arm_plants)
            write_commit(dst, "arm plants")
        return dst

    def derive_digest(t):
        return derive_tree_digest(t, ctx["pin_modes"])

    def add_red(line):
        reds.append(f"{case} · {line}")
        print_line(f"{case} · {line} · RED")

    def read_states(t):
        return {r["id"]: r for r in us.read_step_states(json.loads((t / RECEIPT).read_text(encoding="utf-8")))}

    def run_up_walk() -> tuple[pathlib.Path, dict]:
        key = ("up", inject)
        if key not in ctx["cache"]:
            t = build_case_tree("up-" + "-".join(inject))
            rc, out = run_child_walk(ctx, t, walk, inject=inj_rows)
            bad = check_walk_exit(rc, out, ctx["ordered"])
            if bad:
                raise Stop("up · the walk to the tip did not return: " + " | ".join(bad))
            gc = json.loads((t / RECEIPT).read_text(encoding="utf-8")).get("gov_commit")
            if rc and gc != ctx["pin"]:
                raise Stop(f"up · the walk held a kit and gov_commit reads {gc}, not the pin")
            write_commit(t, "up")
            ctx["cache"][key] = (t, derive_digest(t))
        return ctx["cache"][key]

    def check_digest(label, t, want):
        diff = derive_digest_diff(derive_digest(t), want)
        if diff:
            add_red(f"{label}: the digest differs at {', '.join(diff[:20])}" + (f" and {len(diff) - 20} more" if len(diff) > 20 else ""))
        return not diff

    if case == "up":
        t, _d = run_up_walk()
        st = read_states(t)
        for r in rows:
            s = st.get(r.id, {}).get("state")
            w = us.run_step_isolated(r, "witness", t, ctx["clone"])["verdict"]
            line = f"up · {r.id} · {s or 'not recorded'} · witness {w}"
            if s != "applied" or w != "ok":
                add_red(line.split("up · ", 1)[1])
            else:
                print_line(line)
    elif case == "down":
        up_t, _d = run_up_walk()
        t = build_case_tree("down", up_t)
        rc, out = run_child_walk(ctx, t, back, inject=inj_rows)
        bad = check_walk_exit(rc, out, ctx["ordered"])
        if bad:
            add_red("the rollback to the pin did not return: " + " | ".join(bad))
        write_commit(t, "down")
        if check_digest("rollback to the pin", t, ctx["d_r0"]):
            print_line("down · the rollback's digest equals release-0's")
        ctx["cache"][("down", inject)] = t
    elif case == "reup":
        t0 = ctx["cache"].get(("down", inject))
        if t0 is None:
            reds += run_walk_case(ctx, "down", None, inject)
            t0 = ctx["cache"][("down", inject)]
        _u, d_up = run_up_walk()
        t = build_case_tree("reup", t0)
        rc, out = run_child_walk(ctx, t, walk, inject=inj_rows)
        bad = check_walk_exit(rc, out, ctx["ordered"])
        if bad:
            add_red("the second walk did not return: " + " | ".join(bad))
        write_commit(t, "reup")
        if check_digest("second walk", t, d_up):
            print_line("reup · the second walk's digest equals the first's")
    elif case == "plants":
        t, _d = run_up_walk()
        for x in check_plant_rows(ctx, t, ctx["plants"]):
            reds.append(f"plants · {x.split(' · ', 1)[1]}")
    elif case == "shims":
        t, _d = run_up_walk()
        extra = [arms[n]["shim"] for n in inject if "shim" in arms.get(n, {})]
        got, n = check_shim_paths(ctx, t, extra)
        reds += got
        ctx["shims"] = n
    elif case == "isolation":
        for r in steps or rows:
            verdict, line = check_step_isolation(ctx, r)
            if verdict in ("isolated", "attended"):
                print_line(line)
                ctx["attended"] += verdict == "attended"
            else:
                add_red(f"{r.id} · {verdict} · {line}")
    else:
        up_t, d_up = run_up_walk()
        conds = {c["step"]: c for c in ctx["conds"]}
        for k, r in enumerate(steps or rows):
            pos = [x.id for x in rows].index(r.id)
            before_ids, later_ids = [x.id for x in rows[:pos]], [x.id for x in rows[pos + 1:]]
            t = build_case_tree(f"{case}-{pos}")
            rc, out = run_child_walk(ctx, t, walk, case, r.id, inj_rows)
            forced = f"upgrade-walk: forced {r.id}" in out
            tag = f"{r.id}" + (" · forced" if forced else "")
            if forced:
                ctx["forced"].setdefault(case, set()).add(r.id)
            if case == "skip":
                write_commit(t, "skip")
                diff = derive_digest_diff(derive_digest(t), d_up)
                w = us.run_step_isolated(r, "witness", t, ctx["clone"])["verdict"]
                bearing = bool(diff) or w != "ok"
                why = (f"the digest differs at {len(diff)} path(s)" if diff else "") or (f"its witness then {w}" if w != "ok" else "")
                if r.id in conds:
                    held, cwhy = run_condition(ctx, conds[r.id], r, walk, inj_rows, build_case_tree)
                    if held:
                        bearing, why = True, (why + "; " if why else "") + cwhy
                    else:
                        add_red(f"{r.id} · under its condition {cwhy}")
                if bearing:
                    print_line(f"skip · {tag} · load-bearing · {why}")
                else:
                    add_red(f"{r.id} · not load-bearing: skipped, the digest equals up's and its witness exits 0")
            elif case == "fail":
                rec = json.loads((t / RECEIPT).read_text(encoding="utf-8"))
                st = read_states(t) if r.id != SCHEMA_STEP else {}
                bad = []
                got = check_walk_exit(rc, out, ctx["ordered"], stops=1)
                if got:
                    bad.append("the walk did not stop as a held walk stopping at it does: " + " | ".join(got))
                if r.id == SCHEMA_STEP:
                    line = next((ln for ln in out.splitlines() if ln.startswith(f"step {r.id} · failed")), "")
                    if not line.rstrip().endswith(us.NOT_RECORDED_SUFFIX):
                        bad.append(f"its step line {line!r} does not end {us.NOT_RECORDED_SUFFIX}")
                    if rec.get("schema") != 3 or "steps" in rec or rec.get("gov_commit") != ctx["pin"]:
                        bad.append(f"the receipt reads schema {rec.get('schema')}, steps {'steps' in rec}, "
                                   f"gov_commit {str(rec.get('gov_commit'))[:8]}, not schema 3, none, the pin")
                else:
                    applied = [i for i in before_ids if st.get(i, {}).get("state") == "applied"]
                    if applied != [i for i in before_ids if i in st]:
                        bad.append("a step before it does not read applied")
                    if [i for i in before_ids if i not in st and i != SCHEMA_STEP]:
                        bad.append("a step before it is not recorded")
                    f = st.get(r.id, {})
                    if f.get("state") != "failed" or not str(f.get("failure", "")).startswith("exit 1"):
                        bad.append(f"it reads {f.get('state')} {f.get('failure', '')!r}, not failed with exit 1")
                    if [i for i in later_ids if i in st]:
                        bad.append(f"a later step is recorded: {[i for i in later_ids if i in st]}")
                if bad:
                    add_red(f"{r.id} · {'; '.join(bad)}")
                else:
                    print_line(f"fail · {tag} · the walk stopped at it, " + (
                        "the receipt at schema 3, its line not recorded" if r.id == SCHEMA_STEP and not st
                        else (f"last applied {before_ids[-1] if before_ids else 'none'}, it failed with exit 1")))
            elif case == "kill" and "first write undetermined" in out:
                add_red(f"{tag} · " + next(ln for ln in out.splitlines() if "first write undetermined" in ln).split(" · ", 1)[-1])
            elif case == "kill":
                bad = []
                if rc != 137:
                    bad.append(f"the child exited {rc}, not 137, so no walk was killed")
                lock = t.joinpath(*".governance/outbox/.update.lock".split("/"))
                _raw, holder = us.read_lock_holder(lock)
                dead, dwhy = us.check_holder_dead(holder)
                if dead != "dead":
                    bad.append(f"the lock's holder reads {dead}: {dwhy}")
                rec = json.loads((t / RECEIPT).read_text(encoding="utf-8"))
                kst = next((x for x in rec.get("steps") or [] if isinstance(x, dict) and x.get("id") == r.id), None)
                if r.id == SCHEMA_STEP:
                    kst_ok = kst is None  # TOOL-dSafePassage-15 S4: release-0's schema-3 receipt takes no row
                else:
                    kst_ok = bool(kst) and kst["state"] == "failed" and str(kst.get("failure", "")).startswith("interrupted:")
                if not kst_ok:
                    bad.append(f"its killed row reads {kst}")
                tr = build_case_tree(f"kill-{pos}-back", t)
                tw = build_case_tree(f"kill-{pos}-w", t)
                held = us.run_step_isolated(r, "witness", tw, ctx["clone"])["verdict"] == "ok"
                remove_tree(tw)
                # TOOL-dSafePassage-40 S1: the re-run marks the row only where the killed state holds
                # no record of it and no before-image
                marked = held and kst is None and not us.derive_image_path(t, r.id).exists()
                rc2, out2 = run_child_walk(ctx, t, walk, inject=inj_rows)
                got = check_walk_exit(rc2, out2, ctx["ordered"])
                if got:
                    bad.append("the re-run did not return: " + " | ".join(got))
                write_commit(t, "re-run")
                # AC7: k's row read without `via` on both sides, which TOOL-dSafePassage-33 S1 marks
                # exactly when `marked` holds
                diff = derive_digest_diff(derive_tree_digest(t, ctx["pin_modes"], r.id),
                                          derive_tree_digest(up_t, ctx["pin_modes"], r.id))
                if diff:
                    bad.append(f"the re-run's digest differs from up's at {', '.join(diff[:12])}")
                rrow = next((x for x in json.loads((t / RECEIPT).read_text(encoding="utf-8")).get("steps") or []
                             if isinstance(x, dict) and x.get("id") == r.id), {})
                if (rrow.get("via") == "witness") != marked:
                    bad.append(f"the re-run's row carries via {rrow.get('via')!r} where the killed state's "
                               f"witness {'holds' if held else 'does not hold'}"
                               + ("" if marked or not held else ", over a record or a before-image of its up"))
                rc3, out3 = run_child_walk(ctx, tr, back, inject=inj_rows)
                got = check_walk_exit(rc3, out3, ctx["ordered"])
                if got:
                    bad.append("the rollback from the killed state did not return: " + " | ".join(got))
                write_commit(tr, "rollback")
                diff = derive_digest_diff(derive_digest(tr), ctx["d_r0"])
                if diff:
                    bad.append(f"the rollback's digest differs from release-0's at {', '.join(diff[:12])}")
                if bad:
                    add_red(f"{tag} · {'; '.join(bad)}")
                else:
                    print_line(f"kill · {tag} · lock holder dead, " + ("no row for it (schema-3 receipt)" if kst is None
                        else "it failed interrupted:") + ", the re-run equals up"
                        + (", via witness as its witness holds" if marked else ", no via") + ", the rollback equals release-0")
                remove_tree(tr)
            remove_tree(t)
    return reds


def run_condition(ctx, cond: dict, row, walk, inj_rows, build_case_tree) -> tuple[bool, str]:
    """A `[[condition]]` row: under its plant or its fakes the walk without the skip stops at the
    step and with it gets past it. Returns (held, what was seen)."""
    us, _shims, _gk = load_engine()
    path_first = None
    if "fakes" in cond:
        fakes = ctx["root"] / "fakes"
        fakes.mkdir(exist_ok=True)
        for name, ver in cond["fakes"].items():
            (fakes / name).write_text(f"#!/usr/bin/env bash\necho {ver}\n", encoding="utf-8", newline="\n")
            (fakes / name).chmod(0o755)
        path_first = str(fakes)
    seen = {}
    for skip in (False, True):
        t = build_case_tree("cond-" + ("skip" if skip else "plain"))
        if "plant" in cond:
            write_plant_edits(t, [cond["plant"]])
            run_git(t, "-c", "user.email=t@e", "-c", "user.name=t", "commit", "-qam", "condition")
        rc, out = run_child_walk(ctx, t, walk, "skip" if skip else None, row.id if skip else None, inj_rows, path_first)
        rec = json.loads((t / RECEIPT).read_text(encoding="utf-8"))
        st = {x["id"]: x["state"] for x in us.read_step_states(rec)}
        seen[skip] = st.get(row.id)
        remove_tree(t)
    held = seen[False] == "failed" and seen[True] == "applied"
    return held, (f"{cond.get('id', row.id)}: unskipped it reads {seen[False]}, skipped {seen[True]}")


def check_arm_caught(rows: list[dict], got: int, want: int, lines: list[str]) -> bool:
    """TOOL-dSafePassage-77 S2: an arm set is caught by its own defect: its case exited `want`, and
    every `needle` of its `rows` is in one of `lines`, the case's reds or, for exit 2, the Stop's."""
    return got == want and all(any(r["needle"] in ln for ln in lines) for r in rows)


def run_case_arms(ctx: dict) -> list[str]:
    """S7: each arm's case run with it injected, after the real cases; an arm whose case stays green,
    or goes red naming no `needle` of its set, is a red. Arms naming each other in `with` run
    together once."""
    reds, done = [], set()
    for a in ctx["arms"]:
        names = tuple(sorted({a["name"], *a.get("with", [])}))
        if names in done:
            continue
        done.add(names)
        want = a.get("exit", 1)
        try:
            steps = [ctx["arm_rows"][a["name"]]] if a["case"] in PER_STEP and a["name"] in ctx["arm_rows"] else None
            check_inject(ctx, names)
            lines = run_walk_case(ctx, a["case"], steps, names)
            got = 1 if lines else 0
        except Stop as e:
            print_line(f"arm {'+'.join(names)} · {e}")
            lines, got = [str(e)], 2
        rows = [x for x in ctx["arms"] if x["name"] in names]
        caught = check_arm_caught(rows, got, want, lines)
        missed = ", ".join(sorted({r["needle"] for r in rows if not any(r["needle"] in ln for ln in lines)}))
        verdict = ("red on its case, as it must be" if caught
                   else f"exit {got} on {a['case']}, expected {want}" if got != want
                   else f"red, but no red names {missed}")
        print_line(f"arm {'+'.join(names)} · {a['case']} · {verdict}")
        ctx["arm_verdicts"].append(caught)
        if got != want:
            reds.append(f"arm {'+'.join(names)} · its case stays {'green' if got == 0 else got}")
        elif not caught:
            reds.append(f"arm {'+'.join(names)} · {a['case']} · red, but no red names {missed}")
    return reds


def check_inject(ctx: dict, names) -> None:
    """Each `--inject` name is an `[[arm]]` row's; a `plant` arm's path is tested where
    `write_plant_edits` applies it to each case tree (TOOL-dSafePassage-77 S6)."""
    for n in names:
        if not any(x["name"] == n for x in ctx["arms"]):
            raise Stop(f"--inject {n}: no [[arm]] row is named so")


# ------------------------------------------------------------------------------------------ the leg
def resolve_arm_rows(ctx: dict, us) -> dict:
    """Each step arm as a StepRow, its `{arms}`, `{plant:<id>}` and `{shim:<arm>}` tokens resolved."""
    subs = {"{arms}": (FIXTURE / "arms").as_posix()}
    subs.update({f"{{plant:{p['id']}}}": p["path"] for p in ctx["plants"]})
    subs.update({f"{{shim:{a['name']}}}": a["shim"]["from"] for a in ctx["arms"] if "shim" in a})

    def resolve_tokens(argv):
        out = []
        for tok in argv:
            for k, v in subs.items():
                tok = tok.replace(k, v)
            out.append(tok)
        return out
    rows = {}
    for a in ctx["arms"]:
        if "step" in a:
            s = a["step"]
            rows[a["name"]] = us.StepRow(id=f"upgrade-walk/{a['name']}", up=resolve_tokens(s["up"]), down=resolve_tokens(s["down"]),
                                         witness=resolve_tokens(s["witness"]), resume=s.get("resume", "atomic"), surfaces=[],
                                         needs_target=False, file=(FIXTURE / "arms.toml").as_posix(), row=0,
                                         introduced=ctx["tip"])
    return rows


def check_tree_clean(gov_root, own) -> list[str]:
    """TOOL-dSafePassage-77 S3: the tracked paths under the leg's directory and its sibling `lib`,
    both spelled from HERE's place in the toplevel, that differ from HEAD in `gov_root`, outside
    `own` (paths relative to HERE). Only those engine files are what the walk takes from HEAD."""
    kit = run_git(HERE, "rev-parse", "--show-prefix").rstrip("/")
    lib = f"{kit.rsplit('/', 1)[0]}/lib" if "/" in kit else "lib"
    mine = [f"{kit}/{o}" for o in own]
    out = subprocess.run(["git", "-C", str(gov_root), "status", "--porcelain", "--untracked-files=no", "--", kit, lib],
                         capture_output=True, text=True, encoding="utf-8", errors="replace",
                         env={k: v for k, v in os.environ.items() if not k.upper().startswith("GIT_")},
                         stdin=subprocess.DEVNULL).stdout  # not run_git: its strip eats the first status column
    paths = [ln[3:].split(" -> ")[-1].strip('"') for ln in out.splitlines() if len(ln) > 3]
    return sorted(p for p in paths if not any(p == m or p.startswith(m + "/") for m in mine))


def render_case_counts(per_case: dict) -> str:
    """TOOL-dSafePassage-77 S4: each case `<case> <n - u> passed <u> red`, `per_case` mapping a case
    to (n, its red lines), `u` the units that redded: a per-step or `plants` red line's second
    ` · ` field, the case itself otherwise. Ends `red lines <k>`, every red line counted."""
    parts, k = [], 0
    for c, (n, lines) in per_case.items():
        k += len(lines)
        if c in PER_STEP or c == "plants":
            u = len({ln.split(" · ")[1] if " · " in ln else ln for ln in lines})
        else:
            u = 1 if lines else 0
        parts.append(f"{c} {n - u} passed {u} red")
    return " · ".join(parts + [f"red lines {k}"])


def check_graders() -> list[str]:
    """TOOL-dSafePassage-77 S7: S1, S2, S3 and S4's functions fed fabricated inputs, one line per
    grader; returns the reds. Each is a pure call or a scratch repository it removes."""
    import contextlib
    import io
    kit = run_git(HERE, "rev-parse", "--show-prefix").rstrip("/")
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="uwg"))

    def build_repo(name: str, files: dict) -> pathlib.Path:
        t = scratch / name
        t.mkdir()
        run_git(t, "init", "-q")
        run_git(t, "config", "core.autocrlf", "false")
        for p, text in files.items():
            (t / p).parent.mkdir(parents=True, exist_ok=True)
            (t / p).write_text(text, encoding="utf-8", newline="\n")
        write_commit(t, "grader")
        return t

    def check_grade_order_kind() -> str:
        path = ".claude/skills/lexicon/SKILL.md"
        row = {"id": "edited-render", "path": path, "expect": "ordered", "order": "render-edited"}
        t = build_repo("order", {f"{OUTBOX}/update-rollback-demo.md": f"# an order naming {path}\n"})
        with contextlib.redirect_stdout(io.StringIO()):
            before = check_plant_rows({}, t, [row])
            _us, _shims, gk = load_engine()
            (t / OUTBOX / (gk.render_row_order_key("render-edited", path) + ".md")).write_text("x\n", encoding="utf-8")
            after = check_plant_rows({}, t, [row])
        if not before:
            return "an outbox naming the path under another order's file read ordered"
        return f"its own order's file did not read ordered: {after}" if after else ""

    def check_grade_arm_needle() -> str:
        row = {"name": "witness-first", "case": "kill", "needle": ".uw-arm/1-payload"}
        tie = ["kill · upgrade-walk/witness-first · first write undetermined: a and b share one modification time"]
        own = ["kill · upgrade-walk/witness-first · the re-run's digest differs from up's at .uw-arm/1-payload"]
        if check_arm_caught([row], 1, 1, tie):
            return "a first write undetermined red caught the arm"
        if check_arm_caught([row], 0, 1, own):
            return "a case exiting 0 caught the arm"
        return "" if check_arm_caught([row], 1, 1, own) else "a red naming its needle did not catch the arm"

    def check_grade_tree_clean() -> str:
        tools, gates = (kit.rsplit("/", 1)[0] if "/" in kit else "."), "run-gates"
        steps, plants = f"{kit}/steps.toml", f"{kit}/fixtures/release-0/plants.toml"
        memo, evidence = "memory/note.md", f"{tools}/{gates}/ceiling-evidence.txt"
        t = build_repo("clean", {steps: "a\n", plants: "a\n", memo: "a\n", evidence: "a\n"})
        for p in (plants, memo, evidence, f"{kit}/untracked.py"):
            with open(t / p, "a", encoding="utf-8", newline="\n") as fh:
                fh.write("\n")
            got = check_tree_clean(t, LEG_OWN)
            if got:
                return f"{p} edited, it returned {got}"
            run_git(t, "checkout", "-q", "--", ".")
        with open(t / steps, "a", encoding="utf-8", newline="\n") as fh:
            fh.write("\n")
        got = check_tree_clean(t, LEG_OWN)
        return "" if got == [steps] else f"{steps} edited, it returned {got}"

    def check_grade_case_counts() -> str:
        line = render_case_counts({"down": (1, ["down · a", "down · b"]),
                                   "kill": (2, ["kill · r1 · a", "kill · r1 · b"])})
        want = ("down 0 passed 1 red", "kill 1 passed 1 red", "red lines 4")
        return "" if all(w in line for w in want) else f"it rendered {line!r}"

    def check_grade_fixture_keys() -> str:
        fx = scratch / "fixture"
        fx.mkdir()
        seen = []
        for name, text, read, key in (
                ("plants.toml", '[[plant]]\nid = "no-kind"\npath = "a"\nedit = "append"\ntext = "x"\nexpect = "ordered"\n',
                 read_plant_rows, "no-kind"),
                ("arms.toml", '[[arm]]\nname = "no-needle"\ncase = "up"\n', read_arm_rows, "no-needle")):
            (fx / name).write_text(text, encoding="utf-8", newline="\n")
            try:
                read(fx)
                seen.append(f"{name} with no key read as a default")
            except Stop as e:
                if key not in str(e):
                    seen.append(f"{name}'s Stop does not name {key}: {e}")
        return "; ".join(seen)

    reds = []
    try:
        for name, grade in (("order-kind", check_grade_order_kind), ("arm-needle", check_grade_arm_needle),
                            ("tree-clean", check_grade_tree_clean), ("case-counts", check_grade_case_counts),
                            ("fixture-keys", check_grade_fixture_keys)):
            try:
                why = grade()
            except (Stop, OSError, KeyError, ValueError) as e:
                why = f"it raised {type(e).__name__}: {e}"
            print_line(f"grader · {name} · " + (f"RED · {why}" if why else "ok"))
            if why:
                reds.append(f"grader {name}")
    finally:
        remove_tree(scratch)
    return reds


def main(argv: list[str]) -> int:
    args, case, step, inject, pin_rev, listing = list(argv), None, None, [], None, False
    while args:
        a = args.pop(0)
        if a == "--list":
            listing = True
        elif a in ("--case", "--step", "--inject", "--pin") and args:
            v = args.pop(0)
            if a == "--case":
                case = v
            elif a == "--step":
                step = v
            elif a == "--inject":
                inject.append(v)
            else:
                pin_rev = v
        else:
            sys.stderr.write(__doc__.split("\n\n")[0] + "\nusage: upgrade_walk.py [--list] [--case <case> "
                             "[--step <id>] [--inject <name> ...]] [--pin <rev>]\n")
            return 2
    if case is not None and case not in CASES:
        print_line(f"no case {case!r}: the cases are {', '.join(CASES)}")
        return 2
    if check_graders():
        print_line("RED: a grader of this leg reads wrong, so nothing it would measure is trusted")
        return 1
    gov_root = pathlib.Path(run_git(HERE, "rev-parse", "--show-toplevel"))
    root = pathlib.Path(tempfile.mkdtemp(prefix="uw"))
    t0 = time.time()
    try:
        dirty = [] if listing else check_tree_clean(gov_root, LEG_OWN)
        if dirty:
            raise Stop(f"the working tree differs from HEAD at {', '.join(dirty)}, engine files the walk "
                       "takes from HEAD's committed bytes; commit or stash them")
        us, _shims, _gk = load_engine()
        pin = run_git(gov_root, "rev-parse", "--verify", f"{pin_rev}^{{commit}}") if pin_rev else read_release_pin()
        problems = check_release_pin(gov_root, pin)
        if problems:
            for p in problems:
                print_line(p)
            raise Stop(f"the pin {pin[:8]} is not release-0's commit")
        plants, conds = read_plant_rows(), read_condition_rows()
        gov_plants = read_fixture_rows("gov_plant")
        ctx = build_release_tree(gov_root, root, pin, plants, gov_plants, with_target=not listing)
        ctx.update(ordered={r['path'] for r in plants if r['expect'] == 'ordered'}, plants=plants, conds=conds, arms=read_arm_rows(), cache={}, forced={}, attended=0, shims=None,
                   arm_verdicts=[])
        ctx["rows"] = us.read_steps(ctx["clone"], ctx["tip"], us.resolve_landed_ref(ctx["clone"]) or "")
        ctx["arm_rows"] = resolve_arm_rows(ctx, us)
        print_line(f"pin {pin} · landed ref {ctx['landed']} · tip {ctx['tip']} · {len(ctx['rows'])} step(s)")
        if listing:
            for n, r in enumerate(ctx["rows"], 1):
                print_line(f"step {n} · {r.id} · introduced {r.introduced} · {r.file}")
            for kind, rows in (("plant", plants), ("gov_plant", gov_plants), ("condition", conds), ("arm", ctx["arms"])):
                for r in rows:
                    print_line(f"{kind} · {r.get('id') or r.get('name') or r.get('step')} · "
                        + " · ".join(f"{k} {v}" for k, v in r.items() if k in ("path", "expect", "what", "step", "case", "fakes")))
            return 0 if ctx["rows"] else 2
        if not ctx["rows"]:
            raise Stop("no step is declared at the tip, so there is nothing to walk")
        if step is not None and step not in {r.id for r in ctx["rows"]} | {r.id for r in ctx["arm_rows"].values()}:
            raise Stop(f"--step {step}: no declared step has that id")
        check_inject(ctx, inject)
        ls = run_git(ctx["clone"], "ls-tree", "-r", pin)
        ctx["pin_modes"] = {ln.split("\t", 1)[1]: ln.split()[0] for ln in ls.splitlines() if "\t" in ln}
        ctx["d_r0"] = derive_tree_digest(ctx["r0"], ctx["pin_modes"])
        reds, per_case = [], {}
        probe = os.environ.get("FOREIGN_PREFIX_PROBE") == "1"
        for c in ([case] if case else CASES):
            pool = [r for r in ctx["rows"] + [ctx["arm_rows"][n] for n in inject if n in ctx["arm_rows"]]
                    if step is None or r.id == step] if c in PER_STEP else None
            got = run_walk_case(ctx, c, pool, tuple(inject))
            per_case[c] = (len(pool) if pool is not None else len(plants) if c == "plants" else 1, got)
            reds += got
            # FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the case above walked the subject, and a probe stops here.
            if probe:
                print("foreign-prefix-probe: stopped after 1 arm", flush=True)
                break
        if not case and not inject and not probe:
            reds += run_case_arms(ctx)
        forced = "; ".join(f"{c} {', '.join(sorted(s))}" for c, s in ctx["forced"].items()) or "none"
        print_line(f"summary · pin {pin[:8]} · tip {ctx['tip'][:8]} · {len(ctx['rows'])} step(s) · "
            + render_case_counts(per_case)
            + f" · forced {forced} · shims {ctx['shims'] if ctx['shims'] is not None else 'not run'}"
            + (" (measured nothing)" if ctx["shims"] == 0 else "")
            + f" · attended {ctx['attended']}"
            + (f" · arms {sum(ctx['arm_verdicts'])} red on their case, {len(ctx['arm_verdicts']) - sum(ctx['arm_verdicts'])} not"
               if ctx["arm_verdicts"] else "")
            + f" · {round(time.time() - t0)} s")
        print_line("RED: " + " | ".join(reds) if reds else "GREEN")
        return 1 if reds else 0
    except Stop as e:
        print_line(f"nothing measured: {e}")
        return 2
    finally:
        remove_tree(root)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main(sys.argv[1:]))
