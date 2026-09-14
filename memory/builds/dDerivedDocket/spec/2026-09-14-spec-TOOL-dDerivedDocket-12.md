# TOOL-dDerivedDocket-12 — relocation tools for pre-flip branches

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g2-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g2-round1.md) | spec-audit | TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 |

<!-- /gen:spec-records -->

## 1. Goal

A branch that forked before the flip and edited authored backlog shards carries row changes that no
longer have a file to land in, because the shards become generated views. Give that branch, the
default branch acting on its behalf, and any node repairing a merge that already lost rows one delta
engine that moves every changed row into the per-build files, writes a provenance row the transition
audit can count, and refuses to finish while any change is unaccounted.

## 2. Scope (IN)

- **S1** `migrate_backlog.py --relocate --as <slug> [--from <ref>]`, run on the straggler after it
  merged the default branch. The straggler side is `HEAD` while `MERGE_HEAD` exists, else the first
  parent of a merge `HEAD`, else `--from <ref>`; the other side is `MERGE_HEAD`, the second parent,
  or `HEAD` respectively. Anything else refuses and prints the recipe. Observed by AC1 and AC9.
- **S2** The classification table in §4 maps every delta entry to records: a new ask row in its id's
  slug folder, a disposition in the `--as` folder, a path repoint of the ask text (ruling D9), a
  mechanical drop, or NEEDS-HUMAN. Observed by AC1, AC2 and AC11.
- **S3** Provenance (design A4). Every delta entry gets exactly one
  `- RELOCATED · <id> · by <sha> · kept|dropped|amended: <why>` row in the `--as` folder's
  `BACKLOG.md`, where `<sha>` is the change commit unit 9's delta names. After writing, the verb
  re-reads the tree through unit 9's accounting predicate and exits 1 on any entry not accounted
  exactly once. Observed by AC1 and AC4.
- **S4** Plan, then write, all or nothing. Any NEEDS-HUMAN entry, or any record S5 holds for
  confirmation, makes the verb write NOTHING and print the plan with the exact re-run command. A
  human classifies an entry with `--drop <id>=<why>`, which writes a `dropped:` provenance row and no
  other record. Observed by AC2.
- **S5** Confirmation (design A6). Under `--repair` and `--ingest`, a planned record that changes the
  id's derived status at the target tree requires `--confirm <id>`; without it the verb refuses,
  naming the status before and after and the change commit. `--relocate` writes its author's flips
  and lists every status change in its table. Observed by AC3.
- **S6** `--ingest <ref> --as <slug>`, run from a builds-mode checkout of the default branch for a
  straggler nobody will revisit. Same engine, delta of `<ref>` against `HEAD`, no merge made.
  Observed by AC5.
- **S7** `--repair <merge-sha> --as <slug>`, run from any builds-mode checkout for a transition that
  hygiene check 25 reports. It plans only the entries not already accounted at `HEAD`, so a second
  run plans nothing. Observed by AC4.
- **S8** `--stragglers [--local] [--tsv]`, a print mode over every local and remote-tracking ref,
  `--local` narrowing to `refs/heads`. A ref is listed while its delta against the default branch
  holds an entry that the default tip neither holds in history nor accounts. It prints a liveness
  line with refs examined, and exits 1 as a DEAD PROBE on zero refs or a shallow repository.
  Observed by AC6.
- **S9** `--dry-run` on the three writing verbs prints the plan and the conservation table, touches
  neither the worktree nor the index, and exits 0 only when the plan would write. Observed by AC7.
- **S10** `--recipe` prints the relocation recipe of design §18r.4 from the one constant unit 7 keeps
  in `backlog.py`, holding no copy of its own. The kit selftest compares that output with the recipe
  block in the view header the generator renders and in the row driver's shard-into-view banner,
  over fixtures, so a carrier that re-spells the text reds. Observed by AC8.
- **S11** Under `--relocate`, every view path and every backlog archive path is set to the other
  side's version, or removed where the other side has none, and `gen_build_index.py --write`
  re-renders the views before the table prints. Observed by AC1 and AC11.
- **S12** Arms for every verb in the kit selftest `migrate_backlog.py --selftest`, each observed RED
  with its fix unstaged, and the selftest's `PASS (<n> assertions)` floor moved in the same commit.
  Observed by AC10.

## 3. Non-goals (OUT)

- The delta itself and the accounting predicate are unit 9's; this unit calls them and never spells
  a second transition or row-version rule.
- The ask, disposition and `RELOCATED` grammars and the status fold are unit 6's; the permissive
  legacy-row parser and the module file are unit 11's. This unit writes rows in those grammars.
