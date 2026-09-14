# TOOL-dDerivedDocket-34 — the switch-over: migration applied and the views rendered

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling+kickoff · order 34

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g5-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g5-round1.md) | spec-audit | TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

Switch this repo from authored backlog shards to asks filed per build with generated family views,
in ONE commit that applies the migration exactly as the signed tables say, renders the views,
removes what the per-build model replaces, and arms builds mode. After it, no backlog status in this
repo is authored anywhere, and the commit carries every edit its own deletions and mode switch make
necessary, so no gate reads a half-switched tree.

## 2. Scope (IN)

- **S1** A `--write` mode of `tools/memory-tree/migrate_backlog.py`, built as a thin driver over
  `TOOL-dDerivedDocket-12`'s delta engine: the whole legacy corpus, live shards and backlog archives
  together, is the delta from an empty base, and the two signed records are the adjudication input.
  It writes each ask row in its id's slug folder, the migration's own step-6 dispositions in the ask
  owner's folder, and the signed triage dispositions in this build's `BACKLOG.md`. Observed by AC1,
  AC2 and AC3.
- **S2** Conservation. Every id the planner's census collected has exactly one ask row, and its text
  equals the legacy text apart from the declared normalizations in §4. Observed by AC2.
- **S3** The family views are rendered by `gen_build_index.py --write` for all four declared
  families, in the same commit. Observed by AC1.
- **S4** `.memory-tree.conf` declares `BACKLOG_MODE="builds"` and an `ASK_CUTOFF` the writer derives
  as the first date strictly after every `filed` date it wrote. Observed by AC4.
- **S5** `.gitattributes` gains `memory/builds/*/BACKLOG.md merge=rows` and KEEPS
  `memory/backlog/*.md merge=rows`, which the row driver's shard-into-view refusal needs.
  Observed by AC5.
- **S6** The three backlog archives are deleted after the conservation proof (owner ruling D8), and
  every carrier outside `memory/` that names one of their basenames is reworded in the same commit,
  because the dead-path gate derives its needles from files git no longer tracks. Observed by AC6.
- **S7** The curation-debt row for `memory/backlog/TOOL.md` is deleted. The view leaves the size
  check (owner ruling D3) and the backlog status check retires in builds mode, so the row would hide
  nothing and the registry's stale-entry guard would red it. Observed by AC7.
- **S8** `.unattended.conf` drops `memory/backlog` from `SHARED_RECORDS` and adds two
  `GENERATED_INDEXES` pairs, one per renderer file. Observed by AC8.
- **S9** Recall's durable-home pattern admits `builds/<slug>/BACKLOG.md`, the recall cache version
  bumps because extraction changed, and the recall floor is measured before and after the switch.
  Observed by AC9.
- **S10** Drift-audit: `backlog_rows_outliving_closed_specs` and its pin retire; the live-rows signal
  is re-pointed at `gen_build_index.py --asks --json` with its watermark re-measured through
  `RATCHETS`; the terminal-status tuple reads the derived output; three report-only signals are
  added, each with a liveness assertion. Observed by AC10.
- **S11** `TOOL-aWeighedCompass-3` is disposed WONTDO, superseded by this unit, in this build's
  `BACKLOG.md` (design §14). Observed by AC11.
- **S12** The kickoff manifest's claims this commit makes stale are updated in the same commit, and
  its `last-audit` is re-stamped, because the manifest's staged leg refuses a watched-file change
  without one. Observed by AC12.
- **S13** Four breaks are staged on the real tree after the switch-over commit, each confirmed RED and
  then removed: V1, the view's data-loss guard, V10 and V13. Observed by AC13.
- **S14** The straggler inventory is taken over every local and remote-tracking ref before the write,
  and recorded. It is report-only; the owner replaced the all-node drain with the permanent
  transition audit. Observed by AC14.
