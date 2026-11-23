#!/usr/bin/env python3
"""loop_transition.py — a build's stage transition recorded three ways, the set `transitions.record` selects (TOOL-dDeclaredLoop-3).

    python loop_transition.py record --build <slug> --from <state> --item <tag> --outcome <o> --witness <sha>
                                     [--fact k=v]... [--field k=v]... [--root <path>]
    python loop_transition.py check --build <slug> [--root <path>]
    python loop_transition.py check --selftest
    python loop_transition.py dependents --build <slug> [--root <path>]
    python loop_transition.py progress --build <slug> --event <park|landing|transition> --detail <text> [--root <path>]
    python loop_transition.py --fixture --plant <case>

THE CHANNELS. The policy key `transitions.record`, read through the policy kit's `resolve` at one
revision per move, selects any non-empty subset of three, all three by default:

    trailer        Gov-Transition: <from> -> <to> · build=<slug> · item=<tag> · sha=<sha8>[ · <name>=<value>]...
    log            <date>-build-<anchor id>-transition-<n>.md in the build's build/ folder, written through the
                   memory-tree kit's `write_record`: Build, From, To, Item, Sha, then each extension field capitalised
    micro-format   transition — <slug> · <from> → <to> · <item tag> · <sha>, printed after the commit

`build`, `item` and `sha` come first in that order, and any other field name is one of
`TRANSITION_FIELDS`; every value matches `VALUE`, so none holds the separator. The anchor is the lowest
unit id a tracked spec H1 under the build defines. A move made before the build's first spec writes no
record, and the writer's next move after it back-fills one per earlier trailer, oldest first.

`record` (`write_transition`) reads the set at HEAD, the move's parent; answers the move by the build
table's `derive_move`, printing `refused — ...` and exiting 1 where no row holds it, and where Test's exit
into deploying (`TREE_GATED_MOVE`) carries no `--field tree=<hash>` whose full per-tree verdict, the
runner's `<common dir>/gate-verdict/<hash>`, reads GREEN (TOOL-dWitnessedBar-4 S6); resolves `--witness`
to HEAD or an ancestor of it, adding `stand-in=<owner>` where the item has a `[[stand-in]]` row and
`composition=<sha8>`, the commit HEAD names (`composition.py`, TOOL-dDeclaredLoop-26), which a `--field`
may not give; refuses a move into `designing` of a build whose claim body, as `claim.py`'s `read_claim_body`
reads this node's cache of `refs/gov/claims/<slug>`, says `disposition: patch` while `check_patch_ratified`
holds it under `patch.ratify` = `owner`, naming that key and the owner item, exit 2 (TOOL-dPlacedRequest-21
S6); adds `scenario=<tags>`, the scenarios the build runs under joined by `+`, and
`scenario-settled=<entries>` where a conflict settled, both derived by `scenario.py`'s
`derive_move_scenarios` and never given, printing `loop: scenario · unread · <why>` and recording neither
where the scenario composition at HEAD is unarmed (TOOL-dDeclaredLoop-27); refuses a staged index; where the build's previous move was pinned at another commit,
files `composition.py`'s `item-ended` orders, printing `loop: order · <path>` per order or
`loop: composition · unread · <why>` where the composition at HEAD does not answer; on a forward move
prints `adapt.py`'s path comparison, `loop: path · ...`, filing a `flow-deviation` order per deviation it
reads, and on a forward or backward move gives each pending flow change of the build its state row in
`RUN.md` under `flow.adapt`, the file staged beside the records and cut back to its length where the move
does not record (TOOL-dDeclaredLoop-28), and where a state row reads `applied` holds the composition the move
applies, its scenarios and applied changes at HEAD, to `termination.py`'s check, refusing the move on a
finding or a program `check_program` refuses, naming it (TOOL-dDeclaredLoop-33); back-fills, writes this move's record, commits the records, or an empty commit, as
`loop transition(<slug>): <from> -> <to>` with the trailer where selected, prints
`loop: recorded · <from> -> <to> · <direction> · commit <sha8>`, and prints the transition line where
`micro-format` is selected, after the progress line THE PROGRESS below names where `notify.owner` selects it. A
set storing neither the trailer nor the log writes no commit. A backward move, testing to building say,
goes through this one writer, its channels and its fields as a forward move does: the direction is
`loop_table`'s `derive_direction`, derived on every print and read, and never stored. The rework budget
rides the same records (`budget.py`, TOOL-dDeclaredLoop-30): a backward move draws `route-back`, refused
before any write where the budget is spent, save on a row reading `draws = "none"`, an ending, which draws
nothing (TOOL-dDeclaredLoop-31); and the move from `designing` to `building` writes the freeze
row, once; each row is a line after the record's fields, the build's first record copying the rows before
it. Where the move writes no record its rows take the first home that exists (TOOL-dDeclaredLoop-48):
under a set without `log`, the build's newest record, staged into the move's commit, else the trailer's
derived `BUDGET_FIELDS`, `budget=` and `draw=`, where the set holds `trailer`; else run-state lines. With
none, a route-back is refused naming the build and the freeze writes nothing.

`check` (`check_transition_channels`) holds each channel to the trailer: per trailer whose commit's set
holds `log`, one record with equal `**Key:**` fields; no record left over where its adding commit's set
holds `trailer`; and the `transition` and `progress` definitions of the micro-format fence of `AGENTS.md`
at `--root` equal to `TRANSITION_LINE` and `PROGRESS_LINE`, each found by its head word
(`check_line_definition`). A record whose adding commit's set lacks `trailer` is its move's source.
It prints each finding as `loop: transition · ...`, naming the commit, the channel and the field;
`pending — <n> move(s) before the build's first spec` while trailers wait on a spec; `unstored — ...`
where the set at HEAD stores nothing; then its summary. `read_transitions(build, repo)` is the build's
moves newest first, from the trailer where one was written and from the record otherwise, each with
its `direction` derived over this kit's definition.

THE MAIL GUARD (KICK-dKeptSession-5 S9, S10): after the set is read and before the table answers, `record`
runs the unattended driver's `--mail read <slug>` once (`read_mail_rows`, under `MAIL_GUARD_SECONDS`).
Over that read the move first acknowledges each notice it has consumed (`write_consumed_acks`,
KICK-dKeptSession-42): every open `landed`, `superseded` or `withdrawn`, and per parent with an open
`confirmed` or `changed` of subject `interfaces <parent>`, `check_parent_interfaces` once, the row its
`interface — current <id>` line names and every such row of that parent it supersedes, by content key or
by the session chain `derive_mail_chain` reads off the rows' `seq` and `after` (KICK-dKeptSession-53),
never by arrival, each by the driver's `--mail ack <slug> <id>`. To order a parent's notices the move also
reads every message that parent wrote, with `--mail read <parent> --local --sent`, from the copy its
first read fetched (KICK-dKeptSession-61), the ids it acks still the rows of its own read; a chain read
that does not answer is that parent's `mail — interfaces <parent> unread · <why>`. The acks are all or nothing
(KICK-dKeptSession-55): posted only where every open row of the read is consumed, else none, so a consumed
notice beside an open question stays open and named; a posted ack prints `mail — acked <kind> <id> from
build:<parent>` on stderr as it happens, so a move refused later still shows it, a failed ack prints `mail —
ack not posted <id> · rc <n|->` there, and a check other than confirmed or awaiting `mail — interfaces
<parent> unread · <why>`. A row
still reading `open`, a message addressed to the build or one of its units neither answered,
acknowledged nor past its deadline, refuses the move as `refused — <slug> · mail open <id> …`, exit 1,
writing nothing (`MailHeld`); where every row it holds is one whose owed ack was refused, for no
`CLAUDE_CODE_SESSION_ID` or an origin out of reach, the refusal names each ack's own cause instead,
`refused — <slug> · mail ack not posted: <id> · <the ack's first line>`, one per row joined by `; `
(KICK-dKeptSession-56 S32); a row acknowledged here is disposed by the build's next move. A message this node first saw more than its `deadline` hours ago reads `expired`
(KICK-dKeptSession-24 S5), its asker's `default` the answer, and holds nothing. `mail — off`, no driver, or a root with no `.unattended.conf` passes with one `loop: mail ·
unarmed · <why>` line; a driver no bash sees, a read silent within the bound, or a non-zero read with no
row is `loop: unanswered · mail unknown: ...`, exit 2. Past the guard, each `answered`, `acked` or
`expired` row no earlier move names is recorded in the derived field `disposed=<id>+<id>`, and where the
set holds `log` one `mailbox-message` record per id is written after the move's own record and committed
with it (`write_mail_records`). `--fixture --plant mail-open` holds the refusal over an open question on
a bare remote, `mail-disposed` the disposal after its `ack` and a second move that disposes nothing, and
`mail-expired` the disposal of a question carrying `deadline: 30`, first sighted 31 hours ago and never
answered, its record's `State` reading `expired`; `acks-landed` a `landed` the move acknowledges and
records past, `acks-confirmed` a `confirmed` whose key recomputes at the parent lease's witness acknowledged
over the real chain, `acks-superseded` a `confirmed` and the later `changed` the stood-in check names
current both acknowledged, then another parent's pair held under an unconfirmed check, and `acks-failed`
one ack across two moves, then a refused and a raising ack, each on stderr, holding the third move;
`acks-takeover` a take-over's `changed` sighted before its predecessor's `confirmed`, both acknowledged
over the real chain, the chain read the same with their `first-seen` swapped, `acks-later-key` a
later `changed` on the take-over's ref, which the chain places after the current one, holding the move
with no ack posted; `acks-withdrawn` a lone `withdrawn` acknowledged, its `mail — acked` line printed,
`acks-withdrawn-question` a `withdrawn` beside an open `question`, the move refused naming both, no ack
posted and the `withdrawn` read open after it; `acks-no-session` `acks-landed`'s move with
`CLAUDE_CODE_SESSION_ID` unset, refused naming the ack's `no session id` and the row read open after it
(KICK-dKeptSession-56 AC27); and `chain-two-dependents` a parent writing to tFix and
tTwo, its take-over's first `after` naming the row to tTwo: each dependent's move acks both its rows over
the chain read of every row the parent wrote, its chain line telling that read from tFix's rows alone,
then that sent read's four rows read `acked` and `build:fy`'s sent read refused.

THE NOTICES (KICK-dKeptSession-7 S4, S9). On a move from designing to building, after the card follow,
`write_dependency_notices` posts the build's frozen interfaces to each dependent `dependents --build <slug>`
lists, every build the "Child builds" line of its own README's rendered `<!-- gen:build-edges -->` region
names, the memory-tree kit's inversion of `parents:` (KICK-dKeptSession-44 S20), so a dependent opened
after that README's last render is not notified until the next: the driver's `--mail post <slug> --to
build:<dependent> --kind confirmed --subject "interfaces <slug>" --interface <listing> --pass <n>`, the
listing the bytes of `git ls-tree -r` over the build's `spec/` folder at the transition commit (at HEAD
where the set makes none), the body that commit's sha, and `<n>` the Design-exit ordinal, one plus the
moves from designing to building the build recorded before this one (KICK-dKeptSession-35 S1), so a
later exit is never refused as a repeat of an earlier one; `changed` where the dependent's mailbox
already holds a `confirmed` of that subject from the build. A dependent whose mailbox does not read gets
nothing and one `loop: notice · unread · <dependent> · <why>` line; a failed post prints its line and,
where it exits non-zero, `notice — not posted <kind> to build:<dependent> · rc <n> · <its first line>`;
neither fails the move. A notice refused or lost is posted again (KICK-dKeptSession-56 S33): every other
move after a Design exit runs, per dependent, the driver's `check_interface_notice` over the latest exit's
listing, posting that exit's notice again, its pass the exit's ordinal, only where the check reads
`unconfirmed`, and adding the `unread` line where it does not answer, so a dependent holding the current
interface is never posted to again. `--fixture --plant deps-notices` holds both notices' keys over a two-build
scratch, `notices-two-dependents` six posts to two dependents over three Design exits, their passes 1, 2
and 3, `notices-refused` the refused post's line under a move that still records, and `notices-reposted` a
Design exit's post to dA refused exit 2, then a later move posting it again to dA alone, both dependents
then holding a `confirmed` of pass 1.

THE PROGRESS (KICK-dKeptSession-11). The policy key `notify.owner`, read in process at HEAD through
`read_policy_value`, the read `read_record_channels` makes of its own key, selects the events an owner
hears of as `progress — <slug> · <event> · <detail>`, `PROGRESS_LINE`, which `render_progress_line`
alone fills: `NOTIFY_OWNER_EVENTS` maps `turn-micro-formats`, the default, to none, `park-and-landing` to
`park` and `landing`, `every-transition` to those and `transition`, and `park-only` to `park`. No value
pushes anything. `progress --build <slug> --event <e> --detail <text>` prints the line where the value
selects the event and nothing otherwise, exit 0; an event other than `park`, `landing` or `transition`
is refused before any read. `record` reads the key once beside the set; where it selects `transition`,
the move's line, detail `<from> → <to> · <item tag>`, is the last of its order lines, and a key that
does not resolve is one `loop: progress · unread · <why>` line there that never refuses the move.
`--fixture --plant notify-micro`, `notify-park-landing`, `notify-every` and `notify-park-only` each
record B4 under one value, `NOTIFY_SETS` committing it and `notify-micro` committing none, then run
`progress` for a park and a landing and print `loop: fixture · progress <n>`, the lines the three
printed; `notify-shape`'s `AGENTS.md` drops ` · <detail>` from the progress definition, owing `check`
one finding.

Exit: `record` 0 recorded, 1 refused by the table or held by open mail; `check` 0 clean, 1 on a finding, `pending` or
`unstored`; `dependents` 0 with one slug per line; `progress` 0, its line printed or not. Each exits 2 printing `loop: unanswered · <why>` on a value outside its grammar, a witness
that is not HEAD or its ancestor, a staged index, or a policy refusal naming `transitions.record`, an
empty set with no valid revision before it among them, or, for `dependents`, a README that does not read,
or, for `progress`, an event outside the three or a policy refusal naming `notify.owner`;
and 2 printing `loop: unarmed · <why>` where the policy or memory-tree kit does not resolve, never a default. The loop kit takes no edge to the policy
kit, which is why.

`--fixture --plant <case>` builds a scratch repository under the host temp directory holding the build
`tFix`, runs `record` and `check` there in process, prints each verdict, removes the scratch and exits
as its last verb. `field` records a `colour=red` move and a `composition=3f9c2a71` move, each refused,
then a plain move carrying its derived `composition`. `backward-rows` and `skip-backward` record `BACKWARD_MOVES`, three moves forward and
three back; the first prints every trailer and read with its direction, the second deletes the newest
record and owes its move's finding. `check --selftest` holds both definitions of `AGENTS.md` in the
current directory, then runs every plant through `run_selftest_cases`, each plant once however many
cases read it.

WHAT THIS DOES NOT CHECK: that a witness holds beyond resolving; a record's lines after its fields; a
feature- or unit-level move; a charter other than the one `AGENTS.md`; an old move's direction against
the definition at its commit, since it is derived from today's. A record pairs with a trailer by
order, the n-th owing trailer with the n-th such record, so two records swapped read as two drifts.
`progress` never checks that the event it is told of happened: it renders what its caller names.
"""
import argparse
import contextlib
import io
import pathlib
import re
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import read_definition, read_memory_tree, resolve_memory_root, run_selftest_cases  # noqa: E402
from loop_parents import read_policy_kit  # noqa: E402
from loop_table import (TransitionRefused, derive_direction, derive_move, read_stand_ins,  # noqa: E402
                        read_transition_rows)
from loop_witness import FIXTURE_REMOTE, read_git, remove_tree, resolve_commit, run_fixture_git, write_fixture_files  # noqa: E402

SAY = "loop"
KEY = "transitions.record"
#: The key selecting the events an owner hears of as a `progress —` line (KICK-dKeptSession-11 S2).
NOTIFY_KEY = "notify.owner"
TRAILER_KEY = "Gov-Transition"
KIND = "transition"
#: The rework budget's fields (`budget.py`, TOOL-dDeclaredLoop-48), `budget=frozen@<units>@<total>` and
#: `draw=<cause>@<item>@<spent>+<total>`: the writer puts a move's rows on its trailer where the set holds
#: `trailer` and no `log` and the build holds no log record, and refuses either from a `--field`.
BUDGET_FIELDS = ("budget", "draw")
#: The extension fields a trailer and a record may carry after `build`, `item` and `sha`, in the order
#: they are written; later units extend it. `composition`, `scenario`, `scenario-settled`, the
#: `BUDGET_FIELDS` and `disposed`, the mail the move disposed (KICK-dKeptSession-5 S10), are derived by
#: the writer, never given; the `mail-open` and `mail-disposed` plants hold the guard and the disposal,
#: and `mail-expired` the disposal of a question past its deadline (KICK-dKeptSession-24 S5).
TRANSITION_FIELDS = ("stand-in", "composition", "scenario", "scenario-settled") + BUDGET_FIELDS + ("tree", "disposed")
#: The mail guard's bound in seconds on the unattended driver's `--mail read` (KICK-dKeptSession-5 S9),
#: twice the kickoff engine's claims read, since the guard fetches every build's mail refs.
MAIL_GUARD_SECONDS = 30
#: The first eleven columns of one `--mail read` row, in order (KICK-dKeptSession-5 S6), which the guard
#: reads, their count the floor of a row it keeps. The row's five later columns: 12 `seq`, 13 `after` and
#: 14 `content-key` (KICK-dKeptSession-27 S4), `MAIL_ORDER_COLUMNS`, which `derive_mail_chain` and
#: `write_consumed_acks` read (KICK-dKeptSession-53 S2); then 15 `deadline` and 16 `default`
#: (KICK-dKeptSession-24 S5), which the driver judges and no row dict carries. Then the states a move
#: disposes.
MAIL_COLUMNS = ("id", "kind", "to", "state", "first-seen", "from-build", "subject", "answers", "ref", "commit", "reply")
MAIL_ORDER_COLUMNS = ("seq", "after", "content-key")
MAIL_DISPOSED_STATES = ("answered", "acked", "expired")
#: The record kind a disposed message is written as (KICK-dKeptSession-5 S12).
MAIL_KIND = "mailbox-message"
#: The move whose `tree` field must name a GREEN full per-tree verdict (TOOL-dWitnessedBar-4 S6): Test's
#: exit, `item.test.exit` from testing into deploying, and the runner's directory it reads under the
#: common dir.
TREE_GATED_MOVE = ("testing", "item.test.exit", "deploying")
VERDICT_DIR = "gate-verdict"
#: A tree hash, SHA-1 or SHA-256: the one shape that may name a file under the verdict directory.
TREE_HASH = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
#: The fields `scenario.py`'s `derive_move_scenarios` derives for each move (TOOL-dDeclaredLoop-27).
DERIVED_SCENARIO_FIELDS = ("scenario", "scenario-settled")
#: The micro-format definition `render_transition_line` fills, held equal to `AGENTS.md`'s by `check`.
TRANSITION_LINE = "transition — <slug> · <from> → <to> · <item tag> · <sha>"
#: The owner's progress line `render_progress_line` fills, held equal to `AGENTS.md`'s by `check` too, and
#: the events each `notify.owner` value reports on it, the default none (KICK-dKeptSession-11 S2).
PROGRESS_LINE = "progress — <slug> · <event> · <detail>"
NOTIFY_OWNER_EVENTS = {"turn-micro-formats": (), "park-and-landing": ("park", "landing"),
                       "every-transition": ("park", "landing", "transition"), "park-only": ("park",)}
