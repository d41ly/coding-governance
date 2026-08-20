# TOOL-dScriptedRepeat-8 — the output-scope refusal, and what it cannot see

**Status:** SPECCED · rev-1 · 2026-08-20 · node d · Tier-2 · base d2a40aa8 · streams tooling

## 1. Goal

Refuse a code build wearing the playbook mode: red when a playbook-mode run's diff touches anything
outside the declared output globs plus a closed exemption set — and state, in the gate's own header,
the class this predicate cannot see.

## 2. Scope (IN)

- **S1.** The DIFF POPULATION, defined precisely and not as "the diff". It is the set of paths the
  RUN's own commits introduce or modify, computed over the run's commits individually rather than as a
  `BASE..HEAD` range. §4 gives the measurement that forces this.
- **S2.** The EXEMPTION SET, closed and enumerated: the run's own build folder under the memory root;
  the generated work-state artifacts every build touches; the run-state file; the backlog shard the run
  appends to; the decision log; and the PLAYBOOK ITSELF, because fork 6's improvement loop edits it.
- **S3.** The REFUSAL: a leg arm that reds naming every offending path, evaluated at close and again on
  the bar, so a run cannot pass it by closing before the bar runs.
- **S4.** The STATED CHECK. The gate's own header names what it cannot see: a code change that lands
  INSIDE a declared output path. §4 argues why this class cannot be narrowed and why the gate is still
  worth having.
- **S5.** Running the candidate predicate over the REAL TREE before wiring it — over past builds'
  actual diffs — printing hits AND near-misses, per the charter's rule. The research already ran a
  first version and found it reds the mandated memory update, which is why S2 exists in this shape.
- **S6.** Arms: an out-of-scope source edit reds; an exemption-set path passes; the playbook's own edit
  passes; a merge commit's combined-diff change is SEEN; the predicate over a real past build's diff
  produces the documented hit/near-miss list.

## 3. Non-goals (OUT)

- No content-kind or extension narrowing. A playbook that generates tests emits `.py` and `.sh` under
  its output paths as the ORDINARY case; the owner's ask names tests as a content kind. The research
  proposed a kind-based refinement and another lens killed it on exactly this. Recorded so it is not
  re-proposed.
- The gate does not read the CONTENT of a changed file.
- No exemption for "small" changes, no allowance list an operator edits per run. An exemption that a
  run can widen is not an exemption.

## 4. Design

### Why `BASE..HEAD` is the wrong population

Measured in the research on a real build in this tree: a `BASE..HEAD` range reported 383 changed files
against 17 the build actually authored — a factor of 22.5 — because the range absorbs everything that
landed on the default branch between BASE and the run. And `--no-merges` is NOT the repair: seven
merges in another build carried combined-diff changes to real source files, so excluding merges hides
exactly the changes a scope gate exists to see. The population is therefore the run's OWN commits,
enumerated, with merges included and read as combined diffs.

This is the "same word, two things" defect the research names: two lenses used "the diff" for two
different populations and only one measured it.

### Why the exemption set must include the memory update

A first cut of this predicate reds the memory update the charter MANDATES — every build writes its
build folder, appends a backlog row, and re-renders the generated work-state index. A scope gate that
reds a run for obeying the Definition of Done is a false red that will be disabled within a week, and
a disabled gate is worse than none. The exemption set is closed and enumerated rather than pattern-
based, so widening it is a diff somebody reviews.

### What this gate cannot see, and why it is still worth having

It cannot see a code change that lands inside a declared output path. That class cannot be narrowed:
narrowing by file kind dies on test-generating playbooks, and narrowing by content would make this a
semantic gate, which it is not. So the header says so.

It is still worth having because the class it DOES catch is the one that actually happens: a run that
drifts from making content into editing the machinery around it touches paths nobody declared. That is
a structural refusal with an observable failing case, which is more than the "the Skill tells the agent
to refuse" alternative offers — that one is a CHECK, unenforceable, and indistinguishable from an agent
that simply did not refuse.

### Alternatives rejected

**A pathspec `guard` like the gate manifest's.** Attractive, and the wrong grain: a guard scopes whether
a leg RUNS. This decides whether a diff is legal.

**Redding at the bar only.** Rejected: a run that closes and lands before the bar sees it has already
spent the mandate. Evaluated at both moments.

## 5. Production-readiness checklist

