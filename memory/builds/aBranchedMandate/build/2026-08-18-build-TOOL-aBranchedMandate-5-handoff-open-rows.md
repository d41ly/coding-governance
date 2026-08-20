# Handoff — the six rows aBranchedMandate opened and did not build

**Serves:** none — a handoff for a SEPARATE session; the six rows it details are OPEN backlog rows this build never specced, so it holds no spec to serve

Written at the close of the `aBranchedMandate` unattended run (landed on `main` at `038ff91`) for a
SEPARATE session to spec and build. Every row below was MEASURED during that run, not suspected.
Each entry gives the reproduction, the fix shape, and the gate that should hold it — but **re-measure
before speccing**: `main` moved under this build five times in one day, and two of this run's own
findings were refuted by re-measurement.

## Before you start

- These are SIX rows, and `memory/HYGIENE.md` M2's rule is one mechanism per unit. Do not fold them
  into one spec because they are all small.
- Two are in `tools/unattended/` (`-8`, `-9`) and touch the same file. Sequence them; do not run
  their passes concurrently (M6's parallelism rule — their write sets intersect).
- `memory/backlog/TOOL.md` was at **20464 B against a 20480 cap** when this run finished, with **zero**
  terminal rows available to rotate. Closing any row frees rotation headroom; opening one does not
  fit. Plan the rotation before you plan the rows.

## The rows

### `TOOL-aBranchedMandate-5` — Tier 1 — the third adopter has no empty-render guard

`tools/drift-audit/adopt-drift-audit.sh` renders to a temp file and diffs it with **no `[ -s ]`
test** — verified still true at `038ff91` (`grep -c '\-s "\$TMP"'` returns 0). An empty render
against an equally empty Skill is a PASS, which is the green-by-absence shape the kit refuses by
name elsewhere. `adopt-unattended.sh:170` has the guard; `adopt-memory-recall.sh` gained it in
`TOOL-aBranchedMandate-1`. This is the third instance of a three-copy idiom.

**Fix shape:** port the `[ -s "$TMP" ]` refusal from `adopt-unattended.sh`, with its message.
**Gate:** an arm in that kit's selftest asserting an empty render REDS. Note the trap unit 1 hit —
the fixture must construct emptiness deliberately; a fixture that hopes for it passes with the fix
reverted.

### `TOOL-aBranchedMandate-6` — Tier 1 — the selftest leaks its scratch repos on Windows

`tools/memory-recall/selftest.py` cleans up with `shutil.rmtree(ignore_errors=True)`, which cannot
remove read-only git objects on Windows, so every run leaks ~30 scratch repos. **3,616 measured** in
`%TEMP%` on node `a`; each is a `.git/objects` skeleton. `t_adopter_layout` nests one level, so a run
leaks twice over. The manifest's §B already records the consequence — a `TMPDIR` holding tens of
thousands of entries makes the full bar time out — and its guidance is to point `TMPDIR` elsewhere,
NOT to delete the shared one.

**Fix shape:** an `onerror` handler that clears the read-only bit and retries, which is the
documented `rmtree` idiom. **Gate:** an arm asserting the scratch root is gone after a run.

### `TOOL-aBranchedMandate-8` — Tier 2 — `--preflight` clobbers a LIVE run-state file

Reproduced on this run's own record: `--preflight` on a slug whose `RUN.md` is NON-terminal
overwrites it in place, losing the keepalive id and re-pinning the anchor evidence. `dClosedLexicon`
added rotation for a TERMINAL record; a live one is still clobbered. The damage here was recoverable
only because the record was committed and could be restored from `HEAD`.

**Fix shape:** refuse, or rotate, a non-terminal record — decide which, and say why in the spec.
Tier 2 because it is a write path in the authorization kit. **Gate:** an arm that preflights twice
and asserts the first record's keepalive id survives.

### `TOOL-aBranchedMandate-9` — Tier 2 — rotation writes before refusals that can still fire

`--preflight`'s `GIT mv -f` rotation and `scaffold_runmd` run BEFORE two `region` validations and the
`set_fact`/`stage_or_fail` block, each of which can `return 1`. A malformed build-README marker pair
— a data condition a conflicted three-way merge can commit — leaves the record archived, an untracked
phase-less `RUN.md` on disk, no repair verb, and every later verb wedged. This contradicts the
function's own "NOTHING is written until every precondition above has passed" and `fail 29`'s
"nothing was moved".

**Fix shape:** hoist both region checks above the write gate. The review that found it called the fix
free. **Gate:** an arm with a malformed marker pair asserting the tree is byte-identical after the
refusal.

### `TOOL-aBranchedMandate-10` — Tier 1 — the map adopter's template contradicts itself

`tools/codebase-map/map_extractors.template.py` unions the two JS scans with a bare `+` while its own
instruction one line above says "Dedupe the union on (id, file)". Gov's own `_build_js_layer` dedupes.
An adopter copying the template gets duplicate symbols. **Re-measure first** — my grep for this at
`038ff91` did not match, so either the line moved or upstream fixed it.

**Fix shape:** dedupe in the template, matching `_build_js_layer`. **Gate:** the codebase-map selftest.

### `TOOL-aBranchedMandate-11` — Tier 1 — an unreachable skip branch in the deployer

`tools/govkit/govkit.py`'s `blocked` skip reason and its `_resolve_skip_destinations` branch are
unreachable behind `cmd_apply`'s early merged-rule refusal. The selftest arm asserts the refusal
text, not the skip path — so the dead branch is scored as covered.

**Fix shape:** either make it reachable or delete it; an unreachable branch that an arm appears to
cover is worse than no branch. **Gate:** `tools/govkit/refusal_join.py` already enumerates refusal
branches by anchor — check whether this one is in its population.

## What NOT to re-open

`gate-logs/` is **not** shared across worktrees. This run reported it as a defect twice and
retracted it on measurement: `run-gates.sh:34` composes its log dir from `git rev-parse --git-dir`,
which in a linked worktree is `.git/worktrees/<name>`. The struck record is in this build folder.
`AGENTS.md`'s claim about `gate-last-failure.txt` is correct.

## One more, unrowed and unmeasured

`build-complete` requires a `<!-- roster:units -->` pair, and most build READMEs in this tree predate
it — this build's did, and its `--close` blocked with a bare "unmet" until the pair was added by hand.
`TOOL-aBranchedMandate-13` made the refusal name the region, which is legibility, not migration. The
open question is whether existing build folders should be migrated or left to fix themselves on their
next unattended run. That is an owner call, not a defect, which is why it has no row.
