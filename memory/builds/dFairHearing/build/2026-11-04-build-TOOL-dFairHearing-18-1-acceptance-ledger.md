# Acceptance ledger — TOOL-dFairHearing-18

**Serves:** journal TOOL-dFairHearing-18

Built against spec rev-3 and committed as the pass commit `b21501741`, whose parent is `d562f515e`. The main loop drafted this ledger at the close from the builder return `2026-11-03-build-TOOL-dFairHearing-18-1-builder-return.md`, and every observation below is that return's. No suite, gate, bar or selftest ran in the pass: the checks were scratch probes standing in for the `tier2-review self-test` leg and the `review-replay selftest` leg, and both `New arm:` lines' red-first observations and the spec's legs are owed to the close.

**Evidences:** TOOL-dFairHearing-18
- AC1 — `walk` — a node probe over the render's prelude ran these three criteria, and all 29 of its checks passed. Each `walk` refusal names its field
- AC2 — `deriveWalkSlices` — the same probe's cases for `deriveWalkSlices` passed
- AC3 — `deriveWalkGaps` — the same probe's cases for `deriveWalkGaps` passed
- AC4 — `verify:cells` — an AsyncFunction stub run of the whole render covered these three criteria, a dead walker and twin under the preset, and all 15 of its checks passed. A no-finding walk still sends one `verify:cells` batch
- AC5 — `cell-sample` — the same stub run passed this case: a refuted clean cell becomes an unverified `cell-sample` finding
- AC6 — `WALK_RULES` — the same stub run passed the walker-prompt cases. The return's one count is `WALK_RULES` at 7 in both the template and the render, and it does not state that the constant is defined once. At the tip `const WALK_RULES` is defined once, at `tools/workflows/tier2-review.js:1130`
- AC7 — amended rev-2 — the revision log's rev-2 line adds the hands-off edge to unit 23, which consumes unit 12's tag reader with its integer section, AC7 included. The tag reader returns the integer section 3 for the third case where the criterion's text expects the section-sign string, and the builder reused it and wrote no second definition. A python probe ran the reader over the criterion's refs, and a node probe of deriveAddressKey gave the same file and tag for the first ref
- AC8 — `--design-recall` — a python probe of the `--design-recall` entry over scratch fixtures exited 1 when both runs missed a plant and 0 once run 2 found it. The return states those exits and does not state the printed figures or the missed plant's `tag`. At the tip the `design-recall` arm of `--selftest` asserts `run 1: 2 of 3 · missed c`, the same for run 2 and the union, with exit 1, and `union: 3 of 3 · missed none` with exit 0
- AC9 — `--seed none` — the same probe exited 2 on a changed key, a missing run and a plant whose escaped flag disagrees with the seed, and 0 under `--seed none`. The return does not state that the run left the key unopened. At the tip the same arm asserts the exit 2 naming the `SHA-256` and the exit 2 naming the missing run. It does not grade whether the run left the key unopened
- AC10 — amended rev-2 — the revision log's rev-2 line adds the hands-off edge to unit 23, which replaces this criterion's render-diff clause, and the rev-3 line says that hand-off stands. The template and render diffs differ by one line, the new literal's token that the render fills with the five walker rows, and every other line matches. The return records the criterion's greps as holding
