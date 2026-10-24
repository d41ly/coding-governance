**Serves:** research PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-46

# Brief: the owner's four fork picks, and the dOrderedCharter half of the parent audit

## The prompt

> put the decisions to me

— owner, 2026-10-25. Asked the four open forks, the owner picked the recommended option on each:
spec 15 F4 "Own check on stderr (Recommended)", spec 31 F6 "Class row + dConvergedCharter
(Recommended)", spec 31 F7 "Ask dSafePassage unit 9 (Recommended)", spec 1 F4 "Probe first, then ask
(Recommended)". Then:

> Next audit things that look off in the parents' specs you found, fix where possible, land everything.

— owner, 2026-10-25. The audit record is
`memory/builds/dOrderedCharter/build/2026-10-25-build-PLAY-dOrderedCharter-1-parents-audit.md`. Its
dSafePassage half is fixed in the same commit by
`memory/builds/dSafePassage/prompts/2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md`: dSafePassage
unit 6 drops the `map_lib` first-shim-row mention, unit 9 routes retired seed rows through its
`retired-edited` arm and gives `read_policy_value` a `rev`, unit 1 adds the `policy` cap home form. So
spec 31's two asks are answered by those edits, not filed.

## The brief

### Goal

Mark the four forks resolved by the owner, make each spec read as its fork now decides, and fold the
audit items that sit in dOrderedCharter's own scope.

### Items

1. **Spec 15 F4.** Append `RESOLVED (owner, 2026-10-25): (a).` in the closed-paren form
   `memory/TEMPLATE-SPEC.md` gives, and state (a) directly where S5, §4 or the page point at the fork.
2. **Spec 7.** Where `core.exceptions: owner-only-expiring` points at spec 15's fork, state the settled
   proof (stderr is a terminal, through spec 15's check) instead of an open fork.
3. **Spec 31 F6.** `RESOLVED (owner, 2026-10-25): (a).`; the window is counted by dConvergedCharter from
   the `module-export` row's landing commit, and dSafePassage unit 6 no longer names this re-export as a
   shim row (its rev at this commit). **Spec 19 S9:** the hold is now spec 31's settled F6, not an open fork.
4. **Spec 31 F7.** `RESOLVED (owner, 2026-10-25): (a).`; dSafePassage unit 9 now routes a retired seed
   row through its `retired-edited` arm (its rev at this commit), so AC9 expects `retired-edited` with one
   order for an edited copy and `withdrawn` for an unedited one, consuming that unit.
5. **Spec 1 F4.** `RESOLVED (owner, 2026-10-25): (a).`, keeping the probe. Add the evidence that the
   live dGroundRules run's built catalogue (`origin/branch/unattended-dgroundrules-e47ae1` at `df4912bd`)
   holds `charter.practices` as `{ type = "set", item = "[A-Za-z0-9][A-Za-z0-9_.-]*", registry = ... }`,
   and its `check_value` admits a set member the `item` pattern matches, so the probe is expected to read
   source `file`; the probe still decides at the build run.
6. **Specs 11, 6 and 34: one reader of a consumer cap's home (audit P1).** dGroundRules' `budgets.py` has
   only `resolve` and `check`, and returns a `constant:` value only when the caller hands it in, so
   specs 6 and 11 each parse the `codex-instructions` census row. Spec 11 adds one verb to the policy
   kit's `budgets.py`, `home <cap>`, printing the census row's `home` and, for a `constant:` home, the
   constant's value read from that file. Specs 6 (shell) and 34 call it, and neither parses
   `caps.toml`. Spec 11 owns the verb, its AC and its fixture case in `tools/policy/check_policy.py`.
7. **Spec 32: the mirror and the guard see the overlay's policy rows (audit P4).** S7's rows reach the
   matcher, `validate` and `arm_schema`. State also that the mirror's staleness key gains the overlay
   blob's id (dGroundRules unit 5 records only the policy file's and the catalogue's) and that the
   guard's mirror shape compares `.governance/instructions.toml` with HEAD too (dGroundRules unit 19), or
   that the mirror omits `adopter.` keys and a JS reader cannot read them. Pick one, as a fork with a
   recommendation if it is not derivable.
8. **Specs 35 and 36: `instructions.exclude`'s default (audit P11).** The built catalogue holds
   `default = []` with `empty = "allowed"`; v2's "none" is the empty set. Say `[]` (none) wherever the
   specs say the default is `none`, and make spec 36's probe expect the `item` pattern above.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-10-25, the status kept `DEFERRED`, and add one §9 line
  naming the item and this brief. Specs 15, 31 and 1 also carry `ratified 2026-10-25` at the end of the
  Status line, as dSafePassage's owner-resolved specs do.
- Stay under the 49152-byte cap with the generated records rows the render adds; a spec over 47000
  bytes is trimmed in its authored prose.

### Acceptance

- `grep -n 'RESOLVED (owner, 2026-10-25): (a)'` prints spec 15's F4, spec 31's F6 and F7, and spec 1's F4.
- `grep -n 'budgets.py home'` prints spec 11's verb and the calls in specs 6 and 34.
- Each Status line is one rev higher, and §9 holds the new line.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index reset to HEAD
  with `git read-tree HEAD` and only your specs staged, names them only for findings a
  `gen_build_index.py --write` render cures. Delete the copy after.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No dGroundRules or dSafePassage file; no spec outside the eleven above.
- No commit, no stage into the real index, no deviation record: the main loop writes those.
- Probe copies only under the session scratchpad's `d<letter>/` folder you used before.

### Reuse

The re-ground brief `memory/builds/dOrderedCharter/prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md`
and the owner-forks precedent
`memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-1-owner-forks.md`.
