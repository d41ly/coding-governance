**Serves:** journal TOOL-dQuietDisk-28

# gov-spec-writer handoff — TOOL-dQuietDisk-28

<!-- gov:handoff role=gov-spec-writer build=dQuietDisk unit=TOOL-dQuietDisk-28 path=memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-28-1-spec-writer.md role-sha=91ec0ce505aa task-sha=43b56e56b4ad -->

## Role

[.claude/agents/gov-spec-writer.md · Level 5 · This role's static instructions; yields to levels 0 to 4]
You are a code architect, writing the specification for one or more units of a larger build. You are
not writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design.

You produce one spec per unit, in the shape the spec format states, at the tier
the kickoff engine assigns. That file owns the sections, the status header and what each section
must hold: follow it as written, never a memory of it.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite where you read it in the
  form the spec format's writing rules give. A claim you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the naming lexicon over your specs, and grade each spec you wrote with memory
  hygiene's spec-format check as `check-memory-hygiene.sh --only 12 --spec <path>`. The whole-tree
  gate reads tracked files only, so it never grades a spec you have not committed, and it grades
  every other spec for minutes. Where this repository has it, run the spec-token checker as
  `check-spec-tokens.py --spec <path>` over each spec you wrote. Fix every finding either check
  names before you return. You run no other gate.
- When your task names the unattended driver's `--check-specs` command, run it before you return;
  it prints each refusal `--dispatch` would make from your specs, in its words, and you fix every
  one naming a unit of yours.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3). Never decide one
  silently.

You are not building. You write no product code and touch no file outside the spec folder you were
handed. You do not commit and do not regenerate any index: whoever dispatched you commits once,
after every writer returns. At a spec audit's disposal, a correction to an unbuilt sibling's spec
rewrites that sibling's text, with a rev bump and a revision-log line naming the repair unit and
the review record by its file stem, and a CLOSED sibling stays frozen.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## House rules

A `check-spec-tokens.py --spec` run that finds a miss exits 1. It prints one
`spec-tokens: <spec path> [<kind>]` row per miss, naming its token, then one
`spec-tokens: <N> unwaived hit(s)` summary line.
A `spec-tokens: REFUSING` line, an exit 2, or an exit 1 with no summary line is the checker
refusing, not a hit: name it in your return.

### Drive

- spec-write · gov-spec-writer — a build whose units lack a spec or hold a thin one: `Workflow <prefix>/workflows/unattended-build.js`
[/.claude/agents/gov-spec-writer.md]

## Task

