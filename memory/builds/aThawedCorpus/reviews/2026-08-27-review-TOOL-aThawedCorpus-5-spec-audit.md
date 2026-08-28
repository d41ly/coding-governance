## Verdict: BLOCKED

**Serves:** spec-audit TOOL-aThawedCorpus-5 TOOL-aThawedCorpus-4 TOOL-aThawedCorpus-1 TOOL-aThawedCorpus-2 TOOL-aThawedCorpus-3

The two collapse units (`-4`, `-1`) and the one-line guard (`-5`) are the right shape and rest on
a real, directly measured defect; their problems are fixable in the spec text. The two deferred
units (`-2`, `-3`) are each blocked on a mechanism claim that source contradicts, and the build
folder itself will red the gate this build exists to speed up. Everything below was verified
against source in this worktree, or against `main`, at audit time — no finding here is an
inference from the specs alone. Five blockers, nine highs. The build should not start on unit `-5`
until B1 is cleared, because the very first commit of this build lands on a tree whose build index
is already stale.

## BLOCKER

- **`spec-TOOL-aThawedCorpus-5.md` is UNTRACKED, and the build README's generated regions are
  stale — front matter `ids:` line, the generated index, unit and order regions.** `git ls-files`
  does not list the `-5` spec, so it does not exist to any gate: not to check 21's set of ids a
  spec defines, not to check 23's population, and not to the build-index generator. Observed
  directly while filing this record — `gen_build_index.py --print-bindings` emits a `B` row against
  this very review, "TOOL-aThawedCorpus-5 is named but no spec H1 in this tree defines it", which
  is a check 21 failure caused by nothing but the missing `git add`. Downstream of the same cause,
  `gen_build_index.py --check` exits 1 naming the README stale: the front matter id list carries
  four ids and omits `TOOL-aThawedCorpus-5`, the generated index says four units, and the generated
  order table maps step 1 to `TOOL-aThawedCorpus-4` while the five spec status headers declare
  `order 1` through `order 5` with `-5` first. The authored unit table already lists five. So a
  builder reading the generated order builds the wrong unit first, and check 9 and check 21 both
  red on the first commit. **Fix:** track the `-5` spec, add `TOOL-aThawedCorpus-5` to the front
  matter id list, and re-run the generator with `--write`, all in one commit before any unit
  starts.

- **All five specs — status header, `base 4f406bf7`.** `memory/TEMPLATE-SPEC.md:69` requires
  `base` to be "the immutable default-branch sha the design was grounded against". `git branch
  --contains 4f406bf7` returns only this feature branch, so the pinned base is a commit this run
  itself wrote. The real grounding point is the merge-base `f5dff6ae`, and local `main`
  (`f1be0b49`) is 39 commits ahead of it. Inside that window `tools/gate-legs.json` and
  `tools/run-gates/run-gates.sh` both moved, which is exactly the surface `-2` and `-3` are
  specced against. **Fix:** re-pin every header to a default-branch sha, rebase the worktree onto
  it, and re-verify `-2` and `-3` against the run-gates and leg-manifest that actually ship.

- **`spec-TOOL-aThawedCorpus-2.md` — AC3, AC4, and §4 Rollout.** Guard-skip is decided before
  reuse and subsumes it. In `tools/run-gates/run-gates.sh` the guard pre-pass at `:762` runs
  unconditionally and writes `skip` for any guarded leg whose pathspecs are unchanged versus BASE;
  the reuse loop at `:855` begins `[ -f "$WORK/$i.rc" ] && continue` at `:858`. So a newly guarded
  memory leg can never print `GATE reuse` (AC3 is unobservable), and AC4's contrast is impossible
  — on a `tools/govkit/`-only commit both halves produce `GATE skip`. §4 Rollout's "No default
  changes" is false for the same reason: guard evaluation does not consult `GATE_REUSE`, so
  declaring a guard changes every bar that does not set `GATE_FULL`. **Fix:** restate §1 and the
  goal — the saving this unit buys is the guard-skip, not the reuse freeze — then rewrite AC3 and
  AC4 to grade guard-skip on a diff that misses the pathspecs and a real run on a diff that hits
  them, and delete the "no default changes" sentence.

