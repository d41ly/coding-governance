# TOOL-aTimedTurnstile-2 — diff-scope the self-test legs, keep the push boundary full

**Status:** CLOSED · rev-2 · 2026-08-20 · node a · Tier-2 · base af6de231 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

29 of the 47 legs are self-tests holding 96.7% of the bar's wall clock, and only one leg carries a
`guard`. A self-test proves its engine works, so its verdict depends on its own code and not on the
repo's data — it need not re-run when neither moved. Guard them, and make the push boundary force
every leg so the authoritative run stays full.

## 2. Scope (IN)

- **S1** — add a `guard` to each of the 29 self-test legs in `tools/gate-legs.json`, keyed on the kit
  directory that holds the test and its engine, plus any path the leg genuinely compares against.
- **S2** — add `GATE_FULL`: when set, `changed()` returns "run" for every leg, so guards are bypassed
  wholesale.
- **S3** — `.githooks/pre-push` sets `GATE_FULL=1`, so the authoritative full-bar run is unchanged by
  S1 and no guard can weaken it.
- **S4** — a manifest check: every `guard` path must match at least one TRACKED path. A guard naming a
  path that does not exist never reports a diff, so the leg skips forever and silently.
- **S5** — arms for the skip/run/force behaviours, and for S4.
- **S6** — record the new posture in `AGENTS.md` and the kickoff manifest's gate-command block.

## 3. Non-goals (OUT)

- Guarding the 18 legs that check this repo's actual state. They cost 12.7s combined and their inputs
  are the repo's own data, which is exactly what a scoped run is scoping.
- Making any individual leg faster. That remains `TOOL-aTimedTurnstile-3`.
- Changing what any leg asserts.

## 4. Design

### Data model

A `guard` is a list of pathspecs already understood by `run-gates.sh`: the leg runs when
`git diff --quiet <BASE> -- <paths>` reports a difference, and skips otherwise. `BASE` is the mainline
tip. Two existing fail-safes are load-bearing and unchanged: an unresolvable `BASE` runs everything,
and a guard evaluation error runs the leg.

### Inventory

The guard for a self-test is the directory holding it, because a self-test is hermetic — it builds its
own `mktemp` fixture tree rather than reading the repo's data. Six legs compare against something
outside their own kit and carry that path too:

| Leg | Extra guard beyond its kit dir | Why |
|---|---|---|
| python resolver | `tools/` | asserts every kit carries the resolver inline byte-identical, and bans the retired idiom repo-wide |
| install-prefix self-test | `tools/` | the gate's kit-name alternation is derived from the tracked `tools/*` dirs |
| kit/dogfood doc parity | `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` | compares the shipped templates against this repo's installed copies |
| review-protocol parity | `memory/guides/REVIEW-PROTOCOL.md` | same shape, one directory over |
| unattended gate selftest | `memory/guides/UNATTENDED-PROTOCOL.md` | the shipped protocol must equal the installed one |
| check-wiring self-test | `.claude/` | the wiring it checks lives there |

`tools/lib/` is added to every self-test's guard: it holds the one python resolver every kit inlines,
so a change there can move any leg's verdict.

### Rollout

