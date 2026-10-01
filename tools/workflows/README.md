# `tools/workflows/` — the review harness and the gates over it

Three gates in this directory read the tree and delegate their verdict to the agent-cap hook:

| gate | what it judges |
|---|---|
| `check-review-join.sh` | no ref-keyed verdict join, and every agent wave a source scan can see is counted |
| `check-verifier-fanout.sh` | the committed harnesses obey the verify-stage cap |
| `check-workflow-syntax.js` | every workflow script parses |

`tier2-review.js` is the ready-made harness they exist to protect. It carries this directory's
version under **two** kit ids, and both are paired — see its line 3 and `check-kit-versions.sh`.

## What this kit RENDERS, and its one renderer

`check-protocol-parity.test.sh --render` writes every artifact below, and the same script with no
argument is the leg that grades them:

| rendered | from | tokens |
|---|---|---|
| `<memory root>/guides/REVIEW-PROTOCOL.md` | `REVIEW-PROTOCOL.template.md` | `TOOL_ROOT` |
| `unattended-build.js`, beside its template | `unattended-build.template.js` | `KIT_DIR`, `TOOL_ROOT`, `MEMORY_TREE_DIR`, `FANOUT_CAP` |
| `tier2-review.js`, beside its template | `tier2-review.template.js` | `FANOUT_CAP` |
| `drift-audit-code.js`, beside its template | `drift-audit-code.template.js` | `FANOUT_CAP` |
| `drift-audit-state.js`, beside its template | `drift-audit-state.template.js` | `FANOUT_CAP` |

**`FANOUT_CAP` is the agent-cap hook's own declaration** (TOOL-aRepatriatedFork-7): `FANOUT_CAP=<n>` in
`.agent-cap.conf` at the checkout root, ANSWERED by the hook (`agent-cap.js --print-cap`) rather than
parsed here, so the value rendered is the value enforced and a repo that
lowers its cap receives harnesses its hook admits. No conf renders the ceiling, byte-identical to the
harnesses as they shipped before. A value the hook would refuse makes the render refuse too. The
three harnesses beside the build harness moved from `engine` to `rendered` at review-harness 1.9, and
an install from before that migrates them the way the build harness migrated at 1.8, below. A
`*.template.js` is a render source, not a harness: the verifier fan-out and syntax gates judge its
render and skip the template.

**Edit the template, never the render.** The build harness names four install paths: the driver,
the bug-class checklist, the review sub-workflow it awaits and the child it hands the caller. A
workflow script has no filesystem when it runs, so it cannot find its siblings, and apply would
write a shipped copy verbatim, naming this repo's `tools/` layout in every adopter. So the kit
renders it instead, and `kit.toml`'s `[[regenerate]]` block re-runs the render on every update run
unless `GOVKIT_RERENDER=0` is exported. With `GOVKIT_RERENDER=0` set `update` declines that block and
NAMES the decline on stdout — `DECLINED review-harness: the re-render step is OFF …` — on every `--write`,
whatever the flag says (`DEPL-cMendedVintage-1`, which made that decline decide whether a kit's
writes are rolled back; a decline that can decide that must not be invisible). It still prints the
harness row as `re-rendered` although no render ran, and where your bar wires the parity leg, that
leg reds the stale copy there.

**The regenerate refreshes an install and never creates one.** It runs `--render --tracked-only`,
which skips by name any pair whose live copy is absent and untracked, because govkit rows nothing
a regenerate writes. So an install that never took `REVIEW-PROTOCOL.md` does not receive one from
an update. To install it, run `--render` by hand and commit what it writes.

**`MEMORY_TREE_DIR` is probed, not derived.** An adopter may install the memory-tree kit flat in
its tool root, so the tool root plus `memory-tree/` is not an answer. The render takes the first
TRACKED of `{{TOOL_ROOT}}memory-tree/gotchas.py` and `{{TOOL_ROOT}}gotchas.py`. When neither is
tracked it SKIPS the harness pair out loud and still renders and grades the protocol, because this
kit requires only agent-cap and an install without the memory-tree kit is legal. If yours is
somewhere else, run the render with `MEMORY_TREE_DIR=<dir>` exported; an override naming nothing
tracked is refused. That override comes only from the environment, so a tree that needs it on its
bar exports it there too. A template in this directory with no pair in the script is a red, so a
new one cannot ship ungraded.