- **`spec-TOOL-aThawedCorpus-4.md` — S3 against §4 Data model against §8 F2.** Three normative
  statements that cannot all hold. S3 puts the criterion-to-ledger membership map "in the same
  `awk` pass" as the spec prologue; §4 Data model says "The join stays in the shell"; F2 resolves
  the record pass and the spec pass to be two separate `awk` processes selected by different `git
  ls-files` patterns. The ledger triples S3 wants to look up are produced by the record pass, so
  the spec pass has nothing to consult. A builder cannot implement S3 as written. **Fix:** pick
  one. The cheapest consistent shape is to keep the join in the shell but replace the
  per-criterion `grep` with a single associative lookup built once from `$alledger`, and rewrite
  S3 to say that.

- **`spec-TOOL-aThawedCorpus-3.md` — §4 Data model against §8 F1.** The declarations file has two
  incompatible schemas in one spec. §4 fixes `spawn-ceilings.txt` as `<leg name>` TAB `<integer
  ceiling>`, one row per leg; F1 recommends a three-field row carrying "the corpus size it was
  measured at, on the same row" and closes with "Resolve before code". AC3 and AC4 both grade the
  file against the leg manifest, so the field count is load-bearing for the parser. **Fix:**
  resolve F1 in a `rev-2` and make §4 say the same thing, before code.

## HIGH

