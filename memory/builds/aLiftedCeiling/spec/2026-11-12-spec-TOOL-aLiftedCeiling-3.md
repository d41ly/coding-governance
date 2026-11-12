# TOOL-aLiftedCeiling-3 — the instruction-edits evidence row's source spells no kit path

**Status:** CLOSED · rev-1 · 2026-11-12 · node a · Tier-1 · base 5b42d34db · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aLiftedCeiling-1-agent-ledger.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-1-agent-ledger.md) | journal | TOOL-aLiftedCeiling-1 TOOL-aLiftedCeiling-2 |
| [2026-11-12-build-TOOL-aLiftedCeiling-1-runlog-0a5fb16b.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-1-runlog-0a5fb16b.md) | journal | TOOL-aLiftedCeiling-1 TOOL-aLiftedCeiling-2 |
| [2026-11-12-build-TOOL-aLiftedCeiling-3-ledger.md](../build/2026-11-12-build-TOOL-aLiftedCeiling-3-ledger.md) | journal | — |
| [2026-11-12-prompt-TOOL-aLiftedCeiling-3-1-spec-writer.md](../prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-3-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-TOOL-aLiftedCeiling-3-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-3-build-brief.md) | journal | — |
| [2026-11-12-prompt-TOOL-aLiftedCeiling-3-spec-brief.md](../prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-3-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The `instruction edits (manifest checks)` row in `tools/run-gates/ceiling-evidence.txt` gets a
source text that spells no kit path and says what TOOL-aLiftedCeiling-2's text said. The close's bar
over the prepared merge `889f6b571` red `install-prefix (shipped surface)` on that row alone, and the
leg has no waiver (`memory/builds/aLiftedCeiling/prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-3-spec-brief.md@09adfa867:9`).

## 2. Scope (IN)

- **S1** — The leg's row keeps 110.0 seconds, 1 reading and node `a`, and its source text is
  replaced by the text in section 4. The kit's own `--write` produces it in a fresh scratch clone,
  and the generated file is copied back. Observed by AC1, AC2 and AC4.
  **Readers:** the old source text, quoted in section 4.
  by name: `tools/run-gates/ceiling-evidence.txt`, the row's own file, is the one reader that spells it, and this unit rewrites that row. A fixed-string git grep for its phrase "tools/playbook is identical at both" over the tracked tree finds that file, the CLOSED spec TOOL-aLiftedCeiling-2 and this unit's two prompt records, and no other file (PINNED 2026-11-12 at base 5b42d34db). The spec and the records quote it and resolve nothing.
  by value: `tools/check-install-prefix.sh` scans the text and reds it (`tools/check-install-prefix.sh@401a476df:393`), which is the reason for this unit; `tools/run-gates/derive-ceilings.py` reads the source only to tell it from `runner` (`tools/run-gates/derive-ceilings.py@9f57a263f:706`), which stays true; `tools/run-gates/run-gates.sh` reads the leg name and seconds only (`tools/run-gates/run-gates.sh@970e3e89a:2892`); `tools/run-gates/owed_rows.py` reads the leg-name column only (`tools/run-gates/owed_rows.py@cf24e5293:122`).
- **S2** — No other row of the file moves. Against the build's base `123123146` the file still
  differs by one added line. Observed by AC3.

## 3. Non-goals (OUT)

- No change to the leg's ceiling, to the measured 110 s, or to any other row.
- No new race, and no change to what the text claims: the clone's commit, the playbook kit being
  identical at the commit unit 1's spec named, the host load and the wall all stay.
- No change to `derive-ceilings.py` or to `check-install-prefix.sh`, and no waiver: the check has
  none (`tools/check-install-prefix.sh@401a476df:24`).
- No edit to spec TOOL-aLiftedCeiling-2. It is CLOSED and frozen.
- No help page. The file is declared `project-owned` and is not shipped to an adopter
  (`tools/run-gates/kit.toml@9bd37dd65:73` and `:74`).

## 4. Design

### What reds today

The row at `tools/run-gates/ceiling-evidence.txt@8b6d530c8:67` holds leg
`instruction edits (manifest checks)`, 110.0 s, 1 reading, node `a` and date 2026-11-12. Its source
text, written by TOOL-aLiftedCeiling-2, is:

```
gov_tag.py check raced against instructions_edit.py check on a fresh index in a scratch clone of 33a1a8676 (the pass commit; unit 1's spec named 123123146, and tools/playbook is identical at both), instructions_edit waiting on the tag-index write lock, 110s wall, no other gate run on the host during the race (the main loop's account; no census reached it), TOOL-aLiftedCeiling-1 AC2, source restated by TOOL-aLiftedCeiling-2
```

The check's rule 2 counts the install prefix `tools/` followed by a kit name, directory-only
included (`tools/check-install-prefix.sh@401a476df:393`). Its population is every tracked file
under the tool root, shipped or not (`tools/check-install-prefix.sh@401a476df:35`), so the
project-owned file is graded. `tools/playbook` is the one hit. Run over this worktree at
`5b42d34db`, the check printed one spelling on one line, `tools/run-gates/ceiling-evidence.txt:67`,
kit `playbook` (PINNED 2026-11-12).

### The new text

All four counting rules need a `/` after the prefix or the kit, or a kit name or `tools` alone
between matching quotes (`tools/check-install-prefix.sh@401a476df:393` to `:397`). The new text
carries no `/`, and its only quote characters are the two apostrophes the old text already had,
which enclose no kit name. The kit path becomes the prose "the playbook kit". The raced scripts
`gov_tag.py` and `instructions_edit.py` both live in that kit, so the claim is unchanged:
`git diff --stat 123123146 33a1a8676 -- tools/playbook` prints nothing (PINNED 2026-11-12).

`<how>` is exactly this text, one line, with no tab or newline:

```
gov_tag.py check raced against instructions_edit.py check on a fresh index in a scratch clone of 33a1a8676 (the pass commit; unit 1's spec named 123123146, and the playbook kit is identical at both), instructions_edit waiting on the tag-index write lock, 110s wall, no other gate run on the host during the race (the main loop's account; no census reached it), TOOL-aLiftedCeiling-1 AC2, source restated by TOOL-aLiftedCeiling-3
```

Only two spans change: `tools/playbook` becomes `the playbook kit`, and the restating unit becomes
TOOL-aLiftedCeiling-3.

### The steps

The route is TOOL-aLiftedCeiling-2's, read from `derive-ceilings.py` at `9f57a263f`, the same blob
at `5b42d34db`. `--write --observed` alone is refused, because 110 is not above the stored 110
(`tools/run-gates/derive-ceilings.py@9f57a263f:581`). With `--reset` in the same call the leg's
stored row is not carried forward (`tools/run-gates/derive-ceilings.py@9f57a263f:558`), so the
observed path writes the new row (`tools/run-gates/derive-ceilings.py@9f57a263f:587`). Every other
row is carried forward and written in sorted order (`tools/run-gates/derive-ceilings.py@9f57a263f:625`).

The write runs in a fresh `git clone --local` of the worktree at its HEAD, made outside the
repository. `--reset` deletes the leg's killed readings from the checkout's own run record, and a
fresh clone has none, so the worktree's retained readings survive. In the clone:

```
GOV_NODE=a python tools/run-gates/derive-ceilings.py --write --reset 'instruction edits (manifest checks)' --observed 'instruction edits (manifest checks)=110' --how '<how>'
```

The builder copies the clone's `tools/run-gates/ceiling-evidence.txt` over the worktree's. Copying
the generator's output is not a hand edit.

The row's date column is the clone HEAD's commit date
(`tools/run-gates/derive-ceilings.py@9f57a263f:527`). At `5b42d34db` that is 2026-11-12. It moves
only if the clone's HEAD is a later day's commit, and AC2 admits that; the value, readings and node
are the fields that must not move.

### Files touched (estimate)

`tools/run-gates/ceiling-evidence.txt`

## 5. Acceptance criteria

- **AC1** — When `bash tools/check-install-prefix.sh` runs, it exits 0 and names no line of `tools/run-gates/ceiling-evidence.txt`.
  Red when: the source text still spells `tools/playbook` or another kit path, which the check
  names as `tools/run-gates/ceiling-evidence.txt:67` and exits 1.
  figure: PINNED 2026-11-12, at `5b42d34db` that row was the check's only hit.
- **AC2** — When `grep -c "^instruction edits (manifest checks).110\.0.1.a.[0-9-]*.gov_tag\.py[^/]*scratch clone of 33a1a8676[^/]*playbook kit is identical at both[^/]*110s wall[^/]*no other gate run on the host[^/]*TOOL-aLiftedCeiling-3$" tools/run-gates/ceiling-evidence.txt` runs, it prints `1`.
  Red when: the source text carries a `/`, drops the commit, the playbook clause, the wall or the
  load, the value left 110.0, the node left `a`, or a second row for the leg was written.
  figure: the date field is DERIVED from the clone HEAD's commit date, so the pattern admits any.
- **AC3** — When `git diff --numstat 123123146 -- tools/run-gates/ceiling-evidence.txt` runs, it prints `1` added and `0` deleted.
  Red when: the write read a retained run record and rewrote other legs' rows, which shows as more
  added and deleted lines.
- **AC4** — When `python tools/run-gates/derive-ceilings.py --check` runs, it exits 0, prints no `CEILING-EVIDENCE FAILED` line, and its `OUTSIDE` line names the leg at `110.0s on node a` with the new source text.
  Red when: the row was dropped and the leg reads unbacked, or its source reads `runner`, which
  takes the leg off the `OUTSIDE` line.

## 6. Gates

`leg ceilings clear their evidenced maximum` · `install-prefix (shipped surface)` · `spec tokens (a spec's own names resolve)`

The unit adds no suite arm. `install-prefix (shipped surface)` runs the check AC1 observes; it does
not check that the text is true, only that it spells no kit path. `leg ceilings clear their
evidenced maximum` runs the `derive-ceilings.py --check` AC4 observes, and grades only the seconds
against the ceiling.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-12 · initial draft.
