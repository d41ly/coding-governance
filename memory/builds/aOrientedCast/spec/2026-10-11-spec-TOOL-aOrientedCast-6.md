# TOOL-aOrientedCast-6 — the write gate admits a spec write only from the spec-writer role and a product write only from the builder role

**Status:** OPEN · rev-1 · 2026-10-11 · node a · Tier-2 · base 646d4a73 · streams tooling · order 9 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md](../build/2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md) | research | TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's mandate puts spec writing and building in their role agents and nowhere else, and today
no hook knows which agent is writing. This unit gives `checkRouted` in `tools/hooks/scratch-guard.js`
a ROLE arm. A write under a build's `spec/` folder is admitted only from an agent whose type is a role
declaring `writes = spec`. A write under `ROUTED_PATHS` is admitted only when aRoutedQuill's
buildable-unit arm admits it AND the agent's type is a role declaring `writes = product`. The main loop
and an untyped harness agent are refused both, except for a flip of a spec header's status cell.

## 2. Scope (IN)

- **S1** — `loadRoleIndex(top)` in `tools/hooks/scratch-guard.js` reads `.claude/roles.json` at the
  target's toplevel and answers one of three states: absent, broken (unreadable, not JSON, or not
  the shape of §4 "Data model"), or ok with its `roles` and `harnesses`. It is exported, so
  `agent-cap.js` reads the index through the same reader. Observed by AC4.
- **S2** — The SPEC class: a target whose path relative to its toplevel sits under
  `<MEMORY_ROOT>/builds/<one segment>/spec/`, at any depth. With the index ok, such a write is admitted
  when the payload's `agent_type` names a role whose `writes` is `spec` and whose `agent` is true.
  Otherwise S4 decides, and a write S4 does not admit refuses. Observed by AC1 and AC5.
- **S3** — The PRODUCT class: a target under a `ROUTED_PATHS` entry. aRoutedQuill's steps 7 to 9 run
  first and unchanged, and their refusals stand. Only when step 9 finds a buildable unit does the role
  arm run, as step 9a, admitting a payload whose `agent_type` names a role whose `writes` is `product` and whose
  `agent` is true. Observed by AC2.
- **S4** — The status flip. An `Edit`, `MultiEdit` or `Write` on a spec is admitted when its result
  differs from the file on disk in exactly one line, that line is the spec's status header, and only
  its first cell (the status) and its third cell (the date) differ. It is admitted from the main loop,
  a payload carrying no `agent_type`, and from a `product` role when the card's `## route` names the
  target as a routed unit's spec. Observed by AC3.
- **S5** — Arming, as §8 F2 resolved it. An absent index adds no arm, so a repository without the
  roles kit sees aRoutedQuill's gate exactly as it is. A broken index refuses every write in the two
  classes, naming the file. An ok index naming no `agent`-true role for a class refuses every write in
  that class as UNARMED, naming the class and the file. Writes outside both classes are never read
  against the index. Observed by AC4.
- **S6** — Every refusal names the target, its class, the writer as the payload shows it, the roles
  the index lets write that class, the index path, the renderer verb that reaches such a role, and the
  status-flip admission. Observed by AC1 and AC2.
- **S7** — `checkRouted`'s comment is the ONE evaluation order and carries the new steps. The file
  header's write-gate paragraph and its ceiling, and a `tools/hooks/README.md` section, state the arm
  and what passes it. NOT OBSERVED by a criterion: prose. The review reads it against §4.
- **S8** — The arms live in `tools/hooks/scratch-guard.test.sh` over its existing linked-worktree
  fixture, with an index written for the role arms and absent for every arm that exists today, and
  `FLOOR_ASSERTIONS` moves by the count added. Each arm is observed RED on a staged break first.
  Observed by AC1, AC2, AC3 and AC4.

## 3. Non-goals (OUT)

- Bash and PowerShell writes. The gate never sees `sed -i`, an interpreter or a redirect, and the
  routed-commits push leg is aRoutedQuill's guarantee for product paths. No leg grades who wrote a spec.
- Enforcing the `none`, `review` and `records` write classes. The index declares them and this arm
  reads only `spec` and `product`. A follow-up may grade the rest once a review or records path set is
  declared somewhere a hook can read it.