- **S15** The flip's landing reconcile is specified in §4 and rehearsed in this pass against the
  current remote tip, because the landing merge of this build is itself a transition and the rows
  main gains during the build must be carried across it. Observed by AC15.
- **S16** The per-id status report: after the switch, each id's derived status equals the status the
  planner's per-id report predicts under the signed tables. Observed by AC3.

## 3. Non-goals (OUT)

- No adopter migration. Adopters keep the absent-key default, which reads as shards mode.
- No drain of other nodes' branches (owner, 2026-09-14). Stragglers are the transition audit's.
- No relocation of any straggler branch. A run never performs one (design §18 rev-3 A10); the landing
  reconcile in §4 carries only rows the delta engine classifies mechanically and parks the rest.
- No gate run in the unit pass beyond the observations §6 names. The bar runs once, on the landing
  merge, and that bar owes `GATE_FULL=1 GATE_SELFTESTS=1` because this build is kit work.
- No kit or HYGIENE prose beyond the carriers S6 and S12 require. The memory-tree kit README's
  backlog sections, the agent carriers and the backlog dossier are `TOOL-dDerivedDocket-36`'s; the
  charter is `PLAY-dDerivedDocket-1`'s; the runbook is `DEPL-dDerivedDocket-1`'s.
- No `backlog_closeout_pending` drift signal. Design §6 proposed it while the closeout was
  report-only; D6 made the closeout a gate from this commit, so a report-only count of a gated
  population reads zero by construction, which is a probe that cannot move.
- No arming of the ask-driven unattended path. That is `TOOL-dDerivedDocket-35`'s.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-8` — the hygiene engine, id corpus and row grammar in
  builds mode. Without them the switch reds checks 3, 4, 8, 13, 15 and 20 on the first run.
- **consumes-from** `TOOL-dDerivedDocket-9` — the permanent transition audit, which the owner's
  delegation substitutes for the all-node drain, and which treats this build's landing merge as its
  first transition.
- **consumes-from** `TOOL-dDerivedDocket-10` — the row driver's refusal of a shard merged into a
  view, which is what makes the kept attribute worth keeping.
- **consumes-from** `TOOL-dDerivedDocket-11` — the census the conservation proof counts against, and
  the per-id report the status proof compares with. Added by this spec, not in the brief's edge
  table.
- **consumes-from** `TOOL-dDerivedDocket-12` — the delta engine `--write` drives, the provenance row
  shape, and `--stragglers`.
- **consumes-from** `TOOL-dDerivedDocket-15` — verdict V13, which S13 stages on the real tree. Added
  by this spec, not in the brief's edge table.
- **consumes-from** `TOOL-dDerivedDocket-33` — the two signed records, and the signer the landing
  reconcile re-runs.
- **hands-off** `TOOL-dDerivedDocket-35` — a builds-mode tree to arm the ask-driven path against.
- **hands-off** `TOOL-dDerivedDocket-36` — the kit README, agent carriers and backlog dossier that
  describe the switched tree.
- **hands-off** `PLAY-dDerivedDocket-1` — the charter wording the switched tree contradicts.
- **hands-off** `DEPL-dDerivedDocket-1` — the adopter runbook's migrate step and added attribute.
- **hands-off** external — the landing reconcile in §4, which runs at the landing, after the closing
  review and outside any unit pass.

## 4. Design

### What the one commit carries

