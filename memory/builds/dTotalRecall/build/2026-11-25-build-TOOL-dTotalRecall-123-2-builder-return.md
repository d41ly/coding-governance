**Serves:** journal TOOL-dTotalRecall-123
**Caused-by:** TOOL-dTotalRecall-123

# TOOL-dTotalRecall-123 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `62fabf4a5` from [2026-11-25-prompt-TOOL-dTotalRecall-123-build-2-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-123-build-2-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `62fabf4a5`.

## Why

DIVERGENCE: spec section 4 "The record of the relaxation", and nothing else in the design. Its two rows `Departs from: cl-dClosedLoop-0228@fcc9ca71` and `Follow-through: ask TOOL-dTotalRecall-111` cannot both be committed. `tools/memory-tree/asbuilt_view.py#resolve_clause_rows` makes a finding of any record that departs from a clause without an `amends` or `supersedes` follow-through. With the record written exactly as specified, `gen_build_index.py --write` printed `as-built VERDICT ... 2026-11-25-build-TOOL-dTotalRecall-123-deviation-1021: departs from cl-dClosedLoop-0228 and carries no amends or supersedes row`, and said `--write` cannot cure it. Hygiene check 30 turns that finding into a failure, and the commit hook runs check 30 staged. Every other record in the tree that departs from a cl-dClosedLoop clause says `amends` (DERIVED 2026-11-25).

I tried two corrections in C:/Temp/rf2, each with the repository's commit hooks on (DERIVED 2026-11-25):

(a) `Departs from` kept, `Follow-through: amends cl-dClosedLoop-0228@fcc9ca71`, and `After` carrying the whole amended clause text. Check 30 passes. The amended text then makes spec 17's frozen `Carries: cl-dClosedLoop-0228@fcc9ca71 whole` stale, and the hook refused the commit with `the hygiene gate, its check-29 FAILED ... TOOL-dTotalRecall-123.md is INPROGRESS while dTotalRecall's coverage is red: stale cl-dClosedLoop-0228`. This route also needs spec 17's `Carries` hash re-stamped, which section 3 puts out of scope, and this unit cannot carry the clause by section 8 F3. (DERIVED 2026-11-25, the pass)

(b) `Departs from: `TOOL-dTotalRecall-17@rev-3`` with a section tail, every other field as specified, `Follow-through` still the ask. The whole pass committed with rc=0: check 29 and check 30 both clean, 2389 deviation records read. (DERIVED 2026-11-25, the pass)

So section 4's table would have to say one of these:
 - Recommended, proved end to end: `Departs from` is `TOOL-dTotalRecall-17@rev-3` [§4 "The terms"], the spec 17 heading that defines the twin difference. The trial used the tail [§4 "The instance"]; only the tail differs. The spec should then also say that the as-built view keeps the baseline text of cl-dClosedLoop-0228, or name who amends it later. (DERIVED 2026-11-25, the pass)
 - Otherwise the `amends` form with the full clause text in `After`, plus a stated re-stamp of spec 17's `Carries` and of section 3's non-goal.

For the same revision: section 4 "Files touched" should list `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, whose head count line any new deviation record moves. It was already in the dispatch. The task text also says to flip the header to CLOSED in the pass commit, while rev-2 and the brief say it stays INPROGRESS. I was following the spec and brief; nothing in the spec needs to change for that.

## Summary

Nothing is committed. Every path I changed in the worktree is restored; only the main loop's staged memory/builds/dTotalRecall/RUN.md remains, as found. The brief was already recorded at 5163d684ba2e. The design (S1-S3, S5) and AC1-AC4 and AC10 build as written; only the S4 record's fields block the commit.

The complete pass is drafted in C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/u123b/ :
- `trial2.patch`: the whole pass as committed in the scratch clone under route (b). It holds the scorer, the README, the record, the ledger, the manifest, `symbols.json` and the renders. It has no RUN.md, and its ledger was written before the trial, so re-read it. The commit's message and author are scratch.
- `draft3.patch`: the same without the renders, with the record as the spec states it.
- `deviation-unit17.md` (route b) and `deviation-amends.md` (route a).
- `door.py`: the `gov_record.py new deviation` call, which minted number 1021 in the worktree. The file is removed, so expect 1021 again. (DERIVED 2026-11-25, the pass)

Checks run (DERIVED 2026-11-25). They stand in for the `review-replay selftest` leg, which did not run:
- AC1: both `term recall` lines read exactly as specified.
- AC2: a dropped run, two declared counts, an undivided count, one run and an extra run each refused; the complete set returned lines.
- AC3: the boundaries held and the first record's six pairs read 15.46.
- AC4: the grep printed nothing.
- AC5: over the record as specified, `read_record` gave an empty `malformed` and the F1 value as `bound`, and the anchored grep named the one file. Under route (b) neither read was repeated.
- AC10: exit 2 naming `map None: not a source of a non-empty map`. The manifest's `known` equals the first experiment's. (DERIVED 2026-11-25, the pass)
- `map-noise`, `map-verdict`, `map-experiment` and `map-known`, cut out of `run_selftest`, each answered None. In scratch copies `map-noise` failed on the range put back, on the division cut and on the exact-count refusal cut, and `map-verdict` failed on the margin alone.
- The lexicon's `--suggest` admits the four names, and `--measure` reads the offender pin unmoved at 1443.
- The hooks over the clone commit took about 75 s and passed for route (b); those are the only hygiene and map checks that ran. (DERIVED 2026-11-25, the pass)
- `gotchas.py --for-diff` ran over the clone commit, with only the tail of its output read. The re-dispatched pass must run it over its own commit and act on it.

Owed to the close: the RED-first observation of both `New arm:` lines, the section 7 legs, and AC9. Owed to the main loop: AC6 to AC8. No command exceeded its bound. Scratch commit `f068fed86` sits on a detached HEAD in C:/Temp/rf2. (DERIVED 2026-11-25, the pass)
