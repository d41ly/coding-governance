# TOOL-dWitnessedBar-60 — every bar caller that records a trusted green scrubs every knob the hook clears, held by one parity arm over the three lists

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 33 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 |
| [2026-10-25-build-TOOL-dWitnessedBar-58-round3-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-58-round3-fix-return.md) | research | TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-62 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-58-round3-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-58-round3-fix-brief.md) | research | TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-62 |
| [2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-62 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 52 to 57
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md`)
confirmed finding **id 28 at HIGH**, its item **H3**, alone in that item. `TOOL-dWitnessedBar-56` S9 has
only the pre-push hook clear `GATE_BASE_FROM` and `GATE_SELECTION`, citing the `GATE_DOCS_BASE`
precedent. Two other bar callers already scrub `GATE_DOCS_BASE` and record a trusted green:
`PM_SCRUB` in `tools/run-gates/post-merge.sh` (`:35-38`) and the unattended driver's gates-green
`_gknobs` (`tools/unattended/unattended.sh:11159`), whose comment says its rc-0 result "would certify the
whole bar for this tree" (`:11152-11158`). Neither is in unit 56's scope, so an inherited
`GATE_SELECTION` holds legs in a bar the driver then records as green for the whole tree, and an
inherited `GATE_BASE_FROM=inherited` makes a scoped driver bar skip its verdict. This unit takes the
report's fix and its left-shift: both callers scrub every knob the hook clears, and one arm derives the
three lists and holds them together. It repairs `TOOL-dWitnessedBar-56`.

## 2. Scope (IN)

- **S1** — One list of the hook's per-bar clears. `.githooks/pre-push` gains
  `BAR_CLEARED_KNOBS="GATE_DOCS_BASE GATE_BASE_FROM GATE_SELECTION GATE_REUSE_PUSH GATE_REUSE_LINEAGE GATE_REUSE_DIGEST_ENV GATE_REUSE_SAMPLE GATE_REUSE_DAY"`,
  the knobs it clears for every bar, a STUB included, and sets again only on a decision of its own. One
  loop over it replaces the clear of `GATE_DOCS_BASE` (`:1857-1858`), the two reuse loops (`:1864-1875`)
  and unit 56 S9's two clears; each name still joins `ENV_CLEARED` when it was set, so the hook's
  "not honoured from the environment" line (`:1876-1877`) is unchanged. Observed by AC1.
- **S2** — post-merge scrubs them. `PM_SCRUB` carries every name in `BAR_SCRUBBED_KNOBS`
  (`.githooks/pre-push:1842`) and in `BAR_CLEARED_KNOBS`. It gains `GATE_BASE_FROM`, `GATE_SELECTION`,
  `GATE_REGEN_CHECK`, `GATE_REUSE_PUSH`, `GATE_REUSE_DIGEST_ENV`, `GATE_REUSE_SAMPLE` and
  `GATE_REUSE_DAY`. Observed by AC1 and AC3.
- **S3** — The driver scrubs them. `_gknobs` gains the same seven names. The driver's own
  `GATE_BASE_FROM` export of `TOOL-dWitnessedBar-40` S2 is passed in the `env` argv after the `-u`
  scrub, as `GATE_BASE="$_gbase"` already is (`:11262`), so the driver's value still reaches its bar and
  an inherited one never does. Observed by AC1 and AC4.
- **S4** — The class gate. `tools/run-gates/run-gates.gov.test.sh` gains an arm that reads
  `BAR_SCRUBBED_KNOBS` and `BAR_CLEARED_KNOBS` off the shipped hook, `PM_SCRUB` off `post-merge.sh` and
  `_gknobs` off `unattended.sh`, each by the `sed` cut the driver suite's parity arm already uses
  (`tools/unattended/unattended.test.sh:4337`, `:4341`), and fails naming every hook name a caller list
  lacks. It fails too when any of the four lists reads empty, so a moved line cannot pass it over
  nothing. Observed by AC2.
- **S5** — The behaviour on one caller. The post-merge arms of
  `tools/run-gates/run-gates.evidence.test.sh` gain a run whose caller sets `GATE_SELECTION` and
  `GATE_BASE_FROM=inherited`; the probe bar's environment dump (`bar.sh`, `:2299`) holds neither name.
  Observed by AC3.

## 3. Non-goals (OUT)

- The hook's own clear of the two knobs, their class line in `BAR_INERT_KNOBS` and §8 F2's inert class:
  `TOOL-dWitnessedBar-56` S9's. `BAR_CLEARED_KNOBS` is not a class of `check_knob_classes`, which still
  reads three.
- The export and the decline: `TOOL-dWitnessedBar-40` S2.
- A behavioural arm on the driver's gates-green bar: the unattended kit's own suites are waived for this
  build's landing (README rule), so the driver half is held by S4's parity and AC4's probe.
- The knobs the hook drops before the decision (`ENV_DROPPED_KNOBS`): those are the hook's alone and no
  other caller inherits a push's environment.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-56` — S9's clears of `GATE_BASE_FROM` and `GATE_SELECTION`, which S1 folds into `BAR_CLEARED_KNOBS`
- **consumes-from** `TOOL-dWitnessedBar-40` — the driver's own `GATE_BASE_FROM` export and its decline, which S3 keeps reaching the bar after the scrub
- **consumes-from** `TOOL-dWitnessedBar-5` — the `GATE_SELECTION` knob and the held legs it names, which S2 and S3 keep out of a trusted green
- **hands-off** `TOOL-dWitnessedBar-63` — S4's arm reading `PM_SCRUB` as a range with a count per list, the `_gknobs` comment, the README's scrub sentences and the floor raise that chains with unit 58's (ids 1, 9, 15, 16, 23, 26)

## 4. Design

### Evidence

- `PM_SCRUB` today: `GIT_DIR … GATE_LEGS GATE_REUSE GATE_REUSE_LINEAGE GATE_BASE GATE_DOCS_BASE
  GATE_PUSH_BASE GATE_ATTRIBUTE GATE_SPAWN_CMD GATE_SPAWN_FLOOR GATE_VERDICT_FAULT GATE_RUN_ID
  GATE_TURNSTILE_HOLDER` (`post-merge.sh:35-38`).
- `_gknobs="GATE_LEGS GATE_REUSE GATE_REUSE_LINEAGE GATE_DOCS_BASE GATE_SPAWN_CMD GATE_SPAWN_FLOOR
  GATE_VERDICT_FAULT"`, both bar calls run `env "${_gscrub[@]}"` (`unattended.sh:11159`, `:11262`, `:11264`).
- `BAR_SCRUBBED_KNOBS` holds `GATE_REGEN_CHECK` (`.githooks/pre-push:1839-1842`), which "set to 0 skips
  the runner's generated-output" check; neither caller list holds it today, so the driver suite's own
  parity arm (`unattended.test.sh:4334-4344`) reads red on the base and is unseen while those suites are
  waived.
- The runner honours `GATE_REUSE_PUSH` (`run-gates.sh:2631`), which neither caller scrubs.

### The lists, before and after

| Name | hook | `PM_SCRUB` | `_gknobs` |
|---|---|---|---|
| `GATE_LEGS` `GATE_REUSE` `GATE_SPAWN_CMD` `GATE_SPAWN_FLOOR` `GATE_VERDICT_FAULT` | scrubbed | has | has |
| `GATE_REGEN_CHECK` | scrubbed | gains | gains |
| `GATE_DOCS_BASE` `GATE_REUSE_LINEAGE` | cleared | has | has |
| `GATE_BASE_FROM` `GATE_SELECTION` | cleared (unit 56) | gains | gains |
| `GATE_REUSE_PUSH` `GATE_REUSE_DIGEST_ENV` `GATE_REUSE_SAMPLE` `GATE_REUSE_DAY` | cleared | gains | gains |

### Inventory

Minted: the hook constant `BAR_CLEARED_KNOBS`. Naming cells: asked of
`python tools/lexicon/lexicon.py --suggest BAR_CLEARED_KNOBS` at the pass.

### Migration

None: no caller sets any of the added names on purpose; each was a leak.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-56`, in the parallel group of order 33 with
`TOOL-dWitnessedBar-58`. The hook ships verbatim, so the kit version moves with it.

### Files touched (estimate)

- `.githooks/pre-push`
- `tools/run-gates/post-merge.sh`
- `tools/unattended/unattended.sh`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`

### Alternatives rejected

- **Add only the two knobs id 28 names.** The predicate run over the tree first finds five more names
  the hook clears and both callers inherit; an instance fix leaves the class open with its gate red.
- **Move the two knobs to `BAR_SCRUBBED_KNOBS`.** Unit 56 F2 rejected the scrubbed class: the hook
  sets `GATE_BASE_FROM` after that scrub runs.
- **Source one list from a shared file.** The hook ships verbatim and sources no kit
  (`.githooks/pre-push:1300-1301`), so a parity arm holds the copies instead.

## 5. Production-readiness checklist

- security — closes a fail-open path: an inherited knob can no longer hold legs in, or skip the verdict
  of, a bar a caller records as a trusted green.
- perf / scale — seven more `-u` arguments per bar call.
- error / empty / loading states — S4 refuses an empty list as well as a short one.
- observability — each caller's existing "not honoured from the environment" line names a dropped knob.
- risks — a future hook knob reds S4 until both callers carry it, which is its purpose.
- testing — AC1 to AC4 by probe and fixture; the arms of §7 at the close.
- migration — none.
- user docs — `tools/run-gates/README.md`'s post-merge section names the scrub by pointing at
  `PM_SCRUB` at the pass; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When `sed -n 's/^BAR_CLEARED_KNOBS="\([^"]*\)"$/\1/p' .githooks/pre-push` runs on the built
  tree, it prints the eight names of S1, and `grep -c 'GATE_SELECTION' tools/run-gates/post-merge.sh
  tools/unattended/unattended.sh` prints at least 1 for each file.
  Red when: either caller list lacks a hook knob.
- **AC2** — When the S4 arm runs over the built tree it prints no missing name; over a copy of
  `post-merge.sh` with `GATE_SELECTION` cut from `PM_SCRUB`, it fails naming `GATE_SELECTION` and
  `PM_SCRUB`; over a copy of the hook with the `BAR_CLEARED_KNOBS` line removed, it fails naming the
  empty list.
  Red when: the arm passes over a short or an empty list.
- **AC3** — When `post-merge.sh` runs in the evidence suite's post-merge fixture with the caller's
  environment setting `GATE_SELECTION` and `GATE_BASE_FROM=inherited`, `grep -c '^GATE_SELECTION=\|^GATE_BASE_FROM=' "$PM_PROBE"` prints 0.
  Red when: post-merge's bar inherits either knob.
  fixture: the evidence suite's own bare remote and clone, built by the suite.
- **AC4** — When `sed -n 's/^ *local _gk _gknobs="\([^"]*\)".*/\1/p' tools/unattended/unattended.sh` runs,
  it prints every name AC1's two hook constants hold, and `grep -n 'GATE_BASE_FROM=' tools/unattended/unattended.sh`
  names the driver's own export on a bar call's `env` argv after `"${_gscrub[@]}"`.
  Red when: the driver's scrub drops its own export, or keeps an inherited knob.

## 7. Gates

`pre-push self-test` · `pre-push bar self-test` · `measure-legs selftest` · `run-gates evidence` · `run-gates gov canary` · `memory hygiene`

The unattended kit's own suites are waived for this build's landing (README rule), so S3 is observed by
AC4 and S4's arm, not by that kit's suites.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC2 · the four lists read off the three shipped files, staged red by cutting `GATE_SELECTION` from a copy of `PM_SCRUB` · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC3 · a post-merge run under an inherited `GATE_SELECTION` and `GATE_BASE_FROM`, staged red by restoring the old `PM_SCRUB` · FLOOR_ASSERTIONS raised by these assertions

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-56`'s clause. Unit 56 carries none,
  being itself derived, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which population does the class gate hold?** Options: (a) the two knobs id 28 names; (b) every
  knob the hook clears or scrubs for every bar, which the predicate run over the tree first finds
  includes five more that both callers inherit today. (a) leaves `GATE_REGEN_CHECK` and the reuse knobs
  on one admission path, the class the report's left-shift names. RESOLVED (agent, 2026-10-25,
  delegated): (b), rung 3, the option gating the class and meeting every criterion; it narrows what a
  caller's environment reaches and widens no surface.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 52 to 57, id 28
  (HIGH, item H3).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-63's
  consumes-from edge, promoted by the round-1 spec audit of units 58 to 62; nothing else moved.

## 10. Reuse audit

The seams are the three existing scrub lists and the driver suite's parity arm
(`tools/unattended/unattended.test.sh:4334-4344`, `TOOL-aFrugalTurnstile-12` AC3), whose `sed` cuts S4
reuses from a suite that is not waived. `python tools/codebase-map/reuse_lookup.py "scrub bar knobs
inherited from the environment before a trusted green"` ranked `before`, `write_bar_green`,
`write_inherited_asks` and `MERGE-BAR.md`; `write_bar_green` is the writer both callers share, not a
scrub, so no existing seam fits beyond the three lists and the parity arm named.

Recall terms used: `python tools/memory-recall/query.py "where does a bar caller scrub the knobs the pre-push hook clears" --terms "BAR_SCRUBBED_KNOBS PM_SCRUB _gknobs GATE_DOCS_BASE gates-green trusted gate-bar-green inherited knob scrub parity"`