| Group | Change | Why it cannot wait for a later commit |
|---|---|---|
| records | every `builds/<slug>/BACKLOG.md`, the rendered views, the regenerated README regions | the views are check 9's byte-compare subject from this commit |
| deletions | `memory/archive/TOOL.2026-08-14.md`, `TOOL.2026-08-17.md`, `TOOL.2026-08-17b.md`; the curation-debt row at `memory/project/curation-debt.txt:54` | the archives are second definitions of migrated ids; the debt row would red its stale guard |
| carriers of the deletion | the archive basenames at `.memory-tree.conf:387`, `tools/memory-tree/.memory-tree.conf.example:201`, `tools/memory-tree/check-memory-hygiene.sh:1057`, `tools/memory-tree/README.md:133`, `tools/memory-tree/row_grammar.py:167` and `:630`, reworded to describe the same-day suffix without naming a deleted file | `tools/check-dead-paths.sh` derives its needles from git and reds any carrier outside `memory/` naming them |
| conf | `BACKLOG_MODE`, `ASK_CUTOFF`; the two `.unattended.conf` lines at `.unattended.conf:206` and `:207`; the added attribute line beside `.gitattributes:65` | the mode is what every builds-mode verdict keys on |
| recall | the durable-home alternative beside `tools/memory-recall/extract.py:144`; `CACHE_VERSION` at `tools/memory-recall/query.py:134`; the memory-recall kit version | an old cache would serve anchors from files this commit deletes |
| drift | the pin at `tools/drift-audit/drift_signals.py:260` and its signal retire; the live-rows watermark at `:288` re-measured; `_TERMINAL_STATUSES` at `tools/drift-audit/drift_report.py:1324` reads the derived output; three new signals; the drift-audit kit version | a retired signal left one commit reports a reassuring zero |
| disposal | WONTDO for `TOOL-aWeighedCompass-3`, superseded by this unit | its split-or-shorten call dissolves with the shard |
| manifest | the rotation-union trap at `memory/guides/SESSION-KICKOFF.md:200`, the check-8 trap at `:251`, the pointer-map rows at `:114`-`:117` and the governing-docs line at `:67`, then the re-stamp | the manifest's staged leg refuses a watched-file change without a re-stamp, and the re-stamp asserts the claims were re-verified |

### Conservation — the declared normalizations

An ask's text equals its legacy row's text except for exactly these, each one counted in the
conservation table the writer prints:

1. the status slot removed;
2. the `filed` field inserted, and `unit` where the signed same-id record says so;
3. the declared wrapped-row join (design §9 step 2);
4. a relative link rebased for the file's new depth;
5. NEW HERE: a backticked citation of a backlog archive this commit deletes is rewritten as plain
   text naming the archive and the last commit that tracked it. Measured at BASE, one legacy row
   carries such citations, and it would otherwise sit in a present-corpus `BACKLOG.md` citing a file
   that no longer exists, which check 15 reds against a pin of 0. The writer derives the population
   at flip time rather than trusting this count (§8 F3).

### ASK_CUTOFF — derived, not the flip date

Design §9 step 10 sets `ASK_CUTOFF=<flip date>`. That reds this commit's own output whenever a legacy
row was first seen on the flip date, which this build's own discoveries make likely: verdicts V9, V12
and V14 grade every ask filed on or after the cutoff, and a migrated row carries no severity row, no
clause and no `unit` unless signed. The writer therefore takes the first date strictly after every
`filed` date it wrote, which is the flip date or the day after it, and prints it. The one-day window
in which a new ask could be filed ungraded is stated here rather than implied away (§8 F2).

### The three drift signals added

| Signal | Counts | Liveness |
|---|---|---|
| `backlog_asks_contested` | asks with both closing and declining evidence, and asks whose terminal evidence sits beside a live spec | asks examined > 0 |
| `backlog_evidence_sha` | `by <sha>` evidence the object database does not resolve | shas examined > 0 |
| `backlog_asks_unlabelled` | live asks with no severity row | asks examined > 0 |

Each reads `gen_build_index.py --asks --all --json` and implements no second fold, and each is
report-only.

### Staged REDs, and why they run after the commit

Each break is staged over the COMMITTED switch-over tree and removed with a checkout. Staging one
over the uncommitted switch-over would be unsafe: a checkout restores the whole file, and the
switch-over edits most of the files a break touches.

