# TOOL-dDerivedDocket-9 — transition-merge audit over history and at commit time

**Status:** SPECCED · rev-2 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round1.md) | spec-audit | TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 |
| [2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round2.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round2.md) | spec-audit | TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 |

<!-- /gen:spec-records -->

## 1. Goal

A merge that joins a lineage still editing authored backlog shards to a lineage already in builds
mode can lose a row change with no hook watching, on any node and months after the flip. Audit every
such merge from the history HEAD carries, and again at the moment a merge is concluded, so a lost
change reds the bar everywhere and is repaired forward instead of trusted.

## 2. Scope (IN)

- **S1** A new memory-tree kit module, `transition_audit.py`, stdlib plus git, beside the engine in
  the kit directory it derives from its own location. Every git read goes through a pinned
  dereference: `git --no-replace-objects` with `GIT_GRAFT_FILE=/dev/null`, the same property the
  unattended kit's history leg holds (`tools/unattended/check-pass-order.sh:40-48`). Observed by
  AC13.
- **S2** Mode per commit. A commit is in builds mode when its own tree's `.memory-tree.conf` sets
  `BACKLOG_MODE=builds`, and in shards mode otherwise, an absent key included. The value is read
  from the committed blob, never from a working copy. Observed by AC1 and AC5.
- **S3** The transition predicate, by LINEAGE and never by tip (design A1). A merge M is a
  transition when some parent P has, in `merge-base --all(P, others)..P`, a commit whose own tree is
  in shards mode and that touches `<MEMORY_ROOT>/backlog/` or `<MEMORY_ROOT>/archive/`, AND some
  other parent Q has, in its own lineage against P, a commit whose own tree is in builds mode.
  Observed by AC1, AC2 and AC3.
- **S4** The delta of a transition, keyed by row id through the kit's one anchor grammar. For every
  id whose row version at P differs from its version at EVERY merge base and was never held by a
  shards-mode commit on the other parents' side (design A6), the delta names the id, the change
  kind (new, changed, removed) and the newest lineage commit that made it. Shard and archive rows
  of one family are one population, so a row rotated away with its status flipped is a change and
  a row removed from both is a REMOVED change (design A5). Observed by AC3, AC4 and AC14.
- **S5** Accounting (design A4). A delta entry is accounted when HEAD's tree carries EXACTLY ONE
  provenance row `- RELOCATED · <id> · by <sha> · kept|dropped|amended: why` in some
  `<MEMORY_ROOT>/builds/*/BACKLOG.md`, whose sha is a 7+ hex prefix of the change commit. Zero is
  unaccounted; two or more is a duplicate verdict naming both files. Observed by AC1 and AC2.
- **S6** Full mode is hygiene check 25, run by `check-memory-hygiene.sh` when not `--staged` and
  delegated to the module exactly as check 24 is delegated to `row_grammar.py`. It prints one
  liveness line on every run and, per unaccounted entry, the merge sha, the id, the change commit
  and the remedy line naming the merge sha and the `--repair` verb. It runs S14's code path at HEAD;
  there is no second walk. Observed by AC1 and AC5.
- **S7** Liveness, three refusals and one announcement. On a HEAD the SHELL's own conf read calls
  builds mode: a walk that finds no builds-mode commit at all is a DEAD PROBE (the two conf readers
  disagree); a history holding a shards-mode commit but yielding no mode boundary is a DEAD PROBE; a
  shallow repository is a DEAD PROBE (design A9). On a shards-mode HEAD the check prints that it is
  dormant and why. Every line check 25 prints — the liveness line, the dormant announcement and each
  refusal — begins `memory-hygiene: check 25 `, so a consumer greps one prefix. Observed by AC5 and
  AC6.
- **S8** A pinned registry, `transition-audit.txt` under `<MEMORY_ROOT>/project/`, admitted by
  name in check 3's registry list. A row names a transition merge sha and the word `accounted`. The
  check reds when a listed sha is absent from HEAD's history, no longer classifies as a transition,
  or no longer reads accounted. Transitions not yet listed are counted `unpinned`, never red, and
  `transition_audit.py --pin` prints their rows for a later commit to append. Observed by AC7.
