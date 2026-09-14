# TOOL-dDerivedDocket-8 — hygiene engine in builds mode

**Status:** SPECCED · rev-2 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round1.md) | spec-audit | TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 |

<!-- /gen:spec-records -->

## 1. Goal

The hygiene engine grades the authored backlog shards in five places and the id corpus in three,
and every one of those assumes the shard layout. Teach each of them the declared `BACKLOG_MODE`: in
`builds`, per-build `BACKLOG.md` files join the checks that bound and grade records, the generated
views leave the checks that exist to police authored rows, and check 13 regains the forward
collision check the blanket skip would lose. In `shards`, every check's output stays byte-identical,
so this repo and every adopter see nothing until they switch.

## 2. Scope (IN)

- **S1** The shell engine presets `BACKLOG_MODE` for `set -u`, validates it in the project-key block
  beside `ROTATION_MODE` (blank or `shards` or `builds`; anything else aborts at exit 2 naming the
  key), and names a set value on stderr with the other project keys. The Python checks read the
  mode through the parser unit's one conf reader, and an arm asserts the shell and Python readers
  agree over every value. Observed by AC9.
- **S2** Check 4 admits `F:BACKLOG.md` in a build folder under `builds`, including a folder holding
  nothing else (a filing home), and still refuses it under `shards`. Observed by AC1.
- **S3** Check 6 under `builds`: every tracked `builds/*/BACKLOG.md` joins the index population in
  the row class, and a finding against one fails on its own branch whose remedy is "move detail into
  a `build/` recording; never rotate". The family views leave check 6's population (owner ruling D3).
  Observed by AC2.
- **S4** Check 7 under `builds`: `BACKLOG.md` joins the entry-budget exemptions, because the ask is the
  record and its text is free prose on one line; the views stay graded, short by construction.
  Observed by AC3.
- **S5** Check 8 under `builds` is RETIRED and prints `memory-hygiene: check 8: backlog layout
  builds — graded by check 9` in place of its graded-row line; its population guard learns the mode
  and does not fire. Under `shards` it runs exactly as today, graded-row line included. Observed by
  AC4.
- **S6** Check 13 (owner ruling D12-g): a `BACKLOG.md` ask row filed before `ASK_CUTOFF` does not
  count as its folder's claim on the id, so the legacy foreign anchors stay quiet; an ask filed on or
  after it does, so a new foreign anchor is a collision. The row still DEFINES the id for check 14, so
  no legacy ask becomes an orphan. A cutoff the parser unit returns as V15 (blank) or V16 (not a
  `DATE`) under `builds` skips every ask row and says so once, naming that verdict. Observed by AC5.
- **S7** Check 15 under `builds`: the present-tense corpus drops `backlog/` and adds
  `builds/<slug>/BACKLOG.md`, so every path an ask cites stays graded and the views' derived text does
  not (owner ruling D9). Observed by AC6.
- **S8** Checks 20 and 24 under `builds`: `row_docs()` holds `DECISIONS.md` and the decision-log
  archives only. The views are not row documents, a family archive is the view unit's archive-guard
  verdict and not a second finding here, and ask uniqueness is the fold's V3 corpus-wide. Observed by
  AC7.
- **S9** Check 10 under `builds` leaves a family-stem archive to that same guard and prints one line
  counting what it left, rather than reporting "not referenced from its live index" against a view
  that could never reference it. Observed by AC8.
- **S10** Shards byte-identity: the engine's full output over this repo is identical before and after
  the unit, finding for finding and line for line. Observed by AC10.
- **S11** The curation-debt stale-entry guard needs no new code, and this unit proves it: under
  `builds` a debt row naming a family view records nothing, reads as stale, and reds — the red the
  switch-over clears by deleting the row. Observed by AC11.
- **S12** The HYGIENE template and its rendered instance describe both modes for every check this
  unit changes, the tree diagram, the backlog status-vocabulary section and the single-file-build
  sentence (a filing home under `builds`); the spec template names `closes` and `advances` as header
  verbs legal only under `builds`. Template and instance move together, because the parity leg binds
  them. Observed by AC12.