[AGENTS.md#practices-at-design · Level 0 · Non-negotiable project instructions, always enforced unless the owner explicitly overrides them; the override is recorded]
### Practices at design

- [yagni] no extension point, option or layer the unit does not use
- [reuse] a kind's second instance extracts its factory
- [core] logic and authorization live in one core, each surface a thin adapter
- [contract] one source, generated copies, a parity gate against a live re-derivation
- [derive] status, counts, inventories and indexes are generated or declared
- [one-fact] each value has one owning source
- [gate] state what a gate does not check
- [class] a guard shares no state with what it guards
- [cost] declare a wall-clock ceiling for each suite
- [migrations] every migration is reversible
- [security] deny by default and give automation the narrowest grant
- [bound] a fan-out declares its bound
[/AGENTS.md#practices-at-design]

## Card

[.claude/orientation-card.md · Level 1 · the build's card: where this session stands; level 0 outranks it]
- build: dQuietDisk
- unit: TOOL-dQuietDisk-14 · spec memory/builds/dQuietDisk/spec/2026-11-20-spec-TOOL-dQuietDisk-14.md
- brief: memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-14-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-28-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dQuietDisk`, unit `TOOL-dQuietDisk-28`.
Not supplied, optional: `input:code`.

### brief:prompt

> Background (from the session that started this one):
> C: (Intel RST RAID 0 NVMe, about 88% full) sits at 100% active time from small-file and git-process churn caused by the governance and test workflows in coding-governance (gov), incms and nicocares.
>
> A read-only analysis session measured and traced the causes: hermetic per-case git repos, history legs whose cache keys include HEAD, adopters re-running gov's kit selftests, govkit baseline bars, and unswept test output. That session wrote the report referenced in the brief, which ranks the reworks.
>
> Temp-leak fixes have already landed: gov `5a311c9fa`, incms `b4850abfb`, nicocares `bb2e6543`. The owner is separately turning off 8.3 names and last-access updates on C:.
>
> Commits in these repos follow strict governance (specs, gate bars, landers), and other sessions are active:
> - dWitnessedBar's unattended build run in gov;
> - gov-upgrade runs in the incms and nicocares `gov-upgrade` worktrees.
>
> Integration with those runs and with gov's adopters is the owner's explicit requirement.
>
> Task:
> Build fixes 1–4 from the disk-churn analysis as an UNATTENDED run. Use this repo's `/unattended` skill, under gov's own governance (spec → build → closing review → bar → lander).
>
> The owner's words, which are your authorization for an unattended run: "Gather all the necessary details and build fixes 1-4 in an unattended handoff session, ENSURING it cleanly integrates into the in-progress dClosedLoop rebuild and works cleanly with gov's adopters."
>
> READ FIRST: the full report, `C:\Users\d41ly\AppData\Local\Claude-Data\claude_pzs8sxrjxfjjc\side-session-notes\local_22c30fbd-4971-4107-b3d9-acd2fca20e6a\disk-churn-analysis.md`. It has file:line evidence, measured numbers and the rework ids (K1–K12, P1–P8, R1–R8) used below.
>
> ## The four fixes
>
> **Fix 1 — history checks cache their answers and batch git (K5 + K6).**
> - `check-pass-order.sh`, `check-brief-recorded.sh` and `routed_commits.py` currently regrade all of history on every commit.
>   - Their cache key includes HEAD: `tools/run-gates/run-gates.sh@a1ea1e57d8fa:3370`, `head $RG_HEAD` for legs declaring history.
>   - They launch git once per question: `tools/unattended/lib-unattended.sh@1c5ed3436d86:1323`, `tools/unattended/check-pass-order.sh@7a0e27e6ea1e:475-531, 599-630`, `tools/unattended/check-brief-recorded.sh@ffb59f089e03:520-619`, `tools/memory-tree/routed_commits.py@7ef53bccab4f:353, 410-413`.
> - Cache each unit/commit verdict under the commit and blob ids it reads, and grade only new units (`rev-list <last-graded>..HEAD`).
> - Use one `git cat-file --batch` coprocess per leg. `tools/memory-tree/routed_commits.py@7ef53bccab4f:454` and `tools/lexicon/lexicon.py@a4787e4f4051:4241-4292` already do this.
> - Run one `git diff --name-only BASE` for all guarded legs instead of one per leg (`tools/run-gates/run-gates.sh@a1ea1e57d8fa:3249-3295`).
> - Scope the pickaxe in `skills/session-kickoff/manifest-check.sh@0784ef8f1b4b:1971`.
>
> **Fix 2 — fixtures built once per suite (K1 + K2 + K3 + K12).**
> - Generalise `tools/lib/lib-selftest.sh` and `tools/govkit/fixture_target.py` into one template cache, keyed by kit tree hash, under the runner's owned `$WORK`.
> - Each test case gets a `git clone --shared` or a worktree of the template.
> - Arms that only read share one read-only checkout. Arms that mutate get a `--shared` clone.
> - Build ONE shared sparse no-checkout snapshot for:
>   - `tools/run-gates/foreign-prefix.gov.test.sh@cd32e4001f65:453`, `tools/chain-packet.test.sh@6b7a4d274a6f:295`, `tools/policy/check_policy.py@ddd97c3bb21b:1270-1290` / `loop/factories.py`, `tools/govkit/selftest.py@0862f3954625:5867`, `tools/govkit/matrix.py@8bb81dbe52f9:976` and `tools/govkit/upgrade_walk.py@aea8e1c7386b:230`.
> - Build the `unattended.test.sh` prologue once as a bundle, not once per shard.
> - Put every scratch path under one owned, swept root. Replace `rmtree(ignore_errors=True)` and `ignore_cleanup_errors=True` with a chmod-and-retry handler.
> - Biggest targets: `unattended/unattended.test.sh`, `check-unattended.test.sh`, `govkit/selftest.py`, `.githooks/pre-push.test.sh`, `run-gates*.test.sh`, `check-wiring.test.sh`.
>   - check-wiring measured 3,786 git processes in 350 s [PINNED].
>
> **Fix 3 — adopters stop re-running gov's kit selftests; govkit stops redoing work (K4 + K7 + K8).**
> - Add a content-addressed attestation: "kit tree <hash> passed its selftests". Adopter bars (incms `scripts/gov-bar.sh`, nicocares `scripts/nc-bar.sh`) check it and run the selftests only when the vendored kit tree hash is unattested.
> - `govkit update`: pass the existing `blob_at(..., batch=)` handle (`tools/govkit/upgrade_steps.py@89c3c58a02b2:2628`; callers at `tools/govkit/govkit.py@1ac058b76254:9993, 9244-9245, 9481, 9490`), and run each `adopt-*.sh --check` once (`tools/govkit/govkit.py@1ac058b76254:11169` and `:12507`).
> - `govkit apply`: the before/after maps (`read_gate_verdicts`, `tools/govkit/govkit.py@1ac058b76254:6239`, `:7763`, `:8465`) come from the target's reuse cache, and only legs whose guards intersect the written files are re-run.
>
> **Fix 4 — incms and nicocares tests (P1 + P2 + P4 + P5).**
> - nicocares `tests/v3_harness.py@fad7dc0a42a6:191-264`: seed `v3_seeded` once per session, then copy the template DB per test (`sqlite3` `backup()` or `copyfile`).
> - Set `STORAGE_LOCAL_PATH` to a per-session temp dir in nicocares `tests/conftest.py`, incms `scripts/check-vendor-suite.sh`, `scripts/run-core-venv.sh` and the e2e `run.sh`. The default is repo-relative: `services/api/app/core/config.py@4cc111fec6b1:1078`.
> - incms `scripts/gate.sh` gets the owned, swept `TMPDIR` / `--basetemp` block from `tools/run-gates/run-gates.sh@a1ea1e57d8fa:2333-2358`. It also stops leaking its `mktemp` table files (`:121, :126`).
> - incms `web-build` (`apps/web/build-check.sh@a0c8fab37655:34`) goes through the turbo cache, with no `standalone` output in the gate.
> - Fix 4 lands in the nicocares repo (`C:\projects\nicocares\main`, remote d41ly/nc) and in incms (`C:\projects\incms\main`), each under its own governance (`/unattended` there), followed by the incms submodule pin bump.
> - You may start your own side sessions in those folders for it.
>
> ## Integration — the hard requirement
>
> 1. **dWitnessedBar, the dClosedLoop chain's Test build, is running unattended RIGHT NOW.**
>    - Worktree `.claude/worktrees/unattended-dwitnessedbar-2ed3b3`, branch `branch/unattended-dwitnessedbar-2ed3b3`, about 302 commits [PINNED] ahead of main, base `9e21ac760`.
>    - Its lease is in that branch's `memory/builds/dWitnessedBar/RUN.md`.
>    - Never write into its worktree or branch.
>    - It already changes files fixes 1–2 need: `run-gates.sh`, `run-selftests.sh`, `selftest-budgets.txt`, `check-pass-order.sh`, `check-brief-recorded.sh`, `lib-unattended.sh`, `unattended.test.sh`, and a new `tools/run-gates/verdict_flow.py` (verdict routing, leg `select`, the flake ledger).
>    - Read its specs (`memory/builds/dWitnessedBar/spec/`) and its branch diff before writing yours.
>    - Extend its verdict/ledger machinery rather than adding a parallel store.
>    - Units touching those files must be built on its landed tip. Wait for it to land, or for its land branch, rather than racing it. Units with no overlap may go first.
> 2. **The chain's rules** are in `memory/builds/dClosedLoop/README.md` "Build-level rules" and `build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` `[chain]` (line ~1760).
>    - A live build sharing a subject finishes on its own track and is reconciled at the merge.
>    - Map each of your units to the chain build that owns the area, and record that mapping in your build README:
>      - dWitnessedBar (Test) for gate health and budgets;
>      - dSafePassage (Supersession, DEFERRED, specs in `memory/builds/dSafePassage/spec/`; see 5, 10, 25–27) for govkit update/apply;
>      - dScopedBuild where relevant.
>    - Do not contradict their specs. Name any overlap so they can absorb it.
> 3. **Adopters** are listed in `tools/govkit/adopters.toml`: nc, ic, swydee.
>    - Kit changes reach them only through minted kit versions and `govkit update`. Never hand-edit vendored kit copies in adopters.
>    - The attestation must fall back safely: unknown hash → run the selftests as today.
>    - Prove each kit change on adopter fixtures (`tools/govkit/fixtures/`) and with `govkit check` against incms and nicocares, run read-only from gov.
> 4. **Gov upgrades are in progress** in `C:\projects\incms\gov-upgrade` and `C:\projects\nicocares\gov-upgrade` (branch `feature/gov-upgrade`, another session).
>    - Do not touch or run anything heavy there.
>    - Before changing incms `scripts/gate.sh` or nicocares runner files, check whether that branch changes them, and sequence your fix-4 landings after it, or tell the owner.
>
> ## Done means
>
> - Each fix is specced, built, reviewed, green on its repo's bar, and landed by that repo's lander, OR deferred with a recorded reason.
> - Measured before/after numbers for at least `check-wiring.test.sh`, `check-pass-order.sh`, one `govkit/selftest.py` shard and the nicocares seed suite:
>   - git processes, via `GIT_TRACE2_EVENT=<dir>` and counting files;
>   - peak and residual temp entries, with `TEMP`/`TMP`/`TMPDIR` pointed at a scratch dir;
>   - wall time.
> - Add the R1–R8 rules and the G-A/G-B budgets only if they fit a unit cleanly; otherwise record them as backlog asks.
>
> ## Do NOT
>
> - Change host settings (8.3 names, last access, Dev Drive).
> - Delete incms `services/api/var/media` (202k files). Leave that to the owner and say so.
> - Run gates inside other sessions' worktrees.
>
> Report back: the landing commits per repo, the measured reductions, and anything deferred or waiting on dWitnessedBar or gov-upgrade.
>
> Shared notes folder for this group of sessions (outside the repo; read siblings' notes there, leave hand-over notes or large findings there instead of pasting them into messages): C:\Users\d41ly\AppData\Local\Claude-Data\claude_pzs8sxrjxfjjc\side-session-notes\local_80075476-7489-4b7f-a330-9218f30d7721

### brief:goal

Gov's history legs, kit suites, adopter bars and `govkit update`/`apply` stop spending git processes and file
creates on answers they already hold. Each verdict stays what it was today, and every claim is backed by numbers
measured before and after.

### brief:items

1. History verdicts cached under the commit and blob ids each one reads, in one store read through one `cat-file --batch` coprocess [planned TOOL-dQuietDisk-1]
2. `check-pass-order.sh` grades only units new since its last graded tip, including its `lib-unattended.sh` reads [planned TOOL-dQuietDisk-2]
3. `check-brief-recorded.sh` grades only units new since its last graded tip [planned TOOL-dQuietDisk-3]
4. `routed_commits.py` grades only commits past its last graded tip [planned TOOL-dQuietDisk-4]
5. One `git diff --name-only BASE` serves every guarded leg of a bar [planned TOOL-dQuietDisk-5]
6. The pickaxe in `manifest-check.sh` is scoped by path and range [planned TOOL-dQuietDisk-6]
7. One template cache keyed by kit tree hash under the runner's owned `$WORK`; a `--shared` clone or worktree per mutating case, one read-only checkout for reading cases [planned TOOL-dQuietDisk-7]
8. One shared sparse no-checkout snapshot for the six whole-tree copies the prompt names [planned TOOL-dQuietDisk-8]
9. The `unattended.test.sh` prologue built once as a bundle [parked the owner's standing rule of 2026-08-23 forbids running the unattended kit's suites, so the change cannot be observed by this run]
10. Every scratch path under one owned, swept root, removed by a chmod-and-retry handler in place of `ignore_errors` and `ignore_cleanup_errors` [planned TOOL-dQuietDisk-9]
11. `check-wiring.test.sh` on the template cache [planned TOOL-dQuietDisk-10]
12. `govkit/selftest.py` on the template cache [planned TOOL-dQuietDisk-11]
13. `.githooks/pre-push.test.sh` on the template cache [planned TOOL-dQuietDisk-12]
14. The `run-gates*.test.sh` suites on the template cache [planned TOOL-dQuietDisk-13]
15. `check-unattended.test.sh` on the template cache [parked the same owner rule as item 9 forbids running it]
16. A content-addressed attestation that a kit tree passed its self-tests, recorded by gov and carried to adopters with the minted kit [planned TOOL-dQuietDisk-14]
17. An adopter's kit self-test leg is held when its vendored kit tree hash is attested, and runs as today when the hash is unknown [planned TOOL-dQuietDisk-15]
18. `govkit update` passes one `blob_at(..., batch=)` handle to every receipt-row read [planned TOOL-dQuietDisk-16]
19. `govkit update` runs each `adopt-*.sh --check` once [planned TOOL-dQuietDisk-17]
20. `govkit apply` takes its before map from the target's reuse cache and re-runs only legs whose guards meet the files it wrote [planned TOOL-dQuietDisk-18]
21. Measured before and after: git processes, peak and residual temp entries, and wall time for `check-wiring.test.sh`, `check-pass-order.sh` and one `govkit/selftest.py` shard [planned TOOL-dQuietDisk-19]
22. Fix 4 in nicocares and incms, with the incms pin bump [parked it lands in those repositories under their own governance, through side sessions; the nicocares seed-suite numbers come from there]
23. The R1 to R8 design rules and the G-A and G-B budgets [parked R1 to R8 change governance carriers, which a run may not change (`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`, veto 2), and the G-A and G-B rows sit in files dWitnessedBar owns; both are filed as asks in this build's `BACKLOG.md`]

### brief:acceptance

- Over the real tree at BASE, each changed history leg's verdict and its printed findings are identical to the old leg's, on a cold store and on a warm one. A second run with no new unit launches a bounded number of git processes, stated in its spec and observed.
- A planted change to one graded unit's spec or record re-grades that unit, and only that unit, red where the old leg is red.
- Each suite moved onto the template cache passes exactly the arms it passed before, with the same RED and GREEN results, with fewer git processes and fewer temp entries measured.
- Residual temp entries after each changed suite is 0, including after a kill the next run sweeps.
- An attested kit tree hash holds its self-test leg on a fixture adopter. An unknown hash, a vendored edit or a missing attestation runs it, each seen.
- `govkit update` and `apply` produce identical receipts, writes and verdicts on `tools/govkit/fixtures/`, with fewer git processes. `govkit check` against incms and nicocares, run read-only from gov, reads unchanged.
- Before and after numbers recorded beside their instruments in TOOL-dQuietDisk-19's record.

### brief:gates

The merge bar, `bash tools/run-gates/run-gates.sh`, once at the close. Per unit, the direct check its spec names: the
equivalence corpus, the changed suite run directly (never an unattended-kit suite), or the probe. Never a bar inside a
pass.

### brief:non-goals

- Host settings: 8.3 names, last access, Dev Drive.
- Deleting incms `services/api/var/media`, which is the owner's.
- K9 to K11 (bar fixed cost, hooks, generators): the prompt does not ask for them.
- Hand edits to vendored kit copies in any adopter.

### input:spec

memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-28-spec-task.md

### task:reuse

run-gates.sh REUSE_CACHE and gate-selftest-last records; verdict_flow.py select (dWitnessedBar); aPiecewiseGrade-1's per-spec incremental cache; routed_commits.py:454 and lexicon.py:4241 cat-file batch; upgrade_steps.py:2628 blob_at batch=; lib-selftest.sh and fixture_target.py.

### card:route

- build: dQuietDisk
- unit: TOOL-dQuietDisk-14 · spec memory/builds/dQuietDisk/spec/2026-11-20-spec-TOOL-dQuietDisk-14.md
- brief: memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-14-build-brief.md
[/memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-28-1-spec-writer.md]
