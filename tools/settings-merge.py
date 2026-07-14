#!/usr/bin/env python3
"""settings-merge.py — idempotently wire the agent-cap PreToolUse/Workflow hook into a target
repo's .claude/settings.json. Stdlib only (json, argparse, pathlib); py>=3.10 (write_text newline=).

# gov:kit settings-merge@1.0

The hook it ensures (shape mirrors WIRE-INTO-PROJECT.md and tools/hooks/agent-cap.js verbatim):

    {"hooks": {"PreToolUse": [
      {"matcher": "Workflow",
       "hooks": [{"type": "command",
                  "command": "node \\"${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js\\""}]}]}}

Idempotent by structure: a re-run finds the existing Workflow matcher group already carrying an
`agent-cap.js` command and makes NO change (apply-twice-changed = 0). Existing keys and any other
PreToolUse groups are preserved; a foreign command inside the Workflow group is kept alongside.

A wired target is DETECTED by grepping the literal `agent-cap.js` in .claude/settings.json — JSON
carries no comment marker, so that command substring IS the deployer's "is-it-wired?" signal.

Usage:
    python tools/settings-merge.py [SETTINGS_FILE] [--hook-path PATH] [--check] [--selftest]
      SETTINGS_FILE  default .claude/settings.json (resolved from cwd = target repo root)
      --hook-path    default .claude/hooks/agent-cap.js (the copied hook, repo-relative)
      --check        report drift without writing: exit 1 if a merge WOULD change the file
      --selftest     run the in-file assert suite in a tempdir; exit 0 on pass
Exit: 0 wired (already present OR merged this run) · 1 --check found drift · 2 error.

# ponytail: hard-wired to the single agent-cap Workflow hook — the only settings.json merge that
# exists in this repo today. Lift the matcher-group to a `--fragment FILE` arg when a second
# consumer (statusLine, another matcher) appears. Dedup is a substring test on 'agent-cap.js' and
# deliberately does NOT rewrite a stale hook path (a Phase-3 upgrade concern, not Phase-0 wiring).
"""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

KIT_SETTINGS_MERGE_VERSION = "1.0"  # gov:kit settings-merge@1.0 — engine identity
HOOK_MARKER = "agent-cap.js"  # the loose join: dedup key AND the deployer's "is-it-wired?" grep target


def _command(hook_path: str) -> str:
    # forward slashes on purpose: ${CLAUDE_PROJECT_DIR} + POSIX path is identical on every OS
    return f'node "${{CLAUDE_PROJECT_DIR}}/{hook_path}"'


def merge(obj: dict, hook_path: str) -> dict:
    """Ensure the agent-cap Workflow hook is present in obj (mutates + returns obj)."""
    hooks = obj.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        raise ValueError("settings 'hooks' is not an object")
    pre = hooks.setdefault("PreToolUse", [])
    if not isinstance(pre, list):
        raise ValueError("settings 'hooks.PreToolUse' is not an array")
    entry = {"type": "command", "command": _command(hook_path)}
    group = next((g for g in pre if isinstance(g, dict) and g.get("matcher") == "Workflow"), None)
    if group is None:
        pre.append({"matcher": "Workflow", "hooks": [entry]})
        return obj
    inner = group.setdefault("hooks", [])
    if not isinstance(inner, list):
        raise ValueError("settings Workflow group 'hooks' is not an array")
    if any(isinstance(h, dict) and HOOK_MARKER in str(h.get("command", "")) for h in inner):
        return obj  # already wired — no change
    inner.append(entry)
    return obj


