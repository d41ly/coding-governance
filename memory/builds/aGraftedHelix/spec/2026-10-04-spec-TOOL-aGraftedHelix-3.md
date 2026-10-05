# TOOL-aGraftedHelix-3 — invariant records in the bug-class catalogue become the review's by-design list

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 5266d22e · streams tooling · order 3 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |
| [2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |

<!-- /gen:spec-records -->

## 1. Goal

The review harness has a `byDesign` input that tells finders what not to report and tells skeptics
what to refute, and no code in the tree fills it (`tools/workflows/tier2-review.template.js:159-164`
says so). This unit adds an `invariant` kind to the gotcha catalogue, prints the invariants a
change touches as a by-design block after the bug-class checklist, and makes the harness take that
block as its by-design list. The checklist is already handed to reviewers, so no new caller is
needed. The unit also routes the checklist into the spec audit, which has never received one.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/gotchas.py` admits `kind: invariant` (pinned interface I5). Such a
  record carries a `decision:` front-matter key and five body sections: `## Looks wrong`,
  `## Actually`, `## Do`, `## Do not` and `## Guarded by`. `records()` carries the decision id and the
  first paragraph of each section. Observed by AC1 and AC2.
- **S2** — Check 18 grades every invariant record. Its `decision:` id must be in the defined-id set
  `corpus_ids.py` already derives. All five sections must be present and non-empty. The first line
  of `## Guarded by` must be `no machine gate`, or carry only backticked tokens that each resolve to
  a tracked path or to a leg name in the manifest the new `LEG_MANIFEST` conf key names. Observed by
  AC2 and AC3.
- **S3** — Check 19 grades invariants the way it grades classes: at least one derived anchor, and
  anchors that reach more than the append-only tree. An invariant marked `universal` is a finding.
  Observed by AC2.
- **S4** — `--for-diff` and `--for-paths` print the by-design block (pinned interface I4) after the
  checklist, whenever the selection is non-empty, with the count `0` when no invariant is selected.
  The selection predicate is `selectable()`, unchanged. `main()` sets stdout to UTF-8 before it
  prints. Observed by AC1 and AC4.
- **S5** — `INDEX.md`'s summary line and `--report` count invariant records. Observed by AC5.
- **S6** — `LEG_MANIFEST` is declared in `.memory-tree.conf` as `tools/gate-legs.json`. It is also
  declared blank, with its comment, in the shipped `tools/memory-tree/.memory-tree.conf.example`.
  When it is blank, a guard token that is not a tracked path is announced as unresolved and does not
  fail the check. Observed by AC2, AC3 and AC11.
- **S7** — The hygiene engine prints `gotchas.py --check`'s output on a green run too, as it already
  does for `corpus_ids.py` and `row_grammar.py`. Otherwise S6's announcement would never reach a
  reader. Observed by AC3.
- **S8** — `tools/workflows/tier2-review.template.js` handles a string `checklist` carrying an I4
  block. It cuts the block out before `parseChecklist()`, so no by-design line is ever swept as a
  bug class. `byDesign` becomes the caller's `args.byDesign` when one is supplied, then the block's
  entries, each source under its own label, so a caller's tracked-issue list never displaces the
  invariants. It refuses a block whose header count disagrees with its entry lines. It reads a
  remainder made only of `# ` header lines as zero items, rather than refusing it. It logs each
  by-design source it used with its count, and the RUN INTEGRITY block states them. Observed by AC6
  and AC7.
- **S9** — The spec-audit stage of `tools/workflows/unattended-build.template.js` gets a checklist.
  Its subject-resolver agent also runs the kit's `gotchas.py --for-paths` over every path in the
  subjects' `### Files touched` sub-heads. It returns that stdout verbatim with the paths it passed,
  and the stage forwards the stdout to the audit as `checklist`. A resolver that returns none
  produces a `WARNING:` line naming the gap. Observed by AC8.
- **S10** — At least three invariant records are seeded from `memory/DECISIONS.md` rulings, each
  checked against the code it describes at the pass's HEAD. The first three candidates in §4
  "Seeds" are tried in order, then the fallbacks. Each seed is claimed under `gotcha-classes` by the
  dossier that owns its anchors, and the map's generated artifacts are re-rendered. Observed by AC9
  and AC10.
- **S11** — The rule documents state the new kind and the block: the HYGIENE template and its render,
  the memory-tree README's `gotchas.py` row, the workflows README's `checklist` section, and the
  harness's `args` header and its `byDesign` comment. Observed by AC7 and AC11.
- **S12** — The memory-tree, review-harness and unattended-build kit versions are bumped once,
  after the last move. The kickoff manifest is re-stamped, because the unit edits three watched
  files. Observed by AC12.

## 3. Non-goals (OUT)

- **No new gate leg.** The arms live inside check 18 and check 19 of `memory hygiene` and inside the
  existing self-tests (shared invariant 5).
- **No by-design block in the array form of `checklist`.** An array caller has already split its
  items. The header comment says the block is read from the string form only.
- **No `universal` invariant.** A by-design line on every review would skip the selection and the
  universal budget.
- **No edit to BUILD-METHOD M8's invocation block** (shared invariant 10). The closing review already
  passes the `--for-diff` output as its checklist, and the block rides inside it.
- **No change to the per-pass child's prompt.** `tools/workflows/unattended-unit.js` already tells the
  child to run `--for-diff HEAD~1..HEAD`, and the block now appears in that output.
- **No content-duplicate or near-match grading of the seeds.** Units 6 and 9 own those checks.
- **No `superseded` gotcha handling.** Zero records of that kind exist (`INDEX.md`: `0 superseded`).

### Edges

none

## 4. Design

### Data model — the invariant record (I5)

```markdown
---
name: canary-waits-on-a-rendezvous-not-a-clock
description: the run-gates canary never compares elapsed times, and that is the ruling, not a gap
kind: invariant
decision: TOOL-cSteadyMetronome-1
---

## Looks wrong
The canary never compares a serial run's elapsed time with a concurrent run's.

## Actually
It counts the peers announced at once, because a clock measures the node and not the runner.

## Do
Grade concurrency by the rendezvous peak in `tools/run-gates/run-gates.test.sh`.

## Do not
Reintroduce an elapsed-time ratio or an interval intersection.

## Guarded by
`run-gates canary`
```

Front matter stays at column 0, which the parser already enforces. `decision:` holds exactly one id.
Each section's first paragraph, squeezed to one line, is what the block prints. Prose may follow the
first line of `## Guarded by`, which is the only line graded.

### The by-design block (I4)

```text
# recurring-bug-class checklist for tools/run-gates/run-gates.test.sh (1 file(s))
# 4 class(es) selected by an anchor + 6 universal
- [ ] ...
# by design — 1 invariant(s) this selection touches
- canary-waits-on-a-rendezvous-not-a-clock — The canary never compares a serial run's elapsed time with a concurrent run's. → It counts the peers announced at once, because a clock measures the node and not the runner. (TOOL-cSteadyMetronome-1)
```

The header line is printed whenever the selection is non-empty, `0` included. That way a reader can
tell "no invariant touched" apart from "a kit that predates the block". The early-return messages,
`touches no file` and `selects no file`, print no block. `→` is U+2192, which cp1252 cannot encode,
so S4 sets stdout to UTF-8 explicitly. On node `a` a piped stdout reports `utf-8` only because
`PYTHONUTF8=1` is set (measured 2026-10-04, Python 3.14.6, `sys.flags.utf8_mode` 1). On a node
without that variable, a piped stdout would use the locale codec, and that is UNVERIFIED there. AC4
reproduces the condition by forcing `PYTHONIOENCODING=cp1252`.

### Grading — what check 18 and check 19 assert of an invariant

| arm | finding | reads |
|---|---|---|
| decision resolves | `decision:` absent, or not in the defined-id set | `corpus_ids` walk, imported through `importlib` like `append_only_re()` already does |
| sections present | any of the five headings absent or empty | the record body |
| guard resolves | first line of `## Guarded by` is neither `no machine gate` nor a run of resolving backticked tokens | `git ls-files` (already loaded) and the `LEG_MANIFEST` JSON's `name` fields |
| anchored | no derived anchor | `ANCHOR_RE`, as for a class |
| not inert | every reachable path is append-only | `inert_only()`, as for a class |
| not universal | `universal: true` | front matter |

Two announcements, printed at exit 0, never red. The first: `LEG_MANIFEST` is blank and a guard
token is not a tracked path. The second: the defined-id set cannot be derived because the id
grammar's kit is absent, since `corpus_ids` raises its own named problem then. Both print as
`gotchas: … NOT resolved — <why>`. S7 is what lets them reach a reader. A set `LEG_MANIFEST` naming
an unreadable file is a named `HYGIENE` failure, never a traceback.

Cost, PINNED on node `a` at `89bcefc8`: `gotchas.py --check` takes 5.3 s today, and
`corpus_ids.py --print-defined-ids` takes 2.8 s as a process. The walk runs only when at least one
invariant record exists, so the check rises by roughly the walk, inside a leg whose ceiling is
12720 s. `--for-paths` and `--for-diff` resolve nothing, and they stay at 0.3 s.

### The harness — reading I4 out of `checklist`

`extractByDesign(text)` is a top-level function in the template, evaluated before `parseChecklist()`:

1. It runs only when `a.checklist` is a string. It finds the line
   `# by design — <n> invariant(s) this selection touches`.
2. The block's entries are the following lines that open with `- `, blank lines skipped. The block
   ends at the first other line or at the end of the string.
3. When `<n>` is not the number of entries, the run refuses before any agent spawns, and the message
   names both numbers.
4. The remainder, which is everything outside the block, goes to `parseChecklist()`. When every
   non-blank line of it opens with `# `, it parses as zero items and logs `supplied with no item`,
   instead of taking the non-blank-string refusal. That refusal still covers prose with no item.
5. `byDesign` is the concatenation of two labelled parts, each present only when non-empty: the
   caller's `a.byDesign` under `Known and tracked — do not re-report:`, then the entries,
   newline-joined, under `Intended behaviour — invariants this change touches:`. With neither it is
   `none supplied`. The two inputs differ: the args contract defines `byDesign` as known and
   tracked issues (`tools/workflows/tier2-review.template.js:76`), and an invariant is intended
   behaviour, so neither replaces the other.

Log lines, one per run, name each source and its count: `by-design: the caller's byDesign`,
`by-design: <n> invariant(s) from the checklist's by-design block`, both when both are present, or
`by-design: none supplied — no caller byDesign and <no block | a block of 0>`. RUN INTEGRITY gains a
`By design:` clause carrying the same words. The review key already fingerprints `byDesign` and the
parsed `checklist`. Both are now computed after extraction, so the key reads what the lenses read.
`REVIEW_SHAPE` is bumped only if the pass changes a lens or skeptic prompt's bytes for an input whose
parsed checklist and resolved `byDesign` are unchanged, which is that constant's own rule.

### The spec-audit route

Measured over the tracked review records on 2026-10-04: 0 of 247 `spec-audit` records carry a
RUN INTEGRITY `Checklist:` line, and 4 closing diff reviews do. 14 of 464 review records name a
hand-typed by-design input. So the checklist route reaches the closing review, which the main loop
feeds per M8, and never reaches the spec audit. The harnessed audit's call to `tier2-review.js`
(`tools/workflows/unattended-build.template.js:840-854`) passes `kind`, `repo`, `round`,
`reviewDir` and `subjects`, and nothing else.

The resolver agent (`tools/workflows/unattended-build.template.js:778-787`) already runs git in the
repo for each spec. It gains one instruction. It collects every backticked path token under each
subject's `### Files touched` sub-head, in either spelling. It runs
`python {{MEMORY_TREE_DIR}}/gotchas.py --for-paths <those paths>`, which is the render token the
stage's `CHECKLIST` constant already uses, so invariant 2 holds. It returns the stdout verbatim as
`checklist` and the paths as `checklistPaths`. Both fields are optional in `SUBJECTS_SCHEMA`, so a
caller-supplied subject set and the suite's stubs keep working. The stage logs
`audit round <n>: checklist from --for-paths over <k> path(s)` when the field is present, and a
`WARNING:` line otherwise. A caller-supplied `checklist` argument wins over the resolver's, which
matches the existing rule for `subjects`.

### Seeds — candidates, the check each passed, and the ones rejected

Primary seeds, in the order tried. Each verification command is re-run at the pass's HEAD, and its
output goes into the ledger.

| ruling | record | anchors | guard | verified at writing by |
|---|---|---|---|---|
| `TOOL-cSteadyMetronome-1` | `canary-waits-on-a-rendezvous-not-a-clock.md` | `tools/run-gates/run-gates.test.sh` | `run-gates canary` | `git grep -n "a fact about the NODE" -- tools/run-gates/run-gates.test.sh`; a spec audit's F18 (aPacedTurnstile review) caught a spec re-proposing the refuted interval form |
| `TOOL-aPooledSweep-1` | `sweep-issues-no-cost-verdict.md` | `tools/run-gates/run-selftests.sh` | `run-selftests self-test` | `git grep -n "TOOL-aPooledSweep-1" -- tools/run-gates/run-selftests.sh` (603, 854) |
| `TOOL-aUnblockedFleet-1` | `concurrent-runs-are-announced-not-refused.md` | `tools/unattended/unattended.sh` | `tools/unattended/unattended.test.sh`, whose arm at line 695 pins the announcement; no bar leg runs that suite, so the guard names the file | `git grep -n "ANNOUNCED, NEVER REFUSED" -- tools/unattended/unattended.sh` (2180); the aDeferredBar spec audit's L5 caught a spec asserting the retired one-live-run rule |

The third seed is checked after unit 1 lands, because unit 1 adds a same-slug claim refusal to
`tools/unattended/`. A same-slug refusal is not what `TOOL-aUnblockedFleet-1` retired, since that
ruling covers runs of different builds. The record says so in its `## Actually`. If unit 1 rewrote
the cited comment, the seed fails its check and the next fallback is taken.

Fallbacks, in order: `TOOL-dHonouredPark-3` (the dead-path waiver keys on line text plus an
ordinal, not a line number) and `TOOL-cSpliceWarden-6` (a mode check delegates to the grammar's
owner).

Rejected at writing, with the test that rejected each:

- `PLAY-aCandidStub-1` has the strongest reviewer evidence: seven of nineteen refutations in one
  review. Its premise, "the kit is Optional", is false at HEAD. The charter template's §5 opens the
  memory-tree bullet with `Required — a structured, machine-linted memory tree`.
- `TOOL-aBoundedVerdict-2` says "never a new phase". At HEAD, `tools/unattended/unattended.sh:5145`
  branches on a non-terminal `HELD` phase.

### Inventory

| identifier | where | cell |
|---|---|---|
| `parse_sections` | `gotchas.py` | `py.function` |
| `check_invariant` | `gotchas.py` | `py.function` |
| `render_by_design` | `gotchas.py` | `py.function` |
| `load_defined_ids` | `gotchas.py` | `py.function` |
| `load_leg_names` | `gotchas.py` | `py.function` |
| `BY_DESIGN_HEAD` | `gotchas.py` | constant |
| `INVARIANT_SECTIONS`, `GUARD_TOKEN_RE` | `gotchas.py` | constant |
| `build_invariant`, `build_tree` | `gotchas.py`, nested in `cmd_selftest` | `py.function` |
| `extractByDesign` | `tier2-review.template.js` | `js.function` |
| `LEG_MANIFEST` | `.memory-tree.conf` and the shipped example | conf (dark) |
| `checklist`, `checklistPaths` | `SUBJECTS_SCHEMA` fields | n/a |

Each function name above was asked of `python tools/lexicon/lexicon.py --suggest <name> --as <cell>`
on 2026-10-04 and answered OK; the two self-test helpers were asked on 2026-10-05 and answered OK.
The new map keys are the seeds' basenames, claimed under `gotcha-classes`. The two
`tools/run-gates/` seeds go to the run-gates dossier. The `tools/unattended/` seed goes to the
unattended-mandate dossier, whose globs also own `tools/unattended/unattended.sh`: the unattended
dossier measured 20478 bytes against its 20480-byte `DOSSIER_CAP_BYTES` at the build pass's base,
so one more claim there reds check 6, and the ruling is a preflight rule, which is that dossier's
seam.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `tools/memory-tree/ANNOTATION-STYLE.template.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `tools/memory-tree/README.md`
- `tools/memory-tree/.memory-tree.conf.example`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/README.md`
- `memory/HYGIENE.md`
- `memory/TEMPLATE-SPEC.md`
- `memory/guides/ANNOTATION-STYLE.md`
- `memory/guides/BUILD-METHOD.md`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/gotchas/INDEX.md`
- `memory/map/features/run-gates.md`
- `memory/map/features/unattended-mandate.md`
- `memory/map/features/review-harnesses.md`
- `memory/map/generated/`
- `.memory-tree.conf`

The seed records themselves are three new files under `memory/gotchas/`.

### Rollout

1. Edit the templates and sources, then render. `adopt-memory-tree.sh --render` renders the four
   memory-tree documents. The workflows kit's parity script renders the two harnesses in its
   `--render` mode. `gotchas.py --write` renders `INDEX.md`, and `gen_map.py --write` renders the map.
2. Bump the versions once, after the last move. memory-tree is `2.118` today, in the engine
   constant and in a marker on each of its four templates and four renders. review-harness and
   tier2-review are both `1.28`, on one template line. unattended-build is `1.2`. The re-render
   changes `memory/guides/BUILD-METHOD.md`'s first line only (§8 F1).
3. Re-stamp the kickoff manifest's `last-audit`, because the unit touches
   `tools/memory-tree/check-memory-hygiene.sh`, `.memory-tree.conf` and that marker line, which are
   all in its `watch:`.

### Alternatives rejected

- **An authored invariants table, as helixir keeps one.** It would need either a second path
  selector or emitting every row on every review. It would also be a shared mutable index every node
  edits, which the charter's §5 forbids. The catalogue already has derived anchors and one selector.
- **Leaving `byDesign` to the caller per call.** Measured: 14 of 464 review records carry a
  hand-typed by-design input, and 0 of 247 spec audits do. A per-call input reaches 3% of reviews.
- **A `--for-specs` verb on `gotchas.py`.** It would need a second parser for the `### Files touched`
  sub-head, whose only reader today is `tools/check-spec-tokens.py`, a repo-root tool that does not
  ship. That is two parsers for one grammar (§8 F2).
- **Resolving `decision:` against `memory/DECISIONS.md` row heads only.** That would be a third id
  grammar beside `extract.py`'s and `corpus_ids.py`'s. The defined set already exists, and it also
  admits a ruling recorded as a spec.
- **ASCII `->` in the block.** I4 pins `→`. Setting stdout's encoding is one line, and it keeps the
  pinned interface.

## 5. Production-readiness checklist

- security — N/A for authority: the block is repository content of the same trust as the checklist
  that already reaches the prompt. A caller's `byDesign` is kept whole and labelled ahead of the
  block, so a block cannot override an explicit instruction, and the instruction cannot erase the
  invariants.
- perf / scale — one corpus walk per `--check` while any invariant exists, about 2.8 s on node `a`.
  The checklist verbs are unchanged. Each invariant costs one line in the brief of the lenses whose
  selection touches it.
- error / empty / loading states — a header-only remainder is zero items, logged. A count mismatch
  refuses. A missing block, or a block of 0, logs `none supplied` with its reason. A missing grammar
  or a blank manifest key is announced, never silent.
- observability — the harness's log line and the RUN INTEGRITY `By design:` clause. The audit
  stage's checklist line or `WARNING:`. Hygiene's green-run output. The `--report` and `INDEX.md`
  counts.
- risks — a seed whose ruling drifts from the code would refute a real finding. Every seed carries a
  `## Guarded by` that resolves. A resolver agent could return altered stdout; the header-count check
  catches truncation, and the stdout has the same trust as the blob it already returns.
- testing — new arms in `gotchas.py --selftest`, in the harness self-test and in the build-harness
  self-test, each observed red on a staged break (shared invariant 6).
- migration — none. Existing records keep their kinds, and a string checklist with no block parses
  exactly as at base.
- user docs — HYGIENE's catalogue section, the memory-tree README row and the workflows README's
  `checklist` paragraph.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --for-paths tools/run-gates/run-gates.test.sh`
  runs on the built tree, its stdout ends with `# by design — 1 invariant(s) this selection touches`
  and one `- ` line ending `(TOOL-cSteadyMetronome-1)`.
  Red when: the block is absent, its count disagrees with its lines, or the seed's anchor does not
  select the file.
  figure: PINNED at 1 for this path at the pass's HEAD; a later invariant anchored on the same
  basename raises it.
- **AC2** — When `python tools/memory-tree/gotchas.py --selftest` runs, it prints `PASS` with arms
  for: the block on a hit, the `0` header on a miss, an unresolved `decision:`, a missing section, an
  unresolved guard path, a leg name resolved through a fixture `LEG_MANIFEST`, the blank-key
  announcement, an unanchored invariant, a `universal` invariant, an invariant whose only anchor
  resolves to an append-only path, a set `LEG_MANIFEST` naming a missing file, which prints a
  `HYGIENE` line and no traceback, and an absent id-grammar kit, which prints `NOT resolved` and
  exits 0. Each arm was observed FAIL once, with its predicate disabled in the working tree, the
  inert-only arm with `inert_only()` disabled, before it landed.
  Red when: an arm passes with its predicate disabled, or an invariant anchored only on the
  decision log passes check 19.
- **AC3** — When one seed's `decision:` is changed in the working tree to an id no record defines,
  `python tools/memory-tree/gotchas.py --check` exits 1 and prints `HYGIENE check 18` naming that
  record and that id. Restored, it exits 0. When `LEG_MANIFEST` is blanked in `.memory-tree.conf`,
  the same command exits 0 and prints the `NOT resolved` announcement for each seed's leg-name guard.
  The engine's call site at `tools/memory-tree/check-memory-hygiene.sh:2461` prints a green run's
  output, and the memory-hygiene self-test carries the arm for that.
  Red when: an unresolved decision passes, or the announcement is missing or reds the check.
  permission: the engine-level arm is a self-test this pass does not run; the main loop runs it at
  VERIFYING.
- **AC4** — When `PYTHONUTF8=0 PYTHONIOENCODING=cp1252 python tools/memory-tree/gotchas.py --for-paths tools/run-gates/run-gates.test.sh`
  runs, it exits 0 and its output decoded as UTF-8 contains `→`.
  Red when: the UTF-8 line is removed and the run raises `UnicodeEncodeError`.
- **AC5** — When `python tools/memory-tree/gotchas.py --report` runs, it prints an invariant count
  equal to the number of seeds. `memory/gotchas/INDEX.md`'s summary line carries the same count, and
  `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: the counts disagree, or `INDEX.md` is stale.
  figure: DERIVED from the catalogue at observation.
- **AC6** — When a scratch `node` probe evaluates the prelude of the rendered
  `tools/workflows/tier2-review.js`, the same extraction the harness self-test performs, it runs with
  AC1's stdout as `checklist`. It then logs `by-design: 1 invariant(s) from the checklist's by-design
  block`, and no parsed checklist item opens with the seed's name. The synthesis prompt, sliced the
  way the harness self-test already slices it for RUN INTEGRITY, carries
  `By design: 1 invariant(s) from the checklist's by-design block`. Given `byDesign: 'x'`, it logs
  both sources, the resolved `byDesign` carries `x` and the seed's entry under their two labels, the
  RUN INTEGRITY clause names both, and the items still exclude the block. Given a header claiming 2
  over one entry, it refuses and names both numbers. Given a remainder of header lines only, it
  parses zero items without refusing.
  Red when: a by-design entry is counted as a checklist item, a mismatch proceeds, a caller's
  `byDesign` drops the invariants, or RUN INTEGRITY omits or misstates a source.
- **AC7** — When the workflows kit's renderer runs in its render mode,
  `git status --porcelain tools/workflows/` prints nothing new, so the render equals the template.
  The RUN INTEGRITY clause is observed in AC6's sliced prompt, not by a source grep, which any
  comment would satisfy.
  Red when: the render was edited by hand.
- **AC8** — When a scratch `node` probe evaluates the rendered `tools/workflows/unattended-build.js`
  the way the build-harness self-test does, it uses a stub resolver returning subjects plus a
  `checklist`. The stub `workflow()` then records spec-audit args whose `checklist` equals the stub's
  string. With the field absent, a `WARNING:` line names the missing checklist and no `checklist` key
  is passed. Given a caller `checklist` argument beside the resolver's, the audit receives the
  caller's. The rendered resolver prompt in `tools/workflows/unattended-build.js` names
  `gotchas.py --for-paths` through the rendered memory-tree path, and names `### Files touched`.
  Red when: the audit call drops the resolver's checklist, its absence is silent, the resolver's
  overrides the caller's, or the prompt carries no instruction to run `--for-paths`, which a stub
  resolver alone cannot see.
  permission: the permanent arm lives in the build-harness self-test, which the main loop runs at
  VERIFYING.
- **AC9** — When `python tools/memory-tree/gotchas.py --report` runs, at least three `invariant`
  rows appear. Each seed's verification `git grep` from §4, re-run at the pass's HEAD, prints at
  least one line, and the ledger records each command with its output.
  Red when: a seed is kept whose ruling the code no longer states.
- **AC10** — When `python tools/codebase-map/test_codebase_map.py` runs, every line reads `ok`. The
  seeds' basenames are then claimed and `generated/` is fresh.
  Red when: a seed's basename is unclaimed, or the map was not re-rendered.
- **AC11** — When `grep -c "kind: invariant" memory/HYGIENE.md tools/memory-tree/README.md` runs,
  each file counts at least 1. When `grep -c "by design —" tools/workflows/README.md` runs, it
  prints at least 1. When `grep -c "supplied by no caller anywhere in the tree" tools/workflows/tier2-review.js`
  runs, it prints 0. `grep -n '^LEG_MANIFEST=""' tools/memory-tree/.memory-tree.conf.example`
  prints one line.
  Red when: a rule document still describes the catalogue as classes, notes and superseded only,
  the harness still states that nothing fills `byDesign`, or the example conf ships a manifest path
  an adopter may lack.
- **AC12** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs, its
  `memory-tree` and `review-harness` lines read `clean` at the bumped versions.
  `git diff <the pass's parent sha> -- memory/guides/BUILD-METHOD.md` changes line 1 only.
  `bash skills/session-kickoff/manifest-check.sh` exits 0.
  Red when: a carrier keeps the old version, BUILD-METHOD content moved, or the manifest stamp is
  stale.

## 7. Gates

`memory hygiene` · `gotchas selftest` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms`

New arm: tools/memory-tree/gotchas.py · each invariant predicate disabled in the working tree · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · the green-run print at the gotchas call site deleted · none
New arm: tools/workflows/tier2-review.test.sh · extraction disabled, so a by-design entry lands in the items · the suite's assertion floor, raised by the arms added
New arm: tools/workflows/unattended-build.test.sh · the resolver's checklist not forwarded · the suite's assertion floor, raised by the arms added
New arm: tools/workflows/tier2-review.test.sh · the RUN INTEGRITY slice carrying each by-design source, and a caller byDesign beside a block; stage the clause deleted and the caller's value made to replace the block · the suite's assertion floor, raised by the arms added
New arm: tools/workflows/unattended-build.test.sh · a caller checklist beside the resolver's, and the rendered resolver prompt's --for-paths instruction; stage the precedence reversed and the instruction deleted · the suite's assertion floor, raised by the arms added

## 8. Open questions

- **F1 — Does re-rendering the memory-tree version marker on `memory/guides/BUILD-METHOD.md` breach
  shared invariant 10, which says no unit edits that file?**
  Option A: bump memory-tree everywhere, accepting that line 1 of `BUILD-METHOD.md` moves. Option B:
  leave that marker stale, which reds `kit version markers` and breaks shared invariant 4. Option C:
  do not touch the memory-tree kit, which loses S1-S7. The marker is a derived carrier of the kit
  version, and `check-kit-versions.sh` pairs it with the engine constant. Invariant 10 protects the
  method's content, which the render leaves byte-identical below line 1. A is the only option that
  satisfies both invariants as they are meant, and AC12 observes that only line 1 moved.
  RESOLVED (agent, 2026-10-04, delegated): A, with AC12's line-1 diff as the observation.
- **F2 — How does the spec audit get a checklist: from paths the resolver agent extracts and hands to
  `--for-paths`, from a new deterministic `--for-specs` verb, or not at all?**
  The new verb is deterministic, but it adds a public CLI surface and a second parser of a sub-head
  whose only reader is a gov-only repo-root tool (M3 veto 2 on the surface). Leaving the audit
  without a checklist fails the brief's instruction that the route reach both reviews. The resolver
  route uses the existing verb and the agent the stage already runs. It returns the paths it passed,
  so the selection is auditable in the log.
  RESOLVED (agent, 2026-10-04, delegated): the resolver route, as S9 states.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 3 section and pinned interfaces I4
  and I5. Grounded against `gotchas.py`, the two workflow templates and the hygiene call site at
  `89bcefc8`.
- rev-2 · 2026-10-04 · §4 §5 §6 §7 · S6 S8 · AC2 AC6 AC7 AC8 AC11 · folded the round-1 spec audit's
  findings on this unit: 50 (a caller's `byDesign` and the block are concatenated under two labels
  rather than one replacing the other, §4 step 5, §5 security, AC6); 12 (RUN INTEGRITY's by-design
  source is observed in AC6's sliced synthesis prompt, and AC7's source grep is dropped); 13 (AC8
  observes the rendered resolver prompt and the caller-checklist precedence); 14 (AC2's inert-only
  invariant arm); and 15 (AC2's missing-manifest and absent-grammar arms, and AC11's example-conf
  grep).
- rev-3 · 2026-10-05 · §4 · the build pass's divergences, before the code. The `tools/unattended/`
  seed is claimed by the unattended-mandate dossier rather than the unattended one, which sat two
  bytes under its 20480-byte dossier cap, and Files touched names that dossier in place of the
  unattended one. The Inventory gains the two constants the grading reads (`INVARIANT_SECTIONS`,
  `GUARD_TOKEN_RE`) and the two nested self-test helpers.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "select catalogue records whose path anchors intersect a changed file"`
ranked `records` in `tools/memory-tree/gotchas.py` first (fan-in 8, SEAM), with `anchor_at` and
`corpus_files` behind it. A second probe, `"hand reviewers the intentional behaviour they must not
report as a bug"`, returned only name-stem noise. The probe prints `unscanned layers: .sh`, so the
hygiene call site was read by hand. Extended: `records()`, `selectable()`, `inert_only()`,
`cmd_check()` and `cmd_for_paths()` in `gotchas.py`; the defined-id walk in `corpus_ids.py`, reached
the way `append_only_re()` already reaches it; `parseChecklist()` and the `byDesign` constant in
`tools/workflows/tier2-review.template.js`; and the subject-resolver agent in
`tools/workflows/unattended-build.template.js`. Recall surfaced `TOOL-aBoundedVerdict-14`, which
keeps `priorFindings` apart from `byDesign`. This unit keeps them apart too: an invariant is
intended behaviour, and a prior finding is a fixed defect. It also surfaced `TOOL-aSightedSkeptic-1`,
which already hands `byDesign` to every skeptic, so this unit adds no skeptic plumbing. And it
surfaced `TOOL-aWeighedCompass-14`, a measurement that `--for-paths tools/` selects most of the
catalogue. That is why the spec-audit route passes the Files-touched paths and never a tool root.

Recall terms used: byDesign by-design tier2-review refuted skeptic gotcha catalogue invariant checklist priorFindings lens intended

The question passed with them: "why is byDesign supplied by no caller and what should a reviewer be told is intentional".
