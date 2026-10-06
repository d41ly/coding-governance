"""drift_signals.py — coding-governance's own drift-signal declarations (dogfooding the kit).

gov:kit drift-audit@1.24

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
TRACE_GLOBS: list[str] = [
    _TOOLS,
    "skills",
    "coding-governance-agents.template.md",
    "WIRE-INTO-PROJECT.md",
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
]

# --------------------------------------------------------------------------------------------
# SHRINK_ONLY — the lists this repo promises will only ever get shorter, with the seed each was
# measured at. The previous comment here claimed "this repo ships no waiver list of its own", which
# was false when written and falser since: the lists below are live in `memory/project/`, every one
# of them load-bearing for a gate. TOOL-aScouredKit-8 removed a count from this sentence — it said
# "four" against a table of five, and it was wrong by the same act that added a row. The population
# is the table underneath, and the signal derives and prints its own `of`.
#
# `legacy-files.txt` is EXCLUDED, deliberately and in writing rather than by omission: it is the
# memory-tree kit's permanent grandfather list, not a debt being drained, so a shrink-only assertion
# over it would be a ratchet nobody intends to turn.
# --------------------------------------------------------------------------------------------

SHRINK_ONLY: dict[str, str] = {
    "memory/project/id-orphan-waiver.txt": "the orphan-id waiver — one row per id cited but not defined",
    "memory/project/curation-debt.txt": "files exempted from the index caps until they are curated",
    "memory/project/corpus-path-unresolved.txt": "citations that cannot legally be repaired",
    # No cardinality in this gloss. It said "empty today and meant to stay so" while the row beside
    # it printed `entries 3`, so an operator reading the JSON was told the opposite of the derived
    # value standing next to it (TOOL-aScouredKit-8).
    "memory/project/unarmed-branches.txt": "fail branches with no arm; drains as each is armed",
    "memory/project/trace-waiver.txt": "CLOSED specs no TRACE_GLOBS subject can name — signal 6's exemption",
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
    # 19 — MEASURED, and re-measured after round 7 corrected the instrument. The first seed was 31
    # through a skewed one: the blame side read `author-time` as UTC while the spec side is a
    # hand-typed LOCAL date, so 11 rows were pure +0300 artifacts, and one line naming a token twice
    # was counted twice. A pin seeded through a broken instrument makes the later fix read as an
    # improvement, which is why this says so. 19 rows over 7 of 61 build READMEs. Report-only, so it
    # never blocks a merge; it is here so a non-zero count does not read "out of tolerance" from day
    # one. Drain it: each row is one README sentence to re-read against the spec revision beside it.
    #
    # 19 -> 4, a DRAIN by narrowing, not by re-reading (TOOL-aMendedFleet-51). The signal now grades
    # only builds with at least one non-terminal spec: 27 of the 31 rows it read at that unit's base
    # sat in builds whose every spec is CLOSED or WONTDO, frozen records nobody acts on. Re-measured
    # at that unit's commit: 4 rows over 19 live-build READMEs, in dScaffoldedMirror and
    # dScriptedRepeat.
    "readme_mechanism_drift": 4,
    # 7 — the number of legs in `<prefix>/gate-legs.json` whose script path the charter's gate-suite
    # section does not cite, measured at 647bfd9. The old seed of 1 was a per-row boolean against a
    # one-row population, so `value > pin` needed 2 against a ceiling of 1 and the signal could not
    # fire at all. Its comment claimed "7 of 19" against a manifest that holds 37.
    #
    # DRAINED to 0: all seven were SELF-TESTS whose parent gate was cited but whose own script
    # path was not; the charter now names them in one bullet, so every leg on the bar is spelled there.
    #
    # RE-ARMED at 0 over a different population (TOOL-aMendedFleet-52): the charter row is retired,
    # and the pin now holds the README signal table's names to the names the engine reports, which
    # agreed on the arming commit. The figures above describe the retired charter row.
    "handkept_inventories_disagreeing_with_source": 0,
    # `backlog_rows_outliving_closed_specs` and its pin RETIRED together at the backlog switch-over
    # (TOOL-dDerivedDocket-34 S10): no backlog status is authored once BACKLOG_MODE is builds, so a
    # row token compared with its spec's status has nothing left to read. The stance it counted is
    # superseded in `memory/DECISIONS.md` under that unit's id.
    # DRAINED to 0 at TOOL-aMendedFleet-47. It was seeded at 3 for the aspirational verbs curation
    # declared before any definition led with them; every one of them is in use now, and the signal
    # reads 0 of the declared table. GATEABLE, so a NEW aspirational verb reds `--check` until a
    # definition uses it, which is the intended price of declaring one.
    #
    # It is the DELETION direction that earns the signal: a verb outliving the code that justified it
    # is the one thing neither the map ratchet nor the lexicon gate can see. Raising this pin to admit
    # an aspirational verb is the RATCHETS row below, which needs the move written here with a reason.
    "lexicon_verbs_declared_but_unused": 0,
    # 0, and it can move: the stamp is a date and the language surface is a commit date, so adding a
    # LANGS entry without re-ratifying turns this to 1 the same day.
    # MEASURED at the unit that added the signal, on this corpus, and expected to be small: the
    # slug discriminator drops every fixture id with no waiver list at all, so what remains is
    # actionable rather than tolerated. A drain target from the first commit, which is why it is
    # shrink-only rather than a tolerance — and shrink-only means the RATCHETS row below, not
    # this sentence.
    # 2 - MEASURED on this corpus at the unit that added the signal. NO POPULATION FIGURES HERE,
    # and that is the correction rather than an omission: an earlier revision stated the cited-id
    # count and it was wrong at the very commit that wrote it, because the count moves whenever a
    # record or a source file does. The signal derives and PRINTS its own `of`, `known_slugs` and
    # `scanned_source_files` on every run; read them there. Both
    # survivors belong to one foreign build whose records were minted and never written, and
    # both are already filed as a backlog row. Every other dangling citation in the tree is a
    # fixture id under a slug no record anchors, and the discriminator drops all of them with
    # NO waiver list - which is the property that makes this population drainable rather than
    # decorative. A drain target from the first commit.
    "source_cited_ids_resolving_to_no_record": 2,
    "lexicon_ratified_older_than_language_surface": 0,
    # MEASURED at the unit that added the signal, TOOL-dLoggedFlight-13, against local `main`.
    # Report-only, and it carries NO RATCHETS row on purpose: a sanctioned worktree landing raises
    # this count through nobody's fault, so a raise needs no reason and holding the pin proves
    # nothing. What the pin buys is the status column, which reads `ok` at the measured value and
    # `over pin` once it rises. The records are not named here, for the reason the non-terminal-specs
    # pin above gives: read the signal's own `detail`.
    # RE-SEEDED at the drained value by TOOL-aMendedFleet-47, which stopped counting a `LANDING`
    # record whose landing commit is on the base ref (owner ruling D12-i2, derived LANDED). What
    # remains is non-`LANDING` records only; the detail's summary line counts the derived ones.
    "run_records_nonterminal_but_merged": 2,
    # MEASURED at the unit that added the signal, TOOL-dUnstuckLanding-15, against origin/main: live
    # LEGACY ABORTED records whose work the content predicate reads landed and which carry no upheld
    # `work-landed-at`. Report-only with no RATCHETS row, for the reason the pin above gives; it drains
    # by `--settle` on each listed slug and a commit of what that staged, and is lowered as it does.
    # Its sibling `discarded_work_landed` carries no pin: no ABORTED record here is dated on or after
    # HANDOFF_CUTOFF yet, so it reads DEAD, and a pin over a population that does not exist is a guess.
    # Drained 8 -> 0 by `--settle` on all eight slugs (aec85436), 2026-10-05.
    "aborted_work_landed": 0,
    # MEASURED at TOOL-aMendedFleet-15, after the prior unit's five dispositions. It stands in
    # for check 20's `SEVERITY_UNLABELLED_PIN`, which the backlog switch-over blanked because the
    # shard census reads a generated view as zero rows; this signal shipped with no pin, so it read
    # `over pin 0` on every run and a rise moved no number anybody was held to.
    # The population can only FALL on its own: V12 refuses an ask filed on or after ASK_CUTOFF with
    # no SEV row, so a new unlabelled ask arrives only as a pre-cutoff row relocated from a stale
    # branch, or as a terminal ask a REOPEN revives. Report-only, like its sibling above; the
    # RATCHETS row below is what makes a raise cost a written `<old> -> <new>` reason.
    "backlog_asks_unlabelled": 447,
    # MEASURED at TOOL-aMendedFleet-21, which added the signal: every armed `_CUTOFF` key across the
    # tracked root confs. GATEABLE, so a change that arms a new key reds `drift-audit records` unless
    # another key stops being armed in the same change. Raising it instead is the RATCHETS row below,
    # which needs the old and new values written here. The keys are not named: read the detail.
    # 29 -> 30 at the reconcile of aMendedFleet with origin/main, 2026-10-06: main's dThriftyLanding
    # handoff verb arrived with its own armed cutoff in .unattended.conf, and no key stopped being armed.
    "cutoff_keys_armed": 30,
    # 26 - MEASURED at TOOL-aMendedFleet-37, which added the signal, at its own commit: 26 of 27
    # feature dossiers older than their paths, every one but the codebase-map dossier that unit
    # refreshed. Report-only; the pin is a declared DRAIN, one dossier re-read at a time, and the
    # RATCHETS row below makes a raise cost a written `<old> -> <new>` reason. The dossiers are not
    # named here: read the signal's own detail, which derives them most-behind first.
    "dossiers_older_than_their_paths": 26,
}

# --------------------------------------------------------------------------------------------
# BASELINES — the gateable signals bounded by WHICH offenders they hold rather than how many
# (TOOL-aMendedFleet-56). A pin bounds a count, so a drained offender and a new one at an equal count
# read as no change; here a new id reds, a listed id that no longer offends reds until its line is
# deleted, and the set may never gain an id against the base. There is no escape: each signal below
# has a remedy that is not an addition. Delete an id the moment `--check` names it stale.
# Moving a signal out of this dict into PINS is graded too (TOOL-aMendedFleet-110): it may be pinned
# no higher than the size of the set the base held, so a move cannot buy headroom.
#
# Seeded with the offenders the BASE measured, never with ones that arrived on a branch: those red
# as `new`, naming their id, until their cause is removed.
# --------------------------------------------------------------------------------------------

BASELINES: dict[str, list[str]] = {
    # THE IDS ARE SPELLED HERE NOW, and that needed an engine change rather than a comment. This
    # file sits inside EVIDENCE_GLOBS, so spelling an id here used to make it cite itself: measured,
    # this file was returned in the citation set for both pinned ids, and the old pin could not be
    # drained by removing the annotations describing it. The engine now excludes the project layer
    # from signal 2's evidence, so a listed id drains when its real citations do.
    #
    # WHAT THE RESIDUAL IS, which is the part worth keeping: both are INPROGRESS with their ids in
    # tracked kit source, and INPROGRESS means "approved, build underway" — arguably TRUE of a
    # built-but-unmerged unit. So this is the oracle's known ambiguity rather than proven rot.
    # Listed rather than gated to zero for exactly that reason; read the detail before deleting one.
    #
    # RE-MEASURED at the unit that took the shipped id grammar and narrowed this signal's globs off
    # test files. The value did not move, and that is the expected result rather than a failed
    # change: both ids keep non-test product citations that neither the grammar swap nor the
    # narrowing touches. What DID move is the judgeable population, upward, because the shipped
    # grammar matches correction-form ids that the old hand-typed one silently declined to judge.
    "non_terminal_specs_cited_by_product_source": [
        "TOOL-aBatchedLintel-1",
        "TOOL-dNarrowedAnchor-1",
    ],
    # The oracle's known residual. Its build commits are 59b4710 and its siblings, whose subjects
    # name neither its id nor its slug: it closed on 2026-08-11, hours after the convention it is
    # judged by landed the same day. Read it before deleting it.
    #
    # LISTED, NOT ZERO, and the difference is the whole reason the bound is trustworthy. Counting
    # merge commits this signal reads 0 — but the only commits naming its slug are two reconcile
    # merges whose subjects name the branch merged INTO, carrying another build's work. A 0 measured
    # that way is a number, not a measurement.
    "closed_specs_with_no_product_commit": [
        "TOOL-aMooredAnchor-1",
    ],
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

# ONE SPELLING OF THIS FILE'S OWN PATH, not one per row. Every ratchet row below that names this
# module used to carry the literal again, so adding a row RAISED the carried-literal count and
# tripped the ban on a kit file spelling paths. The rows need a repo-relative path because the
# reader resolves it against the repo root, so this is the narrowest honest form: one name, used
# by every row that names this module, and adding another row costs nothing.
#
# DERIVED from this file's own location (TOOL-aRepatriatedFork-29 S6); see `_TOOLS` at the top.
_THIS_FILE = _HERE.relative_to(_CHECKOUT).as_posix()

RATCHETS: list[dict] = [
    {"file": ".memory-tree.conf", "key": "ORPHAN_ID_PIN", "weakens": "up"},
    {"file": ".memory-tree.conf", "key": "DEAD_PATH_PIN", "weakens": "up"},
    {"file": ".memory-tree.conf", "key": "UNIVERSAL_BUDGET", "weakens": "up"},
    {"file": ".memory-tree.conf", "key": "ROW_DUPLICATE_PIN", "weakens": "up"},
    {"file": _THIS_FILE,
     "key": "handkept_inventories_disagreeing_with_source", "weakens": "up"},
    # The signal is report-only, so crossing this pin never blocks a merge. What the row buys is
    # that RAISING it needs a reason written in place — which is the whole of "shrink-only" for
    # an ungateable pin, and without it the word is a comment.
    {"file": _THIS_FILE,
     "key": "source_cited_ids_resolving_to_no_record", "weakens": "up"},
    {"file": _THIS_FILE, "key": "backlog_asks_unlabelled", "weakens": "up"},
    {"file": _THIS_FILE, "key": "cutoff_keys_armed", "weakens": "up"},
    {"file": _THIS_FILE, "key": "dossiers_older_than_their_paths", "weakens": "up"},
    # Gateable at 0: without this row, raising it to admit a new aspirational verb would look like
    # a drain to `--check` (TOOL-aNumeralWarden-3).
    {"file": _THIS_FILE, "key": "lexicon_verbs_declared_but_unused", "weakens": "up"},
    # A pin in ANOTHER kit's conf. The ratchet does not care which file a scalar lives in, and
    # codebase-map has no shrink-only mechanism of its own - so an adopter without drift-audit
    # gets a declared pin and no enforcement, which the conf example states rather than hides.
    {"file": ".codebase-map.conf", "key": "DOSSIER_DECISIONS_EMPTY_PIN", "weakens": "up"},
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