def _load(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:  # ValueError covers json.JSONDecodeError
        raise ValueError(f"cannot read {path}: {e}") from e
    if not isinstance(data, dict):
        raise ValueError(f"{path} is not a JSON object")
    return data


def _dump(obj: dict) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def run(settings_file: str, hook_path: str, check: bool) -> int:
    path = Path(settings_file)
    existed = path.exists()
    try:
        before = _dump(_load(path))
        after = _dump(merge(json.loads(before), hook_path))
    except ValueError as e:
        print(f"settings-merge: {e}", file=sys.stderr)
        return 2
    if before == after:
        print(f"settings-merge: agent-cap Workflow hook already wired in {settings_file}")
        return 0
    if check:
        print(f"settings-merge: DRIFT — {settings_file} is missing the agent-cap Workflow hook",
              file=sys.stderr)
        return 1
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        if existed:
            Path(str(path) + ".bak").write_bytes(path.read_bytes())  # byte-faithful, not the normalized parse
        path.write_text(after, encoding="utf-8", newline="\n")
    except OSError as e:
        print(f"settings-merge: write failed: {e}", file=sys.stderr)
        return 2
    print(f"settings-merge: wired agent-cap Workflow hook into {settings_file}"
          + (f" (backed up to {settings_file}.bak)" if existed else " (created)"))
    return 0


def _selftest() -> int:
    hp = ".claude/hooks/agent-cap.js"
    cmd = _command(hp)
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)

        # 1) absent file -> creates the Workflow group + agent-cap command, exit 0
        sf = root / ".claude" / "settings.json"
        assert run(str(sf), hp, check=False) == 0
        wf = [g for g in json.loads(sf.read_text(encoding="utf-8"))["hooks"]["PreToolUse"]
              if g.get("matcher") == "Workflow"]
        assert len(wf) == 1 and any(h["command"] == cmd for h in wf[0]["hooks"])
        assert "\r" not in sf.read_text(encoding="utf-8")  # LF-only on every OS

        # 2) re-run -> byte-identical (no change); --check on a wired file -> 0
        first = sf.read_text(encoding="utf-8")
        assert run(str(sf), hp, check=False) == 0 and sf.read_text(encoding="utf-8") == first
        assert run(str(sf), hp, check=True) == 0

        # 3) pre-existing unrelated key is preserved through the merge
        sf2 = root / "s2.json"
        sf2.write_text('{"model": "x"}\n', encoding="utf-8")
        assert run(str(sf2), hp, check=False) == 0
        o2 = json.loads(sf2.read_text(encoding="utf-8"))
        assert o2["model"] == "x" and o2["hooks"]["PreToolUse"][0]["matcher"] == "Workflow"

        # 4) pre-existing Workflow group w/ a FOREIGN command -> agent-cap appended, foreign kept, ONE group
        sf3 = root / "s3.json"
        sf3.write_text(json.dumps({"hooks": {"PreToolUse": [
            {"matcher": "Workflow",
             "hooks": [{"type": "command", "command": "node other.js"}]}]}}) + "\n", encoding="utf-8")
        assert run(str(sf3), hp, check=False) == 0
        wf3 = [g for g in json.loads(sf3.read_text(encoding="utf-8"))["hooks"]["PreToolUse"]
               if g.get("matcher") == "Workflow"]
        cmds = [h["command"] for h in wf3[0]["hooks"]]
        assert len(wf3) == 1 and "node other.js" in cmds and cmd in cmds

        # 5) malformed JSON -> exit 2
        sf4 = root / "s4.json"
        sf4.write_text("{ not json", encoding="utf-8")
        assert run(str(sf4), hp, check=False) == 2

        # 6) --check on an absent file -> drift (1), and nothing written
        sf5 = root / "sub" / "s5.json"
        assert run(str(sf5), hp, check=True) == 1 and not sf5.exists()

    print("settings-merge selftest: PASS")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Idempotently wire the agent-cap Workflow hook into .claude/settings.json")
    p.add_argument("settings_file", nargs="?", default=".claude/settings.json")
    p.add_argument("--hook-path", default=".claude/hooks/agent-cap.js")
    p.add_argument("--check", action="store_true")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args(argv)
    if a.selftest:
        return _selftest()
    return run(a.settings_file, a.hook_path, a.check)


if __name__ == "__main__":
    sys.exit(main())