- **`spec-TOOL-aThawedCorpus-4.md` — S1 and S2, the ARGV file list.** One `awk` taking every path
  as an operand aborts the whole pass on the first path it cannot open, where today's per-file
  loop skips that path and continues. Verified on this node's GNU Awk 5.4.0: `awk '{print
  FILENAME}' f1 missing f3` prints `f1`, emits `fatal: cannot open file`, exits 2, and never reads
  `f3`. `git ls-files` enumerates the INDEX, so a tracked-but-absent path is a real operand — this
  same checker already carries a branch for that class at check 12's `M` tag. And an empty operand
  list makes `awk` read stdin instead of running zero times. **Fix:** feed the path list as a
  stream (the shape check 12's own driver already uses at `:775`), which resets per-record state
  without `FILENAME`/`FNR`, tolerates a missing path, and is a no-op on an empty list.

- **`spec-TOOL-aThawedCorpus-3.md` — §1, N1, §4 Alternatives rejected, §10.** The premise that
  this repo has no per-leg ceiling precedent in the leg manifest is false on `main`. `git show
  main:tools/gate-legs.json` carries a `ceiling` field on 85 of its 86 legs, `memory hygiene`
  among them at 1270, and `run-gates.sh` on `main` already reports how many legs that will run
  declare no ceiling. That is the "declare it or be reported" property S4 asks for, already built,
  in the file this unit edits. **Fix:** re-ground the unit on `main`, state what the spawn ceiling
  adds over the wall-clock ceiling that now exists, and declare a `ceiling` for the new leg.

- **`spec-TOOL-aThawedCorpus-3.md` — §2 Scope, §4 Files touched, §7.** `check-spawn-ceilings.sh`
  will define `fail()` and carry at least four red branches (AC2, AC3, AC4, AC6), and §4 lists no
  sibling `check-spawn-ceilings.test.sh`. `tools/memory-tree/check-arms.py:122` discovers a gate
  as any tracked non-`.test.sh` shell file that owns a `fail()` helper and has `fail <n> "` call
  sites; a missing sibling test means every branch is unarmed. §7 names `harness arms` as a gate
  this unit must keep green, so the unit reds the moment the file lands. **Fix:** add the sibling
  test to §4 Files touched, plus an `ARMS_FLOORS` row in `.memory-tree.conf` (it carries seven
  entries today).

- **`spec-TOOL-aThawedCorpus-3.md` — S2, S3, AC1, §5 perf.** The new leg's own cost is unpriced
  and is roughly the sum of every leg it grades. Sixteen legs in `tools/gate-legs.json` name
  `tools/memory-tree/` in their argv; S3 demands a row per leg, S4 reds an undeclared one, and S2
  obtains each count by executing that leg under the shim. Ten of the sixteen carry `chunk:
  selftests` and are held off the default bar by the 2026-08-23 owner ruling — this runner would
  run them anyway, and would run `memory hygiene` a second time on every bar. **Fix:** state the
  leg selector, exclude the held chunk or move the runner on-demand, and declare its ceiling.

- **`spec-TOOL-aThawedCorpus-5.md` — §5 risks, the compensating control.** `.githooks/pre-push`
  does not run an unconditional full bar. Verified at `:222`: it DECIDES, exporting `GATE_FULL=1`
  only on the force branch and otherwise exporting `GATE_BASE="$rec_sha"` for a scoped run, and
  only `GATE_FULL` bypasses guards. Once `TOOL-aThawedCorpus-2` declares a guard on `memory
  hygiene`, a scoped push whose diff misses `memory/` skips the leg outright — so the control that
  is supposed to compensate for the coverage this unit removes at pre-commit can itself be absent
  at push. Neither spec acknowledges the other. **Fix:** name the actual condition under which the
  full pass runs, and have `-2` state explicitly that its guard must not be the only thing
  standing between check 23 and never running.

- **`spec-TOOL-aThawedCorpus-2.md` — S3, AC1, AC2.** The arm has no way to read the value it must
  assert on. `input_key` is a shell function defined at `run-gates.sh:781`, after BASE resolution
  and the manifest parse; the script takes no arguments, exposes no print mode, and sourcing it
  runs the bar. Its only external surface is a field of a `<git-dir>/gate-ledger.tsv` row written
  at `:921` for legs that RAN — and a guard-skipped leg writes no row, which is precisely the
  state the over-declaration half of S3 must probe. S3's second clause is also stated with
  inverted polarity: "assert the key does NOT move" HOLDS while the pathspec is missing and FAILS
  once it is added, which is the opposite of AC2. **Fix:** add a `--print-key` mode to
  `run-gates.sh` as a scoped in-unit change, or re-scope the arm to grade the declaration against
  a derived reader list rather than against the key; and flip S3's second clause to match AC2.

- **`spec-TOOL-aThawedCorpus-2.md` — §1, S1, S2, §4 Inventory.** "The memory legs are excluded
  because they declare no `guard`" is false for nine of the sixteen memory-tree legs: the six
  self-test legs, `verdict-epoch self-test`, `row-keyed merge driver replay` and `kit/dogfood doc
  parity` all already carry one. Exactly seven are unguarded (`verdict epoch`, `method carriers`,
  `method-carriers self-test`, `build README slot contract`, `harness arms`, `memory hygiene`,
  `marker contracts`), and §4 Inventory derives the inputs of only one of them. §4 Inventory also
  omits `tools/memory-recall/`, which `corpus_ids.py:46` imports from and `kit.toml` declares as a
  conditional edge — the exact under-declaration this unit exists to prevent. **Fix:** name the
  seven-leg population explicitly, derive inputs for each, and add the recall path to the
  inventory.

- **`spec-TOOL-aThawedCorpus-1.md` — S2, N2, AC5; and `spec-TOOL-aThawedCorpus-4.md` — S4, §4.**
  The branch counts are wrong in both directions. `check-memory-hygiene.sh` has FIVE `fail 21`
  call sites (`:670`, `:673`, `:680`, `:683`, `:704`), of which only `:704` belongs to the
  projection loop this unit touches — so "keep the four `fail 21` branches" misnames the surface.
  AC5 is then unobservable: the projection has one `fail 21`, three outcomes feed its body, and
  the fourth outcome prints nothing by construction, which S1 itself says. On the other side,
  check 23 has THREE `fail 23` calls (`:1175`, `:1176`, `:1177`); the fourth item `-4` S4 lists is
  the liveness `printf` at `:1178`, which is not a `fail` branch and is not in the arms
  population. **Fix:** correct both counts, and restate AC5 as "the three projection message lines
  still appear inside the single `fail 21` body, and a conformant record still contributes none".

- **`spec-TOOL-aThawedCorpus-4.md` §1 and `spec-TOOL-aThawedCorpus-5.md` §4 — the corpus
  figures.** Measured now in this worktree: `git ls-files 'memory/builds/*/spec/*.md'` is 321, not
  "~250" and not "317"; check 23's own ledger population, `build/` plus `reviews/`, is 308, not
  "310" and not "307". The 310 figure is check 21's `build|prompts|reviews` population, a
  different set that check 23 does not read. The spec count is understated by about 22% in three
  documents, which understates the per-spec prologue's spawn total by the same margin. **Fix:**
  re-derive both figures and say which check each belongs to.

## MEDIUM

- **`spec-TOOL-aThawedCorpus-4.md` — §4 Data model, the spec-pass filter list.** It says "a status
  header in the first six unfenced lines". Source at `:1141` is `sed -n '1,6p' | grep -m1
  '^\*\*Status:\*\*'` — the first six RAW lines, no fence tracking. The checker has an unfenced
  reader at `:200` and check 12 uses it; check 23 deliberately does not. A builder who implements
  unfencing moves the verdict, which the build-level rules forbid. **Fix:** say "raw lines".

- **`spec-TOOL-aThawedCorpus-4.md` — §4 Data model, and S5.** The ordered filter list stops at "an
  `H1` id" and never mentions `ACCEPTANCE_LEDGER_GRANDFATHER`, which sits at `:1153`, after the id
  is read and before `alpop=$((alpop + 1))` at `:1154`. A grandfathered spec is therefore excluded
  from the population COUNT as well as the label loop, which is what makes the liveness line
  honest. **Fix:** add the grandfather filter to the list, in position, and say where `alpop`
  increments.

- **`spec-TOOL-aThawedCorpus-4.md` — S2, S3, S4, AC1.** Two ordering properties are load-bearing
  and unstated. Per-spec labels come from `awk ... | sort -u` at `:1160`, so the loop iterates
  deduplicated, collation-sorted labels, and that order is what builds the `$algap` and `$albad`
  strings printed verbatim in the failure texts — file order differs from sorted order for every
  spec that reaches AC10. And the ledger lookup is `grep -m1`, FIRST match wins, where an `awk` or
  bash associative array is LAST write wins. **Fix:** pin both in S2 and S3.

- **`spec-TOOL-aThawedCorpus-4.md` — AC1; same shape at `spec-TOOL-aThawedCorpus-1.md` AC1.** The
  byte-identity oracle is one-sided over this corpus. Check 23 emits nothing today except the
  liveness line, which is itself suppressed while the population is non-empty, so a stdout diff
  can catch a regression that ADDS output but cannot catch one that drops a true finding. **Fix:**
  run the diff over a scratch corpus seeded with one instance of each outcome as well as over the
  real one, and say so in AC1.

- **`spec-TOOL-aThawedCorpus-2.md` — §8 F1's liveness clause.** F1's decision rule turns on "the
  shell half is 34 s of set checks TODAY", but after `-4` and `-1` land, checks 21 and 23 are
  still shell checks reading `memory/` and belong to the same guardable half, at their own targets
  of under 30 s and under 60 s. The guardable half after the collapse is therefore around 120 s,
  not 34 s, which lands in the "materially larger, declare the guard" branch and makes the stated
  live negative not live. **Fix:** restate the figure with the post-collapse composition, or move
  the threshold.

- **`spec-TOOL-aThawedCorpus-3.md` — S5 and §5 observability.** The declared coverage mode names
  the wrong gap. It says the count is a lower bound "because shell builtins and absolute-path
  invocations do not traverse `PATH`" — true, but the class it omits is half of what this build
  measured: a `$( )` command substitution and every pipeline stage FORK a subshell with no `exec`,
  and a `PATH` shim cannot see a fork. This build's own measurement record attributes check 21's
  cost to a command substitution plus a `grep`, and a pipeline subshell plus `tr` and `grep`.
  **Fix:** add forks to the announced lower-bound statement.

- **`spec-TOOL-aThawedCorpus-3.md` — S1, S5, N2 (Windows).** The shim is extensionless shell
  wrappers on a `PATH`-prepended temp dir, and two counted checkers reach `git` from Python:
  `corpus_ids.py` and `check-arms.py` call it through `subprocess`. On Windows a bare name
  resolves through `CreateProcess`/`PATHEXT`, which will not execute an extensionless text wrapper
  — `corpus_ids.py` already documents that exact trap. **Fix:** ship `.cmd` wrappers alongside, or
  declare Python-launched spawns as an announced dark class.

- **`spec-TOOL-aThawedCorpus-3.md` — §4 Files touched, §10.** `spawn-ceilings.txt` would ship to
  adopters with this repo's measured values. The kit's catch-all rule is `include = "**"` with
  `role = "engine"`, so a new file under `tools/memory-tree/` ships verbatim unless an earlier row
  claims it; `build-readme-slot-limits.txt`, the shape §10 copies, is declared `role = "seed"` for
  precisely this reason. That is the copied-pin defect N3 warns about, one file over. **Fix:**
  declare the new file as a seed row in `kit.toml` and say so in §4.

- **`spec-TOOL-aThawedCorpus-3.md` — AC6 against §5 error states.** §5 defines the vacuous case as
  "a count of zero with a NON-EMPTY shim list". AC6 stages the break by EMPTYING the shim list,
  which is a different condition and would pass a correct implementation of §5. **Fix:** stage the
  break by pointing the shim at a command the leg never calls, or restate §5.

- **`spec-TOOL-aThawedCorpus-2.md` — §4 Files touched and §7.** §7 names `govkit selfcheck` as a
  gate to keep green, but Files touched lists no `tools/govkit/registry.toml` entry for the new
  arm, and the new leg is declared with no `chunk` and no `subject`. `run-gates.gov.test.sh` reds
  a leg whose chunk is outside gov's declared set. **Fix:** add both to Files touched. The same
  omission applies to `-3`'s new leg.

- **`spec-TOOL-aThawedCorpus-2.md` — S2, N4, §4 Files touched.** Declaring the guard only in
  `tools/gate-legs.json` does not reach adopters. An adopter's `memory hygiene` leg is emitted
  from `tools/memory-tree/kit.toml`'s own gate-leg block, which carries `guard = []`, and the
  emitter resolves guards through `{kit}`/`{memory_root}`/`{prefix}` substitution. A pathspec
  written as gov's literal `memory/` would be wrong in a target with a different memory root.
  **Fix:** declare the guard in the kit descriptor with the token form, and let the gov manifest
  be rendered from it.

- **`spec-TOOL-aThawedCorpus-5.md` — AC3.** The staged fixture trips a different check first.
  Staging a spec under a build folder moves the generated build index, and check 9 runs under
  `--staged` whenever any `memory/**` path is staged — which is the only case in which the
  pre-commit hook invokes the leg at all, as this spec's own N2 records. The `--staged` run reds
  on check 9 before check 23's absence can be observed. **Fix:** state the fixture construction,
  and regenerate the index in the staged set so check 9 is green.

- **`spec-TOOL-aThawedCorpus-5.md` — S2 and AC1; also `-4` AC3 and `-1` AC3.** The cleanliness
  predicate counts the wrong process class. AC1 verifies "three or fewer live `bash` processes",
  but the contamination this build's own measurement record documents, and which forced the
  withdrawal of the 913 s reading, was forty-odd `python.exe` processes from another project. A
  `bash` count would have read clean throughout. **Fix:** make the predicate the foreign
  `python.exe` count the measurement record already established, and keep the `bash` count as a
  secondary line.

- **`spec-TOOL-aThawedCorpus-3.md` — §1 and §10, "hand-fixed five times".** The measurement record
  this build rests on says two prior hand-fixes (`TOOL-aBatchedLintel-1` for checks 12 and 7, and
  `TOOL-aCollapsedScan-1`), with checks 21 and 23 as the still-unfixed instances. **Fix:** cite
  the record's count rather than a rounded one; the argument does not need the larger number.

- **All five specs — §10 Reuse audit.** Every one records the identical `reuse_lookup.py` query
  about skipping an unchanged build folder — the cache question the build README explicitly says
  it is not answering. For `-3` the conclusion is load-bearing: "surfaced no existing
  spawn-counting seam" rests on a query that never asked about spawn counting, process budgets or
  per-leg ceilings, and a query that did would have found the ceiling field now on `main`.
  **Fix:** re-run `-3`'s audit with terms for its actual subject.

## LOW

- **`spec-TOOL-aThawedCorpus-1.md` — §1.** "four to six processes for each of 310 records": the
  loop iterates the `S` rows of `--print-bindings`, which this build's measurement record counts
  at 301. 310 is check 21's file population, a different set.

- **`spec-TOOL-aThawedCorpus-1.md` — §4 Alternatives rejected, N1, §7.** "deferred to unit 3" and
  "unit 3 owns the ceiling" now read ambiguously: since `-5` was added, the roster ordinals no
  longer match the id ordinals — roster position 3 is `TOOL-aThawedCorpus-1` and position 5 is
  `TOOL-aThawedCorpus-3`. Cite ids, never positions.

- **`spec-TOOL-aThawedCorpus-4.md` — §4 Alternatives rejected.** The stated ground for rejecting
  the stream form ("a stdin stream has neither `FILENAME` nor `FNR`") is disproved by the seam §10
  names as the one being extended: check 12's driver IS a stdin stream and resets its per-record
  state without either. Folded into the HIGH above; noted here so the sentence gets deleted rather
  than merely overridden.

## What was refuted and why

- **"The Windows command-line limit breaks the ARGV form."** Measured: the record path list is
  27,764 bytes over 308 paths and the spec list is 24,369 over 321, against a `CreateProcess`
  limit of 32,767. Under it today, so this is not itself a break. It stands only as supporting
  evidence for the stream fix in the HIGH above, and it does say the ARGV form has roughly one
  corpus-growth cycle of headroom left.

- **"`-2` AC1 is a tautology."** Partly fair — `input_key` is defined over the leg's own guard
  pathspecs, so a byte changed under a declared pathspec moves the key by construction, and the
  one residual mode (a pathspec matching nothing tracked) is the run-gates canary's job, which §5
  already names as covered upstream. But AC1 is not the defect; the defect is that the arm cannot
  read the key at all, which is carried as a HIGH. Fixing that subsumes this.

- **"`-2` AC6 asserts the negation of what a guard does."** True as literally worded, and it is
  already inside the AC3/AC4 blocker: once those are rewritten around guard-skip, AC6's "no check
  became unreachable" has to be rewritten with them. Not raised separately, and it should not be
  re-raised as its own item. The related observation that the checker prints nothing per green
  check, so there is no roster of executed checks in its output to diff, is real and belongs in
  the same rewrite.

- **"The absolute wall-clock figures may be wrong."** Known and recorded — the box was contended
  and the numbers are being re-taken. Not a finding. What IS carried above is the derived-count
  errors (spec and record populations, branch counts, spawn-loop cardinality), which are wrong
  independently of any clock.

- **"The build should build a cache."** Out of scope by the build README's own rule, and correctly
  so: `run-gates.sh`'s `input_key` plus `GATE_REUSE` already is one. No finding proposes building
  a second.

- **"`-2` and `-3` may be dropped on their own probes."** Deliberate and recorded in the README.
  The blockers against them are not "these units are unnecessary" — they are "if these units are
  built, they cannot be built as written". If either closes as a documented refusal on its probe,
  its blockers close with it.

- **"`-4`'s rejection of moving check 23 into Python is wrong."** Not raised. The reasoning holds:
  `check-arms.py` discovers fail branches from tracked shell, and `.memory-tree.conf` pins this
  file at `20:20`. The `awk` choice is correct.
