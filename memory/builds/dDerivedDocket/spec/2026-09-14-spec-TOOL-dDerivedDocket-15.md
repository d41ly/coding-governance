# TOOL-dDerivedDocket-15 — ask envelope, READY predicate and new-build scaffold

**Status:** SPECCED · rev-6 · 2026-09-21 · node d · Tier-2 · base fb07ca25 · streams tooling · order 15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md) | spec-audit | TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 |
| [2026-09-20-review-TOOL-dDerivedDocket-15-spec-audit-g3-round2.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-15-spec-audit-g3-round2.md) | spec-audit | TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 |

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
  `ASK_CUTOFF` whose MERGED clauses (S2: the ask row and every SCOPE row naming it) carry neither
  `accept` nor a `seen` that carries `run`. Observed by AC4.
- **S5** The READY predicate of §4 over a mandated set M, graded `yes`, `legacy` or `no`, with fix F5
  on R2 and fix F6 on R5 and `legacy`. Observed by AC5 and AC6.
- **S6** Print modes on unit 7's `--asks`: `--ready <IDLIST>` sets M, `--target <slug>` names the
  folder R2 admits its own live specs for, `--live-builds <slug>…` names the builds whose runs are
  live, `--at <rev>` reads one tree through `git ls-tree` and `git cat-file --batch`, and `--tsv`
  prints the machine projection of §4. `--ready` sets the EXAMINED population to the ids its list
  names, and an empty list is accepted rather than refused as a usage error: M and that population
  are both empty, nothing is graded, and the run prints `examined` and 0. All write nothing and exit
  0. Observed by AC5, AC7 and AC8.
- **S7** `PROBE_ALLOW` in `.memory-tree.conf`, shipped blank (owner ruling D12-e), and
  `--asks --probe <id>`, the one path that may execute a `seen` command. It refuses unless the
  command's leading argv tokens equal one declared `PROBE_ALLOW` entry token for token (§4, §8 F5),
  and it never runs through a shell. Observed by AC9.
- **S8** `gen_build_index.py --new-build <slug> --asks <IDLIST>`, the scaffold of owner ruling D12-a:
  it parses the list all or nothing (fix F2), refuses a slug the all-time grep finds, an id with no
  filed ask, and a list whose every id grades `no`, and otherwise writes the build README with a
  canonical one-line `asks:` key, its bound row in `memory/project/readme-contract.txt`, and the
  `--write` render, and writes `ids:` and `status: OPEN` among its keys (§4). It never emits `may:`.
  Observed by AC10, AC11 and AC13.
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
- The scaffold's README resolves to `slug`, so the mode-scoped directives bind it as they bind any
  `slug` run: `researched` and `solution-tested` do not (TOOL-aPromptedMandate-4), and
  `pieces-recorded` and `playbook-followed` do not (recipe mode only). The question whether the first
  two should is parked (unit 16 §3).

### Edges

- **consumes-from** `TOOL-dDerivedDocket-6` — the ask and disposition parser the clause tail extends,
  the fold R2 reads, the verdict list V13 and V14 join, and the `ASK_CUTOFF` key V14 compares.
- **consumes-from** `TOOL-dDerivedDocket-7` — the `--asks` print mode S6 extends, its link-wrapped
  first cell, and the `--write` render the scaffold runs.
- **consumes-from** `TOOL-dDerivedDocket-50` — the in-kit seam this kit reaches `anchor_at` through.
  The G3 round-2 record's H2 measured that AC13's `fixture:` line routed through a conf key the
  memory-tree kit does not declare; that unit landed `resolve_anchor(root, E=None)` in
  `tools/memory-tree/corpus_ids.py`, and AC13 names it.
- **consumes-from** `TOOL-dDerivedDocket-51` — the id family AC13's fixture files its asks under. The
  same record's H3 measured that `anchor_at` admits only the conf's declared families, so an `EXMP`
  id anchors nothing before the scaffold writes a line; that unit picks the family and pins the
  staged RED.
- **consumes-from** `TOOL-dDerivedDocket-53` — which tree supplies the conf under `--at`. The same
  record's H5 measured that the conf is read from the working tree whatever `<rev>` is, so S6's
  pinned-tree read is not a pure function of that rev; that unit decides it.