- **S13** Every new `fail` branch is armed in the engine's self-test in the same commit, and
  `ARMS_FLOORS` for the engine moves by the branches added. Observed by AC13.
- **S14** The two frozen waivers this unit's edits would unpin — rows
  `tools/memory-tree/corpus_ids.py:935` and `:939` of `tools/install-prefix-waivers.txt`, the check-15
  selftest's wrong-prefix fixture and the citation it proves — become in-line
  `# gov:root-fixture — <reason>` markers on those two fixture lines, and both rows leave the
  registry in the same commit, so no later edit above them can unpin them again. Observed by AC14.

## 3. Non-goals (OUT)

- Check 9's verdicts, the views, the mode and archive guards, and filing homes in the generator. The
  view unit's; this unit only stops the engine double-reporting what check 9 owns.
- Check 3. Under `builds`, `backlog/` still holds only `<FAMILY>.md` and a filing home is a folder,
  both of which it already admits; no change is needed and none is made.
- Check 25, the transition audit, and its registry's admission to check 3. The audit unit's.
- Retiring the drift pin, re-pointing the live-rows signal, and deleting the curation-debt row or the
  archives. The switch-over's.
- The memory-tree kit README, the guides and the backlog dossier. The docs unit's.
- Promoting check 16's read-path rules from report to gate.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-6` — the conf reader and the two keys' semantics, and the
  ask row's `filed` field that check 13's skip reads, and the conf verdicts V15 and V16 on which that
  skip treats the cutoff as unusable. Without them the Python checks would each spell a second
  reader.
- **consumes-from** `TOOL-dDerivedDocket-7` — the family view set that leaves check 6 and stays in
  check 7, and the archive guard that checks 10, 20 and 24 defer to under `builds`.
- **hands-off** `TOOL-dDerivedDocket-34` — an engine that grades a builds-mode tree, so the switch-over
  commit reds nothing in checks 4, 6, 7, 8, 13, 15 or 20 on its first run.

## 4. Design

### What each check does under each mode

| Check | Where at BASE | `shards` | `builds` |
|---|---|---|---|
| 4 | the folder whitelist at `tools/memory-tree/check-memory-hygiene.sh:611` | unchanged | `F:BACKLOG.md` admitted |
| 6 | `index_set()` at `:650`, fail at `:736` | unchanged | `BACKLOG.md` in the row class on its own branch; views leave |
| 7 | `ex7` at `:751` | unchanged | `BACKLOG.md` exempt; views stay graded |
| 8 | population at `:828`, fail at `:866`, count line at `:868` | unchanged | retired, one announcement line |
| 10 | enumeration at `:1076` | unchanged | family archives left to check 9's guard, counted in one line |
| 13 | `def_builds` at `tools/memory-tree/corpus_ids.py:393` | unchanged | pre-cutoff ask rows are not a folder's claim |
| 15 | the `present` expression at `tools/memory-tree/corpus_ids.py:372` | unchanged | `backlog/` out, `builds/<slug>/BACKLOG.md` in |
| 20, 24 | `row_docs()` at `tools/memory-tree/row_grammar.py:180` | unchanged | the decision log and its archives only |

Check 7's population is no longer derived from check 6's under `builds`, because the two now differ by
the views. It becomes check 6's set plus the views, minus the exemptions — one expression per mode,
never a second spelling of the base selector (the `ex7` rule the engine records at `:747-750`).

### The check 13 skip, precisely

`corpus_ids.walk()` records every anchor in `defs` and, for a build-folder file, in `def_builds`. The
change touches only the second: an anchored line in a `builds/<slug>/BACKLOG.md` whose ask row, read by
the parser unit's reader, carries a `filed` date before `ASK_CUTOFF` is not added to `def_builds`.
Measured at BASE with the real `extract.anchor_at` over every tracked build-folder file: 27 of the 599
distinct legacy row ids are already anchored in another build's records, the same 27 design §6
measured, all in unattended runs' own records (design §19.1 K9). Every one of them is migrated with a
`filed` date before the cutoff the switch-over derives, so all 27 stay quiet and every ask filed
afterwards is checked.