#: Each placeholder of `TRANSITION_LINE` and the field that fills it.
LINE_FIELDS = (("<slug>", "build"), ("<from>", "from"), ("<to>", "to"), ("<item tag>", "item"), ("<sha>", "sha"))
#: The fields every trailer carries after its head, in this order.
HEAD_FIELDS = ("build", "item", "sha")
#: A field value: never a space, so never the separator.
VALUE = re.compile(r"[A-Za-z0-9._:+@-]+")
STATE = re.compile(r"[a-z0-9][a-z0-9-]*")
SHA = re.compile(r"[0-9a-f]{8,40}")
SEP = " · "
#: A spec's status header, its first word the unit's status.
STATUS_HEADER = re.compile(r"^\*\*Status:\*\* ([A-Z]+)", re.M)
#: That header's tier, the digits of its `Tier-<n>` (TOOL-dDeclaredLoop-19).
TIER_HEADER = re.compile(r"^\*\*Status:\*\* .*?\bTier-(\d+)", re.M)
FENCE =("<!-- microformats -->", "<!-- /microformats -->")
PLANTS = {"default": "the default set, one B4 move with its witness",
          "subset-trailer-line": "the set [\"trailer\", \"micro-format\"], one B4 move",
          "subset-log": "the set [\"log\"], one B4 move",
          "empty-set": "the set [], the policy file's one revision",
          "log-drift": "one B4 move, its record then edited to To: building",
          "orphan-log": "one B4 move, then a second record committed with no trailer",
          "no-row": "planning to building through item.design.exit, which no row holds",
          "line-drift": "an AGENTS.md whose definition drops <item tag>",
          "pre-spec": "a build with no spec moved once, then a spec planted and a second move",
          "field": "a move with --field colour=red, one with composition=3f9c2a71, refused as derived, then a plain move",
          "backward-rows": "B4, B5 and B7 forward, then B13, B8 and B6 back, each trailer and read printed",
          "skip-backward": "the six moves of backward-rows, then the newest record, B6's, deleted",
          "descope-spent": "flow.rework-budget = 0: B4, B5 and B7 forward, B13 back refused as spent, then "
                           "@any's descope from testing",
          "mail-open": "the driver's conf with RUN_CLAIMS on and a bare remote holding fy's question to build:tFix: "
                       "B4 refused naming it, no commit",
          "mail-disposed": "the same question and tFix's ack of it: B4 disposes it in one commit, its record read, "
                           "then B5 disposes nothing",
          "mail-expired": "the same question with deadline: 30 and default: no, first sighted 31 hours ago and "
                          "never answered: B4 disposes it as expired in one commit, its record read",
          "mail-argv": "the driver's conf with RUN_CLAIMS on and subprocess.run wrapped: B4's --mail read argv "
                       "recorded, answered zero rows, and held to the located driver and the bash that sees it",
          "mail-no-driver": "the driver's conf, the driver's locator run over an empty scratch directory: B4 "
                            "records with the mailbox unarmed",
          "mail-no-bash": "the driver's conf and resolve_bash answering None: B4 refused as mail unknown, no commit",
          "mail-read-crash": "the driver's conf and the guard's --mail read answering exit 3 with no output: B4 "
                             "refused as mail unknown naming the read's exit, no commit",
          "deps-notices": "the driver's conf with RUN_CLAIMS on, a bare remote and tDep naming tFix in parents: B5 at "
                          "an older --witness posts one confirmed to build:tDep keyed over tFix's spec listing at the "
                          "transition commit; B8 back and B5 again post changed with another key, no second confirmed",
          "notices-two-dependents": "the driver's conf with RUN_CLAIMS on, a bare remote and dA and dB naming tFix in "
                                    "parents: B5, B21 back, B5, B21 back and B5, each exit over a new spec, post one "
                                    "confirmed and two changed to each, passes 1, 2 and 3, every post posted",
          "notices-refused": "the same two dependents and the post to dA answering 1: B5 records, printing "
                             "notice — not posted confirmed to build:dA · rc 1, and dB's post is posted",
          "notices-repeat-key": "the driver's conf with RUN_CLAIMS on, a bare remote and dA alone naming tFix in "
                                "parents: B4, then B5, B21, B5, B21 and B5, the spec edited after the first B21 "
                                "alone, so the listings read A, B and B: one confirmed and two changed of one key, "
                                "passes 1, 2 and 3, every post posted",
          "notices-reposted": "the two dependents and B5's post to dA answering 2, launching nothing, then B7: "
                              "B7 posts the exit's notice again to dA alone, each dependent then holding one "
                              "confirmed of pass 1",
          "acks-landed": "the driver's conf with RUN_CLAIMS on and a bare remote holding fy's landed to build:tFix: "
                         "B4 acknowledges it and records, the read after it reading the row acked",
          "acks-confirmed": "fy's spec committed, its lease witnessing that commit and fy's confirmed keyed over its "
                            "listing there: B4 acknowledges it over the real chain and records, the row read acked",
          "acks-superseded": "the interfaces check stood in: fy's confirmed sighted, then fy's changed it names "
                             "current, B4 acking both; then fz's pair under an unconfirmed check, B5 refused",
          "acks-failed": "one landed, B4 acking it and B5 posting nothing; then two landed whose acks exit 1 and "
                         "raise LookupError, B7 refused naming both, each failure on stderr",
          "acks-takeover": "fy's spec and lease as acks-confirmed stages them: the take-over's changed b, seq 1 after "
                           "a, keyed over the listing and sighted first, then the predecessor's confirmed a: B4 acks "
                           "both over the real chain, the chain read with first-seen as read and swapped",
          "acks-later-key": "a, b after a, then c pushed onto b's ref as seq 2, the interfaces check stood in naming "
                            "b current and each ack answered posted: c unconsumed, B4 acks none and is refused "
                            "naming a, b and c",
          "acks-withdrawn": "the driver's conf with RUN_CLAIMS on and a bare remote holding fy's withdrawn to "
                            "build:tFix alone: B4 acknowledges it, printing its mail — acked line, and records",
          "acks-withdrawn-question": "fy's withdrawn and fz's question to build:tFix: B4 acks neither and is refused "
                                     "naming both, the read after it reading the withdrawn open",
          "acks-no-session": "acks-landed's landed with CLAUDE_CODE_SESSION_ID unset: B4's real ack refused, B4 "
                             "refused naming mail ack not posted and no session id, the row read open",
          "chain-two-dependents": "fy's session s-1 posting a1 confirmed to tFix and b1 to tTwo, the take-over s-2 "
                                  "a2 changed to tFix after b1 and b2 to tTwo: tFix's and tTwo's B4 each ack both "
                                  "over the chain read of every row fy wrote, then that sent read and build:fy's "
                                  "refused",
          "notify-micro": "no policy file, so notify.owner reads its default: B4, then progress park and landing, "
                          "no progress line",
          "notify-park-landing": "notify.owner = park-and-landing: B4, then progress park and landing, two lines",
          "notify-every": "notify.owner = every-transition: B4's progress line, then park and landing, three lines",
          "notify-park-only": "notify.owner = park-only: B4, then progress park and landing, the park line alone",
          "notify-shape": "an AGENTS.md whose progress definition drops <detail>: one B4 move, then the check"}
#: The mail plants' messages, each `(ref, build, id, to, kind, subject, answers)`, put straight on the fixture's
#: remote; `mail-disposed` adds the ack. `mail-expired` writes the question with `FX_DEADLINE`'s two keys and
#: its first sighting `FX_SIGHTED_HOURS` back in the fixture's feed, past the 30-hour deadline.
FX_QUESTION = ("refs/gov/mail/fy/z/s-other", "fy", "a1b2c3d4e5f6", "build:tFix", "question", "the fixture's question", "none")
FX_ACK = ("refs/gov/mail/tFix/z/s-fx", "tFix", "0f1e2d3c4b5a", "build:fy", "ack", "the fixture's question", "a1b2c3d4e5f6")
FX_DEADLINE = {"deadline": "30", "default": "no"}
FX_SIGHTED_HOURS = 31
#: The moves the backward plants record in order, each an argv tail for `record` before its witness.
BACKWARD_MOVES = (("--from", "planning", "--item", "item.plan.exit", "--outcome", "recorded"),
                  ("--from", "designing", "--item", "item.design.exit", "--outcome", "recorded"),
                  ("--from", "building", "--item", "item.build.exit", "--outcome", "recorded"),
                  ("--from", "testing", "--item", "item.test.attribute", "--outcome", "code-miss"),
                  ("--from", "building", "--item", "item.build.unit-pass", "--outcome", "spec-wrong"),
                  ("--from", "designing", "--item", "item.design.decompose", "--outcome", "goal-fork"))
#: The plants' policy values, committed as `.governance/policy.toml`; a plant not here commits none.
PLANT_SETS = {"subset-trailer-line": '["trailer", "micro-format"]', "subset-log": '["log"]', "empty-set": "[]"}
#: The notify plants' `notify.owner` values, committed as `.governance/policy.toml` `[notify]`; `notify-micro`
#: commits none, so the catalogue default answers (KICK-dKeptSession-11 S9).
NOTIFY_SETS = {"notify-park-landing": "park-and-landing", "notify-every": "every-transition",
               "notify-park-only": "park-only"}
FX_BUILD = "tFix"
FX_UNIT = "TOOL-tFix-1"
FX_SPEC = "memory/builds/tFix/spec/2026-01-01-spec-%s.md" % FX_UNIT
#: The `deps-notices` plant's dependent, whose README names `FX_BUILD` in `parents:` (KICK-dKeptSession-7 AC7),
#: and the session its posts run as. `FX_BUILD`'s README then holds the region `render_edges` renders over
#: its dependents (KICK-dKeptSession-44 S20).
FX_DEPENDENT = "tDep"
FX_SESSION = "s-notice"
#: The two dependents of the `notices-` plants (KICK-dKeptSession-35 AC1, AC3), each README naming `FX_BUILD`.
FX_DEPENDENTS = ("dA", "dB")


# ------------------------------------------------------------------------------------------ the grammar
def render_transition_trailer(fields):
    """`Gov-Transition: <from> -> <to> · build=<slug> · item=<tag> · sha=<sha>`, then each extension field
    `fields` carries as ` · <name>=<value>`, in `TRANSITION_FIELDS` order."""
    names = HEAD_FIELDS + tuple(n for n in TRANSITION_FIELDS if n in fields)
    return "%s: %s -> %s%s" % (TRAILER_KEY, fields["from"], fields["to"],
                               "".join("%s%s=%s" % (SEP, n, fields[n]) for n in names))


def parse_transition_trailer(value):
    """The fields of one `Gov-Transition` value, `from` and `to` first; ValueError naming what is outside
    the grammar."""
    parts = value.split(SEP)
    head = re.fullmatch(r"(\S+) -> (\S+)", parts[0])
    if not head or not all(STATE.fullmatch(s) for s in head.groups()):
        raise ValueError("the head %r is not <from> -> <to>, each one state word" % parts[0])
    fields = {"from": head.group(1), "to": head.group(2)}
    for part in parts[1:]:
        name, eq, v = part.partition("=")
        if not eq or name in fields:
            raise ValueError("the field %r is not one <name>=<value> named once" % part)
        fields[name] = v
    names = list(fields)[2:]
    if names[:3] != list(HEAD_FIELDS):
        raise ValueError("the fields open %s, not build, item and sha in that order" % " ".join(names[:3]))
    extra = [n for n in names[3:] if n not in TRANSITION_FIELDS]
    if extra:
        raise ValueError("the field %s is no registered extension field: %s" % (extra[0], " ".join(TRANSITION_FIELDS)))
    bad = [n for n in names if not VALUE.fullmatch(fields[n])] + [n for n in ("sha",) if not SHA.fullmatch(fields[n])]
    if bad:
        raise ValueError("the value of %s is outside its grammar: %r" % (bad[0], fields[bad[0]]))
    return fields


def render_transition_line(fields):
    """The micro-format line of one move: `TRANSITION_LINE` with each placeholder filled from `fields`."""
    line = TRANSITION_LINE
    for placeholder, name in LINE_FIELDS:
        line = line.replace(placeholder, fields[name])
    return line


def render_record_key(name):
    """A field name as a record's `**Key:**`: `stand-in` reads `Stand-in`."""
    return name[:1].upper() + name[1:]


def render_progress_line(slug, event, detail):
    """The owner's progress line, the one producer: `PROGRESS_LINE` with its three placeholders filled."""
    return PROGRESS_LINE.replace("<slug>", slug).replace("<event>", event).replace("<detail>", detail)


def derive_owner_events(value):
    """The events a `notify.owner` value reports, from `NOTIFY_OWNER_EVENTS`. ValueError on a value the
    map does not hold."""
    if value not in NOTIFY_OWNER_EVENTS:
        raise ValueError("%s reads %r, which names no events: %s" % (NOTIFY_KEY, value, " ".join(NOTIFY_OWNER_EVENTS)))
    return NOTIFY_OWNER_EVENTS[value]


def check_line_definition(root, line):
    """The findings of the definition of `line`, found by its head word, in the micro-format fence of
    `AGENTS.md` at `root` against `line`: none where one definition equals it."""
    head = line.split(" ", 1)[0]
    try:
        text = (pathlib.Path(root) / "AGENTS.md").read_bytes().decode("utf-8", "replace")
    except OSError as e:
        return ["definition · AGENTS.md does not read: %s" % e.strerror]
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    if FENCE[0] not in lines or FENCE[1] not in lines[lines.index(FENCE[0]):]:
        return ["definition · AGENTS.md holds no %s fence, so the renderer's %s is defined nowhere" % (
            FENCE[0], line)]
    start = lines.index(FENCE[0])
    held = [ln[3:-1] for ln in lines[start:lines.index(FENCE[1], start)]
            if ln.startswith("- `%s — " % head) and ln.endswith("`")]
    if not held:
        return ["definition · the micro-format fence of AGENTS.md defines no %s line; the renderer "
                "writes %s" % (head, line)]
    return ["definition · AGENTS.md reads %s, while the renderer writes %s" % (d, line)
            for d in held if d != line]


# ------------------------------------------------------------------------------------------ the reads
def read_policy_value(root, key, rev):
    """The value the policy key `key` resolves to at `rev`. ValueError naming the key on a policy refusal;
    LookupError where the policy kit does not resolve."""
    policy, _guard = read_policy_kit()
    try:
        return policy.resolve(key, str(root), rev).value
    except policy.Refusal as e:
        raise ValueError("%s does not resolve at %s: %s" % (key, rev, e)) from None


def read_record_channels(root, rev):
    """The channel set `transitions.record` selects at `rev`, a frozenset. ValueError naming the key on a
    policy refusal; LookupError where the policy kit does not resolve."""
    return frozenset(read_policy_value(root, KEY, rev))


def read_cached_channels(root, rev, cache):
    """`read_record_channels` once per revision, `cache` keyed by the revision as given."""
    if rev not in cache:
        cache[rev] = read_record_channels(root, rev)
    return cache[rev]


def resolve_build_anchor(build, root):
    """The lowest unit id a tracked spec H1 under `build` defines, by its number, or None."""
    ids = read_build_unit_ids(build, root)
    return min(ids, key=lambda i: (int(i.rsplit("-", 1)[1]), i), default=None)


def read_build_unit_ids(build, root):
    """The unit ids the tracked spec H1s under `build` define, in `git ls-files` order: the anchor's walk,
    and the units the rework budget counts at its freeze (`budget.py`)."""
    return [uid for uid, _status in read_build_specs(build, root)]


def read_build_specs(build, root):
    """`[(unit id, status)]` of each tracked spec H1 under `build`, in `git ls-files` order: the status the
    word its `**Status:**` header opens with, empty where it carries none, `read_build_headers`' pairs.
    `budget.py`'s ending reads the statuses (TOOL-dDeclaredLoop-31)."""
    return [(uid, status) for uid, status, _tier in read_build_headers(build, root)]


def read_build_headers(build, root):
    """`[(unit id, status, tier)]` of each tracked spec H1 under `build`, in `git ls-files` order: the status
    the word its `**Status:**` header opens with, the tier the digits of that header's `Tier-<n>`, each empty
    where the header carries none. `breakpoints.py` reads the tiers (TOOL-dDeclaredLoop-19)."""
    read_memory_tree("tree_lib.py")
    from design_lib import read_design_conf, read_tracked_builds
    from tree_lib import parse_spec_h1
    conf = read_design_conf(root)
    memory_root = resolve_memory_root(root)
    families = [p.split(":", 1)[1] for p in conf.get("FAMILIES", "").split() if ":" in p]
    prefix = "%s/builds/%s/spec/" % (memory_root, build)
    ids = []
    for rel in read_tracked_builds(root, memory_root):
        path = pathlib.Path(root, rel)
        if rel.startswith(prefix) and rel.endswith(".md") and path.is_file():
            text = path.read_bytes().decode("utf-8", "replace")
            hit = parse_spec_h1(rel, text, memory_root, families)
            if hit:
                status, tier = STATUS_HEADER.search(text), TIER_HEADER.search(text)
                ids.append((hit[1], status.group(1) if status else "", tier.group(1) if tier else ""))
    return ids


def read_transition_commits(build, root):
    """`([(commit, fields)], findings)`: every commit reachable from HEAD carrying a `Gov-Transition`
    trailer whose `build` is `build`, oldest first, read by the memory-tree kit's `read_commits`; a
    trailer outside the grammar and a commit carrying two are findings."""
    read_memory_tree("commit_trailers.py")
    from commit_trailers import read_commits
    commits = read_commits(str(root), ["--grep=^%s: " % TRAILER_KEY, "HEAD"], [TRAILER_KEY])
    out, findings = [], []
    for c in reversed(commits):
        values = [v for v in c["trailers"][TRAILER_KEY] if v]
        mine = [v for v in values if "build=%s" % build in v.split(SEP)]
        if not mine:
            continue
        if len(values) > 1:
            findings.append("commit %s · trailer · carries %d %s trailers, and a transition commit carries one" % (
                c["sha"][:8], len(values), TRAILER_KEY))
        try:
            out.append((c, parse_transition_trailer(mine[0])))
        except ValueError as e:
            findings.append("commit %s · trailer · %s" % (c["sha"][:8], e))
    return out, findings


def read_transition_records(build, root):
    """The build's transition records in its `build/` folder, by `<n>`, each read by the memory-tree
    kit's `read_transition`, with `fields`, its `**Key:**` fields under their lowercase names."""
    read_memory_tree("build_records.py")
    from build_records import read_transition
    folder = pathlib.Path(root, resolve_memory_root(root), "builds", build, "build")
    out = []
    for p in folder.glob("*-%s-*.md" % KIND) if folder.is_dir() else ():
        rec = read_transition(p.relative_to(root).as_posix(), p.read_bytes().decode("utf-8", "replace"))
        if rec["n"] is not None:
            rec["fields"] = {k.lower(): v for k, v in rec.items() if k[:1].isupper()}
            out.append(rec)
    return sorted(out, key=lambda r: r["n"])


