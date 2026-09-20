# TOOL-dDerivedDocket-13 — straggler hook bodies and the fleet inventory

**Status:** SPECCED · rev-5 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round1.md) | spec-audit | TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-14 |
| [2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round2.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round2.md) | spec-audit | TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 |

<!-- /gen:spec-records -->

## 1. Goal

The transition audit catches a lost row after a pre-flip branch merges; nothing tells that branch
beforehand. Instruct a straggler at each moment its own node can see it, by a commit, a rebase, a
push or a session start wherever its node's hooks resolve to post-flip hook files, and name every
local straggler from any post-flip session tree otherwise, and report every pushed straggler from
every node's drift run until its changes are accounted on the default branch, so relocation happens
before a merge rather than as a repair after one.

## 2. Scope (IN)

- **S1** A sourced library, `straggler-guard.sh`, beside the tracked hook files and located through
  the calling hook's own directory, never through the committing tree. It reads git objects only.
  It decides three predicates: FLIPPED, the default branch's committed `.memory-tree.conf` sets
  `BACKLOG_MODE=builds`; PRE-FLIP, every merge base of the default branch and the subject commit is
  in shards mode; HAS-DELTA, the subject's lineage against the default holds a commit whose own tree
  is in shards mode and touches the backlog shards or a family-named backlog archive. It also
  carries the recipe text. When FLIPPED is false it stops after one git read and prints nothing.
  Observed by AC1, AC2, AC3, AC7 and AC11.
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
  HAS-DELTA gets `transition_audit.py --at <sha> --expect-builds` (unit 9 S14), the library passing
  `--expect-builds` because its own PRE-FLIP read found a builds-mode merge base; exit 1 refuses the
  push naming the merge and the repair verb (design A8), and exit 2, a DEAD PROBE, prints that line
  naming the ref and allows the push, since these layers instruct and the bar guarantees. The block
  does nothing when the library is absent. Observed by AC4 and AC5.
- **S5** `tools/check-wiring.sh --session` gains a step that, on a FLIPPED tree where the memory-tree
  kit's `migrate_backlog.py` resolves, runs `--stragglers --local --tsv` under a bound and prints at
  most one `note` line naming the local stragglers. The step never gates and `--session` still exits
  0. For a straggler checked out in a linked worktree whose effective `core.hooksPath` resolves
  inside that worktree, the same line marks it `hooks own-tree`, because that worktree's commits run
  its own pre-flip hooks and only this note, the drift signal and the audit reach it. Observed by
  AC6 and AC12.
- **S6** A report-only drift signal, `backlog_stragglers`, over local and remote-tracking refs: value
  is the straggler count, `of` is refs examined, live only when refs examined is above zero, and
  not asked when the memory-tree kit or its inventory mode is absent. Observed by AC8.
- **S7** Declarations in the same commit: a `govkit` `[[exempt]]` row each for
  `.githooks/straggler-guard.sh`, `.githooks/pre-rebase` and `.githooks/straggler-guard.test.sh` (an
  exemption does not cover siblings; precedent `.githooks/pre-commit.test.sh` in
  `tools/govkit/registry.toml`), each with the design §18.5 reason; an `[[exempt_leg]]` row for the
  new leg with the same reason, as `branch-guard self-test` has; `pre-rebase` added to
  `GOV_WIRING_HOOKS`; both `git-hooks` keys and the new leg claimed in
  `memory/map/features/memory-tree-hygiene.md` with the map regenerated, and
  `tools/govkit/subject-pins.tsv` regenerated for the new leg; and the frozen install-prefix waiver
  row `.githooks/pre-commit:48`, the `gate_at` dual-spelling probe that S2's new lines shift,
  converted to an in-line `# gov:root-fixture — <reason>` marker on the probe's line, its row leaving
  `tools/install-prefix-waivers.txt` in the same commit, as unit 8 S14 does for its two (§8 F7).
  Observed by AC9.
- **S8** A repo-subject suite, `straggler-guard.test.sh`, on a new leg in chunk `declarations`, so it
  is not held like a kit self-test. One fixture repo whose default branch is in builds mode, one arm
  per hook behaviour above, and a parity arm comparing the library's recipe with the bytes
  `migrate_backlog.py --recipe` prints. It prints `PASS (<n> assertions)`. The leg sits in chunk
  `declarations` with subject `repo`, guarded on `.githooks/`, `tools/check-wiring.sh`, `tools/lib/`,
  `tools/memory-recall/` and `tools/memory-tree/`, every path its arms run, and declares a `ceiling`
  in `tools/gate-legs.json`: 300 s, the branch-guard sibling's, until the post-build bar's first
  reading re-declares it as `tools/run-gates/ceiling-margin.txt` sizes it over that reading, recorded
  through `derive-ceilings.py --write` (§8 F6). The suite also has a `--topology <repo> <branch>`
  mode, the linked-worktree topology helper: it adds a linked worktree of `<branch>` beside the
  primary tree of `<repo>`, prints the worktree's path, sets no `core.hooksPath` and runs no arm.
  AC12's arm builds its linked worktree through the same function, and unit 35's scratch clone runs
  the mode (§8 F8). Observed by AC10 and AC14.
