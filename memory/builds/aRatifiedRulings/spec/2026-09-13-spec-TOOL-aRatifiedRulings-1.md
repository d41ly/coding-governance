# TOOL-aRatifiedRulings-1 — a converged subject's later blocker is disposed, never re-rounded

**Status:** CLOSED · rev-4 · 2026-09-13 · node a · Tier-2 · base 16da4c6a · streams tooling · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-aRatifiedRulings-1-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-aRatifiedRulings-1-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-aRatifiedRulings-1-0-run-mandate.md](../prompts/2026-09-13-prompt-TOOL-aRatifiedRulings-1-0-run-mandate.md) | journal | — |
| [2026-09-13-prompt-TOOL-aRatifiedRulings-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-aRatifiedRulings-1-1-build-brief.md) | journal | — |
| [2026-09-13-review-TOOL-aRatifiedRulings-1-round1.md](../reviews/2026-09-13-review-TOOL-aRatifiedRulings-1-round1.md) | spec-audit | TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 TOOL-aRatifiedRulings-4 |
| [2026-09-13-review-TOOL-aRatifiedRulings-1-round2.md](../reviews/2026-09-13-review-TOOL-aRatifiedRulings-1-round2.md) | spec-audit | TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 TOOL-aRatifiedRulings-4 |
| [2026-09-14-review-TOOL-aRatifiedRulings-1-diff-round1.md](../reviews/2026-09-14-review-TOOL-aRatifiedRulings-1-diff-round1.md) | diff-review | TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 TOOL-aRatifiedRulings-4 |

<!-- /gen:spec-records -->

## 1. Goal

Owner ruling `TOOL-aLeakedHandle-6` in `memory/DECISIONS.md`: a blocker found on a subject whose
review loop already recorded `CONVERGED` is DISPOSED under M4 fold/promote and never re-rounded, and
the loop does not re-arm on a rev bump. The ruling owes two edits and this unit makes both: M4 of
the build method says it, and check 37 of `tools/unattended/unattended.sh`, which already refuses
the round, names that route in its refusal so the next run reads it there instead of parking the
same question again. The park that motivated it is the `2026-09-10T08:43:58Z decision` entry in
`memory/builds/aLeakedHandle/RUN.md`; this spec points at the ruling and does not restate it.

## 2. Scope (IN)

- **S1** — M4 of `tools/memory-tree/BUILD-METHOD.template.md` gains one paragraph after the
  disposition paragraph: `CONVERGED` is terminal for its subject, rev bumps included; a blocker
  confirmed on it afterwards takes the exit's own disposition, FOLD or PROMOTE, and never another
  round; `--review` refuses the round and names this route. The render
  `memory/guides/BUILD-METHOD.md` is re-made from the template by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, never hand-edited. Observed by AC1
  and AC2.
- **S2** — M4's first paragraph, which today makes any rev-moved spec unreviewed, gains the
  qualifier "by anything but that review's own fold", so the method no longer instructs a round the
  driver refuses. Same two files, same render step. Observed by AC1 and AC2.
- **S3** — Check 37 branch 10 at `tools/unattended/unattended.sh:4096` keeps its predicate and
  extends its message: after "would rewrite that history" it says that a blocker confirmed on the
  subject now is DISPOSED under the build method's M4, fold or promote, and never re-rounded. No
  other branch, predicate or row grammar moves. Observed by AC3 and AC4.
- **S4** — `tools/unattended/unattended.test.sh`: the two existing arms that quote branch 10's text
  move to the new signature, and one new arm drives the ruling's own sequence — round 1
  `CLEAN WITH FIXES` at zero blockers, so the subject records `CONVERGED`, then a `BLOCKED` round at
  one blocker — and asserts the refusal text and that the run-state file still holds exactly one
  review row for that subject. Observed by AC3, AC4 and AC5.
- **S5** — The obligations the method edit incurs, in the same commit as the edit that incurs them:
  the kickoff manifest `last-audit` re-stamp, because `memory/guides/BUILD-METHOD.md` is on its
  watch list; the memory-tree kit version, 2.69 to 2.70, across every carrier and re-rendered. The
  unattended kit version does NOT move in this pass: `TOOL-aRatifiedRulings-2` §8 F1, RESOLVED,
  assigns the single 1.19 to 1.20 bump to the closing pass, after every unit that edits the
  unattended kit has landed, and this unit leaves `KIT_UNATTENDED_VERSION` at 1.19 in all four
  scripts. Observed by AC6 and AC7.

## 3. Non-goals (OUT)

- **The loop does not re-arm on a rev bump.** That was option 1 of the park and the ruling refused
  it. `review_state`, `review_counts`, `review_last_reason` and the terminal-token grep at
  `unattended.sh:4095` are untouched; a round on a subject carrying `CONVERGED`, `NON-CONVERGENT`
  or `CEILING` is refused exactly as before.
