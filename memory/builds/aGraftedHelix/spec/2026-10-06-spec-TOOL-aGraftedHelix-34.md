# TOOL-aGraftedHelix-34 — every red arm of the owed unattended suites is fixed, proved inherited, or proved a pool-contention race, and each one not fixed here is filed

**Status:** SPECCED · rev-1 · 2026-10-06 · node a · Tier-2 · base 290d0d2d · streams tooling · order 18 · ratified 2026-10-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-prompt-TOOL-aGraftedHelix-34-1-spec-brief.md](../prompts/2026-10-06-prompt-TOOL-aGraftedHelix-34-1-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The unattended suites the close owes ran once, pooled eight-wide, on a frozen clone at `90a6f6fae`,
and came back red. This unit classifies every real red arm of that sweep by a slice observed on
frozen clones at this branch's HEAD `b5d40c61` and at origin/main `290d0d2d`. It fixes the one cause
this build introduced, and files the rest as asks, so the close's attributed Definition of Done can
name a record for each suite that stays red.

## 2. Scope (IN)

- **S1** — The AC3 arm of the driver suite's GH-1 block stages its unanswering remote on BOTH URLs of
  `origin`. It reads `remote.origin.pushurl` into a local before the staging, sets the fetch URL and
  the push URL to the missing path, runs `--claims`, then sets the fetch URL back to `$ORIGIN` and
  the push URL back to the value it read, or unsets it when it read none. No assertion is added or
  moved, so the suite's floors stay as they are. Observed by AC1 and AC2.
- **S2** — Six asks are filed in this build's own backlog file, one per cause group in §4's ask
  table, each in `tools/memory-tree/backlog.py`'s ask grammar with a `seen` clause at `290d0d2d` and an
  `accept` clause. Each ask gets a SEV row at the severity the table gives and a KEEP row in the same
  commit. The ids are the ones the main loop names in this unit's build brief (§3 Edges). Observed by
  AC3.
- **S3** — The pass re-observes the inherited classification: each inherited slice §4 names prints,
  at `290d0d2d`, the FAIL lines §4's disposition table quotes for it. Observed by AC4.
- **S4** — The pass re-observes the contention classification: the ledger slice and the resume-tick
  slice print no FAIL line alone at the pass's commit, and the start-token probe moves a fresh
  sleep's token under fork load. Observed by AC5.
- **S5** — The unattended kit's version moves one minor step in every carrier
  `tools/check-kit-versions.sh` pairs, once, after the pass's last move, and the rendered guides and
  the Skill are re-adopted from their templates in the same commit. Observed by AC6.

## 3. Non-goals (OUT)

- **Fixing an arm or a product path this build did not cause.** The brief's rule 3 binds: an
  inherited red is proved and recorded, never fixed here. S2 files each one instead, and adopting any
  of those asks as a unit is the main loop's decision under protocol §11.
- **Calibration.** The count-only MISMATCH rows (adopter e2e, gate shards 2 to 5, stall-recorder,
  stop-guard) and gate shard 8's pooled bound are the close's `--calibrate`, per the brief.
- **Arms added after `90a6f6fae`.** Units 29 to 33 added arms, check 51's in gate shard 8 among
  them, and each unit observed its own by a slice. The close's sweep is their first whole run.
- **Which URL `read_claims` fetches.** Claims live on the remote the landing push goes to, which is
  the shared brief's I1, so reading the push URL is the design. The arm was wrong, not the reader.
- **Running any suite whole, or the merge bar.** Every observation here is a slice.

### Edges

- **consumes-from** external — the main loop mints six ask ids under this run's slug in the TOOL
  family and names them in this unit's build brief. Charter §2 bars a fan-out child from minting, so
  without them the pass files nothing and AC3 stays red.
- **hands-off** external — the close: the pooled `--calibrate` over the count-only rows and over
  gate shard 8, and the attributed verdict, where an arm §4 calls a pool-contention race may red at
  L and not at R. The close re-runs that arm's slice alone before it reads the red as new.

## 4. Design

### Evidence

Every reading below is PINNED: measured on node `a` on 2026-10-06, each slice run once on a
`git clone --local` frozen at the named sha under a short `%TEMP%` root, with `TMPDIR` pointing
there. No suite was run whole. The sweep's own logs are the frozen clone's
`.git/gate-logs/selftests/*.out` at `90a6f6fae`; the FAIL lines quoted come from there and from the
slices.

The slices were built by one recipe: a suite's prologue, then the named blocks, with the shard gate
lines (`if in_shard N; then` and the region-closing `fi`) left out and a trailer appended that
prints the executed count and exits with the suite's status. Each slice sits inside its clone's kit
directory, because every prologue resolves the driver from its own directory. The block bounds are
anchor texts, so the recipe survives line moves:

| Slice | Suite | Blocks after the prologue |
|---|---|---|
| `cr` | driver | `crbc='--override build-complete` through the line before `# ---- TOOL-cBriefedPilot-4: --preflight REFUSES` |
| `sa` | driver | the line `bcsetup; bcrestore`, then the block headed `TOOL-aGradedMandate-1` through `git checkout -qf unit; BCP=$_sa_bcp0; bcreset` |
| `s4pw` | driver | `# Rule 1 - a function that writes the phase must also stage` through the S4 rule 1 FAIL line, then the `writers=` line and the one after it |
| `gh1` | driver | the block headed `TOOL-aGraftedHelix-1 — THE RUN CLAIM ON THE REMOTE`, to its closing `fi` |
| `trgh1` | driver | the `scope()` line, the arm from `echo "MARK ac1-refused" >&2` through its two restoring `set-url` lines, then `gh1`'s block |
| `pl` | driver | `slice_fn()`, the block headed `TOOL-dDerivedDocket-28: the run-owned process ledger` to its region `fi`, then the region block from `# ---- AC6:` through the line before `TOOL-dDerivedDocket-27` |
| `cc` | cross-component | lines 1 through arm 3b's two `same` lines |
| `s1` | gate | `# ---- EVERY DISPATCHED VERB IS DOCUMENTED` through the dispatched-verb FAIL line |
| `c39` | gate | the block headed `TOOL-dDerivedDocket-4: the phase-read routing` through the control's `a phase reader holds no read` line |
| `g0` | gate | `reset_tree`, then `ma_root=$(mktemp -d)` through the AC5 hit naming `ruling D12-j` |
| `rt` | resume-tick | the AC4 block to the line before `# ---- U12`, then the AC13 HUNG block to the line before the AC13 IMAGE block |

### The dispositions

No arm is already fixed at HEAD: every red the sweep printed reds, or races, identically at `b5d40c61`
and at `290d0d2d`. The brief's guess that shard 8's G0 failure follows from its fixture no-op is
wrong: `g0` carries no check-39 block and reds alone.

| Red (suite · arm) | Disposition | Evidence |
|---|---|---|
| driver · closing-review arm 5, `base: abc`, `missing: closing-review-recorded` | inherited, `a52f744e` | `cr` reds at both trees, 38 assertions each, with the same `check 104` refusal: the arm passes `--override build-complete` to a close that LANDING_NODES hands off, which is refused before the DoD prints |
| driver · `S4 rule 1 does NOT fire` | inherited, `a52f744e` | `s4pw` reds at both. `verb_close` carries two `stage_or_fail` calls since the hand-off branch, so stripping the one after the LANDING write leaves the other and the rule stays silent |
| driver · `the driver has 8 phase writer(s)` | inherited, `e63806aa` | `s4pw` reds at both. `--settle`'s LANDED write is the eighth `set_fact "$rel" phase`, and the arm pins 7 |
| driver · conf-dies arm, `could not be evaluated to the end` and `specs-audited — not gradable` | inherited, `a52f744e` | `sa` reds at both, 91 assertions each. The landing-node read of the dying conf hands off at the advertised tip before either sentence prints |
| driver · GH-1 `AC3 an unanswering remote exits 2` and its check-109 sentence | OURS, unit 1's arm | `gh1` alone is green, 150 assertions. `trgh1` reds with exactly the sweep's two lines, 152 assertions, `GOT: gA other live - unknown`. The refused-endpoint arm restores with `git remote set-url --push origin "$ORIGIN"`, which leaves a push URL set; `resolve_claim_remote` reads `get-url --push`, so AC3's fetch-URL staging never reaches the reader. S1 fixes it |
| driver · ledger AC6, its no-write check and its second hold; ledger AC12's KEPT line and its ledger check | pool contention, code inherited from `1acce23d` | `pl` is green alone at both trees, 79 assertions each, 256 s and 263 s. The same slice with this build's blocks between the fixture and AC6 is green, 636 assertions, 1757 s; three calls to `write_aged_commit`, a helper defined outside that slice, failed there as unknown commands. `run_bounded`, `write_proc_record` and `derive_proc_state` are byte-identical at both trees, and so are the arms |
| cross-component · `arm 3b: the leg is silent` | inherited, `d99cd032` | `cc` reds at both, 15 assertions each: check 23 prints its `check 23 fleet` line on every run that grades a pass, and `remove_announcements` does not strip it |
| gate shard 1/8 · dispatched verb absent, `--highs` and `--minors` | inherited, `131537ae` | `s1` reds at both, 34 assertions each: `_denied` lacks the two `--review` arguments that commit added |
| gate shard 8/8 · `fixture no-op` on check 39's arm two | inherited, `9dbc09be` | `c39` reds at both, 11 assertions each. That commit rewrote the `verb_preflight` line the sed anchors on |
| gate shard 8/8 · the G0 fixture and three `may:`-grant arms | inherited, `d6d51fa0` | `g0` reds at both with the same five FAIL lines, 9 assertions. That landing merge respelled the greps to `bin/lander-granted.sh` and left the three seds writing `tools/` |
| gate shard 8/8 · killed at its 6260 s bound | inherited cost growth | the region grew from 57 leg-run sites at its 2026-09-24 pooled reading (`b7377232`) to 174 at `290d0d2d` and 179 here. A sed-site count, re-derivable over the region's lines. The no-op costs nothing: `c39` took 203 s stale and 202 s with the anchor respelled, green. A fixed fixture cannot bring the shard inside its bound |
| resume-tick · `AC4 the sleep is gone from tasklist`, `AC13 the hung launched pid is gone from tasklist` | pool contention, arms inherited from `1df36af3` and `9808fe1d` | `rt` is green alone at both trees, 6 passed each. The suite from its prologue through AC13, in order, is green, 70 passed. Three `rt` runs at each tree under twelve fork loops are green |

### The contention mechanisms

The ledger's is MEASURED. A fresh `sleep 30 &` has its start token, field 22 of its procfs stat
line, read at once by the suite's own `read_pl_token` and again 0.5 s later. Idle, 0 of 30 trials
moved. Under twelve fork loops, 3 of 30 moved, by 75 to 130 ticks. The token read before the exec
is the forked shell's. The ledger arms read it at that moment, and so does the driver: `run_bounded`
calls `write_proc_record` on `$!` as soon as `&` returns, and the job it forks execs `bash`. Under
load `derive_proc_state` then reads the arm's live sleep as `reused`, and the sweep printed exactly
that: `NOT reaped 9193 — exited, pid reused`. The driver's own bar takes the same code path, so the
same misread can reach it; that half is inferred from the code and was not observed on a real bar.
So this is a race in origin/main's recorder, and the arms surface it.

The resume-tick one is UNVERIFIED. The arms read `tasklist` the moment the tick's
`taskkill //PID … //T //F` returns, and termination may still be in flight under load. Fork load did
not reproduce it, so the disposition rests on elimination: green alone, green in order, and the arms
and the kill path are identical at origin/main.

### The fix (S1)

```bash
gh_pu=$(git config --get remote.origin.pushurl || true)
git remote set-url origin "$ORIGIN_DIR/no-such-remote.git"
git remote set-url --push origin "$ORIGIN_DIR/no-such-remote.git"
out=$(bash "$SCRIPT" --claims 2>&1); rc=$?
git remote set-url origin "$ORIGIN"
if [ -n "$gh_pu" ]; then git remote set-url --push origin "$gh_pu"; else git config --unset remote.origin.pushurl; fi
```

The assertions under it are unchanged. The block's own exit line, which sets the fetch URL back to
`$ORIGIN`, stays as it is.

### The asks (S2)

`<A1>` to `<A6>` stand for the ids the build brief names; `<date>` is the pass's date. Each row
is followed in the Dispositions section by `- SEV · <id> · <severity> · <why>` and by
`- KEEP · <id> · filed by an unattended run for the owning build; outside this build's goal`.

| Ask | SEV | why | Covers |
|---|---|---|---|
| `<A1>` | MED | a held self-test suite reds on three stale fixtures; no product defect | the driver's inherited rows |
| `<A2>` | HIGH | under load the driver can read its own live process as exited, then hold or abort over it | the ledger arms |
| `<A3>` | MED | a held self-test suite reds on a stale denylist; no product defect | gate shard 1/8 |
| `<A4>` | MED | a held self-test suite reds on two stale fixtures; no product defect | gate shard 8/8's arms |
| `<A5>` | MED | a held self-test suite reds on a stale silence assertion; no product defect | cross-component |
| `<A6>` | LOW | an arm asserts a forced kill finished the moment it was issued; the tick's behaviour is unaffected | resume-tick |

```text
- <A1> · filed <date> · inherited red: leg unattended driver selftest red at 290d0d2d, three stale arms: the phase-writer population pins 7 where --settle made the driver's writers 8 (e63806aa); S4 rule 1's red fixture strips one of verb_close's two stage calls (a52f744e); closing-review arm 5 and the conf-dies spec-audit arm pass an override to a close LANDING_NODES hands off, refused at check 104 before the DoD prints (a52f744e) · seen `tools/unattended/unattended.test.sh`@290d0d2d run `bash tools/unattended/unattended.test.sh` · accept the four arms are green at the default branch's tip
- <A2> · filed <date> · inherited red under load: leg unattended driver selftest at 290d0d2d, the ledger arms AC6 and AC12 red in an eight-wide pool and are green alone; run_bounded's recorder reads a process's start token the moment its job is forked, before the exec moves it, so derive_proc_state can read the driver's own live bar as exited, pid reused, and --hold and --abort then proceed over work in flight (1acce23d) · seen `tools/unattended/unattended.sh`@290d0d2d run `bash tools/unattended/unattended.test.sh` · accept a recorded process keeps the token its ledger line carries across its own exec under load, and the ledger arms are green in an eight-wide pool
- <A3> · filed <date> · inherited red: leg unattended gate selftest shard 1/8 red at 290d0d2d, the verb-surface arm counts --highs and --minors, arguments of --review, as verbs because its flag denylist lacks them (131537ae) · seen `tools/unattended/check-unattended.test.sh`@290d0d2d run `bash tools/unattended/check-unattended.test.sh --shard 1/8` · accept the verb-surface arm is green at the default branch's tip
- <A4> · filed <date> · inherited red: leg unattended gate selftest shard 8/8 red at 290d0d2d, two stale fixtures: check 39's arm two seds a verb_preflight line 9dbc09be rewrote, so it edits nothing; the G0 fixture writes its may: grant as tools/lander-granted.sh while its greps read bin/lander-granted.sh (d6d51fa0), so G0 and the three grant arms red · seen `tools/unattended/check-unattended.test.sh`@290d0d2d run `bash tools/unattended/check-unattended.test.sh --shard 8/8` · accept check 39's arm two and the G0 arms are green at the default branch's tip
- <A5> · filed <date> · inherited red: leg unattended cross-component red at 290d0d2d, arm 3b asserts the leg silent while check 23 prints its fleet line on every run that grades a pass (d99cd032), and remove_announcements does not strip it · seen `tools/unattended/cross-component.test.sh`@290d0d2d run `bash tools/unattended/cross-component.test.sh` · accept arm 3b is green at the default branch's tip
- <A6> · filed <date> · inherited red under load: leg unattended resume-tick selftest at 290d0d2d, AC4 and AC13 read tasklist the moment the tick's forced taskkill returns, and red in an eight-wide pool while green alone and in order (1df36af3, 9808fe1d) · seen `tools/unattended/resume-tick.test.sh`@290d0d2d run `bash tools/unattended/resume-tick.test.sh` · accept AC4 and AC13 are green in an eight-wide pool
```

A concurrent build on another branch, aMendedFleet, specs the G0 half of `<A4>` as its unit 101.
Its census predates every other introducer named here. The ask paraphrases that unit rather than
citing its id, because the id resolves nowhere in this tree.

### Inventory

Nothing is minted: no function, file of code, leg, conf key or naming cell. The backlog file is a
record, and the six ask ids are the main loop's.

### Rollout

Edit the arm, file the asks, bump the kit, re-adopt the rendered guides and the Skill, and
re-render the generated views with `python tools/memory-tree/gen_build_index.py --write`. One commit.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`, the GH-1 AC3 arm
- `tools/unattended/unattended.sh`, the version line only
- `tools/unattended/`, every other version carrier
- `memory/guides/`, the rendered unattended guides, re-adopted
- `.claude/skills/unattended/SKILL.md`, re-adopted
- `memory/builds/aGraftedHelix/`, its new backlog file
- `memory/backlog/TOOL.md` and `memory/LIVE.md`, by the index generator

### Alternatives rejected

Each with the test that rejected it, per BUILD-METHOD M12.

- **Fixing the leftover at its source**, so the refused-endpoint arms unset the push URL rather
  than setting it to `$ORIGIN`. Those arms are origin/main's, which §3's first non-goal keeps out,
  and the GH-1 arm would still depend on whatever a later arm leaves. `trgh1` against `gh1` is the
  test: the arm's verdict moved with an earlier arm's leftover.
- **Staging the push URL alone.** Under the staged break where the reader fetches the fetch URL,
  that arm reds for a reason its name does not state, so it would pin a second property. Staging
  both keeps it on its subject, an unanswering remote.
- **Moving the reader to the fetch URL.** It changes product behaviour to suit a fixture, against
  the shared brief's I1.
- **One ask per arm, or one per suite.** Per arm would ask the main loop for fifteen ids for six
  causes. Per suite would join the driver's stale fixtures with its product race, whose severities
  differ.

## 5. Production-readiness checklist

- security — N/A: a test fixture and records; no write path, no new surface.
- perf / scale — two git config calls added to one arm; nothing else runs.
- error / empty / loading states — a slice whose fixture fails prints its FAIL and exits non-zero,
  as the suite does. An origin/main slice printing none of its quoted lines stops the pass before
  any ask is filed (AC4).
- observability — every ask carries a runnable `seen` and an `accept`, so each inherited red is
  reproducible from the record alone.
- risks — the contention arms may red again in the close's pooled run, and under the attributed
  verdict a race red at L and green at R reads as NEW; the hand-off in §3 covers it. The ledger
  mechanism is measured on node `a` only, and the resume-tick one is UNVERIFIED.
- testing — AC1 and AC2 observe the fix red then green; AC4 and AC5 re-observe the classification.
- migration — none.
- user docs — N/A: suites and records internal to the kit.

## 6. Acceptance criteria

Every criterion runs on a `git clone --local` frozen at the named sha under a short `%TEMP%` root,
with each slice built by §4's recipe inside the clone's kit directory and deleted after. A staged
break is made in the clone's own copy and nowhere else.

- **AC1** — When the `trgh1` slice runs on a clone at the pass's commit, it prints no `FAIL` line and
  its trailer reads `(152 assertions executed)`.
  Red when: the arm stages its remote on the fetch URL alone while a push URL is set, as at
  `b5d40c61`, where the same slice printed `FAIL AC3 an unanswering remote exits 2: expected [2], got [0]`
  beside the missing check-109 sentence. Staged twice in the clone: the S1 edit reverted, and,
  separately, the case arm of `read_claims` that sets `CL_WHY` on a failed fetch emptied in the
  clone's driver, so a failed fetch reads as a read. Each prints the AC3 FAIL line.
  cost: about seven minutes on node `a`.
  figure: 152 is PINNED, measured at `b5d40c61`; S1 adds no assertion.
- **AC2** — When the `gh1` slice runs on a clone at the pass's commit, with the line
  `git config --get remote.origin.pushurl || echo NONE` appended before its trailer, it prints no
  `FAIL` line, `(150 assertions executed)`, and `NONE`.
  Red when: the arm's restore leaves a push URL set in a tree that had none, which every later arm
  reading the push remote inherits. Staged: the restore written as
  `git remote set-url --push origin "$ORIGIN"`, which prints the origin path in place of `NONE`.
  cost: about eight minutes on node `a`.
  figure: 150 is PINNED, measured at `b5d40c61`.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --asks --build aGraftedHelix --all` runs
  at the pass's commit, it lists the six asks the build brief names, each OPEN with a `seen` clause
  at `290d0d2d` and an `accept` clause, and the build's backlog file carries one SEV row at §4's
  severity and one KEEP row for each.
  Red when: a cause §4 groups is left with no filed record, so the attributed Definition of Done the
  kit README states cannot name one for that suite. Staged: in a clone at the pass's commit, one
  ask's three rows taken out, which lists five.
  figure: six is PINNED, the cause groups of §4's ask table.
- **AC4** — When the slices `cr`, `sa`, `s4pw`, `cc`, `s1`, `c39` and `g0` run on a clone at
  `290d0d2d`, each prints the FAIL lines §4's disposition table quotes for it, and none prints a
  FAIL line the table does not name.
  Red when: a slice prints none of its quoted lines at `290d0d2d`, so that arm is not inherited and
  this spec misclassified it; the pass stops there, before any ask is filed, and the spec is amended.
  cost: about nine minutes on node `a` with the seven run concurrently.
- **AC5** — When the `pl` and `rt` slices run alone on a clone at the pass's commit, neither prints
  a `FAIL` line; and when the start-token probe, the suite's own `read_pl_token` read on a fresh
  `sleep 30 &` at once and again 0.5 s later, runs 30 trials idle and 30 under twelve fork loops, the
  idle trials move no token and the loaded ones move at least one.
  Red when: a slice reds alone, which makes that arm a defect rather than a race and moves it to S1's
  kind; or the loaded probe moves no token, which leaves `<A2>`'s mechanism unproved and its text
  false, so the ask is not filed as written.
  cost: about five minutes on node `a`.
  figure: 0 of 30 idle and 3 of 30 loaded are PINNED, node `a` 2026-10-06. The loaded count is a
  sample, and any count above zero passes.
- **AC6** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no unattended carrier, and `bash tools/check-kit-versions.sh` exits 0.
  `KIT_UNATTENDED_VERSION` in `tools/unattended/unattended.sh` reads one minor step above its value at
  the pass's parent.
  Red when: the kit's shipped bytes moved without its version.
  figure: both versions are DERIVED from the pass's parent at observation time.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · GH-1 AC3 now stages the push URL beside the fetch URL and restores what it found; stage the S1 edit reverted behind the refused-endpoint arm, and the fetch-failure case of read_claims emptied · none, no assertion is added

The close runs the legs and the suites. A pass runs the slices of §6 and the commands of AC3 and
AC6 as its check.

## 8. Open questions

- **F1 — Is a red that reds only in the eight-wide pool fixed here, adopted as its own unit, or
  filed?**
  Option A fixes both races in this unit: the recorder reads a process's token only after its exec,
  and the resume-tick arms poll `tasklist` within a bound. Option B has the main loop adopt each as a
  new unit now. Option C files each as an ask carrying its evidence, `<A2>` and `<A6>`, and leaves
  adoption to the main loop.
  A is the most feature-rich, and it violates §3's first non-goal, which the brief's rule 3 states:
  neither race is this build's, since the code and the arms are byte-identical at origin/main. It is
  also a second mechanism in a product function this build never touched, which BUILD-METHOD M2
  makes a unit of its own. B is not a spec writer's act: an adoption is the main loop's, under
  protocol §11, and it needs an ask or a finding to adopt from. C is that precondition.
  RESOLVED (agent, 2026-10-06, delegated): C. Both races are filed with their evidence, `<A2>` at
  HIGH because the recorder's misread can reach `--hold` and `--abort`; adoption stays open to the
  main loop. Veto 1 removes A, and B is outside this unit's authority.

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, adopted mid-run after the owed suites ran red on a frozen
  clone at `90a6f6fae`. Every red arm was sliced on frozen clones at `b5d40c61` and `290d0d2d`, and
  a start-token probe measured the ledger race on node `a`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "attribute a red self-test arm to the branch or to
origin/main by slicing the suite"` ranked name-stem neighbours, `armed`, `attribute_paths` and the
`check-arms.py` branches among them. It printed `unscanned layers: .sh`, so it cannot see the five
suites, which are all shell; no existing seam fits a classifier of held-suite reds, and the
classification here is a record, not code. The seams this unit extends are the suites' own:
their prologues and blocks, sliced rather than re-run, and the GH-1 arm itself. S2 reuses the ask
grammar in `tools/memory-tree/backlog.py` and the inherited-red row shape `write_inherited_asks`
in `tools/unattended/unattended.sh` writes at the close. That function files only bar legs from the
close's own attribution file, so it cannot be called for a held self-test suite, and S2 writes its
row shape by hand. The recall probe returned the asks other builds filed for held-suite reds,
among them `TOOL-aHonedRuleset-16` (a stale sed target in the gate suite) and
`TOOL-aSightedSkeptic-12` (an inherited red filed by ask), plus the brief itself; no record covers
any red §4 names.

Recall terms used: inherited red attribute selftest suite fixture no-op mutate stale fixture backlog origin/main slice arm

The question passed with them: "how are pre-existing red arms in the unattended kit self-test
suites attributed and recorded as inherited rather than fixed".
