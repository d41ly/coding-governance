# TOOL-dIndexedDesign-31 — the blinded scout's input as a true allow-list: `derive_scouted_seam_input` names the keys a scout may see, and a planted unknown key is withheld

**Status:** DEFERRED · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 11 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-31-deviation-311.md](../build/2026-10-28-build-TOOL-dIndexedDesign-31-deviation-311.md) | deviation | — |
| [2026-10-28-build-TOOL-dIndexedDesign-31-promoted-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-31-promoted-fix-return.md) | research | TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-31-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-31-1-spec-writer.md) | journal | — |
| [2026-10-28-prompt-TOOL-dIndexedDesign-31-promoted-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-31-promoted-fix-brief.md) | research | TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 |
| [2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md`)
confirmed finding **id 37 at BLOCKER**, report item **B1**, the item's only id.
`TOOL-dIndexedDesign-5` S6 calls the `case_input` hook an allow-list, then defines the `scouted-seam`
instance's input as "every key of a case but `ground_truth` and `control`", which is a deny-list. The
aScoutedSeam cases carry keys derived from the answer: `probe_evidence` names the ground-truth symbols
and their ranks, `reinvention` names the reinvented paths, and `decoys`, `classification` and `sha`
pass through too. So the blinded scout is handed the answer, and every reuse-bench figure the factory
produces, unit 5 S10's reproduction of the bar included, is scored against an answer the subject saw.
Unit 5 AC7 checks only that two keys are absent, so it certifies blinding that does not hold.

This unit makes `derive_scouted_seam_input` a true allow-list that names the keys a scout may see and
withholds every other, and proves it with a planted key nobody listed. It repairs
`TOOL-dIndexedDesign-5` and builds one step after it, at order 11.

## 2. Scope (IN)

Build-run precondition this unit calls and does not build: `replay_scorer.py`'s `INSTANCES` and the
`case_input` hook with `--blind`, as `TOOL-dIndexedDesign-5` S6 lands them one order earlier, on the
scorer factory of TOOL-dFairHearing-12 S1 and TOOL-dFairHearing-14 S2.

- **S1** — The allow-list. `tools/workflows/replay_scorer.py` gains the constant
  `SCOUTED_SEAM_INPUT_KEYS = ("prompt", "repo", "sha_before", "slug")`, and the `scouted-seam`
  instance's `case_input` hook, `derive_scouted_seam_input(case)`, returns exactly the members of that
  tuple a case carries, in that order, and nothing else. It never names a key it withholds. `prompt`,
  `repo` and `sha_before` are required: a case lacking one is refused by `--blind` with exit 2, naming
  the case's `id` and the key. `slug` is optional, because 8 of the 30 cases lack it. The case `id`
  stays outside `input`, as unit 5 S6's printed shape `{"id": <id>, "input": ...}` already puts it.
  Observed by AC1 and AC3.
- **S2** — The unknown key withheld. A key the tuple does not name is withheld whatever its name,
  so a key added to a case file later never reaches a scout until this tuple names it. That covers
  `probe_evidence`, `reinvention`, `decoys`, `classification`, `sha`, `short`, `point`,
  `reconstructed`, `core_sha`, `core_point_sha`, `ground_truth` and `control`, and a planted `hint`.
  Observed by AC2.
- **S3** — Unit 5 answered. Unit 5 AC7's first clause, that no printed case holds `ground_truth` or
  `control`, is superseded by this unit's AC1 and AC2, which observe the whole key set. Unit 5's
  acceptance ledger records, as a continuation line under its `- AC7` answer, the label
  `TOOL-dIndexedDesign-31 S3` and the backticked `SCOUTED_SEAM_INPUT_KEYS` token on that one
  physical line. Unit 5 AC7's two other clauses stand. Observed by AC4.

## 3. Non-goals (OUT)

- The `case_input` hook, `--blind`, the control rule and S3's harness refusal of a case key other
  than `id` and `input`: `TOOL-dIndexedDesign-5` S3 and S6. This unit changes one hook body and adds
  one constant.
- Any other instance's hook. `review-replay` declares none and stays not dispatchable; the
  `bug-class-intent` instance is `TOOL-dIndexedDesign-14`'s and declares its own.
- What a scout could find by reading its tree. Blinding binds what the scout is handed, which unit 5
  §5 already says.
- The report's left-shift text, a bug-class checklist entry for the class
  `withheld-value-recovered-from-a-derived-one`. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-5` — the `scouted-seam` instance's `case_input` hook and `--blind`, whose deny-list body S1 replaces with `derive_scouted_seam_input` over `SCOUTED_SEAM_INPUT_KEYS`, and AC7, which S3 supersedes in that unit's ledger (id 37)
- **hands-off** `TOOL-dIndexedDesign-46` — S1's required keys, which that unit types as non-empty strings (id 39)

## 4. Design

### Evidence

- The case blob `921345a50b49d8fb87687b3e411611d1d0b8e740`, tracked at
  `memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-3-cases.json`, read on
  2026-10-28 with its `// **Serves:**` line cut: 30 cases. Key counts: `id`, `short`, `repo`,
  `point`, `sha`, `sha_before`, `prompt`, `reconstructed`, `ground_truth` and `probe_evidence` 30
  each; `reinvention` 25; `slug` 22; `classification` 14; `core_point_sha` and `core_sha` 9;
  `decoys` 4; `control` 2. PINNED on 2026-10-28; AC1 re-derives the printed set at observation time.
- Case `incms-decor-texture` holds `probe_evidence` reading "'pick an image for a block property' put
  imageField #1 and MediaPickerField #7 of 146", and its `ground_truth` symbols are `imageField` and
  `MediaPickerField`. Its `reinvention.paths` names `packages/blocks/src/shared/decor.tsx`.
- The parent bench, TOOL-dLinkedLibrary-2 S11, dispatches one scout per case "over its tree and
  index". The tree is `repo` at `sha_before`, and `prompt` is the request, so the four keys are what
  a scout needs to search; `slug` names the build it was in.
- Unit 5 S3 refuses a case carrying any key but `id` and `input`, so the harness never sees a
  withheld key either way; the leak is inside `input`, which S3 does not open.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `SCOUTED_SEAM_INPUT_KEYS` | module constant, `replay_scorer.py` | none |
| `derive_scouted_seam_input` | the `scouted-seam` hook's function, named in unit 5's Inventory | `py.function`, answered OK by `lexicon.py --suggest` |

### Migration

None: no stored data changes. A results file scored before this unit lands was never produced, since
unit 5 S10's live run is at the close, after this order.

### Rollout

Live at its pass, order 11, one above unit 5's 10, beside `TOOL-dIndexedDesign-4`. Unit 5 S10's
reuse-bench run at the close reads the allow-list, so its figures are scored blind.

### Files touched (estimate)

- `tools/workflows/replay_scorer.py`: S1, S2 and the selftest arm §7 declares
- `memory/builds/dIndexedDesign/build/`: S3's ledger note, at the close

### Alternatives rejected

- **Extend the deny-list by the five leaking keys.** Lost to the planted-key test S2 states: a key
  added to the case file later, `hint` say, still reaches the scout, which is the class the finding
  names. The charter's `[security]` rule is deny by default.
- **Strip at the harness with S3's refusal widened.** Lost to unit 5's own split: the harness sees only
  `id` and `input`, so it cannot tell a leaked key inside `input` from a needed one.
- **Hand `id` inside `input`.** Lost to the evidence: ids such as `incms-decor-texture` describe the
  answer's subject, and unit 5 S6 already prints `id` beside `input`, never inside it.

## 5. Production-readiness checklist

- security — the fix is the security boundary itself: an allow-list at the one read that builds a
  scout's input, deny by default.
- perf / scale — one dict comprehension per case.
- error / empty / loading states — a case missing a required key refuses with exit 2 naming it; a
  case carrying only the four keys prints them all.
- observability — the refusal names the case and the key.
- risks — a scout that needs a fifth key reads less than before; the tuple is the one place to add
  it, and AC1 re-derives what prints.
- testing — AC1 over the real blob, AC2 and AC3 over a planted case set, AC4 at the close.
- migration — none.
- user docs — none under `help/`; `help/experiments.md` (unit 5 S9) names the blind verb and gains
  nothing here.

## 6. Acceptance criteria

- **AC1** — When `python replay_scorer.py --blind scouted-seam <cases src>` runs over the tracked
  case file holding blob `921345a50b49d8fb87687b3e411611d1d0b8e740`, and its output is piped to a
  `python -c` that unions every printed case's `input` keys, the union is a subset of `prompt`,
  `repo`, `sha_before` and `slug`, and 30 cases print.
  Red when: `probe_evidence`, `reinvention`, `decoys`, `classification`, `sha` or any other key
  outside the tuple prints.
  figure: 30 is DERIVED from the case file at observation time.
- **AC2** — When `--blind scouted-seam` runs over a planted case set, committed in a scratch
  repository, whose one control case and one plain case each carry a `hint` key and a
  `probe_evidence` key beside the four admitted keys, neither printed `input` holds `hint` or
  `probe_evidence`. With `derive_scouted_seam_input` staged back to "every key but `ground_truth` and
  `control`", both keys print.
  Red when: a key the tuple does not name prints, or the staged deny-list still prints nothing extra.
  fixture: a scratch repository under `%TEMP%/<short-name>`, since `<cases src>` must be tracked.
- **AC3** — When `--blind scouted-seam` runs over a planted case set whose plain case lacks
  `sha_before`, it exits 2 naming that case's `id` and `sha_before`, and prints no case.
  Red when: the case prints without the key, or the refusal names neither the case nor the key.
- **AC4** — When
  `grep -n "TOOL-dIndexedDesign-31 S3" memory/builds/dIndexedDesign/build/*TOOL-dIndexedDesign-5*acceptance-ledger*`
  runs at the close, it prints one line holding `SCOUTED_SEAM_INPUT_KEYS`, and that line sits under
  unit 5's `- AC7` answer.
  Red when: unit 5 AC7 is recorded on its two-key clause alone.
  permission: the ledger is written at the close.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `review-replay selftest` · `memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/workflows/replay_scorer.py · covers AC2 AC3 · `run_selftest`'s blind arm over a planted case set carrying `hint` and `probe_evidence`, staged by reverting `derive_scouted_seam_input` to the deny-list · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of this build, id 37
  (BLOCKER, item B1), repairing TOOL-dIndexedDesign-5 S6 and AC7.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-46, promoted by the round-1 spec audit of units 31 to 38; nothing else
  moved.

## 10. Reuse audit

The seam is unit 5 S6's `case_input` hook in `replay_scorer.py`, beside TOOL-dFairHearing-14 S2's
`case_evidence`; this unit fills one instance's hook body and adds no hook.
`python tools/codebase-map/reuse_lookup.py "pass only named keys of a case to a blinded agent"`
ranked `key`, `keys`, `read_conf_key` and `readConfKey`, each a config or merge-row key reader and
none a case-key filter, so no existing seam fits beyond the hook unit 5 lands. The scorer is unbuilt
at base, so no hit could name it.

Recall terms used: `python tools/memory-recall/query.py "how does a blinded experiment keep the answer out of the subject's input" --terms "blinded scout allow-list case_input ground_truth probe_evidence withheld key deny-list reuse bench"`