- **No new `--review` row for the disposed blocker.** The ruling accepts that cost and section 5
  states it. This unit adds no verb, no row kind and no field.
- **The convergence key stays `--subject` alone.** Keying on (kind, subject) is
  `TOOL-dHonouredPark-8` and a cross-run loop is `TOOL-dCarriedReceipt-1`; both stay open.
- **M1's budget does not move.** M3 puts it outside the mandate. The sentence is sized to the
  measured headroom in section 4, and if it did not fit the trade would come out of M4's own
  prose, not out of the ceiling.
- **No backlog row is edited.** `memory/backlog` is a `SHARED_RECORDS` member in `.unattended.conf`,
  so a dispatched pass may not declare it. The row this ruling answers is named as an edge below.
- **The gotcha `fold-text-is-unreviewed-surface` is not amended.** The park notes it does not say the
  loop can close before the fold text exists; the ruling does not owe that clause, and the class
  record is a `memory/gotchas/` edit for the next run that hits it.
- **No new gate leg, no pin row, no floor change.** The suite's shrink-only floors are minimums and
  the added assertions only raise the executed count above them.

### Edges

- **hands-off** external — the `KIT_UNATTENDED_VERSION` bump, 1.19 to 1.20, across every carrier
  `git grep -l 'gov:kit unattended@1\.19' -- tools/unattended .claude/skills/unattended memory/guides`
  returns, run before the bump at the value being left. At base `16da4c6a` that is FIFTEEN files,
  DERIVED by that probe on 2026-09-13: the four `.sh` constants, reached through their same-line
  markers; the five `tools/unattended/*.template.md`; the five renders `adopt-unattended.sh --check`
  re-makes and diffs, `.claude/skills/unattended/SKILL.md`, the two `memory/guides/UNATTENDED-*.md`
  copies, `memory/guides/PLAYBOOK-TEMPLATE.md` and `tools/unattended/playbook.fixture.md`; and
  `tools/unattended/README.md:1`, which `tools/check-kit-versions.sh` pairs with nothing
  (`DEPL-aHoistedPass-10`, OPEN). `b8e8d6dc`, the commit `TOOL-dMuffledSentinel-3` names, is the
  commit shape: it moved exactly those fifteen. The closing pass owns the bump, once for the kit,
  per `TOOL-aRatifiedRulings-2` §8 F1, and declares every file the probe returns; a pass that
  declares only what `check-kit-versions.sh` pairs plus the renders writes `README.md:1`
  undeclared, or leaves it at 1.19 with no gate to say so. No epoch gate observes that bump's
  placement: `check-verdict-epoch.sh` is hardcoded to the memory-tree engine, which
  `tools/check-kit-versions.sh:49` says in its own comment, so the closing pass's declaration is the
  only record of which commit moved the constant relative to the two commits that moved the bytes.
- **hands-off** external — the status flip of backlog row `TOOL-dCarriedReceipt-2`, which records
  this exact collision between the terminal rule and M4's rev-moved clause. It is owed by whichever
  commit next opens the shared records; until then that row reads OPEN against a ruling that closed
  it.
- **consumes-from** external — the signature rule in `tools/memory-tree/check-arms.py`: a branch is
  armed only by a test line containing its longest literal run. That rule is what makes the message
  and its arms one observable pair on every bar, and if it changed to a shorter match the staged
  break in AC3 would stop being red.
- **consumes-from** external — the render direction of `tools/memory-tree/kit-dogfood-parity.test.sh`:
  template to live, never the reverse. A future template that stops shipping the method would leave
  the render with no source and this unit's S1 with no file to edit.

## 4. Design

### Where each half lives, and which file is the source

The method is a RENDER. `tools/memory-tree/BUILD-METHOD.template.md` is the authored source and
`memory/guides/BUILD-METHOD.md` is this repo's dogfood render of it, produced by the `render_doc`
block in `tools/memory-tree/kit-dogfood-parity.test.sh` substituting `{{KIT_DIR}}` and
`{{TOOL_ROOT}}`. The `kit/dogfood doc parity` leg diffs the live copy against a fresh render of the
template and reds on any difference, and its printed fix is `--render`, which OVERWRITES the live
copy. So an edit made only to the render reds the bar and the remedy it prints erases the edit. This
was observed on 2026-09-13 in a scratch copy of base `16da4c6a`: the render-only edit produced
`kit-parity: DRIFT — memory/guides/BUILD-METHOD.md does not match`, and the same edit made to the
template then `--render` produced a live copy byte-identical to the hand edit and a green leg. Edit
the template, render, commit both.

### The M4 bytes

Measured on 2026-09-13 at base `16da4c6a` with `stat -c%s` and `wc -l`:

