#!/usr/bin/env python3
"""build_records.py — the typed build-folder record factory (PLAY-dOrderedCharter-7 S7, S8).

Extracted from `deviation_join.py` at its second instance, the exception kind. A typed record is one file,
`<MEMORY_ROOT>/builds/<build>/build/<date>-build-<unit id>-<kind>-<n>.md`, `<n>` unique within its build and
kind, its id the file's stem. Its fields are bold-key bullets, `- **Key:** value`, read with `FIELD`, the one
field grammar of this kit. Each kind in `KINDS` names its required fields and its closed sets;
`read_record` refuses a field given twice, a required field missing, a value outside its closed set, a
`Caused-by` that is not one id and a file name outside the grammar, naming each, and returns the fields
whatever it found. `read_records` reads a kind's TRACKED population, the one `design_lib.read_tracked_builds`
lists, and names two files of one build sharing one `<n>`. A kind's own rules ride in as hooks: the
deviation kind's `**After:**` pipe, `DEPARTS`, `FOLLOW` and `**Supersedes:**` stay in `deviation_join.py`.

THE EXCEPTION KIND and its stand-in door (S8): `build_records.py new exception --build <slug> --unit <id>
--principle <tag> --excuses <part> --reason <text> [--expires <YYYY-MM-DD>]` writes the next
`<date>-build-<unit id>-exception-<n>.md` in that build's `build/` folder of the session's own tree, its
`**Serves:** exception <unit id>`, for the session's own commit. It is the door the memory plan lists until
dTotalRecall's record door adopts it. The core gates read the register (`core.py exceptions`).

THE CHANGE KIND and its stand-in door (PLAY-dOrderedCharter-15 S7, S14): `write_change` is the one writer of a
record of an instruction unit's change, `read_changes` the register, by date, build and `<n>`, since a unit's
status is its last record. Its two callers are `instructions_edit.py` and `build_records.py new change --build
<slug> --unit <id> --tag <unit tag> --action <verb> --mark <mark> --before <pin> --after <pin> [--successor
<tag[,tag]>] [--promoted-from <source>]`, the door a build's builder records a kit manifest change through
while that command refuses every write. A pin is `none` or `<tag>@<hash8>`. `--tag` fills `Unit`, `--unit` names
the file and fills `Caused-by`, and `Proof` reads `DOOR_PROOF`, no flag, so no caller of the door claims a proof.
Two builds' same-day records of one tag order by slug, the read's known ceiling.

THE OVERRIDE KIND and its stand-in door (PLAY-dOrderedCharter-2 S4): `build_records.py new override --build
<slug> --unit <id> --rule <tag> --words <text> --session <id>` writes the next
`<date>-build-<unit id>-override-<n>.md`, a record of the owner setting a charter rule aside in so many words,
its fields `Rule` (the tag set aside), `Words` (the owner's words, verbatim), `Session`, `Value` (the
`charter.override` value it was taken under, read at the tree's landed revision through the policy kit's
`policy.py get`) and `Caused-by`. It refuses, exit 1 and writing nothing, under `absolute`, where no override
is taken, with any field empty, where no policy kit answers the key, and where `--rule` names no tag of the
playbook kit's practice catalogue, a practice or its `<practice>.<rule>`. It is a door the memory plan lists
until dTotalRecall's record door adopts it.

THE RED-FIX KIND, its door and its join (TOOL-aNimbleMend-9): `build_records.py new red-fix --build <slug>
--unit <id> --leg <leg name> --red-line <line> --commit <rev> --rerun <command · result>` writes the next
`<date>-build-<unit id>-red-fix-<n>.md`, the record of an inline red fix, after the fix: `Leg`, `Red line`,
`Files` and `Commit` (both derived from the commit, the sha in full), `Rerun` and `Caused-by`. It refuses,
exit 1 and writing nothing, a rev naming no commit reachable from HEAD, a commit carrying no `Red-fix:`
trailer or none naming `--leg`, and an empty text flag. `build_records.py join red-fix [--staged] [--root
<path>]` joins every `Red-fix:` commit reachable from HEAD to its record both ways, findings J1 to J6 of
`check_red_fix_join`: exit 0 clean, 1 on a finding, 2 where git or the tracked population cannot be read,
its last line a summary. A fix at HEAD with no record is printed as owed, since its record is the next
commit; `--staged` grades HEAD alone and refuses that same fix, so the commit after a fix is its record's.
A PATH-LESS trailer commit, an empty commit or any merge, whose paths the join's one log pass reads empty,
owes no record (TOOL-aClearedLedger-9): the door refuses it saying so, and the join holds it out of the fix
count, prints one `path-less` line per trailer value and counts such commits last on the summary.
NOT CHECKED: that the record is the fix's direct child, that `Rerun` or `Red line` is true, that the leg
was red, or whether a merge's resolution changed a file. `--fixture --plant red-fix-join` stages the door's
refusals, the path-less cases and each finding.

THE DISPOSITION KIND and its stand-in door (TOOL-dDeclaredLoop-16 S4): `build_records.py new disposition
--build <slug> --unit <id> --item <tag> --disposition <word> --channel <channel> [--reason <text>]` writes the
next `<date>-build-<unit id>-disposition-<n>.md`, the owner's disposition of one loop item: `Item` (a tag
opening `item.`), `Disposition` (one word), `Channel` (`mailbox`, `terminal` or `prompt`, where the owner
answered), an optional `Reason` and `Caused-by`. It refuses, exit 1 and writing nothing, an `--item` that is no
such tag, a `--disposition` that is not one word, a `--channel` outside the closed set and an empty
`--reason`. It is the door every channel calls until a mailbox or a prompt writer adopts it. NOT CHECKED
here: that the word is a member of the item's closed outcome set, which is the loop kit's
`check_disposition_record`, since a kit imports no sibling; and that the item is declared.

THE ACCEPTANCE KIND (TOOL-dDeclaredLoop-17 S1): `<date>-build-<unit id>-acceptance-<n>.md`, a unit's
acceptance commands re-run at one commit: `Sha` (the full commit the re-run read), `Writer` (`executor` or
`stand-in`) and `Caused-by`, then one `run · <exit> · <hash12> · <command>` line per command, `RUN_LINE`.
`write_acceptance` is its one writer and `read_acceptance` its reader, which refuses a `Sha` that is not 40
hex, no run line, and a line opening `run ·` outside the grammar. It has no `new` door, so no flag types a
run line: the loop kit's re-run stand-in, `loop_witness.py acceptance`, computes them and calls the writer.

THE TRANSITION KIND (TOOL-dDeclaredLoop-3 S2): `<date>-build-<anchor id>-transition-<n>.md`, one build stage
move, the anchor the lowest unit id a spec H1 under the build defines: `Build`, `From`, `To`, `Item` and `Sha`,
then any extension field the move carries. `read_transition` is its reader, which refuses a `Sha` that is not
eight to forty hex digits and a `From` or `To` that is not one word. It has no `new` door: every field is
computed from the move, and the loop kit's transition writer, `loop_transition.py record`, calls `write_record`.

THE RECOMMENDATION KIND and its door (TOOL-dDeclaredLoop-22 S1): `build_records.py new recommendation --build
<slug> --unit <id> --stage <stage> --score <score> --source <source> --binds yes|no --reason <text> --role
<role> [--signals <text>] [--answers <record stem>]` writes the next `<date>-build-<unit id>-recommendation-<n>.md`,
one stage exit's review recommendation. A SCORE record, the unattended driver's `--recommend`, carries
`Signals` and `Role` `command`; a REASON record carries `Answers`, the stem of the score record it answers,
and the answering role. Both carry `Stage`, `Score` (`RECOMMEND_SCORES`), `Source`, `Binds`
(`RECOMMEND_BINDS`), `Reason` and `Caused-by`. `check_recommendation_fields` holds the shape both ways:
`Stage`, `Source` and `Role` one word each, exactly one of `Signals` and `Answers`, and `Role` `command`
exactly where `Signals` stands. The door also refuses an `Answers` naming no recommendation record of the
build; every refusal exits 1, writing nothing. `--fixture --plant recommendation` stages a score record, the
reason answering it, each refusal and their bindings.

THE WIDEN KIND (TOOL-dWitnessedBar-14 S5): `<date>-build-<unit id>-widen-<n>.md`, a population's growth
admitted with its reason: `Population`, `Keys` (each key backticked, its fields TAB-joined), `Reason` and
`Caused-by`. It has no `new` door: the ratchet pack's `ratchet.py widen` calls `write_record` and writes the
row `widened:<record stem>` beside it, and its `never gains` leg reads the record back through `read_record`.

THE CARD KIND (TOOL-dPlacedRequest-2 S8): `<date>-build-<anchor id>-card-<n>.md`, a build's orientation card
at one step, its snapshot, the anchor the transition kind's: `Build`, `Step` (one word), `Ref` (the card ref's
commit, eight to forty hex digits, or `none`), then the card's text in one `~~~~` fenced block. `read_card`
is its reader, which refuses each of those shapes and a record holding no fenced block. It has no `new`
door: the kickoff engine's snapshot calls `write_record`.

THE PROBE-TRIGGER AND PROBE KINDS (TOOL-dPlacedRequest-7 S6): `<date>-build-<unit id>-probe-trigger-<n>.md`, a
probe opened at an item boundary: `Cause`, `Asker`, `Subject`, `At` and `Key`, `none` where the trigger names no
position or content key. `<date>-build-<unit id>-probe-<n>.md`, the probe it opened: `Sha` (the pinned commit,
eight to forty hex digits), `Kind` (`PROBE_KINDS`), `Question`, `Losing`, `Asker` and `Trigger`, written at the
pin; `Verdict`, closed per `Kind` by `PROBE_VERDICTS`, beside `Judged` (`computed` or `claimed`, a claimed
judgment carrying no `Verdict`) and `Writer` (`stand-in` until the executor lands), written later; then a
`## Method` section of `METHOD_LINE` entries and the `RUN_LINE` lines. `read_probe_trigger` and `read_probe`
are their readers. Neither kind has a `new` door: the loop kit's `probe.py` computes every field and calls
`write_record`.

THE SHAPE-RUN KIND (TOOL-dTotalRecall-11): `<date>-build-<unit id>-shape-run-<n>.md`, one review exit's
`review-shape` line as typed fields, `Kind` to `Out-tokens` in the line's order and `Caused-by` the review
record's stem, then each optional field the line carries (`Merged`, `Trigger`, `Shape`, `Efforts`,
`Role-sha`). `Kind`, `Intensity` and `At` are closed to `SHAPE_KINDS`, `SHAPE_INTENSITIES` and
`SHAPE_STAGES`, the sets `shape_run.SHAPE_RE` compiles. Its door is the record door's `gov_record.py new
shape-run --review <path>`, never this file's `new`, and `shape_run.py --check` compares each record with
its review's line.

ONE LINE PER VALUE, at the one writer (PLAY-dOrderedCharter-49 S53): `write_record` refuses a field value
holding a CR or an LF, or opening `**<Word>:**`, before it writes anything, so no door's value forges a
field; every door's refusal exits 1, writing nothing. Its `lines`, written after the fields, are refused
the same way, and so is a line that reads as a field.

THE FLAKE KIND (TOOL-dWitnessedBar-8 S3): `<date>-build-<unit id>-flake-<n>.md`, one `test.flakes` run's
verdicts: `Run`, `Ended`, `Sha`, `Tree` and `Legs`, then one fenced block of TAB rows, `<leg> · <first rc> ·
<re-run rc or ->`, one per leg the run executed. It has no `new` door: the run-gates kit's `verdict_flow.py
flakes` loads this factory as `keep_tails.py` does and calls `write_record`. The body's one reader is
`read_flake_body`, its rows, and a row flaked where `derive_flaked` says so: its first rc a non-zero integer and
its re-run rc 0. Both kits that read flake records, run-gates and drift, read them through these two
(TOOL-dWitnessedBar-1 S7), so the grammar has this one home.

THE GATE-HEALTH KIND (TOOL-dWitnessedBar-1 S4): `<date>-build-<unit id>-gate-health-<n>.md`, one gate-health
measurement: `Measured` (the reliability bar, `<count>/10`), `Verdicts` (the `Run` of every flake record it
read) and `Legs` (`<armed>/<bar legs>`). It has no `new` door: the drift kit's `drift_report.py --gate-health
--write` loads this factory in-process and calls `write_record`, and the run-gates kit's `verdict_flow.py` reads
the newest one's `Measured` as `verdict.flakes.entry`'s `measured` threshold.

THE RECORD DOOR (TOOL-dTotalRecall-2): `write_new_record` is the one write of `gov_record.py new <kind>`, the
door of each kind whose registry row names it its writer (`read_kind_row`, `DOOR_WRITER`). It renders the row's
template, refuses the bytes by the kind's own check (`check_typed_record`, the reader the `read` verb
dispatches to), lists the kind's home for a record of the same content key (`derive_content_key`), reads the
build's authority (`check_mint_authority`) and mints: a typed kind through `write_record`, whose `check` hook
reads the exact bytes before the file opens, an empty id rule by the caller's `--name`, a `SEQ_RULE` by the
claim CLI's counter. The factory's own `new` doors stay their kinds' doors.

`build_records.py read <path>` prints one record's fields and every refusal: exit 0 well-formed, 1 malformed,
2 an unreadable path or a pending kind. A kind with a reader of its own is read by it; `exception` by
`read_exception`; every other kind, `widen`, `leg-tail`, `flake` and `gate-health` among them, by
`read_record` and its `KINDS` entry alone.

ONE KIND LIST (PLAY-dOrderedCharter-42 S2): `KINDS`' keys are `tree_lib.TYPED_RECORD_KINDS`, the kinds the
bindings reader admits and joins to their file names, and an import whose table differs from that tuple
raises naming each kind. A kind whose fields a later unit owns holds a declared-pending entry,
`{"pending": "<unit id>"}`, which `read` and `write_record` each refuse naming the unit, the second before
any write; `--fixture --plant pending-kind` stages one in a copy of this module. `build_records.py --fixture --plant typed-kinds` writes one record of every typed
kind into a scratch git repository, through `new <kind>` where the kind has a door and `write_record`
otherwise, asserts `tree_lib.read_bindings` reads each `bound` and `gen_build_index.py --print-bindings`
prints no `A` row, and asserts no door takes another door's flags: exit 0 PASS, 1 FAIL naming each failure.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import os
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from design_lib import read_design_conf, read_tracked_builds  # noqa: E402  the tracked population
from tree_lib import RED_FIX_TRAILER, TYPED_RECORD_KINDS  # noqa: E402  the reader's kind list, this table's keys
from id_grammar import SlugPattern  # noqa: E402  the slug grammar, bound at first use (TOOL-dTotalRecall-5 S7)

FIELD = re.compile(r"^- \*\*([A-Z][a-z-]+(?: [a-z]+)?):\*\* (.+)$")     # the instrument deviations.py's
ID = SlugPattern(lambda g: r"[A-Za-z]+-(?:" + g.slug_class + r")-\d+")   # a unit id, its slug the grammar's
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG = SlugPattern(lambda g: g.BUILD_SLUG_RE.pattern)       # a build slug, every grammar one was minted under
PRINCIPLE = re.compile(r"^principle\.p[1-9]\d*$")
SEG = r"[a-z0-9][a-z0-9-]*"                                    # one segment of a tag, and one disposition word
TAG = SEG + r"(?:\." + SEG + r")+"
PIN = re.compile(TAG + r"@[0-9a-f]{8}")
FORGED_FIELD = re.compile(r"^\s*\*\*[A-Za-z][A-Za-z-]*(?: [a-z]+)?:\*\*")   # a value that would read as a field
CHANGE_ACTIONS = ("add", "edit", "remove", "rename", "split")   # the one list `instructions_edit.WRITE_VERBS` reads
ENDING_ACTIONS = ("remove", "rename", "split")                   # those that end a tag and so name a `Successor`
CHANGE_MARKS = ("editorial", "semantic")
OVERRIDE_TAKEN = ("explicit-override", "live-owner-wins")   # the `charter.override` values an override is taken under
PROOF = re.compile(r"tty-cli|none — \S.*")
DOOR_PROOF = "none — stand-in door"
DISPOSITION_CHANNELS = ("mailbox", "terminal", "prompt")   # where the owner answered a held item
ACCEPTANCE_WRITERS = ("executor", "stand-in")   # who re-ran an acceptance record's commands
RECOMMEND_SCORES = ("review", "no-review", "unarmed", "none")   # a recommendation's score, or a role's verdict
RECOMMEND_BINDS = ("yes", "no")
#: one re-run command of an acceptance record: its exit (an integer, or `timeout`), the first twelve hex
#: digits of the SHA-256 of its combined output, and the command as run
RUN_LINE = re.compile(r"run · (?P<exit>-?\d+|timeout) · (?P<hash>[0-9a-f]{12}) · (?P<command>\S.*)")
PROBE_KINDS = ("verification", "reproduction", "experiment")   # a probe's kind, closed (TOOL-dPlacedRequest-7)
#: a probe's verdict, closed per its kind
PROBE_VERDICTS = {"verification": ("confirmed", "refuted", "inconclusive", "unrunnable"),
                  "reproduction": ("confirmed", "refuted", "inconclusive", "unrunnable"),
                  "experiment": ("measured", "within-noise", "aborted", "unrunnable")}
PROBE_JUDGED = ("computed", "claimed")   # how a probe's judgment was reached, a fact beside its verdict
#: a review exit's closed words on its `review-shape` line (TOOL-dTotalRecall-11), which `shape_run.SHAPE_RE`
#: compiles from: the review's kind, its intensity and the stage it reached
SHAPE_KINDS = ("diff-review", "spec-audit")
SHAPE_INTENSITIES = ("full", "light")
SHAPE_STAGES = ("find", "verify", "synth")
METHOD_MARKS = ("judge claimed", "visual")   # a method entry's optional trailing fields
#: one entry of a probe's method: the predicted `<exit>:<hash12>`, the command, which never holds the field
#: separator, then any of `METHOD_MARKS`, each after a ` · `
METHOD_LINE = re.compile(r"- method · (?P<exit>-?\d+|timeout):(?P<hash>[0-9a-f]{12}) · (?P<command>(?:(?! · )\S)"
                         r"(?:(?! · ).)*)(?P<marks>(?: · (?:judge claimed|visual))*)")

# kind -> its required fields and its closed sets, `(field, allowed values)` in refusal order
KINDS = {
    "deviation": {
        "required": ("Departs from", "Hand-off", "Before", "After", "Cause", "Reason", "Evidence", "Risk",
                     "Approver", "Follow-through", "Caused-by"),
        "closed": (("Hand-off", ("design-to-spec", "design-revised", "spec-revised", "spec-to-code",
                                 "code-to-record")),
                   ("Cause", ("design defect", "owner ruling", "builder discovery", "review finding", "external")),
                   ("Risk", ("editorial", "additive", "stricter", "loosening", "breaking"))),
    },
    "exception": {
        "required": ("Principle", "Excuses", "Reason", "Caused-by"),
        "closed": (),
    },
    "override": {
        "required": ("Rule", "Words", "Session", "Value", "Caused-by"),
        "closed": (("Value", OVERRIDE_TAKEN),),
    },
    "change": {
        "required": ("Unit", "Action", "Before", "After", "Mark", "Proof", "Caused-by"),
        "closed": (("Mark", CHANGE_MARKS), ("Action", CHANGE_ACTIONS)),
    },
    "red-fix": {
        "required": ("Leg", "Red line", "Files", "Commit", "Rerun", "Caused-by"),
        "closed": (),
    },
    "disposition": {
        "required": ("Item", "Disposition", "Channel", "Caused-by"),
        "closed": (("Channel", DISPOSITION_CHANNELS),),
    },
    "acceptance": {
        "required": ("Sha", "Writer", "Caused-by"),
        "closed": (("Writer", ACCEPTANCE_WRITERS),),
    },
    "transition": {
        "required": ("Build", "From", "To", "Item", "Sha"),
        "closed": (),
    },
    "recommendation": {
        "required": ("Stage", "Score", "Source", "Binds", "Reason", "Role", "Caused-by"),
        "closed": (("Score", RECOMMEND_SCORES), ("Binds", RECOMMEND_BINDS)),
    },
    "widen": {   # TOOL-dWitnessedBar-14 S5: written by the ratchet pack's `ratchet.py widen`, no `new` door
        "required": ("Population", "Keys", "Reason", "Caused-by"),
        "closed": (),
    },
    "leg-tail": {   # TOOL-dWitnessedBar-25 S6: written by the run-gates kit's `keep_tails.py`, no `new` door;
        # the tail itself is one fenced block after the fields
        "required": ("Leg", "Hash", "Run", "Sha", "Cause"),
        "closed": (),
    },
    "flake": {   # TOOL-dWitnessedBar-8 S3: written by the run-gates kit's `verdict_flow.py flakes`, no `new` door;
        # one TAB row per executed leg in a fenced block after the fields
        "required": ("Run", "Ended", "Sha", "Tree", "Legs"),
        "closed": (),
    },
    "gate-health": {   # TOOL-dWitnessedBar-1 S4: written by the drift kit's `drift_report.py --gate-health --write`,
        # no `new` door
        "required": ("Measured", "Verdicts", "Legs"),
        "closed": (),
    },
    "card": {
        "required": ("Build", "Step", "Ref"),
        "closed": (),
    },
    "probe-trigger": {
        "required": ("Cause", "Asker", "Subject", "At", "Key"),
        "closed": (),
    },
    "probe": {
        "required": ("Sha", "Kind", "Question", "Losing", "Asker", "Trigger"),
        "closed": (("Kind", PROBE_KINDS), ("Judged", PROBE_JUDGED), ("Writer", ACCEPTANCE_WRITERS)),
    },
    "stream-plan": {   # TOOL-dTotalRecall-25 S6: one TOML fence, no field; `record_kinds.check_stream_plan` grades it
        "required": (),
        "closed": (),
    },
    "shape-run": {   # TOOL-dTotalRecall-11: one review exit's `review-shape` line, written by `gov_record.py new
        # shape-run`; each optional field the line carries follows `Caused-by`, and `shape_run.py --check`
        # re-parses the line to hold the counts
        "required": ("Kind", "Round", "Intensity", "At", "Raw", "Confirmed", "Refuted", "Unverified", "Blocker",
                     "High", "Medium", "Low", "Agents", "Out-tokens", "Caused-by"),
        "closed": (("Kind", SHAPE_KINDS), ("Intensity", SHAPE_INTENSITIES), ("At", SHAPE_STAGES)),
    },
}
if set(KINDS) != set(TYPED_RECORD_KINDS):
    raise ImportError("build_records: the kind table and tree_lib.TYPED_RECORD_KINDS differ on "
                      + ", ".join(sorted(set(KINDS) ^ set(TYPED_RECORD_KINDS))))
DOORS = ("exception", "change", "override", "red-fix", "disposition", "recommendation")  # the kinds `new <kind>` writes; every other kind is `write_record`'s alone
PLANTS = ("typed-kinds", "pending-kind", "red-fix-join", "recommendation", "ask-door")
SHA40 = re.compile(r"[0-9a-f]{40}")
SAY_JOIN = "build-records: red-fix join"
#: PLAY-dOrderedCharter-55 S8's `pending-kind`: the exception kind's entry staged pending, in a copy of this module
PENDING_ENTRY = ('    "exception": {\n        "required": ("Principle", "Excuses", "Reason", "Caused-by"),\n'
                 '        "closed": (),\n    },\n', '    "exception": {"pending": "ARCH-tKinds-9"},\n')


def derive_stem(kind):
    """A `kind` record's stem as a regex, its `<n>` following."""
    return r"\d{4}-\d{2}-\d{2}-build-" + ID.pattern + "-" + re.escape(kind) + "-"


