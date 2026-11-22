**Serves:** research TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19

# Spec brief — dQuietDisk, the nineteen units and what they share

You author specs and write no product code. Read these in order before your first line:

1. The prompt record, `memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md`, whole. Its
   brief's Acceptance, Gates, Non-goals and Limitations bind every unit.
2. The build README, `memory/builds/dQuietDisk/README.md`. Its build-level rules bind every spec.
3. The analysis, `memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`. Your unit's
   rework id (K1 to K12) is named below. §3 holds the evidence rows, and §4 says why each design churns.
4. `memory/TEMPLATE-SPEC.md` and the build method's sections `doc.build-method#m2-the-spec-set-decompose-detect-classify-act`, `doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`, `doc.build-method#m5-recall-and-reuse` and `doc.build-method#m12-research-test-choose-when-the-solution-is-not-given`. Units 1 to 18 are Tier 2,
   because each changes a shipped kit's contract. Unit 19 is Tier 1, because it writes only records.

## What every spec here must hold

### Read the code at dWitnessedBar's tip, not at this branch

Read every file named below at `59e882afd` (`git show 59e882afd:<path>`). That commit is the tip of
`branch/unattended-dwitnessedbar-2ed3b3`.
- dWitnessedBar is the dClosedLoop chain's Test build, still running, and it changes most of these files. The units
  are built on its landed tip, never on this branch's copy.
- Cite a code fact as `<path>@609cd40b1:<line>` or by symbol name. Never cite a bare line number that this
  branch's copy would resolve differently.
- Never write into that branch or its worktree.
- Read its specs under `memory/builds/dWitnessedBar/spec/` where your unit touches its area. Units 4, 5, 6, 8, 25,
  30 and 41 are the verdict, held-leg, selection and flake units.
- Contradict none of them. Where your mechanism meets theirs, extend theirs. Name the overlap in §3 or §10, so the
  merge can reconcile it.

### Say which chain build owns the area

The README rule maps each unit to the chain build that owns its area. Name that build in §10.
- **dWitnessedBar** (Test): gate health, held legs, verdicts, budgets.
- **dSafePassage** (Supersession): govkit update and apply. Its specs under `memory/builds/dSafePassage/spec/`, units 5, 10 and 25 to 27, are CLOSED, so read them.
- **dScopedBuild** (Build): the history-derived exit base.

### Verdicts are unchanged

Every unit is an optimisation, and §6 proves the verdict did not move:
- the same rc;
- the same findings, byte for byte, where the tool prints them;
- the same RED and GREEN arms.

For a history leg, the observation is an equivalence corpus: the old and the new leg over the real tree at the
build's base, with the store cold and then warm, compared byte for byte. Then one planted change regrades its unit
red, where the old leg reds too.

### Count what was saved

§6 also states the saving as a count:
- git processes, via `GIT_TRACE2_EVENT=<dir>`, by counting the files in it;
- peak and residual temp entries, with `TEMP`/`TMP`/`TMPDIR` pointed at a scratch dir;
- or both.

Give the bound the unit promises. Measure in a scratch `git clone --shared`, never in the worktree.

### The cache is a switch

Every new cache, store or skip is a switchable policy. The default is the answer, and the other value is today's
behaviour (owner principle). Look for an existing key under `tools/policy/` before adding one. A new key lands with
its catalogue row.

### Safe fallback

A missing, unreadable, partial or foreign-version store entry costs a saving, never a verdict: that item is graded
as today. Any key holds the blob id of the grading code itself, the leg's script and every library it sources, so a
change to the checker invalidates its own entries. The gotcha classes `append-without-an-idempotence-key`,
`suite-invalidated-by-a-commit-under-it`, `history-leg-graded-before-the-reconcile-commit` and
`test-oracle-read-from-a-historical-sha` all apply. Read each before writing §6.

### What a pass may run

No unattended-kit suite is ever run: `check-unattended.test.sh`, `unattended.test.sh`, `check-pass-order.test.sh`,
`check-brief-recorded.test.sh`, or anything `run-unattended-gates.sh --selftests` drives. That is the owner's rule of
2026-08-23.
- A criterion on those checkers is observed by a hermetic probe or the equivalence corpus.
- A new arm in such a suite goes on a `New arm:` line, and the main loop observes it.
- No other §6 criterion names a gate, the bar or a `GATE_*=` prefix either.

