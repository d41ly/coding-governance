# Acceptance ledger — TOOL-dFairHearing-13

**Serves:** journal TOOL-dFairHearing-13

Built against spec rev-3 and committed as pass commit `864f43d25`, at parent `4c1f75d92`. The main loop drafted this ledger at the close from the builder return `2026-11-02-build-TOOL-dFairHearing-13-2-builder-return.md` and the pass commit's message; nothing below was observed again for it. The first return, `2026-11-02-build-TOOL-dFairHearing-13-1-builder-return.md`, committed nothing, and its findings led to rev-3, which rewrote AC2 and AC4 and re-checked AC1's pin before this pass, so every line reads the rev-3 text. No suite, gate or bar ran in the pass: both `New arm:` lines, their RED-first observations, the floor of 372 and the spec's legs are owed to the close.

**Evidences:** TOOL-dFairHearing-13
- AC1 — `tools/workflows/render_lenses.py` — rendering the template over the shipped catalogue gave `key:` and brief lines identical to those in `git show 3708a705:tools/workflows/tier2-review.js`
- AC2 — `git diff -U0` — against the parent it shows no change outside `//` comment lines except the two marked opening lines, and the live copy differs from the new render only by the same token substitutions as before
- AC3 — `SLOTS` — with a sixth slot planted the gate printed the line naming `unit-spec` and 6, and exited 1
- AC4 — `slots` — adding an opt-in row left the render byte-identical, and the gate printed `slots — 2 lens-slot literal(s), each holding 5` and exited 0
- AC5 — `check-verifier-fanout.sh` — a fixture whose strings carry punctuation and template spans, with a trailing comma, read 5
- AC6 — `no lens-slot literal` — an unmarked whole-tree fixture repository at `%TEMP%/fh13`, since removed, printed the line and exited 1
- AC7 — `render_lenses.py` — the new `runLensArms` block, run on its own over this kit, passed 15 of 15, the eleven refusals included
- AC8 — `LENS_SLOTS` — the grep counted 2 in `tools/workflows/kit.toml` and 3 in `tools/workflows/check-protocol-parity.test.sh`
- AC9 — `one source` — both hits name `lenses.toml`, and `gov:lens-slots` counts 1 in `memory/map/features/agent-cap.md`