- **S9** Arms for S5 in `tools/check-wiring.test.sh` and for S6 in `tools/drift-audit/selftest.py`,
  each observed RED with its fix unstaged. Observed by AC6 and AC8.
- **S10** The `core.hooksPath` premise is corrected in the five carriers §4 names, with no change in
  line count in `tools/check-wiring.sh`. Each comment carrier and the gotcha body carries the sentence
  §4 pins, its phrase "unless a worktree's config.worktree sets its own" on one physical line; the
  note at `tools/check-wiring.sh:287` says the value in effect names another checkout, which supplies
  the hook; the gotcha's description drops the premise, and `memory/gotchas/INDEX.md` is regenerated
  with `python tools/memory-tree/gotchas.py --write`. Observed by AC13.
- **S11** The build's one-owner rule gives each kit's one version move to the unit first in build
  order to change that kit's shipped bytes, and S6 and S9 are the build's first `tools/drift-audit/`
  changes, so this unit moves the drift-audit version (§8 F9). In one commit it raises
  `KIT_DRIFT_AUDIT_VERSION` in `tools/drift-audit/drift_report.py` as an X.Y pair, strictly above
  both the value each carrier `tools/check-kit-versions.sh` names holds at `fb07ca25` and the value
  it holds on the advertised tip read after a fetch in the pass, and sets every
  `gov:kit drift-audit@` marker to the same value: in `tools/drift-audit/README.md`,
  `tools/drift-audit/drift_report.py`, `tools/drift-audit/drift_signals.py`,
  `tools/drift-audit/drift_signals.template.py`, `tools/drift-audit/selftest.py` and
  `tools/drift-audit/adopt-drift-audit.sh`, and in `tools/workflows/drift-audit-code.js` and
  `tools/workflows/drift-audit-state.js` with each harness's `version:` field. The drift-audit bytes
  every later unit of this build changes ride this move. Observed by AC15.

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

- **consumes-from** `TOOL-dDerivedDocket-9` — `transition_audit.py --at <sha> --expect-builds`
  (S14), which the pre-push block runs over an integrated feature tip before a squash can erase its
  transition, and the both-ways real-tree hook-list arm in `transition-audit.test.sh` (its S16), which
  reds until `pre-rebase` joins `GOV_WIRING_HOOKS`.
- **consumes-from** `TOOL-dDerivedDocket-12` — `--stragglers`, which the session step and the drift
  signal read, and `--recipe`, which the parity arm compares.
- **hands-off** `TOOL-dDerivedDocket-35` — the real-tree staged RED of the pre-commit refusal
  against a scratch pre-flip branch, once the default branch is in builds mode; the linked-worktree
  topology helper, `straggler-guard.test.sh` in its `--topology` mode (S8), through which AC12 builds
  its worktree and which that unit's scratch clone runs, so the two cannot drift; that unit now runs
  the helper at the one post-build run at `VERIFYING` rather than inside its pass, because its head
  word ends `.test.sh` and `--topology` is not one of gate-guard's read-only verbs, which is the
  same reading AC10 already takes of this unit's own `--topology` run; and the hooks-path
  value settled here (§8 F5): under the relative `.githooks` that `tools/check-wiring.sh` writes, a
  straggler in a linked worktree runs its own hooks and is not refused — the documented inert case,
  with the `hooks own-tree` note — and under an absolute `config.worktree` override naming the
  primary tree's `.githooks` it is refused; AC12 builds both.
- **hands-off** `DEPL-dDerivedDocket-1` — the gov-only library and `pre-rebase` hook, which the
  adopter runbook names as the reference an adopter copies in its own deployer build.

## 4. Design

### Why a library beside the hooks, and what it may read

