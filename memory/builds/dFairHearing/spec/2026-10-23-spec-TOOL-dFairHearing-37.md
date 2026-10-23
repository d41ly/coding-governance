# TOOL-dFairHearing-37 — the round-4 spec audit's 19 minors on units 30 and 32: one replay procedure that isolates each arm, criteria over the scored attempt, and checks that can go red

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 24 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-37-deviation-371.md](../build/2026-10-23-build-TOOL-dFairHearing-37-deviation-371.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md) | research | TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 |
| [2026-10-23-prompt-TOOL-dFairHearing-37-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-37-1-spec-writer.md) | journal | — |
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
unit it repairs. It makes each corrected statement true on what those units built, carries every
rule a later replay needs into the one replay procedure, and observes what each criterion claimed. A
criterion it supersedes is named by the hands-off bullet in that unit's §3, and that unit's
acceptance ledger records it superseded here (`TOOL-dFairHearing-23` §8 F7's form).

## 2. Scope (IN)

Each item names its report id, its report item, the unit it lands on and the criterion that observes
it.

- **S1** — id 1 (M1, unit 30). Unit 30 and unit 27 share order 21 and wrote the same files. The
  scoring, the decision and spec 15 S6's product files moved to `TOOL-dFairHearing-35` at order 22, so
  unit 30's commit writes only its verdict record and `--experiment` runs after unit 27 S7's rewrite of
  `check_held_out_frozen`. This item observes both. Observed by AC1.
- **S2** — id 2 (M2, unit 32). Unit 32's S20, S21 and AC12, for unit 15's replay, read unit 35's
  attempt rule instead of imposing a cap after the runs: a third completed attempt is `unscored` there,
  never a red here, and a `void after cap` record is unit 35's `no decision`. Unit 32 keeps their
  replay-1 half. Observed by AC2.
- **S3** — id 4 (M4, unit 32, AC9). A field unit 32 S14 appends to a record from git is marked
  `(derived)` on its line, and AC9's comparison grades only values a record held before that append.
  Unit 30's record held no orchestrating commit, so its line reads `(derived)` and AC9 reports it
  ungraded rather than passed. S8 captures the value at call time for every later replay. Observed by
  AC3.
- **S4** — id 5 (M5, unit 30, AC4). AC4's `selected` half is observed by behaviour, not by
  `grep -c -- "--all-ungated"`, which a docstring stating unit 23 S21's contract reds. When unit 35's
  record states `selected`, `gotchas.py --for-diff <range> --all-ungated` exits 2 with argparse's
  `unrecognized arguments`, so no flag shipped. This also answers unit 32 S13 and AC8, whose
  byte-identical comparison presumes the flag ships. Observed by AC4.
- **S5** — id 10 (M6, unit 32 S31, AC19). `check_held_out_frozen` in
  `tools/workflows/replay_scorer.py` runs `git --literal-pathspecs ls-files --full-name -- <path>`, the
  global option before the subcommand; the spelling in unit 32 S31 exits 129. AC19 gains a valid-path
  control. Observed by AC5.
- **S6** — id 12 (M8, unit 30). The harness takes `repo` with every backslash folded to `/` at its one
  read, `tools/workflows/tier2-review.template.js:180`, the fold `repoFold` (:491) already applies for
  its comparison. Every `git -C ${repo}` command an agent runs then carries a path bash cannot strip.
  The README's per-arm step (S8) builds the clone path with `cygpath -m`. Observed by AC6.
- **S7** — id 13 (M9, unit 32 S7, AC4). AC4's "neither reader changes" half reads the reader where unit
  12 S2 moved it: the body of `extract_section_ref` in `tools/workflows/replay_scorer.py`, sliced from
  its `def` line to the next top-level `def` or `class`, is byte-identical at unit 32's commit and its
  parent. This supersedes AC4's whole-file diff of `tools/workflows/review_replay.py`. Observed by AC7.
- **S8** — id 20 (M11, unit 30). The replay section of `tools/workflows/README.md`, the single source
  unit 32 S17 names, gains the per-arm steps unit 30 stated only in its own spec: one fresh clone per
  record and arm named `f<r><a><n>` under `$(cygpath -m "$TEMP")`, the status read as its own call with
  its exit checked before the clean test, a new clone per attempt, and the orchestrating repository's
  `git rev-parse HEAD` written to the run log at call time. Observed by AC8.
- **S9** — id 23 (M12, unit 32 S22, AC13). AC13's absence check reads the two `.js` files on the
  blanked view and, in a second pass, on every `${…}` interpolation inside a template literal, which
  `renderBlankedView`'s `tmpl` branch (`tools/hooks/agent-cap.js:1325-1328`) skips whole. A copy
  holding `` `x ${MAX_LENSES}` `` fails it. The residual: an identifier spelled at run time from
  pieces. Observed by AC9.
- **S10** — id 25 (M13, unit 32). `resolveKitDir`, which unit 32 S25 adds to `tools/hooks/agent-cap.js`,
  is a function the symbol tier lists, so `memory/map/generated/symbols.json` is regenerated with
  `python tools/codebase-map/gen_map.py --write` wherever `--check` reports it stale, and this unit's
  leg line carries `codebase-map coverage + freshness`. Observed by AC10.
- **S11** — id 33 (M17, unit 30, AC1). Unit 30's AC1 is restated over each record and arm's scored
  attempt as unit 35's checker names it: eight distinct scored clones, each with an empty observed
  status before its call, `HEAD` equal to its record's range head and exactly one untracked path, its
  report. Every other attempt is listed with its status and reason. Observed by AC11.
- **S12** — id 34 (M18, unit 30). S8's status step is
  `s=$(git -C "$c" status --porcelain --untracked-files=all) || { echo "status failed: $c"; exit 2; }`
  then `test -z "$s"`, so a status call that fails is a refusal and never a clean tree. Observed by
  AC8.
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
  end. Observed by AC14.
- **S16** — id 8 (L3, unit 32 AC14, AC10). AC14 is recorded evidence for unit 32 S23 under S14's
  computed precondition, and AC10's in-repository `git for-each-ref refs/replay/` half is a
  precondition, each so labelled in unit 32's ledger. NOT OBSERVED by a criterion here: it labels two
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
  replace the placement's. Observed by AC17.

## 3. Non-goals (OUT)

- No re-review, and no fold into the specs of units 30 and 32: each item makes the corrected statement
  true and reopens no severity.
- No re-run of a replay: unit 30's runs are read as they were made. An exposure S6 or S12 names in
  them is recorded beside the attempt, never re-run here.
- No HIGH finding: ids 22, 31 and 32 are `TOOL-dFairHearing-33`, `-34` and `-35`.
- No minor on units 28, 29 and 31: those 13 are `TOOL-dFairHearing-36`'s.
- No new gate leg: every arm lands in a suite that exists or that an earlier unit adds.
- No help page: `help/` covers neither the review harness, the scorer factory nor the hooks.

### Edges

- **consumes-from** `TOOL-dFairHearing-30` — the verdict record, its attempts and clones, and AC1, which S1, S6, S11 and S12 read or restate
- **consumes-from** `TOOL-dFairHearing-32` — S6, S7, S13, S14, S18, S20 to S23, S25, S26, S31, S32 and their criteria, which S2 to S5, S7, S9, S10 and S13 to S19 correct
- **consumes-from** `TOOL-dFairHearing-35` — the attempt rule and its checker, which S2 and S11 read for the scored attempt
- **hands-off** `TOOL-dFairHearing-38` — finding id 1 (item H1, shared with id 11) of the round-5 spec audit: S4's argparse sentence, its claim to answer unit 32 S13 and AC8, and AC4's `selected` half are superseded by its S2, S3, AC1 and AC2; AC4's `ungated` half stands
- **hands-off** `TOOL-dFairHearing-39` — finding id 11 (item H1, shared with id 1) of the same audit: AC4's argparse wording, cited in the bug-class catalogue as the form a criterion takes when it quotes an error text its tool never emits
- **hands-off** `TOOL-dFairHearing-40` — the same audit's minors on this spec, ids 4, 5, 8, 15, 18, 22, 28, 29, 30, 36, 37 and 38: AC11 over each scored clone, AC17's and AC5's counts, AC15's anchor, the per-arm step's variables and its orchestrating-commit read and log arm, AC9's view through `renderLexedView`, AC12's Red when half and the port's cure, the `ungated` class set re-derived after S15, the pass's write set counting its ledger record, and every `git -C ${repo}` quoted (its S10, S12 to S15, S17, S20, S23, S30, S31, S33 and S34)


## 4. Design

### Why two batch units

`TOOL-dFairHearing-36` §4 states the line: this half writes the workflows README, `replay_scorer.py`,
the harness template and render, `tier2-review.test.sh`, `gotchas.py`,
`tools/lib/resolve-python.test.sh`, `symbols.json` and two records, and reads neither suite that half
writes; that half defines no function, so `symbols.json` and its generator are this half's alone.

### The per-arm step (S6, S8, S12)

```bash
c="$(cygpath -m "$TEMP")/f<r><a><n>"          # forward slashes, so no shell strips the path
test ! -e "$c" || { echo "stale: $c"; exit 2; }
# the recipe over "$c" at the record's range head, with its exact-commit check
s=$(git -C "$c" status --porcelain --untracked-files=all) || { echo "status failed: $c"; exit 2; }
test -z "$s" || { echo "dirty: $c"; exit 2; }
echo "orchestrating $(git rev-parse HEAD) clone $c" >> "$SCRATCH/run.log"
# the harness call, `repo` set to "$c"; a refused attempt takes the next <n> and a new clone
```

On a host with no `cygpath` the line reads `c="$TEMP/f<r><a><n>"`, whose path already uses forward
slashes. Measured on 2026-10-23: `cygpath -m "$TEMP"` printed `C:/Users/DAILY-~1/AppData/Local/Temp`
here, and in a fixture whose `.git/index` was overwritten with seven bytes, `git status` exited 128
while `test -z "$(git status …)"` read the tree as clean.

### The placement's one trap (S19)

```bash
idx=$(mktemp -p "$SCRATCH")
trap 'rm -f "$idx"; git update-ref -d refs/replay/<name> 2>/dev/null' EXIT
# the placement of unit 32 S18, then the recipe with its own trap line taken out
```

### The harness's one read (S6)

```js
const repo = String(a.repo || '.').replace(/\\/g, '/')
```

A POSIX path holds no backslash, so the fold changes nothing there; on Windows git takes forward
slashes in every path argument. A refusal was weighed and declined: it would fail every caller that
passes a native Windows path today, for a value the harness can make safe in one place.

### Files touched (estimate)

- `tools/workflows/README.md`
- `tools/workflows/replay_scorer.py`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/memory-tree/gotchas.py`
- `tools/lib/resolve-python.test.sh`
- `memory/map/generated/symbols.json`
- `memory/builds/dFairHearing/build/`

`tools/workflows/tier2-review.js` is the template's render. `symbols.json` changes only where
`gen_map.py --check` reports it stale. Under the build folder only the two replay verdict records
change: S3's `(derived)` marks and S11's attempt listing.

### Alternatives rejected

- **Refuse a backslashed `repo` in the harness (S6).** §4 "The harness's one read".
- **Re-run unit 30's arms whose `repo` held a backslash.** A re-run is outside every unit after order
  21; the exposure is recorded, and S8 and S6 close the class for every later replay.
- **Keep AC13's view and add the interpolation case to S22's residual only (S9).** The case is a live
  code reference, so the probe reads it.

## 5. Production-readiness checklist

- security — S6 folds a path separator at the harness's one `repo` read and admits nothing new; the
  spec-kind `..` refusal after it (:486-489) still reads the folded value. No new write path.
- perf / scale — one string replace per harness call; one `git ls-files` per held-out path.
- error / empty / loading states — S12 makes a failed status a named refusal; S5 makes every held-out
  path resolve or exit 2 naming it.
- observability — the run log names the orchestrating commit beside each clone (S8).
- risks — S3 marks lines in two records written by earlier units, only where git derived the value.
- testing — scratch probes and fixtures per criterion; the §7 arms observed RED then GREEN at the close.
- migration — none for adopters beyond the harness's folded `repo`.
- user docs — `tools/workflows/README.md`, the replay section; there is no `help/` page (§3).

## 6. Acceptance criteria

`$SCRATCH` is the pass's scratch directory, and a clone or fixture repository goes under
`%TEMP%/<short name>`. Unit 30's record is
`memory/builds/dFairHearing/build/<date>-build-TOOL-dFairHearing-30-replay-verdict.md`.

- **AC1** — When `git show --name-only --format= <c30>` runs, where `<c30>` is the commit
  `git log --diff-filter=A --format=%H -1 -- <unit 30's record>` prints, every path it lists sits under
  `memory/builds/dFairHearing/`. `git merge-base --is-ancestor <unit 27's pass commit> <c35>` exits 0,
  where `<c35>` is the commit that adds unit 35's manifest.
  Red when: unit 30's commit writes a product file, or the scoring ran before unit 27's rewrite.
- **AC2** — When unit 35's `attempts.py` runs over unit 30's record, each `unscored` attempt it names
  is listed `unscored` in the record, and unit 32's acceptance ledger answers AC12's unit-30 clause as
  superseded by `TOOL-dFairHearing-37`. Replay 1's half of AC12 is answered in unit 32's ledger as it
  stands.
  Red when: unit 32's ledger reds AC12 on an attempt unit 35's rule never read.
- **AC3** — When `grep -n "orchestrating commit" <unit 30's record>` runs, its line ends `(derived)`.
  A scratch run of unit 32's AC9 probe over that record prints `orchestrating commit: derived, not
  graded`, and over unit 25's record it compares the recorded value.
  Red when: a value git derived after the fact is graded as evidence.
- **AC4** — When unit 35's record states `selected`, `python tools/memory-tree/gotchas.py --for-diff
  HEAD~1..HEAD --all-ungated` exits 2 and prints `unrecognized arguments`. When it states `ungated`,
  unit 35's AC4 answers this criterion.
  Red when: a `selected` verdict ships the flag.
- **AC5** — When `--experiment` runs with `heldOut` naming one tracked file, it exits 0 or reaches the
  freeze comparison. With `heldOut` naming a directory, and again a path holding `*`, each exits 2
  naming the path and its line count. Run in the workflows kit,
  `grep -c "git --literal-pathspecs ls-files" replay_scorer.py` prints 1.
  Red when: the valid path exits 2, which is the spelling that exits 129 refusing every path.
- **AC6** — When a scratch stub-agent run of `tools/workflows/tier2-review.js` is given `repo` as
  `C:\x\y`, every captured prompt's `git -C` command names `C:/x/y`, and no prompt holds a backslash
  inside that path.
  Red when: `tools/workflows/tier2-review.template.js:180` still reads `a.repo` raw.
- **AC7** — When the body of `extract_section_ref`, sliced as S7 states, is taken from
  `git show <c32>:tools/workflows/replay_scorer.py` and from `git show <c32>~1:tools/workflows/replay_scorer.py`,
  where `<c32>` is unit 32's pass commit, the two slices are byte-identical and neither is empty.
  Red when: unit 32 rewrote the scorer's section reading.
- **AC8** — When `grep -n "cygpath -m" tools/workflows/README.md` and `grep -n "status failed" tools/workflows/README.md`
  run, each prints a line in the replay section. A scratch run of that per-arm block over a fixture
  clone whose `.git/index` is overwritten exits 2 printing `status failed:` before any harness call,
  and over a clone holding one planted untracked file exits 2 printing `dirty:`.
  Red when: a failed status reads as clean.
  fixture: one clone under `%TEMP%/fcx`, made by the probe and removed after it.
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
- **AC17** — When the replay section's placement and recipe run in a fixture repository with
  `git bundle create` forced to fail, `git for-each-ref refs/replay/` prints nothing and no file is
  left in the temporary directory the placement made. `grep -c "trap " tools/workflows/README.md` counts
  one trap line in the replay section.
  Red when: the recipe's trap replaces the placement's and the temporary index survives.
  fixture: the repository under `%TEMP%/fpl`, made by the probe and removed after it.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `review-replay selftest` · `gotchas selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `workflow script syntax` · `codebase-map coverage + freshness` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC6 · a stub run whose `repo` holds backslashes, staged against the harness at `TOOL-dFairHearing-32`'s commit, where `repo` is read raw · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/workflows/replay_scorer.py (its runner, in the `review-replay selftest` leg) · covers AC5 · a held-out path naming one tracked file, staged against the factory at `TOOL-dFairHearing-32`'s commit · that runner's `ARMS_DECLARED`, raised by the arm added
New arm: tools/lib/resolve-python.test.sh · covers AC12 · a JS port testing `isDirectory()` for `.git`, and one letting `JSON.parse` throw · none
New arm: tools/memory-tree/gotchas.py (its selftest) · covers AC14 · a gated sentence closing on `.*)`, staged against `TOOL-dFairHearing-32`'s `check_ungated` · none

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

## 10. Reuse audit

Every item extends a seam an earlier unit mints or the base tree carries: the README replay section
(unit 23 S17, unit 27 S22, unit 32 S17), the harness's `repoFold` (`tools/workflows/tier2-review.template.js:491`),
`renderBlankedView` (`tools/hooks/agent-cap.js:1303`), `resolve_kit_dir` and its behaviour arm
(`tools/lib/resolve_kit_dir.py`, `tools/lib/resolve-python.test.sh`), the syntax checker's
explicit-file mode (`tools/workflows/check-workflow-syntax.js`) and unit 35's attempt checker.
`python tools/codebase-map/reuse_lookup.py "normalise a repository path before pasting it into a git
command"` ranked the generic `git`, `run_git` and `path` stems and no path normaliser in the
workflows kit, so the fold reuses `repoFold`'s expression rather than a module. The recall query
returned `TOOL-aProbedUnit-11`, whose record that a clone under the scratchpad hits MAX_PATH is why
S8's clones sit under `$TEMP`, the audit's M8 item and unit 30's spec, and no prior per-arm procedure
in the README.

Recall terms used: `python tools/memory-recall/query.py "a replay clone path with backslashes pasted unquoted into git commands, and a status check that reads a failed call as clean" --terms "repo backslash cygpath clone path git -C status porcelain fails open per-arm replay README EXIT trap"`
