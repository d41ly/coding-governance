# Acceptance ledger — TOOL-dFairHearing-2

**Serves:** journal TOOL-dFairHearing-2

Built against spec rev-2 at pass commit `e21580aac`, with the follow-up `37ff1d91b` the bug-class checklist forced, both carrying `Pass: TOOL-dFairHearing-2`. The main loop drafted this ledger at the close from the builder return and those two commit messages. Every observation is a scratch probe of the pass or a grep at its commit. No suite, gate or bar ran in the pass: the `New arm:` line on `tools/workflows/tier2-review.test.sh`, with its floor raised from 372 to 387, and the spec's legs are owed to the close, which records the arm's RED and GREEN here under a `Pass: none` commit.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-2
- AC1 — `tools/workflows/tier2-review.js` — a scratch node probe cutting the prelude as the suite cuts it let `preset: 'design-audit'` through, and refused `preset: 'whole-design'`, `preset: 7` and an empty string naming `unit-spec | design-audit`. `preset: 'unit-spec'` beside `kind: 'diff-review'` threw naming the diff kind. On base the same call threw `preset is not defined`
- AC2 — `gov:lens-slots design-audit` — the spec's `render_lenses.py` command put the literal's five keys in order, `coherence`, `grounding`, `reuse`, `failure-envelope` and `alternatives-and-cost`, and the `key:` and brief lines of the `unit-spec` and `diff-review` literals equal base's
- AC3 — `preset: 'design-audit'` — a whole-script run of `tools/workflows/tier2-review.js` over stub `agent` calls gave the design-audit finders the five design briefs and the default finders base's spec briefs. Base fans the same request over blast-radius, the `SPEC_LENSES` set
- AC4 — `preset` — the same probe read two different keys, and the default key equals base's, `spec-audit-r1-89f75f4b-e4499dd5`
- AC5 — `bash tools/workflows/check-verifier-fanout.sh tools/workflows/tier2-review.js` — at the tip `948e4141b` it exits 0 and its slot line counts 4 literals, not three: unit 18 added `whole-design`. A node probe read `PRESETS` as `design-audit`, `whole-design` beside the `gov:lens-slots` names `design-audit`, `whole-design`, so the two sets agree
- AC6 — `preset: 'design-audit'` — the complete return and the no-finding return each carry it, and RUN INTEGRITY names `preset: design-audit`
- AC7 — `grep -n "preset" tools/workflows/tier2-review.template.js` — the builder return records that both greps hold, and that the header block gained its `preset:` line
- AC8 — `git grep -n "preset: 'design-audit'" -- tools/` — at `e21580aac` it hit two lines of `tools/workflows/README.md`, which `37ff1d91b` rewrote. On the re-run every hit is in `tools/workflows/tier2-review.test.sh`