def read_transition_moves(build, root, cache):
    """The build's moves as its channels hold them: `trailers` `[(commit, fields)]` oldest first, `owing`
    those whose commit's set holds `log`, `paired` the records whose adding commit's set holds `trailer`
    (the n-th pairs with the n-th owing trailer), `sourced` the rest, each its move's source, `adding`
    `{record path: its adding commit}`, and `findings`."""
    read_memory_tree("tree_lib.py")
    from tree_lib import read_adding_commits
    trailers, findings = read_transition_commits(build, root)
    records = read_transition_records(build, root)
    glob = "%s/builds/%s/build/*-%s-*.md" % (resolve_memory_root(root), build, KIND)
    adding = read_adding_commits(str(root), glob, [r["path"] for r in records])
    paired = [r for r in records if "trailer" in read_cached_channels(root, adding.get(r["path"], "HEAD"), cache)]
    return {"trailers": trailers, "owing": [(c, t) for c, t in trailers
                                            if "log" in read_cached_channels(root, c["sha"], cache)],
            "paired": paired, "sourced": [r for r in records if r not in paired], "adding": adding,
            "findings": findings}


def read_transitions(build, repo):
    """The build's recorded moves, newest first: each the fields of its trailer, or of its record where
    the move wrote no trailer, with `commit`, `source` (`trailer` or `log`) and `direction`, derived on
    read by `derive_direction` over this kit's definition and never stored. ValueError or OSError where a
    read is refused; LookupError where a kit does not resolve."""
    root = pathlib.Path(repo).absolute()
    tables = read_transition_rows(*read_definition(KIT))
    moves = read_transition_moves(build, root, {})
    out = [dict(t, commit=c["sha"], source="trailer") for c, t in moves["trailers"]]
    if moves["sourced"]:
        order = read_git(root, "rev-list", "--reverse", "HEAD")[1].split()
        at = {sha: n for n, sha in enumerate(order)}
        out += [dict(r["fields"], commit=moves["adding"].get(r["path"]), source="log") for r in moves["sourced"]]
        out.sort(key=lambda m: at.get(m["commit"], len(at)))
    for m in out:
        m["direction"] = derive_direction(m.get("from"), m.get("to"), tables)
    return out[::-1]


# ------------------------------------------------------------------------------------------ the writer
class TreeUnverified(TransitionRefused):
    """Test's exit asked for a tree no GREEN full per-tree verdict covers; the message names the tree."""

    def __init__(self, tree, why):
        Exception.__init__(self, "%s · tree %s: %s" % (TREE_GATED_MOVE[1], tree or "-", why))


def check_tree_verdict(root, tree):
    """None where the runner's full per-tree verdict `<common dir>/gate-verdict/<tree>` in the repository
    at `root` reads `verdict GREEN` for `tree`; else why not. WHAT IT DOES NOT CHECK: that `tree` is the
    one `verdict.tree` selects, the prepared merge's or the build tip's; the caller names it."""
    if not tree:
        return "the move names no tree; give --field tree=<tree hash>"
    if not TREE_HASH.fullmatch(tree):
        return "%s is no tree hash" % tree
    rc, common = read_git(root, "rev-parse", "--path-format=absolute", "--git-common-dir")
    if rc != 0 or not common:
        return "the git common dir of %s does not resolve" % root.as_posix()
    path = pathlib.Path(common, VERDICT_DIR, tree)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return "no full per-tree verdict at %s" % path.as_posix()
    keys = dict(ln.split("\t", 1) for ln in text.splitlines() if "\t" in ln)
    if keys.get("tree") != tree:
        return "%s names tree %s" % (path.as_posix(), keys.get("tree") or "none")
    if keys.get("verdict") != "GREEN":
        return "%s reads verdict %s, not GREEN" % (path.as_posix(), keys.get("verdict") or "none")
    return None


class MailHeld(TransitionRefused):
    """A message addressed to the build is open, neither answered, acknowledged nor past its deadline
    (KICK-dKeptSession-5 S9, KICK-dKeptSession-24 S5); the message names the build and every open id. Where
    `refused`, the causes `write_consumed_acks` recorded by id, holds every one of `ids`, each row is held
    only because the ack the move owed it was refused, and the message names each ack's own cause instead,
    `mail ack not posted: <id> · <the ack's first line>`, joined by `; ` (KICK-dKeptSession-56 S32): a
    missing session id or an unreachable origin is said, never read as an open question."""

    def __init__(self, build, ids, refused=None):
        refused = refused if isinstance(refused, dict) else {}
        if ids and all(i in refused for i in ids):
            Exception.__init__(self, "%s · %s" % (build, "; ".join(
                "mail ack not posted: %s · %s" % (i, refused[i]) for i in ids)))
        else:
            Exception.__init__(self, "%s · mail open %s · a message addressed to the build holds its moves until it "
                                     "is answered, acknowledged or past its deadline" % (build, " ".join(ids)))


def read_mail_rows(root, build, local=False, sent=False):
    """The build's mailbox as the unattended driver's `--mail read <build>` prints it, run in `root` with stdin
    closed, under `read_clean_env()` and `MAIL_GUARD_SECONDS`, the bash `resolve_bash`'s, as `write_card_follow`
    runs the engine: `(rows, unarmed)`, each row a dict of `MAIL_COLUMNS`, then of `MAIL_ORDER_COLUMNS`
    where the row holds them, the order `derive_mail_chain` and `write_consumed_acks` read
    (KICK-dKeptSession-53 S2), a row of fewer than `len(MAIL_COLUMNS)` fields dropped, `unarmed` why the mailbox was not
    read or None. Unarmed: the driver's locator answering LookupError, a `root` with no `.unattended.conf`,
    which launches nothing, and `mail — off`. ValueError, `mail unknown: ...`, for a driver no bash sees, a
    read silent within the bound, and any other non-zero read with no row: unknown, never none. `local`
    appends `--local`, a read of the node's cache with no fetch, which the position engine's
    `read_mail_interrupts` passes for its `--local` (KICK-dKeptSession-10); the transition guard passes none.
    `sent` appends `--sent` after it, the rows of every message the build `build` wrote, whoever it was
    addressed to, each state as the reader decides it (KICK-dKeptSession-61 S1), which `write_consumed_acks`
    passes with `local` for a parent's chain; a `build` that is no slug then exits 2, a `ValueError`."""
    import subprocess
    import loop_witness
    from loop_lib import resolve_kit_dir
    try:
        driver = resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
    except LookupError as e:
        return [], str(e)
    if not pathlib.Path(root, ".unattended.conf").is_file():
        return [], "no .unattended.conf at %s, so no driver reads its mailbox" % pathlib.Path(root).as_posix()
    bash = loop_witness.resolve_bash(driver.as_posix())
    if bash is None:
        raise ValueError("mail unknown: no bash that can see %s" % driver.as_posix())
    try:
        p = subprocess.run([bash, driver.as_posix(), "--mail", "read", build, *(["--local"] if local else []),
                            *(["--sent"] if sent else [])],
                           cwd=str(root), stdin=subprocess.DEVNULL,
                           capture_output=True, encoding="utf-8", errors="replace", timeout=MAIL_GUARD_SECONDS,
                           env=loop_witness.read_clean_env())
    except subprocess.TimeoutExpired:
        raise ValueError("mail unknown: --mail read %s printed no answer within %ds" % (build, MAIL_GUARD_SECONDS)) from None
    except OSError as e:
        raise ValueError("mail unknown: --mail read %s did not start: %s" % (build, e)) from None
    lines = [ln.rstrip("\r") for ln in p.stdout.splitlines() if ln.strip()]
    rows = [dict(zip(MAIL_COLUMNS + MAIL_ORDER_COLUMNS, ln.split("\t"))) for ln in lines
            if ln.count("\t") >= len(MAIL_COLUMNS) - 1]
    if lines[:1] == ["mail — off"]:
        return [], "mail — off"
    if p.returncode != 0 and not rows:
        raise ValueError("mail unknown: --mail read %s exited %d: %s" % (
            build, p.returncode, (lines or p.stderr.strip().splitlines() or ["no output"])[0]))
    return rows, None


def write_mail_records(root, build, anchor, rows):
    """One `mailbox-message` record per row under `anchor`, the build's anchor unit (KICK-dKeptSession-5 S12):
    its fields from the row, its body the message's text after its `key: value` block, read from the row's
    commit in `root`, in one `~~~~` fenced block. -> the records' repo-relative paths. ValueError where a
    commit does not read or the factory refuses a record."""
    read_memory_tree("build_records.py")
    from build_records import write_record
    out = []
    for r in rows:
        rc, text = read_git(root, "log", "-1", "--format=%B", r["commit"], "--")
        if rc != 0:
            raise ValueError("the message %s's commit %s does not read in %s" % (r["id"], r["commit"], root.as_posix()))
        lines = text.replace("\r\n", "\n").split("\n")
        at = next((i for i in range(2, len(lines)) if lines[i] == ""), len(lines))
        body = lines[at + 1:]
        while body and body[-1] == "":
            body.pop()
        fields = [(k.capitalize(), r[n]) for k, n in (("id", "id"), ("from", "from-build"), ("to", "to"),
                                                       ("kind", "kind"), ("subject", "subject"), ("answers", "answers"),
                                                       ("state", "state"), ("reply", "reply"), ("ref", "ref"))]
        out.append(write_record(root, build, anchor, MAIL_KIND, "%s %s" % (r["kind"], r["id"]), fields,
                                lines=["~~~~", *body, "~~~~"]))
    return out


def render_fixture_mail(build, mid, to, kind, subject, answers="none", deadline=None, default=None, content_key=None,
                        seq=None, after=None):
    """A mail commit's message as `KICK-dKeptSession-5`'s post recorded it, with no deadline, for a plant that puts
    one straight on its remote: the header, the ten keys, `from-tag` `z` and `from-session` `s-other`, and a
    one-line body; `deadline` and `default`, where given, append the two keys KICK-dKeptSession-24's post writes,
    and `content_key` a `content-key: <k>` line, the key a `confirmed` or `changed` post carries
    (KICK-dKeptSession-27 S3), which the dependency plants set (KICK-dKeptSession-7); `seq` and `after`, where
    given, a `seq: <n>` and an `after: <id>` line, the session order a post writes (KICK-dKeptSession-27 S1,
    S2), which the take-over plants set (KICK-dKeptSession-53)."""
    keys = (("id", mid), ("build", build), ("from-tag", "z"), ("from-session", "s-other"), ("to", to), ("kind", kind),
            ("item", "none"), ("pass", "none"), ("subject", subject), ("answers", answers))
    keys += tuple((k, v) for k, v in (("seq", seq), ("after", after), ("content-key", content_key),
                                      ("deadline", deadline), ("default", default)) if v is not None)
    return "gov-mail %s/%s\n\n%s\nthe fixture's message\n" % (build, mid, "".join("%s: %s\n" % kv for kv in keys))


# ------------------------------------------------------------------------------------------ the dependents
def derive_interface_listing(root, build, commit):
    """The interfaces a `confirmed` notice carries the key of (KICK-dKeptSession-7 S4, §8 F3): the bytes
    `git ls-tree -r <commit> -- <memory root>/builds/<build>/spec/` prints, run under `read_clean_env()` and
    never through `read_git`, which decodes and strips, so a key posted on one node recomputes on another.
    ValueError on a non-zero exit or a run past `MAIL_GUARD_SECONDS`."""
    import subprocess
    from loop_witness import read_clean_env
    path = "%s/builds/%s/spec/" % (resolve_memory_root(root), build)
    try:
        p = subprocess.run(["git", "ls-tree", "-r", commit, "--", path], cwd=str(root), capture_output=True,
                           stdin=subprocess.DEVNULL, env=read_clean_env(), timeout=MAIL_GUARD_SECONDS)
    except (OSError, subprocess.TimeoutExpired) as e:
        raise ValueError("the spec listing of %s at %s did not answer: %s" % (build, commit, e)) from None
    if p.returncode != 0:
        raise ValueError("the spec listing of %s at %s exited %d: %s" % (
            build, commit, p.returncode, p.stderr.decode("utf-8", "replace").strip().split("\n")[0] or "no output"))
    return p.stdout


def read_dependents(root, build):
    """Every build `build`'s own README names in its rendered `<!-- gen:build-edges -->` region
    (KICK-dKeptSession-44 S20): the link texts of the "Child builds" line the memory-tree kit's `render_edges`
    writes, the inversion of every README's `parents:` its `plan` derives, found by `GEN_REGIONS`' markers
    and that line's lead `render_edges` itself prints, sorted. No README's `parents:` is read here, so a
    dependent opened after the parent's last `gen_build_index.py --write` is listed from the next render on.
    An absent README, region or line lists none. ValueError on a README that does not read; LookupError
    where the memory-tree kit does not resolve."""
    read_memory_tree("gen_build_index.py")
    from gen_build_index import GEN_REGIONS, render_edges
    mo, mc = next((o, c) for n, o, c in GEN_REGIONS if n == "build-edges")
    lead = next(ln for ln in render_edges({"parents": [], "children": ["x"]}).split("\n") if "[x]" in ln)
    lead = lead[:lead.index("[x]")]
    readme = pathlib.Path(root) / resolve_memory_root(root) / "builds" / build / "README.md"
    try:
        text = readme.read_bytes().decode("utf-8")
    except FileNotFoundError:
        return []
    except (OSError, UnicodeDecodeError) as e:
        raise ValueError("the build %s's README does not read: %s" % (build, e)) from None
    start = text.find(mo)
    end = text.find(mc, start) if start >= 0 else -1
    lines = text[start + len(mo):end].splitlines() if end >= 0 else []
    line = next((ln.rstrip("\r") for ln in lines if ln.startswith(lead)), "")
    return sorted(re.findall(r"\[([^\]]+)\]\(", line[len(lead):]))


def check_parent_interfaces(root, slug, parent):
    """`(rc, line)` of the dependent `slug`'s confirmation of `parent`'s interfaces (KICK-dKeptSession-7 S3):
    the parent lease's `witness` by the driver's `--lease show build <parent>`; where that commit is absent
    here, one bounded `git fetch` of the claims remote; `derive_interface_listing` at it in a scratch file;
    then the driver's `check_interface_notice <slug> "interfaces <parent>" <file>`. 0 confirmed, its line;
    1 awaiting, the check's exit 1 or a witness of `-`; 2 unread, the check's exit 2, a read past
    `MAIL_GUARD_SECONDS`, a commit still absent or a listing that does not derive, naming why."""
    import os
    import subprocess
    from breakpoints import run_sourced   # it imports this module at its top, so here
    from claims import resolve_remote

    def read_driver(script, *args):
        """`(exit, its last non-empty line)` of one sourced driver call, `(2, why)` where it does not answer."""
        try:
            rc, out = run_sourced(root, script, args=args, timeout=MAIL_GUARD_SECONDS)
        except (LookupError, OSError, subprocess.TimeoutExpired) as e:
            return 2, "the driver did not answer within %ds: %s" % (MAIL_GUARD_SECONDS, str(e) or type(e).__name__)
        lines = [ln.rstrip("\r") for ln in out.splitlines() if ln.strip()]
        return rc, lines[-1] if lines else "exit %d with no output" % rc
    rc, wit = read_driver('( load_driver_conf && main --lease show build "$2" )', parent)
    if rc != 0:
        return 2, "--lease show build %s: %s" % (parent, wit)
    if wit == "-":
        return 1, "the lease of %s holds no witness" % parent
    if not SHA.fullmatch(wit):
        return 2, "--lease show build %s printed %s" % (parent, wit)
    if read_git(root, "cat-file", "-e", "%s^{commit}" % wit)[0] != 0:
        remote = resolve_remote(root)[0]
        try:
            subprocess.run(["git", "fetch", "-q", remote or "origin"], cwd=str(root), capture_output=True,
                           stdin=subprocess.DEVNULL, timeout=MAIL_GUARD_SECONDS)
        except (OSError, subprocess.TimeoutExpired):
            pass
        if read_git(root, "cat-file", "-e", "%s^{commit}" % wit)[0] != 0:
            return 2, "the witness %s of %s is not a commit here, fetched or not" % (wit[:12], parent)
    fd, name = tempfile.mkstemp(prefix="loop-interfaces-")
    os.close(fd)
    try:
        try:
            pathlib.Path(name).write_bytes(derive_interface_listing(root, parent, wit))
        except ValueError as e:
            return 2, str(e)
        rc, line = read_driver('load_driver_conf && check_interface_notice "$2" "$3" "$4"', slug,
                               "interfaces %s" % parent, pathlib.Path(name).as_posix())
    finally:
        pathlib.Path(name).unlink(missing_ok=True)
    return (rc, line) if rc in (0, 1) else (2, line)


def derive_mail_chain(rows, chain):
    """The session chain among the ids of `rows`, one parent's rows of the guard's one `read_mail_rows` read,
    those whose `from-build` is that parent, placed over the rows of `chain`, every message that parent
    wrote, whoever it was addressed to, as `read_mail_rows(root, <parent>, sent=True)` reads them
    (KICK-dKeptSession-53 S1, KICK-dKeptSession-61 S2): the set of `(earlier id, later id)` pairs, both ids
    among `rows`', so R precedes C where `(R id, C id)` is in it. Over `chain`, R precedes C where the two
    share a `ref` and R's `seq` is lower; or where the `seq` 1 row of C's ref names in `after` a row that R
    precedes or is; applied transitively, so a take-over whose `after` names its predecessor's row to
    another dependent still places that predecessor's row to this one. A row whose `seq` is no positive
    integer, a missing column or `-` included, is in no pair, so nothing places it. `first-seen` and the
    read's order are never read. Pure: no read, no launch."""
    ids = {r.get("id") for r in rows}
    placed = {}
    for r in chain:
        seq = r.get("seq") or "-"
        if r.get("id") and re.fullmatch(r"[0-9]+", seq) and int(seq) > 0:
            placed[r["id"]] = (r.get("ref") or "-", int(seq), r.get("after") or "-")
    pairs = {(a, c) for a, (ref_a, seq_a, _x) in placed.items() for c, (ref_c, seq_c, _y) in placed.items()
             if ref_a == ref_c and seq_a < seq_c}
    for c, (ref_c, _seq, _x) in placed.items():   # a session's first row names its predecessor in `after`
        pairs |= {(after, c) for ref, seq, after in placed.values() if ref == ref_c and seq == 1 and after in placed}
    while True:   # the transitive closure, which a cycle cannot make reflexive
        more = {(a, d) for a, b in pairs for c, d in pairs if b == c and a != d} - pairs
        if not more:
            return {(a, c) for a, c in pairs if a != c and a in ids and c in ids}
        pairs |= more


