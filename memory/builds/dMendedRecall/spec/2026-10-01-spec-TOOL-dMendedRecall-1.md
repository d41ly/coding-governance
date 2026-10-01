# TOOL-dMendedRecall-1 — the recall selftest's memory-tree fixture carries the kit's python surface, and the spec-H1 arm reads only that

**Status:** CLOSED · rev-1 · 2026-10-01 · node d · Tier-2 · base 1f915870 · streams tooling · order 1 · closes TOOL-dAlignedCarrier-8 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-build-TOOL-dMendedRecall-1-1-acceptance-ledger.md](../build/2026-10-01-build-TOOL-dMendedRecall-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-01-prompt-TOOL-dMendedRecall-1-build-brief.md](../prompts/2026-10-01-prompt-TOOL-dMendedRecall-1-build-brief.md) | journal | TOOL-dMendedRecall-2 TOOL-dMendedRecall-3 |
| [2026-10-01-prompt-TOOL-dMendedRecall-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-dMendedRecall-1-spec-brief.md) | journal | TOOL-dMendedRecall-2 TOOL-dMendedRecall-3 |

<!-- /gen:spec-records -->

## 1. Goal

The `memory-recall kit selftest` leg is red on the default branch since the merge `78c4bf7d`. Its
fixture builder copies two named files of the memory-tree kit into every scratch repository, and
the index generator it imports gained a third sibling, `backlog.py`, on a branch that merged after
that list was written. This unit makes the fixture copy what the memory-tree kit actually installs,
so the leg goes green, and makes the one arm that imports the generator read that fixture alone, so
the next sibling the generator gains reds the plain run and not only the nested one.

## 2. Scope (IN)

- **S1** — `make_repo` in `tools/memory-recall/selftest.py` derives the file set it copies into the
  fixture's `memory-tree/` from the directory `E.resolve_kit_dir("memory-tree", "tree_lib.py", KIT)`
  answers: every top-level `*.py` module there, sorted, copied byte for byte. The set at
  `tools/memory-recall/selftest.py:209` becomes derived rather than spelled. The comment above it
  says why the set is derived and names the kit descriptor's `include = "**"` as what it mirrors.
  Observed by AC1, AC2.
- **S2** — The spec-H1 arm, `test_spec_h1_anchors_the_id_it_defines`, reads `spec_ids` through a
  child interpreter instead of an in-process `import gen_build_index`. The child is a module-level
  probe constant, `_SPEC_IDS_PROBE`, in the shape `_GRAMMAR_PROBE` already has
  (`tools/memory-recall/selftest.py:2595`). It runs as `sys.executable -I -c`, with `cwd` at the
  fixture root, `sys.dont_write_bytecode` set first, and the resolved memory-tree directory as the
  only path it inserts. It prints the sorted id set as JSON. The arm's assertions are unchanged.
  Observed by AC1, AC3.
- **S3** — No arm is added or taken away: `SELFTEST_ARMS` stays 75 and its provenance chain is
  untouched. Observed by AC2.
- **S4** — The whole leg reads green, which is the ask's own accept clause. Observed by AC4.

## 3. Non-goals (OUT)

- `tools/memory-tree/gen_build_index.py`'s import of `backlog`. Every real install ships that
  sibling beside the generator, so the generator is correct and stays as it is.
- Any other arm's fixture, and any other kit's selftest. Other fixtures that hand-list a sibling
  kit's files are a class this unit does not survey.
- Running the leg inside the pass. The gate-guard hook denies the whole-suite file before
  VERIFYING; the close's flagged bar reads it.
- The memory-recall kit version marker. The orchestrator moves it once, at VERIFYING.

### Edges

- **consumes-from** external — the close's flagged bar, which is the one reading of the whole leg
  this run may take; AC4 rests on it.

## 4. Design

### Evidence

Read at `1f915870` on 2026-10-01, PINNED to that date.

- The red, from the persisted leg log of the last flagged bar on node `d` (2026-09-30 23:52): the
  ADOPTER-layout arm fails, and inside it `a spec H1 anchors the id it defines` fails with
  `ModuleNotFoundError: No module named 'backlog'`. The SAME arm reads `ok` in the plain run of that
  very log. So the fixture is short of a file, and the plain run's in-process import found the file
  somewhere outside the fixture.
- The two halves met at the merge. `ca4bff24` (TOOL-aRepatriatedFork-40, 2026-09-28, on `main`)
  wrote the two-name copy list at `tools/memory-recall/selftest.py:208-210`. `3c338bac`
  (TOOL-dDerivedDocket-6, 2026-09-21, on its own branch) added `import backlog` at
  `tools/memory-tree/gen_build_index.py:290`. `78c4bf7d` merged the second into a tree holding the
  first. Neither branch alone was red.
- Probe, a scratch directory holding only `tree_lib.py` and `gen_build_index.py`, imported under
  `python -I`: `ModuleNotFoundError: No module named 'backlog'`. The same with `backlog.py` added:
  imports, and `spec_ids` is present.
