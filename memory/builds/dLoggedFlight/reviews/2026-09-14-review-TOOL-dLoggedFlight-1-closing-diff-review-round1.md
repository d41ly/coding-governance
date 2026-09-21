**Serves:** diff-review TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13

# dLoggedFlight — the CLOSING diff review, ROUND 1

*This is an adversarial Tier-2 pass over what the thirteen units SHIPPED. Node `d`, 2026-09-14, on
`branch/unattended-build-transparency-ea83a5` at HEAD `36d531b9`. This is ROUND 1 of the closing
review. Its shape was four primed finder lenses, then a skeptic stage of five batches prompted to REFUTE
each finding, then one synthesis pass, which is this record. The lenses covered the runlog kit, the
three producers, the unattended Skill and protocol templates, the BUILD-METHOD trailer and the
drift-audit signal. The three earlier records under `reviews/` are SPEC audits:
[round 1](2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md),
[round 2](2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) and
[round 3](2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md). None of their findings is
raised again here. Every cited line was re-read at `36d531b9`. The severities in the table are this
synthesis's own adjudication, not the finders' grades. Some figures were measured by this synthesis,
and "What this synthesis re-derived" lists them. Where a figure is a finder's or a skeptic's and was
not measured again, the text says so. The binding contracts are
`memory/guides/UNATTENDED-PROTOCOL.md` and `memory/guides/BUILD-METHOD.md`.*

**Range, ROUND 1:** `9ce37fcced5f9b4525f73b7c7663de3453522c4a...36d531b9`. This is the build's
cumulative change on top of origin/main as it was reconciled. `9ce37fcc` is the origin/main tip that
the merge `9ed23769` brought into the branch, so the three-dot range holds exactly this build's own
change set: 56 commits, 120 files, +25026/−112. The run's own pinned BASE is `a4007553`, the mandate
commit, and its parent `9fac2b53` is the base the specs state. The review is not pinned to
`a4007553`, because a range from there would include again everything `9ed23769` merged in from main.

## Verdict: BLOCKED

The finding set is one BLOCKER, two HIGHs, seven MEDIUMs and five LOWs. That is fifteen distinct
defects from eighteen confirmed reports.

**The blocker breaks the property that makes it acceptable to commit run records to a public
repository.** The closed schema keeps owner turns to counts per position, and spec 9 rejects owner-turn
clock times in so many words. The model, though, computes idle gaps over a timeline that still holds
the in-window owner turns, and the record renders each gap's start and length. So when an owner turn
opens a gap, the gap row's UTC is that turn's time. When an owner turn closes a gap, the turn's time is
that UTC plus the duration. The README accepts the second case as residue. That sentence was written in
the unit-9 build commit, and no audit round read it. The first committed run record is this run's own
placement-2 render, and it rides the merge to a public remote. This record leaves out the example one
finder quoted, because that example was an owner turn's time.

The two HIGHs are about the answers a committed record gives on an ordinary run:

- **H1: idle gaps ignore tool calls.** On this build's own model, every one of the 23 idle-gap
  anomalies is false. Between them the gaps hold 4303 of the window's 5480 tool calls. They also push
  the Anomalies table past its bound, so the other six anomalies, all destructive-git, lose their
  times.
- **H2: the primary tree becomes one of the run's worktrees.** Once `--landed` runs in the primary
  tree, that tree counts as the run's for the whole window. Another run's landing push and bar then
  join this run's Timeline and its journal commitment.

**The design stands.** The four spec-audit highs were folded into code that does what they asked:

- Progress is read from the run's own commits.
- Windows are half-open and bounded to the era.
- The landing push joins by the sha it pushed.
- A journal START joins its start commit by the spec's named key.

Every finding sits at an edge of those rules: which events a gap or a window counts, which trees count
as the run's, and at which moment a key is read. Every fix uses mechanisms this build already has, so
B1 is disposed as a FOLD, not a PROMOTE. BUILD-METHOD then owes a re-review of the fix, not of the
whole diff. That re-review matters here: B1, H1 and H2 all rewrite the same stretch of
`build_run_model`, and fold text is where the next round's findings usually are.

## Run integrity

- Lenses: **4 of 4** returned, **0 died**.
- Skeptic batches: **5 of 5** returned, **0 died**.
- Verdicts: **0** contradictory ones demoted to unverified, **0** spurious ones discarded, **0**
  duplicates.
- Unverified findings: **0**.

Every stage returned, so for this lens set the run is complete. A zero anywhere below is a result of
the lens set, not a gap left by an agent that died. It is still weaker than evidence of absence in one
respect: the twelve refuted findings were not handed to this synthesis, so this record cannot say which
surfaces they covered.

## Review shape

- Raw findings **30**, confirmed **18**, refuted **12**, unverified **0**, precision **0.60**.
- The 18 confirmed reports collapse to **15** distinct defects. Three pairs each describe one defect
  that two lenses reported: reports 2 and 18 (M1), 8 and 24 (M2), and 10 and 23 (H1). The pipeline's
  duplicate count of 0 counts only byte-identical reports. These pairs differ in wording and in
  reproduction, so merging them was this synthesis's decision.
- Precision 0.60 is above the retune floor of about 0.5, so the lens set and the priming stay as they
  are.
- Severity is this synthesis's call. Every confirmed report arrived graded medium or low. One is a
  BLOCKER here (B1) and two are HIGH (H1, H2), and the reasons are given under each.

## Lens brief — the bug classes this range selected