- security — this is a scope gate, not a security boundary. A run with shell access edits the gate; §9's
  reduction is unchanged and the header says the control that binds lives on the remote.
- perf / scale — one commit enumeration per evaluation.
- a11y — N/A.
- i18n — paths compared as bytes; a non-ASCII path must not be silently dropped by a locale-sensitive
  comparison, which is an arm rather than an assumption.
- error / empty / loading states — an EMPTY diff population is a run that changed nothing, which is a
  dead probe and reports as one rather than as a clean scope check.
- observability — the refusal names every offending path, and a passing run prints the counts of
  in-scope and exempt paths so a reader can see the gate had something to look at.
- risks — false reds are the risk that kills this gate. S5's requirement to run it over real past
  diffs before wiring is the control, and it has already found one false red.
- testing + left-shift gates — S6, including the merge-commit arm, which is the one a naive
  implementation gets wrong.
- migration / rollback — scoped to the playbook mode, so no existing run is affected.
- user docs — the leg header carries the stated CHECK; the Skill names the exemption set.

## 6. Acceptance criteria

- **AC1** — When a playbook-mode run's commit modifies a source file outside the declared globs and
  outside the exemption set, `bash tools/unattended/check-playbook.sh` REDS naming that path. Staged
  and observed.
- **AC2** — When the run writes its build folder, appends its backlog shard and re-renders the
  generated work-state index, `bash tools/unattended/check-playbook.sh` PASSES. This is the mandated memory update and a first cut of
  this predicate red it.
- **AC3** — When the run edits the PLAYBOOK itself, `bash tools/unattended/check-playbook.sh` passes.
- **AC4** — When a run's history contains a MERGE whose combined diff touches an out-of-scope source
  file, the gate SEES it. Observed; `--no-merges` fails this and is the obvious wrong implementation.
- **AC5** — When the diff population is EMPTY, `bash tools/unattended/check-playbook.sh` reports a dead
  probe and does not report a clean scope check.
- **AC6** — When the candidate predicate is run over at least three real past builds in this tree
  before wiring, the hits AND near-misses are recorded in
  `memory/builds/dScriptedRepeat/build/`, and any false red is either fixed or its exemption added with
  a reason. Per the charter's rule about running a predicate over the real tree first.
- **AC7** — When the mode is not the playbook mode, the gate does not evaluate and reports `skipped`
  with its reason rather than green.

## 7. Gates

`bash tools/unattended/check-playbook.sh` · `bash tools/unattended/check-playbook.test.sh` ·
`bash tools/unattended/unattended.test.sh` for the close-path arm ·
`bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — does the exemption set live in the kit or the playbook?** In the kit it is closed and a
  playbook cannot widen it, which is the property that makes it an exemption. In the playbook it can
  name a project's own mandated-write paths, which differ per adopter. Recommendation: kit-owned CORE
  plus a playbook EXTENSION, exactly the shape the phase, DoD and directive sets already use, so a
  project may add and never delete. **Agent-resolvable; the precedent is strong enough that I will take
  it unless you say otherwise.**
- **F2 — what happens on a run that legitimately must touch machinery**, for instance a playbook run
  that discovers its own checker is broken. Recommendation: it parks the decision and stops, because
  fixing machinery is a code build and this mode refuses those by design. That is the mode working, not
  a gap — recorded because it will read like a gap the first time it fires.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft. S1's population and S2's exemption set both come from measured
  results in the research: a factor-of-22.5 range error, a merge-visibility trap, and a false red on the
  mandated memory update, each reproduced rather than reasoned about.

## 10. Reuse audit

No existing seam does this job, and the nearest one is a trap worth naming: the gate manifest's `guard`
pathspec looks like the same mechanism and answers a different question — whether a leg runs, not
whether a diff is legal — and reaching for it is the mistake this audit exists to prevent. What IS
reused is the discipline around building the predicate: run it over the real tree first and print hits
and near-misses, which this repo's charter states as a rule and which has already paid here by finding
the mandated-memory false red before a line was written. The CORE-plus-EXTENSION shape proposed in §8
F1 is the phase, DoD and directive sets' shape, reused rather than invented. The dead-probe report on an
empty population is `drift-audit`'s liveness rule. Recall terms used: diff population commit range
merge combined scope refusal exemption guard pathspec false red near miss dead probe predicate real
tree staged observed.
