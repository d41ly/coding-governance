# TOOL-dDerivedDocket-15 — ask envelope, READY predicate and new-build scaffold

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g3-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g3-round1.md) | spec-audit | TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 |

<!-- /gen:spec-records -->

## 1. Goal

An unattended run pointed at asks can only execute one that says what was seen, what done looks
like and where the work lives; today an ask is free prose, and three id-driven runs derived their
acceptance with nobody to check it. Give an ask an optional clause tail, a predicate that grades
whether a set of asks can be executed without asking anyone, and a scaffold that turns an owner's id
list into a build README the owner lands, so authority stays with the owner's commit.

## 2. Scope (IN)

- **S1** The clause tail on an ask row: zero or more ` · <label> <value>` segments before the
  optional ` → ` pointer, read right to left, each label at most once, labels `seen`, `accept`,
  `out`, `may`, `verify` and `data`. A row with no clause parses as it does under unit 6. Observed by
  AC1.
- **S2** `- SCOPE · <id> · <clause>…` event rows in the writer's own `BACKLOG.md`, one per (file,
  target). Clause values merge per label over the ask row and every SCOPE row naming it: `seen`,
  `accept`, `out`, `verify` and `data` conjoin, and `may` is a union in which `none` is absorbed.
  A SCOPE row derives no status. Observed by AC2.
- **S3** Verdict V13 in `gen_build_index.py --check`, builds mode only: a clause value failing its
  grammar, a label written twice, a `seen` locator carrying a bare line number with no pinned commit
  (fix F6), a SCOPE row whose target is not a filed ask, and two SCOPE rows for one target in one
  file. Observed by AC3.
- **S4** Verdict V14 (owner ruling D12-d), builds mode only and forward-only: an ask filed on or after
  `ASK_CUTOFF` must carry `accept`, or a `seen` that carries a command. Observed by AC4.
- **S5** The READY predicate of §4 over a mandated set M, graded `yes`, `legacy` or `no`, with fix F5
  on R2 and fix F6 on R5 and `legacy`. Observed by AC5 and AC6.
- **S6** Print modes on unit 7's `--asks`: `--ready <IDLIST>` sets M, `--target <slug>` names the
  folder R2 admits its own live specs for, `--live-builds <slug>…` names the builds whose runs are
  live, `--at <rev>` reads one tree through `git ls-tree` and `git cat-file --batch`, and `--tsv`
  prints the machine projection of §4. All write nothing and exit 0. Observed by AC5, AC7 and AC8.
- **S7** `PROBE_ALLOW` in `.memory-tree.conf`, shipped blank (owner ruling D12-e), and
  `--asks --probe <id>`, the one path that may execute a `seen` command. It refuses unless the
  command's leading argv tokens match a declared prefix, and it never runs through a shell. Observed
  by AC9.
- **S8** `gen_build_index.py --new-build <slug> --asks <IDLIST>`, the scaffold of owner ruling D12-a:
  it parses the list all or nothing (fix F2), refuses a slug the all-time grep finds, an id with no
  filed ask, and a list whose every id grades `no`, and otherwise writes the build README with a
  canonical one-line `asks:` key, its bound row in `memory/project/readme-contract.txt`, and the
  `--write` render. It never emits `may:`. Observed by AC10 and AC11.
- **S9** Arms for every verdict, grade and refusal above in `gen_build_index.py --selftest`, each
  observed RED with its fix unstaged. Observed by AC12.

## 3. Non-goals (OUT)

- The base ask, disposition, SEV and REOPEN grammars, the fold and verdicts V1 to V12 are unit 6's;
  the view and the bare `--asks` print mode are unit 7's. This unit extends both and re-implements
  neither.
- Scoping check 13's `BACKLOG.md` skip to asks filed before `ASK_CUTOFF` (owner ruling D12-g). The
  design placed it in this unit; the spec brief's roster gives it to unit 8, beside the skip itself,
  and this spec follows the roster (§9).
- Honouring a `may` grant, and refusing `may` on a SCOPE row, are unit 19's; this unit parses the
  label and prints it in the Grant column only.
