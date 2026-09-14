# TOOL-dLoggedFlight-4 — the pre-push hook writes one line per push

**Status:** CLOSED · rev-5 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-build-TOOL-dLoggedFlight-4-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-dLoggedFlight-4-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md](../reviews/2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

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
  reads. After the stdin loop it writes a START line in the grammar of `TOOL-dLoggedFlight-1` and
  installs the EXIT trap. The three default-branch refusals at `:95`, `:102` and `:108` run before the
  stdin loop, so each writes one `ev=once` line instead, carrying `decision=refuse-default-branch`,
  the remote fields, `lander` and the worktree, and no START or END. Observed by AC1 and AC7.
- **S2** START carries every ref line from stdin as `ref.<i>=<local-ref> <local-sha> <remote-ref>
  <remote-sha>`, up to 10, with `ref_more=<n>` beyond. It also carries `lander=1` or `lander=0`, always
  written, according to whether the `push-main-active` marker exists in the git dir, and the
  worktree. The stdin loop keeps the ref lines it discards today. Observed by AC1 and AC6.
- **S3** The remote URL is never written, since it can carry credentials. `remote=<name>` is written
  only when `$1` differs from `$2`. A push to a bare URL passes the URL in both, so it writes
  `remote_unnamed=1` instead. Either way the line records `url_userinfo=1` when `$2` holds a `user@`
  part. Observed by AC2.
- **S4** An EXIT trap writes the END line with `rc`, `exit=clean|unclean` and a `decision`. The
  decision is set before each exit after the stdin loop and is one of `skip-nondefault`,
  `skip-delete`, `refuse-manifest`, `refuse-raw`, `refuse-head`, `full` and `scoped`. Every exit after
  the trap is installed sets the clean-exit marker immediately before it. No TERM, HUP or INT trap is
  installed, because a trapped signal waits for the foreground bar, so a killed hook reads
  `exit=unclean`. Observed by AC1 and AC3.
- **S5** When the hook runs the bar, it exports `GATE_RUN_ID` as `push-<epoch digits>-<pid>` and records
  it as `gate_run=` on END, so the push line joins the gate line of `TOOL-dLoggedFlight-3` by id. The
  runner reads that id and then removes it from its environment, before any leg starts. Left there,
  it reaches every leg, and a leg that drives a nested runner, as the runner's own suites do, would
  reuse one run directory for every nested bar it starts. The runner calls per-run uniqueness a
  correctness property, and `TOOL-aQuenchedHarness-11` refused an export of this variable for this
  reason. Observed by AC4.
- **S6** No added process spawn beyond the first-ever `mkdir` of the journal directory. Time is
  `EPOCHREALTIME` and appends are builtin. A failed write changes neither the exit code nor stdout and
  prints one `pre-push: run log` line on stderr. `GOV_RUNLOG=0` turns the lines off. Observed by AC5
  and AC7.
- **S7** A new small suite, `.githooks/pre-push.runlog.test.sh`, with its leg and budget row. It is
  claimed by the `push-main` govkit entry as `project-owned`, with its leg carried by an
  `[[exempt_leg]]` registry row, per TOOL-aQuenchedHarness-3. That row's reason names the entry's
  descriptor, which sits one directory below the kit dir, and the carried-prefix predicate counts a
  file only directly under one. So the `tools/govkit/registry.toml` row of
  `tools/install-prefix-carried.txt` stays at its count, measured by applying that predicate's pattern
  to the registry before and after. A reason naming a counted literal would raise it by hand, per
  TOOL-dRetiredFork-17. `.githooks/pre-push.test.sh` ships to adopters today, and changing that is not
  this unit's. Observed by AC8.

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

The three default-branch refusals come before the stdin loop, so each writes its own `ev=once` line and
exits; the EXIT trap does not exist yet. Every later exit sets `RUNLOG_DECISION` and the clean-exit
marker before it exits, and the EXIT trap reads both. The suite enumerates every `exit` in the hook and
fails on one that maps to no decision and is not one of the two named exemptions.

The hook resolves no git dir before `:157` today, and the lines must be writable on the early skips,
so the builtin resolution is added at `:49`. `GATE_RUN_ID` is an existing seam of the gate runner
(`tools/run-gates/run-gates.sh:1080-1095`), which reuses a pinned id through `mkdir -p`. A time-and-pid
id cannot collide with a live run. It can collide with a NESTED one: the runner scrubs nothing from
its legs' environment, so the export reached every leg, and a runner suite that starts several bars
in one scratch clone would give them all one run directory. The runner therefore removes the
variable once it has read it (S5), one builtin line beside the assignment it feeds.

Every line goes through one append, `write_push_line`, in the grammar's bytes: each value escaped
backslash first, then TAB, LF and CR. A line over the cap is fitted by the runlog kit's reference
rule, the same two steps the gate runner implements. Whole `ref.<i>` fields drop first, highest
index first, into the `ref_more` the count cap may already have written. Only when none is left is
the longest unprotected value cut, never inside a UTF-8 character or an escape. `LC_ALL=C` holds for
that function alone, so a length counts bytes.

### Data model

START: `v t p=pushes ev=start n remote remote_unnamed url_userinfo lander wt ref.1..ref.10 ref_more`.
END: `v t p=pushes ev=end n rc exit decision gate_run`. A pre-loop refusal: `v t p=pushes ev=once
decision remote remote_unnamed url_userinfo lander wt`. Ten refs at about 180 bytes each keep START
under the 2048-byte cap.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `write_push_start`, `write_push_end`, `write_push_once`, `write_push_line`, `render_push_remote`, `resolve_push_dirs` | shell functions | `sh.function`, verb-led |
| `pre-push run-log line` | leg, `repo` / `selftests`, as `pre-push self-test` is | manifest |

`render_push_remote` renders the remote fields of S3 once, and both `write_push_start` and
`write_push_once` call it, so the refusal line cannot carry a weaker guard than START.
`write_push_line` is the one append and the one fit; the three writers only assemble fields.

### Files touched (estimate)

`.githooks/pre-push`, `.githooks/pre-push.runlog.test.sh`, `tools/govkit/entries/push-main.kit.toml`,
`tools/gate-legs.json`, `tools/govkit/{registry.toml,subject-pins.tsv}`,
`tools/run-gates/selftest-budgets.txt`, `tools/run-gates/run-gates.sh` and its README, the runlog
kit's README, and the regenerated map. `.gitattributes` is not touched: its `*.sh` rule already pins
the suite LF, and the hook has its own row. No dossier claims the hook's legs, which sit in the map
baseline, so the new leg is claimed by the runlog dossier, which already names this unit as a
producer. `tools/install-prefix-carried.txt` does not move (S7).

### Alternatives rejected

- A journal line from `tools/push-main.sh`: rejected because it sees only lander pushes, and the push
  worth seeing is the one that bypasses the lander.
- Arms in `.githooks/pre-push.test.sh`: rejected by cost. Its budget row is 1020 s.
- Reading the runner's `gate-run/current` pointer after the bar instead of pinning an id: rejected,
  because another bar in the same clone can move it, and the join must be exact.
- Leaving `GATE_RUN_ID` in the bar's environment: rejected, for the nested-runner reason in S5.

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
  `lander` 0, 1 and 0, and `exit=clean`. A default-branch refusal at `:95` writes one `ev=once` line
  with `decision=refuse-default-branch` and its worktree. Over the whole journal the suite writes,
  every END nonce has a START.
  Red when: the trap misses an early exit, the refs are not recorded, `lander=0` is omitted, or an END
  is unpaired.
- **AC2** — When `bash <suite>` pushes once through a named remote whose URL carries `user:pass@` and
  once to that bare URL, both line pairs carry `url_userinfo=1`, the bare push carries
  `remote_unnamed=1`, and no line contains `pass`. A third push to the credentialed bare URL, with the
  default branch misconfigured so the hook refuses before its stdin loop, writes an `ev=once` line
  carrying `remote_unnamed=1`, `url_userinfo=1` and `lander`. After every arm of the suite, no line of
  the whole journal contains `pass`.
  Red when: `$1` or `$2` reaches any line, the refusal line's remote fields included.
- **AC3** — When the stubbed bar writes a ready file as its first act and then sleeps 20 s, and the
  hook is sent TERM only after that file appears, checked with a bounded poll that also asserts the stub
  is still running, the END reads `exit=unclean` and the hook has exited before the stub's 20 s would
  have elapsed.
  Red when: a TERM trap is added, so the hook outlives the signal until the bar returns.
- **AC4** — When the hook runs the stubbed bar, the stub sees `GATE_RUN_ID` equal to the END line's
  `gate_run`. When the hook runs a copy of the real runner instead, that runner's `gates.log` line
  reads `run=` the END line's `gate_run`, and a leg of that bar sees no `GATE_RUN_ID` at all.
  Red when: the id is not exported, or differs, or the runner leaves it in its legs' environment.
- **AC5** — When the journal directory is a file, the hook's `rc` and stdout are unchanged and stderr
  carries one `pre-push: run log` line. With `GOV_RUNLOG=0` no line is written.
  Red when: a failed write changes the push outcome, or fails silently.
- **AC6** — When `bash <suite>` pushes 21 refs, named short enough that eleven would fit the byte
  cap, START carries `ref.10`, no `ref.11`, `ref_more=11`, and stays at or under 2048 bytes. Names
  long enough that only ten fit would let the byte cap alone write the same fields, so the count cap
  would go unobserved. A START whose ten refs overflow the cap, and one
  whose remote name alone does, are each fitted byte for byte as the runlog kit's `render_line` fits
  them: `ref.<i>` fields drop into `ref_more` first, and a value is cut only once none is left.
  Red when: the cap is not applied, or a value is cut instead.
- **AC7** — When `bash -x` traces the skip-nondefault and full paths from a linked worktree and from a
  primary clone with no `commondir` file, both lines land in `<common-dir>/runlog/pushes.log`, and the
  external-exec count equals the count before the unit.
  Red when: the primary tree finds no journal, or the writer adds a `git` call.
  figure: the exec count is DERIVED at observation time.
- **AC8** — When `GATE_SELFTESTS=1` runs the `pre-push run-log line` leg, it passes at or above
  `FLOOR_ASSERTIONS` inside its budget, and `python tools/govkit/govkit.py selfcheck` is green with
  the suite claimed by the `push-main` entry as `project-owned`.
  Red when: the suite ships to adopters, or is unclaimed or unbudgeted.

## 7. Gates

`pre-push self-test` · `pre-push run-log line` · `push-main self-test` · `run-gates run-log line` · `run-gates canary` · `run-gates evidence` · `testsuite counts (every bar self-test prints one)` · `every held leg is budgeted, every budget row resolves` · `govkit selfcheck` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene`

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
- rev-3 · 2026-09-13 · S1 S4 S7 · §4 · AC1 AC3 AC8 · folded round-2 spec audit H3 (the pre-loop refusals
  write an `ev=once` line, so no END is ever unpaired, and AC1 checks the pairing over the journal),
  M12 (AC3's TERM waits on a ready file the stub writes) and the withholding of the new suite per
  TOOL-aQuenchedHarness-3.
- rev-4 · 2026-09-13 · S7 · §4 · AC2 · folded round-3 spec audit M6 (the refusal line's remote fields
  meet the credential check through one shared renderer) and M10 (the carried-prefix row is raised by
  hand, and the registry is in the write set).
- rev-5 · 2026-09-13 · S5 S7 · §4 · AC4 AC6 · §7 · the build pass, before its code. S5: the runner
  removes `GATE_RUN_ID` once read, because the export reached every leg and a nested runner would
  reuse one run directory, the class the `TOOL-aQuenchedHarness-11` probe design refused the export
  for. S7: the carried-prefix row does not move, since the new reason names a descriptor one
  directory below the kit dir, which the predicate does not count. §4: the one append and its fit,
  and the corrected files list. AC4: the join graded against a real runner copy. AC6: the fit graded
  against `render_line`, and "long-named" refs replaced by refs short enough that the count cap is
  the only thing that can remove `ref.11`, since with long names the byte cap writes the same line.
  §7: the legs of the runner suites the S5 line touches.

## 10. Reuse audit

The seam is the hook's own stdin loop and exit points, found by reading `.githooks/pre-push` whole.
`tools/codebase-map/reuse_lookup.py` cannot see shell. The join to the gate line reuses the runner's
existing `GATE_RUN_ID` seam rather than adding a key. No existing writer records pushes.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