| File | Bytes | Lines |
|---|---|---|
| `memory/guides/BUILD-METHOD.md` (the gated render) | 26439 | 336 |
| `tools/memory-tree/BUILD-METHOD.template.md` (the source) | 26464 | 336 |

M1 declares `≤27648 bytes, ≤350 lines` and says the byte half binds first. Headroom before this
unit: 1209 bytes and 14 lines. The `build-method size` leg reads only the byte half, against the
`memory/guides/BUILD-METHOD.md` row of `tools/template-size-limits.txt`, and reds through its
check 6 if M1's own `**Budget:` line ever disagrees with that row; the line half is read by nobody,
which `tools/template-size-limits.txt` says in its own comment. Both figures here are PINNED at the
date above; AC2 re-derives them.

The two edits cost 304 bytes and 4 lines: the paragraph quoted below is 258 bytes with the blank
line that separates it from M5, and the qualifier below it adds 46, one comma out and one em-dash
pair in. Re-measured on 2026-09-13 by staging both edits into a copy of the template at base
`16da4c6a` with `stat -c%s` and `wc -l`; the render costs the same, because neither edit carries a
`{{KIT_DIR}}` or `{{TOOL_ROOT}}` token and a wrap moves a space to a newline at no byte cost. The
render therefore measures 26743 bytes and 340 lines, leaving 905 bytes and 10 lines under M1, and
198 bytes under the 26941 high-water in `tools/template-size-highwater.txt`. So no `--bump` is owed
and the leg prints no `TEMPLATE-SIZE WARN` line. The figures are PINNED at that date and AC2
derives the real ones.

The added paragraph, placed directly after the paragraph that opens `**A BLOCKED verdict has a
disposition**`, in the template's own wrap style:

```
**CONVERGED is terminal for its subject, rev bumps included**: a blocker confirmed on it afterwards — in the
fold text, say — takes the exit's own disposition, FOLD or PROMOTE, and never another round; `--review`
refuses the round and names this route.
```

The qualifier, in M4's first paragraph, replacing `A spec whose rev moved since its last review, or
that you authored this run, is unreviewed.`:

```
A spec whose rev moved since its last review — by anything but that review's own fold — or that you
authored this run, is unreviewed.
```

Why the qualifier is part of the ruling and not a widening. `TOOL-dCarriedReceipt-2` names the
collision exactly: the terminal rule in the driver against M4's rev-moved clause, which meet on every
spec a round both clears and edits in its fold. The ruling's "no re-arm on a rev bump" resolves that
collision in the driver's favour, and the rev-moved clause is the method's spelling of the re-arm.
Left as written, M4 would instruct a round the driver refuses, which is the `a directive names a
route that does not run` class `tools/template-size-limits.txt` already records for this file. The
qualifier is minimal: a rev moved by anything OTHER than the loop's own fold — a THIN fill, an
AMEND — still makes the spec unreviewed, in this run or a later one, which is a new loop under a
different run-state file and never a round on a closed one.

Why the paragraph carries no decision id. The template ships to adopters, where
`TOOL-aLeakedHandle-6` names nothing, and the template carries no decision id today; M1 records its
own owner calls by date for the same reason. Provenance lives in the decision log and in this spec.

### The check 37 message

`verb_review` in `tools/unattended/unattended.sh` reaches branch 10 after the row-grammar guards and
before the state gate: it greps the run-state file's `review` rows for the subject with `-F`, reads
the reason field, and refuses on any of the three terminal tokens. The predicate is not touched. The
message becomes:

```
fail 37 "this subject already carries a terminal review round, so the loop ended for it and another round would rewrite that history; a blocker confirmed on it now is DISPOSED under the build method's M4, fold or promote, and never re-rounded: $subj"
```

It names the section and not the file, as the driver's check 49 already does for M2, so no new
literal `BUILD-METHOD.md` enters `unattended.sh` and the `method carriers` registry row for that
file stays true as written. It carries no path, so the install-prefix ratchet does not move.

Observed on 2026-09-13 against a scratch copy of base `16da4c6a` with a fixture run-state file at
phase `SPECCING` carrying one `CONVERGED` row: the unedited driver printed the current refusal in
0.69 s and left the row count at 1; the edited driver printed the new one, exit 1, row count 1.

### What check-arms sees

`tools/memory-tree/check-arms.py` discovers every `fail <n> "` branch in a tracked gate and requires
a POSITIVE assertion in the sibling `.test.sh` containing the branch's signature — the longest
literal run between interpolations, trailing `: ` trimmed. `--report` at base lists this branch as
`check 37 branch 10 line 4096 ARMED`. The new signature is the whole message up to `: $subj`, and
the two existing arms quote only the old text, which is a strict prefix of it. So the message change
ALONE turns the `harness arms` leg red, naming branch 10 and the new signature; observed on
2026-09-13 in the scratch copy, and green again once the two arms quote the new text. That leg is
`chunk: declarations`, unguarded, on every bar. It is the cheap observation of the pair; the suite
below is the expensive one.

