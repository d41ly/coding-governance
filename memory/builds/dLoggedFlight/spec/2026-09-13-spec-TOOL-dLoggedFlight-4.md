# TOOL-dLoggedFlight-4 — the pre-push hook writes one line per push

**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing records a push today. A raw branch push published a private file from another repo into this
public one, and a run pushed its branch outside the lander, and neither left a record here. Make the
pre-push hook, which git runs for every push that is not `--no-verify`, write a start and an end line
to `pushes.log`, and pin the bar's run id so a push joins to its gate line exactly.

## 2. Scope (IN)

- **S1** After the stdin loop, the hook writes a START line in the grammar of `TOOL-dLoggedFlight-1`.
  It carries the remote NAME from `$1`, every ref line from stdin as `ref.<i>=<local-ref> <local-sha>
  <remote-ref> <remote-sha>` (up to 20, with `ref_more=<n>` beyond), `lander=1` when
  the `push-main-active` marker exists in the git dir, and the worktree. The stdin loop keeps the ref
  lines it discards today. Observed by AC1.
- **S2** The remote URL is never written, since it can carry credentials. The line records
  `url_userinfo=1` when `$2` holds a `user@` part. Observed by AC2.
- **S3** An EXIT trap writes the END line with `rc` and a `decision` set before each exit. The
  decisions are `skip-nondefault`, `skip-delete`, `refuse-manifest`, `refuse-raw`, `refuse-head`,
  `full` and `scoped`. TERM, HUP and INT exit `128+n` so the END reads the real status. Observed by
  AC1 and AC3.
- **S4** When the hook runs the bar, it exports `GATE_RUN_ID` as `push-<epoch digits>-<pid>` and records
  it as `gate_run=` on END, so the push line joins the gate line of `TOOL-dLoggedFlight-3` by id.
  Observed by AC4.
- **S5** No added process spawn. Time is `EPOCHREALTIME`, the common dir is resolved with builtin reads
  from the git dir the hook already resolves, and appends are builtin. A failed write changes neither
  the exit code nor stdout, and `GOV_RUNLOG=0` turns the lines off. Observed by AC5.
- **S6** A new small suite, `.githooks/pre-push.runlog.test.sh`, shipped through the `push-main`
  govkit entry beside `.githooks/pre-push.test.sh`, with its leg and budget row. Observed by AC6.

## 3. Non-goals (OUT)

- A pre-push act is not a push. Git fires the hook for a `--dry-run`, and for a push the remote later
  rejects. The line records an ATTEMPT and its `rc`; whether it landed is git's answer.
- A `--no-verify` push runs no hook and leaves no line. The lander never passes it, and the unattended
  close path greps for it. Detecting one afterwards is out of scope.
