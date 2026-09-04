# TOOL-aSurfacedLexicon-3 — one corpus walk, two passes, two fewer modes

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Delete the `--brief` and `--probe` modes with the `DEAD_TOKENS` constant they carry, collapse the
duplicated corpus walks into one `scan_corpus` generator, and split the 278-line `run()` into a
measurement pass and a verdict pass. The two-mode duality inside one function has produced three
separately documented armed-but-unreachable defects, each fixed by hoisting code above a `return`,
and all three confessions are still in the source.

## 2. Scope (IN)

- **S1** — Delete `run_brief` and its four helpers from `tools/lexicon/lexicon.py`:
  `read_object_state`, `read_token_is_live`, `read_object`, plus the `DEAD_TOKENS` and
  `MIN_LIVE_TOKEN` constants. Measured at 166 lines by AST spans at writing time.
- **S2** — Delete `run_probe`, measured at 84 lines by the same method.
- **S3** — Drop `--brief` and `--probe` from the `main` dispatcher at
  `tools/lexicon/lexicon.py:1164-1197`, including the mode tuple, the usage block and the
  argument-count guard that special-cases them.
- **S4** — Add `scan_corpus(root, declared)`, one generator yielding each armed file with its
  extracted definitions, and route every surviving walk through it.
- **S5** — Split `run()` into a measurement pass returning counts and refusals, and a verdict pass
  consuming them. Neither `--check` nor `--measure` may read a refusal the other cannot.
- **S6** — Delete the 23 self-test arms in `tools/lexicon/selftest.py` covering the deleted modes and
  constants, and add the differential arm named in §6.
- **S7** — Delete the stopword parity arm at `tools/codebase-map/selftest.py:1305-1313`, in this same
  commit. Rev-1 cited `:1268-1276`, which sits inside a DIFFERENT arm's docstring; the parity
  assertion opens at `if lx.DEAD_TOKENS != m._STOPWORDS:` on `:1305`, per
  `grep -n DEAD_TOKENS tools/codebase-map/selftest.py`.
- **S8** — Repair the Skill surface: the `{{BRIEF_CLI}}` substitution at
  `tools/lexicon/adopt-lexicon.sh:110`, the placeholder array at `tools/lexicon/kit.toml:38`, the
  `description` line and the routing block at `tools/lexicon/SKILL.template.md:3` and `:30`, and the
  re-rendered `.claude/skills/lexicon/SKILL.md`.
- **S9** — Repair the prose carriers: `tools/lexicon/README.md:107` and `:115`, and
  `tools/lexicon/LEXICON.md:45`. The README also gains the SURVIVING pre-adoption route ratified in
  §8 — `python tools/lexicon/scaffold_lexicon.py <path-outside-the-repo>` — written as a route a
  reader can run, not as a record of a lost capability.

## 3. Non-goals (OUT)

- Deleting P3, the `LAYERS` block or the layer waiver file. That is the sibling unit at the same
  build order, and this unit does not touch the third predicate beyond the walk it shares.
- Changing any predicate's verdict. Every surviving output line is byte-identical, which is the
  point of §6 AC1 and is what makes this unit safe to land first.
- Wiring `--suggest` to the canon, or adding `--as <cell>`. The Skill loses one of its two routes
  for the units between this one and the one that adds the cell-aware suggestion, and that is stated
  rather than hidden.
- Replacing the pre-adoption reading `--probe` provided. See the fork in §8.
- Touching `extract`, `extract_text` or `_python_defs`. `scan_corpus` calls `extract`; it does not
  change it. Their signatures are frozen by contract for `drift_report.py`.
- Any change to `map_lib._STOPWORDS`. This unit deletes the lexicon's restatement of that set, not
  the set.

## 4. Design

### Inventory

Measured on this worktree at writing time by AST spans over `tools/lexicon/lexicon.py` and by
`grep -c` over the self-test.

