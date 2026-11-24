**Serves:** research KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-1

# Returns — dKeptSession build run: build orders 14 to 19 re-grounded, and unit 1's divergence folded

Four gov-spec-writer agents, one per brief under `prompts/` named
`2026-11-21-prompt-KICK-dKeptSession-<lead>-orders-<orders>-reground-brief`, re-grounded the fourteen specs of build
orders 14 to 19 on the tree at the run's BASE `c2a407b0`, concurrently over disjoint spec sets, while unit 1's
builder ran in a pass worktree of its own. The main loop relayed each writer's `interface-changes` to the writer
whose spec they touched, and resumed the writer of spec 36 once spec 5's rewrite moved its argv.

## The revs reached

- Order 14 (window): specs 45, 46, 47, 48 rev-3.
- Orders 14 to 16 (recipient and id): spec 28 rev-3, spec 22 rev-6, spec 31 rev-3.
- Orders 16 to 17 (mailbox): spec 5 rev-9, specs 23 and 39 rev-3, spec 51 rev-2.
- Orders 17 to 19: spec 36 folded once more over spec 5 rev-9, spec 27 rev-5, spec 24 rev-3.

## Unit 1's divergence

Unit 1's builder (run `wf_c7d6ba36-6f3`) returned a DIVERGENCE before any edit: the `policy fixtures` guard in
`tools/gate-legs.json` covered neither the loop kit nor the playbook kit's `layers.toml`, which the fixture copies,
and nothing said what the presets arm does where the loop kit does not resolve. The main loop ruled both in
`prompts/2026-11-21-prompt-KICK-dKeptSession-1-divergence-brief.md` (the guard gains the copied paths; an announced
skip, never a finding, where the loop kit is absent), a gov-spec-writer folded them at rev-6, and its pass worktree,
which committed nothing, was removed with `pass-tree.sh --remove`.

## Rulings the main loop took on the returns

- Unit 5 writes the post's eight-argument id call and the `--mail` guide entry itself (specs 28 F3 and 31 F2 move
  their guide text to it), since unit 31 lands before unit 5 and no post exists at its build.
- Unit 5's sightings prefix is `refs/gov/remote/`, as every landed caller passes it; the earlier spelling would have
  hidden every mail sighting from the deadline read.
- Unit 36 observes the landed `tools/loop/loop_witness.py#resolve_bash` and mints no second resolver.

## Carried to later waves' re-ground briefs

- 44 S27: no render_playbook.py --fleet-tags call; the playbook-render kit joins requires because check_mail_recipient calls check_fleet_tag (already read undeclared by check_fleet_tag, resolve_fleet_tag).
- 42, 44, 56: no no-argument resolve_bash() in loop_lib.py raising LoopError; the landed one is tools/loop/loop_witness.py#resolve_bash(<script>), returning None. 56 S4-S6, AC4-AC5 void or an ask to TOOL-dGroundRules-25's shared block; 56 S27, S44 name loop_transition.py and its leg (loop transition record), not tools/loop/selftest.py.
- 53, 61, 63: mail row columns 12-14 are seq, after, content-key (spec 27); 15-16 deadline, default (spec 24); column 11 reply (spec 5).
- 25: check_mail_deadline keeps its signature but deadline may be fractional hours; the landed check_lease_witness reads an expired question as closed.
- 55, 62: "the --open row set" now reads as the open rows of unit 5's single unfiltered read (F9).
- 56 S13: met inside unit 5 (tuple member, build-index selftest); AC1 stays in spec 39 in the shape S40 asks.
- TOOL-dPlacedRequest-66 accept line met by landed code; still open in dPlacedRequest's BACKLOG.md (that build's to close).
- 62 S29: spec 45's Evidence bullet already says it. 62 S30: spec 45 AC1 aims HOME and USERPROFILE; LOCALAPPDATA, XDG_STATE_HOME remain S30's. 62 S26: 45, 46, 47 window criteria remove CLAUDE_CODE_MAX_CONTEXT_TOKENS themselves; S26's class arm unaffected.
