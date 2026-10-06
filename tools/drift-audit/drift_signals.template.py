"""drift_signals.py — THIS PROJECT's drift-signal declarations (the only project-owned code).

gov:kit drift-audit@1.23

Copied from <prefix>/drift-audit/drift_signals.template.py at adoption. Fill the four required names below,
then run `python <prefix>/drift-audit/drift_report.py`.

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
import pathlib
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
    # This file lands beside the kit, and the manifest sits in the kit's parent: derived, not spelled.
    legs = json.loads((pathlib.Path(__file__).resolve().parent.parent / "gate-legs.json")
                      .read_text(encoding="utf-8"))
    legs = legs if isinstance(legs, list) else legs.get("legs", legs)
    actual = len(legs)
    charter = (ctx.root / (ctx.charter or "AGENTS.md")).read_text(encoding="utf-8", errors="replace")
    m = re.search(r"gate suite.*?\((\d+)\s+checks?\)", charter, re.I | re.S)
    claims = int(m.group(1)) if m else -1
    return claims, actual


HANDKEPT: list[dict] = [
    # {"record": "charter gate-leg count", "source": "<prefix>/gate-legs.json",
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

# TRACE_WAIVER: where the signal's per-spec waiver registry lives, repo-relative. One row per waived
# spec, `<spec path><TAB><reason>`, for a CLOSED unit no TRACE_GLOBS subject can ever name, such as
# one whose product landed before your id-in-subject convention. A records-only deliverable takes NO
# row: its spec declares `records-only` as a `·`-separated field of its status header, and the signal
# sets it aside and lists it under `records_only`. BLANK keeps `<MEMORY_ROOT>/project/trace-waiver.txt`,
# where an absent file is an empty waiver set. Declare it when your memory tree has no `project/`
# directory. A DECLARED path that is absent or outside the tree is a finding of its own.
TRACE_WAIVER: str = ""

# EVIDENCE_GLOBS — signal 2's population, narrower than PRODUCT_GLOBS. A citation from a test
# file is the house's own bookkeeping certifying the bookkeeping, so signal 2 should not read
# one as evidence a unit shipped. SHIPS EMPTY and falls back to PRODUCT_GLOBS, which is the
# unnarrowed behaviour — correct on day one and permanently inert if nobody fills it, which is
# why the kit descriptor declares it a hole with a discharge probe rather than leaving it to
# be noticed. Git pathspec magic works here: `:(exclude)*.test.sh` and friends.
EVIDENCE_GLOBS: list[str] = []

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
    # "readme_mechanism_drift": 0,   # REPORT-ONLY: seed it at what your first report MEASURES.
    #   Left at 0 every non-empty count reads "out of tolerance", which is how a reader learns
    #   to skip the line. The kit cannot ship a number for it: the value is your corpus’s, and a
    #   guessed pin is the one thing this block forbids.
    # "cutoff_keys_armed": 0,   # armed `_CUTOFF` keys in your tracked root confs. Seed it from your
    #   first report's value; with no entry it reports and never gates, because the shipped example
    #   confs arm a key and a default of 0 would red your first `--check`.
    # "aborted_work_landed": 0,     # REPORT-ONLY: seed it at what your first report MEASURES; it
    #   drains as `--settle` writes `work-landed-at` onto each listed record.
    # "discarded_work_landed": 0,   # REPORT-ONLY: seed it at what your first report MEASURES; no
    #   verb clears it, so a pin there records the value rather than a drain target.
}

# --------------------------------------------------------------------------------------------
# BASELINES — optional. For a GATEABLE signal whose detail rows each name their offender by `id`
# (`non_terminal_specs_cited_by_product_source`, `closed_specs_with_no_product_commit`), list the
# offender ids instead of pinning a count: a pin cannot tell a drained offender from a new one at an
# equal count, and a set can. `--check` reds on an id the list does not carry, on a listed id that
# no longer offends (delete its line), and on a list that gains an id against the base, or is first
# seeded above the base's pin. Seed it with the ids your first report measured, and drop that
# signal's PINS entry in the same change: a signal takes one bound, and declaring both is refused.
# --------------------------------------------------------------------------------------------

BASELINES: dict[str, list[str]] = {}

# --------------------------------------------------------------------------------------------
# CHARTER — optional. The governing doc a HANDKEPT probe reads as `ctx.charter`, as the example
# probe above does. Defaults to AGENTS.md then CLAUDE.md when unset.
# --------------------------------------------------------------------------------------------

# CHARTER = "AGENTS.md"

# --------------------------------------------------------------------------------------------
# AUTO_MEMORY_DIR — optional. The agent auto-memory directory `dangling_pointers_in_own_ledger`
# audits: every backticked repo path in its `*.md` notes is checked against `git ls-files`. Two
# expansions: `~` is the user's home, and `{checkout}` is the primary checkout's absolute path with
# every character outside `[A-Za-z0-9-]` turned into `-`, which is how Claude Code keys a project.
# For Claude Code: "~/.claude/projects/{checkout}/memory". BLANK is NOT ASKED; a declaration naming
# no directory on this node reads DEAD PROBE. Report-only: the notes are one machine's.
# --------------------------------------------------------------------------------------------

AUTO_MEMORY_DIR: str = ""

# --------------------------------------------------------------------------------------------
# REMOTE_CI_WORKFLOW — optional. The workflow file (e.g. "ci.yml") whose runs on the default branch
# `remote_ci_red_streak` reads through an authenticated `gh`. BLANK is NOT ASKED: a repo with no
# remote CI reads neither a clean 0 nor a dead probe. Report-only, and never asked under --check.
# --------------------------------------------------------------------------------------------

REMOTE_CI_WORKFLOW: str = ""

# --------------------------------------------------------------------------------------------
# DEAD_READINGS_LIMIT and DEAD_FILED — optional. A report-only signal that reads DEAD PROBE for
# DEAD_READINGS_LIMIT recorded readings in a row (the shipped 10 when absent) stops printing
# "ignore its value" and asks you to take it out of SIGNALS, or to file an ask and name it here.
# DEAD_FILED maps a signal to that ask's id, and the status then prints `filed <id>`; an entry for a
# signal that is not in the report, or is live, is named in the header until you take it out. The
# readings come from `--check`'s node-local history, so this never moves an exit status.
# --------------------------------------------------------------------------------------------

# DEAD_READINGS_LIMIT = 10

DEAD_FILED: dict[str, str] = {}

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

# How many lines ABOVE a ratcheted pin this gate looks for the `<old> -> <new>` justification
# that excuses a weakening move. Absent takes the kit's shipped 14. Widen it if your repo writes
# long justifications above a pin; narrow it if your pins sit close together, so a justification
# for a DIFFERENT pin cannot be read as this one's.
# RATCHET_LOOKBACK = 14

RATCHETS: list[dict] = [
    # {"file": ".memory-tree.conf", "key": "ORPHAN_ID_PIN", "weakens": "up"},
    # {"file": "<path of this file>", "key": "cutoff_keys_armed", "weakens": "up"},
]
