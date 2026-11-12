#!/usr/bin/env python3
"""The memory-recall kit's project layer: read `.memory-tree.conf`, declare nothing of its own.

gov:kit memory-recall@1.34

The kit indexes the memory tree the memory-tree kit already declares, and the conf layer that reads
it lives in that kit since PLAY-dOrderedCharter-18: `id_grammar.py`, beside the memory-tree kit's other
modules, holds `repo_root`, `load_conf`, `ConfError`, `Conf` with `Conf.digest`, and `resolve`, and
this file re-exports every one of them, found through `resolve_kit_dir` (this kit `requires`
memory-tree). Two of that conf's keys are read and no third declaration is invented:

  MEMORY_ROOT   the corpus root passed to `git ls-files` and folded into extract.DURABLE
  FAMILIES      discipline:FAMILY pairs; the uppercase FAMILY tokens are the id allowlist

The conf is REQUIRED and its absence is a refusal, not a default. This kit does not OWN the conf, so
it must not create one: the refusal names the memory-tree kit and prints a two-key stub instead.
There is deliberately no --memory-root and no --families flag anywhere in the kit.

What stays here: `KIT_MEMORY_RECALL_VERSION`, which `kit.toml`'s `version_from` reads, and `main()`,
the KEY=VALUE printer `adopt-memory-recall.sh` parses.
"""

from __future__ import annotations

import pathlib
import sys

# The kit never leaves bytecode in the adopter's worktree — see query.py's note. ABOVE the import of
# the grammar module: the flag is read when a module is imported, not when it is defined.
sys.dont_write_bytecode = True

KIT_MEMORY_RECALL_VERSION = "1.34"


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


_GRAMMAR_KIT = str(resolve_kit_dir("memory-tree", "id_grammar.py", pathlib.Path(__file__).resolve().parent))
if _GRAMMAR_KIT not in sys.path:
    sys.path.append(_GRAMMAR_KIT)

from id_grammar import (  # noqa: E402,F401 — re-exported: every recall reader keeps its spelling
    CONF_NAME,
    DEFAULT_CACHE_BUDGET_MB,
    NODE_TAG_CLASS,
    Conf,
    ConfError,
    load_conf,
    refusal,
    repo_root,
    resolve,
)


def main() -> int:
    """Print the resolved project layer as KEY=VALUE, or the refusal on stderr.

    ONE home for the refusal text: adopt-memory-recall.sh shells out to this rather than restating
    it, so the CLI and the adopt script cannot drift on what a missing conf says (AC3).

    The KEY=VALUE lines are a MACHINE-READABLE protocol (adopt-memory-recall.sh parses them with
    `read`), so the newline is part of the contract. On Windows, text-mode stdout translated every
    \\n to \\r\\n and each value reached the shell carrying a trailing CR — which rendered into
    SKILL.md as `memory\\r/` and `(PLAY KICK TOOL DEPL\\r)`, breaking its YAML frontmatter outright.
    Pin LF so the protocol is byte-identical on every OS.
    """
    try:
        sys.stdout.reconfigure(newline="\n")
    except (AttributeError, ValueError):  # a replaced or non-TextIOWrapper stdout
        pass
    try:
        c = resolve()
    except ConfError as e:
        print(e, file=sys.stderr)
        return 2
    print(f"ROOT={c.root.as_posix()}")
    print(f"MEMORY_ROOT={c.memory_root}")
    print(f"FAMILIES={' '.join(c.families)}")
    print(f"NODE_TAG_CLASS={c.node_tag_class}")
    print(f"CITED_FAMILIES={' '.join(c.cited_families)}")
    print(f"BUILD_QID_CUTOFF={' '.join(f'{k}:{v}' for k, v in sorted(c.build_qid_cutoff.items()))}")
    print(f"EXPORT_DIR={c.export_dir or ''}")
    print(f"RECALL_EXCLUDE={' '.join(c.exclude)}")
    print(f"CONF_DIGEST={c.digest()}")
    print(f"KIT_VERSION={KIT_MEMORY_RECALL_VERSION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
