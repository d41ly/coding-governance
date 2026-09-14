# TOOL-dDerivedDocket-13 — straggler hook bodies and the fleet inventory

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g2-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g2-round1.md) | spec-audit | TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-14 |

<!-- /gen:spec-records -->

## 1. Goal

The transition audit catches a lost row after a pre-flip branch merges; nothing tells that branch
beforehand. Instruct a straggler at each moment its own node can see it, by a commit, a rebase, a
push or a session start, and report every pushed straggler from every node's drift run until its
changes are accounted on the default branch, so relocation happens before a merge rather than as a
repair after one.

## 2. Scope (IN)

- **S1** A sourced library, `straggler-guard.sh`, beside the tracked hook files and located through
  the calling hook's own directory, never through the committing tree. It reads git objects only.
  It decides three predicates: FLIPPED, the default branch's committed `.memory-tree.conf` sets
  `BACKLOG_MODE=builds`; PRE-FLIP, every merge base of the default branch and the subject commit is
  in shards mode; HAS-DELTA, the subject's lineage against the default holds a commit whose own tree
  is in shards mode and touches the backlog shards or a family-named backlog archive. It also
  carries the recipe text. When FLIPPED is false it stops after one git read and prints nothing.
  Observed by AC1, AC2 and AC7.
- **S2** `.githooks/pre-commit` refuses a commit on a FLIPPED, PRE-FLIP branch that stages a backlog
  shard or a backlog archive, unless `MERGE_HEAD` names a builds-mode commit, and prints the recipe.
  Any other commit on a PRE-FLIP branch gets a one-line notice and is never refused. Observed by AC1
  and AC2.
- **S3** A new tracked hook, `.githooks/pre-rebase`, refuses a rebase whose upstream is in builds
  mode when the rebased branch is PRE-FLIP and HAS-DELTA against that upstream, and prints the
  recipe, whose first step says merge and never rebase. `git rebase --no-verify` bypasses it.
  Observed by AC3.
- **S4** `.githooks/pre-push` gains a feature-branch block, placed BEFORE its "nothing to gate" exit.
  For each pushed ref that is not the default branch and not a delete: a PRE-FLIP, HAS-DELTA tip
  gets the recipe as a notice and is never blocked; a tip that has integrated the flip and is still
  HAS-DELTA gets unit 9's audit at that tip, and an unaccounted transition refuses the push naming
  the merge and the repair verb (design A8). The block does nothing when the library is absent.
  Observed by AC4 and AC5.
- **S5** `tools/check-wiring.sh --session` gains a step that, on a FLIPPED tree where the memory-tree
  kit's `migrate_backlog.py` resolves, runs `--stragglers --local --tsv` under a bound and prints at
  most one `note` line naming the local stragglers. The step never gates and `--session` still exits
  0. Observed by AC6.
- **S6** A report-only drift signal, `backlog_stragglers`, over local and remote-tracking refs: value
  is the straggler count, `of` is refs examined, live only when refs examined is above zero, and
  not asked when the memory-tree kit or its inventory mode is absent. Observed by AC8.
- **S7** Declarations in the same commit: a `govkit` exempt row each for the library and
  `.githooks/pre-rebase`, with the design §18.5 reason; `pre-rebase` added to `GOV_WIRING_HOOKS`;
  both `git-hooks` keys and the new leg claimed in `memory/map/features/memory-tree-hygiene.md`
  with the map regenerated. Observed by AC9.
- **S8** A repo-subject suite, `straggler-guard.test.sh`, on a new leg in chunk `declarations`, so it
  is not held like a kit self-test. One fixture repo whose default branch is in builds mode, one arm
  per hook behaviour above, and a parity arm comparing the library's recipe with the bytes
  `migrate_backlog.py --recipe` prints. It prints `PASS (<n> assertions)`. Observed by AC10.
- **S9** Arms for S5 in `tools/check-wiring.test.sh` and for S6 in `tools/drift-audit/selftest.py`,
  each observed RED with its fix unstaged. Observed by AC6 and AC8.

## 3. Non-goals (OUT)