### The suite arms

`tools/unattended/unattended.test.sh`, region two, in the `MARK review-loop` block. Two moves and
one addition:

- The `hit` at `unattended.test.sh:4589` and the one at `unattended.test.sh:4601` quote the new
  signature in full. `check-arms.py` matches by substring over the whole line, so each must contain
  the entire run; a line stopping at the old text reads as unarmed with no hint why, and `--report`
  prints the row to copy.
- One new block after the `S1` block, on a fresh subject, driving the ruling's sequence:

```
bcopen
run --review tRun --subject C1 --verdict "CLEAN WITH FIXES" --blockers 0 >/dev/null
hit "$(run --review tRun --subject C1 --verdict BLOCKED --blockers 1)" "<the new signature, verbatim>"
same "a refused round on a converged subject wrote nothing" "$(grep -c 'review · item C1 · reason' memory/builds/tRun/RUN.md)" "1"
reset_tree
```

`hit` is positive by construction: it greps the captured output for the text, so an empty capture —
a driver that crashed, a `run` that returned nothing — fails it rather than passing it. The `same`
asserts the VALUE the ruling cares about, one row, not that a row exists. Both existing arms reach
branch 10 through `NON-CONVERGENT`; this is the first that reaches it through `CONVERGED`, which is
the case the ruling is about. The sequence was driven against the real driver on 2026-09-13: round 1
printed `CONVERGED — the loop is done for this subject`, the second call was refused, the row count
read 1.

Two assertions are added. `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` are shrink-only minimums and stay
where they are; the executed count rises by two above them, which is the direction a floor permits.

### Inventory

No identifier is minted: no function, no leg, no file, no conf key, no pin row. The lexicon has
nothing to grade.

### Rollout

The pass writes `tools/memory-tree/BUILD-METHOD.template.md`, `memory/guides/BUILD-METHOD.md` (by
`--render`), `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`,
`memory/guides/SESSION-KICKOFF.md` (the `last-audit` line only), its own acceptance ledger under
`memory/builds/aRatifiedRulings/build/`, and the memory-tree version carriers —
`KIT_MEMORY_TREE_VERSION` in `tools/memory-tree/check-memory-hygiene.sh`, the marker in each shipped
`.template.md` under `tools/memory-tree/`, the four renders re-made by `--render`. No unattended
carrier moves here; section 3's edge names who owns that.

The PRODUCT write set is disjoint from unit 2's. `TOOL-aRatifiedRulings-2` §4 lists
`tools/unattended/check-unattended.sh`, where check 23 of the LEG opens at `check-unattended.sh:2222`
and closes at `:2361`, `tools/unattended/check-unattended.test.sh`, and its own ledger under
`build/`; the `fail 23` at `unattended.sh:712` is the driver's object-substitution refusal and unit 2
does not touch it. Nothing in this unit's product list appears in that one.

Disjoint product files do NOT make the passes concurrent. A pass's declared set is never only its
product files: every pass commit moves its spec's status header, hygiene check 9
(`gen_build_index.py --check`, run by the pre-commit staged leg whenever `memory/` is touched)
then forces `memory/LIVE.md` and `memory/ledger/<month>.md` to be re-rendered in the same commit,
and every pass edits the build README — so every pass of this build declares its spec, the README
and those two indexes beside its products, as every dispatch row of the parent build
`aLeakedHandle` did and as its pass commit `922fd926` wrote. `--dispatch` check 49 condition 1 at
`unattended.sh:4853` refuses a declared path that `overlaps` any still-open sibling's, and
`overlaps` at `lib-unattended.sh:100-105` is `covers` both ways with `covers` true on EQUALITY, so
the second of two open passes honestly declaring `memory/LIVE.md` is refused and the run parks; a
pass declaring less than it writes prints check-23 lines instead. Units 1 and 4 additionally both
declare `memory/guides/SESSION-KICKOFF.md`, which is no `SHARED_RECORDS` member and collides on
equality the same way. The passes of this build are therefore SEQUENTIAL, and the M2 roster orders
them; this spec derives no order among them. The second of units 1 and 4 to land re-stamps
`last-audit` over the first, per the charter's kickoff-manifest merge exception. One fact the
roster still weighs, stated so it does not re-derive it: each unit's self-test reads the other's
product file at lines the other does not move — `check-unattended.test.sh:147` greps
`unattended.sh` for its `_CORE` constants, and `unattended.test.sh:3729` greps
`check-unattended.sh` for `ls-remote` — which is M6 condition 2 at file grain, false at line grain,
and moot while the passes are sequential. Declaring the ledger under
`memory/builds/aRatifiedRulings/build/` by FILE rather than by directory would matter only if two
passes were ever open together, which check 49 makes impossible here.