The shared `core.hooksPath` applies unless a worktree's `config.worktree` sets its own, and WHICH hook
files run depends on the VALUE in effect. An absolute value — this repo's shared config does not hold
one, but a `config.worktree` override does, on seven of nine live worktrees on node `d` (PINNED,
measured 2026-09-14) — makes each worktree it governs run the files of the one checkout it names, the
primary tree's. The relative `.githooks` that `tools/check-wiring.sh:312`
writes resolves against the worktree running the hook, so a linked worktree runs its OWN hook files,
and a pre-flip branch's are pre-flip copies with no library. Design §18.1's "absolute" was measured
from a worktree carrying an override (§9, §10). The library therefore reaches a straggler only under
an absolute value; under the relative one it is inert there, and the audit and the bar are what
guarantee (§5). It is still sourced from the directory the hook was run from, which is right for
both values. A pre-flip branch's own tree carries the old kit and no straggler rule, so the rule
cannot live in any kit the hook resolves through `$top`, the way `.githooks/pre-commit:48` resolves
the hygiene engine, and it cannot be sourced from `$top` the way `.githooks/pre-push:198-200` sources
`gate-env.sh`.

Five carriers state the old premise, and S10 corrects them: the `.githooks/pre-push` header (lines
6-9), the comment at `tools/check-wiring.sh:241-243` and the note check H prints at `:287`, the
comment at `tools/check-wiring.test.sh:918`, and `memory/gotchas/hookspath-resolves-into-another-checkout.md`.
The comment carriers and the gotcha body carry one sentence: "The shared `core.hooksPath` applies
unless a worktree's config.worktree sets its own, and the value in effect decides which hook files
run: an ABSOLUTE value runs the hooks of the checkout it names, the relative `.githooks` check-wiring
writes runs each worktree's own." The gotcha's description drops the premise, which regenerates its
index row, and its body names the configuration each measurement was taken under. `AGENTS.md`'s
merge-bar sentence states the same premise and is parked for the owner in this build's `RUN.md`; it
is not a carrier here.

The library reads the default branch's conf blob, commit conf blobs through one `cat-file --batch`,
merge bases, one `rev-list` over the lineage, and the staged name list. It never runs a python kit
module except where S4 and S5 name one. The default branch is resolved as `.githooks/pre-push:91-110`
does, observed `origin/HEAD` first with `GOV_DEFAULT_BRANCH` only a cross-check, because
`TOOL-aStandingWrit-5` records an environment value that disabled the primary-tree branch guard.
The conf is read from the remote-tracking default where it exists, since that is where the flip is
observed, and from the local branch otherwise. `MEMORY_ROOT` and `FAMILIES` come from the same blob.
Both reads, and the allow on a default the library cannot resolve, are observed by AC11.

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
| pre-push, feature ref | yes | no | yes | — | unit 9's `--at <sha> --expect-builds` at the pushed tip; refuse if unaccounted, allow with a line on a DEAD PROBE |
| any | no | — | — | — | nothing printed |

The relocation merge itself, concluded by `git commit` with restored views staged, carries a
builds-mode `MERGE_HEAD`, so pre-commit lets it through and `commit-msg` (unit 9) decides it.

### Resolving the audit from a hook

The pre-push block resolves `transition_audit.py` under the pushing tree's kit root, derived as
`.githooks/pre-push:71-76` derives `GOV_KITROOT`, and falls back to the same path under the hook
directory's own tree. Neither resolving prints one skip line naming the ref, never silence. The
audit runs as `--at <pushed sha> --expect-builds`, never over `HEAD`, since a push may name any ref.

### The session step, and where it may sit in a shipped file

`tools/check-wiring.sh` ships verbatim and its root-install spellings at lines 442, 492, 708 and
717 are held by the install-prefix gate's frozen, position-keyed waiver registry. A line added above
them shifts them and unpins every waiver, and a new root-install literal takes no new waiver. So the
step is a function defined and called below line 717, and it reaches the memory-tree kit through a
directory derived from `KIT_REL` with the file name joined at run time. Its line uses the `note`
severity, which the script reserves for a true condition that is not dormant wiring (its header).

