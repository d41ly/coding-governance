# TOOL-dDerivedDocket-11 — migration planner

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

Before any shard is rewritten, someone has to know exactly what the migration will do to every id:
which copy of it survives, which legacy pairs are one subject, which open asks on finished builds
need a disposition, and what each id's status will be afterwards. Build that knowledge as a
read-only planner, `migrate_backlog.py --plan`, that reads every legacy row, refuses to certify a
corpus it cannot fully read, and files the census, the same-id worksheet, the triage worksheet and a
per-id status prediction as records the delegated signer signs and the switch-over applies exactly.

## 2. Scope (IN)

- **S1** A new memory-tree kit module, `migrate_backlog.py`, beside the generator in the kit
  directory it derives from its own location. This unit creates it with `--plan` and `--selftest`;
  the relocation and switch-over units add their modes to it. `--plan` reads only the repo it runs
  in, through that repo's own conf, so an adopter's deployer build runs it unchanged. It writes
  nothing unless `--record` names a directory, and then writes only there. Observed by AC8 and AC9.
- **S2** The permissive legacy parser. It reads every line of every live shard and every family-stem
  backlog archive, joins a declared wrapped row (an indented continuation beneath a row), and passes
  each logical row to the parser unit's one-line legacy reader. A line that is row-shaped and reads
  as nothing is reported by file and line, and `--plan` then exits 1 and files no worksheet. It never
  drops a row and never guesses a status. Observed by AC1.
- **S3** The census. One copy per id: a live copy beats an archived one, and among archived copies a
  terminal one beats a non-terminal one. Two live copies of one id are a blocker, because
  conservation would need two asks. It also derives: the distinct-id count, the slugs owning rows,
  the slugs owning rows with no build README (the prospective filing homes), each slug's prospective
  `BACKLOG.md` size against the row cap `INDEX_CAP_BYTES` declares, and the rows whose text cites a
  backlog archive by path. Observed by AC1 and AC7.
- **S4** The same-id worksheet (owner ruling D2). One row per census id that equals a spec H1: the
  spec path, the legacy token, an evidence class — `specced-in-place`, `born-in-spec-commit` or
  `none` — with the sha that shows it, and a low-overlap flag with its score. The planner proposes
  nothing: the signer decides `unit` under its own rules. Observed by AC3.
- **S5** The triage worksheet (owner ruling D6). The population is every ask deriving OPEN on a build
  whose derived status is terminal, computed under D2's default of no `unit` and after the
  migration's own dispositions. Each row carries the ask's home, its source line, its legacy token,
  its derived status, a proposal with its evidence and basis, and a dead-pointer flag. Observed by
  AC4.
- **S6** Proposals are selected, never decided. A proposal cites a spec other than the ask's same-id
  spec whose body carries a closing phrase naming the ask, a commit whose message names the ask and
  which neither filed the row nor touched only the memory tree, or a hold target the row's own text
  names. A same-id spec is NEVER proposed as closing evidence, because that is D2's question, and the
  triage must not answer it a second way. Observed by AC4.
- **S7** The migration's own dispositions, previewed. For every id the planner computes the records
  the switch-over's writer will put in the owner's folder: a terminal legacy token becomes a terminal
  disposition, a hold naming an id becomes that hold, and a hold naming none becomes a hold on the
  one triage ask the switch-over files, written as the placeholder `TRIAGE-ASK` because the planner
  never mints an id. A hold whose named id is neither a census id nor a spec H1 — a shorthand `-4`,
  a decision id — counts as naming none, because it would otherwise land as a V6 verdict. Observed
  by AC5.
- **S8** The per-id status report. For every census id: the legacy token, the status the parser
  unit's fold predicts over the simulated migrated corpus together with this tree's spec index and
  build statuses from the view unit's collect path, and a difference class. With `--signed` naming
  the two signed records, the prediction applies their verdicts, read by the pinned header cells in
  §4. Observed by AC5 and AC6.
- **S9** The conservation proof. The prospective ask row of every id is rendered with the parser
  unit's renderer, re-parsed, and compared with its chosen legacy copy modulo the declared
  normalizations in §4; the proof prints a count per normalization and refuses any other difference.
  Observed by AC6.
