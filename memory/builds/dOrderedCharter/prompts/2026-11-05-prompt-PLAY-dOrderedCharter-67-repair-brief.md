**Serves:** research PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70

# Brief: the closing diff review's promotions — units 67 to 70

## The prompt

> finish building this unit and PAUSE the build.

> merge this branch to remote as well

— owner, 2026-11-05. The partial close's review confirmed no blockers, 3 highs and 20 mediums and lows. Every confirmed finding is
promoted, and a unit this run adds is never carried forward, so these four units build before the close.

## The brief

### Goal

Write one spec for each of units 67, 68, 69 and 70, so a builder can build each as written and the findings close.

### Items

1. **The source.** `memory/builds/dOrderedCharter/reviews/2026-11-05-review-PLAY-dOrderedCharter-1-closing-diff-review-round1.md`, its HIGH, MEDIUM and LOW sections. Each finding names its place, the defect, its fix and its left-shift gate.
   Where a skeptic judged a fix UNSOUND, the report's corrected fix binds. Re-read each finding against the tree before specifying it.
2. **Unit 67: H1.** The recall suites' guards gain the moved `tools/memory-tree/id_grammar.py`. Write one fix for the class if the
   report's left-shift arm fits this unit; if not, the unit adds its checklist entry instead.
3. **Unit 68: H2.** `scan_unfenced` walks `tree_lib.unfenced_lines` and reports an unclosed fence, as the report says, with its plant.
4. **Unit 69: H3 with M17.** One class, one fix shape: `instruction_units`, and `gov_tag`'s `--fixture` path, set `GIT_ENV_LEAKS` aside. Each
   arm runs in a disposable repository, never against this one. M17 moves here from unit 70, because it shares the fix.
5. **Unit 70: the rest.** M1 to M16, M18 and L1, batched. Fix each as the report says. Where a finding's fix needs a mechanism this
   batch cannot carry, say so in section 8 and rule it by the fork rule. A finding is never dropped.
6. **Also fix by the same class:** unit 18's undefined names passed every pass, because the bar reads no undefined module name. Unit 67
   carries a gate for that class, or a bug-class entry where no gate fits. A scan script exists: the scratch file `undef.py`, in the
   folder named by the fold briefs; it walks `ast` for names loaded and never bound, over changed Python files.

In each spec:

- Follow `memory/TEMPLATE-SPEC.md`, and write it at `memory/builds/dOrderedCharter/spec/2026-11-05-spec-PLAY-dOrderedCharter-<n>.md`.
- Status `DEFERRED`, rev-1, dated 2026-11-05, base `de8d2d3a1`, streams playbook, `order 17`, advancing PLAY-dOrderedCharter-38, Tier-2.
- Declare each new arm on a `New arm:` line, and list each leg it moves in section 7.
- Name every path in Files touched, and keep the four units' write sets disjoint where the findings allow, naming any overlap.
- New text cites code as `path#symbol`, outside the acceptance bullets. An acceptance bullet spells a plain tracked path, with no `#` and
  no `HEAD:` prefix, and never a file not yet tracked. A `python -c` path takes spaces around it, as `open( 'a/b' , 'rb')`.
- New text names a section in words, and names a check by what it checks.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Four specs exist, and every confirmed finding of the report is owned by exactly one of them.
- Each H and M and L id is named in its spec's goal or scope.

### Gates

Memory hygiene, as your role runs it. The main loop live-sweeps each spec before its dispatch.

### Non-goals

- No code.
- No edit to an existing spec.
- Nothing about unit 3's F5 or any deferred unit.