def derive_record_name(kind):
    """The name grammar of a `kind` record in a build's `build/` folder, `build` and `n` its groups."""
    return re.compile(r"(?:^|/)builds/(?P<build>[^/]+)/build/" + derive_stem(kind) + r"(?P<n>\d+)\.md$")


def read_record(path, text, kind, check_line=None, check_fields=None):
    """-> (fields, malformed, name match) for one `kind` record. `check_line(key, value, next line)` returns
    the refusals of one field as it is read, `check_fields(fields)` those of the whole record before the
    `Caused-by` rule; both are a kind's own rules."""
    lines = text.replace("\r\n", "\n").split("\n")
    fields, bad, seen = {}, [], {}
    for n, ln in enumerate(lines):
        m = FIELD.match(ln)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if key in seen:
            bad.append((key, f"is given twice, at lines {seen[key]} and {n + 1}"))
            continue
        seen[key] = n + 1
        fields[key] = value
        if check_line:
            bad += check_line(key, value, lines[n + 1] if n + 1 < len(lines) else "")
    spec = KINDS[kind]
    name = derive_record_name(kind).search(path)
    if not name:
        bad.append(("file name", f"is not <date>-build-<unit id>-{kind}-<n>.md in a build's build/ folder"))
    bad += [(k, "is missing") for k in spec["required"] if k not in fields]
    for key, allowed in spec["closed"]:
        if key in fields and fields[key] not in allowed:
            bad.append((key, f"{fields[key]} is outside {' · '.join(allowed)}"))
    if check_fields:
        bad += check_fields(fields)
    if "Caused-by" in fields and not re.fullmatch(r"`?[^\s`]+`?", fields["Caused-by"]):
        bad.append(("Caused-by", f"{fields['Caused-by']} is not one id"))
    return fields, bad, name


def read_records(root, conf, kind, reader):
    """Every TRACKED `<MEMORY_ROOT>/builds/*/build/*-<kind>-*.md`, sorted by path, each read by `reader(rel,
    text)` from its working copy, a dict carrying `build`, `n` and `malformed`; two files of one build at
    one `<n>` are each malformed, naming the other. A tracked path absent from the working tree is absent."""
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    glob = re.compile(re.escape(memory_root) + r"/builds/[^/]+/build/[^/]*-" + re.escape(kind) + r"-[^/]*\.md")
    # PLAY-dOrderedCharter-70 S4: a typed kind selects by its own name grammar, so `<kind>-plan-<n>.md` of another
    # kind is never read as one; the deviation kind keeps its instrument's glob, its one explicit exception.
    named = derive_record_name(kind) if kind != "deviation" else None
    keep = (lambda p: named.search(p)) if named else glob.fullmatch
    records = []
    for rel in sorted(p for p in read_tracked_builds(root, memory_root) if keep(p)):
        p = pathlib.Path(root, rel)
        if p.is_file():
            records.append(reader(rel, p.read_bytes().decode("utf-8", "replace")))
    shared = {}
    for r in records:
        if r["n"] is not None:
            shared.setdefault((r["build"], r["n"]), []).append(r)
    for (_b, n), group in shared.items():
        for r in group if len(group) > 1 else ():
            others = ", ".join(o["path"] for o in group if o is not r)
            r["malformed"].append(("file name", f"shares {kind}-{n} with {others}"))
    return records


# -------------------------------------------------------------------------------- the flake kind's body
def read_flake_body(text):
    """[(leg, first rc, re-run rc or -)], the TAB rows of a flake record's body (TOOL-dWitnessedBar-1 S7)."""
    return [tuple(ln.split("\t")) for ln in text.replace("\r\n", "\n").split("\n") if ln.count("\t") == 2]


def derive_flaked(first, rerun):
    """True where a flake row flaked: its first rc a non-zero integer and its re-run rc 0."""
    return first not in ("0", "-") and first.lstrip("-").isdigit() and rerun == "0"


