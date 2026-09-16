# TOOL-dDerivedDocket-34 — the switch-over: migration applied and the views rendered

**Status:** SPECCED · rev-2 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling+kickoff · order 34

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round1.md) | spec-audit | TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round2.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round2.md) | spec-audit | TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

Switch this repo from authored backlog shards to asks filed per build with generated family views,
in ONE commit that applies the migration exactly as the signed tables say, renders the views,
removes what the per-build model replaces, and arms builds mode. After it, no backlog status in this
repo is authored anywhere, and the commit carries every edit its own deletions and mode switch make
necessary, so no gate reads a half-switched tree.

## 2. Scope (IN)

- **S1** A `--write` mode of `tools/memory-tree/migrate_backlog.py`,
  `--write --as <slug> --signed <same-id record> <triage record> [--triage-ask <id>]`, built as a
  thin driver over `TOOL-dDerivedDocket-12`'s engine in its migration set (unit 12 §4). The whole
  legacy corpus, live shards and backlog archives together, is the delta from an empty base, and the
  two signed records are the adjudication input. It writes each ask row in its id's slug folder, with
  `filed` taken by unit 12's rule over the full history of the shard and archive paths. It writes
  the migration's own step-6 dispositions in the ask owner's folder, and each hold naming no id (unit
  11 S7's test) as a hold on the `--triage-ask` id. In the `--as` folder, which for this build is
  `memory/builds/dDerivedDocket/BACKLOG.md`, it files the triage ask with its KEEP (S17) and the
  signed triage dispositions. After the conservation proof passes, and only then, it removes the
  authored shard files from the worktree and the index, so the first builds-mode render writes the
  views into absent paths (§4 Rollout, §8 F9). Its refusals are §5's, each observed by AC17. Observed
  by AC1, AC2, AC3, AC16, AC18 and AC19.
- **S2** Conservation. Every id the planner's census collected has exactly one ask row, and its text
  equals the legacy text apart from the declared normalizations in §4. Observed by AC2.
- **S3** The family views are rendered by `gen_build_index.py --write` for all four declared
  families, in the same commit. Observed by AC1.
- **S4** `.memory-tree.conf` declares `BACKLOG_MODE="builds"` and an `ASK_CUTOFF` the writer derives
  as the first date strictly after every `filed` date it wrote. The landing reconcile moves it by the
  same rule (§4). Observed by AC4 and AC15.
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
  Observed by AC9 and AC23.
- **S10** Drift-audit: `backlog_rows_outliving_closed_specs` and its pin retire; the live-rows signal
  is re-pointed at `gen_build_index.py --asks --json` with its watermark re-measured through
  `RATCHETS`; the terminal-status tuple reads the derived output; three report-only signals are
  added, each with a liveness assertion. Under `shards` the live-rows signal keeps reading the
  authored shards, and the three new signals report not-asked with `gateable: False`, as
  `signal_closed_specs_untraceable` does; they also report not-asked while no `BACKLOG.md` is
  tracked. One `memory/DECISIONS.md` row under the TOOL heading, keyed by this unit's id, records
  that `unit` and `advances` supersede DEPL-dGaugedVintage-13's stance ("COUNTED, NEVER REFUSED"),
  citing design §4.4. Observed by AC10, AC21 and AC22.
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
- **S15** The flip's landing reconcile is specified in §4 and rehearsed in this pass, in a scratch
  repository shaped as the landing and against the current remote tip. The landing merge is a
  transition whenever the tip's lineage carries a shards-mode backlog commit since the fork (unit 9
  S3's predicate), and the rows main gains during the build, with the triage its finished builds now
  owe, must be carried across it. Observed by AC15 and AC20.
- **S16** The per-id status report: after the switch, each id's derived status equals the status the
  planner's per-id report predicts under the signed tables. Observed by AC3.
- **S17** The triage ask. The orchestrator mints `<triage-id>` at this pass (charter §2: a fan-out
  child never mints) and records it in the pass's journal line before `--write` runs. The writer
  files it in this build's `BACKLOG.md` with `filed` set to the commit's day and text naming every
  legacy hold that named no id, beside
  `- KEEP · <triage-id> · awaits the owner's triage of <n> legacy holds that named no id`. Every such
  hold is written on it. It stays live at this build's close, where the KEEP satisfies V10 and unit
  35 S9. Given with zero such holds, the writer files nothing and prints `triage ask: 0 holds`.
  Observed by AC16.

## 3. Non-goals (OUT)

- No adopter migration. Adopters keep the absent-key default, which reads as shards mode.
- No drain of other nodes' branches (owner, 2026-09-14). Stragglers are the transition audit's.
- No relocation of any straggler branch. A run never performs one (design §18 rev-3 A10); the landing
  reconcile in §4 carries only entries the delta engine classifies mechanically, confirms only ids
  the receiving branch never acted on since the fork, and parks the rest with the recipe.
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

- **consumes-from** `TOOL-dDerivedDocket-6` — the `unit` and `advances` model, whose supersession
  of the stance DEPL-dGaugedVintage-13 recorded is what S10's DECISIONS row records.
- **consumes-from** `TOOL-dDerivedDocket-7` — `gen_build_index.py --write`, `--check` and
  `--asks --json`, which S3, S10, AC1 and AC3 run, and the data-loss guard, which S1 satisfies by
  removing the authored shards before the first render.
- **consumes-from** `TOOL-dDerivedDocket-8` — the hygiene engine, id corpus and row grammar in
  builds mode. Without them the switch reds checks 3, 4, 8, 13, 15 and 20 on the first run.
- **consumes-from** `TOOL-dDerivedDocket-9` — the permanent transition audit, which the owner's
  delegation substitutes for the all-node drain, and which audits this build's landing merge
  whenever the tip's lineage carries a shards-mode backlog commit since the fork (its S3 predicate).
- **consumes-from** `TOOL-dDerivedDocket-10` — the row driver's refusal of a shard merged into a
  view, which is what makes the kept attribute worth keeping.
- **consumes-from** `TOOL-dDerivedDocket-11` — the census the conservation proof counts against, and
  the per-id report the status proof compares with, and the placeholder `TRIAGE-ASK`, for which
  S17's id is substituted in AC3; and `--plan` over a worktree of the remote tip, which reconcile
  step 2 runs (its S1). Added by this spec, not in the brief's edge table.
- **consumes-from** `TOOL-dDerivedDocket-12` — the delta engine in its migration set (the owner's
  folder for transferred tokens, the `--as` folder for signed triage verdicts, a hold on the
  `--triage-ask` id for a hold naming no id), the provenance row shape, the landing form of
  `--ingest` the reconcile runs, and `--stragglers`.
- **consumes-from** `TOOL-dDerivedDocket-15` — verdict V13, which S13 stages on the real tree. Added
  by this spec, not in the brief's edge table.
- **consumes-from** `TOOL-dDerivedDocket-20` — the two-key refusal AC8 reads; without it AC8 passes by
  absence.
- **consumes-from** `TOOL-dDerivedDocket-33` — the two signed records, and the signer's landing
  re-run (its S11), which reconcile step 3 runs over the worksheets step 2 recomputes at the tip.
- **hands-off** `TOOL-dDerivedDocket-35` — a builds-mode tree to arm the ask-driven path against, and
  the triage ask with its KEEP, which unit 35 S9's read lists.
- **hands-off** `TOOL-dDerivedDocket-36` — the kit README, agent carriers and backlog dossier that
  describe the switched tree.
- **hands-off** `PLAY-dDerivedDocket-1` — the charter wording the switched tree contradicts.
- **hands-off** `DEPL-dDerivedDocket-1` — the adopter runbook's migrate step and added attribute, and
  the argument shape S1 pins for `--write`, which the runbook's switch step spells.
- **hands-off** external — the landing reconcile in §4, which runs at the landing, after the closing
  review and outside any unit pass; its verb is unit 12's landing form of `--ingest`.

## 4. Design

### What the one commit carries

| Group | Change | Why it cannot wait for a later commit |
|---|---|---|
| records | every `builds/<slug>/BACKLOG.md`, the rendered views, the regenerated README regions; the authored shard bodies removed by the writer before the views are rendered at their paths | the views are check 9's byte-compare subject from this commit |
| deletions | `memory/archive/TOOL.2026-08-14.md`, `TOOL.2026-08-17.md`, `TOOL.2026-08-17b.md`; the curation-debt row at `memory/project/curation-debt.txt:54` | the archives are second definitions of migrated ids; the debt row would red its stale guard |
| carriers of the deletion | the archive basenames at `.memory-tree.conf:387`, `tools/memory-tree/.memory-tree.conf.example:201`, `tools/memory-tree/check-memory-hygiene.sh:1057`, `tools/memory-tree/README.md:133`, `tools/memory-tree/row_grammar.py:167` and `:630`, reworded to describe the same-day suffix without naming a deleted file | `tools/check-dead-paths.sh` derives its needles from git and reds any carrier outside `memory/` naming them |
| conf | `BACKLOG_MODE`, `ASK_CUTOFF`; the two `.unattended.conf` lines at `.unattended.conf:206` and `:207`; the added attribute line beside `.gitattributes:65` | the mode is what every builds-mode verdict keys on |
| recall | the durable-home alternative beside `tools/memory-recall/extract.py:144`; `CACHE_VERSION` at `tools/memory-recall/query.py:134`; the memory-recall kit version | an old cache would serve anchors from files this commit deletes |
| drift | the pin at `tools/drift-audit/drift_signals.py:260` and its signal retire; the live-rows watermark at `:288` re-measured; `_TERMINAL_STATUSES` at `tools/drift-audit/drift_report.py:1324` reads the derived output; three new signals; the drift-audit kit version; the DECISIONS row recording the supersession | a retired signal left one commit reports a reassuring zero |
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

The landing reconcile re-applies this rule over the union of rows the writer and the reconcile
transferred: unit 12's landing form prints the later of the current value and the first date
strictly after every `filed` date it wrote, and reconcile step 5 writes that into `.memory-tree.conf`
in the landing merge. Rows main filed in the window are legacy rows, which D7's forward-only rule
already exempts. The ungraded window F2 accepted, at most one day, therefore becomes the span from
the switch-over commit to the landing, for asks filed on main or on this branch in it (§8 F10).

### The three drift signals added

| Signal | Counts | Liveness |
|---|---|---|
| `backlog_asks_contested` | asks with both closing and declining evidence, and asks whose terminal evidence sits beside a live spec | asks examined > 0 |
| `backlog_evidence_sha` | `by <sha>` evidence the object database does not resolve | shas examined > 0 |
| `backlog_asks_unlabelled` | live asks with no severity row | asks examined > 0 |

Each reads `gen_build_index.py --asks --all --json` and implements no second fold, and each is
report-only. Under `shards` the live-rows signal keeps reading the authored shards, and the three new
signals report not-asked with `gateable: False`, as `signal_closed_specs_untraceable` does; they also
report not-asked while no `BACKLOG.md` is tracked (S10, AC21).

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
and the branch is post-switch, so that merge is a transition whenever the tip's shards moved since
the fork (unit 9 S3). Whenever the tip's shards moved since the branch's merge-base, the row driver
refuses the shard-into-view merge on each view it touches, by design.

The reconcile's verb is unit 12's LANDING FORM of `--ingest` (its S6). It is admitted only when
`<tip>` is the resolved default tip, resolved as that unit's straggler inventory resolves it (the
observed `origin/HEAD` wins), when that tip's `.memory-tree.conf` blob reads shards, and when HEAD's
reads builds. It needs no MERGE_HEAD: during a conflicted merge the tip is MERGE_HEAD, and after a
clean one it is HEAD^2, and every step names it by sha. It takes unit 9's no-merge
`delta(ours=HEAD, theirs=<tip>)` (its S13), writes only per-build files, runs the migration set and
prints the re-derived cutoff. The reconcile is then:

1. `push-main.sh --prepare` merges the tip in place. When the tip's shards or backlog archives moved
   since the fork, the row driver refuses on each view and the merge stops conflicted. Take the
   branch's side of every conflicted view path and every backlog-archive path.
2. Plan at the tip. Run `git worktree add --detach <scratch> <tip>`, then run the branch's
   `migrate_backlog.py --plan --record <run-tree>/memory/builds/dDerivedDocket/build --record-as TOOL-dDerivedDocket-34`
   inside that worktree, then remove the worktree.
3. Sign. Run the signer's landing re-run (unit 33 S11) over that worksheet pair with its landing
   tail; its `--check` exits 0.
4. Ingest. Run
   `migrate_backlog.py --ingest <tip> --as dDerivedDocket --signed <landing same-id record> <landing triage record> --triage-ask <triage-id>`
   with `--dry-run`, and confirm per the rule below. Any park condition stops the landing with the
   recipe; otherwise re-run without `--dry-run`.
5. Write the `ASK_CUTOFF` the ingest printed into `.memory-tree.conf` (§4 "ASK_CUTOFF").
6. Run `gen_build_index.py --write`, then `--check`, which exits 0 with no V6, V9, V10, V12 or V14.
   Conclude the merge, or commit the follow-up after a clean merge. Check 25 reads the merge
   accounted when it is a transition, and prints `transitions examined 0` when the tip's shards did
   not move.