- **hands-off** `TOOL-dDerivedDocket-16` — READY at a pinned rev with a target folder (the driver
  passes no live-build set), the `--tsv` projection, and the `--new-build` command the driver's ids
  refusal prints.
- **hands-off** `TOOL-dDerivedDocket-17` — the eleven-field `--tsv` row and its closing examined
  line, which the `asks-disposed` witness parses.
- **hands-off** `TOOL-dDerivedDocket-48` — the rule that under `--tsv` stdout carries only the
  `ask` lines and the `examined` line while every notice goes to stderr, which is what makes a
  stream split worth making: that unit gives `run_bounded` two capture files so the row stream the
  parse reads is `RB_STDOUT` and the notices are reported beside it rather than inside it.
- **hands-off** `TOOL-dDerivedDocket-19` — V13, which that unit extends to a SCOPE row carrying
  `may`, and the scaffold, which that unit asserts never emits `may:`.
- **hands-off** `TOOL-dDerivedDocket-20` — the clause grammar, READY and `--probe`, which the
  companion guide states as contract and the Skill's orientation steps call, and the rule that a
  scaffolded build's first spec commit deletes `status: OPEN`.
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
spec counts as a live claim, which is the conservative reading a human query gets and the reading the
ask driver pins, because no tree it reads shows every run in flight (unit 16 §8 F2). A foreign live
spec that R2 admits because its build is not live is printed in the closers field as `stale:<id>`,
which is how fix F5 names a stale claim without a fourth grade (§8 F2). Status comes from unit 6's
fold only; this predicate adds no status rule.

Which tree supplies the CONF under `--at` is not settled in this spec. At `fb07ca25` `load_conf`
reads `.memory-tree.conf` from the WORKING-TREE root
(`tools/memory-tree/gen_build_index.py:286-291`) and runs before mode dispatch, so `ASK_CUTOFF` and
`BACKLOG_MODE` stay evaluation-time values whatever `<rev>` is, and READY at a pinned rev is
therefore not a pure function of that rev. The G3 round-2 record's H5 promoted that to
`TOOL-dDerivedDocket-53`, which decides whether the conf is read at `<rev>` or the grade-bearing keys
are named so a caller can skip by name. S6, the predicate above and §5's cost line keep their current
text and take the answer from that unit.

### The machine projection

`--tsv` prints one line per ask with exactly eleven TAB-separated fields, then one closing line:

```
ask  <id>  <status>  <decided-by>  <home>  <sev>  <ready>  <missing>  <holds>  <grant>  <closers>
examined  <n>
```

Each field's value set, spelled as unit 7's `--json` projection spells the same data, so the two
projections share one spelling:

- `status`: unit 6's vocabulary `CLOSED WONTDO INPROGRESS SPECCED BLOCKED DEFERRED OPEN`, or
  `UNRESOLVED` for unit 6's placeholder.
- `decided-by`: a comma list of EVERY member of the set that decided the status, never one member
  picked (`memory/gotchas/one-value-field-records-a-mixed-outcome.md`): for CLOSED the `closing`
  set, for WONTDO the `declining` set (the `--json` fields of those names), for unit 6's fold rules
  R3 to R6 the deciding spec ids and hold targets; `-` for its R7, OPEN. These are the fold's rule
  numbers, not READY's. A spec member is its id; a CLOSED row's member is its `by`
  value, a hex sha. The two shapes are disjoint, because an id carries a family prefix.
- `home`: the home build's slug; never empty.
- `sev`: unit 6's SEV label, or `-` when the ask carries none.
- `ready`: `yes`, `legacy` or `no`.
- `missing`: the failing rules as `R<n>` joined by commas, or `-`.
- `holds`: live hold targets joined by commas, or `-`.
- `grant`: the merged `may` grants joined by commas; `none` when the merged value is `none`; `-`
  when no `may` clause exists.
- `closers`: the ask's LIVE closing specs (the `--json` `live_specs` set), each an id, a foreign one
  that R2 admitted prefixed `stale:`; `-` when none. A CLOSED closing spec is never here: it is a
  member of `decided-by`.

