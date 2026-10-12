# TOOL-aOrientedCast-14 — the role gate reads past every launcher option, and both role arms find the session's checkout

**Status:** OPEN · rev-3 · 2026-10-12 · node a · Tier-2 · base 646d4a73 · streams tooling · order 14 · ratified 2026-10-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-prompt-TOOL-aOrientedCast-12-1-spec-brief.md](../prompts/2026-10-12-prompt-TOOL-aOrientedCast-12-1-spec-brief.md) | journal | TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-15 |
| [2026-10-12-prompt-TOOL-aOrientedCast-12-2-fold-brief.md](../prompts/2026-10-12-prompt-TOOL-aOrientedCast-12-2-fold-brief.md) | journal | TOOL-aOrientedCast-12 |
| [2026-10-12-prompt-TOOL-aOrientedCast-13-1-fold-brief.md](../prompts/2026-10-12-prompt-TOOL-aOrientedCast-13-1-fold-brief.md) | journal | TOOL-aOrientedCast-13 TOOL-aOrientedCast-15 |

<!-- /gen:spec-records -->

## 1. Goal

This unit closes review items M2 and M3 of
[the closing review, round 1](../reviews/2026-10-12-review-TOOL-aOrientedCast-1-closing-diff-round1.md).
`scanCommandHeads` in `tools/hooks/scratch-guard.js` steps past one launcher option, so
`bash -o pipefail <runner>` and `python -X utf8 <suite>` reach a role agent unrefused; and rule 6 in
`tools/hooks/agent-cap.js` and `checkRoleGate` read the role index only from the payload cwd, so a
session whose shell has left the checkout arms neither. This unit steps past every option a
launcher or a prefix word takes, and anchors both arms on the payload cwd, then on
`CLAUDE_PROJECT_DIR`.

## 2. Scope (IN)

- **S1** — A rule table `GATE_OPTION_RULES` beside `GATE_LAUNCHERS` (`scratch-guard.js:1198`) states,
  per launcher family and per prefix word, the options that take the next word as their argument,
  the options that end the simple command because it runs no script, and the options whose next word
  is a command body. §4 "The rule table" is its content. Observed by AC1 and AC2.
- **S2** — `scanLauncherOptions`, a new function, steps from a word index past every option of one
  rule: a word opening `-`, or `+` for a shell. It returns the index of the next non-option word, or
  -1 when the simple command ends; a body option scans its next word once through `scanCommandHeads`
  at depth 0 before it returns -1, as `-c` does today. A `--` is stepped past and ends the options.
  Observed by AC1 and AC2.
- **S3** — `scanCommandHeads` (`scratch-guard.js:1232-1286`) calls `scanLauncherOptions` after each
  prefix word and after the launcher, in place of its one-option step. `exec`, `command` and `nice`
  join `GATE_PREFIX_WORDS` (`:1200`). Observed by AC1 and AC2.
- **S4** — `resolveRoleRoot(cwd, env)`, a new exported function in `scratch-guard.js`, returns the
  toplevel above the payload cwd, else the toplevel above `env.CLAUDE_PROJECT_DIR`, else null, each
  start resolved as `checkRouted` resolves its session start (`:1131-1133`). Observed by AC3 and AC4.
- **S5** — `checkRoleGate(cmd, data, env)` takes `env`, which `main` passes as `process.env`
  (`:1540`), and reads its root through `resolveRoleRoot`. With no root it returns null, or one
  witness when `CLAUDE_PROJECT_DIR` is set: `role-gate unarmed — neither the payload cwd <cwd> nor
  CLAUDE_PROJECT_DIR <dir> lies in a checkout, so no role index was read`. G1 still resolves the
  command's paths against the payload cwd, and against the root when the payload has none. Observed
  by AC3.
- **S6** — Rule 6 in `agent-cap.js` (`:2253-2266`) reads its root through the sibling's
  `resolveRoleRoot(data.cwd || process.cwd(), process.env)` in place of `resolveCheckoutRoot`. With no
  root it adds no rule, and writes `agent-cap: rule 6 unarmed — neither the payload cwd <cwd> nor
  CLAUDE_PROJECT_DIR <dir> lies in a checkout, so no role index was read` to stderr when
  `CLAUDE_PROJECT_DIR` is set. Observed by AC4.