def write_consumed_acks(root, build, rows, refused=None):
    """The ids of `rows`, the guard's one `read_mail_rows` read of `build`'s mailbox, that the dependent's
    transition has consumed and acknowledged with exit 0 (KICK-dKeptSession-42 S1 to S3). Consumed: every
    `open` `landed`, `superseded` or `withdrawn` row; and per parent, the `from-build` of an `open` `confirmed` or `changed`
    row whose subject is `interfaces <parent>`, one `check_parent_interfaces` call, whose `rc` 0 line
    `interface — current <id> · <kind> · key <k>`, `<id>` an `open` row of the read, consumes that row and
    every `open` `confirmed` or `changed` of that parent and subject it supersedes (KICK-dKeptSession-53 S3):
    one whose `content-key` equals the current row's, or which `derive_mail_chain` over that parent's rows
    of the read places before the current row. The chain is placed over every message the parent wrote,
    whoever it was addressed to, one more read per parent so judged, `read_mail_rows(root, <parent>,
    local=True, sent=True)`, the driver's `--mail read <parent> --local --sent` over the cache the guard's
    read has just fetched (KICK-dKeptSession-61 S2), so a take-over naming its predecessor's row to another
    dependent still places that predecessor's row here, while the ids acked stay the rows of `rows`. A
    row the chain places after the current one, or cannot place at all, stays open and the guard names it;
    `first-seen` and arrival are never read. Any other answer consumes nothing from that parent: `rc` 1
    silently, any other `rc` or a raise with one `mail — interfaces <parent> unread · <line or why>` on
    stderr, and so does a chain read that raises or answers unarmed, naming its why. The acks are all or nothing (KICK-dKeptSession-55 S1, S2): the consumed ids
    are computed first, posting nothing, and posted only where every `open` row of the read is consumed, so
    the guard then holds no row but one whose ack failed; otherwise none is posted, the empty set is
    returned and the guard names every open row. Each consumed id is posted once, `--mail ack <build> <id>`
    through `breakpoints.run_sourced` under `MAIL_GUARD_SECONDS`; a post exiting 0 writes `mail — acked
    <kind> <id> from build:<parent>` on stderr as it happens, `<parent>` the row's `from-build`
    (KICK-dKeptSession-55 S3), and a post exiting non-zero, or a launch raising, writes `mail — ack not
    posted <id> · rc <n|->` there and leaves the row open. Where `refused` is a dict, each such post also
    sets `refused[<id>]` to the ack's own first output line, `mail — not written: no session id` say, or
    the raise's class and text, so the guard names the ack's cause and never only `mail open`
    (KICK-dKeptSession-56 S32). Never raises."""
    import subprocess
    from breakpoints import run_sourced   # it imports this module at its top, so here
    open_rows = [r for r in rows if r.get("state") == "open"]
    consumed = [r["id"] for r in open_rows if r.get("kind") in ("landed", "superseded", "withdrawn")]
    notices = {}
    for r in open_rows:
        parent = r.get("from-build") or ""
        if r.get("kind") in ("confirmed", "changed") and parent and r.get("subject") == "interfaces %s" % parent:
            notices.setdefault(parent, []).append(r)
    by_id = {r["id"]: r for r in open_rows}
    for parent, held in notices.items():
        try:
            rc, line = check_parent_interfaces(root, build, parent)
        except (LookupError, OSError, ValueError, subprocess.TimeoutExpired) as e:
            rc, line = None, str(e) or type(e).__name__
        if rc == 1:
            continue
        hit = re.fullmatch(r"interface — current (\S+) · (?:confirmed|changed) · key \S+", line or "") if rc == 0 else None
        if hit is None:
            if rc != 0:
                print("mail — interfaces %s unread · %s" % (parent, line), file=sys.stderr)
            continue
        current = by_id.get(hit.group(1))
        if current is None:
            continue
        try:   # KICK-dKeptSession-61 S2: every row the parent wrote, from the cache the guard's read fetched
            sent, unarmed = read_mail_rows(root, parent, local=True, sent=True)
        except (LookupError, OSError, ValueError) as e:
            sent, unarmed = None, str(e) or type(e).__name__
        if unarmed is not None:
            print("mail — interfaces %s unread · %s" % (parent, unarmed), file=sys.stderr)
            continue
        consumed.append(current["id"])
        chain = derive_mail_chain([r for r in rows if r.get("from-build") == parent], sent)
        key = current.get("content-key") or "-"
        consumed += [r["id"] for r in held
                     if (r.get("content-key") or "-") == key or (r["id"], current["id"]) in chain]
    acked = set()
    consumed = list(dict.fromkeys(consumed))   # once per id, in the order consumed
    if set(consumed) != set(by_id):   # all or nothing: another open row would hold the move, so none is posted
        return acked
    for mid in consumed:
        try:
            rc, out = run_sourced(root, '( load_driver_conf && main --mail ack "$2" "$3" )', args=(build, mid),
                                  timeout=MAIL_GUARD_SECONDS)
            cause = next((ln.rstrip("\r") for ln in (out or "").splitlines() if ln.strip()),
                         "the ack exited %s and printed nothing" % rc)
        except (LookupError, OSError, subprocess.TimeoutExpired) as e:
            rc, cause = None, "%s: %s" % (type(e).__name__, e)
        if rc != 0 and isinstance(refused, dict):
            refused[mid] = cause
        if rc == 0:
            acked.add(mid)
            print("mail — acked %s %s from build:%s" % (by_id[mid].get("kind"), mid, by_id[mid].get("from-build")),
                  file=sys.stderr)
        else:
            print("mail — ack not posted %s · rc %s" % (mid, "-" if rc is None else rc), file=sys.stderr)
    return acked


def write_dependency_notices(root, build, commit, ordinal, repost=False):
    """The notices of `build`'s frozen interfaces (KICK-dKeptSession-7 S4): per dependent of `read_dependents`,
    one post of `derive_interface_listing` at `commit` as its interface and `commit`'s full sha as its body,
    `--mail post <build> --to build:<dependent> --kind <kind> --subject "interfaces <build>" --pass <ordinal>`,
    `<kind>` `changed` where `read_mail_rows` over the dependent holds a `confirmed` row from `build` with that
    subject, else `confirmed`, and `ordinal` the Design-exit ordinal its caller counts (KICK-dKeptSession-35
    S1), so two exits never share a message id. -> the posts' lines, and after a post exiting non-zero one
    `notice — not posted <kind> to build:<dependent> · rc <n> · <the post's first line>`; a read answering
    unarmed or raising, or a raising `read_dependents`, posts nothing to whom it covers and adds one
    `loop: notice · unread · <whom> · <why>`. THE RE-POST (KICK-dKeptSession-56 S33): with `repost`, the
    caller's move is no Design exit, `commit` is the latest exit's and `ordinal` its ordinal, and per
    dependent the driver's `check_interface_notice <dependent> "interfaces <build>" <listing>` runs first
    through `run_sourced`, as `check_parent_interfaces` ends: exit 0, the dependent holds the current
    interface and is posted nothing; exit 1, `unconfirmed`, the notice above is posted again, so one a
    refused post lost is not lost; exit 2 or a raise adds the `unread` line. Never raises."""
    import subprocess
    from breakpoints import run_sourced   # it imports this module at its top, so here
    subject = "interfaces %s" % build
    try:
        dependents = read_dependents(root, build)
    except (ValueError, LookupError, OSError) as e:
        return ["%s: notice · unread · the dependents of %s · %s" % (SAY, build, e)]
    if not dependents:
        return []
    top = pathlib.Path(tempfile.mkdtemp(prefix="loop-notice-"))
    said = []
    try:
        listing, body = top / "interfaces", top / "body"
        try:
            listing.write_bytes(derive_interface_listing(root, build, commit))
            sha = resolve_commit(root, commit)
            if sha is None:
                raise ValueError("%s names no commit" % commit)
            body.write_bytes(("%s\n" % sha).encode("utf-8"))
        except (ValueError, OSError) as e:
            return ["%s: notice · unread · %s · %s" % (SAY, " ".join(dependents), e)]
        for dependent in dependents:
            if repost:   # KICK-dKeptSession-56 S33: a dependent holding the current interface is never posted again
                try:
                    rc, out = run_sourced(root, 'load_driver_conf && check_interface_notice "$2" "$3" "$4"',
                                          args=(dependent, subject, listing.as_posix()), timeout=MAIL_GUARD_SECONDS)
                    line = next((ln.rstrip("\r") for ln in out.splitlines()[::-1] if ln.strip()),
                                "exit %d with no output" % rc)
                except (LookupError, OSError, subprocess.TimeoutExpired) as e:
                    rc, line = None, "the interfaces check did not answer: %s" % (str(e) or type(e).__name__)
                if rc == 0:
                    continue
                if rc != 1:
                    said.append("%s: notice · unread · %s · %s" % (SAY, dependent, line))
                    continue
            try:
                rows, unarmed = read_mail_rows(root, dependent)
            except ValueError as e:
                rows, unarmed = [], str(e)
            if unarmed:
                said.append("%s: notice · unread · %s · %s" % (SAY, dependent, unarmed))
                continue
            kind = "changed" if any(r.get("kind") == "confirmed" and r.get("from-build") == build
                                    and r.get("subject") == subject for r in rows) else "confirmed"
            try:
                rc, out = run_sourced(root, '( load_driver_conf && main --mail post "$2" --to "$3" --kind "$4" '
                                            '--subject "$5" --interface "$6" "$7" "$8" "$9" )',
                                      args=(build, "build:%s" % dependent, kind, subject, listing.as_posix(),
                                            "--pass", str(ordinal), body.as_posix()), timeout=MAIL_GUARD_SECONDS)
            except (LookupError, OSError, subprocess.TimeoutExpired) as e:
                said.append("%s: notice · %s · the post did not answer: %s" % (SAY, dependent, str(e) or type(e).__name__))
                continue
            lines = [ln.rstrip("\r") for ln in out.splitlines() if ln.strip()]
            said += lines
            if rc != 0:   # a refused post stays visible (KICK-dKeptSession-35 S3); the move stands
                said.append("notice — not posted %s to build:%s · rc %d · %s" % (
                    kind, dependent, rc, lines[0] if lines else "no output"))
    finally:
        remove_tree(top)
    return said


def write_transition_record(root, anchor, move, lines=()):
    """The next transition record of the move's build, under `anchor`, from `move`'s fields, then `lines`,
    the rework budget's rows: its path."""
    read_memory_tree("build_records.py")
    from build_records import write_record
    names = ("build", "from", "to", "item", "sha") + tuple(n for n in TRANSITION_FIELDS if n in move)
    return write_record(root, move["build"], anchor, KIND, "%s -> %s" % (move["from"], move["to"]),
                        [(render_record_key(n), move[n]) for n in names], lines=tuple(lines))


def write_transition(root, build, state, item, outcome, witness, facts, fields):
    """Record one build move in the repository at `root`, an absolute path: `(move fields, the commit's
    sha or None, [record paths], the line or None, [order lines])`, the order lines `loop: order · <path>`
    per `item-ended` order or one `loop: composition · unread · <why>`, after a `loop: scenario · unread`
    line where the scenario composition is unarmed, then the build card follow's `card —` lines
    (`write_card_follow`, TOOL-dPlacedRequest-2 S4), a `loop: mail · unarmed` line first where the mailbox
    was not read, and on a move from designing to building the notices' lines last, each dependent's post,
    carrying `--pass <n>`, `<n>` one plus the moves from designing to building in `before` (KICK-dKeptSession-35
    S1), then a `notice — not posted <kind> to build:<dependent> · rc <n> · <its first line>` line where the
    post exits non-zero, or its `loop: notice · unread` line (`write_dependency_notices`, KICK-dKeptSession-7
    S4); on every other move after a Design exit, the latest exit's notice, at its commit and ordinal, posted
    again to each dependent whose interfaces check reads it unconfirmed (KICK-dKeptSession-56 S33), then, where `notify.owner` at HEAD selects `transition`, the move's `progress — <slug> · transition ·
    <from> → <to> · <item tag>` line, or one `loop: progress · unread · <why>` line where that key does not
    resolve, which never refuses the move (KICK-dKeptSession-11 S4). TransitionRefused where no row holds the move, `MailHeld` where a message addressed to the
    build is still open once `write_consumed_acks` has acknowledged the notices the move consumed, a
    `landed`, `superseded` or `withdrawn` row and a `confirmed` or `changed` its parent's interfaces check
    names current or supersedes (KICK-dKeptSession-42), the acks all or nothing: posted only where no other
    row is open, each posted one a `mail — acked <kind> <id> from build:<parent>` line and each failed one a
    `mail — ack not posted` line on stderr, and none where another row is open, the refusal then naming
    every open row (KICK-dKeptSession-55), save where every row it holds is one whose owed ack was refused:
    then it names each ack's cause, `mail ack not posted: <id> · <the ack's first line>` (KICK-dKeptSession-56
    S32); ValueError on a value, witness, index, policy read, tag resolver, scenario conflict or
    unknown mailbox refused, writing no record; LookupError where a kit it reads does not resolve."""
    from composition import PINNED, derive_composition_revision, read_step_composition, write_ended_orders
    from scenario import derive_move_scenarios   # it imports this module through composition.py, so here
    cache = {}
    chosen = read_cached_channels(root, "HEAD", cache)
    # the owner's progress (KICK-dKeptSession-11 S4): `notify.owner` read once at HEAD, a refusal said as one
    # `unread` line and never refusing the move
    try:
        events, unread = derive_owner_events(read_policy_value(root, NOTIFY_KEY, "HEAD")), None
    except ValueError as e:
        events, unread = (), str(e)
    # the mail guard (KICK-dKeptSession-5 S9): one read of the build's mailbox, its open rows refusing the
    # move before any write and its answered and acknowledged rows disposed below; an unarmed mailbox is a line.
    # Between the read and the refusal the move acknowledges each notice it has consumed, a landed, superseded
    # or withdrawn row and a confirmed or changed its parent's interfaces check names current or supersedes
    # (`write_consumed_acks`, KICK-dKeptSession-42): those leave the refusal, and the next move disposes of them.
    # The acks are all or nothing (KICK-dKeptSession-55): posted only where every open row is consumed, each
    # posted one a `mail — acked` line on stderr, which survives a refusal as `said` does not; else none
    said = []
    mail, unarmed = read_mail_rows(root, build)
    if unarmed:
        said.append("%s: mail · unarmed · %s" % (SAY, unarmed))
    # A row held only because its owed ack was refused is named with that ack's cause (KICK-dKeptSession-56 S32)
    refused = {}
    acked = write_consumed_acks(root, build, mail, refused) if mail else set()
    held = [r["id"] for r in mail if r.get("state") == "open" and r.get("id") not in acked]
    if held:
        raise MailHeld(build, held, refused=refused)
    data, where = read_definition(KIT)
    row, to = derive_move("build", state, item, outcome, facts, read_transition_rows(data, where))
    if to == "designing":   # a placed patch waits on its owner's ratification (TOOL-dPlacedRequest-21 S6)
        from claim import PatchHeld, check_patch_ratified, read_anchor_unit, read_claim_body
        if read_claim_body(root, build).get("disposition") == "patch":
            held = check_patch_ratified(root, build)
            if held in ("held", "rejected"):
                raise PatchHeld("patch.ratify is owner and %s's patch is %s: the owner item ratify %s, item.entry.claim "
                                "disposed ratified under %s, releases the record into designing"
                                % (build, "rejected for good" if held == "rejected" else "unratified", build,
                                   read_anchor_unit(root, build)))
    sha = resolve_commit(root, witness)
    if sha is None:
        raise ValueError("--witness %s names no commit in %s" % (witness, root.as_posix()))
    if read_git(root, "merge-base", "--is-ancestor", sha, "HEAD")[0] != 0:
        raise ValueError("--witness %s is neither HEAD nor an ancestor of it" % witness)
    move = {"from": state, "to": to, "build": build, "item": item, "sha": sha[:8]}
    for name, value in fields.items():
        if name not in TRANSITION_FIELDS:
            raise ValueError("--field %s is no registered extension field: %s" % (name, " ".join(TRANSITION_FIELDS)))
        if name == "composition":
            raise ValueError("--field composition is derived: the writer sets it to the commit HEAD names, so it "
                             "is never given")
        if name in DERIVED_SCENARIO_FIELDS:
            raise ValueError("--field %s is derived: the writer places the build's scenarios from the move's facts "
                             "and the previous move, so it is never given" % name)
        if name in BUDGET_FIELDS:
            raise ValueError("--field %s is derived: the writer places the move's rework budget rows on the trailer "
                             "where no log record holds them, so it is never given" % name)
        if name == "disposed":
            raise ValueError("--field disposed is derived: the writer sets it to the mail the move disposes, so it is "
                             "never given")
        move[name] = value
    if (state, item, to) == TREE_GATED_MOVE:
        why = check_tree_verdict(root, move.get("tree"))
        if why:
            raise TreeUnverified(move.get("tree"), why)
    owner = {r.get("item"): r.get("owner") for r in read_stand_ins(data, where)}.get(item)
    if owner:
        move["stand-in"] = owner
    move["composition"] = derive_composition_revision(root)[:8]
    before = read_transitions(build, root)
    # the disposal (KICK-dKeptSession-5 S10): each answered, acknowledged or expired message no earlier move
    # names in `disposed`, joined by `+`, so the trailer and the log record both carry it
    done = {i for m in before for i in (m.get("disposed") or "").split("+") if i}
    disposing = [r for r in mail if r.get("state") in MAIL_DISPOSED_STATES and r.get("id") not in done]
    if disposing:
        move["disposed"] = "+".join(r["id"] for r in disposing)
    placed = derive_move_scenarios(root, state, facts, before)
    if placed is None:
        said.append("%s: scenario · unread · the scenario composition at HEAD answers unarmed, so the move records "
                    "no scenario" % SAY)
    else:
        move["scenario"] = placed[0]
        if placed[1]:
            move["scenario-settled"] = placed[1]
    bad = [n for n, v in move.items() if not (isinstance(v, str) and VALUE.fullmatch(v))]
    if bad:
        raise ValueError("the value of %s, %r, is outside [A-Za-z0-9._:+@-]+" % (bad[0], move[bad[0]]))
    if read_git(root, "diff", "--cached", "--quiet")[0] != 0:
        raise ValueError("the index holds staged changes, and a transition commit carries its own records alone")
    # the rework budget (TOOL-dDeclaredLoop-30): a backward move draws `route-back`, refused here before any
    # write where the budget is spent, and the move from designing to building freezes it, once. The rows
    # are lines of this move's record, the build's first record copying the rows before them, or, where the
    # move writes no record, the first home that exists (TOOL-dDeclaredLoop-48): under a set without log
    # the build's newest record, staged into this commit, else the trailer where the set holds trailer;
    # else run-state lines. A route-back draw with no home is refused, and a freeze with none writes nothing
    from adapt import read_adapt_mode, read_pending_rows, read_run_file, write_flow_states, write_path_orders
    # budget.py imports this module, so its names are imported here
    from budget import freeze_budget, read_budget_rows, record_draw, render_budget_fields, write_budget_rows
    direction = derive_direction(state, to, read_transition_rows(data, where))
    anchor = resolve_build_anchor(build, root) if "log" in chosen else None
    records = [] if "log" in chosen else read_transition_records(build, root)
    newest = pathlib.Path(root, records[-1]["path"]) if records else None
    on_trailer = "trailer" in chosen and "log" not in chosen
    run, rows = read_run_file(root, build), []
    homed = bool(anchor or newest or on_trailer or run.is_file())
    if direction == "backward" and row.get("draws") != "none":   # an ending row draws nothing (TOOL-dDeclaredLoop-31)
        answer, drawn = record_draw(build, "route-back", item, root, lines=rows, moves=before)
        if answer == "exhausted":
            raise ValueError("the rework budget is spent, %s, so the backward move is refused and nothing is "
                             "recorded; flow.on-exhausted names the ending" % drawn)
        if rows and not homed:
            raise ValueError("%s has neither a transition log record nor a run-state file, and %s holds no trailer "
                             "to carry it, so the route-back draw has no home" % (build, KEY))
    elif (state, to) == ("designing", "building"):
        rows += [r for r in (freeze_budget(build, root),) if r and homed]
    carried = read_budget_rows(build, root, before)["carried"] if anchor and not read_transition_records(
        build, root) else []
    pin, state_read = read_step_composition(root, before)
    if state_read == PINNED and not pin.startswith(move["composition"]):
        try:
            orders, unread = write_ended_orders(root, build, before)
        except LookupError as e:   # the writer answers an unanswered resolver exit 2, `unanswered`
            raise ValueError(str(e)) from None
        said += ["%s: order · %s" % (SAY, p) for p in orders]
        said += ["%s: composition · unread · %s" % (SAY, unread)] if unread else []
    # the build's own flow changes at this boundary (TOOL-dDeclaredLoop-28): the walked path held to the
    # composition on a forward move, then each pending change given its state row in RUN.md, which rides
    # this move's commit and is cut back to its length here where the move does not record
    if direction == "forward":
        said += write_path_orders(root, build, state)
    size, written = None, []
    if direction in ("forward", "backward") and read_pending_rows(root, build):
        mode = read_adapt_mode(root)
        size = run.stat().st_size
        written = write_flow_states(root, build, mode)
    staged = [run.relative_to(root).as_posix()] if size is not None else []
    wrote, prior = [], None
    try:
        # a change applied here is held to the termination check over the composition this move applies, its
        # scenarios and its applied changes at HEAD; a finding, or a program check_program refuses, refuses the
        # move, RUN.md cut back below (TOOL-dDeclaredLoop-33)
        if any(" · applied · " in line for line in written):
            from termination import check_termination, read_termination_inputs, render_finding
            try:
                found = check_termination(read_termination_inputs(root, build, [move] + before))
            except LookupError as e:
                raise ValueError("the termination check is unarmed, so the move applying a flow change is refused: "
                                 "%s" % e) from None
            except ValueError as e:
                raise ValueError("the build's composition does not read, so the move applying a flow change is "
                                 "refused: %s" % e) from None
            if found:
                raise ValueError("the termination check refuses the move applying a flow change: %s" % "; ".join(
                    render_finding(f) for f in found))
        if "log" in chosen:
            if anchor is None and "trailer" not in chosen:
                raise ValueError("%s selects log without trailer and %s defines no spec, so the move has no record "
                                 "to write and no trailer to back-fill one from" % (KEY, build))
            if anchor:
                moves = read_transition_moves(build, root, cache)
                try:
                    for _c, t in moves["owing"][len(moves["paired"]):]:
                        wrote.append(write_transition_record(root, anchor, t, () if wrote else carried))
                    wrote.append(write_transition_record(root, anchor, move, ([] if wrote else carried) + rows))
                    # one record per disposed message after this move's own, staged by the one commit below
                    wrote += write_mail_records(root, build, anchor, disposing)
                except (ValueError, OSError):
                    for rel in wrote:
                        pathlib.Path(root, rel).unlink()
                    raise
        if rows and not wrote and newest:   # its bytes written back below where the move does not commit
            prior = newest.read_bytes()
            write_budget_rows(newest, rows, True)
            staged.append(newest.relative_to(root).as_posix())
        elif rows and not wrote and on_trailer:
            move.update(render_budget_fields(rows))
        elif rows and not wrote:
            size = run.stat().st_size if size is None else size
            write_budget_rows(run, rows, False)
            staged = [run.relative_to(root).as_posix()]
        commit = None
        if wrote or "trailer" in chosen:
            argv = ["commit", "-q", "--allow-empty", "-m", "loop transition(%s): %s -> %s" % (build, state, to)]
            argv += ["-m", render_transition_trailer(move)] if "trailer" in chosen else []
            if ((wrote or staged) and read_git(root, "add", "--", *wrote, *staged)[0] != 0) \
                    or read_git(root, *argv)[0] != 0:
                if wrote or staged:
                    read_git(root, "reset", "-q", "--", *wrote, *staged)
                for rel in wrote:
                    pathlib.Path(root, rel).unlink()
                raise ValueError("git could not commit the move in %s, so nothing is recorded" % root.as_posix())
            commit = read_git(root, "rev-parse", "HEAD")[1]
    except (ValueError, OSError):
        if size is not None:
            with open(run, "r+b") as fh:
                fh.truncate(size)
        if prior is not None:
            newest.write_bytes(prior)
        raise
    # the build's card follows the move, its last step (TOOL-dPlacedRequest-2 S4); the move stands whatever it prints
    said += write_card_follow(root, build, to, to in read_transition_rows(data, where)["terminal"])
    # Design's exit posts the frozen interfaces to each dependent (KICK-dKeptSession-7 S4), the listing at the
    # transition commit, at HEAD where the set makes none; the move stands whatever a notice prints. Its pass
    # is the Design-exit ordinal, counted off `before`, read above, never a second read (KICK-dKeptSession-35 S1)
    exits = [m for m in before if (m.get("from"), m.get("to")) == ("designing", "building")]
    if (state, to) == ("designing", "building"):
        said += write_dependency_notices(root, build, commit or "HEAD", 1 + len(exits))
    elif exits and exits[0].get("commit"):   # KICK-dKeptSession-56 S33: every other move after a Design exit
        # posts again the latest exit's notice, at its commit and ordinal, to a dependent not holding it
        said += write_dependency_notices(root, build, exits[0]["commit"], len(exits), repost=True)
    # the owner's progress line, last, where the value selects the move's event (KICK-dKeptSession-11 S4)
    if unread:
        said.append("%s: progress · unread · %s" % (SAY, unread))
    elif "transition" in events:
        said.append(render_progress_line(build, "transition", "%s → %s · %s" % (state, to, item)))
    return move, commit, wrote, render_transition_line(move) if "micro-format" in chosen else None, said


