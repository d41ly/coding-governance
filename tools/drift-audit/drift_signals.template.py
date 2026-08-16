"""drift_signals.py — THIS PROJECT's drift-signal declarations (the only project-owned code).

gov:kit drift-audit@1.3

Copied from tools/drift-audit/drift_signals.template.py at adoption. Fill the four required names below,
then run `python tools/drift-audit/drift_report.py`.

The engine (`drift_report.py`) owns the signal IMPLEMENTATIONS. This file owns only what is
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
- TRACE_CUTOFF is a GRANDFATHER, not a tuning knob. Set it to the date your repo's "unit id in the
  commit subject" rule became binding, and never to whichever date makes the number smallest — a
  cutoff chosen to read zero is the vacuous-selector defect, not a clean signal.
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
# TRACE_CUTOFF / TRACE_GLOBS — signal `closed_specs_with_no_product_commit`, which asks whether a
# spec claiming CLOSED is backed by any commit that both names it and changed the product.
#
# BOTH ARE OPTIONAL AND BOTH SHIP UNSET. With TRACE_CUTOFF empty the signal reports
# `gateable: False` and judges nothing, so adopting this kit never reds your first run over specs
# that closed before you had a convention for the engine to check.
#
# TRACE_CUTOFF: the date, `YYYY-MM-DD`, from which your repo's commit subjects reliably name the
# unit. It is compared against each spec's STATUS-HEADER date (the last-change date, so on a CLOSED
# spec the close date), never the filename date — keying on the filename exempts every spec AUTHORED
# before the cutoff even when it closes long after, which on the reference repo was 18 live units.
#
# TRACE_GLOBS: the pathspecs that count as evidence a build shipped. Defaults to PRODUCT_GLOBS.
# Narrow it when PRODUCT_GLOBS holds paths your RECORD-keeping commits routinely touch (rendered
# skills, a kickoff manifest, generated config) — otherwise a bookkeeping commit certifies the
# bookkeeping, which is the hole the path restriction exists to close.
TRACE_CUTOFF: str = ""

TRACE_GLOBS: list[str] = []

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

# --------------------------------------------------------------------------------------------
# DECLARED_EMPTY — signals whose population is empty ON PURPOSE. `--check` reds a gateable signal
# that has gone DEAD, because a blind instrument reporting 0 is the failure this kit exists to
# refuse; a signal you have deliberately not populated yet is not blind, and belongs here.
#
# `shrink_only_lists_not_shrinking` starts here because SHRINK_ONLY above ships empty. Remove it the
# moment you declare your first list — leaving it here after that is how the exemption becomes the
# hole.
# --------------------------------------------------------------------------------------------

DECLARED_EMPTY: set[str] = {
    "shrink_only_lists_not_shrinking",   # SHRINK_ONLY above ships empty
    "handkept_inventories_disagreeing_with_source",   # HANDKEPT above ships empty
}

# --------------------------------------------------------------------------------------------
# RATCHETS — the shrink-only NUMBERS whose WEAKENING direction must be justified in place.
#
# Every gate that owns a pin compares only `value > pin`, so RAISING the pin and DRAINING the
# population look identical from the outside: both turn a red run green, and nothing distinguishes
# "we fixed it" from "we stopped asking". Declaring a scalar here makes a weakening move refuse
# unless a comment within the preceding lines names BOTH numbers as `<old> -> <new>`.
#
# `weakens` is the direction that makes the guarantee weaker, and it differs by kind: a pin, ceiling
# or budget weakens UPWARD; a floor weakens DOWNWARD. It is declared per entry rather than inferred
# from the name, because getting it backwards refuses every honest ratchet and waves through every
# regression.
#
# SCALARS ONLY. A compound floor (`<name>:<n>:<n>` sets) needs a per-member diff and is not covered;
# leave those to the gate that owns them rather than declaring them here and believing they are
# watched. Ships EMPTY — seed it with the pins you actually keep.
# --------------------------------------------------------------------------------------------

RATCHETS: list[dict] = [
    # {"file": ".memory-tree.conf", "key": "ORPHAN_ID_PIN", "weakens": "up"},
]
