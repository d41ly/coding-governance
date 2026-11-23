#!/usr/bin/env python3
"""spawn_guard_pack.py — the upgrade step `agent-cap/spawn-guard-to-roles-pack` (TOOL-dBoundRoles-25, S7).

    python <gov tool root>/govkit/steps/spawn_guard_pack.py up|down|witness <target> <prefix>

Its row is the hooks kit descriptor's `[[upgrade]]`. The hooks kit's agent limit hook retired, and every rule
it ran moved into the roles kit's spawn guard; this step moves a target's wiring with it. `<prefix>` is the
target's install prefix: the roles kit's `spawn-guard.fragment.json` is found under it by `resolve_kit_dir`,
the receipt first, and the target's own `settings-merge.py` at `<prefix>/settings-merge.py`, else at the path
its receipt row records.

THE UP. No command in the target's `.claude/settings.json` naming `agent-cap.js`: exit 0, nothing written.
Otherwise it writes the before-image of that file through the step reader's `write_before_image`, the
after-state computed first by the same two merges run over a scratch copy, so a re-run over a killed up
converges on the first image. Then, where the target installs the roles kit, it runs the target's
`settings-merge.py --fragment <roles kit>/spawn-guard.fragment.json`, and only then `settings-merge.py
--fragment <tmp> --unwire` once per group carrying the old command, `<tmp>` a fragment for that entry
written under `tempfile.mkdtemp`: the marker `agent-cap.js`, the group's event and matcher, and the hook
path the target's receipt records. Wiring first means a killed up leaves both hooks wired, never neither,
the order the hooks kit's descriptor records for a moved security guard. A target without the roles kit
loses the guard, which matches what it had: rule 6 is armed only by a role index. The settings file then
holds the image's after-bytes, or the up refuses naming the drift.

THE WITNESS exits 0 when no command naming `agent-cap.js` is wired and, where the roles kit is installed,
the `Workflow|Agent` group of `PreToolUse` carries a command naming `spawn-guard.js`; 1 otherwise. It reads
the working tree and runs no target code.

THE DOWN restores `.claude/settings.json` from the before-image (`write_from_before_image`): byte-identical,
or a refusal, exit 1, naming the file where it was edited since the up, nothing restored.

WHAT IT DOES NOT CHECK: a hand-written command naming the old hook by another file name, and the old hook
file itself, which govkit's withdrawn arm removes under `--write-withdrawals` once the command has moved.

Exit 0 done, 1 refused or not applied, naming why, 2 a usage error.
"""

import importlib.util
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

STEP_ID = "agent-cap/spawn-guard-to-roles-pack"
SAY = "spawn-guard-pack"
SETTINGS = ".claude/settings.json"
OLD_MARKER = "agent-cap.js"
NEW_MARKER = "spawn-guard.js"
FRAGMENT = "spawn-guard.fragment.json"
ROLES_HOME = "roles"
MERGER = "settings-merge.py"
EVENT = "PreToolUse"
MATCHER = "Workflow|Agent"


