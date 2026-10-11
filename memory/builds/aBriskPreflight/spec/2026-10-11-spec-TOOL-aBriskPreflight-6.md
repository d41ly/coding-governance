# TOOL-aBriskPreflight-6 — the pre-push hook sets up its straggler audit only when a pushed ref can carry a delta

**Status:** SPECCED · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 1 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md](../build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-7 |
| [2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-7 |
| [2026-10-11-prompt-TOOL-aBriskPreflight-6-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-6-build-brief.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-6-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-6-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The unattended claim write pushes a parentless commit over the empty tree to `refs/gov/runs/<slug>`
under `REMOTE_BOUND=60`, and that push runs `.githooks/pre-push`. On node `a` the hook took 53 s to
reach its `skip-nondefault` exit. About 35 s of that went on setting up a straggler audit that can
only answer "no delta" for such a commit, and on resolving a gate runner that nothing reads on such a
push. Four preflights in a row were refused at check 109 because of it. The hook does each piece of
setup only for a push that reads it, so a claim push fits its bound, and a branch push still gets
every refusal, notice and run-log line it gets today.

## 2. Scope (IN)

Line numbers are at BASE `b726385f`.

- **S1** — The straggler layer's candidate refs are listed once, by the three tests its loop applies
  today at `.githooks/pre-push:686-688`: a non-empty remote ref, not `refs/heads/<default>`, and a
  local sha that is not all zeros. The shortcut of S2 and the per-ref loop both read that one list,
  so the population is spelled once. Observed by AC3, AC4 and AC5.
- **S2** — Before `straggler-guard.sh` is sourced, one `git cat-file --batch-check` asks two things
  of every candidate: its `^{tree}` and its `^`. A candidate whose tree has size 0 and whose first
  parent reads `missing` is a root commit over the empty tree. When every candidate has that shape,
  or there is no candidate, the layer does no setup: it does not source the library and does not
  call `init_straggler_guard`, `resolve_python` or `resolve_kit_dir`. Any other answer runs the layer
  exactly as today, and so does a failed or short answer. The layer's comment block gains a
  paragraph stating the shortcut and the reason it loses nothing. Observed by AC1, AC5 and AC6.
- **S3** — The gate-runner resolution at `.githooks/pre-push:630-641` runs only when the push carries
  the default branch or the vetted `.githooks/gate-env.sh` declares `GOV_BRANCH_GATE_CMD`. Those are
  the only two paths on which `GATE_RUNNER` or `RUNNER_MISS` is read. Observed by AC1 and AC7.
- **S4** — `.githooks/straggler-guard.test.sh` gains two arms in its F3 fixture. A tag pushed at a tip
  holding an unaccounted transition merge is still refused. A push carrying a claim-shaped ref
  together with that branch is still refused. Observed by AC5.

## 3. Non-goals (OUT)

- `REMOTE_BOUND`, which the prompt forbids raising.
- The default-branch gates below the exits: the merge-loss check, the bar and the doc class.
- `straggler-guard.sh`'s own predicates. The shortcut derives `check_has_delta`'s answer for the one
  object shape where that answer is fixed, and calls nothing in the library.
- The vetting and sourcing of `.githooks/gate-env.sh`, and the kit-root ladder. Both still run for
  every push, for the reasons §4 gives.
- The claim write in `tools/unattended/unattended.sh`. The push it makes is unchanged.
- The push-main kit's version marker, which the build moves once after its last move of this hook.

### Edges

- **consumes-from** external — the claim commit `write_claim` builds: a parentless commit over the
  empty tree (`tools/unattended/unattended.sh:1842`, `:2189`). The speed-up rests on that shape and
  correctness does not, because any other shape runs the layer as today.
- **hands-off** external — the push-main kit's version marker, moved once in every carrier
  `tools/check-kit-versions.sh` names, after the build's last move of `.githooks/pre-push`. The
  kickoff manifest's `watch:` line in `memory/guides/SESSION-KICKOFF.md` names no file this unit
  touches, verified 2026-10-11, so no `last-audit` re-stamp is owed for it.

## 4. Design

### Where a claim push spends its time today

From the baseline's run `hook-base` (traced, 53 s, 45 forks, 31 execs): `init_straggler_guard` 7 s,
its `resolve_remote_sh` 8 s, `resolve_kit_dir` 9 s, `resolve_python` 3 s, `read_blob_at` 4 s and
`read_conf_value` 2 s. Two of those python starts are the runner resolution at
`.githooks/pre-push:632-633`. The other two are the layer's own, at `:677` and `:680`. All of it buys
one `check_has_delta` call on a commit that cannot have a delta.

### The prelude, settled against source

The brief places the kit-root ladder and the `gate-env.sh` check above the stdin read. In source,
both sit below the ref loop at `.githooks/pre-push:445-453` and above the layer at `:643`. What each
one does on a push with no branch:

- **The `gate-env.sh` vetting and source, `:487-493`, stays for every push.** That file may declare
  `GOV_BRANCH_GATE_CMD`, and the branch bar at `:942` runs on every push that carries no
  default-branch ref, a claim push included, as `TOOL-aGraftedHelix-10` S3 records. Skipping the file
  on such a push would skip an adopter's declared refusal.
- **The kit-root ladder, `:507-538`, stays.** It costs file tests and at most one `awk`, and the
  layer reads the `GOV_KITROOT` it sets whenever the layer runs.
- **The runner resolution, `:630-641`, moves behind a reader (S3).** `GATE_RUNNER` and `RUNNER_MISS`
  are read inside `check_bar_command` at `:847-848`, which the branch bar and the default bar call,
  and at `:975`, `:1137`, `:1354-1377` and `:1389-1428`, all below the `skip-nondefault` exit. With
  no default-branch ref and no declared branch bar, none of those lines runs.
- **The run log's START and END lines are untouched**, for every push.

### The empty-root shortcut (S2)

`check_has_delta` (`.githooks/straggler-guard.sh:289-304`) asks
`git rev-list "$base..$sha" -- <watched paths>`. A root commit over the empty tree changes no path,
so that list is empty and the predicate returns 1. The loop then `continue`s and prints nothing. The
shortcut reaches the same answer from the object alone, before any setup. It reads the tree's size,
which is 0 for the empty tree under SHA-1 and SHA-256 alike, rather than its object id.

The answer shape was probed on node `a` on 2026-10-11 in a scratch repository. An empty-root commit
answers `<oid> tree 0` and then `<sha>^ missing`. A root commit holding one file answers `tree 29`
and then `missing`, so it runs the layer.

Other object kinds take the same rule:

- An annotated tag peels to its commit under both `^{tree}` and `^`.
- A ref naming a tree has no `^`; if that tree is empty the shortcut applies, and today's
  `check_has_delta` on a tree fails its `rev-list` and also reads "no delta".
- A ref naming a blob has no `^{tree}`, so it is not the shape and the layer runs as today.

A mixed push, a branch beside a claim, runs the layer as today with the claim's ref in its loop.

The batch returns two lines per candidate, in input order. A line count other than twice the
candidate count, a non-zero exit, or any pair other than (`tree 0`, `missing`) means the layer runs.
The answer is read through builtins from a captured variable, which is the feed the shell-hygiene
leg admits.

### What a skipped setup changes on screen

The exits, the `skip-nondefault` decision and the run-log lines do not move. In a healthy clone the
layer prints nothing on a claim push today. In three degraded states `init_straggler_guard` prints a
diagnostic line: when its own remote ladder observes no default branch, when `GOV_DEFAULT_BRANCH`
disagrees with the observed default, and when the default ref resolves to no commit. After S2 that
line is not printed on a push whose every candidate is an empty root, or on a push with no candidate,
such as a push of the default branch alone. Each of those lines says the layer checked nothing, on a
push where the layer has nothing to check. No refusal, notice or decision moves, and a branch push
prints them exactly as today.

### Cost after, estimated and then measured by AC1

What remains on a claim push: the work-tree resolution, the run-log directories, the default-branch
observation (`symbolic-ref` and `rev-parse`), the `gate-env.sh` vetting (`rev-parse` and
`hash-object`) where that file exists, and the one `cat-file`. That is about a dozen programs, about
9 s at node `a`'s 0.75 s spawn under the pool leak. UNVERIFIED until AC1.

### Hazards this path carries

- `.githooks/pre-push.runlog.test.sh` keys every exit by its exact text (its table at `:970-975`),
  so no line carrying a `RUNLOG_DECISION=` assignment changes; the edits sit above the layer's loop
  and around the runner resolution only.
- The resolve-python parity gate compares the hook's inlined `resolve_python` and `resolve_kit_dir`
  blocks byte for byte with their canonical copies, so S3 wraps the call site at `:631` and touches
  neither marked block.
- `gotchas.py --for-paths .githooks/pre-push` selected `decision-re-derived-by-a-second-process`. The
  shortcut decides from the pushed object in this process, the same object the layer would audit.

### Inventory

No new function, conf key, flag or run-log field. Two hook-local variables: `_sg_cands`, the
candidate list S1 builds, and `_sg_need`, set when S2's batch finds a candidate of any other shape.
The lexicon's `sh.function` cell grades nothing new.

### Files touched (estimate)

`.githooks/pre-push` · `.githooks/straggler-guard.test.sh` · `.githooks/pre-push.test.sh` ·
`memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-6-claim-push.sh` ·
`memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-6-claim-push-ab.md`

`.githooks/pre-push.test.sh` is touched only if AC7's fixture has to place a runner where the ladder
finds it.

### Alternatives rejected

- **The layer selects only `refs/heads/`**, the brief's mechanism, and **`refs/heads/` plus
  `refs/tags/`**. Each stops auditing namespaces the layer audits today; §8 F1.
- **The claim push passes `--no-verify`.** It skips the run log's START and END lines and an
  adopter's branch bar on that push, and it edits the unattended kit to fix the push-main kit's cost.
- **The layer skips `refs/gov/` by name.** That writes the unattended kit's claim namespace into a
  file the push-main kit ships to adopters that may not run the unattended kit, and it stops auditing
  a branch-like history somebody pushes there; §8 F1.
- **Faster ladders inside `straggler-guard.sh`.** That edits the library's predicates, which are out
  of scope, and the layer would still start python to resolve its module.
- **A larger `REMOTE_BOUND`.** The prompt forbids it.

## 5. Production-readiness checklist

- security — The hook is the push boundary. For every ref that can carry a delta, every refusal path
  runs as today. The shortcut reads git objects only, never a working-tree file or an environment
  value, and the one shape it admits cannot carry a row change by construction. S3 still resolves the
  runner for both of its readers.
- perf / scale — One `cat-file` per push that has a candidate, whatever the ref count. A branch push
  pays that one program on top of today's cost; a claim push saves the setup. AC1 measures both
  figures.
- error / empty / loading states — A failed or short `cat-file` answer runs the layer as today. With
  no candidate there is no setup, where today the setup ran and the loop then found nothing.
- observability — The run-log lines and the decision are unchanged. §4 names the one stdout line that
  no longer prints, and on which pushes.
- risks — Mixed pushes, annotated tags and SHA-256 repositories, each covered in §4. Adopters without
  the library stay inert as today. Under an absolute `core.hooksPath` the hook and library come from
  one checkout, so the shortcut cannot pair a new hook with an old library.
- testing — Sliced arms of `.githooks/straggler-guard.test.sh` and `.githooks/pre-push.test.sh`, the
  two new arms of S4, and the claim-push instrument of AC1.
- migration — N/A — the hook keeps no state and changes no format; it ships verbatim and takes effect
  at an adopter's next copy.
- user docs — N/A — this repository has no `help/` tree, and the layer's comment block, which S2
  amends, is the documentation of the layer.

## 6. Acceptance criteria

- **AC1** — When `2026-10-11-build-TOOL-aBriskPreflight-6-claim-push.sh` builds a throwaway clone under
  `%TEMP%/bp6`, it sets `core.hooksPath` to the clone's own hooks, records `origin/HEAD`, and builds a
  claim commit the way `write_claim` does (`git mktree` over empty input, then `git commit-tree`). It
  then feeds `.githooks/pre-push origin <url>` one line naming `refs/gov/runs/x` under
  `2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh`, with BASE's hook and with the built one,
  A/B interleaved twice, with a host-state line beside each run. For the built hook, forks plus execs
  multiplied by the per-spawn cost from its host-state line (`spawn5` divided by 5) is at most 30 s,
  half of `REMOTE_BOUND`. An untraced run of the same push finishes within 30 s. BASE's figures are
  printed beside them.
  Red when: either figure for the built hook is over 30 s.
  figure: DERIVED from each run's host-state line. At writing BASE took 45 forks and 31 execs at
  about 0.75 s each.
  fixture: a throwaway clone, never the shared git dir, whose push journal the hook would write.
- **AC2** — When AC1's runs finish, the last line of each clone's `pushes.log` carries `ev=end`,
  `decision=skip-nondefault` and `exit=clean` for both hooks, and the hook exits 0.
  Red when: the decision differs between the two hooks, or the END line is missing.
- **AC3** — When the F3 block of the straggler-guard suite runs as a sliced arm against the built
  hook, every one of its assertions passes. A feature branch holding an unaccounted transition merge
  is refused, and the refusal names the merge sha and `--repair`. The branch lands once its rows are
  accounted. With the audit module absent the push prints the `did NOT run` line naming the ref, and
  with its reader broken it prints the `DEAD PROBE` line. With S2's predicate made to report every
  candidate as an empty root, as a staged break, the first push lands and the arm fails. Restored, it
  passes.
  Red when: the staged break leaves the arm passing, so it never reached the layer.
- **AC4** — When the pre-flip feature-push block of the straggler-guard suite runs as a sliced arm
  against the built hook, the push prints `migrate_backlog.py --relocate --as <your-slug>` and lands.
  Under AC3's staged break the recipe is missing and the arm fails. Restored, it passes.
  Red when: the staged break leaves the arm passing.
- **AC5** — When S4's two new arms run as sliced arms against the built hook, a lightweight tag
  pushed as `refs/tags/t-strag` at the F3 tip is refused naming the merge, and a push carrying both
  `refs/gov/runs/x`, an empty-root commit, and `feat` is refused naming the merge. With the candidate
  list limited to `refs/heads/` as a staged break, the tag arm fails. With the shortcut taken when
  ANY candidate is an empty root, rather than every one, as a staged break, the mixed arm fails.
  Restored, both pass.
  Red when: either staged break leaves its arm passing.
  fixture: both arms run against BASE's hook first and are refused there too, which is what makes
  them arms that preserve today's audit rather than new requirements.
- **AC6** — When `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py`
  reads AC1's traced runs, the built hook's `execs by program` table has no `python`, `python3` or
  `py` row and its `wall by function` table has no `init_straggler_guard` row. BASE's run has both.
  Red when: either appears for the built hook, so some setup still runs on a claim push.
- **AC7** — When the branch-bar block of the pre-push suite runs as a sliced arm, the untracked
  branch bar's refusal prints a `Sanctioned use: GOV_BRANCH_GATE_CMD=` line that is byte-identical
  between BASE's hook and the built one. With S3's condition reduced to the default-branch test, as a
  staged break, the line changes. Restored, it matches.
  Red when: the staged break leaves the line unchanged, so the arm never reached the runner.
  fixture: the line names a runner only when the fixture resolves a kit root. Whether BASE's line
  names one there is read first. If it prints the placeholder, the slice places the runner where the
  ladder finds it, and the pre-push suite takes that fixture change.
- **AC8** — When the hook-wired claim block of the unattended suite, the arm `TOOL-aGraftedHelix-10`
  S4 added, runs as a sliced arm with the built hook copied in, its create, CAS update, unset-HEAD
  refusal and stale-refusal-file assertions pass.
  Red when: any of them fails, so the claim write no longer goes through the hook as that unit built
  it.

## 7. Gates

`straggler-guard arms` · `pre-push self-test` · `pre-push run-log line` · `push-main self-test` · `kit version markers` · `python resolver (behaviour + inline parity + idiom ban)` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: .githooks/straggler-guard.test.sh · covers AC5 · a tag at, and a claim ref pushed beside, a tip holding an unaccounted transition merge · none

## 8. Open questions

- **F1 — Which pushed refs the straggler layer audits, and how a claim push avoids its setup.**
  (a) Only refs under `refs/heads/`, the brief's mechanism. (b) Refs under `refs/heads/` and
  `refs/tags/`. (c) Every ref but those under `refs/gov/`. (d) Every ref the layer audits today, with
  setup skipped when every candidate is a root commit over the empty tree. Recommendation: (d).
  RESOLVED (agent, 2026-10-11, delegated): (d), by M3's rule. (a) fails AC5 and the build rule that
  no check is weakened. A tag can be merged with `git merge <tag>`, and a review namespace such as
  `refs/for/<branch>` carries commits that are merged later, so both lose an audit they have today.
  (b) keeps tags and still stops auditing every other namespace. (c) writes the unattended kit's
  namespace into a file the push-main kit ships to adopters that may not run that kit, and it stops
  auditing a branch-like history pushed there. (d) satisfies every criterion and stops auditing
  nothing. It skips setup only where `check_has_delta` could answer nothing but "no delta". No tie
  arose.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "skip pre-push hook setup for a pushed ref that cannot carry a
backlog delta"` returned name-stem neighbours, among them `delta` in
`tools/memory-tree/transition_audit.py`, `check_claim_push_lock_stale` and `write_claim_push_lock`
in `tools/unattended/unattended.sh`, and `run_push` in `.githooks/pre-push.runlog.test.sh`. None
decides whether a pushed object can carry a delta, so no existing seam fits as the predicate. The
seam this unit extends is the layer itself at `.githooks/pre-push:643-716`, and the answer it
derives is `check_has_delta`'s in `.githooks/straggler-guard.sh`. The recall probe returned
`TOOL-aGraftedHelix-10`, which routes the claim push through this hook by remote name and states its
branch-bar path, which is the reason §4 keeps `gate-env.sh` for every push. It also returned
`TOOL-aStandingWrit-4`, the fail-open an environment-chosen default branch caused, which is why S2
reads git objects and no environment value.

Recall terms used: `python tools/memory-recall/query.py "why does the pre-push straggler layer run
on every non-default pushed ref and what is the claim push bound" --terms "pre-push straggler layer
check_has_delta init_straggler_guard claim push refs/gov/runs REMOTE_BOUND check 109
skip-nondefault feature branch"`
