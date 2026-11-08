# Acceptance ledger — TOOL-dFairHearing-3

**Serves:** journal TOOL-dFairHearing-3

Built against spec rev-3 at pass commit `9ce7710ab`, with the follow-up `b620b6327` the bug-class checklist forced, both carrying `Pass: TOOL-dFairHearing-3`. The main loop drafted this ledger at the close from the builder return and those two commit messages. Every observation is a scratch probe of the pass or a command it ran over the built tree. No suite, gate or bar ran in the pass: the two `New arm:` lines, on `tools/workflows/tier2-review.test.sh` with its floor raised to 411 and on `tools/workflows/unattended-build.test.sh` with its floor raised from 899 to 903, and the spec's legs are owed to the close, which records each arm's RED and GREEN here under a `Pass: none` commit.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-3
- AC1 — `optIn` — a scratch prelude probe of `tools/workflows/tier2-review.js`, standing in for the self-test, observed all five shape cases as the spec states them: `optIn: {}` proceeds and the malformed values throw
- AC2 — `optIn: { topology: 'blast-radius' }` — a scratch render with `topology` shipped, run as an AsyncFunction over stub agents, fanned `coherence`, `grounding`, `reuse`, `topology` and `failure-envelope`, with `topology`'s brief in blast-radius's slot, and its return carried the swap
- AC3 — `{ coherence: 'reuse' }` — that probe's four refusals, this one with `{ portability: 'reuse' }`, `{ topology: 'nope' }` and `{ topology: 'reuse', 'adopter-migration': 'reuse' }`, each threw before any `agent` call, each with its wording
- AC4 — `optIn: { portability: 'seams' }` — a light diff swap ran `correctness`, `portability` and `verification`, and skipped `security` and `intent`
- AC5 — `optIn: { topology: 'blast-radius' }` — with it the key differs, and without it the key equals base's, on spec and diff runs
- AC6 — `bash tools/workflows/check-verifier-fanout.sh <render>` — over the scratch render this pass's six opt-in catalogue produced on 2026-11-02 it exits 0 and reads 3 literals of 5. A fresh render of that catalogue at the tip refuses at `render_lenses.py` rule 9, because the catalogue predates unit 18's `whole-design` literal, so this figure is the old render's
- AC7 — `{"preset": "unit-spec"}` — `review_pin.py` ran on the CLI with the exact cases and printed the five lines the criterion states. The hands-off edge to TOOL-dFairHearing-32 at rev-3 re-pins this criterion's arm and changes none of its text
- AC8 — `SPEC_SUBJECT_PATH` — `review_pin.py` exited 2 on each refusal, naming `SPEC_SUBJECT_PATH`, `--opt-in` and `--subject`
- AC9 — `tools/workflows/unattended-build.js` — a node probe's `workflow()` stub received both keys, or neither when none were passed
- AC10 — `OPTIN_LENSES` — a tomllib probe read the six rows of `'tools/workflows/lenses.toml'` as the table states, each `optin = false` with `default_in = []`, and the shipped `OPTIN_LENSES` is empty
- AC11 — `grep -n "losing test" memory/builds/dCalibratedLens/BACKLOG.md` — it found the ask row, TOOL-dCalibratedLens-19, which names the six lenses. At the landing reconcile on 2026-11-08 the ask became TOOL-dCalibratedLens-56, the next id that build's index reported, because its own run had meanwhile minted TOOL-dCalibratedLens-19 for a unit. `optIn` appears 7 times in `tools/workflows/README.md`