| What dies | Size | Note |
|---|---|---|
| `run_brief` | 134 lines | the largest function in the file after `run` |
| `read_object_state`, `read_token_is_live`, `read_object` | 29 lines | `--brief` is their only caller |
| `DEAD_TOKENS`, `MIN_LIVE_TOKEN` | 3 lines | a restatement of `map_lib`'s set and its length rule |
| `run_probe` | 84 lines | |
| Self-test arms for the above | 23 of 140 | `grep -c` over `tools/lexicon/selftest.py` |
| Cross-kit parity arm | 9 lines | `tools/codebase-map/selftest.py:1305-1313` |

Two hundred and fifty engine lines, and the deletion also removes a second copy of a neighbour kit's
data. `DEAD_TOKENS` exists only because the declared layer rule forbade importing `map_lib`, so the
lexicon restated 21 words inline and a cross-kit arm asserted the two never diverge. Deleting the
restatement retires the fact-in-two-places rather than continuing to gate it.

### Data model

**`scan_corpus(root, declared)`** yields one record per armed file: the repo-relative path, the
extension, and the extracted triple of functions, types and imports. It owns the four behaviours the
call sites currently re-derive, and re-derive differently: filtering to declared extensions, skipping
`dark` and unshipped pattern sets, calling `extract`, and deciding what an extraction error means.
That last one is the divergence that matters. `run()` turns a `SyntaxError` into a named refusal,
while `run_probe` and both `scaffold_lexicon.py` walks swallow it, so the same unparseable file is a
gate failure in one reader and invisible in three.

There are FIVE walks today, not the four the research record names, and the fifth is live. They are
`tools/lexicon/lexicon.py:550` in `run()`, `:994` in `run_brief`, `:1076` in `run_probe`,
`tools/lexicon/scaffold_lexicon.py:124` in `main`, and `:70` in `_measure_suffix_offenders`, which
`main` calls at `:143`. Two die with their modes, leaving three call sites for `scan_corpus`. The
correction matters because a collapse spec naming four would leave the fifth walking the corpus on
its own, which is the shape being removed.

**The two passes.** `measure_pass` walks the corpus once and returns the graded counts, the offender
lists per predicate, and the refusal list. `verdict_pass` consumes that and decides. `--measure`
prints the pins plus the refusals; `--check` prints the counts, the pin verdicts and the same
refusals. One reader of the refusal set, so there is no path on which one mode can see a refusal the
other cannot.

That is the class the current file confesses to three times, at
`tools/lexicon/lexicon.py:624-632`, `:654-663` and `:738-745`. Each confession describes the same
shape: a refusal written below the `measure_mode` return, therefore reachable from `--check` and not
from `--measure`, therefore a mode that could not fail while its sibling redded the same tree by
name. Each was repaired by moving code above the return, which is a fix to one instance and leaves
the next author one `return` away from re-earning it.

**The live population of that defect today is zero, and this unit does not claim otherwise.** All
three were repaired. Verified by staging a stale waiver row into a temporary fixture repo and
running both modes: `--check` exits 1 and `--measure` exits 1 printing
`# NOTE:` with `STALE WAIVERS` and `UNDECLARED EXTENSIONS` beneath it. So the acceptance for this
half is a STAGED break rather than a tree observation, and §6 says so.

### Migration

`--brief` and `--probe` are removed from a shipped CLI, so every carrier of their spelling has to
move in the same commit. `grep -rn -- "--probe|--brief"` outside `memory/` finds them in the kit
engine, the kit self-test, `tools/lexicon/adopt-lexicon.sh:110`, `tools/lexicon/kit.toml:38`,
`tools/lexicon/SKILL.template.md`, `tools/lexicon/README.md`, `tools/lexicon/LEXICON.md`, and the
rendered `.claude/skills/lexicon/SKILL.md`.

The `lexicon wiring` leg carries `guard: []`, so it runs on every bar and byte-compares the rendered
Skill against a fresh render. A template edit that is not re-rendered reds immediately, and a
placeholder dropped from `tools/lexicon/kit.toml:38` without the matching template edit reds too.
The transition's tripwire is therefore already installed and needs nothing new.

The cross-kit deletion is different and is the one that can be missed. `codebase-map kit selftest`
names `tools/lexicon/` in its guard, so a lexicon-only commit does select it — but its chunk is
`selftests`, `.githooks/pre-push` sets `GATE_FULL` and not `GATE_SELFTESTS`, and no boundary sets
the latter. A miss will not surface at the push that caused it. S7 lands in this commit or the
neighbour kit is broken behind a leg the push bar never runs.

