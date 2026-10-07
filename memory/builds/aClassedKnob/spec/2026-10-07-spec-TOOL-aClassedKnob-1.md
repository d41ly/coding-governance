# TOOL-aClassedKnob-1 — the pre-push self-test classifies every runner knob and reads the adopter's own policy

**Status:** SPECCED · rev-1 · 2026-10-07 · node a · Tier-1 · base c83ef509 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make `.githooks/pre-push.test.sh` pass in gov and in any adopter on gov's bytes: classify the four
runner knobs H49 finds unclassified, and make IR AC11 assert the policy the repository under test
declares rather than gov's.

## 2. Scope (IN)

- S1. Add `GATE_CENSUS_EVERY`, `GATE_MEMINFO`, `GATE_MEMPAUSE` and `GATE_MEMPAUSE_HOLD` to
  `BAR_INERT_KNOBS`, with a comment line saying why each is inert. Observed by AC1 and AC2.
- S2. IR AC11's "this repository" arm derives its expectation from the repository's own committed
  `.githooks/gate-env.sh` at HEAD, sourced in a subshell the way the suite already reads
  `GOV_KITROOT`, and mapped through the kit contract: absent file or blank key reads `land`, a value
  outside `park land` reads `park`, a non-positive bound reads none. Observed by AC3.
- S3. A fixture arm runs the same sliced reader over a commit declaring `park` with a bound of 7 and
  over one with no `gate-env.sh`, so the reader keeps a case gov's own values cannot satisfy.
  Observed by AC4.

## 3. Non-goals (OUT)

No change to `.githooks/pre-push`, `tools/run-gates/run-gates.sh` or the policy itself. inCMS's asks
ABL-aYieldedFork-1, -2 and -3 are not built here.

### Edges

none

## 4. Design

The knobs, read from `tools/run-gates/run-gates.sh` at base:

- `GATE_MEMPAUSE` and `GATE_MEMPAUSE_HOLD` set the memory pause's threshold and its hold bound. The
  pause holds a dispatch and every hold ends; the kit's own comment says the knob "narrows a pool and
  never turns a leg into anything". A breach of the wall is RED. Width class.
- `GATE_MEMINFO` is the meminfo path the pause reads, the sibling of `GATE_CGROUP_ROOT`, which is
  already inert. An unreadable path makes the pause INERT and says so.
- `GATE_CENSUS_EVERY` is the foreign-load census period. The census writes a `foreign` field into
  each `.leg` row for the evidence tool and decides no leg's verdict.

IR AC11's oracle sources `gate-env.sh` in a subshell, which is the shell's own reading and not a
second copy of `read_policy_key`. Where the two disagree on a declaration, the arm reds and names both.

### Files touched (estimate)

- `.githooks/pre-push.test.sh`

## 5. Production-readiness checklist

- risks — an adopter whose `gate-env.sh` assigns the policy in a form the hook's line reader cannot
  see (`export INHERITED_RED=park`) now reds AC11 instead of passing; that red is a real
  disagreement between the hook and the shell.
- testing — AC1 to AC4.
- user docs — N/A, no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `check_knob_classes` runs over the shipped gate runner, it prints nothing.
  Red when: any of the four knobs is left out of every set.
- **AC2** — When the existing planted-knob arm appends `GATE_PLANTED` to a copy of the runner, the
  arm reports it by name. Red when: the classification is widened by a pattern rather than by name.
- **AC3** — When the pre-push suite runs in gov, its `IR AC11` arm passes reading `land 10`; when it
  runs in a clone of inCMS `branch/adopt-coding-governance-3946e4`, the arm passes reading `park 10`.
  Red when: the expectation is hardcoded to either repository.
- **AC4** — When the sliced reader runs over the fixture commits, it reads `park 7` and `land` with no
  bound. Red when: the reader returns gov's own values regardless of the commit it reads.

## 7. Gates

`pre-push self-test`

New arm: .githooks/pre-push.test.sh · covers AC4 · a fixture commit declaring park 7, and one with no gate-env.sh · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-07 · initial draft.
