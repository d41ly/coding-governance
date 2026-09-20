# TOOL-aProbedUnit-1 — acceptance ledger

**Serves:** journal TOOL-aProbedUnit-1

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite, per the build README's rule five. The one check the pass verified with is AC6's double,
sourced from the suite and run alone, seconds; it stands in for the harness suite whole.

**Evidences:** TOOL-aProbedUnit-1
- AC1 — `grep -cF "NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS" tools/workflows/unattended-unit.js` — printed `1` at the tip and `0` at base; the comment above the block does not repeat the phrase. Leg half, `bash tools/check-install-prefix.sh` — observed at --close; the paragraph spells no path
- AC2 — `grep -cF "No gate, suite or bar runs inside a unit pass"` over `tools/workflows/unattended-build.template.js` and `tools/workflows/unattended-build.js` — each printed `1`; the render came from `bash tools/workflows/check-protocol-parity.test.sh --render --tracked-only`, the argv `tools/workflows/kit.toml` `[[regenerate]]` names
- AC3 — `git diff --cached --name-only` before the commit listed both `tools/workflows/unattended-build.template.js` and `tools/workflows/unattended-build.js`, the set `git show --name-only --format= HEAD` reads on the pass commit. Leg half, `bash tools/workflows/check-protocol-parity.test.sh` — observed at --close
- AC4 — `grep -cF "No gate, suite or bar runs"` over `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md` — each printed `1`; `grep -cF "Then the diff-scoped" memory/guides/BUILD-METHOD.md` printed `0`; the render came from `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. Leg half, the `kit/dogfood doc parity` leg — observed at --close
- AC5 — `wc -c < memory/guides/BUILD-METHOD.md` printed `26846` and `wc -l` printed `341`, the section 4 pins exactly; `tools/template-size-highwater.txt` reads `26941` and `tools/template-size-limits.txt` reads `27648` for the file, so 95 under the high-water and no `--bump` owed. Leg half, `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` — observed at --close
- AC6 — `run_wf` and `CHILD_ARGS` sourced from `tools/workflows/unattended-build.test.sh` into a scratchpad shell and the child traced in `unattended` mode, then `grep -c "NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS"` — printed `0` against the base child with the new `has` arm reading `FAIL`, and `1` against the landed child with the arm reading `ok`; `grep -cF "NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS" tools/workflows/unattended-build.test.sh` printed `0` at base and `1` at the tip. This is the ONE check the pass ran, and it stands in for the harness suite
- AC7 — `grep -cF "ordered to run no gate, suite or bar inside its pass"` over `tools/unattended/SKILL.template.md` and `.claude/skills/unattended/SKILL.md` — each printed `1`; the render came from `bash tools/unattended/adopt-unattended.sh`. Leg half, `bash tools/unattended/adopt-unattended.sh --check` — observed at --close
- AC8 — `git diff --cached --name-only` before the commit listed both `memory/guides/BUILD-METHOD.md` and `memory/guides/SESSION-KICKOFF.md`; `git diff --cached -- memory/guides/SESSION-KICKOFF.md | grep -c '^+last-audit:'` printed `1`; `git grep -lE '^\*\*Status:\*\* CLOSED' -- memory/builds/aProbedUnit/spec/` listed this unit's spec. The commit message carries the `manifest-audit:` delta line. Leg half, `bash skills/session-kickoff/manifest-check.sh` check 5 — observed at --close

## What this ledger does not evidence

No parity leg, size leg, install-prefix leg, manifest ratchet or harness suite ran inside this
pass; every one of those is `--close`'s and each row above says so. The three renders were made
by their renderers and not diffed by their legs. The build README's authored roster row for this
unit moved `PLANNED` to `CLOSED` beside the spec header, which nothing grades and 68 prior rows do.