**Deleting `run_probe` orphans an import, and nothing in this repo would notice.**
`grep -n 'canon\.' tools/lexicon/lexicon.py` returns only lines inside `run_probe`, so
`import canon  # noqa: E402` at `tools/lexicon/lexicon.py:84` loses its last caller in this commit.
Unit 11 gives it one again at build order 6, and there is no python lint leg on this bar that would
red a dead import in between. The remedy is decided in this commit rather than discovered later:
either keep the import with a one-line comment naming the unit that restores its caller, or delete
it here and re-add it there. Silence is not an option, because silence is exactly what the tooling
will give.

**The deletion also forecloses the cheapest route for a unit that is not being built.** `run_probe`
at `tools/lexicon/lexicon.py:1053-1136` already implements unit 10's S3 candidate computation and
its S4 unruled tail, in S4's own framing, and unit 10 sits at build order 6 — so deleting these 84
lines makes unit 10 re-implement roughly two thirds of them. Unit 10's own F1 is PARKED for an owner
turn, no option having survived its veto ladder, so unit 10 is not built by this run. This unit
lands FIRST, which is why the consequence is written here: the owner turn is owed BEFORE this
deletion lands if the owner wants that route preserved.

### Rollout

One commit, no flag. A deleted CLI mode cannot ship dark, and the Skill render must agree with the
template at every commit because the wiring leg compares them on every bar.

### Files touched (estimate)

`tools/lexicon/lexicon.py`, `tools/lexicon/selftest.py`, `tools/lexicon/scaffold_lexicon.py`,
`tools/lexicon/adopt-lexicon.sh`, `tools/lexicon/kit.toml`, `tools/lexicon/SKILL.template.md`,
`tools/lexicon/README.md`, `tools/lexicon/LEXICON.md`, `.claude/skills/lexicon/SKILL.md` and
`tools/codebase-map/selftest.py`. Ten files, no deletions and no additions.

### Alternatives rejected

**Keep `--brief` and only collapse the walks.** Rejected because `--brief` is the corpus-as-authority
direction the canon exists to close: it reports how this tree already spells a concept, which is the
input a naming decision must not take. It is also the second-largest function in the kit and the
owner of two of the five walks.

**Keep `--probe` for the pre-adoption reading.** It is not the only such reading — rev-1 said it was
and that was wrong. `python tools/lexicon/scaffold_lexicon.py <path-outside-the-repo>` gives one
without writing into the target, measured in §8. The cost is real but smaller than rev-1 priced it,
and it is the fork in §8 rather than an alternative dismissed here.

**Split `run()` without deleting the modes.** Rejected as more work for less: `run_brief` and
`run_probe` own two of the five walks and 23 of the 140 self-test arms, so splitting first means
restructuring code that is about to be deleted.

**Leave `DEAD_TOKENS` and its parity arm alone.** Rejected because the restatement exists only to
satisfy an import ban, and the arm gating it lives on a leg the push bar does not run. One fact in
one place is cheaper than a gated copy, and cheaper still than a gated copy nobody's push executes.

## 5. Production-readiness checklist

- security — N/A. No write path, no untrusted input, no egress. This unit only deletes read paths.
- perf / scale — one corpus walk replaces up to two per invocation on the `--check` path, and
  `scaffold_lexicon.py` drops from two walks to one. The `lexicon naming predicates` leg keeps its
  300 s ceiling and the `lexicon selftest` leg its 880 s ceiling; neither is renegotiated here.
- a11y — N/A. A command-line checker with no user interface.
- i18n — N/A. No user-facing strings beyond the checker's own English diagnostics.
- error / empty / loading states — `scan_corpus` owns the extraction-error policy for all three
  remaining callers, and it takes `run()`'s policy: an unparseable file in an armed language is a
  named refusal, never a silent skip. That is a behaviour change for `scaffold_lexicon.py`, which
  swallows it today, and it is deliberate.
- observability — the surviving output lines do not move. §6 AC1 pins that as a byte comparison
  rather than an eyeball.
