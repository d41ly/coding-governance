# TOOL-dGroundRules-34 — the round-1 audit of units 26 to 32, its minors: thirty-seven findings closed in the code those units leave, one scope item each

**Status:** DEFERRED · rev-5 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 12 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-34-deviation-22.md](../build/2026-10-23-build-TOOL-dGroundRules-34-deviation-22.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-34-deviation-63.md](../build/2026-10-23-build-TOOL-dGroundRules-34-deviation-63.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-21-trim-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-21-trim-task.md) | research | TOOL-dGroundRules-21 TOOL-dGroundRules-25 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-34-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-34-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-34-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-34-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-34-fold-trim-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-34-fold-trim-brief.md) | research | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-33 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 26 to 32
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md`)
exited CONVERGED with 38 confirmed findings. Its one HIGH, id 26, is promoted alone as
`TOOL-dGroundRules-33`; BUILD-METHOD M4 batches the other thirty-seven, twenty-three MEDIUM and
fourteen LOW, into this unit. They land on units 26 to 32, and M6's clauses yield no two disjoint
write sets (§4 "Alternatives rejected"). It builds at order 12, above every unit of this build,
`TOOL-dGroundRules-33` at order 11 included.

Ids sharing a review item each take their own scope item, a distinct facet of its defect. Ids 2 and
1 are taken at MEDIUM and ids 11 and 36 at LOW, the grades the review's skeptic re-graded them to.

| Finding id | Severity | Review item | Unit it lands on | Scope item | Criterion |
|---|---|---|---|---|---|
| 2 | MEDIUM | M1 | 26 | S1 | AC1 |
| 10 | MEDIUM | M1 | 26 | S2 | AC2 |
| 22 | MEDIUM | M1 | 26 | S3 | AC3 |
| 31 | MEDIUM | M1 | 26 | S4 | AC4 |
| 1 | MEDIUM | M2 | 30, 25 | S5 | AC5 |
| 25 | MEDIUM | M2 | 30, 25 | S6 | AC6 |
| 3 | MEDIUM | M3 | 27, 23 | S7 | AC7 |
| 23 | MEDIUM | M3 | 27, 24 | S8 | AC8 |
| 4 | MEDIUM | M4 | 27 | S9 | AC9 |
| 34 | MEDIUM | M4 | 27 | S10 | AC10 |
| 5 | MEDIUM | M5 | 29 | S11 | AC11 |
| 14 | MEDIUM | M5 | 29 | S12 | AC12 |
| 28 | MEDIUM | M5 | 29 | S13 | AC13 |
| 37 | MEDIUM | M5 | 29, 32 | S14 | AC14 |
| 6 | MEDIUM | M6 | 32 | S15 | AC15 |
| 15 | MEDIUM | M6 | 32 | S16 | AC16 |
| 29 | MEDIUM | M6 | 32 | S17 | AC17 |
| 24 | MEDIUM | M7 | 29, 9 | S18 | AC18 |
| 33 | MEDIUM | M7 | 29 | S19 | AC19 |
| 32 | MEDIUM | M8 | 31 | S20 | AC20 |
| 35 | MEDIUM | M9 | 32 | S21 | AC21 |
| 18 | MEDIUM | M10 | 32 | S22 | AC22 |
| 19 | MEDIUM | M11 | 32 | S23 | AC23 |
| 7 | LOW | L1 | 26 | S24 | AC24 |
| 8 | LOW | L2 | 30 | S25 | AC25 |
| 9 | LOW | L3 | 32 | S26 | AC26 |
| 11 | LOW | L4 | 26 | S27 | AC27 |
| 12 | LOW | L5 | 26 | S28 | AC28 |
| 13 | LOW | L6 | 26 | S29 | AC29 |
| 17 | LOW | L7 | 30 | S30 | AC30 |
| 38 | LOW | L7 | 30 | S31 | AC31 |
| 16 | LOW | L8 | 32 | S32 | AC32 |
| 20 | LOW | L9 | 27 | S33 | AC33 |
| 21 | LOW | L10 | 28 | S34 | AC34 |
| 27 | LOW | L11 | 32 | S35 | AC35 |
| 30 | LOW | L12 | 31 | S36 | AC36 |
| 36 | LOW | L13 | 32 | S37 | AC37 |

Each item's fix is the one the review's skeptic judged sound; for ids 24, 30 and 35 it is the
skeptic's corrected fix. Where the review offered options, §8 records the pick.

## 2. Scope (IN)

- **S1** — Finding 2. Before its `git add -A`, `build_source_snapshot` (`TOOL-dGroundRules-26` S1)
  copies the source's exclude file,
  `git -C <source> rev-parse --path-format=absolute --git-path info/exclude`, to
  `<s>/.git/info/exclude` when that file exists. The `add` then reads the source's `.gitignore`
  files through `GIT_WORK_TREE`, its exclude file through the copy and `core.excludesFile` through
  the user's own configuration, which are the rules `git status` in the source reads.
  Observed by AC1.
- **S2** — Finding 10. `TOOL-dGroundRules-26` S1's sentence "the source's ignore rules decide what
  counts" holds as written: the snapshot's file set is exactly the set the source reports as tracked
  or untracked and not ignored. Observed by AC2.
- **S3** — Finding 22. `--git-path info/exclude` resolves, from a linked worktree, to the common
  directory's file, which the main checkout and every linked worktree share. A snapshot taken from
  the main checkout therefore carries no path under `.claude/worktrees/` and none of the local state
  files that file ignores. Observed by AC3.
- **S4** — Finding 31. After `write-tree`, a gitlink (mode `160000`) in the snapshot tree that the
  source's own index does not carry fails the case naming its path and the source's exclude file. A
  nested repository no ignore rule covers is a named `WRONG`, never a silent gitlink and never an
  unexplained `add` failure. Observed by AC4.
- **S5** — Finding 1. The arm `TOOL-dGroundRules-25` §7 declares in
  `tools/workflows/check-protocol-parity.test.sh` for its AC18, which stages the hook's
  `KIT_AGENT_CAP_VERSION` below the writer marker's version and expects the fallback render, is
  removed. `TOOL-dGroundRules-30` AC1 and AC2 observe AC18's outcome in its place, through the
  predicate that unit's render has.
  **Readers:** by name: READER NOT IN TREE — the arm belongs to unit 25 and is not built at this
  spec's base. by value: NO VALUE READERS — the arm declares floor none, so no floor row counts it.
  Observed by AC5.
- **S6** — Finding 25. This spec's §7 carries the arm line for
  `tools/workflows/check-protocol-parity.test.sh` that names `TOOL-dGroundRules-30`'s writer-marker
  arm as the arm observing `TOOL-dGroundRules-25` AC18's outcome, so the close's RED-first
  observation for AC18 is made through an arm the built tree holds. Observed by AC6.
- **S7** — Finding 3. `resolve_govkit(root)` in `tools/policy/check_policy.py` returns
  `<root>/<tool root>/govkit/govkit.py`, the tool root derived as `TOOL-dGroundRules-24` S4 derives
  it. `run_govkit` (`TOOL-dGroundRules-27` S1) and `budgets-ships-join`'s in-process `importlib`
  load (`TOOL-dGroundRules-23` S1, through `TOOL-dGroundRules-32` S8's `read_shipped_descriptors`)
  each take the path from it. The in-process load reads the source's working tree by design and is
  the one sanctioned read of the deployer outside a snapshot. `TOOL-dGroundRules-27` S4's rule
  reads: no line of `check_policy.py` outside `resolve_govkit` spells the deployer's file name.
  Observed by AC7.
- **S8** — Finding 23. `TOOL-dGroundRules-24` S4's refusal for a source tree with no deployer,
  naming where it looked, is raised by `resolve_govkit`, so the in-process join and every deployer
  run fail with one named `WRONG` when the deployer is missing. Observed by AC8.
- **S9** — Finding 4. `build_source_snapshot` adds each root it returns, resolved, to the
  module-level set `SNAPSHOT_ROOTS`. `run_govkit` refuses, as the case's `WRONG`, any `snapshot_root`
  whose resolved path is not in that set, naming it and `build_source_snapshot`, and runs no
  deployer. `TOOL-dGroundRules-27` S1's equality refusal is one case of this rule. Observed by AC9.
- **S10** — Finding 34. The class `TOOL-dGroundRules-27` §1 claims is closed holds for the other
  roots no snapshot made: a clone of the source made by any other route, and the two arguments
  swapped. Observed by AC10.
- **S11** — Finding 5. `TOOL-dGroundRules-29` AC4's planted tree, spelled whole: a receipt-less
  `git init` target holding `tools/govkit/registry.toml` and `vendor/gov/govkit/registry.toml`.
  `arm_cap_census` prints one finding naming both paths. Observed by AC11.
- **S12** — Finding 14. `TOOL-dGroundRules-29` S1's depth window, observed at its edge: a candidate
  whose `<d>` sits at depth 3 is not counted, and a `registry.toml` at the top level is not a
  candidate. Observed by AC12.
- **S13** — Finding 28. The standing case `census-ambiguous-registry` in `CASES` of
  `tools/policy/check_policy.py` plants S11's two candidates in its temporary repository; the plant
  reads red as the one finding naming both, and the unplanted copy reads `unadopted` and green.
  Observed by AC13.
- **S14** — Finding 37. Its corrupted criteria, `TOOL-dGroundRules-29` AC4 and
  `TOOL-dGroundRules-32` AC9, are re-spelled here as literal inputs, each checked
  inside the rule it probes: S11's two candidates put `<d>` at depths 1 and 2, inside
  `TOOL-dGroundRules-29` S1's window of 0 to 2, and AC15's two pairs are the directory-over-file and
  string-prefix pairs `overlaps` decides (`tools/unattended/lib-unattended.sh:745-750`).
  Observed by AC14, AC15.
- **S15** — Finding 6. `TOOL-dGroundRules-32` AC9's probe, spelled whole:
  `check_writes_intersect(["tools/policy/"], ["tools/policy/x.py"])` answers `True` and
  `check_writes_intersect(["tools/policy/a.py"], ["tools/policy/ab.py"])` answers `False`.
  Observed by AC15.
- **S16** — Finding 15. The parity half of `TOOL-dGroundRules-32` S9: `overlaps` gives the same two
  answers for the same two pairs. Observed by AC16.
- **S17** — Finding 29. The arm `TOOL-dGroundRules-32` S9 adds to `tools/check-spec-tokens.test.sh`
  runs exactly S15's two pairs, its disjoint pair being the string-prefix pair, so it tells a raw
  prefix compare from the containment rule. Observed by AC17.
- **S18** — Finding 24. Under `unadopted`, `arm_cap_census` withholds
  only the per-row grading of enforcer presence. It keeps both directions of
  `TOOL-dGroundRules-9` S7's census-to-tree join: a requested cap with no row and a row with no case
  are findings in any tree. Observed by AC18.
- **S19** — Finding 33. The census cases and the tree answer each repository reads after this unit,
  the list `TOOL-dGroundRules-29` §4's copy rule never applied: `budgets-census-join`
  (`TOOL-dGroundRules-9` S7) reads `unadopted` and is held by S18; `census-receiptless-target`
  (`TOOL-dGroundRules-29` S4) reads `unadopted`, then `source` after its registry copy;
  `census-adopter-receipt` (`TOOL-dGroundRules-22` S4) and `census-default-adopter`
  (`TOOL-dGroundRules-25` S12) read `adopter`; and `census-ambiguous-registry` (S13) reads the
  ambiguity finding. Observed by AC19.
- **S20** — Finding 32. Before `adopt-policy.sh --scaffold` takes `TOOL-dGroundRules-31` S1's
  deferral, it runs the installed `check_policy.py --repo <t>` and reads its `arm_schema` line. A
  finding count above zero makes `--scaffold` exit 2 printing the arm's finding lines and no
  deferral line. `TOOL-dGroundRules-31` AC4 is observed through this real control flow, not through
  a staged `policy.py`. Observed by AC20.
- **S21** — Finding 35. `TOOL-dGroundRules-32` S11's prefix rule is
  stated inline in `check_policy.py`: each `\` in a receipt's `prefix` becomes `/`, and a value that
  is then absolute, matches `^[A-Za-z]:`, or holds a `..` segment after `posixpath.normpath` answers
  `invalid` naming `prefix`. Nothing is imported from the deployer, which adopters never install.
  Observed by AC21.
- **S22** — Finding 18. `build_fresh_target` (`TOOL-dGroundRules-32` S16) runs
  `run_govkit(snapshot_root, source_root, "intake", "--target", t, "--kits", <ids>, "--answer", "<key>=<value>", ...)`
  over the `git init` target before its one commit, one `--answer` per key of S23's answers. `intake`
  writes `.governance/deploy.toml`, its `gov_source`, the answers the closure needs and the
  `[gate_runner]` seed, and its refusal is the case's `WRONG`. The builder writes no descriptor of
  its own and derives no answer list of its own. Observed by AC22.
- **S23** — Finding 19. `read_deploy_answers(source_root)` in `check_policy.py` reads `DEPLOY_FULL`'s
  `[answers]` from `<source tool root>/govkit/selftest.py` with `ast`, never by import: the module's
  `DEPLOY_FULL` assignment, its constant string parts joined and parsed with `tomllib`. A missing
  assignment or an unparsable table is the case's `WRONG` naming the file. `build_fresh_target`
  takes its `--answer` values from it. Observed by AC23.
- **S24** — Finding 7. `TOOL-dGroundRules-26` AC4 is a guard, not acceptance. The acceptance of the
  snapshot's isolation is that the snapshot commit `TOOL-dGroundRules-26` S3 prints is absent from
  the source's object store after the case, and that a snapshot staged to write into the source's
  store makes it present. Observed by AC24.
- **S25** — Finding 8. `TOOL-dGroundRules-30` AC3's observation is made by behaviour: a hook whose
  `KIT_AGENT_CAP_VERSION` reads `0.0` and whose writer marker is intact still receives the writer
  render. Observed by AC25.
- **S26** — Finding 9. `TOOL-dGroundRules-32` AC6 is observed by count: the rows `ORDER_ROWS`
  prints equal the distinct `order` values this build's specs declare. Observed by AC26.
- **S27** — Finding 11. `TOOL-dGroundRules-26` S3's snapshot line gains ` · <n> files · <t>s`, `n`
  being the entries of `git -C <s> ls-tree -r HEAD` and `t` the wall seconds the snapshot took, so
  the cost `TOOL-dGroundRules-26` §5 states is measured on every run. Its pinned 5873 is superseded:
  the tree held 5888 tracked files at `f4d31452a` (`git ls-files | wc -l`, PINNED 2026-10-23).
  Observed by AC27.
- **S28** — Finding 12. Every `--git-path` call `build_source_snapshot` makes carries
  `--path-format=absolute`, the index call `TOOL-dGroundRules-26` S1 names included, so a primary
  checkout's `.git/index` never resolves against the caller's working directory. Observed by AC28.
- **S29** — Finding 13. The snapshot is selected by `run_govkit` running
  `<s>/<tool root>/govkit/govkit.py`, whose `repo_root` resolves `<s>`; `apply` writes the receipt's
  `gov_source` and `gov_commit` from that root (`tools/govkit/govkit.py:7981`, `:13030`). The
  descriptor's `gov_source` is written by `intake` (S22) and selects nothing. `adopter-fresh-target`
  asserts that the receipt's `gov_source` is the snapshot root. Observed by AC29.
- **S30** — Finding 17. `TOOL-dGroundRules-30` S1's fallback notice quotes the hook's reason: the
  first line of the probe's output that opens with four spaces, the indent stripped, because
  `tools/workflows/check-verifier-fanout.sh:213-214` prints `verifier-fanout: FAILED — <file>` first
  and the hook's output after it, indented. Observed by AC30.
- **S31** — Finding 38. When the probe's output holds no indented line, the notice reads
  `the agent-cap hook exited <rc> with no reason`, never the gate's header or the render's temporary
  path. Observed by AC31.
- **S32** — Finding 16. `TOOL-dGroundRules-32` §4's first Evidence bullet is re-cited by marker: the
  build-order region is the lines between `<!-- gen:build-order -->` and its closing marker, at lines
  165 to 179 of `memory/builds/dGroundRules/README.md` at `f4d31452a`. `ORDER_ROWS` selects it by
  those markers. Observed by AC32.
- **S33** — Finding 20. The docstring of `run_govkit` names `run_in_gov`
  (`tools/govkit/matrix.py:409`) and the `clone -q --local` checkout it runs from (`:929`), and says
  why neither is reused: the policy kit cannot import the govkit kit's test harness, `run_in_gov`
  has no source-root refusal, and its clone grades HEAD, the exposure units 26 and 27 close for the
  policy cases. The docstring names the deployer in words, so S7's rule holds. Observed by AC33.
- **S34** — Finding 21. `memory/gotchas/suite-invalidated-by-a-commit-under-it.md` gains, under its
  fix, a paragraph saying a frozen `--local` clone grades HEAD, so a suite whose verdict is recorded
  against the working tree commits that tree in a scratch clone (`build_source_snapshot`) instead;
  the paragraph backticks `tools/govkit/govkit.py`, `tools/govkit/matrix.py` and
  `tools/policy/check_policy.py`, which anchors H1 there. The HEAD paragraph
  `TOOL-dGroundRules-28` S2 wrote in `memory/gotchas/test-oracle-read-from-a-historical-sha.md`
  keeps its anchors and points to that record for the false-green shape, so its own symptom stays the
  false red. `memory/gotchas/INDEX.md` is regenerated with `gotchas.py --write`. Observed by AC34.
- **S35** — Finding 27. The build READMEs `TOOL-dGroundRules-32` S13's `unknown` re-renders are named
  in §4 "Writes `TOOL-dGroundRules-32` declares", the seven the review's probe printed and this
  build's own, and the hands-off edge in `TOOL-dGroundRules-32` §3 hands them to that unit's
  `--dispatch` write set. Observed by AC35.
- **S36** — Finding 30. `help/policy.md` carries a `## Install` section
  holding `TOOL-dGroundRules-31` S6's deferral line and its order: commit the install and the policy
  file, then re-run `--scaffold`. Observed by AC36.