`python tools/memory-tree/gotchas.py --for-diff 9ce37fcc..36d531b9` selects 44 classes over the 120
changed files: 39 by anchor, plus 5 universal ones. Ten findings are instances of a class on that
list:

- `two-answers-to-one-question`: H1 (the timeline says idle while `tools` says busy), M1 (`tools` is
  windowed and attribution is not), L2 (the Skill says `absent` where the model says `dead`) and L4 (two
  slug grammars).
- `fallback-fabricates-the-passing-value` and `degradation-known-but-unreported`: M6.
- `two-readers-of-one-config-one-re-derived`: M7.
- `one-value-field-records-a-mixed-outcome`: M3.
- `vacuous-selector-empty-population` and `fixture-passes-by-finding-nothing`: M2.
- `fold-text-is-unreviewed-surface` and `amendment-leaves-its-other-half-standing`: M5, and the README
  residue under B1.
- A close relative of `id-matched-as-a-substring`: L5.

Five fit no class on the list. Two of them suggest new classes, which their left-shift lines name:
B1 (a withheld value you can recover from a rendered value derived from it) and H2 (a join key widened
by a location every run shares). M4, L1 and L3 stay unclassed.

## Findings

| # | Severity | Location | Defect | Reports |
|---|---|---|---|---|
| B1 | BLOCKER | `tools/runlog/model.py:1344` | Idle gaps use in-window owner turns as endpoints, so an owner turn's clock time reaches the committed record as an idle row's UTC, or as its UTC plus its duration | 1 |
| H1 | HIGH | `tools/runlog/model.py:1344` | `idle-gap` is judged over a timeline that never holds a tool call, so busy stretches read as idle: all 23 gaps on this build's model are false | 10, 23 |
| H2 | HIGH | `tools/runlog/model.py:1242` | The worktree join key is every tree any of the run's verbs ran in, so `--landed` in the primary tree makes every primary-tree push and bar in the window this run's | 7 |
| M1 | MEDIUM | `tools/runlog/model.py:715` | Attribution counts every tool call of every named session with no window bound, and a later run's END never supersedes this run's | 2, 18 |
| M2 | MEDIUM | `tools/runlog/model.py:1416` | The `pushes` dead proof needs a LANDED move inside a window that ends at that move, so it can never fire | 8, 24 |
| M3 | MEDIUM | `tools/runlog/model.py:1351` | A `--close` END reading `rc=0 exit=unclean` counts as a successful close | 15 |
| M4 | MEDIUM | `tools/runlog/model.py:1183` | Own commits are bounded by era rather than by window, so a later commit naming a unit id moves `last_own`, unjoins the landing push, and makes `verify` report a changed journal | 16 |
| M5 | MEDIUM | `tools/runlog/model.py:1235` | A non-terminal window ends one second past the last driver line or run-state commit, and ignores the run's own later commits, bars and transcript events | 17 |
| M6 | MEDIUM | `tools/runlog/record.py:614` | When transcripts are not-local, owner turns, usage and attributed calls render as a literal 0 rather than `-` | 26 |
| M7 | MEDIUM | `tools/runlog/runlog_lib.py:360` | `MEMORY_ROOT="v"  # note` is read with its quotes kept, so the schema leg reds every bar at an adopter who uses that legal spelling | 27 |
| L1 | LOW | `.githooks/pre-push:146` | Under an `insteadOf` rewrite, git passes the typed URL as `$1`, and the hook writes it as `remote=`, credentials included | 4 |
| L2 | LOW | `tools/runlog/model.py:654` | A run made on another node reads `driver: dead`, where the Skill tells the agent it reads `absent` | 12 |
| L3 | LOW | `tools/runlog/model.py:259` | After a memory-root move, every rotated build's archive and live record share one start, and `check-records` refuses them from then on | 13 |
| L4 | LOW | `tools/runlog/extract.py:64` | The extractor's slug grammar rejects dashed and single-letter slugs that the driver accepts | 14 |
| L5 | LOW | `tools/runlog/model.py:1051` | The unit-id reader does not expand the `N..M` range spelling, so eight whole-set commits are credited to unit 1 alone | 20 |

### B1 — an owner turn's clock time reaches the committed record (BLOCKER)

**Where.** Four places combine:

- `tools/runlog/model.py:1330-1332` appends each in-window owner event to `timeline`.
- `:1344` builds the gap list, `inside`, from that same list, and `:1347` emits each gap at `a["t"]`,
  which is its start.
- `tools/runlog/record.py:501` drops `owner` rows. That is the only kind the timeline holds that the
  renderer withholds (`:95-96`).
- `record.py:487-490` renders each idle row's UTC and duration. The idle-gap anomaly carries the same
  start (`model.py:993`) into the Anomalies UTC column (`record.py:559-563`).

**Defect.** When an owner turn opens a gap, the idle row's UTC is that turn's time, to the second. When
one closes a gap, the turn's time is that UTC plus the duration. Owner is the only kind the renderer
withholds. So a gap endpoint with no rendered row beside it can only be an owner turn, or, in a long
run, a row the Timeline elided. The spec says the opposite in two places:

- Spec 9 S4 says owner turns appear "as counts per position, with no clock time".
- Spec 9's alternatives reject owner-turn clock times "as new public data about when the owner was at
  the keyboard".

`tools/runlog/README.md:353-354` accepts the gap-end case as residue. That line arrived in the unit-9
build commit `33b25e3f`, after the last spec audit. The gap-start case is not mentioned anywhere.