- **S10** The records. `--record <dir> --record-as <unit-id>` writes a markdown census summary and
  three TAB-separated worksheets — `same-id`, `triage` and `status` — each carrying a Serves line
  naming the unit id, named by the recording grammar and dated by HEAD's commit day, never the
  clock. Two runs over one tree write byte-identical records. Observed by AC8.
- **S11** A `--selftest` over fixture repositories with real history, printing `PASS (<n>
  assertions)` against a floor constant, on a new gate leg, `backlog migration selftest`, in chunk
  `selftests` with subject `kit`, guarded on the kit directories it reads, and claimed by the
  memory-tree hygiene dossier. The relocation unit extends this suite. Observed by AC10.
- **S12** The unit's own product: `--plan` run over this repo in the unit's pass, filing the records
  into this build's `build/` folder as `TOOL-dDerivedDocket-11`, which is what the delegated signer
  signs. Observed by AC11.

## 3. Non-goals (OUT)

- `--write`, and any write outside the named record directory. `--write` is the switch-over's.
- `--relocate`, `--ingest`, `--repair`, `--stragglers` and `--recipe`. The relocation unit's.
- Signing either worksheet, or proposing a `unit` verdict. The signer's.
- The `filed` date of an ask. Status is date-free, so the prediction needs none, and the relocation
  engine already mines it from the delta walk; a second miner would be a second answer.
- A census over an adopter's tree from this build (§8 F3). Each adopter runs `--plan` in its own
  deployer build.
- The one-line legacy row grammar and the fold. The parser unit's; this unit calls them.
- Minting the triage ask's id. The orchestrator mints it at the switch-over.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-6` — the one-line legacy reader, the row renderers and the
  fold. Without them the planner would spell a second row grammar and a second status rule.
- **consumes-from** `TOOL-dDerivedDocket-7` — collect's spec index and build-status map, and the view
  renderer the census sizes prospective views with. Without them the triage population and the
  prediction have no build status to read.
- **hands-off** `TOOL-dDerivedDocket-12` — the module, the permissive legacy parser, the copy-choice
  rule, and the `--selftest` leg that the relocation engine extends.
- **hands-off** `TOOL-dDerivedDocket-33` — the same-id and triage worksheets, with the columns §4
  pins, which the signer reads and signs.
- **hands-off** `TOOL-dDerivedDocket-34` — the census's distinct-id count the conservation check
  counts against, the per-id report its status proof compares with, and the size, filing-home and
  archive-citation findings its commit must absorb.
- **hands-off** `DEPL-dDerivedDocket-1` — `--plan` and its records, which the adopter runbook's first
  step runs in an adopter's own tree.

## 4. Design

### The worksheets, column for column

Every worksheet opens with a `# **Serves:** journal <unit-id>` line, then one `#` line naming the tree
sha it was computed at and whether signed records were applied, then a header row, then data rows,
then a closing `examined<TAB><n>` line. No data row leads with an id in a list or table shape, so no
worksheet anchors an id.

| Worksheet | Columns, in order |
|---|---|
| same-id | `id` · `spec` · `legacy` · `evidence` · `sha` · `low_overlap` · `overlap` |
| triage | `id` · `home` · `source` · `legacy` · `derived` · `proposal` · `evidence` · `basis` · `dead_pointer` |
| status | `id` · `legacy` · `predicted` · `class` · `decided_by` |

- `evidence` on the same-id worksheet is `specced-in-place`, `born-in-spec-commit` or `none`; `sha`
  is the commit that shows it, or `-`.
- `source` is `<file>:<line>`. `proposal` is CLOSED, WONTDO, BLOCKED, DEFERRED or `none`; `evidence`
  is a spec id, a sha, a hold target or `-`; `basis` names the rule that selected it: `mined-closure`,
  `commit-names-ask`, `row-names-hold`, `design-named` or `none`.
- `class` on the status worksheet is `same`, `mirror-closed`, `stale-spec`, `mined-closure`,
  `recovered-flip`, `collision-kept-live` or `triaged`.

The signed records the prediction reads are the signer's markdown tables. The planner locates their
columns by the header cells `Ask`, `Verdict` and, on the triage record, `Field`, and refuses a record
whose header lacks one; §8 F4 records why these bytes are pinned here.

### Evidence, and what each class rests on