No field is ever empty. Every field that can be empty carries `-`, because the kit reads TAB records
with `IFS=$'\t' read` and a run of tabs collapses
(`memory/gotchas/empty-field-collapses-unless-it-is-last.md`). A consumer validates each field
against its value set, so a reorder or an empty field is a parse refusal, never a misread row.

The human table is the same data with a link-wrapped first cell, so a pasted copy anchors nothing
(design §19.7 layer 1). Its summary line reads
`asks: <n> examined · <y> ready · <l> legacy · <x> not ready · at <rev or the working tree>`.

Under `--tsv`, stdout carries the n `ask` lines and the one `examined` line and nothing else. The
tolerated-by-waiver line `collect()` prints (`tools/memory-tree/gen_build_index.py:819-822`), unit
7's S11 liveness line and every other notice go to stderr, by unit 7's rule that every `--asks`
output mode writes only its value to stdout.

### The probe runner

`--asks --probe <id>` takes the one `run` command of the merged `seen`. When the ask row and its
SCOPE rows carry more than one `run`, it refuses as ambiguous, names each row and runs nothing (§8
F7). It refuses the command outright, before splitting, if it carries a shell metacharacter or a
newline, splits it into argv without a shell, and runs it only when those argv tokens begin with one
of the entries of `PROBE_ALLOW`, bounded, from the repo root. Entries are separated by `|`; an entry
is one or more whitespace-separated argv tokens, and it matches only when each of its tokens EQUALS
the command's token at that position, so `python3` never admits `python3x` and `tools/` never admits
`tools/../x` (§8 F5). A single-token interpreter entry such as `python3` admits `python3 -c` followed
by anything: declare the script, not the interpreter. The bound kills a command that outlives it and
reports it as never answered. It prints the locator, the decision and, when it ran, the exit status
and the output tail.
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
derived from the asks' families through `FAMILIES`, `ids:` (written empty and filled by the
`--write` render the scaffold runs), `status: OPEN`, `authorized-by: slug` and `asks:`.
`status: OPEN` is required because `derive_status` has no spec to derive from
(`tools/memory-tree/gen_build_index.py:635-641`). The run's first spec commit deletes it, because an
authored status beside a parseable spec header is the generator's two-answers refusal (`:644-649`);
this build's own README did exactly that at `c6cb6951`. The five canon slots of `SLOT_CANON`
(`tools/memory-tree/gen_build_index.py:107-113`) get generated bodies naming the asks and the tree
they were read at, so the file carries no authored prose; the units roster pair is empty. Those
bodies WRAP. Every generated line stays under hygiene check 7's per-line build-README entry cap
`BUILD_README_ENTRY_CAP_CHARS` (`tools/memory-tree/check-memory-hygiene.sh:94`), through the
generator's own `_render_wrapped_ids` (`tools/memory-tree/gen_build_index.py:957`) and its
`IDS_WRAP` cap (`:918`), because a slot body names one id per mandated ask and a dozen ~22-character
ids plus framing prose already crosses that cap. The front-matter block is exempt from check 7
(`tools/memory-tree/check-memory-hygiene.sh:790-798`) and a slot body is not, so the one physical
line the `asks:` key pins is safe and the bodies beside it are the lines that would red the
`memory hygiene` leg §7 names on the README the owner's one command just wrote. Every
generated body cites an ask inside prose, never as a bullet's or a table row's first token:
`A_BOLD_LI`, `A_DASH` and `A_TABLE` anchor an id that leads one
(`tools/memory-recall/extract.py:117-121`), and the new build would become a second claimant under
check 13. The contract row is BOUND, so the registry's exempt pin does not move. The
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
`memory/map/generated/` regenerated for the new symbols and staged in the same commit as the `.py`
it describes, because the pre-commit fast leg runs the codebase-map gate whenever a `.py` is staged
and refuses a stale or unstaged artifact (dUnstagedSymbol, `1a774fcd`).

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
  under a declared `PROBE_ALLOW` entry matched token for token, without a shell, bounded; gov
  declares none. An entry naming a bare interpreter admits arbitrary code, and §4 says so. The
  scaffold writes a README with no `may:`, so it can grant nothing.
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