`.githooks/pre-commit` carries one row in the same frozen registry, `.githooks/pre-commit:48`, its
`gate_at` probe, and S2's refusal sits above it, outside the shipped `govkit:branch-guard` block. The
row is therefore converted to an in-line `gov:root-fixture` marker on the probe line in this commit
(S7, §8 F7), which no line added above it can unpin.

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
`.githooks/straggler-guard.test.sh` (new) · `.githooks/pre-commit` (S2, and the `gov:root-fixture`
marker, S7) · `.githooks/pre-push` (S4, and its header, S10) · `tools/check-wiring.sh` (S5, and the
comment at 241-243 and the note at 287, S10) · `tools/check-wiring.test.sh` (S9, and the comment at
918, S10) · `tools/install-prefix-waivers.txt` (one row leaves, S7) ·
`tools/drift-audit/drift_report.py` · `tools/drift-audit/selftest.py` · the other drift-audit
version carriers (S11): `tools/drift-audit/README.md`, `tools/drift-audit/drift_signals.py`,
`tools/drift-audit/drift_signals.template.py`, `tools/drift-audit/adopt-drift-audit.sh`,
`tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js` ·
`tools/gate-legs.json` · `tools/govkit/registry.toml` · `tools/govkit/subject-pins.tsv`
(regenerated, S7) · `memory/map/features/memory-tree-hygiene.md` · `memory/map/generated/` ·
`memory/gotchas/hookspath-resolves-into-another-checkout.md` and the generated
`memory/gotchas/INDEX.md` (S10). Under the build's one-owner rule this unit moves one kit version,
`KIT_DRIFT_AUDIT_VERSION` with its markers (S11), being the first unit in build order to change
`tools/drift-audit/` bytes; its check-wiring bytes ride unit 9's move of `KIT_CHECK_WIRING_VERSION`
(unit 9 S17). `tools/check-wiring.sh` lines 241-243 and 287 are reworded in place with no change in
line count; every new line sits below line 717.

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
- risks — A worktree whose `core.hooksPath` resolves inside itself — the relative value check-wiring
  writes, with no absolute override — runs its own pre-flip hook files, so S2 to S4 never fire
  there; S5 marks such a straggler `hooks own-tree` from any post-flip session tree, S6 lists it from
  any node's drift run, and unit 9's check 25 and unit 32's CI audit are the guarantee (design
  §18r.5). A node that has not pulled main runs old hook files, too. A deliberate rebase with
  `--no-verify` still drops rows (design §18r.6 hole 1).
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
  on a HAS-DELTA branch, the `pre-rebase` hook refuses both with the recipe; a branch with no
  backlog commit rebases, and `git rebase --no-verify` bypasses; a PRE-FLIP branch whose only change
  under `memory/archive/` is a decision-log archive rebases with no refusal, and its commits print
  the merge-first notice and never the recipe.
  Red when: the hook reads only its second argument, so `git pull --rebase`, which passes none,
  rebases the straggler; or HAS-DELTA reads unit 9's whole archive directory, so a decision-log
  rotation draws the recipe and `pre-rebase` refuses the branch.
- **AC4** — When the fixture pushes a PRE-FLIP, HAS-DELTA feature branch to a local bare remote,
  `.githooks/pre-push` prints the recipe and the push lands.
  Red when: the feature push is refused, which strands the straggler's only off-node copy.
- **AC5** — When the fixture pushes a feature branch holding an unaccounted transition merge, the
  push exits 1 naming the merge sha and `--repair`; with its `RELOCATED` rows committed it lands;
  with the audit module removed from both trees it lands and prints a skip line naming the ref; with
  the module's conf reader staged broken, the push lands and prints the DEAD PROBE line naming the
  ref.
  Red when: the block sits after the "nothing to gate" exit, so it never runs for a feature push; or
  a DEAD PROBE refuses a feature push, stranding its only off-node copy.
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
  `python3 tools/codebase-map/test_codebase_map.py` run, both pass with the library, `pre-rebase`,
  `straggler-guard.test.sh` and the new leg tracked and declared; `bash tools/check-install-prefix.sh`
  passes with no new waiver, `grep -c 'githooks/pre-commit' tools/install-prefix-waivers.txt` prints
  0, and the `gate_at` probe line in `.githooks/pre-commit` carries `gov:root-fixture` with a reason;
  and the both-ways real-tree hook-list arm in `transition-audit.test.sh` (unit 9 S16) passes with
  `pre-rebase` tracked.
  Red when: a new tracked `.githooks/` path or the new leg passes without its own `[[exempt]]` or
  `[[exempt_leg]]` row, or `pre-rebase` is tracked and absent from `GOV_WIRING_HOOKS`, or a line added
  above check-wiring's waived lines unpins them; or S2's refusal lines shift the pre-commit probe
  while its position-keyed row stays, which `install-prefix` reds as a stale waiver and an unwaived
  hit at the post-build bar.
- **AC10** — When `bash tools/check-testsuite-counts.sh` runs, the new suite prints its
  `PASS (<n> assertions)` line at or above its floor, including an arm that fails when the library's
  recipe differs by one byte from `migrate_backlog.py --recipe`.
  Red when: the library's recipe drifts from the canonical text and no arm reds.
  cost: fixture repos only; observed at the one post-build bar.
  permission: unit passes run no gate, suite or bar (fix F7, and the child prompt in
  `tools/workflows/unattended-unit.js` since aProbedUnit, which `tools/unattended/gate-guard.js`
  enforces before `VERIFYING`). This criterion, the suite runs AC1 to AC5, AC11 and AC12 name, and
  the suite and leg runs AC6 to AC9 name, are observed at the one run the main loop makes at
  `VERIFYING`, which is `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`:
  `check-wiring self-test`, `drift-audit selftest`, `branch-guard self-test` and
  `pre-push self-test`, which AC6 to AC8 read, are all HELD, every one carrying `chunk` `selftests`
  in `tools/gate-legs.json`, and a plain bar and `GATE_FULL=1` alone both skip them. AC14's `--topology` run, which no bar leg makes, is one of
  the suite runs attributed beside that bar, made by hand once every unit is terminal; in the pass,
  each arm's RED is observed by hand against a scratch fixture repo, and AC14's `grep -n` runs there.
