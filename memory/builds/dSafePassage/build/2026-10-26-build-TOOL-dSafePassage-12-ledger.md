**Serves:** journal TOOL-dSafePassage-12

# TOOL-dSafePassage-12 — acceptance ledger

The unit as built, at spec rev-3. In `.github/workflows/remote-ci.yml` each of the four jobs gains
§4's two steps after its last git-only step (`origin/HEAD resolves before any bar command runs`) and
before its first step that runs Python: `the floor, read from its one declaration` (id `floor`,
working directory `tree` in `history-audit` and `held-plan`, `${{ env.PRIMARY_TREE }}` in `bar` and
`held`) and `Python at the floor`, `actions/setup-python@6d4fd22b20465ccc0f7354476588e8df7c9ca0e0 #
v7.1.0`. `bar` gains `the floor's preflight, the bar's first step` between the setup and the merge
bar. The header names the setup and the preflight under WHAT RUNS, and its permanent-gate sentence
now names the floor query. The pin was re-read at build time by `git ls-remote --tags
https://github.com/actions/setup-python` on 2026-10-26: v7.1.0 is still the newest tag and still
resolves to the sha §4 pinned on 2026-10-23, a lightweight tag (no `^{}` row) naming the commit.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node d
by the criterion's own command over the working file and over scratch copies with the staged break
§6 names; AC3's break ran in a fixture repository under `%TEMP%`, because the floor query reads
tracked files through `git grep`.

Owed at the close: `python resolver (behaviour + inline parity + idiom ban)` (TOOL-dSafePassage-11's
floor-query arm, which now reads four `python-version` lines of this file), `memory hygiene`, `spec
tokens (a spec's own names resolve)`. This unit adds no arm (§8 F1), so no RED-first observation is
owed for it.

**Evidences:** TOOL-dSafePassage-12
- AC1 — `awk '/^jobs:/{f=1;next} ...'` over the file printed `bar: 1`, `held-plan: 1`, `held: 1`, `history-audit: 1` and no other line; on a scratch copy with the `held` job's setup step deleted it printed `held: 0`.
- AC2 — `grep -cE 'uses: actions/setup-python@[0-9a-f]{40} # v[0-9]+\.[0-9]+\.[0-9]+$'` and `grep -c 'uses: actions/setup-python@'` each printed `4`; on a scratch copy with one pin staged as `@v7` they printed `3` and `4`.
- AC3 — `grep -c 'python-version: ${{ steps.floor.outputs.floor }}'` printed `4`; `python tools/lib/python_floor.py check` in this worktree named no line of the workflow and exited 0; in a fixture repository carrying the declaration, `python_floor.py` and the workflow with its first setup input staged as `python-version: '3.14'`, it printed `.github/workflows/remote-ci.yml:89: python-version: '3.14'` and exited 1.
- AC4 — `awk '/^  bar:/{f=1;next} ...'` printed, in order, `origin/HEAD resolves before any bar command runs` (122), `the floor, read from its one declaration` (125), `Python at the floor` (135), `the floor's preflight, the bar's first step` (139), `the merge bar, every leg guard ignored, walled inside the job limit` (142); on a scratch copy with the preflight moved below the bar step, the bar printed at 139 and the preflight at 142.
- AC5 — the `floor` step's `run:` body, cut from the file with `awk` and run under `bash` in a scratch directory with `GITHUB_OUTPUT` set to a scratch file: a declaration of `3.15` appended `floor=3.15` and exited 0; `3.15` then `x=1` exited 1 with `floor: tools/lib/python-floor.txt holds '3.15x=1', not <major>.<minor>` and the output file held no line; a CRLF `3.15` appended `floor=3.15`; an absent declaration exited 1 naming the file, no line written. The four jobs' `floor` bodies are byte-identical but for `working-directory`.
- AC6 — `grep -n 'python_floor.py\|setup-python\|preflight'` printed header lines 11-12, naming `actions/setup-python` and `bash tools/lib/python-floor.sh preflight` under WHAT RUNS, and lines 20-22, where the permanent-gate sentence names `python tools/lib/python_floor.py check` and no longer says that no permanent gate grades the file.
- AC7 — owed at the close: `git show "HEAD:.governance/install.json"` on the prepared merge after the main loop's `push-main.sh --prepare`; no unit pass runs the lander (§6's own permission line).
- AC8 — owed after the landing: remote CI's first run on the landed sha, the `bar` job's log showing the setup installing 3.15 and the preflight naming a 3.15 interpreter; only the lander's push to main runs it (§6's own permission line).
