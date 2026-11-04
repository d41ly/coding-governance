# TOOL-dFairHearing-37 — the round-4 spec audit's 19 minors on units 30 and 32: one replay procedure that isolates each arm, criteria over the scored attempt, and checks that can go red

**Status:** CLOSED · rev-6 · 2026-11-04 · node d · Tier-2 · base 3708a705 · streams tooling · order 26 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-37-deviation-371.md](../build/2026-10-23-build-TOOL-dFairHearing-37-deviation-371.md) | deviation | — |
| [2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 |
| [2026-11-04-build-TOOL-dFairHearing-37-1-acceptance-ledger.md](../build/2026-11-04-build-TOOL-dFairHearing-37-1-acceptance-ledger.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-37-1-builder-return.md](../build/2026-11-04-build-TOOL-dFairHearing-37-1-builder-return.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md) | research | TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 |
| [2026-10-23-prompt-TOOL-dFairHearing-37-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-37-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFairHearing-37-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFairHearing-37-build-brief.md) | research | — |
| [2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief.md) | research | TOOL-dFairHearing-25 TOOL-dFairHearing-30 TOOL-dFairHearing-35 TOOL-dFairHearing-32 TOOL-dFairHearing-40 |
| [2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief.md) | research | TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-35 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-36 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 |
| [2026-11-04-prompt-TOOL-dFairHearing-37-1-spec-writer.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-37-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-TOOL-dFairHearing-37-fix-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-37-fix-brief.md) | research | — |
| [2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md) | spec-audit | TOOL-dFairHearing-35 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-36 |

<!-- /gen:spec-records -->

## 1. Goal

One of two batch units closes the MEDIUM and LOW findings that the round-4 spec audit confirmed
(`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`) and
that land on units 30 and 32. That is 19 report ids. MEDIUM ids: 1 (item M1), 2 (M2), 4 (M4), 5 (M5),
10 (M6), 12 (M8), 13 (M9), 20 (M11), 23 (M12), 25 (M13), 33 (M17), 34 (M18), 35 (M19) and 36 (M20).
LOW ids: 6 (L1), 8 (L3), 17 (L6), 26 (L9) and 37 (L11). Each id is its own §2 item. The other 13
minors land on units 28, 29 and 31 and are `TOOL-dFairHearing-36`'s; the two write sets are disjoint
by BUILD-METHOD M6 (that spec's §4), so the halves build concurrently. This unit builds after every
unit it repairs. It makes each corrected statement true on what those units built and observes what
each criterion claimed. The rules unit 30's runs needed before they ran (ids 20 and 34, and id 33's
restatement of unit 30's AC1) are folded into unit 30, and the placement's one trap (id 37) into
unit 25 (unit 25 §8 F2). A
criterion it supersedes is named by the hands-off bullet in that unit's §3, and that unit's
acceptance ledger records it superseded here (`TOOL-dFairHearing-23` §8 F7's form).

## 2. Scope (IN)

Each item names its report id, its report item, the unit it lands on and the criterion that observes
it.

- **S1** — id 1 (M1, unit 30). Unit 30 and unit 27 shared order 21 when the round-4 audit read them, and wrote the same files. The
  scoring, the decision and spec 15 S6's product files moved to `TOOL-dFairHearing-35` at order 24, so
  unit 30's commit writes only its verdict record and the replay section's per-arm step (unit 30 S7),
  and `--experiment` runs after unit 27 S7's rewrite of `check_held_out_frozen`. This item observes
  both. Observed by AC1.
- **S2** — id 2 (M2, unit 32). Unit 32's S20, S21 and AC12, for unit 15's replay, read unit 35's
  attempt rule instead of imposing a cap after the runs: a third completed attempt is `unscored` there,
  never a red here, and a `void after cap` record is unit 35's `no decision`. That wording is carried
  by unit 30 S9 and unit 32's AC12 since the fold, and unit 32 keeps their replay-1 read. This item
  keeps the read after unit 35 scores. Observed by AC2.
- **S3** — id 4 (M4, unit 32, AC9). AC9 grades only values a record held before any append. Since the
  fold, units 25 S7 and 30 S8 write the orchestrating commit at call time and unit 32 S14 appends
  nothing, so no line is marked `(derived)` and AC9 grades both records. This item observes that
  neither record holds a derived line. Observed by AC3.
- **S4** — id 5 (M5, unit 30 AC4's `selected` half, read after unit 35's decision). The `selected` half
  is observed by behaviour, not by `grep -c -- "--all-ungated"`, which a docstring stating unit 23
  S21's contract reds; unit 30 AC4 holds no count since the fold. When unit 35's record states
  `selected`, `gotchas.py --for-diff <range> --all-ungated` exits 2 with argparse's `unrecognized
  arguments`, so no flag shipped. This also answers unit 32 S13 and AC8, whose byte-identical
  comparison presumes the flag ships. The argparse sentence does not hold on the built tree:
  `gotchas.py` reads its arguments by hand and exits 0 on an unknown flag (probe at `8d58d785c`), the
  repair `TOOL-dFairHearing-38` S2 and S3 own (§3). Observed by AC4.
- **S5** — id 10 (M6, unit 32 S31, AC19). `check_held_out_frozen` in
  `tools/workflows/replay_scorer.py` already runs `git --literal-pathspecs ls-files --full-name -- <path>`,
  the global option before the subcommand (:870 at `fb755fa80`, as `read_git("--literal-pathspecs",
  "ls-files", …)`): unit 32 built it so, its `Decided:` line departing from its S31 spelling after the
  verb, which git refuses with exit 129. This unit changes no scorer code; it adds the valid-path control
  unit 32 AC19 lacked, a runner arm over one tracked file. Observed by AC5.
- **S6** — id 12 (M8, unit 30). Unit 30's runs pass a forward-slash clone path, built with `cygpath -m`
  by its S7 before they run, so this item hardens the harness for every other caller and corrects no
  run. The harness takes `repo` with every backslash folded to `/` at its one read, `const repo`
  (`tools/workflows/tier2-review.template.js:215` at `9c1a2857a`), the fold `repoFold` (:652) already
  applies for its comparison. Every `git -C ${repo}` command an agent runs then carries a path bash
  cannot strip. Observed by AC6.
- **S7** — id 13 (M9, unit 32 S7, AC4). AC4's "neither reader changes" half reads the reader where unit
  12 S2 moved it: the body of `extract_section_ref` in `tools/workflows/replay_scorer.py`, sliced from
  its `def` line to the next top-level `def` or `class`, is byte-identical at unit 32's commit and its
  parent. This supersedes AC4's whole-file diff of `tools/workflows/review_replay.py`. Observed by AC7.
- **S8** — id 20 (M11, unit 30). The per-arm steps in the replay section of
  `tools/workflows/README.md`, the single source unit 32 S17 names: one fresh clone per record and arm
  named `f<r><a><n>` under a forward-slash temp path, the status read as its own call with its exit
  checked, a new clone per attempt, and the orchestrating commit written to the run log at call time.
  Carried by unit 30 S7 before its runs, as unit 40 S12 to S14 correct them. NOT OBSERVED here: unit
  30 AC5 observes it.
- **S9** — id 23 (M12, unit 32 S22, AC13). AC13's absence check reads the two `.js` files on the
  blanked view and, in a second pass, on every `${…}` interpolation inside a template literal, which
  `renderBlankedView`'s `tmpl` branch (`tools/hooks/agent-cap.js:551-554` at `9c1a2857a`) skips whole. A copy
  holding `` `x ${MAX_LENSES}` `` fails it. The residual: an identifier spelled at run time from
  pieces. Observed by AC9.
- **S10** — id 25 (M13, unit 32). `resolveKitDir`, which unit 32 S25 adds to `tools/hooks/agent-cap.js`,
  is a function the symbol tier lists, so `memory/map/generated/symbols.json` is regenerated with
  `python tools/codebase-map/gen_map.py --write` wherever `--check` reports it stale, and this unit's
  leg line carries `codebase-map coverage + freshness`. Observed by AC10.
- **S11** — id 33 (M17, unit 30, AC1). Unit 30's AC1 is restated over every attempt at unit 30, which
  carries it since the fold. This item keeps the read after unit 35 scores: the scored attempt of each
  record and arm, as unit 35's checker names it, is one of eight distinct scored clones, each with an
  empty observed status before its call, `HEAD` equal to its record's range head and exactly one
  untracked path, its report. Observed by AC11.
- **S12** — id 34 (M18, unit 30). The per-arm status step reads the status as its own call, exit
  checked, then tests it empty, so a status call that fails is a refusal and never a clean tree.
  Carried by unit 30 S7 before its runs. NOT OBSERVED here: unit 30 AC5 observes it.
- **S13** — id 35 (M19, unit 32 §4 truth table, AC15, AC16). The truth table gains row 8, `.git` a
  file at the worktree root with the pack beside the hook, answering the probe's directory with the
  root at the worktree, and row 9, a receipt holding invalid JSON with the pack beside the hook,
  answering the probe's directory. `tools/lib/resolve_kit_dir.py:29` finds the root by
  `(d / ".git").exists()`, true for a file, and :33 catches `ValueError`. Both rows join the behaviour
  arm unit 32 S26 adds to `tools/lib/resolve-python.test.sh`. Observed by AC12.
- **S14** — id 36 (M20, unit 32, AC14). AC14 computes its precondition: the scratch prefix's length
  plus the longest tracked path's. It expects `Filename too long` only on win32 with that sum above
  259, and otherwise prints `AC14 n/a: <platform>/<length>`, recorded as not observed on that node.
  Observed by AC13.
- **S15** — id 6 (L1, unit 32 S32, AC20). `check_ungated`'s sentence end is a full stop, optionally
  followed by a run of closing `*`, `_`, `)` or backtick characters, then whitespace or the paragraph's
  end. Unit 32 already built the run: `GATED_SCOPE_RE` (`tools/memory-tree/gotchas.py:419` at
  `fb755fa80`) holds `` \.(?![*_)`]*(?:\s|\Z)) ``, and its selftest pins `.**` (:1000-1009). This unit
  changes no `check_ungated` code; it adds the selftest arm for a mixed run, `.*)`. Observed by AC14.