| Break | Staged as | Expected |
|---|---|---|
| V1 | one ask row moved into a folder that is not its id's slug | `gen_build_index.py --check` names both folders |
| data-loss guard | one authored dash row appended to the TOOL view | `--write` leaves that view untouched, names the line and the ingest remedy, exits 1 |
| V10 | one signed triage disposition removed | `--check` names the ask and its finished build |
| V13 | one ask row given a malformed clause | `--check` names V13 and the row |

Each RED is copied verbatim into the unit's acceptance ledger.

### The landing reconcile

This build lands by an in-place merge of the remote tip into the run branch. The tip is pre-switch
and the branch is post-switch, so that merge is a transition. Whenever the tip's shards moved since
the branch's merge-base, the row driver refuses the shard-into-view merge on each view it touches,
by design. The reconcile is then:

1. take the branch's side of every conflicted view;
2. run the delta engine over the tip's shard delta from the merge-base, which writes each new row as
   an ask in its slug folder, each status flip as a disposition carrying `by <sha>` of the tip commit
   that made it, and a provenance row for every changed row;
3. re-run the signer over the triage population recomputed at the merged tree, so an ask the tip
   added on a finished build is disposed under the same rules;
4. re-render with `gen_build_index.py --write` and confirm the transition audit reads the merge
   accounted.

A row the engine cannot classify mechanically, which is a text amendment of an existing row, stops
the landing with the relocation recipe as a park. That is the design's A10 class, kept.

### Rollout

1. Reground and confirm every consumed unit reads CLOSED.
2. Take the straggler inventory and record it.
3. Measure the recall floor standalone.
4. Run the signer's `--check`, then `migrate_backlog.py --write`.
5. Apply the conf, attribute, recall, drift, deletion, carrier, disposal and manifest changes.
6. Render with `gen_build_index.py --write`, then run `--check`.
7. Confirm the per-id report, the conservation table, the recall floor and `drift_report.py --check`.
8. Commit, with the pre-commit hook's timeout raised to 600000 ms.
9. Stage and remove the four breaks.
10. Rehearse the landing reconcile's classification against the current remote tip, writing nothing.
11. Commit the acceptance ledger and the status flip.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `--write` | CLI mode | `tools/memory-tree/migrate_backlog.py` | a flag, not a function; the function it calls leads with a verb `.lexicon.conf` declares |
| `BACKLOG_MODE`, `ASK_CUTOFF` | conf keys, declared by `TOOL-dDerivedDocket-6` and `-8` | `.memory-tree.conf` | screaming snake, as every key there |
| the three drift signals | signal keys | `tools/drift-audit/drift_report.py` | snake case, as every signal there |
| one added attribute line | git attribute | `.gitattributes` | none |

### Files touched (estimate)

| Path | Change |
|---|---|
| `memory/builds/*/BACKLOG.md` | new, one per slug owning a row, plus this build's |
| `memory/backlog/*.md` | rewritten as generated views |
| `memory/archive/TOOL.*.md` | the three backlog archives deleted |
| `memory/project/curation-debt.txt` | one row deleted |
| `memory/guides/SESSION-KICKOFF.md` | four claims updated, audit block re-stamped |
| `.memory-tree.conf`, `.unattended.conf`, `.gitattributes` | as above |
| `tools/memory-tree/migrate_backlog.py` | `--write` |
| `tools/memory-tree/` carriers | five comment or prose lines reworded |
| `tools/memory-recall/extract.py`, `query.py`, `recall_conf.py` | durable alternative, cache version, kit version |
| `tools/drift-audit/drift_report.py`, `drift_signals.py` | retire, re-point, add, kit version |
| `memory/builds/*/README.md` | generated regions re-rendered |

### Alternatives rejected

- **The drift signals in a unit of their own.** The retirement and the re-point must share this
  commit, and the new signals read the same projection the re-point does. A signal landing one
  commit later leaves the liveness hole design §6 names.