- **AC1** — When the selftest parses the §4 example ask, `backlog.py` yields its three clauses and
  its pointer; when it parses a fixture row whose TEXT contains ` · out ` before the real `seen` and
  `accept` clauses, it yields the real `seen` and `accept` values read right to left, and `--check`
  reports V13 on the misread `out` value; a clause-free legacy row yields the same fields unit 6
  yields.
  Red when: the tail is read left to right, so the TEXT's ` · out ` swallows the real clauses and no
  V13 names it.
- **AC2** — When a fixture carries a SCOPE row adding `accept` to an ask with only `seen`,
  `gen_build_index.py --asks --tsv` grades it `yes`, and its status is unchanged by the SCOPE row;
  with the ask row and a SCOPE row both carrying `accept`, `--asks <id>` prints both values; a SCOPE
  row carrying `may none` beside the ask's grant leaves the grant unchanged.
  Red when: a SCOPE row moves the derived status, or a SCOPE row replaces the ask's value, so one
  `accept` disappears.
- **AC3** — When a builds-mode fixture carries a `seen` locator with a bare line number, a doubled
  label, a SCOPE row naming an unfiled id, and a second SCOPE row for one target in one file,
  `gen_build_index.py --check` names V13 four times with each file and row.
  Red when: the bare line number passes, so an ask stays located after its line moved.
- **AC4** — When `gen_build_index.py --check` runs over a fixture holding asks filed on
  `ASK_CUTOFF` — one with no clause, one with a bare `seen`, one carrying `accept`, one carrying
  `seen … run`, and one with no clause that a SCOPE row cures with `accept` — it names V14 for the
  first two only, and the clause-free ask filed the day before passes.
  Red when: V14 reds every ask filed on or after the cutoff, or grades asks filed before it, which
  reds every legacy ask on arrival.
- **AC5** — When `gen_build_index.py --asks --tsv --ready` grades a fixture set holding an OPEN ask
  with `accept` (`yes`); an ask held on one outside the set (`no`, missing `R3`); an ask whose hold
  target is inside the set (R3 passes); an id with no ask row and an id with two (`no`, `R1`); an ask
  filed in a foreign folder (`no`, `R1`); a pointer whose path is absent from the tree (`no`, `R4`);
  an external locator with no `data` clause (`no`, `R6`); a pre-cutoff ask with a pointer and no
  acceptance (`legacy`); and a pre-cutoff ask with neither pointer nor acceptance (`no`, `R4,R5`),
  each row's `ready` and `missing` fields equal the values named.
  Red when: the last ask is graded `legacy` with both R4 and R5 failing, which fix F6 forbids, or any
  named rule is ignored so its row reads `yes`.
- **AC6** — When an ask's only live closing spec sits in another build, the ask grades `no` on R2;
  with `--live-builds` omitting that build it grades `yes` and the closers field reads `stale:` and
  the spec id; with `--target` naming that build it grades `yes`; a terminal ask grades `no` on R2; a
  `unit` ask of the `--target` folder that is not terminal grades `yes`.
  Red when: a foreign live spec in a live build is admitted, so two builds answer one ask.
- **AC7** — When `gen_build_index.py --asks --tsv` runs over a builds-mode fixture holding an
  unlabelled OPEN ask, an ask closed by one CLOSED spec and one CLOSED row, and a BLOCKED ask graded
  `yes`, plus one header tolerated by waiver, the whole of stdout is exactly four lines: three `ask`
  lines of exactly eleven TAB-separated fields, then `examined` and 3. Every field holds the value
  the fixture fixes, position by position: field 3 the status; field 4 `-` for the OPEN ask and both
  closing members for the closed one; field 6 `-` for the unlabelled ask; field 7 the grade; field 11
  `-` or the live closer. No field is empty, and the waiver line appears on stderr. The run exits 0,
  and so do two further runs of the same mode: one over a fixture where every examined ask grades
  `no`, whose stdout is the `ask` lines and the `examined` line and whose exit status is 0; and one
  `--ready` naming no id, whose stdout is `examined` and 0 and whose exit status is 0.
  Red when: a notice reaches stdout, a field is empty, or two fields swap (status and ready, say), so
  a consumer parsing by position misreads a row that still has eleven fields; or the grade decides
  the exit status, so an all-`no` mandate reaches unit 16's preflight as a producer failure naming an
  exit status rather than as the refusal that prints each id's failing rules.
