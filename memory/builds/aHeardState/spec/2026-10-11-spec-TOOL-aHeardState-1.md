# TOOL-aHeardState-1 — format-guard: the turn end refuses a final message without the BUILD/SPEC pair or a committed line

**Status:** INPROGRESS · rev-2 · 2026-10-12 · node a · Tier-2 · base 2f01150c · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-TOOL-aHeardState-1-1-live-witness.md](../build/2026-10-12-build-TOOL-aHeardState-1-1-live-witness.md) | journal | — |
| [2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md) | research | TOOL-aHeardState-2 |
| [2026-10-13-review-TOOL-aHeardState-1-2-closing-diff-review-round1.md](../reviews/2026-10-13-review-TOOL-aHeardState-1-2-closing-diff-review-round1.md) | diff-review | TOOL-aHeardState-2 |

<!-- /gen:spec-records -->

## 1. Goal

The charter's micro-formats are mandatory, and emission has no machine gate: session 86a064cd emitted
none across 1,162 assistant entries. A `Stop` hook can see the final message at the one moment the
session decides to end its turn. This unit makes that hook refuse the turn end when a session routed
to a live build omits the `BUILD`/`SPEC` pair, breaks rule r1, or leaves a new commit unreported.

## 2. Scope (IN)

- **S1** — `tools/hooks/format-guard.js`, a `Stop` hook. It ARMS only when all three hold: the
  payload's `session_id` has an orientation card at `<git-common-dir>/orientation/<sid>.md`; the
  card's `## route` carries a `- build: <slug>` line; and `<slug>` is a row of
  `<MEMORY_ROOT>/LIVE.md` under the payload `cwd`'s toplevel. Unarmed, it exits 0 and prints nothing.
  AC5.
- **S2** — the shape grammar is DERIVED from the `<!-- microformats -->` fence of the toplevel's
  `AGENTS.md`: each definition line becomes a line regex, placeholder `<…>` as a run carrying no
  ` · `, literal text literal, `[ · …]` an optional group, anchored at a column-0 `- `. No fence, or
  no definition for a needed head keyword, allows with one stderr witness line. AC7, AC8.
- **S3** — the pair check reads the payload's `last_assistant_message`. It blocks when the `BUILD`
  line is missing; when the `SPEC` line is missing while the route names a unit with a `· spec`
  path; when the line after the last bare `BUILD` line is not a bare `SPEC` line; when either line
  fails r1, written backticked, bold, indented, as a heading, inside a fence, or without its `- `;
  and when either line fails its derived shape. An absent `last_assistant_message` allows with a
  witness line. AC1, AC2, AC3, AC4, AC8.
- **S4** — the commit check. The hook keeps the last HEAD it saw in a per-worktree sidecar,
  `<git-dir>/format-guard/<sid>.head`. When HEAD differs from the sidecar, every first-parent commit
  in `<sidecar>..HEAD` must be named by a bare `- committed — <sha>` or `- merged — … · <sha>` line
  whose sha field is a prefix of at least 7 hex of that commit. The first armed stop of a session
  records a baseline and requires nothing. A sidecar sha that is not an ancestor of HEAD writes a
  witness and blocks nothing. Git is spawned only when HEAD moved. AC6.
- **S5** — the bound. The hook never blocks when `stop_hook_active` is true, so it refuses at most
  once per turn end and keeps no block count. A payload carrying `agent_id`, any event but `Stop`,
  unreadable stdin and any thrown error exit 0. The block is `{"decision":"block","reason":…}` on
  exit 0, the reason naming each defect and quoting the charter definition it breaks. AC1, AC9.
- **S6** — the card and route readers are scratch-guard's, imported from `tools/hooks/scratch-guard.js`
  through its existing `module.exports`, widened by `resolveToplevel` and `resolveCommonDir`. AC5.