#: The kickoff engine the card follow runs, homed as the roles kit's handoff finds it (TOOL-dPlacedRequest-2 S4).
KICKOFF_HOME, KICKOFF_ENGINE = "session-kickoff", "manifest-check.sh"
#: The follow's bound in seconds: the engine's own reads and its push are each bounded inside it.
CARD_FOLLOW_BOUND_S = 120


def resolve_kickoff_engine(root):
    """The kickoff engine, an optional sibling: through the inline kit resolver from this kit, else the ONE
    file of that name `root` tracks, since gov homes that kit under `skills/`, where no probe walks. None
    when neither answers, or the index names two."""
    from loop_lib import resolve_kit_dir
    try:
        return resolve_kit_dir(KICKOFF_HOME, KICKOFF_ENGINE, KIT) / KICKOFF_ENGINE
    except LookupError:
        pass
    rc, out = read_git(root, "ls-files", "--", KICKOFF_ENGINE, "*/" + KICKOFF_ENGINE)
    hits = [ln for ln in out.splitlines() if ln.strip()] if rc == 0 else []
    return pathlib.Path(root, hits[0]) if len(hits) == 1 and pathlib.Path(root, hits[0]).is_file() else None


def write_card_follow(root, build, state, terminal):
    """The build card follows a recorded move: `manifest-check.sh --card --follow --build <build> --to <state>`,
    `--terminal` where the state is in the `terminal` set, run in `root` with stdin closed and a bound. ->
    its printed lines, or one `card — skipped:` line where no engine or bash resolves or the run does not
    answer. Never raises: the move stands whatever the card does."""
    import subprocess
    from loop_witness import read_clean_env, resolve_bash
    engine = resolve_kickoff_engine(root)
    if engine is None:
        return ["card — skipped: no kickoff engine"]
    bash = resolve_bash(engine.as_posix())
    if bash is None:
        return ["card — skipped: no bash runs the kickoff engine %s" % engine.as_posix()]
    argv = [bash, engine.as_posix(), "--card", "--follow", "--build", build, "--to", state]
    try:
        p = subprocess.run(argv + ["--terminal"] * bool(terminal), cwd=str(root), stdin=subprocess.DEVNULL,
                           capture_output=True, encoding="utf-8", errors="replace", timeout=CARD_FOLLOW_BOUND_S,
                           env=read_clean_env())
    except (OSError, subprocess.SubprocessError) as e:
        return ["card — skipped: the follow did not answer: %s" % e]
    lines = [ln for ln in p.stdout.splitlines() if ln.strip()]
    if p.returncode != 0 and not lines:
        lines = ["card — skipped: the follow exited %d: %s" % (p.returncode, (p.stderr.strip() or "no output").split("\n")[0])]
    return lines


# ------------------------------------------------------------------------------------------ the check
def check_transition_channels(build, root):
    """`(lines, findings)` of the build's channels held to its trailers, and the two definitions held to
    `TRANSITION_LINE` and `PROGRESS_LINE`: `lines` the `pending` or `unstored` line and the summary.
    ValueError or OSError where a read is refused; LookupError where a kit does not resolve."""
    cache = {}
    head = read_cached_channels(root, "HEAD", cache)
    findings = [f for line in (TRANSITION_LINE, PROGRESS_LINE) for f in check_line_definition(root, line)]
    if not head & {"trailer", "log"}:
        return derive_floor_report(root, [
            "unstored — %s · %s selects %s at HEAD, which stores no move" % (build, KEY, " ".join(sorted(head))),
            "%s: transition check · %s · unstored · %d finding(s)" % (SAY, build, len(findings))], findings)
    moves = read_transition_moves(build, root, cache)
    findings += moves["findings"]
    lines = []
    for (c, t), rec in zip(moves["owing"], moves["paired"]):
        for name in dict.fromkeys([*t, *rec["fields"]]):
            if t.get(name) != rec["fields"].get(name):
                findings.append("commit %s · log %s · %s: the trailer says %s, the record %s" % (
                    c["sha"][:8], rec["path"], render_record_key(name), t.get(name, "nothing"),
                    rec["fields"].get(name, "nothing")))
    for rec in moves["paired"] + moves["sourced"]:
        findings += ["log %s · malformed · %s %s" % (rec["path"], key, why) for key, why in rec["malformed"]]
    left = moves["owing"][len(moves["paired"]):]
    if left and resolve_build_anchor(build, root) is None:
        lines.append("pending — %d move(s) before the build's first spec" % len(left))
    else:
        findings += ["commit %s · log · the move %s -> %s owes a record, and none holds it" % (
            c["sha"][:8], t["from"], t["to"]) for c, t in left]
    findings += ["log %s · no trailer matches this record, written where %s held trailer" % (rec["path"], KEY)
                 for rec in moves["paired"][len(moves["owing"]):]]
    lines.append("%s: transition check · %s · %d trailer(s) · %d record(s) · %d finding(s)" % (
        SAY, build, len(moves["trailers"]), len(moves["paired"]) + len(moves["sourced"]), len(findings)))
    return derive_floor_report(root, lines, findings)


def derive_floor_report(root, lines, findings):
    """`(lines, findings)` as the check owes them, or, where a finding, a `pending` or an `unstored` line
    stands and `floor.record-changes` reads `off` at `root`'s landed revision (TOOL-dDeclaredLoop-2 S14),
    `floor: record-changes off` and each of them reported as a line, with no finding left to exit on."""
    held = [ln for ln in lines if ln.startswith(("pending — ", "unstored — "))]
    if not (findings or held):
        return lines, findings
    from floor import read_floor
    if read_floor(root)["record-changes"] != "off":
        return lines, findings
    return (["floor: record-changes off"] + ["%s: reported · %s" % (SAY, f) for f in findings]
            + [("%s: reported · %s" % (SAY, ln)) if ln in held else ln for ln in lines]), []


# ------------------------------------------------------------------------------------------ the plants
def write_transition_plant(top, case):
    """The scratch repository at `top` for `case`, committed on `main`: the witness commit's sha."""
    run_fixture_git(top, "init", "-q", "--template=", "-b", "main")
    for key, value in (("user.name", "fx"), ("user.email", "fx@example.invalid"), ("commit.gpgsign", "false"),
                       ("core.autocrlf", "false")):
        run_fixture_git(top, "config", key, value)
    line = TRANSITION_LINE.replace(" · <item tag>", "") if case == "line-drift" else TRANSITION_LINE
    # the progress definition after it (KICK-dKeptSession-11 S9), `notify-shape`'s dropping ` · <detail>`
    progress = PROGRESS_LINE.replace(" · <detail>", "") if case == "notify-shape" else PROGRESS_LINE
    files = {".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tool:TOOL"\n',
             "AGENTS.md": "# AGENTS.md\n\n%s\n- `committed — <sha> · <branch> · <subject>`\n- `%s`\n- `%s`\n%s\n" % (
                 FENCE[0], line, progress, FENCE[1]),
             "memory/builds/%s/README.md" % FX_BUILD: "# %s\n" % FX_BUILD}
    if case != "pre-spec":
        files[FX_SPEC] = "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01\n" % FX_UNIT
    if case in PLANT_SETS:
        files[".governance/policy.toml"] = "[transitions]\nrecord = %s\n" % PLANT_SETS[case]
    if case in NOTIFY_SETS:
        files[".governance/policy.toml"] = '[notify]\nowner = "%s"\n' % NOTIFY_SETS[case]
    if case == "descope-spent":
        files[".governance/policy.toml"] = "[flow]\nrework-budget = 0\n"
    notices = case == "deps-notices" or case.startswith("notices-")
    acks = case.startswith("acks-") or case == "chain-two-dependents"
    if case in ("acks-confirmed", "acks-takeover", "chain-two-dependents"):   # KICK-dKeptSession-42 AC2,
        # KICK-dKeptSession-53 AC1, KICK-dKeptSession-61 AC1: the parent fy's spec, its lease's witness this commit
        files["memory/builds/fy/spec/2026-01-01-spec-TOOL-fy-1.md"] = (
            "# TOOL-fy-1 — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01\n")
    if case == "chain-two-dependents":   # KICK-dKeptSession-61 AC1: the second dependent, staged as FX_BUILD is
        files["memory/builds/tTwo/README.md"] = "# tTwo\n"
        files["memory/builds/tTwo/spec/2026-01-01-spec-TOOL-tTwo-1.md"] = (
            "# TOOL-tTwo-1 — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01\n")
    if case.startswith("mail-") or notices or acks:   # the driver's conf, RUN_CLAIMS on, as the placement plants copy it
        src = next((d for d in (KIT, *KIT.parents) if (d / ".unattended.conf").is_file()), None)
        if src is None:
            raise LookupError("the mail plants copy .unattended.conf from this tree, which holds none")
        files[".unattended.conf"] = (src / ".unattended.conf").read_text(encoding="utf-8") + \
            '\nSPEC_TOKENS_CLI=""\nRUN_CLAIMS="on"\n'
    # KICK-dKeptSession-7 AC7: the second build, its README naming tFix a parent; KICK-dKeptSession-35 AC1, AC3: two;
    # KICK-dKeptSession-52 S1: dA alone, since the id carries the recipient and a second one decides nothing
    dependents = ((FX_DEPENDENT,) if case == "deps-notices" else FX_DEPENDENTS[:1] if case == "notices-repeat-key"
                  else FX_DEPENDENTS if notices else ())
    for dependent in dependents:
        files["memory/builds/%s/README.md" % dependent] = (
            "---\nslug: %s\nnode: a\nopened: 2026-01-01\nstreams: tooling\nroster: TOOL\nids: TOOL-%s-1\nparents: %s\n"
            "---\n# %s\n" % (dependent, dependent, FX_BUILD, dependent))
    if dependents:   # KICK-dKeptSession-44 S20: the parent's README holds the region the index renders, by its renderer
        read_memory_tree("gen_build_index.py")
        from gen_build_index import render_edges
        files["memory/builds/%s/README.md" % FX_BUILD] = "# %s\n\n%s\n" % (
            FX_BUILD, render_edges({"parents": [], "children": sorted(dependents)}))
    write_fixture_files(top, files)
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "-m", "fixture")
    if case in ("mail-open", "mail-disposed", "mail-expired") or notices or acks:   # a bare remote inside the git dir, so the scratch's removal takes it too
        from placement import write_fixture_gov_ref
        origin = top / ".git" / "fx-origin.git"
        run_fixture_git(top, "init", "-q", "--bare", "--template=", str(origin))
        run_fixture_git(top, "remote", "add", FIXTURE_REMOTE, str(origin))
        run_fixture_git(top, "push", "-q", FIXTURE_REMOTE, "main")
        for ref, *mail in () if notices or acks else (FX_QUESTION, FX_ACK) if case == "mail-disposed" else (FX_QUESTION,):
            write_fixture_gov_ref(top, ref, render_fixture_mail(*mail, **(FX_DEADLINE if case == "mail-expired" else {})))
        if case == "mail-expired":
            # its first sighting, the six-field line `claim.py`'s stale-holder plant writes for a lease: the commit
            # the remote holds, seen FX_SIGHTED_HOURS back. The driver's sightings walk appends its own line for
            # the tip at the read, after this one, and the first line of a ref and commit is the one it ages
            import datetime
            ref = FX_QUESTION[0]
            sha = run_fixture_git(top, "ls-remote", FIXTURE_REMOTE, ref).split("\t", 1)[0]
            feed = pathlib.Path(run_fixture_git(top, "rev-parse", "--path-format=absolute", "--git-common-dir")) / "gov-feed.log"
            rows = feed.read_text(encoding="utf-8").splitlines() if feed.exists() else []
            seq = max([int(r.split("\t", 1)[0]) for r in rows if r.split("\t", 1)[0].isdigit()] or [0]) + 1
            ago = (datetime.datetime.now(datetime.timezone.utc)
                   - datetime.timedelta(hours=FX_SIGHTED_HOURS)).strftime("%Y-%m-%dT%H:%M:%SZ")
            with feed.open("a", encoding="utf-8", newline="\n") as fh:
                fh.write("%d\t%s\tmail\t%s\t%s\t%s\n" % (seq, ref, run_fixture_git(top, "rev-parse", sha + "^{tree}"), sha, ago))
    return run_fixture_git(top, "rev-parse", "HEAD")


def run_notice_plant(top, witness):
    """The `deps-notices` plant's misses (KICK-dKeptSession-7 AC7) over the scratch at `top`, `witness` its
    fixture commit, run as the fleet registry's first user and `FX_SESSION`: a spec added, then B5 at that
    older `witness`, B8 back, a spec added and B5 again; then the driver's `--mail read` of the dependent,
    owed one `confirmed` keyed over the spec listing at the first move's commit, never at `witness`, and one
    `changed` keyed over the second's, each key the driver's `derive_gov_id --file` over that listing."""
    import os
    from breakpoints import run_sourced   # it imports this module at its top, so here
    from placement import read_fleet_user
    at = ["--build", FX_BUILD, "--root", str(top)]
    kept = {k: os.environ.get(k) for k in ("USERNAME", "CLAUDE_CODE_SESSION_ID")}
    os.environ.update(USERNAME=read_fleet_user(), CLAUDE_CODE_SESSION_ID=FX_SESSION)
    exits, commits = [], []
    try:
        for n in (2, 3):   # each Design exit after a spec is added, so its listing differs from the one before
            uid = "TOOL-%s-%d" % (FX_BUILD, n)
            write_fixture_files(top, {"memory/builds/%s/spec/2026-01-0%d-spec-%s.md" % (FX_BUILD, n, uid):
                                      "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01\n" % uid})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "a spec of %s" % uid)
            exits.append(main(["record", *at, "--from", "designing", "--item", "item.design.exit", "--outcome",
                               "recorded", "--witness", witness if n == 2 else "HEAD"]))
            commits.append(run_fixture_git(top, "rev-parse", "HEAD"))
            if n == 2:   # B8, back into designing
                exits.append(main(["record", *at, *BACKWARD_MOVES[4], "--witness", "HEAD"]))
        files = []
        for n, sha in enumerate([witness] + commits):
            path = top / ".git" / ("fx-listing-%d" % n)
            path.write_bytes(derive_interface_listing(top, FX_BUILD, sha))
            files.append(path.as_posix())
        _rc, out = run_sourced(top, 'load_driver_conf && for f in "$2" "$3" "$4"; do derive_gov_id --file "$f"; done',
                               args=files, timeout=MAIL_GUARD_SECONDS)
        keys = [ln.strip() for ln in out.splitlines() if re.fullmatch(r"[0-9a-f]{12}", ln.strip())]
        _rc, out = run_sourced(top, '( load_driver_conf && main --mail read "$2" )', args=(FX_DEPENDENT,),
                               timeout=MAIL_GUARD_SECONDS)
    finally:
        for k, v in kept.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
    rows =[ln.rstrip("\r").split("\t") for ln in out.splitlines() if ln.count("\t") >= 13]
    for r in rows:
        print("%s: fixture · deps-notices · row %s · %s · %s · %s · content-key %s" % (SAY, r[0], r[1], r[2], r[6], r[13]))
    print("%s: fixture · deps-notices · keys %s" % (SAY, " ".join(keys) or "none"))
    subject = "interfaces %s" % FX_BUILD
    held = {kind: [r[13] for r in rows if r[1] == kind and r[2] == "build:%s" % FX_DEPENDENT and r[6] == subject]
            for kind in ("confirmed", "changed")}
    return [why for ok, why in (
        (exits == [0, 0, 0], "the three moves exited %s" % exits),
        (len(keys) == 3 and len(set(keys)) == 3, "the three listings keyed %s, owed three distinct keys" % keys),
        (len(keys) == 3 and held["confirmed"] == [keys[1]], "the confirmed rows carry %s, owed the one key %s of the "
         "first move's commit and never %s of --witness" % (held["confirmed"], keys[1:2], keys[:1])),
        (len(keys) == 3 and held["changed"] == [keys[2]], "the changed rows carry %s, owed the one key %s of the "
         "second move's commit" % (held["changed"], keys[2:3]))) if not ok]


