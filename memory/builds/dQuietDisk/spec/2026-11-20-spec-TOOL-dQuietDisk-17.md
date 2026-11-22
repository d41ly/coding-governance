# TOOL-dQuietDisk-17 — `govkit update` skips a kit's verify check when nothing moved since its baseline

**Status:** SPECCED · rev-3 · 2026-11-22 · node d · Tier-2 · base 609cd40b · streams tooling · order 5 · ratified 2026-11-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md) | research | TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit update --write` runs each touched kit's own `[check]` argv twice: once as a baseline before
the first byte moves, and once in the verify pass after the writes. The analysis counts about 22 kits
at 10 to 16 s each [PINNED], twice (`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`,
row G4). This unit keeps the baseline's result keyed by the kit's installed bytes and a fingerprint
of the target, and reuses it in the verify pass when neither moved and no target-side program ran in
between. Every receipt, write, rollback decision and tally is unchanged. Section 4 says why this
saving is narrow, and section 6 states what it buys.

## 2. Scope (IN)

- **S1** — Beside each baseline call, `update` records the key: the blob ids of the kit's own
  receipt-row paths in the target, read by one `git hash-object --stdin-paths`, and the target
  fingerprint, `HEAD`, the output of `git --no-optional-locks status --porcelain=v2 -z
  --untracked-files=all`, and the blob of every path that status lists. Observed by AC1.
- **S2** — In the verify pass, a kit whose key is unchanged takes the baseline's
  `(state, detail, rc)` as `now` instead of running `run_kit_check`, but only when no target-side
  argv ran since the baseline: no `[[regenerate]]` argv, no step, no default-gained adopter and no
  hole probe. Every decision after it, verified, unverified, pre-existing red, rolled back or
  declined red, reads `now` exactly as today. Observed by AC1 and AC2.
- **S3** — A kit whose key moved, or any run where a target-side argv ran, runs `run_kit_check` in
  the verify pass as today. A key that cannot be read, because a hash or status call failed, reads as
  moved. Observed by AC2 and AC3.
- **S4** — A reused verify announces itself: its verify line gains the tail `· baseline reused: no
  target byte moved and no target program ran since it`, and the closing tally gains `reused <n>`
  beside `verified`. Observed by AC1.
- **S5** — The switch. `install.check-reuse` is read from the target's policy through
  `read_policy_value`, as `update` reads its other `install.*` keys. `reuse`, the default, is S2. `rerun` is today's
  behaviour: every verify runs. The key lands with its catalogue row, `owner = "dQuietDisk"`, a
  `summary` and a `usage`, and `help/reference/policy.md` is re-rendered. Observed by AC4.

## 3. Non-goals (OUT)

- No reuse across invocations. A stored result could outlive a change the target fingerprint cannot
  see, since a kit's check may read the machine outside the target, so a second `update` never reads
  the first one's results.
- No change to `run_kit_check`, to `govkit check`, to the baseline population `touched_kits`, or to
  any rollback rule of DEPL-dCarriedReceipt-14.
- No change to `blob_at` batching, which is TOOL-dQuietDisk-16's.
- No kit version bump by hand.

### Edges

none

## 4. Design

### The two runs today

All citations are read at `609cd40b1`.

`run_kit_check` is the one runner of a kit's `[check]` (`tools/govkit/govkit.py#run_kit_check`). Its
docstring says `update` calls it twice per touched kit. The baseline loop runs it over
`touched_kits`, before the first write (`tools/govkit/govkit.py@609cd40b1:11084`). The verify pass
runs it again per touched kit after the write loop, the regenerate loop, the steps and the
default-gained adopters (`tools/govkit/govkit.py@609cd40b1:12422`), then keys every rollback on the
transition from the baseline to that result.

### Why the reuse is narrow

`touched_kits` is the claimed kits with a snapshotted row, and a row is snapshotted only when its
verdict is one that writes (`tools/govkit/govkit.py@609cd40b1:11073`). So a touched kit's own bytes
almost always move between the two runs, and its verify must run: it is the only measurement of
those writes. The key moves, and S3 runs it. The reuse fires only for a touched kit whose writes did
not land, a held, declined or refused one, in a run that wrote nothing else to the target and ran
no target-side program. The analysis's estimate, the `--check` pass going from two to one, assumed
a key that would skip verifying real writes, which would move a rollback verdict.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `install.check-reuse` | policy key, values `reuse` and `rerun` | the catalogue's row | AC4 |
| `derive_check_key` | function in `govkit.py` | none | AC1, AC3 |
| `reused` | a field of the verify tally line | none | AC1 |

### Files touched (estimate)

`tools/govkit/govkit.py` · `tools/govkit/selftest.py` · `tools/policy/catalogue.toml` · `help/reference/policy.md`

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Key on the kit's own paths alone | A kit's check reads files other kits write, so a verify skipped because its own bytes held could miss a break another kit's write caused. |
| Persist results for the next `update` | Section 3: a check may read the machine outside the target, which no fingerprint holds. |
| Skip silently | govkit's verify pass announces every skip (its S8 comment), so a reused result reading as a run would claim a measurement nobody made. |

## 5. Production-readiness checklist

- security: N/A — reads of the target the verb already writes; nothing new is written.
- perf / scale: one `hash-object` and one `status` per touched kit, saved against a check of 10 to
  16 s [PINNED] only where the reuse fires.
- error / empty / loading states: an unreadable key reads as moved and the check runs (S3).
- observability: the announced tail and the tally field (S4).
- risks: a fingerprint that misses a change the check reads. The rule that any target-side program
  disables the reuse is the defence; AC2 plants one.