- **`--write` in the planner's unit.** Design §15 makes the planner read-only on the tree, and a
  writer built in one pass and first run in another has no reviewed boundary between them anyway.
  It is a thin driver over the relocation engine, so it adds little new code here.
- **Keeping the archives until a later unit.** They are second definitions of migrated ids, and
  recall would serve their stale statuses (owner ruling D8).
- **Waiving the dead archive citation instead of normalizing it.** `DEAD_PATH_PIN` is 0 and
  shrink-only; raising it is the weakening move the pin exists to refuse.
- **Leaving the kickoff manifest to the docs unit.** The staged leg would take a bare re-stamp, and
  the re-stamp would then assert a re-verification that did not happen (§8 F4).

## 5. Production-readiness checklist

- security — the writer is the one sanctioned cross-folder writer, and only at this commit and its
  landing reconcile. It transfers text owners already wrote and the signed records' rows; it
  executes nothing from any row.
- perf / scale — roughly 600 ids across roughly 90 folders, written once. The pre-commit hygiene run
  over that many new files needs the raised hook timeout.
- error / empty / loading states — the writer refuses on an unsigned or stale signed record (the
  signer's `--check` fails), on an id with no single chosen copy, and on any row it cannot parse. It
  never drops a row.
- observability — the conservation table, the per-id report, the generator's backlog liveness line,
  the straggler inventory, and the three new signals' examined counts.
- risks — the flip lands through a transition merge it cannot fully rehearse, because the tip keeps
  moving. The landing reconcile's classification is rehearsed (AC15), and the rows it cannot classify
  park rather than guess. Between this commit and the landing merge the transition audit reads zero
  transitions on the branch; that is its designed dead-probe state on a builds-mode tree with no
  transition yet, and no bar runs in that window.
- testing — the four staged REDs on the real tree, the conservation and per-id proofs, and the recall
  and drift observations. The kit self-tests are the landing bar's.
- migration — this IS the migration. Rollback is reverting one commit, which restores the shards,
  archives and conf together.
- user docs — the kickoff manifest here; the rest is handed off (§3).

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --check` runs on the switch-over commit,
  it exits 0 and its backlog liveness line reports a non-zero ask count across the tracked
  `memory/builds/*/BACKLOG.md` files and one view per declared family.
  Red when: a family view is missing or stale against its render, which check 9's byte-compare reds.
  cost: seconds.
- **AC2** — When the conservation table `migrate_backlog.py --write` prints is read, the number of ask rows equals the planner
  census's distinct-id count, no id has two ask rows, and every text difference falls in one of the
  five declared normalizations.
  Red when: a row is dropped because it matched no parser shape, which leaves the count one short
  while every surviving row looks correct.
  figure: DERIVED from the census at flip time; design §9's 592 is the 2026-09-13 measurement and is
  not pinned here.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --asks --all --json` runs after the
  switch, every id's derived status equals the planner's predicted status under the signed tables,
  and the comparison prints zero differing ids.
  Red when: a `unit` marker is written for a pair the signed record says `not-unit`, which closes
  that ask through its spec and shows as one differing id.
- **AC4** — When `.memory-tree.conf` is read it declares `BACKLOG_MODE="builds"` and an
  `ASK_CUTOFF` later than every migrated `filed` date, and `gen_build_index.py --check` reports no
  V9, V12 or V14 verdict on a migrated ask.
  Red when: the cutoff equals a date some legacy row was first seen, which reds that row under V12
  for carrying no severity.
- **AC5** — When `git check-attr merge memory/backlog/TOOL.md` and `git check-attr merge` over one
  `memory/builds/*/BACKLOG.md` file run, both read `rows`.
  Red when: the builds line replaces the backlog line instead of joining it, which lets a pre-switch
  branch's shard merge into a view by line merge with nothing refusing it.
- **AC6** — When `git ls-files memory/archive` runs it lists no backlog archive, and
  `bash tools/check-dead-paths.sh` exits 0.
  Red when: a carrier outside `memory/` still names a deleted archive's basename, which the dead-path
  gate derives from git history and reds.
- **AC7** — When `memory/project/curation-debt.txt` is read it carries no row for the TOOL view, and
  `bash tools/memory-tree/check-memory-hygiene.sh` names no stale debt row.
  Red when: the row survives, and the stale-entry guard reds a row that no longer hides a finding.
  cost: minutes, since the hygiene leg is minutes.
- **AC8** — When `.unattended.conf` is read, `SHARED_RECORDS` no longer names `memory/backlog`,
  `GENERATED_INDEXES` pairs it with both renderer files, and `bash tools/unattended/check-unattended.sh`
  reports no path declared under both keys.
  Red when: only the generator is paired, so a pass editing the backlog module never trips the
  generated-index refusal.
  permission: the kit's checks only, which the standing instruction permits; its self-tests are not
  run here.
- **AC9** — When `python3 tools/memory-recall/check-recall.py` runs before and after the switch, the
  floor after is equal or better, and each of the ten fixture ids that were backlog rows resolves to
  a durable anchor under `memory/builds/*/BACKLOG.md`.
  Red when: the durable pattern still admits only one directory level, so those ids lose their
  durable home and the floor drops.
  cost: minutes, for the cache rebuild the version bump forces.
  figure: "ten of twelve" is PINNED as measured 2026-09-14 at BASE against
  `tools/memory-recall/recall-fixture.json`.
- **AC10** — When `python tools/drift-audit/drift_report.py --check` runs after the switch, it exits 0,
  prints no `backlog_rows_outliving_closed_specs` line, and prints an examined count above zero for
  each of `backlog_asks_contested`, `backlog_evidence_sha` and `backlog_asks_unlabelled`.
  Red when: a new signal reads a field the JSON projection does not emit and reports zero examined,
  which its liveness assertion must turn into a DEAD PROBE rather than a clean zero.
- **AC11** — When `python tools/memory-tree/gen_build_index.py --asks TOOL-aWeighedCompass-3` runs, it
  prints WONTDO decided by the superseding disposition in this build's own file.
  Red when: the disposal is written in the ask owner's folder, which is a foreign write outside the
  migration's transferred text.
- **AC12** — When `bash skills/session-kickoff/manifest-check.sh` runs on the switch-over commit, check
  5 passes, and `memory/guides/SESSION-KICKOFF.md` no longer carries the rotation-union trap.
  Red when: the audit block is re-stamped and the stale trap is left, which passes the gate and makes
  the stamp assert a re-verification that did not happen.
- **AC13** — When each break in §4's table is staged over the committed switch-over and the named
  command runs, each exits non-zero with its expected verdict, and after each removal
  `gen_build_index.py --check` exits 0 again.
  Red when: a break is staged over a tree where builds mode is not armed, so the verdict never runs
  and the RED is the mode guard's instead of the verdict's.
- **AC14** — When `migrate_backlog.py --stragglers` runs before the write, it
  prints a refs-examined count above zero, and the inventory is recorded in this unit's journal.
  Red when: only local branches are walked, so a pushed straggler on another node reads as none.
- **AC15** — When the landing reconcile's classification is rehearsed with `migrate_backlog.py`
  against the current remote tip,
  every row the tip changed since the merge-base is classified as new, flipped, already present or
  needing a human, and the record names each one needing a human.
  Red when: a text amendment is classified as a flip, which writes a disposition over another
  session's wording at the landing.
  cost: seconds; it writes nothing. fixture: the remote tip at the moment of the rehearsal, which
  will have moved again by the landing, so this observes the classifier and not the final delta.

## 7. Gates

`memory hygiene` · `recall floor` · `drift-audit records` · `dead-path carriers (deleted files still named)` · `kickoff-manifest ratchet` · `unattended kit gate` · `codebase-map coverage + freshness`

No new gate arm. The verdicts this unit stages are armed by the units that built them; this unit
observes them live on the real tree for the first time.

## 8. Open questions

- **F1** — Where is `--write` built? (a) In the planner's unit. (b) Here, over the relocation engine.
  RESOLVED (agent, 2026-09-14, delegated): (b). Design §15 makes the planner read-only on the tree and
  lists `--write` among this unit's contents.
- **F2** — What is `ASK_CUTOFF`? (a) The flip date, as design §9 step 10 writes. (b) The first date
  after every migrated `filed` date. (a) reds this commit's own output whenever a legacy row was
  first seen on the flip date. RESOLVED (agent, 2026-09-14, delegated): (b), at the stated cost of at
  most one ungraded day.
- **F3** — A migrated ask citing a deleted archive. (a) Keep the archives. (b) Waive the dead path
  and raise its pin. (c) Normalize the citation to plain text naming the archive and its last
  tracking commit. (a) contradicts ruling D8, and (b) is the weakening move a shrink-only pin
  refuses. RESOLVED (agent, 2026-09-14, delegated): (c), as the fifth declared normalization.
- **F4** — Who fixes the kickoff manifest's stale claims? (a) The docs unit, after this one. (b) This
  commit. RESOLVED (agent, 2026-09-14, delegated): (b). The manifest's staged leg requires the
  re-stamp here, and a re-stamp without the re-verification is a false record.
- **F5** — How does this build's own landing carry the rows main gained during it? (a) Park whenever
  the tip's shards moved, reading A10 literally. (b) The reconcile in §4: ingest what classifies
  mechanically, park only on the A10 class. (a) almost certainly parks, and the owner's delegation
  exists so that the switch-over lands in this run. RESOLVED (agent, 2026-09-14, delegated): (b).
- The rulings this unit executes and does not revisit: D1 adopt, D3 no hard view cap, D6 closeout
  gated from this commit, D8 delete the archives, D9 check 15 keeps grading asks, D11-c direct-push
  landing — all RESOLVED (owner, 2026-09-13). The delegated signatures, and the replacement of the
  all-node drain by the permanent transition audit — RESOLVED (owner, 2026-09-14).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.

## 10. Reuse audit

The seam is the index generator's own render path, `tools/memory-tree/gen_build_index.py --write`,
which already renders `memory/LIVE.md` and the ledger shards as generated, byte-compared artifacts;
the views join it as one more artifact per family, and `.unattended.conf` already pairs `memory/LIVE.md`
with that generator, which is the precedent S8 copies. The recorded precedent for retiring an
authored index into a generated one is `TOOL-aMendedLedger-1`, which retired the per-node session
ledger in favour of the generated `LIVE.md`. `python tools/codebase-map/reuse_lookup.py "switch a
memory tree from authored backlog shards to generated views in one commit"` returned name-stem
neighbours only, the codebase map's own reinvention-backlog helpers among them, which are unrelated;
no existing seam performs a switch-over, and the writer is a driver over the relocation engine
rather than a new engine.

Where the design and the source disagree at BASE, re-verified here:

- Design §11 puts the curation-debt row at line 46; it is at line 54.
- Design §9 step 10 says the archives' citing records are frozen and backticked, so deleting them is
  safe. That holds for check 2, but five carriers outside `memory/` name the archive basenames and
  the dead-path gate reds them, and one live backlog row cites two archives in backticks, which
  becomes a check 15 finding once it is an ask (S6; §8 F3).
- `ROTATION_MODE="cut"` now exists (`TOOL-cSpliceWarden-1`), and hygiene check 24 grades rotated
  archives. After the deletion its population is the one decision-log archive, so it stays graded
  rather than going vacuous.
- The recall cache carries a version constant that must bump when extraction changes; the design did
  not mention it.

Recall terms used: `flip BACKLOG_MODE generated view curation-debt rotation archive drift pin recall DURABLE SHARED_RECORDS GENERATED_INDEXES merge=rows`