### The Python modules and the mode

`corpus_ids.py` and `row_grammar.py` import the parser unit's module lazily, inside the functions that
need it, because that module reads the conf through `corpus_ids.parse_conf` and a module-level import
each way would be a cycle. No third conf reader is written.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `BACKLOG_MODE` preset and validation | shell block in the engine | none; mirrors `ROTATION_MODE` |
| the check 6 `BACKLOG.md` branch | a new `fail 6` call | the check-arms signature, armed in the engine's self-test |
| the check 8 and check 10 announcement lines | stdout lines | none |

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/check-memory-hygiene.test.sh` ·
`tools/memory-tree/corpus_ids.py` · `tools/memory-tree/row_grammar.py` ·
`tools/memory-tree/HYGIENE.template.md` · `memory/HYGIENE.md` ·
`tools/memory-tree/SPEC-TEMPLATE.template.md` · `memory/TEMPLATE-SPEC.md` · `.memory-tree.conf`
(`ARMS_FLOORS` only) · `tools/install-prefix-waivers.txt` (two rows leave, S14).

### Alternatives rejected

- **A blanket check 13 skip over every `BACKLOG.md`** (the ratified design before D12-g). Once the
  ask's home stops counting as a claim, one foreign anchor reds nothing anywhere, so the forward
  check is lost for every new ask (design §19.7).
- **Keeping the views under check 6 at 61,440 B** (option D3 a). A hard live-ask cap near 400 TOOL asks,
  about a week of headroom, and the thing `TOOL-aRelaxedShard-4` refused (owner ruling D3).
- **Leaving checks 10, 20 and 24 reading family archives under `builds`.** Each would report the same
  tracked archive the view unit's guard already reds, three findings for one fact, and check 24's
  exclusivity half would name a view as the archive's "live index".
- **Extending check 6's existing message with a second remedy clause.** It changes the branch's
  signature and still tells a `BACKLOG.md` author to rotate, which the per-build model never does.

## 5. Production-readiness checklist

- security — N/A for input handling: the engine reads tracked files and git objects only, and the new
  mode value is validated before any check reads it.
- perf / scale — no new walk: every change is a selector or a filter inside an existing pass; check 13
  reads each `BACKLOG.md` ask row's date once per walk.
- error / empty / loading states — an unrecognised mode aborts at exit 2; a retired check and a
  deferred archive each announce themselves rather than printing nothing.
- observability — the check 8 announcement, the check 10 count line, and the stderr project-key line.
- risks — the shell and Python mode readers could diverge on an odd spelling; the agreement arm is the
  control. An adopter whose `BACKLOG.md` files outgrow the kit's 20,480 B row cap meets check 6's
  never-rotate remedy (design §16 risk 4).
- testing — builds-mode scratch-tree fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`,
  `tools/memory-tree/corpus_ids.py --selftest` and `tools/memory-tree/row_grammar.py --selftest`, each
  staged RED, and the shards byte-identity arm over this repo.
- migration — none; a conf without the key reads `shards`, and the HYGIENE text describes both modes.
- user docs — the HYGIENE and TEMPLATE-SPEC text in S12, template and instance together.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs its builds-mode fixture,
  a build folder holding `BACKLOG.md` beside its README, and a folder holding only `BACKLOG.md`, raise
  no check 4 finding; the same folders in its shards-mode fixture raise check 4.
  Red when: the admission is unconditional, so a shards adopter's stray `BACKLOG.md` is never named.
- **AC2** — When the builds-mode fixture carries a `BACKLOG.md` over the row cap, check 6 fails on the
  branch naming the never-rotate remedy and not the rotate one; a family view over the same cap
  raises no check 6 finding; in the shards fixture an oversized shard fails with today's message.
  Red when: the `BACKLOG.md` finding rides the rotate message, which instructs the one act the
  per-build model forbids.
- **AC3** — When a builds-mode fixture ask row is 500 characters and a view line is 320, check 7
  grades the view line and not the ask.
  Red when: `BACKLOG.md` is graded by the entry budget, which would force a record into a 300-character
  summary it was designed to outgrow.