def load_steps():
    """The step reader beside this file's directory, imported by its path: the runner's `-I` drops
    this file's own directory from `sys.path`, and the before-image helpers live there."""
    path = pathlib.Path(__file__).resolve().parents[1] / "upgrade_steps.py"
    mod = sys.modules.get("upgrade_steps")
    if mod is not None and getattr(mod, "__file__", None) and pathlib.Path(mod.__file__).resolve() == path:
        return mod
    spec = importlib.util.spec_from_file_location("upgrade_steps", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["upgrade_steps"] = mod
    spec.loader.exec_module(mod)
    return mod


STEPS = load_steps()
Refusal = STEPS.Refusal


def read_settings(data: bytes | None) -> dict:
    """The settings document `data` holds, {} where there is none; text that is not a JSON object refuses."""
    if data is None:
        return {}
    try:
        doc = json.loads(data.decode("utf-8-sig"))
    except (UnicodeDecodeError, ValueError) as e:
        raise Refusal(f"{SETTINGS}: does not parse as JSON ({e}), so its hooks cannot be read") from None
    if not isinstance(doc, dict):
        raise Refusal(f"{SETTINGS}: is not a JSON object, so its hooks cannot be read")
    return doc


def read_groups(doc: dict, marker: str) -> list[tuple[str, str]]:
    """Each `(event, matcher)` of a group in `doc` holding a command that names `marker`, in file order, once."""
    out = []
    hooks = doc.get("hooks") if isinstance(doc.get("hooks"), dict) else {}
    for event, groups in hooks.items():
        for g in groups if isinstance(groups, list) else []:
            inner = g.get("hooks") if isinstance(g, dict) else None
            if any(isinstance(h, dict) and marker in str(h.get("command", "")) for h in inner or []):
                key = (event, g.get("matcher") if isinstance(g.get("matcher"), str) else "")
                if key not in out:
                    out.append(key)
    return out


def read_receipt_path(target: pathlib.Path, name: str) -> str | None:
    """The `path` of the target receipt's row whose `path` or `source` ends in `name`, None where none does."""
    try:
        rows = json.loads((target / ".governance" / "install.json").read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        return None
    for row in rows:
        if isinstance(row, dict) and row.get("path") and any(
                str(row.get(k) or "").split("/")[-1] == name for k in ("path", "source")):
            return str(row["path"])
    return None


def read_fragment(target: pathlib.Path, prefix: str) -> pathlib.Path | None:
    """The roles kit's spawn-guard fragment in `target` under `prefix`, None where no roles kit holds one."""
    try:
        kit = STEPS.resolve_kit_dir(ROLES_HOME, FRAGMENT, target / prefix)
    except LookupError:
        return None
    return kit / FRAGMENT if target in kit.parents else None


def read_merger(target: pathlib.Path, prefix: str) -> pathlib.Path:
    """The target's own settings-merge.py: at `<prefix>/`, else where its receipt row says; a refusal where neither is."""
    for rel in (f"{prefix}/{MERGER}" if prefix not in ("", ".") else MERGER, read_receipt_path(target, MERGER)):
        if rel and STEPS.derive_contained_rel(rel) and (target / rel).is_file():
            return target / rel
    raise Refusal(f"{MERGER}: the target holds none at {prefix or '.'}/ nor where its receipt records one, so "
                  f"its settings cannot be merged; remedy: install the settings-merge entry, then re-run the step")


def build_env() -> dict:
    """The caller's environment less every `GIT_` name, so a merge answers for the target alone."""
    return {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}


def run_merges(target: pathlib.Path, merger: pathlib.Path, settings: pathlib.Path, fragment: pathlib.Path | None,
               groups: list[tuple[str, str]], scratch: pathlib.Path, old_path: str) -> None:
    """The up's merges over `settings`, run from the target root: the pack's fragment wired FIRST, then one
    `--unwire` per group still carrying the old command, each through a fragment written under `scratch`."""
    calls = []
    if fragment is not None:
        calls.append([str(fragment.relative_to(target).as_posix())])
    for n, (event, matcher) in enumerate(groups):
        frag = scratch / f"old-{n}.fragment.json"
        frag.write_text(json.dumps({"name": "agent-cap", "event": event, "matcher": matcher,
                                    "marker": OLD_MARKER, "hook_path": old_path}) + "\n", encoding="utf-8")
        calls.append([str(frag), "--unwire"])
    for extra in calls:
        p = subprocess.run([sys.executable, "-I", str(merger), str(settings), "--fragment", *extra],
                           cwd=str(target), env=build_env(), stdin=subprocess.DEVNULL, capture_output=True,
                           encoding="utf-8", errors="replace")
        if p.returncode != 0:
            tail = " / ".join((p.stderr or p.stdout).strip().splitlines()[-3:]) or f"exit {p.returncode}"
            raise Refusal(f"{merger.relative_to(target).as_posix()} --fragment {' '.join(extra)} exited "
                          f"{p.returncode}: {tail}")


def cmd_up(target: pathlib.Path, prefix: str) -> int:
    path = target / SETTINGS
    if not read_groups(read_settings(path.read_bytes() if path.is_file() else None), OLD_MARKER):
        print(f"{SAY}: up · no command in {SETTINGS} names {OLD_MARKER}, so there is nothing to move")
        return 0
    merger = read_merger(target, prefix)
    fragment = read_fragment(target, prefix)
    old_path = read_receipt_path(target, OLD_MARKER) or OLD_MARKER
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="spawn-guard-pack-"))
    try:
        def derive_after(before):
            data = (before or {}).get(SETTINGS) if before is not None else path.read_bytes()
            copy = scratch / "settings.json"
            copy.write_bytes(data)
            run_merges(target, merger, copy, fragment, read_groups(read_settings(data), OLD_MARKER), scratch, old_path)
            return {SETTINGS: copy.read_bytes()}

        after = STEPS.write_before_image(target, STEP_ID, derive_after)
        groups = read_groups(read_settings(path.read_bytes()), OLD_MARKER)
        run_merges(target, merger, path, fragment, groups, scratch, old_path)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    if path.read_bytes() != after[SETTINGS]:
        raise Refusal(f"{SETTINGS}: the merges wrote other bytes than the before-image records; remedy: run the "
                      f"step's down, which restores the file or names why it cannot")
    print(f"{SAY}: up · {SETTINGS} " + (f"wires {NEW_MARKER} from {fragment.relative_to(target).as_posix()} and "
                                         if fragment is not None else "holds no roles kit's pack to wire, and ")
          + f"no longer wires {OLD_MARKER}")
    return 0


def cmd_down(target: pathlib.Path, prefix: str) -> int:
    restored = STEPS.write_from_before_image(target, STEP_ID)
    print(f"{SAY}: down · restored {', '.join(restored) or 'nothing: no before-image, no up applied'}")
    return 0


def cmd_witness(target: pathlib.Path, prefix: str) -> int:
    path = target / SETTINGS
    doc = read_settings(path.read_bytes() if path.is_file() else None)
    if read_groups(doc, OLD_MARKER):
        print(f"{SAY}: witness · {SETTINGS} still wires {OLD_MARKER}: not applied")
        return 1
    if read_fragment(target, prefix) is not None and (EVENT, MATCHER) not in read_groups(doc, NEW_MARKER):
        print(f"{SAY}: witness · the roles kit is installed and the {EVENT} {MATCHER} group of {SETTINGS} carries no "
              f"{NEW_MARKER} command: not applied")
        return 1
    print(f"{SAY}: witness · no command names {OLD_MARKER}, and the pack is wired wherever the roles kit is: applied")
    return 0


def main(argv: list[str]) -> int:
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(argv) != 3 or argv[0] not in verbs:
        sys.stderr.write("usage: python spawn_guard_pack.py up|down|witness <target> <prefix>\n")
        return 2
    prefix = argv[2]
    if prefix not in ("", ".") and STEPS.derive_contained_rel(prefix) is None:
        sys.stderr.write(f"{SAY}: '{prefix}' is not an install prefix inside the target\n")
        return 2
    try:
        return verbs[argv[0]](pathlib.Path(argv[1]).resolve(), prefix)
    except Refusal as e:
        sys.stderr.write(f"{SAY}: {argv[0]} refused · {e}\n")
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
