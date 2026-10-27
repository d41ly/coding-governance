# TOOL-dRankedPlan-22 — the session-scoped ratification predicate is asked only at the act it ratifies, gated over the tree

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 6 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-22-deviation-221.md](../build/2026-10-26-build-TOOL-dRankedPlan-22-deviation-221.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) | spec-audit | TOOL-dRankedPlan-27 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-21 TOOL-dRankedPlan-20 TOOL-dRankedPlan-19 TOOL-dRankedPlan-28 TOOL-dRankedPlan-23 TOOL-dRankedPlan-29 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`) confirmed
**finding 37 at HIGH**. It shares item **H2** with finding 3, which `TOOL-dRankedPlan-21` closes by
re-pointing `TOOL-dRankedPlan-2`'s order check to the recorded crossing. Finding 37 is the failure
envelope of the same defect: a commit-time guard, `TOOL-dRankedPlan-2` S4's pre-commit block, asks
`read_plan_ratification`, whose `request` witness exists only in the session that typed the request
(`TOOL-dPlacedRequest-19` S5), so in a later session, an unattended run or on another node the guard
fails open. The class is any reader that asks the session-scoped predicate after the act it
ratifies; `TOOL-dRankedPlan-15`'s `show` is a second instance (item H3). This unit gates the class: a
declared set of files may call the predicate, each the act it ratifies, and a check over the tracked
tree refuses every other caller, so neither instance nor a later one can ship.

## 2. Scope (IN)

- **S1** — The declared callers. `SESSION_PREDICATE_CALLERS` in `tools/loop/ratify.py` names the
  repository-relative files whose call of the predicate is the act it ratifies:
  `tools/loop/ratify.py`, where `TOOL-dRankedPlan-10`'s `derive_plan_exit_ratification` answers at the
  `plan.exit` move, and `tools/memory-tree/triage.py`, where `TOOL-dRankedPlan-3` S6 asks at the
  owner-batches write. Each entry carries its reason in a comment beside it. Observed by AC2.
- **S2** — The check. `check_predicate_callers(root)` in `ratify.py`, run as `python
  tools/loop/ratify.py --check-callers [--root <dir>]`, reads every tracked `*.py`, `*.sh` and `*.js`
  file and every file under `.githooks/` through `git ls-files`. A caller is a code line, one whose
  first non-blank characters are not `#` or `//`, that matches `\bread_plan_ratification\s*\(`, or a
  shell line invoking `ratify.py` with no argument that begins `--`, the predicate's own CLI form
  (`TOOL-dRankedPlan-9` S1). A caller outside S1's set prints `ratify — <path>:<line> asks the
  session-scoped predicate after its act; read the crossing record instead` and the check exits 1;
  otherwise it prints `ratify — callers: <n> file(s), each at the act` and exits 0. Exit 2 when git
  cannot list the tree. Observed by AC1 and AC3.
- **S3** — The arm. `tools/loop/selftest.py` runs S2 over the repository it runs in, and the plant
  `caller-guard` of `ratify.py --fixture`: a scratch repository whose `.githooks/pre-commit` calls
  `read_plan_ratification(` is refused naming that file, and the same line in a planted
  `tools/memory-tree/triage.py` is admitted. Observed by AC1 and AC3.
- **S4** — `tools/loop/README.md`'s paragraph on `ratify.py` (`TOOL-dRankedPlan-9` S9) names the rule
  and `--check-callers`. Observed by AC4.

## 3. Non-goals (OUT)

- Re-pointing the callers the check finds. `TOOL-dRankedPlan-2`'s order check is
  `TOOL-dRankedPlan-21`'s, and `TOOL-dRankedPlan-15`'s `show` is `TOOL-dRankedPlan-23`'s; until each
  lands, S2 reds on it, which is the gate seeing its class.
- The driver's plan-gate arm, `TOOL-dRankedPlan-10` S6, which calls `ratify.py <slug> --exit`, the
  exit act's answer. Until dWellOiledMachine's intake lands, every `request` build takes the fallback
  there, whose release is a durable disposition record, so no session-scoped answer reaches it.
- Calls in prose, fixtures named as data or comments: a comment line is not a call.

### Edges

- **consumes-from** `TOOL-dRankedPlan-9` — `read_plan_ratification`, its CLI form and `ratify.py`'s `--fixture`, the predicate whose callers S2 bounds and the fixture S3 plants into
- **hands-off** `TOOL-dRankedPlan-30` — `SESSION_PREDICATE_CALLERS` and the `caller-guard` plant, which that unit re-spells as kit anchors resolved at run time, superseding S1's literal paths and AC2 (spec audit of units 19 to 29, id 19)
- **hands-off** `TOOL-dRankedPlan-31` — S3's tree run of `--check-callers`, which that unit moves onto its own unguarded repo leg, leaving the selftest the plant (spec audit of units 19 to 29, id 20)
- **hands-off** `TOOL-dRankedPlan-32` — S2's caller definition, which that unit re-points to a structural reading of Python, shell and JavaScript statements (spec audit of units 19 to 29, id 30)
- **hands-off** `TOOL-dRankedPlan-37` — AC3, which that unit observes at order 18 after units 21, 23 and 29, and the `caller-guard` plant, which it extends with a bare and a continued shell call (spec audit of units 19 to 29, ids 4, 31)

## 4. Design

### Evidence

- `TOOL-dPlacedRequest-19` S5: the consent predicate returns 0 only when this session's id is a line
  of `requests/<key>.typed`; another session or node "has no such line, so the predicate refuses it".
- Callers specced at base: `TOOL-dRankedPlan-10` S3 (at the move), `TOOL-dRankedPlan-3` S6 (at the
  batch write), `TOOL-dRankedPlan-2` S3 (at commit, after the act) and `TOOL-dRankedPlan-15` S5 (at
  Design's read, after the act); `TOOL-dRankedPlan-5` S4 runs the CLI by hand in its pass, a session
  act and no tracked caller.
- The repository's precedent for a banned construct gated over the tracked tree is
  `tools/workflows/check-review-join.sh`, which judges code lines only so its own documentation of
  the ban does not red it (its header, lines 25-28).

### The rule

| Caller | When it asks | In S1 |
|---|---|---|
| `derive_plan_exit_ratification`, `ratify.py` | at the `plan.exit` move | yes |
| `triage.py ratify` | at the owner-batches write | yes |
| `check_ratified_order`, `gen_build_index.py` | at a later commit | no: `TOOL-dRankedPlan-21` |
| `derive_revision_state`, `plan_revision.py` | when Design reads, later | no: `TOOL-dRankedPlan-23` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_predicate_callers` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest check_predicate_callers --as py.function` answered OK |
| `SESSION_PREDICATE_CALLERS` | constant, `ratify.py` | none declared |
| `--check-callers` | flag of `ratify.py` | none |
| `caller-guard` | `ratify.py` fixture plant | none |

### Rollout

Live at landing. Between this unit and `TOOL-dRankedPlan-23`, S2 reds on `plan_revision.py`, a red the
close's bar reads only after that unit has landed.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2, S3's plant
- `tools/loop/selftest.py`: S3's tree run
- `tools/loop/README.md`: S4

### Alternatives rejected

- **A checklist entry alone.** The audit's left-shift names one; a line nothing runs does not stop the
  third instance, and the charter's `[class]` rule asks the class gated.
- **A new gate leg.** A leg owes a budget row, a ceiling row, a map claim and a foreign-prefix
  declaration (items M12, M13 of the same audit); the loop kit's selftest already runs `ratify.py`'s
  fixture, so the check rides it.
- **Allow-by-default with a ban list.** A new caller would pass until someone listed it; deny by
  default is the charter's `[security]` rule.

## 5. Production-readiness checklist

- security — deny by default: an unlisted caller reds. The list lives beside the predicate, so a new
  caller is a reviewed edit of the kit that owns it.
- perf / scale — one `git ls-files` and one read per tracked code file, within the selftest.
- error / empty / loading states — git failing exits 2; an empty population prints `0 file(s)`, which
  the plant's admitted case proves is not the only answer.
- observability — every refusal names the file and line.
- risks — a call built at runtime, by `getattr` or an assembled command string, is invisible to S2,
  as `check-review-join.sh` is to a constructed join.
- testing — the `caller-guard` plant, red and green, and the tree run.
- migration — none.
- user docs — N/A — no user-facing surface; the kit README carries the rule (S4).

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-guard` runs, the planted
  `.githooks/pre-commit` caller is refused with exit 1 naming `.githooks/pre-commit` and its line, and
  the planted caller at the memory-tree kit's `triage.py` is admitted.
  Red when: a commit-time hook may ask the predicate, or a declared act is refused.
- **AC2** — When a probe imports `ratify.py` and prints `SESSION_PREDICATE_CALLERS`, it lists exactly
  two paths, the loop kit's `ratify.py` and the memory-tree kit's `triage.py`, as S1 spells them.
  Red when: a later reader is declared as an act.
- **AC3** — When `python ratify.py --check-callers` runs at the close's tip, after
  `TOOL-dRankedPlan-21` and `TOOL-dRankedPlan-23` have landed, it exits 0; on a scratch copy of the tree
  whose `gen_build_index.py` carries one `read_plan_ratification(` call, it exits 1 naming that file.
  Red when: the tree holds a later caller and the check passes.
  fixture: the scratch copy is a clone under a short `%TEMP%` path.
- **AC4** — When `grep -n "check-callers" README.md` runs over the loop kit's README, it finds S4's
  paragraph.
  Red when: the kit README does not state the rule.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/selftest.py · covers AC1 AC3 · the `caller-guard` plant and the tree run of `--check-callers`, staged by a `.githooks/pre-commit` that asks `read_plan_ratification` · none

## 8. Open questions

- **F1 — Is `TOOL-dRankedPlan-10` S6's driver arm a later caller?** Options: (a) out of this unit, as
  §3 states, since its `--exit` answer under the stand-in always takes the durable fallback; (b)
  re-point it to `TOOL-dRankedPlan-21`'s reader here. (b) depends on a unit of this unit's own
  parallel group, which M6 clause 2 forbids. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  tie-broken by fewer open questions; S2's shell rule does not flag an `--exit` call, so the arm is
  neither listed nor refused. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's finding 37 (HIGH, item
  H2, shared with finding 3), repairing `TOOL-dRankedPlan-2`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-30`, the hands-off edge to `TOOL-dRankedPlan-31`, the hands-off edge to `TOOL-dRankedPlan-32`, the hands-off edge to `TOOL-dRankedPlan-37`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

No existing seam fits the check: `python tools/codebase-map/reuse_lookup.py "check that no caller
outside an allowlist calls a function"` ranked name stems only (`check`, `checks`, `check_line`,
`check_convention`), and the one tracked ban over the tree, `tools/workflows/check-review-join.sh`, is a
JavaScript-only gate for one construct whose population and exit grammar it owns; its code-line rule
is reused here as a rule, not as code, because a shell gate over `*.js` cannot be pointed at Python
callers without a second population in it. The predicate and its CLI are `TOOL-dRankedPlan-9`'s,
which S1's list sits beside. The recall query returned the audit's H2 left-shift entry and
`TOOL-dPlacedRequest-19` S5, which agree with the specs read.

Recall terms used: `python tools/memory-recall/query.py "how is a session-scoped consent predicate kept out of a commit-time guard" --terms "request-consent typed relayed session predicate commit-time guard pre-commit ratified order cross-session plant"`
