# TOOL-aHastenedSweep-1 — check 25's by-name pass tests `index()` before `test_whole_token`

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-2 · base f25308f0 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aHastenedSweep-1-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aHastenedSweep-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aHastenedSweep-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aHastenedSweep-1-brief.md) | research | TOOL-aHastenedSweep-2 TOOL-aHastenedSweep-3 TOOL-aHastenedSweep-4 |

<!-- /gen:spec-records -->

## 1. Goal

Check 25's by-name resolution pass calls `test_whole_token` once per reader line and per unresolved
token, and each call copies the line with `substr` before it searches. This unit puts a plain
`index()` test in front of that call, so a line that cannot hold the token is skipped before the
copy. The verdict is unchanged, because `test_whole_token` already returns 0 whenever `index()`
does. The analysis measured the pass at 347 s inside a full run and 41.7 s guarded, PINNED
2026-11-15 on node a (the build's brief, item 1).

## 2. Scope (IN)

- **S1** — In the END block of check 25's by-name awk program in
  `tools/memory-tree/check-memory-hygiene.sh`, the per-token condition gains `index(ln, pl[i]) &&`
  between the `got` test and the `test_whole_token` call, in the exact line §4 gives. Observed by
  AC1 and AC2.
- **S2** — One awk comment line above that `for` line says why the guard is exact and names this
  unit. It carries no single quote, because the awk program is a single-quoted shell word. Observed
  by AC2.
- **S3** — The U records, the N records, their order, and the `D` completion sentinel printed last
  are byte-identical to the shipped engine's, on a fixture and on the live tree. Observed by AC1 and
  AC3.
- **S4** — `memory/guides/SESSION-KICKOFF.md` takes its `last-audit` re-stamp in the same commit,
  because that manifest's `watch:` line names the edited shell. Observed by AC4.

## 3. Non-goals (OUT)

- Any change to `test_whole_token`, to the reader allowlist, to the identity map `idn`, or to the
  batched `git grep -I -l -F -f` that narrows the candidate files.
- A gawk alternation or regex prefilter. The analysis measured one identical and slower (PINNED
  2026-11-15): 87 s and 52 s against 41.7 s, PINNED 2026-11-15.
- Any other check, any other awk program, and any cache of check 25's result across runs or commits.
- The memory-tree kit version constant `KIT_MEMORY_TREE_VERSION`. This unit does not move it.
- The R5 commit recipe, the render stamp, R6, and the spec-writer prompt's hygiene scope. The owner
  holds those.
- `memory/builds/dDeclaredLoop/`, the worktree `unattended-declared-loop-d56bf0`, its branch and
  its run-state file.

### Edges

- **hands-off** external — the memory-tree kit version: this unit leaves `KIT_MEMORY_TREE_VERSION`
  as it is, and the build's brief places its one move in the build's last unit, which the verdict
  epoch leg holds owed at the lander.
- **hands-off** external — the live-tree A/B of AC3 and the close's legs of §7. Both are the main
  loop's, at the close, recorded in this unit's acceptance ledger under a `Pass: none` commit.

## 4. Design

### Evidence

Read at f25308f0.

| Fact | Where |
|---|---|
| `test_whole_token(s, w)` sets `q = 0` and opens with `while ((p = index(substr(s, q + 1), w)) > 0)`, and returns 0 when that loop never enters. | `tools/memory-tree/check-memory-hygiene.sh@a55d262d:3077-3089` |
| The END loop reads each reader line with `getline` and tests every unresolved token on it through `test_whole_token`. | `tools/memory-tree/check-memory-hygiene.sh@a55d262d:3101-3105` |
| The one call site is the condition `!(pl[i] in got) && test_whole_token(ln, pl[i])`. | `tools/memory-tree/check-memory-hygiene.sh@a55d262d:3103` |
| The U and N records print in token order after the loop, and `D` prints last. | `tools/memory-tree/check-memory-hygiene.sh@a55d262d:3106-3111` |
| A missing `D` reds check 25 as a pass that did not complete. | `tools/memory-tree/check-memory-hygiene.sh@a55d262d:3116-3117` |
| The awk program is one single-quoted shell word, opened after `awk -F'\t' -v m="$M"`. | `tools/memory-tree/check-memory-hygiene.sh@a55d262d:3076` |
| The suite's word-boundary fixtures and their assertions. | `tools/memory-tree/check-memory-hygiene.test.sh@4c50ac3a:1180-1193` and `tools/memory-tree/check-memory-hygiene.test.sh@4c50ac3a:2047-2068` |
| The kickoff manifest watches the shell. | `memory/guides/SESSION-KICKOFF.md`, its `watch:` line |

The brief and the analysis cite the condition at line 3100 of an earlier main, a76c6afe7. The line
is 3103 at f25308f0, and its text is the same.

### Why the guard is exact

`substr(s, 1)` is `s` itself, so the first test `test_whole_token` makes is `index(s, w)`. When that
is 0 the loop body never runs and the function returns 0. The guard computes the same `index(ln,
pl[i])` first and short-circuits only in that case. When it is non-zero, `test_whole_token` runs
exactly as it does today, so a whole-word hit and a substring-only miss are decided by the same
code. An empty token gives 0 from both. The guard reads no state and writes none, so `got`, `left`
and the order of the U and N records cannot move.

### The line

At `tools/memory-tree/check-memory-hygiene.sh@a55d262d:3103` this line:

```awk
          for (i = 1; i <= np; i++) if (!(pl[i] in got) && test_whole_token(ln, pl[i])) { got[pl[i]] = 1; left-- }
```

becomes these two:

```awk
          # index() first: test_whole_token returns 0 whenever index() does, so this skips only the line copy (TOOL-aHastenedSweep-1)
          for (i = 1; i <= np; i++) if (!(pl[i] in got) && index(ln, pl[i]) && test_whole_token(ln, pl[i])) { got[pl[i]] = 1; left-- }
```

The comment holds no single quote. A single quote there would close the shell word and break the
whole program, which `bash -n` does not see.

### What this does not check

- That a by-name token is live. Resolution shows a name is spelled where something reads, as the
  block comment at `tools/memory-tree/check-memory-hygiene.sh@a55d262d:3062-3063` says.
- Speed. AC3 records each side's wall time, and no gate holds a figure.

### Inventory

Nothing is minted: no function, variable, key, flag, leg or file.

### Migration

None. An adopter receives the line on its next kit update, and no verdict moves.

### Rollout

No switch. The pass runs `bash -n tools/memory-tree/check-memory-hygiene.sh`, then AC1 and AC2,
then `python tools/codebase-map/gen_map.py --write`, and commits whatever that rewrites with the
code. The re-stamp of S4 is `<ISO datetime with offset> @ <full sha of HEAD>`, under the stamp rule
of `skills/session-kickoff/manifest-check.sh`, with a delta line in the commit message naming the
guard.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/builds/aHastenedSweep/build/2026-11-15-build-TOOL-aHastenedSweep-1-1-acceptance-ledger.md`

### Alternatives rejected

- **A gawk alternation prefilter over all tokens.** Measured identical and slower than the guard, at
  87 s and 52 s against 41.7 s (PINNED 2026-11-15, the analysis's R1).
- **The guard inside `test_whole_token`.** Same verdicts, but the function call and its argument
  setup are part of the cost, and the loop is the only caller.
- **Caching check 25's whole result.** Every records commit moves the tree, so a cache would almost
  never answer, and the owner ruled out a cache across commits.

## 5. Production-readiness checklist

- security — No input boundary moves. The guard reads the same bytes `test_whole_token` reads.
- perf / scale — PINNED 2026-11-15, node a, contended: the pass measured 347 s in a full run and
  507 s alone, against 41.7 s guarded, PINNED 2026-11-15. The `--only 12` and `--only 25` runs take the same saving.
- error / empty / loading states — An empty token gives 0 on both paths. A pass that dies still
  prints no `D`, and check 25 reds as it does today.
- observability — None owed. The output is byte-identical, so nothing new is printed.
- risks — A single quote in the new comment would close the shell word. §4 holds the exact
  comment, and AC1 runs the program.
- testing — AC1 runs the changed engine and the shipped one over one fixture and compares them.
  AC3 compares them on the live tree. The suite's check 25 arms run at the close.
- migration — None (§4, "Migration").
- user docs — No page under `help/` describes check 25's cost, and no behaviour a user sees moves.

## 6. Acceptance criteria

- **AC1** — When `bash <worktree>/tools/memory-tree/check-memory-hygiene.sh --only 25` runs in a
  fixture repository, and the shipped engine runs there as
  `bash <scratch>/shipped/tools/memory-tree/check-memory-hygiene.sh --only 25`, the two outputs are
  `cmp`-identical with the same exit code. Each output carries one U line for each of `count_shard`,
  `tRerun`, `shard_rows`, `--dry` and `tAbsentReader`, each saying the token is one `which no
  reader spells`, and one `READER NOT IN TREE covers it` line for `tAbsentReader`. Neither output
  names `count_shard_rows` or `tSpelledInGuide`.
  Red when: the guard is written `index(ln, pl[i]) > 1`, so `count_shard_rows`, which the fixture's
  guide spells only at column 1 of one line, stops resolving and prints a U line; or the program no
  longer parses and no `D` prints.
  fixture: a fresh repository under `%TEMP%/hs1fx`, built by the builder, holding none today. Its
  conf is the one the suite writes at `tools/memory-tree/check-memory-hygiene.test.sh@4c50ac3a:279`.
  Its guide `treaders.md`, in the fixture's guides folder, has a line that opens with `count_shard_rows` and is the
  only place any reader spells it, and a line spelling `tSpelledInGuide`, `tRerunAll` and
  `--dry-run`. Its specs take the shape of the suite's `write_readers_spec`, one per by-name token:
  `count_shard`, `tRerun()`, `shard_rows`, `--dry`, `tAbsentReader`, `count_shard_rows` and
  `tSpelledInGuide`, and one more naming `tAbsentReader` under READER NOT IN TREE with a reason.
  The fixture is committed, because the engine selects by `git ls-files`. The shipped engine is
  `git archive f25308f0 tools` unpacked under the run's scratchpad.
- **AC2** — When `git diff --numstat f25308f0 -- tools/memory-tree/check-memory-hygiene.sh` runs
  it prints one row of 2 added and 1 deleted. Over the same file,
  `grep -c 'index(ln, pl\[i\]) && test_whole_token(ln, pl\[i\])'` prints 1, and
  `grep -c "TOOL-aHastenedSweep-1)"` prints 1.
  Red when: the edit moved another line of the engine, the guard landed somewhere other than the
  one call site, or the comment is missing.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 25` and the shipped engine's
  same command run on the live tree at one commit, their outputs are `cmp`-identical with the same
  exit code, and the acceptance ledger records both wall times and the output's line count.
  Red when: a token resolves on one side and not the other, or the record order moves.
  cost: the shipped side measured 347 s to 507 s, PINNED 2026-11-15 by the analysis.
  permission: the main loop observes this at the close, as the build's brief assigns.
  figure: the two wall times are DERIVED at the observation.
- **AC4** — When `git show --stat HEAD -- memory/guides/SESSION-KICKOFF.md` runs at the pass commit
  it lists the manifest, and `git log -1 --format=%H -G'^last-audit:' -- memory/guides/SESSION-KICKOFF.md`
  names that same commit.
  Red when: the shell moved and the stamp did not, which the manifest check's staged leg refuses.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kickoff-manifest ratchet` · `verdict epoch (kit version dates the engine)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

The close's bar runs these once, after the last unit. The `memory-hygiene self-test` leg carries
the check 25 arms the analysis names: `tFixture-208`, `tFixture-209` and `tFixture-216`, and the
word-boundary fixtures 218 to 221 for `count_shard`, `tRerun()`, `shard_rows` and `--dry`, at
`tools/memory-tree/check-memory-hygiene.test.sh@4c50ac3a:2047-2068`. Each asserts a red verdict,
so each was seen red when written. The `verdict epoch` leg reads an engine move with no version
move as owed at the lander, not as a red off the push boundary.

This unit adds no arm and moves none. AC1 is its direct observation of the class those arms guard.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

No existing seam fits beyond the one this unit edits. `python tools/codebase-map/reuse_lookup.py
"resolve a by-name token as a whole word in a reader file"` returned generic readers and resolvers
(`read`, `read_text`, `resolve`), none of them an awk matcher. The seam is check 25's own
`test_whole_token` and its END loop in `tools/memory-tree/check-memory-hygiene.sh`, and the unit
adds one short-circuit in front of its one call. The recall probe returned the brief, the build
README, TOOL-dTotalRecall-23's scout on the shell's Python delegations, and the 2026-10-08
`aMeteredSweep` suites research. None of them names this guard. The probes and source agree, except
the line number the analysis cites, which §4 corrects.

Recall terms used: `hygiene check 25 by-name readers test_whole_token corpus_ids walk gotchas selectable print-index-set INDEX_SET ask_shell`
