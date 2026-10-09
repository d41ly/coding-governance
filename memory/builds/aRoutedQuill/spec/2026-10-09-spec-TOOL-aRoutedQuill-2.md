# TOOL-aRoutedQuill-2 — scratch-guard refuses a product write no buildable unit on the card owns

**Status:** CLOSED · rev-7 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 3 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aRoutedQuill-2-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aRoutedQuill-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-build-TOOL-aRoutedQuill-2-subagent-payload-probe.md](../build/2026-10-09-build-TOOL-aRoutedQuill-2-subagent-payload-probe.md) | research | TOOL-aRoutedQuill-4 |
| [2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md) | journal | TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7 |
| [2026-10-09-prompt-TOOL-aRoutedQuill-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Every product-code write needs a specced unit (owner decision D3), and today no hook sees an Edit or
a Write. This unit makes `scratch-guard.js` refuse an `Edit`, `Write`, `MultiEdit` or `NotebookEdit`
whose target lies under the repository's declared product paths, `ROUTED_PATHS`, unless the
session's orientation card routes a unit whose spec is BUILDABLE. The refusal names the missing
piece and the remedy, and it binds a subagent exactly as it binds the main loop.

## 2. Scope (IN)

- **S1** — `ROUTED_PATHS` is a `.memory-tree.conf` key: whitespace-separated repo-root-relative
  entries, a trailing `/` naming a directory. Gov declares
  `ROUTED_PATHS="tools/ skills/ coding-governance-agents.template.md WIRE-INTO-PROJECT.md"` beside
  `MEMORY_ROOT`, with a comment naming this unit. Observed by AC4 and AC9.
- **S2** — `checkRouted` in `tools/hooks/scratch-guard.js` is the predicate, and §4 "The evaluation
  order" is its ONE order, written in its comment as `checkOriented`'s is. Observed by AC1, AC2 and
  AC3.
- **S3** — BUILDABLE is decided per `- unit:` line of the card's `## route`: the spec path is
  repo-relative and sits under `<MEMORY_ROOT>/builds/<build slug>/spec/`, the file exists, its H1
  names that unit id, and its status header reads Tier-2 at INPROGRESS, Tier-1 at INPROGRESS, or
  Tier-1 at SPECCED when the micro-spec arm graded it: `SPEC_TIER1_CUTOFF` in the target's
  `.memory-tree.conf` is set and the spec's filename date is on or after it (F4). One buildable unit
  admits the write. Observed by AC1 and AC2.
- **S4** — On a product path, an absent card, a card with no `## route`, and a route with no
  buildable unit each refuse with their own reason and remedy. A card the replay wrote is read like
  any other. Observed by AC2.
- **S5** — The target is `tool_input.file_path`, else `tool_input.notebook_path`, resolved against
  the payload `cwd` when relative. The walk to `.git` runs on the native spelling; the compare runs
  on `buildComparablePath`'s form. A target under no repository, or in a repository whose common
  dir is not the session's, is not gated. A write payload carrying neither field refuses. Observed
  by AC3, AC4 and AC6.
- **S6** — A conf that declares `MEMORY_ROOT` or `ROUTED_PATHS` blank or absent, or an entry that
  is absolute, climbs through `..` or covers `MEMORY_ROOT`, is UNARMED: every write in that
  repository refuses except a write to the conf itself. An entry covering `MEMORY_ROOT` would make
  writing a spec need a spec first; `TOOL-aRoutedQuill-3` and `TOOL-aRoutedQuill-5` refuse it too. No conf at the target's toplevel admits with one witness line; a conf
  that exists and cannot be read refuses. Observed by AC5 and AC6.
- **S7** — No `agent_id` exemption: a subagent's write is judged by the same order. Observed by AC7.
- **S8** — `main` routes the four write tools to `checkRouted` under a catch that refuses with the
  error named, the fail-closed rule `agent-cap.js` keeps for its spec-audit kind. The Bash and
  PowerShell checks keep their fail-open. NOT OBSERVED by a criterion of its own: once every input
  is guarded no payload reaches a throw, so the catch is a backstop; AC6's cannot-place refusals are
  the observable class, and the builder stages a throw once when the arm goes RED first.
- **S9** — `readConfKey(bytes, key)` in `scratch-guard.js` lifts the shell grammar of
  `readSpecAuditDefault` (`agent-cap.js`), with the key compared as a string and never put into a
  regex. `readSpecAuditDefault` delegates to it through the `require` that file already makes of
  this one, so the hooks home keeps one conf grammar. Observed by AC10.
- **S10** — The shipped fragment's matcher widens to
  `Bash|PowerShell|Edit|Write|MultiEdit|NotebookEdit` and `main` dispatches on `tool_name`. Gov's `.claude/settings.json` is re-merged through
  `tools/settings-merge.py --fragment`. `check-wiring.sh`'s scratch arm reads its matcher from the
  fragment, so an unwired or hand-narrowed install reports `UNWIRED  scratch` with no edit there,
  which is owner decision D7's report. Observed by AC8.
- **S11** — The file header and a `tools/hooks/README.md` section state the gate, its order and its
  ceiling: a Bash or PowerShell write, a hook-less or `--bare` run, a narrowed key, a hand-written
  card and a status flipped without approval all pass it. NOT OBSERVED by a criterion: prose.
- **S12** — The arms live in `tools/hooks/scratch-guard.test.sh` over its existing orientation
  fixture, each observed RED before it lands, and `FLOOR_ASSERTIONS` moves by the count added.
  Observed by AC1 through AC7 and AC10.

## 3. Non-goals (OUT)

- Bash and PowerShell writes to product paths. `scanWriteTargets` reads redirect and copy shapes
  and misses `sed -i` and every interpreter write, so a textual arm here would be a partial gate
  that reads as a whole one. The build README assigns the guarantee to the push-time leg.
- Matching a write to its unit's §4 Files touched. That list is an estimate by the template's own
  name, and a gate built on it refuses honest scope growth.
- Re-running check 12 per write. "Conforms" is the bar's verdict; the gate reads the status header.
- Comparing the card's `tree —` cell, as `checkOriented` does. An isolated-worktree subagent writes
  in its own tree under the parent's card.
- A bypass, a waiver, an environment knob or a dark launch (owner decisions D4 and D7).
- Applying the scratch-litter rules (home, drive root, `/tmp`) to Edit and Write targets. A
  follow-up if one is observed; nothing here measured it.
- The check-wiring red for an install with no conf, the adopter scaffold of the key, the example
  conf, govkit's default set, and a kit version bump.

### Edges

- **consumes-from** `TOOL-aRoutedQuill-1` — the Tier-1 micro-spec profile check 12 grades. Without
  it, admitting a Tier-1 unit at SPECCED admits a status header with no body behind it, because this
  gate reads only the header.
- **consumes-from** `KICK-aRoutedQuill-1` — the card's `## route` section, its three line shapes,
  and the `--card --append` that writes it. Without it no card routes a unit and every product
  write refuses.
- **hands-off** `TOOL-aRoutedQuill-3` — the Bash-made and hook-less product writes this gate never
  sees; the push-time leg reads the same `ROUTED_PATHS` key.
- **hands-off** `TOOL-aRoutedQuill-4` — telling a subagent, before its first write, what this gate
  will admit; it reuses `checkBuildable` and the conf and card readers in `scratch-guard.js`.
- **hands-off** `TOOL-aRoutedQuill-5` — scaffolding `ROUTED_PATHS` at adoption and update before
  the widened fragment lands, the session-start red for a wired install with no conf, and the
  gate's kit in govkit's default set.
- **hands-off** `PLAY-aRoutedQuill-1` — the charter sentence that a write gate refuses product
  writes no specced unit owns.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- `checkOriented` (`tools/hooks/scratch-guard.js:687`) returns on `data.agent_id` at `:692`, so
  subagent commits are never gated. Its helpers are reused here: `readCard` (`:596`),
  `resolveToplevel` (`:560`), `resolveCommonDir` (`:581`), `buildComparablePath` (`:95`) and
  `checkUnderRoot` (`:181`).
- `main` exits 0 for any `tool_name` outside `TOOLS` (`:728`) and wraps both checks in a fail-open
  catch (`:737-741`). The deny protocol is stderr plus exit 2 (`:44`).
- `.claude/settings.json:13-25` wires `scratch-guard.js` and `gate-guard.js` in one
  `Bash|PowerShell` group, and no group matches Edit or Write.
- `settings-merge.py`'s `check_ours` (`tools/settings-merge.py:390`) calls a command a fragment's
  when it carries the fragment's marker AND the hook basename; `set_group` (`:400`) moves such an
  entry out of every same-event group whose matcher differs. The shipped fragment's marker is
  `scratch-guard.js`, the basename itself.
- `check_scratch_guard` (`tools/check-wiring.sh:687`) reads marker, matcher and path from the
  shipped fragment (`:699-706`) and reports `UNWIRED` for any other matcher (`:732-736`).
  `tools/check-wiring.test.sh:366-392` stages a stale matcher against the fragment's own.
- `add_card_body` refuses an append to an absent card and names the remedy, `--card --write
  --session <sid>` (`skills/session-kickoff/manifest-check.sh:886`).
- `readSpecAuditDefault` (`tools/hooks/agent-cap.js:1863`) is the hooks home's shell-grammar conf
  reader, and `agent-cap.js` already requires this file for `readFrontMatterKey` (`:1950`). A
  root-level conf name as a literal in a kit file has precedent at `agent-cap.js:1993`.
- Tool input fields: `Edit` and `Write` carry `file_path`, and `NotebookEdit` carries
  `notebook_path` (verified 2026-10-09, node a, from the tools' own schemas in a live session).
  `MultiEdit` is absent from that session's tool set, so its field is UNVERIFIED; `file_path` is
  read, and a payload carrying neither field refuses.
- A `PreToolUse` hook fires inside a `Workflow` sidechain, measured 2026-09-12 on node d
  (`tools/workflows/REVIEW-PROTOCOL.template.md:106-110`).

### Data model

```sh
# .memory-tree.conf — gov's declaration
ROUTED_PATHS="tools/ skills/ coding-governance-agents.template.md WIRE-INTO-PROJECT.md"
```

Step 3 compares the two common dirs after `realpath`, so an 8.3 spelling and git's long one are one
directory. The `<build slug>` of S3 is the route's `- build:` value; a route with none builds nothing.

A file is a PRODUCT PATH when its path relative to the target's toplevel, in comparable form, equals
a file entry or sits under a directory entry by `checkUnderRoot`. The route section is
`KICK-aRoutedQuill-1`'s; this unit reads it and nothing else on the card:

```markdown
## route
- build: <slug>
- unit: <unit id> · spec <repo-relative path>
- brief: <repo-relative path>
```

The section runs from its heading to the next `## ` heading or `READY — ` line. Backticks around a
token are stripped before matching. The `- brief:` line is not read here.

| Tier on the spec header | Statuses that admit a write |
|---|---|
| Tier-1 | INPROGRESS; SPECCED only when `SPEC_TIER1_CUTOFF` is set and the spec is dated on or after it |
| Tier-2 | INPROGRESS |

### The evaluation order

`checkRouted(data, env)` returns null to print nothing, `{ witness }` to allow with one stderr line,
or `{ deny }` to refuse.

1. `tool_name` outside `WRITE_TOOLS` → null.
2. No non-empty string in `file_path` or `notebook_path`, or a relative one with no payload `cwd`
   → deny, naming both fields.
3. The session repository is the common dir of `env.CLAUDE_PROJECT_DIR`, else of the payload `cwd`.
   No `.git` above the target, no session repository, or a target common dir that differs in
   comparable form → null.
4. `<target toplevel>/.memory-tree.conf` absent → witness. Present and unreadable → deny naming it.
5. UNARMED by S6 → null when the target is the conf, else deny naming the key and the conf.
6. The target under no entry → null. Only a product path reads the card.
7. `session_id` missing, or no card for it under the common dir → deny, absent.
8. No `## route`, or no `- unit:` line in it → deny, unrouted.
9. Any unit BUILDABLE by `checkBuildable` → null; else deny listing each unit's reason.

Every refusal on a product path names the target, the entry it fell under, the state, the remedy,
and that writes outside `ROUTED_PATHS`, the spec and the card included, are not gated. The remedies:
an absent card names `manifest-check.sh --card --write --session <sid>` with the id filled in, then
`/session-kickoff`; an unrouted card names `/session-kickoff`, the unit's spec, and a `## route`
appended through `--card --append`; a Tier-2 spec at SPECCED says that a Tier-2 unit admits writes
at INPROGRESS, which follows the owner's scope approval.

### Wiring

One fragment, widened. `scratch-guard.fragment.json` declares
`"matcher": "Bash|PowerShell|Edit|Write|MultiEdit|NotebookEdit"`, and `main` sends a `Bash` or
`PowerShell` payload to the two existing checks and a write tool to `checkRouted`. Re-merged in
memory at `6473ae38` over gov's `.claude/settings.json`, the fragment lands in its own group and
`gate-guard.js` stays alone under `Bash|PowerShell`. The codebase-map key
`PreToolUse tools/hooks/scratch-guard.js` does not change, because it carries no matcher.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `checkRouted` | function | `js.function`; `lexicon.py --suggest checkRouted --as js.function` answered OK |
| `checkBuildable` | function | `js.function`; answered OK |
| `extractRouteUnits` | function | `js.function`; answered OK |
| `readConfKey` | function | `js.function`; answered OK |
| `renderRouteDeny` | function | `js.function`; answered OK |
| `checkUnarmed` | function, S6's predicate | `js.function`; answered OK (rev-7) |
| `buildNativePath` | function, the MSYS drive fold for the walk | `js.function`; answered OK (rev-7) |
| `resolveComparableCommon` | function, the common dir 8.3-expanded | `js.function`; answered OK (rev-7) |
| `run_write`, `write_spec`, `write_route_card`, `write_conf`, `read_conf`, `check_stderr` | self-test helpers | `sh.function`; answered OK (rev-7) |
| `WRITE_TOOLS` | array constant | none: no constant cell is declared in `.lexicon.conf` |
| `BUILDABLE_STATUS` | object constant, tier to admitting tokens | none, as above |
| `ROUTE_CONF` | string constant, `.memory-tree.conf` | none, as above |
| `ROUTED_PATHS` | conf key | none: conf keys carry no naming cell |

### Rollout

Lands at order 3, after `TOOL-aRoutedQuill-1` at order 1 and `KICK-aRoutedQuill-1` at order 2.
One commit carries the hook, the widened fragment, gov's re-merged `.claude/settings.json` and gov's
`ROUTED_PATHS`, so gov is never wired and unarmed. A settings edit is live on the NEXT tool call, not
at the next session (`memory/gotchas/settings-edit-takes-effect-mid-session.md`, measured
2026-08-10), so enforcement begins inside the session that lands this commit. That session, and
every later one, needs a route on its card before its next product write, this build's own later
units included. `.memory-tree.conf` is on the kickoff manifest's `watch:` line, so that arming
commit also re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md` with a delta line in its
commit message. No kit version moves here: the hooks
kit bumps once, after the build's last unit touching it, and until then `govkit.py epoch` reports
the move as owed at the lander.

### Files touched (estimate)

`tools/hooks/scratch-guard.js` · `tools/hooks/scratch-guard.test.sh` · `tools/hooks/scratch-guard.fragment.json` · `tools/hooks/agent-cap.js` · `tools/hooks/README.md` · `.claude/settings.json` · `.memory-tree.conf` · `memory/guides/SESSION-KICKOFF.md` · `memory/map/features/agent-cap.md` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **A second fragment of `scratch-guard.js` with its own matcher and marker, as the shared contract
  placed it.** Rejected by an in-memory `merge()` of the two fragments over an empty settings
  object at `6473ae38`. The order shipped-then-new kept both entries; new-then-shipped, and
  shipped-new-shipped, left only the `Bash|PowerShell` entry, because the shipped marker is a
  substring of the new command and `set_group` moved it out. No marker can separate them while the
  shipped command, carrying no arguments, is a prefix of the new one. Giving the shipped fragment an
  argument appends a duplicate in every tree already wired, whose entry carries no new marker. An
  exact-argument join in `check_ours` and `matchers_of` would work, at the cost of two kits' joins.
- **A separate hook file.** One spawn either way, since nothing else fires on Edit or Write. The
  helpers this needs live in `scratch-guard.js`, and a second file would copy or re-export them.
- **Gating a target by its own repository's conf.** A scratch clone of this repository carries
  `ROUTED_PATHS` and no card, so a Write into a frozen-clone suite or a sliced suite inside a kit
  directory would refuse with a remedy that cannot apply there.
- **Reading `MEMORY_ROOT` as `memory` when absent.** That retypes the hygiene engine's default
  (`tools/memory-tree/check-memory-hygiene.sh:37`); an absent key is UNARMED instead.
- **JSON `permissionDecision` instead of exit 2.** Both reach the model, and this file keeps one
  protocol (`:44`).

## 5. Production-readiness checklist

- security — Three file reads, the conf, the card and at most one spec per routed unit, all under
  the resolved toplevel and common dir; no spawn. The payload path locates files and is never put
  into a shell or a regex, and the key reaches `readConfKey` as a string compare. The gate stops
  forgetting, not evasion, and S11's ceiling says so in the header.
- perf / scale — One node spawn per write-tool call, measured at 0.8–1.1 s on node a (PINNED:
  verdict 13 of the aReplayedCard design record, 2026-09-13, which priced exactly this at its line
  427). No git spawn. A non-product write reads only the conf, 71,782 bytes in gov (PINNED,
  `wc -c`, 2026-10-09).
- error / empty / loading states — A missing path field, an unreadable conf, an UNARMED conf and a
  throw each refuse with a named reason; an absent conf admits with a witness line.
- observability — Each refusal names target, entry, state and remedy. The absent-conf witness
  reaches the debug log and the self-test only, as the header's protocol note already states.
- risks — A defect in the predicate refuses every product write; a Bash edit or unwiring
  `.claude/settings.json` recovers, and neither is gated. A subagent that cannot find its parent's
  card refuses every product write, which §8 F1's probe decides before the build. A builder session
  restarted inside its own worktree after the rewire runs the hook it is editing.
- testing — The arms in §7 over `scratch-guard.test.sh`'s scratch repository and linked worktree,
  plus a second `git init` for the foreign-repository case; `agent-cap.test.sh`'s existing
  `SPEC_AUDIT_DEFAULT` arms re-observe the lifted grammar unchanged.
- migration — Gov's re-merge and key in one commit. Adopters move with `TOOL-aRoutedQuill-5`.
- user docs — The `tools/hooks/README.md` section; the deny text is the in-session documentation.

## 6. Acceptance criteria

- **AC1** — When the self-test feeds a `Write` payload whose target sits under the fixture's
  `tools/` entry and whose card routes one unit, the hook exits 0 with empty stderr for a `Tier-2`
  spec at `INPROGRESS` and for a `Tier-1` spec at `SPECCED` dated on or after the fixture's
  `SPEC_TIER1_CUTOFF`. It exits 2 naming the unit, `Tier-2` and `INPROGRESS` for a Tier-2 spec at
  `SPECCED`, and naming `SPEC_TIER1_CUTOFF` for a Tier-1 spec at `SPECCED` dated before the cutoff
  or with the key blank. A route of two units, one buildable, exits 0.
  Red when: a Tier-2 unit admits writes before INPROGRESS, a graded Tier-1 unit at SPECCED refuses,
  an ungraded Tier-1 unit at SPECCED admits, or an unbuildable unit refuses a route that also holds
  a buildable one.
- **AC2** — When the target is a product path and the card is absent, the hook exits 2 naming the
  card path, the session id and `--card --write`; with no `## route`, it exits 2 naming `## route`
  and `/session-kickoff`; when a `- unit:` line names a missing spec, a spec outside
  `builds/<slug>/spec/`, or a spec whose H1 names another unit, it exits 2 naming the unit and the
  reason; a card whose header names `--card --replay` and routes a buildable unit exits 0.
  Red when: an absent or unrouted card admits a product write, a route line is trusted without
  reading its spec, or a replay-written card is judged differently from a written one.
- **AC3** — When the target sits under the suite's temp root and no repository, or in a second
  repository that declares `ROUTED_PATHS` and is not the session's, or in the session's repository
  outside every entry, the hook exits 0 with empty stderr over an unrouted card; when the target
  sits under the fixture's linked worktree and `CLAUDE_PROJECT_DIR` is the primary, it exits 2.
  Red when: a scratch clone's writes are gated by its own conf, a non-product write reads the card,
  or a linked worktree of the session's repository escapes the gate.
- **AC4** — When the product target arrives with backslashes, with upper-case segments, as
  `notebook_path` on a `NotebookEdit` payload, or as `file_path` on a `MultiEdit` payload, the hook
  exits 2 over an unrouted card; a sibling directory whose name extends an entry, `toolsx` beside
  `tools/`, and a file whose name extends a file entry each exit 0.
  Red when: a spelling of a product path escapes the compare, or the boundary matches a prefix that
  is not a whole segment.
- **AC5** — When the fixture's conf declares `ROUTED_PATHS=""`, a `Write` to any other file exits 2
  naming `UNARMED`, `ROUTED_PATHS` and the conf, and a `Write` to the conf exits 0; the same holds
  with `MEMORY_ROOT` blank, with an entry that climbs through `..`, and with an entry covering
  `MEMORY_ROOT`; with no conf in the fixture,
  a write to its `tools/` directory exits 0 with one witness line naming the absent conf.
  Red when: a blank or malformed key turns the gate off without a refusal, or the refusal also
  blocks the one edit that arms it.
- **AC6** — When a `Write` payload carries neither `file_path` nor `notebook_path`, or a relative
  `file_path` and no `cwd`, the hook exits 2 naming the fields; when the fixture's conf path is a
  directory, so its read fails with something other than `ENOENT`, it exits 2 naming the conf.
  Red when: the write branch fails open on a payload or a conf it cannot read.
- **AC7** — When the payload carries `agent_id` and the parent's `session_id`, the hook exits 0 on a
  buildable route and 2 on an unrouted card, exactly as for the main loop.
  Red when: a subagent's product write is exempt, as `checkOriented` exempts its commits.
- **AC8** — When `python tools/settings-merge.py --check --fragment tools/hooks/scratch-guard.fragment.json`
  runs here after the rewire it exits 0, and `.claude/settings.json` holds `scratch-guard.js` once
  under PreToolUse, under the widened matcher, with `gate-guard.js` alone under `Bash|PowerShell`;
  `bash tools/check-wiring.sh --check` prints `ok       scratch` naming the widened matcher.
  Red when: the merge leaves two scratch-guard entries, strands gate-guard, or check-wiring reads
  the guard as unwired.
- **AC9** — When `node -e` loads the hook's exported `readConfKey` over this repository's
  `.memory-tree.conf`, `ROUTED_PATHS` reads
  `tools/ skills/ coding-governance-agents.template.md WIRE-INTO-PROJECT.md`; and a `Write` payload
  for `tools/hooks/README.md` from this repository, under a session id with no card, exits 2.
  Red when: gov ships wired with its key blank or unquoted, so every write here meets the UNARMED
  refusal, or gov's own product path is not gated.
- **AC10** — When `readConfKey` reads bytes holding two assignments, an `export` prefix, both quote
  styles, a trailing `# comment` behind whitespace and a `#` glued to a bare word, it returns the
  last assignment's value as the shell reads it; and `agent-cap.js` fed a conf in each
  `SPEC_AUDIT_DEFAULT` spelling its existing arms use gives the verdicts it gave at base.
  Red when: the lifted grammar reads a spelling differently from the shell, or the two hooks keep
  two grammars.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `check-wiring self-test` · `lexicon naming predicates` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `straggler-guard arms` · `transition-audit arms` · `settings-merge selftest` · `hook destinations (every declared hook path ships)` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kickoff-manifest ratchet`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC10 · the base hook, which exits 0 for every Edit, Write, MultiEdit and NotebookEdit payload and has no readConfKey · FLOOR_ASSERTIONS

AC8 and AC9 are direct observations of this repository after the rewire and add no arm.
`tools/check-wiring.test.sh`'s stale-matcher arm already reads the matcher from the fragment.

## 8. Open questions

- **FACT-QUESTION · F1 — Does a subagent's PreToolUse payload carry the parent session's `session_id`?**
  The card is keyed by session id. If a subagent carries its own, every subagent product write meets
  the absent-card refusal, and a build pass is a subagent
  (`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-35.md:211`). Prior
  evidence is indirect: `CLAUDE_CODE_SESSION_ID` in a sidechain agent's Bash environment carried
  the parent's id (`memory/builds/dLoggedFlight/build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md:61`),
  which is the environment and not the hook payload.
  Probe: a throwaway clone under a short TEMP root whose `.claude/settings.json` adds a PreToolUse
  hook on `Write` and a SubagentStart hook, each appending one JSON line of `hook_event_name`,
  `session_id`, `agent_id`, `agent_type`, the `tool_input` keys and `CLAUDE_CODE_SESSION_ID` from
  its own environment to a scratchpad log. One `claude -p` session, never `--bare`, which skips
  hooks, has the main loop Write one scratch file, spawn one `Agent` subagent and run one
  `Workflow` script with one agent, each writing one scratch file.
  Deciding observation: every line carrying `agent_id` has a `session_id` byte-equal to the
  main-loop Write line's.
  Liveness: the log holds at least one main-loop Write line and at least one `agent_id` line per
  spawn kind; fewer is a DEAD PROBE for that kind, never a "no".
  Options if no: (a) key the card on the hook's own `CLAUDE_CODE_SESSION_ID` where the probe shows
  it holds the parent's id; (b) have TOOL-aRoutedQuill-4's SubagentStart hook link the subagent's
  id to the parent's card, which needs that payload to carry both; (c) admit any card in the
  common dir, rejected because one session's route would admit another session's subagent.
  Recommendation: run the probe before the build pass, expecting yes; on a no, take (a) where the
  environment carries the id, else (b).
  RESOLVED (agent, 2026-10-09, delegated): yes. Every `agent_id` line, for an `Agent` subagent and a
  `Workflow` agent alike, carried the main loop's `session_id` byte-equal; the card keyed by the
  payload's `session_id` is the parent's, and no option is taken. Evidence: `memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-2-subagent-payload-probe.md`.
- **F2 — On a product path, does an absent or replay-written card refuse, unlike the commit deny?**
  `checkOriented` admits both, because during aReplayedCard's own landing the remedy was out of
  reach (`memory/builds/aReplayedCard/spec/2026-09-13-spec-TOOL-aReplayedCard-1.md:228-232`).
  Option refuse: the remedy is reachable now, since the writer has been wired in gov since
  aReplayedCard and `--card --write --session <sid>` creates a card for a running session, with the
  refusal printing the id. Admitting absence would make a deleted or never-written card a silent
  off of a gate D7 gives no bypass. A replay-written card is a real card `--card --append` writes
  to. Option admit: no session is refused for a card it lacks, and the gate stops binding every
  install whose writer is not wired, which is every adopter until TOOL-aRoutedQuill-5.
  Recommendation: refuse both, as S4 and the evaluation order are written.
  RESOLVED (owner, 2026-10-09): refuse both, as S4 and the evaluation order are written.
- **F3 — Where does an UNARMED conf go red?**
  Option (a), as written: the hook refuses every write in the repository except to the conf, naming
  the key. Option (b): the hook admits, and the red is a session-start line in `check-wiring.sh`.
  Under (b) a key blanked mid-session is a silent off until the next session start, because an
  exit-0 witness line reaches nobody (`tools/hooks/scratch-guard.js:66-69`). Under (a) arming is
  the one edit the refusal names and exempts. Neither stops a narrowed key; that is a visible conf
  diff and TOOL-aRoutedQuill-3's leg.
  Recommendation: (a), with TOOL-aRoutedQuill-5's session-start report covering an install that
  has no conf at all. That report is a printed `UNWIRED  routed` line, since `check-wiring.sh
  --session` always exits 0; only its `--check` mode can fail.
  RESOLVED (owner, 2026-10-09): (a). The hook refuses every write in an unarmed repository except to the conf.
- **F4 — Does a Tier-1 spec the micro-spec arm never graded admit writes at SPECCED?**
  `TOOL-aRoutedQuill-1`'s F1 hands this decision here. A Tier-1 spec dated before
  `SPEC_TIER1_CUTOFF`, or in a tree whose key is blank, reaches SPECCED with nothing checking its
  sections, and every adopter is in that state until it arms the key. Option (a), as S3 is
  written: admit every Tier-1 spec at SPECCED. Option (b): admit a Tier-1 spec at SPECCED only when
  the key is set and the spec's filename date is on or after it, else only at INPROGRESS. Option
  (c): refuse such a spec outright. Recommendation: (b). D6 admits a Tier-1 spec once it CONFORMS,
  and only (b) admits nothing the arm has not graded; it costs one conf read and one string compare
  in `checkBuildable`. Taking (b) moves S3 and AC1 in a rev-3.
  RESOLVED (owner, 2026-10-09): (b). S3, the admission table and AC1 now admit a Tier-1 spec at SPECCED only when graded.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §3 · §4 · §8 · S6 · AC5 · cross-read fold: order 2 to 3, because
  `KICK-aRoutedQuill-1` moved to order 2 when it and `TOOL-aRoutedQuill-1` were found to share the
  kickoff manifest's stamps; S6 and AC5 now treat an entry covering `MEMORY_ROOT` as UNARMED, as
  units 3 and 5 already did; F3 says the session-start report prints rather than reds; F4 carries
  the Tier-1 admission fork unit 1 handed here.
- rev-3 · 2026-10-09 · §4 · §8 · S3 · AC1 · owner resolves F2 (refuse an absent or replay-written
  card), F3 (a) and F4 (b): a Tier-1 spec admits at SPECCED only when `SPEC_TIER1_CUTOFF` graded it.
- rev-4 · 2026-10-09 · §4 · Rollout corrected: hooks are re-read on the next tool call, per the
  gotcha catalogue's measurement, so enforcement starts inside the landing session, not after it.
- rev-5 · 2026-10-09 · §4 · §7 · the M2 cross-read of 2026-10-09 found Rollout's arming commit
  stages `.memory-tree.conf`, which the kickoff manifest watches, with no manifest re-stamp; Rollout
  now re-stamps `last-audit` with a delta line, Files touched gains
  `memory/guides/SESSION-KICKOFF.md` and Gates gains `kickoff-manifest ratchet`.
- rev-6 · 2026-10-09 · §8 F1 · resolved by the stated probe, run by the unattended run before step 3; the record is `memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-2-subagent-payload-probe.md`.
- rev-7 · 2026-10-09 · §4 · the build pass: the Inventory gains three hook helpers and the self-test's helpers; the common-dir compare in step 3 runs on the realpath, because a linked worktree's `gitdir:` carries git's long spelling while `CLAUDE_PROJECT_DIR` may carry the 8.3 one; BUILDABLE also needs the route's `- build:` line, the slug S3 names; and `run_card`'s stderr grading moved into `check_stderr`, shared with `run_write`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse an Edit or Write tool call whose target file is
under declared product paths unless the session orientation card routes a specced unit; read a key
from .memory-tree.conf in node"` ranked the conf readers first: `readMemoryRoot` in
`tools/unattended/gate-guard.js` and `tools/unattended/run-lease.js`, and the Python `load_conf`
family. None is reachable from the hooks kit, which names no sibling kit by literal and cannot
assume the opt-in unattended kit is installed (`tools/hooks/README.md`, "The authoring rule for kit
files"). The extended seams are in this kit: `checkOriented`'s helpers in
`tools/hooks/scratch-guard.js`, and `readSpecAuditDefault` in `tools/hooks/agent-cap.js`, whose
grammar `readConfKey` lifts so the home keeps one reader. The wiring extended is the inventory key
`PreToolUse tools/hooks/scratch-guard.js`.

Recall terms used: `scratch-guard checkOriented orientation card sentinel replay-written absent
witness PreToolUse agent_id session_id ROUTED_PATHS Edit` — which surfaced `TOOL-aReplayedCard-1`
and its §8 on absent cards, the aReplayedCard design record's priced cut on gating Edit and Write,
and `TOOL-dDerivedDocket-35`, which records that a build pass is a subagent.