### Adopters

Kit changes reach nc, ic and swydee (`tools/govkit/adopters.toml`) only through a minted kit version and
`govkit update`. A unit whose kit an adopter installs states, in §6:
- the adopter fixture under `tools/govkit/fixtures/` it is proven on;
- that `govkit check` against `C:/projects/incms/main` and `C:/projects/nicocares/main`, run read-only from gov,
  reads the same before and after.

### Order verbs

Give each unit the order below in its status header. Two units share an order only when their write sets are
disjoint (M6). If your reading of the code shows they are not, re-order and say why in §9.

## The units

### 1 — the history verdict store (K5, K6) · order 1 · dWitnessedBar, dScopedBuild

One store of immutable verdicts for history legs. Each item, a unit or a commit, is stored under the ids it reads:
- its build commit;
- its spec blob and any record blobs;
- the blob of the grading code.

The store also holds the last graded tip per leg and per repository, so a leg grades only `rev-list <last>..HEAD`
plus the items whose keys moved.

It lives under the git common dir, beside the reuse cache. That way every worktree shares it, nothing pushes it, and
it is never a ref.

It comes with one reader: a `git cat-file --batch` coprocess helper in `tools/lib/`, one per leg run, which units 2
to 4 call instead of a spawn per question. `tools/memory-tree/routed_commits.py@7ef53bccab4f:454` and `tools/lexicon/lexicon.py@a4787e4f4051:4241-4292` already
hold coprocesses. Fold the shape into one helper rather than writing a third, and find whether `tools/lib/` already
has one.

Prior art:
- `TOOL-aPiecewiseGrade-1` and `-2`, the spec-token checker's per-spec incremental cache with live generations. It
  is the closest seam, so extend its shape.
- The reuse cache block of `tools/run-gates/run-gates.sh` (TOOL-aSparedSpawn-13).
- `TOOL-dUnstuckLanding-7` and `-17`, RANGE-mode history legs.

Concurrency: two bars finishing together lose no entry, by tmp-then-rename. Pruning is by age, in one process.

### 2 — `check-pass-order.sh` incremental · order 2 · dWitnessedBar, dScopedBuild

- Grades only units whose key moved since its last graded tip, through unit 1's store and reader.
- Includes the reads it makes through `tools/unattended/lib-unattended.sh` (around line 1323 at main) and its own
  loops (`check-pass-order.sh` around 475-531 and 599-630 at main; re-find them at `59e882afd`).
- The analysis counts about 11.5k git processes per run; state the bound after the change.
- `TOOL-aMeasuredDrag-1` already narrowed `--check-commit`, so read it first.

### 3 — `check-brief-recorded.sh` incremental · order 2 · dWitnessedBar, dScopedBuild

As unit 2, for `check-brief-recorded.sh` (around 520-619 at main). Its `_SUBJ` subject cache (around 450-459) is
the in-run half that already exists. Persist it through unit 1, and do not add a second store.

Units 2 and 3 both read `lib-unattended.sh`. If both must write it, sequence them and say so.

### 4 — `routed_commits.py` incremental · order 2 · dWitnessedBar, dScopedBuild

- `tools/memory-tree/routed_commits.py` runs `git log --raw --numstat` over every commit (around 353 and 410-413 at
  main), measured at 1,761 s, PINNED in the analysis.
- Grade only commits past its last graded tip, with each commit's verdict keyed by its id and the grading code's
  blob.
- Read `TOOL-aMeasuredDrag-1`'s findings record (`memory/builds/aMeasuredDrag/build/2026-11-15-build-TOOL-aMeasuredDrag-1-findings-gate.md`), which proposed exactly this.

### 5 — one guard diff per bar (K6) · order 2 · dWitnessedBar

- `run-gates.sh` runs a serial `git diff --quiet BASE -- <guard>` per guarded leg (around 3249-3295 at main).
- Replace that with ONE `git diff --name-only BASE` read once per bar, matched against each leg's guard in-process.
  The guard-matching rule must not change; `changed-mode-selection-ignores-doc-reads` applies.