- The audit itself, in full and staged modes, and the `commit-msg` carrier are unit 9's. This unit
  calls the audit at a named tip and adds no second transition rule.
- The inventory's content judgement and the recipe's canonical text are unit 12's `--stragglers` and
  `--recipe`. This unit prints and counts; it never decides what is accounted.
- Adopters' hooks. The library and `pre-rebase` are gov-only, and each adopter wires them in its own
  deployer build (design §18.5). `.githooks/pre-push` ships verbatim through the push-main kit, so
  its new block is inert wherever the library is absent.
- A default-branch push gets no second refusal here. The bar that push runs carries hygiene check
  25 in the unguarded `memory hygiene` leg, which is the same audit (§8 F3).
- `tools/push-main.sh` refusing a straggler (design §18.3 G4) and a `pre-merge-commit` hook (§18.3
  G3) are superseded by design §18r.2 and amendment A7, and are not built.
- Remote CI is unit 32's. The real-tree staged RED of the pre-commit refusal against a scratch
  pre-flip branch is unit 35's.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-9` — the full-mode audit at a named tip, which the pre-push
  block runs over an integrated feature tip before a squash can erase its transition.
- **consumes-from** `TOOL-dDerivedDocket-12` — `--stragglers`, which the session step and the drift
  signal read, and `--recipe`, which the parity arm compares.
- **hands-off** `TOOL-dDerivedDocket-35` — the real-tree staged RED of the pre-commit refusal
  against a scratch pre-flip branch, once the default branch is in builds mode.
- **hands-off** `DEPL-dDerivedDocket-1` — the gov-only library and `pre-rebase` hook, which the
  adopter runbook names as the reference an adopter copies in its own deployer build.

## 4. Design

### Why a library beside the hooks, and what it may read

`core.hooksPath` is repo-global and absolute, so every worktree on a node runs the PRIMARY tree's
hook files (design §18.1; the `.githooks/pre-push` header records the measured case). A pre-flip
branch's own tree carries the old kit and no straggler rule. So the rule cannot live in any kit the
hook resolves through `$top`, the way `.githooks/pre-commit:48` resolves the hygiene engine, and it
cannot be sourced from `$top` the way `.githooks/pre-push:59-61` sources `gate-env.sh`. It is sourced
from the directory the hook itself was run from, which is the primary tree's `.githooks/`.

The library reads the default branch's conf blob, commit conf blobs through one `cat-file --batch`,
merge bases, one `rev-list` over the lineage, and the staged name list. It never runs a python kit
module except where S4 and S5 name one. The default branch is resolved as `.githooks/pre-push:91-110`
does, observed `origin/HEAD` first with `GOV_DEFAULT_BRANCH` only a cross-check, because
`TOOL-aStandingWrit-5` records an environment value that disabled the primary-tree branch guard.
The conf is read from the remote-tracking default where it exists, since that is where the flip is
observed, and from the local branch otherwise. `MEMORY_ROOT` and `FAMILIES` come from the same blob.

### The predicates, and why PRE-FLIP is not the tip's conf

The bypass hunt's blocker was a straggler that pulled the new conf early and blinded a tip read
(design A1), so no predicate here reads the subject's own conf. PRE-FLIP asks whether the branch has
INTEGRATED the flip, through its merge bases: once a builds-mode default commit is merged in, the
merge base is that commit and the branch is no longer pre-flip, even though its lineage still holds
the old shard commits. HAS-DELTA asks whether there is anything to relocate, by lineage. The backlog
archive population is the family-named one, narrower than unit 9's whole archive directory on
purpose: a decision-log rotation on a pre-flip branch has nothing to relocate and must not print a
recipe (§8 F4).

| Hook | FLIPPED | PRE-FLIP | HAS-DELTA | Staged backlog path | Result |
|---|---|---|---|---|---|
| pre-commit | yes | yes | any | yes, no builds-mode `MERGE_HEAD` | refuse, recipe |
| pre-commit | yes | yes | yes | no | notice naming the recipe |
| pre-commit | yes | yes | no | no | notice: merge the default before filing asks |
| pre-rebase | upstream builds | yes | yes | — | refuse, recipe |
| pre-push, feature ref | yes | yes | yes | — | recipe as a notice, push proceeds |
| pre-push, feature ref | yes | no | yes | — | unit 9's audit at the pushed tip; refuse if unaccounted |
| any | no | — | — | — | nothing printed |