def run_transition_fixture(case):
    """`record` and `check` over a scratch repository planted as `case`: the last verb's exit."""
    top = pathlib.Path(tempfile.mkdtemp(prefix="loop-transition-")).absolute()
    try:
        print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
        witness = write_transition_plant(top, case)
        at = ["--build", FX_BUILD, "--root", str(top)]
        b4 = ["record", *at, "--from", "planning", "--item", "item.plan.exit", "--outcome", "recorded",
              "--witness", witness]

        def run_verb(argv):
            rc = main(argv)
            print("%s: fixture · %s · exit %d" % (SAY, argv[0], rc))
            return rc

        def read_count():
            return run_fixture_git(top, "rev-list", "--count", "HEAD")

        def read_folder():
            recs = read_transition_records(FX_BUILD, top)
            print("%s: fixture · records %d%s" % (SAY, len(recs), "".join(" · %s-%d %s -> %s" % (
                KIND, r["n"], r.get("From"), r.get("To")) for r in recs)))
            return recs

        def write_commit(subject):
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", subject)

        if case == "descope-spent":   # the ending row E5 records a backward move on a spent budget, drawing nothing
            for n, tail in enumerate(BACKWARD_MOVES[:3]):
                run_verb(["record", *at, *tail, "--witness", "HEAD" if n else witness])
            before = read_count()
            refused = run_verb(["record", *at, *BACKWARD_MOVES[3], "--witness", "HEAD"])
            kept = read_count() == before
            rc = run_verb(["record", *at, "--from", "testing", "--item", "@any", "--outcome", "descope", "--witness", "HEAD"])
            from budget import read_budget_rows   # it imports this module, so here
            held, moves = read_budget_rows(FX_BUILD, top), read_transitions(FX_BUILD, top)
            print("%s: fixture · rows %s" % (SAY, " | ".join(held["rows"]) or "none"))
            misses = [why for ok, why in (
                (refused == 2 and kept, "the backward move on item.test.attribute's code-miss was not refused"),
                (rc == 0 and bool(moves) and (moves[0]["from"], moves[0]["to"], moves[0]["item"]) == (
                    "testing", "building", "@any"), "the descope did not record testing -> building on @any"),
                (not held["draws"], "the descope drew a row")) if not ok]
            print("%s: fixture · descope-spent · %s" % (SAY, "held" if not misses else "MISSED " + "; ".join(misses)))
            return 0 if not misses else 1
        if case == "deps-notices":   # KICK-dKeptSession-7 AC7: Design's exits notify the dependent
            misses = run_notice_plant(top, witness)
            print("%s: fixture · deps-notices · %s" % (SAY, "held" if not misses else "MISSED " + "; ".join(misses)))
            return 0 if not misses else 1
        if case in ("notices-two-dependents", "notices-refused", "notices-repeat-key", "notices-reposted"):
            # KICK-dKeptSession-35 AC1, AC3, KICK-dKeptSession-52 S1 and KICK-dKeptSession-56 AC28: each plant
            # rebinds the launcher the writer imports inside its function, recording every post, and restores it
            import os
            import breakpoints
            from placement import read_fleet_user
            real, posts, refused = breakpoints.run_sourced, [], "build:%s" % FX_DEPENDENTS[0]
            b5 = ["record", *at, *BACKWARD_MOVES[1], "--witness", "HEAD"]
            b7 = ["record", *at, *BACKWARD_MOVES[2], "--witness", "HEAD"]
            b21 = ["record", *at, "--from", "building", "--item", "item.build.unit-pass", "--outcome",
                   "interface-change", "--witness", "HEAD"]
            mark = 0   # under notices-reposted, the posts B5 made: B7's are those after it

            def run_recorded_post(repo, script, *rest, **kw):
                """The landed launcher, each post's argv, exit and output recorded; under `notices-refused` the
                first post to dA answers 1, under `notices-reposted` 2, launching nothing."""
                if "--mail post" not in script:
                    return real(repo, script, *rest, **kw)
                argv = [str(a) for a in kw.get("args", ())]
                first = argv[1:2] == [refused] and not any(p[0][1] == refused for p in posts)
                if case == "notices-refused" and first:
                    got = (1, "mail — duplicate 000000000000 · the plant's refusal\n")
                elif case == "notices-reposted" and first:
                    got = (2, "mail — not written · the plant's refusal\n")
                else:
                    got = real(repo, script, *rest, **kw)
                posts.append((argv,) + tuple(got))
                return got
            kept = {k: os.environ.get(k) for k in ("USERNAME", "CLAUDE_CODE_SESSION_ID")}
            os.environ.update(USERNAME=read_fleet_user(), CLAUDE_CODE_SESSION_ID=FX_SESSION)
            breakpoints.run_sourced = run_recorded_post
            exits, rows, notes, unread = [], {}, [], None
            try:
                if case == "notices-repeat-key":   # B4, then three Design exits over the listings A, B and B
                    exits.append(run_verb(b4))
                    for n in range(3):
                        if n:   # B21, back into designing on an interface change
                            exits.append(run_verb(b21))
                        if n == 1:   # the one edit, after the first B21 and none after the second
                            write_fixture_files(top, {FX_SPEC: "# %s — a unit\n\n**Status:** INPROGRESS · rev-2 · "
                                                               "2026-01-02\n" % FX_UNIT})
                            write_commit("the spec of %s edited" % FX_UNIT)
                        exits.append(run_verb(b5))
                    try:   # the one read of dA's mailbox, its rows' pass and key read off their commits below
                        notes, unread = read_mail_rows(top, FX_DEPENDENTS[0])
                    except ValueError as e:
                        unread = str(e)
                else:
                    for n in range(2, 5 if case == "notices-two-dependents" else 3):   # each exit over a new spec
                        if n > 2:   # B21, back into designing on an interface change
                            exits.append(run_verb(b21))
                        uid = "TOOL-%s-%d" % (FX_BUILD, n)
                        write_fixture_files(top, {"memory/builds/%s/spec/2026-01-0%d-spec-%s.md" % (FX_BUILD, n, uid):
                                                  "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01\n"
                                                  % uid})
                        write_commit("a spec of %s" % uid)
                        exits.append(run_verb(b5))
                    if case == "notices-reposted":   # KICK-dKeptSession-56 AC28: a later move, no Design exit
                        mark = len(posts)
                        exits.append(run_verb(b7))
                for dependent in FX_DEPENDENTS if case in ("notices-two-dependents", "notices-reposted") else ():
                    _rc, out = real(top, '( load_driver_conf && main --mail read "$2" )', args=(dependent,),
                                    timeout=MAIL_GUARD_SECONDS)
                    held = [ln.rstrip("\r").split("\t") for ln in out.splitlines() if ln.count("\t") >= 13]
                    held = [r for r in held if r[2] == "build:%s" % dependent and r[6] == "interfaces %s" % FX_BUILD]
                    rows[dependent] = sorted(held, key=lambda r: int(r[11]) if r[11].isdigit() else 0)
            finally:
                breakpoints.run_sourced = real
                for k, v in kept.items():
                    if v is None:
                        os.environ.pop(k, None)
                    else:
                        os.environ[k] = v
            said = {}
            for dependent, held in rows.items():   # each row's pass, read off its commit, column 10
                said[dependent] = [(r[1], (re.findall(r"^pass: (\S+)$", run_fixture_git(top, "log", "-1", "--format=%B",
                                                                                      r[9]), re.M) or ["none"])[0])
                                   for r in held]
                print("%s: fixture · %s · %s" % (SAY, dependent, " · ".join("%s pass %s" % k for k in said[dependent])
                                                   or "no row"))
            print("%s: fixture · posts %d · %s" % (SAY, len(posts), " · ".join(
                "%s rc %d" % (p[0][1], p[1]) for p in posts) or "none"))
            posted = [p for p in posts if any(ln.startswith("mail — posted ") for ln in p[2].splitlines())]
            if case == "notices-repeat-key":   # KICK-dKeptSession-52 S1: each row's pass and key off its commit
                bodies = [(r["kind"], run_fixture_git(top, "log", "-1", "--format=%B", r["commit"])) for r in notes
                          if r["to"] == "build:%s" % FX_DEPENDENTS[0] and r["subject"] == "interfaces %s" % FX_BUILD]
                notes = sorted(((kind,) + tuple((re.findall(r"^%s: (\S+)$" % k, body, re.M) or ["none"])[0]
                                                for k in ("pass", "content-key")) for kind, body in bodies),
                               key=lambda n: n[1])
                for note in notes:
                    print("%s: fixture · notice %s · pass %s · key %s" % ((SAY,) + note))
                firsts = [([ln.rstrip("\r") for ln in p[2].splitlines() if ln.strip()] or ["no output"])[0] for p in posts]
                owed = [("confirmed", "1"), ("changed", "2"), ("changed", "3")]
                keys = [n[2] for n in notes]
                checks = ((len(firsts) == 3 and all(ln.startswith("mail — posted ") for ln in firsts),
                           "the posts' first lines read %s, owed three mail — posted" % (firsts,)),
                          ([n[:2] for n in notes] == owed, "the rows of %s read %s, owed %s%s" % (
                              FX_DEPENDENTS[0], [n[:2] for n in notes], owed,
                              " · its mailbox unread: %s" % unread if unread else "")),
                          (len(keys) == 3 and keys[1] == keys[2] != keys[0], "the keys read %s, owed the two changed "
                           "equal and the confirmed another" % keys))
                misses = [why for ok, why in checks if not ok]
                print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "not held · " + misses[0]))
                return 0 if not misses else 1
            if case == "notices-two-dependents":
                owed = [("confirmed", "1"), ("changed", "2"), ("changed", "3")]
                checks = ((exits == [0] * 5, "the five moves exited %s" % exits),
                          (len(posts) == 6 and len(posted) == 6, "%d of %d posts printed mail — posted, owed 6 of 6"
                           % (len(posted), len(posts))),
                          (all(said.get(d) == owed for d in FX_DEPENDENTS), "the rows read %s, owed %s to each"
                           % (said, owed)))
            elif case == "notices-reposted":   # KICK-dKeptSession-56 AC28: the refused notice posted again by B7
                # to dA alone, dB holding the current interface and posted nothing
                later = [(p[0][1], p[1]) for p in posts[mark:]]
                checks = ((exits == [0, 0], "the two moves exited %s" % exits),
                          ([p[0][1] for p in posts[:mark] if p[1] == 2] == [refused], "B5's posts refused exit 2 are %s, "
                           "owed %s" % ([p[0][1] for p in posts[:mark] if p[1] == 2], refused)),
                          (later == [(refused, 0)], "B7's posts are %s, owed one to %s exiting 0" % (later, refused)),
                          (all(said.get(d) == [("confirmed", "1")] for d in FX_DEPENDENTS),
                           "the rows read %s, owed one confirmed of pass 1 to each" % said))
            else:
                checks = ((exits == [0], "the move exited %s" % exits),
                          ([p[0][1] for p in posts if p[1] == 1] == [refused], "the refused posts are %s, owed %s"
                           % ([p[0][1] for p in posts if p[1] == 1], refused)),
                          ([p[0][1] for p in posted] == ["build:%s" % FX_DEPENDENTS[1]], "the posted ones are %s"
                           % [p[0][1] for p in posted]))
            misses = [why for ok, why in checks if not ok]
            print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
            return 0 if not misses else 1
        if case.startswith("acks-") or case == "chain-two-dependents":   # KICK-dKeptSession-42 AC1 to AC4,
            # KICK-dKeptSession-55 AC1, AC2, KICK-dKeptSession-61 AC1 to AC3: a move acknowledges what it
            # consumed, all or nothing, run
            # as the fleet registry's first user and FX_SESSION, the launcher the writer imports inside its function
            # rebound to record each ack and, under acks-superseded and acks-later-key, the interfaces check stood
            # in; all restored
            import os
            import time
            import breakpoints
            from placement import read_fleet_user, write_fixture_gov_ref, write_foreign_lease
            real_run, real_check = breakpoints.run_sourced, globals()["check_parent_interfaces"]
            ids = {"landed": "a1a2a3a4a5a6", "confirmed": "c1c2c3c4c5c6", "changed": "d1d2d3d4d5d6",
                   "fz confirmed": "e1e2e3e4e5e6", "fz changed": "f1f2f3f4f5f6", "lost": "b1b2b3b4b5b6",
                   "raised": "b7b8b9b0b1b2", "a confirmed": "aa11aa11aa11", "b changed": "bb22bb22bb22",
                   "c changed": "cc33cc33cc33", "withdrawn": "9a9b9c9d9e9f", "fz question": "8a8b8c8d8e8f",
                   "a1 confirmed": "a1a1a1a1a1a1", "b1 confirmed": "b1b1b1b1b1b1", "a2 changed": "a2a2a2a2a2a2",
                   "b2 changed": "b2b2b2b2b2b2"}
            acked, checked, failing, exits, refused = [], [], {}, [], []
            b5 = ["record", *at, *BACKWARD_MOVES[1], "--witness", "HEAD"]
            b7 = ["record", *at, *BACKWARD_MOVES[2], "--witness", "HEAD"]
            stood_in = case in ("acks-superseded", "acks-later-key")

            def write_notice(n, parent, name, key=None, tip=None, to=FX_BUILD, **order):
                """The message `ids[name]` from `parent` to build:`to`, tFix unless given (KICK-dKeptSession-61),
                on its own ref, a `landed` of subject `landing <parent>`, a `confirmed` or `changed` of
                `interfaces <parent>` keyed `key`, or a `withdrawn` or `question` (KICK-dKeptSession-55) of
                `<kind> <parent>`; `order` its `seq` and
                `after` keys and `tip`, where given, its commit's parent on the ref (KICK-dKeptSession-53 S7).
                -> the commit's sha."""
                kind = name.split()[-1] if name.split()[-1] in ("confirmed", "changed", "withdrawn", "question") \
                    else "landed"
                subject = ("interfaces %s" if kind in ("confirmed", "changed") else "landing %s" if kind == "landed"
                           else kind + " %s") % parent
                return write_fixture_gov_ref(top, "refs/gov/mail/%s/z/s-%d" % (parent, n), render_fixture_mail(
                    parent, ids[name], "build:%s" % to, kind, subject, content_key=key, **order), parent=tip)

            def run_recorded_ack(repo, script, *rest, **kw):
                """The landed launcher, each `--mail ack` recorded as `(id, exit)`; an id `failing` names answers
                exit 1 with the post's lost line, or raises LookupError, launching nothing; under acks-later-key
                each answers the post's posted line, launching nothing."""
                if "--mail ack" not in script:
                    return real_run(repo, script, *rest, **kw)
                mid = ([str(a) for a in kw.get("args", ())][1:2] or ["-"])[0]
                if failing.get(mid) == "raise":
                    acked.append((mid, "-"))
                    raise LookupError("the plant's driver does not resolve")
                if case == "acks-later-key":
                    got = (0, "mail — posted %s · refs/gov/mail/%s/z/%s\n" % (mid, FX_BUILD, FX_SESSION))
                elif failing.get(mid) == "lost":
                    got = (1, "mail — lost %s · the plant's refusal\n" % mid)
                else:
                    got = real_run(repo, script, *rest, **kw)
                acked.append((mid, got[0]))
                return got

            def check_stood_in(root, slug, parent):
                """The interfaces check stood in, each parent recorded: fy's `changed` current, `b` under
                acks-later-key, any other unconfirmed."""
                checked.append(parent)
                if parent == "fy":
                    return 0, "interface — current %s · changed · key 0123456789ab" % ids[
                        "b changed" if case == "acks-later-key" else "changed"]
                return 1, "interface — unconfirmed · key 0123456789ab"

            def run_held_verb(argv):
                """`run_verb` with its output echoed and kept, so a refusal's line is read."""
                out = io.StringIO()
                with contextlib.redirect_stdout(out):
                    rc = run_verb(argv)
                sys.stdout.write(out.getvalue())
                exits.append(rc)
                refused.extend(ln for ln in out.getvalue().splitlines() if ln.startswith("refused — "))
                return rc

            def read_row_state(name, seen=None):
                """The row `ids[name]` as `read_mail_rows` reads it now, or as `seen`, one read's rows, holds it,
                printed."""
                rows = read_mail_rows(top, FX_BUILD)[0] if seen is None else seen
                state = next((r.get("state") for r in rows if r.get("id") == ids[name]), "none")
                print("%s: fixture · state %s · %s" % (SAY, ids[name], state))
                return state
            err = io.StringIO()
            kept = {k: os.environ.get(k) for k in ("USERNAME", "CLAUDE_CODE_SESSION_ID")}
            os.environ.update(USERNAME=read_fleet_user(), CLAUDE_CODE_SESSION_ID=FX_SESSION)
            if case == "acks-no-session":   # KICK-dKeptSession-56 AC27: the harness exports no session id
                os.environ.pop("CLAUDE_CODE_SESSION_ID", None)
            breakpoints.run_sourced = run_recorded_ack
            if stood_in:
                globals()["check_parent_interfaces"] = check_stood_in
            try:
                with contextlib.redirect_stderr(err):
                    if case == "acks-landed":   # AC1
                        write_notice(1, "fy", "landed")
                        run_held_verb(b4)
                        states = [read_row_state("landed")]
                        checks = ((acked == [(ids["landed"], 0)], "the acks are %s" % acked),)
                    elif case == "acks-no-session":   # KICK-dKeptSession-56 AC27: the real ack refused for no
                        # session id, the move refused naming that cause and never `mail open`
                        write_notice(1, "fy", "landed")
                        run_held_verb(b4)
                        states = [read_row_state("landed")]
                        checks = (([a[0] for a in acked if a[1] != 0] == [ids["landed"]],
                                   "the acks are %s, owed the landed's one, refused" % acked),
                                  (len(refused) == 1 and "mail ack not posted: %s · " % ids["landed"] in refused[0]
                                   and "no session id" in refused[0] and "mail open" not in refused[0],
                                   "B4's refusal read %s, owed the ack's no session id" % refused))
                    elif case in ("acks-confirmed", "acks-takeover", "chain-two-dependents"):   # AC2: the real
                        # chain, its key the driver's over fy's listing
                        write_foreign_lease(top, "fy", fields=(("witness", witness),))
                        listing = top / ".git" / "fx-listing-fy"
                        listing.write_bytes(derive_interface_listing(top, "fy", witness))
                        rc, out = real_run(top, 'load_driver_conf && derive_gov_id --file "$2"', args=(listing.as_posix(),),
                                           timeout=MAIL_GUARD_SECONDS)
                        key = (out.strip().splitlines() or ["unkeyed"])[-1].strip() if rc == 0 else "unkeyed"
                        print("%s: fixture · key %s" % (SAY, key))
                        if case == "acks-confirmed":
                            write_notice(1, "fy", "confirmed", key)
                            run_held_verb(b4)
                            states = [read_row_state("confirmed")]
                            checks = ((acked == [(ids["confirmed"], 0)], "the acks are %s" % acked),)
                        elif case == "chain-two-dependents":   # KICK-dKeptSession-61 AC1 to AC3: s-1 posts a1 then
                            # b1, both confirmed K1, to tFix then tTwo; the take-over s-2 posts a2 after b1, then b2,
                            # both changed K2 over the listing, to the same two. tFix's rows never hold b1, so only
                            # the chain read over every row fy wrote places a1 before a2
                            names = ("a1 confirmed", "b1 confirmed", "a2 changed", "b2 changed")
                            tip = write_notice(1, "fy", names[0], "0123456789ab", seq="1", after="none")
                            write_notice(1, "fy", names[1], "0123456789ab", tip=tip, to="tTwo", seq="2", after="none")
                            tip = write_notice(2, "fy", names[2], key, seq="1", after=ids[names[1]])
                            write_notice(2, "fy", names[3], key, tip=tip, to="tTwo", seq="2", after="none")
                            run_held_verb(b4)
                            run_held_verb([b4[0], "--build", "tTwo", *b4[3:]])
                            mine = [r for r in read_mail_rows(top, FX_BUILD)[0] if r.get("from-build") == "fy"]
                            sent = read_mail_rows(top, "fy", sent=True)[0]   # fetched, so it holds every ack
                            pair = (ids[names[0]], ids[names[2]])
                            chained = ["yes" if pair in derive_mail_chain(mine, held) else "no" for held in (sent, mine)]
                            print("%s: fixture · chain tFix · %s precedes %s · sent %s · filtered %s" % (SAY, *pair,
                                                                                                       *chained))
                            ordered = sum((r.get("seq") or "-") != "-" and (r.get("after") or "-") != "-" for r in sent)
                            print("%s: fixture · sent fy · %d row(s) · seq and after on %d" % (SAY, len(sent), ordered))
                            states = [read_row_state(n, sent) for n in names]
                            try:
                                why = "read %d row(s)" % len(read_mail_rows(top, "build:fy", sent=True)[0])
                                said = "read"
                            except ValueError as e:
                                why, said = str(e), "refused"
                            print("%s: fixture · sent build:fy · %s · %s" % (SAY, said, why))
                            checks = ((sorted(acked) == sorted((ids[n], 0) for n in names),
                                       "the acks are %s, owed the four rows', each exit 0" % acked),
                                      (chained == ["yes", "no"], "the chain read %s, owed yes over the sent read and "
                                       "no over tFix's rows alone" % chained),
                                      ((len(sent), ordered) == (4, 4), "the sent read held %d row(s), %d ordered, owed 4 "
                                       "and 4" % (len(sent), ordered)),
                                      (said == "refused" and "exited 2" in why and "is no build's slug" in why,
                                       "the sent read of build:fy %s: %s" % (said, why)))
                        else:   # KICK-dKeptSession-53 AC1, AC2: the take-over's changed b, keyed over the listing,
                            # sighted by one read before its predecessor's confirmed a, keyed by no listing, lands
                            pair = (ids["a confirmed"], ids["b changed"])
                            write_notice(2, "fy", "b changed", key, seq="1", after=pair[0])
                            read_mail_rows(top, FX_BUILD)
                            write_notice(1, "fy", "a confirmed", "0123456789ab", seq="1")
                            run_held_verb(b4)
                            seen = [r for r in read_mail_rows(top, FX_BUILD)[0] if r.get("from-build") == "fy"]
                            states = [read_row_state(n, seen) for n in ("a confirmed", "b changed")]
                            stamps = {r.get("id"): r.get("first-seen") for r in seen}
                            swapped = [dict(r, **{"first-seen": stamps.get(pair[1 - pair.index(r["id"])])})
                                       if r.get("id") in pair else dict(r) for r in seen]
                            chained = ["yes" if pair in derive_mail_chain(held, held) else "no" for held in (seen, swapped)]
                            print("%s: fixture · chain · a precedes b · %s · first-seen swapped · %s" % (SAY, *chained))
                            checks = ((sorted(acked) == sorted([(pair[0], 0), (pair[1], 0)]),
                                       "the acks are %s, owed a's and b's, each exit 0" % acked),
                                      (chained == ["yes", "yes"], "the chain read %s, owed yes over the read and "
                                       "over first-seen swapped" % chained))
                    elif case == "acks-later-key":   # KICK-dKeptSession-53 AC3: c pushed onto b's ref over b, seq 2,
                        # a later key the chain places after the current b; KICK-dKeptSession-55 S2: c unconsumed,
                        # so no ack posts and the refusal names every open row
                        write_notice(1, "fy", "a confirmed", "111111111111", seq="1")
                        tip = write_notice(2, "fy", "b changed", "222222222222", seq="1", after=ids["a confirmed"])
                        write_notice(2, "fy", "c changed", "333333333333", tip=tip, seq="2")
                        run_held_verb(b4)
                        states = []
                        named = refused[0].split(" · ")[1].split()[2:] if len(refused) == 1 else []
                        checks = ((acked == [], "the acks are %s, owed none while c is open" % acked),
                                  (sorted(named) == sorted(ids[n] for n in ("a confirmed", "b changed", "c changed")),
                                   "B4's refusal read %s, owed a, b and c" % refused))
                    elif case in ("acks-withdrawn", "acks-withdrawn-question"):   # KICK-dKeptSession-55 AC1, AC2: a
                        # lone withdrawn acked and printed; beside an open question, neither acked and both named
                        write_notice(1, "fy", "withdrawn")
                        if case == "acks-withdrawn":
                            run_held_verb(b4)
                            states = []
                            checks = ((acked == [(ids["withdrawn"], 0)], "the acks are %s, owed the withdrawn's" % acked),
                                      ("mail — acked withdrawn %s from build:fy" % ids["withdrawn"] in err.getvalue(),
                                       "stderr read %r, owed the withdrawn's mail — acked line" % err.getvalue()))
                        else:
                            write_notice(2, "fz", "fz question")
                            run_held_verb(b4)
                            seen = read_mail_rows(top, FX_BUILD)[0]   # one read after the refusal, each row printed
                            states = [read_row_state(n, seen) for n in ("withdrawn", "fz question")]
                            named = refused[0].split(" · ")[1].split()[2:] if len(refused) == 1 else []
                            checks = ((acked == [], "the acks are %s, owed none beside the open question" % acked),
                                      (sorted(named) == sorted(ids[n] for n in ("withdrawn", "fz question")),
                                       "B4's refusal read %s, owed the withdrawn and the question" % refused),
                                      ("mail — acked" not in err.getvalue(), "stderr read %r, owed no mail — acked line"
                                       % err.getvalue()))
                    elif case == "acks-superseded":   # AC3: the confirmed sighted a second before the changed
                        write_notice(1, "fy", "confirmed")
                        read_mail_rows(top, FX_BUILD)
                        time.sleep(1.1)   # a sighting is stamped to the second, and a tie is never earlier
                        write_notice(2, "fy", "changed")
                        run_held_verb(b4)
                        write_notice(3, "fz", "fz confirmed")
                        write_notice(4, "fz", "fz changed")
                        run_held_verb(b5)
                        states = [read_row_state(n) for n in ("confirmed", "changed", "fz changed")]
                        checks = ((sorted(acked) == sorted([(ids["confirmed"], 0), (ids["changed"], 0)]),
                                   "the acks are %s, owed fy's confirmed and changed, each exit 0" % acked),
                                  (len(refused) == 1 and refused[0].startswith("refused — %s · mail open " % FX_BUILD)
                                   and ids["fz changed"] in refused[0].split(" · ")[1], "B5's refusal read %s" % refused),
                                  (checked == ["fy", "fz"], "the check ran for %s, owed fy then fz" % checked))
                    else:   # AC4: one ack across B4 and B5, then a lost ack and a raising one holding B7
                        write_notice(1, "fy", "landed")
                        run_held_verb(b4)
                        run_held_verb(b5)
                        failing.update({ids["lost"]: "lost", ids["raised"]: "raise"})
                        write_notice(2, "fy", "lost")
                        write_notice(3, "fz", "raised")
                        run_held_verb(b7)
                        states = [read_row_state(n) for n in ("landed", "lost", "raised")]
                        said = err.getvalue()
                        checks = (([a for a in acked if a[0] == ids["landed"]] == [(ids["landed"], 0)],
                                   "the first landed's acks are %s, owed one" % acked),
                                  # KICK-dKeptSession-56 S32: both rows held for their refused acks alone, so
                                  # the refusal names each ack's cause, never `mail open`
                                  (len(refused) == 1 and all("mail ack not posted: %s · " % ids[n] in refused[0]
                                                             for n in ("lost", "raised")),
                                   "B7's refusal read %s" % refused),
                                  ("mail — ack not posted %s · rc 1" % ids["lost"] in said
                                   and "mail — ack not posted %s · rc -" % ids["raised"] in said,
                                   "stderr read %r" % said))
            finally:
                breakpoints.run_sourced = real_run
                globals()["check_parent_interfaces"] = real_check
                for k, v in kept.items():
                    if v is None:
                        os.environ.pop(k, None)
                    else:
                        os.environ[k] = v
            for line in err.getvalue().splitlines():
                print("%s: fixture · stderr · %s" % (SAY, line))
            owed = {"acks-landed": ([0], ["acked"]), "acks-no-session": ([1], ["open"]), "acks-confirmed": ([0], ["acked"]),
                    "acks-superseded": ([0, 1], ["acked", "acked", "open"]),
                    "acks-failed": ([0, 0, 1], ["acked", "open", "open"]),
                    "acks-takeover": ([0], ["acked", "acked"]), "acks-later-key": ([1], []),
                    "acks-withdrawn": ([0], []), "acks-withdrawn-question": ([1], ["open", "open"]),
                    "chain-two-dependents": ([0, 0], ["acked"] * 4)}[case]
            print("%s: fixture · acks %s" % (SAY, " · ".join("%s rc %s" % a for a in acked) or "none"))
            misses = [why for ok, why in ((exits == owed[0], "the moves exited %s, owed %s" % (exits, owed[0])),
                                          (states == owed[1], "the rows read %s, owed %s" % (states, owed[1])),
                                          *checks) if not ok]
            print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
            return 0 if not misses else 1
        if case.startswith("notify-") and case != "notify-shape":   # KICK-dKeptSession-11 AC1, AC2: B4, then a
            # park and a landing reported, the progress lines the three print counted on a line a case can hold
            out, rcs = io.StringIO(), []
            with contextlib.redirect_stdout(out):
                rcs.append(run_verb(b4))
                for event, detail in (("park", "item fx-fork"), ("landing", witness[:8])):
                    rcs.append(run_verb(["progress", *at, "--event", event, "--detail", detail]))
            sys.stdout.write(out.getvalue())
            print("%s: fixture · progress %d" % (SAY, sum(ln.startswith("progress — ") for ln in out.getvalue().splitlines())))
            return max(rcs)
        if case == "mail-open":   # KICK-dKeptSession-5 AC6: the open question refuses B4, writing nothing
            before = read_count()
            rc = run_verb(b4)
            print("%s: fixture · commits %s" % (SAY, "unchanged" if read_count() == before else "changed"))
            return rc
        if case in ("mail-disposed", "mail-expired"):   # KICK-dKeptSession-5 AC6: B4 disposes the acknowledged
            # question in one commit; KICK-dKeptSession-24 AC2: B4 disposes the question past its deadline, never
            # answered, as expired
            read_memory_tree("build_records.py")
            import build_records
            before = read_count()
            moved = run_verb(b4)
            files = [p for p in run_fixture_git(top, "show", "--format=", "--name-only", "HEAD").splitlines() if p]
            mails = [p for p in files if "-%s-" % MAIL_KIND in p]
            print("%s: fixture · commits %d · %d file(s) · %d %s record(s)" % (
                SAY, int(read_count()) - int(before), len(files), len(mails), MAIL_KIND))
            print("%s: fixture · trailer %s" % (SAY, run_fixture_git(top, "log", "-1", "--format=%%(trailers:key=%s,valueonly)"
                                                                      % TRAILER_KEY) or "none"))
            for rec in read_folder():
                print("%s: fixture · record %s-%d · disposed %s" % (SAY, KIND, rec["n"], rec["fields"].get("disposed", "none")))
            for rel in mails:
                out = io.StringIO()
                with contextlib.redirect_stdout(out):
                    rc = build_records.main(["read", str(top / rel)])
                text = (top / rel).read_text(encoding="utf-8")
                serves, state = (re.search(r"^%s$" % p, text, re.M) for p in (r"\*\*Serves:\*\* (.+)", r"- \*\*State:\*\* (.+)"))
                print("%s: fixture · %s · read exit %d · Serves %s · State %s" % (
                    SAY, rel, rc, serves.group(1) if serves else "none", state.group(1) if state else "none"))
            if case == "mail-expired":
                return moved
            run_verb(["record", *at, *BACKWARD_MOVES[1][:6], "--witness", "HEAD"])
            value = run_fixture_git(top, "log", "-1", "--format=%%(trailers:key=%s,valueonly)" % TRAILER_KEY)
            print("%s: fixture · next move · %s" % (SAY, "disposes again: " + value if "disposed=" in value else "disposes nothing"))
            return run_verb(["check", *at])
        if case in ("mail-argv", "mail-no-driver", "mail-no-bash", "mail-read-crash"):   # KICK-dKeptSession-36 S4: the guard's launch
            import subprocess   # each plant rebinds the name the guard imports inside its function, then restores it
            import loop_lib
            import loop_witness
            spawned, real_run, real_locate = [], subprocess.run, loop_lib.resolve_kit_dir
            empty = top / ".git" / "fx-empty"   # inside the git dir, so the scratch's removal takes it too
            empty.mkdir()

            def run_mail_spawn(argv, *rest, **kw):   # the one --mail call recorded and answered zero rows
                if "--mail" in [str(a) for a in argv]:
                    spawned.append([str(a) for a in argv])
                    return subprocess.CompletedProcess(argv, 0, "", "")
                return real_run(argv, *rest, **kw)

            def run_mail_crash(argv, *rest, **kw):   # KICK-dKeptSession-44 S29: the --mail read exits 3, printing nothing
                if "--mail" in [str(a) for a in argv]:
                    return subprocess.CompletedProcess(argv, 3, "", "")
                return real_run(argv, *rest, **kw)

            def resolve_empty_kit(home, anchor, here):   # the driver's locator over an empty scratch directory
                return real_locate(home, anchor, empty if (home, anchor) == ("unattended", "unattended.sh") else here)

            def resolve_no_bash(script):
                return None
            owner, name, stand_in = {"mail-argv": (subprocess, "run", run_mail_spawn),
                                     "mail-no-driver": (loop_lib, "resolve_kit_dir", resolve_empty_kit),
                                     "mail-no-bash": (loop_witness, "resolve_bash", resolve_no_bash),
                                     "mail-read-crash": (subprocess, "run", run_mail_crash)}[case]
            real, before = getattr(owner, name), read_count()
            setattr(owner, name, stand_in)
            try:
                rc = run_verb(b4)
            finally:
                setattr(owner, name, real)
            if case in ("mail-no-bash", "mail-read-crash"):
                print("%s: fixture · commits %s" % (SAY, "unchanged" if read_count() == before else "changed"))
            if case != "mail-argv":
                return rc
            try:
                driver = (real_locate("unattended", "unattended.sh", KIT) / "unattended.sh").as_posix()
            except LookupError as e:
                driver = "unlocated: %s" % e
            got = spawned[0] if len(spawned) == 1 else ["none"] * 3
            misses = [why for ok, why in (
                (len(spawned) == 1, "%d --mail call(s) recorded, not one" % len(spawned)),
                (got[1] == driver, "argv[1] is not the located driver %s" % driver),
                (len(spawned) == 1 and got[0] == loop_witness.resolve_bash(got[1]), "argv[0] is not resolve_bash(argv[1])"),
                (got[2:] == ["--mail", "read", FX_BUILD], "the rest is not --mail read %s" % FX_BUILD),
                (rc == 0, "the move did not record")) if not ok]
            print("%s: fixture · mail-argv · %s" % (SAY, "held" if not misses else "MISSED %s · argv %s" % (
                "; ".join(misses), spawned or "none")))
            return 0 if not misses else 1
        if case in ("no-row", "empty-set"):
            before = read_count()
            argv = b4 if case == "empty-set" else b4[:7] + ["--item", "item.design.exit"] + b4[9:]
            rc = run_verb(argv)
            print("%s: fixture · commits %s" % (SAY, "unchanged" if read_count() == before else "changed"))
            return rc if case == "no-row" else run_verb(["check", *at])
        if case == "field":
            run_verb(b4 + ["--field", "colour=red"])
            run_verb(b4 + ["--field", "composition=3f9c2a71"])
            run_verb(b4)
        elif case in ("backward-rows", "skip-backward"):
            for n, tail in enumerate(BACKWARD_MOVES):
                run_verb(["record", *at, *tail, "--witness", "HEAD" if n else witness])
        else:
            run_verb(b4)
        span = "--reverse" if case == "backward-rows" else "-1"
        values = [v for v in run_fixture_git(top, "log", span, "--format=%%(trailers:key=%s,valueonly)" % TRAILER_KEY)
                  .splitlines() if v]
        for value in values or ["none"]:
            print("%s: fixture · trailer %s" % (SAY, value))
        recs = read_folder()
        if case == "default" and recs:
            read_memory_tree("build_records.py")
            import build_records
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rc = build_records.main(["read", str(top / recs[0]["path"])])
            print("%s: fixture · build_records read · exit %d · %d field(s)" % (SAY, rc, out.getvalue().count("\n")))
        if case in ("subset-log", "field", "backward-rows"):
            for m in read_transitions(FX_BUILD, top):
                print("%s: fixture · read %s · %s · %s" % (
                    SAY, m["source"], render_transition_trailer(m).split(": ", 1)[1], m["direction"]))
        if case == "backward-rows":
            held = [r for r in recs if "direction" in (top / r["path"]).read_bytes().decode("utf-8", "replace")]
            print("%s: fixture · direction stored · %d trailer(s) · %d record(s)" % (
                SAY, sum("direction" in v for v in values), len(held)))
        if case == "skip-backward" and recs:
            (top / recs[-1]["path"]).unlink()
            write_commit("the newest record, B6's, deleted")
        if case == "log-drift" and recs:
            path = top / recs[0]["path"]
            path.write_bytes(path.read_bytes().replace(b"- **To:** designing", b"- **To:** building"))
            write_commit("the record edited")
        if case == "orphan-log" and recs:
            write_transition_record(top, FX_UNIT, recs[0]["fields"])
            write_commit("a record no trailer backs")
        if case == "pre-spec":
            run_verb(["check", *at])
            write_fixture_files(top, {FX_SPEC: "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01\n" % FX_UNIT})
            write_commit("the first spec")
            run_verb(["record", *at, "--from", "designing", "--item", "item.design.exit", "--outcome", "recorded",
                      "--witness", "HEAD"])
            read_folder()
        return run_verb(["check", *at])
    finally:
        remove_tree(top)