**Reached by.** Any run with an in-window owner turn next to 15 minutes with no timeline event. Per
H1, that is any 15 minutes with no commit, verb, bar or push. This synthesis measured it on this build's
own model: one of the 23 gaps ends exactly on one of its two in-window owner turns. The record rendered
at HEAD does not show that gap, but only by accident, for two reasons:

- The Timeline elides its middle beyond 30 rows at each end.
- The 29 anomalies exceed the bound of 20 rows, so the Anomalies table is aggregated.

A sparser run has neither protection. The first committed run record is this run's placement-2 render
(`tools/unattended/SKILL.template.md:787-789`), which rides the merge to a public remote. Once a time is
published there, it cannot be withdrawn.

**Why BLOCKER.** The record's premise is that its closed schema makes run data safe to publish. This
defect breaks that premise, on the one value the spec singled out. And a README line written during an
unattended run narrowed an explicit spec decision without an owner ruling.

**Fix.** Build the gap sequence without owner events:
`[e for e in timeline if check_in_window(e["t"]) and e["kind"] != "owner"]`. Merge this with H1's fix,
so that tool-call times fill the sequence too. Once the arm below holds, delete the README residue
rather than rewording it.

**Left-shift.**

- A self-test arm with an owner turn at a gap's start, another at a gap's end and a third inside a gap.
  It asserts that no rendered UTC, and no UTC plus duration, equals any owner turn's second.
- A render-time refusal: before writing, `record` compares every rendered idle row's endpoints with the
  model's owner turns and refuses on a match.
- A new class filed under `memory/gotchas/`: a withheld value you can recover from a rendered value
  derived from it.

### H1 — idle-gap never sees a tool call (HIGH)

**Where.** `tools/runlog/model.py:1338-1342` puts each in-window tool call in `tools`, and usage events
are never kept. `:1344-1347` computes gaps over `timeline` alone. `:991-994` turns each gap into an
`idle-gap` anomaly reading "N s with no event".

**Defect.** Spec 8 S6 defines `idle-gap` as fifteen minutes or more "with no event of any source" (spec
8 line 140), and spec 8 S3 takes idle gaps "from the extractor where local". The code reads only the
sources the rendered timeline holds. `stalled` has the same blind spot, but it follows its spec as
written, so it is noted here and not counted.

**Reached by.** Every run with a turn of 15 minutes or more that makes no commit and runs no verb: a
unit build, a Tier-2 review workflow, or a 26-minute bar. This synthesis measured this build's model at
HEAD, with the driver journal partial and transcripts present:

- 23 of the model's 29 anomalies are `idle-gap`.
- The 23 gaps hold 4303 of the window's 5480 tool calls, and every one of them holds at least one.
- The first gap reads 3053 s from 2026-09-13T11:07:25Z, and 642 tool calls ran inside it.

The record rendered at HEAD therefore reads `anomalies: 29 · shown 0 · aggregated yes`. The other six
anomalies, all `destructive-git`, lose their UTC to the aggregation. This review did not examine
whether those six are themselves correct.

**Fix.** Compute gaps over one time-sorted sequence, and render none of the added times. The sequence
holds:

- the timeline times, excluding owner turns;
- each in-window tool call's start and end;
- the window's usage times.

Emit `idle-gap` only when the driver journal or the transcripts cover the window, meaning either reads
`present` or `partial`. Otherwise record in Coverage that idleness could not be judged, rather than
reporting missing sources as idle time.

**Left-shift.**

- A self-test arm with 20 minutes of workflow tool calls between two timeline events, where no
  `idle-gap` fires.
- A git-only arm that expects no `idle-gap` and expects the could-not-be-judged note.
- A model invariant, asserted by every model arm: no idle gap contains an in-window `tools` entry.

### H2 — the primary tree becomes the run's worktree (HIGH)

**Where.** `tools/runlog/model.py:1242` builds the join key from every `wt` in the run's driver segment.
Three joins then take any in-window line from those trees: pushes at `:1277`, `ev=once` refusals at
`:1297` and bars at `:1307`.

**Defect.** `--landed` runs on the default branch in the primary tree: spec 11 S6 says the build
"merges into `main` in the primary tree". An owner running `--status` there is also ordinary. From that
call on, the primary tree is one of the run's worktrees for the whole window. For a landed run, the
window runs from the preflight START to the `--landed` END. Spec 8 line 219 promises "A bar run in
another worktree at the same minute is never attributed". Yet the primary tree is exactly the tree
every other run lands from.

**Reached by.** Two runs on one node whose windows overlap. That is ordinary in this repository, where
the primary tree is shared and builds land from it several times a day. When run A renders its
placement-3 record, three things go wrong:

- Run B's landing push and its bar join A by worktree.
- Both enter A's Timeline and A's journal commitment.
- A refused raw push to `main` by anyone in the primary tree fires `push-outside-lander` on A.

A skeptic reproduced this on the self-test's landed fixture, with the `--landed` START moved to the
primary tree. A foreign refused push at minute 10 and a foreign bar at minute 12 both joined by
`worktree`, both entered `journal_lines`, and the anomaly fired. No AC10 arm stages `--landed` from any
tree but `FX_WT_RUN`.

**Fix.** Build the worktree key only from the trees where the run's own pre-close verbs ran: the
joined preflight and the unit-bearing verbs. Exclude `--status` and `--landed`. The landing push then
joins by pushed sha and the landing bar by its `gate_run` pin, which are what those keys exist for. If a
tree has to stay in the key, bound its join to the span between that tree's first and last pre-close
verb.

**Left-shift.** An AC10 arm with these parts:

- `--landed` and a `--status` run from `FX_WT_PRIMARY`;
- a foreign bar and a foreign refused push in the primary tree in mid-window;
- assertions that neither line joins, that `journal_lines` excludes both, and that
  `push-outside-lander` does not fire.

Then file the class under `memory/gotchas/`: a join key widened by a location that every run shares.

### M1 — attribution counts calls outside the window (MEDIUM)

**Where.** `tools/runlog/model.py:1423` calls `derive_attribution(seg, extracts)`, and `:715-741`
counts every `tool` event of each extract. Compare `:1338`, where `tools` is windowed, and `:1434`,
where usage is. The attribution points come only from this slug's segment (`:703-709`).

**Defect.** A call after the run's last END takes that END's unit and phase. That includes calls made
after the close and calls of a later run in the same session. The later run's own END is filtered out,
so it never supersedes this run's. This contradicts spec 8 S8's "the most recent unit-bearing END", and
the model's own METHOD string at `:122`.

**Reached by.** Every re-render, because the session keeps working after the window closes. This
synthesis built the model twice, minutes apart:

- First build: `attributed calls` read 2968 of 7219.
- Second build: it read 2971 of 7222.
- Both times, the window (closed at 2026-09-14T05:34:12Z) held 5480 tool calls.

So the committed Summary line (`tools/runlog/record.py:615`) moves on every re-render. In a multi-run
session, which the model flags as `multi-run-session`, the next build's work is credited to this run's
last unit.

**Fix.** Pass `w_start` and `w_end` in and skip calls outside them, as `build_run_usage` does. Build the
points from every invocation in the session, that is `all_invs` filtered by session, so a later END of
any slug supersedes. A call whose latest END belongs to another slug does not belong to this run.

**Left-shift.**

- An AC17 arm with one same-session call after the run's `--landed` END and one after another slug's
  `--brief` END. It asserts neither call is counted.
- The invariant that `attribution.calls` equals `len(tools)`, asserted on every model arm.

### M2 — the pushes liveness probe cannot move (MEDIUM)

**Where.** `tools/runlog/model.py:1409-1417`. The window end comes from `derive_window` (`:329-333`),
and `check_in_window` (`:1239-1240`) is half-open.

**Defect.** `pushes` reads `dead` only when a LANDED move lies inside the window. But a landed run's
window ends exactly at that move: at the `--landed` END when the journal holds it, and otherwise at the
first terminal write. `t < w_end` excludes both, and the LANDED record commit comes after the verb
anyway. So on every landed run, a pre-push writer that wrote nothing reads `present` with 0 lines.
`gates` works because its proof, a LANDING move, comes before the window end. The rule is rev-5 text
(spec 8 lines 443-444), which no audit round read.

**Reached by.** Two skeptics reproduced it independently on the kit's `build_landed_fixture`. They
removed the landing push and used a pushes journal whose epoch predates the run. `pushes` read
`present` with 0 lines, both with and without the driver journal. Under the same absence, `gates` reads
`dead`. AC10 asserts only the passing side.

**Fix.** Judge the proof on the terminal move itself, by either of two tests:

- `term_end is not None` with `phase_to == "LANDED"`;
- the run's phase is LANDED and its terminal write exists.

Or, in this one test only, admit the terminal END with `w_start <= t <= w_end`.

**Left-shift.** For each journal, an arm that stages its `dead` state and observes it, starting with the
landed fixture without its push. The §7 rule that a new gate is not landed until its failing case has
been observed applies to each coverage state as much as to a leg.

### M3 — a killed `--close` reads as a successful one (MEDIUM)

**Where.** `tools/runlog/model.py:1351` keeps a `--close` END on `rc == "0"` alone.
`tools/runlog/record.py:475` renders that rc without its `exit` value.

**Defect.** The driver documents that an unclean END's rc is whatever `$?` its EXIT trap saw, which is
often 0, and says to read `exit=` first (`tools/unattended/unattended.sh:4923-4928`). A skeptic
reproduced `rc=0 exit=unclean` in this Git Bash, after an untrapped TERM during a foreground child. The
model then takes that END as the close, with two effects:

- `green-at-close` is judged against it. It can read MET from an earlier GREEN at the same head, even
  though no LANDING was ever written.
- The END becomes the boundary between in-window and post-close owner turns.

Every other rc consumer in the file requires `exit == "clean"`: `check_record_creating`,
`refusal-loop` and `derive_merged_subclass`.

**Fix.** Require `exit == "clean"` in the `closes` filter, or require that the verb moved the phase into
LANDING. In `derive_timeline_values`, render rc as `-` whenever `exit` is not `clean`, so the committed
Timeline never shows a killed verb as rc 0.

**Left-shift.**

- An arm with a `--close` END reading `rc=0 exit=unclean` that expects `close.t` to be None and
  `green-at-close` to be UNJUDGEABLE.
- A source arm asserting that every read of an END's `rc` in `model.py` is paired with a read of its
  `exit`.

### M4 — `last_own` moves after the run, and `verify` reports tampering (MEDIUM)

**Where.** Three places in `tools/runlog/model.py`:

- `:1181-1185` bounds own commits by era, and for a build's last run the era is open to HEAD.
- `:1189-1193` takes the descendants of `last_own`.
- `:1279-1284` is the pushed-sha join.

**Defect.** Any later commit on the default branch whose subject names one of the build's unit ids
becomes `last_own`. The landing tip is then its ancestor rather than its descendant, so the landing
push stops joining by pushed sha. It cannot join by worktree either, because the lander pushes from the
primary tree. The push's `gate_run` pin is lost with it.

