# `<prefix>/workflows/` — the review harness and the gates over it

Three gates in this directory read the tree; two of them run a rule that lives beside them and reads
the agent-cap hook's views (see "The rules that left the hook" below):

| gate | what it judges |
|---|---|
| `check-review-join.sh` | no ref-keyed verdict join, through `check-review-join.js`, and every agent wave a source scan can see is counted |
| `check-verifier-fanout.sh` | the committed harnesses obey the verify-stage cap and the loop markers, through `check-verifier-fanout.js` |
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
| `tier2-review.js`, beside its template | `tier2-review.template.js` | `FANOUT_CAP`, `LENS_SLOTS` |
| `drift-audit-code.js`, beside its template | `drift-audit-code.template.js` | `FANOUT_CAP` |
| `drift-audit-state.js`, beside its template | `drift-audit-state.template.js` | `FANOUT_CAP` |

**`FANOUT_CAP` is the agent limit** (TOOL-dGroundRules-10, which re-pointed TOOL-aRepatriatedFork-7's
token from the agent-cap hook): `runtime.agents-in-flight` as the policy kit's reader answers it at
HEAD, `policy.py get runtime.agents-in-flight --rev HEAD`, a `FANOUT_CAP` lowering in `.agent-cap.conf`
included, so a policy write and the widths rendered from it land together. It carries the concurrency
widths and the build harness's `SPEC_WRITERS`, never the verify total: the review and drift-audit
templates write the agent-cap hook's `MAX_VERIFIERS` as a literal. No policy kit, a refused read, or an
answer that is not a positive integer makes the render refuse, naming why. The
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

**A harness citation resolves through the install receipt first** (`TOOL-dRenderedAnchor-6`).
govkit homes this kit by its entry id, so an adopter's directory need not carry gov's name for it,
and the tool root plus gov's home for a harness names nothing there. So before the plain
`{{TOOL_ROOT}}` substitution, the render applies each `{{TOOL_ROOT}}<home>/<file>` citation the
install HOLDS, as `derive_kit_paths` resolves it: the receipt row first, then the probe beside this
kit. Only a citation nothing holds renders as the tool root plus its home. A receipt's top-level
`prefix` is not applied, because the tool root is this kit's own parent and a second answer to it
would disagree.

**A held citation's path is checked before anything is written** (`TOOL-dRenderedAnchor-7`). The
receipt row writes it, and it lands in a JS string literal and in commands an agent runs, so a path
that is empty or holds a character outside `[A-Za-z0-9._/+@-]` is exit 2 with one line naming the
citation and its path, the same set this script refuses for the kit path. Fix the receipt row.

**`--render` derives the citations twice.** A rendered harness is held only once it is a file, and
on a fresh install this render is what writes them, so the first derivation cannot see them. After
writing, the render derives again, and when the citations moved it runs itself once more with the
same arguments, printing one line that says so, and exits with the re-run's status.
`PROTOCOL_PARITY_REPASS` bounds that to one re-run. `--tracked-only` creates only a live copy this
install already tracks: on a tree that holds every rendered harness the two derivations agree and it
does not re-run, and a tracked harness deleted from the worktree is written again, and then the run
re-runs once, like a fresh render. When the citations moved and an inherited
`PROTOCOL_PARITY_REPASS=1` suppressed the re-run, the render prints one line naming
`PROTOCOL_PARITY_REPASS` and exits 1, because a rendered copy may name a stale path; run `--render`
again with it unset.

**`MEMORY_TREE_DIR` is probed, not derived.** An adopter may install the memory-tree kit flat in
its tool root, so the tool root plus `memory-tree/` is not an answer. The render takes the first
TRACKED of `{{TOOL_ROOT}}memory-tree/gotchas.py` and `{{TOOL_ROOT}}gotchas.py`. When neither is
tracked it SKIPS the harness pair out loud and still renders and grades the protocol, because this
kit requires only agent-cap and policy, and an install without the memory-tree kit is legal. If yours is
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

## The rules that left the hook — `TOOL-dFairHearing-16`

Three of the agent-cap hook's rules are this kit's since the owner's NT-27, each seen red at its new
home before the hook stopped carrying it. The hook keeps rules 6 and 7, which judge the call, and
exports the readers these homes share with it: its views, `runBothViews`, `MAX_VERIFIERS`, the
writer bound, the args reader and the slug walk. Rule 2's lens-literal bound is `LENS_SLOTS` in
`check-verifier-fanout.js`, the same number the slot count holds every marked literal to, so it has
one home (TOOL-dFairHearing-23). Every `--only=` the hook was
given before now refuses, exit 2, naming the two script homes.

| rule | home | runs from |
|---|---|---|
| the verify-stage total and the loop markers (`gov:fixed-verifiers`, `gov:fixed-writers`, `gov:sequential-agents`) | `check-verifier-fanout.js` | `check-verifier-fanout.sh`, per harness |
| the ref-keyed verdict join ban | `check-review-join.js` | `check-review-join.sh` alone, per script |
| the spec-audit opt-in | `spec-audit-optin.js` | the `PreToolUse` wiring, on `Workflow` calls |

The two script homes are CLIs as well as modules, and take the hook as `--hook`:

```bash
node <prefix>/workflows/check-verifier-fanout.js --hook <prefix>/hooks/agent-cap.js <file>…
node <prefix>/workflows/check-review-join.js --hook <prefix>/hooks/agent-cap.js <file>…
```

Each prints a finding as the hook printed it and exits 1, exits 0 clean, and exits 2 when it cannot
load the hook's exports or read a file. A writer split's bound is read at the working directory. An
inline `script` on a `Workflow` call is no longer judged at the tool call: the harness's own
concurrency settings bound it, and the gates judge every harness that lands.

**The spec-audit opt-in pack** is a hook of its own, wired through its fragment beside it:

```bash
python <prefix>/settings-merge.py --fragment <prefix>/workflows/spec-audit-optin.fragment.json
```

A default install wires it through govkit, and `<prefix>/check-wiring.sh` grades it with the same
per-fragment loop that grades the hooks kit's fragments, reporting it UNWIRED in a tree that unwired
it. It reads `extractWorkflowArgs` and `extractBuildSlug` from the hook and `readFrontMatterKey` and
`readConfKey` from scratch-guard.js, both in the hooks kit beside this one; a copy with no hooks kit
beside it denies a call whose args may be a spec audit, naming the reader it could not load, and
admits every other. What the rule denies is stated in `<prefix>/hooks/README.md`.

## `tier2-review.js` — the five diff lenses, and `lensNotes`

A diff review fans out over five finder lenses, in this order: `security`, `correctness`, `seams`,
`verification` and `intent`. Since 1.17 `verification` asks whether every changed behaviour has a
check that can fail, and `intent` whether the diff does what its commit messages and specs say; the
old `regressions` lens is retired. A spec audit runs five lenses of its own, in this order:
`coherence`, `grounding`, `reuse`, `blast-radius` and `failure-envelope` (TOOL-aEvidencedLens-1),
or, under the `design-audit` preset (below), the five of `DESIGN_LENSES`, and under `whole-design` the five
walkers of `WHOLE_DESIGN_LENSES`. Every set has one source,
`lenses.toml`, this kit's lens catalogue (below); `DIFF_LENSES`, `SPEC_LENSES`, `DESIGN_LENSES` and `WHOLE_DESIGN_LENSES` in
the harness are its render, and the method and the memory-tree README point at the literal. The
fan-out leg holds each rendered literal to exactly five slots, and five is also the most the
agent-cap hook admits on that receiver, so no set can grow a sixth.

