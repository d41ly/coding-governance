# TOOL-dDerivedDocket-16 — driver ask-awareness: the asks key, preflight and plan

**Status:** SPECCED · rev-3 · 2026-09-16 · node d · Tier-2 · base abac6d59 · streams tooling · order 16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 |

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
  copies, and leg check 22's join. Its contract is the three call shapes of §4, each appended to the
  declared value. Observed by AC13 and AC15.
- **S2** The authorization scan (`tools/unattended/unattended.sh:1375-1381`) also reads `asks:` from
  the same blob. An `asks:` key while `ASKS_CMD` is blank refuses `--preflight`, which is term T1 of
  unit 17 enforced where it belongs. A README carrying `asks:` whose resolved mode is not `slug`
  refuses `--preflight` under a new driver code and writes nothing: `prompt` and `recipe` resolve at
  the second anchor (`SECOND_ANCHOR_MODES`, `tools/unattended/unattended.sh:497`), which the run can
  write, and choosing WHICH filed asks is what ruling D12-a took from the run. This is the driver twin
  of unit 18 S5 and mirrors unit 19 S2. Observed by AC5 and AC16.
- **S3** Preflight pins three facts for a record whose README carries `asks:`: `m-base:`, the
  merge base of the pinned `anchor-sha:` and `HEAD` at preflight (fix F4); `asks:`, the line as read;
  and `asks-ready:`, one `<id>=<grade>` pair per mandated id. Observed by AC3.
- **S4** Property P5 (design §19.2): every mandated id has its ask row `- <ID> · filed ` in its home
  folder's `BACKLOG.md` at `m-base:`, read with one `git show` per folder and a line match placed in
  `tools/unattended/lib-unattended.sh` for unit 18 to share. Property P6: the README's `asks:` line
  is byte-equal at `HEAD` on every later preflight and resume, and no verb adds to the mandated set.
  Observed by AC3 and AC4.
- **S5** READY at `m-base:` through one bounded `ASKS_CMD` call that passes no `--live-builds`, so
  every foreign live closing spec is a claim (§4). Its row count must equal the mandate's size or
  preflight refuses as a DEAD PROBE; a mandate whose every id grades `no` refuses and prints the
  failing rules. For each mandated ask graded `no` on R2 by a foreign live spec, preflight prints one
  report-only line naming the spec, its build, and whether that build's tracked run-state file reads
  terminal through unit 4's `derived_phase()`; the line pins nothing and admits nothing. Observed by
  AC6 and AC14.
- **S6** Ids and filing homes (rulings D12-a and D12-f). A verb value shaped like an id, a value
  carrying both a slug and ids, and a slug whose folder at the first anchor's merge-base holds only a
  `BACKLOG.md` all refuse under code 6 and print the scaffold recipe
  `gen_build_index.py --new-build <new-slug> --asks <ids>`, writing nothing. Both tests run before
  any other preflight refusal can answer (§4). Observed by AC1 and AC2.
- **S7** The roster is the authored units table together with the folder's `unit` asks, read by a
  line match on the folder's `BACKLOG.md`. `--plan` lists planned units as MISSING even over zero
  specs, in numeric sequence order, and code 19 fires only when the roster, the specs and the pinned
  `asks:` mandate are all empty. A mandate-only build — unit 15's scaffold writes an empty roster
  pair, no spec and an `asks:` line — plans from its mandate. Observed by AC7, AC8 and AC17.
- **S8** `--plan --asks`, an output mode like `--paths`: one ASK row per mandated ask and per live
  ask filed in the folder, with its status, grade, covering unit or disposition, and rank; under
  `--paths` an ASK row carries exactly three TAB fields. The new `next:` shape of §4 prints only
  after every unit shape, the existing literals stay byte-identical, and `--status` and `--resume`
  read the same next. Two live units of one build closing one ask print a refusal row. On a
  mandate-only build, `--plan --asks` prints one ASK row per mandated ask and
  `next: <id> (UNDECIDED …)`. Observed by AC9, AC17 and AC18.