- **S16** — id 8 (L3, unit 32 AC14, AC10). AC14 is recorded evidence for unit 32 S23 under S14's
  computed precondition, and AC10, now its in-repository `git for-each-ref refs/replay/` read alone, is
  a precondition, each so labelled in unit 32's ledger. NOT OBSERVED by a criterion here: it labels two
  ledger lines; AC13 is the computed form of the first.
- **S17** — id 17 (L6, unit 32 S6). The instrument keys `t.group(1).lower()` at
  `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication-instruments.md:1665-1666`,
  not :1664-1665. Where the comment above `deriveAddressKey` cites the instrument by line, it cites
  :1665-1666. Observed by AC15.
- **S18** — id 26 (L9, unit 30 §7). Spec 15 S6's harness change moved to unit 35, whose leg line
  carries `workflow script syntax`, and this unit's harness edit (S6) carries it too. The render
  parses at this unit's commit. Observed by AC16.
- **S19** — id 37 (L11, unit 32 S18). The README's placement step and recipe set one EXIT trap that
  holds both `rm -f "$idx"` and `git update-ref -d refs/replay/<name>`, so the recipe's trap cannot
  replace the placement's. Carried by unit 25 S9 before replay 1 runs, with unit 32 S18's placement.
  NOT OBSERVED here: unit 25 AC8 observes it.