**An install from before 1.8 rows the harness as an engine file**, and `update` keeps that role, so
it writes gov's own render and cannot move the row. The migration that converges, verified on a
fixture, is in the coding-governance runbook's Maintenance section, under "The build harness is
rendered from review-harness 1.8".

## How the three find things — stated ONCE, for all of them

**None of these scripts spells an install prefix.** They ran with `tools/` hard-coded until
`TOOL-dRetiredFork-10`, which cost three carve-outs at one adopter and three divergence rows at
another — six hand-maintained records for a path each script can work out from where it is standing.

**The population.** Each shell gate derives the kit directory from its own location — the
predicate's probe needs it, and `check-review-join.sh` scopes its population to it:

```sh
HERE="$(cd "$(dirname "$0")" && pwd)"
KIT_PREFIX="$(cd "$HERE/.." && git rev-parse --show-prefix)"   # `tools` here, `scripts` at adopters
```

Two things about that line are load-bearing and neither is obvious.

*Git computes the relative path.* The tempting spelling — subtract `git rev-parse --show-toplevel`
from `pwd` — is broken on MSYS, where `pwd` yields `/c/projects/...` and `--show-toplevel` yields
`C:/projects/...`. The subtraction then leaves the string untouched, the population matches nothing,
and there is no error: measured at population 0 during the unit that wrote this.

*An empty prefix is a real layout.* A kit installed at the repository root has nothing to strip, and
the population is then every `*.js` the repo holds.

**The population rule, for all three gates** (TOOL-aRepatriatedFork-4):

- `check-workflow-syntax.js` and `check-verifier-fanout.sh` apply NO prefix filter. Each applies a
  `meta`-declaration marker to every `*.js` git lists, so the population is *a file declaring
  workflow meta* wherever it lives — including `.claude/workflows/`, where both adopters keep their
  harnesses and where a prefix filter judged none of them.
- `check-review-join.sh` applies no marker filter, so dropping its prefix would widen it into files
  whose own ban tables trip the predicate — measured, and it reds the bar. It keeps the derived prefix
  and ADDS `.claude/workflows/` as a literal, the harness's own convention. `.claude/hooks/` stays out.

**The predicate.** Three rungs, tried in order, then a refusal:

1. `$HERE/hooks/agent-cap.js`
2. `$HERE/../hooks/agent-cap.js` — gov and adopter nc both resolve here
3. `$ROOT/.claude/hooks/agent-cap.js` — adopter ic has no sibling `hooks/` at all, and this is its only copy

The third rung is not a fallback for tidiness; a two-rung chain strands a real adopter, which was
found by testing the derivation against both trees rather than by reasoning about one. A gate that
resolves none of the three **refuses and names what it tried** — it does not pass quietly, which is
the whole point of a gate whose verdict comes from somewhere else.

`.claude/hooks/` in rung 3 is a literal, and it is the one place these scripts do not practise what
they enforce. It is the harness's own convention rather than a prefix an adopter picks, so it stays;
said here rather than left for a reader to find.

## Running them

```bash
bash tools/workflows/check-review-join.sh              # the whole population
bash tools/workflows/check-review-join.sh --explain    # plus the resolved predicate and population
bash tools/workflows/check-verifier-fanout.sh
node tools/workflows/check-workflow-syntax.js
```

Each also accepts explicit files, which is how the suites drive their fixtures. The `--explain`
output is where the resolved predicate path is reported: the default run's bytes are pinned by an
acceptance criterion, so diagnostics that would change them live behind the flag.

## `tier2-review.js` — the five diff lenses, and `lensNotes`

A diff review fans out over five finder lenses, in this order: `security`, `correctness`, `seams`,
`verification` and `intent`. Since 1.17 `verification` asks whether every changed behaviour has a
check that can fail, and `intent` whether the diff does what its commit messages and specs say; the
old `regressions` lens is retired. A spec audit keeps its four lenses. Five is also the most the
agent-cap hook admits on that receiver, so the set cannot grow a sixth.

