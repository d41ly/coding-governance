"""drift_signals.py — coding-governance's own drift-signal declarations (dogfooding the kit).

gov:kit drift-audit@1.4

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
    # The kickoff manifest, by FILE path. `memory/` stays absent for the reason above; this one file
    # is product CONFIGURATION that moved into the tree, not a record. Naming the DIRECTORY would let
    # every spec cite its own id through the corpus and certify all of them at once.
    "memory/guides/SESSION-KICKOFF.md",
    "parallel-coding-governance.template.md",
    "parallel-coding-governance.customize.md",
    "parallel-coding-governance.domain-rules.md",
    "WIRE-INTO-PROJECT.md",
]

# --------------------------------------------------------------------------------------------
# TRACE_CUTOFF / TRACE_GLOBS — signal 6 (`closed_specs_with_no_product_commit`).
#
# The cutoff is the date THIS repo's "unit id in the commit subject" rule became binding: 2026-08-11,
# when `memory/guides/BUILD-METHOD.md` landed at a383375. It is judged against each spec's
# STATUS-HEADER date, which TEMPLATE-SPEC defines as the last-change date and which on a CLOSED spec
# is therefore the close date.
#
# It is a grandfather, not a knob to tune until the number looks good. Before that commit the subjects
# were `feat(memory-tree)!: U1 — …` and `fix(aStandingWrit): …` — the unit number or the slug, never
# the id — so 36 CLOSED specs are correctly unjudgeable. A cutoff of 2026-08-12 would read 0 misses
# instead of 1, by dropping ten specs from the population to avoid investigating three entries; that
# is the vacuous-selector class, and it is why this date is the convention's and not the tidiest.
TRACE_CUTOFF: str = "2026-08-11"

# NARROWER than PRODUCT_GLOBS, deliberately. `.claude/` and the kickoff manifest are product
# CONFIGURATION that a records or kickoff commit routinely touches, so leaving them in lets the
# house's own bookkeeping certify the bookkeeping — the exact hole the path restriction exists to
# close. Today the narrowing changes no verdict; it is taken before it costs something, not after.
TRACE_GLOBS: list[str] = [
    "tools",
    "skills",
    "parallel-coding-governance.template.md",
    "parallel-coding-governance.customize.md",
    "parallel-coding-governance.domain-rules.md",
    "WIRE-INTO-PROJECT.md",
]

# --------------------------------------------------------------------------------------------
# SHRINK_ONLY — the lists this repo promises will only ever get shorter, with the seed each was
# measured at. The previous comment here claimed "this repo ships no waiver list of its own", which
# was false when written and falser since: four such lists are live in `memory/project/`, every one
# of them load-bearing for a gate.
#
# `legacy-files.txt` is EXCLUDED, deliberately and in writing rather than by omission: it is the
# memory-tree kit's permanent grandfather list, not a debt being drained, so a shrink-only assertion
# over it would be a ratchet nobody intends to turn.
# --------------------------------------------------------------------------------------------

SHRINK_ONLY: dict[str, str] = {
    "memory/project/id-orphan-waiver.txt": "the orphan-id waiver — one row per id cited but not defined",
    "memory/project/curation-debt.txt": "files exempted from the index caps until they are curated",
    "memory/project/corpus-path-unresolved.txt": "citations that cannot legally be repaired",
    "memory/project/unarmed-branches.txt": "fail branches with no arm; empty today and meant to stay so",
}

# --------------------------------------------------------------------------------------------
# DECLARED_EMPTY — signals whose population is empty ON PURPOSE, so `--check` must not red them for
# being dead. Every other gateable signal that goes dead is a blind instrument and IS a failure.
#
# The exception exists because the SHIPPED template declares no shrink-only lists at all, so without
# it a fresh adopter reds on their first run for doing exactly what the template told them to. An
# exemption that is not enumerated is not an exemption — this list is the enumeration.
# --------------------------------------------------------------------------------------------

DECLARED_EMPTY: set[str] = {
    # The authored per-node session ledger was RETIRED by the aMendedLedger U2 unit: its three shards
    # moved to memory/archive/ledger/ and memory/project/in-flight/ no longer exists, so this
    # probe's population is empty BY DESIGN rather than blind. The kit ENGINE is untouched —
    # drift_report.py still reads <memory_root>/project/in-flight/*.md for adopters who keep a
    # ledger — and the declaration is not a muzzle: put one row back and the probe goes live and
    # scores again. selftest.py asserts both directions over one fixture.
    "ledger_rows_contradicting_git",
}

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
    # MATCHED ON THE LEG'S ARGV SCRIPT PATH, not its display name. The display name is a label
    # somebody types twice; the script path is the identifier every charter bullet already cites, and
    # it does not move when a leg is renamed. Measured at 647bfd9: by display name 11 of 37 legs read
    # as named, by script path 30 — the name predicate was over-counting in one direction (crediting
    # a self-test leg when only its gate's path is cited) and under-counting in the other (missing
    # every bullet that groups legs in prose). The real gap is 7, and every one of the 7 is a
    # self-test whose parent gate IS named — a number that drains one bullet at a time.
    total = len(legs)
    charter = (ctx.root / (ctx.charter or "AGENTS.md")).read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^##\s+The gate suite.*?$(.*?)^##\s", charter, re.M | re.S)
    section = m.group(1) if m else ""
    if not section:
        return -1, total
    mentioned = 0
    for leg in legs:
        paths = [a for a in leg.get("argv", []) if "/" in str(a)]
        if any(str(p) in section for p in paths):
            mentioned += 1
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
    # ledger_rows_contradicting_git carries NO pin. Its population is empty by declaration (above),
    # and a pin of 4 over an empty population is a ratchet that can never turn. If a ledger ever
    # returns, the default tolerance of 0 is the right bar — not a number measured against rows that
    # no longer exist.
    # Main reached the same place from the other side while this branch was building: node `a`
    # self-pruned its three landed rows and lowered the pin 4 -> 1, leaving node `b`'s single row.
    # That drain is subsumed — the shards are now frozen under `archive/ledger/` and the signal is
    # declared empty, so there is no population left for a pin of 1 to ratchet against.
    # 2 — TOOL-aBatchedLintel-1 and TOOL-aGuardedTally-1, both INPROGRESS with their ids in tracked
    # kit source. INPROGRESS means "approved, build underway", which is arguably TRUE for a
    # built-but-unmerged unit, so this is the oracle's known residual ambiguity rather than proven
    # rot. Pinned, not gated to zero, for exactly that reason — read them before lowering it.
    #
    # UNCHANGED by the glob repair, which is the point: the pre-flatten glob matched 0 files and the
    # signal read 0-of-0 DEAD; the flat glob reads 2-of-9, exactly this pin. The seed was right all
    # along and the instrument was not.
    "non_terminal_specs_cited_by_product_source": 2,
    # 7 — the number of legs in `tools/gate-legs.json` whose script path the charter's gate-suite
    # section does not cite, measured at 647bfd9. The old seed of 1 was a per-row boolean against a
    # one-row population, so `value > pin` needed 2 against a ceiling of 1 and the signal could not
    # fire at all. Its comment claimed "7 of 19" against a manifest that holds 37.
    #
    # DRAINED to 0: all seven were SELF-TESTS whose parent gate was cited but whose own script
    # path was not; the charter now names them in one bullet, so every leg on the bar is spelled there.
    "handkept_inventories_disagreeing_with_source": 0,
    # 1 — TOOL-aMooredAnchor-1, the oracle's known residual. Its build commits are 59b4710 and its
    # siblings, whose subjects name neither its id nor its slug: it closed on 2026-08-11, hours after
    # the convention it is judged by landed the same day. Read it before lowering this pin.
    #
    # SEEDED AT 1, NOT 0, and the difference is the whole reason the pin is trustworthy. Counting
    # merge commits this signal reads 0 — but the only commits naming aMooredAnchor are two reconcile
    # merges whose subjects name the branch merged INTO, carrying another build's work. A 0 measured
    # that way is a number, not a measurement.
    "closed_specs_with_no_product_commit": 1,
    # 3 — MEASURED on the day the table was ratified, and non-zero BY CONSTRUCTION rather than as
    # tolerated rot. `--scaffold` derives the verb table by leading-token frequency and a human then
    # curates it, and curation ADDS aspirational verbs the corpus does not use yet: `measure`, `print`
    # and `set` are declared because that is what this repo should call those operations, not because
    # anything is already called that. Reading this 3 as debt inverts what it records.
    #
    # It is the DELETION direction that earns the signal: a verb outliving the code that justified it
    # is the one thing neither the map ratchet nor the lexicon gate can see. Lower the pin when a verb
    # genuinely comes into use — never raise it to admit a new aspirational one without saying which.
    "lexicon_verbs_declared_but_unused": 3,
    # 0, and it can move: the stamp is a date and the language surface is a commit date, so adding a
    # LANGS entry without re-ratifying turns this to 1 the same day.
    # 81 — the live (non-terminal) row count of the LARGEST backlog shard, measured 2026-08-18 on
    # memory/backlog/TOOL.md. TOOL-aRelaxedShard-4.
    #
    # This is a WATERMARK, not a ceiling, and the signal is `gateable: False` so crossing it never
    # blocks a merge. What it buys is that RAISING it lands in RATCHETS below and therefore needs a
    # reason written in place — which is the whole point: this repo hit a spent budget twice in one
    # session because the number nobody was tracking moved without anyone deciding it should.
    #
    # Do not turn this gateable without also declaring it in the shipped conf template. A signal
    # absent from an adopter's PINS falls back to tolerance 0, so a gateable version reds their first
    # `--check` on one open row.
    # 81 -> 89. RAISED at the reground onto main, and by the signal doing its job on its first real
    # merge: two branches' live rows united, and neither side was over its own watermark. Same shape
    # as READ_PATH_CEILING in this same reconcile, one budget over.
    "live_backlog_rows_per_shard": 89,
    "lexicon_ratified_older_than_language_surface": 0,
}

# --------------------------------------------------------------------------------------------
# RATCHETS — the shrink-only NUMBERS whose weakening direction must be justified in place.
#
# TOOL-aNumeralWarden-3: every gate that owns one of these compares only `value > pin`, so RAISING
# the pin and DRAINING the population look identical from the outside. `ORPHAN_ID_PIN` 4 -> 5 and
# `handkept` 1 -> 7 both landed unchallenged that way.
#
# The fix reads a marker that was ALREADY being written by hand. `.memory-tree.conf` says, in prose,
# "RAISED 2 -> 3 at the merge with main, and this is a RAISE, not a drain — the distinction the
# drift-audit backlog row warns is invisible to every gate." The convention existed; nothing read it.
# So a weakening move now REQUIRES a nearby comment naming both numbers in `<old> -> <new>` form,
# and the marker goes stale visibly because it spells the values.
#
# `weakens` is the direction that makes the guarantee WEAKER, and it differs by kind: a pin, ceiling
# or budget weakens UPWARD, a floor weakens DOWNWARD. Getting that backwards would make the guard
# refuse every legitimate ratchet and wave through every regression, so it is declared per entry
# rather than inferred from the name.
#
# SCALARS ONLY, stated rather than implied. The compound floors — `ARMS_FLOORS` and `CORE_FLOOR`,
# both `<name>:<n>:<n>` sets — are NOT covered here: they need a per-member diff, which is a
# different parse and a different message. They keep their own gates' one-sided checks. Naming the
# gap is the point; a guard whose coverage is guessed at is the class this repo keeps finding.
# How many lines ABOVE a ratcheted pin this gate looks for the `<old> -> <new>` justification
# that excuses a weakening move. Absent takes the kit's shipped 14. Widen it if your repo writes
# long justifications above a pin; narrow it if your pins sit close together, so a justification
# for a DIFFERENT pin cannot be read as this one's.
# Declared explicitly at the shipped value, so the example an adopter copies is a LIVE one and the
# key is discoverable from this file rather than only from the kit's default.
RATCHET_LOOKBACK = 14

RATCHETS: list[dict] = [
    {"file": ".memory-tree.conf", "key": "ORPHAN_ID_PIN", "weakens": "up"},
    {"file": ".memory-tree.conf", "key": "DEAD_PATH_PIN", "weakens": "up"},
    {"file": ".memory-tree.conf", "key": "READ_PATH_CEILING", "weakens": "up"},
    {"file": ".memory-tree.conf", "key": "UNIVERSAL_BUDGET", "weakens": "up"},
    {"file": ".memory-tree.conf", "key": "ROW_DUPLICATE_PIN", "weakens": "up"},
    {"file": "tools/drift-audit/drift_signals.py",
     "key": "non_terminal_specs_cited_by_product_source", "weakens": "up"},
    {"file": "tools/drift-audit/drift_signals.py",
     "key": "handkept_inventories_disagreeing_with_source", "weakens": "up"},
    {"file": "tools/drift-audit/drift_signals.py",
     "key": "live_backlog_rows_per_shard", "weakens": "up"},
]

CHARTER = "AGENTS.md"