## 3. Non-goals (OUT)

- No re-review. The items unit 30's runs and unit 25's placement needed before they ran are folded
  into those specs under M4's repair rule (unit 25 §8 F2). Each item left here corrects what unit 32
  built, hardens the harness for other callers (S6), or reads what units 30 and 35 left, and reopens
  no severity.
- No re-run of a replay: unit 30's runs are read as they were made.
- No HIGH finding: ids 22, 31 and 32 are `TOOL-dFairHearing-33`, `-34` and `-35`.
- No minor on units 28, 29 and 31: those 13 are `TOOL-dFairHearing-36`'s.
- No new gate leg: every arm lands in a suite that exists or that an earlier unit adds.
- No help page: `help/` covers neither the review harness, the scorer factory nor the hooks.

### Edges

- **consumes-from** `TOOL-dFairHearing-25` — replay 1's verdict record, whose call-time orchestrating commit AC3 reads
- **consumes-from** `TOOL-dFairHearing-30` — the verdict record, its attempts and clones, which S1 to S4 and S11 read
- **consumes-from** `TOOL-dFairHearing-32` — S6, S7, S13, S14, S20 to S23, S25, S26, S31, S32 and their criteria, which S2 to S5, S7, S9, S10 and S13 to S17 correct or read
- **consumes-from** `TOOL-dFairHearing-35` — the attempt rule and its checker, which S2 and S11 read for the scored attempt
- **hands-off** `TOOL-dFairHearing-38` — finding id 1 (item H1, shared with id 11) of the round-5 spec audit: S4's argparse sentence, its claim to answer unit 32 S13 and AC8, and AC4's `selected` half are superseded by its S2, S3, AC1 and AC2; AC4's `ungated` half stands
- **hands-off** `TOOL-dFairHearing-39` — finding id 11 (item H1, shared with id 1) of the same audit: AC4's argparse wording, cited in the bug-class catalogue as the form a criterion takes when it quotes an error text its tool never emits
- **hands-off** `TOOL-dFairHearing-40` — the same audit's minors on this spec, ids 4, 5, 8, 18, 28, 29, 30, 36 and 37: AC11 over each scored clone, AC5's count, AC15's anchor, AC9's view through `renderLexedView`, AC12's Red when half and the port's cure, the `ungated` class set re-derived after S15, the pass's write set counting its ledger record, and every `git -C ${repo}` quoted (its S10, S15, S17, S20, S23, S30, S31, S33 and S34); ids 15, 22 and 38, the per-arm step's corrections, are carried by unit 30 S7, and id 5's trap count by unit 25 S9