- **S7** — wiring: `tools/hooks/format-guard.fragment.json` (`Stop`, matcher `*`, marker
  `format-guard.js`), merged into `.claude/settings.json` by `tools/settings-merge.py --fragment`; a
  `[[files]]` rule per new file in `tools/hooks/kit.toml`; a section in `tools/hooks/README.md`; and
  a held `format-guard self-test` row in `tools/gate-legs.json` running
  `tools/hooks/format-guard.test.sh`, shaped like `scratch-guard self-test`'s. AC10.
- **S8** — the header names what the hook does NOT check: emission mid-turn; the ⏳ heartbeat; every
  other micro-format; field VALUES; where in the message the pair sits; sub-agent stops; every stop
  after a block in the same chain, whichever hook blocked; and whether it is wired. NOT OBSERVED —
  comment prose, which no arm reads.
- **S9** — the in-tree witness: the hook, run as the wired command runs it, against this run's own
  orientation card, this tree's `memory/LIVE.md`, charter and HEAD, with only the Stop payload built
  by hand, recorded in a `build/` record together with the turn this run ended without the pair. The
  harness half — that a session started in a tree carrying the wiring delivers `last_assistant_message`
  and surfaces the block — is handed to the owner, because this session's hooks load from the tree it
  was launched in (F4). AC11.

## 3. Non-goals (OUT)

- Grading emission mid-turn, the ⏳ heartbeat, the `gates`, `pushed`, `READY`, `up`, `unchanged` or
  `skipped` lines, or any field VALUE: a well-formed pair naming the wrong build passes.
- Grading where in the message the pair sits (the `[state]` rule) or that the final message opens
  with its highest-severity item.
- Any change to the charter template, its micro-format block or its rules.
- A block count, a sidecar log of blocks, or a knob: S5's stateless bound replaces them.
- A `check-wiring.sh` arm proving the hook is wired; that kit owns wiring checks, and a follow-up may
  add one.
- The transcript measure, which is `TOOL-aHeardState-2`.

### Edges

- **hands-off** `TOOL-aHeardState-2` — the pair grammar this unit derives, which the transcript measure
  re-uses under a parity arm rather than restating.
- **hands-off** external — a `check-wiring.sh` arm that reports an unwired `format-guard` belongs to the
  check-wiring kit.

## 4. Design

### Data model

The hook reads, in order, and stops at the first miss with an exit-0 allow:

| Step | Read | Miss |
|---|---|---|
| 1 | stdin JSON; `hook_event_name` is `Stop`, no `agent_id` | silent |
| 2 | `stop_hook_active` false | silent |
| 3 | `cwd` → toplevel → common dir (scratch-guard's walk) | silent |
| 4 | the card for `session_id`, its `## route` and `- build:` line | silent |
| 5 | `.memory-tree.conf`'s `MEMORY_ROOT`, then `<MEMORY_ROOT>/LIVE.md` holds a table row whose link target is `builds/<slug>/README.md` | silent |
| 6 | `AGENTS.md`'s fence holds `BUILD`, `SPEC`, `committed` and `merged` definitions | witness |
| 7 | `last_assistant_message` is a string | witness |

Then the pair check (S3) and the commit check (S4) run, each appending defects. Any defect blocks.
The sidecar is written on every armed stop that reaches step 7, block or allow, after the checks.

The line classifier walks the message once. A fence opens and closes on a line starting with
three backticks or three tildes. A line is BARE for head `H` when it is outside a fence and starts with
`- H — ` at column 0. A line is a NON-BARE candidate for `H` when it carries `H — ` anywhere else.

### Rollout

The fragment lands with the hook in one commit. Wiring it into this branch's `.claude/settings.json`
arms it against this run's own stops on the next tool call
(`memory/gotchas/settings-edit-takes-effect-mid-session.md`). Every other session sees it only when
the branch lands, which is the owner's act: this run closes into an owner-landing hand-off.

### Files touched (estimate)

- `tools/hooks/format-guard.js`
- `tools/hooks/format-guard.fragment.json`
- `tools/hooks/format-guard.test.sh`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/kit.toml`
- `tools/hooks/README.md`
- `tools/hooks/agent-cap.js`
- `.claude/settings.json`
- `tools/gate-legs.json`

### Alternatives rejected

- **A block count in a sidecar, as `stop-guard.js` keeps.** It buys a second correction per turn at
  the cost of a file the hook must write before it may block. The harness's own `stop_hook_active`
  already says whether this stop follows a block, so the stateless bound is the smaller mechanism.
- **The terminal-status set restated in the hook.** `memory/LIVE.md` is the generated non-terminal
  set and `gen_build_index.py --check` keeps it current, so reading it restates nothing.
- **Reading the template, `coding-governance-agents.template.md`.** An adopter holds only the
  rendered charter, and `adopt-playbook.sh --check` proves the two equal at gov.
- **Parsing the transcript for the final message.** The payload carries `last_assistant_message`
  (the aWokenSentinel keepalive research record), and a transcript walk is a second reader of a
  format the harness owns.

## 5. Production-readiness checklist

- security — no new write surface beyond the sidecar under the session's own git dir; the card path
  is joined only for an id-shaped session id, as `readCard` already refuses.
- perf / scale — one card read, one LIVE.md read, one charter read per stop; one git spawn only when
  HEAD moved, ~751 ms on node a.
- error / empty / loading states — every unreadable input allows; a missing grammar or message allows
  with a witness line.
- observability — the block reason names each defect; stderr carries one witness line per degraded
  allow.
- risks — a false block costs one extra turn and cannot loop (S5); a grammar edit in the charter moves
  the hook with it, by design.
- testing — `tools/hooks/format-guard.test.sh` pipes payloads over a fixture repository.
- migration — N/A — no data; the first armed stop writes the sidecar baseline.
- user docs — the hooks kit README section; there is no `help/` tree in this repository.

## 6. Acceptance criteria

- **AC1** — When a `Stop` payload whose `last_assistant_message` carries no pair is piped to
  `node format-guard.js` under a fixture card routing a build that the fixture
  `memory/LIVE.md` lists, stdout is `{"decision":"block",…}` naming the missing `BUILD` line, and the
  same payload with `stop_hook_active: true` prints nothing. Red when: the hook exits silently on the
  first payload, or blocks on the second.
- **AC2** — When the pair is written backticked, indented two spaces, bold, under a `##` heading, or
  inside a fenced block, each payload blocks naming rule r1 and quoting the line. Red when: any
  one of the five reads as bare.
- **AC3** — When the `SPEC` line precedes the `BUILD` line, or a blank line separates them, the
  payload blocks naming adjacency. Red when: either order passes.
- **AC4** — When the message ends with a well-formed adjacent bare pair, `node format-guard.js`
  exits 0 with empty stdout. Red when: a correct pair blocks.
- **AC5** — When the fixture has no card, a card without `## route`, a route whose build is absent
  from `memory/LIVE.md`, or the payload carries `agent_id`, the hook exits 0 with empty stdout and
  empty stderr. Red when: any unarmed case blocks or writes a witness.
- **AC6** — When the fixture HEAD moves one commit past the sidecar and the message names no
  `committed` line, the payload blocks naming the new commit's short sha; when the message adds
  `- committed — <sha7> · <branch> · <subject>`, it exits 0; on a session's first armed stop it
  writes `<git-dir>/format-guard/<sid>.head` and blocks nothing. Red when: an unreported commit
  passes, or a reported one blocks.
- **AC7** — When the fixture `AGENTS.md` loses its `<!-- microformats -->` fence, a pair-less message
  exits 0 with one stderr line naming the missing fence; when the fixture's `BUILD` definition gains a
  fourth field, a message correct under the real charter blocks naming the shape. Red when: the hook
  blocks with no grammar, or the edited definition changes nothing.
- **AC8** — When a `BUILD` line drops its `left` field, the payload blocks quoting the charter's
  `BUILD` definition. Red when: a line with the wrong field count passes.
- **AC9** — When stdin is not JSON, `node format-guard.js` exits 0 with empty stdout.
  Red when: a parse error exits non-zero, which the harness reads as a block.
- **AC10** — When `python tools/settings-merge.py --fragment format-guard.fragment.json --check`
  runs against `.claude/settings.json`, it reports the fragment wired, and
  `bash tools/check-hook-destinations.sh` exits 0. Red when: the fragment is unwired, or its
  `hook_path` names no shipped destination.
- **AC11** — When the witness message this run's session ended a turn with is piped to
  `format-guard.js` with this session's id and this tree as `cwd`, the hook reads the real card's
  `- build: aHeardState` route and the real `memory/LIVE.md` row and blocks; the same message carrying
  this build's pair allows; both recorded in a `memory/builds/aHeardState/build/` record. Red when:
  the real inputs leave the hook unarmed, or the paired message blocks.
  permission: the harness half needs a session launched in a tree carrying the wiring, which this
  run's session is not; it is the owner's observation at the hand-off.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test` · `check-wiring self-test` · `lexicon naming predicates` · `run-gates canary` · `run-gates gov canary`

New arm: tools/hooks/format-guard.test.sh, the new held leg `format-guard self-test` · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 · payloads piped over a fixture repository with a card, a LIVE.md, a charter fence and a moved HEAD · none

## 8. Open questions

- **F1 — Should the hook land dark behind a default-off switch, per the charter's `[small]` practice?**
  Options: a conf key read at arm time; an environment kill switch; no switch, the wiring itself
  being the switch. Recommendation: no switch. The arm condition already confines it to a session
  routed to a live build, and this run does not land, so the owner decides at the hand-off whether
  gov's wiring goes on. A conf key would be a new public surface (M3 veto 2).
  RESOLVED (agent, 2026-10-11, delegated): no switch; the owner-landing hand-off is the on-switch.
- **F2 — Does a `merged` line report a commit, or only `committed`?** Recommendation: both, because a
  reconcile merge is a commit the session made and the charter gives it its own shape.
  RESOLVED (agent, 2026-10-11, delegated): both; the sha field of either shape counts.
- **F3 — Share scratch-guard's readers, or copy them?** The charter's `[reuse]` says extract at the
  second instance. scratch-guard already exports `readCard`, `extractRouteUnits` and `readConfKey`;
  widening its export list by two names is the smallest seam.
  RESOLVED (agent, 2026-10-11, delegated): import through scratch-guard's `module.exports`.
- **FACT-QUESTION · F4 — Can this run's own session observe the wired hook end to end?** Probe: end one
  turn without the pair after the wiring commit, and look for `Stop hook feedback:`. Liveness: the
  same session's stop-guard is wired and RUN.md binds the session, so a run-open block would appear
  if this tree's hooks were the ones loaded. Observation, 2026-10-12: the turn ended with no feedback
  from either hook, and the Bash environment carries no `CLAUDE_PROJECT_DIR`; the session was launched
  in another worktree and moved here, so its hooks resolve there, where no aHeardState RUN.md exists.
  RESOLVED (agent, 2026-10-12, delegated): no; AC11 is observed in-tree on the real inputs, and the
  harness half goes to the owner.

## 9. Revision log

- rev-1 · 2026-10-11 · first draft, from the brief record and the kickoff's design defaults.
- rev-2 · 2026-10-12 · S9 · AC11 · §8 · the end-to-end witness turn drew no feedback, because this
  session's hooks load from its launch tree (F4); AC11 now observes the hook on the real card, LIVE.md,
  charter and HEAD, and the harness half is the owner's at the hand-off.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "stop hook that inspects the last assistant message"` names the
`harness-hooks` inventory rows, `Stop tools/unattended/stop-guard.js` among them; this unit takes
stop-guard's payload reading and block shape, and scratch-guard's card and route readers
(`tools/hooks/scratch-guard.js`), and the fence keying of `tools/check-microformats.sh`. No existing
seam reads a final message, so the pair classifier is new.

Recall terms used: micro-format emission final message BUILD SPEC pair state block stop hook chat-prose audit narration