- **S9** The staged form (design L2, carrier A7): a new tracked `.githooks/commit-msg` runs
  `transition_audit.py --staged` when `MERGE_HEAD` exists and the module resolves in the committing
  tree. It audits the pending merge, parents HEAD and every `MERGE_HEAD` line, tree the index, and
  refuses the commit on an unaccounted entry. With no `MERGE_HEAD` the hook exits 0 and prints
  nothing. Observed by AC8.
- **S10** A per-merge cache under the git common dir, keyed by merge sha and a module constant
  `CACHE_EPOCH`, holding the delta only, because the delta is immutable and the verdict is not. An
  unreadable or foreign-epoch cache is recomputed, costing wall clock only. A cache entry recomputed
  because it was unreadable or carried a foreign `CACHE_EPOCH` prints one line per run,
  `memory-hygiene: check 25 cache recomputed <n> (foreign epoch|unreadable)`. Observed by AC9.
- **S11** A repo-subject arms suite, `transition-audit.test.sh`, on a new gate leg in chunk
  `declarations`, so it is not held the way a kit self-test is (design A3). One fixture repo per
  §18r.1 row the audit can see, plus the criss-cross, liveness, registry and commit-msg arms. It
  prints the agreed `PASS (<n> assertions)` line against a floor. Observed by AC10.
- **S12** The declarations the new moving parts owe in the same commit: a `govkit` exempt row for
  `.githooks/commit-msg` with its reason, `commit-msg` added to `GOV_WIRING_HOOKS`
  (`tools/check-wiring.sh:209`), and the new leg and hook claimed in
  `memory/map/features/memory-tree-hygiene.md` with the map regenerated; a `requires_if` edge in
  `tools/memory-tree/kit.toml` to `memory-recall`, `when_any_key_set = ["BACKLOG_MODE"]`, whose `why`
  says check 25 keys every delta row through the recall kit's anchor grammar under builds mode, and
  that an explicit `shards` value over-selects the kit harmlessly because govkit has no value
  condition; and an arm in `tools/check-wiring.test.sh` comparing, both ways, the tracked files under
  `.githooks/` whose names are git hook names (the closed list in `githooks(5)`) with
  `GOV_WIRING_HOOKS`, observed RED with `commit-msg` removed from the list in a scratch copy.
  Observed by AC10.
- **S13** The delta and the accounting predicate as callable functions, so the relocation tools and
  the hooks reach the ONE transition rule. `delta(ours, theirs)` returns S4's entries for the side
  `ours` against the side `theirs` with no merge commit: the merge bases are
  `merge-base --all(ours, theirs)`, and each entry carries the id, the change kind, the row version
  at every merge base and at `ours`, and the change commit. S4's per-merge delta IS this function
  applied to each shards-side parent against the other parents, so there is one rule, not two.
  `accounted(entries, tip)` evaluates S5 against `tip`'s tree, HEAD by default. Observed by AC11.
- **S14** `transition_audit.py --at <sha> [--expect-builds]` runs full mode over the history `<sha>`
  carries and accounts against `<sha>`'s tree, never HEAD's. `--expect-builds` is the CALLER's own
  independent reading that `<sha>`'s history holds a builds-mode commit; with it S7's first refusal
  applies against that reading, and without it the liveness line ends
  `· reader cross-check not run`. S7's other two refusals apply either way. Exit 0 accounted or
  dormant, 1 unaccounted or duplicate, 2 DEAD PROBE. Full mode (S6) is this code path at HEAD with
  the shell engine's reading passed in. Observed by AC12.
- **S15** On a builds-mode HEAD with the memory-recall kit's `extract.py` unresolvable from the kit
  directory the module derives, check 25 refuses by name — the kit, the path it looked in, and that
  there is no degraded mode — and exits 1. On a shards-mode HEAD it never imports the kit and prints
  its dormant line. Observed by AC15.

## 3. Non-goals (OUT)

- The `RELOCATED` row grammar and its place in the ask parser are unit 6's. Writing those rows is
  unit 12's `--relocate`, `--ingest` and `--repair`; this unit only reads them.
- Instructing a straggler before it merges is unit 13's: the hook bodies, `pre-rebase`, and the
  pre-push call of this module over a pushed feature branch (design A8).