- **S37** — Finding 36. The `arm_cap_census` and `legacy-homes` rows of `tools/policy/README.md`
  state the `invalid` answer `TOOL-dGroundRules-32` S11 adds and the finding each prints under it.
  Observed by AC37.

## 3. Non-goals (OUT)

- The HIGH: `TOOL-dGroundRules-33`.
- Rewriting any reviewed spec's text: each defect is closed here in code and in the observation it
  governs, and each repaired unit's §3 names this unit; nothing is folded (BUILD-METHOD M4).
- Renumbering any unit's `order`.
- The review's left-shift gates beyond what an item here builds: the spec-lint for a criterion that
  repeats a path or opens a list without `[`, the pre-unit-observation rule, and the checklist
  entries. Each is a bug-class follow-up for the closing review's left-shift (BUILD-METHOD M8).
- `tools/govkit/matrix.py`'s own HEAD exposure through `run_in_gov`. S33 records it; the policy
  cases are this build's.
- A new `policy.py` or `govkit.py` flag (§8 F1).

### Edges

- **consumes-from** `TOOL-dGroundRules-9` — `budgets-census-join` and the census-to-tree join of S7, which S18 keeps live under `unadopted` and AC18 observes
- **consumes-from** `TOOL-dGroundRules-23` — `budgets-ships-join`'s in-process `importlib` load of the deployer, which S7 routes through `resolve_govkit`
- **consumes-from** `TOOL-dGroundRules-24` — S4's tool-root derivation and its locate refusal, which S7 and S8 move into `resolve_govkit`
- **consumes-from** `TOOL-dGroundRules-25` — AC18's version-staging arm, which S5 removes, and `census-default-adopter`, which S19 lists
- **consumes-from** `TOOL-dGroundRules-26` — `build_source_snapshot` and the snapshot line, which S1 to S4, S9, S24 and S27 to S29 amend
- **consumes-from** `TOOL-dGroundRules-27` — `run_govkit` and its refusal, which S7 to S10 and S33 amend
- **consumes-from** `TOOL-dGroundRules-28` — the HEAD paragraph of the historical-sha record, which S34 points at the record that owns the false green
- **consumes-from** `TOOL-dGroundRules-29` — `derive_census_tree`'s three answers, the census arm under `unadopted` and `census-receiptless-target`, which S11 to S14, S18 and S19 amend
- **consumes-from** `TOOL-dGroundRules-30` — the render's writer-marker probe and its fallback notice, which S5, S6, S25, S30 and S31 amend
- **consumes-from** `TOOL-dGroundRules-31` — `--scaffold`'s deferral and the help page's install text, which S20 and S36 amend
- **consumes-from** `TOOL-dGroundRules-32` — `build_fresh_target`, the receipt shape rule, the overlap rule and its arm, the build-order criterion and the kit README's census rows, which S15 to S17, S21 to S23, S26, S32, S35 and S37 amend
- **consumes-from** `TOOL-dGroundRules-33` — the `{prefix}/govkit/selftest.py` guard line and the guard trace, which hold S23's `ast` read inside the leg that runs it
- **hands-off** `TOOL-dGroundRules-38` — S1's exclude-file read, kept out of the trace (id 18)
- **hands-off** `TOOL-dGroundRules-39` — `census-ambiguous-registry` and S11-S12's window (id 2)
- **hands-off** `TOOL-dGroundRules-40` — S16's parity and S17's arm, held in one table (id 17)
- **hands-off** `TOOL-dGroundRules-41` — S36's `## Install` section, held to the deferral line (id 21)
- **hands-off** `TOOL-dGroundRules-43` — the snapshot, govkit, receipt and `gov_source` amendments to this unit (ids 3-16, 26)