`lensNotes` appends a project addendum to one lens's brief, and to no other prompt:

```js
args: { repo, base, head, reviewDir,
        lensNotes: { security: 'shell is built from conf values; treat .unattended.conf as input' } }
```

Its keys are the lens keys of the run's own kind. A key naming no such lens, a non-object, or an
empty note refuses before any agent spawns, with the legal keys in the message.

A caller that runs more than one literal passes the notes per preset instead: an object whose every
key is a literal name, `diff-review`, `unit-spec` or `design-audit`, each mapping to the map above.

```js
args: { kind: 'spec-audit', subjects, scratch,
        lensNotes: { 'unit-spec': { reuse: 'the kits under tools/ are the seams' },
                     'design-audit': { 'alternatives-and-cost': 'price a new kit against tools/lib/' } } }
```

The run reads only its own literal's entry, absent meaning `{}` and announced as no notes; only that
entry is checked, and another preset's is checked when that preset runs. An object mixing literal
names with lens keys refuses, naming both forms. The flat form keeps its meaning, and the two forms of
the same notes derive one review key. After an `optIn` swap (below) the legal keys are the literal's
defaults plus the opt-ins swapped in: a note keyed to a default the swap displaced is accepted and
reported unread, in the log and in RUN INTEGRITY, as a skipped light lens's note is, and a note keyed
to the swapped-in opt-in reaches that slot's prompt. Absent, it is
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