- **S7** — Both suites stop inheriting the caller's `CLAUDE_PROJECT_DIR`. `agent-cap.test.sh` unsets
  it in its prologue, and `scratch-guard.test.sh`'s `run_role_bash` runs the hook under
  `env -u CLAUDE_PROJECT_DIR`, adding it back only for an arm that names one, the shape
  `run_sub_hook` already has (`scratch-guard.test.sh:1124-1131`). Observed by AC5.
- **S8** — The headers and the README say the new reading. `scratch-guard.js`'s fourth-check block
  (`:105-119`) and the README's role-gate section (`tools/hooks/README.md:407-412`) say a launcher's
  options and a prefix word's options are stepped past by the rule table, and the ceiling sentence
  names an option missing from the table. `agent-cap.js`'s rule 6 block (`:39-41`) and the README's
  rule 6 section (`:196`) say the index is read at the checkout root of the payload cwd, else of
  `CLAUDE_PROJECT_DIR`. The `agent-cap.test.sh` comment at `:2220`, which names an AC6 arm that does
  not exist, is reworded to name the renderer-against-hook arm `TOOL-aOrientedCast-15` adds to the
  roles adopter's self-test. NOT OBSERVED by a criterion: prose, read by the review against §4.

## 3. Non-goals (OUT)

- No change to G1, G2 or G3, to the allowlist, or to the index's shape.
- No change to `checkRouted` or `renderRouteContext`, which keep reading `CLAUDE_PROJECT_DIR` first.
- No parse of a shell's option grammar beyond the table: an option the table does not name that
  takes an argument is part of the ceiling, said in the header.
- No edit of the roles kit. The renderer-against-hook arm is `TOOL-aOrientedCast-15`'s, in the roles
  adopter's self-test, so this unit's write set and that unit's do not meet.
- No kit-version bump for hooks; it moves once at the close.

**What it is built on.** This unit extends `TOOL-aOrientedCast-11`'s `scanCommandHeads`,
`checkRoleGate` and its evaluation order, and widens the anchor of `TOOL-aOrientedCast-7`'s rule 6
and its arming from `.claude/roles.json`. Both specs are CLOSED and declare no edge to this unit, and
a one-sided edge reds the hygiene gate's join, so the dependency is stated here rather than as an
edge.

**It shares one reword with `TOOL-aOrientedCast-15`, and no output.** The reworded `agent-cap.test.sh`
comment names arm 6 of the roles adopter's self-test by the label `TOOL-aOrientedCast-15`'s §4 "The
agreement arm" already fixes, so this unit reads a ratified spec and needs nothing that unit builds.
That arm in turn pipes a payload carrying the fixture's `cwd` to rule 6 under
`env -u CLAUDE_PROJECT_DIR`, which reads the same root before and after this unit's anchor, so it
needs nothing this unit builds either. Neither consumes the other's output, so no edge joins them.

### Edges

none

## 4. Design

### The rule table

| Rule | Applies to | Takes the next word | Ends the simple command | Next word is a body |
|---|---|---|---|---|
| shell | `bash`, `sh` | `-o`, `+o`, `-O`, `+O`, `--rcfile`, `--init-file` | a single-dash cluster holding `n` | a single-dash cluster holding `c`, tested after `n` |
| python | `python`, `python3`, `python3.<n>`, `py` | `-W`, `-X`, `-Q` | a single-dash cluster ending `c` or `m` | none |
| node | `node` | `-r`, `--require`, `--import` | `-e`, `--eval`, `-p`, `--print` | none |
| env | `env` | `-u`, `--unset`, `-C`, `--chdir` | none | `-S`, `--split-string` |
| nice | `nice` | `-n`, `--adjustment` | none | none |
| exec | `exec` | `-a` | none | none |
| command | `command` | none | `-v`, `-V` | none |