The relocation merge itself, concluded by `git commit` with restored views staged, carries a
builds-mode `MERGE_HEAD`, so pre-commit lets it through and `commit-msg` (unit 9) decides it.

### Resolving the audit from a hook

The pre-push block resolves `transition_audit.py` under the pushing tree's kit root, derived as
`.githooks/pre-push:71-76` derives `GOV_KITROOT`, and falls back to the same path under the hook
directory's own tree. Neither resolving prints one skip line naming the ref, never silence. The
audit runs over the pushed sha, not `HEAD`, since a push may name any ref.

### The session step, and where it may sit in a shipped file

`tools/check-wiring.sh` ships verbatim and its root-install spellings at lines 386, 449, 612 and
621 are held by the install-prefix gate's frozen, position-keyed waiver registry. A line added above
them shifts them and unpins every waiver, and a new root-install literal takes no new waiver. So the
step is a function defined and called below line 621, and it reaches the memory-tree kit through a
directory derived from `KIT_REL` with the file name joined at run time. Its line uses the `note`
severity, which the script reserves for a true condition that is not dormant wiring (its header).

### The drift signal

`backlog_stragglers` follows the report-only shape of `build_live_backlog_rows`
(`tools/drift-audit/drift_report.py:1332-1372`), with `gateable: False`, so `--check` never reds on
it. It reaches the memory-tree kit the way `_resolve_ident` reaches the recall kit
(`tools/drift-audit/drift_report.py:476-495`), by a directory beside its own, and returns the
not-asked shape when that kit or its mode is missing. Before the flip it reports design §9 step 1's
inventory; after it, the stragglers left, until zero.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `straggler-guard.sh` and its functions | sourced hook library | lexicon shell function cell, checked by `lexicon.py --suggest` before writing |
| `.githooks/pre-rebase` | tracked hook | as above |
| `backlog_stragglers` | drift signal | snake case, as every signal there |
| `straggler-guard.test.sh` and its leg | repo-subject suite | testsuite-counts contract |

### Files touched (estimate)

`.githooks/straggler-guard.sh` (new) · `.githooks/pre-rebase` (new) ·
`.githooks/straggler-guard.test.sh` (new) · `.githooks/pre-commit` · `.githooks/pre-push` ·
`tools/check-wiring.sh` · `tools/check-wiring.test.sh` · `tools/drift-audit/drift_report.py` ·
`tools/drift-audit/selftest.py` · `tools/gate-legs.json` · `tools/govkit/registry.toml` ·
`memory/map/features/memory-tree-hygiene.md` · `memory/map/generated/` · the check-wiring and
drift-audit version constants where `kit version markers` requires a move.

### Alternatives rejected

- **The rule inside the hygiene engine or the generator.** A pre-flip branch runs its own old copy of
  both (design §18.1), so the rule would never reach it.
- **Sourcing from `$top`, the `gate-env.sh` precedent.** The committing tree of a straggler predates
  the library.
- **Inline copies in three hooks.** Three answers to one predicate, and the first fix lands in two.
- **Reading the branch tip's conf** (design §18.2 P2). Refuted by the bypass hunt's blocker (A1).

## 5. Production-readiness checklist

- security — every hook reads git objects and the staged list, and executes only the one kit module
  S4 names and the one S5 names. A refusal is bypassed by `--no-verify`, which is the deliberate
  bypass every other refusal here uses; the audit then binds at the bar.
- perf / scale — one git read on every commit, rebase and push until the flip; after it, about five
  processes where the branch is pre-flip, and the audit's cache for the push case.
- error / empty / loading states — an unresolvable default branch or conf blob prints a named line
  and allows, because these layers instruct and the audit and the bar are what guarantee.
- observability — every refusal and notice names the predicate that fired and prints the recipe; the
  drift signal lists each straggler ref with its unaccounted count.
