"""drift_signals.py — coding-governance's own drift-signal declarations (dogfooding the kit).

gov:kit drift-audit@1.0

Copied from drift_signals.template.py and filled for THIS repo. The corpus root and disciplines are
NOT restated here — they come from `.memory-tree.conf`, which the memory-tree kit owns.
"""

from __future__ import annotations

import json
import re

# --------------------------------------------------------------------------------------------
# PRODUCT_GLOBS — this repo's "product" is its kits, its skill engine and the playbook template.
# `memory/` is deliberately absent: keying a record's truth on another record is circular, and an id
# catalog inside the corpus would certify every spec at once.
# --------------------------------------------------------------------------------------------

PRODUCT_GLOBS: list[str] = [
    "tools",
    "skills",
    ".claude",
    "parallel-coding-governance.template.md",
    "parallel-coding-governance.customize.md",
    "parallel-coding-governance.domain-rules.md",
    "WIRE-INTO-PROJECT.md",
]

# --------------------------------------------------------------------------------------------
# SHRINK_ONLY — nothing here yet. This repo ships no waiver/baseline/grace list of its own; the ones
# the kits CREATE live in adopting repos, not here.
#
# Declared empty rather than omitted so the signal reports `live: False` (DEAD PROBE) instead of a
# clean 0. An empty population scoring "ok" is precisely the green-by-absence reading this kit exists
# to refuse — and the kit holds itself to that rule too.
# --------------------------------------------------------------------------------------------

SHRINK_ONLY: dict[str, str] = {}

# --------------------------------------------------------------------------------------------
# HANDKEPT — hand-maintained inventories mirroring an authoritative source.
# --------------------------------------------------------------------------------------------


def _charter_mentions_every_leg(ctx) -> tuple[int, int]:
    """Does the charter's gate-suite section still NAME every leg the manifest defines?

    Returns (legs mentioned, legs total) so `agrees` means "the charter describes the whole manifest".

    A FIRST attempt compared the charter's BULLET COUNT (12) to the leg count (19) and was a
    guaranteed false positive: a charter bullet legitimately groups several legs ("kit self-tests"
    covers six commands), so those two numbers should never be equal. Comparing NAMES instead gives a
    predicate that can legitimately reach zero offenders — which is the difference between a signal
    and a permanently-red decoration. A leg the charter never names is the real defect: a session
    obeying the charter's "enumerate exhaustively" instruction under-reports its own coverage.
    """
    legs = json.loads((ctx.root / "tools/gate-legs.json").read_text(encoding="utf-8"))
    legs = legs if isinstance(legs, list) else legs.get("legs", legs)
    names = [str(l.get("name") or l.get("id") or "") for l in legs]
    names = [n for n in names if n]
    total = len(names)

    charter = (ctx.root / (ctx.charter or "AGENTS.md")).read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^##\s+The gate suite.*?$(.*?)^##\s", charter, re.M | re.S)
    section = m.group(1) if m else ""
    if not section:
        return -1, total
    mentioned = sum(1 for n in names if n in section)
    return mentioned, total


HANDKEPT: list[dict] = [
    {
        "record": "AGENTS.md gate-suite section names every leg",
        "source": "tools/gate-legs.json",
        "probe": _charter_mentions_every_leg,
    },
]

# --------------------------------------------------------------------------------------------
# PINS — seeded at MEASURED values, never guessed. Lower each as its population drains; raising one
# needs the same justification any other ratchet raise does.
# --------------------------------------------------------------------------------------------

PINS: dict[str, int] = {
    # 1 — `in-flight/b.md:5` says "merged ... NOT pushed" while `c2f608e7` IS an ancestor of
    # origin/main. Verified by hand. Node `b` owns that file, so node `c` does not edit it; the pin
    # holds the line until b prunes its own row, and drops to 0 when it does.
    "ledger_rows_contradicting_git": 1,
    # 2 — TOOL-aBatchedLintel-1 and TOOL-aGuardedTally-1, both INPROGRESS with their ids in tracked
    # kit source. INPROGRESS means "approved, build underway", which is arguably TRUE for a
    # built-but-unmerged unit, so this is the oracle's known residual ambiguity rather than proven
    # rot. Pinned, not gated to zero, for exactly that reason — read them before lowering it.
    "non_terminal_specs_cited_by_product_source": 2,
    # 1 — the charter's gate-suite section names 7 of the manifest's 19 legs. A real gap: a session
    # obeying "enumerate exhaustively" from the charter under-reports its own coverage by 12 legs.
    "handkept_inventories_disagreeing_with_source": 1,
}

CHARTER = "AGENTS.md"