`checklist` carries the project's recurring bug classes. On the diff kind the harness ACQUIRES it
when the caller passes none (TOOL-dFairHearing-15): its first agent, `resume:checklist` in the
`Resume` phase, before the input print and the resume probe, finds the memory-tree kit's checker
at run time, the first of `<tool root>memory-tree/gotchas.py` and `<tool root>gotchas.py` that
`git ls-files --error-unmatch` calls tracked, runs `gotchas.py --for-diff <base>..<head>` over the
range the call pinned with a 120-second bound, and returns its stdout verbatim, which then takes
the path a caller's string takes below. An acquired checklist logs `checklist from --for-diff
<base>..<head>` and RUN INTEGRITY says so; no checker tracked, a non-zero exit, a timeout, stdout
with no `- ` line (`no bug class selected`), a return that is not whole or a dead agent logs a `WARNING:`
naming the reason, and
RUN INTEGRITY's `Checklist:` line names it as `not acquired: <reason>`. A caller's `checklist`
wins and no agent spawns; the spec kind never acquires, since `unattended-build.js` hands its audit
a `--for-paths` one. A return is WHOLE (TOOL-dFairHearing-23) when it carries the checker's `# by
design —` head and its `- ` items before that head number `n + u + k`, `n` and `u` from its `# <n>
class(es) selected by an anchor + <u> universal` line and `k` from its `# invariants are read at <sha>;
<k> that ...` line, 0 when absent; any other return is a `checklistError` naming the cut, so a
tail-truncated stdout never passes as complete. A caller passes the same stdout, or its own curated list:

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
split is logged, and RUN INTEGRITY states it. An absent (on the spec kind) or itemless checklist logs a `WARNING:` and
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

Under a declared `disposal`, every hand-out past the disposal carries `chainRecord`, the one command
that records the round through the driver's `--record-round`. The harness renders it and never runs
it, because the round is recorded after the caller commits the folds it joins to. A dead disposal
returns before it, and with no `disposal` or no audit the key is absent.

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

`batchBy` is `'id'` or `'address'`, and absent it is `'id'`: the order the findings are sliced into
the fixed count of skeptic batches in. `'id'` slices them in id order, lens by lens. `'address'` sorts a
copy by `deriveAddressKey`, the file, then the line on a diff review or the first `[tag]` or section
token of `where` on a spec audit, then lens and id, so two lenses citing one place meet one skeptic; the
batch count and sizes are the same on both. Any other value refuses before the first agent, and the
`<n> finding(s) -> <k> verifier(s)` log line ends `by id` or `by address`. It ships dark: nothing in this
kit passes `'address'` until the replay records a hit. On both orders a batch is labelled
`verify:batch-<n>` and its result file is `verify-batch-<n>.json`, carrying its member ids as `ids`,
since the label no longer tells them; a verify file without `ids` is never reused.

`addressTwins` is `'hidden'` or `'shown'`, and absent it is `'shown'`. Under `'shown'` the synthesis
is handed two more blocks after the UNVERIFIED findings: `REFUTED findings`, one line per refuted
finding with its claim and the skeptic's reason, and `SAME-ADDRESS PAIRS`, each confirmed and refuted
finding that `deriveTwinPairs` reads as one address through `deriveAddressKey` and `checkSameAddress`.
A merged duplicate is never among the refuted. The synthesis is told to flag a refuted finding that
describes the same defect as a confirmed one and return each as `{refuted, confirmed}` in `twinFlags`,
which its schema then requires, and RUN INTEGRITY states how many refuted findings and pairs it was
shown. A flag notes a twin and never overturns a verdict: no verdict, grade, item or count moves. Any
other value refuses before the first agent. It joins no review key, since the synthesis writes no keyed
file. Its default became `'shown'` when TOOL-dFairHearing-1's replay 3 met its bar
(`memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-verdicts.md`), so every run that
passes no `addressTwins` hands the synthesis both blocks and requires `twinFlags` of it; a caller passes
`'hidden'` for the synthesis prompt and schema of before.

`twin` is the policy key `review.twin`, passed directly as a pin argument until a policy-file trigger
lands: `'never'`, `'design-records'`, `'design-and-landing'` or `'always'`, and absent it is `'never'`;
any other value refuses before the first agent. It twins a run under `'always'`; under
`'design-records'` on a design-record audit, a spec audit whose subjects are all design subjects by
`SPEC_SUBJECT_PATH` or whose `preset` is not `'unit-spec'`; and under `'design-and-landing'` on that case
or on any diff review, every diff review here being the closing review. A twinned run dispatches a
second finder run, run b, over the same lens literal after run a, as a second bounded fan: run b's
labels end `:b` (`find:<lens>:b`, so a dead one sits in `pending` that way) and its lens files are
`find-<lens>-b.json`. Ids number run a's findings first and then run b's, so each run is one contiguous
range; the verify stage keeps its fixed batch count over the union, and `agents`, `lensesRun`, every
count and the review-shape line cover both runs. Each confirmed finding reaches the synthesis carrying
`run=a` or `run=b`, under a `TWIN RUN` block listing the cross-run candidate pairs at one address by
`deriveAddressKey` and asking for one item per defect, its ids from either run or both. The harness
renders `review-twin runs=2 a=<first>-<last> b=<first>-<last>` (`-` for a run with no finding), which the
synthesis copies verbatim directly below the review-shape line. The final return carries `twin`: `{a,
b, agreed, onlyA, onlyB}`, run a's and run b's confirmed ids and three ITEM counts derived from the
item list, `agreed` holding a confirmed id of each run; it is `null` when the tally refuses the items,
when no synthesis ran, and on every untwinned run. A twinned run's key print gains `twin: true`, so it
never reuses an untwinned run's files; an untwinned run's key and synthesis prompt are unchanged.

`fixJudge` is `'instance'` or `'class'`, and absent it is `'class'`: how a skeptic judges a finding's
proposed fix. Under `'instance'` it judges the fix against the instance the finding cites, and every
skeptic prompt and the review key are as they were. Under `'class'` it asks whether the fix cures the
defect's class, every instance of the pattern the claim names in the subject and the code or specs it
reaches, and `FIX_VERDICTS` gains `'instance'`: the fix cures the cited instance and leaves another of
its class standing, `fixNote` holding the class-level fix. A fix judged `'instance'` with a note gives
way to that note in `confirmedFindings` and the synthesis's fix line, as an unsound one gives way to its
correction, and RUN INTEGRITY counts the instance-only fixes. Under `'instance'` a skeptic answering
`'instance'` reads as not judged. `'class'` joins the review key; any other value refuses before the
first agent. Its default became `'class'` when TOOL-dFairHearing-1's replay 4 met its bar (the same
verdict record). Since `'class'` joins the review key, every run that passes no `fixJudge` derives a new
key from then on, and no lens or verify file an earlier default run wrote is reused; a caller passes
`'instance'` for the skeptic prompts and the key of before.

Every confirmed finding is given one DISPOSITION from the report step's grammar: `class:<slug>`, a
class this run was handed; `gate:<leg>`, a leg of the leg manifest; `new:<slug>`, a slug matching
`[a-z][a-z0-9]*(-[a-z0-9]+)*` that is no handed slug; or `none`. The handed class slugs are the
checklist items' slugs, read by the rule `classes` reads, so a `C<n>` label with no slug is no class.
The leg names come from `gateManifest`, the name drift-audit-state's harness gives the same input
(TOOL-dFairHearing-23), a repo-relative path refused on the `specs` rule, defaulting to the kit root's
`gate-legs.json` as rendered at install: the resume probe reads it and returns `legs`, the `name` of
every object in its top-level array, beside `legCount`, the array's element count, and leaves both out
when the file is absent or is not such an array. The list is used whole or not at all: an empty one, one
whose length is not `legCount`, or one holding a non-string, an empty string or a duplicate reads as no
`legs`. With no `legs`, the log and RUN INTEGRITY say no leg manifest was read, and every
`gate:` disposition is refused. `unclassed` is the policy key `review.unclassed`, passed as a pin
argument until a policy-file trigger lands: `'refuse'`, `'reason'` or `'owner-rules'`, and absent it is
`'refuse'`; any other value refuses before the first agent. `none` is refused under `'refuse'`, and
admitted under the other two with a non-empty reason. The synthesis is handed the four forms, the
`unclassed` value, the class slugs and the leg names in a DISPOSITIONS block after RUN INTEGRITY, and
returns `dispositions`, one `{id, disposition, reason}` per confirmed id, which its schema requires.
The harness accepts the set only when every confirmed id has exactly one legal disposition and no other
id has one; otherwise it refuses the set whole, and `blockers` and `highs` keep their own derivation.
Neither `unclassed` nor `gateManifest` joins the review key.

`preset` picks a spec audit's lens literal, `'unit-spec'`, `'design-audit'` or `'whole-design'` (below), and absent it is
`'unit-spec'`, the five lenses above. Only the caller picks it, and the kind stays `spec-audit`, so
the binding line is unchanged. `'design-audit'` runs `DESIGN_LENSES`, the `design-audit` rows of `lenses.toml`, for a design or
architecture record, whose sections are not a unit spec's: `coherence`, `grounding`, `reuse` and
`failure-envelope` in design briefs of their own, and `alternatives-and-cost` in place of
`blast-radius`. Any value outside `PRESETS` refuses, and so does any `preset` on a diff review, before
the first agent. A preset off the default is logged before the first agent and joins the review key,
so a design-audit run never reuses a unit-spec run's lens files; a run without it keeps its key. Every
spec audit names its preset in RUN INTEGRITY and carries `preset` on every return, beside `intensity`.
It ships dark: nothing in this kit passes `'design-audit'` yet.

**The whole-design walk, `preset: 'whole-design'`** (TOOL-dFairHearing-18). Five walkers, `WHOLE_DESIGN_LENSES`,
the `walk-1` to `walk-5` rows of `lenses.toml`, walk every item of a design through every scenario. The
preset requires a `walk` argument and every other preset refuses one, each refusal naming its field before the
resume probe:

```js
walk: { items: [{ tag: 'plan.input', step: 's1' }, ...],        // non-empty; tag and step ^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$, tags unique
        scenarios: [{ id: 'S1', name: '...', walks: '...' }, ...], // non-empty; id ^[A-Za-z0-9][A-Za-z0-9._-]{0,31}$, unique
        runs: 2,              // review.design-audit.runs: 1, 2 or 3, absent 2
        run: 1,               // which run this invocation is, 1 to runs; required
        seed: 'reverted-escapes', // review.design-audit.seed: reverted-escapes | synthetic | none, absent reverted-escapes
        keySha: '<64 hex>' }  // the key's SHA-256, required unless seed is none
```

One invocation is one run: `review.pin` invokes the harness `runs` times, `run` 1 to `runs`, so no run's report
exists while the next walks. `deriveWalkSlices` deals every cell of the item-by-scenario grid to exactly one
walker slot: run 1 by scenario, round-robin through `deriveChecklistShares`; run 2 by contiguous step band, the
steps in first-seen item order; run 3 diagonally, cell (i, j) to slot (i + j) mod 5. A slot with no cell is not
dispatched, and RUN INTEGRITY names it as an idle walker slot. Each walker is told `WALK_RULES`, held once in the
harness, its own slice, its scenarios with their `name` and `walks`, and, when seeded, the key's SHA-256 and that
the key is never to be read. Its schema is the spec kind's plus a required `walk`, one row per cell: `item`,
`scenario`, `actor`, `needs`, `witness`, `route`, `verdict` (`holds`, `finding` or `not-on-path`), `findings`
(zero-based indexes into its own findings) and `reason`. `deriveWalkGaps` checks each walker's rows against its
slice: a cell with no row or two, a row outside the slice, an empty field, a verdict outside the three, a
`finding` with no index or one past the findings, a `not-on-path` with no reason, and a `holds` carrying an
index are each a gap, and any gap reds the walk: the synthesis is told the count, to list each gap first, and
that its verdict token is BLOCKED. The joined table reaches the synthesis between `<<<WALK TABLE` and
`WALK TABLE>>>`, to be copied verbatim directly before the appendix:

```
## Walk table — run <r> of <runs>, sliced by <scenario|step|diagonal>
walk-seed mode=<seed> key-sha256=<keySha|->

