# TOOL-cWidenedNet-1 — the extension class widens, the gate derives its own sidecars, and the root spelling is graded over the received set

**Status:** CLOSED · rev-2 · 2026-09-13 · node c · Tier-2 · base c4f02308 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-cWidenedNet-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-cWidenedNet-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-install-prefix.sh` cannot see a literal naming a `.txt`, `.tsv`, `.conf` or
`.conf.example` path, and cannot see a root-install spelling inside a received test, selftest or
example conf. Close both, so the gate grades the class it claims rather than the subset its
predicate happens to reach.

## 2. Scope (IN)

- **S1** Both arms' extension alternation gains `txt|tsv|conf|example`. The lead-character class,
  the loose-file existence filter and the `{`/`}` placeholder exclusion are unchanged. Observed by
  AC1 and AC2.
- **S2** The single live root-install spelling the widening exposes is FIXED. It is
  `tools/memory-tree/README.md:57`, a `cp` step naming `memory-tree/.memory-tree.conf.example`,
  which fails in every adopter that installed the kit under a prefix. Observed by AC1.
- **S3** `PREDICATE_EPOCH` moves 2 to 3 with an epoch comment saying what the predicate now sees,
  and `--rebaseline` re-derives `tools/install-prefix-carried.txt` once. Every hand-written reason
  column survives the write. Observed by AC3.
- **S4** The gate derives its own two sidecar paths instead of spelling them. `WAIVERS` and
  `CARRIED` are resolved from the script's own tracked location, and an empty derivation REFUSES
  rather than falling back to a guessed prefix. Observed by AC4.
- **S5** Arm 1's population gains the files it excludes by suffix WHEN those files are in the
  received set, derived from the same descriptor resolution arm 2 already uses. Where that
  derivation is unavailable the repo is not a kit source, and the arm announces the narrower
  population rather than passing silently over it. Observed by AC5 and AC6.
- **S6** A root spelling on a line carrying the inline marker `gov:root-fixture` followed by a
  non-empty reason is exempt. A marker with no reason is a refusal, not an exemption. Observed by
  AC5.
- **S7** The six broken usage headers are fixed, and the deliberate fixture lines take markers with
  reasons. `tools/drift-audit/selftest.py` repeats one literal twelve times, so it takes a module
  constant and one marker rather than twelve. Observed by AC1 and AC5.

## 3. Non-goals (OUT)

- The 31 carried-prefix occurrences the widening exposes are NOT fixed. They are rebaselined under
  the epoch, which is what the epoch exists for, and the ban then holds them at the new floor.
  Draining them belongs to `DEPL-dCarriedReceipt-15`, which already owns that class.
- `TOOL-aScouredKit-21` stays open. `tools/check-testsuite-counts.sh` hardcodes its manifest path
  and its waiver root, and that is an engine defect rather than a predicate gap.
- No change to how `.conf.example` VALUES are stamped at install. `adopt-codebase-map.sh` stamps
  `MAP_DIFF_CMD` per prefix with a tested decline path, and that mechanism is correct as it stands.
- No new gate leg and no new registry file. This unit changes one predicate, one population and one
  exemption rule inside a leg that already runs.

### Edges

- **consumes-from** external — `TOOL-aScouredKit-20`, the OPEN backlog row that measured both
  blindnesses and specified the remedy shape. Without its measurement this unit would be widening a
  predicate on a hunch.
- **hands-off** external — `DEPL-dCarriedReceipt-15` receives the 31 rebaselined rows as its
  working set, now visible where before they were not.

## 4. Design

### Data model

The exemption for the new root-spelling class is an inline marker, not a registry row. The marker is
`gov:root-fixture` followed by a reason on the same line, matching the `gov:literal-python` and
`gov:literal-resolve` idioms already in this tree. Positional keying was rejected on recorded
evidence rather than on taste: `install-prefix-waivers.txt` keys on `<path>:<line>` and any edit
above a waived line unpins it, which reds a merge touching nothing the waiver guards.

### Migration

`--rebaseline` runs exactly once, guarded by the epoch it just bumped. The mode refuses when the
recorded epoch and the declared one agree, so it cannot be spent twice on this change and cannot
absorb a literal added afterwards.

### Files touched (estimate)

`tools/check-install-prefix.sh` · `tools/check-install-prefix.test.sh` ·
`tools/install-prefix-carried.txt` · `tools/memory-tree/README.md` · the twelve received files
carrying a root spelling · `memory/map/features/install-prefix.md`.

### Alternatives rejected

A third arm beside the carried one was rejected: arm 1 already owns the root predicate, its waiver
loop and its stale-row detection, and a second copy of that logic is a second place for the two to
disagree. A file-level opt-out was rejected because it re-creates the hole being closed — a usage
header inside an opted-out file stays invisible, which is how this gap arose.

## 5. Production-readiness checklist

- security — N/A. No write path, no untrusted input, no egress. The gate reads tracked text.
- perf / scale — the leg's declared ceiling is 2940s and it runs in seconds; the population grows by
  52 files and the predicate by four alternatives.
- error / empty / loading states — an empty derived population is already a REFUSAL on both arms,
  and S5's conditional population adds a third case that announces itself.
- observability — `--list` remains the one emitter for both the report and the artifact, so the
  widened predicate cannot report one thing and record another.
- risks — the widening is definitional, so it necessarily makes many literals visible at once. That
  is the exact failure mode the epoch guard was built for, and it is spent here.
- testing — `tools/check-install-prefix.test.sh` gains an arm per new behaviour, each staged RED
  before it is wired.
- migration — one `--rebaseline` write, reversible by `git checkout` of the ratchet file.
- user docs — `memory/map/features/install-prefix.md` refreshes its prose and its `[paths]` globs.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-install-prefix.sh` runs over the tree after S1, S2, S5 and S7,
  arm 1 reports clean over a population LARGER than the one it graded before, and names a non-zero
  count of marked fixture lines.
  Red when: `tools/memory-tree/README.md:57` is waived instead of fixed, so the run is green over a
  live root spelling; or the marked count is zero, which would mean S5's population growth never
  reached a fixture and the arm is clean because it graded nothing new.
  figure: every count on that line is DERIVED at emission time. Measured on this build: 207 files
  before, 257 after, 20 marked lines. None of the three is pinned by the criterion.