- dWitnessedBar's `select` (`tools/run-gates/verdict_flow.py`) and the held-selftest selection program in
  `run-gates.sh@609cd40b1` around 3300-3370 already run one `diff --name-only <sha>` per recorded sha. Reuse that
  read where the bases agree.

### 6 — the scoped pickaxe · order 2 · dScopedBuild

- `skills/session-kickoff/manifest-check.sh` runs an unscoped `git log -G` (around 1971 at main).
- Scope it by the paths it can match and by the range since its last-audit stamp. It must give the same answer.
- `skills/session-kickoff/` stays at the repository root (README rule). dWitnessedBar unit 27 changed this file.

### 7 — the suite template cache (K1, K2) · order 1 · dWitnessedBar

Generalise `tools/lib/lib-selftest.sh` and `tools/govkit/fixture_target.py` into ONE template-cache factory:
- a bash face and a python face;
- each distinct base repository (kit copied in, configured, committed) is built once per runner invocation;
- keyed by the kit tree hash;
- held under the runner's owned `$WORK` (`run-selftests.sh` gives each pooled row `SWEEP_ROOT/<row>/tmp`; find the
  equivalent for a direct suite run).

Each case gets one of two things:
- a mutating case: a `git clone --shared` (objects not copied), or `git worktree add --detach`;
- a reading case: a path to one read-only checkout.

Fold in the local templates: `tools/check-wiring.test.sh@214f029f82db:40-52` `NEWREPO_SEED` and
`skills/session-kickoff/manifest-check.test.sh@3eaf707dd66e:60-70`. Moving the suites onto the factory is units 10 to 13, not
this one. This unit proves the factory on one small consumer of `lib-selftest.sh` that it already serves.

### 8 — one tree snapshot per bar (K3) · order 2 · dWitnessedBar, dSafePassage

ONE `clone --shared --no-checkout` plus a sparse checkout of only the paths the readers read, built once per bar and
handed by path. No `--no-hardlinks`. Its readers:
- `tools/run-gates/foreign-prefix.gov.test.sh` (around 453);
- `tools/chain-packet.test.sh` (around 295);
- `tools/policy/check_policy.py` `build_source_snapshot` (around 1270-1290) and its two callers in
  `tools/loop/factories.py`;
- `tools/govkit/selftest.py` (around 5867);
- `tools/govkit/matrix.py` (around 976);
- `tools/govkit/upgrade_walk.py` (around 230). dSafePassage unit 5 owns the upgrade walk; read it.

A reader that needs a different revision or a moved prefix (foreign-prefix moves the tool root three times) states
how it derives that from the shared snapshot without a full copy. If one reader cannot share, say which and why,
and leave it as today.

### 9 — the owned, swept scratch root (K12) · order 1 · dWitnessedBar

- **Python:** one helper sets `tempfile.tempdir` to the runner's owned root when one is exported, and removes trees
  with a chmod-and-retry handler (`onexc=` on 3.12+, `onerror=` below the floor).
- **Bash:** the same through `tools/lib/`.
- Every `shutil.rmtree(..., ignore_errors=True)` and `TemporaryDirectory(ignore_cleanup_errors=True)` under
  `tools/` and `skills/` moves to it.
- A gate-lint row reds a new one, with a waiver registry on the `dead-path-waivers.txt` pattern. This is G-C's
  rmtree clause, which fits this unit cleanly. The other G-C clauses are asks.

Read `run-gates.sh@609cd40b1` around 2333-2358, the `$WORK/tmp` owner and sweep block, and extend it rather than
copying it. Run a candidate predicate over the real tree first (`[class]`), and list the population it finds in §6.

### 10 to 13 — suites on the template cache (K1) · order 3 · dWitnessedBar

One suite per unit, each on unit 7's factory:
- 10 `tools/check-wiring.test.sh` (measured: 255 arms, 42 `newrepo`, 3,786 git processes, 307 s, PINNED in the analysis);
- 11 `tools/govkit/selftest.py` (102 `build_target`/`build_scratch_gov` calls, 144 `apply`);
- 12 `.githooks/pre-push.test.sh` (49 fixture builders, 75 real pushes);
- 13 `tools/run-gates/run-gates*.test.sh`, the suites `.test`, `.turnstile`, `.evidence` and `.gov`.

