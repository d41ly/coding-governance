"""drift_signals.py — coding-governance's own drift-signal declarations (dogfooding the kit).

gov:kit drift-audit@1.36

Copied from drift_signals.template.py and filled for THIS repo. The corpus root and disciplines are
NOT restated here — they come from `.memory-tree.conf`, which the memory-tree kit owns.
"""

from __future__ import annotations

import json
import pathlib
import re

# THE TOOL ROOT, DERIVED (TOOL-aRepatriatedFork-29 S6): this file sits in `<tool root>/<kit>/`, and the
# checkout root is the first directory above it holding a `.git` entry. Both globs below name the
# kits through it, so gov's product is graded at whatever kit root it was checked out under.
_HERE = pathlib.Path(__file__).resolve()
_CHECKOUT = next((_p for _p in _HERE.parents if (_p / ".git").exists()), _HERE.parents[2])
_TOOLS = _HERE.parent.parent.relative_to(_CHECKOUT).as_posix()

# --------------------------------------------------------------------------------------------
# PRODUCT_GLOBS — this repo's "product" is its kits, its skill engine and the playbook template.
# `memory/` is deliberately absent: keying a record's truth on another record is circular, and an id
# catalog inside the corpus would certify every spec at once.
# --------------------------------------------------------------------------------------------