**Reached by.** History of this shape already exists: `e2cb770c` names two unit ids of a build after
that build closed. After such a commit, `runlog.py verify` rebuilds the model
(`tools/runlog/record.py:935-941`) and finds fewer journal lines. It then reports "the journal changed
after the render", although no journal byte changed. That is a false tamper signal. Any re-render also
moves the Summary's `own commits` and `last own commit` values and the Units counts.

**Fix.** For a terminal run, keep only own commits made before the window end. Test the pushed sha
against the last own commit at or before the push's START, not against whatever `last_own` is when the
model is built.

**Left-shift.** A landed-fixture arm that adds a later commit naming a unit id. It asserts that `verify`
still returns `match` and that the landing push still joins by `pushed-sha`.

### M5 — a non-terminal window ignores the run's own later work (MEDIUM)

**Where.** `tools/runlog/model.py:1235-1236` passes only the driver segment's last line to
`derive_window`. That function's last-activity branch (`:334-337`) takes whichever is later: that line
or the last run-state commit.

**Defect.** Spec 8's rev-5 line says a non-terminal window "closes one second past its last event, so
that event is inside it" (lines 438-439). The code looks at only two of the run's sources to find its
last event. Own commits, bars, pushes and transcript events after the last driver line or run-state
write fall outside the window. Yet the timeline still lists the later own commits and slug-naming
merges, because those are bounded by era. The record then lists events outside its own stated window.

**Reached by.** This build, as measured by this synthesis:

- The window ends 2026-09-14T05:34:12Z, by `last-activity`.
- Three own commits sit after that on the timeline: `d99edec6` at 05:35:04Z, `454b9016` at 05:52:24Z
  and `9e9109da` at 05:58:36Z. So does the merge `9ed23769`.
- The gates journal holds this run's two bars from its own worktree: RED at `9e9109da` (06:11:20Z) and
  GREEN at `36d531b9` (07:02:58Z).
- Coverage still reads `gates absent, 0 lines`.

A run that dies without making another driver call loses exactly the evidence that the question "why
did it stop" needs.

**Fix.** Take the window end over every source the run owns:

- the driver segment;
- the run-state commits;
- the own commits and slug-naming merges;
- the journal lines from the run's pre-close trees, which is H2's narrowed key and does not need the
  window to join.

Bound the commit and merge timeline events by the same window. The finder proposed adding only
`own[-1]["t"]`, but that would still leave both bars outside the window here, because they come after
the last own commit.

**Left-shift.**

- A non-terminal fixture with an own commit and a bar from the same tree twenty minutes after the last
  driver line, both expected inside the window.
- A model invariant that every timeline event lies in `[start, end)`. It catches this defect and M1
  together.

### M6 — an unknown count renders as a clean zero (MEDIUM)

**Where.** `tools/runlog/record.py:614-618` renders owner turns, the three usage lines and attributed
calls with 0 as the default. `tools/runlog/model.py:1423-1434` produces zeros from empty inputs.

**Defect.** When transcripts are `not-local`, those five facts read as counts of zero, although the
schema's value for an absent fact is `-` (spec 9 S4). An `in-window 0` owner-turn count reads as a
clean unattended run. The runlog Skill routes "what did it decide without asking" to these counts
(`tools/runlog/SKILL.template.md:63`), and its warning that zero means unknown covers usage only
(`:71-72`).

**Reached by.** Every adopter on the shipped default. `tools/unattended/.unattended.conf.example:263`
leaves `RUNLOG_SESSION_VARS` blank, so the journal names no session, and the Skill's record step runs
no discovery. A finder rendered this build with an empty state directory and an empty transcripts
directory, and got `owner turns: launch 0 · pre-run 0 · in-window 0 · post-close 0` and
`attributed calls: 0 of 0`. The true counts are 1, 1, 2 and 0. This repository sets the variable, so
its own records are safe unless a run's environment leaves it unset.

**Fix.** In `build_summary_facts`, pass None for those five facts whenever the transcripts' coverage
state is neither `present` nor `partial`, so they render `-`. Extend the Skill's warning to the
owner-turn counts.

**Left-shift.**

- An arm that renders a `not-local` model and expects `-` in each of the five facts.
- Better, a schema-leg rule over committed records: a Summary fact derived from transcripts must read
  `-` when the same record's Coverage row for transcripts is neither `present` nor `partial`. Both
  values are in the record, so the leg can check this without a journal.

### M7 — the conf reader keeps quotes when a comment follows (MEDIUM)

**Where.** `tools/runlog/runlog_lib.py:360-363`.

**Defect.** `MEMORY_ROOT="docs/memory"  # note` reads as `"docs/memory"`, quotes included. Stripping
the quotes requires the value's first and last characters to match, and a trailing comment breaks that.
The fallback then takes the first word, quotes and all. Bash sourcing and the memory-tree kit's
`parse_conf_line` both read `docs/memory`, and that parser's own notes record this exact spelling as
one its first version missed. AC10 tests a quoted value and a commented value, but never both on one
line (`tools/runlog/selftest.py:592-601`).

**Reached by.** Any adopter using that legal spelling. The `runlog record schema` leg has no guard, so
it runs on every bar. It finds no tracked file under the quoted root and reds its `root` liveness
check. `record` and `model` refuse with "no run-state file". The failure is loud rather than silent,
which is why this is MEDIUM rather than higher.

