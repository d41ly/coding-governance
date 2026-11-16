**Serves:** research TOOL-aLightenedLoop-8

# Reconcile — TOOL-aLightenedLoop-8: origin/main merged in, and unit 3's input-keyed cache ported onto the split spec-token check

## The prompt

> Reconcile and land

> The reconcile with origin/main conflicts in `run_spec_token_check`: aBriskDeclaration split it into an async start half and a read half, keyed before the run, while aLightenedLoop unit 3 re-keyed its cache on the checker's recorded inputs, with a stability bracket after the run. How should the reconcile resolve it?

Answer: "Port unit 3, run driver suite (Recommended)"

## The brief

### Goal
Merge `origin/main` into `branch/alightenedloop-eb7b8b` and resolve every conflict. In `tools/unattended/unattended.sh`, port TOOL-aLightenedLoop-3's spec-token cache, as TOOL-aLightenedLoop-6 repaired it, onto aBriskDeclaration's split of `run_spec_token_check` into `init_spec_token_check` and the read half (TOOL-aBriskDeclaration-1 S3, S4). The merge's own changes stay as main shipped them, and unit 3's verdicts stay as its spec states them.

### Items
1. The merge: `git merge --no-ff origin/main`. A trial merge at `aebbb4a72` conflicted in five files:
   - `memory/project/readme-contract.txt`: keep every row from both sides.
   - `memory/guides/SESSION-KICKOFF.md`: a `last-audit` re-stamp at this branch's HEAD, as the manifest's stamp rule says.
   - `tools/template-size-limits.txt`: the protocol row becomes the merged render's measured bytes, with both raises named in its comment. A run's raise is allowed on the file's own terms, with a `memory/DECISIONS.md` row.
   - `tools/check-spec-tokens.test.sh`: `FLOOR_ASSERTIONS` becomes the reconciled sum, both sides' additions over their common base, each named. The two sides' comments disagree on that base, 245 against 247, so measure it.
   - `tools/unattended/unattended.sh`: item 2.
2. The port. In the merged split:
   - The start half derives the lookup key over the existing input record (`derive_spec_token_key` with the record argument, unit 3's three-argument form, which the merge keeps), compares it with the recorded key, and skips on a match.
   - The start half also reads the tree state before the checker starts, and starts the checker with `SPEC_TOKENS_INPUTS` set to the record path, removing the stale record first.
   - The read half, after an admitted verdict, derives the key over the new record and only then re-reads the tree state, exactly as unit 6 S3 ordered it. It records the key only when the two states match and the record replays. Otherwise it prints the same one-line not-recorded reasons unit 3 and unit 6 print.
   - The start/read split, its silence, `remove_spec_token_check` and main's refusal order all stay exactly as main has them.
   - The comment block states the merged design once.
3. The suites: `tools/unattended/unattended.test.sh` holds main's split arms (aBriskDeclaration A1 to A6) and this build's cache arms (unit 3's inverted steps a, b and c, and unit 6's raced and popen stubs). Each must still say what it says against the merged driver. Reconcile `FLOOR_ASSERTIONS` and its shard floors as sums, each named.
4. Every other auto-merged file in the merge must keep both sides' intent. In particular: `tools/unattended/stop-guard.js`, `check-unattended.sh`'s allow-list, the unattended templates (re-render the copies with the kit's adopter), `tools/check-spec-tokens.py` and `tools/policy/check_policy.py`. Regenerate the generated outputs (`bash tools/run-gates/run-gates.sh --regen`, `gen_build_index.py --write`, `gen_map.py --write`).

### Acceptance
- The merge commit has both parents and no conflict markers (`git grep -n '^<<<<<<< '` prints nothing).
- `bash -n tools/unattended/unattended.sh` passes.
- A scratch-fixture probe of the merged `run_spec_token_check` shows:
  - a skip on an unchanged input record;
  - a re-run when an input moves;
  - no recorded key when the tree moves inside the bracket;
  - the "cannot be replayed" line on a popen record;
  - main's start-before-read ordering.
- The unattended driver suite, pooled, and the merge bar are the main loop's, after this pass.

### Gates
The merge bar, and `bash tools/unattended/run-unattended-gates.sh --pooled`, at the main loop.

### Non-goals
No change to aBriskDeclaration's behaviour beyond what the port needs, and no change to unit 3's or unit 6's verdicts or line texts.

### Limitations
The build brief's limitations hold: `memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md`. Never write under `memory/builds/dDeclaredLoop/`.

### Reuse
`tools/unattended/unattended.sh#init_spec_token_check` and `tools/unattended/unattended.sh#derive_spec_token_key`, as merged; unit 3's and unit 6's acceptance ledgers.
