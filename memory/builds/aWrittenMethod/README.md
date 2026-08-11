---
slug: aWrittenMethod
node: a
opened: 2026-08-11
streams: tooling+playbook+kickoff
roster: TOOL
ids: TOOL-aWrittenMethod-1
---

# aWrittenMethod — the instruction layer: the build method, written down

Node `a` · opened 2026-08-11 · streams tooling+playbook+kickoff.

The unattended-run kit supervises a build but does not instruct one. `--preflight` asserts a mandate,
pins a BASE, sets phase RUNNING and returns. Between RUNNING and `--close` the driver does nothing:
no loop, no dispatch, no prompt. The build method — how to spec, how to review, how to build — is
supplied by the owner pasting prose into chat on every run, which is exactly the state
`aUnmannedHelm` found the mandate in before it became a kit.

This build turns that prose into a durable instruction layer.

This README is the **master overview and the owner decision menu**, per `memory/TEMPLATE-SPEC.md`.

## Start here

**State.** Two design passes, one converged spec at rev-3, and ten of eleven scope items BUILT on
`branch/unattended-kit-builds-27d8c6`. Unmerged and unpushed, deliberately — see the park below.

| Pass | Landed | Scope |
|---|---|---|
| 1 | `a383375` | S1 the method template, S2 the render pair and its derived count |
| 2 | `7ff43c1` | S3 the adopter path, S4 the kit version pair, and M6's own broken recipe |
| 3 | `0f7688e` | S9 the delegated-resolver grammar, S7 the declared keepalive cadence |
| 4 | `22b14ca` | S5 the four delivery sites, S10 and S6's charter half |
| 5 | `f8182aa` | S8 the map dossier, S11 the three declines |

**PARKED — S6, the playbook half, and why the build does not land.**

*The question:* collapse the thirteen-bullet unattended block in
`parallel-coding-governance.domain-rules.md` §1 to one pointer, shorten the duplicate landing clause
at `parallel-coding-governance.template.md:158`, add `MEMORY_ROOT` to the companion's catalog and
update its three-deletion recipe, bump both `governance-template` markers to v2.7, and snapshot v2.6
into `memory/archive/`.

*The options seen:* do it now under a nearly exhausted context window; or park it whole; or split it
and land the safe half. The middle option was taken.

*The reason:* S6 is the only destructive item in the build, it edits a byte-gated product template
whose size gate leaves 154 bytes free, and a §-renumbering there has already broken three shipped
cross-references once. A careful restructure attempted at the end of a long run is how the removals
become a defect instead of a repair. Nothing already landed depends on S6.

*Why this blocks landing rather than just deferring:* the owner's standing rule is that the merge and
push happen only when the ENTIRE build is done. A scope item parked means it is not. AC10 is
unmet by construction, so the bar would be graded against a spec the tree does not satisfy. The
correct terminal state for this run is therefore not LANDED.

**Next action:** build S6, then the closing diff review, then the full bar, then land.

**Next action:** owner reads the spec's §8 and resolves the open forks.

## The two passes, and why there are two

The first pass was aimed at the wrong target and is kept as a record rather than deleted, because its
method was sound and three of its findings are independently real.

| Pass | Aimed at | Verdict |
|---|---|---|
| 1 — `build/2026-08-11-build-aWrittenMethod-1-enforcement-pass.md` | proving a run did not tamper with its own instructions | REJECTED for scope. It designed an enforcement layer and labelled it an instruction layer |
| 2 | the method itself: how to spec, how to review, how to build, and how that text reaches the agent | converged into the spec below |

The scope error in pass 1 was introduced by its own briefing, not discovered in its output. The
briefing named "a run that writes its own SPEC is the analogue of a run that writes its own MANDATE"
as the central tension and scored candidates on checkability and self-authorization safety. Every
candidate and both judges optimized that faithfully. The output graded the owner's sixteen rules as
six machine-checked, six witnessed, three agent-attested and three unenforceable — a grading rubric,
where a procedure had been asked for.

The distinction the two passes separate, and which the kit currently conflates:

| Layer | Scope | Answers |
|---|---|---|
| Mandate | per-run | may this run merge and push |
| Specs | per-build | what to build |
| **Method** | **generic, stable across builds** | **how to spec, review, build, recall, parallelize, reground, land** |

The method is mostly generic. That is why it does not need per-run provenance, and it is the reason
pass 1's apparatus was answering a question nobody asked.

## What survives pass 1

Three findings, each verified against source rather than inherited from the pass:

- **The pinned BASE is forgeable.** `default_branch()` returns `$GOV_DEFAULT_BRANCH` verbatim, and
  `git update-ref refs/remotes/origin/<name> <sha>` writes a remote-tracking ref with no push and no
  network. Reproduced end to end in a scratch repo: BASE resolves to a commit the run authored while
  staying unequal to HEAD, so the degenerate guard does not fire, and `check_mandate` compares
  run-authored bytes against run-authored bytes. The driver's own comment asserts the opposite
  defense. This was already filed as D3/BLOCKER in
  `../aUnmannedHelm/reviews/2026-08-10-review-aUnmannedHelm-2.md` and no backlog row tracked it.
  Now `TOOL-aWrittenMethod-2`, and it is **not** in this build's scope.
- **Four project declarations are delivery, not enforcement**, and carry into pass 2: the recall
  entrypoint, the reuse entrypoint, the review harness, and the keepalive interval.
- **Measured corpus facts** that constrain any design here: `## Verdict` appears in 8 of 32 review
  records and no verdict field exists anywhere; the build README `ids:` key is written as ranges and
  unions across all 25 builds, so it is not a machine-readable unit roster; and the mandatory-key
  mechanism in `.unattended.conf` is the required-key loop in the gate leg, not the
  surviving-placeholder grep, because an empty value substitutes silently.

## Ratified decisions

None yet. The forks are in the spec's §8.

Records live under `spec/` and `build/`. The table below is GENERATED from the status header of every
spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node a · opened 2026-08-11 · streams tooling+playbook+kickoff · ids TOOL-aWrittenMethod-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aWrittenMethod-1 — the build method, rendered and delivered](spec/2026-08-11-spec-aWrittenMethod-1.md) | INPROGRESS | rev-3 | 2026-08-11 |
<!-- /gen:build-index -->
