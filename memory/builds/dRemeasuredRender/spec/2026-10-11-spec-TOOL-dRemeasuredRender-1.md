# TOOL-dRemeasuredRender-1 — gov's shipped suites scrub every bare location probe, and gov's own row stops excluding them

**Status:** SPECCED · rev-1 · 2026-10-11 · node d · Tier-2 · base 9a8777b8 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-dRemeasuredRender-1-brief.md](../prompts/2026-10-11-prompt-TOOL-dRemeasuredRender-1-brief.md) | research | DEPL-dRemeasuredRender-1 DEPL-dRemeasuredRender-2 |

<!-- /gen:spec-records -->

## 1. Goal

The location-probe leg's adopter row passes no registry and no pathspec, so it grades gov's shipped
`*.test.sh` suites, which gov's own row excludes. At base, 58 bare sites in 30 suites red every
adopter on bytes it may not edit. Scrub every site in place, and grade gov with the population it
ships.

## 2. Scope (IN)

- **S1** — Every bare site `sh_hygiene.py --location-probes` reports at base, run with no registry
  and no pathspec, is rewritten in place to the scrub the scanner prints for it:
  `(unset GIT_DIR GIT_WORK_TREE; ...)` opening the command substitution. Observed by AC1, AC3.
- **S2** — Gov's own row in `tools/gate-legs.json` drops the `:!*.test.sh` pathspec and keeps
  `:!memory/` and its registry argument. Observed by AC2.
  **Readers:**
  by name: `tools/check-testsuite-counts.sh`, which skips the spelling as a pathspec naming no
  suite, and `tools/gate-lint/sh_hygiene.py`, whose self-test passes it as a fixture pathspec.
  by value: `tools/check-testsuite-counts.sh` reads the row's argv, and with the token gone it skips
  one fewer non-suite token.
- **S3** — The gate-lint descriptor's comment on that row stops saying gov's row excludes its suites.
  NOT OBSERVED — a comment, and AC2 observes the row it describes.

## 3. Non-goals (OUT)

- The adopter row's argv and the registry grammar: both unchanged, as the prompt states.
- The scanner's near-miss classes, which it already reports without gating.
- Deleting the adopters' `location-probes.txt` rows: their own units, at their next pull.

### Edges

- **hands-off** external — inCMS and nc delete the 18 rows each declares for gov's suites.

## 4. Design

### Evidence

Read at base `9a8777b8`: the no-registry run prints `[GATED] 58 site(s) in 30 file(s)`, every one a
`*.test.sh`, and `[scrubbed] 37`. The scanner's remedy line for each site is that site's text with
the scrub applied, so the rewrite is the scanner's own output, applied. Two suites assign `GIT_DIR`,
and only as a prefix on one command that invokes a subject, never on a probe site: the scrub is a
no-op in a suite run from a clean environment, and it is the fix when a hook exports `GIT_DIR`.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/gate-lint/kit.toml`
- `.githooks/straggler-guard.test.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `tools/check-hook-destinations.test.sh`
- `tools/check-line-length.test.sh`
- `tools/check-spec-tokens.test.sh`
- `tools/check-wiring.test.sh`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/scratch-guard.test.sh`
- `tools/lib/extract-arms.test.sh`
- `tools/lib/lib-selftest.test.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/memory-tree/check-verdict-epoch.test.sh`
- `tools/memory-tree/marker-contract.test.sh`
- `tools/memory-tree/merge-rows.test.sh`
- `tools/memory-tree/transition-audit.test.sh`
- `tools/process-monitor/adopt-process-monitor.test.sh`
- `tools/push-main.test.sh`
- `tools/run-gates/foreign-prefix.gov.test.sh`
- `tools/run-gates/run-gates.runlog.test.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/run-gates/run-selftests.test.sh`
- `tools/unattended/adopt-unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/cross-component.test.sh`
- `tools/unattended/resume-tick.test.sh`
- `tools/unattended/runlog-writer.test.sh`
- `tools/unattended/unattended.test.sh`
- `tools/workflows/check-verifier-fanout.test.sh`
- `tools/workflows/unattended-build.test.sh`

Each touched kit's version moves once, after the last edit, per `tools/check-kit-versions.sh`.

### Alternatives rejected

- **Ship `:!*.test.sh` in the adopter row.** Rejected by the prompt: the leg's header bans a
  spelling, not a population, and an adopter's own suites would then go ungraded.
- **Declare gov's sites in a registry the adopters receive.** Rejected: a waiver for a probe that
  can simply be scrubbed is a hand-kept list, which is the defect.

## 5. Production-readiness checklist

- security — N/A — test code only; the scrub narrows what a probe reads from the environment.
- perf / scale — none: one `unset` builtin per site.
- error / empty / loading states — N/A — a substitution's exit status is unchanged by `unset`.
- observability — the leg's own report; GATED reads 0.
- risks — a suite that relied on an inherited `GIT_DIR` at a probe site; none does, per §4.
- testing — every touched suite outside `tools/unattended/` run directly; those six by parse check
  and a probe of each scrubbed line, under the owner's standing instruction.
- migration — none.
- user docs — N/A — nothing user-facing moves.

## 6. Acceptance criteria

- **AC1** — When `python3 tools/gate-lint/sh_hygiene.py --location-probes` runs with no registry
  and no pathspec, it reports `[GATED] 0` over every tracked shell source outside `memory/`.
  Red when: any site stays bare.
- **AC2** — When gov's own row, `shell hygiene (a location probe asked from a moved directory)`,
  runs from `tools/gate-legs.json` without `:!*.test.sh`, it exits 0. Red when: the pathspec is
  dropped while a site is still bare, which is the base state.
- **AC3** — When each touched suite outside `tools/unattended/` runs directly, it exits 0, and each
  `tools/unattended/` suite passes `bash -n`. Red when: a rewrite breaks a suite's syntax or an arm.
  permission: the six `tools/unattended/` suites are under the owner's no-run instruction.
  cost: the direct suite runs are tens of minutes on node d, so they run once, at the close.

## 7. Gates

`shell hygiene (a location probe asked from a moved directory)` · `shell-hygiene selftest` · `line-length gate selftest` · `manifest-check self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `process-monitor adopter selftest` · `run-gates canary` · `run-gates gov canary` · `hook destinations self-test` · `lexicon naming predicates` · `selftest harness self-test` · `extract-arms self-test` · `run-selftests self-test`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the owner's prompt.

## 10. Reuse audit

No existing seam fits beyond the scanner itself: it prints each site's remedy, and the rewrite
applies it. The recall query returned `TOOL-aGraftedHelix-45`, the unit that added the leg and
scoped it as "every bare site in the population is scrubbed in place", and the class record
`memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md`, whose gate is this leg.

Recall terms used: location probe scrub unset GIT_DIR GIT_WORK_TREE sh_hygiene gate-lint adopter row waiver registry test.sh exclusion
