# TOOL-aDeferredBar-2 — the spec gate: a bar or suite invocation is not an acceptance observation

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-2 · base b2a330be · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md](../build/2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md) | research | TOOL-aDeferredBar-1 TOOL-aDeferredBar-3 |
| [2026-09-13-prompt-TOOL-aDeferredBar-2-1-spec-brief.md](../prompts/2026-09-13-prompt-TOOL-aDeferredBar-2-1-spec-brief.md) | journal | — |
| [2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round1.md) | spec-audit | TOOL-aDeferredBar-1 TOOL-aDeferredBar-3 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-spec-tokens.py` gains a fourth join, `bar`: in a live spec dated at or after a new
`.memory-tree.conf` cutoff, a backticked token inside a `## 6. Acceptance criteria` bullet or on the
`## 7. Gates` leg line that spells a merge-bar or self-test-suite invocation is a hit. It refuses
the instruction at the cheapest point — the writer, before any child agent reads it — because the
research record under `build/` traced one unit's 68-minute stall to exactly such a token in its AC8.
Tier-2 by the manifest's tier rule: it changes the spec template's rules and a shipped kit's conf.

## 2. Scope (IN)

- **S1** — The join itself in `tools/check-spec-tokens.py`: the predicate, the two populations it
  reads, the cutoff read through `read_conf_key`, the hit kind `bar`, a refusal text that names the
  substitute, and a report line printed on every run. Observed by AC1, AC2, AC3, AC4, AC5 and AC8.
- **S2** — The module docstring: the population list gains the fourth join and the WHAT IT DOES NOT
  CHECK paragraph gains what this join cannot see. NOT OBSERVED — a sentence in a docstring has no
  command that observes it; the spec audit reads it.
- **S3** — `--list` prints every near-miss of the predicate as a `NEAR` line, exit 0. Observed by
  AC3 and AC9.
- **S4** — The key `SPEC_DIRECT_CUTOFF` in `.memory-tree.conf` at `2026-09-13`, with a register
  comment in the idiom of its neighbours, and a blank row in
  `tools/memory-tree/.memory-tree.conf.example`. Observed by AC8 and AC14.
- **S5** — Seven arms in `tools/check-spec-tokens.test.sh`, and its assertion floor moved to the
  count the suite prints. Observed by AC1 through AC7, each arm's fixture exercised by the direct
  checker; the suite's own verdict is the main loop's at `VERIFYING`, per the build README's rule 6.
- **S6** — One paragraph in `tools/memory-tree/SPEC-TEMPLATE.template.md` under the §6 rules,
  beside the `SPEC_WITNESS_CUTOFF` and `SPEC_FAILURE_MODE_CUTOFF` paragraphs, stating the rule and
  the substitute; rendered to `memory/TEMPLATE-SPEC.md`. Observed by AC10.
- **S7** — The memory-tree version step: `KIT_MEMORY_TREE_VERSION` in
  `tools/memory-tree/check-memory-hygiene.sh` and the `gov:kit memory-tree@` marker on every
  `tools/memory-tree/*.template.md` and every rendered copy, one step past the value unit 1 leaves.
  Observed by AC11.
- **S8** — The kickoff manifest's `last-audit` re-stamp, owed because `.memory-tree.conf` and the
  engine are both on its `watch:` line. Observed by AC12.
- **S9** — The dossier `memory/map/features/spec-tokens.md` refreshed from three joins to four, and
  the generated map re-rendered if the checker edit moves it. Observed by AC13.
- **S10** — `memory/project/spec-token-waivers.txt` untouched unless the first real run finds a hit
  dated at or after the cutoff that is not this build's; expected empty. Observed by AC8.

## 3. Non-goals (OUT)

- The memory hygiene gate gains nothing. The spec-token checker already extracts both populations
  and owns the waiver registry; a second extractor for the same population is the two-mechanisms
  defect M2 exists to prevent.
- No live spec of another build is rewritten, and there is no drain. The 23 live specs that carry
  such a token today are other builds' to fix, and the cutoff excludes them by construction.
- The act — a bar run that no spec named — is `TOOL-aDeferredBar-3`'s, and the wording at the
  method's M6 and at the manifest is `TOOL-aDeferredBar-1`'s. This unit sees only the instruction
  as a spec writes it.
