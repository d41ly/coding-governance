**Serves:** research TOOL-dSafePassage-1 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-13 TOOL-dSafePassage-26

# Brief: four dSafePassage specs fixed for what dOrderedCharter's re-ground found

## The prompt

> Next audit things that look off in the parents' specs you found, fix where possible, land everything.

— owner, 2026-10-25, after picking (a) for dOrderedCharter spec 31's F6 ("Class row + dConvergedCharter")
and F7 ("Ask dSafePassage unit 9"), in the session that re-grounded dOrderedCharter's specs
(`memory/builds/dOrderedCharter/build/2026-10-25-build-PLAY-dOrderedCharter-1-parents-audit.md` lists
every item and where it is fixed). dSafePassage's run claim is stale since 2026-10-23, so its specs are
fixed here; dGroundRules' run is live on another node, so no dGroundRules file is touched.

## The brief

### Goal

Fix the five dSafePassage defects dOrderedCharter's re-ground found, two of them the owner's picks, in
four specs. Each spec's design otherwise stays as it is.

### Items

Read the audit record first,
`memory/builds/dOrderedCharter/build/2026-10-25-build-PLAY-dOrderedCharter-1-parents-audit.md`, then
each spec you revise and the units it cites. dGroundRules' built code is on
`origin/branch/unattended-dgroundrules-e47ae1` (read it with `git show <ref>:<path>`, never check it out).

1. **Spec 1, P2: the `policy` home form.** S8 (owner-resolved F12 (a)) rewrites `tools/policy/caps.toml`'s
   seven `limits:` rows to a `policy` home form, a value held only under `budgets.<cap>`. dGroundRules
   unit 9's data model defines four forms only, and the built `tools/policy/budgets.py` on the live
   dGroundRules branch holds `HOME_FORMS = ("limits", "file", "conf", "constant")`. State in S8 and in
   Files touched that this unit adds the `policy` form to `budgets.py`'s `HOME_FORMS` and to the census
   reader's and `arm_cap_census`'s join, and spell the row's `home` value (for example `policy:`). An
   AC observes it: a census row with the `policy` home resolves its value from `budgets.<cap>`, and
   `arm_cap_census` stays green on gov's tree after S8.
2. **Spec 1, P7: what `step-rows-frozen` does not check.** S9 freezes the bytes of every program a
   landed argv names, not the modules that program imports, so a landed step's behaviour can still
   change through an import. State it once where the spec lists what its arms do not check. Do not
   widen the freeze: dOrderedCharter spec 31 keeps its class reader in an imported module on purpose.
3. **Spec 1 size.** The spec is near the 49152 class cap and the index render adds records rows. Bring
   `wc -c` to at most 47800 before you return, by cutting authored prose outside the `gen:` regions.
   Change no criterion, decision or Carries line.
4. **Spec 6, the owner's F6 pick.** Drop §3's naming of dOrderedCharter's `map_lib` re-export among the
   first shim rows (`:89-91`). By the owner's pick, that re-export is held by dOrderedCharter spec 31's
   `module-export` class row and its window is counted by dConvergedCharter, so no `[[shim]]` row
   carries it. Keep dWellOiledMachine's `/unattended` shim as the named first row.
5. **Spec 9, the owner's F7 pick: seed rows.** The arm before the write loop takes "both a first-time
   engine row and a row already carrying the role" (`:127-128`), and the seed override in
   `tools/govkit/govkit.py:9988-10000` (`UPDATE_ROLE` maps `seed` to `report-reseed`, `:8480`)
   rewrites a seed row's verdict after the grid, so an edited seeded copy gov stops shipping reads
   `patched` with no order. Route a retired seed row, one whose source gov no longer ships, through the
   `retired-edited` arm before that override: edited, it reads `retired-edited` with one order under
   `order`; unedited, `withdrawn`. Add a fixture plant (an edited and an unedited retired seed) and an
   AC. A seed row gov still ships keeps today's override.
6. **Spec 9, P3: `read_policy_value` takes a revision.** Give it `rev=None`, passed to `policy.py get` as
   `--rev <rev>` when set, its default reading the landed revision as now. State it where the helper is
   defined; specs 6 and 13 call it without `rev` and need no change beyond what their text already says.
7. **Spec 13, P8: the docs leg's row sources and the `none` shape.**
   - S1 and S2 name a closed list of row sources. Make the source an extension point the way
     dSafePassage unit 10 makes class readers one: a `[[class]]` row of `tools/govkit/usage.toml` may
     name a `rows` reader as `<path under the tool root>:<function>` returning the members' usage
     rows from their own registry, so a later class whose registry states its usage joins without a
     `[[usage]]` row restating it.
   - State how a class whose usage shape is `none` spells `rows` (absent, or a literal), once.
   - Fix the hand-off text that asks later builds to add "its members' rows" to `usage.toml` so it agrees
     with S2's no-restating rule.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-10-25, the status kept `DEFERRED`, and add one §9 line
  naming the items and this brief.
- Replace each now-false sentence where it stands.
- Stay under 49152 bytes; spec 1 at most 47800 (item 3).

### Acceptance

- `grep -n 'HOME_FORMS\|policy:' <spec 1>` prints S8's new form; spec 1's `wc -c` is at most 47800.
- `grep -n 'map_lib' <spec 6>` prints no line naming it a first shim row.
- Spec 9 names seed rows in its arm, its fixture plants both retired-seed cases, and `read_policy_value`
  carries `rev`.
- Spec 13's S1 or S2 states the `rows` reader form and the `none` spelling.
- Each Status line is one rev higher, and §9 holds the new line.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index reset to
  HEAD with `git read-tree HEAD` and only your specs staged, names them only for findings a
  `gen_build_index.py --write` render cures. Delete the copy after.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No dGroundRules or dOrderedCharter file, and no other dSafePassage spec.
- No commit, no stage into the real index, no deviation record: the main loop writes those.
- Probe copies only under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-thermostat-power-issue-370c51/784b9d4d-3d6b-441c-87c6-b603e2cf2649/scratchpad/dS/`, deleting nothing else there.

### Reuse

dSafePassage unit 10's class-reader rows as the extension-point precedent for item 7; the owner-forks
brief `memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-1-owner-forks.md` for how
an owner pick is folded.