## 4. Design

### Evidence

Every line below was read on 2026-10-23 at `f4d31452a`, the commit this spec stands on, unless it
names another revision.

- `git -C C:/projects/coding-governance rev-parse --git-path index` printed `.git/index`, and
  `--path-format=absolute --git-path info/exclude` printed `C:/projects/coding-governance/.git/info/exclude`,
  on git 2.54.0.
- `git ls-files | wc -l` printed 5888; `git ls-files -s | grep -c "^160000"` printed 0, so gov's index
  carries no gitlink and S4 refuses none of gov's own entries. `git ls-files .claude` prints only
  `.claude/agents/` files, so AC3's pattern names untracked state only.
- `tools/govkit/govkit.py:13089` `needed_answers` scans destinations, hole discharges, gate-leg argv
  and guards, adopt and check argv and `config.seeded_from`; `cmd_intake` (`:13122`) refuses an
  existing descriptor and a missing answer with `Refusing to invent one`, and writes
  `gov_source = root` (`:13125-13160`).
- `tools/govkit/govkit.py:7981` and `:13030` write the receipt's `gov_source` as `str(root)`.
- `tools/govkit/govkit.py:1301` declares `DRIVE_PREFIX_RE = ^[A-Za-z]:/` beside
  `demand_contained_dest` (`:1304`); `tools/govkit/registry.toml` exempts `{prefix}/govkit` from
  adopter installs, so `check_policy.py` in an adopter cannot import it.