- The generator cannot defer the import: `tools/memory-tree/gen_build_index.py:2331` reads
  `backlog.UNRESOLVED` at module scope, and `backlog.` appears on 170 of the module's lines.
- What an install delivers: `tools/memory-tree/kit.toml:21` ships the kit with `include = "**"`, so
  every adopter has every sibling module beside the generator.
- How the nested run finds its kit: `make_repo` copies from the kit its own `KIT` resolves, and in
  the nested run `KIT` is the outer fixture's `memory-recall/`, so the inner fixture inherits
  exactly the outer fixture's `memory-tree/` file set. Deriving the set in the outer run fixes both.
- Which in-process path handed the plain run its `backlog` is UNVERIFIED. The log proves that it
  happened; the arm runs at decoration time, after earlier arms have put directories on
  `sys.path`, and S2 makes the question moot instead of answering it.

### Data model

`_SPEC_IDS_PROBE` takes three argv words: the resolved memory-tree directory, the fixture root, and
the memory root. It runs `git -C <root> ls-files` itself, calls
`spec_ids(root, tracked, {"MEMORY_ROOT": <m>, "FAMILIES": "tooling:TOOL"})`, and prints
`json.dumps(sorted(ids))`. A non-zero exit is an assertion failure carrying the child's stderr, so a
missing sibling names itself in the arm's own row.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `_SPEC_IDS_PROBE` | module-level string constant | none; `.lexicon.conf` declares no `py.constant` cell, asked of `python tools/lexicon/lexicon.py --suggest _SPEC_IDS_PROBE --as py.constant` on 2026-10-01 |

No function is minted. `make_repo` and the arm keep their names.

### Rollout

Nothing renders from this file. The pass edits it, observes AC1 to AC3, and commits.

### Files touched (estimate)

`tools/memory-recall/selftest.py`

### Alternatives rejected

Each was tested before the pick, and the test that rejected it is named.

- **Add `backlog.py` to the literal list.** Rejected by the closure probe: an `ast` walk of the two
  files the arm reaches already yields three files at module scope and four counting deferred
  imports (`corpus_ids.py`). The set grew once by a merge nobody saw; a literal fixes this instance
  and leaves the class.
- **Copy the sibling-import closure computed by an `ast` walk.** Rejected on the kit's own house
  style: `gotchas.py`, `merge-rows.py` and `migrate_backlog.py` each load a sibling through
  `importlib.util.spec_from_file_location`, which an import-statement walk does not see. A closure
  that misses the kit's own dynamic loads is a narrower copy of the same hand-kept list.
- **Defer the generator's `import backlog`.** Rejected by `gen_build_index.py:2331`, which reads the
  module at import time, and by the descriptor: the generator is right for every real install.
- **Copy the whole kit directory.** It would mirror `include = "**"` most literally, and it would
  copy the kit's withheld `*.test.sh` suites into every scratch repository a run builds, which the
  2026-09-30 log's sweep row counts at 76. The python modules are what an import can reach.
- **Keep the arm's in-process import.** The 2026-09-30 log shows that import passing over a
  fixture the nested run proves incomplete. The plain run is the one an author runs first.

Cost does not discriminate among the copy sets. Measured 2026-10-01 on node `d`, PINNED: 104
fixture builds copy the two-file set in 0.11 s, the four-file closure in 0.19 s, and all ten
top-level modules in 0.42 s.

## 5. Production-readiness checklist

- security — N/A: a test fixture copies files the repository already tracks into a scratch
  directory it already creates; no new read or write surface.
- perf / scale — about 0.3 s more copying per full run, measured above; one extra interpreter start
  for the spec-H1 arm.
- error / empty / loading states — a resolver miss raises `LookupError` naming where it looked, as
  today; a child that cannot import prints its traceback into the arm's FAIL row.
- observability — the arm's FAIL row now names the missing module in both layouts, not only the
  nested one.
- risks — every arm's fixture gains eight more `*.py` files under `memory-tree/`. An arm that
  enumerates fixture files or counts `git ls-files` could move. The build pass greps the selftest
  for whole-tree enumerations and names in its ledger any it found. The corpus is read under the
  memory root, which these files are not under.
- testing — the scratch reproduction AC1 to AC3 describe; the leg itself at the close.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When a scratch reproduction under the run's scratchpad builds the adopter layout the
  nested run sees, a `memory-recall/` copy of the kit beside a `memory-tree/` directory, seeds one
  spec whose H1 is `# TOOL-aQuill-9 — x` under `builds/bQuill/spec/`, stages it, and runs
  `_SPEC_IDS_PROBE` read out of the edited file with `ast` and never imported, then with
  `memory-tree/` holding only `tree_lib.py` and `gen_build_index.py` the probe exits non-zero with
  `No module named 'backlog'` on stderr, and with `memory-tree/` holding the set S1 derives it exits
  0 and its JSON carries `TOOL-aQuill-9`.
  Red when: the two-file layout imports, which means the probe still reads something outside the
  fixture, or the derived layout fails.
  fixture: none in the tree. The pass builds it under the scratchpad. Importing the selftest file to
  reach the constant would run every arm at decoration time, which is why the constant is read with
  `ast`.
