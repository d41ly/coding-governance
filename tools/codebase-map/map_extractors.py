"""map_extractors.py — coding-governance's inventory declarations (the only project-owned code).

Instantiated from map_extractors.template.py per INVENTORY-DERIVATION.md.

WHAT IS ENUMERABLE HERE. This repo's product is a merge bar and a set of copy-in kits, so the
surfaces where "somebody added one and nobody recorded it" actually hurts are the gate legs, the
kits, the hooks and the catalogues — not routes or screens. Every inventory below is a NAMED,
ADDABLE moving part of that product.

ROOT RESOLUTION. Handled by the engine since the aRootedPrefix unit: map_lib walks up for
`.codebase-map.conf` bounded by `.git`, so this repo's `tools/` install prefix needs nothing here.

Rules honoured (each was a shipped bug once, per the derivation checklist):
- Fail CLOSED. Every extractor raises MapError rather than returning fewer keys; an extractor that
  quietly returns [] is a permanent coverage hole the freshness gate structurally cannot see.
- No hardcoded enum of anything forward-only. Kits, hooks and skills are enumerated from the tree,
  so tomorrow's member needs no code patch here.
- Exclude by SUFFIX or by a generated-file name, never by a list of today's filenames.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

import map_lib as m

# THE INSTALL PREFIX is no longer this file's problem. It used to set CODEBASE_MAP_ROOT from
# `Path(__file__).resolve().parents[2]`, because map_lib resolved the root as the kit dir's
# GRANDPARENT and this repo installs kits under `tools/`. the aRootedPrefix unit fixed that in the
# ENGINE — `map_lib.resolve_root()` walks up for `.codebase-map.conf`, bounded by `.git` — so the
# workaround is obsolete. It is also now BANNED: the kit's selftest rejects `resolve()` in kit code,
# since it follows a junction to the link target and would disagree with `map_lib.kit_dir()` about
# the prefix stamped into byte-compared artifacts.
ROOT = m.repo_root()


def _tool_kits() -> list[str]:
    """Every kit directory directly under tools/.

    Deliberately NOT README-gated: tools/hooks, tools/lib and tools/workflows carry no README and
    are still kits. Gating on a README would have silently dropped three of ten, which is the
    green-by-absence class this file exists to avoid.
    """
    base = ROOT / "tools"
    if not base.is_dir():
        raise m.MapError("kits: tools/ is missing — the extractor is mis-rooted")
    names = sorted(p.name for p in base.iterdir() if p.is_dir() and p.name != "__pycache__")
    if not names:
        raise m.MapError("kits: no kit directories under tools/ — the extractor is mis-rooted")
    return names


def _git_hooks() -> list[str]:
    """The tracked git hooks in .githooks/ (core.hooksPath points here).

    A hook's sibling `<stem>.test.sh` is its TEST, not a hook, and is excluded by suffix so a new
    hook-plus-test pair needs no patch here.
    """
    base = ROOT / ".githooks"
    m.no_subdirs(base, "git-hooks")
    names = sorted(
        p.name for p in base.iterdir() if p.is_file() and not p.name.endswith(".test.sh")
    )
    if not names:
        raise m.MapError("git-hooks: .githooks/ holds no hook files")
    return names


def _gate_legs(doc: object) -> object:
    """Leg names from tools/gate-legs.json — the single source the runner reads.

    Raises through json_artifact_inventory on a malformed doc. A leg with no name is a MapError
    rather than a dropped key, because a nameless leg is exactly the one nobody would notice.
    """
    if not isinstance(doc, list):
        raise m.MapError("gate-legs: expected a JSON array of legs")
    for leg in doc:
        if not isinstance(leg, dict) or not leg.get("name"):
            raise m.MapError(f"gate-legs: a leg carries no name: {leg!r}")
    return (leg["name"] for leg in doc)


# --------------------------------------------------------------------------------------
# EXTRACTORS — inventory id -> zero-arg callable returning sorted list[str] of keys.
# --------------------------------------------------------------------------------------

EXTRACTORS: dict[str, object] = {
    # The merge bar itself. The runner single-sources its legs from this artifact and
    # tools/run-gates.test.sh forbids a hardcoded leg command, so the JSON IS the registry.
    "gate-legs": lambda: m.json_artifact_inventory(
        ROOT / "tools" / "gate-legs.json", "gate-legs", _gate_legs
    ),
    # The copy-in kits — the deployable product.
    "kits": _tool_kits,
    # The tracked hooks that enforce the bar at the git boundary.
    "git-hooks": _git_hooks,
    # The multi-agent harnesses and the gates over them.
    "workflow-scripts": lambda: m.glob_inventory(
        ROOT / "tools" / "workflows", "*.js", "workflow-scripts"
    ),
    # The skill ENGINE sources (machine-junctioned per node).
    "skill-engines": lambda: m.walk_dir_keys(
        ROOT / "skills", frozenset({"SKILL.md"}), "skill-engines"
    ),
    # The RENDERED skills a session actually loads (adopters re-render these from a template).
    "rendered-skills": lambda: m.walk_dir_keys(
        ROOT / ".claude" / "skills", frozenset({"SKILL.md"}), "rendered-skills"
    ),
    # The bug-class catalogue. INDEX.md is GENERATED from the records and is not itself a class.
    "gotcha-classes": lambda: m.glob_inventory(
        ROOT / "memory" / "gotchas",
        "*.md",
        "gotcha-classes",
        exclude=frozenset({"INDEX.md"}),
    ),
    # Charter-cited binding documents — each one spends from the read-path budget (hygiene 16).
    "guides": lambda: m.glob_inventory(ROOT / "memory" / "guides", "*.md", "guides"),
    # One mutable shard per id family, per .memory-tree.conf FAMILIES.
    "backlog-shards": lambda: m.glob_inventory(
        ROOT / "memory" / "backlog", "*.md", "backlog-shards"
    ),
}


# --------------------------------------------------------------------------------------
# SYMBOL_EXTRACTORS — the reuse RECALL tier. Feeds generated/symbols.json only, never the
# ratchet, so a new symbol never fails CI.
#
# bash is DECLARED RECALL-DARK in .codebase-map.conf rather than covered here: map_lib ships a
# real parser for Python and an enumeration floor for JS, and nothing for shell. A regex over
# shell function definitions would be exactly the silently-skips-what-it-forgot extractor the
# fail-closed law bans, and it would look like coverage.
# --------------------------------------------------------------------------------------

def _live_py(layer: str) -> list[dict[str, str]]:
    """Python symbols under tools/, minus the `*.template.py` scaffolding sources.

    A template and its instantiated twin define the SAME function names in two files, and
    map_lib.fan_in() counts distinct referencing files minus the symbol's own def file — so the
    twin counts as a reference and every duplicated symbol's fan-in is inflated by one. Measured
    here: with the templates indexed, two `test_*` functions from test_codebase_map.template.py
    outranked walk_dir_keys in the reuse shortlist on that artifact alone.

    This filters the RESULT of the real parser rather than narrowing its walk, so a SyntaxError in
    a template still raises instead of being skipped. The exclusion is by the `.template.py`
    suffix, a kit-wide naming convention, not by a list of today's filenames.
    """
    rows = m.python_symbols(ROOT / "tools", layer)
    live = [r for r in rows if not r["file"].endswith(".template.py")]
    if not live:
        raise m.MapError(f"{layer}: every python symbol under tools/ was filtered as a template")
    return live


SYMBOL_EXTRACTORS: dict[str, object] = {
    # Real-parser-backed (ast); raises MapError on a SyntaxError rather than indexing less.
    "kit-py": lambda: _live_py("kit-py"),
    # The stdlib enumeration floor. Sparse by construction here — the hooks and gates are
    # CommonJS scripts that export nothing, so the only exports are the workflow `meta` blocks.
    # That is accurate coverage of a layer with few exports, not a hole.
    "kit-js": lambda: m.enumerate_exports(
        ROOT / "tools", "kit-js", extensions=frozenset({".js"})
    ),
}


def all_symbols() -> list[dict[str, str]]:
    """Every covered layer's symbols, concatenated (recall index source)."""
    out: list[dict[str, str]] = []
    for layer, fn in SYMBOL_EXTRACTORS.items():
        out.extend(fn())  # type: ignore[operator]
    return out


#: Record ids are `FAMILY-<slug>-<seq>` over the FAMILIES enum in .memory-tree.conf. The families
#: are forward-only — a fifth stream is a conf edit, not a code edit — so the default open grammar
#: is kept rather than pinning today's PLAY/KICK/TOOL/DEPL alternation here.
DECISION_ID_RE = m.DEFAULT_DECISION_ID_RE

#: No path in this repo encodes a claim key in its filename (no migration chain, no revision ids),
#: so map_diff attributes purely through dossier globs.
KEYED_ATTRIBUTORS: tuple[tuple[re.Pattern[str], str], ...] = ()


def inventory_ids() -> tuple[str, ...]:
    if not EXTRACTORS:
        raise m.MapError(
            "map_extractors.EXTRACTORS is empty — declare this project's inventories "
            "(see codebase-map/INVENTORY-DERIVATION.md); an inventory-less map enforces nothing"
        )
    return tuple(EXTRACTORS)


def all_inventories() -> dict[str, list[str]]:
    return {inv_id: fn() for inv_id, fn in EXTRACTORS.items()}  # type: ignore[operator]