- No change to any gating decision or refusal the hook makes.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-1` — the line grammar and the journal location contract.
- **hands-off** `TOOL-dLoggedFlight-8` — the run model joins pushes to a run and flags pushes outside
  the lander.

## 4. Design

The hook reads refs at `.githooks/pre-push:115-117` and keeps only the default-branch local sha. The
loop gains an array of every ref line. The gating exits are `:119`, `:120`, `:140-150`, `:157-160`
and `:164-169`, plus the bar's pass-through `exit "$rc"`. Each sets `RUNLOG_DECISION` before it
exits, and the EXIT trap reads it.

The hook already resolves `$(git rev-parse --git-dir)` at `:157` and `:202`. The common dir comes from
that value's `commondir` file, read with builtin `read`, so no git call is added. `GATE_RUN_ID` is an
existing seam of the gate runner (`tools/run-gates/run-gates.sh:1080-1095`), which reuses a pinned id
through `mkdir -p`. A time-and-pid id cannot collide with a live run.

### Data model

START: `v t p=pushes ev=start n remote url_userinfo lander wt ref.1..ref.20 ref_more`. END:
`v t p=pushes ev=end n rc decision gate_run`.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `write_push_start`, `write_push_end` | shell functions | `sh.function`, verb-led |
| `pre-push run-log line` | leg, `repo` / `selftests`, as `pre-push self-test` is | manifest |

### Files touched (estimate)

`.githooks/pre-push`, `.githooks/pre-push.runlog.test.sh`, `tools/govkit/entries/push-main.kit.toml`,
`.gitattributes`, `tools/gate-legs.json`, `tools/govkit/subject-pins.tsv`,
`tools/run-gates/selftest-budgets.txt`, the dossier that claims the hook's legs, and the regenerated map.

### Alternatives rejected

- A journal line from `tools/push-main.sh`: rejected because it sees only lander pushes, and the push
  worth seeing is the one that bypasses the lander.
- Arms in `.githooks/pre-push.test.sh`: rejected by cost. Its budget row is 1020 s.

## 5. Production-readiness checklist

- security — no URL, so no credential. Ref names and shas are what the push publishes anyway.
- perf / scale — zero added spawns in a hook that then runs a bar of minutes.
- error / empty / loading states — an empty stdin writes a START with no refs and an END with
  `decision=skip-nondefault`.
- observability — a push with no END is a hook that was killed.
- risks — `core.hooksPath` is absolute, so a push from any worktree runs the PRIMARY tree's copy of
  the hook. Lines appear only once the primary tree has this change, which the rollout states.
- testing — the new suite stages each AC RED before landing.
- migration — none. Adopters take the hook through the `push-main` entry on their next update.
- user docs — the hook header and the runlog kit README.

## 6. Acceptance criteria

`<suite>` below is `.githooks/pre-push.runlog.test.sh`, which this unit creates. It builds a bare
remote and a work clone the way `.githooks/pre-push.test.sh` does, with the bar stubbed through
`GOV_GATE_CMD`.

- **AC1** — When `bash <suite>` pushes a feature branch, then the default branch with the marker and a
  green stub, then the default branch with no marker, `pushes.log` holds three START and END pairs.
  Their decisions are `skip-nondefault`, `full` or `scoped`, and `refuse-raw`, with `rc` 0, 0 and 1.
  Red when: the trap misses an early exit, or the refs are not recorded.
- **AC2** — When the remote URL carries `user:pass@`, the lines carry `url_userinfo=1` and neither
  line contains `pass`.
  Red when: `$2` reaches the line.
- **AC3** — When the stubbed bar sleeps and the hook is sent TERM, the END reads `rc=143`.
  Red when: the signal traps are removed.
- **AC4** — When the hook runs the stubbed bar, the stub sees `GATE_RUN_ID` equal to the END line's
  `gate_run`.
  Red when: the id is not exported, or differs.
- **AC5** — When the journal directory is a file, the hook's `rc` and stdout are unchanged, and with
  `GOV_RUNLOG=0` no line is written.
  Red when: a failed write changes the push outcome.
- **AC6** — When `GATE_SELFTESTS=1` runs the `pre-push run-log line` leg, it passes at or above
  `FLOOR_ASSERTIONS` inside its budget, and `python tools/govkit/govkit.py selfcheck` is green with
  the suite claimed by the `push-main` entry.
  Red when: the suite ships unclaimed or unbudgeted.

## 7. Gates

`pre-push self-test` · `push-main self-test` · `testsuite counts (every bar self-test prints one)` · `every held leg is budgeted, every budget row resolves` · `govkit selfcheck` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene`

New arm: `.githooks/pre-push.runlog.test.sh` · each AC staged RED by removing the property it observes · floor set at landing

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seam is the hook's own stdin loop and exit points, found by reading `.githooks/pre-push` whole.
`tools/codebase-map/reuse_lookup.py` cannot see shell. The join to the gate line reuses the runner's
existing `GATE_RUN_ID` seam rather than adding a key. No existing writer records pushes.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
