#!/usr/bin/env python3
"""stale_edges.py — the fixture of PLAY-dOrderedCharter-33 AC9: `update` runs the playbook kit's drift
verb over a target whose overlay pins a gov unit gov has since changed in meaning.

    python <this kit>/fixtures/stale_edges.py --plant order|refuse [--stub no-handler]

Each plant builds a scratch gov holding a copy of this kit's `govkit.py`, gov's policy, playbook and
memory-tree kits, and a kit `alpha` shipping one open unit; installs a target selecting the `playbook`
entry, commits its overlay unit amending gov's unit at its pin, then lands a gov release changing the
unit's text under a `semantic` change record. `order` leaves `instructions.stale` at its default and
observes the `stale` line among the verdicts, the tally's count and, under `--write`, one
`update-unit-<slug>.md`; `refuse` commits `instructions.stale = "refuse"` in the target's policy file and
observes exit 1 with nothing written. `--stub no-handler` removes the handler call in the scratch copy,
so each observation is seen red.

Exit 0 every observation matched · 1 one missed its case · 2 the plant could not be built or observed.
"""
from __future__ import annotations

import argparse
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import govkit  # noqa: E402 — the deployer itself, for its tool root and its sibling resolver
from fixture_target import build_scratch_gov, build_target  # noqa: E402 — the scratch repositories' factory
from retired_edits import LOADER, read_clean_env, resolve_kit_path, run_git, write_commit  # noqa: E402

