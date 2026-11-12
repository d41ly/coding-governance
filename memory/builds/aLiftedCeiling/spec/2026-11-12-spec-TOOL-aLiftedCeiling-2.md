# TOOL-aLiftedCeiling-2 — the instruction-edits evidence row names its host load and its clone's commit

**Status:** CLOSED · rev-1 · 2026-11-12 · node a · Tier-1 · base b28597c1f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aLiftedCeiling-1-agent-ledger.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-1-agent-ledger.md) | journal | TOOL-aLiftedCeiling-1 TOOL-aLiftedCeiling-3 |
| [2026-11-12-build-TOOL-aLiftedCeiling-1-runlog-0a5fb16b.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-1-runlog-0a5fb16b.md) | journal | TOOL-aLiftedCeiling-1 TOOL-aLiftedCeiling-3 |
| [2026-11-12-build-TOOL-aLiftedCeiling-2-1-builder-return.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-2-1-builder-return.md) | journal | — |
| [2026-11-12-build-TOOL-aLiftedCeiling-2-ledger.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-2-ledger.md) | journal | — |
| [2026-11-12-prompt-TOOL-aLiftedCeiling-2-1-spec-writer.md](../prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-2-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-TOOL-aLiftedCeiling-2-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-2-build-brief.md) | journal | — |
| [2026-11-12-prompt-TOOL-aLiftedCeiling-2-spec-brief.md](../prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-2-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The `instruction edits (manifest checks)` row in `tools/run-gates/ceiling-evidence.txt` gets a
source text that states the host load its race ran under and the commit its clone was taken at. The
file's header says that text is the only record of an `--observed` reading's load, and the closing
review's round 1 (`2026-11-12-review-TOOL-aLiftedCeiling-1-diff-review-round1`, item L1) found it
names none.

## 2. Scope (IN)

- **S1** — The leg's row keeps 110.0 seconds, 1 reading and node `a`, and its source text is
  replaced by the text in section 4. The kit's own `--write` produces it in a fresh scratch clone,
  and the generated file is copied back. Observed by AC1 and AC4.
  **Readers:** the old source text, quoted in section 4.
  by name: `tools/run-gates/ceiling-evidence.txt`, the row's own file, is the one reader that spells it, and this unit rewrites that row. `tools/run-gates/derive-ceilings.py` spells none of it: its check echoes the source column verbatim on its OUTSIDE line at run time. The closing review's round 1 and this spec quote it as records, which resolve nothing. A fixed-string git grep for its phrase "instructions_edit waiting on the tag-index write lock" over the tracked tree, with this spec staged, finds the row's file and those two records and no other file (PINNED 2026-11-12).
  by value: `tools/run-gates/derive-ceilings.py` grades the row's seconds, which stay 110.0, and reads the source only to tell it from `runner` (`tools/run-gates/derive-ceilings.py@9f57a263f:706`), which stays true; `tools/run-gates/run-gates.sh` takes the seconds as a dispatch prior (`tools/run-gates/run-gates.sh@970e3e89a:2885`); `tools/run-gates/owed_rows.py` reads the leg-name column only (`tools/run-gates/owed_rows.py@cf24e5293:116`). No reader acts on the source text's content.
- **S2** — No other row of the file moves. Against the build's base the file still differs by one
  added line, and against this spec's base by the one row replaced. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- No change to the leg's ceiling, to the measured 110 s, or to any other row.
- No new race. Section 7 F1 says why the race is not repeated at `123123146`.
- No change to `derive-ceilings.py`. The review's left-shift gate, an `--observed` refusal of a
  `--how` text without a load clause, is a separate unit and is not built here.
- No edit to spec TOOL-aLiftedCeiling-1. It is CLOSED and frozen, so this spec is where the clone's
  commit is recorded.
- No help page. The file is declared `project-owned` and is not shipped to an adopter
  (`tools/run-gates/kit.toml@9bd37dd65:73` and `:74`).

## 4. Design

### What the row says today

The row at `tools/run-gates/ceiling-evidence.txt@628251fa2:67` holds leg
`instruction edits (manifest checks)`, 110.0 s, 1 reading, node `a` and date 2026-11-12. Its
source text is:

```
gov_tag.py check raced against instructions_edit.py check on a fresh index in a scratch clone of 33a1a8676, instructions_edit waiting on the tag-index write lock, 110s wall, TOOL-aLiftedCeiling-1 AC2
```

It names no load. It names `33a1a8676`, the unit's pass commit, while unit 1's Design asked for a
clone of `123123146`
(`memory/builds/aLiftedCeiling/spec/2026-11-12-spec-TOOL-aLiftedCeiling-1.md@a255c4d63:131`).

The race did run at `33a1a8676`
(`memory/builds/aLiftedCeiling/build/2026-11-12-build-TOOL-aLiftedCeiling-1-ledger.md@026fdf620:27`).
It ran with no other gate run on the host. That is the main loop's account, recorded in this unit's
brief (`memory/builds/aLiftedCeiling/prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-2-spec-brief.md@8f4457c03:29`),
PINNED 2026-11-12. No census reached the race, so the account is the only record of the load.

### Why the kit needs `--reset` beside `--observed`

The file is generated and monotone, so the source text is replaced through `derive-ceilings.py`,
never by hand. Two shorter routes fail, both read from the code at `9f57a263f`:

- `--write --observed` alone is refused. A reading at or under the stored maximum writes nothing
  and exits 1 (`tools/run-gates/derive-ceilings.py@9f57a263f:581`). 110 equals 110.
- A `--write --reset` first, then `--write --observed`, fails at the first step. In a clone with no
  run record and no `--observed`, the write returns DEAD PROBE and exit 2
  (`tools/run-gates/derive-ceilings.py@9f57a263f:513`).

One invocation carrying both flags works. The reset leg's stored row is not carried forward
(`tools/run-gates/derive-ceilings.py@9f57a263f:558`), so the observed path then finds no previous
row and writes the new one (`tools/run-gates/derive-ceilings.py@9f57a263f:587`). Every other row is
carried forward as read, and the rows are written in sorted order
(`tools/run-gates/derive-ceilings.py@9f57a263f:625`), which is how unit 1's write stayed one line.

The write MUST run in a fresh clone. `--reset` deletes the leg's killed readings from the
checkout's own run record under `<git-dir>/gate-run/`. In this worktree that would erase the leg's
retained killed readings, such as the two 180 s timeouts unit 1 tabled. The re-derive would also
rewrite the 16 UNDER legs unit 1 left alone
(`memory/builds/aLiftedCeiling/spec/2026-11-12-spec-TOOL-aLiftedCeiling-1.md@a255c4d63:40`). A
`git clone --local` carries no run record, so the reset removes nothing there.

### The steps

From a fresh `git clone --local` of the worktree at its HEAD, made outside the repository:

```
GOV_NODE=a python tools/run-gates/derive-ceilings.py --write --reset 'instruction edits (manifest checks)' --observed 'instruction edits (manifest checks)=110' --how '<how>'
```

`<how>` is exactly this text, one line, with no tab or newline:

```
gov_tag.py check raced against instructions_edit.py check on a fresh index in a scratch clone of 33a1a8676 (the pass commit; unit 1's spec named 123123146, and tools/playbook is identical at both), instructions_edit waiting on the tag-index write lock, 110s wall, no other gate run on the host during the race (the main loop's account; no census reached it), TOOL-aLiftedCeiling-1 AC2, source restated by TOOL-aLiftedCeiling-2
```

The kit's summary line then reads `1 dropped by --reset` and `1 raised by --observed`, with
`0 killed reading(s) removed by --reset`. The `raised` count is the observed path's tally and does not
mean the value moved. The builder copies the clone's `tools/run-gates/ceiling-evidence.txt` over the
worktree's. Copying the generator's output is not a hand edit.

The row's date column is the clone HEAD's commit date (`tools/run-gates/derive-ceilings.py@9f57a263f:527`).
At `b28597c1f` that is 2026-11-12, so the column does not move unless the clone's HEAD is a later
day's commit.

The phrase "no other gate run on the host" is the claim made, not "a quiet host". It matches what
the file header lets a census say, and it claims nothing about non-gate load.

### Files touched (estimate)

`tools/run-gates/ceiling-evidence.txt`

## 5. Acceptance criteria

- **AC1** — When `grep -c "^instruction edits (manifest checks).110\.0.1.a.[0-9-]*.gov_tag.py.*scratch clone of 33a1a8676.*no other gate run on the host" tools/run-gates/ceiling-evidence.txt` runs, it prints `1`.
  Red when: the source text still names no load or another commit, the value left 110.0, or a
  second row for the leg was written.
- **AC2** — When `git diff --numstat 123123146 -- tools/run-gates/ceiling-evidence.txt` runs, it prints `1` added and `0` deleted.
  Red when: the write read a retained run record and rewrote other legs' rows, which shows as more
  added and deleted lines.
- **AC3** — When `git diff --numstat b28597c1f -- tools/run-gates/ceiling-evidence.txt` runs, it prints `1` added and `1` deleted.
  Red when: a row other than the leg's moved, or the header was regenerated differently.
- **AC4** — When `python tools/run-gates/derive-ceilings.py --check` runs, it exits 0, prints no `CEILING-EVIDENCE FAILED` line, and its `OUTSIDE` line names the leg at `110.0s on node a` with the new source text.
  Red when: the row was dropped and the leg reads unbacked, or its source reads `runner`, which
  takes the leg off the `OUTSIDE` line.

## 6. Gates

`leg ceilings clear their evidenced maximum` · `spec tokens (a spec's own names resolve)`

The unit adds no suite arm. `leg ceilings clear their evidenced maximum` runs the same
`derive-ceilings.py --check` AC4 observes. It does not check that the source text is true, nor that
it carries a load clause: it grades only the seconds against the ceiling.

## 7. Open questions

- **F1 — Does the source name the clone's commit as run, or is the race repeated at `123123146`?**
  - (a) Name `33a1a8676` as run, and say in the text that unit 1's spec named `123123146`.
    `tools/playbook` is identical between the two commits (`git diff --stat 123123146 33a1a8676 -- tools/playbook`
    prints nothing), so the race exercised the same code. The value stays 110 s.
  - (b) Repeat the race in a clone of `123123146`. It yields a new wall, which changes the measured
    value against this unit's non-goal. A lower wall is refused by the monotone rule, and a higher
    one raises the row.
  - Recommendation: (a). It is the truthful record, and it costs no race.
  - RESOLVED (agent, 2026-11-12, delegated): (a). The handoff directs the writer to take its
    recommendation and mark it resolved.

## 8. Revision log

- rev-1 · 2026-11-12 · initial draft.