- testing: fixture updates on `tools/govkit/fixtures/` (AC1 to AC3) and the switch (AC4).
- migration: none.
- user docs: `help/reference/policy.md` (S5).

## 6. Acceptance criteria

The saving the reuse buys, stated as a count. Each reused verify saves exactly one `run_kit_check`
call, the kit's own `[check]` argv and every process it starts, which the analysis puts at 10 to 16 s [PINNED]
(row G4, PINNED 2026-11-20). The run's saving is the `reused <n>` field of the tally, so `n` calls.
It costs §5's one `hash-object` and one `status` per touched kit, at the baseline and again in
verify, whether or not the reuse fires. On an ordinary version-bump update every touched kit's
writes land, every key moves, `n` is 0, and the unit saves nothing and costs those reads. It pays
back only on an update that holds, declines or refuses a touched kit's writes and runs no
target-side program, where it saves one kit check per such kit.

- **AC1** — When `python tools/govkit/govkit.py update --target <fixture> --write` runs on an adopter
  fixture built from `tools/govkit/fixtures/release-0` where one touched kit's only row is held back,
  that kit's verify line carries the `baseline reused` tail, the tally reads `reused 1`, and the
  receipt, the target's files and the exit equal those of the same run under
  `install.check-reuse = "rerun"`.
  Red when: the reused kit's state differs from a run that re-checks it, or the reuse is silent.
  fixture: built by govkit's own fixture factory in a scratch directory under `%TEMP%`.
  figure: the saving is the tally's `reused 1`: one `run_kit_check` call fewer than the `rerun` run,
  which reuses none, makes. DERIVED at observation from the two runs' tallies.
- **AC2** — When the same fixture's update also runs a `[[regenerate]]` argv, no verify is reused,
  and the output equals the `rerun` run's.
  Red when: a target-side program ran and a baseline was still reused.
- **AC3** — When a touched kit's write lands, its verify runs, and when the status call is made to
  fail by a stub on `PATH`, every verify runs.
  Red when: a moved key or an unreadable key reuses the baseline.
- **AC4** — When `python tools/policy/policy.py get install.check-reuse` runs with no policy file, it
  prints `reuse`, and under `rerun` the AC1 run's verify lines carry no reuse tail.
  Red when: the default is not `reuse` or `rerun` does not restore today's behaviour.
- **AC5** — When `python tools/govkit/govkit.py check --target C:/projects/incms/main` and the same for
  `C:/projects/nicocares/main` run read-only from gov before and after this unit, each prints the
  same lines and exits the same.
  Red when: an adopter's check reading moves.
  permission: both are read and never written; nothing runs in either `gov-upgrade` worktree.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy check` · `policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `recall floor arms` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · an update over a fixture with a held-back kit, then with a regenerate argv, then with a landed write; its failing case is staged by reusing the baseline whatever the key says · none

## 8. Open questions

- **F1** — Build the within-run reuse, whose saving section 4 shows is confined to touched kits whose
  writes did not land, or retire the unit?
  - (a) Build S1 to S5 as written. Every criterion here holds, and on an ordinary version-bump update
    the reuse rarely fires, so the measured saving is small.
  - (b) Retire the unit, `WONTDO`, with section 4 as its reason, and file the cross-invocation reuse
    as an ask for the owner, since a stored check result can outlive a change outside the target.
  - Recommendation: (b). The charter's YAGNI rule is level 0 and a skip that seldom fires is
    machinery for its own sake; M3's feature-rich rule would pick (a), so the resolver should weigh
    the two openly.
  - RESOLVED (agent, 2026-11-20, delegated): (a), build S1 to S5 as written. It is the most
    feature-rich option, it is what the owner's prompt asked for, and P18 ranks the decision rule
    above the YAGNI practice in an unattended fork; section 6 states the saving it buys.

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Ordered 5, not the brief's 2: `tools/govkit/govkit.py` is
  written by TOOL-dQuietDisk-16 at order 1 and TOOL-dQuietDisk-18 at order 3, and every order-2 and
  order-4 sibling whose acceptance installs kits through govkit reads it, so this unit runs alone
  after them.
- rev-2 · 2026-11-20 · §1 · §6 · AC1 · §8 · F1 resolved (a) under
  `2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task`: S1 to S5 are built as written, and §6 now states
  the saving the narrow reuse buys, with a `figure:` line on AC1.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  1, section 5 and section 6 the analysis's per-kit check time is marked PINNED on each line that
  quotes it. Design, scope and acceptance unchanged.

## 10. Reuse audit

The seam extended is the verify pass's own baseline map, `baseline`, and `run_kit_check`, the one
runner of a kit's check (`tools/govkit/govkit.py#run_kit_check`), whose docstring forbids a second
implementation; this unit adds none and reuses its triple. The switch reads through
`read_policy_value` (`tools/govkit/govkit.py#read_policy_value`), the reader `update` already uses for
its `install.*` keys.
The chain build owning the area is dSafePassage (Supersession: govkit update and apply); its CLOSED
units 5, 10 and 25 to 27 leave the verify pass's transition rule as DEPL-dCarriedReceipt-14 wrote it,
and this unit keeps it.

`python tools/codebase-map/reuse_lookup.py "skip re-running an adopter check when nothing moved since the baseline"`
returned name-token neighbours only (`check`, `skip`, `adopt`, `checks`). Recall returned
DEPL-cMendedVintage-29, DEPL-dSealedTally-4 and DEPL-cMendedVintage-1, which shaped the verify pass's
exits, and TOOL-dPolishedVitrine-12. The source agreed; none proposes a reuse.

Recall terms used: run_kit_check baseline verify touched_kits adopt check rollback transition update pre-existing red