- Re-specifying aRoutedQuill's route, card or buildable check. Steps 1 to 9 of `checkRouted` keep their
  order, their reasons and their remedies, and every existing arm runs with no index.
- Telling a subagent its own write class at `SubagentStart`. `renderRouteContext` still states what
  holds for the route; a line stating the agent's role and class is a follow-up, kept out so this unit
  stays one mechanism, as aRoutedQuill split its gate and its context.
- Proving who RENDERED a role agent's prompt. That is `TOOL-aOrientedCast-7`'s spawn guard; this arm
  reads only the writer's type.
- A waiver, an environment knob or a warn phase. Enforcement starts at landing, by the owner's ruling.
- A kit version bump. The hooks kit moves once, after this build's last unit touching it.

**This run is not bound by this arm until it lands.** This session's hooks run from the PRIMARY tree
(the mandate record's orientation finding), so an edit to `scratch-guard.js` on this branch binds this
session only once the landing merge is in the primary tree's working copy. Every repair the close owes
before that moment runs under today's gate. After it, this session's main loop is refused every spec
content write and every product write, and its agent registry, read before `.claude/agents/` existed,
holds no role it could spawn instead. So a repair owed after the landing merge, a post-push red say,
belongs to a fresh session whose registry holds the rendered types. A status flip stays admitted, and
records outside the two classes are untouched.

### Edges

- **consumes-from** `TOOL-aOrientedCast-1` — the role slots and the closed `writes` set. Without a role
  declaring `writes = spec` and one declaring `writes = product`, gov's own index arms both classes
  UNARMED and every spec and product write here refuses.
- **consumes-from** `TOOL-aOrientedCast-3` — the generated `.claude/roles.json` and its shape. Without
  it the arm reads an absent index in gov, and AC5 has nothing to observe.
- **consumes-from** `TOOL-aOrientedCast-4` — the unit harness's builder prompt, which on a divergence
  returns uncommitted instead of rev-bumping its spec, and flips its status by the S4 shape. Without it
  every unattended unit pass meets this arm's refusal on its own spec at landing.
- **hands-off** `TOOL-aOrientedCast-7` — the spawn half of the same rule, which reads the index through
  the exported `loadRoleIndex` rather than a second reader.
- **hands-off** external — every other running session of this repository on the landing node, which
  meets this arm the moment the landing merge is in the primary tree and must restart before it can
  spawn a role that writes.

## 4. Design

### Evidence

Read at `646d4a73` on 2026-10-11; nothing under `tools/` or `.claude/` moved between it and `744e55db2`.

- `checkRouted` (`tools/hooks/scratch-guard.js:914`) is the write gate. Its step 6 returns null for a
  target under no `ROUTED_PATHS` entry (`:968`), so every spec write is admitted today. Step 9 returns
  null on the first buildable routed unit (`:983`).
- `checkUnarmed` (`:876`) refuses a `ROUTED_PATHS` entry that covers `MEMORY_ROOT` or sits under it
  (`:885`), so the spec class and the product class are disjoint in every armed repository.
- `readStatusCells` (`:822`) splits the status header on `·` and reads its first cell; `readCard`
  (`:628`) and `extractRouteUnits` (`:800`) are the card and route readers this arm reuses.
- `main` sends the four write tools to `checkRouted` under a catch that refuses (`:1084-1099`), so the
  arm inherits fail-closed with no new wrapper.
- A main-loop `PreToolUse` payload carries neither `agent_id` nor `agent_type`, and a subagent's adds
  both (`memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-2-subagent-payload-probe.md:30`).
- A custom agent type reports its own name as `agent_type`, for an `Agent` spawn and for a `Workflow`
  `agent()` given `agentType`, and an untyped `Workflow` agent reads `workflow-subagent`
  (`memory/builds/aOrientedCast/build/2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md:39-51`).
- `agent-cap.js` already requires this file for `readFrontMatterKey` and `readConfKey` (`:1865`,
  `:1947`), so an exported reader here is how the two hooks share one index read.
- Gov's `.claude/settings.json:23` wires `scratch-guard.js` on
  `Bash|PowerShell|Edit|Write|MultiEdit|NotebookEdit`, so no wiring changes.
- `unattended-unit.js` tells the builder to change its spec first on a divergence and to set its spec's
  status header to CLOSED in the pass commit (`tools/workflows/unattended-unit.js:183-184`, `:220-223`).

### Data model

The index is `TOOL-aOrientedCast-3`'s, read and never written here:

```json
{ "roles": { "<name>": { "workflow": "<w>", "writes": "none|spec|product|review|records", "agent": true } },
  "harnesses": ["<repo-relative script path>"] }
```

`loadRoleIndex` checks the shape it reads and nothing more: an object whose `roles` is an object of
objects each carrying a string `writes` and a boolean `agent`, and whose `harnesses` is an array of
strings. Anything else is broken. The value set of `writes` is not retyped here; a value outside it
simply admits no class this arm reads.

A target's CLASS is computed on `buildComparablePath`'s form of its path relative to the toplevel,
with `MEMORY_ROOT` normalized exactly as `checkUnarmed` normalizes it:

| Class | Predicate |
|---|---|
| spec | the path opens `<mem>/builds/`, then one non-empty segment, then `spec/` |
| product | the path falls under a `ROUTED_PATHS` entry, as step 6 already decides |
| neither | everything else, which the arm never reads |

### The evaluation order

aRoutedQuill's numbers stay, because its README section and its arms cite them. Steps 1 to 5, 7 and 8
are unchanged; step 6 narrows, and two steps are inserted:

6. Class neither → null. Only a spec or a product path reads further.
6a. Class spec → `loadRoleIndex(top)`. Absent → null. Broken → deny naming the index and the fault.
    No `agent`-true role with `writes = spec` → deny, UNARMED for specs. The payload's `agent_type`
    names such a role → null. S4's status flip from an admitted writer → null. Else deny.
7. Class product, and `session_id` missing or no card → deny, absent, as today.
8. No `## route`, or no `- unit:` line in it → deny, unrouted, as today.
9. No routed unit BUILDABLE → deny listing each unit's reason, as today; else step 9a.
9a. `loadRoleIndex(top)`. Absent → null. Broken → deny. No `agent`-true role with `writes = product`
    → deny, UNARMED for product paths. The payload's `agent_type` names such a role → null. Else deny.

The route arm runs before the role arm on a product path and never instead of it: a builder with no
buildable route meets aRoutedQuill's refusal, word for word. The index is read only on a spec or
product path, so a records write costs no extra read.

### The status flip

`buildEditResult(text, tool, toolInput)` computes the file as the tool would leave it. An `Edit`
replaces its `old_string` once, or everywhere under `replace_all`, and an `old_string` the file does
not hold, or holds twice without `replace_all`, yields nothing. A `MultiEdit` applies its `edits` in
order under the same rule. A `Write` yields its `content`. A `NotebookEdit` yields nothing.

`checkStatusOnlyEdit(before, after)` then holds when both texts, split on `\r?\n`, have the same line
count and differ in exactly one line. That line must be the first line opening `**Status:**` in both,
the line `readStatusCells` reads. Split on `·` and trimmed, both cell lists must have the same length,
and every cell but the first and the third must be byte-equal. The first cell must still read
`**Status:**` and one word. Neither the status word nor the date is graded here: check 12 owns the
status vocabulary and the date shape, and retyping either would be a second answer to its question.

Admitted writers, per §8 F1: the main loop, which carries no `agent_type`; and a role whose `writes` is
`product` when the target, in comparable form, equals the toplevel-joined spec of a `- unit:` line in
the session card's `## route`. A `spec` role needs no exemption, and every other type is refused.

### Refusal text

`renderRoleDeny` follows `renderRouteDeny`'s shape. It names the tool and target, the class, and the
writer: the main loop, a type the index does not name, or a role with another `writes`. It names the
roles the index lets write that class and the index path. For a role in that class it gives the route
that reaches it in one sentence: render its handoff with `handoff.py render --role <name> --part task`
and pass the output as the prompt of an `Agent` call whose `subagent_type` is that role, or name the
role in its harness's `roles` argument. The renderer is named by its bare file name, because a kit file
names no sibling kit by literal. A spec refusal adds that a flip of the header's status and date cells
is admitted from the main loop and from the routed unit's builder.

### Measurement — what each status-flip option lets through

PINNED, measured 2026-10-11 on node a over `git log --no-merges --since=2026-10-04 -p -U0` of spec
files at `744e55db2`, with a scratch instrument that classifies each spec file diff. A file diff is
STATUS-ONLY when its single removed and single added line are status headers differing only in the
status and date cells. A commit cannot tell an Edit from a generator write, so the content count
overstates hand edits.

| Spec file diffs since 2026-10-04 | Count |
|---|---|
| status-only, the S4 shape | 135 |
| a status line whose tail cells also moved (`order`, `ratified`) | 5 |
| new spec file | 273 |
| content diff, generator rewrites of the records region included | 973 |

The 135 transitions were SPECCED to CLOSED 100 times, SPECCED to INPROGRESS 10, OPEN to CLOSED 9,
INPROGRESS to CLOSED 9 and OPEN to INPROGRESS 7. Under the resolved option all 135 stay one Edit by
the main loop or the routed builder, the 5 tail moves go to the spec-writer, and no content diff moves
outside the spec-writer.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `loadRoleIndex` | function, the one index reader of this home | `js.function`; `lexicon.py --suggest loadRoleIndex --as js.function` answered OK |
| `checkRoleWrite` | function, steps 6a and 9a's role verdict | `js.function`; answered OK |
| `buildEditResult` | function, the file as the tool would leave it | `js.function`; answered OK |
| `checkStatusOnlyEdit` | function, S4's predicate | `js.function`; answered OK |
| `renderRoleDeny` | function, the refusal text | `js.function`; answered OK |
| `write_roles`, `run_edit` | self-test helpers | `sh.function`; answered OK |
| `ROLE_INDEX` | string constant, `.claude/roles.json` | none: no constant cell is declared in `.lexicon.conf` |

### Rollout

Lands at order 9, after `TOOL-aOrientedCast-3` committed gov's index at order 3 and
`TOOL-aOrientedCast-4` changed the builder's prompt at order 4. One commit carries the hook, its arms
and its README section. No settings change: the wired matcher already covers the four write tools. A
hook script is read afresh on every call (`memory/gotchas/settings-edit-takes-effect-mid-session.md`),
so the arm binds every session whose hooks run from a tree holding this commit, from its next write.
In gov that tree is the primary, so the moment is the landing merge, as §3 says. The hooks kit's
version and its five carriers move once, after `TOOL-aOrientedCast-7`, and `govkit.py epoch` reports
the move as owed until then.

### Files touched (estimate)

`tools/hooks/scratch-guard.js` · `tools/hooks/scratch-guard.test.sh` · `tools/hooks/README.md` · `memory/map/features/agent-cap.md` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **A second hook file for the role arm.** The arm needs the target placement, the conf, the card and
  the route that `checkRouted` already computes, and one spawn per write either way. A second file
  would copy or re-export them.
- **Reading the role from `.claude/agents/<type>.md` front matter.** The index is generated for the
  hooks to read, carries `writes` and `agent` already, and is one parse; a per-type file read would make
  a hand-written agent definition decide its own class.
- **Keying on `agent_id` as well as `agent_type`.** It would refuse a session launched as a role,
  which is the other-session handoff the `gov-session` slot opens, and buys nothing the type does not.
- **Grading the new status word against a list in the hook.** That list is check 12's, and a copy here
  is the replicated-value rot the kit authoring rule names.

## 5. Production-readiness checklist

- security — One more file read, `.claude/roles.json` under the resolved toplevel, on a spec or product
  path only, and the payload path is never put into a shell or a regex. The arm stops forgetting, not
  evasion: a Bash write, a hook-less run, a hand-edited index and a session launched as a role all pass
  it, and the header says so.
- perf / scale — One node spawn per write-tool call already, measured at 0.8–1.1 s on node a (PINNED,
  `TOOL-aRoutedQuill-2` §5). The arm adds one read and one parse of an index of a few hundred bytes, and
  a status flip adds one read of the spec. No git spawn.
- error / empty / loading states — An absent index admits as today; a broken index, an UNARMED class,
  an unplaceable flip and a throw each refuse with the reason named.
- observability — Each refusal names target, class, writer, the admitted roles, the index and the route
  to a role. No witness line is added: an absent index is the uninstalled state, and
  `TOOL-aOrientedCast-8`'s session-start report is where it shows.
- risks — From landing, a main loop resolving a merge conflict in a spec or product file by Edit is
  refused; it spawns the role or resolves with git. A defect in the class predicate refuses every spec
  write; a Bash edit or unwiring recovers, and neither is gated. Gov's index missing a writer role makes
  that class UNARMED here at landing, which AC5 observes before the close.
- testing — The arms in §7 over `scratch-guard.test.sh`'s fixture, with an index written and removed
  per arm group; every arm that exists today runs with no index, which is S5's absent case observed
  unchanged.
- migration — None in gov beyond landing. An adopter receives the arm with the hooks kit and is
  unaffected until `TOOL-aOrientedCast-8` renders its index.
- user docs — The `tools/hooks/README.md` section; the refusal text is the in-session documentation.

## 6. Acceptance criteria

- **AC1** — When `node tools/hooks/scratch-guard.js` reads a `Write` payload for a spec under the
  fixture's `builds/bx/spec/`, with the fixture's `roles.json` naming `gov-spec-writer` as `spec` and
  `gov-builder` as `product`, it exits 0 with empty stderr for `agent_type` `gov-spec-writer`. It exits
  2 for no `agent_type`, for `workflow-subagent` and for `gov-builder`, naming `gov-spec-writer`, the
  index and `handoff.py render`.
  Red when: the main loop, an untyped harness agent or the builder writes spec content, or the
  spec-writer is refused its own class.
- **AC2** — When the payload's target sits under the fixture's `ROUTED_PATHS` entry and the card routes
  a Tier-2 unit at `INPROGRESS`, the hook exits 0 for `agent_type` `gov-builder` and exits 2 naming
  `gov-builder` for no `agent_type` and for `gov-spec-writer`. With an unrouted card, `gov-builder`
  exits 2 with aRoutedQuill's `## route` refusal.
  Red when: a product write admits on the role without a buildable route, or on the route without the
  builder role.
- **AC3** — When the main loop's `Edit` changes only the status and date cells of a spec's
  `**Status:**` line, the hook exits 0, and so does a `Write` whose content is that file with only those
  cells changed. A `gov-builder` `Edit` taking its routed unit's spec from `INPROGRESS` to `CLOSED`
  exits 0, and the same edit to a spec the card does not route exits 2. A main-loop `Edit` moving the
  `rev-` cell, a `Write` moving a section 2 line beside the status, and a `MultiEdit` whose
  `old_string` the file does not hold each exit 2.
  Red when: a flip that moves any other cell or line admits, or a pure flip from the main loop or the
  routed builder refuses.
- **AC4** — With no `roles.json` in the fixture, a main-loop `Write` to a spec exits 0 and a main-loop
  product write over a buildable route exits 0, as at base. With `roles.json` holding `{`, both exit 2
  naming the index, while a `Write` to the build's `README.md` exits 0. With an index naming no `spec`
  role, a spec write exits 2 naming `UNARMED` and the class, and a `gov-builder` product write still
  exits 0.
  Red when: a broken or narrowed index turns a class off without a refusal, a records write meets the
  index, or one class's state leaks into the other's verdict.
- **AC5** — When `node tools/hooks/scratch-guard.js` reads, from this repository with
  `CLAUDE_PROJECT_DIR` set to it, a `Write` payload carrying no `agent_type` whose target is a new file
  under `memory/builds/aOrientedCast/spec/`, it exits 2 naming `gov-spec-writer` and this repository's
  `roles.json`. Nothing is written, because the hook only judges.
  Red when: gov lands its index without a `spec` writer, or the arm reads an index other than the
  target toplevel's, so the build's own acceptance, an inline spec write refused, is not met.
  fixture: this repository once `TOOL-aOrientedCast-3` has committed its index; the tree holds none at
  `646d4a73`.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `recall floor` · `recall floor arms` · `hook destinations (every declared hook path ships)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 AC4 · the base hook, which admits every spec write and admits a product write from any writer once a routed unit is buildable · FLOOR_ASSERTIONS

AC5 is a direct observation of this repository after `TOOL-aOrientedCast-3` lands and adds no arm.
The close's bar runs the legs above once; no pass runs them.

## 8. Open questions

- **F1 — How does a status flip reach a spec once the main loop and the builder may not write one?**
  Two existing rules move a header: aRoutedQuill admits a Tier-2 product write only at INPROGRESS, which
  the main loop sets after approval, and the unit harness has the builder set CLOSED in its pass
  commit. §4 "Measurement" counts 135 such flips in a week. What each option lets through:
  - (a) An Edit the hook proves touches only the status line, from the routed unit's builder alone.
    The builder's CLOSED flips pass. The main loop's 17 INPROGRESS flips are refused, so each costs a
    spec-writer spawn for one word.
  - (a+) The same proof, admitted from the main loop on any spec and from a `product` role on its
    routed unit's spec. All 135 flips pass as one Edit. Nothing beyond the status and date cells
    passes, so rev, tier, base, tail and every section stay the spec-writer's. The main loop can still
    flip a status without approval, which aRoutedQuill's ceiling already states.
  - (b) A driver or renderer verb the flip runs through Bash, which this gate never sees. Every flip
    passes, and so does every other Bash write. No such verb exists, and adding one is a new public
    surface, M3's veto 2.
  - (c) A `writes` value covering both classes for the builder. The builder could rewrite any spec,
    content included, which is the write `TOOL-aOrientedCast-4` takes away from it.
  Recommendation: (a+), the option satisfying both existing rules with the narrowest surface; (b) is
  vetoed and (c) widens the builder past what this unit prices.
  RESOLVED (agent, 2026-10-11, delegated): (a+). S4 admits a status-and-date-only flip from the main
  loop and from a `product` role on its routed unit's spec; a WONTDO that needs a tail pointer is the
  spec-writer's, because the pointer moves a tail cell.
- **F2 — How is the arm armed, and what does a repository without the roles kit see?**
  Options: (a) an absent index adds no arm; a broken index refuses both classes; an ok index naming no
  writer for a class refuses that class as UNARMED, which is aRoutedQuill's rule for its conf. (b) An
  index naming no writer for a class leaves that class unarmed and admitted. (c) An absent index in a
  repository where the roles kit is installed refuses, which needs this hook to read govkit's install
  receipt, a sibling kit's file.
  Under (b) deleting one role from the catalogue is a silent off, which the owner's no-bypass ruling
  forbids. Under (c) a kit file names a sibling by literal. Under (a) an uninstalled kit is untouched and
  an installed-but-unrendered one is reported by `TOOL-aOrientedCast-8` at session start.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a), as S5 is written.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a spec file write unless the writing agent's
agent_type names a role whose declared write class is spec, reading a generated role index json"`
ranked general readers and writers first: `read_text` and `write_text` in `gen_build_index.py`,
`read_conf`, and `build_spec_path_re` in `tools/memory-tree/tree_lib.py`. None is reachable from the
hooks kit, which is node and names no sibling kit by literal. A second probe, "admit an Edit that changes
only a spec's status header token, refuse product writes from the main loop in the PreToolUse write
gate", surfaced `check_gen_region_only` and `check_lease_only_diff` in `tools/unattended/lib-unattended.sh`,
the same only-this-region-moved shape in shell, not reachable from a hook. The seam extended is in this
kit: `checkRouted`, `readStatusCells`, `readCard` and `extractRouteUnits` in
`tools/hooks/scratch-guard.js`, and its export list, which `agent-cap.js` already requires.

Recall terms used: `scratch-guard checkRouted ROUTED_PATHS agent_type write gate spec status header
INPROGRESS CLOSED builder spec-writer role` — which surfaced this build's spec brief, `TOOL-aRoutedQuill-2`,
and `TOOL-dLandedVerdict-2` S2, which holds that a status flip keeps the rev and moves the date only, the
rule S4 encodes.