- **AC8** — When `--asks --ready --at <rev>` runs with a fixture's working tree edited after `<rev>`,
  the grades reflect `<rev>` only, and `git status --porcelain` is unchanged; it is unchanged again
  after a `--tsv --ready <ids> --target <slug> --live-builds <slug>` run over the same fixture, which
  writes no cache and no log.
  Red when: `--at` reads a working-tree file, so a row filed after the pinned base grades as filed;
  or a print mode writes a cache or a log, so the tree unit 16's `--preflight` just required clean is
  dirty when the producer returns.
- **AC9** — When `gen_build_index.py --asks --probe <id>` runs with `PROBE_ALLOW` blank it refuses
  naming the key; with a non-blank `PROBE_ALLOW` of which no entry matches, it refuses naming the
  key; with `python3` declared and the command `python3x …` it refuses; with the two-token entry
  `python3 p.py` declared it runs `python3 p.py`, prints the exit status, and refuses `python3 q.py`;
  with `;` or a newline in the command it refuses before splitting; with a fixture command that
  sleeps past the bound it kills it and reports it never answered; with two `seen … run` values it
  refuses as ambiguous naming both rows.
  Red when: the match is a string prefix, or the command reaches a shell, so an allowed entry admits
  `python3x`, `tools/../x` or `; anything`.
- **AC10** — When `gen_build_index.py --new-build <slug> --asks` receives `EXMP-aFoo-3 -4` in a
  scratch fixture repository filing both, and the scaffold's files are then staged, the README's
  `asks:` line reads `EXMP-aFoo-3..4`, it carries `authorized-by: slug`, `status: OPEN` and a filled
  `ids:`, its contract row is bound, and `gen_build_index.py --check` and
  `gen_build_index.py --check-format` both exit 0. And when the same command receives a mandate
  large enough that an unwrapped slot body would exceed the cap, every unfenced line of the written
  `README.md` outside its front-matter block measures at or under `BUILD_README_ENTRY_CAP_CHARS`,
  read from `tools/memory-tree/check-memory-hygiene.sh` rather than typed into this criterion.
  Red when: the key list drops `ids`, or the scaffold writes `authorized-by: prompt`, so the owner's
  one command produces a README the bar refuses or one units 16, 18 and 19 treat as run-writable; or
  a generated slot body lands as one long line, so the `memory hygiene` leg §7 names reds the
  `README.md` the owner's one command just wrote and `--check-format`, which grades no slot's size,
  sees nothing.
- **AC11** — When the scaffold receives `EXMP-aFoo-3...5`, an unfiled id, a slug the all-time grep
  finds, or a list whose every id grades `no`, it exits non-zero and writes nothing; over an ask
  carrying `may`, its README has no `may:` line.
  Red when: a malformed token is dropped and the rest scaffolded, which is fix F2's silent narrowing.
- **AC12** — When `python3 tools/memory-tree/gen_build_index.py --selftest` runs, every arm this unit
  adds passes, and each was observed RED with its fix unstaged.
  Red when: an arm is wired without its failing case ever being seen.
  cost: one kit selftest run, whose declared ceiling `tools/gate-legs.json` carries on the
  `build-index selftest` row is inside what a pass can hold, so no cost deferral applies.
  permission: the `--selftest` FLAG clause decides this criterion, not the gate-leg one: a flag on
  another file is what `memory/guides/BUILD-METHOD.md` M6 and the header of
  `tools/unattended/gate-guard.js` both name as a pass's direct check, and the hook denies a
  `.test.sh` or `selftest.py` FILE invocation rather than this form. The pass runs it. That
  `tools/gate-legs.json` also carries the same argv as a leg defers the BAR's run, never this one;
  and that leg is HELD, `chunk = selftests`, so the run covering it is
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at VERIFYING and never a plain
  bar. Each arm's RED is still observed by hand against a scratch fixture with its fix unstaged.
