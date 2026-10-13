# TOOL-aOrientedCast-23 — one stated answer on which declared size ceilings a run may raise, held in the limits file and pointed at by M3 and the size gate

**Status:** CLOSED · rev-3 · 2026-10-13 · node a · Tier-2 · base 646d4a73 · streams tooling · order 25

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md](../build/2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 TOOL-aOrientedCast-22 |
| [2026-10-13-build-TOOL-aOrientedCast-23-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aOrientedCast-23-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-aOrientedCast-1-7-owner-addendum.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-7-owner-addendum.md) | research | TOOL-aOrientedCast-25 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/template-size-limits.txt` says only a person writes it, the size gate's over-budget message
calls any raise an owner decision, and M3 makes a change to a governance carrier an owner turn. Read
together, they made the `AGENTS.md` raise that `PLAY-aOrientedCast-3` needed look like a fork no
delegated resolver could take, so the run asked the owner. The owner ruled on 2026-10-13 that the
raise "was perfectly resolvable on your own". This unit writes that ruling as one stated rule in the
limits file's header, saying which rows a run may raise and on what terms, and makes M3 and the size
gate point at it rather than answer the question a second time.

## 2. Scope (IN)

- **S1** — The header of `tools/template-size-limits.txt` (`:10-13`) states who writes the file and
  gains the paragraph "WHEN A RUN MAY RAISE A ROW" of §4 "The rule", the one place its terms live.
  Observed by AC1 and AC4.
- **S2** — M3's "What is delegated" paragraph, in `tools/memory-tree/BUILD-METHOD.template.md` and its
  render `memory/guides/BUILD-METHOD.md`, gains the one sentence of §4 "The pointers": a declared
  ceiling is the owner's to move unless the file declaring it states otherwise, and a raise on its
  stated terms changes no governance carrier. Observed by AC2, AC4 and AC7.
- **S3** — The over-budget message of `tools/check-template-size.sh` (`:144-148`) stops calling every
  raise the owner's and points at the limits file's header. Observed by AC3 and AC4.
- **S4** — `memory/DECISIONS.md` holds this unit's row at the end of its `## TOOL — tooling` group,
  written by the main loop before the build: a pass may not declare that shared record, so the
  pass observes the row and writes none (§4 "The decision row"). Observed by AC5.
- **S5** — The memory-tree kit moves from 2.147 to 2.148 with every carrier
  `tools/check-kit-versions.sh` asserts. Observed by AC6.
- **S6** — The same commit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`, whose
  `watch:` list holds the build method, the size gate and the hygiene engine. Observed by AC8.
- **S7** — A second build pass changes term 4's one line in `tools/template-size-limits.txt`
  (`:23` at `dfc13bc1a`, where the first pass wrote "the same commit adds that unit's row to
  memory/DECISIONS.md") to §4 "The rule"'s wording, and nothing else in the file. The file is in no
  kit and on no `watch:` list, so the pass owes no version move and no re-stamp. Observed by AC9.

## 3. Non-goals (OUT)

- Moving any row of the limits file. The rule governs the next raise; this unit raises nothing.
- Other declared ceilings: `tools/line-length-limits.txt`, the per-class caps in
  `.memory-tree.conf`, and the high-water record. Each stays as it reads today; a follow-up may give
  each a header rule of its own.
- A gate that checks a raise against the terms, for example that a raised row carries its argued
  movement and a decision row. The terms are stated here and graded by review; the follow-up is a
  size-gate arm.
- Any edit to the unattended protocol. Its §11 parks a discovery that needs a governance-carrier
  change and names no ceiling, so it reads M3 and needs no word of its own.
- Defining "governance carrier" in general. M3 uses the term without a definition, and this unit
  settles only the ceilings question the owner ruled on.

### Edges

none

## 4. Design

Line numbers were read at `4d749701a` on 2026-10-13, the run branch's HEAD after this unit's split.

### Evidence

- The limits file opens on its grammar and its rationale, then "WHO WRITES THIS FILE: a person,
  deliberately" (`tools/template-size-limits.txt:10-13`), whose point is that `--bump` records a
  measurement and never moves a ceiling. Every movement since is argued above its row in capitals:
  `RAISED from 32768 on owner order, 2026-08-16` for the template (`:28-32`), `LOWERED to 16384` for
  `AGENTS.md` (`:61-64`), two raises of the unattended protocol by units (`:120-122`).
- The build method's row reserves its own next movement: "Spent, it is the owner's again" (`:98-105`),
  and M3 keeps "M1's own budget" outside the delegation (`tools/memory-tree/BUILD-METHOD.template.md:80-81`).
- The unattended protocol's row is pinned "deliberately no headroom" (`:109-114`).
- The size gate's message: "Raising the limit is an OWNER decision recorded in memory/DECISIONS.md,
  never a fix for the edit that hit it", shared by every subject the gate measures
  (`tools/check-template-size.sh:144-148`).
- M3's veto 2 discards an option needing "a change to a governance carrier"
  (`tools/memory-tree/BUILD-METHOD.template.md:89`), and a `may:` grant lifts it for what it names
  (`:82`). No file defines a governance carrier.
- The limits file ships to no adopter: the deployer's registry exempts it (`tools/govkit/registry.toml:275-277`),
  and its own build-method row records dropping a template sentence that named a checker adopters do
  not receive (`tools/template-size-limits.txt:87-93`). The method template IS shipped, so it may not
  name the limits file.

### The rule

The paragraph `:10-13` keeps its rationale and changes its first sentence to
`WHO WRITES THIS FILE: a person or a run, deliberately, and never a measurement.` Directly below it,
after a `#` line, the rule:

```text
# WHEN A RUN MAY RAISE A ROW. Every row here is the owner's to move, except that a run may RAISE a
# measured-file row, in the commit of a unit of a build the owner mandated, when all four hold:
#   1. that unit's own change takes the row's subject past the row, measured CR-stripped;
#   2. the row's comment block does not reserve its next movement to the owner, and the new value
#      keeps to any rule that block states, such as no headroom;
#   3. the movement is argued in place above the row, in the shape the movements below take:
#      RAISED <old> -> <new>, the date, the unit, the measured figure and why the new value;
#   4. the run records that unit's row in memory/DECISIONS.md before or with the raise.
# A class row, a lowering, a new row and a removal stay the owner's. This paragraph is the one
# statement of these terms: the build method's M3 and check-template-size.sh's over-budget message
# point here rather than restate them. Ruled by the owner on 2026-10-13, of the AGENTS.md raise this
# file records below: it "was perfectly resolvable on your own" (memory/DECISIONS.md,
# TOOL-aOrientedCast-23).
```

Read against the rows: the `AGENTS.md` raise of `PLAY-aOrientedCast-3` meets all four terms; the
build method's row stays the owner's under term 2, which is what M3's "M1's own budget included"
already says; the unattended protocol's row may be raised by a run to the measured figure and no
further, under term 2's second half.

### The pointers

M3's "What is delegated", after the `may:` sentence (`BUILD-METHOD.template.md:82`), gains one line,
identical in the template and the render:

```text
A declared ceiling is the owner's to move unless the file declaring it states which rows a run may raise and on what terms; a raise on those terms changes no governance carrier.
```

It names no file, because the template ships to adopters who hold no limits file; gov's limits file
is the file that states such terms. The render follows the template byte for byte at that line, since
the sentence carries no token. The method stays inside its budget: it measures 29144 bytes and 361
lines against `≤30720` and `≤400` (`memory/guides/BUILD-METHOD.md:8`), and the line adds 178 bytes
with its newline, and one line.

The size gate's message keeps its first two lines and replaces the last two with:

```text
  Raising the limit is the owner's decision, or a run's on the terms the header of $LIMITS
  states; either way it is argued beside the row and recorded in memory/DECISIONS.md, never a fix
  for the edit that hit it. This message is shared with the kickoff engine at its own limit.
```

`$LIMITS` is the script's own resolved path to the limits file (`:63`), so the message names the
file the gate read, whatever the prefix.

So one place holds the terms, and two point at it: M3 defers to the declaring file, the gate names
it, and neither restates a term. AC4 observes that.

### The decision row

The main loop appends this row before the build, after the `## TOOL — tooling` group's last row and
before `## DEPL — deployer` (`memory/DECISIONS.md:138`). A pass may not declare that shared record
in its write set, so the builder writes no row: it observes this one by AC5 and leaves the file
alone. The row is 239 characters, under the 300 that `ENTRY_CAP_CHARS` allows an index entry:

```text
- TOOL-aOrientedCast-23 · a run may RAISE a measured-file row of the size limits on the four terms that file's header states; M3 and the size gate point there (owner, 2026-10-13: the AGENTS.md raise "was perfectly resolvable on your own").
```

### Kit version

`TOOL-aOrientedCast-19`, building now, moves the memory-tree kit from 2.146 to 2.147. This unit edits
the kit's method template after it, so it moves the kit again, to 2.148, as the last unit of the set
to touch `tools/memory-tree/`. The carriers `tools/check-kit-versions.sh` asserts
(`:140`, `:245-280`): `KIT_MEMORY_TREE_VERSION` with its same-line marker
(`tools/memory-tree/check-memory-hygiene.sh:64`), and the `gov:kit memory-tree@` marker of every
tracked `tools/memory-tree/*.template.md`. Their rendered copies, `memory/HYGIENE.md`,
`memory/TEMPLATE-SPEC.md`, `memory/guides/ANNOTATION-STYLE.md` and `memory/guides/BUILD-METHOD.md`,
carry the same marker, which the kit/dogfood parity leg compares with each template.

### Inventory

Minted: the header paragraph's title `WHEN A RUN MAY RAISE A ROW`, M3's ceiling sentence, and the
version 2.148. No function, file, conf key or flag is minted, so no `.lexicon.conf` cell grades a name.

### Files touched (estimate)

`tools/template-size-limits.txt`
`tools/check-template-size.sh`
`tools/memory-tree/BUILD-METHOD.template.md`
`tools/memory-tree/HYGIENE.template.md`
`tools/memory-tree/SPEC-TEMPLATE.template.md`
`tools/memory-tree/ANNOTATION-STYLE.template.md`
`tools/memory-tree/check-memory-hygiene.sh`
`memory/guides/BUILD-METHOD.md`
`memory/HYGIENE.md`
`memory/TEMPLATE-SPEC.md`
`memory/guides/ANNOTATION-STYLE.md`
`memory/guides/SESSION-KICKOFF.md`

### Rollout

1. Built after `TOOL-aOrientedCast-19` lands, whose memory-tree move this unit's follows; the builder
   re-reads the carriers' version first and moves it by one step from what it finds.
2. Edit the limits header, the size gate's message and M3 in the template and the render, as above.
3. Move the version in every carrier; `python tools/govkit/govkit.py selfcheck --fix` writes the
   template markers from the constant, and where the role gate refuses it to the builder, the
   builder edits every file `git grep -l "gov:kit memory-tree@2.147"` lists.
4. Confirm the decision row the main loop wrote before the build is in place, by AC5; write none.
5. Re-stamp `last-audit` in `memory/guides/SESSION-KICKOFF.md` at staging, and derive check 9's count
   as `PLAY-aOrientedCast-2` §4 "Rollout" step 7 states, advancing `last-body-change` at 9 or more.
6. Commit once, with the unit id in the subject.

Adopters receive M3's sentence with the kit at `govkit update`; the limits file and the gate are
gov's alone. Rollback is a revert of the one commit.

### Alternatives rejected

- M3 holding the terms and the header pointing at M3: §8 F2.
- Stating the terms in all three places: three answers to one question, the drift [one-fact] names.
- Defining "governance carrier" in M3 and listing the limits file outside it: it widens the change to
  every carrier the term reaches, which the owner did not rule on.

## 5. Production-readiness checklist

- security — no code path changes; a run gains authority to raise a size ceiling under four stated
  terms, each visible in the diff and in the decision index, and loses none of the owner's other
  turns.
- perf / scale — M3 grows by one line, 178 bytes, inside the method's budget, so M7's re-read cost
  barely moves.
- error / empty / loading states — N/A: prose and one message string.
- observability — every raise a run takes leaves an argued RAISED paragraph and a decision row, by
  terms 3 and 4.
- risks — the terms are graded by review, not by a gate (§3), so a raise that skips term 4 lands
  green; the size-gate arm is the named follow-up. The owner ratified the change to M3 (§8 F1).
- testing — the greps of §6; the size, parity, version, method-carrier, manifest and hygiene legs at
  the close. No new arm.
- migration — none; rollback is a revert.
- user docs — N/A: the readers are runs and maintainers, and both texts are where they read.

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag. Each reads a file on the unit's
commit.

- **AC1** — When `grep -n "WHO WRITES THIS FILE: a person or a run\|WHEN A RUN MAY RAISE A ROW\|perfectly resolvable on your own" tools/template-size-limits.txt`
  runs, it prints three lines in that order, all above the first row, `coding-governance-agents.template.md`.
  Red when: the terms are absent, sit below a row, or the owner's ruling is not quoted.
- **AC2** — When `grep -c "A declared ceiling is the owner's to move unless the file declaring it states" tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md`
  runs, it prints 1 for each file, the line sitting in M3's "What is delegated" paragraph; and
  `grep -c "template-size-limits" tools/memory-tree/BUILD-METHOD.template.md` prints 0.
  Red when: M3 lacks the pointer, template and render disagree, or the shipped template names a file
  adopters do not receive.
- **AC3** — When `grep -c "OWNER decision" tools/check-template-size.sh` runs it prints 0, and
  `grep -c "on the terms the header of" tools/check-template-size.sh` prints 1; `bash -n tools/check-template-size.sh`
  exits 0.
  Red when: the gate still calls every raise the owner's, or the edit breaks the script's syntax.
- **AC4** — When `git grep -l "reserve its next movement to the owner" -- tools memory/guides` runs, it
  prints `tools/template-size-limits.txt` alone.
  Red when: a second carrier restates a term, which makes two answers to one question.
- **AC5** — When `grep -c "^- TOOL-aOrientedCast-23 · " memory/DECISIONS.md` runs it prints 1;
  `grep -n "^## \|^- TOOL-aOrientedCast-23 · " memory/DECISIONS.md` shows the row between
  `## TOOL — tooling` and `## DEPL — deployer`; and
  `grep "^- TOOL-aOrientedCast-23 · " memory/DECISIONS.md | awk '{ print length($0) }'` prints at
  most 300; and on the unit's commit `git diff --name-only HEAD~1 HEAD -- memory/DECISIONS.md`
  prints nothing.
  Red when: the rule has no decision row, the row sits outside its group or twice, it passes the
  index's entry cap, or the unit's own commit writes the record the main loop owns.
- **AC6** — When `grep -c "^KIT_MEMORY_TREE_VERSION=2.148" tools/memory-tree/check-memory-hygiene.sh`
  prints 1 and `git grep -l "gov:kit memory-tree@2.147" -- tools memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides`
  prints nothing, every carrier moved.
  Red when: the constant or one carrier keeps 2.147.
  figure: PINNED on the assumption that `TOOL-aOrientedCast-19` lands 2.147 first; any other move
  landing before this unit shifts the expected value by the same step.
- **AC7** — When `tr -d '\r' < memory/guides/BUILD-METHOD.md | wc -c` and
  `awk 'END{print NR}' memory/guides/BUILD-METHOD.md` run, they print at most 30720 and at most 400.
  Red when: the pointer pushes the method past its own budget, which is the owner's to move.
  figure: DERIVED at observation; 29144 and 361 are PINNED at `4d749701a`.
- **AC8** — When `git show` reads `memory/guides/SESSION-KICKOFF.md` at `HEAD` and `HEAD~1`, the two
  `last-audit:` lines differ and the first ends with the sha `git rev-parse HEAD~1` prints.
  Red when: the commit stages a watched file with no new stamp.

- **AC9** — When `grep -c "^#   4. the run records that unit's row in memory/DECISIONS.md before or with the raise.$" tools/template-size-limits.txt`
  runs it prints 1, `grep -c "the same commit adds that unit's row" tools/template-size-limits.txt`
  prints 0, and on the second pass's commit `git diff --numstat HEAD~1 HEAD -- tools/template-size-limits.txt`
  prints one line changed each way.
  Red when: term 4 keeps the first pass's wording, or the pass moves another line of the file.

## 7. Gates

`build-method size` · `template size <=48KiB` · `template size gate selftest` · `kit/dogfood doc parity` · `method carriers (every pointer declared)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `memory hygiene` · `memory-hygiene self-test` · `spec tokens (a spec's own names resolve)`

This unit adds no gate arm. The main loop runs the legs once, at the close; no pass runs one.

## 8. Open questions

- **F1 — May this unit change M3 at all, or is the change itself the owner's?**
  M3 is a governance carrier by any reading, its veto 2 makes a change to one an owner turn, and the
  unattended protocol's §11 parks a discovery that needs one. The owner's ruling covers one raise;
  this unit turns it into a standing rule every later run may use.
  (a) The owner ratifies §4 "The rule" and "The pointers" as written before the unit is built, and
  the main loop records that ruling here and in the run record.
  (b) Build under the ruling on the `AGENTS.md` raise alone.
  (c) Write only the limits header, which states its own terms, and leave M3 and the gate unchanged.
  (b) widens a run's authority on the strength of a ruling about one instance, the act M3 forbids a
  run to take for itself. (c) leaves M3 and the gate answering the question the other way, which
  is the defect this unit exists to remove.
  Recommendation: (a). This fork is the owner's; the builder takes no option before the ruling.
  RESOLVED (owner, 2026-10-13): (a), §4 "The rule" and "The pointers" ratified as written, with no
  cap on a raise, chosen over a capped raise and over retiring the unit.
- **F2 — Which text holds the terms, and which point?**
  (a) The limits file's header holds them; M3 and the gate point at it. (b) M3 holds them; the header
  and the gate point at M3. (c) Each states them.
  (b) puts gov's file-specific terms into a document every adopter renders, where no limits file
  exists, and M3 would have to name per-row reservations it cannot see. (c) is three copies.
  (a) keeps the terms beside the rows they govern, the place the file's own rationale says a
  movement is argued.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The rule" and "The pointers" state it.

- **F3 — Term 4 has the raising unit's own commit add its `memory/DECISIONS.md` row, and a pass may
  not declare that shared record. Which gives?**
  (a) Reword term 4 so the run records the row before or with the raise; (b) keep the wording and let
  a raising unit declare the record.
  RESOLVED (owner, 2026-10-13): (a), verbatim "Reword term 4 so the run records the row "before or
  with the raise"", recorded in the build's fourth owner addendum; §4 "The rule", S7 and AC9 carry it.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.
- rev-2 · 2026-10-13 · §8 F1 · S4 · AC5 · §4 · §5 · the owner ratified §4 "The rule" and "The
  pointers" as written, with no cap, over a capped raise and over retiring the unit, and F1 is
  marked. The decision row moves to the main loop, written before the build because a pass may not
  declare that shared record: S4, §4 "The decision row", rollout step 4 and AC5 have the builder
  observe it and write none, and files touched drops `memory/DECISIONS.md`.
- rev-3 · 2026-10-13 · §4 · S7 · AC9 · §8 F3 · the owner reworded term 4: the run records the
  raising unit's row before or with the raise. §4 "The rule" carries it, S7 and AC9 add the one-line
  change a second pass makes to the file the first pass wrote, and F3 records the ruling.

## 10. Reuse audit

No existing seam fits, and the evidence is that this unit writes no code: it edits three texts that
already exist and adds one row to an index, and the seam is those texts themselves.
`python tools/memory-recall/query.py "may a run raise a declared size ceiling without the owner"`
with the terms below surfaced this build's rescope row, `PLAY-aOrientedCast-2` §8 F2, which read the
limits file and the gate as making every raise the owner's, and three asks: `TOOL-aHoistedPass-29`,
that nothing catches a later raise of a byte cap, which is this unit's named follow-up;
`TOOL-aScouredKit-23`, two carriers with no declared ceiling at all, outside this unit; and
`TOOL-aLevelledCopy-6`, a runbook edit parked under veto 2, the reading §8 F1 applies to M3 itself.
Each was read against source; the build method's own reservation (`tools/template-size-limits.txt:98-105`)
is kept, under term 2. `python tools/codebase-map/reuse_lookup.py` was not run: it ranks code
symbols, and nothing here is one.

Recall terms used: `size ceiling raise owner decision governance carrier veto limits header M3 delegated run DECISIONS`
