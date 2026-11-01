**Serves:** research TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26

# Spec fix brief — dBoundRoles, what the spec stage's checks found before the spec commit

The five writers of `unattended-build.js` run `wf_b19dd66d-878` authored all 26 specs (their returns:
`memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md`). The specs are staged
and not committed. The main loop then ran `python tools/check-spec-tokens.py` (22 lines on this build) and
`bash tools/memory-tree/check-memory-hygiene.sh` (checks 12 and 30 on this build). Fix every item below in the
spec or record it names, and nothing else. Every spec stays `rev-1`: none is committed yet, so a fix is still
authoring, not a revision, and owes no §9 line. Every rule of the spec brief
`memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md` still binds.

## F1 · the §3 edges (hygiene check 12)

- TOOL-dBoundRoles-20 declares `consumes-from` TOOL-dBoundRoles-15 naming `budget`, the field unit 15 hands it.
- TOOL-dBoundRoles-3 declares `hands-off` TOOL-dBoundRoles-23 naming the work-order blocks unit 23 places in its
  frame (`### item`, `### inputs`, `### allowance`, `### return`, `### witness`, as unit 3 spells them).
- TOOL-dBoundRoles-19 reads `role.<slot>` (its overlay units select `role.<slot>`): add `consumes-from`
  TOOL-dBoundRoles-14 naming `role.<slot>` to unit 19, and `hands-off` TOOL-dBoundRoles-19 naming the same token to
  unit 14.
- TOOL-dBoundRoles-6 lists `acts-as` among the role index additions, beside `layer` and `shapes`, as
  TOOL-dBoundRoles-1 §8 F4 adds it.
- Unit 25 moves a spawn guard that reads the composition unit 20 lands. If unit 25's text reads anything unit 20
  produces (a composed row, `compose_roles`, the role index's held harnesses), declare that edge both ways naming
  the token; if it reads nothing of unit 20's, add no edge and say so in your return.

## F2 · the two deviation records on cl-dClosedLoop-0175 (hygiene check 30)

`2026-10-25-build-TOOL-dBoundRoles-10-deviation-101.md` (`driver.reads`) and `-102.md` (`roles.no-spawn`) both amend
cl-dClosedLoop-0175 with differing **After:** texts and no **Supersedes:** ordering them, so the as-built view renders
the clause's baseline row. `memory/HYGIENE.md` "Deviation records" is the rule: the head of a clause's set (the one
record no other names in Supersedes) supplies the view's text. Give `-102` a `- **Supersedes:** 2026-10-25-build-TOOL-dBoundRoles-10-deviation-101`
bullet, and make `-102`'s **After:** the clause as both departures leave it (its whole text with 101's `driver.reads`
change and 102's `roles.no-spawn` change), one line with no `|`. Leave `-101` as it is.

## F3 · the Carries pins of amended clauses (spec-tokens `[carries]`)

A deviation that amends a clause moves the clause's hash in the as-built view, and the spec-tokens carries join
reads the view. TOOL-dBoundRoles-4 pins `cl-dClosedLoop-0169@cdc1b7f9` and the view hashes it `60524f05`;
TOOL-dBoundRoles-7 pins `cl-dClosedLoop-0172@b73b4974` and the view hashes it `d88edbe8`. Re-pin each to the view's
hash. TOOL-dBoundRoles-10's pin moves too once F2 lands: run `python tools/memory-tree/gen_build_index.py --write`
in your throwaway clone after F2 and read the clause's hash from the view
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, or name in your return that the
main loop must re-pin unit 10. Each re-pinned spec's §8 names the deviation that moved its clause and notes that the
packet's `carries.py --exit` reads v2's baseline hash, which `PLAY-dClosedLoop-30` records as the disagreement.

## F4 · leg lines (spec-tokens `[guards]`)

Each file §4 touches trips the guard of the leg named; add each leg to that spec's §7 leg line, spelled as
`tools/gate-legs.json` spells it:

- TOOL-dBoundRoles-6: `check-wiring self-test`, `lexicon naming predicates` (for `.claude/roles.json`).
- TOOL-dBoundRoles-11: `check-wiring self-test` (`.claude/agents/gov-spec-writer.md`), `recall floor arms`
  (`memory/TEMPLATE-SPEC.md`).
- TOOL-dBoundRoles-13: `check-wiring self-test`, `lexicon naming predicates` (`.claude/skills/build/SKILL.md`).
- TOOL-dBoundRoles-15: `check-wiring self-test`, `lexicon naming predicates` (`.claude/roles.json`).
- TOOL-dBoundRoles-17: `recall floor`, `recall floor arms` (`memory/project/work-order-legacy.txt`).
- TOOL-dBoundRoles-19: `check-wiring self-test` (`.claude/agents/`).
- TOOL-dBoundRoles-26: `check-wiring self-test` (`.claude/roles.json`).

## F5 · paths a criterion names that git does not track (spec-tokens `[path]`)

- TOOL-dBoundRoles-18: `house/gov-diff-reviewer.md` resolves to no tracked file as spelled, and
  `house/gov-reviewer.md` does not exist at HEAD. Spell an existing file by its tracked path
  (`tools/roles/house/gov-diff-reviewer.md`), and cite one this build creates by its basename outside a path shape,
  keeping its full path in §2, §4 and Files touched.
- TOOL-dBoundRoles-21: `agents/default.agent.md` is a planted fixture, not a tracked file: describe the plant (a
  role file named `default` in a fixture tree) without a path shape.

## F6 · suites inside acceptance criteria (spec-tokens `[bar]`)

A criterion observes the unit's own checker on a staged break, a `--selftest` flag of the unit's own tool or a
fixture, never a suite: TOOL-dBoundRoles-18 and TOOL-dBoundRoles-25 name `tools/govkit/selftest.py`,
TOOL-dBoundRoles-24 names `adopt-roles.test.sh`, and TOOL-dBoundRoles-25 names `agent-cap.test.sh` and
`spawn-guard.test.sh`. Rewrite each criterion to observe the checker or fixture directly, and move each suite to a
`New arm:` line in that spec's §7 (or to its `**Readers:**` clause where the suite is retired).

## Return

The list of files you changed, one line each with the F-items it took, any edge you added or declined under F1's
last bullet, and whether unit 10's pin is re-pinned. Commit nothing; do not run the build-index generator outside
your throwaway clone. You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25,30` in a throwaway
clone with every dBoundRoles spec and record committed there.
