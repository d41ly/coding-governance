# TOOL-dDerivedDocket-16 — driver ask-awareness: the asks key, preflight and plan

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

Every unattended verb is addressed by slug, and an id passed where a slug belongs fails with a
message about a missing README (`tools/unattended/unattended.sh:1358`). Teach the driver to take an
ask mandate from the one place the owner controls, a build README's `asks:` line, pin it with the
properties that stop a run from choosing its own asks, plan units against it, and send every
ids-shaped invocation to the owner's one-command scaffold instead of guessing (owner ruling D12-a).

## 2. Scope (IN)

- **S1** `ASKS_CMD` in the conf: the kit default is blank, meaning not adopted and announced as a
  skip; the key joins `tools/unattended/.unattended.conf.example`, protocol §8's table in both
  copies, and leg check 22's join. Its contract is the `--asks` invocation of §4. Observed by AC13.
- **S2** The authorization scan (`tools/unattended/unattended.sh:1375-1381`) also reads `asks:` from
  the same blob. An `asks:` key while `ASKS_CMD` is blank refuses `--preflight`, which is term T1 of
  unit 17 enforced where it belongs. Observed by AC5.
- **S3** Preflight pins three facts for a record whose README carries `asks:`: `m-base:`, the
  merge base of the pinned `anchor-sha:` and `HEAD` at preflight (fix F4); `asks:`, the line as read;
  and `asks-ready:`, one `<id>=<grade>` pair per mandated id. Observed by AC3.
- **S4** Property P5 (design §19.2): every mandated id has its ask row `- <ID> · filed ` in its home
  folder's `BACKLOG.md` at `m-base:`, read with one `git show` per folder and a line match placed in
  `tools/unattended/lib-unattended.sh` for unit 18 to share. Property P6: the README's `asks:` line
  is byte-equal at `HEAD` on every later preflight and resume, and no verb adds to the mandated set.
  Observed by AC3 and AC4.
- **S5** READY at `m-base:` through one bounded `ASKS_CMD` call. Its row count must equal the
  mandate's size or preflight refuses as a DEAD PROBE; a mandate whose every id grades `no` refuses
  and prints the failing rules. The live-build set the call receives is derived from every tracked
  run-state file's phase through unit 4's one phase reader. Observed by AC6 and AC14.
- **S6** Ids and filing homes (rulings D12-a and D12-f). A verb value shaped like an id, a value
  carrying both a slug and ids, and a slug whose folder at BASE holds only a `BACKLOG.md` all refuse
  under code 6 and print the scaffold recipe
  `gen_build_index.py --new-build <new-slug> --asks <ids>`, writing nothing. Observed by AC1 and AC2.
- **S7** The roster is the authored units table together with the folder's `unit` asks, read by a
  line match on the folder's `BACKLOG.md`. `--plan` lists planned units as MISSING even over zero
  specs, in numeric sequence order, and code 19 fires only when the roster is empty too. Observed by
  AC7 and AC8.
- **S8** `--plan --asks`, an output mode like `--paths`: one ASK row per mandated ask and per live
  ask filed in the folder, with its status, grade, covering unit or disposition, and rank; under
  `--paths` an ASK row carries exactly three TAB fields. The new `next:` shape of §4 prints only
  after every unit shape, the existing literals stay byte-identical, and `--status` and `--resume`
  read the same next. Two live units of one build closing one ask print a refusal row. Observed by
  AC9.
- **S9** `--dispatch` refuses under code 49 a unit that closes an ask A while a mandated ask A holds
  on is not terminal. Observed by AC10.
- **S10** `--rescope` accepts retiring a unit whose id is a `unit` ask, and refuses an add whose id
  equals a filed ask that is not `unit`. Observed by AC11.
- **S11** Preflight prints one notice when `BACKLOG_MODE` differs between the anchor's tree and
  `HEAD`'s. Observed by AC12.
