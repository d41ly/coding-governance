# `<prefix>/workflows/` — the review harness and the gates over it

Three gates in this directory read the tree and delegate their verdict to the agent-cap hook:

| gate | what it judges |
|---|---|
| `check-review-join.sh` | no ref-keyed verdict join, and every agent wave a source scan can see is counted |
| `check-verifier-fanout.sh` | the committed harnesses obey the verify-stage cap |
| `check-workflow-syntax.js` | every workflow script parses, and a second pass reds a pathless `git commit` on any code line, `git -C` included, printing how many lines it graded; a zero beside the build harness render is a dead probe |

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

**Edit the template, never the render.** The build harness names install paths: the driver,
the bug-class checklist, the build-index generator `gen_build_index.py` its spec commit runs, the
review sub-workflow it awaits and the child it hands the caller. A
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

1. `agent-cap.js` in `$HERE/hooks/`
2. `agent-cap.js` in `$HERE/../hooks/` — gov and adopter nc both resolve here
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
bash <prefix>/workflows/check-review-join.sh              # the whole population
bash <prefix>/workflows/check-review-join.sh --explain    # plus the resolved predicate and population
bash <prefix>/workflows/check-verifier-fanout.sh
node <prefix>/workflows/check-workflow-syntax.js
```

Each also accepts explicit files, which is how the suites drive their fixtures. The `--explain`
output is where the resolved predicate path is reported: the default run's bytes are pinned by an
acceptance criterion, so diagnostics that would change them live behind the flag.

## `tier2-review.js` — the five diff lenses, and `lensNotes`

A diff review fans out over five finder lenses, in this order: `security`, `correctness`, `seams`,
`verification` and `intent`. Since 1.17 `verification` asks whether every changed behaviour has a
check that can fail, and `intent` whether the diff does what its commit messages and specs say; the
old `regressions` lens is retired. A spec audit runs five lenses of its own, in this order:
`coherence`, `grounding`, `reuse`, `blast-radius` and `failure-envelope` (TOOL-aEvidencedLens-1).
`SPEC_LENSES` in the harness is that catalogue's one source; the method and the memory-tree README
point at it. Five is also the most the agent-cap hook admits on that receiver, so neither set can
grow a sixth.

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
must be a non-empty repo-relative path: no backslash, no leading `/` or `~`, no drive letter, no `..`
segment and no character below 0x20, or the run refuses before any agent spawns. The harness cannot check that a listed document
exists; the lens that reads it reports a missing one. A run given neither `specs` nor `context` logs a
`WARNING:`, and every report's RUN INTEGRITY block says where intent came from. `specs` joins the
review key, like `lensNotes`.

`checklist` carries the project's recurring bug classes. The harness produces none; this repository
passes the stdout of the memory-tree kit's `gotchas.py --for-diff <range>`, from wherever that kit
is installed:

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
RUN INTEGRITY says no class was swept; a string of `# ` header lines alone is itemless, not a refusal.
The parsed checklist joins the review key.

The string form may end with the checker's by-design block, `# by design — <n> invariant(s) this
selection touches` and one `- ` line per invariant the change touches. It is CUT OUT before the items
are parsed, so no lens sweeps intended behaviour as a bug class, and it becomes `byDesign` under the
label `Intended behaviour — invariants this change touches:`, after a caller's own `byDesign` under
`Known and tracked — do not re-report:`. Neither replaces the other. A head whose count disagrees with
its entry lines refuses before any agent spawns. Each source is logged as a `by-design:` line, and
RUN INTEGRITY's `By design:` clause names the same sources. The array form carries no block. The
checker reads that block at the range's base, so an invariant the diff adds, edits or takes out never
reaches `byDesign`: it arrives as an ordinary `- [ ] NEW/CHANGED invariant <name>` item, swept by one
lens like any class, and the checker's header line naming the base is preamble. This suite's
by-design range arm runs the real checker over a fixture range and holds that end to end.

The memory-tree kit's `gotchas.py` prints that head, and every template the checker's
`EVALUATED_TEMPLATES` names spells it: this harness's `BY_DESIGN_HEAD` pattern finds it, and the build
harness carries a second pattern and the `BY_DESIGN_FORMAT` its merged checklist is emitted from.
`check_by_design_parity.py` holds them all. It renders the head through the catalogue's own
`render_by_design`, runs each template's pattern over it in `node`, renders the format at the same
counts, and reds when a pattern stops matching, stops capturing the count, or matches the head behind
a leading space, or when the format renders any other head. It does not trust that list: it scans
its own directory and the memory-tree kit for every file carrying the head's fixed tail and reds on
one outside the evaluated set, so the population is derived rather than stated. The parity leg runs
it in check mode over the memory-tree kit it resolved, so a head reworded in one place reds the bar
rather than leaving a harness logging `none supplied`. A catalogue that predates the block skips out
loud, and `--selftest` covers every outcome.

`unattended-build.js` hands its spec audit a checklist the same way: the subject resolver runs
`gotchas.py --for-paths` over the paths the specs' `### Files touched` sub-heads name and returns its
stdout, which the stage forwards as `checklist`; a caller's `checklist` argument wins, and none at
all logs a `WARNING:`. A `base` of 7-40 hex is forwarded as `--for-paths --base <sha>`, so the
checker reads the by-design block at the run's pinned base and lists every invariant this build
moved as a `NEW/CHANGED invariant` item; the `checklist from` line names that base. With no such
`base`, the stage that takes the resolver's checklist logs a `WARNING:` that the block was read from
the working tree.