- `--write`, the switch-over's whole-corpus migration, is unit 34's thin driver over this engine.
- Printing the recipe in hook bodies, and the drift signal over `--stragglers`, are unit 13's.
- An unattended run never performs a relocation (design A10); that rule lives in the unattended
  carriers, unit 20. The engine does not detect a run. The switch-over's own landing reconcile is
  unit 34's decision (its §8 F5), not this unit's.
- No severity and no `accept` or `seen` clause is invented for a relocated ask. An ask whose
  first-seen date falls on or after `ASK_CUTOFF` is written and listed, and the generator's own
  verdicts then name what it owes.
- A rebase, squash or cherry-pick that discards rows leaves no delta for this engine to find
  (design §18r.6 hole 1).
- The memory-tree kit version constant moves once per landing range under
  `tools/memory-tree/check-verdict-epoch.sh`'s rule, not here.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-6` — the ask, disposition and `RELOCATED` row grammars this
  engine writes, and the fold S5 runs twice to decide whether a record changes a derived status.
- **consumes-from** `TOOL-dDerivedDocket-7` — `gen_build_index.py --write`, its data-loss guard,
  which S11 satisfies by restoring the views first, and the recipe constant in `backlog.py`, which
  `--recipe` prints and the view header renders.
- **consumes-from** `TOOL-dDerivedDocket-9` — the delta, callable for a straggler-side commit against
  the other side's commits without a merge commit, and the accounting predicate S3 re-reads.
- **consumes-from** `TOOL-dDerivedDocket-10` — the row driver's shard-into-view banner, whose recipe
  block S10 compares.
- **consumes-from** `TOOL-dDerivedDocket-11` — `tools/memory-tree/migrate_backlog.py`, its permissive
  legacy-row parser, and its `--selftest` leg, which S12 extends.
- **hands-off** `TOOL-dDerivedDocket-13` — `--stragglers` for the session-start inventory and the
  drift signal, and `--recipe` for the hook bodies' parity arm.
- **hands-off** `TOOL-dDerivedDocket-20` — `--recipe`, the text the unattended carriers tell a run
  on a pre-flip BASE to park with, because a run never relocates (design A10).
- **hands-off** `TOOL-dDerivedDocket-34` — the engine with its disposition-home policy and provenance
  switch for `--write`, `--stragglers` for the inventory before the write, and `--dry-run` for the
  landing-reconcile rehearsal.
- **hands-off** `DEPL-dDerivedDocket-1` — `--stragglers` and `--recipe`, which the adopter runbook's
  migrate steps name.

## 4. Design

### The engine

One planner, three writing verbs. Its input is a delta: entries of id, change kind, the row version
at every merge base and at the straggler side, and the change commit, exactly as unit 9 returns
them. Shard and backlog-archive rows of one family are one population, so a cut-mode rotation on the
straggler (`ROTATION_MODE="cut"`, `.memory-tree.conf:394`) is no change and a flip rotated away with
it is one. Legacy rows are read with unit 11's parser, which admits every shape design §9 step 2
lists. The planner's output is a set of records per file, a NEEDS-HUMAN list and a CONFIRM list;
the writer applies it only when both lists are empty.