**Fix.** Follow `parse_conf_line`'s order. A value that opens with a quote takes the text up to the
matching quote and drops the rest. An unquoted value ends at a `#` that begins a word.

**Left-shift.** AC10 rows for `KEY="v"  # c` and `KEY='v' # c`, each compared against
`bash -c 'set -a; . conf; printf %s "$MEMORY_ROOT"'` over a table of spellings. Then bash grades the
reader, rather than a copy of the reader's own expectation.

### L1 — `pre-push` can write the typed URL, credentials included (LOW)

**Where.** `.githooks/pre-push:146`, with `url_userinfo` computed from `$2` alone at `:148-152`.

**Defect.** The hook treats `$1 != $2` as proof that `$1` is a remote name. That fails under a
`url.<x>.insteadOf` or `pushInsteadOf` rewrite of a URL typed on the command line: git then passes the
typed URL as `$1` and the rewritten one as `$2`. A skeptic reproduced this in a scratch repository on
git 2.54. The hook writes `remote=<typed URL>`, and `url_userinfo` stays unset. This breaks both the
hook's own invariant at `:65` and spec 4 S3.

**Reached by.** A plain URL is written whenever an `insteadOf` rule matches a typed URL. Writing a
credential needs a rule that matches a typed URL carrying credentials, which is rare. The file is
machine-local. This synthesis checked that no committed record renders the field: a push row carries
only the decision, rc and lander (`tools/runlog/record.py:479-482`). `runlog.py journal --producer
pushes` does echo it.

**Fix.** Write `remote=` only when `$1` has the shape of a remote name, meaning no `/`, `\`, `:` or `@`.
Otherwise write `remote_unnamed=1`. Compute `url_userinfo` over both arguments.

**Left-shift.** An arm in `tools/unattended/runlog-writer.test.sh` with an `insteadOf` rule and a typed
URL carrying credentials. It asserts that the pushes line carries `remote_unnamed=1 url_userinfo=1` and
no `://` or `@` byte.

### L2 — another node's run reads `dead` (LOW)

**Where.** `tools/runlog/model.py:654`. The Skill's contrary text is at
`tools/runlog/SKILL.template.md:69`.

**Defect.** Journals never leave their clone. Take a run made on node Y, seen from node X. It has no
lines in X's journals. Its window comes from git, so once X has writers, the window starts after X's
journal epoch. Its parked rows are in the window. `measure_coverage` therefore returns `dead` for the
driver, and for gates too once the run has a LANDING write. The model has no node identity, so it
cannot tell this case from a broken writer. The Skill tells the agent that such journals read `absent`.

**Fix.** Report `dead` only when the journal holds at least one line naming the slug. Otherwise report
`not-local`, which `COVERAGE_STATES` already has, with a note. Or change the Skill's text to match the
state.

**Left-shift.** An arm with parked rows in the window and a journal whose epoch precedes it but whose
lines all name another slug. It expects `not-local`.

### L3 — a memory-root move collapses rotated runs (LOW)

**Where.** `tools/runlog/model.py:259` reads `git log --no-renames --diff-filter=A` under the current
memory root only.

**Defect.** Moving the memory root or a build folder shows up as one commit that ADDS the live `RUN.md`
and every archive at once. So the archive at position 0 and the live record both start at the move
commit. From then on:

- `check_run_states` (`tools/runlog/record.py:1323-1330`) refuses `run-start` on every bar, and no
  fix can keep the history.
- `verify` looks up the old key and raises.
- `record --write` creates a second file.

The README expects the root to move: `tools/runlog/README.md:310` names a moved memory root among the
things the Skill leg reds on until someone re-renders. The leg's list of what it does not check does
not mention this case.

**Fix.** Treat a commit that adds both an archive and the live record of one build, with no earlier
entry, as a relocation. Follow the pre-move path, or fall back to the archive's own run-key facts. At
minimum, name the limit in the leg's does-not-check list and give it a waiver route.

**Left-shift.** An arm next to AC5's squashed-history fixture: a rotated build, then a `git mv` of its
memory root. It expects either distinct starts or the named refusal.

### L4 — two slug grammars (LOW)

**Where.** `tools/runlog/extract.py:64` spells the slug `[A-Za-z][A-Za-z0-9]{1,63}`. The driver's
`check_slug_shape` (`tools/unattended/unattended.sh:1070-1072`) spells it `[A-Za-z][A-Za-z0-9-]*`,
and hygiene check 4 shares the driver's spelling.

**Defect.** `extract --discover --slug my-build` and the model's store fallback never attribute a
session to a dashed or single-letter slug. Such a run reads `not-local` for transcripts. The
journal-driven path is not affected.

**Fix.** Keep one slug constant in `runlog_lib`, spelled the way the driver spells it.

**Left-shift.** A parity arm that reads `check_slug_shape` from the driver's source, the way
`test_model_driver_sets` already reads the driver's sets. It compares the two grammars over a table of
dashed, single-letter and digit-first names.

### L5 — a range of unit ids is read as its first id (LOW)

**Where.** `tools/runlog/model.py:1051`. The reader is used for own commits (`:1183`), for commit units
(`:1263`) and to choose the build commit (`:1364`).

**Defect.** `\b[A-Z]+-<slug>-[0-9]+\b` reads `TOOL-dLoggedFlight-1..13` as unit 1 alone. The
memory-tree grammar expands the range spelling, and this repository's commit subjects use it.