def run_selftest():
    """The tree's own definition, then every plant's owed lines through `run_selftest_cases`, each plant
    run once and its output read by every case naming it."""
    said = {}

    def run_cached_case(argv):
        key = tuple(argv)
        if key not in said:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                if key == ("definition",):
                    found = [f for line in (TRANSITION_LINE, PROGRESS_LINE)
                             for f in check_line_definition(pathlib.Path(".").absolute(), line)]
                    for why in found:
                        print("%s: transition · %s" % (SAY, why))
                    print("%s: transition definition · AGENTS.md · %s" % (SAY, "refused" if found else "held"))
                    rc = 1 if found else 0
                else:
                    rc = main(argv)
            said[key] = (rc, out.getvalue())
        sys.stdout.write(said[key][1])
        return said[key][0]

    def read_plant_argv(plant):
        return ["--fixture", "--plant", plant]
    fx = read_plant_argv
    trailer = "%s: fixture · trailer planning -> designing · build=%s · item=item.plan.exit · sha=" % (SAY, FX_BUILD)
    check = "%s: transition check · %s" % (SAY, FX_BUILD)
    cases = [("definition", ["definition"], 0, "%s: transition definition · AGENTS.md · held" % SAY, ""),
             ("default trailer", fx("default"), 0, trailer, " · stand-in=dRankedPlan"),
             ("default record", fx("default"), 0, "%s: fixture · records 1" % SAY, "transition-1 planning -> designing"),
             ("default read", fx("default"), 0, "%s: fixture · build_records read · exit 0" % SAY, ""),
             ("default line", fx("default"), 0, "transition — %s · planning → designing · item.plan.exit · " % FX_BUILD,
              ""),
             ("default check", fx("default"), 0, check, "· 0 finding(s)"),
             ("subset-trailer-line", fx("subset-trailer-line"), 0, "%s: fixture · records 0" % SAY, ""),
             ("subset-trailer-line trailer", fx("subset-trailer-line"), 0, trailer, ""),
             ("subset-trailer-line check", fx("subset-trailer-line"), 0, check, "· 0 finding(s)"),
             ("subset-log trailer", fx("subset-log"), 0, "%s: fixture · trailer none" % SAY, ""),
             ("subset-log read", fx("subset-log"), 0, "%s: fixture · read log · planning -> designing" % SAY, ""),
             ("empty-set record", fx("empty-set"), 2, "%s: unanswered" % SAY, KEY),
             ("empty-set commits", fx("empty-set"), 2, "%s: fixture · commits unchanged" % SAY, ""),
             ("empty-set check", fx("empty-set"), 2, "%s: fixture · check · exit 2" % SAY, ""),
             ("log-drift", fx("log-drift"), 1, "%s: transition · commit " % SAY,
              "To: the trailer says designing, the record building"),
             ("orphan-log", fx("orphan-log"), 1, "%s: transition · log " % SAY, "transition-2.md · no trailer"),
             ("no-row", fx("no-row"), 1, "refused — build · planning · item.design.exit · recorded", "no row"),
             ("no-row commits", fx("no-row"), 1, "%s: fixture · commits unchanged" % SAY, ""),
             ("line-drift", fx("line-drift"), 1, "%s: transition · definition · AGENTS.md reads" % SAY, ""),
             ("pre-spec pending", fx("pre-spec"), 0, "pending — 1 move(s) before the build's first spec", ""),
             ("pre-spec order", fx("pre-spec"), 0, "%s: fixture · records 2" % SAY,
              "transition-1 planning -> designing · transition-2 designing -> building"),
             ("pre-spec check", fx("pre-spec"), 0, check, "· 0 finding(s)"),
             ("field refused", fx("field"), 0, "%s: unanswered" % SAY, "colour"),
             ("field derived", fx("field"), 0, "%s: unanswered" % SAY, "composition is derived"),
             ("field trailer", fx("field"), 0, trailer, " · composition="),
             ("field read", fx("field"), 0, "%s: fixture · read trailer · " % SAY, " · composition="),
             ("field check", fx("field"), 0, check, "· 0 finding(s)"),
             ("backward-rows trailer", fx("backward-rows"), 0, "%s: fixture · trailer testing -> building · build=%s · "
              "item=item.test.attribute · sha=" % (SAY, FX_BUILD), " · stand-in=dWitnessedBar"),
             ("backward-rows records", fx("backward-rows"), 0, "%s: fixture · records 6" % SAY,
              "transition-6 designing -> planning"),
             ("backward-rows recorded", fx("backward-rows"), 0, "%s: recorded · testing -> building · backward" % SAY,
              ""),
             ("backward-rows read", fx("backward-rows"), 0, "%s: fixture · read trailer · designing -> planning" % SAY,
              " · backward"),
             ("backward-rows stored", fx("backward-rows"), 0,
              "%s: fixture · direction stored · 0 trailer(s) · 0 record(s)" % SAY, ""),
             ("backward-rows check", fx("backward-rows"), 0, check, "· 0 finding(s)"),
             ("skip-backward", fx("skip-backward"), 1, "%s: transition · commit " % SAY,
              "· log · the move designing -> planning owes a record, and none holds it"),
             ("descope-spent refused", fx("descope-spent"), 0, "%s: unanswered · the rework budget is spent" % SAY, ""),
             ("descope-spent", fx("descope-spent"), 0, "%s: fixture · descope-spent · held" % SAY, ""),
             ("mail-open", fx("mail-open"), 1, "refused — %s · mail open %s" % (FX_BUILD, FX_QUESTION[2]), ""),
             ("mail-open commits", fx("mail-open"), 1, "%s: fixture · commits unchanged" % SAY, ""),
             ("mail-disposed commit", fx("mail-disposed"), 0, "%s: fixture · commits 1 · " % SAY,
              "1 %s record(s)" % MAIL_KIND),
             ("mail-disposed trailer", fx("mail-disposed"), 0, trailer, " · disposed=%s" % FX_QUESTION[2]),
             ("mail-disposed log", fx("mail-disposed"), 0, "%s: fixture · record %s-1 · disposed %s" % (
                 SAY, KIND, FX_QUESTION[2]), ""),
             ("mail-disposed record", fx("mail-disposed"), 0, "%s: fixture · memory/builds/%s/build/" % (SAY, FX_BUILD),
              "%s-1.md · read exit 0 · Serves %s %s · State acked" % (MAIL_KIND, MAIL_KIND, FX_UNIT)),
             ("mail-disposed next", fx("mail-disposed"), 0, "%s: fixture · next move · disposes nothing" % SAY, ""),
             ("mail-disposed check", fx("mail-disposed"), 0, check, "· 0 finding(s)"),
             ("mail-expired recorded", fx("mail-expired"), 0, "%s: recorded · planning -> designing" % SAY, ""),
             ("mail-expired commit", fx("mail-expired"), 0, "%s: fixture · commits 1 · " % SAY,
              "1 %s record(s)" % MAIL_KIND),
             ("mail-expired trailer", fx("mail-expired"), 0, trailer, " · disposed=%s" % FX_QUESTION[2]),
             ("mail-expired record", fx("mail-expired"), 0, "%s: fixture · memory/builds/%s/build/" % (SAY, FX_BUILD),
              "%s-1.md · read exit 0 · Serves %s %s · State expired" % (MAIL_KIND, MAIL_KIND, FX_UNIT)),
             ("mail-argv", fx("mail-argv"), 0, "%s: fixture · mail-argv · held" % SAY, ""),
             ("mail-no-driver", fx("mail-no-driver"), 0,
              "%s: mail · unarmed · no unattended kit holding unattended.sh in this install" % SAY, ""),
             ("mail-no-driver recorded", fx("mail-no-driver"), 0, "%s: recorded · planning -> designing" % SAY, ""),
             ("mail-no-bash", fx("mail-no-bash"), 2, "%s: unanswered · mail unknown: no bash that can see " % SAY,
              "unattended.sh"),
             ("mail-no-bash commits", fx("mail-no-bash"), 2, "%s: fixture · commits unchanged" % SAY, ""),
             ("mail-read-crash", fx("mail-read-crash"), 2, "%s: unanswered · mail unknown: --mail read %s exited 3: "
              "no output" % (SAY, FX_BUILD), ""),
             ("mail-read-crash commits", fx("mail-read-crash"), 2, "%s: fixture · commits unchanged" % SAY, ""),
             ("deps-notices", fx("deps-notices"), 0, "%s: fixture · deps-notices · held" % SAY, ""),
             ("notices-two-dependents", fx("notices-two-dependents"), 0,
              "%s: fixture · notices-two-dependents · held" % SAY, ""),
             ("notices-two-dependents passes", fx("notices-two-dependents"), 0, "%s: fixture · %s · " % (
                 SAY, FX_DEPENDENTS[1]), "confirmed pass 1 · changed pass 2 · changed pass 3"),
             ("notices-refused", fx("notices-refused"), 0, "%s: fixture · notices-refused · held" % SAY, ""),
             ("notices-refused line", fx("notices-refused"), 0,
              "notice — not posted confirmed to build:%s · rc 1 · " % FX_DEPENDENTS[0], "mail — duplicate"),
             ("notices-repeat-key", fx("notices-repeat-key"), 0, "%s: fixture · notices-repeat-key · held" % SAY, ""),
             ("notices-reposted", fx("notices-reposted"), 0, "%s: fixture · notices-reposted · held" % SAY, ""),
             ("notices-reposted rows", fx("notices-reposted"), 0, "%s: fixture · %s · " % (SAY, FX_DEPENDENTS[0]),
              "confirmed pass 1"),
             ("acks-landed", fx("acks-landed"), 0, "%s: fixture · acks-landed · held" % SAY, ""),
             ("acks-landed state", fx("acks-landed"), 0, "%s: fixture · state " % SAY, " · acked"),
             ("acks-confirmed", fx("acks-confirmed"), 0, "%s: fixture · acks-confirmed · held" % SAY, ""),
             ("acks-superseded", fx("acks-superseded"), 0, "%s: fixture · acks-superseded · held" % SAY, ""),
             ("acks-superseded refused", fx("acks-superseded"), 0, "refused — %s · mail open " % FX_BUILD, ""),
             ("acks-failed", fx("acks-failed"), 0, "%s: fixture · acks-failed · held" % SAY, ""),
             ("acks-failed stderr", fx("acks-failed"), 0, "%s: fixture · stderr · mail — ack not posted " % SAY,
              " · rc -"),
             ("acks-failed refused", fx("acks-failed"), 0, "refused — %s · mail ack not posted: " % FX_BUILD,
              "LookupError: the plant's driver does not resolve"),
             ("acks-no-session", fx("acks-no-session"), 0, "%s: fixture · acks-no-session · held" % SAY, ""),
             ("acks-no-session refused", fx("acks-no-session"), 0, "refused — %s · mail ack not posted: a1a2a3a4a5a6 · "
              % FX_BUILD, "no session id"),
             ("acks-takeover", fx("acks-takeover"), 0, "%s: fixture · acks-takeover · held" % SAY, ""),
             ("acks-takeover record", fx("acks-takeover"), 0, "%s: fixture · record · exit 0" % SAY, ""),
             ("acks-takeover chain", fx("acks-takeover"), 0, "%s: fixture · chain · a precedes b · yes · first-seen "
              "swapped · yes" % SAY, ""),
             ("acks-later-key", fx("acks-later-key"), 0, "%s: fixture · acks-later-key · held" % SAY, ""),
             ("acks-later-key refused", fx("acks-later-key"), 0, "refused — %s · mail open " % FX_BUILD, "cc33cc33cc33"),
             ("acks-later-key none", fx("acks-later-key"), 0, "%s: fixture · acks none" % SAY, ""),
             ("acks-withdrawn", fx("acks-withdrawn"), 0, "%s: fixture · acks-withdrawn · held" % SAY, ""),
             ("acks-withdrawn record", fx("acks-withdrawn"), 0, "%s: fixture · record · exit 0" % SAY, ""),
             ("acks-withdrawn line", fx("acks-withdrawn"), 0, "%s: fixture · stderr · mail — acked withdrawn " % SAY,
              " from build:fy"),
             ("acks-withdrawn-question", fx("acks-withdrawn-question"), 0,
              "%s: fixture · acks-withdrawn-question · held" % SAY, ""),
             ("acks-withdrawn-question record", fx("acks-withdrawn-question"), 0, "%s: fixture · record · exit 1" % SAY,
              ""),
             ("acks-withdrawn-question refused", fx("acks-withdrawn-question"), 0, "refused — %s · mail open " % FX_BUILD,
              "9a9b9c9d9e9f"),
             ("acks-withdrawn-question state", fx("acks-withdrawn-question"), 0,
              "%s: fixture · state 9a9b9c9d9e9f · open" % SAY, ""),
             ("chain-two-dependents", fx("chain-two-dependents"), 0, "%s: fixture · chain-two-dependents · held" % SAY,
              ""),
             ("chain-two-dependents record", fx("chain-two-dependents"), 0, "%s: fixture · record · exit 0" % SAY, ""),
             *(("chain-two-dependents state %s" % mid, fx("chain-two-dependents"), 0, "%s: fixture · state %s · acked"
                % (SAY, mid), "") for mid in ("a1a1a1a1a1a1", "b1b1b1b1b1b1", "a2a2a2a2a2a2", "b2b2b2b2b2b2")),
             ("chain-two-dependents chain", fx("chain-two-dependents"), 0, "%s: fixture · chain tFix · a1a1a1a1a1a1 "
              "precedes a2a2a2a2a2a2 · sent yes · filtered no" % SAY, ""),
             ("chain-two-dependents sent", fx("chain-two-dependents"), 0, "%s: fixture · sent fy · 4 row(s) · seq and "
              "after on 4" % SAY, ""),
             ("chain-two-dependents refused", fx("chain-two-dependents"), 0, "%s: fixture · sent build:fy · refused · "
              % SAY, "exited 2: mail — not read · --sent reads one build's own mail refs, and 'build:fy' is no build's "
              "slug"),
             ("notify-micro", fx("notify-micro"), 0, "%s: fixture · progress 0" % SAY, ""),
             ("notify-every", fx("notify-every"), 0, "%s: fixture · progress 3" % SAY, ""),
             ("notify-every transition", fx("notify-every"), 0, render_progress_line(
                 FX_BUILD, "transition", "planning → designing · item.plan.exit"), ""),
             ("notify-every landing", fx("notify-every"), 0, "progress — %s · landing · " % FX_BUILD, ""),
             ("notify-park-landing", fx("notify-park-landing"), 0, "%s: fixture · progress 2" % SAY, ""),
             ("notify-park-landing park", fx("notify-park-landing"), 0, "progress — %s · park · item fx-fork" % FX_BUILD,
              ""),
             ("notify-park-only", fx("notify-park-only"), 0, "%s: fixture · progress 1" % SAY, ""),
             ("notify-park-only park", fx("notify-park-only"), 0, "progress — %s · park · item fx-fork" % FX_BUILD, ""),
             ("progress unknown event", ["progress", "--build", FX_BUILD, "--event", "lunch", "--detail", "x"], 2,
              "%s: unanswered · the event lunch is none of park, landing, transition" % SAY, ""),
             ("notify-shape", fx("notify-shape"), 1, "%s: transition · definition · AGENTS.md reads %s, " % (
                 SAY, PROGRESS_LINE.replace(" · <detail>", "")), "while the renderer writes %s" % PROGRESS_LINE),
             ("notify-shape check", fx("notify-shape"), 1, check, "· 1 finding(s)")]
    return run_selftest_cases(run_cached_case, cases, "%s: transition selftest" % SAY)


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="loop_transition.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run record and check over a scratch repository")
    ap.add_argument("--plant", choices=list(PLANTS))
    sub = ap.add_subparsers(dest="verb")
    rec = sub.add_parser("record", help="record one build move on the channels the set selects")
    for flag in ("--build", "--from", "--item", "--outcome", "--witness"):
        rec.add_argument(flag, required=True)
    rec.add_argument("--fact", action="append", default=[], help="k=v, a fact a row's guard or target reads")
    rec.add_argument("--field", action="append", default=[], help="k=v, a registered extension field")
    rec.add_argument("--root", default=".")
    chk = sub.add_parser("check", help="hold each channel of a build's moves to its trailer")
    chk.add_argument("--build")
    chk.add_argument("--root", default=".")
    chk.add_argument("--selftest", action="store_true", help="the tree's definition, then every plant")
    dep = sub.add_parser("dependents", help="the builds --build's README's rendered build-edges region names "
                                            "as its child builds, one per line")
    dep.add_argument("--build", required=True)
    dep.add_argument("--root", default=".")
    pro = sub.add_parser("progress", help="print the owner's progress line where notify.owner selects the event")
    pro.add_argument("--build", required=True)
    pro.add_argument("--event", required=True, help="park, landing or transition")
    pro.add_argument("--detail", required=True)
    pro.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    if args.fixture != bool(args.plant) or (args.fixture and args.verb):
        ap.error("--fixture takes --plant <case> and no verb")
    if args.fixture:
        return run_transition_fixture(args.plant)
    if args.verb is None:
        ap.error("a verb, record, check, dependents or progress, or --fixture --plant <case>")
    if args.verb == "check" and args.selftest != (args.build is None):
        ap.error("check takes --build <slug>, or --selftest alone")
    if args.verb == "check" and args.selftest:
        return run_selftest()
    pairs = {}
    for flag in ("fact", "field"):
        pairs[flag] = {}
        for text in getattr(args, flag, None) or []:
            k, eq, v = text.partition("=")
            if not (k and eq):
                ap.error("--%s takes k=v, and %r is not" % (flag, text))
            pairs[flag][k] = v
    root = pathlib.Path(args.root).absolute()
    try:
        if args.verb == "dependents":   # KICK-dKeptSession-7 S9: the builds a landing or Design's exit notifies
            for slug in read_dependents(root, args.build):
                print(slug)
            return 0
        if args.verb == "progress":   # KICK-dKeptSession-11 S3: the event checked before any policy read
            known = tuple(dict.fromkeys(e for events in NOTIFY_OWNER_EVENTS.values() for e in events))
            if args.event not in known:
                raise ValueError("the event %s is none of %s" % (args.event, ", ".join(known)))
            if args.event in derive_owner_events(read_policy_value(root, NOTIFY_KEY, "HEAD")):
                print(render_progress_line(args.build, args.event, args.detail))
            return 0
        if args.verb == "record":
            move, commit, wrote, line, said = write_transition(root, args.build, getattr(args, "from"), args.item,
                                                               args.outcome, args.witness, pairs["fact"], pairs["field"])
            for text in said:
                print(text)
            for rel in wrote:
                print("%s: wrote %s" % (SAY, rel))
            direction = derive_direction(move["from"], move["to"], read_transition_rows(*read_definition(KIT)))
            print("%s: recorded · %s -> %s · %s · %s" % (
                SAY, move["from"], move["to"], direction,
                "commit %s" % commit[:8] if commit else "no commit: the set stores neither trailer nor log"))
            if line:
                print(line)
            return 0
        lines, findings = check_transition_channels(args.build, root)
    except TransitionRefused as e:
        print("refused — %s" % e)
        return 1
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    except (ValueError, OSError) as e:
        print("%s: unanswered · %s" % (SAY, e))
        return 2
    for why in findings:
        print("%s: transition · %s" % (SAY, why))
    for line in lines:
        print(line)
    return 1 if findings or any(ln.startswith(("pending — ", "unstored — ")) for ln in lines) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