- `tools/govkit/selftest.py:195` runs `resolve_gov_pin` at import and `:197` prints; an `ast` read of
  `DEPLOY_FULL` (`:703`), its constant parts joined and parsed by `tomllib`, printed the five
  answers `memory_root`, `playbook_path`, `playbook_dir`, `manifest_path` and `user_skills`, with
  no import (run 2026-10-23).
- `overlaps tools/policy/ tools/policy/x.py` returned 0 and `overlaps tools/policy/a.py tools/policy/ab.py`
  returned 1 after sourcing `tools/unattended/lib-unattended.sh` (run 2026-10-23).
- `render_order` (`tools/memory-tree/gen_build_index.py:1716`) prints one row per distinct `order`
  value across the build's units.
- `memory/gotchas/suite-invalidated-by-a-commit-under-it.md:28` names `_cmd_apply` stamping from live
  HEAD, and `:53` prescribes `git clone -q --local --no-hardlinks`.
- `memory/map/generated/symbols.json` carries eight symbols of
  `tools/workflows/check-protocol-parity.test.sh`.
- A kit may not read a sibling kit (`tools/codebase-map/map_lib.py:1505`), and
  `TOOL-dGroundRules-2` S2 states that nothing in `policy.py` opens the working-tree policy file.

### The snapshot after S1 to S4, S9 and S27 to S28