| Class | Shown by |
|---|---|
| `specced-in-place` | the chosen copy's token is SPECCED or INPROGRESS, or the history walk sees the row's token move from OPEN to SPECCED |
| `born-in-spec-commit` | the commit that first added the row also added the same-id spec file |
| `none` | neither |

The overlap score compares the row's words with the spec's H1 title and Goal; below a module
constant, the pair is flagged low-overlap. It is a heuristic, stated as one, and it only ever moves a
pair toward `not-unit` in the signer's rules.

Two history walks, one over the shard and archive paths and one over the spec paths, plus one walk of
commit messages. The process count is constant in the size of the census, and the liveness line
prints it.

### The declared normalizations

An ask's prospective text equals its chosen legacy copy's text except for exactly these, each
counted:

1. the status slot removed;
2. the `filed` field and, where a signed record says so, `unit` inserted;
3. a declared wrapped row joined onto one line;
4. a relative link rebased for the file's new depth;
5. a backticked citation of a backlog archive the switch-over deletes, rewritten as plain text — the
   switch-over spec's fifth normalization, counted here so its population is known before its commit.

### Measured at BASE, and what re-derives each figure

Over the tree at this build's records commit, 2026-09-14, node `d`: 599 distinct row ids across the
four shards and three family archives, 521 live row copies, 152 ids equal to a spec H1, 91 slugs
owning rows of which 6 have no build README, and 288 OPEN asks on 56 builds whose derived status is
terminal, plus 14 OPEN asks in README-less slugs that no build status covers. PINNED as that
measurement; `--plan` re-derives every one of them and the switch-over reads its own run.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `migrate_backlog.py` and its public functions: parse legacy rows, choose a copy, build the census, build each worksheet, predict, prove conservation, write records | kit module | lexicon python function cell; names pass `lexicon.py --suggest` before they are written |
| `--plan`, `--record`, `--record-as`, `--signed`, `--selftest` | CLI mode and options | flags |
| `TRIAGE-ASK` | placeholder in the triage and status worksheets | none; the switch-over substitutes the minted id |
| `backlog migration selftest` | gate leg | a gate-legs key, claimed by the memory-tree hygiene dossier |

### Files touched (estimate)

`migrate_backlog.py` (new) · `tools/gate-legs.json` · `memory/map/features/memory-tree-hygiene.md` ·
`memory/map/generated/` · the four records under `memory/builds/dDerivedDocket/build/`.

### Alternatives rejected