- **S9** `--dispatch` refuses under code 49 a unit that closes an ask A while a mandated ask A holds
  on is not terminal. Observed by AC10.
- **S10** `--rescope` accepts retiring a unit whose id is a `unit` ask, and refuses an add whose id
  equals a filed ask that is not `unit`. Observed by AC11.
- **S11** Preflight prints one notice when `BACKLOG_MODE` differs between the anchor's tree and
  `HEAD`'s. Observed by AC12.
- **S12** Every new `fail` branch gets an arm in `tools/unattended/unattended.test.sh`,
  `ARMS_FLOORS` moves in the same commit, and the unattended suites run once at the unit's end under
  `--attribute <BASE>` (owner ruling D12-h). Observed by AC13.

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
- Widening `researched:M12:prompt` and `solution-tested:M12:prompt` (`DIRECTIVES_CORE`,
  `tools/unattended/unattended.sh:473`) to a record that pins `asks:`. An ask-driven run resolves to
  `slug` mode by ruling D12-a, and owner ruling TOOL-aPromptedMandate-4 scopes both directives to
  prompt-authorized runs, so neither binds it. Whether they should is parked for the owner, because
  either answer changes or restates the reach of an owner ruling. Until then the run's per-ask
  orientation (unit 20 S6) is the only step that examines each ask before planning.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-4` — the one derived phase reader, through which S5's
  report-only line labels a claiming build terminal or not. Added by this spec; that unit's spec owes
  the matching line.
- **consumes-from** `TOOL-dDerivedDocket-15` — READY at a pinned rev with a target folder (this
  driver passes no live-build set), the eleven-field `--tsv` projection, the `--new-build` command
  S6 prints, and the scaffold's key list, which is the shape a mandate-only build starts in.
- **consumes-from** `TOOL-dDerivedDocket-1` — `run-unattended-gates.sh --attribute <BASE>`, whose
  attributed verdict, `verdict clean` with every inherited suite filed, is the only criterion the
  unattended suites, red at BASE (TOOL-aHoistedPass-36), can meet.
- **consumes-from** `TOOL-dDerivedDocket-7` — the `--asks --build <slug>` table form that call shape
  3 prints, and the stdout rule shapes 1 and 2 rely on.
- **hands-off** `TOOL-dDerivedDocket-17` — `ASKS_CMD` and the pinned `asks:`, `asks-ready:` and
  `m-base:` facts that the `asks-disposed` terms grade, and the P5 line matcher that enumerates F,
  and the one TSV parse the witness reuses.
- **hands-off** `TOOL-dDerivedDocket-18` — the pinned facts, `ASKS_CMD`, and the P5 line matcher in
  the kit library, which the leg's second opinions re-read, and S2's non-`slug` refusal, the driver
  twin of unit 18 S5, and the READY call shape S8 re-runs at `m-base:`, a pure function of pinned
  inputs because no live-build set is passed.
- **hands-off** `TOOL-dDerivedDocket-19` — the one-scan front-matter parse that `may:` joins, the
  pinned-fact seam, and the resolved mode.
- **hands-off** `TOOL-dDerivedDocket-20` — every driver behaviour the Skill and the companion guide
  describe: the recipe refusal, the pinned facts, `--plan --asks` and the UNDECIDED shape.
- **hands-off** `TOOL-dDerivedDocket-35` — the `ASKS_CMD` contract and its example entry, which that
  unit sets gov's value against, and P5 at preflight, which it stages RED on the real tree.
- **hands-off** `TOOL-dDerivedDocket-24` — the `ASKS_CMD` key and its projection contract, which that
  unit's auto-file calls to read its staged rows back, and to read back an earlier auto-filed id it
  may reuse.

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

The driver runs the declared value with arguments appended, in exactly three shapes:

1. READY at preflight: `<ASKS_CMD> --tsv --ready <asks: ids> --target <slug> --at <m-base>`;
2. the status witness at close and at the freeze (unit 17),
   `<ASKS_CMD> --tsv --ready <ids of M ∪ F> --target <slug> --at <rev>`, `<rev>` being the commit
   the verb examines;
3. the filing-home listing at refusal: `<ASKS_CMD> --build <home> --at <merge-base(ASHA, HEAD)>`,
   whose table the refusal prints verbatim.

Shapes 1 and 2 are parsed as unit 15's projection; shape 3 is printed and never parsed. While
`ASKS_CMD` is blank, the filing-home refusal prints the recipe with `<ids>` left for the owner, and in
place of the listing one line saying `ASKS_CMD` is not adopted, naming the key and the generator's
`--asks --build <home>` form to run by hand. It never lists asks from a local parse, because only the
fold knows which are live. Naming the generator in a refusal's hint has precedent in the driver's own
repair hints (`tools/unattended/unattended.sh:1525`, `:2011`, `:2042`).

A later caller adds one more shape: the inherited-red auto-file of unit 24 runs
`<ASKS_CMD> --tsv --ready <ids> --target <slug>` over the WORKING TREE, for two reads. It reads its
staged rows back under their new ids; and before it files for a leg, it reads back an earlier
auto-filed id for the same leg red at the same rev, which an earlier Close sequence may already
have committed, to decide whether that OPEN ask is reused instead. It carries no `--at`,
because a new row is staged and exists at no rev and the reuse reads the tree a new row would join,
and no `--live-builds`, because only a row's status, severity and home are read; it is parsed as
shapes 1 and 2 are.

Gov's value, set by unit 35, is the generator's `--asks` mode. The output is unit 15's projection:
exactly eleven TAB fields led by `ask`, then `examined` and a count. Anything else is a parse refusal
rather than a row, so a column change in the producer reads as a dead probe and never as a pass. The
call runs through `run_bounded`, and a bound breach is named as never answered, which is not the same
fault as a red.

### The live-build set

A foreign live spec closing a mandated ask is a claim. Fix F5 admits it as stale when its build's run
is not live, but no tree the driver can read shows every live run: a run's record exists only on its
own branch until it lands, and this build's own folder was absent from `main` and `origin/main` while
it ran. A set derived from tracked run-state files holds the landed-but-unrotated records and misses
every run in flight, which admits exactly the double claim F5 exists to stop. So the driver passes no
`--live-builds`. Every foreign live spec is a claim, and a stale one costs an ask this run could have
taken: that ask grades `no`, orientation parks it as an owner call (unit 20), and the report-only line
names the build whose tracked record reads terminal, so the owner can retire its stale spec.
`--live-builds` stays in unit 15 for a caller that can observe every live run; the driver is not one.

### Ids-shaped invocations

A verb value matching the id shape the conf's `FAMILIES` spell, or carrying whitespace, is not a
slug. The refusal keeps code 6 because design §19.1 K1 already routes an id there, and it prints
three lines: the recipe with the tokens exactly as typed and `<new-slug>` left for the owner to
mint, the rule that the owner lands the scaffolded README, and `/unattended <slug>` as the second
legal form. The driver never parses the id list itself: the scaffold parses it all or nothing (fix
F2), so there is one parser. For a filing home, the recipe lists that folder's live asks as the
`--asks --build <slug>` print mode reports them at the first anchor's merge-base (call shape 3).

Order. The id-shape test — a value matching the `FAMILIES` id shape, carrying whitespace, or mixing
a slug and ids — runs FIRST in `--preflight`, before `check_slug`
(`tools/unattended/unattended.sh:1060-1070`) and before any anchor work, because it needs no tree;
`check_slug`'s fail 1 therefore never answers an ids value. The filing-home test runs next, once the
anchor is observed, against the first anchor's merge-base `merge-base(ASHA, HEAD)` and before
`trusted_base`: under `ANCHOR_SCOPE=published` a README absent at that merge-base widens to the
second anchor (`:903-915`), and an unpushed branch is then refused with fail 32's push instruction
(`:863`), which carries no recipe and, once followed, writes to the remote.

### Plan, next and rank

The UNDECIDED shape is `next: <id> (UNDECIDED - plan a unit that closes it, or dispose it)`, printed
only when no unit shape remains. `next: none - every tracked spec is terminal` is never printed
while a mandated ask, or a live ask filed in this folder, has no covering unit and no disposition.
Rank follows design §19.4: hold edges between mandated asks lifted to the units that close them,
then severity, then the `asks:` listing order, then numeric sequence. MISSING units sort by numeric
sequence, never the string order that puts `-10` before `-2` (`missing_units`,
`tools/unattended/unattended.sh:1917-1934`).

Under `--paths` an ASK row is exactly `ASK<TAB><id><TAB><summary>`, the summary
`status=<S>;ready=<G>;cover=<unit id | disposition verb | ->;rank=<n>` in that key order (design
§19.4 names a `k=v;…` summary and no keys). A live ask filed in the folder but not mandated carries
`ready=-`. Two live units of one build closing one ask print
`ASK<TAB><id><TAB>refused=duplicate-closer;units=<u1>,<u2>`, still three fields.

### Fail codes

Code 6 keeps the ids and filing-home refusals. The refusals of S2, S4 and S5 and the rescope refusal
take new driver codes, S2 now making two refusals, each its own new code; and the dispatch hold
refusal takes code 49 beside the order gate it joins (`tools/unattended/unattended.sh:4699-4720`).
New numbers are allocated at build time as the next free integer, because other units of this build
allocate codes concurrently.

### Rollout

Dark. Every new branch sits behind a non-blank `ASKS_CMD` or an `asks:` key, and no gov README
carries one. The protocol §8 row (S1) names the key, its blank default and "called in the shapes
listed in `UNATTENDED-ASKS.md`", so the argument lists live in one carrier; the row is about 250
bytes against a guide cap of 61440 B at 57815 B, which is shared with at least five units of this
build.

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
- perf / scale — one `git show` per mandated home folder, one bounded `ASKS_CMD` call, and one phase
  read per build a report-only claim line names at preflight.
- error / empty / loading states — no `asks:` key is today's path, unchanged; a short witness is a
  DEAD PROBE; an all-`no` mandate refuses with the rules; an ids value refuses with the recipe.
- observability — preflight prints the pinned facts and the ready counts; `--plan --asks` prints
  every mandated ask's standing.
- risks — every foreign live spec is a claim, so a stale one costs an ask this run could have taken;
  it is named, never admitted. `m-base:` equality depends on preflight staging the record before any
  other commit, as unit 18 records. An ask-driven run carries no M12 obligation, and a `legacy` ask
  carries no mechanical acceptance, so orientation alone stands between such an ask and a unit
  (parked, §3).
- testing — one arm per branch in `tools/unattended/unattended.test.sh`, each observed RED; the
  unattended suites run once at the unit's end and are read through unit 1's `--attribute <BASE>`.
- migration — additive; every existing record takes the no-mandate path.
- user docs — the protocol §8 row here; the Skill and the companion guide are unit 20's.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --preflight` receives an id-shaped value, and
  separately a two-token value, in `tools/unattended/unattended.test.sh`, each under the kit default
  `ANCHOR_SCOPE` and under `ANCHOR_SCOPE=published` on an unpushed branch, it refuses under code 6,
  prints the `--new-build` recipe with the value as typed, and leaves `git status --porcelain`
  unchanged.
  Red when: the value is looked up as a folder, or answered first by `check_slug`'s fail 1 or the
  second anchor's fail 32, so the message names a missing README, the slug grammar or a push instead
  of the recipe.
