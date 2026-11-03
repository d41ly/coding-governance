"""policy_value — the playbook kit's one caller of the policy reader (PLAY-dOrderedCharter-19 S8).

Built to PLAY-dOrderedCharter-7's section 4 "The policy reads": `read_policy_value(key, root, rev=None)`
finds the policy kit through the inline `resolve_kit_dir` below, since a kit imports no sibling kit, and
runs `<sys.executable> <kit>/policy.py get <key> --explain [--rev <rev>]` with `root` as its working
directory, so the value is `root`'s committed policy at its landed revision, an unset key its catalogue
default with its reason. It returns the stdout lines, one per member for a list, and the `--explain`
line. On exit 2, or with no policy kit found, it raises `PolicyRefused` carrying the key and the
reader's own line, which each caller names in its own refusal. Every call passes its key as a string
literal first, the shape the policy kit's reader-coverage arm counts. Units 7, 25 and 26 call this
module and never copy it.
"""
from __future__ import annotations

import os
import pathlib
import subprocess
import sys

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent


# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


class PolicyRefused(RuntimeError):
    """The policy reader refused `key`, or no policy kit was found; `line` is the reader's own words."""

    def __init__(self, key: str, line: str):
        super().__init__(f"{key}: {line}")
        self.key = key
        self.line = line


def read_policy_value(key: str, root, rev: str | None = None) -> tuple[list[str], str]:
    """-> (the value's stdout lines, the `--explain` line) for policy key `key` at `root`."""
    try:
        kit = resolve_kit_dir("policy", "policy.py", KIT_DIR)
    except LookupError as exc:
        raise PolicyRefused(key, f"no policy kit found: {exc}") from None
    argv = [sys.executable, str(kit / "policy.py"), "get", key, "--explain", *(["--rev", rev] if rev else [])]
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    try:
        p = subprocess.run(argv, cwd=str(root), capture_output=True, text=True, encoding="utf-8",
                           errors="replace", stdin=subprocess.DEVNULL, env=env)
    except OSError as exc:
        raise PolicyRefused(key, f"policy.py get did not run: {exc}") from None
    err = [ln for ln in (p.stderr or "").splitlines() if ln.strip()]
    if p.returncode != 0:
        raise PolicyRefused(key, err[-1] if err else f"policy.py get exited {p.returncode}")
    return p.stdout.splitlines(), err[-1] if err else ""