# -------------------------------------------------------------------------------- the exception kind
def check_exception_fields(fields):
    """The exception kind's own field rules: `Principle` a principle tag, `Expires` a date."""
    bad = []
    if "Principle" in fields and not PRINCIPLE.match(fields["Principle"].strip("`")):
        bad.append(("Principle", f"{fields['Principle']} is not a principle.p<n> tag"))
    if "Expires" in fields and not DATE.match(fields["Expires"]):
        bad.append(("Expires", f"{fields['Expires']} is not a YYYY-MM-DD date"))
    return bad


def read_exception(path, text):
    """One exception record: its fields, keyed for the core gates, and `malformed`."""
    fields, bad, name = read_record(path, text, "exception", check_fields=check_exception_fields)
    return {"id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "principle": fields.get("Principle", "").strip("`"), "excuses": fields.get("Excuses", "").strip("`"),
            "reason": fields.get("Reason"), "expires": fields.get("Expires"), "caused_by": fields.get("Caused-by"),
            "malformed": bad}


def read_exceptions(root, conf=None):
    """The exception register: every tracked exception record of `root`, read by `read_exception`."""
    return read_records(root, read_design_conf(root) if conf is None else conf, "exception", read_exception)


def write_exception(root, build, unit, principle, excuses, reason, expires=None, today=None):
    """The stand-in door: the next exception record of `build`, written under `root`'s own memory tree.
    -> its repo-relative path. Every value is validated here, the write boundary; a refusal is ValueError."""
    for name, value in (("--excuses", excuses), ("--reason", reason)):
        if not value or not value.strip():
            raise ValueError(f"{name} is one non-empty line")
    if not PRINCIPLE.match(principle):
        raise ValueError(f"--principle {principle!r} is not a principle.p<n> tag")
    if expires is not None and not DATE.match(expires):
        raise ValueError(f"--expires {expires!r} is not a YYYY-MM-DD date")
    fields = [("Principle", principle), ("Excuses", excuses), ("Reason", reason)]
    if expires is not None:
        fields.append(("Expires", expires))
    fields.append(("Caused-by", unit))
    return write_record(root, build, unit, "exception", f"{principle} excused for {excuses}", fields, today)


# -------------------------------------------------------------------------------- the change kind
def check_change_fields(fields):
    """The change kind's own field rules: `Unit` a tag, the pin shapes, `Proof`, and `Successor` on an ending
    action alone: one tag on a rename, `none` on a removal, a list on a split, whose `After` holds one pin per
    successor in that order."""
    bad = []
    action, heir = fields.get("Action"), fields.get("Successor")
    if "Unit" in fields and not re.fullmatch(TAG, fields["Unit"]):
        bad.append(("Unit", f"{fields['Unit']} is no tag"))
    for key in ("Before", "After"):
        pins = fields.get(key, "none").split(",") if key == "After" and action == "split" else [fields.get(key, "none")]
        bad += [(key, f"{p} is neither none nor <tag>@<hash8>") for p in pins if p != "none" and not PIN.fullmatch(p)]
    if "Proof" in fields and not PROOF.fullmatch(fields["Proof"]):
        bad.append(("Proof", f"{fields['Proof']} is neither tty-cli nor none — <value>"))
    if action not in ENDING_ACTIONS:
        if heir is not None:
            bad.append(("Successor", f"is given on {action}, which ends no tag"))
        return bad
    if heir is None:
        return bad + [("Successor", f"is missing on {action}")]
    heirs = heir.split(",")
    if action == "remove" and heir != "none":
        bad.append(("Successor", f"{heir} on a removal, which is none"))
    if action != "remove" and not all(re.fullmatch(TAG, h) for h in heirs):
        bad.append(("Successor", f"{heir} is no tag or comma list of tags"))
    if action == "rename" and len(heirs) != 1:
        bad.append(("Successor", f"{heir} on a rename, which is one tag"))
    if action == "split" and [p.split("@")[0] for p in fields.get("After", "").split(",")] != heirs:
        bad.append(("After", f"{fields.get('After')} is not one pin per successor of {heir}, in its order"))
    return bad


def read_change(path, text):
    """One change record: its fields under their own names, the mapping `derive_status` reads, and `id`, `path`,
    `date`, `build`, `n` and `malformed`."""
    fields, bad, name = read_record(path, text, "change", check_fields=check_change_fields)
    stem = pathlib.PurePosixPath(path).stem
    return {**fields, "id": stem, "path": path, "date": stem[:10], "build": name.group("build") if name else None,
            "n": int(name.group("n")) if name else None, "malformed": bad}


def read_changes(root, conf=None):
    """The change register: every tracked change record of `root`, by date, build and `<n>` as a number."""
    records = read_records(root, read_design_conf(root) if conf is None else conf, "change", read_change)
    return sorted(records, key=lambda r: (r["date"], r["build"] or "", r["n"] or 0))


def write_change(root, build, unit, tag, action, mark, before, after, proof, successor=None, promoted_from=None,
                 today=None, lines=()):
    """The one writer of a change record, under `root`'s own memory tree. -> its repo-relative path. Every value
    is validated here, the write boundary; a refusal is ValueError. `lines`, written after the fields, are
    `write_record`'s, as the acceptance kind's are: the loop kit's flow proposal holds its row there
    (TOOL-dDeclaredLoop-28)."""
    fields = [("Unit", tag), ("Action", action), ("Before", before), ("After", after), ("Mark", mark)]
    fields += [("Successor", successor)] * (successor is not None)
    fields += [("Proof", proof)] + [("Promoted-from", promoted_from)] * (promoted_from is not None)
    fields.append(("Caused-by", unit))
    spec, held = KINDS["change"], dict(fields)
    bad = [f"{k} is one non-empty line" for k, v in fields if not v or not v.strip()]
    bad += [f"{k} {held[k]} is outside {' · '.join(allowed)}" for k, allowed in spec["closed"] if held[k] not in allowed]
    bad += [f"{k} {why}" for k, why in check_change_fields(held)]
    if bad:
        raise ValueError("; ".join(bad))
    return write_record(root, build, unit, "change", f"{action} {tag}", fields, today, lines)


# -------------------------------------------------------------------------------- the override kind
def check_override_fields(fields):
    """The override kind's own field rule: `Rule` the tag of the rule set aside."""
    rule = fields.get("Rule", "").strip("`")
    return [("Rule", f"{fields['Rule']} is no tag")] if "Rule" in fields and not re.fullmatch(TAG, rule) else []