- **AC2** — When `grep -c -F 'for f in ("tree_lib.py", "gen_build_index.py")' tools/memory-recall/selftest.py`
  runs it prints 0, where BASE prints 1; `grep -c -F 'import gen_build_index as G' tools/memory-recall/selftest.py`
  prints 0, where BASE prints 1; `grep -c -F 'glob("*.py")' tools/memory-recall/selftest.py` prints
  at least 1; and `grep -c '^SELFTEST_ARMS = 75$' tools/memory-recall/selftest.py` prints 1.
  Red when: the literal list or the in-process import survives, or an arm was added or taken away.
- **AC3** — When the AC1 reproduction runs over the two-file layout with `PYTHONPATH` naming this
  repository's `tools/memory-tree`, the probe still exits non-zero with `No module named 'backlog'`.
  Red when: the child resolves a sibling from the host environment, which is the shape that let the
  plain run pass on 2026-09-30.
- **AC4** — When the close's flagged bar runs the `memory-recall kit selftest` leg, its persisted
  `memory-recall_kit_selftest.log` carries no `FAIL` row, its tally line reads every check passed,
  and its arm-count row reads `75 == SELFTEST_ARMS`. After landing, the same leg is green at the
  default branch's tip, which is the accept clause of TOOL-dAlignedCarrier-8.
  Red when: any row reads FAIL, the ADOPTER-layout arm and the spec-H1 arm above all.
  permission: the gate-guard hook denies the whole-suite file in any phase before VERIFYING, so no
  unit pass may run it; this criterion is observed at the close and not in the pass.
  cost: the leg's own wall clock, paid once inside the close's flagged bar.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `hook destinations self-test` · `install-prefix (shipped surface)`

No arm is added or moved, so this unit carries no `New arm:` line; S2 changes how one existing arm
reads its subject, and AC4 is where that arm runs.

## 8. Open questions

- **F1 — Where does the fix go?** (a) Add `backlog.py` to the fixture's literal list. (b) Derive the
  list from the resolved memory-tree directory: every top-level `*.py`. (c) Copy the sibling-import
  closure an `ast` walk computes. (d) Defer the generator's `import backlog` so two files suffice.
  (a) fixes the instance and leaves the class; (c) misses the kit's own three dynamic sibling loads;
  (d) is refuted by the module-scope read at `gen_build_index.py:2331` and would edit a shipped
  generator that is correct for every install. (b) satisfies the accept clause and closes the class
  for every future sibling, at 0.3 s a run. Recommendation (b). RESOLVED (agent, 2026-10-01,
  delegated): (b), the survivor satisfying the most stated criteria with the fewest follow-ups,
  M3's rule; the tests that rejected the others are §4's.
- **F2 — Does the spec-H1 arm keep its in-process import?** (a) Keep it: the nested run already
  catches a missing sibling. (b) Read `spec_ids` through an isolated child, so the plain run grades
  the fixture alone. (a) is what let the plain run read `ok` over an incomplete fixture on
  2026-09-30; (b) costs one interpreter start and follows `_GRAMMAR_PROBE`, a shape the file already
  uses. Recommendation (b). RESOLVED (agent, 2026-10-01, delegated): (b), the more feature-rich
  survivor under M3; no veto applies, as it adds no dependency, surface or carrier.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the ask's accept clause, the build's spec brief, the
  2026-09-30 leg log and the probes §4 names.

## 10. Reuse audit

The probe, run on 2026-10-01:

```
python tools/codebase-map/reuse_lookup.py "copy the sibling kit modules a fixture needs into a scratch adopter layout"
```

It ranked `kit_rel`, `adopt` and `kit_dir` as name-stem seams, listed `resolve_kit_dir` across
eight files, and reported `.sh` as an unscanned layer. None of them is a fixture copy rule. The
seams reused are both in the file being edited: `E.resolve_kit_dir`, which already answers where
the memory-tree kit sits and stays the one resolver, and the `_GRAMMAR_PROBE` / `read_grammar`
child-probe shape at `tools/memory-recall/selftest.py:2595`, which S2 copies for
`_SPEC_IDS_PROBE`. For the copy rule itself no existing seam fits: nothing in the tree derives a
fixture's sibling-kit file set, and the lookup returned nothing that does. The recall hit on
TOOL-aRepatriatedFork-40's spec confirms the declared direction, recall reaching into memory-tree
through `resolve_kit_dir`, and says nothing about the copy list.

Recall terms used: make_repo fixture memory-tree tree_lib gen_build_index backlog spec_ids adopter layout resolve_kit_dir selftest sibling import

The question passed with them: "why does the recall selftest copy only two memory-tree files into
its fixture, and what imports backlog".
