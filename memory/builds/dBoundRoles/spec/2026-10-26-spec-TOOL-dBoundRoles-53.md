# TOOL-dBoundRoles-53 — unit 47's case proves its render arguments are read before it relies on them, so neither half can pass or fail on argument parsing

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 22 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 |
| [2026-10-26-build-TOOL-dBoundRoles-52-round3-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-52-round3-fix-return.md) | research | TOOL-dBoundRoles-52 TOOL-dBoundRoles-55 TOOL-dBoundRoles-58 |
| [2026-10-26-prompt-TOOL-dBoundRoles-52-round3-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-52-round3-fix-brief.md) | research | TOOL-dBoundRoles-52 TOOL-dBoundRoles-55 TOOL-dBoundRoles-58 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the seven promoted specs 45 to 51
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md`) confirmed
finding **id 30 at HIGH**, report item **H1**. Id 13 shares the item at HIGH and takes
`TOOL-dBoundRoles-52`; ids 2 and 39 report the same defect at MEDIUM, item M1, and are
`TOOL-dBoundRoles-58`'s.

Id 30 is the blast-radius face of the item. `tools/roles/handoff.py:1025-1028` refuses an unread input
with `ap.error`, which exits 2, while a refusal by `check_anchors` raises `RolesError` and returns 1
(`:1051-1053`). Unit 47's first render expects only "non-zero", so a usage error satisfies its exit
half, and its second render can never be observed. Nothing in the case says the render pair is
accepted before its verdict is read, so a role swap that the read check refuses is found only by
hand, and the cheap repair, widening a role's `reads`, is invisible in the diff of the test.

This unit makes the case check its own arguments: the role reads every key the case passes, the control
render is seen to exit 0 first, and the refusal is the anchor check's exit, not a usage error. It
repairs `TOOL-dBoundRoles-47` and builds one step after it (order 22), after unit 52 re-roles the pair.

## 2. Scope (IN)

- **S1** — The read check, `assert_role_reads <role> <key>...` in `tools/roles/adopt-roles.test.sh`. It
  reads the role's `reads` through the installed kit's `roles_lib.load_roles`, the parse
  `tools/roles/handoff.py:1025-1026` makes (split on commas, strip, drop a trailing `?`), and fails the
  case naming the role and the first key it does not read. It checks every key, `input:prompt`
  included: the render exempts `prompt` from its refusal (`:1027`), but a role that does not read it
  renders no block for it, so a handed half would pass on absence. Observed by AC1.
  **Readers:** by name: `tools/roles/handoff.py:1025`, the render's read set, which drops the same
  trailing question mark and which S1 copies without changing; no name leaves the tree. by value: NO VALUE
  READERS — the `?` is dropped only from the test's own copy of each key, and the role's `reads` field
  and what `load_roles` returns keep it.
- **S2** — The case calls it first. Before either render, unit 47's case calls `assert_role_reads` for its
  role and every `input:` key it passes, then runs the plain-words render and requires exit 0 and a
  written prompt file before it runs the refusal render. Observed by AC2.
- **S3** — The refusal is the anchor check's. The refusal render's verdict requires exit 1, a stderr
  naming the span, and no `does not read` in stderr; exit 2 fails the case as a usage error, naming it.
  Observed by AC3.

## 3. Non-goals (OUT)

- Which role carries the pair: `TOOL-dBoundRoles-52`'s, for id 13.
- The report's left-shift gate, a probe over every spec's render commands. S1 is the regression for this
  case; no clause of this build names the probe.
- Other render cases in the suite. A reuse of S1 by them is their pass's choice.

### Edges

- **consumes-from** `TOOL-dBoundRoles-52` — the re-roled pair on `gov-orienter`, whose keys S2 checks before the case reads a verdict (ids 13 and 30)
- **hands-off** `TOOL-dBoundRoles-58` — `assert_role_reads` and S3's exit check, which unit 58's item for id 39 observes rather than rebuilds (id 39)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/roles/handoff.py:1025-1028` builds the read set and calls `ap.error`; argparse exits 2.
- `tools/roles/handoff.py:1051-1053` catches `RolesError` from the render and returns 1, the exit every
  `refusals` line produces.
- `tools/roles/adopt-roles.test.sh:83` defines `check_arm`, the suite's verdict helper, which S1 and S3
  report through.

### Why the case checks keys the render does not

The render's read check guards the caller, and it skips `prompt`. The case's question is narrower: did
both copies of the span reach the section? A key the role does not read is silently dropped from the
section, so the check the case needs is stricter than the render's.

### Inventory

Minted: `assert_role_reads` (`sh.function`), asked of
`python tools/lexicon/lexicon.py --suggest assert_role_reads --as sh.function` at the pass.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 22. It consumes from `TOOL-dBoundRoles-52` at the same order and writes the same
suite, so `--dispatch` holds this pass until unit 52 is CLOSED.

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`

### Alternatives rejected

- **Exit-code check alone.** Exit 1 also follows any other render refusal; the span in stderr and the
  absence of `does not read` are what tie the verdict to the anchor check.
- **Assert `gov-builder`'s reads stay unwidened.** It pins one role's surface inside an unrelated
  suite; S1 already fails any role swap whose keys are not read.

## 5. Production-readiness checklist

- security — no new write path; the case can no longer be greened by a role whose read check refuses.
- perf / scale — one `python3 -c` read of the roster per call.
- error / empty / loading states — an empty `reads` fails S1 naming the first key.
- observability — each failure names the role and the key, or the usage error.
- risks — a renamed role or key fails loudly at S1 rather than inside a verdict.
- testing — AC1 to AC3 by staged copies of the case; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a scratch copy of the roles adopter suite whose case passes `--role gov-builder` with
  `--input question=` runs that case, it fails naming `gov-builder` and `input:question` before any
  render runs.
  Red when: the case reaches a verdict with a key its role does not read.
  fixture: a scratch repository with the roles kit installed, under `%TEMP%`, short-pathed.
- **AC2** — When a scratch copy whose role reads `input:question` but not `input:prompt` runs the case, it
  fails naming `input:prompt`; and the unmodified case runs the plain-words render before the refusal
  render.
  Red when: the handed half passes because the role renders no block for it.
- **AC3** — When a scratch copy of `tools/roles/handoff.py` that raises a usage error for every render
  runs under the case, the refusal half fails naming the usage error.
  Red when: exit 2 satisfies the refusal half.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC3 · the read check and the exit check, staged by re-roling the case to `gov-builder` and by a usage-error render · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 47 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 45 to 51, id 30
  (HIGH, item H1, shared with id 13; ids 2 and 39 share the defect at MEDIUM, item M1).

## 10. Reuse audit

The seams are the suite's `check_arm` (`tools/roles/adopt-roles.test.sh:83`) and the installed kit's
`roles_lib.load_roles`, the loader `handoff.py` itself reads the roster through.
`python tools/codebase-map/reuse_lookup.py "assert a test case's inputs are accepted before relying on its refusal"`
ranked `before`, `refusal`, `DesignRefusal` and `corpus_inputs`, none a role-reads check, so no existing
seam fits beyond the loader and the suite's helper.

Recall terms used: `python tools/memory-recall/query.py "how does a render case pick a role whose reads accept its inputs" --terms "handoff render role reads input question prompt spec typed handed refusal fixture"`