The safety property that makes this change tractable, stated plainly: **a guard can only affect a
NON-authoritative run.** `.githooks/pre-push` forces `GATE_FULL=1`, so a guard that is too narrow
costs an early signal and can never produce a wrong merge verdict. This is why erring wide is cheap
and erring narrow is survivable — but S4 exists because the quietest hole is a guard that never
matches anything at all.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/gate-legs.json` | 29 `guard` keys |
| `tools/run-gates.sh` | `GATE_FULL` in `changed()` |
| `.githooks/pre-push` | export `GATE_FULL=1` |
| `tools/run-gates.test.sh` | S4 check, S5 arms |
| `AGENTS.md`, `.claude/SESSION-KICKOFF.md` | the posture |

### Alternatives rejected

- **Honouring guards at the push boundary too.** It is the faster option and it is wrong: `AGENTS.md`
  calls that run the full bar, and a diff-scoped authoritative run means no run ever executes every
  leg against the tree that lands.
- **Deriving guards mechanically from each script's referenced paths.** Attempted first. Nearly every
  script mentions `tools/` in prose, so the derivation collapsed to "guard everything on everything"
  and the guards stopped discriminating. An explicit table is auditable; a derivation that over-matches
  is not.

## 5. Production-readiness checklist

- security — a guard can only reduce what a NON-authoritative run checks; `GATE_FULL=1` at the push
  boundary is the invariant that keeps the merge verdict total.
- perf / scale — the point: a records-only commit drops from 47 legs to 18.
- a11y — N/A, a shell gate runner has no user interface.
- i18n — N/A, output is developer-facing English.
- error / empty / loading states — an unresolvable `BASE` still runs every leg; a guard naming an
  untracked path is refused by S4 rather than silently skipping.
- observability — every skipped leg already prints `GATE skip … (unchanged vs …)`.
- risks (concurrency, data-loss, rollback hazards) — the failure mode is a too-narrow guard hiding a
  regression from an early run. Bounded by S3. Rollback is deleting the `guard` keys.
- testing + left-shift gates — S4 and S5; S4 is the mechanical one that outlives this unit.
- migration / rollback — none; `guard` is an existing manifest key.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When a commit touches only `memory/*.md`, the bar runs the 18 state gates and skips the 29
  self-tests, and still exits 0.
- **AC2** — When a commit touches a kit directory, that kit's self-tests run and the others skip.
- **AC3** — When `GATE_FULL=1` is set, every leg runs regardless of any guard.
- **AC4** — When a leg's `guard` names a path matching no tracked file, the manifest check reds.
- **AC5** — When `.githooks/pre-push` runs the bar, it runs with `GATE_FULL` set.
- **AC6** — When `BASE` cannot be resolved, every guarded leg still runs.

## 7. Gates

`run-gates canary` carries the new checks. `memory hygiene (19 checks)` covers this spec.
`pre-push self-test` covers S3. The whole bar runs at the DoD under `GATE_FULL=1`, since a scoped run
is by construction not a full verification.

## 8. Open questions

none — the one fork (whether the push boundary honours guards) is resolved in §4 Rollout and its
rejected alternative, on the grounds that `AGENTS.md` defines that run as the full bar.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft, written against the measurement in commit f638d8b and the
  runner delivered by TOOL-aTimedTurnstile-5.
- rev-2 · 2026-08-20 · CLOSED, on a status audit run during the aPacedTurnstile re-scope. Every scope
  item of this unit is in the tree and has been for some time: `tools/gate-legs.json` carries a
  `guard` on 50 of its 86 legs (S1), `run-gates.sh` implements `GATE_FULL` (S2), `.githooks/pre-push`
  exports it (S3), and the guard-must-name-a-tracked-path refusal is armed in the shipped canary,
  which checks against `git ls-files` rather than the filesystem because a guard is a pathspec git
  resolves (S4). The unit shipped and nobody moved the status word, which is the closed-plan-with-no-
  status-move class this repo's own drift audit hunts. What the audit found FIRST was the cost of
  leaving it open: a sibling survey reported this unit as a BLOCKER on `TOOL-aPacedTurnstile-7`,
  because a non-terminal spec asserting "the push boundary stays full" is a live second owner of a
  property another build is about to retire. It was never a design conflict, only an unclosed record.
  S3 is now SUPERSEDED by `TOOL-aPacedTurnstile-7`, which makes the push boundary decide rather than
  force. Superseded, not rewritten: this unit's decision was correct when it was taken and is the
  reason the property existed to be replaced.

## 10. Reuse audit

No lookup needed and none performed: the seam already exists and this unit only populates it. `guard`
is an existing key in `tools/gate-legs.json`, read by `run-gates.sh` at the guard pre-pass, and one leg
(`manifest-check self-test`) has used it since before this build. This unit adds 29 more entries and
one bypass; it introduces no new mechanism to discover.