PLANTS = ("order", "refuse")
STUBS = {"no-handler": "m.read_unit_drift = lambda *a, **k: ({}, None)"}
UNIT, REPO, BUILD = "unit.push", "repo.push", "tFx"
TEXTS = ("MUST tell the team before a push.", "MUST tell nobody before a push.")
PLAYBOOK_KIT = ('id = "playbook"\nhome = "playbook"\nversion_from = { none = "fixture" }\n\n'
                '[check]\nnone = "fixture"\n\n[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                '[adopt]\nargv = []\nmutates_index = false\n')
IGNORE = shutil.ignore_patterns("__pycache__", "*.test.sh", "legacy-homes.txt")


def build_stale_gov(tmp: pathlib.Path) -> pathlib.Path:
    """Release A: the deployer, the three kits, `alpha`'s unit at its first text, one build folder."""
    g = build_scratch_gov(tmp / "gov")
    gk = g / resolve_kit_path(govkit.GOVKIT_DIR.name)
    gk.mkdir(parents=True)
    for name in ("govkit.py", "adopters.toml", "upgrade_steps.py"):
        shutil.copy2(govkit.GOVKIT_DIR / name, gk / name)
    exempt = "".join(f'[[exempt]]\npath = "{{prefix}}/{d}"\nwhy = "the fixture\'s {d}"\n\n'
                     for d in (govkit.GOVKIT_DIR.name, "policy", "memory-tree", "alpha"))
    (gk / govkit.REGISTRY_NAME).write_text(
        '[surface]\nglobs = ["{prefix}/*"]\n\n[selection]\ndefault = ["playbook"]\n\n'
        '[[entry]]\nid = "playbook"\ndescriptor = "{prefix}/playbook/kit.toml"\n\n' + exempt,
        encoding="utf-8", newline="\n")
    for home, anchor in (("policy", "policy.py"), ("playbook", "pins.py"), ("memory-tree", "design_lib.py")):
        shutil.copytree(govkit.resolve_kit_dir(home, anchor, govkit.GOVKIT_DIR), g / resolve_kit_path(home),
                        ignore=IGNORE)
    (g / resolve_kit_path("playbook", "kit.toml")).write_text(PLAYBOOK_KIT, encoding="utf-8", newline="\n")
    (g / resolve_kit_path("alpha")).mkdir(parents=True)
    (g / resolve_kit_path("alpha", "kit.toml")).write_text('id = "alpha"\n', encoding="utf-8", newline="\n")
    write_manifest(g, TEXTS[0])
    (g / ".memory-tree.conf").write_text('MEMORY_ROOT=memory\nFAMILIES="play:PLAY"\n', encoding="utf-8", newline="\n")
    (g / "memory" / "builds" / BUILD).mkdir(parents=True)
    (g / "memory" / "builds" / BUILD / "README.md").write_text("# the fixture build\n", encoding="utf-8", newline="\n")
    write_commit(g, "A")
    return g


def write_manifest(g: pathlib.Path, text: str) -> None:
    (g / resolve_kit_path("alpha", "instructions.toml")).write_text(
        f'[[unit]]\ntag = "{UNIT}"\nlevel = 3\ntype = "directive"\nscope = ["reader.every"]\n'
        f'trigger = "always"\nclass = "open"\ntext = "{text}"\n', encoding="utf-8", newline="\n")


def derive_pin(g: pathlib.Path, text: str) -> str:
    sys.path.insert(0, str(g / resolve_kit_path("memory-tree")))
    import design_lib
    return design_lib.derive_pin_hash(text)


def run_govkit(g: pathlib.Path, t: pathlib.Path, *args: str, stub: str = "") -> subprocess.CompletedProcess:
    path = (g / resolve_kit_path(govkit.GOVKIT_DIR.name, "govkit.py")).as_posix()
    return subprocess.run([sys.executable, "-c", LOADER, path, stub, args[0], "--target", str(t), *args[1:]],
                          capture_output=True, text=True, encoding="utf-8", errors="replace",
                          stdin=subprocess.DEVNULL, env=read_clean_env())


def read_unit_orders(t: pathlib.Path) -> list[str]:
    box = t / ".governance" / "outbox"
    return sorted(p.name for p in box.glob("update-unit-*.md")) if box.is_dir() else []


def run_stale_plant(tmp: pathlib.Path, plant: str, stub: str) -> list[tuple[str, str, str]]:
    g = build_stale_gov(tmp)
    t = build_target(tmp, f'gov_source = "local"\nprefix = "{govkit.derive_tool_root(govkit.repo_root())}"\n'
                          'kits = ["playbook"]\n', "t")
    p = run_govkit(g, t, "apply")
    if p.returncode != 0:
        raise OSError(f"the scratch install refused (exit {p.returncode}): {(p.stdout + p.stderr)[-900:]}")
    write_commit(t, "the install")
    pin = derive_pin(g, TEXTS[0])
    (t / ".governance" / "instructions.toml").write_text(
        f'[[unit]]\ntag = "{REPO}"\nlevel = 3\ntype = "directive"\nscope = ["reader.every"]\n'
        f'trigger = "always"\nedges = ["amends={UNIT}@{pin}"]\ntext = "MUST also post in the channel."\n',
        encoding="utf-8", newline="\n")
    if plant == "refuse":
        (t / ".governance" / "policy.toml").write_text('[instructions]\nstale = "refuse"\n', encoding="utf-8",
                                                       newline="\n")
    write_commit(t, "the overlay")
    write_manifest(g, TEXTS[1])
    sys.path.insert(0, str(g / resolve_kit_path("memory-tree")))
    import build_records
    build_records.write_change(g, BUILD, "PLAY-tFx-1", UNIT, "edit", "semantic", f"{UNIT}@{pin}",
                               f"{UNIT}@{derive_pin(g, TEXTS[1])}", build_records.DOOR_PROOF)
    write_commit(g, "B")
    p = run_govkit(g, t, "update", stub=stub)
    out = p.stdout + p.stderr
    stale = [ln for ln in out.splitlines() if ln.startswith("  stale") and "[unit" in ln and REPO in ln]
    tally = next((ln for ln in out.splitlines() if ln.startswith("govkit update — ") and "unit:stale" in ln), "")
    if plant == "order":
        obs = [("the read-only exit", str(p.returncode), "0"),
               ("the stale line among the verdicts", str(len(stale)), "1"),
               ("the tally's count", str("unit:stale 1" in tally), "True")]
        p = run_govkit(g, t, "update", "--write", stub=stub)
        return obs + [("the --write exit", str(p.returncode), "0"),
                      ("update-unit orders", str(len(read_unit_orders(t))), "1")]
    p = run_govkit(g, t, "update", "--write", stub=stub)
    dirty = run_git(t, "status", "--porcelain", "--untracked-files=all").stdout.strip()
    return [("the refused exit", str(p.returncode), "1"),
            ("the stale line names the edge", str(len(stale)), "1"),
            ("bytes written", "none" if not dirty and not read_unit_orders(t) else dirty or "an order", "none")]


def run_fixture(plant: str, stub: str | None) -> int:
    print(f"stale-edges fixture: plant {plant}" + (f" · stub {stub}" if stub else ""))
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="sted-"))
    try:
        obs = run_stale_plant(tmp, plant, STUBS.get(stub or "", ""))
    except (govkit.Refusal, LookupError, OSError, ValueError) as exc:
        print(f"stale-edges fixture: cannot observe: {exc}")
        return 2
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    bad = 0
    for name, seen, want in obs:
        bad += seen != want
        print(f"  {name}: {seen!r} · expects {want!r} · {'ok' if seen == want else 'MISS'}")
    print(f"stale-edges fixture: {len(obs) - bad} of {len(obs)} observation(s) matched")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="stale_edges.py")
    ap.add_argument("--plant", choices=PLANTS, required=True)
    ap.add_argument("--stub", choices=sorted(STUBS))
    args = ap.parse_args(argv)
    return run_fixture(args.plant, args.stub)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    raise SystemExit(main(sys.argv[1:]))