Its SPEC stage ends in ONE commit (TOOL-aGraftedHelix-15): when the writers authored a unit and the
caller pinned no `subjects`, one agent commits the authored specs with `Pass: none` and the program
writes each committed path onto its unit, so the audit pins them at `HEAD` in the same call. That
commit's checklist items are merged into the audit's with its by-design block left out
(TOOL-aGraftedHelix-35), so the audit's block is the first input's alone, less any ruling either input
itemises as a `NEW/CHANGED invariant`; with the audit off the checklist rides the hand-out whole as
`specCommit`. With a 7-40 hex `base` the commit stage runs `gotchas.py --for-paths --base <sha>` over
the paths its commit wrote, so that block is read at the run's pinned base; with none it runs
`--for-diff HEAD~1..HEAD`, read at the spec commit's parent, and the audit-OFF route logs a `WARNING:`
saying so. Each writer's `authored` entry is resolved to its roster
unit before that commit, whether it is spelled as an id, a repo-relative path or an absolute one
(TOOL-aGraftedHelix-33): an entry that names no roster unit by id and no unit's spec by path refuses
the run, and a unit placed by path whose committed spec, found by its H1, is another file refuses
after the commit. Every refusal that asks for a commit names a fresh
re-invoke, never a `resumeFromRunId` resume, because a resume replays the cached answer that refused.

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
it as `lens=<key>`. Every return carries five fields beside the counts:

- `shape` — one record line, also logged, in this fixed grammar:
  `review-shape kind=<diff-review|spec-audit> round=<n> intensity=<full|light> at=<find|verify|synth> raw=<n|-> confirmed=<n|-> refuted=<n|-> unverified=<n|-> blocker=<n|-> high=<n|-> medium=<n|-> low=<n|-> agents=<n> out-tokens=<n|unknown>`.
  `at` is the stage the exit reached; a count that stage has not produced is `-`, never `0`, and the
  every-lens-dead exit prints `raw=-`. The four severities count RAW confirmed findings by binding
  grade, not the synthesis's adjudicated items, which stay in `blockers` and `highs`. `agents` is the
  final return's formula through the stage reached. `out-tokens` is a `budget.spent()` DELTA from just
  before the first agent: the counter is a pool shared by the main loop and every workflow in the
  turn, so spend elsewhere during the run inflates it, and `unknown` means no `budget` was readable.
  The `at=synth` line is rendered before the synthesis agent runs, so its out-tokens EXCLUDE the
  synthesis agent's own spend. The synthesis is told to copy it verbatim, alone on its line,
  immediately above the appendix heading, and the final return carries the same string, so the
  record's copy can be compared to it.

