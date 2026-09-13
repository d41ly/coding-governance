# TOOL-dLoggedFlight-4 — the pre-push hook writes one line per push

**Status:** SPECCED · rev-2 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 4

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

- **S1** Right after `cd "$top"` at `.githooks/pre-push:49`, the hook resolves its git dir from
  `$top/.git`, a directory or the `gitdir:` line of a file, and its common dir as
  `<git-dir>/<commondir contents>` when that file exists, else the git dir itself. Both use builtin
  reads. After the stdin loop it writes a START line in the grammar of `TOOL-dLoggedFlight-1`. Observed
  by AC1 and AC7.
- **S2** START carries every ref line from stdin as `ref.<i>=<local-ref> <local-sha> <remote-ref>
  <remote-sha>`, up to 10, with `ref_more=<n>` beyond. It also carries `lander=1` or `lander=0`, always
  written, according to whether the `push-main-active` marker exists in the git dir, and the
  worktree. The stdin loop keeps the ref lines it discards today. Observed by AC1 and AC6.
- **S3** The remote URL is never written, since it can carry credentials. `remote=<name>` is written
  only when `$1` differs from `$2`. A push to a bare URL passes the URL in both, so it writes
  `remote_unnamed=1` instead. Either way the line records `url_userinfo=1` when `$2` holds a `user@`
  part. Observed by AC2.
- **S4** An EXIT trap writes the END line with `rc`, `exit=clean|unclean` and a `decision`. The
  decision is set before each exit and is one of `skip-nondefault`, `skip-delete`,
  `refuse-default-branch`, `refuse-manifest`, `refuse-raw`, `refuse-head`, `full` and `scoped`. Every
  exit after `:49` sets the clean-exit marker immediately before it. No TERM, HUP or INT trap is
  installed, because a trapped signal waits for the foreground bar, so a killed hook reads
  `exit=unclean`. Observed by AC1 and AC3.
- **S5** When the hook runs the bar, it exports `GATE_RUN_ID` as `push-<epoch digits>-<pid>` and records
  it as `gate_run=` on END, so the push line joins the gate line of `TOOL-dLoggedFlight-3` by id.
  Observed by AC4.
- **S6** No added process spawn beyond the first-ever `mkdir` of the journal directory. Time is
  `EPOCHREALTIME` and appends are builtin. A failed write changes neither the exit code nor stdout and
  prints one `pre-push: run log` line on stderr. `GOV_RUNLOG=0` turns the lines off. Observed by AC5
  and AC7.
- **S7** A new small suite, `.githooks/pre-push.runlog.test.sh`, shipped through the `push-main`
  govkit entry beside `.githooks/pre-push.test.sh`, with its leg and budget row. Observed by AC8.

## 3. Non-goals (OUT)

- A pre-push act is not a push. Git fires the hook for a `--dry-run`, and for a push the remote later
  rejects. The line records an ATTEMPT and its `rc`; whether it landed is git's answer.
- A `--no-verify` push runs no hook and leaves no line. The lander never passes it, and the unattended
  close path greps for it. Detecting one afterwards is out of scope.
- The two refusals before any root is known, `:47` (no top level) and `:51` (cannot `cd` to it), can
  write no line, because no journal root exists yet.