Any other option word of a rule is stepped past alone. `nohup`, `export` and `time` keep their place
in `GATE_PREFIX_WORDS` and take the empty rule. `timeout` keeps its own reading at `:1255-1260`. A
cluster is `^-[A-Za-z]+$`, so `--norc` is an ordinary option and not a cluster holding `n`. The
shell's `n` test runs before its `c` test, because `bash -nc '<x>'` checks the syntax of `<x>` and
runs nothing. Each body is scanned only at depth 0, the bound `-c` has today.

### The walk

```
scanCommandHeads, per simple command:
  loop: skip NAME=value words
        a prefix word  → k = scanLauncherOptions(a, k + 1, its rule); k < 0 → the command ends
        timeout        → as today
        else stop
  a launcher           → k = scanLauncherOptions(a, k + 1, its family's rule); k < 0 → the command ends
                         k past the end → the command ends; else launched = true
  push { text, head: a[k], argv: a.slice(k), launched }
```

The cases the review probed, and what each now reads:

| Command | Before | After |
|---|---|---|
| `bash -o pipefail tools/run-gates/run-gates.sh` | head `pipefail`, admitted | head the runner, G2 |
| `bash -e -x tools/hooks/agent-cap.test.sh` | head `-x`, admitted | head the suite, G3 |
| `bash -e -c 'bash tools/run-gates/run-gates.sh'` | head `-c`, body unread | the body scanned, G2 |
| `python -X utf8 tools/govkit/selftest.py` | head `utf8`, admitted | head the suite, G3 |
| `env -u FOO bash tools/run-gates/run-gates.sh` | head `-u`, admitted | head the runner, G2 |
| `bash -n tools/hooks/agent-cap.test.sh` | ends, admitted | ends, admitted |

### The anchor

```
resolveRoleRoot(cwd, env):
  for start in [cwd, env.CLAUDE_PROJECT_DIR]:
    a non-empty string → resolveToplevel(path.resolve(buildNativePath(start))) → its toplevel, if any
  → null
```

The payload cwd is read first because the command or spawn runs there: a role agent working in a
scratch clone reads the clone's own index, and a cwd in any checkout decides exactly as today, so
`TOOL-aOrientedCast-7` S2 and `TOOL-aOrientedCast-11`'s step 3 stay true wherever they were true.
`CLAUDE_PROJECT_DIR` is read only when the cwd lies in no checkout, which is the case M3 found. The
fork is §8 F1. The witness prints only when `CLAUDE_PROJECT_DIR` is set, because a session that names
no project directory has claimed no governed repository to report against; §8 F2.

Rule 6 then resolves a relative `scriptPath` and the marker's `path` exactly as today: the scriptPath
against the payload cwd, taken relative to the root. From a cwd outside the root a relative
`scriptPath` names no harness and is refused, which is fail-closed and named in the refusal.

### Inventory

| Name | Kind | Cell |
|---|---|---|
| `scanLauncherOptions` | function | `js.function`, `scan` |
| `resolveRoleRoot` | function, exported | `js.function`, `resolve` |
| `GATE_OPTION_RULES` | constant | none graded |

Both function names were asked of `lexicon.py --suggest` on 2026-10-12 and returned OK. Gov's map
symbol index is regenerated in the same commit, since both are new symbols.

### Files touched (estimate)

`tools/hooks/scratch-guard.js`
`tools/hooks/agent-cap.js`
`tools/hooks/scratch-guard.test.sh`
`tools/hooks/agent-cap.test.sh`
`tools/hooks/README.md`
`memory/map/generated/symbols.json`

### Alternatives rejected

- A loop with no table, stepping every `-` word alone: `bash -o pipefail` keeps `pipefail` as the
  head, which is the defect.
- `CLAUDE_PROJECT_DIR` first, as `checkRouted` reads it: §8 F1.

## 5. Production-readiness checklist

- security — The hooks stay routing guards and the push-boundary bar stays the guarantee. The walk
  refuses more and admits nothing new: every case that was admitted and is now refused is a gate run.
- perf / scale — A table lookup per option word; one more toplevel walk only when the cwd lies in no
  checkout.