```text
build_source_snapshot(source):
    t0 = now
    s = git clone --quiet --shared --no-checkout source <case tmp>/<s>
    copy (git -C source rev-parse --path-format=absolute --git-path index) to the temporary index
    ex = git -C source rev-parse --path-format=absolute --git-path info/exclude
    if ex exists: copy ex to <s>/.git/info/exclude
    GIT_DIR=<s>/.git GIT_WORK_TREE=source git add -A; write-tree; commit-tree -p HEAD; checkout --detach
    for each 160000 entry of ls-tree -r HEAD not among source's index gitlinks: WRONG naming it and ex
    SNAPSHOT_ROOTS.add(resolve(s))
    print snapshot line + " · <n> files · <t>s"
    return s
```

### The fresh-target builder after S22 and S23

```text
build_fresh_target(snapshot_root, source_root, kits):
    answers = read_deploy_answers(source_root)          # ast, never import
    t = git init; core.autocrlf=false; local user.email, user.name; README.md
    rc, out = run_govkit(snapshot_root, source_root, "intake", "--target", t, "--kits", kits,
                         *("--answer", f"{k}={v}") for k, v in answers)
    WRONG unless rc == 0                                # intake's own refusal names the answer
    commit once
    apply and check through run_govkit, as TOOL-dGroundRules-32 S16 and S18 state
    WRONG unless receipt gov_source == snapshot_root     # S29
```

### Per-item changes, by file

| File | Items |
|---|---|
| `tools/policy/check_policy.py` | S1 to S4, S7 to S13, S18, S19, S21 to S24, S27 to S29, S33 |
| `tools/policy/adopt-policy.sh` | S20 |
| `tools/policy/adopt-policy.test.sh`, `.memory-tree.conf` | S20 |
| `tools/workflows/check-protocol-parity.test.sh` | S5, S30, S31 |
| `tools/check-spec-tokens.test.sh` | S17 |
| `memory/gotchas/suite-invalidated-by-a-commit-under-it.md`, `memory/gotchas/test-oracle-read-from-a-historical-sha.md`, `memory/gotchas/INDEX.md` | S34 |
| `help/policy.md` | S36 |
| `tools/policy/README.md` | S37 |
| the codebase map | S7, S23, by regeneration |

S6, S14 to S16, S25, S26, S32 and S35 change no code; each is an observation owed for a defective
criterion or stated outcome, made against the code units 26 to 33 build.

### Writes `TOOL-dGroundRules-32` declares

S13 of that unit re-renders the build-order region of each build README holding a step of two or
more units with a spec that has no `### Files touched` sub-head. The review's probe printed seven
(re-read 2026-10-23 at `f4d31452a`, PINNED): `memory/builds/aBlindedTrial/README.md`,
`memory/builds/aBoundedCeiling/README.md`, `memory/builds/aBriskPreflight/README.md`,
`memory/builds/aTunedCompass/README.md`, `memory/builds/dDerivedDocket/README.md`,
`memory/builds/dGaugedVintage/README.md` and `memory/builds/dRetiredFork/README.md`, each of which
holds a build-order region with a Parallel column. With `memory/builds/dGroundRules/README.md` they
are the eight READMEs that unit's commit may write.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `resolve_govkit` | py.function | `tools/policy/check_policy.py` |
| `read_deploy_answers` | py.function | `tools/policy/check_policy.py` |
| `SNAPSHOT_ROOTS` | module-level set | `tools/policy/check_policy.py` |
| `census-ambiguous-registry` | `CASES` entry | `tools/policy/check_policy.py` |