def read_override(path, text):
    """One override record: its fields under their own names, and `id`, `path`, `build`, `n` and `malformed`."""
    fields, bad, name = read_record(path, text, "override", check_fields=check_override_fields)
    return {**fields, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


def read_override_value(root):
    """`charter.override` at `root`'s landed revision, through the policy kit's `policy.py get`, found beside
    this kit since a kit imports no sibling. ValueError where no policy kit answers or the reader refuses."""
    from tree_lib import read_policy_value   # noqa: E402  the kit's one policy read (TOOL-aNimbleMend-8 S7)
    try:
        return read_policy_value("charter.override", root)
    except LookupError as exc:
        raise ValueError(f"charter.override cannot be read, so no override is recorded: {exc}") from None


def read_rule_tags():
    """The tags an override's `Rule` may name: each practice of the playbook kit's catalogue and each of its
    `<practice>.<rule>` tags, read beside this kit since a kit imports no sibling. ValueError where no
    catalogue reads."""
    import tomllib
    from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
    try:
        path = resolve_kit_dir("playbook", "practices.toml", KIT) / "practices.toml"
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("practice") or []
    except (LookupError, OSError, ValueError) as exc:
        raise ValueError(f"no practice catalogue reads, so no --rule can be checked: {exc}") from None
    return {r.get("tag") for r in rows} | {f"{r.get('tag')}.{n}" for r in rows for n in r.get("rules") or ()}


def write_override(root, build, unit, rule, words, session, today=None):
    """The stand-in door: the next override record of `build`, written under `root`'s own memory tree, its
    `Value` the key's at the landed revision. -> its repo-relative path. Every value is validated here, the
    write boundary; a refusal, `absolute` among them, is ValueError."""
    for name, value in (("--words", words), ("--session", session)):
        if not value or not value.strip():
            raise ValueError(f"{name} is one non-empty line")
    if not re.fullmatch(TAG, rule or ""):
        raise ValueError(f"--rule {rule!r} is no tag")
    if rule not in read_rule_tags():
        raise ValueError(f"--rule {rule} names no practice or practice rule of the practice catalogue")
    value = read_override_value(root)
    if value not in OVERRIDE_TAKEN:
        raise ValueError(f"charter.override is {value}: the charter outranks every live instruction and no "
                         f"override is taken")
    fields = [("Rule", rule), ("Words", words), ("Session", session), ("Value", value), ("Caused-by", unit)]
    return write_record(root, build, unit, "override", f"{rule} set aside by the owner", fields, today)


# -------------------------------------------------------------------------------- the red-fix kind
def read_red_fix(path, text):
    """One red-fix record: its fields under their own names, and `id`, `path`, `build`, `n` and `malformed`.
    Its own field rule: `Commit` is a full 40-hex sha."""
    fields, bad, name = read_record(
        path, text, "red-fix",
        check_fields=lambda f: [("Commit", f"{f['Commit']} is not a full 40-hex sha")]
        if "Commit" in f and not SHA40.fullmatch(f["Commit"]) else [])
    return {**fields, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


def write_red_fix(root, build, unit, leg, red_line, commit, rerun, today=None):
    """The door: the next red-fix record of `build`, written under `root`'s own memory tree after the fix,
    its `Commit` the full sha `commit` resolves to and its `Files` that commit's paths, both read from the
    commit and never from a flag. -> its repo-relative path. Every value is validated here, the write
    boundary; a refusal, a commit that is no `Red-fix:` commit of `leg` among them, is ValueError."""
    import routed_commits   # noqa: E402  the trailer's one read; imported here so no cycle forms at load
    for name, value in (("--leg", leg), ("--red-line", red_line), ("--commit", commit), ("--rerun", rerun)):
        if not value or not value.strip():
            raise ValueError(f"{name} is one non-empty line")
    leg = leg.strip()
    try:
        got = routed_commits.run_git(root, "rev-parse", "--verify", "--quiet", "--end-of-options",
                                     commit.strip() + "^{commit}", may_fail=True)
        sha = (got or b"").decode("utf-8", "replace").strip()
        if not SHA40.fullmatch(sha) or routed_commits.run_git(root, "merge-base", "--is-ancestor", sha, "HEAD",
                                                               may_fail=True) is None:
            raise ValueError(f"--commit {commit!r} names no commit reachable from HEAD")
        fix = routed_commits.read_routed_commits(root, ["-1", sha])[0]
    except routed_commits.Refusal as exc:
        raise ValueError(str(exc)) from None
    if not fix["red_fix"]:
        raise ValueError(f"commit {sha[:8]} carries no `{RED_FIX_TRAILER}:` trailer, so it is no red fix")
    if leg not in fix["red_fix"]:
        raise ValueError(f"--leg {leg!r} is no `{RED_FIX_TRAILER}:` trailer value of {sha[:8]}, whose legs are: "
                         + " · ".join(fix["red_fix"]))
    if not fix["paths"]:
        raise ValueError(f"commit {sha[:8]} touches no path, so it owes no red-fix record and the join asks none")
    fields = [("Leg", leg), ("Red line", red_line), ("Files", ", ".join(sorted(fix["paths"]))), ("Commit", sha),
              ("Rerun", rerun), ("Caused-by", unit)]
    return write_record(root, build, unit, "red-fix", f"{leg} fixed in {sha[:8]}", fields, today)


def check_red_fix_join(root, staged=False):
    """`join red-fix`: every `Red-fix:` commit reachable from HEAD against every tracked red-fix record, each
    trailer value owing one record whose `Commit` is that sha and whose `Leg` is that value.
    -> (exit, lines), the last line of exit 0 and 1 a summary.

    J1 a fix commit below HEAD with a value no record answers · J2 a record whose `Commit` is no fix commit
    of the population · J3 a record whose `Leg` is no trailer value of its commit · J4 a record whose `Files`
    differs from the commit's paths · J5 two records answering one commit and leg · J6 a record malformed by
    `read_record`. A value at HEAD with no record is printed as owed and is no finding. `staged` reads HEAD
    alone: an unanswered value there is J1, J2 is not graded since the population is one commit, and a HEAD
    with no trailer is held. Exit 2 where git fails or the tracked population cannot be read; a repository
    with no commit holds an empty population.

    PATH-LESS (TOOL-aClearedLedger-9): a trailer commit whose `paths` is empty in the one log pass, an empty
    commit or any merge, owes no record. It is outside the fix set, so it raises no J1 at any depth and a
    record naming it is J2; each of its trailer values is printed on a `path-less` line and the summary
    counts such commits last. NOT CHECKED: whether a merge's resolution changed a file, or whether a
    path-less commit should carry the trailer at all."""
    import routed_commits                  # noqa: E402  imported here so no cycle forms at load
    from design_lib import DesignRefusal   # noqa: E402
    try:
        born = routed_commits.run_git(root, "rev-parse", "--verify", "--quiet", "HEAD^{commit}", may_fail=True)
        commits = routed_commits.read_routed_commits(root, ["-1", "HEAD"] if staged else ["HEAD"]) if born else []
        records = read_records(root, read_design_conf(root), "red-fix", read_red_fix)
    except (routed_commits.Refusal, DesignRefusal, OSError, ValueError) as exc:
        return 2, [f"{SAY_JOIN} · refused · {exc}"]
    head = commits[0]["sha"] if commits else None
    trailed = {c["sha"]: list(dict.fromkeys(c["red_fix"])) for c in commits if c["red_fix"]}
    paths = {c["sha"]: ", ".join(sorted(c["paths"])) for c in commits if c["red_fix"] and c["paths"]}
    fixes = {sha: legs for sha, legs in trailed.items() if sha in paths}   # the commits that owe a record
    bare = {sha: legs for sha, legs in trailed.items() if sha not in paths}
    if staged and not trailed:
        return 0, [f"{SAY_JOIN} · held under --staged · HEAD carries no `{RED_FIX_TRAILER}:` trailer"]
    found, answers, owed = [], {}, 0
    said = [f"{SAY_JOIN} · path-less · {sha[:8]} · {leg} · touches no path, so it owes no record"
            for sha, legs in bare.items() for leg in legs]
    for r in records:
        if r["malformed"]:
            found += [f"J6 · {r['path']} · {key} {why}" for key, why in r["malformed"]]
            continue
        sha, leg = r["Commit"], r["Leg"]
        if sha not in fixes:
            if not staged:
                found.append(f"J2 · {r['path']} · Commit {sha} is no `{RED_FIX_TRAILER}:` commit reachable from HEAD")
            continue
        if leg not in fixes[sha]:
            found.append(f"J3 · {r['path']} · Leg {leg} is no trailer value of {sha[:8]}, whose legs are: "
                         + " · ".join(fixes[sha]))
            continue
        if r["Files"] != paths[sha]:
            found.append(f"J4 · {r['path']} · Files {r['Files']} differs from {sha[:8]}'s paths: {paths[sha]}")
        answers.setdefault((sha, leg), []).append(r["path"])
    found += [f"J5 · {' · '.join(held)} · two records answer {sha[:8]} · {leg}"
              for (sha, leg), held in answers.items() if len(held) > 1]
    for sha, leg in ((s, v) for s, legs in fixes.items() for v in legs):
        if (sha, leg) in answers:
            continue
        if sha == head and not staged:   # owed and not late: the record is the next commit
            owed += 1
            said.append(f"{SAY_JOIN} · owed · {sha[:8]} · {leg}")
        else:
            found.append(f"J1 · {sha[:8]} · {leg} · the fix commit has no red-fix record")
    lines = [f"{SAY_JOIN} · {f}" for f in found] + said
    lines.append(f"{SAY_JOIN} · {len(fixes)} fix commit(s) · {len(records)} record(s) · {owed} owed · "
                 f"{len(bare)} path-less")
    return (1 if found else 0), lines


# -------------------------------------------------------------------------------- the disposition kind
def check_disposition_fields(fields):
    """The disposition kind's own field rules: `Item` a tag opening `item.`, `Disposition` one word."""
    bad = []
    item, word = fields.get("Item"), fields.get("Disposition")
    if item is not None and not (item.startswith("item.") and re.fullmatch(TAG, item)):
        bad.append(("Item", f"{item} is no tag opening item."))
    if word is not None and not re.fullmatch(SEG, word):
        bad.append(("Disposition", f"{word} is not one word"))
    return bad


def read_disposition(path, text):
    """One disposition record: its fields under their own names, and `id`, `path`, `build`, `n` and
    `malformed`."""
    fields, bad, name = read_record(path, text, "disposition", check_fields=check_disposition_fields)
    return {**fields, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


def write_disposition(root, build, unit, item, disposition, channel, reason=None, today=None):
    """The stand-in door: the next disposition record of `build`, written under `root`'s own memory tree.
    -> its repo-relative path. Every value is validated here, the write boundary; a refusal is ValueError.
    The word's membership of the item's outcome set is not read here: that join is the loop kit's."""
    fields = [("Item", item), ("Disposition", disposition), ("Channel", channel)]
    fields += [("Reason", reason)] * (reason is not None)
    fields.append(("Caused-by", unit))
    bad = [f"{k} is one non-empty line" for k, v in fields if not v or not v.strip()]
    if channel not in DISPOSITION_CHANNELS:
        bad.append(f"Channel {channel} is outside {' · '.join(DISPOSITION_CHANNELS)}")
    bad += [f"{k} {why}" for k, why in check_disposition_fields(dict(fields))]
    if bad:
        raise ValueError("; ".join(bad))
    return write_record(root, build, unit, "disposition", f"{item} disposed {disposition}", fields, today)


# -------------------------------------------------------------------------------- the acceptance kind
def read_acceptance(path, text):
    """One acceptance record: its fields under their own names, `runs` its run lines as `(command, exit,
    hash)`, and `id`, `path`, `build`, `n` and `malformed`. Its own rules: `Sha` is a full 40-hex sha, at
    least one line reads `RUN_LINE`, and every line opening `run ·` matches it."""
    opened = [ln.strip() for ln in text.replace("\r\n", "\n").split("\n") if ln.startswith("run ·")]
    runs = [(m.group("command"), m.group("exit"), m.group("hash")) for ln in opened if (m := RUN_LINE.fullmatch(ln))]

    def check_fields(fields):
        bad = [("run line", f"{ln!r} is not run · <exit> · <hash12> · <command>")
               for ln in opened if not RUN_LINE.fullmatch(ln)]
        if not opened:
            bad.append(("run line", "is missing: the record holds one run · <exit> · <hash12> · <command> line per "
                                    "command re-run"))
        if "Sha" in fields and not SHA40.fullmatch(fields["Sha"]):
            bad.append(("Sha", f"{fields['Sha']} is not a full 40-hex sha"))
        return bad

    fields, bad, name = read_record(path, text, "acceptance", check_fields=check_fields)
    return {**fields, "runs": runs, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


def write_acceptance(root, build, unit, sha, writer, runs, today=None):
    """The one writer of an acceptance record, under `root`'s own memory tree: `runs` is `[(command, exit,
    hash12)]`, each written as one run line after the fields. -> its repo-relative path. Every value is
    validated here, the write boundary; a refusal is ValueError. The kind has no `new` door: its run lines
    are computed by the caller and never typed from a flag."""
    bad = []
    if not SHA40.fullmatch(sha or ""):
        bad.append(f"Sha {sha!r} is not a full 40-hex sha")
    if writer not in ACCEPTANCE_WRITERS:
        bad.append(f"Writer {writer} is outside {' · '.join(ACCEPTANCE_WRITERS)}")
    if not runs:
        bad.append("no run: an acceptance record holds one run line per command re-run")
    lines = [f"run · {code} · {digest} · {command}" for command, code, digest in runs]
    bad += [f"run line {ln!r} is not run · <exit> · <hash12> · <command>" for ln in lines if not RUN_LINE.fullmatch(ln)]
    if bad:
        raise ValueError("; ".join(bad))
    fields = [("Sha", sha), ("Writer", writer), ("Caused-by", unit)]
    return write_record(root, build, unit, "acceptance", f"re-run at {sha[:8]}", fields, today, lines)


# -------------------------------------------------------------------------------- the transition kind
def read_transition(path, text):
    """One transition record: its fields under their own names, and `id`, `path`, `build`, `n` and
    `malformed`. Its own rules: `Sha` is eight to forty hex digits, and `From` and `To` are single words."""
    def check_fields(fields):
        bad = [(k, f"{fields[k]} is not one word") for k in ("From", "To")
               if k in fields and not re.fullmatch(SEG, fields[k])]
        if "Sha" in fields and not re.fullmatch(r"[0-9a-f]{8,40}", fields["Sha"]):
            bad.append(("Sha", f"{fields['Sha']} is not eight to forty hex digits"))
        return bad

    fields, bad, name = read_record(path, text, "transition", check_fields=check_fields)
    return {**fields, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


# -------------------------------------------------------------------------------- the card kind
def read_card(path, text):
    """One card record: its fields under their own names, `card` the text of its fenced block, and `id`,
    `path`, `build`, `n` and `malformed`. Its own rules: `Build` a slug, `Step` one word, `Ref` `none` or eight
    to forty hex digits, and one `~~~~` fenced block after the fields."""
    lines = text.replace("\r\n", "\n").split("\n")
    fences = [i for i, ln in enumerate(lines) if ln == "~~~~"]
    card = "\n".join(lines[fences[0] + 1:fences[1]]) if len(fences) >= 2 else None

    def check_fields(fields):
        bad = [] if card is not None else [("card", "is missing: the record holds the card's text in one ~~~~ fenced block")]
        if "Build" in fields and not SLUG.fullmatch(fields["Build"]):
            bad.append(("Build", f"{fields['Build']} is not a build slug"))
        if "Step" in fields and not re.fullmatch(SEG, fields["Step"]):
            bad.append(("Step", f"{fields['Step']} is not one word"))
        if "Ref" in fields and not re.fullmatch(r"none|[0-9a-f]{8,40}", fields["Ref"]):
            bad.append(("Ref", f"{fields['Ref']} is neither none nor eight to forty hex digits"))
        return bad

    fields, bad, name = read_record(path, text, "card", check_fields=check_fields)
    return {**fields, "card": card, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


# -------------------------------------------------------------------------------- the probe kinds
def read_probe_trigger(path, text):
    """One probe-trigger record: its fields under their own names, and `id`, `path`, `build`, `n` and
    `malformed`. Its own rules: `Asker` an item tag, and `At` an item tag or `none`."""
    def check_fields(fields):
        return [(k, f"{fields[k]} is not an item tag{' or none' if k == 'At' else ''}") for k in ("Asker", "At")
                if k in fields and not (re.fullmatch(r"item\." + TAG, fields[k]) or (k == "At" and fields[k] == "none"))]

    fields, bad, name = read_record(path, text, "probe-trigger", check_fields=check_fields)
    return {**fields, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


def check_probe_fields(fields, lines):
    """The probe kind's own rules over its `fields` and its `lines`: `Sha` eight to forty hex digits; a
    `Verdict` inside its `Kind`'s `PROBE_VERDICTS` and standing exactly where `Judged` is `computed`; every
    line opening `- method ·` a `METHOD_LINE` and every line opening `run ·` a `RUN_LINE`."""
    bad = []
    if "Sha" in fields and not re.fullmatch(r"[0-9a-f]{8,40}", fields["Sha"]):
        bad.append(("Sha", f"{fields['Sha']} is not eight to forty hex digits"))
    allowed = PROBE_VERDICTS.get(fields.get("Kind"))
    if "Verdict" in fields and allowed and fields["Verdict"] not in allowed:
        bad.append(("Verdict", f"{fields['Verdict']} is outside {' · '.join(allowed)}, a {fields['Kind']}'s verdicts"))
    if ("Verdict" in fields) != (fields.get("Judged") == "computed") and "Judged" in fields:
        bad.append(("Verdict", f"stands where Judged is {fields['Judged']}: a computed judgment carries a verdict and "
                               f"a claimed one none"))
    if "Verdict" in fields and "Judged" not in fields:
        bad.append(("Judged", "is missing beside Verdict"))
    bad += [("method", f"{ln!r} is not - method · <exit>:<hash12> · <command>[ · <mark>]")
            for ln in lines if ln.startswith("- method ·") and not METHOD_LINE.fullmatch(ln)]
    bad += [("run line", f"{ln!r} is not run · <exit> · <hash12> · <command>")
            for ln in lines if ln.startswith("run ·") and not RUN_LINE.fullmatch(ln)]
    return bad


def read_probe(path, text):
    """One probe record: its fields under their own names, `method` its entries as `(exit, hash, command,
    marks)`, `runs` its run lines as `(command, exit, hash)`, and `id`, `path`, `build`, `n` and `malformed`."""
    lines = [ln.strip() for ln in text.replace("\r\n", "\n").split("\n")]
    method = [(m.group("exit"), m.group("hash"), m.group("command"), tuple(x for x in METHOD_MARKS
                                                                          if f" · {x}" in m.group("marks")))
              for ln in lines if (m := METHOD_LINE.fullmatch(ln))]
    runs = [(m.group("command"), m.group("exit"), m.group("hash")) for ln in lines if (m := RUN_LINE.fullmatch(ln))]
    fields, bad, name = read_record(path, text, "probe", check_fields=lambda f: check_probe_fields(f, lines))
    return {**fields, "method": method, "runs": runs, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


# -------------------------------------------------------------------------------- the recommendation kind
def check_recommendation_fields(fields):
    """The recommendation kind's own field rules, both ways: `Stage`, `Source` and `Role` one word each;
    exactly one of `Signals` (a score record) and `Answers` (a reason record); `Role` `command` exactly where
    `Signals` stands."""
    bad = [(k, f"{fields[k]} is not one word") for k in ("Stage", "Source", "Role")
           if k in fields and not re.fullmatch(SEG, fields[k])]
    if ("Signals" in fields) == ("Answers" in fields):
        bad.append(("Answers", "and Signals: a record carries exactly one, Signals on a score record and "
                               "Answers on a reason record"))
    if "Role" in fields and (fields["Role"] == "command") != ("Signals" in fields):
        bad.append(("Role", f"{fields['Role']} is not command exactly where Signals stands"))
    return bad


def read_recommendation(path, text):
    """One recommendation record: its fields under their own names, and `id`, `path`, `build`, `n` and
    `malformed`."""
    fields, bad, name = read_record(path, text, "recommendation", check_fields=check_recommendation_fields)
    return {**fields, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


def write_recommendation(root, build, unit, stage, score, source, binds, reason, role, signals=None,
                         answers=None, today=None):
    """The door: the next recommendation record of `build`, written under `root`'s own memory tree, a score
    record where `signals` is given and a reason record where `answers` names the score record's stem.
    -> its repo-relative path. Every value is validated here, the write boundary; a refusal is ValueError."""
    fields = [("Stage", stage), ("Score", score)] + [("Signals", signals)] * (signals is not None)
    fields += [("Source", source), ("Binds", binds), ("Reason", reason), ("Role", role)]
    fields += [("Answers", answers)] * (answers is not None)
    fields.append(("Caused-by", unit))
    held = dict(fields)
    bad = [f"{k} is one non-empty line" for k, v in fields if not v or not v.strip()]
    bad += [f"{k} {held[k]} is outside {' · '.join(allowed)}" for k, allowed in KINDS["recommendation"]["closed"]
            if held[k] not in allowed]
    bad += [f"{k} {why}" for k, why in check_recommendation_fields(held)]
    if answers is not None and not bad:
        memory_root = (read_design_conf(root).get("MEMORY_ROOT") or "memory").strip().strip("/")
        answered = pathlib.Path(root, memory_root, "builds", build, "build", f"{answers}.md")
        if not (re.fullmatch(derive_stem("recommendation") + r"\d+", answers) and answered.is_file()):
            bad.append(f"Answers {answers} names no recommendation record of {build}")
    if bad:
        raise ValueError("; ".join(bad))
    return write_record(root, build, unit, "recommendation", f"{stage} review", fields, today)


def write_record(root, build, unit, kind, title, fields, today=None, lines=(), check=None):
    """The record writer every door shares: the next `kind` record of `build` under `root`'s own memory tree,
    headed `# <unit> <kind> <n> — <title>`, then `**Serves:** <kind> <unit>`, each `(key, value)` of
    `fields` as a bold-key bullet and, after one blank line, each of `lines` as written (TOOL-dDeclaredLoop-17
    S1), each refused as a value is. `check(rel, text)`, where given, reads the bytes about to be written and
    raises ValueError to refuse them, before the file is opened (TOOL-dTotalRecall-2 S4). -> its
    repo-relative path. A refusal is ValueError."""
    if kind not in KINDS:
        raise ValueError(f"{kind!r} is not a typed kind: " + ", ".join(KINDS))
    if "pending" in KINDS[kind]:   # PLAY-dOrderedCharter-55 S8: refused before any write, as `read` refuses it
        raise ValueError(f"the {kind} kind is pending on {KINDS[kind]['pending']}, which gives it fields, so no "
                         f"record of it is written")
    if not SLUG.match(build):
        raise ValueError(f"--build {build!r} is not a build slug")
    if not ID.fullmatch(unit):
        raise ValueError(f"--unit {unit!r} is not a unit id")
    forged = [key for key, value in fields if "\n" in value or "\r" in value or FORGED_FIELD.match(value)]
    if forged:
        raise ValueError(f"{', '.join(forged)}: a value is one line and never opens **<Word>:**, so it cannot "
                         f"forge a field")
    forged = [ln for ln in lines if "\n" in ln or "\r" in ln or FORGED_FIELD.match(ln) or FIELD.match(ln)]
    if forged:
        raise ValueError(f"{forged[0]!r}: a line after the fields is one line that never reads as a field, so it "
                         f"cannot forge one")
    memory_root = (read_design_conf(root).get("MEMORY_ROOT") or "memory").strip().strip("/")
    folder = pathlib.Path(root, memory_root, "builds", build)
    if not folder.is_dir():
        raise ValueError(f"{memory_root}/builds/{build}/ is no build folder of this tree")
    out = folder / "build"
    stem = derive_stem(kind)
    taken = [int(m.group(1)) for p in (out.glob(f"*-{kind}-*.md") if out.is_dir() else ())
             if (m := re.fullmatch(stem + r"(\d+)\.md", p.name))]
    n = max(taken, default=0) + 1
    day = today or datetime.date.today().isoformat()
    path = out / f"{day}-build-{unit}-{kind}-{n}.md"
    body = [f"# {unit} {kind} {n} — {title}", "", f"**Serves:** {kind} {unit}", ""]
    body += [f"- **{key}:** {value}" for key, value in fields]
    body += [""] + list(lines) if lines else []
    if check:
        check(path.relative_to(root).as_posix(), "\n".join(body) + "\n")
    out.mkdir(exist_ok=True)
    with open(path, "x", encoding="utf-8", newline="\n") as fh:   # never over a record already there
        fh.write("\n".join(body) + "\n")
    return path.relative_to(root).as_posix()


# -------------------------------------------------------------------------------- the record door
# TOOL-dTotalRecall-2: `gov_record.py new <kind>` is the thin adapter over `write_new_record`, the door of each
# kind whose registry row names it its writer.
#: The writer cell of a kind this door writes; `{}` the kind.
DOOR_WRITER = "gov_record.py new {}"
#: An id rule's counter mint, the one shape a `<seq>` is minted in.
SEQ_RULE = "<FAMILY>-<slug>-<seq>"


def check_typed_record(rel, text, kind):
    """`[(field, why)]`, the refusals of one typed `kind` record at `rel`: the kind's own reader where it has
    one, `deviation_join.read_record` for a deviation, else `read_record` by its `KINDS` entry alone. The
    `read` verb and the record door both call it, so the write boundary and the gate are one predicate."""
    if kind == "deviation":
        import deviation_join  # noqa: E402  the deviation kind's own rules live with its join
        return deviation_join.read_record(rel, text)["malformed"]
    readers = {"change": read_change, "override": read_override, "red-fix": read_red_fix,
               "disposition": read_disposition, "acceptance": read_acceptance, "transition": read_transition,
               "recommendation": read_recommendation, "card": read_card, "probe-trigger": read_probe_trigger,
               "probe": read_probe, "exception": read_exception}
    if kind in readers:
        return readers[kind](rel, text)["malformed"]
    return read_record(rel, text, kind)[1]   # TOOL-dWitnessedBar-8 §8 F12: no rules of its own


def derive_content_key(kind, fields, given=None):
    """The content key of one record: the first 12 hex digits of the SHA-256 of the LF-folded text of the kind
    name, the given name where the row mints none, and each `(key, value)` of `fields` in schema order, the
    formula of the roles kit's `derive_section_sha`. Derived from the fields, never stored beside them."""
    text = "\n".join([kind, given or ""] + [f"{key}: {value}" for key, value in fields])
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()[:12]


def read_kind_row(root, kind):
    """The `[[record-kind]]` row of `kind`, read through `tree_lib.resolve_kind`, whose writer is this door;
    ValueError naming `record-kinds.toml` where the registry or the row is absent, and naming the row's
    writer where another door writes the kind (S2)."""
    import record_kinds  # noqa: E402  the registry's reader, a sibling of this file
    from tree_lib import resolve_kind
    try:
        rows = record_kinds.read_record_kinds(root)
    except record_kinds.RecordKindsError as exc:
        raise ValueError(str(exc)) from None
    if rows is None:
        raise ValueError(f"no {record_kinds.REGISTRY} in this tree, so no kind has a door")
    name = resolve_kind(kind)
    row = next((r for r in rows if r.get("name") == name), None)
    if row is None:
        raise ValueError(f"no [[record-kind]] row of {record_kinds.REGISTRY} names {kind}")
    if row.get("writer") != DOOR_WRITER.format(name):
        raise ValueError(f"its door is {row.get('writer')}, the writer {record_kinds.REGISTRY} names, and each "
                         f"kind has one door")
    return row


def check_mint_authority(root, build):
    """The lines a mint under `build` prints, after its authority reads: the build lease, classed by the loop
    kit's `read_lease_class` where the unattended driver resolves, `mine` admitting and any fact refusing;
    then, the lease free or unread for want of a kit, the claim's `session` in this node's cache ref
    (`gen_build_index.read_claim_lines`), this session's admitting and another's refusing; with neither, the
    charter's per-session rule, named. ValueError naming the holder or the fact (S6, §4 "Minting")."""
    from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
    lines, loop = [], None
    for home, anchor in (("unattended", "unattended.sh"), ("loop", "placement.py")):
        try:
            loop = resolve_kit_dir(home, anchor, KIT)
        except LookupError:
            lines, loop = [f"unarmed — no {home} kit"], None
            break
    if loop is not None:
        if str(loop) not in sys.path:
            sys.path.insert(0, str(loop))
        import placement  # noqa: E402  the loop kit's lease comparison, kept one (§8 F6)
        cls = placement.read_lease_class(root, build)
        if cls == "mine":
            return lines
        if cls != "free":
            raise ValueError(cls)
    import gen_build_index  # noqa: E402  the claim's cache ref and its reader
    claim = gen_build_index.read_claim_lines(str(root), build)
    if claim is not None:
        sessions = [ln[len("session: "):].strip() for ln in claim if ln.startswith("session: ")]
        me = os.environ.get("CLAUDE_CODE_SESSION_ID") or "absent"
        holder = sessions[-1] if sessions else "absent"   # the oldest commit, the claim itself
        if holder != me:
            raise ValueError(f"the claim of {build} ({gen_build_index.CLAIM_CACHE_NS}/{build}) is held by session "
                             f"{holder}, not this session {me}")
        return lines
    return lines + [f"minted under the session rule: no claim or lease for {build}"]


def write_seq_mint(root, family, build, key):
    """The counter mint of one `<FAMILY>-<slug>-<seq>` id, `key` its claimant: `gov-claim.sh ask <family>
    <build> --claimant <key>` through the claim CLI's one caller seam, and on its `local … · no remote`
    answer the driver's floor `derive_ask_seq`, run sourced. The counter ref is the authority, so no lease
    or claim is read. Its callers are the `fields` door's `<seq>` rule and the ask handler of
    `gov_record.py` (TOOL-dTotalRecall-7 §4). -> `(word, said, lines)`, `word` `minted` or `waiting`,
    `said` the id or the waiting line, `lines` the `local` line where the floor minted; ValueError for
    every refusal."""
    import gen_build_index  # noqa: E402  the claim CLI's one caller seam
    try:
        rc, said = gen_build_index.run_claim_cli(str(root), "ask", family, build, "--claimant", key)
    except gen_build_index.Problem as exc:
        raise ValueError(str(exc)) from None
    if rc == 4:
        return "waiting", said, []
    if rc != 0:
        raise ValueError(said)
    if not said.startswith("local "):
        return "minted", said.split(" ", 1)[1].strip(), []
    from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
    try:
        resolve_kit_dir("unattended", "unattended.sh", KIT)
        loop = resolve_kit_dir("loop", "breakpoints.py", KIT)
    except LookupError:
        raise ValueError("unarmed — no unattended kit") from None
    if str(loop) not in sys.path:
        sys.path.insert(0, str(loop))
    from breakpoints import run_sourced   # noqa: E402  the driver's one floor, never a third copy
    rc, out = run_sourced(root, "derive_ask_seq %s %s" % (family, build))
    if rc != 0 or not out.strip().isdigit():
        raise ValueError(f"derive_ask_seq {family} {build} answered exit {rc}: {out.strip()[-200:]}")
    return "minted", f"{family}-{build}-{out.strip()}", [said]


def write_new_record(root, kind, build, unit, title, fields, name=None):
    """The record door's one write (TOOL-dTotalRecall-2 S1-S8): the `kind` record of `build` serving `unit`,
    headed `title`, `fields` its `(key, value)` pairs in the caller's order, `name` the stem a row with an
    empty `id-rule` takes. In order: the row (S2), the render and its refusal by the kind's own check (S3,
    S4), the listing of the kind's home for a record of the same content key (S5), the authority (S6), then
    the mint and the write, staged (S8). -> `(word, path or line, key, lines)`, `word` one of `wrote`,
    `exists` and `waiting`, `lines` the authority's. ValueError for every refusal, nothing written."""
    import fnmatch
    import record_kinds  # noqa: E402  the registry's template and field check
    from tree_lib import TYPED_RECORD_KINDS
    root = pathlib.Path(root)
    row = read_kind_row(root, kind)
    kind = row["name"]
    schema = row.get("schema") if isinstance(row.get("schema"), dict) else {}
    if schema.get("form") != "fields":
        raise ValueError(f"its schema form is {schema.get('form')}, written only by a kind handler")
    rule, home, typed = row.get("id-rule") or "", row.get("home"), kind in TYPED_RECORD_KINDS
    for flag, value in (("--build", build), ("--unit", unit), ("--title", title)):
        if not value:
            raise ValueError(f"{flag} is required")
    if not SLUG.match(build):
        raise ValueError(f"--build {build!r} is not a build slug")
    if not ID.fullmatch(unit):
        raise ValueError(f"--unit {unit!r} is not a unit id")
    forged = [key for key, value in [("title", title)] + list(fields)
              if "\n" in value or "\r" in value or FORGED_FIELD.match(value)]
    if forged:
        raise ValueError(f"{', '.join(forged)}: a value is one line and never opens **<Word>:**, so it cannot "
                         f"forge a field")
    order = [f for f in schema.get("fields", []) if f != "Serves"]
    given = dict(fields)
    ordered = [(f, given[f]) for f in order if f in given] + [(k, v) for k, v in fields if k not in order]
    template = record_kinds.render_template([row], kind).split("\n")

    def render_text(rel, n):
        """The template filled for the record at `rel`, `n` its minted `<n>`."""
        head = template[0].replace("<unit id>", unit).replace("<n>", str(n)).replace("<title>", title)
        body = [head, "", f"**Serves:** {kind} {unit}", ""]
        body += [f"- **{f}:** {given[f]}" if f in given else f"- **{f}:** " for f in order]
        body += [f"- **{k}:** {v}" for k, v in ordered if k not in order]
        return "\n".join(body) + "\n"

    def read_ordered_fields(text):
        """A record's `(key, value)` field lines, the row's fields first in schema order, then the rest."""
        pairs = [(m.group(1), m.group(2).strip()) for ln in text.replace("\r\n", "\n").split("\n")
                 if (m := FIELD.match(ln))]
        seen = dict(pairs)
        return [(f, seen[f]) for f in order if f in seen] + [(k, v) for k, v in pairs if k not in order]

    def check_text(rel, text):
        """The kind's own check over the bytes at `rel`: S4's refusal, naming each field and its reason."""
        if typed:
            bad = check_typed_record(rel, text, kind)
        else:
            missing, misplaced = record_kinds.derive_field_lines(text, schema.get("fields", []))
            bad = [(f, "is missing") for f in missing] + [(f, "is out of the row's order") for f in misplaced]
        if bad:
            raise ValueError("; ".join(f"{key} {why}" for key, why in bad))

    # the placement: the row's home with the build for its `builds/*/` segment, and the name its rule gives
    memory_root = (read_design_conf(root).get("MEMORY_ROOT") or "memory").strip().strip("/")
    if not pathlib.Path(root, memory_root, "builds", build).is_dir():
        raise ValueError(f"{memory_root}/builds/{build}/ is no build folder of this tree")
    glob = str(home).replace("builds/*/", f"builds/{build}/", 1)
    folder = glob.rsplit("/", 1)[0]
    if "*" in folder or "builds/*/" not in str(home):
        raise ValueError(f"its home {home} places no record under one build")
    today = datetime.date.today().isoformat()
    seq = None
    if typed:
        if name:
            raise ValueError(f"--name names a record of a row that mints none, and {kind} mints its own")
        rel = f"{memory_root}/builds/{build}/build/{today}-build-{unit}-{kind}-1.md"   # provisional, for the check
        given_id = None
    elif not rule:
        if not name:
            raise ValueError(f"--name <stem> is required: the {kind} row's id-rule is empty, so no grammar "
                             f"mints its name")
        if name in (".", "..") or any(c in name for c in "/\\") or not name.strip():
            raise ValueError(f"--name {name!r} is not one path segment")
        rel = f"{folder}/{name}.md"
        if not fnmatch.fnmatchcase(rel, glob):
            raise ValueError(f"--name {name}: {rel} misses the {kind} row's home {home}")
        hit = next((k for k in TYPED_RECORD_KINDS if derive_record_name(k).search(rel)), None)
        if hit:
            raise ValueError(f"--name {name}: {rel} is a {hit} record's name, graded by that kind alone")
        given_id = name
    elif rule == SEQ_RULE + ".md":
        if name:
            raise ValueError(f"--name names a record of a row that mints none, and {kind} mints its own")
        seq = (unit.split("-", 1)[0], build)   # the counter's family is the serving unit's
        rel, given_id = f"{folder}/{seq[0]}-{build}-0.md", None   # provisional, for the check
    else:
        raise ValueError(f"its id-rule {rule} holds a placeholder this door mints only in a typed kind")
    text = render_text(rel, 1)
    check_text(rel, text)
    key = derive_content_key(kind, read_ordered_fields(text), given_id)

    # the listing: a record of the kind whose re-derived key matches is the same write
    grammars = {k: derive_record_name(k) for k in TYPED_RECORD_KINDS}
    for path in record_kinds.read_tracked(root, str(home)):
        hits = [k for k, g in grammars.items() if g.search(path)]
        if (kind not in hits) if typed else hits:
            continue
        p = pathlib.Path(root, path)
        if not p.is_file():
            continue
        stem = p.stem if not rule else None
        other = derive_content_key(kind, read_ordered_fields(p.read_bytes().decode("utf-8", "replace")), stem)
        if other == key:
            return "exists", path, key, []
        if given_id is not None and path == rel:
            raise ValueError(f"{path} already holds the record {given_id}, its content key {other}, not {key}")
    if given_id is not None and pathlib.Path(root, rel).exists():
        raise ValueError(f"{rel} already exists, untracked: a different value under an existing id")

    # the authority and the mint
    lines = [] if seq else check_mint_authority(root, build)
    if typed:
        def check_written(at, written):
            """The bytes `write_record` is about to write: the template's render, refused by the kind's check."""
            n = re.search(r"-(\d+)\.md$", at).group(1)
            if written != render_text(at, n):
                raise ValueError(f"the factory's layout and the {kind} template disagree at {at}")
            check_text(at, written)
        rel = write_record(root, build, unit, kind, title, ordered, today, check=check_written)
    else:
        if seq:
            word, minted, floor = write_seq_mint(root, seq[0], build, key)
            if word == "waiting":
                return "waiting", minted, key, lines
            lines = lines + floor
            rel = f"{folder}/{minted}.md"
            text = render_text(rel, 1)
        pathlib.Path(root, rel).parent.mkdir(parents=True, exist_ok=True)
        with open(pathlib.Path(root, rel), "x", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    subprocess.run(["git", "add", "--", rel], cwd=str(root), capture_output=True, check=False)
    return "wrote", rel, key, lines


# -------------------------------------------------------------------------------- the fixture
# each door's flags over the fixture, and a flag only it takes, which every other door refuses
DOOR_ARGV = {
    "exception": (["--principle", "principle.p1", "--excuses", "the fixture", "--reason", "the typed-kinds round trip"],
                  ["--principle", "principle.p1"]),
    "change": (["--tag", "unit.fixture", "--action", "add", "--mark", "semantic", "--before", "none",
                "--after", "unit.fixture@0123abcd"], ["--tag", "unit.fixture"]),
    "override": (["--rule", "practice.verify", "--words", "skip the bar on this one", "--session", "fixture"],
                 ["--rule", "practice.verify"]),
    # the fixture's first commit carries the trailer, so HEAD is a fix of this leg when the door runs
    "red-fix": (["--leg", "the fixture leg", "--red-line", "FAIL the fixture leg", "--commit", "HEAD",
                 "--rerun", "the fixture leg · green"], ["--leg", "the fixture leg"]),
    "disposition": (["--item", "item.plan.exit", "--disposition", "continue", "--channel", "terminal"],
                    ["--item", "item.plan.exit"]),
    "recommendation": (["--stage", "design", "--score", "review", "--source", "scored-signals-and-reasoning",
                        "--binds", "no", "--reason", "pending", "--role", "command",
                        "--signals", "3 units in the generated region"], ["--stage", "design"]),
}


def run_door(root, kind, unit, flags):
    """`new <kind>` over the fixture's build: `(exit, what it printed)`, argparse's refusal an exit too."""
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        try:
            rc = main(["new", kind, "--root", str(root), "--build", "tKinds", "--unit", unit, *flags])
        except SystemExit as exc:
            rc = exc.code
    return rc, buf.getvalue()


def check_bindings(root, plant, written, run_git):
    """`written`, `[(kind, rel)]` tracked in the fixture's repository: each read `bound` as its kind by
    `tree_lib.read_bindings`, and `gen_build_index.py --print-bindings` printing its `S` row and no `A` row.
    -> the failures, an empty `written` among them."""
    import subprocess
    from tree_lib import read_bindings   # noqa: E402
    bad = []
    tracked = [p for p in run_git("ls-files").split("\n") if p]
    binds = read_bindings(str(root), tracked, read_design_conf(root))
    for kind, rel in written:
        rec = binds.get(rel) or {"state": "absent", "kind": None, "why": "not read"}
        if rec["state"] != "bound" or rec["kind"] != kind:
            bad.append(f"{kind}: {rel} reads {rec['state']} as {rec['kind']} — {rec['why']}")
        else:
            print(f"build-records: {plant} · {kind} · {rel} · bound")
    p = subprocess.run([sys.executable, str(KIT / "gen_build_index.py"), "--print-bindings"], cwd=root,
                       capture_output=True, text=True, encoding="utf-8")
    lines = p.stdout.splitlines()
    if p.returncode != 0:
        bad.append(f"--print-bindings exited {p.returncode}: {(p.stdout + p.stderr).strip()[:300]}")
    bad += [f"--print-bindings printed {ln}" for ln in lines if ln.startswith("A\t")]
    # no A row is an answer only where the predicate read the records: each owes its S row
    bad += [f"--print-bindings printed no S row for {rel}" for kind, rel in written
            if not any(ln.startswith(f"S\t{rel}\t{kind}\t") for ln in lines)]
    if not written:
        bad.append("no typed kind was written, so no A row proves nothing")
    return bad


def derive_flags(flags, flag, value):
    """`flags` with `flag`'s value replaced by `value`, or `flag value` appended where it is absent."""
    if flag not in flags:
        return [*flags, flag, value]
    at = flags.index(flag) + 1
    return [*flags[:at], value, *flags[at + 1:]]


def check_recommendation_plant(root, unit, run_git):
    """`--fixture --plant recommendation` (TOOL-dDeclaredLoop-22 AC1), over the fixture's committed build: a
    score record numbered 1 and a reason record numbered 2 answering it, each read back by `read` with every
    field; `--score maybe`, `--binds perhaps`, a two-word `--stage`, an `--answers` naming no record and a
    score record carrying `--answers` each exit 1 naming the field, writing nothing; both bound. -> failures."""
    import contextlib
    import io
    bad, written = [], []
    folder = root / "memory/builds/tKinds/build"
    score = DOOR_ARGV["recommendation"][0]
    reason = ["--stage", "design", "--score", "review", "--source", "scored-signals-and-reasoning", "--binds", "no",
              "--reason", "two units share a seam", "--role", "gov-spec-writer"]
    for n, flags, own in ((1, score, "Signals"), (2, reason, "Answers")):
        if n == 2:
            flags = derive_flags(flags, "--answers", pathlib.PurePosixPath(written[0][1]).stem)
        rc, said = run_door(root, "recommendation", unit, flags)
        got = re.search(r"wrote (\S+-recommendation-(\d+)\.md)", said)
        if rc != 0 or not got or got.group(2) != str(n):
            bad.append(f"record {n}: new recommendation exited {rc}, not 0 writing recommendation-{n}: "
                       f"{said.strip()[:200]}")
            return bad
        written.append(("recommendation", got.group(1)))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = main(["read", str(root / got.group(1))])
        missing = [k for k in (*KINDS["recommendation"]["required"], own) if f" · {k}: " not in buf.getvalue()]
        if rc != 0 or missing:
            bad.append(f"record {n}: read exited {rc}, missing {missing}: {buf.getvalue().strip()[:300]}")
        print(f"build-records: recommendation · record {n} · {got.group(1)} · read exit {rc}")
    held = sorted(p.name for p in folder.glob("*.md"))
    nowhere = f"2026-01-01-build-{unit}-recommendation-9"
    for field, flags in (("Score", derive_flags(score, "--score", "maybe")),
                         ("Binds", derive_flags(score, "--binds", "perhaps")),
                         ("Stage", derive_flags(score, "--stage", "design review")),
                         ("Answers", derive_flags(reason, "--answers", nowhere)),
                         ("Answers", derive_flags(score, "--answers", pathlib.PurePosixPath(written[0][1]).stem))):
        rc, said = run_door(root, "recommendation", unit, flags)
        if rc != 1 or (f"refused · {field}" not in said and f"; {field}" not in said):
            bad.append(f"{field}: exited {rc}, not 1 naming {field}: {said.strip()[:200]}")
        print(f"build-records: recommendation · refusal · {field} · exit {rc}")
    if sorted(p.name for p in folder.glob("*.md")) != held:
        bad.append("a refused recommendation door wrote a record")
    run_git("add", "-A")
    return bad + check_bindings(root, "recommendation", written, run_git)


def seed_ask_repo(top, name, policy=None):
    """The `ask-door` plant's seed (TOOL-dTotalRecall-7 AC4): a git repository `top/name` whose one commit on
    `main` holds a `.memory-tree.conf` declaring `example:EXMP`, this kit's `record-kinds.toml` at its kit
    path, and the build folder `tDoor` with its README and no `BACKLOG.md`, plus `policy` as its
    `.governance/policy.toml` where given; no remote. -> its path."""
    import record_kinds  # noqa: E402  the registry's kit path
    import subprocess
    root = pathlib.Path(top, name)
    files = {".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="example:EXMP"\n',
             "memory/builds/tDoor/README.md": "# tDoor\n",
             f"{record_kinds.derive_kit_rel()}/{record_kinds.REGISTRY}": (KIT / record_kinds.REGISTRY).read_bytes().decode("utf-8")}
    if policy is not None:
        files[".governance/policy.toml"] = policy
    for rel, text in files.items():
        pathlib.Path(root, rel).parent.mkdir(parents=True, exist_ok=True)
        with open(pathlib.Path(root, rel), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    for argv in (("init", "-q", "--template="), ("symbolic-ref", "HEAD", "refs/heads/main"),
                 ("config", "user.name", "fx"), ("config", "user.email", "fx@example.invalid"),
                 ("config", "commit.gpgsign", "false"), ("config", "core.autocrlf", "false"),
                 ("add", "-A"), ("commit", "-qm", "the ask-door seed")):
        subprocess.run(["git", *argv], cwd=str(root), capture_output=True, check=True)
    return root


def run_ask_door(root, *flags):
    """`gov_record.py new ask --build tDoor <flags>` run from this kit in the seed `root`: `(exit, output)`."""
    import subprocess
    p = subprocess.run([sys.executable, str(KIT / "gov_record.py"), "new", "ask", "--build", "tDoor", *flags],
                       cwd=str(root), capture_output=True, text=True, encoding="utf-8", errors="replace",
                       stdin=subprocess.DEVNULL, timeout=600)
    return p.returncode, (p.stdout + p.stderr).strip()


#: The renderer plants of TOOL-dTotalRecall-41 AC3 and AC4, each the body of `plant(ask_id, filed, text, unit,
#: pointer, clauses)` over `real`, the renderer it rebinds.
RENDER_PLANTS = {
    "drop-clauses": "return real(ask_id, filed, text, unit, pointer)",
    "second-ask": "return real(ask_id, filed, text, unit, pointer, clauses) + '\\n' + "
                  "real(ask_id + '9', filed, 'planted', clauses=clauses)",
}


def run_planted_door(root, plant, *flags):
    """`run_ask_door` in a child Python that first rebinds `backlog.render_ask_row` to the `RENDER_PLANTS`
    body `plant` (TOOL-dTotalRecall-41 AC3, AC4), then runs `gov_record.main`: `(exit, output)`."""
    import subprocess
    code = ("import sys\n"
            "for s in (sys.stdout, sys.stderr):\n"
            "    s.reconfigure(encoding='utf-8', errors='replace')\n"
            "sys.path.insert(0, sys.argv[1])\n"
            "import backlog\n"
            "real = backlog.render_ask_row\n"
            "def plant(ask_id, filed, text, unit=False, pointer='', clauses=()):\n"
            f"    {RENDER_PLANTS[plant]}\n"
            "backlog.render_ask_row = plant\n"
            "import gov_record\n"
            "sys.exit(gov_record.main(['new', 'ask', '--build', 'tDoor', *sys.argv[2:]]))\n")
    p = subprocess.run([sys.executable, "-c", code, str(KIT), *flags], cwd=str(root), capture_output=True, text=True,
                       encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL, timeout=600)
    return p.returncode, (p.stdout + p.stderr).strip()


def check_ask_plant():
    """`--fixture --plant ask-door` (TOOL-dTotalRecall-7 AC4 to AC7, AC10 to AC12; TOOL-dTotalRecall-41 AC1 to
    AC4): the ask door's refuse, undeclared-family, value-refusal, planted-renderer, file, replay and grade
    cases in one seed, the refused read in a seed whose one commit
    holds an invalid `asks.acceptance`, and the refused and filed cases over a bare remote, each seed under
    the host temp directory and the door run from this kit. -> `(failures, cases)`, or `(None, why)` where
    a kit the door runs beside does not resolve."""
    import subprocess
    import tempfile
    import backlog  # noqa: E402  the parser, the predicate and the verdicts the cases read
    from deviation_join import remove_tree   # noqa: E402  the kit's fixture helper
    for home, anchor in (("policy", "policy.py"), ("unattended", "unattended.sh"), ("loop", "breakpoints.py")):
        try:
            backlog.resolve_kit_dir(home, anchor, KIT)
        except LookupError:
            return None, f"no {home} kit beside this one"
    bad, cases = [], [0]
    rel, first = "memory/builds/tDoor/BACKLOG.md", "EXMP-tDoor-1"
    base = ["--family", "EXMP", "--text", "x", "--sev", "LOW", "a fixture ask"]
    accept = ["--clause", "accept", "the leg is green"]
    grammar = backlog.build_grammar(("EXMP",))
    top = pathlib.Path(tempfile.mkdtemp(prefix="ask-"))

    def run_git(root, *args):
        return subprocess.run(["git", *args], cwd=str(root), capture_output=True, text=True, encoding="utf-8",
                              check=True).stdout

    def check_case(case, got, rc, needles, root=None):
        """One case: its exit, each needle in its output, and where `root` is given a clean status."""
        status = run_git(root, "status", "--porcelain").strip() if root is not None else ""
        lack = [n for n in needles if n not in got[1]]
        cases[0] += 1
        if got[0] != rc or lack or status:
            bad.append(f"{case}: exited {got[0]}, not {rc}; missing {lack}; status {status!r}: {got[1][:300]}")
        print(f"build-records: ask-door · {case} · exit {got[0]}")

    def read_backlog(root):
        """The seed's backlog parsed under `EXMP`, and the verdicts of a corpus of it under the clean conf."""
        parsed = backlog.parse_file(rel, (root / rel).read_bytes().decode("utf-8"), grammar)
        return parsed, backlog.derive_verdicts(backlog.build_corpus([parsed]), backlog._CLEAN_CONF)

    try:
        a = seed_ask_repo(top, "a")
        check_case("refuse", run_ask_door(a, *base), 2, ["asks.acceptance", "accept", "seen … run"], a)   # AC4
        check_case("undeclared family", run_ask_door(a, *derive_flags(base, "--family", "NOPE"), "--clause", "accept",
                                                     "y"), 2, ["--family", "NOPE", "EXMP"], a)   # AC10
        check_case("no family", run_ask_door(a, *base[2:], "--clause", "accept", "y"), 2, ["--family"], a)
        # TOOL-dTotalRecall-41 AC1 to AC3, each before the first filing, so the "file" case's id proves none minted
        check_case("text-newline", run_ask_door(a, *derive_flags(base, "--text", "x\n- X-a-2 · filed 2026-02-01 · "
                                                                "injected"), *accept), 2, ["--text", "a line feed"], a)
        check_case("text-separator", run_ask_door(a, *derive_flags(base, "--text", "x · accept y")), 2,
                   ["--text", "the row separator"], a)
        check_case("pointer-cr", run_ask_door(a, *base, "--pointer", "a\rb", *accept), 2,
                   ["--pointer", "a carriage return"], a)
        check_case("sev-newline", run_ask_door(a, *base[:-1], "w\n- SEV · X-a-1 · HIGH · z", *accept), 2,
                   ["--sev", "a line feed"], a)
        check_case("graded-args-not-row", run_planted_door(a, "drop-clauses", *base, *accept), 2,
                   ["asks.acceptance", "states no acceptance"], a)
        got = run_ask_door(a, *base, *accept)   # AC5
        check_case("file", got, 0, [f"wrote {rel} {first} key "])
        key = (re.search(rf"^wrote {re.escape(rel)} {first} key ([0-9a-f]{{12}})$", got[1], re.M) or [None, None])[1]
        if key is None:
            bad.append(f"file: no `wrote {rel} {first} key <12 hex digits>` line: {got[1][:300]}")
            return bad, cases[0]
        parsed, verdicts = read_backlog(a)
        asks = [x for x in parsed.asks if x.id == first]
        sevs = [r for r in parsed.rows if r.verb == backlog.SEV_VERB and r.target == first and r.value == "LOW"]
        graded = asks and backlog.check_ask_acceptable({label: tuple(backlog.read_clause_values(asks[0].clauses, label))
                                                        for label in backlog.CLAUSE_LABELS})
        named = sorted({v.code for v in verdicts if first in v.text} & {12, 14})
        if len(parsed.asks) != 1 or len(asks) != 1 or not graded or len(sevs) != 1 or named:
            bad.append(f"file: the backlog reads {len(parsed.asks)} ask(s), {len(sevs)} LOW SEV row(s) naming {first}, "
                       f"graded {bool(graded)}, named under {named}")
        held = (a / rel).read_bytes()
        check_case("replay", run_ask_door(a, *base, *accept), 0, [f"exists {rel} {first} key {key}"])   # AC12
        if (a / rel).read_bytes() != held or len(read_backlog(a)[0].asks) != 1:
            bad.append("replay: the backlog's bytes moved, or it no longer reads one ask")
        status = run_git(a, "status", "--porcelain")
        check_case("two-rows-added", run_planted_door(a, "second-ask", *base, *accept), 2,
                   ["add 2 ask(s)", "nothing was minted or written"])   # TOOL-dTotalRecall-41 AC4
        if (a / rel).read_bytes() != held or run_git(a, "status", "--porcelain") != status:
            bad.append("two-rows-added: the backlog's bytes or the status moved on a refused filing")
        (a / ".governance").mkdir(exist_ok=True)
        with open(a / ".governance/policy.toml", "w", encoding="utf-8", newline="\n") as fh:
            fh.write('asks.acceptance = "grade"\n')
        run_git(a, "add", "-A")
        run_git(a, "commit", "-qm", "asks.acceptance graded")
        got = run_ask_door(a, *base)   # AC6
        check_case("grade", got, 0, ["graded: not ready (R5)", f"wrote {rel} "])
        gid = (re.search(rf"^wrote {re.escape(rel)} (\S+) key", got[1], re.M) or [None, "NONE"])[1]
        if not any(v.code == 14 and gid in v.text for v in read_backlog(a)[1]):
            bad.append(f"grade: V14 does not name {gid}, the id the grade case filed")
        b = seed_ask_repo(top, "b", 'asks.acceptance = "bogus"\n')   # AC7
        check_case("refused read", run_ask_door(b, *base), 2, ["asks.acceptance", "policy: refused"], b)
        c = seed_ask_repo(top, "c")   # AC11
        run_git(top, "init", "-q", "--bare", "--template=", "c.git")
        run_git(top / "c.git", "symbolic-ref", "HEAD", "refs/heads/main")
        run_git(c, "remote", "add", "origin", (top / "c.git").as_posix())
        run_git(c, "push", "-q", "origin", "main")
        check_case("refused on a remote", run_ask_door(c, *base), 2, ["asks.acceptance"], c)
        refs = run_git(c, "ls-remote", "origin", "refs/gov/claims/asks/*").strip()
        if refs:
            bad.append(f"refused on a remote: the refused filing left a counter ref on origin: {refs}")
        check_case("filed on a remote", run_ask_door(c, *base, *accept), 0, [f"wrote {rel} {first} key "])
        refs = run_git(c, "ls-remote", "origin", "refs/gov/claims/asks/*").strip().splitlines()
        if len(refs) != 1 or not refs[0].endswith("refs/gov/claims/asks/EXMP-tDoor"):
            bad.append(f"filed on a remote: origin holds {refs}, not the one counter ref of EXMP-tDoor")
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError, ValueError) as exc:
        bad.append(f"the fixture could not be built: {exc}")
    finally:
        remove_tree(top)
    return bad, cases[0]


def run_fixture(plant):
    """`--fixture --plant typed-kinds` (PLAY-dOrderedCharter-42 S4): one record of every kind of
    `TYPED_RECORD_KINDS`, read at run time, in a build folder of a scratch git repository under the host
    temp directory, each read back `bound` as its kind and `--print-bindings` printing no `A` row, and each
    door refusing the flag only another door takes."""
    import subprocess
    import tempfile
    from deviation_join import remove_tree, set_env_aside   # noqa: E402  the kit's fixture helpers
    from tree_lib import GIT_ENV_LEAKS, read_bindings        # noqa: E402
    unit, bad, written = "ARCH-tKinds-1", [], {}
    if plant == "ask-door":   # TOOL-dTotalRecall-7: the ask door's cases, each in a seed of its own
        with set_env_aside(GIT_ENV_LEAKS):
            bad, cases = check_ask_plant()
        if bad is None:
            print(f"build-records: SKIP {plant} — {cases}, so its cases are UNEXERCISED here")
            return 0
        for why in bad:
            print(f"build-records: FAIL {plant} · {why}")
        if bad:
            return 1
        print(f"build-records: PASS {plant} — {cases} cases: refuse, family, file, replay, grade, refused read, remote")
        return 0
    root = pathlib.Path(tempfile.mkdtemp(prefix="br-"))
    if plant == "pending-kind":   # PLAY-dOrderedCharter-55 S8: a copy of this module with one kind pending
        import contextlib
        import io
        import types
        try:
            source = pathlib.Path(__file__).read_text(encoding="utf-8")
            if source.count(PENDING_ENTRY[0]) != 1:
                bad.append("the exception kind's entry is not where the plant stages it")
            mod = types.ModuleType("build_records_pending")
            mod.__file__ = __file__
            try:
                exec(compile(source.replace(PENDING_ENTRY[0], PENDING_ENTRY[1]), __file__, "exec"), mod.__dict__)
                print(f"build-records: {plant} · the module imports with exception pending on ARCH-tKinds-9")
            except ImportError as exc:
                bad.append(f"the import refused a pending entry: {exc}")
                mod = None
            if mod is not None:
                folder = root / "memory/builds/tKinds/build"
                folder.mkdir(parents=True)
                (root / ".memory-tree.conf").write_text("MEMORY_ROOT=memory\n", encoding="utf-8")
                rec = folder / f"2026-01-01-build-{unit}-exception-1.md"
                rec.write_text(f"# {unit} exception 1 — t\n\n**Serves:** exception {unit}\n", encoding="utf-8")
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    rc = mod.main(["read", str(rec)])
                if rc != 2 or "pending on ARCH-tKinds-9" not in buf.getvalue():
                    bad.append(f"read exited {rc}, not 2 naming the unit: {buf.getvalue().strip()[:200]}")
                held = sorted(p.name for p in folder.iterdir())
                try:
                    mod.write_record(root, "tKinds", unit, "exception", "t", [("Caused-by", unit)])
                    bad.append("write_record wrote a pending kind")
                except ValueError as exc:
                    if "pending on ARCH-tKinds-9" not in str(exc):
                        bad.append(f"write_record refused without naming the unit: {exc}")
                if sorted(p.name for p in folder.iterdir()) != held:
                    bad.append("write_record wrote a file for a pending kind")
                print(f"build-records: {plant} · read exited {rc}; write_record refused, writing nothing")
        finally:
            remove_tree(root)
        for why in bad:
            print(f"build-records: FAIL {plant} · {why}")
        if bad:
            return 1
        print(f"build-records: PASS {plant} — the import, read and write_record each hold a pending kind")
        return 0
    try:
        with set_env_aside(GIT_ENV_LEAKS):
            def run_git(*args):
                return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, encoding="utf-8",
                                      check=True).stdout
            run_git("init", "-q", "--template=")
            with open(root / ".memory-tree.conf", "w", encoding="utf-8", newline="\n") as fh:
                fh.write('MEMORY_ROOT=memory\nFAMILIES="arch:ARCH"\n')
            spec = root / "memory/builds/tKinds/spec/2026-01-01-spec-ARCH-tKinds-1.md"
            spec.parent.mkdir(parents=True)
            with open(spec, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(f"# {unit} — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01 · node a · Tier-2 · "
                         "base 0123abcd\n")
            # the override door reads `charter.override` at the landed revision, so main holds a commit
            run_git("symbolic-ref", "HEAD", "refs/heads/main")
            run_git("add", "-A")
            run_git("-c", "user.name=fx", "-c", "user.email=fx@example.invalid", "-c", "commit.gpgsign=false",
                    "commit", "-qm", "the fixture build", "-m", f"{RED_FIX_TRAILER}: {DOOR_ARGV['red-fix'][1][1]}")
            if plant == "red-fix-join":   # TOOL-aNimbleMend-9 S7: the door's refusals and each finding of the join
                leg, folder = DOOR_ARGV["red-fix"][1][1], root / "memory/builds/tKinds/build"
                door = ["--leg", leg, "--red-line", "FAIL the fixture leg", "--rerun", "the fixture leg · green"]
                cases = [0]

                def run_join(*flags):
                    p = subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve()), "join", "red-fix",
                                        "--root", str(root), *flags], capture_output=True, text=True, encoding="utf-8")
                    return p.returncode, (p.stdout + p.stderr).strip()

                def write_commit(subject, *trailers, verb=("commit", "-q")):
                    run_git("add", "-A")
                    run_git("-c", "user.name=fx", "-c", "user.email=fx@example.invalid", "-c", "commit.gpgsign=false",
                            *verb, "-m", subject, *(x for t in trailers for x in ("-m", t)))
                    return run_git("rev-parse", "HEAD").strip()

                def check_case(case, got, rc, *needles):
                    """One case: the exit, and one printed line holding every needle."""
                    line = next((ln for ln in got[1].splitlines() if all(n in ln for n in needles)), None)
                    cases[0] += 1
                    if got[0] != rc or line is None:
                        bad.append(f"{case}: exited {got[0]}, not {rc} with one line holding {' and '.join(needles)}: "
                                   f"{got[1][:400]}")
                    print(f"build-records: {plant} · {case} · exit {got[0]} · {line}")

                fix = run_git("rev-parse", "HEAD").strip()
                check_case("owed at HEAD", run_join(), 0, "owed", fix[:8], leg)
                check_case("staged, unrecorded at HEAD", run_join("--staged"), 1, "J1", fix[:8])
                rc, said = run_door(root, "red-fix", unit, door + ["--commit", fix[:8]])
                rel = (re.search(r"wrote (\S+)", said) or [None, ""])[1]
                rec = read_red_fix(rel, (root / rel).read_bytes().decode("utf-8")) if rc == 0 and rel else {}
                files = ".memory-tree.conf, memory/builds/tKinds/spec/2026-01-01-spec-ARCH-tKinds-1.md"
                cases[0] += 1
                if rec.get("Commit") != fix or rec.get("Files") != files or rec.get("malformed"):
                    bad.append(f"door: exited {rc} from the rev {fix[:8]} and wrote Commit {rec.get('Commit')}, Files "
                               f"{rec.get('Files')}, malformed {rec.get('malformed')}: {said.strip()[:200]}")
                print(f"build-records: {plant} · door · exit {rc} · from {fix[:8]} · Commit {rec.get('Commit')} · "
                      f"Files {rec.get('Files')}")
                if not bad:
                    run_git("add", "--", rel)
                    check_case("staged, recorded at HEAD", run_join("--staged"), 0, "1 fix commit(s)")
                    plain = write_commit("the record")
                    check_case("clean", run_join(), 0, "1 fix commit(s) · 1 record(s) · 0 owed")
                    # TOOL-aClearedLedger-9 S5: a path-less fix commit owes no record, at HEAD and below it
                    bare = write_commit("an empty fix", f"{RED_FIX_TRAILER}: {leg}", verb=("commit", "-q", "--allow-empty"))
                    check_case("path-less at HEAD", run_join(), 0, "path-less", bare[:8], leg)
                    check_case("staged, path-less at HEAD", run_join("--staged"), 0, "path-less", bare[:8], leg)
                    for case, flags, why in (
                            ("a commit with no trailer", door + ["--commit", plain[:8]], ""),
                            ("a --leg no trailer names", ["--leg", "another leg", *door[2:], "--commit", fix[:8]], ""),
                            ("a rev that names no commit", door + ["--commit", "no-such-rev"], ""),
                            ("a commit that touches no path", door + ["--commit", bare[:8]], "owes no red-fix record")):
                        rc, said = run_door(root, "red-fix", unit, flags)
                        held = len(list(folder.glob("*-red-fix-*.md")))
                        cases[0] += 1
                        if rc != 1 or held != 1 or why not in said:
                            bad.append(f"refusal, {case}: exited {rc}, not 1, with {held} record(s), not 1"
                                       f"{', saying ' + why if why else ''}: {said.strip()[:200]}")
                        print(f"build-records: {plant} · refusal · {case} · exit {rc} · {held} record(s)")
                    run_git("checkout", "-q", "-b", "side")
                    (root / "side.txt").write_text("a side branch\n", encoding="utf-8")
                    write_commit("a side commit")
                    run_git("checkout", "-q", "main")
                    write_commit("a merge carrying the trailer", f"{RED_FIX_TRAILER}: {leg}",
                                 verb=("merge", "-q", "--no-ff", "side"))
                    (root / "after.txt").write_text("one commit on the merge\n", encoding="utf-8")
                    write_commit("one commit on two path-less fixes")
                    check_case("path-less below HEAD", run_join(), 0, "0 owed · 2 path-less")
                    text = (root / rel).read_bytes().decode("utf-8")
                    twin = rel.replace("-red-fix-1.md", "-red-fix-2.md")
                    for case, old, new, needles in (
                            ("J2, a record naming a path-less commit", fix, bare, (rel, bare)),
                            ("J4", "- **Files:** .memory-tree.conf, ", "- **Files:** ", (rel,)),
                            ("J3", f"- **Leg:** {leg}", "- **Leg:** another leg", (rel, leg)),
                            ("J2", fix, "0" * 40, (rel, "0" * 40)),
                            ("J6", "- **Rerun:** the fixture leg · green\n", "", (rel, "Rerun is missing")),
                            ("J5", None, None, (rel, twin))):
                        if old is not None and old not in text:
                            bad.append(f"{case}: the record does not hold {old!r}, so the plant stages nothing")
                        with open(root / (rel if old is not None else twin), "w", encoding="utf-8", newline="\n") as fh:
                            fh.write(text.replace(old, new) if old is not None else text)
                        run_git("add", "-A")
                        check_case(case, run_join(), 1, f"· {case[:2]} ·", *needles)
                        if old is None:
                            run_git("rm", "-qf", "--", twin)
                        with open(root / rel, "w", encoding="utf-8", newline="\n") as fh:
                            fh.write(text)
                    (root / "fixed.txt").write_text("a second fix\n", encoding="utf-8")
                    late = write_commit("a second fix", f"{RED_FIX_TRAILER}: {leg}")
                    (root / "later.txt").write_text("one more commit\n", encoding="utf-8")
                    write_commit("one more commit on an unrecorded fix")
                    check_case("J1", run_join(), 1, "· J1 ·", late[:8], leg)
                for why in bad:
                    print(f"build-records: FAIL {plant} · {why}")
                if not bad:
                    print(f"build-records: PASS {plant} — {cases[0]} cases: the door, its refusals, owed, --staged, "
                          f"path-less and J1 to J6")
                return 1 if bad else 0
            if plant == "recommendation":   # TOOL-dDeclaredLoop-22 AC1: the door, its refusals, the bindings
                bad += check_recommendation_plant(root, unit, run_git)
                for why in bad:
                    print(f"build-records: FAIL {plant} · {why}")
                if not bad:
                    print(f"build-records: PASS {plant} — a score record, the reason answering it, five refusals "
                          f"writing nothing, and both bound")
                return 1 if bad else 0
            try:
                read_override_value(root)
                unarmed = set()
            except ValueError as exc:
                print(f"build-records: {plant} · unarmed · the override door needs a policy kit: {exc}")
                unarmed = {"override"}
            for kind in TYPED_RECORD_KINDS:
                if kind in DOORS and kind not in unarmed:
                    rc, said = run_door(root, kind, unit, DOOR_ARGV[kind][0])
                    got = re.search(r"wrote (\S+)", said)
                    if rc != 0 or not got:
                        bad.append(f"{kind}: new {kind} exited {rc}")
                        continue
                    written[kind] = got.group(1)
                    for other in (d for d in DOORS if d not in (kind, *unarmed)):
                        rc, said = run_door(root, kind, unit, DOOR_ARGV[kind][0] + DOOR_ARGV[other][1])
                        if rc != 2:
                            bad.append(f"{kind}: new {kind} took {other}'s {DOOR_ARGV[other][1][0]}, exiting {rc}")
                else:
                    written[kind] = write_record(root, "tKinds", unit, kind, "the typed-kinds round trip",
                                                 [("Caused-by", unit)])
            # PLAY-dOrderedCharter-49 S53: a value forging a field and a --rule the catalogue lacks each refuse,
            # exit 1, naming why, and write nothing
            held = sorted(p.name for p in (root / "memory/builds/tKinds/build").glob("*.md"))
            refusals = [("exception", DOOR_ARGV["exception"][0][:4] + ["--reason", "a\nExpires: 2099-01-01"],
                         "cannot forge a field"),
                        ("override", ["--rule", "practice.verify", "--words", "**Value:** owner", "--session", "fx"],
                         "cannot forge a field"),
                        ("override", ["--rule", "practice.nosuch", "--words", "w", "--session", "fx"],
                         "names no practice or practice rule")]
            for kind, flags, why in refusals:
                if kind in unarmed:
                    continue
                rc, said = run_door(root, kind, unit, flags)
                if rc != 1 or why not in said:
                    bad.append(f"{kind}: {flags[-3:]} exited {rc}, not 1 naming `{why}`: {said.strip()[:200]}")
            if sorted(p.name for p in (root / "memory/builds/tKinds/build").glob("*.md")) != held:
                bad.append("a refused door wrote a record")
            # PLAY-dOrderedCharter-70 S4: a research record whose name holds `-change-` is no change record
            research = "memory/builds/tKinds/build/2026-01-01-build-ARCH-tKinds-1-change-plan-2.md"
            with open(root / research, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(f"# {unit} — a change plan\n\n**Serves:** research {unit}\n")
            run_git("add", "-A")
            changes = [r["path"] for r in read_changes(root)]
            if research in changes or changes != [written.get("change")]:
                bad.append(f"read_changes selected {changes}, not the change record alone")
            bad += check_bindings(root, plant, list(written.items()), run_git)
    except (subprocess.CalledProcessError, OSError, ValueError) as exc:
        bad.append(f"the fixture could not be built: {exc}")
    finally:
        remove_tree(root)
    for why in bad:
        print(f"build-records: FAIL {plant} · {why}")
    if bad:
        return 1
    print(f"build-records: PASS {plant} — {len(written)} typed kinds bound, --print-bindings printed no A row")
    return 0


def main(argv):
    ap = argparse.ArgumentParser(prog="build_records.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run a plant's round trip over a scratch repository")
    ap.add_argument("--plant", choices=PLANTS)
    sub = ap.add_subparsers(dest="verb")
    new = sub.add_parser("new", help="write the next record of a kind through its door")
    doors = new.add_subparsers(dest="kind", required=True)
    for door in DOORS:
        one = doors.add_parser(door, allow_abbrev=False)
        one.add_argument("--build", required=True)
        one.add_argument("--unit", required=True)
        one.add_argument("--root", default=".")
    doors.choices["exception"].add_argument("--principle", required=True)
    doors.choices["exception"].add_argument("--excuses", required=True)
    doors.choices["exception"].add_argument("--reason", required=True)
    doors.choices["exception"].add_argument("--expires")
    change = doors.choices["change"]
    for flag in ("--tag", "--action", "--mark", "--before", "--after"):
        change.add_argument(flag, required=True)
    change.add_argument("--successor")
    change.add_argument("--promoted-from")
    for flag in ("--rule", "--words", "--session"):
        doors.choices["override"].add_argument(flag, required=True)
    for flag in ("--leg", "--red-line", "--commit", "--rerun"):
        doors.choices["red-fix"].add_argument(flag, required=True)
    for flag in ("--item", "--disposition", "--channel"):
        doors.choices["disposition"].add_argument(flag, required=True)
    doors.choices["disposition"].add_argument("--reason")
    for flag in ("--stage", "--score", "--source", "--binds", "--reason", "--role"):
        doors.choices["recommendation"].add_argument(flag, required=True)
    doors.choices["recommendation"].add_argument("--signals")
    doors.choices["recommendation"].add_argument("--answers")
    read = sub.add_parser("read", help="read one record and name every refusal")
    read.add_argument("path")
    join = sub.add_parser("join", help="join every Red-fix: commit to its red-fix record, both ways")
    join.add_argument("joined", choices=("red-fix",))
    join.add_argument("--staged", action="store_true", help="grade HEAD alone against the records in the index")
    join.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    if args.fixture:
        if args.verb or not args.plant:
            ap.error("--fixture takes --plant <case> and no verb")
        return run_fixture(args.plant)
    if args.plant:
        ap.error("--plant takes --fixture")
    if args.verb is None:
        ap.error("a verb, new, read or join, or --fixture --plant <case>")
    if args.verb == "join":
        rc, lines = check_red_fix_join(pathlib.Path(args.root).absolute(), args.staged)
        if hasattr(sys.stdout, "reconfigure"):   # check 31 reads these lines: UTF-8 and LF whatever the host
            sys.stdout.reconfigure(encoding="utf-8", newline="\n")
        print("\n".join(lines))
        return rc
    if args.verb == "new":
        root = pathlib.Path(args.root).absolute()
        try:
            if args.kind == "change":
                rel = write_change(root, args.build, args.unit, args.tag, args.action, args.mark, args.before,
                                   args.after, DOOR_PROOF, args.successor, args.promoted_from)
            elif args.kind == "override":
                rel = write_override(root, args.build, args.unit, args.rule, args.words, args.session)
            elif args.kind == "red-fix":
                rel = write_red_fix(root, args.build, args.unit, args.leg, args.red_line, args.commit, args.rerun)
            elif args.kind == "disposition":
                rel = write_disposition(root, args.build, args.unit, args.item, args.disposition, args.channel,
                                        args.reason)
            elif args.kind == "recommendation":
                rel = write_recommendation(root, args.build, args.unit, args.stage, args.score, args.source,
                                           args.binds, args.reason, args.role, args.signals, args.answers)
            else:
                rel = write_exception(root, args.build, args.unit, args.principle, args.excuses, args.reason,
                                      args.expires)
        except (ValueError, OSError) as exc:
            print(f"build-records: refused · {exc}", file=sys.stderr)
            return 1
        print(f"build-records: wrote {rel}")
        return 0
    rel = args.path.replace("\\", "/")
    kind = next((k for k in KINDS if derive_record_name(k).search(rel)), None)
    try:
        text = pathlib.Path(args.path).read_bytes().decode("utf-8", "replace")
    except OSError as exc:
        print(f"build-records: refused · {exc}", file=sys.stderr)
        return 2
    if kind is None:
        print(f"build-records: {rel} · malformed · file name is no typed record's: " + ", ".join(KINDS))
        return 1
    if "pending" in KINDS[kind]:
        print(f"build-records: {rel} · the {kind} kind is pending on {KINDS[kind]['pending']}, which gives it fields")
        return 2
    bad = check_typed_record(rel, text, kind)
    for ln in text.replace("\r\n", "\n").split("\n"):
        if m := FIELD.match(ln):
            print(f"build-records: {rel} · {m.group(1)}: {m.group(2).strip()}")
    for key, why in bad:
        print(f"build-records: {rel} · malformed · {key} {why}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