- error / empty / loading states — A command that ends in an option admits, as a command with no
  head does today; neither start resolving adds no rule; a throw keeps refusing a role agent.
- observability — The new witness names both starts when a session that names a project directory
  arms neither role arm.
- risks — A table entry that takes an argument it should not hides a head. The near-miss arms pin
  `bash -n`, `command -v`, `python -c` and `node -e`.
- testing — The arms of §7, observed RED-first at the close; the direct payload probes of §6 in the
  pass.
- migration — None. The anchor changes no verdict for a cwd inside a checkout.
- user docs — The hooks README's two sections and the two file headers.

## 6. Acceptance criteria

No criterion runs a gate leg or a suite; each pipes a payload into a hook. The suite arms are under
`New arm:` in §7. The payloads use a scratch repository under a short `%TEMP%` root holding a role
index with `gates` and a manifest, built in the pass, as `TOOL-aOrientedCast-11`'s AC3 built one.

- **AC1** — When `node tools/hooks/scratch-guard.js` reads a `gov-builder` Bash payload for each of
  `bash -o pipefail <runner>`, `bash -O extglob <runner>`, `bash -e -x <suite>`,
  `bash -e -c '<runner>'`, `python -X utf8 <selftest.py>`, `env -u FOO bash <runner>`,
  `exec bash <runner>`, `nice -n 10 bash <runner>` and `node -r <preload.js> <script> --selftest`,
  each exits 2 naming G2 or G3.
  Red when: the walk stops at an option's argument, a second option, a `-c` body or a prefix word's
  option, which is the base hook's reading of every line.
- **AC2** — When the same hook reads `bash -n <suite>`, `bash -e -n <suite>`, `command -v <runner>`,
  `python -c "print(1)" <selftest.py>` and `node -e "1" <script> --selftest` for `gov-builder`, each
  exits 0 with empty stderr.
  Red when: the walk reads a syntax check, a lookup or an inline program as a run.
- **AC3** — When `node tools/hooks/scratch-guard.js` reads a `gov-builder` payload for
  `bash <runner>` with its cwd in a directory under no checkout: with `CLAUDE_PROJECT_DIR` naming the
  scratch repository it exits 2 naming G2; with `CLAUDE_PROJECT_DIR` unset it exits 0 with empty
  stderr; with `CLAUDE_PROJECT_DIR` naming another directory under no checkout it exits 0 with one
  stderr line carrying `role-gate unarmed`.
  Red when: the arm ignores `CLAUDE_PROJECT_DIR`, reads it when the cwd lies in a checkout, or says
  nothing when neither start resolves.
- **AC4** — When `node tools/hooks/agent-cap.js` reads an `Agent` payload of `subagent_type`
  `Explore` with its cwd under no checkout and `CLAUDE_PROJECT_DIR` naming a scratch repository whose
  index is armed, it exits 2 naming the type refusal; with the cwd in a second checkout that holds no
  index and the same `CLAUDE_PROJECT_DIR`, it exits 0 with empty stderr; with both under no
  checkout it exits 0 with one stderr line carrying `rule 6 unarmed`.
  Red when: rule 6 ignores `CLAUDE_PROJECT_DIR`, overrides a cwd that lies in a checkout, or says
  nothing.
- **AC5** — When `grep -c 'unset CLAUDE_PROJECT_DIR' tools/hooks/agent-cap.test.sh` and
  `grep -c 'env -u CLAUDE_PROJECT_DIR' tools/hooks/scratch-guard.test.sh` run, the first prints at
  least 1 and the second prints at least one more than at the base.
  Red when: a suite run from inside a session lets the session's directory arm a role arm over a
  fixture whose cwd lies in no checkout.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 · nine refused and five admitted `run_role_bash` rows, against a walk restored to one option per launcher with no prefix-word options · `FLOOR_ASSERTIONS` raised by the rows added
New arm: tools/hooks/scratch-guard.test.sh · covers AC3 · three rows with a cwd under no checkout, against a `checkRoleGate` that reads the payload cwd alone · `FLOOR_ASSERTIONS` raised by the rows added
New arm: tools/hooks/agent-cap.test.sh · covers AC4 · three `run_spawn` rows with a cwd under no checkout or in an index-less checkout, against a rule 6 that reads the payload cwd alone · none, the suite pins no floor

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