`lexicon.py --suggest` answered OK for `resolve_govkit` and `read_deploy_answers` under
`py.function` on 2026-10-23; it proposed `resolve_govkit` in place of `locate_govkit`. The lexicon
declares no cell for a Python constant, so `SNAPSHOT_ROOTS` is graded by none.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `tools/policy/adopt-policy.sh`
- `tools/policy/adopt-policy.test.sh`
- `tools/policy/README.md`
- `help/policy.md`
- `.memory-tree.conf`
- `tools/workflows/check-protocol-parity.test.sh`
- `tools/check-spec-tokens.test.sh`
- `memory/gotchas/suite-invalidated-by-a-commit-under-it.md`
- `memory/gotchas/test-oracle-read-from-a-historical-sha.md`
- `memory/gotchas/INDEX.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Two batch units, the policy half and the render half.** Both regenerate
  `memory/map/generated/symbols.json`, which carries `check-protocol-parity.test.sh`'s functions,
  and the fresh-target case the policy items change runs the `adopt-policy.sh` the scaffold item
  changes, so one reads the other's write as an acceptance input: M6's first and second clauses fail.
- **`-c core.excludesFile=<source exclude>` for S1**, and **a registry and every census enforcer
  copied into unit 1's base fixture repository (S18)**: §8 F6 and F4.

## 5. Production-readiness checklist

- security — S21 refuses a receipt `prefix` that leaves the target by a drive letter or a backslash;
  S9 and S10 keep the deployer off every root no snapshot made; no item widens a write surface.
- perf / scale — S1 copies one file per snapshot; S4 lists the snapshot tree once; S22 adds one
  `intake` run per installing case; S27 measures, never adds, the snapshot's cost.
- error / empty / loading states — S4, S8, S20 and S23 each turn a silent or misattributed failure
  into a named `WRONG` or refusal; S31 names an empty hook answer.
- observability — the snapshot line carries its file count and seconds; every new `WRONG` names its
  path, root, key or file.
- risks — S5 removes another unit's arm by this unit's mandate; §7's arm line names its replacement.
- testing — the cases under `--fixture`, the suites on §7's arm lines, and AC1 to AC37.
- migration — the codebase map and `memory/gotchas/INDEX.md` regenerated in this unit's commit.
- user docs — `help/policy.md` (S36) and the kit README (S37).

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the policy kit's files by bare name,
`check_policy.py`, `adopt-policy.sh`, `policy.py` and `README.md` under the kit, as
`TOOL-dGroundRules-5` §6 does. Each `--fixture <case>` runs `python check_policy.py --fixture <case>`
and passes when it prints no `WRONG`. A fixture repository is a `git init` repository under
`%TEMP%/<short name>`, because a long path fails a clone on this node. A probe of a function runs it
from `python -c` with the kit directory on `sys.path`, and its `WRONG` is the line the function
prints. Let `ORDER_ROWS` stand for
`awk '/<!-- gen:build-order -->/,/<!-- \/gen:build-order -->/' memory/builds/dGroundRules/README.md | grep -E '^\| [0-9]+ \|'`,
and `GOVKIT_LINES` for a `python -c` probe that parses `check_policy.py` with `ast`, maps each line
holding `govkit.py` to its innermost enclosing function, and prints each line whose function is not
`resolve_govkit`.

- **AC1** — When `build_source_snapshot` runs over a fixture repository holding a committed file, an
  untracked `kept.txt` and an untracked `local.lock` matched only by its `.git/info/exclude`,
  `git -C <s> ls-tree -r --name-only HEAD` lists `kept.txt` and not `local.lock`.
  Red when: the snapshot commits a file the source's `git status` hides.
- **AC2** — When the same fixture repository is snapshotted, the sorted output of
  `git -C <s> ls-tree -r --name-only HEAD` equals the sorted output of
  `git -C <r> ls-files -co --exclude-standard`.
  Red when: the snapshot's file set and the source's differ by any path.
- **AC3** — When `build_source_snapshot` runs over the main checkout, the parent of
  `git rev-parse --path-format=absolute --git-common-dir`,
  `git -C <s> ls-tree -r --name-only HEAD | grep -cE '^\.claude/(worktrees/|scheduled_tasks\.lock|mailbox/)'`
  prints `0`.
  Red when: a snapshot of the main checkout sweeps in its linked worktrees or local state.
  cost: one snapshot of the main checkout, tens of seconds.
- **AC4** — When a fixture repository holds an untracked nested repository `inner/`, its own
  `git init` with one commit, that no ignore rule covers, `build_source_snapshot` over it prints
  `WRONG` naming `inner` and `info/exclude`.
  Red when: a nested repository becomes a silent gitlink in the graded tree.
- **AC5** — When `grep -c "KIT_AGENT_CAP_VERSION" tools/workflows/check-protocol-parity.test.sh`
  runs on the built tree, it prints `0`.
  Red when: `TOOL-dGroundRules-25`'s arm still stages the version and expects a fallback the render
  no longer gives.
  figure: before this unit the count is at least 1, the arm spelling the constant it stages.
- **AC6** — When a scratch clone of the built tree has the marker its hook's `WRITER_MARK` names
  staged to another string and the workflows render runs there, the rendered `unattended-build.js`
  carries `gov:fixed-verifiers` and `Math.min(` on the spec-writer split, and stderr names
  `govkit update --kits agent-cap`.
  Red when: `TOOL-dGroundRules-25` AC18's outcome has no arm once its own arm is gone.
- **AC7** — When `GOVKIT_LINES` runs on the built tree, it prints nothing.
  Red when: a line outside `resolve_govkit` spells the deployer's path.
- **AC8** — When a scratch copy has its `govkit.py` renamed to another name,
  `--fixture budgets-ships-join` and `--fixture adopter-fresh-target` each print `WRONG` naming the same
  looked-in path.
  Red when: the in-process join and the deployer run locate the deployer two ways.
- **AC9** — When `run_govkit("<repo>/tools", "<repo>", "plan")` is probed, it prints `WRONG` naming
  `<repo>/tools` and `build_source_snapshot`, and no deployer process starts.
  Red when: a subdirectory of the tree under test passes as a snapshot.
- **AC10** — When `run_govkit` is probed with a `git clone --local` of the repository made outside
  `build_source_snapshot`, and again with a real snapshot `s` as `run_govkit("<repo>", s, "plan")`,
  each prints `WRONG` naming `build_source_snapshot`.
  Red when: a stale clone or swapped arguments install some HEAD.
- **AC11** — When a receipt-less fixture repository holds `tools/govkit/registry.toml` and
  `registry.toml` and `python check_policy.py --repo <t>` runs, `arm_cap_census`
  prints exactly one finding, and it names both paths.
  Red when: an ambiguous tree is guessed to be gov's at one of its candidates.
- **AC12** — When a receipt-less fixture repository holds `tools/govkit/registry.toml`,
  `registry.toml` and a top-level `registry.toml`, and `python check_policy.py --repo <t>`
  runs, `arm_cap_census` prints no ambiguity finding and a finding for each census enforcer missing
  under `tools/`.
  Red when: a candidate outside the window of depths 0 to 2 decides the answer.
- **AC13** — When `--fixture census-ambiguous-registry` runs, it prints `RED as planted` and no
  `WRONG`; with `derive_census_tree` staged in a scratch copy to answer `source` at the first
  candidate, it prints `WRONG`.
  Red when: the ambiguity branch can regress with the leg green.
- **AC14** — When AC11's fixture repository is built from the two paths S11 names,
  `git -C <t> ls-files --others "*registry.toml"` lists two distinct paths, and the directory above
  `govkit/` in each has one segment and two segments respectively.
  Red when: a restated criterion repeats one input where it names two, or puts one outside the
  window it probes.
- **AC15** — When a `python -c` probe prints
  `check_writes_intersect(["tools/policy/"], x.py"])` and then
  `a.py"], ab.py"])`, it prints `True` then
  `False`.
  Red when: the render's overlap rule misreads a directory over a file or a shared string prefix.
- **AC16** — When
  `bash -c '. lib-unattended.sh; overlaps tools/policy/ x.py; echo $?; overlaps a.py ab.py; echo $?'`
  runs, it prints `0` then `1`, the answers AC15 gives.
  Red when: the render and the dispatcher disagree on either pair.
- **AC17** — When `check_writes_intersect` is staged in a scratch copy to compare the raw strings
  with `startswith` in either direction, the AC15 probe prints `True` for the second pair.
  Red when: the arm's disjoint pair cannot tell a raw prefix compare from containment.
- **AC18** — When `--fixture budgets-census-join` runs after this unit, it prints `RED as planted`
  for the `no-such-cap` request and for the row with no case, and no `WRONG`.
  Red when: the census join goes quiet in a receipt-less tree.
- **AC19** — When `python check_policy.py --fixture budgets-census-join census-receiptless-target census-adopter-receipt census-default-adopter census-ambiguous-registry`
  runs, it prints no `WRONG`.
  Red when: a census case expects a tree answer its repository no longer reads.
- **AC20** — When an install-day target, committed with the install staged and uncommitted as
  `TOOL-dGroundRules-24` §4 steps 1 to 3 leave it, holds a `policy.toml` written before
  `--scaffold` that sets `budgets.enforce` outside its `allowed` set with `policy-file.on-invalid`
  at `refuse`, `bash adopt-policy.sh --scaffold --target <t>` exits non-zero, prints the
  `arm_schema` finding naming `budgets.enforce`, and prints no `mirror deferred`.
  Red when: an invalid policy file is deferred on install day.
- **AC21** — When a case target's receipt holds `{"kits":["policy"],"prefix":"C:/x"}`, then
  `{"kits":["policy"],"prefix":"..\\x"}`, then `{"kits":["policy"],"prefix":"/x"}`, and
  `python check_policy.py --repo <t>` runs, `arm_cap_census` prints one finding naming `prefix` for
  each.
  Red when: a drive, backslash or absolute prefix grades enforcers outside the target.
- **AC22** — When a scratch copy has `{probe_answer}` staged into one closure kit descriptor's
  `[adopt]` argv and `--fixture adopter-fresh-target` runs there, it prints `WRONG` carrying
  `Refusing to invent one` and `probe_answer`.
  Red when: a token outside the destinations reaches `apply` unanswered.
- **AC23** — When a probe prints `read_deploy_answers("<repo>")`, the dict holds `manifest_path` and
  `user_skills`, and no `govkit-selftest:` line is printed; with `DEPLOY_FULL` renamed in a scratch
  copy's selftest.py, the probe prints `WRONG` naming selftest.py.
  Red when: the answers come from an import that runs `resolve_gov_pin`, or from a copy that drifts.
- **AC24** — When `--fixture adopter-fresh-target` runs over a tree carrying one uncommitted edit,
  `git cat-file -e <the snapshot sha8 it printed>` in the source exits non-zero; with
  `build_source_snapshot` staged in a scratch clone to run its `add -A` under the source's own
  `.git`, the same command exits 0.
  Red when: the snapshot commit lands in the tree under test's object store unseen.
- **AC25** — When a scratch clone of the built tree has its hook's `KIT_AGENT_CAP_VERSION` staged to
  `0.0` with the writer marker intact and the workflows render runs there, the rendered
  `unattended-build.js` carries `gov:fixed-writers` on the spec-writer split and stderr holds no
  `govkit update --kits agent-cap`.
  Red when: the render keys the writer marker on a version by any spelling.
- **AC26** — When `ORDER_ROWS | wc -l` runs, it prints the same number as
  `grep -ho "· order [0-9]*" memory/builds/dGroundRules/spec/*.md | sort -u | wc -l`.
  Red when: the region drops, repeats or adds a step.
  figure: both counts are DERIVED at observation time.
- **AC27** — When `--fixture adopter-fresh-target` runs, its snapshot line carries `files` and `s`,
  and the file count equals `git ls-files -co --exclude-standard | wc -l` over the same tree.
  Red when: the snapshot's size and cost are stated rather than measured.
  figure: DERIVED at observation time; 5888 tracked files at `f4d31452a` is PINNED for §4 only.
- **AC28** — When the AC2 probe runs with its working directory set to a fresh directory under
  `%TEMP%`, outside the fixture repository, it prints no `WRONG` and the two lists are equal.
  Red when: a relative `--git-path` result resolves against the caller's working directory.
- **AC29** — When `--fixture adopter-fresh-target` runs, it prints no `WRONG`; with `run_govkit`
  staged in a scratch copy to run the source's own deployer past its refusal, it prints `WRONG`
  naming `gov_source`.
  Red when: the case cannot tell which checkout installed its target.
- **AC30** — When AC6's staging runs, the stderr line carrying `does not admit the writer split:`
  holds neither `verifier-fanout: FAILED` nor a path under the render's temporary directory.
  Red when: the notice prints the gate's header in place of the hook's reason.
- **AC31** — When a scratch clone's hook is staged to exit 1 printing nothing and the workflows
  render runs there, its stderr carries `exited 1 with no reason` and no `FAILED —`.
  Red when: an empty hook answer leaves the notice quoting the gate's header.
- **AC32** — When `git show f4d31452a:README.md | grep -n "gen:build-order"`
  runs, it prints lines 165 and 179.
  Red when: the evidence cites lines its stated revision does not hold.
- **AC33** — When `grep -n "run_in_gov" check_policy.py` runs under the kit, it prints a line inside
  `run_govkit`'s docstring, and `GOVKIT_LINES` still prints nothing.
  Red when: the reuse audit's reason for not reusing `run_in_gov` is absent or wrong.
- **AC34** — When `python tools/memory-tree/gotchas.py --for-paths tools/govkit/govkit.py` runs, its
  output names `suite-invalidated-by-a-commit-under-it` and `test-oracle-read-from-a-historical-sha`;
  and `grep -n "build_source_snapshot" memory/gotchas/suite-invalidated-by-a-commit-under-it.md`
  prints the new paragraph.
  Red when: the record naming `_cmd_apply`'s HEAD stamp still prescribes a clone that grades HEAD.
- **AC35** — When C is the pass commit that built `TOOL-dGroundRules-32` and
  `git diff --name-only C~1 C -- "memory/builds/*/README.md"` runs, it prints only READMEs §4
  "Writes `TOOL-dGroundRules-32` declares" names.
  Red when: that commit writes a build README no spec of this build declares.
- **AC36** — When `awk '/^## Install/{f=1;next} /^## /{f=0} f' policy.md | grep -c "mirror deferred"`
  runs, it prints `1` or more.
  Red when: the deferral line sits outside the section an installer reads.
- **AC37** — When `grep -n "arm_cap_census" README.md` and `grep -n "legacy-homes" README.md` run
  under the kit, each prints a table row carrying `invalid`.
  Red when: the kit README's census rows still state three answers.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `spec-tokens self-test` · `harness arms (fail branches armed or pinned)` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the cases;
they are named by the arm lines, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py --fixture · covers AC8 AC13 AC18 AC19 AC22 AC29 · each case named in S8, S13, S18, S19, S22 and S29, its stated input staged in its temporary repository or scratch copy · none
New arm: tools/check-spec-tokens.test.sh · covers AC17 · `check_writes_intersect` staged to a raw string-prefix compare, against `overlaps` on the prefix pair · that suite's assertion count, raised by the arm
New arm: tools/policy/adopt-policy.test.sh · covers AC20 · an invalid policy file planted before the install-day `--scaffold`, replacing `TOOL-dGroundRules-31` AC4's staged `policy.py` · `ARMS_FLOORS`, as `check-arms.py --emit-floors` prints it
New arm: tools/workflows/check-protocol-parity.test.sh · covers AC6 · `TOOL-dGroundRules-30`'s writer-marker arm, which replaces TOOL-dGroundRules-25's AC18 arm; the hook's writer marker staged to another string in a scratch clone · none

## 8. Open questions

- **F1 — How does `--scaffold` refuse an invalid policy file before it defers the mirror (finding
  32)?** (a) It runs the installed `check_policy.py --repo <t>` and reads `arm_schema`, meeting AC20
  through the real control flow; validating in `policy.py` opens the working-tree file, which
  `TOOL-dGroundRules-2` S2 rules out. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — How does `check_policy.py` read `DEPLOY_FULL`'s answers (finding 19)?** (c) An `ast` read
  of `selftest.py`'s own assignment: one carrier, no copy and no import, meeting AC23; a shared
  module imports across kits, which `tools/codebase-map/map_lib.py:1505` forbids. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (c). widens: none · relaxes: none
- **F3 — Where does the false-green HEAD shape live (finding 21)?** (a) In
  `suite-invalidated-by-a-commit-under-it`, which names `_cmd_apply`'s HEAD stamp, the historical-sha
  record pointing to it and keeping its anchors; moving the HEAD paragraph out reds
  `TOOL-dGroundRules-28` AC1 and AC2. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F4 — How do the census cases keep their join in a receipt-less fixture repository (findings 24
  and 33)?** (a) Under `unadopted` the arm withholds only enforcer presence and keeps the join, meeting
  AC18 and AC19; copying the registry and its enforcers into unit 1's base fixture repository turns
  every case's repository into gov's tree. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F5 — How does `run_govkit` refuse every root no snapshot made (findings 4 and 34)?** (a)
  `build_source_snapshot` records its roots and `run_govkit` refuses any other; a
  `--show-toplevel` check admits a stale `--local` clone, failing AC10. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F6 — How does the snapshot read the source's exclude file (findings 2, 10, 22 and 31)?** (a)
  Copy it into the snapshot's `info/exclude`, keeping `TOOL-dGroundRules-26` S1's `add -A`;
  `-c core.excludesFile=<it>` drops the user's own excludes file, failing AC2. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft from the round-1 spec audit of units 26 to 32, twenty-three MEDIUM and fourteen LOW findings.
- rev-2 · 2026-10-23 · §3 · hands-off edges to units 38-41 and 43 added.
- rev-3 · 2026-10-23 · §1 §3 §4 §5 §8 §10 · prose shortened under the spec ceiling; no meaning moved.
- rev-4 · 2026-10-24 · §7 §9 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; older revision lines condensed under the spec ceiling; no design change.
- rev-5 · 2026-10-24 · §1 §2 §6 §8 §9 · a criterion code span rejoined onto one line and prose shortened under the spec ceiling; no design change.

## 10. Reuse audit

Each item extends the seam its row names: `TOOL-dGroundRules-26`'s `build_source_snapshot`
(S1 to S4, S24, S27 to S29), `TOOL-dGroundRules-27`'s `run_govkit` (S7 to S10, S33),
`TOOL-dGroundRules-29`'s `derive_census_tree` and `arm_cap_census` (S11 to S14, S18, S19),
`TOOL-dGroundRules-32`'s `check_writes_intersect` and the dispatcher's `overlaps` (S15 to S17),
`govkit.py intake` and `needed_answers`, the one derivation of the answers a closure needs (S22),
`DEPLOY_FULL` in `tools/govkit/selftest.py`, read in place (S23), the render's probe through
`check-verifier-fanout.sh` (S25, S30, S31), `arm_schema`, the one grader of a working-tree policy
file (S20), and the gotcha record `suite-invalidated-by-a-commit-under-it` (S34).
`python tools/codebase-map/reuse_lookup.py "install a kit into a scratch target with the deployer and read its receipt"`
ranked `read`, `read_text`, `scratch`, `kit_rel` and `resolve_kit_dir` among name-stem hits; the
other seams came from the files the review cites, each verified at `f4d31452a`.
`tools/govkit/matrix.py`'s `run_in_gov` was weighed for S9 and S10 and not reused (S33). The recall
probe returned the prior minors batches `TOOL-dGroundRules-25` and `TOOL-dGroundRules-32`, whose
per-finding table this unit follows, and this audit's own items.

Recall terms used: `python tools/memory-recall/query.py "how are review minors batched into one
repair unit" --terms "minors batch promoted medium low disposed severity spec-audit repair unit write
set"`