- **AC2** — When the fixture's slug names a folder holding only a `BACKLOG.md` at the first anchor's
  merge-base, under the kit default `ANCHOR_SCOPE` and under `ANCHOR_SCOPE=published` on an unpushed
  branch, preflight refuses under code 6 and the recipe lists that folder's live asks (or, with
  `ASKS_CMD` blank, says it cannot, per §4's contract).
  Red when: the run writes a README or a record into the filing home, which ruling D12-f forbids, or
  the published-scope run answers with fail 32.
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
  id's failing rules; a stub that sleeps past the bound is reported as never answered and not as a
  red; a stub that exits 1 refuses naming the exit status; a stub printing a ten-field row refuses as
  a parse refusal naming the line; and a stub that records its argv shows `--at` equal to the
  `m-base:` the record pins.
  Red when: the driver iterates the rows it received, so a missing id is never graded; or the call
  omits `--at`, so READY grades the working tree and a row filed after the run began counts as filed.
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
  `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once at the unit's end, its
  attribution summary reads `verdict clean`, meaning no NEW FAIL, no `DEAD PROBE at L` and no
  `OVER BUDGET at L`. Every suite it reports with INHERITED lines or `DEAD PROBE at R` is named by its
  file path in a filed backlog row or ask that is not CLOSED, as
  `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'` shows. Every arm this
  unit added passes, each observed RED with its fix unstaged.
  Red when: the key is set by a project and documented nowhere, or an arm lands unobserved; or the
  attributed run is read by its NEW count alone, so a suite this unit's change aborted before its
  first FAIL line, or pushed past its budget, reads as clean; or an inherited failure is attributed
  away with no record filing it.
  cost: one run of the unattended suites, the unit's single sanctioned run (D12-h).
  permission: the leg runs named here and in AC9 are observed at the one post-build bar, because
  unit passes run no gate legs (fix F7); ruling D12-h lifts the suites only.