- Remote CI running this check on every push is unit 32's.
- A rebase, squash or cherry-pick of a straggler that discards rows leaves no merge for this audit
  to see. That is design §18r.6 hole 1, stated in the module header and pinned by an arm, not
  closed.
- Check 9's verdicts, the view and the tracked-archive verdict are units 7 and 8's.
- The memory-tree kit version constant moves once per landing range under
  `tools/memory-tree/check-verdict-epoch.sh`'s topological rule, not in this unit.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-6` — the ask and disposition parser, which must admit the
  `RELOCATED` provenance row the fold ignores, and the frozen `BACKLOG_MODE` key spelling. Without
  them accounting has no rows to read and the mode test has no key. It also takes the
  `BACKLOG_MODE` key's entry in the memory-tree kit's config key list, which S12's `requires_if`
  condition names and govkit selfcheck resolves.
- **hands-off** `TOOL-dDerivedDocket-12` — `delta(ours, theirs)` and `accounted(entries, tip)`
  (S13), which `--relocate`, `--ingest` and `--repair` must satisfy before they finish and which
  `--stragglers` reuses at the default tip.
- **hands-off** `TOOL-dDerivedDocket-13` — `transition_audit.py --at <sha> --expect-builds` (S14),
  which the pre-push body runs over a pushed feature tip before a squash can erase its transition,
  and the both-ways hook-list arm in `tools/check-wiring.test.sh` (S12) that `pre-rebase` joins.
- **hands-off** `TOOL-dDerivedDocket-32` — check 25 inside the unguarded `memory hygiene` leg,
  which remote CI runs over a full-history checkout, and the one line prefix S7 pins, which the
  history-audit job's liveness step greps.
- **hands-off** `TOOL-dDerivedDocket-34` — the flip's landing merge, which S3 classifies as a
  transition exactly when main's lineage against the build branch carries a shards-mode commit
  touching the backlog or archive paths, that is, when main's shards moved since the fork; check 25
  then audits it. When they did not, the merge is no transition, and a builds-mode HEAD prints
  `transitions examined 0` and exits 0 with no DEAD PROBE (S7, §8 F2).
- **hands-off** `TOOL-dDerivedDocket-35` — the real-tree staged RED of this check, which the arming
  unit runs after the flip, as the spec brief assigns.
- **hands-off** `DEPL-dDerivedDocket-1` — `.githooks/commit-msg`, which the runbook's switch section
  names as the reference commit-time carrier an adopter wires in its own deployer build.

## 4. Design

### Data model

- **Mode of a commit** — builds or shards, from that commit's own conf blob (S2). The shell engine
  reads HEAD's mode a second, independent way, by sourcing the conf it already sources, and passes
  it in. A guard sharing a variable with what it guards is not a guard; two readers are.
- **Mode boundary** — a commit in builds mode with a parent in shards mode. A linear flip commit is
  one, and so is every transition merge.
- **Transition** — S3. The second conjunct is what keeps an ordinary pre-flip merge of two
  shards-mode branches out of the population; design A1 states only the first and says the tip does
  not matter, which this keeps.
- **Delta entry** — `(transition sha, id, kind, change sha)`. Keys come from `extract.anchor_at`,
  imported lazily from the memory-recall kit directory the way `tools/memory-tree/merge-rows.py:184-210`
  does, so this module spells no second row grammar. With that kit absent under builds mode, S15
  refuses by name; S12's `requires_if` edge is what installs it beside this kit.
- **Accounting** — S5. The RELOCATED row is matched on id and sha prefix only; its why-field is prose.

### The walk, and what it costs

1. `git rev-list --parents <tip>`: the whole parent graph, one process; the tip is HEAD in full mode
   and `<sha>` under `--at`.
2. One `cat-file --batch-check` resolving every commit's conf blob id, then one `cat-file --batch`
   over the distinct blobs. The mode of every commit falls out.
3. No builds-mode commit anywhere: dormant. This is gov's state until the flip, so the dark cost is
   three processes. Measured at this build's records commit `e7da7bf5`: 2523 commits, 309 merges,
   585 commits touching the backlog or archive paths. PINNED as a measurement of that date.