- **AC13** — When the memory-recall kit's `anchor_at` runs over every line the scaffold writes for
  AC10's fixture, it returns no anchor.
  Red when: a generated bullet reads `- EXMP-aFoo-3 — …`, which anchors a foreign id under the new
  build.
  fixture: the selftest reaches `anchor_at` through this kit's OWN route,
  `corpus_ids.resolve_anchor(root)`, bound to the scratch tree the scaffold just wrote. An absent or
  outdated memory-recall kit raises that route's named `Problem`, which this arm catches and prints
  as a skip naming the arm and the kit — never a pass, and never a silent `None`.
  ONE G3 round-2 finding against this criterion is still a unit of this build rather than an edit
  here, and it keeps its text until that unit lands. H3 measured that `anchor_at` admits only the
  conf's declared families, so an `EXMP` id anchors nothing before the scaffold writes a line and
  this criterion's `Red when:` cannot fire; `TOOL-dDerivedDocket-51` picks the family the fixture
  files under and pins the staged RED. Until it lands, a green run of this arm is not evidence that
  a generated body anchors nothing.

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
  delegated): (b), with the live-build set supplied only by a caller that can observe every live run;
  the ask driver cannot and passes none (unit 16 §8 F2 at rev-2).
- **F3 — where does the `PROBE_ALLOW` key live?** RESOLVED (agent, 2026-09-14, delegated): in
  `.memory-tree.conf`, beside `ASK_CUTOFF`, because the only runner is this kit's `--probe`.
- **F4 — check 13's pre-cutoff scoping (D12-g).** RESOLVED (agent, 2026-09-14, delegated): unit 8's,
  as the spec brief's roster assigns, so the skip and its scope land as one change.
- **F5 — how is `PROBE_ALLOW` written and matched?** Options: whitespace entries by string prefix;
  whitespace entries by token equality; `|` entries of whole tokens by token-sequence equality. The
  first admits `python3x` and `tools/../x`; the first two cannot express an entry narrower than one
  interpreter. RESOLVED (agent, 2026-09-14, delegated): the third, the only one under which §5's
  security claim holds.
- **F6 — does a SCOPE row's `accept` satisfy V14?** Options: the ask row's own clauses; the merged
  clauses. The first gives V14 and R5 two answers to one question and leaves a non-filer no way to
  cure an ask without writing into its home folder. RESOLVED (agent, 2026-09-14, delegated): the
  merged clauses, the same merge R5 reads.
- **F7 — which command does `--probe` run when two merged `seen` values carry `run`?** Options:
  refuse; the ask row's; each. RESOLVED (agent, 2026-09-14, delegated): refuse as ambiguous; running
  a second writer's command for someone else's ask widens the exec surface (veto 3), and ignoring it
  is silent.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from design §19.3, fixes F2, F5 and F6, and rulings D12-a, D12-d
  and D12-e. Adds consumes-from unit 7, whose print mode and render this unit extends, hands-off
  units 17, 19, 24 and 34, whose specs declare the consuming end, and hands-off unit 20, whose
  carriers state this unit's grammar as contract. Leaves D12-g to unit 8 per the
  brief's roster: unit 18's spec says unit 15 refines check 13, and one of the two pointers is wrong.
- rev-2 · 2026-09-14 · §3 §4 §5 §8 · S4 S7 S8 · AC1 AC2 AC4 AC5 AC6 AC7 AC9 AC10 AC13 · spec audit
  round 1 (G3) folded: H1 `--tsv` owns stdout, one rule with unit 7 (G2 M4); H2 every field's value
  set, `-` for every empty field; H10 the scaffold writes `ids:` and `status: OPEN`, AC10 staged end
  to end; H11 `PROBE_ALLOW` grammar (§8 F5); M11 generated bodies anchor nothing (AC13); M14 a failing
  fixture per READY rule; M15 AC7 asserts every position; M16 AC1's fixture carries ` · out `; M17 V14
  reads the merged clauses (§8 F6); L1 `--probe` refuses two `run` values (§8 F7); H4 the ask driver
  passes no live-build set (unit 16 §8 F2 at rev-2); M8 §3 lists which mode-scoped directives bind
  the scaffold's README. AC9's two-token fixture names `p.py` and `q.py` at the fixture root, so no
  untracked path reaches the spec-token join.