- **AC11** — When `straggler-guard.test.sh` gives the fixture a remote whose default branch declares
  builds mode while the local default branch is still in shards mode, a pre-flip branch staging a
  shard edit is refused with the recipe; and when the fixture has no remote-tracking default and no
  local default branch the library can resolve, `git commit` succeeds and prints the library's named
  unresolved-default line.
  Red when: the library reads only the local default, so a node whose local main was never
  fast-forwarded stays dormant; or an unresolvable default refuses or prints nothing.
- **AC12** — When `straggler-guard.test.sh` builds a fixture whose primary tree is on the
  builds-mode default and whose pre-flip branch is checked out in a linked worktree carrying pre-flip
  hook files, and that worktree stages a shard edit: under an ABSOLUTE `core.hooksPath` naming the
  primary tree's `.githooks`, `git commit` exits 1 printing the recipe; under the relative
  `.githooks` that `tools/check-wiring.sh --fix` writes, with no `config.worktree` override, the
  commit is not refused — the documented inert case — and `bash tools/check-wiring.sh --session` run
  in the primary tree prints one `note` line naming the straggler with `hooks own-tree`.
  Red when: the fixture sets `core.hooksPath` by hand in a single-tree clone, so the suite reads
  green over a topology this repo's wiring never produces; or the relative case is refused, which
  would mean the arm ran the primary's hooks and measured nothing.
- **AC13** — When `git grep -n -i 'repo-global' -- .githooks/pre-push tools/check-wiring.sh tools/check-wiring.test.sh memory/gotchas/`
  runs, it prints nothing; and `git grep -c "unless a worktree's config.worktree sets its own" -- .githooks/pre-push tools/check-wiring.sh tools/check-wiring.test.sh memory/gotchas/hookspath-resolves-into-another-checkout.md`
  prints exactly one hit for each of the four files.
  Red when: a carrier keeps BASE's repo-global premise, so the next reader of the hook header, check
  H, its test or the gotcha believes one shared value governs every worktree, including the seven on
  node `d` that override it; or the correction lands in fewer carriers than §4 names, which no other
  criterion reads.
- **AC14** — When `straggler-guard.test.sh --topology <fixture> <branch>` runs over a fixture whose
  primary tree is on its default branch, it exits 0 printing one path that
  `git -C <fixture> worktree list` lists on `<branch>`, prints no `PASS` line, and leaves
  `git -C <fixture> config --get core.hooksPath` as it found it; and `grep -n` of the helper's
  function name in the suite shows its definition, the mode's dispatch and the AC12 arm's call.
  Red when: AC12 inlines its own topology, so unit 35's clone and this suite build two topologies
  that can drift, which the edge to unit 35 exists to prevent; or the mode sets a hooks path, so unit
  35's clone no longer measures the value `tools/check-wiring.sh` writes.
- **AC15** — When the `KIT_DRIFT_AUDIT_VERSION = ` line of `tools/drift-audit/drift_report.py` is
  read at the unit's build commit, its value is higher as an X.Y pair than the value
  `git show fb07ca25:<carrier>` prints and than the value `git show origin/main:<carrier>` prints
  after a `git fetch` in the pass, for each carrier `tools/check-kit-versions.sh` names: that
  constant, the `tools/drift-audit/README.md` marker, and the `version:` field and marker of
  `tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js`.
  `git grep -c "gov:kit drift-audit@<value>"` over each file S11 names counts at least one hit in
  each, and `git grep -h -o "gov:kit drift-audit@[0-9][0-9.]*" -- tools/drift-audit tools/workflows`
  prints no other value. `bash tools/check-kit-versions.sh` exits 0.
  Red when: this unit's drift-audit bytes ship at a version a carrier already holds at `fb07ca25` or
  on the advertised tip, which `tools/check-kit-versions.sh` cannot see, because it compares the
  constant with the README marker and the two harnesses and never with another commit, so an adopter
  pulling the new signal cannot tell the two vintages apart; or a marker that script does not read,
  such as the one in `tools/drift-audit/drift_signals.template.py`, keeps the old value.
  permission: the fetch, the reads and both greps are `git` observations in the pass;
  `check-kit-versions.sh` is the `kit version markers` leg and runs at the one post-build bar.