- risks — a node that has not pulled main runs old hook files; design §18r.5 states that the audit,
  not these layers, is the guarantee. A deliberate rebase with `--no-verify` still drops rows
  (design §18r.6 hole 1).
- testing — S8's suite unheld, S9's arms in held suites; each arm observed RED with its fix unstaged.
- migration — none; every layer is dormant until the default branch declares builds mode.
- user docs — the recipe these layers print; the memory-tree README section is unit 36's.

## 6. Acceptance criteria

- **AC1** — When `straggler-guard.test.sh` stages a shard edit on a fixture pre-flip
  branch whose default branch declares builds mode, `git commit` exits 1 and prints the recipe, and
  `git commit --no-verify` succeeds.
  Red when: PRE-FLIP reads the branch tip's conf, so a straggler that copied the new conf commits its
  shard edit.
- **AC2** — When the same fixture branch commits a non-backlog file, the commit succeeds with one
  notice line; when the fixture concludes a relocation merge by `git commit` with restored views
  staged, `.githooks/pre-commit` does not refuse.
  Red when: the relocation merge is refused, so the recipe's own last step cannot complete.
- **AC3** — When the fixture runs `git rebase` onto the builds-mode default, and `git pull --rebase`,
  on a HAS-DELTA branch, `.githooks/pre-rebase` refuses both with the recipe; a branch with no
  backlog commit rebases, and `git rebase --no-verify` bypasses.
  Red when: the hook reads only its second argument, so `git pull --rebase`, which passes none,
  rebases the straggler.
- **AC4** — When the fixture pushes a PRE-FLIP, HAS-DELTA feature branch to a local bare remote,
  `.githooks/pre-push` prints the recipe and the push lands.
  Red when: the feature push is refused, which strands the straggler's only off-node copy.
- **AC5** — When the fixture pushes a feature branch holding an unaccounted transition merge, the
  push exits 1 naming the merge sha and `--repair`; with its `RELOCATED` rows committed it lands;
  with the audit module removed from both trees it lands and prints a skip line naming the ref.
  Red when: the block sits after the "nothing to gate" exit, so it never runs for a feature push.
- **AC6** — When `bash tools/check-wiring.test.sh` runs `--session` on a builds-mode fixture holding
  one local straggler, it prints one `note` line naming it and exits 0; on a shards-mode fixture it
  prints no straggler line; under `--check` the line is still `note` and the exit ignores it.
  Red when: a straggler is reported as UNWIRED, so the wiring check exits 1 and anything reading it as
  a refusal stops.
- **AC7** — When the fixture's default branch is in shards mode, every hook prints nothing from the
  library, and the existing `bash .githooks/pre-commit.test.sh` and `bash .githooks/pre-push.test.sh`
  pass unchanged.
  Red when: the dormant path prints a line on every commit in a repo that has not flipped.
- **AC8** — When `python tools/drift-audit/selftest.py` builds a fixture with one local and one
  remote-tracking straggler, `backlog_stragglers` reads 2 of the refs examined and is not gateable;
  with no ref it reports not live, and without the memory-tree kit it reports not asked.
  Red when: the signal walks only `refs/heads`, so a pushed straggler from another node reads as none.
- **AC9** — When `python tools/govkit/govkit.py selfcheck` and
  `python3 tools/codebase-map/test_codebase_map.py` run, both pass with the library and `pre-rebase`
  tracked, and `bash tools/check-install-prefix.sh` passes with no new waiver.
  Red when: a new tracked hook passes without an exempt row, or a line added above check-wiring's
  waived lines unpins them.
- **AC10** — When `bash tools/check-testsuite-counts.sh` runs, the new suite prints its
  `PASS (<n> assertions)` line at or above its floor, including an arm that fails when the library's
  recipe differs by one byte from `migrate_backlog.py --recipe`.
  Red when: the library's recipe drifts from the canonical text and no arm reds.
  cost: fixture repos only; observed at the one post-build bar.
  permission: unit passes run no gate legs (fix F7). This criterion, and the suite and leg runs AC6
  to AC9 name, are observed at the one post-build bar; in the pass, each arm's RED is observed by
  hand against a scratch fixture repo.