- rev-3 · 2026-09-16 · regrounded on fb07ca25 (origin/main). No S-item, criterion or fork moves:
  `gen_build_index.py` and `extract.py` are unchanged since `abac6d59`, so every §4 citation holds
  but the two-answers refusal's, one line early at `abac6d59` too and now `:644-649`, and nothing
  landed that grades an ask or scaffolds a README. §4 Files touched names the staged
  map regeneration the dUnstagedSymbol pre-commit leg (`1a774fcd`) now refuses without. §10 records
  the re-run reuse lookups with each neighbour's own file, the new BASE, and that TOOL-aProbedUnit-1
  (`5493495a`) and TOOL-aDeferredBar-2 (`1afd26c9`) leave AC12 as written.
  Extended 2026-09-20, same base, by the regrounding consolidation pass, which changed nothing here
  and records why. AC12's observation is a `--selftest` FLAG on another file, which the header of
  `tools/unattended/gate-guard.js` and the unit child prompt both name as a pass's direct check, so
  it is not deferred. §7's `New arm:` third field stays
  `none`, because `gen_build_index.py` pins no executed-assertion floor. No criterion here asserts
  that a phrase counts zero, and this unit writes to no byte-capped carrier.
  Extended again on the closing consolidation pass · AC12, the one item left open here. The two
  clauses pointed opposite ways because the same argv is a `--selftest` flag AND the
  `build-index selftest` leg's own row in `tools/gate-legs.json`. RESOLVED (agent, 2026-09-20,
  delegated), decided by the orchestrator: the FLAG clause wins, so the pass runs it and nothing
  about it defers. AC12's `cost:` and `permission:` lines are rewritten to say which clause
  applies and why, in place of the earlier text that kept the arms in the pass and sent the run
  itself to the post-build bar — one criterion cannot sit on both sides of the rule. The
  deferral that does survive is the BAR's: that leg carries `chunk = selftests`, so a bar only
  reaches it under `GATE_SELFTESTS=1`, which is a property of the bar and not of this criterion.
  Extended again on the close-out pass, same base and rev · AC12, the only line owed anything here.
  Its `permission:` line names the run that covers the held leg in the terms the build now uses,
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at VERIFYING, so the deferral it
  describes cannot later be read as satisfied by a plain bar. The criterion itself does not move:
  Rule 1's narrow reading leaves a `--selftest` FLAG on another file in the pass, and this spec
  writes to no byte-capped carrier, so the net-zero rule reaches nothing here.

- rev-4 · 2026-09-20 · spec-audit round 3 fold, the G3 round-2 record, which exited BOUNDED.
  §3 Edges · §4 · AC7 AC8 AC10 AC13. M4 (8): S6's "All write nothing and exit 0" was observed for
  `--at` alone, so AC7 now reads exit 0 over an all-`no` fixture and over an empty `--ready` set, and
  AC8's `git status --porcelain` assertion covers a `--tsv --ready --target --live-builds` run
  beside the `--at` one; each half gains its own `Red when:`, the exit-status one naming unit 16's
  producer-failure refusal it would otherwise be mistaken for. M5 (26): §4's scaffold now pins that
  generated slot bodies WRAP under check 7's `BUILD_README_ENTRY_CAP_CHARS`, through the generator's
  own `_render_wrapped_ids` and `IDS_WRAP`, and AC10 measures the written `README.md`'s unfenced
  lines against that cap read from `tools/memory-tree/check-memory-hygiene.sh` rather than against a
  number typed here. Three findings are PROMOTED to units of this build and folded nowhere: H2
  (7, 32) to `TOOL-dDerivedDocket-50` and H3 (22) to `TOOL-dDerivedDocket-51`, both pointed at from
  AC13, and H5 (25) to `TOOL-dDerivedDocket-53`, pointed at from §4's READY block. §3 gains a
  consumes-from edge to each, and S6, §4's predicate, §5's cost line and AC13 keep their current
  text. No cap is raised, §7 does not move, and this unit still writes to no byte-capped carrier.