Landing owes no data step. Existing `review` rows keep their grammar and their meaning; a run-state
file written before this unit reads identically after it.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | one paragraph added in M4, one clause qualified in M4's first paragraph, marker bumped |
| `memory/guides/BUILD-METHOD.md` | re-rendered from the template |
| `tools/unattended/unattended.sh` | one message extended at branch 10; `KIT_UNATTENDED_VERSION` stays 1.19 |
| `tools/unattended/unattended.test.sh` | two `hit` strings moved, one five-line block added |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamped |
| memory-tree version carriers | `KIT_MEMORY_TREE_VERSION` 2.69 to 2.70, template markers moved, renders re-made |
| `memory/builds/aRatifiedRulings/build/<date>-build-TOOL-aRatifiedRulings-1-1-acceptance-ledger.md` | one row per criterion, declared by file |

### Alternatives rejected

- **Re-arm the loop on a rev bump.** Option 1 of the park; refused by the ruling.
- **Reword the sentence in M4 only and leave the driver's message.** The next run parks the same
  question at the same refusal, which is what the park said would happen and why the ruling owes
  both halves.
- **Cite the method by path in the message.** `$M/guides/BUILD-METHOD.md` would split the
  signature and add a second literal mention that the carriers registry row does not describe;
  the section name is what the driver already uses.
- **Put the decision id in the M4 paragraph.** Twenty-four bytes that mean nothing in an adopter's
  render; the template carries none today.
- **Move only one of the two existing arms.** `check-arms.py` needs any one arm to contain the
  signature, so a half-moved pair passes it and leaves a `hit` quoting text the driver no longer
  prints, which fails the suite for a reason nobody staged. Both move.

## 5. Production-readiness checklist

- security — N/A. Two guide sentences and a refusal message; no write path, no input boundary.
- perf / scale — the method grows by 304 bytes against M7's whole-file re-read, 905 bytes under M1
  and 198 under the recorded high-water. The refusal path adds no spawn; the suite adds one driver
  call pair.
- error / empty / loading states — the refusal is the only state this unit touches and it keeps
  exit 1 and writes nothing, which AC5 asserts as a row count.
- observability — THE COST THE RULING RECORDS, stated plainly: a blocker found on a converged
  subject leaves no `--review` row, because the driver refuses the round that would write one. The
  run-state file's review rows, `review_counts`, the closing-loop census over those rows and check 2
  of `tools/unattended/check-unattended.sh` therefore cannot count it. Its only records are the
  review record's `## Verdict:` line under `reviews/` and the spec's rev bump with its §9 line. The
  corpus census of blockers per subject is under-counted by every such finding, and nothing in this
  unit closes that.
- risks — the method is re-read whole by every run, so a sentence that reads as licence to skip a
  review would be read that way; the wording binds the disposition to "a blocker confirmed", never to
  the review itself. The parity leg's printed fix overwrites a render-only edit, named in section 4.
- testing — two arms moved, one added, all in `tools/unattended/unattended.test.sh`, with the
  failing case observed RED first at both observation points: `harness arms` against the unmoved
  arms, and the suite against a driver whose message is reverted. The suite is not a bar leg, so its
  cost and invocation are on AC4.
- migration — N/A. No row grammar, conf key or record format changes.
- user docs — the method is the document. `memory/guides/UNATTENDED-VERBS.md` already says
  `--review` refuses a round on a subject whose loop has ended and is not the carrier of the route,
  so it does not change; the route is now in the driver's own text.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs at the landed tip, it
  prints `shipped and installed docs agree`, and
  `grep -cF "CONVERGED is terminal for its subject" memory/guides/BUILD-METHOD.md` and the same grep
  over `tools/memory-tree/BUILD-METHOD.template.md` each print `1`, as does
  `grep -cF "by anything but that review's own fold"` over both files.
  Red when: either count is `0` in either file, or the parity leg prints `DRIFT`, which is what a
  render-only edit produces and its printed fix then erases.
- **AC2** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs at the landed
  tip, it prints `template-size OK` with a byte figure at or below the 27648 in
  `tools/template-size-limits.txt` and prints no `TEMPLATE-SIZE WARN` line, and
  `wc -l < memory/guides/BUILD-METHOD.md` prints at most 350.
  Red when: the render passes 27648, which is `fail 2`; or passes 26941, the recorded high-water,
  which prints the WARN and means a `--bump` this spec says is not owed has become owed; or the line
  count passes 350, which no leg reads and only this criterion does.
  figure: both bounds are DERIVED at observation from `tools/template-size-limits.txt` and the M1
  `**Budget:` line; the 26743 and 340 in section 4 are PINNED from the staged measurement of
  2026-09-13.
