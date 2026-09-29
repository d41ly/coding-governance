# TOOL-dDerivedDocket-65 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-65

A session waiting on its own sub-agents is now a move. `derive_last_move` gains a last term after
its transcript term. It strips `.jsonl` from the derived transcript path, globs every
`agent-*.jsonl` at any depth under that directory's `subagents/` with `globstar` restored to the
state it was found in, and dates the whole list with one `stat -c %Y` spawn. The readings are split
by default word splitting, never a here-string, and a reading newer than the newest move so far wins
with source `subagent`. No transcript, no directory and no match contribute nothing. Fewer readings
than matched paths sets the dead probe `stat -c %Y over <dir>`, which check 52 already refuses on.
The driver's `--liveness` header, the comment above `derive_last_move`, the term's own comment and
the signals comment in `print_liveness` name the term, its population, the one bound and the
run-log kit's session reader by role. No key, function, `fail` branch, pinned ordinal, version, conf
key or capped carrier moved. The `unattended` dossier gained one clause and reads 20446 bytes
against its 20480 cap.

The suites gained their arms and nothing ran them. The driver suite has 15 assertions in the
`--liveness` signals block after its transcript arm and 8 after unit 64's AC2 arm, all in region
two. So `FLOOR_ASSERTIONS` rose 1736 to 1759 and `FLOOR_SHARD_2` 1540 to 1563, with
`FLOOR_SHARD_1` unmoved. The resume-tick suite has 3 after the U64 block, so its floor rose 176 to
179. Each count is taken off the block's own assertion lines.

No merge bar, no gate leg and no `*.test.sh` suite ran in this pass. The direct checks were these.
§4's fixture was run through the driver and `resume-tick.sh --dry-run`, against this unit's kit and
against a copy whose `derive_last_move` lacks the sub-agent term. Each new suite block was run alone
behind a replica of its own suite's prologue, with `HERE` pointed at a kit copy. The driver replica
ran the signals block from n 20 to 60, its 25 existing assertions and the 15 new ones, and the AC2
block's 8, all green. Under the term-less copy 17 of the 23 new assertions went red. The tick arm was
3 of 3 green, and 2 red under that copy.

AC2, AC3, AC5 and AC6 carry `permission:` lines, so none gets a line here. Their direct checks ran
all the same. For AC3, the fixture's dry-run printed `skip · verdict LIVE` with the sub-agent
transcript fresh and `resumed · attempt 1` with it dated 2000-01-01. The term-less copy printed
`resumed · attempt 1` for both. For AC6, the version marker reads 1. The function count (199) and
the driver's `fail` count (289) equal the parent's. The sub-agent comment grep reads 4. The added
lines carry no `tools/<kit>/` literal. `scan_file` of the shell-hygiene leg reports the same site
counts at the parent and in the edited driver, three `<<<` sites each, and the same for both
suites. The unit names no function, so no lexicon answer is owed.

**Evidences:** TOOL-dDerivedDocket-65
- AC1 — `last-move-source: subagent` — over §4's fixture, with a 5400 s bound, session `S65`, the
  commit and `S65.jsonl` dated 2000-01-01, `--liveness` printed `last-move-source: commit`,
  `stale: yes` and `verdict: STALE` with no sub-agent file. With one `agent-a1.jsonl` touched now
  under `S65/subagents/workflows/wf_x/` it printed `subagent`, `stale: no` and `verdict: LIVE`, on
  the same keys in the same order. The same held directly under `S65/subagents/` and one directory
  deeper than `wf_x/`. Dated 2000-01-01 by `touch -d` it read `commit`, `stale: yes` and
  `verdict: STALE`, and so did a fresh file under another session's `T/subagents/workflows/wf_x/`.
  With a `stat` stub dropping the last of two matched paths, the call exited 1 at check 52 naming
  `stat -c %Y over <config>/projects/<enc>/S65/subagents`, with no `verdict:` line. The term-less
  copy read `commit` and `stale: yes` with every fresh file, and printed `verdict: STALE` under
  the stub.
- AC2 — amended rev-3 — the arm in `tools/unattended/unattended.test.sh` is waived: the owner
  ruled on 2026-09-29 that the unattended kit's own self-test suites are not run for this landing,
  so the attributed run the permission line named is not made and the criterion stays unobserved.
  Section 9 rev-3 logs the amendment. The block's 8 assertions ran once behind a replica prologue
  in the build pass, as the prose above records; that is not the suite run and is not claimed as
  it.
- AC3 — amended rev-3 — the arm in `tools/unattended/resume-tick.test.sh` is waived: the owner
  ruled on 2026-09-29 that the unattended kit's own self-test suites are not run for this landing,
  so that arm stays unobserved. Section 9 rev-3 logs the amendment. The fixture half stands
  observed as the build pass's direct check recorded above: `resume-tick.sh --dry-run` printed
  `skip · verdict LIVE` with the sub-agent transcript fresh and `resumed · attempt 1` with it
  dated 2000-01-01, and the term-less copy printed `resumed · attempt 1` for both.
- AC4 — `grep -cF '/**/agent-*.jsonl'` — printed 1 over the driver, and
  `grep -cE '^[^#]*subagents'` printed 1, the one line deriving the directory from the transcript
  path. The count of `grep -cF "'----'"` read 1 at the parent and 1 at the build.
- AC5 — amended rev-3 — the attributed run over `tools/unattended/unattended.test.sh` and the
  resume-tick suite is waived: the owner ruled on 2026-09-29 that the unattended kit's own
  self-test suites are not run for this landing, so the verdict half stays unobserved. Section 9
  rev-3 logs the amendment. The floor half stands observed, read on 2026-09-29 with `git show`:
  the driver suite's `FLOOR_ASSERTIONS` reads 1736 at the first parent e0643748 and 1759 at the
  build commit 5491f7bc, `FLOOR_SHARD_2` 1540 and 1563, `FLOOR_SHARD_1` 208 at both, and the
  resume-tick suite's `FLOOR_ASSERTIONS` 176 and 179. Those deltas, 23 and 3, are the counts the
  build pass took off the new arms' blocks, as the prose above records.
- AC6 — `grep -c 'KIT_UNATTENDED_VERSION=1.29' tools/unattended/unattended.sh` — printed 1 at the
  build commit 5491f7bc, as at its parent e0643748. Over the driver, `git diff -U0` adds no line
  spelling a `tools/<kit>/` literal; the function-definition and `fail` counts read 199 and 289 at
  both commits; `grep -cE '^ *#.*sub-agent transcript'` reads 4; `git diff --name-only` names the
  driver, its two suites, the unattended dossier and build records only; and `scan_file` of
  `tools/gate-lint/sh_hygiene.py` reports 3 gated `<<<` sites at both commits. At 364278a8 the
  `install-prefix (shipped surface)` leg printed `install-prefix: clean — 322 shipped files`,
  `harness arms (fail branches armed or pinned)` exited 0, silent, and
  `shell hygiene (a loop fed by a command substitution)` printed
  `sh-hygiene: OK — 61 declared site(s) in 46 row(s)`.