- rev-5 · 2026-09-20 · §2 · S6 · the round-3 fold's verifier, repairing the M4 fold above. That
  fold gave AC7 an arm over a `--ready` naming no id, pinning `examined` 0 and exit 0, on an input
  no design section admitted: nothing said whether a bare `--ready` is accepted at all rather than
  refused as a usage error, and nothing said the examined population is the IDLIST rather than the
  filed rows. Both are now S6's, stated once: `--ready` sets the examined population to the ids its
  list names, an empty list is accepted rather than refused, and M and that population are both
  empty, so the arm's `examined` 0 and exit 0 follow from the design instead of being pinned by a
  criterion. AC7 does not move. This entry is its own line with a single bump, the form this
  group's other five specs took for the round-3 fold.
  Extended on the promote close-out pass, same base and rev · §3 Edges · a hands-off edge to
  `TOOL-dDerivedDocket-48`, the reciprocal of that unit's consumes-from: this unit's stdout-only
  rule is what its capture split delivers to the witness parse. That unit and
  `TOOL-dDerivedDocket-49` share this unit's order 15, which is legal because a consumes-from
  target may share an order and may not be later, because orders 1 to 38 were taken, and because
  both must land before `TOOL-dDerivedDocket-16` consumes them; dispatch is strictly sequential
  within a shared order and the id tiebreak runs 15, then 48, then 49, so the sequence is the
  guarantee and no disjointness is claimed here. Nothing else moves: S6, §4's READY block, §5's
  cost line and AC13 keep the text the round-3 fold left them.
- rev-6 · 2026-09-21 · §3 Edges · AC13 · §10 · written by `TOOL-dDerivedDocket-50`'s own pass, in that
  unit's commit, because that unit is what the parked text was waiting for. AC13's `fixture:` line
  routed through `RECALL_CLI`, a conf key the unattended kit declares and the memory-tree kit does
  not, so on any tree that adopted this kit without that one the arm would have taken its named skip
  for ever. It now names `corpus_ids.resolve_anchor(root)`, the in-kit route unit 50 added, and the
  paragraph that parked H2 leaves with the key it parked. H3 and its `TOOL-dDerivedDocket-51`
  hand-off are untouched; no other criterion, scope item or gate line moves.

## 10. Reuse audit

The seams are the generator's own: `_expand_ids` for ranges, the `--write` render for the scaffold's
regions, the `SLOT_CANON` and readme-contract registry for its shape, and unit 7's `--asks` for the
print path. `python tools/codebase-map/reuse_lookup.py "parse clause tail of a row and grade
readiness"`, re-run at `fb07ca25`, returns name-stem neighbours (`parse` in
`tools/memory-recall/query.py`, `parse_args` in `tools/govkit/govkit.py`, `parse_conf` in
`tools/memory-tree/corpus_ids.py`) and no readiness grader; `reuse_lookup.py "scaffold a new build
readme with front matter"` returns `build_*` helpers and no scaffold. No existing seam fits the
predicate or the scaffold: nothing in the tree grades an ask or writes a build README, and no build
landed between `abac6d59` and `fb07ca25` adds one (no tracked file outside this build spells
`--new-build`, `PROBE_ALLOW` or `ASKS_CMD`). The recall probe returned design §19 and
`TOOL-aUnmannedHelm-4`, and no prior record of an ask envelope.

Where the design and BASE disagree: design §19.3's example locator `` `tools/push-main.sh`:212 `` is
illegal under fix F6; design §19.8 U10 places the check-13 scoping here and the brief places it in
unit 8. BASE is `fb07ca25`, origin/main after 210 commits past `abac6d59`. `gen_build_index.py` and
`tools/memory-recall/extract.py` did not change between `09a22d2b` and `fb07ca25`, so every line
citation above holds, the two-answers refusal's corrected to `:644-649` because it was one line early
before, and `SLOT_CANON`, `derive_status`, `_expand_ids` and the readme-contract registry's bound and
exempt rows keep their meaning. Two landed builds bind this unit's pass without
changing its design: TOOL-aProbedUnit-1 puts "no gate, suite or bar inside a pass" in the child
prompt, which AC12's `permission:` line already follows; and the pre-commit codebase-map leg of
dUnstagedSymbol, which Files touched now names. AC12's `--selftest` flag form is not a match for the
spec-token `bar` join or for `tools/unattended/gate-guard.js`, both of which read a flag on another
file as the direct check.

The anchor predicate AC13 asks for is NOT a seam this unit adds either: `TOOL-dDerivedDocket-50`
landed `corpus_ids.resolve_anchor(root)` as the kit's one public route from a repository root to
that predicate, so this spec extends that route rather than deriving a second one.

Recall terms used: `acceptance-underivable orientation ask row pointer observable cut-line resolution
table ids-driven run`