- `ledger` — one entry per finding in id order: `id`, `lens`, `ref`, `severity` (the finder's),
  `skepticSeverity`, `verdict` (`confirmed`, `refuted`, `uncertain`, or `unverified` when no verdict
  stands), `reason`, `fixVerdict`, `claim` and `classes`. An absent optional value is `null`.
  `classes` lists the checklist classes the claim's leading `C<n>` labels denote, by each item's
  slug, in order and without duplicates; a label with no slug to resolve, its item absent or not
  slug-led, is kept as `C<n>`. It is `[]` when the claim opens with no label or the run had no
  checklist.
- `confirmedFindings` — one entry per confirmed finding: `id`, `lens`, `ref`, `claim`, `severity` (the
  binding grade), `fix` and `fixVerdict`. A fix the skeptic judged unsound is replaced by its note
  when it gave one. Pass this array as the next round's `priorFindings` rather than re-typing it.
- `appendix` — the ledger as a markdown table under `## Appendix — every finding`, with the nine
  columns `id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes`. The
  ninth joins the `classes` names with one space, so a class's hits can be counted across records. A
  cell is `-` when its value is absent or empty, a `|` is escaped, and line breaks fold to a space.
- `lensYield` — per lens, `defects` and `unique` are `null` when no item list can be trusted (see below).
  One row per lens that RAN, in dispatch order, none for a lens a light run skipped:
  `lens`, `returned` (false for a lens that died), `raw`, `confirmed`, `refuted`, `uncertain`,
  `unverified` (every finding neither confirmed nor refuted, the uncertain ones included), `precision`
  (`confirmed / (confirmed + refuted)`, `null` when both are 0), `defects` (synthesis items holding a
  confirmed id from this lens) and `unique` (items whose every confirmed id is this lens's). The item
  list is untrusted, and both are `null` on every row, when no synthesis ran, it died,
  or the tally fault fired. Each row is logged as a `lens yield:` line, and the counts known before
  the synthesis reach its prompt as a verbatim block the report copies; the return is the source of
  record, because that copy is not checked.

The two exits before any skeptic runs, every lens dead and no finding raised, return `[]`, `[]` and
`''` as the ledger, the confirmed set and the appendix; a deferred return carries what was judged so far. The harness renders the appendix and tells the
synthesis to copy it verbatim as the report's last section. That copy is the only way a REFUTED finding
reaches a record, and the harness cannot check it was made: compare the report against the returned
`appendix`. A run whose every finding is refuted writes no report, so there the appendix exists in the
return alone, and the caller writes it down if it wants one.

## `workerType` — judges spawned as a named agent type, in all three harnesses

Every agent a harness spawns loads the charter through `CLAUDE.md` before its task. A judge reads a
brief the harness wrote and lands nothing, so `workerType` lets a caller spawn the JUDGES as a named
agent type instead. In `tier2-review.js` an absent `workerType` reads as `Plan`, the default one
measured A/B pair set (TOOL-aMendedFleet-93's reading): its read-only judges matched the charter-loaded
arm's precision at about half the first-turn context. The reserved literal `none` spawns every judge as
before that default, durability instructions and review key included. In the two drift harnesses an
absent `workerType` still spawns every agent as the platform default, because no pair measured them.

```js
// tier2-review.js: every finder and every skeptic batch spawns as the type
args: { repo, base, head, reviewDir, workerType: 'Plan' }
// drift-audit-code.js and drift-audit-state.js: the skeptic batches only
args: { repo, base, outDir, workerType: 'Plan' }
```

The value must match `^[A-Za-z][A-Za-z0-9_-]{0,63}$`, or the harness refuses before any agent spawns
with a message naming `workerType`. A well-formed name the platform does not know comes back as its
named `not found` refusal, which each harness already counts as a dead agent. The orchestrating
agents never take the type: the tier2 resume probe reads the lens files and the synthesis writes the
report.

Under a type, a tier2 judge is told to write no `find-*.json` or `verify-*.json` and to return `path`
empty, because the read-only types hold no Write tool. One log line names the type and says the run's
lens and batch results are NOT durable, so a resume re-dispatches them; pass `workerType: 'none'` when
a run must resume. `workerType` joins the review key only when it names a type, so a `none` run keys as
every run before the default did, and a run under a type is never answered from a `none` run's lens files.

The drift FINDERS keep the default type. Each writes its prose writeup under `outDir`, `wave1-<lens>.md`
from the code harness and `wave2-<lens>.md` from the state harness, as it works, and that file is both its deliverable and the harness's durability control, after a
two-hour finder once died with nothing on disk; a type with no Write tool can hold neither.

Which types omit the charter — verified 2026-10-04, node a, Claude Code 2.1.178, by a read-only
`grep -a -o` over the installed binary for `omitClaudeMd`:

- Only the built-in `Explore` (model `haiku`) and `Plan` (model `inherit`) set it. Both disallow the
  file-editing tools and carry a read-only prompt. `Explore` also changes the model, so an A/B over
  it measures two effects at once; `Plan` changes only the context.
- A project agent definition cannot ask for it: the CLI's list of known definition front-matter keys
  does not carry the field, so a custom type buys a tool restriction and none of the saving.
- UNVERIFIED: whether a custom definition added mid-session is spawnable without restarting the
  session. Name a built-in type unless that has been measured.

## `review_replay.py` — a review scored for recall against a past round

Stdlib Python, run under the repo's python launcher. It answers one question nothing else here can:
does a lens set or a prompt change find MORE of what a previous review proved real? Three modes:

- `python3 {kit}/review_replay.py --known <record> --candidate <report> [--window N]` — the score.
  The known set is a past diff-review or spec-audit record's confirmed findings; for a diff-review
  record it is in one of two UNITS, and the
  `replay: known` line prints which. From its `## Appendix — every finding`, when it has one, the
  unit is `raw-finding`: one entry per confirmed appendix row, so a defect two lenses confirmed
  counts twice. Otherwise it is `adjudicated-item`, read from the legacy item table (a row whose
  second cell is a severity and whose last cell lists raw finding ids; the location is the row's
  first backticked `file:line`). Recall from the two record eras is therefore in different units.
  The candidate is the appendix of a report the harness wrote; only `confirmed` rows count, columns
  are found by header name. A known item is MATCHED when a candidate sits in the same file within
  `--window` lines (default 10); a drive-lettered ref such as `C:/repo/a.sh:12` keeps its path after
  the drive, so it matches a repo-relative one. It prints MATCHED, MISSED, UNSCORABLE and
  CANDIDATE-ONLY lines, a per-lens line, and `replay: recall k/m`, and exits 0 at any recall. When
  the known set came from an appendix, a `per-lens known:` line follows, giving each known-side lens
  its confirmed count and how many a candidate matched.
  **Spec mode** is chosen when the known record's first non-blank line is the `**Serves:** spec-audit`
  binding. The known set is read from its appendix ONLY: with none it is refused `no-appendix`, never
  scored as zero and never read through the legacy table. A spec ref is `<file>:<where>`, and the
  section rule reads the first `§<n>` or `section <n>` in the address, else the first `S<n>`, `AC<n>`
  or `F<n>` as §2, §6 or §8; an address naming none (`status header`) is UNSCORABLE. A match is the
  same file and the same SECTION: the window is forced to 0, `--window` is ignored, and the
  candidate line prints `address section`. The `replay: known` line carries `kind spec-audit` and the
  subject pins written after the binding line, or `subjects none-stated`; no range is required. A
  candidate opening with the other kind's `**Serves:**` binding is refused `kind-mismatch`, naming
  both kinds, in either direction; an unbound candidate is read in the known record's mode. Spec
  records are not listed by `--corpus`: name the known record directly.
- `python3 {kit}/review_replay.py --corpus <dir> [<dir> ...] [--repo <clone>]` — which past records
  are replayable: each record whose first line is the `**Serves:** diff-review` binding, that passes
  the liveness check below and whose range resolves in this clone, with its round, range and scorable
  count. The summary line puts every scanned record in exactly one bucket. Ranges resolve through
  ONE `git cat-file --batch-check` for the whole corpus.
- `python3 {kit}/review_replay.py --selftest` — named arms over inline fixtures, no file
  or git access; red when an arm fails or fewer arms ran than its `ARMS_DECLARED` states. It is the held leg
  `review-replay selftest`.

**Liveness, the reason a score can be trusted at all.** Both inputs must reproduce their own stated
confirmed count from what was extracted, or they are REFUSED with exit 2 naming both numbers — for a
legacy table, the union of the raw ids across its item rows. Most legacy records are free prose and
are refused; a refused record is never scored, which keeps a silent partial extraction out of every
score. A record with no scorable item, no stated count or no hex range is refused the same way. The
candidate side prints how many of its confirmed rows carry no readable `file:line`, and is refused
when it has confirmed rows and none is readable, so a drifted ref shape cannot read as a recall of
zero. An appendix row ends at a newline only, never at another character Python's `splitlines`
breaks on, so a U+2028 inside a cell cannot drop the rows after it.

**The live replay**, run at the main loop because only it holds `Workflow`:

1. List: `python3 {kit}/review_replay.py --corpus memory/builds`, then pick a `round 1` row.
2. `git worktree add --detach <dir> <head>` in a short directory under `%TEMP%`, never inside the
   worktree.
3. Run `Workflow` with this kit's `tier2-review.js`, `repo` set to that checkout, the record's base
   and head, round 1, no `priorFindings`, and a `reviewDir` inside the checkout.
4. Score: `python3 {kit}/review_replay.py --known <record> --candidate <the report it wrote>`.
5. Write the recall, matched, missed and per-lens lines to the acceptance ledger, then
   `git worktree remove` the checkout.

**What the score does NOT mean.** Recall is measured against what ONE past review confirmed, not
against every defect in the range. A candidate-only finding may be a real defect that review missed,
so it is listed and never counted as a false positive: there is no precision figure. Two files
sharing a basename can match, because older records carry basename-only refs. And one replay is one
sample of a stochastic fan — compare two harness versions by two scored runs side by side, never by
one.

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