- **AC14** — When a foreign live spec closes a mandated fixture ask, the pinned `asks-ready:` grade
  is `no` in four fixtures: the foreign build's run-state file absent; tracked and reading a terminal
  phase through `derived_phase()`; tracked and reading HELD; and present only on an unmerged fixture
  branch. The stub `ASKS_CMD`'s recorded argv carries no `--live-builds`. Preflight's report-only
  line names the spec in all four and labels the build terminal only in the second.
  Red when: the driver passes a live-build set read from any tree, so the unmerged-branch fixture's
  in-flight run is admitted as stale and two builds answer one ask; or the label compares a recorded
  phase string against a hard-coded list that omits HELD, so a HELD run's claim is labelled possibly
  stale.
- **AC15** — When `tools/unattended/unattended.test.sh` runs call shapes 1 and 2 against the producer
  the repository's own `.unattended.conf` declares as `ASKS_CMD`, over a builds-mode fixture tree
  holding an unlabelled OPEN ask, an ask closed by two records and a header tolerated by waiver, the
  driver's own parse accepts every row and the counts equal the scope; with `ASKS_CMD` blank in the
  repository's conf the arm prints a named skip.
  Red when: the arm stubs the producer, so a notice on stdout or an empty field is green in the suite
  and a parse refusal on the real call.
  fixture: in gov the arm skips until unit 35 arms the key; unit 35's REDs are this build's first
  real-seam observation, and every later suite run exercises it.
