# TOOL-aLiftedCeiling-1 — the instruction-edits leg's ceiling covers its wait on the tag index

**Status:** CLOSED · rev-1 · 2026-11-12 · node a · Tier-1 · base 123123146 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aLiftedCeiling-1-1-builder-return.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-1-1-builder-return.md) | journal | — |
| [2026-11-12-build-TOOL-aLiftedCeiling-1-agent-ledger.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-1-agent-ledger.md) | journal | TOOL-aLiftedCeiling-2 TOOL-aLiftedCeiling-3 |
| [2026-11-12-build-TOOL-aLiftedCeiling-1-ledger.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-1-ledger.md) | journal | — |
| [2026-11-12-build-TOOL-aLiftedCeiling-1-runlog-0a5fb16b.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-1-runlog-0a5fb16b.md) | journal | TOOL-aLiftedCeiling-2 TOOL-aLiftedCeiling-3 |
| [2026-11-12-prompt-TOOL-aLiftedCeiling-1-1-spec-writer.md](../prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-1-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-TOOL-aLiftedCeiling-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-1-brief.md) | research | — |
| [2026-11-12-prompt-TOOL-aLiftedCeiling-1-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-1-build-brief.md) | journal | — |
| [2026-11-12-prompt-TOOL-aLiftedCeiling-1-spec-brief.md](../prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-1-spec-brief.md) | research | — |
| [2026-11-12-review-TOOL-aLiftedCeiling-1-diff-review-round1.md](../reviews/2026-11-12-review-TOOL-aLiftedCeiling-1-diff-review-round1.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

Raise the `instruction edits (manifest checks)` leg's declared ceiling from 180 s to 420 s. Since
aQueuedIndex the leg waits for the tags leg's tree build instead of failing, and at both of that
build's bars it was killed at 180 s and passed only on its serial retry.

## 2. Scope (IN)

- **S1** — The leg's `ceiling` in `tools/gate-legs.json` reads 420
  (`tools/gate-legs.json@83fb3a5fb:2048`, 180 today). Observed by AC1 and AC5.
- **S2** — One race of the two tag-index checks on a fresh index in a scratch clone, and its
  instruction-edits wall clock recorded as the leg's row in `tools/run-gates/ceiling-evidence.txt`
  by `derive-ceilings.py --write --observed`. Every other row is carried forward byte for byte.
  Observed by AC2, AC3 and AC4.
- **S3** — The kickoff manifest's `last-audit` is re-stamped at or after the commit that changes
  `tools/gate-legs.json`, which its `watch:` list names
  (`memory/guides/SESSION-KICKOFF.md@e7ad37466:7`). Observed by AC6.

## 3. Non-goals (OUT)

- No other leg's ceiling. That includes the 16 legs the read-only `derive-ceilings.py --report`
  shows UNDER against this worktree's retained run record on 2026-11-12 (PINNED).
- No plain `derive-ceilings.py --write` in a checkout with a retained run record. It would rewrite
  those 16 legs' rows from that record and red the ceiling check on legs this unit does not own.
- No change to the tag index, `BUSY_TIMEOUT` (`tools/playbook/tag_index.py@46bfe37d2:117`), the
  runner, `derive-ceilings.py` or the margin file.
- No help page. `git grep` over `help/` finds no page that names this leg's ceiling.

### Edges

- **consumes-from** external — aQueuedIndex, landed at `aa8f08000`: the leg queues behind the
  other writer of the tag index instead of failing on its lock. Without it the race in AC2 reds on
  `database is locked` and measures nothing.
- **hands-off** external — the 16 UNDER legs in node a's retained run record. They are reported
  here and left for whoever next runs a plain `--write` on that node.

## 4. Design

### Why 420 s

The ceiling check in `derive-ceilings.py` requires a ceiling to clear its evidenced maximum R by
`max(floor, fraction × R)` (`tools/run-gates/derive-ceilings.py@9f57a263f:663` and `:683`). The
declared margin is a 120 s floor and a fraction of 1.0
(`tools/run-gates/ceiling-margin.txt@171003169:26`). So for any R of 120 s or more, the ceiling must
be at least 2R.

The leg's readings on node a, from this worktree's retained run record, PINNED on 2026-11-12. The
read-only `derive-ceilings.py --report` re-derives the admitted ones while the record is retained.

| Run | Status | Seconds | Foreign | What the leg did |
|---|---|---|---|---|
| push-179448341701747319733-619 | ok | 171.7 | 0 | Built the tree itself; the tags leg refused on the lock at 43.2 s |
| push-179448446934786916724-837 | fail | 45.1 | 0 | Refused on the lock, before aQueuedIndex |
| push-179448527602962931685-30123 | ok | 89.4 | 1 | Ran after the tags leg finished, on a built tree |
| unattended-179450345232738512245-5856 | timeout | 180.3 | 2 | Waited beside a 221.2 s tags leg; alone on retry, 105.0 s |
| push-179450577388973629-1240 | timeout | 180.2 | 2 | Waited beside a 207.0 s tags leg; alone on retry, 130.9 s |

The last two are aQueuedIndex's merge and landing bars, at `c739aab78` and `aa8f08000`. In
aQueuedIndex's five closing races in a scratch clone, the slowest writer took 130 s and the rest 105
to 110 s (`memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-1-ledger.md@32c697d1d:23`).

Four bounds come out of those readings:

- **344 s is the floor.** The 171.7 s reading has census 0 and status `ok`, so the read path admits
  it (`tools/run-gates/derive-ceilings.py@9f57a263f:280` and `:304`). The next plain `--write` on
  node a carries it into the evidence file. A ceiling under 171.7 + 171.7 s then reds the check.
- **352 s is the worst bar case.** At aQueuedIndex's two bars the leg waited beside a tags leg of up
  to 221.2 s, and then needed up to 130.9 s of its own on a built tree. It waits for the tags leg's
  write block, which is shorter than that whole leg, so this sum is an upper bound.
- **420 s is the partner's ceiling.** The tags leg declares 420 s
  (`tools/gate-legs.json@83fb3a5fb:2072`), which is exactly 210 s plus the margin over its own
  evidence row (`tools/run-gates/ceiling-evidence.txt@0d5d8d621:137`). Either writer may be the one
  that pays the cold tree build, so both writers of one index share one bound.
- **600 s is the busy timeout.** aQueuedIndex-1's design states that every leg opening the index
  carries a lower ceiling than 600 s, so a pathological wait inside a bar ends at the ceiling
  (`memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md@f5ef310a5:147`).

420 s is chosen because it clears both the 344 s floor and the 352 s bar case, and it is a value
the manifest already holds for the same work. It stays under the 600 s busy timeout, so the
property aQueuedIndex-1 relies on holds. A ceiling is a kill bound, so the size follows the wait
rather than the slowest pass anyone has seen. Section 7 F1 records the rejected values.

The kit's sizing rule for a fresh leg is `max(60, 3 × measured seconds)`
(`tools/run-gates/README.md@18e334883:916`). Over the 171.7 s reading it gives 515 s. That rule is
for a leg with no evidence. Here the margin file's rule is the one `--check` enforces, and 420 s
clears it.

### The evidence row

A raised ceiling owes an evidence row, because `--check` reads only the two tracked files. A leg
with no row is reported UNBACKED and is never graded, so without one the new ceiling is checked by
nothing. The leg has no row today. The file is generated and is never hand-edited.

The README's route for a reading the run record cannot give is `--write --observed`
(`tools/run-gates/README.md@18e334883:923`). Every `--write` first re-derives rows from the checkout's
own run record (`tools/run-gates/derive-ceilings.py@9f57a263f:504`), and that record is per
worktree (`tools/run-gates/derive-ceilings.py@9f57a263f:134`). In this worktree it holds the 16 UNDER
legs. So the builder runs the write inside the race's scratch clone, whose run record is empty.
There every existing row is carried forward unchanged
(`tools/run-gates/derive-ceilings.py@9f57a263f:562`), and the one observed row is added. The
builder then copies that generated file into the worktree. Copying the generator's output is not a
hand edit: the bytes are what `--write` wrote.

The steps, from the scratch clone's root, after `git clone --local` of the worktree at base:

```
python tools/playbook/gov_tag.py check & s=$(date +%s); timeout 420 python tools/playbook/instructions_edit.py check; r=$?; echo "ie rc=$r wall=$(( $(date +%s) - s ))s"; wait $!; echo "tags rc=$?"
GOV_NODE=a python tools/run-gates/derive-ceilings.py --write --observed 'instruction edits (manifest checks)=<wall>' --how '<how>'
```

`<wall>` is the printed wall in seconds. `<how>` says the two checks were started together on a
fresh index in a scratch clone of `123123146`, what else was running on the host, and
`TOOL-aLiftedCeiling-1 AC2`. It holds no tab or newline, which the flag refuses.

A later plain `--write` on node a may raise this row to the runner's 171.7 s. That is the monotone
rule working, and 420 s still clears it.

The row is also this leg's dispatch prior in a worktree with no ledger
(`tools/run-gates/README.md@18e334883:872`). The prior is advisory and never moves a verdict.

### The kickoff manifest

`tools/gate-legs.json` is on the manifest's `watch:` list, and the manifest check reds when a watched
file moves past the stamp (`skills/session-kickoff/manifest-check.sh@4d3d63c0f:1844`). The unit
re-stamps `last-audit` (`memory/guides/SESSION-KICKOFF.md@e7ad37466:6`) with the datetime advanced
and `HEAD`, in the commit that changes the ceiling or in a follow-up. The commit message carries the
delta line. No §B claim names this leg's ceiling, so the delta is `none`.

### Files touched (estimate)

`tools/gate-legs.json`
`tools/run-gates/ceiling-evidence.txt`
`memory/guides/SESSION-KICKOFF.md`

## 5. Acceptance criteria

- **AC1** — When `python -c "import json, sys; print([l['ceiling'] for l in json.load(open(sys.argv[1], encoding='utf-8')) if l['name'] == sys.argv[2]])" tools/gate-legs.json "instruction edits (manifest checks)"` runs, it prints `[420]`.
  Red when: the row still reads 180, or a second row of the same name prints two values.
- **AC2** — When `python tools/playbook/gov_tag.py check & s=$(date +%s); timeout 420 python tools/playbook/instructions_edit.py check; r=$?; echo "ie rc=$r wall=$(( $(date +%s) - s ))s"; wait $!; echo "tags rc=$?"` runs once from the root of a fresh scratch clone, it prints `ie rc=0`, a wall under 420 s, and `tags rc=0`.
  Red when: the instruction-edits check is killed at 420 s and prints `ie rc=124`, or either check
  prints `database is locked`.
  cost: about 2 to 4 minutes. aQueuedIndex's closing races took 105 to 130 s each on 2026-11-12,
  PINNED.
  fixture: a `git clone --local` of the worktree at base, made by the observer outside the
  repository, with no `gov` directory in its git dir before the race. The tree holds none today.
  figure: the wall is DERIVED at observation; the 420 s bound is PINNED by S1.
- **AC3** — When `grep -n "^instruction edits (manifest checks)" tools/run-gates/ceiling-evidence.txt` runs, it prints one row whose seconds equal AC2's wall, with readings `1`, node `a`, and the `--how` text as its source.
  Red when: the row is absent and the leg stays UNBACKED, or its source reads `runner`, or its
  seconds exceed 210, which 420 s cannot clear by the margin.
  figure: the seconds are DERIVED from AC2's run.
- **AC4** — When `git diff --numstat 123123146 -- tools/run-gates/ceiling-evidence.txt` runs, it prints `1` added and `0` deleted.
  Red when: the write read a retained run record and rewrote other legs' rows, which shows as more
  added and deleted lines.
- **AC5** — When `python tools/run-gates/derive-ceilings.py --check` runs with the AC3 row in place, it prints no `CEILING-EVIDENCE FAILED` line naming `instruction edits (manifest checks)`, and it names that leg among the ceilings backed by a reading taken outside the runner.
  Red when: the ceiling is held at 180 s with the row in place, and the check prints
  `ceiling 180s does not clear its evidenced maximum` for the leg.
- **AC6** — When `w=$(git log -1 --format=%H -- tools/gate-legs.json ); s=$(git log -1 --format=%H -G"^last-audit:" -- memory/guides/SESSION-KICKOFF.md ); git merge-base --is-ancestor $w $s && echo stamped` runs, it prints `stamped`.
  Red when: the ceiling commit lands after the last re-stamp of `last-audit`.

## 6. Gates

`instruction edits (manifest checks)` · `leg ceilings clear their evidenced maximum` · `kickoff-manifest ratchet` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

The unit adds no suite arm. The one kit check that grades a ceiling against its evidence is
`leg ceilings clear their evidenced maximum`, which runs `derive-ceilings.py --check`. AC5 observes
it red with the row written and the ceiling still at 180 s, then green at 420 s. The run-gates kit's
gov harness checks only that every gov leg declares a positive integer ceiling.

What the ceiling check does not check: whether an `--observed` reading was taken as its `--how`
text says, because no census reaches it. It also does not see a contended bar's wall, or the
readings retained in a worktree's run record that nobody has written into the tracked file.

## 7. Open questions

- **F1 — What value does the ceiling take?**
  - (a) 420 s. It clears the 344 s floor and the 352 s bar case, matches the partner writer's
    ceiling, and stays under the 600 s busy timeout.
  - (b) 344 s. This is the least the margin admits over the 171.7 s reading. The 352 s bar case
    already exceeds it, so a loaded bar could kill the leg again.
  - (c) 515 s. This is the README's `3 ×` rule for a fresh leg. It buys nothing (a) does not cover,
    for a leg that has evidence.
  - (d) 600 s. That is the busy timeout, or 180 s plus the partner's 420 s. It sizes the bound to a
    stuck lock rather than the wait, and it ties the busy timeout that aQueuedIndex-1 keeps above
    every ceiling.
  - Recommendation: (a).
  - RESOLVED (agent, 2026-11-12, delegated): (a) 420 s. The owner's answer "Yes, raise it" and the
    brief leave the value to the writer, and the writer's handoff directs a recommendation be
    taken and marked.
- **F2 — Which reading backs the new ceiling in the evidence file?**
  - (a) The race's wall, by `--write --observed` in the scratch clone, with the file copied back.
  - (b) A plain `--write` in this worktree, which carries the runner's 171.7 s. It also rewrites the
    16 UNDER legs' rows and reds the check on legs outside this unit.
  - (c) An `--observed` row transcribing the 171.7 s runner reading. That labels a reading the
    runner took as one taken outside it, which the source column exists to prevent.
  - Recommendation: (a). It is the measurement the brief asks for, and it moves one row.
  - RESOLVED (agent, 2026-11-12, delegated): (a). Taken under the same authority as F1.

## 8. Revision log

- rev-1 · 2026-11-12 · initial draft.