Each keeps every arm and its RED and GREEN result, and counts its git processes and temp entries before and after.

Unit 11 and unit 18 may both write `selftest.py`. If so, order 11 after 18 and say so.

### 14 — the kit attestation, written by gov (K4) · order 1 · dWitnessedBar

A content-addressed record that kit `<name>` at a given tree passed its self-tests: the tree hash, the gov sha and
the run that proved it.
- It is written only from a real green held run of that kit's suites. The `gate-selftest-last/` records in
  `run-gates.sh@609cd40b1` around 5780-5810 are the per-leg evidence that already exists.
- It is carried to adopters with the minted kit, through `govkit update`'s existing write path.

The hash must identify what an ADOPTER holds. govkit renders kit literals at the install prefix, so gov's source
tree id is not the adopter's bytes. Find how the receipt already records what it wrote (`tools/govkit/registry.toml`,
the receipt schema), and decide which hash both ends can compute. The analysis's K4 row and `WIRE-INTO-PROJECT.md`
name the homes.

### 15 — the attested kit leg is held (K4) · order 2 · dWitnessedBar

In an adopter's bar, a kit self-test leg is HELD when its kit's vendored bytes match an attested hash. Its selection
source is a new word beside `level` and `quarantine` in `verdict_flow.py` `select` (`SELECTION_SOURCES`), not a
second selection program. The leg RUNS as today when:
- the hash is unknown;
- the attestation is missing or unreadable;
- the vendored kit was edited.

Each of those is seen on an adopter fixture.

First establish WHY adopters run gov's kit suites today. Kit-subject legs are held unless `GATE_SELFTESTS=1`, and
gov sets that in `.githooks/gate-env.sh`, which ships nowhere. Find what incms `scripts/gov-bar.sh` (with its
`scripts/run-gates/gate-legs.json`) and nicocares `scripts/nc-bar.sh` actually execute: read them, write nothing
there. State what this unit changes in their bars, and that it reaches them only through `govkit update`.

### 16 — `govkit update` reads through one batch handle (K7) · order 1 · dSafePassage

`tools/govkit/upgrade_steps.py` `blob_at(..., batch=)` (around 2628) takes a handle that no caller passes. The
callers are in `tools/govkit/govkit.py`, around 9993, 9244-9245, 9481 and 9490 at main. Thread one handle through
an update, and give the same receipts and writes on the fixtures.

### 17 — each `adopt-*.sh --check` once per update (K7) · order 2 · dSafePassage

The check runs before writing (`govkit.py` around 11169) and again in verify (around 12507). Keep the pre-write
result keyed by the kit tree hash and the target tree hash. Skip the verify re-run when neither moved, and run it
when either did.

### 18 — `govkit apply` baseline from the reuse cache (K8) · order 3 · dSafePassage, dWitnessedBar

`read_gate_verdicts` builds the before and after maps from two whole target bars (`govkit.py` around 6239, 7763 and
8465). Instead:
- The before map comes from the target's reuse cache (`GATE_REUSE`) for its HEAD. Only legs with no reusable verdict
  run.
- The after run re-runs only legs whose guards meet the files apply wrote.

"Green before, red after" stays computed per leg, and a planted red-after leg is still refused.

### 19 — the measurements (Tier 1) · order 4 · dWitnessedBar

The record of the before and after numbers, with the instruments beside them. It covers:
- `tools/check-wiring.test.sh`;
- the pass-order leg, cold and warm;
- one `tools/govkit/selftest.py` shard;
- the nicocares seed suite, read from the nicocares side session's record.

The instrument for each is:
- git processes, by `GIT_TRACE2_EVENT` file count;
- peak and residual temp entries, by a 0.5 s watcher;
- wall time.

The "before" readings are taken by the main loop at the build base, before the first pass, as a records commit. The
unit pass takes the "after" readings and writes the comparison. Every reading runs in a scratch `git clone --shared`
with its own `TEMP`.