- **AC16** — When `--preflight` runs over a `prompt`-mode fixture README carrying `asks:`, and over a
  `recipe`-mode one, each refuses under the new code, pins no fact, and leaves
  `git status --porcelain` unchanged.
  Red when: preflight pins the run-written mandate, and the violation surfaces only when unit 18's
  check 19 reds at the post-build bar, after the whole build.
- **AC17** — When `--plan --asks` and `--status` run over a fixture README carrying exactly the keys
  unit 15 §4 lists for the scaffold — an empty roster pair, no spec, and an `asks:` line naming two
  filed asks — `--plan` exits 0 and prints one ASK row per mandated ask and `next:` in the UNDECIDED
  shape naming the first by rank, and `--status` prints the same `next:`.
  Red when: code 19 fires on the mandate-only build, so every E3 build refuses at the moment the
  UNDECIDED shape exists for.
- **AC18** — When `--plan --asks --paths` runs over a fixture holding two mandated asks where the
  later-listed holds the earlier, two MISSING units `-2` and `-10`, two live units closing one ask,
  and a live unmandated ask filed in the folder, the ranks follow the hold edge rather than listing
  order, `-2` sorts before `-10`, the duplicate closer prints the refusal row, the unmandated ask
  prints `ready=-`, every summary carries the four keys in order, and `--status` and `--resume` print
  the same UNDECIDED `next:` as `--plan`.
  Red when: the plan ranks by listing order, omits the refusal row, or `--status` prints the old
  terminal `next:`.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `kit/dogfood doc parity` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · one fixture per refusal and output shape in §6, with a local bare remote for the anchor · `ARMS_FLOORS` for `tools/unattended/unattended.sh`