## 7. Gates

`memory hygiene` · `branch-guard self-test` · `pre-push self-test` · `check-wiring self-test` · `drift-audit selftest` · `drift-audit records` · `govkit selfcheck` · `install-prefix (shipped surface)` · `kit version markers` · `leg ceilings clear their evidenced maximum` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: `straggler-guard.test.sh` on a new repo-subject leg · a builds-mode default with a pre-flip branch staging a shard edit, a rebase, two feature pushes, a relocation merge, a recipe byte flipped, a remote-only builds default and an unresolvable one, a decision-log rotation, a broken conf reader on push, a linked worktree under an absolute and a relative hooks path, the `--topology` mode · the new suite's own floor
New arm: `tools/check-wiring.test.sh` · a builds-mode fixture with one local straggler · none
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
- **F5 — reach under a relative `core.hooksPath`.** Options: (a) check-wiring writes and upgrades an
  absolute value; (c) writes one only when unset and reports a relative one; (b) record the layer
  inert there; (d) (b) plus S5 marking such a straggler `hooks own-tree`. (a) reverses the
  never-overwrite rule `AGENTS.md` states and rewrites user config; (c) changes the value shipped to
  every adopter and reinstates TOOL-aWeldedTribunal-7's primary-tree push hook; both are owner turns
  (vetoes 2 and 3) and stay parked. RESOLVED (agent, 2026-09-14, delegated): (d); the audit (unit 9)
  and CI (unit 32) carry D11's fleet-wide guarantee unchanged.
- **F6 — held or unheld.** Options: (i) chunk `selftests` beside the two hook suites, held; (ii)
  `declarations`, unheld, guarded on the directories its inputs live in. The recipe-parity arm grades
  two tracked texts that drift with nobody editing a hook, which is the repository-state class the
  merge bar keeps. RESOLVED (agent, 2026-09-14, delegated): (ii).
- **F7 — how does S2's refusal avoid unpinning the frozen `.githooks/pre-commit:48` waiver?** Options:
  (a) every new pre-commit line sits below line 48; (b) the row becomes an in-line
  `gov:root-fixture — <reason>` marker on the probe line and leaves the registry, as unit 8 S14 does.
  (a) keeps a position hazard for every later edit of the hook and puts a refusal after the legs it
  should precede. RESOLVED (agent, 2026-09-16, delegated): (b).
- **F8 — what entry point does the linked-worktree topology helper have?** Options: (a) a
  `--topology <repo> <branch>` mode of `straggler-guard.test.sh`; (b) a function in a new sourced
  fixture file. (b) adds a tracked `.githooks/` path owing its own `[[exempt]]` row and has unit 35
  source a test file. RESOLVED (agent, 2026-09-16, delegated): (a); the mode sets no hooks path, so
  each caller sets the value it measures.
- **F9 — which unit moves the drift-audit kit version?** Units 13, 17, 21, 23, 26, 34 and 36 all
  change `tools/drift-audit/` or its two workflow harnesses, and this unit is the first in build
  order. Options: (a) this unit, the first to change those bytes, the reading unit 9 F9 applies to
  check-wiring; (b) unit 21, which rev-2 of its S8 named as the earliest to scope the move; (c) each
  unit. (c) breaks the build's one-owner rule, and (b) moves the version after two units'
  drift-audit bytes have already changed, so the tree between orders 13 and 21 ships new drift-audit
  bytes under BASE's version. RESOLVED (agent, 2026-09-16, delegated), decided by the orchestrator: (a), S11,
  observed by AC15 against `fb07ca25` and the advertised tip at the pass (rev-5 moved it off
  `abac6d59`); unit 21 §8 F3 records the same decision from its end.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from design §18.1 to §18.5, §18r.2 L5 and L6, and amendment A8.
  Adds two edges the brief's table does not carry: hands-off unit 35, whose roster note names this
  unit's real-tree staged RED, and hands-off `DEPL-dDerivedDocket-1`, whose spec consumes the library
  as the adopter's reference. Diverges from design §18r.2 L5 on which session tree runs the
  inventory (§8 F2) and drops design §18.3 G2 to G4 as superseded (§8 F3).