A moved tip is re-reconciled from step 1. Every step is idempotent, because accounted entries and
already-disposed ids plan nothing.

**Confirmation, with design A6 kept rather than relaxed.** Unit 12 S5 is unchanged: every
status-changing record needs `--confirm <id>`. The reconcile passes `--confirm` for exactly the
CONFIRM-listed ids that the receiving branch never acted on since the fork, which means two things
hold for the id. First, its legacy row at the switch-over commit's first parent equals its row at
the merge-base, so there was no pre-switch branch edit. Second, no line added on the branch after
the switch-over commit names it. Any other CONFIRM id parks the landing with the recipe, the design
A10 class, and so does every NEEDS-HUMAN entry: a text amendment, a flip to a live token from a
terminal one, or a planned record colliding with an existing record for its target in its file.
This squares with lab case e09b, which overwrote a deliberate act on the RECEIVING side after the
fact: this rule never confirms an id the receiving side acted on (§8 F7).

### Rollout

1. Reground and confirm every consumed unit reads CLOSED.
2. Take the straggler inventory and record it.
3. Measure the recall floor standalone.
4. Mint `<triage-id>` and record it in the pass journal (S17).
5. Run the signer's `--check`, gov's operator step, then
   `migrate_backlog.py --write --as dDerivedDocket --signed <signed same-id record> <signed triage record> --triage-ask <triage-id>`;
   the writer re-checks staleness itself (§5), and it removes the authored shard files after its
   conservation proof, so the render step writes the views into absent paths.