**Reached by.** This build, as measured by this synthesis. Unit 1 has 10 own commits, and every other
unit has between 1 and 4. Eight commit subjects in the range use a range spelling, from `1dd6f3da` to
`8730066b`. All eight are credited to unit 1 and labelled unit 1 on the Timeline. The skew in choosing
the build commit is only hypothetical here: unit 1's build commit is correctly `03ae473c`.

**Fix.** Expand `<id>..<hi>` the way `gen_build_index.py` expands a Serves range, for own commits, for
commit units and for choosing the build commit.

**Left-shift.** An arm with a commit subject naming `X-xFixtureRun-1..2` that expects both units to
count it.

## The priming areas, checked against the code

- **H1: progress comes from the run's own commits.** This holds. `no-progress` and `merged` read own
  commits (`model.py:935-943`, `:1183-1193`), never the witness that `--close` leaves stale. Two defects
  concern how own commits are counted and bounded: L5 and M4. M5 is the matching defect on the window
  side.
- **H2: windows are half-open and bounded to the era.** This holds as a rule: `check_in_era`
  (`model.py:306-307`) and `check_in_window` (`:1239-1240`) are both half-open. Three defects sit at its
  edges. In M2, the half-open end excludes the move that proves push liveness. In M4, own commits are
  bounded by era when they need the window. In M5, the non-terminal end ignores the run's own work. L3
  concerns where the era starts after a root move.
- **H3: a push joins a run by what it pushed.** This holds as a key. The pushed-sha join exists
  (`model.py:1279-1284`), and it is what lets the landing push join at all. H2 is the worktree key
  joining too much once the run touches the primary tree. M4 is the pushed-sha key read against a
  `last_own` that moves. L1 is the defect on the producer's side.
- **H4: a START joins its start commit by a named key.** No confirmed finding. `derive_journal_join`
  (`model.py:546-570`) implements spec 8 S2 as written. The key is the first start commit of the slug at
  or after the START's END. The latest START wins a shared commit. A START that joins nothing starts no
  run. So the key is the slug plus that ordering, because the preflight's END carries no sha to name.
  That is the spec's own definition, not a departure from it.
- **The attribution rule.** M1: it has no time bound, and it cannot see later ENDs of other slugs.
- **The redaction table's coverage.** No confirmed finding. This synthesis probed the table with
  synthetic shapes, and the result is O1 below.
- **The renderer withholding forbidden shapes.** The schema's shape classes drew no confirmed finding.
  Two defects are about values rather than shapes. B1 is a withheld value you can recover from a
  rendered value derived from it. M6 is an unknown rendered as the value that reads clean.

Several components drew no confirmed finding:

- the producers' exit status, stdout and signal behaviour, and their process spawns on the hot path;
- the BUILD-METHOD `Decided:` trailer;
- the drift-audit signal `run_records_nonterminal_but_merged`;
- the text of the unattended Skill and protocol templates.

The model build at HEAD made 6 git calls, which is the constant spec 8 S12 counts. The caveat under
"Run integrity" applies to each of these zeros.

## The open questions, on the merits

1. **Does the idle-gap anomaly make records noisy on runs with no journal?** Yes, and the question is
   too narrow. The anomaly is noisy on runs that have journals and transcripts too, because it never
   reads a tool call (H1). On this build, all 23 idle-gap anomalies are false, and together they hide
   the times of the other six. On a git-only run, it measures missing sources rather than idle time. After H1's
   fix, the anomaly should fire only where a source that can see activity covers the window, and
   should report "could not be judged" otherwise. It is also the route by which B1 leaks, so the two
   share one fix.
2. **Are the gate and push key sets held only to golden lines?** Yes. That is a copy compared against
   another copy, the shape §12 warns about.
   - `PRODUCER_KEYS` (`tools/runlog/selftest.py:1766-1779`) is a hand-written copy.
   - `test_model_driver_sets` (`:2848-2886`) re-reads the driver's two writer arrays from
     `unattended.sh` and compares them in both directions. No arm reads the gate runner's
     `write_runlog_verdict` or the hook's calls to `write_push_line`.
   - `fixtures/golden-lines.txt` is a second copy. So the gates and pushes arms compare one copy with
     another.
   - The push DECISIONS are held to the hook's live source (`selftest.py:3497-3512`). The push KEYS
     are not.

   The consequence is silent. Rename `gate_run` in the hook and every arm still passes, while the
   model's pin (`model.py:1288-1289`, `:1305`) stops joining the landing bar. A missing key reads as
   absent, never as an error. It is not a defect today. This synthesis read the hook's writer calls
   (`.githooks/pre-push:146-152`, `:244`, `:257-259`, `:270-271`), and they name exactly the
   `PRODUCER_KEYS` push sets. This synthesis did not re-derive the gate runner's set. The recommended
   left-shift has two parts. Extend `test_model_driver_sets` to the other two writers, reading their
   sources the same way and comparing in both directions. Then add one arm asserting that every key
   the model reads belongs to its producer's set.
3. **Was spec text revised during the build left unreviewed?** Yes, and it shows. Ten specs carry a
   rev-5 or rev-6 line written by the build pass: units 1, 2, 3, 4, 6, 8, 9, 10, 11 and 13. Units 5, 7
   and 12 carry none. Two confirmed defects trace straight to spec 8's rev-5 line (lines 436-446). M2
   is its S7 dead proof combined with its S2 rule that the window ends at the terminal END. M5 is its
   "one second past its last event" rule, applied over only two sources. B1's README line accepting the
   leak is build-pass text of the same kind. So three of the fifteen distinct defects sit in prose no
   audit round read, which is the `fold-text-is-unreviewed-surface` rate the gotcha corpus predicts.
   Recommended: the round-2 review this verdict owes takes the rev-5 and rev-6 lines of those ten specs
   as subjects, pinned at their blobs, alongside the fix.