- rev-2 · 2026-09-14 · §1 · S1 · S4 · S5 · S7 · S8 · §3 · §4 · §5 · AC3 · AC5 · AC9 · AC11 · AC12 · §8 ·
  §10 · folds spec-audit round 1. G2 H2 (54): diverges from design §18.1, whose `core.hooksPath`
  premise holds only under an absolute value; §4 restates it, S5 marks `hooks own-tree` stragglers,
  §5 records the layer inert under the relative value check-wiring writes with D11's guarantee left
  to units 9 and 32, AC12 and §8 F5, and the premise is corrected in the `.githooks/pre-push`
  header, `tools/check-wiring.sh:188-190`, `tools/check-wiring.test.sh:811` and the hooksPath gotcha.
  G2 H1's unit-13 end: S4 calls unit 9's `--at <sha> --expect-builds`. G2 M13 (60, 75): the suite's
  `[[exempt]]` and the leg's `[[exempt_leg]]` rows, the leg unheld and guarded, §8 F6. G2 M28 (36):
  AC11. G2 L6 (37): AC3 stages a decision-log rotation. G2 L7 (38): AC9 reads the both-ways
  hook-list arm. G5 H6: hands-off 35 names the linked-worktree helper and the settled hooks-path
  value.
- rev-3 · 2026-09-16 · spec-audit round 2 fold. G2 M6's unit-13 end (34, 49): consumes-from 9 and AC9
  read the real-tree hook-list arm in `transition-audit.test.sh`, unit 9 S16. G2 M9 (24): S7 converts
  the `.githooks/pre-commit:48` install-prefix waiver to an in-line `gov:root-fixture` marker; §4 the
  session step; AC9; §8 F7. G2 M10 (8, 27): new S10 corrects five carriers, the `:234` note among
  them, with a sentence naming the per-worktree override; §4; new AC13. G2 M13's unit-13 end (56):
  Files touched says the check-wiring bytes ride unit 9 S17 and the drift-audit bytes unit 21 S8. G2
  L3 (14): S8's `--topology` mode; hands-off 35; new AC14; §7 arm line; §8 F8. G2 L4 (15, 45): S8's
  guard gains `tools/check-wiring.sh` and `tools/memory-recall/`. G2 L5 (53): S8's ceiling is sized by
  `tools/run-gates/ceiling-margin.txt`. The record's class item 1 applied: S7 and Files touched name
  the regenerated `tools/govkit/subject-pins.tsv`. Consequential, not a finding id: §4's opening
  sentence drops its own "repo-global" premise so it agrees with the sentence S10 pins.
  Fold verification: AC3 names the `pre-rebase` hook by basename, the file this unit creates; §7
  gains `leg ceilings clear their evidenced maximum`, the leg that grades S8's ceiling, as unit 9's
  §7 does for its S11.
- rev-4 · 2026-09-16 · S11 · §4 · §8 F9 · AC15 · spec-audit round 2 fold, second pass, from fold
  verifier problem f3 on kit-version ownership, decided by the orchestrator as reading (a): the unit
  first in build order to change a kit's bytes owns that kit's one move. New S11 moves
  `KIT_DRIFT_AUDIT_VERSION` and every `gov:kit drift-audit@` marker once, here. §4's Files touched
  names the version carriers and drops rev-3's claim that the drift-audit bytes ride unit 21 S8.
  New AC15 reads the constant against `abac6d59`, both marker greps and
  `bash tools/check-kit-versions.sh`. New §8 F9 records the decision.
