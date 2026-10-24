**Serves:** research TOOL-dSafePassage-1 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-13 TOOL-dSafePassage-26

# The parent fixes' spec writer: its returns

The gov-spec-writer agent of `memory/builds/dSafePassage/prompts/2026-10-25-prompt-TOOL-dSafePassage-1-1-spec-writer.md`, its end-of-turn texts in order, extracted from its subagent transcript by script, never retyped.

## Returns

### Return 1

I revised all four specs: 1, 6, 9 and 13 under `memory/builds/dSafePassage/spec/`. Each Status line is one rev higher, dated 2026-10-25 and still `DEFERRED`, and each has a §9 line naming its items and the parent-fixes brief. Every acceptance grep in the brief prints what it should. The memory hygiene gate, run over a scratch index reset to HEAD with only these four staged, failed only check 9: the build index needs a fresh render, which `gen_build_index.py --write` cures. I deleted the scratch index and my scripts afterwards.

**TOOL-dSafePassage-1** (rev-10, 47721 bytes, limit 47800)
- **Item 1, the `policy` form (S8):**
  - `HOME_FORMS` swaps `limits` for `policy`, giving `("policy", "file", "conf", "constant")`. The `limits` branch was already retiring in S8.
  - The seven census rows read `home = "policy:"` with nothing after the colon, because the key is already the row's `name`.
  - `resolve_caps` reads a `policy:` row's value from `budgets.<name>` and refuses a value handed in by the caller, as it did for `limits:`.
  - `arm_cap_census` exempts a `policy:` row from naming its cap, as it exempted a `limits:` one. Its check of the limits file's rows goes, since `check_budgets` already flags a `budgets.<cap>` that no census row names. The seven rows' test plants set `budgets.<name>` instead of copying the limits file.
  - Files touched now names these. The new AC19 runs `budgets.py resolve AGENTS.md` (source `file`) and `check_policy.py` (no `arm_cap_census` finding).
  - The F12 text no longer says the census join already accepts the form, or calls it a "fifth" form.
- **Item 2, the import gap:** §7's "does not check" paragraph now says the freeze covers a program's own bytes, not what it imports, and that it stays narrow because dOrderedCharter spec 31 keeps its class reader in an imported module.
- **Item 3, size:** the cuts are in Readers lines, fork reasoning, §10, and brief filenames in §9 (the records table already lists them). I also dropped the dWitnessedBar non-goal, which repeated its hands-off edge. No criterion, option, resolution or Carries line changed. The margin is only 79 bytes; the index render will add a few rows, still well under 49152.

**TOOL-dSafePassage-6** (rev-5): §3 now names only dWellOiledMachine's `/unattended` shim as a first row. It says dOrderedCharter's module re-export is no `[[shim]]` row, that spec 31's `module-export` class row holds it, and that dConvergedCharter counts its window. The one remaining `map_lib` hit (§10, line 467) is an existing note about a record that disagreed with the source, not a shim row.

**TOOL-dSafePassage-9** (rev-4)
- **Item 5, retired seeds:**
  - The seed override at `govkit.py:9988-10000` currently passes through only `missing` and `renamed`. It now keeps a named tuple, `SEED_KEPT_VERDICTS`, which adds `retired-edited` and `withdrawn`. The grid gives those two only when gov no longer holds the seed's source.
  - So an edited retired seed reads `retired-edited` and gets one order. An unedited one reads `withdrawn` and is reported only, never deleted, through its existing `report-reseed` handling. A seed gov still ships keeps today's override.
  - The fixture gains plants `seed-retired-edited` and `seed-retired-clean`, plus a stub `seed-override` for the red case. The new AC12 is added to the §7 arm line.
  - §4 now notes one case it does not check: a retired seed the adopter deleted still goes through the override as today.
- **Item 6:** `read_policy_value(key, root, rev=None)` is stated where the helper is defined: a set `rev` is passed to `policy.py get` as `--rev <rev>`. The hands-off edge to spec 13 is updated to match.

