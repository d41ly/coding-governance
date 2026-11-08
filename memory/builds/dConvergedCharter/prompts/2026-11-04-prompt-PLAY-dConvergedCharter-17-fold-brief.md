**Serves:** research PLAY-dConvergedCharter-17

# Fold brief — PLAY-dConvergedCharter-17, round-1 findings 1 and 2

The round-1 spec audit `memory/builds/dConvergedCharter/reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md`
confirmed findings 1 (H1) and 2 (H2), each naming specs PLAY-dConvergedCharter-9 and PLAY-dConvergedCharter-17, both LOCAL.
The disposal folded both into spec 9 at rev-3 (AC2 restricted to the five renamed kits with `tools/roles/SKILL.template.md`
staying as unit 17's held client; S7 admitting a held client's install rows while its `skill` shim is open). It folded
nothing into spec 17, which the disposal already bumped to rev-2 for findings 17 and 4. Under BUILD-METHOD M4 a LOCAL
finding folds into EACH spec it touches, so spec 17 owes its half.

Edit only `memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-17.md`, and keep it at `rev-2`:
the disposal's fold of this round is one revision.

1. Finding 1: where spec 17 states its held set (S4 and its acceptance), state that `tools/roles/SKILL.template.md` is
   unit 17's held `/build` client until the `roles/build-skill` shim row closes, and that PLAY-dConvergedCharter-9's AC2
   excludes it for that reason (spec 9 restricts its count to the five renamed kits). Name no change to what spec 17
   holds or when it is released.
2. Finding 2: state that while the shim row is open the roles kit's `to`, `probe` and `pattern` rows naming
   `.claude/skills/build/SKILL.md` (`tools/roles/kit.toml`) stay, and that PLAY-dConvergedCharter-9 S7 admits them as a
   held client's install rows, so `core skills conformance` stays green over gov's tree with both units built.
3. Extend the existing `rev-2 · 2026-11-04` revision-log line so it also names
   `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1` findings 1 and 2, each with a short parenthetical, and add
   the sections you touched to its section list.
4. If spec 17's §3 lacks an edge with PLAY-dConvergedCharter-9 for the held client, do not add one unless spec 9 already
   declares its reverse; say in your return what you found.

Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` before returning and quote any red it prints on
spec 17. Return the lines you changed.
