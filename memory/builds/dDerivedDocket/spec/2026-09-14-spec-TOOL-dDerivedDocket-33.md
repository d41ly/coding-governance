# TOOL-dDerivedDocket-33 — delegated signing of the same-id and triage tables

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 33

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

The owner delegated two signatures to this run instead of giving them personally: the D2 same-id
table, which decides which legacy asks carry the `unit` marker, and the D6 triage sweep, which gives
every ask deriving OPEN on a finished build a disposition before the closeout gate goes live. Sign
both under rules stated here, mechanically and conservatively, so that every signature is a row a
later reader re-derives by re-running one script over the planner's recorded output.

## 2. Scope (IN)

- **S1** A signing script, filed as a recording-named artifact under
  `memory/builds/dDerivedDocket/build/`, reads the planner's two worksheets and writes two signed
  records. It is a pure function of its inputs and the tree it reads, and a `--check` mode re-derives
  both records and diffs them against the tracked copies. Observed by AC1 and AC2.
- **S2** The same-id rules U1 to U4 in §4 decide the `unit` marker for every pair the planner lists.
  `unit` is signed only where the planner's evidence says the row was specced in place or born in
  its spec's own commit, the pair is not one the design names as different subjects, and the planner
  did not flag the pair as low-overlap. Every other pair is signed not-`unit`, naming the first rule
  it failed. Observed by AC3.
- **S3** The triage rules T1 to T6 in §4 decide one disposition for every ask the planner lists as
  deriving OPEN on a finished build after the migration's own dispositions. CLOSED and WONTDO are
  signed only with evidence the script re-reads itself. A row no rule decides is signed KEEP, and its
  reason names the rule that could not decide it. Observed by AC4 and AC5.
- **S4** `TOOL-aWeighedCompass-3` is excluded from the triage by rule T1, because the flip disposes
  it as superseded and one file may carry only one disposition per target. Observed by AC6.
- **S5** No severity is signed. Every triage row records `unlabelled`, and the record's header
  carries the census that found no recorded severity in the legacy rows. Observed by AC7.
- **S6** Neither signed record anchors an id. Each table row leads with a row number, and the ask id
  sits in a later cell, so no reader counts the record as a second definition. Observed by AC8.
- **S7** One `memory/DECISIONS.md` row under the TOOL heading, keyed by this unit's id, records that
  both tables were signed under delegation and points at the two signed records. Observed by AC9.
- **S8** A verdict depends only on its own row's evidence, so re-running the script over a worksheet
  recomputed at a later tree changes only the rows whose evidence moved. The flip's landing
  reconcile relies on this. Observed by AC10.
- **S9** The script prints one liveness line counting what it signed per verdict, and refuses an
  empty worksheet or a row it cannot parse instead of skipping it. Observed by AC11.
- **S10** Every triage disposition is to be written in this build's own `BACKLOG.md`, the signer's
  file, which the closeout rule accepts from any file (owner ruling D6 as amended in design §17.2).
  NOT OBSERVED here: this unit writes no `BACKLOG.md`. The write is `TOOL-dDerivedDocket-34`'s, and
  its acceptance criteria observe it.

## 3. Non-goals (OUT)

- No `BACKLOG.md` row, view or disposition is written. The signed records are inputs to the flip,
  which applies them exactly.
- No planner logic. Evidence that needs a history walk, such as "born in its spec's own commit", is
  consumed from the planner's worksheet and never re-derived here; a second walk would be a second
  answer to one question.
- No `--sign` mode in `tools/memory-tree/migrate_backlog.py`. The ratified design names that tool's
  modes, and a new one is a public surface the owner did not price (§8 F1).
- No severity judgment, and no default severity (§8 F2).
- No re-litigation of D2, D6 or D7. The owner ruled them. This unit only replaces the owner's
  signature with rules, as the owner instructed.