Two policies are parameters, so unit 34 can drive the same engine: where a disposition goes (the
`--as` folder here, the ask owner's folder under `--write`), and whether provenance rows are written
(always here; never for a linear switch-over, which is no transition).

### Classification

| Delta entry | Records written | Provenance kind |
|---|---|---|
| new id, legacy token OPEN | ask row in `builds/<slug(id)>/BACKLOG.md` | `kept: new ask` |
| new id with a terminal or held token | ask row, plus the disposition the flip rows below give | `kept: new ask` |
| flip to CLOSED | `- CLOSED · <id> · by <change sha> · …` in the `--as` file | `kept: flip to CLOSED` |
| flip to WONTDO or WITHDRAWN | `- WONTDO · <id> · <the row's own reason, or "withdrawn">` | `kept: flip to WONTDO` |
| flip to BLOCKED or DEFERRED naming an id | `- BLOCKED · <id> · on <X>` or `- DEFERRED · <id> · until <X>` | `kept: hold` |
| flip between live tokens | none; the status is derived now | `kept: live flip, derived` |
| text change confined to path tokens | the ask text in its home file repointed (D9) | `amended: path repoint` |
| any other text change; a flip to a live token from a terminal one; a hold naming no id | NEEDS-HUMAN | via `--drop` only |
| removed row that was terminal at the merge base | none | `dropped: terminal row removed` |
| removed row that was live at the merge base | NEEDS-HUMAN | via `--drop` only |

`filed` on a new ask is the author date, as a day, of the oldest lineage commit whose blob holds the
id, taken from the commit list the delta walk already read. The ask body is the legacy body minus
the status slot, joined onto one physical line where the parser declared a wrap.

A planned disposition for a target the `--as` file already disposes is NEEDS-HUMAN, because one
file carries one disposition per target. An entry already accounted at the target tree plans
nothing, which is what makes every verb idempotent.

### Confirmation, and why it binds two verbs of three

The fold is run over the target tree before and after the planned records. A record whose id moves
status is status-changing. `--repair` and `--ingest` are run by someone other than the straggler's
author, after the fact, on a tree whose default side may have acted deliberately since the fork;
design lab case e09b had `--repair` write CLOSED over a deliberate reopen. Those two verbs therefore
refuse a status-changing record without `--confirm <id>`. `--relocate` is run by the author on a
fresh merge, and the recipe every banner carries is one command; making it demand per-id
confirmation would break the recipe on its own instruction (§8 F1).

### The relocate tree restore

After the merge, a view carries conflict markers or authored rows and an archive carries a
modify/delete conflict. S11 sets each `<MEMORY_ROOT>/backlog/<F>.md` and each path the hygiene
engine's `--print-rotated-archive-ere` selects under the family alternation to the other side's
blob, or removes it, in the worktree and the index. Only then does the generator run, so its
data-loss guard reads a clean view. `--dry-run` does none of this.

### Straggler inventory

The default tip is resolved as `.githooks/pre-push:91-110` resolves it: the observed `origin/HEAD`
wins and `GOV_DEFAULT_BRANCH` only cross-checks it, because the recall hit `TOOL-aStandingWrit-5`
records an environment value that disabled a guard by naming the branch already checked out.

Candidates come from ONE walk, `git log --source` over the selected refs excluding the default
tip's history and limited to the backlog and archive paths, so a ref with no such commit costs no
delta at all. Each candidate ref then gets its delta against the default tip. An entry held by the
default tip's history (design A6) or accounted by a `RELOCATED` row at that tip does not count; that
is CONTENT, not ancestry, so an ingested but unmerged ref stops being listed once the records land.
Before the flip nothing is accounted, so the listing is design §9 step 1's drain inventory.

`--tsv` prints `straggler<TAB><ref><TAB><tip sha><TAB><unaccounted><TAB><first change sha>` per ref,
then `examined<TAB><n>`. Measured on node `d` on 2026-09-14 against `origin/main` at `7484d8d7`: 90
refs, 47 local and 43 remote-tracking, of which 6 carry commits touching the backlog or archive paths
that `origin/main` lacks. PINNED as that measurement; the command re-derives it.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `--relocate`, `--ingest`, `--repair`, `--stragglers`, `--recipe` | CLI modes of `migrate_backlog.py` | flags; the functions behind them lead with a `.lexicon.conf` verb, checked by `lexicon.py --suggest` before they are written |
| `--as`, `--from`, `--drop`, `--confirm`, `--dry-run`, `--local`, `--tsv` | CLI options | flags |

### Files touched (estimate)

`tools/memory-tree/migrate_backlog.py` · its selftest fixtures inside the module or beside it ·
`memory/map/generated/` regenerated for the new symbols · `tools/memory-tree/README.md`'s usage
line for the new modes, if unit 11 created one.

### Alternatives rejected

- **WONTDO as the drop record** (design §18r.3). Rejected by the bypass hunt's A4: it declines a live
  ask, and §2.1 forbids status on a drop.
- **Dispositions in the ask owner's folder.** Rejected by design §3: every authored byte lives in its
  writer's folder; the migration is the one sanctioned exception and it is unit 34's.
- **Confirmation-free `--repair`.** Rejected by lab case e09b (design A6), which wrote CLOSED over a
  deliberate reopen.
- **Classifying a transition by the straggler's tip conf.** Rejected by the bypass hunt's blocker
  (design A1); the engine takes unit 9's lineage delta instead.

## 5. Production-readiness checklist

- security — the three writing verbs are the sanctioned cross-folder writers after the flip. They
  transfer text an owner already wrote, execute nothing from any row, and read git objects through
  unit 9's pinned dereference.
- perf / scale — one delta walk per verb; `--stragglers` pays one narrowing walk for every ref and a
  delta only per candidate ref, and `--local` bounds the session-start call to local branches.
- error / empty / loading states — refusal with nothing written on NEEDS-HUMAN or CONFIRM; exit 2
  with the recipe on a shards-mode target, a missing merge and no `--from`, a malformed `--as`, or a
  shallow repository; DEAD PROBE on zero refs.
- observability — the conservation table on every verb: id, kind, classification, records, file,
  and the status before and after.
- risks — a text change on a continuation line of a wrapped legacy row is invisible to anchor keying
  (unit 9's stated risk). A relocate over a default side that reopened an ask since the fork writes
  the author's close; the table shows it and no confirmation is demanded (§4).
- testing — S12's arms, each staged RED with its fix unstaged; the selftest is a held kit leg, so the
  landing bar owes `GATE_FULL=1 GATE_SELFTESTS=1`.
- migration — none of its own; the modes are inert until the default branch is in builds mode, and
  `--stragglers` is read-only in both modes.
- user docs — the module header and the recipe; the memory-tree README section is unit 36's.

## 6. Acceptance criteria

- **AC1** — When the selftest merges a builds-mode default branch into a fixture straggler that added
  one row, flipped one to CLOSED and repointed one path, and runs
  `migrate_backlog.py --relocate --as <slug>`, it exits 0; the ask row sits in its id's folder, the
  CLOSED disposition cites the flip commit, the ask text carries the new path, each entry has one
  `RELOCATED` row, and `transition_audit.py --staged` accepts the merge commit.
  Red when: a `RELOCATED` row cites the merge sha instead of the change commit, so unit 9's
  accounting reads the entry unaccounted.
- **AC2** — When the fixture straggler also amends one row's prose, `--relocate` exits 1, names the id
  and the `--drop` re-run, and `git status --porcelain` shows the tree exactly as the merge left it;
  re-run with `--drop <id>=<why>` it exits 0 and writes one `dropped:` row for that id.
  Red when: the refusal leaves some records written, so a half-relocated tree gets committed.
- **AC3** — When a fixture's default side carries a REOPEN for an id the straggler closed,
  `migrate_backlog.py --repair <merge-sha> --as <slug>` exits 1 naming the id, its status before
  and after, and `--confirm`; with `--confirm <id>` it writes. An uncontested new ask is written
  without confirmation.
  Red when: the repair writes CLOSED over the reopen unconfirmed, which is lab case e09b.
- **AC4** — When a fixture transition is committed with `--no-verify` and unaccounted,
  `bash tools/memory-tree/check-memory-hygiene.sh` reds check 25; after `--repair` it passes; a
  second `--repair` plans zero records.
  Red when: the second run writes duplicate `RELOCATED` rows, which unit 9 reds as a duplicate.
- **AC5** — When `migrate_backlog.py --ingest <ref> --as <slug>` runs on the default branch and its
  records are committed, `--stragglers` stops listing that ref while it is still unmerged, and a
  later merge of the ref passes the transition audit with no further record.
  Red when: the inventory judges by ancestry, so an ingested ref is listed until someone merges it.
- **AC6** — When `migrate_backlog.py --stragglers` runs over a fixture holding a local straggler, a
  remote-tracking straggler and a clean ref, it prints `examined 3` and lists two; with `--local` it
  lists one; with no ref, and in a `git clone --depth 1`, it exits 1 as a DEAD PROBE.
  Red when: the default walk skips `refs/remotes`, so a pushed straggler on another node reads as
  none.
- **AC7** — When any writing verb runs with `--dry-run`, it prints the plan and the table and
  `git status --porcelain` is unchanged, including no new filing-home folder.
  Red when: the restore of S11 runs under `--dry-run` and stages view paths.
- **AC8** — When the selftest renders a builds-mode fixture view with `gen_build_index.py --write`
  and runs `merge-rows.py` on a shard-into-view fixture, both recipe blocks equal the bytes
  `migrate_backlog.py --recipe` prints.
  Red when: one carrier drifts by a byte and no arm reds.
- **AC9** — When `--relocate` runs where the other side's `.memory-tree.conf` blob is in shards mode,
  or with no `MERGE_HEAD`, no merge `HEAD` and no `--from`, it exits 2 naming the missing condition
  and prints the recipe; an `--as` value outside the slug shape exits 2.
  Red when: the verb writes `BACKLOG.md` files into a shards-mode tree, which the mode guard then
  reds as a half-migration.
- **AC10** — When `migrate_backlog.py --selftest` runs, it prints its
  `PASS (<n> assertions)` line at or above the moved floor, and `bash tools/check-testsuite-counts.sh`
  and `bash tools/check-install-prefix.sh` pass.
  Red when: an arm is added whose failing case was never observed, or the module names a sibling
  kit's path by literal.
  cost: one kit selftest run; it is held, so it runs at the landing bar under `GATE_SELFTESTS=1`.
  permission: unit passes run no gate legs (fix F7), so each arm's RED is observed by hand against a
  scratch fixture in the pass, and the three commands above run at the one post-build bar.
- **AC11** — When the fixture straggler rotated a flipped row into a backlog archive, `--relocate`
  accounts the flip once and removes the archive path the default side does not carry.
  Red when: the archive stays tracked, which the tracked-archive verdict reds after the flip (D8).

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `testsuite counts (every bar self-test prints one)` · `codebase-map coverage + freshness` · `build-index selftest` · `row-keyed merge driver replay`

New arm: `python3 tools/memory-tree/migrate_backlog.py --selftest` · one fixture per classification row, the all-or-nothing refusal, the confirmation refusal, the three DEAD PROBE cases, `--dry-run`, the recipe parity · the selftest's assertion floor

## 8. Open questions

- **F1 — which verbs demand `--confirm` for a status-changing record?** Options: (a) `--repair`
  only, as design A6 words it; (b) all three verbs; (c) `--repair` and `--ingest`. (a) leaves
  `--ingest`, run by the same kind of actor after the fact, open to lab case e09b; (b) makes the
  recipe's own `--relocate` line fail on every honest flip, so every carrier's recipe would change.
  RESOLVED (agent, 2026-09-14, delegated): (c).
- **F2 — a partial write on refusal?** Design §18.4 says the verb refuses to finish while a row is
  unclassified, without saying what is already on disk. RESOLVED (agent, 2026-09-14, delegated):
  plan then write, all or nothing, because a half-relocated tree is one `git add memory/` from
  being committed.
- **F3 — where does a `RELOCATED` row go?** RESOLVED (agent, 2026-09-14, delegated): the `--as`
  folder, the writer's own, which design §3 requires and unit 9's accounting accepts from any
  `BACKLOG.md`.
- **F4 — a removed row.** Design §18.4 does not classify one; A5 says it needs a provenance row.
  RESOLVED (agent, 2026-09-14, delegated): mechanical `dropped:` for a row terminal at the merge
  base, whose status the removal cannot change, and NEEDS-HUMAN for a live one.
- **F5 — the recipe's single source.** Design §18r.4 requires one text in every banner, and units 7,
  10 and 13 print it before or beside this one. RESOLVED (agent, 2026-09-14, delegated): the constant
  unit 7 keeps in `backlog.py`, as that unit's own F5 resolved; `--recipe` prints it, this unit's
  selftest compares the three Python renderings, and unit 13 compares its shell copy.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from design §18.4, §18r.3, §18r.4 and amendments A4, A5, A6
  and A10. Adds five edges the brief's table does not carry: consumes-from units 6, 7 and 10, whose
  grammars, render path and banner this unit writes into or compares, and hands-off unit 20 and
  `DEPL-dDerivedDocket-1`, whose carriers name `--recipe`. Units 6, 7 and 10 declare the matching
  lines. The recipe constant's home follows unit 7's §8 F5. Unit 9's spec describes its delta per transition merge; this spec needs
  it callable for a straggler-side commit with no merge, which the M2 interface cross-read confirms.

## 10. Reuse audit

No existing seam fits the engine itself: nothing in the tree moves a row between files by change
kind. `python tools/codebase-map/reuse_lookup.py "relocate rows from an old branch delta into
per-build files with provenance"` returned name-stem neighbours only (`build_reference_index`,
`corpus_files`) and reports `.sh` unscanned. `reuse_lookup.py "merge rows driver anchor id row key"`
returned `anchors` and `key` in `tools/memory-tree/merge-rows.py` and `anchor_at` in
`tools/memory-recall/extract.py`: the anchor grammar this engine reaches only through unit 9's delta,
never by a copy. The seams it extends are unit 9's delta and accounting, unit 11's parser, and the
generator's `--write`; the default-branch resolution copies `.githooks/pre-push:91-110`. The recall
hit `TOOL-cSpliceWarden-6` is why §4 treats shard and archive as one population: under cut-mode
rotation an archive holds terminal rows only, so a flip can leave the shard and the archive together.

Where the design and BASE disagree: design §18.4 records a drop as WONTDO, superseded by A4; design
§9 step 1 counted 11 straggler refs on this node, re-measured here as 6 of 90 against a later
`origin/main`; `migrate_backlog.py`, `transition_audit.py` and `backlog.py` do not exist at
`abac6d59` and are units 11, 9 and 6.

Recall terms used: `straggler relocate rotation reconcile lost flip merge-rows driver shard archive
provenance`