PRODUCT_GLOBS: list[str] = [
    _TOOLS,
    "skills",
    ".claude",
    # The kickoff manifest, by FILE path. `memory/` stays absent for the reason above; this one file
    # is product CONFIGURATION that moved into the tree, not a record. Naming the DIRECTORY would let
    # every spec cite its own id through the corpus and certify all of them at once.
    "memory/guides/SESSION-KICKOFF.md",
    "coding-governance-agents.template.md",
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
# The residual it trades in is LIVE as of 2026-08-20 and has a home: closing a spec whose product
# landed BEFORE this date advances its header past the cutoff and reds it for want of a convention it
# never had. That is not fixed by moving this date or by raising the pin — both were weighed and
# refused, the first because a filename key exempts every in-flight spec forever and the second
# because cTracedPromise-1 §3 rules it out in writing. The remedy is a row in
# `memory/project/trace-waiver.txt`, which now exists and carries the first five.
#
# A RECORDS-ONLY unit (a journal, an evaluation, a census) does NOT take a waiver row: it declares
# `records-only` as a field of its own status header when it is specced (TOOL-aMendedFleet-91), and
# the signal sets it aside before the slug join. The waiver keeps the other shape, a unit whose
# product landed before the id-in-subject convention.
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
# close. It is taken before it changes a verdict, not after one.
#
# AND ONE PATH WIDER than the kit paths: `help`. It holds the user-facing pages the `docs` leg
# grades, and the charter's [docs] rule makes a current page part of a user-facing change, so a
# pass that writes one has shipped product. Without it a unit whose whole product is a help page
# read as an offender: TOOL-dCountedConsumers-1, whose pass commit touched `help/policy.md` and
# its own records and nothing above. No records commit touches `help/`. Measured 2026-11-02, every
# commit that does is a build, tool, docs or playbook pass.
#
# NOT ADDED TO PRODUCT_GLOBS, and that is a scope line, not a verdict on the pages. PRODUCT_GLOBS
# also feeds signal 2, through EVIDENCE_GLOBS below, and the escape ratio. A help page that names a
# unit id would then cite that unit as shipped, and neither reading was measured with `help` in it.
TRACE_GLOBS: list[str] = [
    _TOOLS,
    "skills",
    "coding-governance-agents.template.md",
    "WIRE-INTO-PROJECT.md",
    "help",
]


# --------------------------------------------------------------------------------------------
# EVIDENCE_GLOBS — signal 2 (`non_terminal_specs_cited_by_product_source`).
#
# NARROWER than PRODUCT_GLOBS, and for the reason written beside TRACE_GLOBS above: a citation from
# a test file is the house's own bookkeeping certifying the bookkeeping. Signal 2 asks whether a
# non-terminal spec describes work that demonstrably SHIPPED, and a fixture id inside a `.test.sh`
# is evidence of a test, not of a shipment.
#
# Declared as its own list rather than by editing PRODUCT_GLOBS, which other signals read and which
# this unit has not measured them against. That is the same precedent TRACE_GLOBS set: a second
# declaration for one signal, taken before it costs something rather than after.
# DERIVED from PRODUCT_GLOBS rather than retyped beside it. The first spelling of this list
# repeated all six product paths and then subtracted; that is a second copy of one declaration
# in one file, which drifts the first time either moves, and it put two more kit-path literals
# into a shipped file that bans them. The narrowing is now only the SUBTRACTION, which is all
# this signal actually declares.
EVIDENCE_GLOBS: list[str] = PRODUCT_GLOBS + [
    ":(exclude)*.test.sh",
    ":(exclude)*/selftest.py",
    ":(exclude)*/test_*.py",
    # FIXTURE ANYTHING, in ONE predicate. An earlier revision answered the three test-file
    # spellings above with four more literal spellings of "a fixture", which is the same
    # gate-the-instance shape one level along. A substring match over the path covers every fixture
    # spelling the tree uses now and every one it grows later.
    ":(exclude)*fixture*",
    # AND THE TEMPLATE SHAPE, which the collapse dropped and nothing else covers: a `.test-template`
    # file is a test that is not named `fixture` and not named `.test.sh`. Losing it re-admitted one
    # file to this population under a comment claiming the single predicate covered everything —
    # a collapse that generalises three cases and silently loses a fourth. Both lines together are
    # 175 files; the predicate alone was 176. Measured at the commit that restored this.
    ":(exclude)*.test-template.*",
    # THE SIZE REGISTRIES. The template-size gate keys its ceiling and high-water rows by FILE PATH,
    # and a live spec is one of the subjects it measures, so a row names the spec's path without
    # claiming any of its work shipped. Admitted, a size row is a citation of every spec it holds.
    ":(exclude)*template-size-*.txt",
    # THE UNSCANNED-READERS LIST, for the size registries' reason. Policy reader coverage keys each
    # row by the tracked FILE PATH where a key's value is consumed, and a record's file name carries
    # its unit id, so a row names that id without claiming any of its work shipped.
    ":(exclude)*/unscanned-readers.txt",
    # THE RECORD-KIND REGISTRY, for the size registries' reason (TOOL-dTotalRecall-16). Each row's purpose
    # cites the design record it was read from by FILE PATH, and a record's file name carries its
    # unit id, so a purpose names that id without claiming any of its work shipped.
    ":(exclude)*/record-kinds.toml",
]

# --------------------------------------------------------------------------------------------
# THE LISTS THAT PROMISE TO SHRINK are no longer typed here (TOOL-dWitnessedBar-16 S8): they are the
# `shrink-only` `[[ledger]]` registrations, read through the memory-tree kit's ledger factory, each
# glossed by its population name, so a converted list joins the signal by being registered.
# --------------------------------------------------------------------------------------------

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
    # `handkept_inventories_disagreeing_with_source` left this set when HANDKEPT gained the README
    # signal-table row below (TOOL-aMendedFleet-52 S4): its population is live again.
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
    # The manifest sits in the tool root, this file's grandparent (TOOL-aRepatriatedFork-29 S6).
    legs = json.loads((pathlib.Path(__file__).resolve().parent.parent / "gate-legs.json")
                      .read_text(encoding="utf-8"))
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


# RETIRED 2026-08-18, ahead of the change that makes it necessary. The charter's gate-suite section
# is deleted against an admission test, so the charter stops CLAIMING to name every leg and there is
# nothing left to disagree with the source.
# The retirement lands here rather than there because three units in between each ADD a gate leg,
# and this signal is gateable at a drained pin of 0 — each of them would red `drift-audit records`
# with no unit owning the fix. Between here and the cut the charter still names every pre-existing
# leg, so retiring it early costs nothing.
#
# The probe function above is deliberately left defined and unreferenced: it is the record of what
# was being asked, and re-arming it is a one-line change if the charter ever re-enumerates.


def read_signal_table_names(ctx) -> tuple[set[str], set[str]]:
    """The README's signal-table names against the names the engine reported, as SETS.

    Only the table under `## The signals`, up to the next heading of ANY level: the harness-note
    table under a `### ` subheading of that same section lists the states `clean`, `partial` and
    `dead`, and a read to the next `## ` heading counts them as three extra signals. No heading reads as an empty claim set, so every engine name is
    `missing` rather than the comparison passing. `ctx.signal_names` is set by the engine's `main`
    before this runs; a caller that never sets it raises, which the signal reports as an error row.
    """
    text = (_HERE.parent / "README.md").read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^## The signals[^\n]*\n(.*?)(?=^#+ |\Z)", text, re.M | re.S)
    claims = set(re.findall(r"^\|\s*`([^`]+)`\s*\|", m.group(1), re.M)) if m else set()
    return claims, set(ctx.signal_names)


# THE README'S SIGNAL TABLE (TOOL-aMendedFleet-52): its first-column names, compared as a set with
# the names the engine reports, so a signal added without a README row, or a row its deleted signal
# left behind, counts one each — named under `missing` or `extra` in the detail.
HANDKEPT: list[dict] = [
    {"record": "drift-audit README `## The signals` table", "source": "the engine's reported signal names",
     "probe": read_signal_table_names},
]

# --------------------------------------------------------------------------------------------
# THE PINS are the rows of the `ceiling` population `drift-pins` (TOOL-dWitnessedBar-16 S8), its home
# `memory/project/drift-pins.txt`: one row per signal, its count the pin, seeded at MEASURED
# values and never guessed. A pin of 0 is no row, so the signal keeps its own tolerance of 0. A
# raise is the `ratchet` pack's widen, which costs a widen record and its reason; each pin's
# history, written here until this unit, is the conversion record's.
# --------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------
# THE BASELINES are the rows of the `shrink-only` population `drift-baselines` (TOOL-dWitnessedBar-16
# S8), its home `memory/project/drift-baselines.txt`: one row per (signal, offender id), the
# gateable signals bounded by WHICH offenders they hold rather than how many (TOOL-aMendedFleet-56).
# A new id reds, a listed id that no longer offends reds until its row is deleted, and the set may
# never gain an id against the base; a signal moved to `drift-pins` is pinned no higher than the
# set the base held (TOOL-aMendedFleet-110).
# --------------------------------------------------------------------------------------------

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
    {"file": ".memory-tree.conf", "key": "UNIVERSAL_BUDGET", "weakens": "up"},
    # The six rows naming this layer's own pins retired with its `PINS` dict (TOOL-dWitnessedBar-16 S8),
    # and the four naming conf pins with their keys (TOOL-dWitnessedBar-17 S5): each is a keyed
    # population now, and its growth is the `ratchet` pack's `never gains` case, which costs a widen
    # record and its reason where these rows cost an `<old> -> <new>` comment. A budget is no pin.
]

CHARTER = "AGENTS.md"

# The auto-memory directory `dangling_pointers_in_own_ledger` audits (TOOL-aMendedFleet-53): `~` is
# the home directory and `{checkout}` the primary checkout's Claude Code project key, so every node
# and every worktree reads its own machine's notes. Report-only, and a node with no such directory
# reads DEAD PROBE rather than a clean 0.
AUTO_MEMORY_DIR = "~/.claude/projects/{checkout}/memory"

# The remote CI workflow `remote_ci_red_streak` reads through `gh` (TOOL-aMendedFleet-8). Report-only
# and NOT ASKED under --check, so the merge bar stays offline; no pin, so any red streak reads over.
REMOTE_CI_WORKFLOW = "remote-ci.yml"