- **AC3** — When the message at `tools/unattended/unattended.sh:4096` is extended and the two arms
  in `tools/unattended/unattended.test.sh` still quote the old text,
  `python3 tools/memory-tree/check-arms.py --check` exits 1 naming `check 37 branch 10` and the new
  signature; once both arms quote the new text it exits 0 and `--report` shows that branch `ARMED`.
  Red when: the staged half exits 0, which would mean the arms were not read as the branch's own
  failure text and the leg cannot see this pair at all.
  fixture: the real tree; the staged half is the state between the driver edit and the arm edit,
  observed before the arm edit is made.
- **AC4** — When `bash tools/unattended/unattended.test.sh --shard 2/2` is run twice with BOTH
  streams redirected to one file, `> <file> 2>&1`, once against the landed driver and once against
  a copy of the driver with the message at `unattended.sh:4096` reverted to the base text, the
  reverted run's file holds `FAIL missing:` followed by the new signature exactly three times — the
  two moved arms and the new one — and the landed run's file holds that line zero times and holds
  `MARK review-loop`. The MARK is written to stderr (`unattended.test.sh:4532`, `>&2`) while
  `hit`, `miss` and `same` at `:69-71` print their `FAIL` lines to stdout, so a stdout-only
  redirect holds the FAIL delta and no MARK, and reads a correct landing as "the region never ran".
  Red when: the reverted run shows fewer than three, which means an arm did not execute or quotes
  something the driver already prints; or the landed run's file lacks `MARK review-loop`, which
  means the region never ran and an absent FAIL line is silence rather than a pass.
  cost: shard two of the suite, last recorded at 2013.7 s in the comment block of
  `tools/unattended/run-unattended-gates.sh`, on each of the two runs. Never read the result through
  `tail`; redirect both streams and grep the file.
  permission: this suite is a kit self-test and is on no boundary bar by the owner's 2026-08-23
  ruling; nothing sets `GATE_SELFTESTS=1` and `tools/gate-legs.json` carries no row for it. The
  direct sharded invocation above is the only one this run executes. The shard carries a
  pre-existing failure population whose size after the fixture-heading fix is unmeasured
  (`TOOL-aTracedSpawn-3`), so the exit status is not the observation and the FAIL-line delta is.
  `TOOL-aTracedSpawn-1` records that the unsharded run aborts at a bare `$1`; that token is absent
  from the file at base `16da4c6a`, but the row stands and the sharded form is the one with a
  recorded cost, so it is the one named here.