## Synthesis observations, outside the tally

These are not skeptic-verified, are not in the finding table, and are not counted in the verdict.

- **O1: the redaction table misses two shapes that sit next to a row it already has.** This synthesis
  ran `scan_secrets` and `render_redacted` over synthetic strings shaped like credentials, none of
  them real.
  - Redacted: an `AKIA` key id, an `Authorization: Bearer` value, `ghp_`, `sk-ant-`, URL userinfo,
    `xoxb-`, an Azure `sig=`, full PEM blocks, a JSON `private_key` and `AWS_SECRET_ACCESS_KEY=`.
  - Not redacted: an AWS STS `ASIA` key id, a `Bearer` value under a header other than Authorization,
    SendGrid `SG.`, DigitalOcean `dop_v1_`, Shopify `shpat_`, Stripe `rk_live_` and Twilio `SK`.

  The README says a class with no row is not redacted (`tools/runlog/README.md:326-328`), so all of
  these are inside the documented residue. Two are worth a row anyway, because their prefix sits next
  to one the table already covers: `ASIA` next to `AKIA`, and a bare `Bearer` outside the
  Authorization header.
- **O2: the landing reconcile owes a version renumber.** This clone's `origin/main` is now `6074d521`,
  37 commits past the `9ce37fcc` this review is pinned on. Those commits include the dPolishedVitrine
  merge `0c312a04`. Both `36d531b9` and `6074d521` read `KIT_UNATTENDED_VERSION=1.21`, and neither
  side's 1.21 contains the other side's changes. Since `9ce37fcc`, 27 files have changed on both sides,
  among them `tools/unattended/unattended.sh`, `check-unattended.sh`, `SKILL.template.md`,
  `PROTOCOL.template.md` and `tools/gate-legs.json`. That merge's fold will be unreviewed surface too,
  so the round-2 review is best pinned after it.

## What this synthesis re-derived

Everything below was measured in this worktree at `36d531b9`, on a clean tree:

- Every file:line in the table, read at that commit.
- The model, from `python tools/runlog/runlog.py model dLoggedFlight --json`:
  - run 1 of 1, with the window running from 2026-09-13T11:05:47Z to 2026-09-14T05:34:12Z, opened by
    git and closed by last-activity;
  - driver `partial` with 64 lines, gates and pushes `absent` (this clone's common dir has no
    `pushes.log`), transcripts `present`;
  - 29 anomalies: 23 `idle-gap` and 6 `destructive-git`;
  - 5480 in-window tool calls, 4303 of them inside idle gaps, and no gap free of calls;
  - 42 own commits, 10 of them credited to unit 1, and three own commits after the window end;
  - 6 git calls.
- Owner turns by position: launch 1, pre-run 1, in-window 2, post-close 0. One idle gap's end falls on
  an in-window owner turn. Which gap it is stays out of this record, for B1's reason.
- The record, rendered to stdout and not written: 19886 bytes, reading
  `anomalies: 29 · shown 0 · aggregated yes`. At this commit, no rendered idle row falls on an owner
  turn.
- Attribution across two renders minutes apart: 2968 of 7219 calls, then 2971 of 7222.
- The gates journal: a full bar with self-tests RED at `9e9109da` (111 legs ran, 5 failed), then GREEN
  at `36d531b9` (111 ran, 0 failed, 0 skipped, 0 held).
- The eight range-spelled subjects (L5), the count of rev-5 and rev-6 lines (question 3), O1's probe
  and O2's refs.

Some results were taken from verification and not measured again here:

- the scratch-repository `insteadOf` reproduction (L1);
- the landed-fixture reproductions (H2, M2);
- the untrapped-TERM `rc=0 exit=unclean` reproduction (M3);
- the render with an empty state directory (M6);
- the conf reproduction (M7).

## What the fold owes, in order

1. **B1 and H1 together**, because both rewrite `model.py:1344`. The gap sequence gains tool-call times
   and loses owner turns, and the render-time refusal and the arms under each finding come with it.
   This must land before the close's placement-2 render, because that render produces the first
   committed record.
2. **H2 and M5 together**, because M5's window end reads the worktree key that H2 narrows.
3. **M1, M4 and M5's timeline bound as one window discipline.** Bound every derived set in
   `build_run_model` by `[start, end)` through one helper, and have every model arm assert the model
   invariant from M5's left-shift.
4. **M2, M3, M6 and M7, then the lows.**
5. **Round 2 re-reviews the FIX, per BUILD-METHOD.** Its subjects are the fold's diff and the rev-5 and
   rev-6 lines named under question 3. Pin it after the O2 reconcile if that reconcile lands first.

Each confirmed finding gets either a regression arm or a `memory/gotchas/` class, as the Definition of
Done requires. The left-shift line under each finding names the one proposed.

## State

- Branch `branch/unattended-build-transparency-ea83a5`, HEAD `36d531b9`, clean.
- The pinned run base is `a4007553`, the reconcile merge is `9ed23769`, and the reviewed range is
  `9ce37fcc...36d531b9`. `origin/main` is now at `6074d521`.
- Gates: the full bar with self-tests was GREEN at `36d531b9`, 111 legs, as read from the gates
  journal. This synthesis did not run the bar again.
- Review shape: 30 raw, 18 confirmed, 12 refuted, 0 unverified, precision 0.60, 15 distinct defects.