**TOOL-dSafePassage-13** (rev-5), item 7
- **The `rows` reader:** S1 makes `rows` an extension point like unit 10's class `reader`. A class names either a `<path under the tool root>:<function>` reader or `usage.toml`.
- **The `none` spelling:** a `page` or `none` class leaves `rows` out, the same way unit 10's optional `witness` is left out. S8 turns a missing or misplaced `rows` into a finding, and a reader that won't load into exit 2.
- **S2's sources:** the four built-in sources become `read_hook_usage`, `read_policy_usage`, `read_verb_usage` and `read_leg_usage` in `docs_leg.py`. The naming lexicon passes all four.
- **Plants and the hand-off:** two new plants, `reader-rows` (AC6) and `none-rows` (AC7). The hand-off to later builds no longer asks them to restate members' rows.

Two of these were my own calls rather than the brief's: spelling the `policy:` home with nothing after the colon, and naming `SEED_KEPT_VERDICTS` as a module constant (the stub needs a name to swap).

The worktree also shows modified dOrderedCharter specs. Those are not my edits; I touched only the four files above and nothing in the real index.

Files:
- C:\projects\coding-governance\.claude\worktrees\thermostat-power-issue-370c51\memory\builds\dSafePassage\spec\2026-10-23-spec-TOOL-dSafePassage-1.md
- C:\projects\coding-governance\.claude\worktrees\thermostat-power-issue-370c51\memory\builds\dSafePassage\spec\2026-10-23-spec-TOOL-dSafePassage-6.md
- C:\projects\coding-governance\.claude\worktrees\thermostat-power-issue-370c51\memory\builds\dSafePassage\spec\2026-10-23-spec-TOOL-dSafePassage-9.md
- C:\projects\coding-governance\.claude\worktrees\thermostat-power-issue-370c51\memory\builds\dSafePassage\spec\2026-10-23-spec-TOOL-dSafePassage-13.md

### Return 2

Spec 26 is now **rev-5** at **47487 bytes**, under your 47500 limit, with the generated records table untouched.

- **Status:** `DEFERRED · rev-5 · 2026-10-25`. The new §9 line names `2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md` and "trimmed under the class cap (audit P12)".
- **What survives:** a script compared the trimmed file with HEAD.
  - All 54 scope items survive. Each still cites the same criteria in its "Observed by" clause.
  - All 52 criteria survive, each with a backticked witness and a "Red when:" clause.
  - F1 to F4 and all four Readers clauses survive.
  - All 23 edges keep the same kind and the same unit id.
  - The §7 gate line and every "New arm … covers" field are byte-identical.
  - The spec has no Carries line; its "Derived:" line is untouched.
- **What I cut:**
  - §1's 46-row table becomes one paragraph. D-10 to D-55 map onto S1 to S54 in order, so a rule plus its five multi-id exceptions keeps the whole mapping.
  - Prose now says "unit N" for TOOL-dSafePassage-N, defined once in §1. Edges, file paths and the brief name keep the full ids.
  - The line-cite base (`3708a705`) is stated once in §1.
  - The consumes-from edges dropped their "which S… amend" lists, since each scope item already names the unit it amends.
  - Elsewhere it is tightened wording.
- **Small corrections along the way:** two §2 sub-heads named the wrong report items and now say "D-11 to D-14" and "D-24 to D-27". I removed a duplicate S47 pointer bullet; S47 itself stays in the low items. The rev-2 to rev-4 lines are restated compactly.
- **Hygiene:** I ran it over a scratch index reset with `git read-tree HEAD`, with only spec 26 staged. It fails only check 9 (the build-index render owed), which `gen_build_index.py --write` cures. My first run also caught two check-25 regressions I had introduced, in S25 and S28, which I fixed before the clean run. I deleted the scratch index and files afterwards. Spec 26 is unstaged and nothing is committed.

Two things for you:
- **Overlap with spec 9:** spec 26's S28 and AC27 already have the seed override pass `retired-edited` through. Spec 9 rev-4 now does that and also passes `withdrawn`, through `SEED_KEPT_VERDICTS`. Since spec 26 builds after spec 9, S28 will find its change already made. I left S28 unchanged; whether to restate it as a reading of unit 9's change is your call.
- **Spec 1 headroom:** the staged spec 1 is my 47721-byte version, not yet rendered. That leaves 1431 bytes under the 49152 cap for the records rows the render adds.

File: C:\projects\coding-governance\.claude\worktrees\thermostat-power-issue-370c51\memory\builds\dSafePassage\spec\2026-10-23-spec-TOOL-dSafePassage-26.md

### Return 3