## 8. Open questions

- **F1 — which unit declares the edge with unit 19?** The brief's table has this unit consuming from
  unit 19, which is ordered after it. RESOLVED (agent, 2026-09-14, delegated): this unit hands off to
  unit 19, matching unit 19's own resolution; the dependency runs from the scan this unit extends.
- **F2 — where the live-build set comes from.** Options: (a) the memory-tree kit reads run-state
  files; (b) the driver derives it from every tracked run-state file through unit 4's phase reader
  and passes it to READY; (c) no set, so every foreign live spec blocks; (d) the driver reads the
  run-state file at every advertised run-branch tip. (a) couples one kit to another's file; (b)'s
  input holds no run in flight, because a run's record lives only on its own branch until it lands,
  so it admits the double claim F5 exists to stop; (d) cannot see a branch nobody pushed and reads
  every published branch at preflight. RESOLVED (agent, 2026-09-14, delegated): (c), at rev-2,
  superseding rev-1's (b) after G3 H4. F5's premise, that a live run's record is visible where READY
  is evaluated, does not hold at the driver; F5's naming survives as a report-only line through unit
  4's `derived_phase()`, which admits nothing.
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
- rev-2 · 2026-09-14 · §3 §4 §5 §8 · S1 S2 S5 S6 S7 S8 S12 · AC1 AC2 AC6 AC13 AC14 AC15 AC16 AC17
  AC18 · spec audit round 1 folded. G3 H4: no `--live-builds`, every foreign live spec a claim, a
  report-only label through `derived_phase()` (§8 F2 re-resolved as (c), superseding (b); replaces
  design fix F5's mechanism at the driver), so consumes-from unit 4 now names the label. G3 H5: the
  id-shape and filing-home tests run before `check_slug` and `trusted_base`, AC1 and AC2 under
  `ANCHOR_SCOPE=published`. G3 H6: a non-`slug` README carrying `asks:` refused (AC16). G3 H9:
  `--attribute <BASE>`, consumes-from unit 1. G3 M2: three `ASKS_CMD` call shapes, consumes-from unit
  7, AC15 against the declared producer. G3 M3: a mandate is plan input (AC17). G3 M8: the M12
  directives' reach stated, widening parked. G3 M10, M18 and M19: criteria (AC14, AC18, AC6). G3 H3
  and M9: hands-off 17 and 18 name the P5 matcher, the one parse and the re-run call shape. G4 L2:
  hands-off unit 24, and §4 names that unit's working-tree read-back as a later caller's shape with
  no `--at`, so the protocol row says "the shapes listed" rather than a count.
- rev-3 · 2026-09-16 · spec-audit round 2 fold, second pass. Plan c1 E37, G1 H1 (2, 24), a sibling
  fold from the G1 round-2 record, over §3 Edges and §6 AC13: AC13 reads unit 1's `verdict clean` (unit 1
  S10) and the inherited-suite filing, its `Red when:` gains the NEW-count-alone reading, and the §3
  consumes-from edge to unit 1 names the attributed verdict in place of the NEW set. Fold
  verification then gave AC13's `Red when:` the rest of plan c1 §12's standard consumer text, the
  over-budget reading and the unfiled inherited failure, so it goes red on every half of unit 1
  S10's criterion, as the other consumers' criteria do. Spec-audit round 2 fold, third pass, from
  the second pass's low-severity verifier problem on this unit: unit 24 S10 and §8 F8 now reuse an
  OPEN auto-filed ask, reading its earlier, possibly committed id back with the same call, so §4's
  paragraph on that later caller's shape and the §3 hands-off edge to unit 24 name both reads. The
  call's arguments are unchanged, and no criterion moves.

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
