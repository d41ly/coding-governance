"""drift_signals.py — THIS PROJECT's drift-signal declarations (the only project-owned code).

gov:kit drift-audit@1.0

Copied from drift-audit/drift_signals.template.py at adoption. Fill the four required names below,
then run `python drift-audit/drift_report.py`.

The engine (`drift_report.py`) owns the five signal IMPLEMENTATIONS. This file owns only what is
genuinely repo-shaped. The corpus root and disciplines are NOT here — they come from
`.memory-tree.conf`, which the memory-tree kit owns. Do not restate them; a second declaration of
the same value is the defect this kit exists to detect.

Rules, each of which was a wrong number once:
- PRODUCT_GLOBS must contain PRODUCT SOURCE ONLY. Never an id catalog, an alias file, a lockfile, or
  anything under the memory tree. Upstream, including a recall alias file (which lists every id in
  the corpus by construction) made the spec-status oracle fire on all 110 specs.
- PINS are measured, never guessed. Run the report first, read the values, then seed the pins at
  exactly those values. A pin above the measured value hides a live regression on day one.
- A HANDKEPT probe returns `(claims, actual)` and must read the GENERATED side from its real source,
  not from a second copy of it.
"""

from __future__ import annotations

import json
import re

# --------------------------------------------------------------------------------------------
# PRODUCT_GLOBS — pathspecs `git grep` searches for evidence that a spec's work actually shipped.
# The oracle is: a non-terminal spec whose own id appears in product source describes shipped work.
# --------------------------------------------------------------------------------------------

PRODUCT_GLOBS: list[str] = [
    # "src",
    # "app",
    # "packages",
]

# --------------------------------------------------------------------------------------------
# SHRINK_ONLY — repo-relative path -> what the list is. Any exemption/waiver/baseline file whose own
# header promises it only shrinks. The signal reports each one's seed count vs its count today.
# A shrink-only list with no scheduled shrinker is a permanent exemption with optimistic framing.
# --------------------------------------------------------------------------------------------

SHRINK_ONLY: dict[str, str] = {
    # "memory/map/baseline.toml": "map coverage backfill grace",
    # "memory/project/curation-debt.txt": "index-budget waiver",
}

# --------------------------------------------------------------------------------------------
# HANDKEPT — hand-maintained inventories that mirror a generated/authoritative source.
# Each entry: {"record": <label>, "source": <label>, "probe": callable(ctx) -> (claims, actual)}.
# `ctx` exposes .root (pathlib.Path), .git (a Git wrapper with .run(*args)), .conf, .memory_root.
# Raise or return mismatched values freely — a probe that throws is REPORTED, never skipped.
# --------------------------------------------------------------------------------------------


def _example_gate_leg_count(ctx) -> tuple[int, int]:
    """Charter prose claims N gate legs; the manifest defines M. Classic hand-kept twin."""
    legs = json.loads((ctx.root / "tools/gate-legs.json").read_text(encoding="utf-8"))
    legs = legs if isinstance(legs, list) else legs.get("legs", legs)
    actual = len(legs)
    charter = (ctx.root / (ctx.charter or "AGENTS.md")).read_text(encoding="utf-8", errors="replace")
    m = re.search(r"gate suite.*?\((\d+)\s+checks?\)", charter, re.I | re.S)
    claims = int(m.group(1)) if m else -1
    return claims, actual


HANDKEPT: list[dict] = [
    # {"record": "charter gate-leg count", "source": "tools/gate-legs.json",
    #  "probe": _example_gate_leg_count},
]

# --------------------------------------------------------------------------------------------
# PINS — shrink-only ceilings per GATEABLE signal, seeded at the values the report actually measured.
# `--check` reds when a value exceeds its pin. Lower a pin whenever its population drops; raising one
# needs the same justification any other ratchet raise does.
#
# Signals with no pin entry default to tolerance 0.
# --------------------------------------------------------------------------------------------

PINS: dict[str, int] = {
    # "ledger_rows_contradicting_git": 0,
    # "non_terminal_specs_cited_by_product_source": 0,
    # "handkept_inventories_disagreeing_with_source": 0,
}

# --------------------------------------------------------------------------------------------
# CHARTER — optional. The file holding the node-registry table, used to resolve THIS node's tag for
# the node-scoped dangling-pointer signal. Defaults to AGENTS.md then CLAUDE.md when unset.
# --------------------------------------------------------------------------------------------

# CHARTER = "AGENTS.md"
