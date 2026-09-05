# TOOL-aHoistedPass-4 — the loop ban learns the two spellings that walk past it

**Status:** SPECCED · rev-3 · 2026-09-05 · node a · Tier-1 · base c4fcf5ad · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md](../build/2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md) | research | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/agent-cap.js` denies an `agent()` call inside a loop, and two loop spellings walk
straight past the predicate that finds the loop. Teach all six predicate sites the two spellings, in
one commit, so the ban covers the class rather than the two shapes somebody happened to write first.

## 2. Scope (IN)

**S1, S2 and S3 LANDED WITHOUT THIS UNIT, between this spec's base and the run's BASE `e828f778`,
under `TOOL-aWeldedTribunal-1`.** They are kept below as written rather than rewritten, because a
scope item edited to match what shipped stops recording that the two differ. What this unit owes for
them is a VERIFICATION at BASE and nothing else; what it BUILDS is S4, S5 and S6, none of which
landed. Section 9's rev-2 row carries the observation and the exact anchors.

- **S1** — ~~Replace the six inline loop-opener literals in `tools/hooks/agent-cap.js` with two named
  constants, `LOOP_HEAD` and `LOOP_TAIL`~~ — **LANDED, and better than specified**: THREE forms, not
  two, at `tools/hooks/agent-cap.js:476-479`. `LOOP_KEYWORDS` holds the keyword set once;
  `LOOP_HEADER`, `LOOP_HEADER_G` and `LOOP_KEYWORD_TAIL` derive from it. The third form exists
  because the opener walk tests the text BEFORE a paren, where a pattern ending in `\(` can never
  match — a distinction this spec's two-constant design did not make.
- **S2** — ~~Both constants recognise `for await (`; `LOOP_HEAD` also recognises a `do {` block
  opener.~~ — **LANDED.** `for(?:\s+await)?|while` plus a `\bdo\s*\{` alternation, with the `do`
  spelling deliberately absent from the tail form because a `do` block opens with a brace.
- **S3** — ~~Arms in BOTH directions in `tools/hooks/agent-cap.test.sh`~~ — **LANDED**, at
  `tools/hooks/agent-cap.test.sh:59-67`: four DENY arms across both walks and a string control
  proving the widened predicate still admits the words inside a string literal.
- **S4** — The mutual-exclusivity note, in the two places a reader extending the slot ledger meets
  it: the RULE 4 comment block at `tools/hooks/agent-cap.js:1214` and the
  `## Direct spawns are COUNTED, not parsed` section at `tools/hooks/README.md:119`.
- **S5** — `KIT_AGENT_CAP_VERSION` 1.12 to 1.13, and every tracked `gov:kit agent-cap@` carrier with
  it. The population is derived by `tools/check-kit-versions.sh:80` and is TWO files today.
- **S6** — Close the backlog row this unit answers, `TOOL-dFoldedVerdict-8` at
  `memory/backlog/TOOL.md:10`.

## 3. Non-goals (OUT)

- **A braceless `do`.** `do await agent(u); while (i++ < n)` is legal JavaScript and stays admitted:
  `LOOP_HEAD` requires the brace. Backlog row, not a unit.
- **A local helper and recursion.** Both remain shapes that reach `agent()` without a loop keyword,
  and neither is closed here. They were already open before this unit and are not made worse by it.
- **`data.cwd` path resolution.** A `scriptPath` that resolves in the wrong tree is a separate
  defect and belongs to whoever takes it.
- **The `braceless` label on a one-line `do { … } while ()`.** The verdict is right and the noun is
  slightly wrong; see §5.
- **Any change to what the hook reads.** This unit widens ONE predicate. It does not make the hook
  read prompts, agent counts, nesting, or the `export const meta` marker.
- **Anything in the hoist.** This unit is independent of `TOOL-aHoistedPass-5` and lands whether or
  not the hoist does.

## 4. Design

### Inventory

Every line below was opened in this worktree at `c4fcf5ad`. `grep -nE 'for\|while' tools/hooks/agent-cap.js`
returns exactly six lines, in three forms, and the design of record's count is correct.

| site | form | what it decides | direction of the widening |
|---|---|---|---|
| `:705` | `\b(for\|while)\s*\(` | C5 of `checkSeqMarker` — the marked line really is a loop header | message correctness |
| `:711` | `\b(?:for\|while)\s*\(/g` | C6 — two openers on one header cannot be attributed | tightens |
| `:738` | `\b(for\|while)\s*\(` | nothing may ENCLOSE a marked loop | tightens |
| `:910` | `\b(for\|while)\s*$` | an `agent()` sitting in the loop's own header expression | tightens |
| `:934` | `\b(for\|while)\s*\(` | a braceless loop body on the call's own line | tightens |
| `:944` | `\b(for\|while)\s*\(` | the enclosing loop found by the brace walk | tightens |

Three of the six sit inside `checkSeqMarker`, which is the `gov:sequential-agents` BLESSING path
rather than the deny path. `TOOL-dFoldedVerdict-8` and the design of record both locate the defect
"in `fanoutFindings`"; `fanoutFindings` calls `checkSeqMarker`, so the widening reaches the blessing
path too, and at `:711` and `:738` that is a tightening rather than a loosening.

### The measurement, taken before anything was designed

Fed to `node tools/hooks/agent-cap.js` as `{"tool_name":"Workflow","tool_input":{"script":"…"}}` on
stdin, with the exit code captured WITHOUT a pipe, at `c4fcf5ad`.

| fixture | exit | output |
|---|---|---|
| `for (const u of units) { await agent(…) }` | **2** | `agent() inside a loop body — a loop-built thunk array is the evasion this rule exists for` |
| `while (i < units.length) { await agent(…) }` | **2** | the same message |
| `for await (const u of units) { await agent(…) }` | **0** | nothing, zero bytes |
| `for await (const u of units) await agent(…)` | **0** | nothing, zero bytes |
| `do { await agent(…); i++ } while (i < units.length)` | **0** | nothing, zero bytes |

A silent exit 0 is what a run sees. There is no partial verdict and no warning channel.

### Data model

Two module-level constants, declared once beside the other file constants.

```js
// The loop-opener predicate, ONE spelling instead of six. `for await (` and a `do { … } while ()`
// block each walked past the six inline literals this replaces, measured at exit 0 with no output.
// A `do` opener is anchored on a non-member prefix so an `obj.do` property is not a loop.
// LOOP_HEAD is NEVER given the `g` flag in place: a shared global regex carries `lastIndex` between
// calls. The one counting site derives a fresh one from `.source`.
const LOOP_HEAD = /\b(?:for(?:\s+await)?|while)\s*\(|(?:^|[^.\w$])do\s*\{/
const LOOP_TAIL = /\b(?:for(?:\s+await)?|while)\s*$/
```

`LOOP_HEAD` replaces the literal at `:705`, `:738`, `:934` and `:944`. `:711` becomes
`(ch.match(new RegExp(LOOP_HEAD.source, 'g')) || []).length > 1`. `LOOP_TAIL` replaces `:910`, with
no `do` arm, because a `do` opener never precedes the paren that site scans for.

The `do` arm matters at `:944` and `:934`. The brace walk at `:939-946` climbs to the line whose
brace opened the block, finds `do {`, and today tests a predicate that line cannot satisfy — the
`while` sits AFTER the closing brace, below the walk. With `LOOP_HEAD` that line matches, `h` is
set, and `checkSeqMarker` returns `''` for an unmarked header, so the call is denied by the existing
`:960-966` branch. No new deny branch is written.

A `do {` header carrying a `gov:sequential-agents` marker is still refused, and by the clause that
already refuses `while`: `:717` requires a `for (const x of <identifier>)` header and a `do` is not
one. The marker path therefore gains a correct refusal message and no new admission.

### The count is the acceptance, not the eye

A five-of-six widening closes three quarters of a hole and reports closed. After this unit the raw
literal `(for|while)` does not appear in `tools/hooks/agent-cap.js` at all, because both constants
spell it `(?:for(?:\s+await)?|while)`. That makes "did every site move" a `grep` rather than a
reading, and §6 asserts it that way.

### The candidate predicate, run over the real tree before wiring

Required by the charter of any new predicate, and it changed the risk assessment rather than
confirming it. Both arms were run over all 1510 tracked files.

- **Hits in tracked `*.js`: ZERO.** `git ls-files -z '*.js' | xargs -0 grep -nE 'for[[:space:]]+await|(^|[^.[:alnum:]_$])do[[:space:]]*\{'`
  exits 123 with no output over all eight tracked JavaScript files. The widening cannot red an
  existing script, because no existing script contains either spelling.
- **Hits elsewhere: 7 for-await and 6 do-block, every one in markdown**, and every one a record
  DESCRIBING this hole — `memory/backlog/TOOL.md:10` and five files under
  `memory/builds/dFoldedVerdict/`. Markdown is not in the hook's population.
- **Near-misses, `do` as an ordinary English word: 2165 lines.** All markdown, and all excluded by
  the `do\s*\{` requirement rather than by the population. The `[^.\w$]` prefix is what keeps an
  `obj.do({…})` call out; no tracked file contains one today, so that guard is written against the
  class rather than against an instance.
- **Near-misses, `for await` without its paren: 3 lines**, all markdown prose.

So the widening's false-positive risk over this tree is measured at zero, and the false-positive
GUARD is unexercised by anything in the tree. That is what the control arms in S3 are for.

### The mutual-exclusivity note

`guardAgentSpawn` claims a numbered slot per session and prompt against `MAX_VERIFIERS`
(`agent-cap.js:403`) and is reached only on an `Agent` payload (`:1494-1499`). The hoisted build
shape makes one `Workflow` call per roster unit from a single prompt. A slot ledger extended to
`Workflow` calls would therefore deny such a build partway through its own roster, on a budget that
was written for a burst of verifiers.

The note states that structure and names no figure. Two reasons. A roster distribution restated in a
hook comment rots on the next build, which is the rule this repo keeps breaking. And the hooks kit's
own authoring rule (`tools/hooks/README.md:134`) forbids a kit file naming anything outside itself
by literal, so the note may cite neither the harness path nor the record that measured the rosters.

It lands in two carriers, because a reader arrives from either direction. The RULE 4 comment block
at `:1214` is where the ledger's own design is argued. `## Direct spawns are COUNTED, not parsed`
at `tools/hooks/README.md:119` is where a reader asking "why not count Workflow too?" arrives first.

### Migration

None. The hook is stateless per invocation, no on-disk format moves, and the slot directories are
untouched. A revert is the same two constants going back to six literals.

### Files touched (estimate)

| file | what |
|---|---|
| `tools/hooks/agent-cap.js` | the two constants, the six sites, the RULE 4 note, `KIT_AGENT_CAP_VERSION` and its same-line marker |
| `tools/hooks/scratch-guard.js` | its `gov:kit agent-cap@` marker alone; `KIT_SCRATCH_GUARD_VERSION` is its own and does not move |
| `tools/hooks/agent-cap.test.sh` | four DENY arms, three control arms |
| `tools/hooks/README.md` | the note under `## Direct spawns are COUNTED, not parsed` |
| `memory/backlog/TOOL.md` | `TOOL-dFoldedVerdict-8` to CLOSED |

No map artifact moves. `JS_DEFINITION_RULES` (`tools/codebase-map/map_lib.py:405-415`) indexes a
`const` only when its right-hand side is a function, an arrow or a class, so a regex constant is not
a symbol and `memory/map/generated/symbols.json` gains no row.

### Alternatives rejected

- **Six one-line edits, no constants.** Shorter to write and it re-creates the defect: the next
  spelling has to be added six times, and a five-of-six pass is invisible.
- **A third constant for the `g` flag at `:711`.** Two literals that must stay identical is the
  drift this unit exists to remove. `new RegExp(LOOP_HEAD.source, 'g')` derives it at the one call
  site and is stateless.
- **Rewording the `braceless` deny message so it reads correctly for a one-line `do {}`.** Cosmetic,
  and it churns text that self-test arms assert against. Disclosed in §5 instead.
- **Extending the slot ledger to `Workflow` instead of widening the script predicate.** It is the
  option the note exists to warn against, and it is a different unit's decision either way.

## 5. Production-readiness checklist

- **security** — This is a guard against an expensive fan-out, not a trust boundary. Widening it
  cannot admit anything it admits today; every arm either denies more or reports a truer reason.
- **perf / scale** — One `new RegExp` construction per `agent()`-bearing line at `:711`, on a hook
  that runs once per tool call. Not measured, and not worth measuring at that rate.
- **a11y** — N/A — a stdin-to-exit-code hook with no interface.
- **i18n** — N/A — the predicate reads JavaScript keywords, which are not translated.
- **error / empty / loading states** — A one-line `do { await agent(u) } while (c)` is denied with
  the message that says `braceless`, which is the wrong noun for a braced one-liner. The verdict is
  correct and the remedy text still applies. Not fixed here, and stated so nobody reports it as new.
- **observability** — None added. The hook's only channels are its exit code and stderr, and a pass
  is silent by design.
- **risks (concurrency, data-loss, rollback hazards)** — The `g`-flag `lastIndex` footgun is the one
  real hazard, and it is removed by construction rather than by comment: no global regex is stored.
  Rollback is a revert of one file.
- **testing + left-shift gates** — Four DENY arms and three control arms in
  `tools/hooks/agent-cap.test.sh`, staged RED before the widening lands. §7 states plainly which
  boundary runs them, because none does.
- **migration / rollback** — N/A — no state, no format, no adopter action beyond the version bump.
- **user docs** — `tools/hooks/README.md` gains the mutual-exclusivity note. The DENIES section
  needs no change: it already names the loop ban without enumerating spellings.

## 6. Acceptance criteria

**AC1 to AC8 were written for a widening this unit no longer builds, and are REWRITTEN here rather
than left standing.** Leaving them would be the `amendment-leaves-its-other-half-standing` class the
checklist selected for this very commit: the scope items were struck at rev-2 and these criteria
still demanded the struck work, one of them (old AC5) naming symbols that do not exist and asserting
a count that cannot be reached. What replaces them is VERIFICATION at the run's BASE, which is what
section 2 says this unit now owes for S1 to S3.

**The loss, stated rather than papered over.** Old AC6 required the failing case to be observed —
arms staged without the widening, RED, then unstaged. That is unobservable now: the widening is
already in the tree. `TOOL-aWeldedTribunal-1` made that observation and this run did not, so this
unit inherits the arms without inheriting the proof that they can fail. It is written here because a
gate whose failing case nobody in this run has seen is exactly what this repo refuses to call
covered.

- **AC1** — When `tools/hooks/agent-cap.js` is read at the landing BASE, `LOOP_KEYWORDS`,
  `LOOP_HEADER`, `LOOP_HEADER_G` and `LOOP_KEYWORD_TAIL` are declared consecutively at `:476-479`,
  `LOOP_KEYWORDS` is the single source of the keyword set, and the `do` spelling is present in
  `LOOP_HEADER` and `LOOP_HEADER_G` and absent from `LOOP_KEYWORD_TAIL`.
- **AC2** — When the four fixtures are fed to `node tools/hooks/agent-cap.js` with the exit code
  captured WITHOUT a pipe, all four exit `2`: the `for await (` thunk array, the `do { … } while ()`
  thunk array, the braceless `for await (const u of units) await agent(…)`, and the inline
  `do { await agent(…) } while (…)`. A pipe returns the pipe's status, which is how the backlog row
  this unit closes came to describe a method that cannot have measured what it reports.
- **AC3** — When the string control is fed to the same hook — the words `for await (x of y)` inside
  a string literal, with a marked bounded fan alongside — it exits `0`. The predicate denies more
  and nothing else.
- **AC4** — When `grep -cE '\(for\|while\)' tools/hooks/agent-cap.js` runs it returns **`1`, not
  `0`**, and the single hit is the comment at `:461` that documents the fix. This is the
  `absence-assertion-over-whole-file-text` class named as such: a ban that greps whole file text reds
  on its own explanation, so the criterion is written to the observed number and not to the
  aspirational one.
- **AC5** — When `bash tools/hooks/agent-cap.test.sh` is run BY HAND at the landing BASE it exits
  `0`, and the four DENY arms plus the string control are present at `:59-67`. Nothing standing
  re-runs this: section 7 states why.
- **AC6** — When `bash tools/workflows/check-verifier-fanout.sh` runs it exits `0` over all eight
  tracked JavaScript files, so no tracked workflow script is denied by the shipped predicate.
- **AC7** — When `git log --oneline -1 -- tools/hooks/agent-cap.js` is read, the landing of S1 to S3
  is attributable to `TOOL-aWeldedTribunal-1` and not to this unit, and this unit's own commit
  touches neither `tools/hooks/agent-cap.js`'s predicate block nor `tools/hooks/agent-cap.test.sh`'s
  arms.
- **AC8** — When this unit's diff is read, the only files it changes under `tools/` are the two the
  residual needs: `tools/hooks/agent-cap.js` (the S4 note and the S5 version constant) and
  `tools/hooks/README.md` (the S4 note). Every other edit is under `memory/`.
- **AC9** — When `git grep -lE "gov:kit agent-cap@" -- '*.js'` runs, every file it names carries
  `1.13`, `KIT_AGENT_CAP_VERSION` reads `1.13`, and `bash tools/check-kit-versions.sh` exits `0`.
  With only one carrier moved it exits non-zero naming the other.
- **AC10** — When `bash tools/check-agent-cap-restatement.sh` runs over the tree carrying the new
  README note, it exits `0`. The note states no bound as a bare number.
- **AC11** — When `bash tools/check-install-prefix.sh` runs, it exits `0` with the
  `tools/hooks/README.md` and `tools/hooks/agent-cap.js` rows of `tools/install-prefix-carried.txt`
  unchanged at `4` and `7`. Neither note spells a path outside its own file.
- **AC12** — When `grep -n "slot ledger" tools/hooks/agent-cap.js tools/hooks/README.md` runs, the
  mutual-exclusivity note is found in the `RULE 4` comment block and under
  `## Direct spawns are COUNTED, not parsed`, in both files.
- **AC13** — When `python3 tools/codebase-map/test_codebase_map.py` and
  `bash tools/memory-tree/check-memory-hygiene.sh` run after the change, both exit `0` with no
  regenerated artifact in the diff.

## 7. Gates

Green on the landing commit: `verifier fan-out`, `agent-cap restatement`, `kit version markers`,
`install-prefix (shipped surface)`, `workflow script syntax`, `codebase-map coverage + freshness`,
`memory hygiene`. Every one of those is chunk `declarations`, `product`, `wiring` or `records` with
subject `repo` and no guard, so every one runs on an ordinary bar.

**The DENY arms are not on any bar, and that is the honest statement of this unit's coverage.** They
live in `tools/hooks/agent-cap.test.sh`, which is the leg `agent-cap self-test` — chunk `selftests`,
subject `kit`, guard `tools/hooks/` and `tools/lib/`. `GATE_FULL=1` holds every `subject = kit` or
`chunk = selftests` leg, and `GATE_SELFTESTS=1` is on demand only with no boundary setting it. So
AC2, AC3, AC4, AC6 and AC7 are observations the RUN makes by executing
`bash tools/hooks/agent-cap.test.sh` by hand and reporting the result. Nothing standing re-checks
them afterwards.

**What the standing legs do cover is over-denial, in one direction only.**
`tools/workflows/check-verifier-fanout.sh` does not re-implement the rule; it feeds each tracked
workflow script to this same hook and reports what the hook says (its header, `:13-17`). Because no
tracked script contains either spelling — measured, zero of eight — that leg can only ever catch the
widening reddening an innocent file. It can never observe either new denial.

This unit adds no gate leg, and at rev-3 it adds no arms either — the arms landed with the widening
under `TOOL-aWeldedTribunal-1`. What it does is RUN that suite by hand at the landing BASE and report
the result, on a kit whose self-tests were taken off the bar by owner ruling on 2026-08-23. The
compensating check is that hand-run, and its weakness is stated in section 6: this run inherits arms
whose failing case it has not itself observed.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against `origin/main` at `c4fcf5ad` in a worktree
  standing at that exact sha, so every line number below was opened locally rather than through a
  blob. Corrections made to the design of record while writing it:
  - **The six sites and their three forms are CONFIRMED, not corrected.** `:705`, `:738`, `:934` and
    `:944` carry `\b(for|while)\s*\(`; `:910` carries `\b(for|while)\s*$`; `:711` carries the `/g`
    form. The design's table is exact.
  - **The backlog row's stated method cannot have measured what it reports.**
    `memory/backlog/TOOL.md:10` records the two admits as measured "by piping the shape to
    `node tools/hooks/agent-cap.js`", and a pipe returns the pipe's status rather than the hook's.
    Re-measured here without a pipe: both verdicts reproduce, so the row's CONCLUSION stands and its
    method does not. Recorded because the same phrasing would mislead the next reader.
  - **"The brace walk in `fanoutFindings`" undersells where the defect lives.** Three of the six
    sites are in `checkSeqMarker`, the marker-blessing path, which `fanoutFindings` calls. Two of
    those three TIGHTEN the blessing path rather than widening the deny path, and the spec says which.
  - **The design's edit set does not name the version-carrier population.** Derived here from
    `tools/check-kit-versions.sh:80`: `git grep -lE "gov:kit agent-cap@" -- '*.js'` returns TWO
    files at this tip, and both must move together. Earlier records in this corpus say four, which
    was true when `.claude/hooks/` copies were tracked.
  - **The design leaves the widening as six edits; this spec collapses them to two constants.** The
    reason is the failure mode the brief names: a five-of-six widening closes three quarters of a
    hole and reports closed. With two constants the completeness check is a `grep` for a literal
    that no longer exists anywhere in the file.
  - **A braceless `do` is named OUT rather than silently covered.** `LOOP_HEAD` requires the brace,
    so `do await agent(u); while (c)` still admits. The design did not mention it.
- rev-2 - 2026-09-05 - **S1, S2 and S3 LANDED WITHOUT THIS UNIT.** Re-derived at the run's
  BASE `e828f778`, 66 commits after this spec's base: `tools/hooks/agent-cap.js:476-479` carries
  `LOOP_KEYWORDS = 'for(?:\s+await)?|while'` with `LOOP_HEADER`, `LOOP_HEADER_G` and
  `LOOP_KEYWORD_TAIL` derived from it, attributed to `TOOL-aWeldedTribunal-1`, and
  `tools/hooks/agent-cap.test.sh:59-67` carries the four DENY arms and the string control S3 asked
  for. That landing is BETTER than this spec's S1: THREE named forms rather than two, because the
  opener walk tests text before a paren and cannot share a pattern ending in `\(`. **What did NOT
  land is S4, S5 and S6** - no mutual-exclusivity note at either site, `KIT_AGENT_CAP_VERSION` still
  `1.12` at `:63`, and `TOOL-dFoldedVerdict-8` still `OPEN` at `memory/backlog/TOOL.md:11`. This unit
  is therefore NARROWED to that residual and to recording the supersession; the M2 route for a
  divergence is to change the spec first, which this row is. Section 8 stays `none`: nothing here is
  a fork.
- rev-3 - 2026-09-05 - the other half of rev-2's amendment, caught by this build's own bug-class
  checklist over rev-2's commit: `amendment-leaves-its-other-half-standing`. Section 2 struck S1 to
  S3 and section 6 still demanded them, so AC1 to AC8 are rewritten to VERIFICATION at the run's
  BASE. Two defects the rewrite had to fix rather than restate. Old AC5 named `LOOP_HEAD` and
  `LOOP_TAIL`, which do not exist - the landed shape is `LOOP_KEYWORDS`, `LOOP_HEADER`,
  `LOOP_HEADER_G` and `LOOP_KEYWORD_TAIL` at `:476-479` - and it asserted
  `grep -cE '\(for\|while\)'` returns 0, which is UNREACHABLE: the comment at `:461` documenting
  the fix carries the literal, so the observed count is 1. That is the
  `absence-assertion-over-whole-file-text` class and AC4 now names it. Old AC6's staged-break is
  recorded as a LOSS rather than dropped silently: this run cannot observe a failing case for arms
  that are already in the tree. Section 7's closing paragraph amended with it.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py "detect a loop header enclosing an agent spawn in a workflow script"`
against a corpus of 645 symbols, 188 inventory keys, 19 affordance seams and 20 dossiers. It surfaced
`guardAgentSpawn` (`tools/hooks/agent-cap.js`) and the two declared seams in
`memory/map/features/agent-cap.md` — `agent-cap.topLevelArgs` at `:216-218` and `agent-cap.boundedK`
at `:219-221`. Verdict, in the sanctioned words: no existing seam fits. One splits source text into
positional arguments, the other resolves a token to an integer bound, and neither detects a loop
header. The thing this unit extends is not a declared seam at all but six copies of one literal
inside `checkSeqMarker` and `fanoutFindings`, and the unit's whole shape is to collapse those six
into two named constants rather than to add a seventh detector. `boundedK` is left untouched and un-called by this change.

Recall terms used: agent-cap, loop ban, fanoutFindings, checkSeqMarker, gov:sequential-agents,
braceless loop body, boundedK, MAX_VERIFIERS, slot ledger, verifier fan-out, for await, do-while,
PreToolUse, kit version markers
