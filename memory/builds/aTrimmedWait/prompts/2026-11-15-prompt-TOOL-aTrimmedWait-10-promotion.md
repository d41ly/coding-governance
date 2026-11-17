# Promotion — TOOL-aTrimmedWait-10: the close bar's two product reds

**Serves:** research TOOL-aTrimmedWait-10

## The prompt

The close bar at `078eb5c58`, run once with `GATE_FULL=1` and no self-test suite, read RED on three
legs, each one this build's own:

- `spec tokens (a spec's own names resolve)`: unit 8 added the hygiene producer to the guard of
  `branch-guard self-test`, and three live specs of other builds (aScoutedSeam-2, dPinnedHandoff-1,
  dPinnedHandoff-3) name that file without naming the leg. The owner ruled, on 2026-11-15, to name
  the leg in those three specs' leg lines. The main loop made that edit as records; it is not this
  unit's.
- `policy check`: `arm_legacy_homes` reads `.memory-tree.conf STAGED_RENDER` as a new legacy home,
  and the legacy-home list is shrink-only; the leg's own remedy is to carry it as a key in
  `tools/policy/catalogue.toml`. The owner ruled, on 2026-11-15, for the catalogue key over dropping
  the switch: off by default, set on in this repository's `.governance/policy.toml`.
- `shell hygiene (a fork spent on builtin work)`: five files carry fork sites this build added.
  `.githooks/pre-commit` measures one `var-pipe` site over its registry row, `.githooks/pre-commit.test.sh`
  one unregistered `cat-file` site, `tools/memory-tree/check-memory-hygiene.sh` one `var-pipe` site
  over its row, `tools/roles/adopt-roles.test.sh` two unregistered `pure-fn-subst` sites, and
  `tools/workflows/unattended-build.test.sh` two `printf-subst` sites over its row.

## The brief

### Goal
Author the spec for TOOL-aTrimmedWait-10, a repair unit that turns the `policy check` and the
`shell hygiene (a fork spent on builtin work)` legs green with no other verdict moved.

### Items
1. The switch unit 3 reads moves from `.memory-tree.conf` to one key of the policy catalogue, read
   through the memory-tree kit's one policy reader, `tree_lib.read_policy_value`. The key's default
   is off; this repository's `.governance/policy.toml` sets it on; the mirror `.governance/policy.json`
   is re-rendered by its own tool. `STAGED_RENDER` leaves `.memory-tree.conf` and the kit's conf
   example, and `help/commit-render.md` names the key. The key's name is graded by the lexicon
   before it is written. Unit 3's arms in `gen_build_index.py --selftest` keep their verdicts with the
   switch read from the key. A tree with no policy kit reads the switch as off.
2. Each fork site the shell-hygiene leg names is converted to its no-fork form, so every count falls
   back to its registry row and no row is added or raised.
3. Acceptance criteria a pass can observe with a fixture or a probe; each new suite arm on a `New arm:`
   line in section 7, observed RED-first by the main loop at the close.

### Acceptance
- `python tools/check-spec-tokens.py --spec <the new spec>` exits 0.
- `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-10` prints its
  clean line.
- The pass shows `python tools/policy/check_policy.py` and the leg argv of
  `shell hygiene (a fork spent on builtin work)` in `tools/gate-legs.json` each exiting 0.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
No verdict change beyond the two legs named. No edit to the legacy-home list or to a waiver or
registry row. No other key of `.memory-tree.conf` moves.

### Limitations
Copied from the build's brief: measurements on node a, one at a time; long suites on a frozen clone.

### Reuse
`tree_lib.read_policy_value` and its callers in `tools/memory-tree/routed_commits.py`; the
catalogue's existing `memory.` keys for shape; the no-fork forms the shell-hygiene leg prints.