- No leg-selection flag for the runner, no environment override for the key
  (`TOOL-aDeclaredBound-2` removed the last such channel), and no change to the waiver registry's
  one-token-per-row grammar.
- The near-miss printing of the three existing joins is not extended; only the new join prints
  `NEAR` lines.
- `TOOL-aKeyedAnnotation-9` — the paths arm redding a unit that names its own deliverable — is
  untouched. This unit creates no file, so it is not exposed to it.

### Edges

- **consumes-from** `TOOL-aDeferredBar-1` — the memory-tree version constant and the render marker
  as unit 1 leaves them; this unit steps one past. Built before unit 1 lands, two bumps contend on
  the one constant line and the nine marker lines it governs.
- **hands-off** external — widening the example-conf parity arm to keys read by tools other than
  the hygiene engine is the open backlog row TOOL-aJoinedCanon-13. This unit adds its key to the
  shipped example by hand, and that arm still cannot see it.

## 4. Design

### Data model

The join is one regex and one conf key, both module constants beside `LEGLINE_KEY`:

```python
DIRECT_KEY = "SPEC_DIRECT_CUTOFF"
# A merge-bar or suite INVOCATION: the runner or a suite at command position — the token's start
# or a chain separator, past optional VAR=value prefixes, `timeout N` and a bash/sh launcher — or a
# GATE_FULL= / GATE_SELFTESTS= assignment anywhere in the token. A `path:line` citation fails the
# trailing lookahead and stays the cites join's; a grep over a suite FILE has grep at command
# position and is not a run.
BAR = re.compile(
    r"(?:^|&&|[;|(])\s*(?:\w+=\S*\s+)*(?:timeout\s+\S+\s+)?(?:bash\s+|sh\s+)?(?:\S*/)?"
    r"(?:run-gates|run-selftests|run-unattended-gates|[^\s/*?]+\.test)\.sh(?=\s|$)"
    r"|(?:^|\s)GATE_(?:FULL|SELFTESTS)=")
```

A glob such as `*.test.sh` names a population and is excluded by the character class, the same
exclusion `check_path_shaped` applies; a `path:line` citation fails the trailing lookahead.