- **AC4** — When the engine runs over the builds-mode fixture, it prints `check 8: backlog layout
  builds` and no check 8 failure or population-guard line; over the shards fixture it prints the
  graded-row line exactly as at BASE.
  Red when: the population guard still fires under `builds`, because its precondition already counts
  `BACKLOG.md` files and its population now holds none.
- **AC5** — When `python3 tools/memory-tree/corpus_ids.py --selftest` stages an ask filed after the
  fixture's cutoff and anchors its id in a second build folder, check 13 names the collision; the same
  shape for an ask filed before the cutoff raises nothing; and that pre-cutoff id is not reported as an
  orphan by check 14; with the fixture's cutoff set to `2026-9-30`, check 13 skips every ask row and
  its one line names V16.
  Red when: the skip is taken for every ask row regardless of date, which is the blanket skip D12-g
  replaced; or a malformed cutoff is compared as a raw string, so a post-cutoff collision is skipped
  silently.
- **AC6** — When a builds-mode fixture ask cites a dead backticked path, check 15 names it; the same
  token in a view is not graded; in the shards fixture a dead path in a shard is still named.
  Red when: the present corpus drops `backlog/` without adding `BACKLOG.md`, so 227 graded ask path
  tokens silently leave the check.
  figure: 227 is PINNED from design §6's measurement and is not re-derived here.
- **AC7** — When `python3 tools/memory-tree/row_grammar.py --selftest` runs its builds-mode fixture, the
  row documents are the decision log and its archive only, a duplicated id inside the decision log
  still fails check 20, and check 24 grades exactly the decision-log archive.
  Red when: a view is read as a row document, so its link-wrapped table rows count as a mis-segmented
  grammar.
- **AC8** — When the builds-mode fixture in `bash tools/memory-tree/check-memory-hygiene.test.sh`
  tracks a family archive, check 10 prints one line counting it as left to check 9's archive guard
  and raises no finding of its own; the shards fixture's archive
  missing its preamble reference still fails check 10.
  Red when: check 10 and check 9 both red the one archive, which is two answers to one question.
- **AC9** — When `BACKLOG_MODE` is `buildz` in a fixture conf, `bash tools/memory-tree/check-memory-hygiene.sh`
  exits 2 naming the key and its legal values; for absent, blank, `shards` and `builds` the shell and
  the Python reader report the same mode.
  Red when: the shell reads an unrecognised value as `shards` while the Python reader refuses it.
- **AC10** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over this repo with the BASE
  engine and then with this unit's engine, the two outputs are byte-identical.
  Red when: any builds-mode branch runs under `shards`, including a new announcement line.
  cost: two full engine runs, minutes each.
- **AC11** — When the builds-mode fixture lists its family view in `curation-debt.txt`, the stale-entry
  guard fails naming that row.
  Red when: the view still records a waived finding from a check it has left, so a row that hides
  nothing stays green.
- **AC12** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, the HYGIENE and
  TEMPLATE-SPEC instances match their templates; `memory/HYGIENE.md` names both modes for checks 4, 6,
  7, 8, 10, 13, 15, 20 and 24; and `memory/TEMPLATE-SPEC.md` names `closes` and `advances` as
  builds-mode header verbs.
  Red when: the instance is edited and the template is not, which the parity leg exists to catch.
- **AC13** — When `python3 tools/memory-tree/check-arms.py --check` runs after the unit, the new check 6
  branch is armed by its self-test assertion and the engine's `ARMS_FLOORS` entry has moved by the
  branches added.
  Red when: the branch lands unarmed and the floor stays, so a deletion of the new remedy passes.