- **AC2** — When a fixture shipped file names a kit sidecar at a root spelling, with the .txt
  extension the predicate could not see, `bash tools/check-install-prefix.sh` exits 1 and names it;
  the same fixture at the declared prefix is clean.
  Red when: the extension alternation is widened in `re_ship` only, so arm 1 stays blind and the
  fixture passes.
- **AC3** — When `--rebaseline` runs with `PREDICATE_EPOCH` at 3 against a ratchet recording 2, it
  rewrites `tools/install-prefix-carried.txt`, preserves every fourth-column reason, and a second
  invocation REFUSES.
  Red when: the second invocation also rewrites, which would make the mode a self-service exemption
  form under a new name.
- **AC4** — When the gate runs from a checkout where its own directory is not `tools/`, it resolves
  `install-prefix-waivers.txt` and `install-prefix-carried.txt` beside itself and reports the same
  verdict as at the default prefix.
  Red when: the derivation falls back to a literal `tools/` on an empty result, which is the shape
  that makes a broken install look like a working one.
  fixture: `tools/check-install-prefix.test.sh` already builds prefixed scratch repos; this reuses
  that helper.
- **AC5** — When a received test carries an unmarked root spelling, the run exits 1 and names it;
  when the same line carries `gov:root-fixture` with a reason, the run is clean; when it carries the
  marker with no reason, the run exits 1. The run is `bash tools/check-install-prefix.sh`, and no
  backticked token here wraps a line — the checker pairs backticks per line and a wrapped span makes
  it pair the wrong two.
  Red when: the marker is honoured without a reason, which makes the exemption self-service.
- **AC6** — When the govkit derivation is unavailable, `bash tools/check-install-prefix.sh` prints
  a line naming the population it did NOT grade, and exits 0.
  Red when: it prints a clean verdict over the narrower population with no announcement, which is
  the skip-that-looks-like-a-pass class.
- **AC7** — When `bash tools/check-install-prefix.test.sh` runs, every new arm above is exercised
  and each one has been observed RED with its fix unstaged before landing.
  Red when: an arm is wired without its failing case ever being seen, which asserts nothing.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `codebase-map coverage + freshness` · `line length`

New arm: `tools/check-install-prefix.test.sh` · a fixture shipped file spelling a widened-extension path, and a received test carrying an unmarked root spelling · none

## 8. Open questions

- **F1 — should `conf` and `example` join the extension class, or only `txt` and `tsv`?**
  `TOOL-aScouredKit-20` names all four. Measured over today's tree the `conf`/`example` half
  contributes the single arm-1 hit that S2 fixes and one arm-2 occurrence, so the cost is small and
  the coverage is the row's own. Recommendation: take all four.
  RESOLVED (agent, 2026-09-13, delegated): all four, per the owner's instruction to close both gaps
  as measured and reported.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · AC1 · AC2 · AC6 · the criterion pinned arm 1's file count as UNCHANGED, which S5
  contradicts by design — the population grows by the received tests. Rewritten to observe the
  growth and the marked count instead, both derived. Caught by running it.

## 10. Reuse audit

- The seam is `tools/check-install-prefix.sh` itself, which already owns both predicates, the waiver
  registry, the ban list, the epoch guard and the stale-row loop; `reuse_lookup.py install prefix
  literal predicate` returns the `install-prefix` dossier and the `testsuite-counts` affordance seam
  covering `install` and `prefix`, and no seam outside this file grades a path spelling. The marker
  idiom being extended is `gov:literal-python`, already live in seven files.
- Recall terms used: `install-prefix carried-prefix predicate-epoch rebaseline root-install
  usage-header selftest-exclusion waiver-keying shipped-surface ban-list sidecar-registry
  literal-ban`