Measured over the 1164 backticked tokens in the two graded populations of the 28 live specs at
`b2a330be`, this predicate and the brief's substring spelling agree on 49 tokens in 23 specs across
10 builds, newest dated 2026-09-04, and disagree on exactly two: the substring form hits a
`path:line` citation of the runner (a citation is the cites join's) and misses a suite path carrying
`--render` (a suite at command position with an argument is a run). Both disagreements fall the
invocation shape's way, which is what decided fork D in §8. The figures are DERIVED: the join's own
report line and `--list` reproduce them on any tree.

**Populations.** Exactly the two the `paths` and `legs` joins already extract, and read from the
same loops: every `TICK` token of a `## 6.` bullet as `extract_section(text, 6)` and the bullet
regex return it, and every `TICK` token of a line `LEG_LINE` matches inside `extract_gates(text)`.
Nothing else: a mention in §4, in a `New arm:` line (a prose prefix keeps it off `LEG_LINE`), in
any prose, or in a fenced block (`TICK` matches inline single backticks only, so a fence line and
its body yield no token) is not a hit.

**Ordering, the one correctness trap.** `NOT_A_TOKEN` (`tools/check-spec-tokens.py:55`) drops any
token opening with `GATE_` before either existing join sees it, and `NOT_A_LEG` drops any token
opening with `bash ` or carrying a slash from the leg join. The live instance that motivates this
build backticks a `GATE_SELFTESTS=` prefix; both exclusions would discard it unread. So the bar test
runs FIRST in each loop, on the raw token, before those `continue` statements. In the leg-line loop
a bar hit then continues, because the token was never a leg; in the bullet loop the paths join still
runs over the token's words, because a tracked runner path resolves either way and the two joins
answer different questions.

**Date gate.** `armed = direct_cut and spec_date >= direct_cut`, with `spec_date` from the existing
`SPEC_DATE` filename regex. A live spec before the cutoff is not graded, but its bar tokens in the
two populations are COUNTED, so the skip announces its size. A blank or absent key is OFF, and the
report line says so together with that same count — the OFF state cannot hide how much it hides.

**Hit shape.** `(f, "bar", tok, WHY)` with the token as the third field, so the existing waiver
lookup keys on it unchanged and the existing stale-row rule applies. `WHY` is the refusal text:

```
a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest
flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build
is complete
```

**Report line**, printed on every run beside the `LEGLINE_KEY` line, one of:

```
spec-tokens: bar join · <k> token(s) examined in <n> live spec(s) at/after SPEC_DIRECT_CUTOFF <date> · <p> pre-cutoff live spec(s) carry one and are not graded
spec-tokens: bar join · SPEC_DIRECT_CUTOFF blank (arm off) · <p> live spec(s) carry a bar token
```

**`--list` near-misses.** Every `TICK` token of a live spec's whole text that `BAR` matches and that
is not one of that spec's graded-population tokens, plus every graded-population match in a
pre-cutoff spec, prints as `spec-tokens: NEAR   [bar] <spec> :: <token> — <where>` where `<where>` is
`outside the graded population` or `predates SPEC_DIRECT_CUTOFF <date>`. Exit 0, never a hit.

**Waiver kind.** A waiver row for a bar hit carries `[bar]` as the first word of its reason column,
the same house convention the `[path]` and `[leg]` rows already follow. The checker keys on the
token and reads no kind; the kind is for the reader dispositioning the row. Stated here so nobody
later builds a kind-reader on the assumption one exists.

### Inventory

| identifier | kind | where | cell |
|---|---|---|---|
| `SPEC_DIRECT_CUTOFF` | conf key | `.memory-tree.conf`, the shipped example | `conf` is `dark` in `.lexicon.conf`; ungraded |
| `DIRECT_KEY` · `BAR` | module constants | `tools/check-spec-tokens.py` | the python cell grades definitions, not constants; no function is minted |
| `bar` | hit kind | the hit tuple's second field | not a naming cell |
| `[bar]` | waiver reason prefix | `memory/project/spec-token-waivers.txt` | not a naming cell |

The suite's arms use the existing `scratch` and `arm` helpers and define no function, so the shell
cell is untouched too.

### Migration

N/A — the key is additive under the blank-means-off idiom every sibling cutoff read by this checker
uses. An adopter whose conf predates it sees the join off and announced, never red.

### Rollout

The cutoff is the landing date, `2026-09-13`. Every hit measured at the base predates it, so
nothing landed reds. The first documents the join grades are this build's three specs, all dated
`2026-09-13`; this file is written to pass it (no §6 bullet and no §7 leg line backticks a runner,
a suite or a flag assignment), and a sibling spec of this build that hits is a defect in THAT
document — fixed there with a rev bump per M2, never waived. `SPEC_DIRECT_CUTOFF` is a merge-bar
knob: the conf comment says why the date is the landing date and what blank does.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/check-spec-tokens.py` | `DIRECT_KEY`, `BAR`, the bar test first in both loops, the date gate, the counts, the report line, the `NEAR` printing, the docstring — about 45 lines |
| `tools/check-spec-tokens.test.sh` | seven arms; `FLOOR_ASSERTIONS` from 20 to the count the suite prints, 27 if all seven land |
| `.memory-tree.conf` | the key at `2026-09-13` with a register comment: what it gates, why the date is the landing date, what blank does |
| `tools/memory-tree/.memory-tree.conf.example` | the key blank, with a comment in the idiom of the `SPEC_LEGLINE_CUTOFF` row; by hand, because the example-parity arm derives its key set from the engine alone |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | one paragraph beside the two §6 cutoff paragraphs; the marker line |
| `memory/TEMPLATE-SPEC.md` | the render of the above |
| `tools/memory-tree/check-memory-hygiene.sh` | the `KIT_MEMORY_TREE_VERSION` line only |
| `tools/memory-tree/HYGIENE.template.md` · `tools/memory-tree/BUILD-METHOD.template.md` · `tools/memory-tree/ANNOTATION-STYLE.template.md` | the marker line only |
| `memory/HYGIENE.md` · `memory/guides/BUILD-METHOD.md` · `memory/guides/ANNOTATION-STYLE.md` | the renders; the marker line only |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp with a delta line in the commit message |
| `memory/map/features/spec-tokens.md` | title and constraints prose: four joins; a paragraph on the bar join and its cutoff |
| `memory/map/generated/` | re-rendered by `python tools/codebase-map/gen_map.py --write` only if `--check` reports drift after the checker edit |
| `memory/project/spec-token-waivers.txt` | expected untouched; see S10 |

Thirteen carriers for one paragraph and one regex is the kit's own convention, not this unit's
choice: the version lives in one constant and nine marker lines, the kit-versions leg compares them
all, and the parity leg re-renders the four live copies from their templates. The memory note that
a watched-file touch owes stamps in several carriers is what this table is for.

### Alternatives rejected

- **A hygiene-engine check.** Rejected: the spec-token checker already extracts both populations and
  owns the waiver file; a second extractor is a second mechanism for one population.
- **The brief's substring predicate.** Rejected on the corpus measurement above: same count, wrong
  on both tokens where the two disagree, and an end-anchored `.test.sh` is evaded by any redirect
  after the path.
- **`SPEC_BAR_CUTOFF`**, matching the hit kind as `SPEC_LEGLINE_CUTOFF` matches `legline`.
  Rejected for interface agreement across the set: the brief's spelling is the one the sibling
  briefs were written against, and M2's interface axis spells a config key once.
- **Only the unattended suites.** Rejected: the owner's sentence names the class, and the ledger
  shows the costliest suites outside that kit.
- **A drain of the 23 carriers.** Rejected: other builds' live specs, and a terminal spec is frozen.
- **A file-keyed waiver row.** Rejected: the registry's grammar is one token per row and every
  consumer of it reads that shape; a bar token waived is waived in every spec, which is the same
  latitude a path token has today.

## 5. Production-readiness checklist

- security — N/A. The checker reads tracked files and the conf and writes nothing.
- perf / scale — one regex per backticked token over two populations of at most the live-spec count
  the checker already prints; the leg costs 1.6 s in the ledger at the base and its 60 s ceiling
  does not move.
- error / empty / loading states — a blank key is OFF and announced with the carrier count; a key
  set with no live spec at or after it prints `0 live spec(s) at/after`, an empty population that
  names itself; the existing zero-spec, missing-manifest and missing-registry refusals are
  untouched.
- observability — the bar line on every run, green included; `NEAR` lines under `--list`; the
  refusal text names the substitute.
- risks — five. (1) `NOT_A_TOKEN` and `NOT_A_LEG` drop the motivating token unread unless the bar
  test runs first; AC1 and AC2 pin the ordering. (2) A sibling spec of this build reds at the bar;
  the remedy is a fold on that spec, never a waiver row. (3) Built before unit 1 lands, the version
  step collides; `order 2` and the §3 edge sequence it. (4) The example-conf parity arm cannot see
  the key, so the example row is by hand and AC14 observes it. (5) An author evades with a path
  built at runtime or inside `sh -c`; the docstring says so, and the act is unit 3's.
- testing — seven arms, each fixture one edit from the suite's clean scratch repo; every failing
  case observed RED by the direct checker on that fixture before the arm lands; the suite itself
  runs at `VERIFYING` under the main loop.
- migration — N/A; additive key, blank-means-off.
- user docs — the template paragraph, rendered; the dossier; the checker's own header. This repo
  keeps no `help/` tree.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py` runs in a scratch repo whose conf sets
  `SPEC_DIRECT_CUTOFF` to 2026-09-01 and whose one live spec, dated 2026-09-02, backticks inside a
  §6 bullet a full-bar invocation carrying the self-test flag assignment, it exits 1 and stdout
  carries `[bar]`, that spec's path and the substitute text.
  Red when: exit 0, or the hit is absent because `NOT_A_TOKEN` dropped the `GATE_`-prefixed token
  before the join saw it.
  fixture: a scratch repo of the shape the suite's `scratch` helper builds, made under `mktemp -d`;
  the tree holds none. Its conf arms `SPEC_DIRECT_CUTOFF` alone; no second key guards this arm.
- **AC2** — When the same token sits instead as a backticked entry on the §7 leg line, the run exits
  1 and stdout carries `[bar]` for it.
  Red when: `NOT_A_LEG` discards the token unread and the run exits 0 with a clean leg join.
  fixture: as AC1.
- **AC3** — When the same token appears only in §4 prose, in a §7 line opening `New arm:`, and in a
  fenced block indented under a §6 bullet, `python tools/check-spec-tokens.py` exits 0 and
  `python tools/check-spec-tokens.py --list` prints three `NEAR` lines reading
  `outside the graded population`.
  Red when: any of the three placements reports as a hit, or `--list` prints fewer than three.
  fixture: as AC1.
- **AC4** — When the spec is dated 2026-08-30 against a cutoff of 2026-09-01 and carries the AC1
  token, `python tools/check-spec-tokens.py` exits 0 and its bar line reads
  `1 pre-cutoff live spec(s) carry one and are not graded`.
  Red when: exit 1, or the count reads 0 while the token is present.
  fixture: as AC1.
- **AC5** — When the conf sets the key to the empty string over the AC1 fixture,
  `python tools/check-spec-tokens.py` exits 0 and its bar line reads
  `SPEC_DIRECT_CUTOFF blank (arm off) · 1 live spec(s) carry a bar token`.
  Red when: the line is absent, or the carrier count reads 0 while the token is present.
  fixture: as AC1.
- **AC6** — When `memory/project/spec-token-waivers.txt` in the AC1 fixture gains a row whose token
  is the AC1 token and whose reason opens `[bar]`, `python tools/check-spec-tokens.py` exits 0 and
  reports `1 waiver(s)`.
  Red when: exit 1, or the summary counts 0 waivers.
  fixture: as AC1.
- **AC7** — When that row's token is one no spec in the fixture carries,
  `python tools/check-spec-tokens.py` exits 1 and stdout carries `STALE WAIVER`.
  Red when: exit 0.
  fixture: as AC1.
- **AC8** — When `python tools/check-spec-tokens.py` runs on this tree at the build commit, it exits
  0; its bar line names `SPEC_DIRECT_CUTOFF 2026-09-13`, examines a non-zero token count in this
  build's live specs, and counts the pre-cutoff carriers; and `git diff --stat` for
  `memory/project/spec-token-waivers.txt` against the base is empty.
  Red when: a hit at or after the cutoff — which by construction can only be a spec of this build,
  this one included — or a new waiver row.
  figure: DERIVED by the run. At `b2a330be` this predicate counts 23 pre-cutoff carriers; the
  brief's 25 was measured with a differently spelled predicate, and neither number is pinned.
- **AC9** — When `python tools/check-spec-tokens.py --list` runs on this tree at the build commit,
  it exits 0 and prints at least one `NEAR` line reading `predates SPEC_DIRECT_CUTOFF 2026-09-13`,
  and the number of distinct specs on such lines equals the pre-cutoff count AC8's bar line reports.
  Red when: the two counts disagree, or no `NEAR` line prints while AC8 counts carriers.
  figure: DERIVED, the same run.
- **AC10** — When `grep -c SPEC_DIRECT_CUTOFF tools/memory-tree/SPEC-TEMPLATE.template.md` and
  `grep -c SPEC_DIRECT_CUTOFF memory/TEMPLATE-SPEC.md` run, both print the same count of at least 1,
  and `head -1 memory/TEMPLATE-SPEC.md` carries a `gov:kit memory-tree@` marker equal to the value
  `KIT_MEMORY_TREE_VERSION` holds in `tools/memory-tree/check-memory-hygiene.sh`.
  Red when: the counts differ, which is a template edited and not re-rendered, or the live marker
  lags the constant.
- **AC11** — When `bash tools/check-kit-versions.sh` runs at the build commit it exits 0, and
  `git grep -l "gov:kit memory-tree@" -- tools/memory-tree memory` lists the same file set it lists
  at the base, every one carrying the stepped value.
  Red when: any listed file carries the previous value, or the set shrank.
  figure: DERIVED by the grep; nine files at `b2a330be`.
- **AC12** — When `bash skills/session-kickoff/manifest-check.sh` runs at the build commit, it exits
  0.
  Red when: check 5 names `.memory-tree.conf` or the engine as touched after the manifest's
  `last-audit` stamp.
- **AC13** — When `python tools/codebase-map/gen_map.py --check` runs at the build commit it exits
  0, and `grep -c "Four joins" memory/map/features/spec-tokens.md` prints 1.
  Red when: the generated set drifted from the checker edit and was not re-rendered, or the dossier
  still says three.
- **AC14** — When `grep -c "^SPEC_DIRECT_CUTOFF=\"\"" tools/memory-tree/.memory-tree.conf.example`
  runs, it prints 1.
  Red when: 0 — the shipped example lacks the key and an adopter installs a dead arm reading as
  armed, which no gate catches (TOOL-aJoinedCanon-13).

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `memory hygiene` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `kit/dogfood doc parity` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `line length`

`spec-tokens self-test` is `chunk: selftests`, `subject: kit`, guarded on `tools/`, so an ordinary
bar holds it; the main loop's flagged bar at `VERIFYING` runs it, and it costs 76 s in the ledger
at the base. `verdict epoch` is named because the constant moves; the move dates no engine change,
which the topological rule permits, and it is the kit-versions leg that demands it.

New arm: tools/check-spec-tokens.test.sh · seven scratch repos, each one edit from the suite's clean fixture — a post-cutoff §6 bullet, a §7 leg-line entry, the three not-hit placements in one spec, a pre-cutoff date, a blank key, a clearing `[bar]` row, a stale one — asserted per AC1 through AC7 · `FLOOR_ASSERTIONS` from 20 to the count the suite prints, 27 if all seven land

## 8. Open questions

- **Fork A — hygiene check or spec-token join.** RESOLVED (agent, 2026-09-13, delegated): the
  spec-token checker. It already extracts both populations and owns the waiver file; a hygiene
  check would be a second extractor for one population.
- **Fork B — ban every `*.test.sh` in an AC, or only the unattended suites.** RESOLVED (agent,
  2026-09-13, delegated): every suite. The owner's third sentence names the class, and the ledger
  puts `govkit selftest` at 3445 s and `manifest-check self-test` at 2162 s beside the unattended
  pair.
- **Fork C — cutoff or drain.** RESOLVED (agent, 2026-09-13, delegated): a cutoff at the landing
  date. The carriers are other builds' live specs, and the newest predates the date by nine days.
- **Fork D — the predicate's shape: the brief's substring spelling, or invocation shape.**
  RESOLVED (agent, 2026-09-13, delegated): invocation shape, on the §4 measurement. Same 49 tokens
  either way; the two disagree on one citation and one suite-with-argument, and the invocation shape
  is right on both. Recorded as a decision rather than a fact-question because the corpus could
  only show where the two differ, not which reading the owner's sentence intends.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a spec acceptance token that spells a merge-bar
or self-test suite invocation"` ranks `CensusRefused` and `build_self_chain` from the
process-monitor kit as its two seams, both by name stem, neither about specs; the affordance rows it
adds name the run-gates knob set, which is what this unit refuses rather than what it extends. The
seam this unit extends was found by reading the checker: `tools/check-spec-tokens.py`, whose `legs`
and `paths` joins already extract the two populations and whose `read_conf_key` and `SPEC_DATE`
already give a dated, conf-gated arm its shape — `LEGLINE_KEY` is the exact precedent and the join
is written beside it. The map probe printed `unscanned layers: .sh`, so the suite side was read by
hand: `tools/check-spec-tokens.test.sh`'s `scratch` and `arm` helpers take the seven arms without a
new function. Two recall hits changed the design: TOOL-aJoinedCanon-13 says the example-conf
parity arm cannot see a key this checker reads, so the example row is by hand and observed by
AC14; TOOL-aDeclaredBound-2 says the last env override for a cutoff was removed because the conf
already won, so this key gets none. Recall's TOOL-aKeyedAnnotation-9 was checked and does not
bind: this unit creates no file for the paths arm to red on. The research record's terms were
re-run and its finding — no seam for refusing a bar inside a pass — stands for the ACT, which is
unit 3's; for the INSTRUCTION the seam above exists and is taken.

Recall terms used: `python tools/memory-recall/query.py "which record decided that spec-token joins
are date-gated by a conf cutoff and waived through the token registry, and why a suite run is not
an acceptance observation" --terms "spec-tokens cutoff waiver legline check-spec-tokens acceptance
witness run-gates self-test GATE_SELFTESTS bar-in-pass suite deferred"`.
