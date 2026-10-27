# TOOL-dWellOiledMachine-74 — a kept return reused only for the same spawn input: the input print joins the spawn site's label

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 32 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-74-deviation-741.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-74-deviation-741.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-79 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 59, item H11, at HIGH. TOOL-dWellOiledMachine-8 S5's `readKeptReturn(a, label)` returns
`a.returns[label]`, and the site is the `agent()` label alone; tier2-review's verifier labels
`verify:ids-<first>-<last>` encode only an id range, and those ids shift when a dead lens is re-run,
the case TOOL-dDerivedDocket-29 S4 already closed for its own directory reuse with a batch print. On a
fresh relaunch old verify verdicts are then paired with new findings, and a review is certified that
never judged them. This unit makes the spawn input part of the key, so a kept return is handed back
only to a spawn whose input is the one that produced it.

## 2. Scope (IN)

- **S1** — The input print. The `gov_returns_js` block (8 S5, canonical in
  `tools/runtime/returns-block.js`) gains `deriveInputPrint(prompt, opts)`: the 8-hex FNV-1a of the
  canonical JSON of `[prompt, opts]` with `opts.label` left out. `deriveFnv1a` and `renderCanonical`
  move from `tools/workflows/tier2-review.template.js` (`:39-54`) into the block, so every carrier holds
  them once and tier2-review keeps calling them by the same names. Observed by AC1, AC4.
- **S2** — The keyed label. The block gains `renderKeptLabel(label, inputPrint)`, returning
  `<label> #<inputPrint>`, and every `agent(` call site of the three harnesses passes that as its
  `label`, so the spawn site 8 S2 reads from the agent's `.meta.json` carries the print, and the store
  keys a return by it with no change to the pack. Observed by AC2.
- **S3** — The read. `readKeptReturn(a, label, inputPrint)` returns
  `a.returns[renderKeptLabel(label, inputPrint)]` or `undefined`; every call site passes the print of
  the input it is about to spawn with. A kept return whose input differs is never returned, so that
  site spawns. Observed by AC2, AC3.
- **S4** — The risk line corrected. 8 §5's risk covers only a label that never matches again; spec 8
  takes a rev bump at this unit's pass naming the paired-with-wrong-input case and this mechanism, its
  §9 line naming this unit and finding 59. Observed by AC4.

## 3. Non-goals (OUT)

- No change to the store's file layout, the pack, or `read_returns`: the site label carries the print.
- No change to tier2-review's own directory reuse by batch print (TOOL-dDerivedDocket-29 S4).
- No reuse across a changed prompt template: a changed template changes the print, which is the point.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-8` — the `gov_returns_js` block, `readKeptReturn`, its carriers and the stub runner of its AC5, which this unit re-keys
- **hands-off** `TOOL-dWellOiledMachine-90` — the kept-return label, re-rendered with the print before the stage, `readKeptReturn` and its readers (findings 3, 21, 32, 43)

## 4. Design

### Evidence

- 8 S5 defines `readKeptReturn(a, label)` as `a.returns[label]` (`spec-8.md:58-65`), and 8 S7 passes a
  `{label: return}` map on a fresh relaunch (`spec-8.md:72-77`).
- tier2-review builds verifier labels from the id range alone
  (`tools/workflows/tier2-review.template.js:1365`), and its comment at `:1357-1361` says the ids
  shift when a dead lens is re-dispatched, which is why its directory reuse also checks a batch print
  (`:1364`, `:1369`).
- `deriveFnv1a` and `renderCanonical` live only in tier2-review (`:39`, `:49`); the build and unit
  harnesses carry neither (`grep -c deriveFnv1a` prints 0 in both).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `deriveInputPrint` | block function | `derive`, OK |
| `renderKeptLabel` | block function | `render`, OK |

### Files touched (estimate)

- `tools/runtime/returns-block.js`
- `tools/workflows/tier2-review.template.js`, `tools/workflows/tier2-review.js` (its render)
- `tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js` (its render)
- `tools/workflows/unattended-unit.js`
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-8.md` (S4's rev bump)

### Alternatives rejected

- **Storing the print in the return file and comparing at read.** The pack writes the store from the
  agent's transcript and never sees the harness's input, so it could only re-derive the print from
  the transcript's first message, a second derivation that can disagree with the first.
- **A second FNV-1a inside the block beside tier2-review's.** Two copies of one function in one
  script; S1 moves the one that exists.

## 5. Production-readiness checklist

- security — a review can no longer be certified with verdicts on findings it never judged.
- perf / scale — one hash of the prompt per spawn.
- error / empty / loading states — a label with no kept entry spawns, as today.
- observability — the agent's label shows its print, so a respawn after an input change is visible in
  the run journal.
- risks — every spawn's label grows by ten characters; readers that match a stage name by prefix keep
  matching.
- testing — AC1 to AC4 and the arm in §7.
- migration — none: kept returns from before this unit carry no print and are simply not reused.
- user docs — `help/runtime.md`'s store section (8 S10) names the print.

## 6. Acceptance criteria

- **AC1** — When `grep -n "function deriveFnv1a" tools/workflows/tier2-review.template.js returns-block.js`
  runs, the only definitions are inside the `gov_returns_js` block, and the inline parity row reports
  every carrier identical.
  Red when: a second definition exists outside the block.
- **AC2** — When the stub runner of 8 AC5 runs `tools/workflows/unattended-unit.js` with `returns`
  holding the unit's label under the print of the args it is given, no `agent()` call is made; with
  the same label under another print, exactly one `agent()` call is made and its label ends ` #<print>`.
  Red when: a kept return is reused for a different input, as `a.returns[label]` reuses it.
- **AC3** — When `python supervise.py --fixture --plant relaunch-changed-input` kills a review act after
  its verify stage, changes one lens's return and relaunches it `fresh`, the stub harness respawns the
  verify batch whose findings moved and reuses the others.
  Red when: the old verify verdicts are handed to the new findings.
- **AC4** — When `grep -n "TOOL-dWellOiledMachine-74" 2026-10-26-spec-TOOL-dWellOiledMachine-8.md`
  runs over spec 8, its §9 carries the rev line and its §5 names the wrong-input case.
  Red when: spec 8's risk line still covers only the safe direction.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/workflows/tier2-review.test.sh · covers AC2 · the stub run with a kept label under another print, staged on 8 S5's label-only read · none
New arm: tools/runtime/supervise.py · covers AC3 · the changed-input relaunch staged on a block whose read ignores the print · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 59 (H11).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-1
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-90.

## 10. Reuse audit

The seam extended is TOOL-dWellOiledMachine-8's `gov_returns_js` block, which every harness already
carries, and the fingerprint pair `deriveFnv1a` and `renderCanonical`
(`tools/workflows/tier2-review.template.js:39`, `:49`), moved into it rather than copied, the same
print TOOL-dDerivedDocket-29 S4 keys its reuse on. The probe
`python tools/codebase-map/reuse_lookup.py "reuse a kept agent return only for the same input"`
ranked `same`, `corpus_inputs`, `read_view_inputs` and `renderAgentLabel`, the last being the label
renderer S2 wraps; none keys a reuse by input, so the print pair is the seam.

Recall terms used: `python tools/memory-recall/query.py "when may a relaunched harness reuse a
persisted agent return" --terms "kept return readKeptReturn label batch print fingerprint relaunch
verify reuse persisted"`