4. Candidates are merges with a mode boundary among their ancestors; lineage sets are computed in
   Python from the graph of step 1, with no process per merge.
5. One `git log --diff-merges=first-parent --name-only` over the two paths names the commits that
   touch them, and one more `cat-file --batch` fetches the blobs the deltas need.
6. Cached deltas skip steps 4 and 5 for every merge already seen.

The first post-flip run on a node pays for every candidate merge once. The `memory hygiene` leg's
declared ceiling is not moved by this unit.

### Liveness, the registry, and the remedy

The liveness line reads
`memory-hygiene: check 25 transitions examined <N> · merges walked <M> · pinned <P> · unpinned <U> · cache hits <H>`,
where H counts transitions whose delta was read from a valid cache entry. Design A3 made N=0 on a builds-mode tree a DEAD PROBE and said the flip's
landing merge guarantees N≥1. Re-grounded: the flip is a linear commit on the build branch, so every
full run between it and the landing merge would red, and the landing merge is a transition only when
one side's lineage carries a shards-mode backlog commit, which nothing guarantees. S7's mode-boundary
predicate replaces it (§8 F2).

The remedy names the repair verb only. The full relocation recipe is a banner the view header, the
driver and the hook bodies carry; this is a verdict line.

### The commit-msg carrier

Re-measured on node `d` with git 2.54.0.windows.1 in a scratch repo: a clean `git merge` fires
`pre-merge-commit` with no `MERGE_HEAD`, then `commit-msg` with `MERGE_HEAD` present; a conflicted
merge concluded by `git commit` fires `pre-commit` and `commit-msg`, both with `MERGE_HEAD` present.
`commit-msg` is the one hook that sees every concluded merge, which is design A7's claim, confirmed.
The hook resolves the module in `$top` with the same probe `.githooks/pre-commit:42-45` uses, so an
old node's hook file still runs the NEW module once the merge brought it in (design §18r.2 L2).

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `transition_audit.py` and its functions | kit module | lexicon: python function cell; names pass `lexicon.py --suggest` before they are written |
| `delta` and `accounted` (S13), `--at` and `--expect-builds` (S14) | module functions and options | lexicon: python function cell for the two functions; they are the interface units 12 and 13 cite, so a rename `--suggest` forces is made in all three specs at once |
| check 25 | hygiene check number | none |
| `transition-audit.txt` | registry under `<MEMORY_ROOT>/project/` | check 3 whitelist |
| `.githooks/commit-msg` | tracked hook | lexicon: shell function cell for any function it defines |
| `transition-audit.test.sh` and its leg | repo-subject suite | testsuite-counts contract |
| `CACHE_EPOCH` | module constant | none |

### Files touched (estimate)

`transition_audit.py` (new) · `tools/memory-tree/check-memory-hygiene.sh` · `transition-audit.test.sh`
(new) · `.githooks/commit-msg` (new) · `tools/gate-legs.json` · `tools/check-wiring.sh` ·
`tools/check-wiring.test.sh` · `tools/govkit/registry.toml` · `tools/memory-tree/kit.toml` · `transition-audit.txt` (new, empty
list plus header) · `memory/map/features/memory-tree-hygiene.md` · `memory/map/generated/` ·
`tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md` (the check 25 entry).

### Alternatives rejected

- **Classify by the parent's TIP conf** (design §18r.2.1): refuted by the bypass hunt's blocker, a
  straggler that pulled the new conf early blinds it (design A1).
- **WONTDO as the accounting record** (design §18r.3): it declines a live ask; forbidden by A4.
- **L2 inside `pre-commit`**: never fires on a clean merge, measured above.
- **L2 through the whole `--staged` hygiene run**: runs every staged check a second time on a
  conflicted merge that `pre-commit` already graded, for no added coverage; the direct module call
  is the smallest carrier (§8 F3).
- **A process per merge per parent**: roughly three per candidate merge on a platform where process
  creation is the cost; the in-memory graph removes them.

## 5. Production-readiness checklist

- security — reads git objects only, through the pinned dereference; a replace ref or a graft
  cannot substitute history. The hook writes nothing.
- perf / scale — dark cost is three processes; the first post-flip walk is paid once per node and
  cached; the cache is advisory.
