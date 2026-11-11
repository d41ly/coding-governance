**Serves:** research PLAY-dConvergedCharter-11

# Fold brief — PLAY-dConvergedCharter-11, round-2 finding 1

The round-2 spec audit `memory/builds/dConvergedCharter/reviews/2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1.md`
confirmed finding 1 (H1, LOCAL), naming specs PLAY-dConvergedCharter-12 and PLAY-dConvergedCharter-11. The disposal
folded it into spec 12 at rev-3 (S3 re-homes `plan_state` in the runtime library, points `brief-recorded` at it, and
moves `PASS_ORDER_CUTOFF`, `BRIEF_RECORDED_CUTOFF`, `PASS_ORDER_PREANCHOR_CAP` and `PASS_ORDER_WAIVER` from
`.unattended.conf` into `.memory-tree.conf` where gov assigns them; AC8 observes both moved checkers on the kitless
clone), and into spec 20 at rev-3 (S3 carries those cutoffs into an adopter's `.memory-tree.conf`). It folded nothing
into spec 11, which the same disposal bumped to rev-4. Under BUILD-METHOD M4 a LOCAL finding folds into EACH spec it
touches, so spec 11 owes its half.

Edit only `memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md`, and keep it at `rev-4`.

1. Where spec 11 states which `.unattended.conf` keys its fold takes into the policy file (its population, the
   `legacy-homes.txt` rows it drains, and the reader inventory), state that `PASS_ORDER_CUTOFF`,
   `BRIEF_RECORDED_CUTOFF`, `PASS_ORDER_PREANCHOR_CAP` and `PASS_ORDER_WAIVER` are not folded into the policy file by
   this unit: PLAY-dConvergedCharter-12 S3 moves them into `.memory-tree.conf` with the checkers that read them, and
   PLAY-dConvergedCharter-20 S3 carries that move to an adopter. Say how spec 11's red arm on a reader of a folded key
   treats them (not folded, so not graded), so the arm cannot read the moved checkers as readers of a folded key.
   Check `tools/policy/legacy-homes.txt` for rows naming these keys with `git grep`, and say what happens to each row.
2. If spec 11's §3 already carries an edge with PLAY-dConvergedCharter-12, name the four keys on it; add no new edge
   unless spec 12 declares the reverse.
3. Extend the existing `rev-4 · 2026-11-04` revision-log line so it also names
   `2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1` finding 1 with a short parenthetical, and add the
   sections you touched to its section list.

Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` before returning and quote its exit and any red on
this build's specs. Return the lines you changed.