6. Apply the conf, attribute, recall, drift, deletion, carrier, disposal and manifest changes.
7. Render with `gen_build_index.py --write`, then run `--check`.
8. Confirm the per-id report, the conservation table, the recall floor and `drift_report.py --check`.
9. Commit, with the pre-commit hook's timeout raised to 600000 ms.
10. Stage and remove the four breaks.
11. Rehearse the landing reconcile (AC15 in scratch, AC20 against the live tip).
12. Commit the acceptance ledger and the status flip.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `--write` | CLI mode | `tools/memory-tree/migrate_backlog.py` | a flag, not a function; the function it calls leads with a verb `.lexicon.conf` declares |
| `--as`, `--signed`, `--triage-ask` | options of `--write` | `tools/memory-tree/migrate_backlog.py` | flags |
| `<triage-id>` | the minted triage ask | `memory/builds/dDerivedDocket/BACKLOG.md` | an id of the TOOL family, never a literal in this spec |
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
| `tools/memory-tree/migrate_backlog.py` | `--write`, and its selftest's `--write` fixtures |
| `tools/memory-tree/` carriers | five comment or prose lines reworded |
| `tools/memory-recall/extract.py`, `query.py`, `recall_conf.py` | durable alternative, cache version, kit version |
| `tools/drift-audit/drift_report.py`, `drift_signals.py` | retire, re-point, add, kit version |
| `tools/drift-audit/selftest.py` | the shards-mode and dead-probe fixtures AC21 runs |
| `memory/DECISIONS.md` | one row under the TOOL heading |
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
- error / empty / loading states — the writer refuses when a signed record's header does not name
  the tracked worksheet's current blob sha; when that worksheet's data rows differ from what
  `--plan`'s own functions compute at this tree; when a header cell `Ask`, `Verdict` or `Field` is
  missing; on an id with no single chosen copy; on any row it cannot parse; when `--triage-ask` is
  missing while a hold names no id, naming those holds; on a `--triage-ask` id whose slug is not
  `--as`'s; and on a `--triage-ask` id equal to a spec H1. Each check is kit-local, so an adopter
  without the signer gets the same refusal. It never drops a row.
