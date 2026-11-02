**Serves:** research TOOL-dSafePassage-81

# Brief: the lexicon offenders this build added over the pin

## The prompt

> At the close, the `lexicon naming predicates` leg (`python tools/lexicon/lexicon.py`) exits 1 at `83817478f` with `verb offenders 1281 over pin 1212`; at the build's base `60d90cb71` it reads exactly 1212. So the build added the red. BUILD-METHOD M10 adopts that discovery as a unit at once.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-81, which brings the lexicon leg back to its pin at the build's head by renaming each offender this build introduced to a declared verb (`python tools/lexicon/lexicon.py --suggest <name> --as <cell>` answers each), every caller moved with it. First derive the exact population: run `lexicon.py --list` at the base and at the head, each in a `git clone --shared` under the temp root, and join the two by file and name. A pair new at the head in a file this build did not change (`git diff --name-only 60d90cb71..83817478f`) is not renamed: find why it appears (a moved population, a changed arming, a parser difference) and state it, with the line that shows it. A name the canon cannot answer (UNRULED, no cluster) is a §8 fork with a recommendation, never a pin raise: a pin move is the owner's. The spec is Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16` (TOOL-dSafePassage-61 holds order 16 and stays non-terminal), carries `**Derived:** TOOL-dSafePassage-1`, declares no `consumes-from` edge onto a CLOSED unit, and has one mechanism, §6 criteria each with a Red-when, §7 gates with a `New arm:` line or the reason the leg's own pin is its arm, and §10 reuse. Add its row to the README `roster:units` table. TOOL-dSafePassage-72 to -78 and -80 are DEFERRED specs that will rename or add names in the same files; say in §4 how this unit's pass orders after them.

### Items
- The pairs new at the head in files this build changed: `tools/govkit/upgrade_steps.py` (about 51), `tools/govkit/selftest.py` (about 12), `.githooks/pre-push.test.sh` and `.githooks/pre-commit.test.sh`, `tools/lib/python_floor.py`, `tools/push-main.test.sh`, `tools/govkit/fixture_target.py`, `tools/govkit/fixtures/release-0/arms/arm_step.py`, `tools/govkit/govkit.py`, `tools/govkit/docs_leg.py`.
- The pairs new at the head in files this build did not change (other builds' scripts under `memory/builds/`): explained, not renamed.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no change to `.lexicon.conf`'s pin.

### Acceptance
The spec lists every new pair with its disposition and target name, the explained remainder with its cause, and is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in it other than check 9's stale build index.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