- error / empty / loading states — shallow, disagreeing readers and a boundary-free history each
  refuse by name; a shards-mode HEAD announces dormancy rather than printing a clean zero.
- observability — the liveness line on every full run; `--pin` and a `--report` print mode list
  every transition and entry without redding.
- risks — a text change on a continuation line of a wrapped legacy row is invisible to anchor
  keying; the module header states it. A deliberate rebase that drops rows stays invisible.
- testing — S11's suite; each arm observed RED with its fix unstaged before the leg is wired.
- migration — none for data. The registry starts as a header with no rows and is appended by
  `--pin` after the flip.
- user docs — the check 25 entry in the HYGIENE template and its dogfood; the memory-tree README
  section is unit 36's.

## 6. Acceptance criteria

- **AC1** — When `transition-audit.test.sh` merges a fixture straggler into a builds-mode default
  branch with `git merge --no-ff` and no RELOCATED row, `bash tools/memory-tree/check-memory-hygiene.sh`
  exits 1 naming the merge sha, the id and the change commit; with one RELOCATED row per entry it
  exits 0. Red when: the predicate reads the parent's tip conf, and a straggler whose tip carries
  the new conf passes unaccounted.
  cost: fixture repos only; observed at the one post-build bar and by hand in a scratch copy.
- **AC2** — When the fixture's accounting carries two RELOCATED rows for one entry, `transition_audit.py`
  exits 1 naming both files; with a row whose sha prefix names another commit, it exits 1 as
  unaccounted. Red when: accounting matches on id alone and a stale provenance row certifies a new
  change.
- **AC3** — When the fixture merges default into the straggler (§18r.1 row 1) and when it merges the
  straggler into default (row 2), `transition_audit.py --report` lists one transition each; after a
  `git merge --squash` onto default (row 3) and a rebase (row 4) it lists none, and the arm asserts
  exactly that. Red when: a squash or rebase fixture is reported as a transition, or the two merge
  rows are not.
  fixture: built by the suite; none exists in the tree today.
- **AC4** — When a criss-cross fixture holds a row version that differs from one merge base and
  equals another, `transition_audit.py --report` omits it from the delta; a row removed from both
  the shard and its archive appears as REMOVED. Red when: the delta compares against the first
  merge base only.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs on this tree before the flip,
  it prints check 25's dormant line and exits 0 on that account; on a builds-mode fixture it prints
  `transitions examined` with a non-zero count. Red when: the dormant branch prints nothing, which
  reads exactly as a clean audit.
  figure: every count on the line is DERIVED at run time.
- **AC6** — When the fixture's HEAD is builds mode and the module's conf reader is staged broken to
  read every blob as shards, the check exits 1 as a DEAD PROBE; a
  `git clone --depth 1 file://<fixture>` of the builds-mode fixture, which
  `git rev-parse --is-shallow-repository` reads as shallow, also exits 1 as a DEAD PROBE; a
  linear-flip fixture with no transition merge exits 0
  and prints `transitions examined 0`; and with the mode-boundary detector staged broken over a
  history holding both shards-mode and builds-mode commits, the check exits 1 as a DEAD PROBE.
  Red when: either of the first two cases prints the dormant line, because one reader then silently
  agrees with a broken other; or N=0 on a builds-mode HEAD is refused (design A3's rule, which F2
  replaced), so the flip branch reds between its flip commit and its landing merge; or a broken
  boundary detector reads as dormant.
- **AC7** — When `transition-audit.txt` lists a sha that the fixture's history does not hold, or one
  that no longer classifies, the check exits 1 naming the row; `transition_audit.py --pin` prints a
  row for each unpinned transition and writes nothing. Red when: a listed row that stopped
  classifying is skipped rather than refused.
- **AC8** — When a fixture merge with an unaccounted entry is concluded, `.githooks/commit-msg`
  refuses both the clean `git merge` and the conflicted merge finished by `git commit`; a non-merge
  commit passes with no output. Red when: the hook keys on `pre-commit`'s staged set, so the clean
  merge commits.