- **F1 — Which start does a role arm read first: the payload cwd, or `CLAUDE_PROJECT_DIR`?**
  The spec brief's table says `CLAUDE_PROJECT_DIR` first, as `checkRouted` reads it. The review
  records that fix as the finder's and the skeptic's verdict on it as unsound, and the brief's own
  rule is that the skeptic's correction is the starting point: the cwd first, then
  `CLAUDE_PROJECT_DIR` when the cwd lies in no checkout.
  Options: (a) `CLAUDE_PROJECT_DIR` first; (b) the cwd first, then `CLAUDE_PROJECT_DIR`.
  (a) moves every verdict whose cwd lies in a checkout other than the session's, so a role agent in a
  scratch clone is graded against the session's index and its paths against the wrong toplevel, and
  every suite arm whose fixture cwd sits under the caller's session directory changes meaning.
  (b) closes M3's case, keeps `TOOL-aOrientedCast-7` S2 and `TOOL-aOrientedCast-11` step 3 true
  where they held, and leaves every existing arm's verdict where it is.
  Recommendation: (b), the most criteria kept and the fewest follow-ups.
  RESOLVED (agent, 2026-10-12, delegated): (b), as §4 "The anchor" states it.
- **F2 — When does the unarmed witness print?**
  Options: (a) whenever neither start resolves; (b) only when `CLAUDE_PROJECT_DIR` is set.
  (a) prints on every spawn of a session outside any repository, and on every early `agent-cap`
  suite arm whose payload carries no cwd. (b) prints exactly where a session has named a project
  directory and the arm still found none, which is the silent state M3 describes; Claude Code sets
  the variable for every hook it runs.
  RESOLVED (agent, 2026-10-12, delegated): (b).
- **F3 — Does the status header carry `closes M2 M3`, as the spec brief asks?**
  `backlog.read_header_verbs` expands a `closes` value through the generator's id grammar, and
  neither is an id: a probe of `_read_backlog_verbs` on such a header raised "is not an id or an id
  range", which refuses every render of the build index. The build keeps no `BACKLOG.md`.
  Options: (a) write the verb; (b) name the review items in §1 and leave the verb out.
  RESOLVED (agent, 2026-10-12, delegated): (b). Option (a) fails the build-index leg, M3 veto 1.

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft.
- rev-2 · 2026-10-12 · AC1's preload payload is spelled `<preload.js>`, a placeholder like its
  siblings, because `./p.js` read to the spec-tokens paths join as an untracked path and redded
  `--dispatch` check 49 for every pass.
- rev-3 · 2026-10-12 · §3. The `consumes-from` edges to the CLOSED `TOOL-aOrientedCast-11` and
  `TOOL-aOrientedCast-7` had no `hands-off` at their sources and redded check 12's join; they move to
  a "What it is built on" paragraph. The edge from `TOOL-aOrientedCast-15`, sequenced after this
  unit, is dropped: the comment takes a label that unit's spec already fixes, and neither unit needs
  the other's built output, so the shared reword is prose. Edges reads `none`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "skip launcher options before the command head"` ranked
name-token neighbours, `before`, `skip` and `head_sha`, none of which reads a shell command. No new
seam fits beside the ones this unit extends, found by reading: `scanCommandHeads`,
`GATE_LAUNCHERS`, `GATE_PREFIX_WORDS`, `resolveToplevel`, `buildNativePath` and `checkRoleGate` in
`tools/hooks/scratch-guard.js`, and rule 6 in `tools/hooks/agent-cap.js`, which already requires
the sibling for `loadRoleIndex`. The anchor order copies `checkRouted`'s start resolution
(`scratch-guard.js:1131-1133`) and reverses its precedence for the reason §8 F1 records. The recall
probe surfaced only this build's review and brief.

Recall terms used: `scanCommandHeads launcher option head checkRoleGate CLAUDE_PROJECT_DIR payload cwd checkout root rule 6 ceiling`