| Item | Scenario | Actor | Needs | Witness | Route | Verdict |
```

A verdict reads `holds`, the finding ids `<R><w>-F<id>` (`R` is `A`, `B` or `C` for runs 1 to 3, `w` the walker
slot), or `not on path: <reason>`. Every skeptic batch is also handed eight clean cells, drawn at an even stride
from the `holds` cells sorted by `<item> · <scenario>`, and a walk with no finding still dispatches one cell-only
batch, `verify:cells`, and still synthesizes. A cell a skeptic refutes becomes an UNVERIFIED finding of the lens
`cell-sample`. A whole-design run is never twinned. Every return past the find stage carries `walkTable`, the
joined rows; `walkGaps`, one `<item> · <scenario> — <what>` per gap; `cellsSampled` and `cellsRefuted`, `null`
until the verify stage. The record's copy of the table is not verified; the return is the source of record.

`optIn` swaps an opt-in lens into a default slot of the run's literal: `{ "<opt-in lens>": "<default
lens it replaces>" }`, absent meaning `{}`. The literal keeps five slots, so the swapped lens runs where
the default would have and the default does NOT run; its coverage is dropped for that run. Each default
slot is rendered as a `deriveSlotLens('<literal>', { key, brief })` call, which returns the
`OPTIN_LENSES` row the swap names, carrying `replaces: <default key>`, so the finder label, the lens
file and the lens-yield row all name the opt-in. Its shape is refused before any agent, beside
`intensity` and `preset`: not an object, or a key or value outside `^[a-z][a-z0-9-]*$`. Its membership
is refused by name before the resume probe, in this order: an opt-in already a lens of the literal; one
no shipped row offers for that literal; a default the literal lacks; and one default named by two
keys. A light diff run selects its slots by each slot's default key, so a swap into a light slot runs
there. A non-empty `optIn` joins the review key, each swap is logged before the first agent and named in
RUN INTEGRITY, and every return carries `optIn` beside `intensity`. A lens note keyed to a replaced
default is accepted and reported unread, since the swapped lens is the one that runs. Only an `optin = true` row of
`lenses.toml` can be swapped in, and today none is: each opt-in row ships `optin = false` until its
losing test is recorded.

`review_pin.py`, beside the harness, is the stand-in for `review.pin`: it prints the `preset`,
`optIn`, `twin` and `unclassed` of one spec-audit call as one JSON line, one line per run under
`whole-design`, and runs nothing.

```
python <kit>/review_pin.py --subject <path> [--subject <path> ...]
                           [--opt-in none|'<json>'] [--design-record-preset unit-spec|design-audit|whole-design]
                           [--design-audit-runs 1|2|3] [--design-audit-seed reverted-escapes|synthetic|none]
                           [--twin never|design-records|design-and-landing|always]
                           [--unclassed refuse|reason|owner-rules]
# defaults: runs 2, seed reverted-escapes
# whole-design: one line per run   {"preset": "whole-design", "walk": {"runs": 3, "run": 1, "seed": "synthetic"}}
# otherwise: one line, a key only for each flag given
```

`--design-audit-runs` and `--design-audit-seed` are `review.design-audit.runs` and
`review.design-audit.seed` (TOOL-dFairHearing-23), checked for shape only. When the printed preset is
`whole-design` the module prints one line per run, run 1 to `runs`, each carrying its `walk` of `runs`,
`run` and `seed`; the caller adds the design's items, scenarios and key hash before it invokes the
harness. Under any other preset no line carries `walk`. A `--subject` carrying `\` exits 2 first,
naming the backslash, as the harness's `specsRule` refuses one, so a backslashed spec path is never
classed a design record.

A subject is a spec subject when the harness's own `SPEC_SUBJECT_PATH`, read from the `tier2-review.js`
beside the module, matches it; every other subject is a design record. A set holding any spec subject
prints `unit-spec`; a set of design records alone prints `--design-record-preset`, whose default,
`DESIGN_RECORD_PRESET`, is `unit-spec` until the design-audit replay's verdict. `--opt-in` is the
`review.opt-in` value: `none`, the default, or a JSON object keyed by literal name whose values are
`optIn` maps, and the entry for the printed preset rides as `optIn`. It checks `--opt-in`'s shape only;
membership is the harness's. It exits 2 naming `SPEC_SUBJECT_PATH`, `--opt-in` or `--subject` on a
harness with no predicate line, a malformed value or no subject. `--twin` is the `review.twin` value,
printed as `twin` when given and checked against the four values only; absent, no `twin` is printed.
`--unclassed` is the `review.unclassed` value, printed as `unclassed` the same way and checked against
the three values only.
`unattended-build.js` forwards a
caller's `optIn`, `preset` and `lensNotes` to its audit stage's review call unchanged, and unchecked.

Every finding carries `lens`, the key of the lens the harness dispatched, never the label the agent
echoed back, and every finding line in a skeptic prompt, the synthesis prompt and the run log names
it as `lens=<key>`. On a spec subject under a declared `disposal` a complete return also carries
`addresses`, one `{ids, severity, specs}` per BLOCKER or HIGH item; with no `disposal` that list is
empty and an item owes no `specs`. Under `addressTwins: 'shown'` the final return also carries
`twinPairs`, the number of same-address pairs the synthesis was handed, and `twinFlags`, each flag it
returned whose `refuted` id stands refuted and whose `confirmed` id stands confirmed, as `{refuted,
confirmed, sameAddress}`, with `sameAddress` true when the pair was one of those handed. A repeated flag
is dropped, a flag naming any other id is discarded and named in a `WARNING:` line, and a dead
synthesis returns `[]`. Under `'hidden'` neither key is present. The final return carries
`dispositions`, the accepted `{id, disposition, reason}` list in confirmed-id order, `null` when the set
was refused or no synthesis ran; `dispositionFault`, `''` or each failing id and why, which the `note`
repeats; and `ownerItems`, the ids disposed `none` under `unclassed: 'owner-rules'`, else `[]`.

Each round's state is the harness's own (TOOL-dFairHearing-17). Two optional arguments, checked before
any agent beside `round`, feed it, and neither joins the review key. `roundLimit` is an integer of 1 or
more, absent meaning no limit, which a log line says, since then neither `BOUNDED` nor `CEILING` can be
reached. `priorCounts` is an array of integers of 0 or more, each an earlier round's `roundCount` in round
order. With no explicit `round`, a non-empty `priorCounts` makes the round `priorCounts.length + 1`; an
explicit `round` that disagrees with it is refused naming both. The rule, `deriveRoundState`, is the
driver's `review_state` order: a count of 0 reads `CONVERGED`; a count no smaller than the round before's
reads `NON-CONVERGENT`; a round past `roundLimit` reads `CEILING`, one at it `BOUNDED`, and any other
`CONVERGING`. The suite's parity arm holds it equal to `review_state` over every sequence both can see. The
synthesis is handed one record line between `<<<ROUND` and `ROUND>>>` and told to copy it verbatim directly
below the review-shape line:
`review-round round=<n> limit=<n|-> prior=<c1,c2,…|-> count=<n|-> state=<STATE|->`, a `-` standing for
an absent value, never a `0`. The harness reports the state and never stops, re-arms or refuses a round on it.

Every return carries seven fields beside the counts:

- `roundCount` and `roundState` — the round's confirmed blocker and high findings by binding grade,
  `verifiedCounts.blocker + verifiedCounts.high`, known before the synthesis, and the rule over it. Both
  are `null` on every `deferred-platform` exit; a complete exit with no confirmed finding carries `0`
  and the rule over `0`. `roundState` is also `null`, beside an integer `roundCount`, on a round above 1
  with no `priorCounts`, which a `WARNING:` line names. Pass `roundCount` on as the next round's
  `priorCounts` entry. A whole-design run whose walk table has a gap, `walkRed`, returns `blockers`, `highs`, `roundCount` and `roundState` as `null` and a `note` opening `BLOCKED: the walk table has <n> gap(s)`,
  ranked after a dead synthesis's `DEFERRED:` and before a tally fault's `UNVERIFIED:`, and its record line reads
  `count=- state=-` (TOOL-dFairHearing-20): a gapped walk's count is no clean reading, so no caller routing on
  the counts may take its `0` and `CONVERGED` as one.

- `shape` — one record line, also logged, in this fixed grammar:
  `review-shape kind=<diff-review|spec-audit> round=<n> intensity=<full|light> at=<find|verify|synth> raw=<n|-> confirmed=<n|-> refuted=<n|-> merged=<n|-> unverified=<n|-> blocker=<n|-> high=<n|-> medium=<n|-> low=<n|-> agents=<n> out-tokens=<n|unknown>`.
  `at` is the stage the exit reached; a count that stage has not produced is `-`, never `0`, and the
  every-lens-dead exit prints `raw=-`. `merged` counts the findings a skeptic refuted as `duplicate of
  id=<n>` of a confirmed finding in the same batch: they leave `refuted`, count as confirmations in
  `precision`, `(confirmed + merged) / (confirmed + merged + refuted)`, and never join the confirmed
  set; the ledger keeps their `refuted` verdict. A duplicate whose original is not such a survivor is
  demoted to unverified on either kind, and every return carrying `refuted` carries `merged`. The four severities count RAW confirmed findings by binding
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
  stands), `reason`, `fixVerdict`, `claim`, `classes` and `disposition`. An absent optional value is `null`.
  `disposition` is the accepted disposition on a confirmed entry, and `-` on every other entry and
  wherever no set was accepted; `confirmedFindings` carries it the same way.
  `classes` lists the checklist classes the claim's leading `C<n>` labels denote, by each item's
  slug, in order and without duplicates; a label with no slug to resolve, its item absent or not
  slug-led, is kept as `C<n>`. It is `[]` when the claim opens with no label or the run had no
  checklist.
- `confirmedFindings` — one entry per confirmed finding: `id`, `lens`, `ref`, `claim`, `severity` (the
  binding grade), `fix` and `fixVerdict`. A fix the skeptic judged unsound is replaced by its note
  when it gave one. Pass this array as the next round's `priorFindings` rather than re-typing it.
- `appendix` — the ledger as a markdown table under `## Appendix — every finding`, with the ten
  columns `id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition`. The
  ninth joins the `classes` names with one space, so a class's hits can be counted across records. The
  tenth is the disposition: the synthesis is handed the table with `(synthesis)` in each confirmed row's
  cell and `-` in every other, and told to copy it verbatim but for those cells, each written with the
  disposition it returns, a `none` as `none — <reason>`, the reason on one line and a pipe written as
  `\|`; a reason carrying a raw `|` or a line break refuses the set, its note naming the record's
  appendix as needing a re-render (TOOL-dFairHearing-23). The returned table carries the accepted
  dispositions so, and `-` in every cell when the set was refused. A
  cell is `-` when its value is absent or empty, a `|` is escaped, and line breaks fold to a space.
- `lensYield` — per lens, `defects` and `unique` are `null` when no item list can be trusted (see below).
  One row per lens that RAN, in dispatch order, none for a lens a light run skipped:
  `lens`, `returned` (false for a lens that died), `raw`, `confirmed`, `refuted`, `merged` (a refuted
  row whose reason opens `duplicate of id=<n>`, out of `refuted`), `uncertain`,
  `unverified` (every finding neither confirmed, merged nor refuted, the uncertain ones included), `precision`
  (`(confirmed + merged) / (confirmed + merged + refuted)`, `null` when all three are 0), `defects` (synthesis items holding a
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

## The lens catalogue — `lenses.toml`

Every review lens is a row of `lenses.toml`, beside the harness. A workflow script has no filesystem
when it runs, so the harness cannot read the file: `render_lenses.py` fills each lens literal of
`tier2-review.template.js` from it, at install and in the parity leg, through the `LENS_SLOTS`
token. A literal opts in with a marker ending its opening line,
`const SPEC_LENSES = [ // gov:lens-slots unit-spec`, and its body is the one line `{{LENS_SLOTS}}`.
Add or swap a lens as a row, never by an edit to either harness copy.

```toml
[[lens]]
key = "coherence"            # ^[a-z][a-z0-9-]*$, the key lensNotes and a finding's `lens` use
kinds = ["spec-audit"]       # the review kinds it may run under: diff-review, spec-audit
presets = ["unit-spec"]      # every literal it may fill, by default or by a swap
default_in = ["unit-spec"]   # the literals it fills by default, a subset of presets
optin = false                # whether it may be swapped into a literal of presets it is no default of
brief = "Coherence: ..."     # one line, raw text; the render escapes \ and '
```

A literal's name is what its marker declares: `diff-review` for the diff kind's literal, a
spec-audit preset name otherwise. The set is read from the template's markers and typed nowhere
else. A row's place in the file is its slot order. A row with `default_in = []` and `optin = false`
is catalogued and selected by nothing. Every `optin = true` row also renders under the line
`const OPTIN_LENSES = [ // gov:lens-optins`, whose body is the same token, as `{ key, presets, brief }`:
the set `optIn` may swap in. The six opt-in rows, `security`, `alternatives`, `cost`, `portability`,
`adopter-migration` and `topology`, ship `optin = false`; recording a blind-replay test a row does not
lose flips that row and nothing else.

The renderer refuses, exit 2, naming the row and the rule: a file that is not TOML or carries a key
beside `lens`, or a python below 3.11 (rule 1); a missing, extra or mistyped field, a bad key, an
empty or multi-line brief (2); an empty or repeating `kinds` or `presets`, an unknown kind (3); a
`default_in` outside `presets` (4); `kinds` disagreeing with the kinds of `presets` (5); two rows
sharing a key and a literal (6); a key equal to a literal name (7); a literal no marker declares (8);
a marked literal no default row fills (9); an opt-in row with no literal outside its `default_in`
(10); a marker not followed by the token, or a token with no marker (11). It does NOT count slots:
`check-verifier-fanout.sh` holds every marked literal to exactly five, so a sixth default row
renders and reds there. The leg finds the literals through `render_lenses.py --markers <file>`, which
prints the line number of each line the renderer's own anchored marker regex matches, so one predicate
finds a marked literal and a comment naming `gov:lens-slots` is no marker; `check-verifier-fanout.js
--slots` counts each with `topLevelArgs`, rule 2's counter, over the hook's literal-blanked view, and
`LENS_SLOTS` there is the one home of the five (TOOL-dFairHearing-23).

## `workerType` — judges spawned as a named agent type, in all three harnesses

Every agent a harness spawns loads the charter through `CLAUDE.md` before its task. A judge reads a
brief the harness wrote and lands nothing, so `workerType` lets a caller spawn the JUDGES as a named
agent type instead. In `tier2-review.js` an absent `workerType` reads as `Plan`, the default one
measured A/B pair set (TOOL-aMendedFleet-93's reading): its read-only judges matched the charter-loaded
arm's precision at about half the first-turn context. The reserved literal `none` spawns every judge as
`general-purpose`, the harness's `PLATFORM_TYPE` and the Agent tool's own default, durability
instructions and review key included (TOOL-dFairHearing-11). In the two drift harnesses an
absent `workerType` still spawns every agent as the platform default, because no pair measured them.

```js
// tier2-review.js: every finder and every skeptic batch spawns as the type
args: { repo, base, head, reviewDir, workerType: 'Plan' }
// drift-audit-code.js and drift-audit-state.js: the skeptic batches only
args: { repo, base, outDir, workerType: 'Plan' }
```

The value must match `^[A-Za-z][A-Za-z0-9_-]{0,63}$`, or the harness refuses before any agent spawns
with a message naming `workerType`. A well-formed name the platform does not know comes back as its
named `not found` refusal, which each harness already counts as a dead agent. `workerType` does not
reach the tier2 orchestrating agents, each typed by its own stage instead: the resume probe, which reads
the lens files, spawns as `Plan` unless `roles.probe` names a type, and the synthesis, which writes the
report, as `general-purpose` unless `roles.synthesis` does. So no tier2 agent spawns untyped, and a stage
resolving to no type is refused by name before the probe.

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

## roles — stage agents spawned as catalogue roles

The build harness, the unit harness and the review harness take an optional `roles` object mapping a
stage key to an agent type: the catalogue's harness arguments for that harness, which a caller passes
as printed. A stage it names spawns as that type and the craft its role now carries is left out of the
prompt; in the build and unit harnesses its prompt also carries one sentence after the grounding text
naming the type. A stage it does not name spawns as it did before roles, untyped in those two and
under `workerType` in the review harness, and each harness logs one line per stage saying which.
`{}` and an absent `roles` mean the same thing.

```js
// unattended-build.js: specWriter, committer and disposal spawn here; builder travels in
// dispatch.args to each unit; specFinder, skeptic and synthesis are forwarded to the audit's review call
args: { repo, slug, scratch, units, roles: { specWriter: 'gov-spec-writer', disposal: 'gov-spec-writer',
        builder: 'gov-builder', specFinder: 'gov-spec-reviewer', skeptic: 'gov-skeptic', synthesis: 'gov-synthesizer' } }
// unattended-unit.js: its one key
args: { ..., roles: { builder: 'gov-builder' } }
// tier2-review.js: its four keys, only the running kind's finder key read
args: { repo, base, head, reviewDir, roles: { diffFinder: 'gov-diff-reviewer', specFinder: 'gov-spec-reviewer',
        skeptic: 'gov-skeptic', synthesis: 'gov-synthesizer' } }
```

Each harness refuses, before any agent spawns: a `roles` that is not a plain object, a key outside its
own set, a value not matching `^[A-Za-z][A-Za-z0-9_-]{0,63}$`, and the value `none`, which is the review
harness's reserved untyped literal; an untyped stage is spelled by leaving its key out.

- **The builder's hand-back.** With `roles.builder` the unit agent does not edit its spec. It sets the
  status header to CLOSED with today's date, an edit changing nothing else, and on a divergence it
  commits nothing and returns `why` opening `DIVERGENCE:`. The unit harness returns `diverged: true`
  exactly then, so the caller branches on a field: it has the spec-writer role revise the spec and
  dispatches the unit again. Untyped, the builder keeps today's order to change the spec first.
- **The audit's roles.** The review keys reach the review harness's `roles` beside `workerType: 'none'`,
  which then governs only a judge stage no role names. A judge run under a role writes no lens or verify
  file, so a deferred-platform return whose review says `durable: false` tells the caller the re-run
  dispatches every judge again, instead of promising a reuse.
- **The review harness's roles.** `tier2-review.js` takes five keys: `probe` names the resume probe;
  `diffFinder` and `specFinder` name the finders of a diff review and of a spec audit, only the running
  kind's key being read; `skeptic` names every skeptic batch; `synthesis` names the synthesis. A key wins
  over `workerType` for its own stage, `workerType` keeps every judge stage no key names, and under
  `none` such a judge takes `general-purpose` (`PLATFORM_TYPE`); the synthesis takes its key or
  `general-purpose`, and the resume probe its key or `Plan`, which holds no Write tool, logged as a
  `role probe:` line beside the other three (TOOL-dFairHearing-11). Every spawn carries an explicit
  `agentType`, from one of the four stage option constants `probeOpts`, `findOpts`, `verifyOpts` and
  `synthOpts`, and the suite reds an `agent(` call taking none. A roled finder or skeptic is told none of
  the posture its role carries, and keeps every stage protocol sentence: the acquire step, the rubric,
  the probe policy, the schemas. Any judge off `general-purpose`, under a type, a role or `workerType`,
  makes the whole run not durable, so every judge writes no file and a re-run dispatches every finder and
  skeptic again; a synthesis or probe role alone keeps a `none` run durable and its key. A judge role
  joins the review key; the synthesis and probe roles do not.
  Compose the object with `<prefix>/roles/handoff.py harness-args tier2-review` rather than by hand.
- **The harnesses' efforts** (TOOL-aOrientedCast-10). Each harness takes `efforts` beside `roles`, keyed
  by the same stage keys: a level of lower-case letters, set as that stage's `agent()` `effort` option.
  It is independent of `roles`, so an untyped stage still takes its level; a stage it does not name
  passes no `effort` and runs at its agent type's level, else the session's, and each harness logs one
  `effort <key>:` line per stage saying which. The review harness sets it on the resume probe only
  under `efforts.probe`; the build harness spawns its spec writer, spec commit and disposal at theirs, forwards the audit's three
  review keys as the review call's `efforts` and `builder` in `dispatch.args`. A malformed object, an
  unknown key or a value off the shape refuses before any spawn. The vocabulary is the roles kit's, so
  a harness grades the shape only. Compose it with `<prefix>/roles/handoff.py stage-efforts
  <workflow>`, keyed by WORKFLOW: the review harness serves spec review and closing review, which run
  one role at two levels.
- **The parity arm.** A workflow script cannot import, so each harness that tests an agent type keeps its
  own copy of the shape. The protocol-parity leg's agent-type shape arm compares every copy in this kit
  with the one `tier2-review.template.js` owns, and reds on a difference or on an owner yielding none.

## Agent labels — slug, scope, stage

Every agent the three declared harnesses spawn carries the label `<slug> · <scope> · <stage>`
(TOOL-aOrientedCast-27), the parts joined by a space, a middle dot and a space. The scope is the unit
id where the stage serves one unit, the ids of its group where a spec writer serves several, and else
the stage's scope.

| Harness | Stage | Label |
|---|---|---|
| `unattended-build` | spec writer | `<slug> · <the group's unit ids> · spec-write` |
| | spec commit | `<slug> · specs · commit` |
| | audit subjects | `<slug> · audit round <n> · subjects` |
| | audit record | `<slug> · audit round <n> · record` |
| | disposal | `<slug> · audit round <n> · dispose` |
| `unattended-unit` | builder | `<slug> · <unitId> · build` |
| `tier2-review` | resume probe | `<slug> · <kind> round <n> · resume:probe` |
| | finder | `<slug> · <kind> round <n> · find:<lens>` |
| | twin run b finder | `<slug> · <kind> round <n> · find:<lens>:b` |
| | verify batch | `<slug> · <kind> round <n> · verify:batch-<n>` |
| | synthesis | `<slug> · <kind> round <n> · synth` |

The group's unit ids are joined by single spaces in roster order, and `<n>` is the run's round. The
review harness reads its slug from `reviewDir`: the segment after a `builds/` segment, when it is
letters only, else none, so a review outside a build folder carries no slug part. Its stage is the
label it carried before, so `pending`, its log lines and every reader of a stage keep their spelling:
`pending` lists stage keys, never whole labels. The roles kit's `handoff.py agents` reads a harness
agent's unit as the one unit id its label names. No hook sees a label, since `agent()` is a runtime
call; the two harness suites hold them.

A run's title is not a label: the tool fixes it from the script's `meta.name`. Each run says what it
is in its first log line, before its first phase, and leads every return with the same text as
`identity`:

| Harness | `identity` |
|---|---|
| `unattended-unit` | `<slug> · <unitId> · build`, its agent's label |
| `unattended-build` | `<slug> · <mode> round <n> · spec, audit, disposal, hand-out`; `spec, hand-out` without `specAudit` |
| `tier2-review` | `<slug> · <kind> round <n> · review`, under its labels' slug rule |

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
  scored as zero and never read through the legacy table. A spec ref is `<file>:<where>`, read by
  `extract_tag_ref`: its key is the first lower-case `[tag]` anywhere in the address, as a
  design-record audit addresses a finding, else the section rule: the first `§<n>` or `section <n>`,
  else the first `S<n>`, `AC<n>` or `F<n>` as §2, §6 or §8; an address naming none (`status header`)
  is UNSCORABLE. A match is the same file and the same key, compared by equality: the window is
  forced to 0, `--window` is ignored, and the candidate line prints `address section`. The `replay: known` line carries `kind spec-audit` and the
  subject pins written after the binding line, or `subjects none-stated`; no range is required. A
  candidate opening with the other kind's `**Serves:**` binding is refused `kind-mismatch`, naming
  both kinds, in either direction; an unbound candidate is read in the known record's mode. Spec
  records are not listed by `--corpus`: name the known record directly.
- `python3 {kit}/review_replay.py --known-set <src> --candidate <src> [--matched <src>]` — a candidate
  scored against a known-set file (`TOOL-dFairHearing-1`) in place of a past record: one
  `| tag | address | grade | escaped |` row per known defect, `address` being `<record path>:[<tag>]`,
  `grade` `high`, `medium` or `ungraded` and `escaped` `yes` or `no`, under a
  `**Population:** <n> · reviewed <n> · escaped <n> · high <n>` line. `parse_known_set` refuses a row
  count or a partition count that line does not state, a repeated tag and an address `extract_tag_ref`
  cannot read. Every confirmed candidate row `extract_tag_ref` keys at a row's record and tag prints as
  an `address-match` line: candidates for the adjudicator, never a score. `--matched` names the
  adjudicator's list, an `**Adjudicator:** <who>` line and a `| candidate | tag |` table of appendix
  ids and known tags; a pair whose candidate is no confirmed row, or whose ref cites the row's `[tag]`
  nowhere, exits 2 by name, each tag counts once, and `reviewed k/n`, `escaped k/n` and `high k/n`
  print from those pairs alone. Every `<src>` reads as the factory's does.
- `python3 {kit}/review_replay.py --corpus <dir> [<dir> ...] [--repo <clone>]` — which past records
  are replayable: each record whose first line is the `**Serves:** diff-review` binding, that passes
  the liveness check below and whose range resolves in this clone, with its round, range and scorable
  count. The summary line puts every scanned record in exactly one bucket. Ranges resolve through
  ONE `git cat-file --batch-check` for the whole corpus.
- `python3 {kit}/review_replay.py --selftest` — named arms over inline fixtures, no file
  or git access, then the factory's runner below; red when an arm of either fails or either ran fewer
  arms than its own `ARMS_DECLARED` states. It is the held leg `review-replay selftest`.

**The replay scorer factory, `replay_scorer.py`** (`TOOL-dFairHearing-12`). The scoring core above
lives there as its `review-replay` instance, and this file is that instance's adapter: its CLI, its
printer, its corpus listing and its arms. The second instance, `scouted-seam`, is aScoutedSeam's
reuse grader (`check_hit`, `check_case` and the `grade`, `compare` and `judged` readings), ported from
its grader blob at `b0fe68f30`. Both sit in one `INSTANCES` table, and `check_instances` reds when it
lacks either. Every population arrives as a `<src>`: a working-tree path, a 40-hex blob or
`<rev>:<path>`, read by one `git cat-file blob`, and an object git cannot read is refused, never an
empty arm. `derive_paired_cases` is the one place variants are paired with cases: it refuses an
answer outside the population, a variant that answered nothing and an empty pairing, and each figure
line opens with `paired <n> of <N> · <variant> unanswered <ids>`, in the case file's and the
arguments' order.

- `python3 {kit}/replay_scorer.py --instance scouted-seam --cases <src> --results <src> --grade <arm>`,
  `--compare <arm> <arm> [...]` or `--judged <arm|a+b> [...]`.
- `python3 {kit}/replay_scorer.py --instance review-replay --known <src> --candidate <src> [--window N]`
  — the same score `review_replay.py` prints, its inputs read as `<src>`.
- `python3 {kit}/replay_scorer.py --experiment <src> [--repo <clone>]` — an experiment declared once,
  in a committed JSON manifest beside its raw outputs, scored under the method below.
- `python3 {kit}/replay_scorer.py --design-recall --key <known-set file> --seed <mode> <record-run-1> [<record-run-2> ...]`
  — a whole-design walk's recall on a seeded key (TOOL-dFairHearing-18), graded as `review.design-audit.seed`
  says. Each record is one run's review record, read by its `## Walk table — run <r> of <runs>` heading, its
  `walk-seed` line and its confirmed appendix rows, each ref keyed by `extract_tag_ref`; each plant is one
  known-set row of the key, matched on the same file and key. It prints each run's and the union's hits over the
  plants, then each missed plant's `tag`, and exits 0 when every run finds two thirds of the plants and, with two
  runs or more, the union five sixths, 1 when one is under its bar, and 2 on a key whose SHA-256 over its bytes
  is not every record's pin, records disagreeing on `runs`, a run missing or repeated, a record seeded another
  way, a plant whose `escaped` disagrees with the seed (true under `reverted-escapes`, false under `synthetic`),
  or a confirmed row with no file and key. `--seed none` prints that recall is not graded, reads no key and
  exits 0. Making the sealed copy and its key stays the caller's.

**The experiment shape, `--experiment`** (`TOOL-dFairHearing-14`). aScoutedSeam's figures held because
of how they were measured, and `check_experiment` makes that method a rule where committed outputs
show it and a recorded line where they cannot. The manifest, read through `read_raw_output`, names
`instance`, `cases`, `results` and `arms`, each arm `{name, base, settings, dispatched}`, and may name
`heldOut`, `judge {verdicts, key}` and `union {tuning, heldOut}`; the `review-replay` instance takes
`known` and `candidates` in place of `cases` and `results`. An unknown key is refused,
so a misspelt rule is never skipped. Every rule runs before the first figure line, and a broken one
exits 2 naming the rule, the arm or case, and the value:

- **evidence** — each instance's `case_evidence` hook: a `scouted-seam` case's `sha` and every
  ground-truth item's `path` and `why`, a `review-replay` item's ref and its record. A case it returns
  nothing for is refused by id, and an instance registered without the hook fails `check_instances`.
- **freeze** — `check_held_out_frozen`: `heldOut` names a working-tree file inside the repository
  whose `git log` lists exactly one commit, printed first as `held-out: frozen at <sha>`, and shares
  no id with the tuning cases. The freeze is the bytes scored: `git hash-object` of the working-tree
  file, hashed through the checkout's filters so a CRLF checkout of an LF blob agrees, must equal the
  freeze commit's blob, or it exits 2 naming both object ids (`TOOL-dFairHearing-21`). A shallow
  history refuses before the history is read, since its boundary commit lists every file and so
  cannot show a freeze. "Never read to change a prompt" is printed as recorded, not checked.
- **one variable** — `check_one_variable`: an arm naming a `base` differs from its settings in exactly
  one key, compared as JSON values, and prints `arm <name>: varies <key> from <base>`.
- **parsed first** — `measure_parsed`: `parsed <arm>: <n> of <dispatched>` for every arm, `n` the
  cases holding a parsed row; an undeclared `dispatched`, or one below `n`, is refused. Figures pair
  the parsed rows only, so an unparsed reply is counted, never scored.
- **blind judge** — `check_judge_rotation`: a committed `judge.key`, `{<case>: {<label>: <arm>}}`,
  gives each arm one label per case, and with two or more of each no arm holds one label throughout.
  With no key it prints `labels rotated — recorded, not checked: no committed key`.
- **union** — `measure_union`, aScoutedSeam's system reading: per set, a positive case any of its arms
  was judged on is covered when any of them covered the primary. With `heldOut` declared it prints
  tuning, held-out and pooled, so the held-out cases join the score instead of standing beside it.

**The `review-replay` manifest** (TOOL-dFairHearing-23), the terms `TOOL-dFairHearing-1`'s void rule and
`TOOL-dFairHearing-15`'s `dispatched 4` and `paired 4 of 4` are written in:

```json
{
  "instance": "review-replay",
  "known": "<src>",
  "candidates": [{"case": "<record>", "report": "<src>", "matched": "<src> or null"}],
  "arms": [{"name": "<arm>", "base": null, "settings": {}, "dispatched": 4}]
}
```

A CASE is one review run of one subject record, and each `candidates` entry is one case: its `report`
and its `matched`, the adjudicated list `read_matched_list` reads, or `null`. An entry names its `arm`
whenever the manifest declares more than one; a one-arm manifest may leave it out. `dispatched` counts
an arm's dispatched runs, and `parsed <arm>: <n> of <dispatched>` counts the arm's runs whose report
holds an appendix with at least one row `parse_candidates` reads, through `measure_parsed`. A parsed
run with a `matched` list prints its known-set figures when `known` is a known set, and a parsed run
against a review record its recall. An agent death is read from the report's `RUN INTEGRITY` lens and
skeptic counts, never from the manifest or `parsed`. A `candidates` that is not such a list is refused
by name.

What the rules do not check: a variable nobody declared, that no prompt author read the held-out file,
that one judge read each case, and that the evidence is right rather than present.

Its runner's arms: the pairing and row refusals, the `[tag]` reading, the instance check, a proof
that the port reproduces the grader's figures over the committed cases and results at `b0fe68f30`,
determinism across two hash seeds, the conformance arm, and one arm per experiment rule over a
planted manifest, the union arm's proof reading the method's own experiment at `5f8ef021d`
(`system tuning 21/23`, `system held-out 12/12`, `system pooled 33/35`). That arm, `scan_pairing_sites`, reds on a
second scorer: a comprehension in a tracked `*.py` at and below this kit's directory, the factory
and any path under `memory/` excepted, so a repository-root install reaches no record folder, whose
filter is `all()` over a second population testing the outer case against the inner variant. It
reads Python only, and a pairing written as a `for` loop is not seen. In a tree without
`memory/builds/aScoutedSeam/` the proof prints `SKIP`, and so does the conformance arm once its
live-root and planted halves pass, its grader half unread, and the union arm once its fixture half passes; the count line names each skip, so an
install outside this repo never reads a skip as a pass.

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

### Replaying a review blind

A blind replay reviews a past state of the tree in a clone that holds nothing after it, so no later
record or object can reach a lens. The clone is made from a bundle of a transient ref, never by a
`git clone` given `--branch`, which cannot name a `refs/replay/` ref and exits 128. `<name>` and the clone
directory are fresh per replay, the directory under `%TEMP%`, never inside the worktree:

```bash
mkdir -p "$TEMP/<name>b"
git update-ref refs/replay/<name> <commit>
git bundle create "$TEMP/<name>b/h.bundle" refs/replay/<name>
git update-ref -d refs/replay/<name>
git init "$TEMP/<name>"
git -C "$TEMP/<name>" fetch "$TEMP/<name>b/h.bundle" refs/replay/<name>:refs/heads/<name>
git -C "$TEMP/<name>" checkout <name>
git -C "$TEMP/<name>" rev-list --count <name>            # above 0, or the clone is empty
```

The `refs/replay/<name>` ref lives only until the bundle is written, so `git show-ref
refs/replay/<name>` in the repository prints nothing afterwards, and the count line is the
liveness check: a clone whose count is not above 0 replays nothing and is not scored.

**A replayed spec audit passes the opt-in pack.** Its `<commit>` is a scratch commit on the original
adding `memory/builds/dFairHearing/README.md` as it stands at `3708a705`, whose front matter is the
owner-landed `spec-audit: 2026-10-21` with no `authorized-by`, and its `reviewDir` is
`memory/builds/dFairHearing/reviews`, the folder that README opts in. A replay that spawns agents
directly renders each prompt as a `gov:handoff` file, all rule 6 of the agent-cap hook admits; a
harness replay runs through `tier2-review.js`, a declared harness.

**The verdict of replay 1 flips `DESIGN_RECORD_PRESET` in `review_pin.py`**, the one value it edits, never
a template default: the harness's own `preset` default stays `unit-spec`, so only a pin over design
records alone moves to `design-audit`.

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
