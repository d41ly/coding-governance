# TOOL-aWokenSentinel-14 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-14

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite, per the build README's rule three. The pass verified with the direct checks the spec's
section 7 names for it — `seed()` extracted from the adopter suite by `sed -n '/^seed() {/,/^}/p'`
and run by hand as one function over `%TEMP%/aws14/base` (the function at `807a39b4`, this unit's
parent) and `%TEMP%/aws14/tip` (the working tree), the adopter's `--check` run once from each,
the greps of AC2 and AC3, and `gotchas.py --check` with `--for-paths` standing in for AC4's
`--for-diff` until the commit exists. `bash -n` over the edited suite file passed, and
`git diff | cat -A` over it counted zero CR bytes.

**Evidences:** TOOL-aWokenSentinel-14
- AC1 — `git -C %TEMP%/aws14/tip log -1 --format=%ct` printed `1789928943`, exit 0, and `git -C %TEMP%/aws14/tip status --short` printed nothing, so the commit took everything the function wrote; over `%TEMP%/aws14/base`, seeded by the parent's function, the same `log` printed `fatal: your current branch 'main' does not have any commits yet` on stderr and nothing on stdout, exit 128. OBSERVED.
- AC2 — `bash tools/unattended/adopt-unattended.sh --check` run once inside each fixture straight after the seed exited 1 from both and printed one line from both, `SKILL.md is not rendered`, identical modulo the fixture's own path; run again after `adopt-unattended.sh` rendered each, both exited 1 with the one line `gate-guard.fragment.json is missing from the kit`, identical modulo the path — the seed at this order copies no fragment, which is spec 3's break at its order 6 and not this unit's. `grep -c 'git commit' tools/unattended/adopt-unattended.test.sh` printed `1`; over `git show 807a39b4:tools/unattended/adopt-unattended.test.sh` it printed `0`. `grep -c 'GIT_CONFIG_GLOBAL=/dev/null'` over the same pair printed `2` and `0`. OBSERVED.
- AC3 — `grep -c 'HEAD is born'` printed `1` over `spec/2026-09-16-spec-TOOL-aWokenSentinel-3.md` and `2` over `spec/2026-09-16-spec-TOOL-aWokenSentinel-4.md`; both folds were landed by the disposals that reached rev-2 of those specs, and this pass wrote neither file. OBSERVED.
- AC4 — `python tools/memory-tree/gotchas.py --for-paths tools/unattended/adopt-unattended.test.sh` listed `borrowed-seed-inherits-its-head-state` with its record path; `gotchas.py --report` printed `unanchored : 0` and the INDEX row shows 3 anchors; `python tools/memory-tree/gotchas.py --check` exited 0 after `gotchas.py --write` rewrote `memory/gotchas/INDEX.md` (71 records). The `--for-diff HEAD~1..HEAD` reading is taken after the commit, in the pass's checklist step. OBSERVED.
- AC5 — the `unattended adopter e2e` row of the close's kit-gate run. observed at --close.

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg or install-prefix leg ran inside this pass; every one is
`--close`'s and each row above says so. The adopter suite was not run whole: its arms over the
committed seed are AC5's, read from the close's runner row, and unit 19's floor is not built at
this order. The rendered `--check` refusal on the missing fragment is the same refusal at base and
at tip, so it is not a change this commit made; it is the state spec 3's `fx` arm names as its
break. No identifier was minted, so no lexicon query was owed. The build README's authored roster
row for this unit moved `PLANNED` to `CLOSED` beside the spec header.