- **A pinned id count as the acceptance of the migration** (the `derive` design's "exactly 29
  OPEN→CLOSED"). It reds the very review that catches an error; a per-id status report is compared
  instead (design critique F1).
- **Inferring `unit` from equal ids.** Refuted by four different-subject pairs (design §2.3); the
  planner reports evidence and never a verdict.
- **Proposing a same-id spec as triage evidence.** It would close a pair D2 left unlinked, through
  the back door of the triage sweep.
- **Mining `filed` here as well as in the relocation engine.** Two miners of one date disagree
  exactly on the rows where the walk is hardest, and no prediction here needs the date.

## 5. Production-readiness checklist

- security — read-only on the tree; the only write is the named record directory, and every value
  written is text the repo already holds or a sha it can resolve. No command from any row executes.
- perf / scale — three history walks regardless of the census size; everything else is in memory.
  The census is about 600 ids and 90 slugs at BASE.
- error / empty / loading states — an unreadable row, two live copies of one id, a signed record
  missing a pinned header cell, or an empty corpus each refuse by name and file no worksheet.
- observability — the liveness line: rows read, ids, slugs, worksheet sizes and git processes spent.
- risks — the overlap heuristic flags too little or too much; its only effect is to push a pair toward
  `not-unit`, the recoverable error. A closing phrase in prose can name an ask it does not close; the
  signer re-reads the spec's status and body before signing.
- testing — `--selftest` on fixture repositories with real history, on its own leg, each arm staged
  RED; one real-tree run in the pass.
- migration — none; it is the plan for one.
- user docs — the module docstring states what `--plan` does not decide; the kit README section is
  the docs unit's, and the adopter runbook's first step is the deployer unit's.

## 6. Acceptance criteria

- **AC1** — When `migrate_backlog.py --plan` runs over a fixture repo, the census counts every row copy
  across shards and archives, joins the fixture's wrapped row, and chooses the live copy over an
  archived one; adding one row-shaped line that reads as nothing makes `--plan` exit 1 naming its
  file and line with no worksheet written.
  Red when: the unreadable line is skipped, so the distinct-id count is one short under a green exit.
- **AC2** — When the fixture holds two live copies of one id, `--plan` exits 1 naming both files.
  Red when: the planner picks one silently, so conservation certifies a migration that drops a row.
- **AC3** — When the fixture history holds a row born OPEN and later flipped to SPECCED, a row added in
  its same-id spec's own commit, and a pair with neither, the same-id worksheet reads
  `specced-in-place`, `born-in-spec-commit` and `none` with the showing sha for the first two.
  Red when: the class is read from equal ids alone, so every pair reads `specced-in-place`.
- **AC4** — When the fixture holds an OPEN ask on a finished build that another spec's body closes, one
  a product commit's message names, one whose pointer path is untracked, and one whose same-id spec
  reads CLOSED, the triage worksheet proposes CLOSED by that spec, CLOSED by that commit, `none` with
  `dead_pointer` set, and `none` for the last.
  Red when: the same-id spec is proposed as evidence, which answers D2 inside the triage.
- **AC5** — When the fixture holds legacy rows CLOSED, WONTDO, BLOCKED naming an id, and DEFERRED
  naming none, the status worksheet predicts CLOSED, WONTDO, BLOCKED and DEFERRED, the last held on
  `TRIAGE-ASK`, and each prediction's `decided_by` names the previewed record.
  Red when: the prediction applies its own status rule instead of the parser unit's fold, so the plan
  and the switch-over can disagree.
- **AC6** — When `--plan --signed` names a signed same-id record marking one pair `unit` whose spec
  reads CLOSED, that id's predicted status becomes CLOSED and its class `mirror-closed`; the
  conservation proof counts each normalization and exits 1 on a fixture row whose text differs in any
  other way.
  Red when: a signed record missing its `Verdict` header cell is read as all `not-unit`.
- **AC7** — When a fixture slug's prospective `BACKLOG.md` exceeds the declared row cap, the census
  names that slug and its size, and the README-less slugs are listed as filing homes.
  Red when: an oversized slug goes unreported, so the switch-over reds check 6 on its first run.
- **AC8** — When `--plan --record <dir> --record-as EXMP-aFoo-1` runs twice over one fixture tree, it
  writes four records named by the recording grammar with HEAD's commit day, each carrying the Serves
  line, byte-identical across the two runs, and `git status --porcelain` shows nothing outside
  `<dir>`.
  Red when: a record embeds the wall clock or an unsorted set, so re-running the plan rewrites a
  worksheet the signer already signed.
- **AC9** — When `--plan` runs over this repo with no `--record`, it exits 0, prints the census summary
  and its liveness line, and `git status --porcelain` is unchanged.
  Red when: the planner writes a cache or a record into the tree on a read-only run.
  figure: every count it prints is DERIVED at run time.
- **AC10** — When `migrate_backlog.py --selftest` runs, it prints its `PASS (<n> assertions)` line at
  or above the floor constant, and `tools/gate-legs.json` carries the leg claimed by the hygiene
  dossier with the codebase-map coverage leg green.
  Red when: an arm's failing case was never observed with its fix unstaged.
  cost: one kit selftest run; it is held, so it binds at the landing bar under `GATE_SELFTESTS=1`.
- **AC11** — When the unit's pass runs `--plan` over this repo with `--record` naming this build's
  `build/` folder, the four records land there, the triage worksheet's row count equals the census's
  OPEN-on-finished-build count, and `bash tools/memory-tree/check-memory-hygiene.sh` names none of the
  four records.
  Red when: a worksheet row leads with an id in a list or table shape, so check 13 sees the record as
  a second claimant of every ask it lists.
  cost: minutes, for the history walks and the hygiene run.

## 7. Gates

`memory hygiene` · `build-index selftest` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: `python3 tools/memory-tree/migrate_backlog.py --selftest` on the new `backlog migration selftest` leg · fixture repositories for each census rule, evidence class, proposal rule, normalization and refusal · the suite's own floor constant

## 8. Open questions

- **F1** — Which triage population does the planner compute before the same-id table is signed? (a)
  Under D2's default, no `unit`, a superset. (b) Under the planner's own guess at `unit`. (b) is a
  verdict the planner may not make. RESOLVED (agent, 2026-09-14, delegated): (a); an ask the signer
  later links as `unit` and whose spec is CLOSED simply derives CLOSED, and a triage KEEP on it is
  inert.
- **F2** — Which commits may evidence a triage closure? (a) Any commit naming the ask. (b) One that
  names it, did not file its row, and touched a path outside the memory tree. The filing commit names
  every ask it files, so (a) proposes a closure for every ask. RESOLVED (agent, 2026-09-14,
  delegated): (b).
- **F3** — Does this build run the design's read-only census over the three adopters? The design's
  planner unit lists it; the mandate refused any adopter migration, and reading three foreign trees
  from this run widens a data surface its tier did not price (M3 veto 3). RESOLVED (agent,
  2026-09-14, delegated): no; `--plan` is repo-agnostic, and each adopter's deployer build runs it.
- **F4** — Does the planner read the signed records? (a) Yes, by pinned header cells. (b) No; it
  predicts both arms of every pair and leaves the choice to the switch-over. The switch-over spec's
  status proof compares against "the planner's predicted status under the signed tables", which only
  (a) produces. RESOLVED (agent, 2026-09-14, delegated): (a). The signer spec names its columns in
  prose; the M2 interface cross-read pins `Ask`, `Verdict` and `Field` in both specs.
- **F5** — What stands in for the design-named closures of design §21.5 when no rule finds evidence?
  RESOLVED (agent, 2026-09-14, delegated): the three rows it names are listed with basis
  `design-named` and no evidence, so the signer applies its own rules to a claim it can see rather
  than to a sha the planner invented.
- The rulings this unit executes: D2 no inferred pairing, the owner or a delegate signs; D6 the
  closeout triage before the switch-over; D8 the archives go after the conservation proof — RESOLVED
  (owner, 2026-09-13). The delegation of both signatures — RESOLVED (owner, 2026-09-14).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds two edges the brief's table does not list: hands-off to
  unit 34, reciprocating that spec's consumes-from, and hands-off to the adopter runbook, which runs
  `--plan`.

## 10. Reuse audit

No existing seam fits the planner itself: nothing in the tree plans a migration or proves
conservation. `python tools/codebase-map/reuse_lookup.py "plan a data migration read-only and report a
per-record conservation proof"` returned the generic readers `read_text` and `read` and the
generator's `plan`, which renders artifacts and plans no migration, with the shell layer unscanned.
The seams this unit reuses are the parser unit's legacy reader, renderers and fold, the view unit's
collect path in `tools/memory-tree/gen_build_index.py`, and the TSV-record precedent a build folder
already carries, a `.tsv` recording whose first line is a commented Serves line. Recall returned
`TOOL-cSpliceWarden-1` and the 2026-08-17 archive supersession note, which are why S3 prefers a live
copy and, among archived ones, a terminal copy: the reconcile that produced that archive lost flips
exactly where a non-terminal archived copy outranked a live one.

Where the design and BASE disagree: design §9 counted 592 distinct ids, 499 live and 161 archived
copies at `09a22d2b`; `TOOL-cSpliceWarden-4` and `-7` since reconciled the archives, and BASE holds
599 ids with 521 live and 78 archived copies. The design's 275 triage asks on 60 builds is now 288 on
56. The design put the adopter census and `--ingest` in this unit; the brief's label table moves
`--ingest` to the relocation unit and §8 F3 drops the census. At BASE, five of the seven legacy
BLOCKED and DEFERRED rows name no full id at all — "blocked on `-4` and `-11`", "only on the owner's
word" — so S7's triage-ask rule has a real population, measured by grepping the live shards. The relocation spec classifies a hold naming no id as
NEEDS-HUMAN for a straggler delta; the switch-over applies design §9 step 6 to the whole corpus
instead, and this preview follows step 6. Which policy the switch-over passes that engine is a line
the M2 interface cross-read must see in the switch-over spec.

M12 losses are the design's own tested rejections, carried in §4 Alternatives rejected with the
measurement that rejected each.

Recall terms used: `rotation reconcile archive lost flip same-id pair spec H1 backlog row census conservation migration WITHDRAWN`