- **AC5** — When the landed shard-two run reaches the new block, the driver's first call prints
  `CONVERGED` for subject `C1`, its second is refused with the new text, and the `same` arm reads
  `1` for the count of `review · item C1 · reason` rows in the fixture build's `RUN.md`.
  Red when: the count reads `2`, meaning the refused round wrote a row, or `0`, meaning round 1 was
  not recorded and the second call was refused for a reason other than the terminal token.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh` runs at the landed tip, its check 5
  reports no watched file changed since `last-audit`, because the commit that edits
  `memory/guides/BUILD-METHOD.md` re-stamps the `last-audit` line in `memory/guides/SESSION-KICKOFF.md`
  with a delta line in its message.
  Red when: the render lands without the re-stamp and check 5 names `memory/guides/BUILD-METHOD.md`
  as a watched file changed after the stamp.
- **AC7** — When `bash tools/check-kit-versions.sh` runs at the landed tip, it exits 0 and prints
  NOTHING — its one summary line, `kit-versions: <n> problem(s)`, is printed on failure alone, at
  `check-kit-versions.sh:270` behind `[ "$fails" = 0 ] && exit 0`, so a `0 problem(s)` line never
  exists to observe — with `KIT_MEMORY_TREE_VERSION=2.70` at
  `tools/memory-tree/check-memory-hygiene.sh:20` and every tracked `tools/memory-tree/*.template.md`
  marker reading `gov:kit memory-tree@2.70`; `grep -c '^KIT_UNATTENDED_VERSION=1\.19 ' tools/unattended/*.sh`
  reports `1` for `unattended.sh`, `check-unattended.sh`, `check-pass-order.sh` and
  `check-brief-recorded.sh` and `0` for every other file; and `bash tools/memory-tree/check-verdict-epoch.sh`
  prints `clean` and exits 0. S5's same-commit rule is joined on the BYTES the bump dates, never on
  the file: `git log -G'^KIT_MEMORY_TREE_VERSION=' --format=%H 16da4c6a..<tip> -- tools/memory-tree/check-memory-hygiene.sh`
  prints exactly one sha, and `git show <that-sha> -- tools/memory-tree/BUILD-METHOD.template.md`
  piped through `grep -c '^+.*CONVERGED is terminal for its subject'` prints `1`, as does the same
  pipe through `grep -c "^+.*by anything but that review.s own fold"`. The marker on the template's
  line 1 does NOT satisfy the join, and no file-level join can: `check-kit-versions.sh:135-147`
  reds any tracked `tools/memory-tree/*.template.md` whose marker disagrees with the constant, so
  the bump commit always touches the template's line 1, and
  `git diff-tree -r --no-commit-id --name-only <sha>` lists the template whether or not the M4
  bytes rode along. `a3b4ca1e`, the last real bump, lists it for a 2-line marker move and no
  method edit. Without `-r` that command prints only `memory` and `tools`, which is why the rev-2
  spelling read red against a correct build.
  Red when: a memory-tree carrier still reads 2.69, which the leg names as
  `marker != KIT_MEMORY_TREE_VERSION`; or any of those four counts reads `0`, which means this pass
  performed the bump `TOOL-aRatifiedRulings-2` §8 F1 assigns to the closing pass, or moved a
  constant the closing pass expects to find at 1.19; or the `-G` log prints no sha or two; or
  either added-line count prints `0`, which is the split S5 forbids — the M4 bytes in one commit,
  the constant and the markers in a later one. Staged break, observed before the fold is trusted:
  on a scratch branch off `16da4c6a`, commit the two M4 edits alone, then the constant, the
  markers and the `--render` as a second commit; the `-G` log prints the second sha and both
  counts print `0` against it. `grep -c` exits 1 on a zero count, so the figure is read from
  stdout and the pipe is never chained with `&&`.
  figure: 2.70 is PINNED as the next value above base `16da4c6a`, where every memory-tree carrier
  reads 2.69; 1.19 is DERIVED from the four `tools/unattended/` scripts at that base and this unit
  moves it nowhere. `clean` here is the gate's second clean form,
  `clean — 2 line(s) moved in <W> and the version moved 2.69 -> 2.70 in <S>`, with W and S the
  same sha by construction: the constant line at `check-memory-hygiene.sh:20` is itself a
  non-comment engine line, so `behav_in` counts the bump as the 2 lines moved, and no other engine
  line moves in this unit. That form prints wherever the range holds the bump — the pass branch,
  or local `main` before the push; once `origin/main` carries the tip the range is empty and the
  first form, `no behaviour-bearing engine line moved`, prints instead. Either way the gate scans
  the engine and six delegates and never the template, so it cannot grade the placement of the M4
  bytes, which is the `git show` join's job, and it says nothing about the unattended kit at all.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `build-method size` · `kit/dogfood doc parity` · `method carriers (every pointer declared)` · `kickoff-manifest ratchet` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

Chunks and guards, read from `tools/gate-legs.json` on 2026-09-13: `harness arms`, `method
carriers`, `kit version markers` and `verdict epoch` are `chunk: declarations` with no guard, so
every bar runs them; `build-method size` is `chunk: product`, unguarded; `kit/dogfood doc parity` is
`chunk: declarations` guarded on six paths, `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`,
`memory/guides/BUILD-METHOD.md`, `memory/guides/ANNOTATION-STYLE.md`, `tools/lib/` and
`tools/memory-tree/`, so a scoped bar whose diff misses all six skips it and the push boundary's
full bar does not — and this pass's diff cannot miss them, because the marker bump plus `--render`
rewrites all four docs in the leg's `PAIRS` line; `kickoff-manifest ratchet` and `memory hygiene`
are `chunk: records`; `spec tokens` is `chunk: declarations`. None of them is `chunk: selftests`.

The suite that observes AC4 and AC5 is `chunk: selftests` by ruling and is on no bar at all: it is
absent from `tools/gate-legs.json`, and its row in `tools/run-gates/selftest-budgets.txt` is a budget
for the on-demand runner, not a leg. The direct invocation is on AC4.

New arm: `tools/unattended/unattended.test.sh` · a fresh subject converges at round 1 and a
`BLOCKED` round follows; the failing case is the driver with its message reverted, which the arm
reports as `FAIL missing:` · no floor moves.

Moved arm: `tools/unattended/unattended.test.sh` · the two `hit` strings at lines 4589 and 4601
quote the new signature in full · no floor moves.

## 8. Open questions

- **F1 — does the ruling reach M4's first paragraph, or only the loop paragraph?** The ruling
  says "an M4 sentence"; the rev-moved clause in the first paragraph is where the method spells
  the re-arm the ruling refuses. Option A, add the terminal paragraph and leave the clause: 258
  bytes, and M4 keeps instructing a round the driver refuses. Option B, add the paragraph and
  qualify the clause: 304 bytes, and the two halves of M4 agree. Recommendation: B.
  RESOLVED (agent, 2026-09-13, delegated): B. Both edits sit inside the section the ruling names
  and both implement its "no re-arm on a rev bump" clause; A leaves the method contradicting the
  driver it points at, which is the `a directive names a route that does not run` class. Veto 2
  is not tripped: the carrier edit is the one the ruling itself mandates, and B adds 46 bytes to
  it under the same budget. The mark is contestable at the spec audit.
- **F2 — does the memory-tree kit version move for a template-only edit?** The engine does not
  change, so `check-verdict-epoch.sh` demands nothing. Option A, bump unattended only: the precedent
  at commit `8c759e50`, a method-only edit that left 2.x alone. Option B, bump both: the precedent
  at `TOOL-dMuffledSentinel-3`, where an adopter refused a pull whose bytes had moved at an unchanged
  version. Recommendation: B, the later ruling.
  RESOLVED (agent, 2026-09-13, delegated): B. The template is a shipped byte and the adopter-side
  refusal that decision records applies to it exactly as to a checker; the epoch gate over-counts by
  design and accepts a bump with no engine change. Cost is one constant, four marker lines and a
  `--render`.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft, from ruling `TOOL-aLeakedHandle-6` and the park it answers.
- rev-2 · 2026-09-13 · S5 · §3 · §4 · §5 · AC7 · §8 · folded round-1 spec-audit clusters A (ids 1,
  12, 30, 43), B (ids 2, 13, 34, 44) and L (id 26). A: the in-pass `KIT_UNATTENDED_VERSION` bump
  left S5, the Rollout carrier list, Files touched and AC7; the closing pass owns it per
  `TOOL-aRatifiedRulings-2` §8 F1, and AC7 now asserts the constant UNCHANGED at 1.19 beside the
  memory-tree 2.70 move. B: the Rollout write-set paragraph named unit 2's files wrongly and derived
  a sequencing rule from that; it now states the sets are disjoint against unit 2's own §4 and
  `unattended.sh:4853`. L: the M4 cost re-measured at 304 bytes, not 310, and its headroom pair
  moved with it in §4, §5 and F1's option figures; the F1 mark stands.
- rev-3 · 2026-09-13 · §3 · §4 · §7 · AC4 · AC7 · folded round-2 spec-audit clusters A (ids 1, 8,
  24, 10), B (ids 17, 9), F (ids 11, 21), G (id 23) and I (id 13); terminal fold, the loop is
  CONVERGED for this subject. A: AC7's same-commit join read red as spelled (`diff-tree` without
  `-r`) and could not fail once spelled, since the bump always moves the template's line-1 marker;
  it now joins on the M4 bytes in the `-G` commit and names the two-commit split that reds it. B:
  the Rollout paragraph licensed a concurrent pass with unit 2, which check 49 condition 1 refuses
  because every pass declares the two generated indexes, the README and its spec; the passes are
  SEQUENTIAL. F: AC4's redirect carries stderr, where the MARK lives. G: the closing pass's carrier
  set is the derived fifteen-file probe, `README.md:1` included, not the paired-plus-two
  enumeration. I: the parity leg's guard list quoted as the manifest has it, six paths.
- rev-4 · 2026-09-13 · AC7 · the build pass. AC7 expected `kit-versions: 0 problem(s)` on stdout,
  a line `tools/check-kit-versions.sh` never prints: it exits 0 silently and prints its
  `<n> problem(s)` summary only past a failure, so the criterion as spelled could not be observed
  against a correct build. The observation is now exit 0 with empty stdout. §4's pinned render
  figures reproduced exactly, 26743 B / 340 lines; the rest of §6 is graded in the acceptance
  ledger under `build/`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a review round refused on a subject whose loop already
converged names the disposal route"`, run on 2026-09-13 at base `16da4c6a`, reported
`scan coverage: 70 files scanned | 0 parse skips | unscanned layers: .sh`. Both files this unit
edits for behaviour are `.sh` and the third is a Markdown template, so the map probe is BLIND to
this subject and NO claim here rests on it; its ranked candidates are Python symbols from the
process-monitor and govkit kits and none is this seam. Said plainly because the probe returns a
confident list either way.

The seams were found by reading source and both EXIST: branch 10 of `verb_review` in
`tools/unattended/unattended.sh`, whose predicate stays and whose message is the surface; and the
M4 disposition paragraph in `tools/memory-tree/BUILD-METHOD.template.md`, which already names FOLD
and PROMOTE, so the new paragraph points at a disposition the method defines rather than defining
one. On the test side the seam is the existing `MARK review-loop` block of
`tools/unattended/unattended.test.sh` with its `bcopen`, `run`, `hit` and `same` helpers; the new
arm mints nothing. The recall probe returned `TOOL-dCarriedReceipt-2` as the backlog row naming this
collision and `TOOL-dHonouredPark-8` and `TOOL-aProvenReuse-3` as the neighbours this unit leaves
alone; the first is where the hit was STALE against source, citing the branch at `unattended.sh:3135`
where the file at base holds it at line 4096.

Recall terms used: `python tools/memory-recall/query.py "what disposes a blocker found on a review
subject whose loop already recorded CONVERGED, and why does check 37 refuse another round" --terms
"review loop CONVERGED terminal round check 37 disposition fold promote M4 re-arm blocker re-round
subject"`.