- **S12** Every new `fail` branch gets an arm in `tools/unattended/unattended.test.sh`,
  `ARMS_FLOORS` moves in the same commit, and the unattended suites run once at the unit's end
  (owner ruling D12-h). Observed by AC13.

## 3. Non-goals (OUT)

- The READY predicate, the `--tsv` projection and the scaffold are unit 15's. The driver reads the
  projection and prints the scaffold's command; it grades nothing itself and holds no second fold.
- The ask grammar is unit 6's; P5's line match spells only the prefix design §19.2 fixes.
- The Definition-of-Done item and the landing freeze are unit 17's; the leg's second opinions on
  these facts are unit 18's; honouring `may:` is unit 19's.
- The Skill's routing rows, orientation steps, owner-call parking and the companion guide are unit
  20's. This unit writes only the protocol §8 row that leg check 22 requires.
- Writing `order <n>` into spec headers. `--plan --asks` prints the rank of design §19.4; the run
  writes the verb, as it does today.
- Gov's `ASKS_CMD` stays blank until unit 35 arms it, so every existing run takes the not-adopted
  path unchanged.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-4` — the one derived phase reader, which S5 uses to decide
  which builds hold a live run. Added by this spec; that unit's spec owes the matching line.
- **consumes-from** `TOOL-dDerivedDocket-15` — READY at a pinned rev with a target folder and a
  live-build set, the eleven-field `--tsv` projection, and the `--new-build` command S6 prints.
- **hands-off** `TOOL-dDerivedDocket-17` — `ASKS_CMD` and the pinned `asks:`, `asks-ready:` and
  `m-base:` facts that the `asks-disposed` terms grade.
- **hands-off** `TOOL-dDerivedDocket-18` — the pinned facts, `ASKS_CMD`, and the P5 line matcher in
  the kit library, which the leg's second opinions re-read.
- **hands-off** `TOOL-dDerivedDocket-19` — the one-scan front-matter parse that `may:` joins, the
  pinned-fact seam, and the resolved mode.
- **hands-off** `TOOL-dDerivedDocket-20` — every driver behaviour the Skill and the companion guide
  describe: the recipe refusal, the pinned facts, `--plan --asks` and the UNDECIDED shape.
- **hands-off** `TOOL-dDerivedDocket-35` — the `ASKS_CMD` contract and its example entry, which that
  unit sets gov's value against, and P5 at preflight, which it stages RED on the real tree.

## 4. Design

### What the owner's commit decides, and what the run cannot move

| Fact | Read from | Pinned when | Moved by |
|---|---|---|---|
| `asks:` | the README blob at BASE, in the one scan | preflight | nothing; P6 refuses a changed line at `HEAD` |
| `m-base:` | `merge-base(anchor-sha, HEAD)` at preflight | preflight | nothing; unit 18 re-derives it from `anchor-sha:` |
| `asks-ready:` | one `ASKS_CMD` call at `m-base:` | preflight | nothing; unit 17 keys its hardening on it |

A run cannot satisfy P5 by construction, because the rows must already sit in a tree the remote's
anchor reached; an ask filed in an unpushed commit is not mandatable. That is design §19.2's
argument, unchanged.

### The `ASKS_CMD` contract

The driver runs the declared value with arguments appended:
`<ASKS_CMD> --tsv --ready <ids> --target <slug> --live-builds <slugs> --at <m-base>`. Gov's value,
set by unit 35, is the generator's `--asks` mode. The output is unit 15's projection: exactly eleven
TAB fields led by `ask`, then `examined` and a count. Anything else is a parse refusal rather than a
row, so a column change in the producer reads as a dead probe and never as a pass. The call runs
through `run_bounded`, and a bound breach is named as never answered, which is not the same fault
as a red.

### The live-build set

A foreign live spec closing a mandated ask is a claim only if its build's run is live (fix F5).
The driver derives the set from every tracked `memory/builds/*/RUN.md` through unit 4's
`derived_phase()`, which KF15 makes the one reader every phase question goes through; a phase
outside `PHASES_TERMINAL` is live. A landed run whose record has not yet been rotated reads live,
which grades its ask `no` rather than admitting a duplicate: the conservative direction.

### Ids-shaped invocations

A verb value matching the id shape the conf's `FAMILIES` spell, or carrying whitespace, is not a
slug. The refusal keeps code 6 because design §19.1 K1 already routes an id there, and it prints
three lines: the recipe with the tokens exactly as typed and `<new-slug>` left for the owner to
mint, the rule that the owner lands the scaffolded README, and `/unattended <slug>` as the second
legal form. The driver never parses the id list itself: the scaffold parses it all or nothing (fix
F2), so there is one parser. For a filing home, the recipe lists that folder's live asks as the
`--asks --build <slug>` print mode reports them at BASE.

### Plan, next and rank

The UNDECIDED shape is `next: <id> (UNDECIDED - plan a unit that closes it, or dispose it)`, printed
only when no unit shape remains. `next: none - every tracked spec is terminal` is never printed
while a mandated ask, or a live ask filed in this folder, has no covering unit and no disposition.
Rank follows design §19.4: hold edges between mandated asks lifted to the units that close them,
then severity, then the `asks:` listing order, then numeric sequence. MISSING units sort by numeric
sequence, never the string order that puts `-10` before `-2` (`missing_units`,
`tools/unattended/unattended.sh:1917-1934`).

### Fail codes

Code 6 keeps the ids and filing-home refusals. The refusals of S2, S4 and S5 and the rescope refusal
take new driver codes, and the dispatch hold refusal takes code 49 beside the order gate it joins
(`tools/unattended/unattended.sh:4699-4720`). New numbers are allocated at build time as the next
free integer, because other units of this build allocate codes concurrently.

### Rollout

Dark. Every new branch sits behind a non-blank `ASKS_CMD` or an `asks:` key, and no gov README
carries one. The protocol §8 row is about 250 bytes against a guide cap of 61440 B at 57815 B, which
is shared with at least five units of this build.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `ASKS_CMD` | conf key | screaming snake, as every key there |
| `asks:`, `asks-ready:`, `m-base:` | README key and run facts | lower kebab, as every fact there |
| `--asks` on `--plan` | output mode | flag, as `--paths` is |
| the P5 line matcher and any new shell function | kit library and driver | lexicon shell function cell, checked with `lexicon.py --suggest` |
| new driver refusal codes | integers | allocated at build time |

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/lib-unattended.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.sh` for check 22's join ·
`tools/unattended/.unattended.conf.example` · `tools/unattended/PROTOCOL.template.md` ·
`memory/guides/UNATTENDED-PROTOCOL.md` · `.memory-tree.conf` for `ARMS_FLOORS` ·
`memory/map/features/unattended.md`.

### Alternatives rejected

- **The zero-commit ids start, E2.** Rejected by owner ruling D12-a: the run would write the folder
  that authorizes it.
- **A driver-side id list parser.** Two parsers of one grammar disagree silently; the scaffold is the
  one parser, and the driver passes the tokens through.
- **Reading status from the view.** The view lists live asks only, and preflight must grade terminal
  ones too.

## 5. Production-readiness checklist

- security — the mandate is read from a README blob at BASE and ask rows at `m-base:`, both beyond
  the run's reach; `ASKS_CMD` is a declared command, never ask text; nothing here executes a `seen`
  command.
- perf / scale — one `git show` per mandated home folder, one bounded `ASKS_CMD` call, one phase read
  per tracked run-state file at preflight.
- error / empty / loading states — no `asks:` key is today's path, unchanged; a short witness is a
  DEAD PROBE; an all-`no` mandate refuses with the rules; an ids value refuses with the recipe.
- observability — preflight prints the pinned facts and the ready counts; `--plan --asks` prints
  every mandated ask's standing.
- risks — a foreign run that landed without rotating its record reads live, which costs an ask it
  could have taken; `m-base:` equality depends on preflight staging the record before any other
  commit, as unit 18 records.
- testing — one arm per branch in `tools/unattended/unattended.test.sh`, each observed RED; the
  unattended suites run once at the unit's end and are read against unit 1's baseline.
- migration — additive; every existing record takes the no-mandate path.
- user docs — the protocol §8 row here; the Skill and the companion guide are unit 20's.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --preflight` receives an id-shaped value in
  `tools/unattended/unattended.test.sh`, it refuses under code 6, prints the `--new-build` recipe
  with the value as typed, and leaves `git status --porcelain` unchanged.
  Red when: the value is looked up as a folder and the message names only a missing README.
- **AC2** — When the fixture's slug names a folder holding only a `BACKLOG.md` at BASE, preflight
  refuses under code 6 and the recipe lists that folder's live asks.
  Red when: the run writes a README or a record into the filing home, which ruling D12-f forbids.
- **AC3** — When preflight runs over a fixture README carrying `asks: EXMP-aFoo-3..4` with both rows
  filed at the merge base, the record gains `m-base:`, `asks:` and `asks-ready:`; with one row filed
  only after the merge base, preflight refuses naming the id and the blob it read.
  Red when: P5 reads the working tree, so a row filed after the run began satisfies it.
- **AC4** — When `--resume` runs after the README's `asks:` line changed at `HEAD`, it refuses naming
  both lines.
  Red when: resume re-reads the mandate from `HEAD`, so the ask set grows mid-run.
- **AC5** — When the fixture README carries `asks:` and `ASKS_CMD` is blank, preflight refuses naming
  the key.
  Red when: preflight pins a mandate that nothing can grade, which unit 17 then meets vacuously.
- **AC6** — When the fixture's `ASKS_CMD` prints one row fewer than the mandate, preflight refuses as
  a DEAD PROBE naming the missing id; when every mandated id grades `no`, it refuses and prints each
  id's failing rules.
  Red when: the driver iterates the rows it received, so a missing id is never graded.
- **AC7** — When `--plan` runs over a fixture whose roster plans `EXMP-tRun-2` and `EXMP-tRun-10` with
  no spec, it lists both as MISSING with `-2` first and prints
  `next: EXMP-tRun-2 (MISSING - spec it first)`; code 19 fires only for an empty roster with no spec.
  Red when: code 19 still fires with a non-empty roster, which is design §19.1 K4.
- **AC8** — When the fixture folder files a `unit` ask with no roster row, `--plan` lists it as
  MISSING and `--close` refuses the build-complete term that requires every roster unit.
  Red when: the `unit` ask is invisible to the roster, so the build closes without it.
- **AC9** — When `--plan --asks --paths` runs over a fixture with an undecided mandated ask, its ASK
  row has exactly three TAB fields, `next:` reads the UNDECIDED shape, and
  `bash tools/unattended/check-unattended.sh` check 30 stays green on the unchanged literals.
  Red when: an ASK row carries four fields, so a harness that dispatches four-field rows builds an
  ask as though it were a unit.
- **AC10** — When `--dispatch` names a unit whose spec closes an ask held on a mandated ask that is
  still live, it refuses under code 49 naming both asks.
  Red when: only declared `order` verbs block, so a hold edge between asks is ignored.
- **AC11** — When `--rescope --act add` names an id equal to a filed ask without `unit`, it refuses;
  `--rescope --act retire` on a unit whose id is a `unit` ask succeeds.
  Red when: the add succeeds, and verdict V9 reds the tree only after the unit exists.
- **AC12** — When the anchor's `.memory-tree.conf` is in shards mode and `HEAD`'s is in builds mode,
  preflight prints one notice naming both.
  Red when: the mode change passes silently, so a run plans against asks its BASE never filed.
- **AC13** — When `bash tools/unattended/check-unattended.sh` runs, check 22's join is green with
  `ASKS_CMD` in the example conf and in both protocol copies; when
  `bash tools/unattended/run-unattended-gates.sh --selftests` runs once at the unit's end, every arm
  this unit added passes, each observed RED with its fix unstaged, and no failure is NEW against
  unit 1's baseline.
  Red when: the key is set by a project and documented nowhere, or an arm lands unobserved.
  cost: one run of the unattended suites, the unit's single sanctioned run (D12-h).
  permission: the leg runs named here and in AC9 are observed at the one post-build bar, because
  unit passes run no gate legs (fix F7); ruling D12-h lifts the suites only.
- **AC14** — When a foreign live spec closes a mandated fixture ask and its build's run-state file
  reads a terminal phase through `derived_phase()`, the pinned `asks-ready:` grade is `yes`; with a
  live phase it is `no`.
  Red when: the live-build set is read from a recorded phase string rather than the shared reader,
  so a HELD run reads as abandoned and its claim is ignored.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `kit/dogfood doc parity` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · one fixture per refusal and output shape in §6, with a local bare remote for the anchor · `ARMS_FLOORS` for `tools/unattended/unattended.sh`

## 8. Open questions

- **F1 — which unit declares the edge with unit 19?** The brief's table has this unit consuming from
  unit 19, which is ordered after it. RESOLVED (agent, 2026-09-14, delegated): this unit hands off to
  unit 19, matching unit 19's own resolution; the dependency runs from the scan this unit extends.
- **F2 — where the live-build set comes from.** Options: (a) the memory-tree kit reads run-state
  files; (b) the driver derives it through unit 4's phase reader and passes it to READY; (c) no set,
  so every foreign live spec blocks. (a) couples one kit to another's file; (c) leaves fix F5 unmet.
  RESOLVED (agent, 2026-09-14, delegated): (b).
- **F3 — which code an ids refusal carries.** RESOLVED (agent, 2026-09-14, delegated): code 6, where
  design §19.1 K1 measured an id already landing, with a message that routes it; a new code would
  leave the old message reachable for the same input.
- **F4 — does an ids invocation still parse the list?** Fix F2 asks for all-or-nothing parsing, and
  owner ruling D12-a moved the list into the scaffold. RESOLVED (agent, 2026-09-14, delegated): the
  scaffold is the one parser and the driver passes tokens through unchanged.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from design §19.2 and §19.4, fixes F2, F4 and F5, and rulings
  D12-a, D12-f and D12-h. Reverses the brief's edge between this unit and unit 19 (§8 F1), adds
  consumes-from unit 4, whose `derived_phase()` supplies the live-build set and whose spec owes the
  matching hands-off line, and adds hands-off unit 35, whose spec declares the consuming end.

## 10. Reuse audit

The seams are the driver's own: the one-scan `awk` in `check_authorization`
(`tools/unattended/unattended.sh:1375-1381`), the `set_fact` pinning beside `playbook:` and
`pieces:` (`:2728-2741`), `roster_ids` and `missing_units` (`:1762-1777`, `:1917-1934`), `plan_row`'s
two shapes (`:2020-2023`), the order gate at `--dispatch` (`:4699-4720`), and `run_bounded` for the
witness call. `python tools/codebase-map/reuse_lookup.py "driver pins a fact at preflight and plans a
roster"` returned `plan` in `tools/memory-tree/gen_build_index.py`, the `.unattended.conf` affordance
seam and `cmd_plan` in govkit, and states `.sh` is unscanned, so it is blind to the driver; the
`unattended` dossier names no second planner. Recall returned `TOOL-dHonouredPark-4` (why `--plan`
reads the rendered region in build order) and `TOOL-cBriefedPilot-6` (the roster join this extends).

Where the design and BASE disagree: design §19.1 cites fail 6 at `:1357-1360`, which at BASE is
`tools/unattended/unattended.sh:1358`; the driver's other citations hold, because `unattended.sh` did
not change between `09a22d2b` and `abac6d59`. Design §19.2's E2 and the prompt-record subset check
are superseded by ruling D12-a.

Recall terms used: `roster_ids preflight authorized-by second anchor fail 6 plan next MISSING
rescope dispatch order`
