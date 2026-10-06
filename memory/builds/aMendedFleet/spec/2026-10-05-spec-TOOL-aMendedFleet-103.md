# TOOL-aMendedFleet-103 — the hygiene suite's python-parity arm exempts `GRAMMAR_WHERE` beside `GRAMMAR_DIR`

**Status:** CLOSED · rev-1 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · order 104

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The held `memory-hygiene self-test` reds on the daily remote CI job with two FAIL lines. One is the
stdout-codec class, cause C1 of the held-red census, which unit 97 owns. The other is cause C7, and it
is a tree defect that reds on node a too: the suite's python-parity arm reports
`.memory-tree.conf.example does not declare GRAMMAR_WHERE`. `GRAMMAR_WHERE` is not a conf key. It is
a module-level constant of `tools/memory-tree/corpus_ids.py`, and that module's own selftest arms
save and restore it through `globals()` beside `GRAMMAR_DIR`, which the arm already exempts for
exactly that reason. This unit adds the one missing name to the arm's exemption list and to the
comment that justifies each entry.

## 2. Scope (IN)

- **S1** — `_pyexempt` in `tools/memory-tree/check-memory-hygiene.test.sh` gains `GRAMMAR_WHERE`,
  placed after `GRAMMAR_DIR` so the list stays sorted. Observed by AC1 and AC2.
- **S2** — The comment block above `_pyexempt` names `GRAMMAR_WHERE` on the line that already
  explains `GRAMMAR_DIR` and `READ_PATH_RULES_GATE` as module constants reached through `globals()`,
  so every exempted name keeps its stated reason. Observed by AC3.
- **S3** — The remote observation: the first scheduled run of the remote CI workflow after landing no
  longer carries the C7 line. Observed by AC4.

## 3. Non-goals (OUT)

- The suite's other FAIL, the check-20 arm that greps for a UTF-8 em dash `row_grammar.py` wrote as
  the byte 0x97. That is cause C1, unit 97's, and this job stays red until both units land.
- Declaring `GRAMMAR_WHERE` in `tools/memory-tree/.memory-tree.conf.example`. It is not an override
  any adopter could set; `corpus_ids.py` computes it from where the memory-recall kit resolved.
- Narrowing `_pykeys` so a `globals()` receiver is never read. The arm's own header, written by node
  d's dDerivedDocket unit 50, keeps the receiver UNCONSTRAINED on purpose and says over-reading reds by
  NAME and is fixed in one line. That is this unit's whole change.
- Moving the memory-tree kit version. The suite is a withheld, `project-owned` file under
  `tools/memory-tree/kit.toml`'s self-test rule, and the build moves every kit version it owes once,
  after the last pass touching that kit; the close's `kit epoch` leg grades that.

### Edges

none

## 4. Design

### Evidence

Read at HEAD `34a99ad1`, whose bytes for every file below equal base `7af5f564` and `origin/main`.

- The census row for cause C7, in
  `memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md`, quotes
  the CI FAIL and places it at the suite's `_pyexempt` line.
- `corpus_ids.py` reads `globals()["GRAMMAR_WHERE"]` at lines 1108, 1111 and 1115, the save-and-restore
  pair commit `cb80898d0` added beside the existing `GRAMMAR_DIR` swap. That commit did not touch the
  hygiene suite, which is how the exemption list fell one name behind.
- Replaying the arm on node a: `_pykeys`, `_pyparity` and the `_pyexempt=` line, cut from the suite
  into a scratch script and run over `tools/memory-tree` with its example conf, print exactly the C7
  line. The same replay with `GRAMMAR_WHERE` appended to the list prints nothing.
- The arm is graded in both directions already: over a scratch copy of the kit's modules whose
  `GRAMMAR_WHERE` reads were rewritten away, the replay with the name exempted prints `the python
  exemption names GRAMMAR_WHERE, which no module ... reads any more`. So the exemption this unit adds
  cannot outlive its reader silently.

### Mechanism

Two edits in one file. The `_pyexempt=` string becomes
`... GOV_DEFAULT_BRANCH GRAMMAR_DIR GRAMMAR_WHERE PATH READ_PATH_RULES_GATE`, and the comment line
`GRAMMAR_DIR READ_PATH_RULES_GATE — this module's OWN module-level constants` names `GRAMMAR_WHERE`
beside them. No arm, function or floor changes, and the suite's assertion count `n` is unchanged.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`

### Alternatives rejected

- **Declare the name in the example conf.** It would document a key nobody may set, and the arm would
  then demand every future save-and-restore constant be dressed as configuration.