## 7. Gates

`memory hygiene` · `branch-guard self-test` · `pre-push self-test` · `check-wiring self-test` · `drift-audit selftest` · `drift-audit records` · `govkit selfcheck` · `install-prefix (shipped surface)` · `kit version markers` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: `straggler-guard.test.sh` on a new repo-subject leg · a builds-mode default with a pre-flip branch staging a shard edit, a rebase, two feature pushes, a relocation merge, a recipe byte flipped · the new suite's own floor
New arm: `tools/check-wiring.test.sh` · a builds-mode fixture with one local straggler · the suite's floor
New arm: `tools/drift-audit/selftest.py` · a fixture with local and remote-tracking stragglers, and one with none · none

## 8. Open questions

- **F1 — where the detection lives.** Options: (a) a library beside the hooks, sourced through the
  hook's own directory; (b) inline in each hook; (c) inside a kit the hook resolves in `$top`. (c)
  never reaches a pre-flip branch (design §18.1); (b) is three copies of one predicate. RESOLVED
  (agent, 2026-09-14, delegated): (a).
- **F2 — which session tree runs the inventory.** Design §18r.2 L5 says a primary-tree step. This
  repo's sessions routinely open in worktrees, and the ref set is repository-wide, so a primary-only
  step would reach almost none of them. RESOLVED (agent, 2026-09-14, delegated): every session tree,
  kept cheap by unit 12's one narrowing walk and `--local`.
- **F3 — a straggler refusal on default-branch pushes** (design §18.3 G2). The bar that push runs
  holds check 25 in an unguarded leg, and §18r.2 superseded the G layers with L1 to L7. RESOLVED
  (agent, 2026-09-14, delegated): none added; a second copy of the audit in a verbatim-shipped hook
  is a second answer to one question.
- **F4 — the archive population.** Options: unit 9's whole archive directory, or the family-named
  backlog archives. RESOLVED (agent, 2026-09-14, delegated): family-named, because these layers
  print relocation instructions and a decision-log rotation has nothing to relocate.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from design §18.1 to §18.5, §18r.2 L5 and L6, and amendment A8.
  Adds two edges the brief's table does not carry: hands-off unit 35, whose roster note names this
  unit's real-tree staged RED, and hands-off `DEPL-dDerivedDocket-1`, whose spec consumes the library
  as the adopter's reference. Diverges from design §18r.2 L5 on which session tree runs the
  inventory (§8 F2) and drops design §18.3 G2 to G4 as superseded (§8 F3).

## 10. Reuse audit

The seams are the hooks' own: the observed-default resolution and `GOV_KITROOT` derivation in
`.githooks/pre-push`, the `gate_at` probe in `.githooks/pre-commit`, `first_of` and the `note`
severity in `tools/check-wiring.sh`, and `_resolve_ident` plus the report-only signal shape in
`tools/drift-audit/drift_report.py`. `python tools/codebase-map/reuse_lookup.py "hook body refuses a
commit on a branch and prints a remedy"` returned name-stem neighbours only (`CensusRefused`,
`branches` in `tools/memory-tree/check-arms.py`) and reports `.sh` as an unscanned layer, so it is
blind to every hook; `reuse_lookup.py "drift signal inventory of refs with liveness examined count"`
returned `inventory_ids` and `DriftError` and no ref-walking signal. No existing seam walks refs for
backlog changes. Recall surfaced `TOOL-aWeldedTribunal-7`, which gave check H its `GOV_WIRING_HOOKS`
walk that `pre-rebase` joins, and `TOOL-aStandingWrit-5`, which decides the default-branch rule.

Where the design and BASE disagree: design §18.1's line citations hold at `abac6d59`
(`.githooks/pre-commit:10` and `:48`, `.githooks/pre-push:40`). The design does not know that
`tools/check-wiring.sh` carries four position-keyed waivers that forbid adding lines above them.

Recall terms used: `pre-commit pre-push pre-rebase hook branch-guard check-wiring SessionStart
hooksPath straggler notice`