Spec 26 is now **47492 bytes**, still rev-5. S28 and AC27 now read unit 9's change instead of making their own edit.

- **S28:** says unit 9's `SEED_KEPT_VERDICTS` already passes `retired-edited` and `withdrawn` through the seed override, so this pass makes no edit and only observes unit 9's plant. Its line cite changed from `:9987-9999` to `:9988-10000`, which is where the override sits at HEAD. Dropping the Readers clause made check 25 red S28, so it keeps a short one: by name `_cmd_update`; by value NO VALUE READERS.
- **AC27:** now runs unit 9's plant, `retired_edits.py --plant seed-retired-edited`. It expects exit 0 with the row reading `retired-edited` and an outbox order, and goes red when the override rewrites it to `patched`.
- **Edge:** the consumes-from edge on unit 9 was already there. It now also names `SEED_KEPT_VERDICTS`.
- **Two knock-on edits:**
  - `edited-gone-seed` is gone from §4's list of minted plants, since this unit no longer adds that plant.
  - AC27 is off the `tools/govkit/selftest.py` New-arm `covers` list, because this unit's arm no longer stages its case; unit 9's arm does.
- **§9:** the rev-5 line gains "S28 and AC27 read unit 9's `SEED_KEPT_VERDICTS`". I replaced its old ending, "no item, criterion, fork or edge changed", because that is no longer true.
- **Hygiene:** run over a scratch index reset with `git read-tree HEAD` with only spec 26 staged, it fails only check 9 (the build-index render owed). I deleted the scratch index. Spec 26 is unstaged and nothing is committed.

File: C:\projects\coding-governance\.claude\worktrees\thermostat-power-issue-370c51\memory\builds\dSafePassage\spec\2026-10-23-spec-TOOL-dSafePassage-26.md

### Return 4

Both specs are now under 47000 bytes with the final records table in place:

- **Spec 1:** 46996 bytes.
- **Spec 26:** 46989 bytes.

Neither rev moved (spec 1 stays rev-10, spec 26 rev-5). Each spec's newest §9 line gains "trimmed again for the records rows". Hygiene, run over a scratch index reset with `git read-tree HEAD` with only these two staged, passed with exit 0 and no findings. I deleted the scratch index and my scratch files. Nothing is staged in the real index and nothing is committed; your earlier staged copies are still there, so both files show `MM`.

I compared each spec with the copy you had staged. In both:
- every scope item still cites the same criteria;
- every criterion is still present with its backticked witness and its "Red when:" clause, and every `figure:` and `fixture:` note survives;
- every fork keeps the same resolution mark;
- every edge keeps its kind and unit id;
- the Carries or Derived line, the records table, the gate line and the New-arm "covers" lists are byte-identical.

**Spec 1 cuts.** Most came from §8: each fork's reasoning is restated in fewer words, with options, recommendations, rungs and marks unchanged. The rest came from the Data model prose, the Inventory notes, the Edges descriptions, §5, §7's "does not check" paragraph, §10 and wording in AC10 to AC13. One change to note: F8's sentence that `TOOL-dGroundRules-13` is the one to grant the write shape now sits in its recommendation, ahead of the mark, rather than after it.

**Spec 26 cuts.** One cut is a visible style change you may want to know about. The 52 criterion labels and 54 scope labels now use the short form `- AC1. ` and `- S1. ` instead of `- **AC1** — `. The spec format admits that form, and every label parser I found (`AC_LABEL`, the hygiene witness and scope-join checks) treats the bold as optional. It is the only spec in this build with that style.

The other spec 26 cuts:
- §1 is tighter, and the review path is now relative.
- S10 and S13 point at §4 Data model for the `{to}` and line-ending rules instead of restating them.
- §5, §8, §10 and the Alternatives are tighter.
- The four `memory/map/generated/` files are one Files-touched line naming the directory.
- Several "Red when:" clauses are worded more briefly.

Files:
- C:\projects\coding-governance\.claude\worktrees\thermostat-power-issue-370c51\memory\builds\dSafePassage\spec\2026-10-23-spec-TOOL-dSafePassage-1.md
- C:\projects\coding-governance\.claude\worktrees\thermostat-power-issue-370c51\memory\builds\dSafePassage\spec\2026-10-23-spec-TOOL-dSafePassage-26.md