- Every driver use of READY, the recipe the driver prints for an ids invocation, and pinning
  `asks-ready:` are unit 16's. The `asks-disposed` witness that parses `--tsv` is unit 17's.
- No run executes a `seen` command in this build: gov's `PROBE_ALLOW` stays blank.
- No `--mode` on the scaffold. Owner ruling D12-a dropped the zero-commit ids start, so the only
  README the scaffold writes is an owner-landed `slug`-mode one.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-6` — the ask and disposition parser the clause tail extends,
  the fold R2 reads, the verdict list V13 and V14 join, and the `ASK_CUTOFF` key V14 compares.
- **consumes-from** `TOOL-dDerivedDocket-7` — the `--asks` print mode S6 extends, its link-wrapped
  first cell, and the `--write` render the scaffold runs.
- **hands-off** `TOOL-dDerivedDocket-16` — READY at a pinned rev with a target folder and live
  builds, the `--tsv` projection, and the `--new-build` command the driver's ids refusal prints.
- **hands-off** `TOOL-dDerivedDocket-17` — the eleven-field `--tsv` row and its closing examined
  line, which the `asks-disposed` witness parses.
- **hands-off** `TOOL-dDerivedDocket-19` — V13, which that unit extends to a SCOPE row carrying
  `may`, and the scaffold, which that unit asserts never emits `may:`.
- **hands-off** `TOOL-dDerivedDocket-20` — the clause grammar, READY and `--probe`, which the
  companion guide states as contract and the Skill's orientation steps call.
- **hands-off** `TOOL-dDerivedDocket-24` — the `seen` and `accept` clauses an auto-filed
  inherited-red ask carries, so it is filed runnable under V14.
- **hands-off** `TOOL-dDerivedDocket-34` — V13, staged RED on the real tree after the switch-over.

## 4. Design

### Grammar

```
ask     := "- " ID " · filed " DATE [" · unit"] " · " TEXT CLAUSE* [" → " POINTER]
scope   := "- SCOPE · " ID CLAUSE+
CLAUSE  := " · " LABEL " " VALUE
LABEL   := "seen" | "accept" | "out" | "may" | "verify" | "data"
seen    := LOCATOR [ " run `" COMMAND "`" ]
LOCATOR := "`" PATH "`@" SHA7+ [ ":" LINE ]        ; a path at a pinned commit
         | "`" PATH "` matching `" PATTERN "`"     ; a path and a content pattern
         | REPO ":" PATH "@" SHA7+                  ; outside this repo; implies a `data` clause
may     := "none" | GRANT ( " " GRANT )*          ; GRANT := "`" PATH "`" | decision ID
```

Fix F6 forbids a bare line number, because a line moves and the ask would then point at nothing
while still reading located. `accept`, `out`, `verify` and `data` are free text on the one physical
line unit 6 requires. A TEXT that happens to contain ` · accept ` is misread as a clause, and the
misread value then fails its grammar as V13, so the collision is loud. Illustrative rows:

```markdown
- EXMP-aFoo-3 · filed 2026-09-15 · push-main.sh reports a gate RED as a network failure · seen `tools/push-main.sh`@7484d8d7:23 · accept a RED bar prints GATE FAIL and exits non-zero · out retry policy → `tools/push-main.sh`
- SCOPE · EXMP-cBaz-5 · accept 0 of 40 fixture runs double-count · verify the hygiene leg alone
```

### READY, evaluated at one tree over a mandated set M

```
R1 FILED       A has exactly one ask row, in builds/<slug(A)>/BACKLOG.md
R2 LIVE        status(A) is OPEN, BLOCKED or DEFERRED; or SPECCED or INPROGRESS where every live
               closing spec is in the --target folder or in a build --live-builds does not name;
               or A is a `unit` ask of the --target folder and not terminal