- rev-5 · 2026-09-16 · regrounded on fb07ca25 (origin/main). Line citations that moved: aReplayedCard
  grew `tools/check-wiring.sh`, so its hooksPath comment is at 241-243, check H's note at 287, the
  `.githooks` write at 312, and its four waived spellings at 442, 492, 708 and 717, with §4, S10 and
  Files touched following. The `tools/check-wiring.test.sh` comment is at 918. §4's gate-env citation
  was wrong at `abac6d59` too, and now names `.githooks/pre-push:198-200`. S11, AC15 and §8 F9 read
  the drift-audit move against `fb07ca25` and the advertised tip, per the orchestrator's kit-version
  decision. That version is still 1.10 at the new base. AC10's permission line covers every suite
  run, because aProbedUnit's child prompt and aDeferredBar's `gate-guard.js` refuse a suite in a
  pass, and names AC14's `--topology` run as a by-hand observation after every unit is terminal,
  since the bar runs the suite and never the mode. `.githooks/pre-commit:10` and `:48`, its waiver
  row, `tools/drift-audit/` and every §7 leg are unchanged; §10 records the base.
  Regrounding consolidation, 2026-09-20: the build-wide rule folded here defers only what the
  gate-guard hook DENIES — a `.test.sh` or `selftest.py` FILE invocation carrying none of its
  read-only verbs — plus a gate-leg command, which the owner rule forbids a pass to run by hand; a
  `--selftest` FLAG on another file stays the direct check build method M6 and the unit child
  prompt name, so deferring it would contradict unit 11 §8 F9. The ruling conflict behind that
  scope is parked for the owner in the build's `RUN.md`; this pass folds the conservative reading
  and decides nothing. No permission line moves: AC10's covers every denied run this unit names,
  AC15's covers the `kit version markers` leg, and no criterion of this unit observes a
  `--selftest` flag that a line wrongly defers. §7's `tools/check-wiring.test.sh` `New arm:` third
  field is corrected from `the suite's floor` to `none`: that suite pins no executed-assertion
  floor at `fb07ca25`, so the old field named a number nothing owns. Also checked and unchanged:
  AC9's `grep -c 'githooks/pre-commit'` counts one and AC13's `repo-global` sweep counts six at
  `fb07ca25`, so neither is green before the unit; and this unit adds text to no capped carrier.
  Closing consolidation, 2026-09-20: the orchestrator RATIFIED the NARROW reading for the build — a
  gate leg's own command run over a FIXTURE or a staged break STAYS in the unit pass, that being the
  direct check `memory/guides/BUILD-METHOD.md` M6 requires; the same command run over the real or
  rendered tree defers to the one run the main loop makes at `VERIFYING`; and a `.test.sh` or
  `selftest.py` FILE invocation carrying no read-only verb defers wherever it runs, because the
  gate-guard hook denies it, while a `--selftest` FLAG on another file is not that shape and stays in
  the pass — and added a single COST exception, which lands in unit 8 alone, where that leg's declared
  `ceiling` sits above the per-command bound a pass holds.
  No criterion of this unit moves. The owed cross-edit is applied: the hands-off to unit 35 now
  records that the unit runs the topology helper at `VERIFYING` rather than in its pass, so the two
  specs agree; §8 F8 stays resolved as it is, and the alternative of giving that helper an entry
  point whose head word does not end `.test.sh` is explicitly not taken. One measured fact for the
  pass rather than a spec change, re-measured at this pass: `origin/main` is already past
  `fb07ca25`, holds `KIT_DRIFT_AUDIT_VERSION` above the base value, and has MOVED AGAIN since the
  last measurement, so no tip value is typed here or in any criterion of this unit. S11 and AC15 are
  right only because they READ the advertised tip after a fetch and take a value strictly above both
  it and the base; a pass that reads the `fb07ca25` value alone ships a duplicate move that
  `tools/check-kit-versions.sh` cannot see, because it never compares against another commit. The
  orchestrator also SET the `VERIFYING` run: `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`,
  plus the suite runs it attributes beside the bar. AC10's line now says so in those terms, because
  the four self-test legs AC6 to AC8 read are HELD and a plain bar would skip every one of them
  while reading green; this unit's other deferrals are to unheld legs any bar runs, and those lines
  are left as they stand. The
  header date is the last-change date; the rev is unchanged, this being the same consolidation.

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

Where the design and BASE disagree: design §18.1's line citations hold at BASE
(`.githooks/pre-commit:10` and `:48`, `.githooks/pre-push:40`). The design does not know that
`tools/check-wiring.sh` carries four position-keyed waivers that forbid adding lines above them.
Design §18.1's `core.hooksPath` premise holds only under an absolute value; the shared config holds
the relative `.githooks` check-wiring writes, and two of nine live worktrees on node `d` carry no
override (G2 H2's re-measurement, 2026-09-14).

BASE is `fb07ca25`. Against `abac6d59` it leaves `.githooks/pre-push`, `tools/drift-audit/`, both
drift-audit harnesses, `tools/govkit/registry.toml`, `tools/check-kit-versions.sh`,
`tools/run-gates/ceiling-margin.txt` and `tools/run-gates/derive-ceilings.py` byte-identical, and
`KIT_DRIFT_AUDIT_VERSION` still reads 1.10. Three landed changes touch this unit's seams.
- aReplayedCard added `check_card`, the `--resolve-fragment` verb and one shared fragment reader to
  `tools/check-wiring.sh`. That moved every line S10 and §4 cite, re-keyed the four install-prefix
  waiver rows, and moved `KIT_CHECK_WIRING_VERSION` from 1.2 to 1.3. Unit 9 S17 still owns the next
  move. The premise sentence is unchanged there and in the suite.
- dUnstagedSymbol appended a codebase-map leg to the end of `.githooks/pre-commit`. That leaves the
  `gate_at` probe at line 48 and its waiver row in place, so S7's conversion stands.
- aProbedUnit's child prompt in `tools/workflows/unattended-unit.js` forbids a suite inside a pass,
  and `tools/unattended/gate-guard.js` denies any word ending `.test.sh` at command position before
  VERIFYING unless the command carries a read-only verb. So this unit's pass runs none of its suite
  arms (AC10). That includes the `--topology` mode S8 gives unit 35.

Recall terms used: `pre-commit pre-push pre-rebase hook branch-guard check-wiring SessionStart
hooksPath straggler notice`