- **AC9** — When `transition_audit.py --report` runs twice on an unchanged fixture, the second run's
  liveness line reads `cache hits <H>` with H equal to its `transitions examined` count; a cache
  file rewritten with a foreign `CACHE_EPOCH` makes the next run print `check 25 cache recomputed`
  naming `foreign epoch` and `cache hits` one lower. Red when: a stale-epoch cache is read as valid,
  so its hit count stays equal to the examined count.
- **AC10** — When `bash tools/check-testsuite-counts.sh` runs, the new suite prints its
  `PASS (<n> assertions)` line at or above its floor, and `python tools/govkit/govkit.py selfcheck`
  passes with `.githooks/commit-msg` tracked and with the new `requires_if` edge; and
  `bash tools/check-wiring.test.sh` passes its both-ways hook-list arm with `.githooks/commit-msg`
  tracked.
  Red when: the hook is tracked with no exempt row and selfcheck is not consulted, which is the
  declared-population class; or `commit-msg` is tracked and absent from `GOV_WIRING_HOOKS`, so check
  H never reports the diverged hook S9 depends on.
- **AC11** — When `transition-audit.test.sh` calls `transition_audit.delta(ours, theirs)` with a
  fixture straggler tip as `ours` and the builds-mode default tip as `theirs`, with no merge between
  them, it returns the entries — id, kind and change commit — that `transition_audit.py --report`
  lists for the transition merge of the same two commits once that merge is made;
  `accounted(entries, tip)` over a tip carrying one `RELOCATED` row per entry returns every entry
  accounted.
  Red when: the function is bound to HEAD or to a merge's parents, so the no-merge call returns
  nothing or raises, and unit 12 has no entry point to call.
- **AC12** — When `transition_audit.py --at <sha> --expect-builds` runs from a checkout whose HEAD is
  a different commit, over a fixture feature tip holding an unaccounted transition merge, it exits 1
  naming that merge and `--repair`; the same fixture checked out at the tip with no `--at` gives the
  same verdict; with the module's conf reader staged to read every blob as shards,
  `--at <sha> --expect-builds` exits 2 as a DEAD PROBE; and without `--expect-builds` the liveness
  line ends `reader cross-check not run`.
  Red when: `--at` reads HEAD's history or tree, so a pushed tip that differs from HEAD is audited
  as HEAD and the pre-push block passes an unaccounted transition.
- **AC13** — When the fixture holding an unaccounted transition has that merge replaced by a
  non-merge commit through `git replace`, `bash tools/memory-tree/check-memory-hygiene.sh` still
  exits 1 naming the merge; and separately, with a graft file under the fixture's git dir that
  re-parents the merge, it exits 1 the same way.
  Red when: one git call in the module lacks `--no-replace-objects` or the `GIT_GRAFT_FILE` pin, so a
  ref an agent can write hides the lost row and check 25 reads clean.
- **AC14** — When a fixture straggler merges a shards-mode default commit that changes one row, then
  merges into the builds-mode default, `transition_audit.py --report` lists no delta entry for that
  id, while a row the straggler changed itself is listed.
  Red when: the A6 clause is dropped, so a row that came across from the default side is reported as
  the straggler's own change and demands a provenance row nobody can honestly write.