- observability — the conservation table, the per-id report, the generator's backlog liveness line,
  the straggler inventory, the three new signals' examined counts, and the landing triage
  population's size, printed by the rehearsal (AC20).
- risks — the flip lands through a merge it cannot fully rehearse, because the tip keeps moving. The
  landing reconcile is rehearsed (AC15 in scratch, AC20 against the live tip), and the entries it
  cannot classify or confirm park rather than guess. Between this commit and the landing merge,
  check 25 prints `transitions examined 0` and passes, because the switch-over commit is a mode
  boundary (unit 9 S7); any DEAD PROBE there is a real fault, such as the two conf readers
  disagreeing. No bar runs in that window.
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
- **AC2** — When the conservation table `migrate_backlog.py --write` prints is read, the number of ask
  rows equals the planner census's distinct-id count, plus one when the writer filed the triage ask,
  no id has two ask rows, and every text difference falls in one of the five declared normalizations.
  Red when: a row is dropped because it matched no parser shape, which leaves the count one short
  while every surviving row looks correct.
  figure: DERIVED from the census at flip time; design §9's 592 is the 2026-09-13 measurement and is
  not pinned here.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --asks --all --json` runs after the
  switch, every id's derived status and hold target equal the planner's prediction under the signed
  tables, with `<triage-id>` substituted for `TRIAGE-ASK`, and the comparison prints zero differing
  ids.
  Red when: a `unit` marker is written for a pair the signed record says `not-unit`, which closes
  that ask through its spec and shows as one differing id.
- **AC4** — When `.memory-tree.conf` is read on the switch-over commit it declares
  `BACKLOG_MODE="builds"` and an `ASK_CUTOFF` equal to the day after the latest `filed` date over
  every ask row in the tree, recomputed from the written `BACKLOG.md` rows independently of the
  writer's printout, and `gen_build_index.py --check` reports no V9, V12 or V14 verdict on a migrated
  ask.
  Red when: the cutoff is any later date, which silently disarms V9, V12 and V14 for every new ask,
  or equals a date some legacy row was first seen, which reds that row under V12.
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
  `records` floor after is equal or better.
  Red when: the switch loses a backlog-row fixture id's record, which drops the floor.
  cost: minutes, for the cache rebuild the version bump forces.
- **AC10** — When `python tools/drift-audit/drift_report.py --check` runs after the switch, it exits 0,
  prints no `backlog_rows_outliving_closed_specs` line, and prints an examined count above zero for
  each of `backlog_asks_contested`, `backlog_evidence_sha` and `backlog_asks_unlabelled`; the
  live-rows signal's reading equals the count of live asks in `gen_build_index.py --asks --json`,
  which also shows the terminal-status tuple reading the derived output.
  Red when: a new signal reads a field the JSON projection does not emit and reports zero examined;
  AC21 stages that zero and observes the DEAD PROBE.
- **AC11** — When `python tools/memory-tree/gen_build_index.py --asks TOOL-aWeighedCompass-3` runs, it
  prints WONTDO decided by the superseding disposition in this build's own file.
  Red when: the disposal is written in the ask owner's folder, which is a foreign write outside the
  migration's transferred text.
- **AC12** — When `bash skills/session-kickoff/manifest-check.sh` runs on the switch-over commit, check
  5 passes, and `memory/guides/SESSION-KICKOFF.md` carries none of the four BASE strings §4's
  manifest row names: the rotation-union trap at `:200`, the check-8 trap at `:251`, the pointer-map
  rows at `:114`-`:117` and the governing-docs line at `:67`, each grepped by its BASE text.
  Red when: the audit block is re-stamped and the stale trap is left, which passes the gate and makes
  the stamp assert a re-verification that did not happen.
- **AC13** — When each break in §4's table is staged over the committed switch-over and the named
  command runs, each exits non-zero with its expected verdict, and after each removal
  `gen_build_index.py --check` exits 0 again.
  Red when: a break is staged over a tree where builds mode is not armed, so the verdict never runs
  and the RED is the mode guard's instead of the verdict's.
- **AC14** — When `migrate_backlog.py --stragglers --tsv` and `--stragglers --local --tsv` run before
  the write, the default run's `examined` count exceeds the `--local` run's while
  `git for-each-ref refs/remotes` lists at least one ref, and the inventory is recorded in this
  unit's journal.
  Red when: only local branches are walked, so a pushed straggler on another node reads as none.
- **AC15** — When the landing reconcile's six steps run to completion in a scratch repository holding
  a builds-mode branch (after its own switch-over) and a shards-mode default tip carrying one new ask
  homed on a finished build and filed after the branch's cutoff, one flip to CLOSED of an untouched
  id, one flip of an id the branch REOPENed after its switch-over, and one text amendment, the
  reconcile parks naming the amendment and the REOPENed id with the recipe and writes nothing. With
  those two removed it completes: `gen_build_index.py --check` exits 0 with no V6, V9, V10, V12 or
  V14, the flip is a CLOSED disposition in its owner's folder, the new ask carries a signed triage
  disposition in the `--as` file, `ASK_CUTOFF` is the day after the new ask's `filed`, and check 25
  reads the merge accounted.
  Red when: a step is skipped — each is staged skipped in turn — or step 4 names `--relocate`, which
  exits 2 on the shards-mode tip.
  cost: minutes. fixture: a scratch repository built in the pass; it writes nothing outside it.
- **AC16** — When `python tools/memory-tree/gen_build_index.py --asks <triage-id>` runs on the
  switch-over commit, it prints the ask with its KEEP in this build's `BACKLOG.md`,
  `--asks --all --json` shows every legacy hold that named no id held on it, and
  `grep -c TRIAGE-ASK memory/builds/*/BACKLOG.md` prints 0 for every file.
  Red when: the placeholder is written verbatim, which reds V6 and fails AC1.
- **AC17** — When `migrate_backlog.py --selftest` runs its `--write` fixtures — a signed record whose
  worksheet was edited after signing, a worksheet stale against a shard that gained a row after
  planning, two live copies of one id, and one unparseable row — each writes nothing, leaves
  `git status --porcelain` unchanged and exits non-zero naming its cause.
  Red when: staleness is judged by the signer's `--check`, a build-folder script an adopter does not
  have, so an adopter's `--write` applies a stale record.
  cost: one kit selftest run; it is held, so it binds at the landing bar under `GATE_SELFTESTS=1`,
  and each arm's RED is observed by hand in the pass.
- **AC18** — When `python tools/memory-tree/gen_build_index.py --asks --all --json` runs on the
  switch-over commit, every row of the signed triage record outside its exclusions list is decided by
  a disposition in this build's `BACKLOG.md`, and no other `BACKLOG.md` under `memory/builds/`
  carries a disposition row naming a triage-record id (triage ids carry no step-6 rows by
  construction, because the triage population derives OPEN after step 6).
  Red when: the engine writes the triage rows into the ask owners' folders, the one-writer breach
  unit 33 §8 F4 rejected; AC1 to AC3 stay green, because the closeout accepts any file.
- **AC19** — When `git ls-files memory/backlog` runs between the `--write` step and the render step,
  it lists nothing, and the render step's `gen_build_index.py --write` exits 0 with all four views
  written.
  Red when: the writer leaves a shard in place, so the guard reads its 460 id-leading lines and the
  flip's render exits 1 with every view unwritten.
- **AC20** — When the reconcile's step 4 runs with `--dry-run` against the current remote tip, it
  prints a non-zero classified count, each entry as new, flipped, CONFIRM, already present or
  NEEDS-HUMAN, the size of the landing triage population steps 2 and 3 compute, and the
  `ASK_CUTOFF` it would write.
  Red when: a text amendment is classified as a flip, which writes a disposition over another
  session's wording at the landing.
  cost: minutes; it writes nothing. fixture: the remote tip at the moment of the rehearsal, which
  will have moved again by the landing, so this observes the classifier and not the final delta.
- **AC21** — When `python tools/drift-audit/selftest.py` runs, a shards-mode fixture reads its
  live-rows count from the shards and prints the three new signals as not-asked with no DEAD PROBE
  line, and a builds-mode fixture whose `--asks --json` projection lacks each new signal's field in
  turn prints that signal's DEAD PROBE.
  Red when: the re-point reads `--asks --json` under shards, so every shards-mode adopter loses its
  live-rows count and prints four DEAD PROBE lines while `--check` stays green.
- **AC22** — When `memory/DECISIONS.md` is read on the switch-over commit, its TOOL heading carries
  one row keyed `TOOL-dDerivedDocket-34` that names DEPL-dGaugedVintage-13 as superseded, cites
  design §4.4, and fits the entry budget.
  Red when: the signal and its pin retire with no row, so a ratified stance is superseded without
  the new id and note charter §6 requires.
- **AC23** — When `python3 tools/memory-recall/extract.py` runs before and after the switch, its
  `(durable home: <n>)` figure after is not below the figure before, and its spine includes the
  `memory/builds/*/BACKLOG.md` files; each of the ten fixture ids that were backlog rows resolves to
  a durable anchor under them.
  Red when: the durable pattern still admits only one directory level, so the migrated ids lose
  their durable home, which the `records` floor cannot see because `DURABLE` selects only the spine
  (`tools/memory-recall/extract.py:674`).
  figure: "ten of twelve" is PINNED as measured 2026-09-14 at BASE against
  `tools/memory-recall/recall-fixture.json`.

## 7. Gates

`memory hygiene` · `recall floor` · `drift-audit records` · `dead-path carriers (deleted files still named)` · `kickoff-manifest ratchet` · `unattended kit gate` · `codebase-map coverage + freshness` · `drift-audit selftest`

New arm: `python3 tools/memory-tree/migrate_backlog.py --selftest` on the `backlog migration selftest` leg `TOOL-dDerivedDocket-11` adds · `--write` fixtures for each §5 refusal, the triage ask's filing and refusals, and the shard removal · the selftest's floor moves in the same commit
New arm: `python tools/drift-audit/selftest.py` on the `drift-audit selftest` leg · the shards-mode fixture and one builds-mode fixture per new signal with its field removed (AC21) · none; it is a held kit leg, so it runs at the landing bar under `GATE_SELFTESTS=1`

The verdicts this unit stages are armed by the units that built them; this unit observes them live on
the real tree for the first time.

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
  exists so that the switch-over lands in this run. RESOLVED (agent, 2026-09-14, delegated): (b), and
  F7 names the verb and the confirmation rule.
- **F6** — Who mints, files and closes out the one triage ask design §9 step 6 names? (a) The
  orchestrator mints it, `--write --triage-ask` files it with a KEEP, and every hold naming no id is
  written on it. (b) The session hand-files it before `--write`. (c) The closing pass writes its
  KEEP. (b) and (c) are manual steps no AC sees before the flip. RESOLVED (agent, 2026-09-14,
  delegated): (a).
- **F7** — Which ids does the reconcile confirm, and how does that square with design A6? (a) Every
  CONFIRM-listed entry, since each change commit is on the tip. (b) Only ids the receiving branch
  never acted on since the fork: the legacy row unchanged from the merge-base to the switch-over's
  parent, and no line added after the switch-over naming it. (a) re-opens lab case e09b on the
  receiving side. RESOLVED (agent, 2026-09-14, delegated): (b); every other CONFIRM id parks with the
  recipe, so A6's protection is restated, not relaxed. The verb is unit 12's landing form of
  `--ingest` (its §8 F7).
- **F8** — How is the triage a tip-added or newly finished ask owes at the landing produced and
  written? (a) The planner at the tip in a scratch worktree, the signer's landing re-run, and
  `--ingest --signed` writing each verdict not already disposed. (b) The signer over the merged
  tree's JSON projection. (c) Park when non-empty. Measured for the G5 audit: 61 of 64 asks main
  filed in seven days sit on finished builds, so (c) parks the routine landing. RESOLVED (agent,
  2026-09-14, delegated): (a).
- **F9** — How does the first builds-mode render meet a guard that reads every file at a view path?
  (a) The writer removes the authored shards after its conservation proof. (b) A one-time flag the
  guard honours. (c) A hand `git rm` in the rollout. (b) is a new generator surface and a standing
  bypass of the guard; (c) is a step an adopter can miss. RESOLVED (agent, 2026-09-14, delegated):
  (a).
- **F10** — Does the landing reconcile move `ASK_CUTOFF`? (a) Yes, by S4's rule over the union of
  transferred rows. (b) An exemption for reconciled rows honoured by units 6 and 15. (c) No. (b) is
  new grammar in two other units; (c) reds V9, V12 and V14 at the landing bar on every row main
  filed after the switch-over day. RESOLVED (agent, 2026-09-14, delegated): (a), at the stated cost
  of an ungraded window as long as the build's span.
- **F11** — What makes a signed record stale to `--write`? (a) The signer's `--check` failing, as
  rev-1. (b) The record's header naming a worksheet blob other than the tracked one. (c) (b), plus
  the tracked worksheet's rows differing from what `--plan` computes at this tree. (a) is a
  build-folder script adopters do not have and cannot run inside the writer; (b) misses a corpus that
  moved after planning. RESOLVED (agent, 2026-09-14, delegated): (c).
- **F12** — Which unit writes the DECISIONS row design §4.4 owes for superseding the stance that
  the record DEPL-dGaugedVintage-13 took? (a) Unit 6, which builds the replacing model. (b) This
  unit, which retires the signal. Under (a) the row would claim a supersession while the stance is still
  enforced, for every unit up to this one. RESOLVED (agent, 2026-09-14, delegated): (b).
- The rulings this unit executes and does not revisit: D1 adopt, D3 no hard view cap, D6 closeout
  gated from this commit, D8 delete the archives, D9 check 15 keeps grading asks, D11-c direct-push
  landing — all RESOLVED (owner, 2026-09-13). The delegated signatures, and the replacement of the
  all-node drain by the permanent transition audit — RESOLVED (owner, 2026-09-14).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.
- rev-2 · 2026-09-14 · spec-audit G2, G3 and G5 round 1 fold. G2 B1 (2, 41), G2 B2 (23, 43) and G5
  B1 (13, 31): S1 pins `--write --as --signed [--triage-ask]` over unit 12's migration set, new S17
  mints and files the triage ask with a KEEP and holds each unnamed hold on it, §4 Rollout and
  Inventory, §5 refusals, AC2, AC3 with the `TRIAGE-ASK` substitution, AC16; §8 F6; hands-off 35
  names the ask. G2 B3 (42) with G5 B2 (14, 32, 58): §4 "The landing reconcile" runs unit 12's
  landing form of `--ingest` in six steps and confirms only ids the receiving branch never acted on
  since the fork; S15, §3 Non-goals, AC15 rewritten to run to completion, AC20 the live-tip
  rehearsal; §8 F7, F5's mark names it. G5 B3 (34): steps 2 and 3 plan at the tip and run the
  signer's landing re-run, consumes-from 11 and 33 name them, §5 observability; §8 F8. G2 H3 (55):
  S1 removes the authored shards before the first render, consumes-from 7 added, AC19; §8 F9. G5 H1
  (33) and M21 (17): the landing moves `ASK_CUTOFF` (S4, §4), widening the ungraded window to the
  build's span, and AC4 pins the cutoff exactly; §8 F10. G5 M3 (16): §5 refusals judged kit-locally,
  AC17, §7's `--write` arm; §8 F11. G5 M4 (60): S10 and §4 keep shards mode, AC21, §7 gains
  `drift-audit selftest`. G2 M6 (49) with G5 M5 (35): the landing merge is a transition only when
  the tip's shards moved (unit 9 S3), consumes-from 9 and §5 risks restate the zero-transition
  window as the honest `examined 0`. G2 M9 (72) with G5 M6 (69): S10's DECISIONS supersession row,
  consumes-from 6 added, AC22; §8 F12. G5 M2 (15, 37): AC18 grades the triage home. G5 M22 (18):
  AC14 compares the remote-ref walk with `--local`. G5 M23 (19): AC10 reads the live-rows count and
  the terminal tuple. G5 M24 (59): AC9 split, AC23 grades the durable home. G5 L2 (21): AC12 greps
  all four manifest claims. G3 M6 (42): consumes-from unit 20, the two-key refusal AC8 reads.

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