- No adopter tables. Each adopter signs its own in its own deployer build.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-11` — the same-id worksheet and the triage worksheet the
  planner files as build records, with the evidence fields §4 lists. Without them there is nothing
  to sign, and the script refuses.
- **hands-off** `TOOL-dDerivedDocket-34` — the two signed records, applied exactly by the flip, and
  the script itself, which the flip's landing reconcile re-runs over the asks the landing tip added.

## 4. Design

### Data model

**Inputs.** The two worksheets the planner files under this build's `build/` folder, read in the
machine-readable form the planner's spec names. The kit precedent for a machine projection is one
TAB-separated line per record, and this spec assumes it. The fields this unit needs are below; if
the planner's spec spells them differently, the M2 interface cross-read decides which spec is wrong.

| Worksheet | Field | Used by |
|---|---|---|
| same-id | ask id, same-id spec path, legacy token | U1-U4 |
| same-id | evidence class: `specced-in-place`, `born-in-spec-commit` or `none`, with its sha | U1 |
| same-id | the planner's low-overlap flag | U3 |
| triage | ask id, home slug, the row's file and line, legacy token | T1-T6 |
| triage | the status the fold derives after the migration's own dispositions | population |
| triage | the planner's proposal: a verdict and its evidence (a spec id, a sha, or a hold target) | T2-T5 |

**Outputs.** Two markdown records under `memory/builds/dDerivedDocket/build/`, each carrying
`**Serves:** journal TOOL-dDerivedDocket-33` in its first twelve lines:

- the signed same-id record: one row per pair, with the columns row number, ask id, spec path,
  verdict (`unit` or `not-unit`), deciding rule, evidence;
- the signed triage record: one row per ask, with the columns row number, ask id, verdict
  (`KEEP`, `CLOSED`, `WONTDO`, `BLOCKED` or `DEFERRED`), the `by`/`on`/`until` field, deciding
  rule, evidence, severity (`unlabelled`), plus an exclusions list.

Each record's header states: the signer as `(agent, 2026-09-14, delegated)`; the authority, which is
the owner mandate record's "single owner turn" section; each worksheet's path and git blob sha; the
rule set, which is this spec at its current rev; and the liveness counts.

### The same-id rules

Evaluated in order; the first rule a pair FAILS decides `not-unit` and is named.

| Rule | A pair signs `unit` only if |
|---|---|
| U1 | the planner's evidence class is `specced-in-place` (the legacy token read SPECCED or INPROGRESS, or history shows the row flipped OPEN to SPECCED) or `born-in-spec-commit` (the commit adding the row also added the same-id spec) |
| U2 | the pair is not one design §2.3 names as different subjects |
| U3 | the planner did not flag the pair low-overlap |
| U4 | the same-id spec file the planner names exists at the signing tree and its H1 carries the ask id |

The U2 set is four ids, embedded in the script with a comment citing design §2.3 and §9 step 5:
`TOOL-dFramedEntrypoint-1`, `TOOL-aSealedCaravan-1`, `TOOL-cBriefedPilot-23` and
`TOOL-aBoundedVerdict-22`. The script is a build record rather than a kit file, so a literal list is
legal here and ships nowhere.

Why U3 overrides U1. A pair with specced-in-place evidence and a low-overlap flag is the one place
the evidence and the subject disagree. `unit` makes the spec's terminal status the ask's, and a
wrong `unit` closes an ask nobody answered. `not-unit` leaves it live and decided by its own
evidence, and the triage then disposes it if its build is finished. The owner's terms say
conservatively, and the second error is recoverable while the first is silent.

### The triage rules

The population is every ask the planner lists as deriving OPEN on a build whose derived status is
terminal, after the migration's own step-6 dispositions. Evaluated in order; the first that matches
decides.

| Rule | Verdict | Signed only when |
|---|---|---|
| T1 | excluded | the ask is `TOOL-aWeighedCompass-3`, which the flip disposes as superseded (design §14) |
| T2 | CLOSED by a spec | the proposal names a spec whose status header the script re-reads as CLOSED at the signing tree, AND that spec's body names the ask id |
| T3 | CLOSED by a sha | the proposal names a sha that `git cat-file -e` resolves to a commit, AND that commit's message names the ask id |
| T4 | WONTDO | the row's own text records a withdrawal, cited by file and line |
| T5 | BLOCKED or DEFERRED | the proposal carries a hold target the row's own text names, the target is a filed ask or a spec H1, it is live at the signing tree, and DEFERRED additionally needs the row's legacy token to read DEFERRED |
| T6 | KEEP | otherwise; the reason names the first of T2 to T5 that the row came closest to, or "no evidence" |

What each rule refuses on purpose:

- **T2 and T3 re-read the evidence rather than trust the proposal.** A mined phrase in a spec that
  still reads SPECCED is not a closure, and neither is a sha whose commit never mentions the ask. The
  planner's proposal selects candidates; the script decides.
- **A partial answer is not mechanically detectable, and that is stated rather than implied away.**
  The planner pre-fills three rows the kit-stop census found already fixed (design §21.5), and one of
  them is only half answered. T3 signs such a row only if the fixing commit's message names the ask.
  If a commit names an ask and answers half of it, the signature is wrong in a way D4's REOPEN
  repairs, and the triage record's header says so.
- **The script never originates a hold.** A hold is a dependency judgment. T5 signs one only when
  the row's own author wrote the target.
- **A dead pointer is not evidence.** The planner flags asks whose pointer target no longer exists.
  Code moves, and the ask may still be wanted, so such a row reaches T6 with that reason.

### Severity

Measured 2026-09-14 at BASE over the four legacy shards: 0 of 521 rows carry an upper-case level word
(`BLOCKER`, `HIGH`, `MED`, `LOW`), and the 18 case-insensitive hits in the TOOL shard are prose about
review findings, not a label on the ask. PINNED as that measurement; the script re-derives the count
at signing time and prints it. A mechanical severity rule would therefore either label nothing or
invent a level, and D7 is forward-only, so no legacy ask is required to carry one (§8 F2).

### Where the triage dispositions land

In `memory/builds/dDerivedDocket/BACKLOG.md`, the signer's own file. Design §17.2 moved the closeout's
satisfying record to ANY file because a finished build's sessions do not come back, and the one-writer
rule then puts a triager's rows in the triager's folder. The migration's own step-6 rows are different:
they transfer text the ask's owner already wrote, so they land in the owner's folder. A triage
disposition is this run's judgment under delegation, so it does not (§8 F4).

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| the signing script | build-folder python artifact, unit tail `signer` | `memory/builds/dDerivedDocket/build/` | not graded: the naming leg's population is `tools/`, `skills/`, `.githooks/` and `.claude/`; its functions still lead with a verb `.lexicon.conf` declares |
| the signed same-id record | build record, unit tail `signed-same-id` | same folder | recording-file grammar, check 5 |
| the signed triage record | build record, unit tail `signed-triage` | same folder | recording-file grammar, check 5 |
| rule ids U1-U4, T1-T6 | labels inside the records | the two records | none |
| the decision row | one `memory/DECISIONS.md` row, keyed by this unit's id | TOOL heading | entry budget, check 7 |

### Files touched (estimate)

| Path | Change |
|---|---|
| `memory/builds/dDerivedDocket/build/` | the script and the two signed records, all new |
| `memory/DECISIONS.md` | one row under the TOOL heading |

### Alternatives rejected

- **A `--sign` mode in the migrator.** Rejected by M3 veto 2 (§8 F1).
- **Signing by hand from the worksheets.** Not re-derivable: a reader re-applying the rules by eye
  across roughly 150 pairs and roughly 275 asks cannot tell a rule error from a transcription error.
- **Re-deriving the planner's history evidence in the script.** Two implementations of one walk, and
  the one that disagrees is unfindable. The cheap facts, a spec's token and a sha's existence, are
  re-read because a wrong one signs a closure; the expensive one is consumed and cited.
- **A default severity for swept asks.** Rejected under §8 F2.

## 5. Production-readiness checklist

- security — N/A for input handling: the script reads tracked records and git objects and writes two
  records in its own build folder. The authority it exercises is the owner's delegation, recorded in
  every signed record's header.
- perf / scale — one `git cat-file --batch-check` for every cited sha and one read per cited spec,
  over a few hundred rows. Seconds.
- error / empty / loading states — an empty worksheet and an unparseable row both refuse (AC11). An
  ask whose cited spec or sha no longer resolves falls through to KEEP with that reason.
- observability — the liveness line, and each row's rule and evidence columns.
- risks — a rule written too loosely signs a closure nobody made. Every CLOSED row therefore carries
  re-read evidence (AC4), and D4's REOPEN is the recovery for one that slips through.
- testing — the script's `--check` re-derivation, the determinism run, and the synthetic-row run
  (AC1, AC2, AC10). No gate leg is added: this is a build record, not a kit file.
- migration — none here. The flip applies the records.
- user docs — N/A: the records are read by the flip and by a reader auditing the delegation. Each
  record's header says how to re-derive it.

## 6. Acceptance criteria

- **AC1** — When the signing script runs twice over the planner's two worksheets and then runs with
  `--check`, both signed records are byte-identical across the two runs and `--check` exits 0.
  Red when: an output depends on hash ordering or on the time of the run, so a second run rewrites
  a signature nobody changed.
  fixture: the planner's two worksheets, filed by `TOOL-dDerivedDocket-11`. None is in the tree
  today.
- **AC2** — When one signed row's verdict is edited by hand and the script runs with `--check`, it
  exits non-zero naming that row's ask id and deciding rule.
  Red when: `--check` compares per-verdict counts rather than rows, so a verdict flipped against
  another left the tally unchanged and passes.
- **AC3** — When the signed same-id record is read, each of `TOOL-dFramedEntrypoint-1`,
  `TOOL-aSealedCaravan-1`, `TOOL-cBriefedPilot-23` and `TOOL-aBoundedVerdict-22` reads `not-unit`
  under rule U2, and every `unit` row cites `specced-in-place` or `born-in-spec-commit` evidence.
  Red when: the U2 set is read from an input that can arrive empty, so a design-named collision
  signs `unit` because its denial never loaded.
- **AC4** — When the signed triage record is read, every CLOSED row cites either a spec whose status
  token the script re-read as `CLOSED` and whose body names the ask, or a sha that
  `git cat-file -e` resolved and whose commit message names the ask.
  Red when: a proposal's CLOSED is copied through on the planner's word, so a closing phrase in a
  spec still reading SPECCED signs a closure.
  figure: the per-verdict counts are DERIVED at signing time and are not pinned here.
- **AC5** — When a triage worksheet row carries no evidence that T2 to T5 accept, its signed verdict
  is `KEEP` and its reason names the rule that could not decide it.
  Red when: an undecided row takes the planner's proposal instead of KEEP.
- **AC6** — When the signed triage record is searched for `TOOL-aWeighedCompass-3`, the id appears
  only in the exclusions list, with a reason naming the flip's disposal.
  Red when: the ask is signed KEEP here and WONTDO by the flip, which puts two dispositions for one
  target in one file and reds verdict V4.
- **AC7** — When the signed triage record is read, no row's severity cell is anything but
  `unlabelled`, and the header states the level-word census and the count the script derived.
  Red when: a default level is written for a row whose text records none.
  figure: the census is PINNED at 0 of 521 legacy rows, measured 2026-09-14 at BASE, and the script
  re-derives it on every run.
- **AC8** — When both signed records are tracked and `python tools/memory-tree/corpus_ids.py --check`
  runs, it reports no id defined twice.
  Red when: a table row leads with a backticked id, which the recall grammar reads as a definition,
  so check 13 sees the record as a second claimant of an ask the backlog already defines.
- **AC9** — When `memory/DECISIONS.md` is read, its TOOL heading carries one row keyed by this unit's
  id that points at both signed records and fits the entry budget.
  Red when: the row restates the rules instead of pointing at them, which breaches the budget and
  makes the row a second copy of this spec.
- **AC10** — When a copy of the triage worksheet gains one synthetic row and the signing script's
  `--check` mode re-runs over the copy, the diff of the signed triage record against its tracked copy is that one added row plus
  the liveness counts.
  Red when: a verdict depends on a population-wide statistic, so an added ask moves an unrelated
  signature at the flip's landing reconcile.
- **AC11** — When the signing script (`--check` and the signing run alike) runs over an empty
  worksheet, and again over one holding a row it cannot parse, it exits non-zero both times naming
  the worksheet and the line.
  Red when: the bad row is skipped and the liveness line still prints a count, which reads exactly
  like a clean signing.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `drift-audit records`

No new gate arm. The script is a build record, and its re-derivation is its own `--check`, run in
this unit's pass and again by the flip before it applies the records.

## 8. Open questions

- **F1** — Where does the signing logic live? (a) A `--sign` mode in
  `tools/memory-tree/migrate_backlog.py`, gated by the kit's self-test and reusable by adopters.
  (b) A script in this build's `build/` folder, re-derivable by `--check`. (c) Hand signing. (a) is
  the most feature-rich, but the ratified design names that tool's modes and a mode it does not name
  is a new public surface, which M3 veto 2 reserves to the owner. (c) is not re-derivable.
  RESOLVED (agent, 2026-09-14, delegated): (b), the only option surviving the vetoes that meets
  the owner's "a record a later reader can re-derive".
- **F2** — What severity does a swept ask get? (a) A declared default level, which satisfies design
  §17.2's "it also gets a SEV" literally. (b) None, recorded as `unlabelled`. The census in §4 found no
  recorded level on any legacy row, so (a) asserts a judgment nobody made, and the owner's terms say
  conservatively. D7 is forward-only, so no verdict requires a legacy label, and the drift count of
  unlabelled asks keeps the gap visible. RESOLVED (agent, 2026-09-14, delegated): (b).
- **F3** — Does a low-overlap pair with specced-in-place evidence sign `unit`? (a) Yes, the evidence
  wins. (b) No. RESOLVED (agent, 2026-09-14, delegated): (b), the recoverable error of the two, as §4
  argues.
- **F4** — Which folder carries a triage disposition? (a) The ask owner's folder, beside the
  migration's own rows. (b) This build's own `BACKLOG.md`. RESOLVED (agent, 2026-09-14, delegated):
  (b). The one-writer rule puts a judgment in its author's file, and design §17.2 already moved the
  closeout's satisfying record to any file for exactly this case.
- The rulings this unit executes and does not revisit: D2, legacy same-id pairs not linked by
  default; D6, the closeout is a gate from the switch-over, retroactive, sweep first; D7, severity
  now and forward-only — all RESOLVED (owner, 2026-09-13). The delegation of both signatures to this
  run, with the D10 drain replaced by the permanent transition audit, is RESOLVED (owner, 2026-09-14).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.

## 10. Reuse audit

No existing seam fits. `python tools/codebase-map/reuse_lookup.py "sign a proposed adjudication
table under mechanical rules before a migration applies it"` returned name-stem neighbours only —
govkit's rule helpers and the build README slot table readers — none of which signs or applies a
proposal, and its scan-coverage line reports the shell layer unscanned. The recall probe returned the
design record, the brief's own delegation section, and the curation-debt note for
`TOOL-aWeighedCompass-3`, and no record of any earlier delegated signing. The nearest prior art is
the three hand-typed resolution tables unattended runs wrote for foreign ids, which design §19.1 K9
measured as the source of 14 of the 27 anchor-hazard ids; §4's row-number-first record shape exists
to avoid exactly that. The recorded precedent for a closeout rule is nicocares' closed-build rows
gate, which is external and is upstreamed by this build's closeout verdict, not by this unit.

Where the design and the source disagree at BASE: design §11 cites the curation-debt row for the TOOL
shard at line 46, and it is at `memory/project/curation-debt.txt:54`. Nothing in this unit depends on
it.

Recall terms used: `same-id pair unit marker adjudication triage closeout KEEP WONTDO delegated signing owner curation-debt backlog shard`