`lensNotes` appends a project addendum to one lens's brief, and to no other prompt:

```js
args: { repo, base, head, reviewDir,
        lensNotes: { security: 'shell is built from conf values; treat .unattended.conf as input' } }
```

Its keys are the lens keys of the run's own kind. A key naming no such lens, a non-object, or an
empty note refuses before any agent spawns, with the legal keys in the message. Absent, it is
announced: a `WARNING:` log line, and a clause in the report's RUN INTEGRITY block. The notes and a
review-shape literal both join the review key, so a lens file written by older prompts or under
other notes is never reused. An adopter test that counted four diff lenses sees five from 1.17.

`specs` names the documents that say what the change was for, so the lenses review against intent
rather than against the code alone:

```js
args: { repo, base, head, reviewDir,
        specs: ['memory/builds/<slug>/spec/<date>-spec-<unit>.md'] }
```

Every finder and skeptic prompt then opens with an `INTENT` block that lists them, and, on a diff
review, always names the range's commit log, `git log --format=%B <base>..<head>` over the resolved
shas. With no `specs` that log is the statement of intent. On a spec audit `specs` is sibling context
the subjects must agree with, never reported against, and naming a subject there refuses. Each member
must be a non-empty repo-relative path: no backslash, no leading `/`, no drive letter and no `..`
segment, or the run refuses before any agent spawns. The harness cannot check that a listed document
exists; the lens that reads it reports a missing one. A run given neither `specs` nor `context` logs a
`WARNING:`, and every report's RUN INTEGRITY block says where intent came from. `specs` joins the
review key, like `lensNotes`.

`checklist` carries the project's recurring bug classes. The harness produces none; this repository
passes the stdout of `python tools/memory-tree/gotchas.py --for-diff <range>`:

```js
args: { repo, base, head, reviewDir,
        checklist: '# preamble\n- [ ] class-one\n    what it is\n- [ ] class-two' }
// or, already split:  checklist: ['class-one: what it is', 'class-two']
```

As a string, lines before the first line starting `- ` are a preamble, each `- ` line opens an item,
and the lines after it continue that item; CRLF reads as LF. A non-blank string with no `- ` line
refuses rather than becoming one item, and so does any value that is neither a string nor an array of
non-empty strings. The items are split ROUND-ROBIN over the lenses of the run's kind: item `n` goes to
lens `(n - 1) % K` in lens order, so each class is swept by exactly one finder, labelled `C<n>`, and
a finder begins a hit's claim with that label. A lens with no share is told so; skeptics get none. The
split is logged, and RUN INTEGRITY states it. An absent or itemless checklist logs a `WARNING:` and
RUN INTEGRITY says no class was swept. The parsed checklist joins the review key.

`intensity` is `'full'` or `'light'`, and absent it is `'full'`. Only the caller picks it; the harness
never chooses light for itself, whatever the diff's size or history:

```js
args: { repo, base, head, reviewDir, intensity: 'light', checklist }
```

A light diff review runs the lenses `LIGHT_LENSES` names, `correctness`, `seams` and `verification`,
and skips `security` and `intent`. The checklist is split over the lenses that run, so a skipped lens
takes no share and no class is lost with it. A light run says what it skipped: a `WARNING:` log line
before the first finder, a RUN INTEGRITY clause telling the report not to call it a full review, and
`intensity` and `skippedLenses` on every return (`skippedLenses` is `[]` on a full run). A skipped
lens counts as neither live nor dead. A spec audit has no light subset, so `'light'` refuses there; any
value other than the two refuses on both kinds. `intensity` joins the review key. A diff that crosses a
trust boundary is not one to review light: the `security` lens is one of the two a light run skips.

Every finding carries `lens`, the key of the lens the harness dispatched, never the label the agent
echoed back, and every finding line in a skeptic prompt, the synthesis prompt and the run log names
it as `lens=<key>`. Every return carries three fields beside the counts:

- `ledger` — one entry per finding in id order: `id`, `lens`, `ref`, `severity` (the finder's),
  `skepticSeverity`, `verdict` (`confirmed`, `refuted`, `uncertain`, or `unverified` when no verdict
  stands), `reason`, `fixVerdict` and `claim`. An absent optional value is `null`.
- `confirmedFindings` — one entry per confirmed finding: `id`, `lens`, `ref`, `claim`, `severity` (the
  binding grade), `fix` and `fixVerdict`. A fix the skeptic judged unsound is replaced by its note
  when it gave one. Pass this array as the next round's `priorFindings` rather than re-typing it.
- `appendix` — the ledger as a markdown table under `## Appendix — every finding`, with the eight
  columns `id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict`. A cell is `-`
  when its value is absent, a `|` is escaped, and line breaks fold to a space.

The two exits before any skeptic runs, every lens dead and no finding raised, return `[]`, `[]` and
`''`; a deferred return carries what was judged so far. The harness renders the appendix and tells the
synthesis to copy it verbatim as the report's last section. That copy is the only way a REFUTED finding
reaches a record, and the harness cannot check it was made: compare the report against the returned
`appendix`. A run whose every finding is refuted writes no report, so there the appendix exists in the
return alone, and the caller writes it down if it wants one.

## `orient-counterfactual.js` — one stage-2 arm per call

The stage-2 `orient` subagent is deferred behind a measurement: whether moving a kickoff's
orientation out of the main context is worth a slot, a child load and the loss of the ask. The
owner widened that measurement to a matrix, and this harness runs ONE cell of it per `Workflow`
call — eight calls for the whole matrix, made by the caller in whatever order it likes:

| axis | values |
|---|---|
| `arm.agent` | `orient` (the custom definition below) · `Explore` (the built-in type) |
| `arm.recall` | `true` — the memory-recall probe runs where the engine asks · `false` — skipped |
| `arm.reuse` | `true` — the reuse-lookup probe runs where the engine asks · `false` — skipped |

```
Workflow { scriptPath: '{kit}/orient-counterfactual.js',
           args: { repo: '<abs repo path>', task: '<the task, as the owner would type it>',
                   arm: { agent: 'Explore', recall: true, reuse: true },
                   engine: '<repo-relative path of the kickoff engine text — optional>' } }
```

Each call spawns two kickoffs of the same task, strictly one after the other: the run count is the
marked literal `const RUNS = [0, 1]` iterated by the one `for (const i of RUNS)` loop the fan-out
hook admits under `gov:sequential-agents(2)`. The second run reads a warm index the first one built;
that is what "matched" means here, and the record carries both READY lines so a reader can tell
them apart. `engine` is optional and exists for an agent type that holds no Skill tool — whether
`Explore` is one is UNVERIFIED and is part of what its arm measures: given the path, such an agent
Reads the engine's text instead of invoking the Skill; without it, it reports `refused-step` naming
`Skill`.

**Installing the `orient` arm.** `orient.agent.md` is the custom agent definition — tools
Read, Grep, Glob and Bash, no Write, no Edit, no Agent, no worktree isolation. Nothing wires it.
For a run: copy it to `.claude/agents/orient.md`, make the calls, remove it. Invoked with no
definition in place, the record reads `arm unavailable: orient` and the spawn's own refusal; that is
a recorded outcome, not a failure of the harness.

**The record.** The script RETURNS it — a workflow script has no filesystem — and the caller writes
the return under `memory/builds/<slug>/build/` in the acceptance-ledger grammar. Fields: `arm` (the
three axis values), `verdict` (`measured`, `partial: n/2 runs spawned`, or `arm unavailable: <type>
— <why>`), `sequential` (true only when the second run's `startMs` is after the first's `endMs`;
null when either run has no clock), `runs` (two entries, each with a closed `outcome` — `spawned`,
`null`, `threw` or `refused-step` — a `reason`, `tokens`, `startMs`, `endMs`, `wallMs`, `ready`,
`card`, `recallRan`, `reuseRan`), and `fallback` (null, or the one re-run of a `refused-step` run
under the default workflow agent type, naming `fallbackFor`). Two notes travel in the record itself
and should travel into the written copy: `tokens` is the `budget.spent()` delta around the spawn,
which is the workflow's OUTPUT tokens while that agent ran and not the subagent's context; `wallMs`
is the agent's own `date +%s%3N` at its first and last Bash call, because a workflow script cannot
read a clock.