- **Exclude `globals()` reads from `_pykeys`.** It fixes the class, and it is the narrowing the arm's
  header argues against: a conf dict may be bound to any name, and the arm's fixtures exist to prove
  the receiver is not anchored. A by-name exemption asserted in both directions is the contract the
  arm already states.

## 5. Production-readiness checklist

- security — N/A: a test file's exemption list; no input, write path or surface.
- perf / scale — N/A: one word in a list the arm already iterates.
- error / empty / loading states — the arm's existing empty-derivation and stale-exemption lines are
  unchanged and still fire.
- observability — N/A: the suite's FAIL lines are the signal, and one of them stops.
- risks — an exemption could mask a real future conf key spelled `GRAMMAR_WHERE`; the stale-exemption
  direction reds the moment `corpus_ids.py` stops reading it, which bounds that.
- testing — AC1 to AC3 are direct and take seconds; AC4 is the held job's.
- migration — N/A.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When the arm is replayed on node a, it prints nothing: the `_pykeys` and `_pyparity`
  definitions and the `_pyexempt=` line are cut from the hygiene suite by `sed -n` into a scratch
  script under the session scratchpad, which calls `_pyparity` over the kit directory with
  `tools/memory-tree/.memory-tree.conf.example` and that list, run by `bash`.
  Red when: `GRAMMAR_WHERE` is absent from `_pyexempt`, which at base printed the one line
  `.memory-tree.conf.example does not declare GRAMMAR_WHERE`.
  figure: the key set is DERIVED at observation time from the kit's own modules.
- **AC2** — When AC1's replay runs over a scratch copy of the kit's `*.py` files in which
  `tools/memory-tree/corpus_ids.py`'s `globals()["GRAMMAR_WHERE"]` reads are rewritten to another
  name, it prints the stale-exemption line naming `GRAMMAR_WHERE`.
  Red when: the replay stays silent, so the new exemption would outlive its only reader.
  fixture: the copy is built in the scratchpad from the tracked modules; the tree is never edited.
- **AC3** — When `grep -n 'GRAMMAR_WHERE' tools/memory-tree/check-memory-hygiene.test.sh` runs, it
  prints two lines: the comment that states why module constants are exempt, and `_pyexempt=`.
  Red when: only the `_pyexempt=` line carries the name, so the exemption has no stated reason.
- **AC4** — When the first scheduled run of `.github/workflows/remote-ci.yml` after landing completes,
  `gh run view` with `--log-failed` over its `memory-hygiene self-test` job carries no line naming
  `GRAMMAR_WHERE`.
  Red when: the CI log still prints the C7 line.
  permission: the suite is held; no unit pass runs it, and the main loop reads this log after landing.
  The job's conclusion may stay `failure` on cause C1 until unit 97 lands; this criterion reads the C7
  line, never the conclusion.

## 7. Gates

`memory-hygiene self-test` · `spec tokens (a spec's own names resolve)`

The guards join owes no further leg: the one path in Files touched trips only the broad `tools/` and
`tools/memory-tree/` guards, which `tools/check-spec-tokens.py` excludes and prints.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the held-red census row for C7 and the arm replayed on node
  a in both directions at base.

## 10. Reuse audit

The seam is the arm's own exemption list, `_pyexempt` in
`tools/memory-tree/check-memory-hygiene.test.sh`, which already carries `GRAMMAR_DIR` for the same
`globals()` save-and-restore; no new mechanism is owed. `python tools/codebase-map/reuse_lookup.py
"exempt a module constant read through globals from the example-conf parity arm"` returned only
conf-loader symbols (`load_conf`, `parse_conf`, `read_conf`) and printed `unscanned layers: .sh`, so
it cannot see a shell arm at all; the seam was found by reading the suite. Recall returned node d's
dDerivedDocket unit 50 spec and its acceptance ledger, whose rev-2 amendment widened the same
exemption list by name to the module constants the unconstrained receiver reads; that is the
precedent this unit follows. The map dossier `memory/map/features/memory-tree-hygiene.md` describes the
exemption list as asserted in both directions, which the replay confirmed.

Where the report and the tree disagree: none. The census read the CI log; this spec re-observed the
same line on node a, so C7 is a tree defect on every host, not only the runner.

Recall terms used: `python tools/memory-recall/query.py "why does the hygiene suite's python parity arm exempt names read through globals, and what was decided about over-reading" --terms "_pyexempt _pykeys python-parity example-conf globals GRAMMAR_DIR GRAMMAR_WHERE exemption stale-exemption receiver unconstrained dDerivedDocket-50"`