## 4. Design

### Why two batch units

`TOOL-dFairHearing-36` §4 states the line: this half writes the workflows README, `replay_scorer.py`,
the harness template and render, `tier2-review.test.sh`, `gotchas.py`,
`tools/lib/resolve-python.test.sh`, `symbols.json` and two records, and reads neither suite that half
writes; that half defines no function, so `symbols.json` and its generator are this half's alone.
Since the fold this half writes neither the workflows README nor the records, which only narrows the
set that line keeps disjoint.

### The per-arm step and the placement's trap (S8, S12, S19)

Carried by unit 30 §4 and unit 25 §4, each written into the README's replay section before its runs.

### The harness's one read (S6)

```js
const repo = String(a.repo || '.').replace(/\\/g, '/')
```

A POSIX path holds no backslash, so the fold changes nothing there; on Windows git takes forward
slashes in every path argument. A refusal was weighed and declined: it would fail every caller that
passes a native Windows path today, for a value the harness can make safe in one place.

### Files touched (estimate)

- `tools/workflows/replay_scorer.py`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/memory-tree/gotchas.py`
- `tools/lib/resolve-python.test.sh`
- `memory/map/generated/symbols.json`
- `memory/builds/dFairHearing/build/`

`tools/workflows/tier2-review.js` is the template's render. `symbols.json` changes only where
`gen_map.py --check` reports it stale. Under the build folder only this unit's acceptance ledger is
written; S3 and S11 read the replay records.

### Alternatives rejected

- **Refuse a backslashed `repo` in the harness (S6).** §4 "The harness's one read".
- **Re-run unit 30's arms whose `repo` held a backslash.** None can: unit 30 S7 builds the clone path
  forward-slashed before its runs, and S6 closes the class for every other caller.
- **Keep AC13's view and add the interpolation case to S22's residual only (S9).** The case is a live
  code reference, so the probe reads it.

## 5. Production-readiness checklist

- security — S6 folds a path separator at the harness's one `repo` read and admits nothing new; the
  spec-kind `..` refusal after it (:647-650 at `9c1a2857a`) still reads the folded value. No new write path.
- perf / scale — one string replace per harness call; one `git ls-files` per held-out path.
- error / empty / loading states — S5's control observes that a valid held-out path resolves, beside
  unit 32's refusals that exit 2 naming the path.
- observability — AC3 reports whether each record's orchestrating commit was written at call time.
- risks — none beyond the reads: this unit writes no replay record.
- testing — scratch probes and fixtures per criterion; the §7 arms observed RED then GREEN at the close.
- migration — none for adopters beyond the harness's folded `repo`.
- user docs — none: the replay section is units 25 and 30's; there is no `help/` page (§3).

## 6. Acceptance criteria

`$SCRATCH` is the pass's scratch directory, and a clone or fixture repository goes under
`%TEMP%/<short name>`. Unit 30's record is
`memory/builds/dFairHearing/build/<date>-build-TOOL-dFairHearing-30-replay-verdict.md`.

- **AC1** — When `git show --name-only --format= <c30>` runs, where `<c30>` is the commit
  `git log --diff-filter=A --format=%H -1 -- <unit 30's record>` prints, every path it lists sits under
  `memory/` or is `tools/workflows/README.md`: piped through
  `grep -v '^memory/' | grep -vx 'tools/workflows/README.md'`, it prints nothing. The `memory/` paths
  are records and the renders the build-index hook forces into every pass commit (`memory/LIVE.md`,
  `memory/backlog/TOOL.md`), never product. `git merge-base --is-ancestor <c27> <c>` exits 0 for `<c>` as `<c30>` and as `<c35>`, where
  `<c27>` is unit 27's pass commit, the one
  `git log --format=%H -1 --grep='^tool(dFairHearing): TOOL-dFairHearing-27 '` prints, and `<c35>` is
  unit 35's scoring commit, the one `git log --format=%H -G'^## Scoring$' -- <unit 30's record>` prints
  (unit 35 adds no manifest; it writes the `## Scoring` section into unit 30's record).
  Red when: unit 30's commit writes a product file other than the README's replay section, or the
  runs or the scoring ran before unit 27's rewrite.
- **AC2** — When unit 35's `attempts.py` (its §4, written under `$SCRATCH`) runs over unit 30's record,
  each `unscored` attempt it names is listed `unscored` in the record; where it names none, as the
  record's `## Scoring` section states, the ledger records this half `n/a: no unscored attempt`, never as
  coverage. Unit 32's builder return
  (`memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-32-1-builder-return.md`) records
  its AC12 with no red on an attempt unit 35's rule never read, and so does unit 32's acceptance ledger
  where one exists at this unit's commit (unit 32 owed it to the close).
  Red when: unit 32's record of AC12 reds an attempt unit 35's rule never read.
- **AC3** — When `grep -n "orchestrating commit" <unit 30's record>` and the same over unit 25's record
  run, each prints a line and neither line ends `(derived)`. A scratch run of unit 32's AC9 probe over
  each record compares the recorded value.
  Red when: a value git derived after the fact is graded as evidence, or a record lacks the call-time
  value.
- **AC4** — When `grep -n "^\*\*The decision:" <unit 30's record>` runs, it prints one line. Where that
  line names `selected`, as it does at `8d58d785c`, this unit's ledger records AC4's `selected` half
  `superseded by TOOL-dFairHearing-38` (its AC1 and AC2, §3) and grades no exit of `gotchas.py` here.
  Where it names `ungated`, unit 35's AC4 answers this criterion.
  Red when: the ledger grades the `selected` half on `gotchas.py`'s exit, which is 0 for any unknown
  flag, or the decision line is missing.
- **AC5** — When `--experiment` runs with `heldOut` naming one tracked file, it exits 0 or reaches the
  freeze comparison. With `heldOut` naming a directory, and again a path holding `*`, each exits 2
  naming the path and its line count. Run in the workflows kit,
  `grep -c '"--literal-pathspecs", "ls-files"' replay_scorer.py` prints 1, the argv form `read_git`
  takes.
  Red when: the valid path exits 2, which is the spelling that exits 129 refusing every path.
- **AC6** — When a scratch stub-agent run of `tools/workflows/tier2-review.js` is given `repo` as
  `C:\x\y`, every captured prompt's `git -C` command names `C:/x/y`, and no prompt holds a backslash
  inside that path.
  Red when: the `const repo` read in `tools/workflows/tier2-review.template.js` still takes `a.repo` raw.
- **AC7** — When the body of `extract_section_ref`, sliced as S7 states, is taken from
  `git show <c32>:tools/workflows/replay_scorer.py` and from `git show <c32>~1:tools/workflows/replay_scorer.py`,
  where `<c32>` is unit 32's pass commit, the two slices are byte-identical and neither is empty.
  Red when: unit 32 rewrote the scorer's section reading.
- **AC9** — When a scratch node probe reads `tools/hooks/agent-cap.js` and `check-verifier-fanout.js`
  on the blanked view and on their template interpolations, neither holds a `MAX_LENSES` identifier. A
  scratch copy holding `` `x ${MAX_LENSES}` `` fails the probe, one holding `// MAX_LENSES was 6`
  passes it, and one holding `const MAX_LENSES = 6` fails it.
  Red when: an interpolated reference passes as absent.
- **AC10** — When `python tools/codebase-map/gen_map.py --check` runs at this unit's commit, it exits 0,
  and `grep -c '"resolveKitDir"' memory/map/generated/symbols.json` prints a number above 0.
  Red when: unit 32's added function is missing from the symbol tier.
- **AC11** — When unit 35's `attempts.py` names each scored attempt, unit 30's record lists for that
  clone an empty observed status, and `git -C <clone> rev-parse HEAD` equals its record's range head.
  The eight scored clones are distinct, and each lists exactly one untracked path, its report. Every
  other attempt is listed with its status and reason.
  Red when: a scored clone was dirty before its call, or two scored attempts share a clone.
  fixture: the clones under `%TEMP%`, kept until the record cites them.
- **AC12** — When a scratch probe runs `tools/lib/resolve_kit_dir.py` and the JS port over rows 8 and
  9, the two print the same directory on each row. A JS copy that tests `isDirectory()` for `.git`
  disagrees on row 8, and one that lets `JSON.parse` throw disagrees on row 9.
  Red when: the port walks past a worktree's `.git` file or denies on a malformed receipt.
- **AC13** — When AC14 of unit 32 runs on this node, it first prints the scratch prefix's length plus
  the longest tracked path's, from `git ls-files`. On win32 with a sum above 259 it observes
  `Filename too long`; otherwise it prints `AC14 n/a: <platform>/<length>` and exits 0.
  Red when: a node with a short scratch path reds a correct build.
  figure: the sum is DERIVED on each node; 152 and 118 were measured here on 2026-10-23.
- **AC14** — When a scratch python probe imports `tools/memory-tree/gotchas.py`, `check_ungated` ends
  ``**Gated by `tools/check-wiring.sh`.** Next`` at `.**` and ``(gated by `tools/check-wiring.sh`.*) Next``
  at `.*)`, with `tools/check-wiring.sh` in scope and the next sentence outside it.
  Red when: a run of two closing characters carries the scope into the next sentence.
- **AC15** — When `grep -n -B12 "function deriveAddressKey" tools/workflows/tier2-review.template.js`
  runs, the comment it prints holds no `:1664`.
  Red when: the comment cites the instrument's `if r['kind'] == 'spec':` line as its keying.
- **AC16** — When `node tools/workflows/check-workflow-syntax.js tools/workflows/tier2-review.js` runs at
  this unit's commit, it exits 0, and over a scratch copy holding `let y=(` it exits 1.
  Red when: the harness edit leaves a render the workflow runtime cannot parse.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `review-replay selftest` · `gotchas selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `workflow script syntax` · `codebase-map coverage + freshness` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `policy fixtures`

New arm: tools/workflows/tier2-review.test.sh · covers AC6 · a stub run whose `repo` holds backslashes, staged against the harness at `TOOL-dFairHearing-32`'s commit, where `repo` is read raw · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/workflows/replay_scorer.py (its runner, in the `review-replay selftest` leg) · covers AC5 · a held-out path naming one tracked file, staged against `check_held_out_frozen` with its `read_git` call spelled as unit 32 S31 did, `--literal-pathspecs` after `ls-files`, which git refuses with exit 129 so the valid path refuses · that runner's `ARMS_DECLARED`, raised by the arm added
New arm: tools/lib/resolve-python.test.sh · covers AC12 · a JS port testing `isDirectory()` for `.git`, and one letting `JSON.parse` throw · none
New arm: tools/memory-tree/gotchas.py (its selftest) · covers AC14 · a gated sentence closing on `.*)`, staged with `GATED_SCOPE_RE`'s closer class narrowed to one character, `` [*_)`]? `` in place of `` [*_)`]* ``, which carries the scope past `.*)` into the next sentence · none

## 8. Open questions

- **F1 — Fold or refuse a backslashed `repo` in the harness (S6)?** Options: (a) fold `\` to `/` at
  the one read; (b) refuse the call naming the forward-slash form. (b) fails every caller that passes a
  native Windows path today; (a) makes the value safe in one place, the fold `repoFold` already
  applies. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3; it satisfies AC6 as (b) does and
  breaks no caller. widens: none · relaxes: none
- **F2 — One batch unit or two (BUILD-METHOD M4, M6)?** `TOOL-dFairHearing-36` §8 F1 resolves it for
  both halves. RESOLVED (agent, 2026-10-23, delegated): two, rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the 14 MEDIUM and 5 LOW findings of the round-4 spec
  audit of specs 28 to 32 that land on units 30 and 32, as one of two batches.
- rev-2 · 2026-10-23 · §3 · the round-5 spec audit's disposal: hands-off edges to TOOL-dFairHearing-38 and -39 (item H1, ids 1 and 11) and
  TOOL-dFairHearing-40 (twelve minors).
- rev-3 · 2026-11-03 · §7 · the leg line adds `policy fixtures`, whose guard §4's
  `tools/memory-tree/gotchas.py` trips (fix brief 2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief, item 1).
- rev-3 · 2026-11-03 · S9 · §10 · `renderBlankedView` and its `tmpl` branch re-cited from
  the hook's lines 1303 and 1325-1328, past its 947 lines since unit 16, to :529 and :551-554
  at `9c1a2857a` (fix brief 2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief, items 2 and 4).
- rev-3 · 2026-11-03 · S6 · §5 · AC6 · §10 · the harness's `repo` read, `repoFold` and the `..` refusal
  re-cited at `9c1a2857a` (:180, :491 and :486-489 to :215, :652 and :647-650), and AC6's red case named
  by the `const repo` read (fix brief 2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief, item 2).
- rev-4 · 2026-11-03 · header · S1 · §4 · the header's order 24 to 26: it consumes from units 30, 32
  and 35, now at 23, 25 and 24; S1 and §4 re-word units 27, 30 and 35's positions to match (fix
  brief 2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief, items 2 and 3).
- rev-5 · 2026-11-03 · §1 · S1 · S2 · S3 · S4 · S6 · S8 · S11 · S12 · S16 · S19 · §3 · §4 · §5 · AC1 ·
  AC2 · AC3 · AC8 · AC17 · the items unit 30's runs and unit 25's placement needed before they ran
  moved to those units (fix brief 2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief, items 2, 3
  and 5; unit 25 §8 F2). S8 (id 20) and S12 (id 34) are carried by unit 30 S7, and AC8 by unit 30
  AC5; S11's restatement of unit 30's AC1 (id 33) is carried by that AC1, S11 keeping the scored-clone
  read; S19 (id 37) is carried by unit 25 S9, and AC17 by unit 25 AC8. AC8 and AC17 leave this spec
  and §4's two blocks with them. S2, S3 and S4 read the records and the decision after the runs, S3's
  `(derived)` mark having no population once units 25 and 30 write the commit at call time; S6
  hardens the harness for other callers, unit 30's path being forward-slashed by its S7; S1 and AC1
  admit unit 30's README step. §3 takes a consumes-from edge on unit 25, whose record AC3 reads, and
  its first non-goal reads today's M4 (owner, 2026-11-01).
- rev-6 · 2026-11-04 · AC1 · the first half's predicate admits every `memory/` path, the generated
  renders the build-index hook forces into unit 30's commit `db0f99c71` (`memory/LIVE.md`,
  `memory/backlog/TOOL.md`) among them, and still reds on a product file (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-37-fix-brief, item 1).
- rev-6 · 2026-11-04 · AC1 · the second half's `<c35>` is unit 35's scoring commit, derived by
  `-G'^## Scoring$'` over unit 30's record, since unit 35 adds no manifest; `<c27>` is derived too, and
  the ancestry is read against `<c30>` as well (fix brief 2026-11-04-prompt-TOOL-dFairHearing-37-fix-brief,
  item 2).
- rev-6 · 2026-11-04 · S5 · §5 · §7 · the AC5 arm's staged break is S31's spelling after the verb,
  which exits 129 on today's code, in place of unit 32's commit, which already spells the option before
  the verb; S5 and §5 state that code as built (fix brief 2026-11-04-prompt-TOOL-dFairHearing-37-fix-brief,
  item 3).
- rev-6 · 2026-11-04 · S15 · §7 · the AC14 arm's staged break is the closer class narrowed to one
  character, in place of unit 32's `check_ungated`, which already reads a run; S15 states that code as
  built (fix brief 2026-11-04-prompt-TOOL-dFairHearing-37-fix-brief, item 3).
- rev-6 · 2026-11-04 · AC5 · the count greps the argv form `"--literal-pathspecs", "ls-files"`, which
  prints 1 at `8d58d785c`, where the string form printed 0 (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-37-fix-brief, item 4).
- rev-6 · 2026-11-04 · S4 · AC4 · `gotchas.py` exits 0 on an unknown flag at `8d58d785c`, so AC4's
  `selected` half is recorded superseded by `TOOL-dFairHearing-38` (§3) and graded on no exit here, and
  S4 names its argparse sentence as not holding (fix brief 2026-11-04-prompt-TOOL-dFairHearing-37-fix-brief,
  item 4).
- rev-6 · 2026-11-04 · AC2 · `attempts.py` is unit 35 §4's scratch checker; the empty `unscored`
  population is recorded `n/a`, and unit 32's AC12 is read from its builder return, its acceptance ledger
  being owed to the close (fix brief 2026-11-04-prompt-TOOL-dFairHearing-37-fix-brief, item 4).

## 10. Reuse audit

Every item extends a seam an earlier unit mints or the base tree carries: the harness's `repoFold` (`tools/workflows/tier2-review.template.js:652`),
`renderBlankedView` (`tools/hooks/agent-cap.js:529`), both at `9c1a2857a`, `resolve_kit_dir` and its behaviour arm
(`tools/lib/resolve_kit_dir.py`, `tools/lib/resolve-python.test.sh`), the syntax checker's
explicit-file mode (`tools/workflows/check-workflow-syntax.js`) and unit 35's attempt checker.
`python tools/codebase-map/reuse_lookup.py "normalise a repository path before pasting it into a git
command"` ranked the generic `git`, `run_git` and `path` stems and no path normaliser in the
workflows kit, so the fold reuses `repoFold`'s expression rather than a module. The recall query
returned `TOOL-aProbedUnit-11`, whose record that a clone under the scratchpad hits MAX_PATH is why
S8's clones sit under `$TEMP`, the audit's M8 item and unit 30's spec, and no prior per-arm procedure
in the README.

Recall terms used: `python tools/memory-recall/query.py "a replay clone path with backslashes pasted unquoted into git commands, and a status check that reads a failed call as clean" --terms "repo backslash cygpath clone path git -C status porcelain fails open per-arm replay README EXIT trap"`