R3 UNHELD      every live hold on A names a target inside M
R4 LOCATED     the POINTER or the seen LOCATOR names a path present in that tree, or is external
R5 ACCEPTABLE  the merged clauses carry `accept`, or a `seen` carrying `run`
R6 BOUNDED     an external LOCATOR or POINTER is accompanied by a `data` clause
yes     R1..R6 all hold
legacy  R1, R2, R3 and R6 hold, exactly one of R4 and R5 holds, and `filed` < ASK_CUTOFF
no      otherwise
```

Without `--ready`, each id is graded with M = {A}. Without `--live-builds`, every foreign live
spec counts as a live claim, which is the conservative reading a human query gets. A foreign live
spec that R2 admits because its build is not live is printed in the closers field as `stale:<id>`,
which is how fix F5 names a stale claim without a fourth grade (§8 F2). Status comes from unit 6's
fold only; this predicate adds no status rule.

### The machine projection

`--tsv` prints one line per ask with exactly eleven TAB-separated fields, then one closing line:

```
ask  <id>  <status>  <decided-by>  <home>  <sev>  <ready>  <missing>  <holds>  <grant>  <closers>
examined  <n>
```

`missing` lists the failing rules as `R<n>` joined by commas, or `-`; `holds` and `closers` list
ids joined by commas, or `-`. The human table is the same data with a link-wrapped first cell, so a
pasted copy anchors nothing (design §19.7 layer 1). Its summary line reads
`asks: <n> examined · <y> ready · <l> legacy · <x> not ready · at <rev or the working tree>`.

### The probe runner

`--asks --probe <id>` takes the merged `seen` command, refuses it outright if it carries a shell
metacharacter or a newline, splits it into argv without a shell, and runs it only when those argv
tokens begin with one of the whitespace-separated prefixes in `PROBE_ALLOW`, bounded, from the repo
root. It prints the locator, the decision and, when it ran, the exit status and the output tail.
Blank `PROBE_ALLOW` refuses every command and says which key would admit it. Ask text is written by
whoever filed it, so this is the only place the kit executes a filer's bytes (charter §9).

### The scaffold

The IDLIST grammar is design §19.2's, including the bare `-n` continuation. Any token with an id
prefix that fails the grammar refuses the whole invocation, and `...` and `…` are refused by name,
because a re-typed prompt once silently narrowed six asks to two (fix F2). The canonical `asks:` is
one physical line, sorted by slug and numeric sequence, consecutive sequences collapsed to `..`
ranges that `_expand_ids` (`tools/memory-tree/gen_build_index.py:500`) already expands; one line
anchors nothing.

The README carries `slug`, `node` (the slug's leading tag), `opened`, `streams` and `roster`
derived from the asks' families through `FAMILIES`, `authorized-by: slug` and `asks:`. The five
canon slots of `SLOT_CANON` (`tools/memory-tree/gen_build_index.py:107-113`) get generated bodies
naming the asks and the tree they were read at, so the file carries no authored prose; the units
roster pair is empty. The contract row is BOUND, so the registry's exempt pin does not move. The
readiness table prints before anything is written, and a list whose every id grades `no` stops
there, which is design §19.2's disqualifier stop.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `--ready`, `--target`, `--live-builds`, `--at`, `--tsv`, `--probe` | options of `--asks` | flags |
| `--new-build`, and its `--asks` | CLI mode | flag; the functions behind it lead with a `.lexicon.conf` verb, checked with `lexicon.py --suggest` |
| `PROBE_ALLOW` | conf key in `.memory-tree.conf` and its example | screaming snake, as every key there |
| V13, V14 | verdict labels | the verdict list's own numbering |
| `SCOPE` | disposition-file row verb | upper case, as every verb there |

### Files touched (estimate)

`tools/memory-tree/backlog.py` · `tools/memory-tree/gen_build_index.py` and its selftest ·
`tools/memory-tree/.memory-tree.conf.example` · `.memory-tree.conf` (the blank key) ·
`memory/map/generated/` regenerated for the new symbols.

### Alternatives rejected

- **Execute `seen` commands by default** (design D12-e option a's inverse). Rejected by the owner's
  ruling: a filer's bytes become commands, which is a new write-to-exec surface.
- **A YAML list for `asks:`.** Rejected in design §19.2: each list row would anchor a foreign id under
  the new build.
- **`--json` for the driver.** Rejected in design §19.3: the driver has no JSON parser, and the kit
  precedent is a TAB machine line.
- **A `stale-claim` fourth grade.** Rejected here (§8 F2): unit 17's hardening is keyed on `yes`, and
  a fourth grade would reach it unhardened.

## 5. Production-readiness checklist

- security — READY and the print modes read records only. `--probe` executes a filer's command only
  under a declared argv prefix, without a shell, bounded; gov declares none. The scaffold writes a
  README with no `may:`, so it can grant nothing.
- perf / scale — one pass over the tracked `BACKLOG.md` files, which the fold already makes; `--at`
  adds two git processes.
- error / empty / loading states — an id with no ask grades `no` on R1 and is named; in shards mode
  every id grades `no` and the output says the tree files no ask per build; the scaffold's refusals
  write nothing.
- observability — the summary line counts every grade; every `no` names its rules.
- risks — a TEXT containing a clause separator is misread, and V13 turns the misread into a verdict
  rather than a silent grade. A `legacy` ask carries no mechanical acceptance, which orientation
  grades (design §19.10 item 4).
- testing — S9's arms in the build-index selftest, a held kit leg, so the landing bar owes
  `GATE_FULL=1 GATE_SELFTESTS=1`.
- migration — none. Legacy asks carry no clause and grade by the `legacy` rule; V14 is forward-only.
- user docs — the grammar and READY as contract text are unit 20's companion guide; this unit's
  module docstrings carry the grammar.

## 6. Acceptance criteria

- **AC1** — When the selftest parses the §4 example ask, `backlog.py` yields its four clauses and
  pointer, and a clause-free legacy row yields the same fields unit 6 yields.
  Red when: the tail is read left to right, so a TEXT containing ` · out ` swallows the real clauses.
- **AC2** — When a fixture carries a SCOPE row adding `accept` to an ask with only `seen`,
  `gen_build_index.py --asks --tsv` grades it `yes`, and its status is unchanged by the SCOPE row.
  Red when: a SCOPE row moves the derived status.
- **AC3** — When a builds-mode fixture carries a `seen` locator with a bare line number, a doubled
  label, a SCOPE row naming an unfiled id, and a second SCOPE row for one target in one file,
  `gen_build_index.py --check` names V13 four times with each file and row.
  Red when: the bare line number passes, so an ask stays located after its line moved.
- **AC4** — When a fixture ask filed on `ASK_CUTOFF` carries neither `accept` nor a `seen` with
  `run`, `--check` names V14; the same ask filed the day before passes.
  Red when: V14 grades asks filed before the cutoff, which reds every legacy ask on arrival.
- **AC5** — When `gen_build_index.py --asks --ready` grades a fixture set holding an OPEN ask with
  `accept`, an ask held on one outside the set, and a legacy ask with a pointer and no acceptance,
  it prints `yes`, `no` naming R3, and `legacy`.
  Red when: `legacy` is granted with both R4 and R5 failing, which fix F6 forbids.
- **AC6** — When an ask's only live closing spec sits in another build, the ask grades `no` on R2;
  with `--live-builds` omitting that build it grades `yes` and the closers field reads `stale:` and
  the spec id; with `--target` naming that build it grades `yes`.
  Red when: a foreign live spec in a live build is admitted, so two builds answer one ask.
- **AC7** — When `--asks --tsv` runs over three fixture asks, it prints three lines of exactly eleven
  TAB-separated fields led by `ask`, then `examined` and 3.
  Red when: a field is added or reordered without the witness in unit 17 failing first.
- **AC8** — When `--asks --ready --at <rev>` runs with a fixture's working tree edited after `<rev>`,
  the grades reflect `<rev>` only, and `git status --porcelain` is unchanged.
  Red when: `--at` reads a working-tree file, so a row filed after the pinned base grades as filed.
- **AC9** — When `--asks --probe <id>` runs with `PROBE_ALLOW` blank it refuses naming the key; with
  a matching prefix it runs and prints the exit status; with `;` in the command it refuses before
  splitting.
  Red when: the command is handed to a shell, so an allowed prefix followed by `;` runs anything.
- **AC10** — When `gen_build_index.py --new-build <slug> --asks` receives `EXMP-aFoo-3 -4` over a
  fixture filing both, it writes a README whose `asks:` line reads `EXMP-aFoo-3..4`, a bound
  contract row, and rendered regions, and `gen_build_index.py --check-format` passes on it.
  Red when: the scaffold writes a README the slot contract refuses, so the owner's one command
  produces a red bar.
- **AC11** — When the scaffold receives `EXMP-aFoo-3...5`, an unfiled id, a slug the all-time grep
  finds, or a list whose every id grades `no`, it exits non-zero and writes nothing; over an ask
  carrying `may`, its README has no `may:` line.
  Red when: a malformed token is dropped and the rest scaffolded, which is fix F2's silent narrowing.
- **AC12** — When `python3 tools/memory-tree/gen_build_index.py --selftest` runs, every arm this unit
  adds passes, and each was observed RED with its fix unstaged.
  Red when: an arm is wired without its failing case ever being seen.
  cost: one kit selftest run; held, so it runs at the landing bar under `GATE_SELFTESTS=1`.
  permission: unit passes run no gate legs (fix F7), so each arm's RED is observed by hand against a
  scratch fixture in the pass, and the selftest itself runs at the one post-build bar.

## 7. Gates

`build-index selftest` · `build README slot contract` · `memory hygiene` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: `python3 tools/memory-tree/gen_build_index.py --selftest` · one fixture per verdict, grade, refusal and print mode in §6 · none

## 8. Open questions

- **F1 — how does fix F6 spell a pinned locator?** F6 forbids a bare line number and names `@SHA7`
  or a content pattern without a syntax. RESOLVED (agent, 2026-09-14, delegated): `` `path`@sha ``
  with an optional `:line`, or `` `path` matching `pattern` ``, and the command marked by `run`,
  because two backticked segments after one label cannot otherwise be told apart.
- **F2 — how does fix F5 name a stale claim?** Options: (a) a fourth grade `stale-claim`; (b) the
  three grades, with the stale spec named `stale:` in closers; (c) the memory-tree kit reads each
  build's run-state file. (a) reaches unit 17 unhardened, whose rules key on `yes`; (c) couples the
  kit to another kit's file and cannot see a derived landing. RESOLVED (agent, 2026-09-14,
  delegated): (b), with the live-build set supplied by the one caller that knows it.
- **F3 — where does the `PROBE_ALLOW` key live?** RESOLVED (agent, 2026-09-14, delegated): in
  `.memory-tree.conf`, beside `ASK_CUTOFF`, because the only runner is this kit's `--probe`.
- **F4 — check 13's pre-cutoff scoping (D12-g).** RESOLVED (agent, 2026-09-14, delegated): unit 8's,
  as the spec brief's roster assigns, so the skip and its scope land as one change.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from design §19.3, fixes F2, F5 and F6, and rulings D12-a, D12-d
  and D12-e. Adds consumes-from unit 7, whose print mode and render this unit extends, hands-off
  units 17, 19, 24 and 34, whose specs declare the consuming end, and hands-off unit 20, whose
  carriers state this unit's grammar as contract. Leaves D12-g to unit 8 per the
  brief's roster: unit 18's spec says unit 15 refines check 13, and one of the two pointers is wrong.

## 10. Reuse audit

The seams are the generator's own: `_expand_ids` for ranges, the `--write` render for the scaffold's
regions, the `SLOT_CANON` and readme-contract registry for its shape, and unit 7's `--asks` for the
print path. `python tools/codebase-map/reuse_lookup.py "parse clause tail of a row and grade
readiness"` returned name-stem neighbours (`parse_args`, `parse_conf` in
`tools/memory-tree/corpus_ids.py`) and no readiness grader; `reuse_lookup.py "scaffold a new build
readme with front matter"` returned `build_*` helpers and no scaffold. No existing seam fits the
predicate or the scaffold: nothing in the tree grades an ask or writes a build README. The recall
probe returned design §19 and `TOOL-aUnmannedHelm-4`, and no prior record of an ask envelope.

Where the design and BASE disagree: design §19.3's example locator `` `tools/push-main.sh`:212 `` is
illegal under fix F6; design §19.8 U10 places the check-13 scoping here and the brief places it in
unit 8; `gen_build_index.py` did not change between `09a22d2b` and `abac6d59`, so the design's line
citations hold.

Recall terms used: `acceptance-underivable orientation ask row pointer observable cut-line resolution
table ids-driven run`