- No change to any gating decision, refusal, or signal behaviour the hook has.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-1` — the line grammar and the journal location contract.
- **hands-off** `TOOL-dLoggedFlight-8` — the run model joins pushes to a run and flags pushes outside
  the lander.

## 4. Design

The hook reads refs at `.githooks/pre-push:115-117` and keeps only the default-branch local sha. The
loop gains an array of every ref line. Its exits are:

- `:95`, `:102` and `:108`, the default-branch refusals, which are `refuse-default-branch`;
- `:119` and `:120`, the skips;
- `:140-150`, `:157-160` and `:164-169`, the refusals;
- the bar's pass-through `exit "$rc"`, whose decision is `full` or `scoped`, with the marker set only
  after the bar returns.

Each sets `RUNLOG_DECISION` and the clean-exit marker before it exits, and the EXIT trap reads both.
The suite enumerates every `exit` in the hook and fails on one that maps to no decision and is not one
of the two named exemptions.

The hook resolves no git dir before `:157` today, and the lines must be writable on the early skips,
so the builtin resolution is added at `:49`. `GATE_RUN_ID` is an existing seam of the gate runner
(`tools/run-gates/run-gates.sh:1080-1095`), which reuses a pinned id through `mkdir -p`. A time-and-pid
id cannot collide with a live run.

### Data model

START: `v t p=pushes ev=start n remote remote_unnamed url_userinfo lander wt ref.1..ref.10 ref_more`.
END: `v t p=pushes ev=end n rc exit decision gate_run`. Ten refs at about 180 bytes each keep START
under the 2048-byte cap.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `write_push_start`, `write_push_end`, `resolve_push_dirs` | shell functions | `sh.function`, verb-led |
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

- security — no URL, so no credential, on both the named-remote and the bare-URL form (AC2). Ref names
  and shas are what the push publishes anyway.
- perf / scale — zero added spawns in a hook that then runs a bar of minutes (AC7).
- error / empty / loading states — an empty stdin writes a START with no refs and an END with
  `decision=skip-nondefault`.
- observability — a push with no END is a hook that was killed; `exit=unclean` is one that was
  signalled.
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
  Their decisions are `skip-nondefault`, `full` or `scoped`, and `refuse-raw`, with `rc` 0, 0 and 1,
  `lander` 0, 1 and 0, and `exit=clean`. A default-branch refusal at `:95` writes
  `decision=refuse-default-branch`.
  Red when: the trap misses an early exit, the refs are not recorded, or `lander=0` is omitted.
- **AC2** — When `bash <suite>` pushes once through a named remote whose URL carries `user:pass@` and
  once to that bare URL, both line pairs carry `url_userinfo=1`, the bare push carries
  `remote_unnamed=1`, and no line contains `pass`.
  Red when: `$1` or `$2` reaches the line.
- **AC3** — When the stubbed bar sleeps 20 s and the hook is sent TERM after one second, the END reads
  `exit=unclean` and the hook has exited before the stub's 20 s would have elapsed.
  Red when: a TERM trap is added, so the hook outlives the signal until the bar returns.
- **AC4** — When the hook runs the stubbed bar, the stub sees `GATE_RUN_ID` equal to the END line's
  `gate_run`.
  Red when: the id is not exported, or differs.
- **AC5** — When the journal directory is a file, the hook's `rc` and stdout are unchanged and stderr
  carries one `pre-push: run log` line. With `GOV_RUNLOG=0` no line is written.
  Red when: a failed write changes the push outcome, or fails silently.
- **AC6** — When `bash <suite>` pushes 21 long-named refs, START carries `ref.10`, no `ref.11`,
  `ref_more=11`, and stays at or under 2048 bytes.
  Red when: the cap is not applied, or a value is cut instead.
- **AC7** — When `bash -x` traces the skip-nondefault and full paths from a linked worktree and from a
  primary clone with no `commondir` file, both lines land in `<common-dir>/runlog/pushes.log`, and the
  external-exec count equals the count before the unit.
  Red when: the primary tree finds no journal, or the writer adds a `git` call.
  figure: the exec count is DERIVED at observation time.
- **AC8** — When `GATE_SELFTESTS=1` runs the `pre-push run-log line` leg, it passes at or above
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
- rev-2 · 2026-09-13 · S1 S2 S3 S4 S6 · §3 · §4 · AC1 AC2 AC3 AC5 AC6 AC7 · folded round-1 spec audit
  H2 (git and common dirs resolved at `:49` with a primary-tree fallback), H5 (a bare-URL push passes
  the URL as `$1`, so `remote` is written only when it differs), M3 (`lander` is always written), M4
  (ten refs, not twenty, fit the cap), M13 (the default-branch refusals get a decision, and `:47` and
  `:51` are named as unloggable), M17 (the stderr line) and M18 (no signal traps; a clean-exit marker
  instead).

## 10. Reuse audit

The seam is the hook's own stdin loop and exit points, found by reading `.githooks/pre-push` whole.
`tools/codebase-map/reuse_lookup.py` cannot see shell. The join to the gate line reuses the runner's
existing `GATE_RUN_ID` seam rather than adding a key. No existing writer records pushes.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