- **AC15** — When `transition-audit.test.sh` runs check 25 over a builds-mode fixture whose
  memory-recall kit directory is absent, it exits 1 naming `memory-recall` and the path it looked
  in; over a shards-mode fixture with the kit absent it prints the dormant line and exits 0.
  Red when: the lazy import raises uncaught, or the delta is keyed without the anchor grammar, so a
  memory-tree-only adopter's permanent audit either crashes the hygiene run or grades nothing.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `govkit selfcheck` · `check-wiring self-test` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `spec tokens (a spec's own names resolve)`

New arm: `transition-audit.test.sh` on a new repo-subject leg · each §18r.1 fixture merged with no provenance row, a broken conf reader, a shallow clone, a stale registry row, a replace ref and a graft, a `--at` tip differing from HEAD, an absent memory-recall kit · the new suite's own floor

New arm: `tools/check-wiring.test.sh` both-ways hook-list arm · `commit-msg` removed from `GOV_WIRING_HOOKS` in a scratch copy · none

## 8. Open questions

- **F1 — what the registry pins.** Design A3 calls it shrink-only. In this repo a shrink-only list
  drains a debt, which here would be a waiver list, and design §18r.3 says there is no waiver
  registry. A transition in history is permanent, so its row is too. Options: (a) an append-only
  pin of known transitions and their verdict, unlisted ones counted not refused, because a merge
  cannot list its own sha; (b) no registry, liveness from N alone; (c) a debt list of unaccounted
  transitions. RESOLVED (agent, 2026-09-14, delegated): (a). It is the only option that catches a
  classifier regression dropping one of several known transitions; (c) fails §18r.3 and (b) fails A3.
- **F2 — the DEAD PROBE predicate.** A3's "N=0 on a builds-mode tree" reds the flip branch between
  its flip commit and its landing merge. RESOLVED (agent, 2026-09-14, delegated): S7's three
  refusals, which can still fail on a broken reader and never red an honest flip branch.
- **F3 — the L2 carrier's call.** RESOLVED (agent, 2026-09-14, delegated): `commit-msg` calls the
  module directly, not the whole `--staged` engine, for the reason §4 gives.
- **F4 — the second conjunct of S3.** A1 alone classifies every pre-flip merge that touched the
  backlog. RESOLVED (agent, 2026-09-14, delegated): require a builds-mode commit in the other
  parent's lineage, which keeps A1's lineage test and its indifference to tips.
- **F5 — the named-tip form's liveness.** A hook has no shell engine to supply S7's second conf
  reader. Options: (i) drop the reader cross-check under `--at`; (ii) keep it when the caller passes
  its own independent reading as `--expect-builds`, and announce the skip otherwise; (iii) read the
  conf twice inside the module. (iii) is one reader twice, which §4's two-readers rule refuses; (i)
  loses a refusal a caller could still arm. RESOLVED (agent, 2026-09-14, delegated): (ii).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.
- rev-2 · 2026-09-14 · S1 · S4 · S6 · S7 · S10 · S12 · S13 · S14 · S15 · §3 · §4 · §6 · §7 · §8 ·
  AC6 · AC9 · AC10 · AC11 · AC12 · AC13 · AC14 · AC15 · F5 · folds spec-audit round 1. G2 H1 (1,
  48): S13 `delta` and `accounted`, S14 `--at <sha> [--expect-builds]`, the hands-offs to 12 and 13
  name them, AC11, AC12 and §8 F5. G2 M6 (49): the hands-off to 34 states when the landing merge is a
  transition. G2 M16 (15): AC13 stages a replace ref and a graft. G2 M17 (17): AC6 stages the linear
  flip and a broken boundary detector. G2 M18 (18): the liveness line gains `cache hits`, S10 its
  recompute line. G2 M8 (76): S12's memory-recall `requires_if` on `BACKLOG_MODE`, S15 and AC15. G2
  L1 (19): AC14. G2 L2 (20): the both-ways hook-list arm. G5 L5 (47): the hands-off to DEPL. G5 H5's
  unit-9 end: S7 pins the `memory-hygiene: check 25 ` line prefix.

## 10. Reuse audit

- `reuse_lookup.py "audit merge commits in history whose parent was in an older mode"` returned no
  seam that classifies merges by a conf read at each commit; its nearest hits were the
  `pass-order history` gate leg and `merge-rows.skeleton`, and it states that `.sh` is an unscanned
  layer. So the seams were located by reading source: check 24's delegation to a sibling module
  (`tools/memory-tree/check-memory-hygiene.sh:1092-1100`) is the carrier this extends; the pinned
  dereference is the one `tools/unattended/check-pass-order.sh` holds, copied rather than sourced
  because a kit may not source a sibling kit; the anchor grammar is reused through the same lazy
  import as `tools/memory-tree/merge-rows.py`; the shallow-clone refusal follows
  `tools/drift-audit/drift_report.py:1228`. The recall hit `TOOL-aSurfacedLexicon-22` (a history
  leg at 267 s standalone before memoising) is why S10 caches and §4 walks the graph in memory.
- Where design and BASE disagree: design A3's liveness predicate (§8 F2); design §18r.2 L2 names
  the `--staged` engine, and A7 plus this spec name the direct module call.
- Recall terms used: `transition merge straggler shards builds history audit liveness DEAD-PROBE
  shallow graft replace-ref pass-order`