- risks (concurrency, data-loss, rollback hazards) — three hazards, none of them touching data. The
  cross-kit arm deletion is invisible to the push bar, for the reason given under Migration.
  Deleting `run_probe` orphans `import canon` at `tools/lexicon/lexicon.py:84` with no lint leg on
  this bar to catch it. And the same deletion forecloses unit 10's cheapest route while unit 10's
  fork is parked for an owner turn. No state is written and rollback is a revert.
- testing + left-shift gates — the differential arm in §6 AC4 is the left-shift: it gates the CLASS
  the three confessions describe rather than the three instances already repaired.
- migration / rollback — covered under §4 Migration. Reversible by revert.
- user docs — `tools/lexicon/README.md` and `tools/lexicon/LEXICON.md` lose their `--brief`
  sections, and the rendered Skill loses one of its two routing blocks. The README gains the
  surviving pre-adoption route, `python tools/lexicon/scaffold_lexicon.py <path-outside-the-repo>`,
  which reads a repo without writing into it.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --check` runs before and after this unit on the
  same tree, every surviving line is byte-identical, compared with `diff` against a baseline file
  captured on the branch point. The pre-edit output is six lines; the `P3 layer` row belongs to the
  sibling unit and is excluded from this comparison rather than counted as a change here.
- **AC2** — When `python tools/lexicon/lexicon.py --measure` runs before and after this unit on the
  same tree, its pin lines are byte-identical by the same `diff`.
- **AC3** — When `python tools/lexicon/lexicon.py --brief <path>` or
  `python tools/lexicon/lexicon.py --probe` is run, the dispatcher prints its usage block and exits
  2, naming neither flag among the modes it accepts.
- **AC4** — When a refusal reachable only from the measurement path is staged into
  `tools/lexicon/lexicon.py`, a new differential arm in `tools/lexicon/selftest.py` REDS by naming
  the `--check` and `--measure` refusal sets as unequal; when the stage is reverted, the same arm
  greens. Both states are observed and recorded, because the live population of that asymmetry is
  zero today and an unstaged arm would be an assertion about nothing.
- **AC5** — When `python tools/codebase-map/selftest.py` runs with its `DEAD_TOKENS` arm deleted, it
  is green, and `grep -c DEAD_TOKENS tools/codebase-map/selftest.py` returns `0`.
- **AC6** — When `python tools/lexicon/selftest.py` runs, it is green and its printed arm count
  equals what `grep -c "check(" tools/lexicon/selftest.py` reports on the landed tree. The expected
  number is RECOMPUTED by that grep at build time and is never carried from a figure typed into this
  spec. Rev-1 asked for a drop "by exactly the arms S6 removes" and inherited an off-by-2: it
  counted 4 probe arms where `grep -n -- "--probe\|run_probe" tools/lexicon/selftest.py` returns
  TWO, at `:744` and `:746`. Any arithmetic anchored to a spec-side constant inherits that class of
  error, so the criterion is written to derive its own expectation.
- **AC7** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs, the `lexicon wiring` leg is
  green, which asserts `.claude/skills/lexicon/SKILL.md` byte-compares against a fresh render after
  `BRIEF_CLI` left `tools/lexicon/kit.toml:38`.
- **AC8** — When `grep -rn -- "--brief" --include=*.py --include=*.sh --include=*.md .` runs outside
  `memory/`, the only hit is the unrelated `tools/unattended/` flag of the same spelling in
  `.claude/skills/unattended/SKILL.md:504`.
- **AC9** — When `scan_corpus` is the only corpus walk left, `grep -c "for rel in files"`
  over `tools/lexicon/lexicon.py` and `tools/lexicon/scaffold_lexicon.py` accounts for no walk
  outside it, and `bash tools/check-dead-paths.sh` plus
  `bash tools/check-testsuite-counts.sh` are green.

## 7. Gates

`lexicon naming predicates`, `lexicon wiring`, `lexicon selftest` and `codebase-map kit selftest`
under `GATE_SELFTESTS=1`, `dead-path carriers (deleted files still named)`,
`testsuite counts (every bar self-test prints one)`, and the memory-tree hygiene leg. This unit adds
no new gate leg and no new ceiling. It adds one self-test arm to an existing suite, so no
`memory/project/testsuite-count-waivers.txt` row is owed.

## 8. Open questions

**F1 — `--probe` is the only pre-adoption reading the kit has. Delete it, or replace it?**
`run_probe` is documented as legal against a repo with no declaration at all, read-only, and
unconditionally exit 0, with two self-test arms at `tools/lexicon/selftest.py:744` and `:746`
asserting exactly that. The research record calls it derivable from `--measure` plus the canon, and
that is true of the numbers but not of the entry condition: `run()` prints `NOT ADOPTED` and returns
0 when `.lexicon.conf` is absent, so `--measure` answers nothing on an unadopted repo.

Three claims rev-1 made in this fork were wrong, and correcting them is what carries the pick rather
than weakening it.

`--probe` is NOT the last pre-adoption route. Rev-1 said the only remaining one was `--scaffold`,
"which writes a file"; it need not. `python tools/lexicon/scaffold_lexicon.py <path-outside-the-repo>`
gives the same reading and writes nothing into the target, because `scaffold_lexicon.py:105-107`
takes `dest = Path(argv[1])` while `:106` derives `root` from `git rev-parse --show-toplevel`
INDEPENDENTLY of `dest`. Measured end to end in a conf-less throwaway repo: the full reading printed,
`git status --short` unchanged, no `.lexicon.conf` created.

The adopter population is NOT zero. A `python -c` read of
`tools/govkit/fixtures/incms-2cff5855.receipt.json` counts 52 rows over 11 kits, 11 of them
`kit: "lexicon"` at prefix `scripts/lexicon/`. Rev-1's "the measured adopter population this build
could read is zero" is therefore struck, and every argument that leaned on it goes with it.

The probe arms are two, not four; `grep -n -- "--probe\|run_probe" tools/lexicon/selftest.py`
returns `:744` and `:746`. The 84 lines are exact, by AST span.

Option A deletes `--probe` and records the SURVIVING route in `tools/lexicon/README.md`. Option B
keeps the entry condition by letting `--measure` fall back to the shipped `KNOWN_EXTS` defaults when
no declaration exists, which is a few lines but emits pins that mean nothing without a table.
**Recommendation: option A, with the surviving route written into the kit README rather than left
for an adopter to discover.**

One appeal in rev-1 is UNVERIFIABLE and is kept only as a note, not deleted: the charter rule that a
deliberate exemption is documented together with its compensating check quantifies over GATE
exemptions, and a deleted CLI mode is not one. Nothing in this fork rests on it.

**RESOLVED (agent, 2026-09-04, delegated): F1 — option A, delete `--probe` and record the
pre-adoption reading in the kit README; the README names the SURVIVING route, not a bare loss.**

Option B falls to veto 1. §3 Non-goals lists verbatim "Replacing the pre-adoption reading `--probe`
provided. See the fork in §8", and option B is that replacement. Everything measured downstream
confirms the discard rather than fighting it. With the exact fallback patched in (`conf = {}`,
`declared = dict(KNOWN_EXTS)`, skipping the NOT ADOPTED return), `--measure` exits **rc 1** — before
and after the sibling unit removes P3 — because `UNDECLARED EXTENSIONS` fires for every extension
outside `{py, js}`. `--probe`'s documented contract is "EXITS 0 UNCONDITIONALLY", so B loses the one
property that justifies it, and buying that property back means suppressing `problems` on the
no-conf path, manufacturing a mode that cannot fail — the exact class this unit exists to close.
Worse, B's pins are FALSELY GREEN: with no conf `banned` is empty, so P2 grades nothing and prints
`SUFFIX_OFFENDER_PIN="0"` over a fixture containing `class ThingManager`, which the scaffold
measures at 1. Green-by-absence, handed to an operator deciding whether to adopt.

A is the sole survivor and is not itself vetoed. It satisfies AC3 (the dispatcher prints usage and
exits 2 for both flags), AC6 as written, AC8 and AC9, and touches none of the frozen contract
functions.

The spec's own rationale for A is REFUTED and A survives on better ground. §8 argues "the measured
adopter population this build could read is zero"; `tools/govkit/fixtures/incms-2cff5855.receipt.json`
carries 52 rows over 11 kits, 11 of them `kit: "lexicon"` at prefix `scripts/lexicon/`, reconstructed
on a node "where both live adopter checkouts are in hand". What actually carries A is that the
capability is NOT LOST: `python tools/lexicon/scaffold_lexicon.py <path-outside-the-repo>` already
gives a pre-adoption reading that writes nothing into the target, because `scaffold_lexicon.py:39`
sets `KNOWN = lex.KNOWN_EXTS` — the same shipped defaults B reaches for — and `:106` derives `root`
from `git rev-parse --show-toplevel` independently of `dest`. Measured end to end in a conf-less
throwaway repo: 77 lines carrying LANGS, all three MEASURED pins, the VERBS proposal table and the
rename-debt worklist, with `git status` unchanged and no `.lexicon.conf` created. That is MORE of
`--probe`'s reading than B preserves, at zero lines. The README line is therefore a ROUTE, and that
is the binding condition on this pick.

Two corrections ride with it. §8's appeal to charter §7 does not reach — that rule quantifies over
GATE exemptions and a deleted CLI mode is not one. And the research record's sentence continues past
what §8 quotes: "Its useful half (the debt/unruled split) becomes the permanent shape of the
ordinary report", which units 7 and 10 implement, so only the pre-adoption ENTRY CONDITION was ever
at stake and the scaffold route already covers it.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against `d0a18683` with every figure re-measured on
  this worktree, including a correction to the research record's walk count.
- rev-2 · 2026-09-04 · F1 ratified as option A (delete `--probe`), with the README naming the
  surviving pre-adoption route — `scaffold_lexicon.py <path-outside-the-repo>`, which writes nothing
  into the target — rather than recording a bare loss. That route is now in §2 S9, §4 Alternatives
  and §5 user docs, not only in the §8 mark. §8's supporting claims corrected: the measured adopter
  population is at least one (11 lexicon rows in the incms receipt), `--scaffold` does NOT
  necessarily write into the repo, the probe self-test arms number 2 and not 4, and the charter's
  exemption rule quantifies over gate exemptions and does not reach a deleted CLI mode. AC6 rewritten
  to recompute its expected arm count from `grep -c "check(" tools/lexicon/selftest.py` at build
  time, since its old arithmetic inherited the off-by-2. Recorded in §4 Migration that deleting
  `run_probe` orphans `import canon` at `tools/lexicon/lexicon.py:84` until unit 11, with no python
  lint leg to catch it, and that the same deletion forecloses unit 10's cheapest route while unit
  10's fork is parked for an owner turn — so that owner turn is owed before this deletion lands. S7's
  cite corrected from `tools/codebase-map/selftest.py:1268-1276`, which is another arm's docstring,
  to `:1305-1313`. Header base re-pinned from `d0a18683` to `6c670b02`, the commit every figure in
  this rev was measured at.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "walk the tracked corpus once and yield each file's
extracted definitions"` ranked `extract` in `tools/lexicon/lexicon.py` first, at fan-in 7 and marked
SEAM, with `tracked_files` in the same file at fan-in 3 and also SEAM. The seam this unit extends is
that pair: `scan_corpus` is a generator wrapping `tracked_files` plus `extract` plus the declared-
extension filter that all five current walks re-derive, and it changes neither function. The probe
also surfaced `corpus_files` in `tools/memory-recall/extract.py` and `load_corpus` in
`tools/codebase-map/reuse_lookup.py`, and neither is reusable here: the lexicon kit ships
self-contained and may not import a neighbour kit, which is the constraint the sibling unit at this
build order preserves.

Recall terms used: `python tools/memory-recall/query.py "why do the lexicon measure and check modes
disagree and what did the armed-but-unreachable defects cost" --terms "lexicon measure check armed
unreachable hoist return problems exit code brief probe DEAD_TOKENS stopword parity corpus walk"`.
It returned 38 hits; the load-bearing one is the cumulative review that staged the break and recorded
both halves, `--check` exiting 1 naming the stale waiver while `--measure` printed three pins, no
note line, and exit 0.