- **AC14** — When `bash tools/check-install-prefix.sh` runs at this unit's commit, it passes;
  `grep -c 'corpus_ids.py' tools/install-prefix-waivers.txt` prints 0, and both fixture lines in
  `tools/memory-tree/corpus_ids.py` carry `gov:root-fixture` with a reason.
  Red when: a line added above line 935 leaves the two position-keyed rows pointing at shifted lines,
  which the gate reports as stale waivers and two unwaived hits on the bar while every unit-pass
  observation stays green.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `corpus-ids selftest` · `row-grammar selftest` · `kit/dogfood doc parity` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `install-prefix (shipped surface)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · builds-mode and shards-mode scratch trees for checks 4, 6, 7, 8 and 10, the curation-debt view row, and a typo'd mode value · the engine's arms floor, by the branches added
New arm: `tools/memory-tree/corpus_ids.py` `--selftest` · a post-cutoff and a pre-cutoff ask anchored in a second folder, and a dead path in an ask and in a view · none
New arm: `tools/memory-tree/row_grammar.py` `--selftest` · a builds-mode tree with a view, a family archive and a duplicated decision id · none

## 8. Open questions

- **F1** — Who reports a tracked family archive under `builds`? (a) Each of checks 10, 20 and 24, as
  today. (b) Check 9's archive guard alone, with check 10 counting what it left. RESOLVED (agent,
  2026-09-14, delegated): (b); one fact, one finding, and the count line keeps the deferral visible.
- **F2** — What does check 13 do with a blank or malformed `ASK_CUTOFF` under `builds`? (a) Skip
  nothing, redding the 27 legacy anchors. (b) Skip every ask row and say so. The parser unit returns
  a blank cutoff as V15 and a malformed one as V16, and the view unit's `--check` reports both, so
  (a) adds 27 findings to one misconfiguration that is already red. RESOLVED (agent, 2026-09-14,
  delegated): (b).
- **F3** — Does check 3 need a builds-mode change? FACT-QUESTION · Probe: its two whitelists at
  `tools/memory-tree/check-memory-hygiene.sh:483` and `:490` against the builds-mode tree shape. The
  probe could have found `BACKLOG.md` refused had check 3 descended into build folders. RESOLVED
  (agent, 2026-09-14, delegated): no; it admits `backlog/<FAMILY>.md` and never descends into a build
  folder, which is check 4's job.
- The rulings this unit executes: D3 the view leaves the size cap; D9 asks keep their path grading;
  D12-g the check 13 skip is scoped to pre-cutoff asks — all RESOLVED (owner, 2026-09-13).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.
- rev-2 · 2026-09-14 · S6 · S14 · §3 · §4 · §7 · §8 · AC5 · AC14 · folds spec-audit round 1. G2 M1
  (47) and M2 (7): S6, F2's premise and AC5 name V15 and V16. G2 M11 (58): S14 and AC14 convert the
  two `corpus_ids.py` install-prefix waivers to in-line markers, and §7 gains
  `install-prefix (shipped surface)`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "switch a hygiene check population by a declared conf
mode"` named the kit's one conf parser, `parse_conf` in `tools/memory-tree/corpus_ids.py`, and the
per-module `load_conf` seams; it reports the shell layer unscanned. Those are the seams this unit
extends, plus two found by reading source: the project-key preset and validation block that
`ROTATION_MODE` already uses in `tools/memory-tree/check-memory-hygiene.sh` (TOOL-cSpliceWarden-1), and
the delegation of a corpus walk to `row_grammar.py` that check 24 established (TOOL-cSpliceWarden-6).
Recall returned both, `TOOL-aFoldedQuarry-5` for the corpus module's own rule that it declares no
grammar it does not own, and the cGradedDebt partition that keeps a listed file inside checks 6, 7
and 8.

Where the design and BASE disagree, re-read at `abac6d59`. Design §6 says check 10's silent
`continue` should announce; `TOOL-cSpliceWarden-2` already made zero-or-many a named finding, so the
only change left is S9's builds-mode deferral. Design §6 has check 8's population guard "learn the
mode" using `PRE_STATUSY`; that precondition already counts `BACKLOG.md`, which is exactly why the
guard would fire under `builds` without S5. Check 24 did not exist when the design was measured; S8
brings it under the same `row_docs()` switch as check 20. The switch-over spec lists check 3 among the
checks this unit keeps green; F3 finds it needs no change.

Recall terms used: `check 8 status vocabulary check 13 collision def_builds check 15 present corpus check 20 row_docs curation-debt ROTATION_MODE`
