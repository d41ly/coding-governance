# TOOL-dSafePassage-101 — the three bar legs this build's diff turns red at `70273a468`, each cleared by the remedy its own message names

**Status:** CLOSED · rev-2 · 2026-11-01 · node a · Tier-2 · base 70273a468 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-82

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md](../build/2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 TOOL-dSafePassage-84 TOOL-dSafePassage-86 TOOL-dSafePassage-87 TOOL-dSafePassage-88 TOOL-dSafePassage-89 TOOL-dSafePassage-90 TOOL-dSafePassage-91 TOOL-dSafePassage-92 TOOL-dSafePassage-93 TOOL-dSafePassage-94 TOOL-dSafePassage-95 TOOL-dSafePassage-96 TOOL-dSafePassage-97 TOOL-dSafePassage-98 TOOL-dSafePassage-99 TOOL-dSafePassage-100 TOOL-dSafePassage-102 TOOL-dSafePassage-103 |
| [2026-11-01-build-TOOL-dSafePassage-101-ledger.md](../build/2026-11-01-build-TOOL-dSafePassage-101-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-101-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-101-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-101-2-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-101-2-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-101-audit-fold-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-101-audit-fold-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dSafePassage-101-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-101-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-101-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-101-spec-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dSafePassage-99-rev3-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-99-rev3-brief.md) | research | TOOL-dSafePassage-99 |
| [2026-11-01-review-TOOL-dSafePassage-101-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dSafePassage-101-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's merge bar at `70273a468` reds four of 75 legs. Three are this build's own: `memory
hygiene`, `shell hygiene (a loop fed by a command substitution)` and `install-prefix (shipped
surface)`. This unit clears each one by the remedy its own refusal names. It uses no waiver, no
exemption and no raised count. After it, `install-prefix` still reds on the three
`tools/run-gates/ceiling-evidence.txt` lines, and the spawn budget leg reds on its five rows. Both
belong to the ask TOOL-dSafePassage-85, and this unit leaves them as they are.

## 2. Scope (IN)

- **S1 — memory hygiene check 12, brief id 1.** TOOL-dSafePassage-99's §3 `### Edges` block drops
  its two `**consumes-from**` bullets and reads `none`. A prose paragraph under it names
  TOOL-dSafePassage-87 and -71 as CLOSED units whose landed code 99 reads (§4 "The edge ruling").
  99 moves to rev-3, and its §9 gains a rev-3 line naming §3, check 12 and this unit. 99 stays
  CLOSED. A gov-spec-writer pass made this edit, because scratch-guard lets only that role write the
  spec class, and it landed at `a78d6affc` with the build README's re-render. Observed by AC1 and
  AC5.
- **S2 — memory hygiene check 23, the form arm, brief id 2.** The seven ledger lines in neither
  legal form each take the OBSERVED form, with a backticked token on their first line that their
  criterion also carries. Each records only what a tracked record already observed, or, for
  TOOL-dSafePassage-80/AC2, what the main loop observes at this unit's build head. The 80/AC2,
  95/AC4 and 96/AC4 lines carry the clauses §4 "The seven lines" requires. Observed by AC2, AC5 and
  AC14.
- **S3 — memory hygiene check 23, the join arm, brief id 2.** The answers TOOL-dSafePassage-59/AC12,
  -77/AC8 and -82/AC2 each gain one backticked token their criterion carries, in a clause that
  names what was observed or what was not. 59/AC12 gains it on a new continuation line, so its first
  line keeps the AMENDED form. No observation changes (§4 "The three answers"). Observed by AC3 and
  AC5.
- **S4 — memory hygiene check 15 rule 1, not named by the brief.** The ask row
  TOOL-dSafePassage-79 in `memory/builds/dSafePassage/BACKLOG.md` cites
  `tools/govkit/upgrade_walk.py` with its line locator inside the backticks. The locator moves out of
  the backticks, and the row keeps its words (§4 "The dead citation"). Observed by AC4 and AC5.
- **S5 — shell hygiene, brief id 3.** The two loops in `tools/push-main.test.sh`, arms 25 and 35, and
  the one in `tools/lib/resolve-python.test.sh` that counts the floor check's pinned statements each
  read from a scratch file. A `printf` writes the captured value to that file. The leg then measures
  no `<<<` site in the lander suite, and one in the resolver suite, which is what its registry row
  declares. The registry is not edited (§4 "The three loops"). Observed by AC6, AC7, AC8 and AC9.
- **S6 — install-prefix, brief id 4.** The five lines the leg names in `tools/govkit/selftest.py` and
  `tools/govkit/upgrade_walk.py` derive each kit path, either from the file's own location or
  through `resolve_kit_dir`, which is the resolver the leg's message names (§4 "The five
  spellings"). The grader loop's handler in `tools/govkit/upgrade_walk.py` also catches the two
  exceptions the new derivations can raise. Observed by AC10, AC11, AC12, AC13, AC15, AC16 and AC17.

## 3. Non-goals (OUT)

- Any edit to `memory/project/fork-ceilings.txt`, `tools/run-gates/ceiling-evidence.txt` or the
  spawn budget's rows. Those belong to the ask TOOL-dSafePassage-85.
- Any edit to `memory/project/substitution-fed-loops.txt`, `memory/project/corpus-path-unresolved.txt`
  or any other registry, and any raised count, pin, ceiling or waiver.
- Any change to a gate, its checker or its manifest row, other than S6's edits of the two graders
  and their loop's handler in the upgrade walk. Those change no verdict at gov (§4 "The five
  spellings").
- Any edit to a CLOSED spec other than S1's edit of TOOL-dSafePassage-99. TOOL-dSafePassage-87 and
  -71 gain no `**hands-off**` line. The specs of 59, 77, 80, 82, 88, 89, 95 and 96 do not change.
- A new observation of a criterion that the close observed in part. Where a record holds only part
  of what its criterion names, the ledger line says which part is not recorded (§4 "The seven
  lines").
- Any change to what a ledger line records as observed.
- `tools/push-main.sh`, which no leg names here.
- A `RUN.md` row, and a help page. No change here is user-facing.

### Edges

- **consumes-from** external — the gov-spec-writer pass that carries S1's edit of the
  TOOL-dSafePassage-99 spec, with that spec's rev-3 line and the build README's re-render. It landed
  at `a78d6affc`. AC1 grades that commit and not the working tree, so an uncommitted edit of 99
  does not satisfy it.
- **consumes-from** external — the main loop's run of the ceiling checker at this unit's build head,
  for the TOOL-dSafePassage-80 AC2 line of S2. Scratch-guard row G1 refuses that checker to a role
  agent (`tools/hooks/README.md`, the G1 row). Without the run, that line has no observation to
  record, AC14 stays red, and S2 is not done.

TOOL-dSafePassage-59, -71, -77, -80, -82, -87, -88, -89, -95, -96 and -99 are CLOSED. They are named
here rather than joined.

## 4. Design

Every line cited here was read at `70273a468`, the HEAD this spec was written at, on 2026-11-01 on
node a. For rev-2 each was re-read at `a78d6affc`. `git diff --stat 70273a468 a78d6affc` names no
file under the tool root, no ledger and no `BACKLOG.md`, so every cited line holds at both. The bar
log is the close's run at `70273a468`, copied to
`C:/Users/daily-agent/AppData/Local/Temp/dsp86-logs/bar-70273a468.log`. Every measurement below was
made on 2026-11-01 on node a.

### The reds at `70273a468`

- `memory hygiene` printed two check 12 lines (log lines 38-40), one check 15 rule 1 line (log line
  65) and two check 23 lines (log lines 80-81), and exited 1. §6 quotes each line beside the
  criterion it reds.
- `shell hygiene (a loop fed by a command substitution)` printed two findings (log lines 101-103):
  the resolver suite measures 2 `<<<` sites against its row's 1, and the lander suite has 2 sites
  that no row declares.
- `install-prefix (shipped surface)` printed 9 kit-path spellings on 8 lines (log lines 174-186).
  Five of those lines are this unit's. The three `ceiling-evidence.txt` lines are not.
- The fourth red leg, the spawn budget (log lines 107-171), is not this unit's.

The brief names checks 12 and 23. The memory hygiene leg also reds on check 15 rule 1. That is
emitted by `tools/memory-tree/corpus_ids.py` lines 896-899, and the hygiene script sets its status
from that exit (`tools/memory-tree/check-memory-hygiene.sh` lines 3127-3132). The leg cannot go green
without it, so S4 carries it.

### The edge ruling

Check 12's reciprocity arm reds when a `**consumes-from**` bullet names a sibling in the graded
population, and that sibling declares no matching `**hands-off**` back
(`tools/memory-tree/check-memory-hygiene.sh` lines 2926-2931). A reciprocity red can be answered from
either side. TOOL-dSafePassage-83 answered from the target side in this build and wrote
`**hands-off**` lines into three CLOSED specs. Its §4 "The edge ruling" (83's lines 123-148) gives
three reasons for that side. This unit answers from the consumer side, and it answers each of 83's
reasons by name below.

The two rulings stand side by side. 83's governs the edges 83 wrote, and this one governs 99's.
Neither is a rule for the build, and a later red of this shape chooses again, citing both.

- **The rule.** 83 reads `memory/TEMPLATE-SPEC.md` §3 as making the consumer's line worth keeping,
  because "writing the line requires reading the handoff" (TEMPLATE-SPEC lines 239-241). The same
  section says what an edge is for: "a criterion resting on something the unit does not build"
  (lines 230-233), with a payload naming "what this unit takes, and what breaks without it"
  (line 219). 99's two bullets named code that was landed, in CLOSED units, before 99's spec was
  written: 87 AC6's staged load and 71's `build_staged_copy`. No criterion of 99 rests on work that
  87 or 71 still owes, so there is no handoff for a reciprocal line to prove was read. A
  `**hands-off**` line written into 87 or 71 now would be written by a spec-writer pass, not by
  either unit's author. That is the rubber-stamped reciprocal that TEMPLATE-SPEC line 240 says
  passes. 83's other concern under this reason, that deleting the line erases a true fact, is met:
  99's paragraph names both units and the code 99 reads. What goes is the join, which "What it does
  not cover" states.
- **The precedent.** 83's precedents stand: the earlier builds that met this shape wrote the
  target's line, CLOSED specs included. This unit does not cite TOOL-dSafePassage-70 against them.
  70's commit `46f1375df` says a CLOSED spec "cannot gain the reciprocal hands-off line", and 83
  showed that this is not so. This ruling rests on the template text quoted under the first reason,
  and not on 70.
- **Nothing landed is rewritten.** This holds here too. The specs of 87 and 71 are not on main:
  `git cat-file -e origin/main:<spec>` exits nonzero for both, with origin/main at `f4597719e`. So
  editing their CLOSED revisions would rewrite nothing landed, and this unit does not reject the
  target side on that ground. It rejects it on cost. Each CLOSED revision is a departure that
  `tools/memory-tree/deviation_join.py` counts and the close records (83's line 144). The consumer
  route cost one revision, 99's rev-3, which landed at `a78d6affc`. The target route would now cost
  three: 87, 71, and a 99 rev-4 that restores its bullets. The brief asked for the remedy that edits
  no other CLOSED spec, and once the first two reasons are answered, nothing outweighs that.

The check's own text admits the consumer side in three ways, and only one fits:

- `none` is a legal Edges body. The awk reads a `none` line as the declared absence (line 2684) and
  skips any line that is not a bullet (line 2685). So `none`, followed by a prose paragraph, passes
  the shape arm and gives the joins nothing to read. An Edges block with neither a bullet nor `none`
  is a finding (lines 2709-2712).
- `**consumes-from** external` is refused when its backticked prose names a sibling in this build
  (lines 2916-2922). 87 and 71 are in this build, so that would be a joinable edge written as an
  unjoinable one, which is the shape the arm exists to refuse.
- A target outside the population is silent (line 2928), but 87 and 71 are Tier-2 and graded.

The paragraph that replaced the two bullets landed at `a78d6affc` as 99's lines 68-71. It reads:

> TOOL-dSafePassage-87 and -71 are CLOSED, and this unit reads their landed code: 87 AC6's staged
> load at selftest.py:3179-3182, the load that displaces the engine, which AC1 re-runs unchanged, and
> 71's `build_staged_copy`, which S3's arm stages its copy through. They are named here rather than
> joined, so neither CLOSED spec gains a line (TOOL-dSafePassage-101 S1).

The line numbers are 99's own, read at `f519c1934`, and are unbackticked as 99 writes them. 99's
header reads rev-3 (its line 3), and its §9 rev-3 line (its line 332) names `§3`, so
`REV_SCOPE_CUTOFF` is satisfied. Check 12's REV_SCOPE arm grades only rev entries that exist, so it
would not have caught a missing bump. AC1 observes both lines at `a78d6affc`.

### The seven lines

Check 23 reads an answer's FORM from its first line alone. A line carrying a backticked token pair
is OBSERVED, a line naming `amended rev-N` is AMENDED, and anything else is `bad`. The backtick test
runs first (`tools/memory-tree/check-memory-hygiene.sh` line 3364). An AMENDED line needs a spec
revision of the CLOSED unit, and §3 rules that out. So each of the seven lines takes the OBSERVED
form, and its first line opens with a token its criterion also carries. Each line records what its
source records, and nothing more. Where that source holds only part of what the criterion names,
the line says which part it does not hold. Re-observing that part now would observe this HEAD and
not the unit's own build. 95's ledger already notes one such drift: 96 changed what 95's
`check_runs` break fails.

| Ledger line | Opens with | Source of the observation |
|---|---|---|
| 80/AC2, line 28 | `python tools/run-gates/derive-ceilings.py --check` | the main loop's run at this unit's build head (§3 Edges) |
| 88/AC2, line 29 | `FOREIGN_PREFIX_PROBE=1 python upgrade_walk.py --case up` | the ledger's own "AC2 — observed at the close" paragraph, line 34: `upgrade-walk: GREEN`, exit 0 in 335 s, at `112e587ea` |
| 89/AC2, line 25 | `FOREIGN_PREFIX_PROBE=1 python upgrade_walk.py --case up` | the ledger's own paragraph, line 30: the `upgrade-walk: pin` line, no `no registry at` line, exit 2 in 222 s, at `ed22e3ef4` |
| 95/AC4, line 27 | `os.utime` and `shutil.rmtree` | the ledger's close paragraph, line 29, batch g in a scratch clone of `390033278` |
| 96/AC2, line 24 | `steps._BASH = None` | the ledger's close paragraph, line 29: all four checks red, details naming `argv94` and `cut94 ['dsp95-sentinel', 'x']` |
| 96/AC3, line 25 | `except OSError:` | the same paragraph: the raise-path `[dSP-95]` red naming `cut94 ['bash', 'x']`, the return-path one `ok` |
| 96/AC4, line 26 | `finally` | the same paragraph: the `finally` cut reds both restore checks |

Three lines carry clauses on their first line, beyond the opening token, and AC14 reads each one:

- **80/AC2.** The line says `not observed in 80's own pass`. It then gives the main loop's run,
  verbatim: the commit it ran at, as `at` and the sha in backticks, the words `exited` and its exit
  code, and the out-of-band line in backticks. That line opens `derive-ceilings:` and holds
  `OUTSIDE the runner`, as `cmd_check` prints it (`tools/run-gates/derive-ceilings.py` line 708).
  The line does not say `owed`. The checker's inputs read as 80 graded them. Over the checker,
  `tools/run-gates/ceiling-evidence.txt` and `tools/run-gates/ceiling-margin.txt`,
  `git diff --stat ec870d637 a78d6affc` prints nothing. Over `tools/gate-legs.json` it prints one
  changed line, the upgrade-walk row's `reads` text, from `5fe2dab8e`. No ceiling moved:
  `git diff -U0 ec870d637 a78d6affc -- tools/gate-legs.json | grep '"ceiling"'` prints nothing.
  The checker reads every leg's ceiling, 148 at `a78d6affc`, because `cmd_check` (line 643) loops
  over every leg (line 654). All of this was measured on 2026-11-01. If the run prints something
  AC2 of 80 does not expect, the line records what it printed, AC14 reds, and the divergence goes
  back to the main loop. It is not this unit's to amend.
- **95/AC4.** The close's paragraph records the `os.utime` and `shutil.rmtree` cuts at 6 of 6 RED,
  and it records the `finally` cut, the restore moved onto the return path, the lost colon, the
  second anchor and the cache removed before `pyc94`. The line says `not recorded`, and names the
  row that also cuts S4's `memo guard`, whose run ends in an `AttributeError`. The same clause names
  the `steps._BASH = None` row and the `except OSError:` row as not recorded under 95's own text,
  because 96's paragraph records both at its HEAD.
- **96/AC4.** The line opens with `finally` and says the `finally` cut reds both restore checks. It
  then says `not recorded`: whether `every other line` read `ok`.

The 88 and 89 lines keep their words "not observed in this pass" and point at the paragraph below
them, which stays as it is.

### The three answers

Check 23's join arm reads the answer's tokens across the whole bullet and its continuation lines.
Every non-blank line up to the next bullet or heading adds its tokens, while the form stays the
first line's (line 3373). A pair passes when one token contains the other, after case folding
(lines 3506-3518).

- **59/AC12.** The ledger's line 37 is the whole bullet:
  `- AC12 — amended rev-3 — struck with S4, its number kept; logged in §9's rev-3 line.` It carries
  no token, and no clause names what the struck criterion counted, so the clause is added rather
  than extended. Line 37 does not change. A new continuation line, indented two spaces, is added
  under it as line 38, and the two read:
  ```
  - AC12 — amended rev-3 — struck with S4, its number kept; logged in §9's rev-3 line.
    It counted a phrase in `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-43.md`; nothing is observed, because the criterion is struck.
  ```
  That path is the criterion's one token (59's spec, lines 294-296), and it is tracked. The form
  test reads only line 37, which holds no
  backtick and still names `amended rev-3`, so the answer stays AMENDED under check 23. The LEDGER
  regex of `tools/memory-tree/deviation_join.py` (line 163) still matches line 37, so the deviation
  join reads it as AMENDED too. AC3 observes both.
- **77/AC8.** The line opens `owed: one case per arm.` and then records a stubbed probe. The
  criterion's tokens are `python tools/govkit/upgrade_walk.py --case kill --inject witness-first`,
  `needle` and `Stop`. The owed clause gains the first of these, as the real run that is owed. No
  later record observed those runs (`git grep` for `--inject witness-first` over the build's records
  outside `spec/` names only TOOL-dSafePassage-5's ledger, at its own pass). So the line stays a
  stubbed observation with its real runs owed, and says so.
- **82/AC2.** The criterion's backticked command wraps across two lines. The extractor reads a token
  only within one line, so the criterion's single readable token is `fetch.py`, from its Red-when
  line. The answer gains one sentence: the `fetch.py` program is text inside
  `tools/govkit/upgrade_steps.py`, so the grep read it. That holds at 82's build commit `5fe2dab8e`,
  where `"fetch.py": (` sits at that file's line 2815. It holds at HEAD too, at line 2822.

### The dead citation

`corpus_ids.py` cuts a `:<line>` locator only from the advisory build-README population (line 557,
used at line 603). In the present-tense corpus, which includes `builds/*/BACKLOG.md` under
`BACKLOG_MODE=builds`, `tools/govkit/upgrade_walk.py:944` inside backticks is one token that resolves
to nothing. The registry cannot take a row: `DEAD_PATH_PIN` is `"0"` (`.memory-tree.conf` line 455),
and rule 2 reds any row over the pin (`corpus_ids.py` lines 900-902). So the citation is repaired.
In the parenthesis at `memory/builds/dSafePassage/BACKLOG.md` line 7, the backticks close after
`tools/govkit/upgrade_walk.py`, and the words ", line 944 when filed" follow outside them. The ask
row stays filed once, in its own build's folder. Only its text changes, and it remains CLOSED by
TOOL-dSafePassage-77. Why no earlier bar named the citation, which `84ffa523f` added on 2026-10-28,
is UNVERIFIED.

### The three loops

`sh_hygiene.py` grades a `<<<` loop whose expansion names a variable assigned from a command
substitution above it (`tools/gate-lint/sh_hygiene.py` lines 335-340). Its remedy is a scratch file
read by redirect, which keeps the loop in the current shell (lines 64-66). A redirect from a file
matches no classifier.

| File | Loop at `70273a468` | Fed by | After |
|---|---|---|---|
| `tools/push-main.test.sh` | arm 25, lines 914-917, `done <<<"$out25"` | `out25=$(` at line 895 | `printf '%s\n' "$out25" >"$tmp/out25.txt"` above the loop, and `done <"$tmp/out25.txt"` |
| `tools/push-main.test.sh` | arm 35, lines 1375-1377, `done <<<"$out35"` | `out35=$(` at line 1362 | `printf '%s\n' "$out35" >"$tmp/out35.txt"`, and `done <"$tmp/out35.txt"` |
| `tools/lib/resolve-python.test.sh` | line 265, `done <<<"$out"` | the `out=$(` at line 263 | `printf '%s\n' "$out" >"$TMP/floor-rev.txt"`, and `done <"$TMP/floor-rev.txt"` |

`$tmp` is the lander suite's `mktemp -d`, removed on exit (lines 177-178). `$TMP` is the resolver
suite's, also removed on exit (line 33). `printf` is a builtin, so the comment above the resolver
loop, "The statements counted with no fork", stays true. A here-string appends one newline, and
`printf '%s\n'` appends the same one, so each loop reads the same lines.

The resolver suite's other `<<<` loop, `done <<<"$copies"` at line 422, is the site its registry row
declares. It stays. After S5 the leg measures 58 sites, which equals the registry's sum: 43 rows
whose count column sums to 58, read from `memory/project/substitution-fed-loops.txt` at
`70273a468`. The log's gated populations sum to 61, which is 18 plus 2 plus 41, and 61 less this
unit's 3 is 58.

Arm 35's edit and the resolver block's edit were run before writing, in the session scratchpad, on
cut copies. Arm 35, cut from `out35=$(` to its `esac` with `lander`, `tmp`, `ok` and `bad` set,
printed its `ok — 35` line at HEAD and with the file feed. With the `printf` line cut, it printed
`FAIL — 35 the skip line was printed 0 time(s) over two absent-deployer runs: ...`. The resolver
block, lines 263 to 268 with `ROOT`, `HERE`, `PFX`, `REALPY` and `TMP` set as the suite sets them,
counted 7 at HEAD and with the file feed. With the `printf` line cut, it printed
`FAIL python_floor.py check --rev 3708a705 did not print the seven pinned statements: ...` and
counted 0.

Arm 25's edit was not run. Its arm clones a fixture and runs the lander, so AC8 cuts only its feed:
the `printf` line through the loop's `done`, over a fixed `out25`. Arm 25 runs only when both
`_mt_gk` and `_ml_lex` are set (line 892), and on node a both are: the govkit and lexicon kits sit
beside the lander, read on 2026-11-01. Where either is missing, the arm prints its skip line
(line 922).

### The five spellings

The leg counts a quoted `"tools"` segment joined to another quoted segment, a kit name followed by
`/` and a file, and a quoted kit name used as a path segment (`tools/check-install-prefix.sh` lines
388-390, with rules 1, 3 and 4 in the header at lines 44-53). Its message names three remedies
(lines 565-567). A kit name held in a variable spells no literal, and the header says so (lines
57-60). The derived names below come from the file's own location, or from the engine's
`GOVKIT_DIR` (`tools/govkit/govkit.py` line 159), which is that file's own location.

| Site at `70273a468` | After |
|---|---|
| selftest.py:4572, `stub92 = root92 / "govkit"` | `stub92 = root92 / HERE.name`, the spelling `build_staged_copy` uses at selftest.py:3658 |
| upgrade_walk.py:1086, `for pre in ("tools", "scripts", ""):` | `gk = load_engine()[2]` and `gkn = gk.GOVKIT_DIR.name` open the function, then `for n, pre in enumerate((gk.derive_tool_root(gk.repo_root()), "scripts", "")):` with `c = scratch / f"pin-{n}"` |
| upgrade_walk.py:1088, `for f in ("govkit/registry.toml", "govkit/govkit.py"):` | `for f in (gk.REGISTRY_NAME, "govkit.py"):`, each written at `c / pre / gkn / f` |
| upgrade_walk.py:1091, `c / pre / "govkit" / "govkit.py"` | `c / pre / gkn / "govkit.py"` |
| upgrade_walk.py:1111, `{f"{pfx}/policy/adopt-policy.sh": ""}` | `poln = gk.resolve_kit_dir("policy", "adopt-policy.sh", HERE).name` after the function's first line and before `t` is built, then `{f"{pfx}/{poln}/adopt-policy.sh": ""}` |

`gk.derive_tool_root(gk.repo_root())` is the walk's own reading of gov's tool root, already used at
upgrade_walk.py:143, and `GOVKIT_DIR.name` is the spelling of upgrade_walk.py:1097. The bare file
names `"govkit.py"` and `adopt-policy.sh` are what `derive_release_engine` (line 206) and
`derive_policy_adopter` (line 213) spell, and the leg names neither. `resolve_kit_dir("policy", ...)`
is line 213's spelling, and the leg does not name it, because rule 4 counts a quoted kit name only as
a path segment (lines 470-482). A scratch copy of the counter's four patterns matched all five old
lines. Of the new lines, it matched only the `resolve_kit_dir` call, by `QKIT` before rule 4's
filter, and that is the filter that leaves line 213 uncounted. At gov the derived values are `govkit`,
`tools` and `policy`, the values the literals spelled, so neither grader's verdict moves at gov. The
pin directories are numbered rather than named by prefix, because a derived tool root may hold a `/`.

Because the derived values equal the literals at gov, no run at gov can tell a derived name from a
literal held in a variable. AC15 runs the graders from a copy whose govkit directory has another
name, where the two diverge. AC16 reads the after-lines' spelling, which also covers the policy kit
name that the renamed copy does not move.

**The grader loop's handler.** The new calls can raise where no handler sits today.
`resolve_kit_dir` raises `LookupError` when the receipt and both probes miss (`tools/govkit/govkit.py`
lines 269-270). `derive_tool_root` raises `Refusal` when it finds no tool root, or more than one
(govkit.py line 209), and `Refusal` is a `RuntimeError` (`tools/govkit/upgrade_steps.py` line 305).
The plant-root grader's only `except LookupError` (upgrade_walk.py line 1118) wraps
`derive_policy_adopter` alone. The loop catches `(Stop, OSError, KeyError, ValueError)` (line 1154),
and `__main__` has no handler (lines 1261-1263). So a miss would end `--list` in a traceback, with
the remaining grader lines and the summary lost. S6 widens the loop's tuple to
`(Stop, OSError, LookupError, ValueError, RuntimeError)`. `KeyError` is a `LookupError`, so the tuple
drops it. The file names no `Refusal` today, so the tuple names its base class rather than importing
a second name. Every caught exception becomes the grader's RED reason, printed as
`it raised <type>: <message>`, so a catch never turns a grader green. A missing gov policy kit then
prints `upgrade-walk: grader · plant-root · RED · it raised LookupError: no policy kit holding
adopt-policy.sh in this install`, and the walk prints its RED summary and exits 1. AC17 observes it.
One handler covers both graders' new calls. A guard inside each grader's body would cover only the
grader it sits in.

### What it does not cover

- The ledger lines are graded for SHAPE. The join reads token presence, so a token in a clause that
  says "owed" satisfies it, as 77/AC8's does. That line stays honest only because its words say the
  run is owed. AC14 reads content for the three lines whose content §4 "The seven lines" requires,
  and only for the phrases it names.
- Under the foreign-prefix leg, gov's tool root is `scripts`. The release-engine grader then grades
  `scripts` twice and the repo root once, and no `tools` pin. At a root install, it grades the root
  twice. Neither grader is graded at another prefix by this unit.
- If gov's own receipt homes the policy kit under another name, `poln` is that name. The target's
  plant then sits where `derive_policy_adopter` reads it only if the target homes the kit the same
  way. Gov's tree has no such row today. A renamed policy kit resolves only through a receipt, and
  no criterion plants one, so AC15 does not move the plant-root grader. AC16 grades its spelling,
  and AC17 grades a missing kit.
- With the widened tuple, a programming error inside a grader that raises a `RuntimeError` or a
  `LookupError` prints as a RED reason with its type and message, not as a traceback. The walk
  still exits 1.
- S1's paragraph is prose, so no join grades 99's dependence on 87 and 71 after this unit.

### Inventory

Minted: no function, type, file, flag, conf key, gate leg, check label or receipt field. The new
locals are in `tools/govkit/upgrade_walk.py`. `check_grade_release_engine` gains `gk`, `gkn` and
`n`, beside the `pre`, `c`, `f`, `got` and `want` it already binds. `gkn` carries the same value
`check_grade_shim_root` binds under that name at line 1097. `check_grade_plant_root` gains `poln`.
That function already binds `gk`, `pfx`, `t`, `real`, `got` and `pol`, and `poln` collides with
none of them, so `pol` keeps its one meaning, the adopter read. The naming lexicon's cells grade
`py.function` and `py.type` (`.lexicon.conf`), so it grades none of the locals. The scratch files
`out25.txt`, `out35.txt` and `floor-rev.txt` live in each suite's own temp directory. They are
written once and never renamed.

### Write sets

The unit splits into two disjoint write sets. Ids 1 and 2, with S4, write only under `memory/`:
TOOL-dSafePassage-99's spec, which the writer pass edited at `a78d6affc`, eight ledgers and the
build's `BACKLOG.md`. Ids 3 and 4 write only under the tool root: the two suites and the two govkit
files. Neither set reads the other as a contract or an acceptance input. So the two sets could build
as two concurrent units. This unit stays one, which is the brief's default and the shape of
TOOL-dSafePassage-82, which cleared six lint legs in one unit.

### Migration

None.

### Rollout

Live at landing, at order 16. 99's rev bump is a revision after its own pass. The build's close
records it with `deviations.py --write`, as TOOL-dSafePassage-83's §4 states for its own three bumps.
Check 30 does not read it.

### Files touched (estimate)

- `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-99.md` — S1, by the writer
  pass, landed at `a78d6affc`.
- `memory/builds/dSafePassage/README.md` — the generated blocks the writer pass re-rendered.
- `memory/builds/dSafePassage/build/2026-10-28-build-TOOL-dSafePassage-80-ledger.md` — S2.
- `memory/builds/dSafePassage/build/2026-10-29-build-TOOL-dSafePassage-88-ledger.md` — S2.
- `memory/builds/dSafePassage/build/2026-10-29-build-TOOL-dSafePassage-89-ledger.md` — S2.
- `memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-95-ledger.md` — S2.
- `memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-96-ledger.md` — S2.
- `memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-59-ledger.md` — S3.
- `memory/builds/dSafePassage/build/2026-10-28-build-TOOL-dSafePassage-77-ledger.md` — S3.
- `memory/builds/dSafePassage/build/2026-10-28-build-TOOL-dSafePassage-82-ledger.md` — S3.
- `memory/builds/dSafePassage/BACKLOG.md` — S4.
- `tools/push-main.test.sh` — S5.
- `tools/lib/resolve-python.test.sh` — S5.
- `tools/govkit/selftest.py` — S6.
- `tools/govkit/upgrade_walk.py` — S6, the five spellings and the grader loop's handler.
- `memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-101-ledger.md` — the
  acceptance ledger.

### Alternatives rejected

- **`**hands-off**` lines on 87 and 71, the route TOOL-dSafePassage-83 took.** §4 "The edge ruling"
  answers 83's three reasons. The route now costs three CLOSED revisions, where the consumer route
  cost one and has landed.
- **`**consumes-from** external` on 99.** Check 12 refuses it, because the prose names in-build
  siblings (lines 2916-2922).
- **The AMENDED form for the seven lines.** Each needs a revision of a CLOSED spec, which §3 rules
  out, and none of the seven criteria was found wrong.
- **The 43-spec path appended to 59's line 37.** The form test reads the backtick first, so the line
  would grade OBSERVED under check 23 while the deviation join still reads it as AMENDED. A
  continuation line keeps one form for both readers.
- **Re-observing 95/AC4's memo-guard row and 96/AC4's other lines at HEAD.** That would observe this
  HEAD and not the units' own builds. §4 "The seven lines" says what each line does not hold.
- **A registry row for the dead citation.** `DEAD_PATH_PIN` is 0, and §3 rules out a raised pin.
- **`n1c=$(grep -c . <<<"$out")` in the resolver suite.** It spends a fork where the comment above
  says the count takes none.
- **A variable holding the literal `"govkit"` or `"policy"`.** That passes the leg by its stated
  blind spot, and derives nothing. AC15 and AC16 red on it.
- **A `try` around the new `resolve_kit_dir` call inside the plant-root grader.** It covers that
  grader only, and leaves the release-engine grader's `Refusal` uncaught.

## 5. Production-readiness checklist

- security: N/A — no write path, spawn, surface or permission changes. Three scratch files land in
  directories each suite already creates and removes.
- perf / scale: each `printf` and redirect is builtin work. The resolver arm keeps its no-fork count.
- error / empty / loading states: a missing scratch file makes the loop read nothing, so its count is
  0 and its arm reds, as §4 "The three loops" measured. It cannot pass silently. In the upgrade
  walk, a `LookupError` from the policy kit's derivation or a `Refusal` from the tool root's
  derivation is caught by the grader loop's widened tuple and printed as that grader's RED line.
  The walk then prints its RED summary and exits 1, instead of ending in a traceback (§4 "The five
  spellings"). AC17 observes the policy case.
- observability: no new output. Each arm's FAIL line already names the count it read, and each
  grader's RED line already names the exception it caught.
- risks: a derived tool root at a foreign prefix collapses the release-engine grader's three pins to
  two (§4 "What it does not cover"). A ledger line written past its source would be a false record,
  and §3 forbids it.
- testing: AC1 to AC17, and four `New arm:` lines (§7).
- migration: N/A — no data or state changes.
- user docs: N/A — no page under `help/` names a ledger, the edited arms or the graders.

## 6. Acceptance criteria

- **AC1** — When
  `git grep -n -E '^- \*\*(consumes-from|hands-off)\*\*' a78d6affc -- '*spec-TOOL-dSafePassage-99.md'`
  runs from the repository root, it prints nothing and exits 1. At the same commit, three more
  commands each print one line.
  `git grep -n -E '^\*\*Status:\*\* CLOSED · rev-3 ' a78d6affc -- '*spec-TOOL-dSafePassage-99.md'`
  prints 99's line 3.
  `git grep -n -E '^- rev-3 · .*§3' a78d6affc -- '*spec-TOOL-dSafePassage-99.md'` prints 99's line
  332.
  `git grep -h -A2 -E '^### Edges' a78d6affc -- '*spec-TOOL-dSafePassage-99.md' | tail -n 1`
  prints `none`, the first non-blank line of the Edges block.
  `git grep -c -F 'They are named here rather than' a78d6affc -- '*spec-TOOL-dSafePassage-99.md'`
  counts 1, the paragraph under it. All five were measured at `a78d6affc` on 2026-11-01.
  Red when: 99's two bullets stay, or its header or §9 carries no rev-3. At `70273a468` the first
  grep prints 99's lines 64 and 66, the rev-3 greps print nothing and exit 1, the Edges probe prints
  the first `**consumes-from**` bullet, and the paragraph count prints nothing, all measured. The
  memory hygiene leg printed:
  ```
  HYGIENE check 12 FAILED — a §3 edge names a sibling that declares no matching edge back, so one author read the handoff and the other never saw it:
  memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-99.md (§3 declares **consumes-from** `TOOL-dSafePassage-87` and that unit declares no matching **hands-off** `TOOL-dSafePassage-99` back)
  memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-99.md (§3 declares **consumes-from** `TOOL-dSafePassage-71` and that unit declares no matching **hands-off** `TOOL-dSafePassage-99` back)
  ```
- **AC2** — When
  `git grep -n -P '^- *(\*\*)?AC\d+(?!.*\x60[^\x60]+\x60)(?!.*amended rev-\d)' HEAD -- '*/dSafePassage/build/*.md'`
  runs from the repository root at the build commit, it prints nothing and exits 1. The pattern is
  check 23's form predicate (`tools/memory-tree/check-memory-hygiene.sh` lines 3361-3364): a label
  bold or plain, a backtick PAIR for OBSERVED, and `amended rev-N` for AMENDED. It reads every line
  of those records, not only the ledger records check 23 selects, so it can over-report and cannot
  under-report.
  Red when: any of the seven lines keeps its form. At `a78d6affc` the grep prints exactly those
  seven, measured: 80's line 28, 88's line 29, 89's line 25, 95's line 27 and 96's lines 24 to 26.
  The leg printed, at `70273a468`:
  ```
  HYGIENE check 23 FAILED — an acceptance-ledger line is in neither legal form, and there is no third: OBSERVED carries a backticked token, AMENDED names the revision, and anything else is a checkbox: TOOL-dSafePassage-80/AC2 TOOL-dSafePassage-88/AC2 TOOL-dSafePassage-89/AC2 TOOL-dSafePassage-95/AC4 TOOL-dSafePassage-96/AC2 TOOL-dSafePassage-96/AC3 TOOL-dSafePassage-96/AC4
  ```
  fixture: a `git` built with PCRE, as Git for Windows is on node a, measured.
- **AC3** — When
  `git grep -n -F -e '2026-10-23-spec-TOOL-dSafePassage-43.md' -e '--inject witness-first' -e 'fetch.py' HEAD -- '*build-TOOL-dSafePassage-59-ledger.md' '*build-TOOL-dSafePassage-77-ledger.md' '*build-TOOL-dSafePassage-82-ledger.md'`
  runs from the repository root at the build commit, it prints exactly three lines: 59's new line
  38, under its AC12 bullet, 77's AC8 answer and 82's AC2 answer. At the same commit,
  `git grep -n -P '^- AC12 — amended rev-3(?!.*\x60)' HEAD -- '*build-TOOL-dSafePassage-59-ledger.md'`
  prints one line, 59's line 37, which holds no backtick and still names `amended rev-3`.
  Red when: an answer gains no token its criterion carries, or the 43-spec path lands on 59's line
  37 and flips its form. At `a78d6affc` the first grep prints nothing, and the second prints line
  37, both measured. A backtick on line 37 makes the second print nothing. The leg printed, at
  `70273a468`:
  ```
  HYGIENE check 23 FAILED — a ledger answer shares no backticked token with the criterion it claims to answer, so the two are joined by label alone and may describe different things: TOOL-dSafePassage-59/AC12 TOOL-dSafePassage-77/AC8 TOOL-dSafePassage-82/AC2
  ```
- **AC4** — When `git grep -n -F 'upgrade_walk.py:944' HEAD -- '*/BACKLOG.md'` runs from the
  repository root at the build commit, it prints nothing and exits 1. The ask row
  TOOL-dSafePassage-79 still cites `tools/govkit/upgrade_walk.py`.
  Red when: the locator stays inside the backticks. At `a78d6affc` the grep prints line 7 of the
  build's `BACKLOG.md`, measured, and the leg printed, at `70273a468`:
  ```
  HYGIENE check 15 rule 1: memory/builds/dSafePassage/BACKLOG.md:7 cites tools/govkit/upgrade_walk.py:944, which resolves to nothing and has no row in memory/project/corpus-path-unresolved.txt
  ```
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs from the repository root of a
  clean tree at the build commit, it exits 0. No line it prints holds `HYGIENE check 12 FAILED`,
  `HYGIENE check 15` or `HYGIENE check 23 FAILED`.
  Red when: any of S1 to S4 is missing. At `70273a468` the leg printed the five lines quoted under
  AC1 to AC4, and exited 1.
  cost: about five minutes. TOOL-dSafePassage-83's §4 measured 279 s alone at `83817478f`.
  permission: scratch-guard row G1 refuses this argv to a role whose allowlist does not name
  `memory hygiene`.
- **AC6** — When
  `git grep -n -F -e 'done <<<"$out25"' -e 'done <<<"$out35"' -e 'done <<<"$out"' HEAD -- '*.sh'`
  runs from the repository root at the build commit, it prints exactly one line, in the unattended
  driver, a site its own registry row declares.
  Red when: a loop keeps its here-string. At `a78d6affc` it prints four lines, measured: the lander
  suite's lines 917 and 1377, the resolver suite's line 265 and the unattended driver's line 4016.
- **AC7** — When
  `python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt` runs from the
  repository root, it exits 0, and its last line is
  `sh-hygiene: OK — 58 declared site(s) in 43 row(s), no undeclared loop fed by a command substitution`.
  Red when: either suite keeps a here-string loop over a captured value. At `70273a468` the leg
  printed:
  ```
  sh-hygiene: 2 finding(s). A `while … done` fed by a heredoc or here-string whose body holds a command substitution reads until EOF, and EOF can never arrive.
    tools/lib/resolve-python.test.sh: the registry declares 1 site(s) at `<<<` and the scan measures 2 — the count may fall with the sites and may not rise
    tools/push-main.test.sh: a loop is fed by `<<<` holding a command substitution, and no registry row declares it (2 site(s)) — feed the loop from a scratch FILE instead
  ```
  figure: 58 and 43 are DERIVED from the registry at observation time, and the registry does not
  change. Read at `70273a468`, it holds 43 rows whose counts sum to 58.
  permission: scratch-guard row G1 refuses this argv to a role whose allowlist does not name the
  leg.
- **AC8** — When arm 35's lines, from `out35=$(` to the `esac` that closes its verdict, are cut from
  the lander suite and run in a scratch bash, it prints exactly one line: two spaces, then
  `ok   — 35 no deployer beside the lander is one skip line and exit 0; a deployer with no python refuses`.
  When arm 25's feed, from the `printf` line above its loop to the loop's `done` line, is cut and
  run in a scratch bash with `out25` set to one line holding
  `steps were NOT run on gov first — no govkit deployer beside this lander`, followed by
  `echo "f25=$f25"`, it prints `f25=1`.
  Red when: either scratch file is not written before its loop. For arm 35, bash names the missing
  file, the count stays 0, and the run prints two spaces, then
  `FAIL — 35 the skip line was printed 0 time(s) over two absent-deployer runs:`, followed by the
  captured output. That was measured on a cut copy carrying S5's feed with its `printf` line removed,
  on 2026-11-01. For arm 25, bash names the missing `out25.txt` and the run prints `f25=0`. That is
  derived from the loop's text and not measured.
  fixture: each scratch bash sets `tmp` to a scratch directory. Arm 35's also sets `lander` to the
  lander beside the suite, and defines `ok` and `bad` as the suite does at lines 185-186. The tree
  holds every input today.
- **AC9** — When the resolver suite's floor-statement block, from the `out=` line that runs the
  floor check with `--rev 3708a705` to the `bad` line after it, is cut and run in a scratch bash, it
  prints no `FAIL` line and counts `n1c=7`.
  Red when: the scratch file is not written before the loop. Then the run prints
  `FAIL python_floor.py check --rev 3708a705 did not print the seven pinned statements:` with the
  captured output, and counts 0. Measured on a cut copy carrying S5's feed with its `printf` line
  removed, on 2026-11-01.
  fixture: the scratch bash sets `ROOT`, `HERE`, `PFX`, `REALPY` and `TMP` as the suite does at its
  lines 13 to 44, and `ok` and `bad` as at lines 35 and 36.
  figure: 7 is PINNED by the suite's own assertion.
- **AC10** — When
  `git grep -n -F -e 'root92 / "govkit"' -e 'for pre in ("tools"' -e 'for f in ("govkit' -e 'pre / "govkit"' -e '{pfx}/policy/' HEAD -- '*.py'`
  runs from the repository root at the build commit, it prints nothing and exits 1.
  Red when: any of the five spellings stays. At `a78d6affc` it prints exactly five lines,
  selftest.py's line 4572 and upgrade_walk.py's lines 1086, 1088, 1091 and 1111, measured.
- **AC11** — When `bash tools/check-install-prefix.sh` runs from the repository root at the build
  commit, no hit line it prints names the govkit selftest or the upgrade walk. Its hit lines are the
  three `tools/run-gates/ceiling-evidence.txt` lines, and its last line ends
  `3 kit-path spelling(s) on 3 line(s)`.
  Red when: any of S6's sites keeps its literal. At `70273a468` the leg printed, among its lines:
  ```
  tools/govkit/selftest.py:4572  govkit  stub92 = root92 / "govkit"
  tools/govkit/upgrade_walk.py:1086  (loose)  for pre in ("tools", "scripts", ""):
  tools/govkit/upgrade_walk.py:1088  govkit  for f in ("govkit/registry.toml", "govkit/govkit.py"):
  tools/govkit/upgrade_walk.py:1091  govkit  got, want = derive_release_engine(c), c / pre / "govkit" / "govkit.py"
  tools/govkit/upgrade_walk.py:1111  policy  t = build_repo("plant-root-target", {f"{pfx}/policy/adopt-policy.sh": ""})
  install-prefix: RED — 450 tracked file(s) graded, 7 render(s) left out as matching their template, 9 kit-path spelling(s) on 8 line(s)
  ```
  figure: 3 on 3 is DERIVED from the log's 9 on 8, less S6's 6 spellings on 5 lines.
  permission: scratch-guard row G1 refuses this argv to a role whose allowlist does not name the
  leg.
- **AC12** — When `python -B tools/govkit/upgrade_walk.py --list` runs from the repository root, it
  exits 0 and prints `upgrade-walk: grader · release-engine · ok` and
  `upgrade-walk: grader · plant-root · ok`.
  Red when: a derived name differs from the one the grader's own reader resolves. A `want` spelled
  under a kit name the pin tree does not hold prints
  `upgrade-walk: grader · release-engine · RED · a pin at`, then the prefix and the two paths. A
  plant under a directory `resolve_kit_dir` does not probe prints
  `upgrade-walk: grader · plant-root · RED · the policy adopter read LookupError:`. A gov policy kit
  that does not resolve from the walk's own directory prints
  `upgrade-walk: grader · plant-root · RED · it raised LookupError: no policy kit holding adopt-policy.sh in this install`,
  which AC17 stages. All three are derived from upgrade_walk.py lines 1092-1093, 1116-1142 and 1154,
  and not measured, because no build exists yet.
  cost: about 49 s, as TOOL-dSafePassage-77's ledger measured for the same command.
- **AC13** — When
  `python -B -c "import pathlib, tempfile, selftest as s; s.check_floor_bash(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`
  runs with the govkit kit directory as its working directory, every `[dSP-92]` line it prints reads
  `ok`, and its last line is `[]`.
  Red when: the stub directory is not named as the kit directory. Then `derive_tool_root` over
  `root92` finds no tool root, because it looks for the engine directory's own name holding the
  registry (`tools/govkit/govkit.py` lines 190-210). Which `[dSP-92]` lines then read FAIL is
  UNVERIFIED.
  cost: about 3 s, as TOOL-dSafePassage-95's AC1 measured.
  fixture: a node whose `PATH` holds a bash, as `[dSP-87 AC5]` already needs.
  permission: scratch-guard row G3 refuses this command to a role whose allowlist does not name
  `govkit selftest`. TOOL-dSafePassage-99's AC1 measured that for `gov-spec-writer`.
- **AC14** — When three commands run from the repository root at the build commit, each prints one
  line, the first line of the answer it names.
  `git grep -n -P '^- AC2 — \x60python [^\x60]*derive-ceilings[^\x60]* --check\x60(?!.*owed)(?=.*not observed in 80.s own pass)(?=.*exited \d)(?=.*OUTSIDE the runner)(?=.*at \x60[0-9a-f]{9,}\x60)' HEAD -- '*build-TOOL-dSafePassage-80-ledger.md'`
  prints 80's AC2 line.
  `git grep -n -P '^- AC4 — (?=.*\x60os\.utime\x60)(?=.*not recorded)(?=.*memo guard)' HEAD -- '*build-TOOL-dSafePassage-95-ledger.md'`
  prints 95's AC4 line.
  `git grep -n -P '^- AC4 — (?=.*\x60finally\x60)(?=.*not recorded)(?=.*every other line)' HEAD -- '*build-TOOL-dSafePassage-96-ledger.md'`
  prints 96's AC4 line.
  Red when: a line takes its legal form and drops a clause §4 "The seven lines" requires, such as
  an 80/AC2 line that opens with the checker's command and still says `owed`. At `a78d6affc` each
  of the three prints nothing and exits 1, because the three lines read `owed`, measured. A line
  whose run printed something AC2 of 80 does not expect holds no `OUTSIDE the runner`, and the
  first command reds on it.
  fixture: a `git` built with PCRE, as for AC2.
- **AC15** — When the build commit's tool root is copied into a scratch tree by `git archive`, with
  `git init` run at that tree's root and the govkit kit directory renamed `gk2`, two runs from inside
  `gk2` read ok. `python -B upgrade_walk.py --list` prints
  `upgrade-walk: grader · release-engine · ok`. The AC13 command, run there, prints every `[dSP-92]`
  line as `ok`.
  Red when: a kit name is still spelled, as a literal or as a variable holding one. The same two
  runs over a copy of `70273a468` built the same way must not read ok. Its release-engine pins sit
  under `govkit` while `derive_release_engine` resolves `gk2` (upgrade_walk.py line 206), so
  `derive_tool_root` finds no candidate and raises `Refusal` (govkit.py lines 206-210). Its stub is
  named `govkit` while `derive_tool_root` looks for `gk2`. That outcome is derived and not measured.
  If the `70273a468` copy reads ok, the probe cannot move, and AC15 is red. If either copy fails
  before printing the line AC15 reads, the probe has not run, and the ledger says so rather than
  recording a red.
  fixture: the copy needs a `.git` at its root, because the selftest finds `GOV_ROOT` by walking up
  for one (selftest.py line 71), and it needs every sibling kit, which the suite requires at import.
  The tree holds every input today, and the copy is a write this role may not make. The build makes
  it.
  cost: about 49 s for the walk, as AC12, and about 3 s for the selftest call, as AC13. Neither was
  measured in a copy.
  permission: scratch-guard row G3 refuses the selftest half to a role whose allowlist does not
  name `govkit selftest`.
- **AC16** — When
  `git grep -h -o -F -e 'stub92 = root92 / HERE.name' -e 'gkn = gk.GOVKIT_DIR.name' -e 'c / pre / gkn / ' -e 'gk.resolve_kit_dir("policy", "adopt-policy.sh", HERE).name' -e '{pfx}/{poln}/adopt-policy.sh' -e 'except (Stop, OSError, LookupError, ValueError, RuntimeError)' HEAD -- '*.py' | sort -u`
  runs from the repository root at the build commit, it prints exactly six lines, one per pattern.
  Red when: an after-line spells a kit name through a variable that holds a literal, or the loop's
  tuple is not widened. At `a78d6affc` it prints nothing, measured. This is the static half of
  AC15, and the only criterion that reads the policy kit name's spelling.
- **AC17** — When the build commit's tool root is copied into a scratch tree by `git archive`, with
  `git init` run at that tree's root and the policy kit directory removed, `python -B upgrade_walk.py
  --list` run from inside the copy's govkit directory prints
  `upgrade-walk: grader · plant-root · RED · it raised LookupError: no policy kit holding adopt-policy.sh in this install`
  and then `upgrade-walk: RED: a grader of this leg reads wrong, so nothing it would measure is trusted`.
  It exits 1 and prints no `Traceback`.
  Red when: the new `resolve_kit_dir` call sits outside every handler. Then the run ends in a
  `Traceback` whose last line names the `LookupError`, prints no plant-root line and no RED summary,
  and exits 1. Derived from upgrade_walk.py lines 1109-1158 and govkit.py lines 269-270, and not
  measured. If the copy fails before the plant-root line for another reason, such as an import that
  needs the policy kit, the probe has not run, and the ledger says so.
  fixture: as AC15's. The build makes the copy.
  cost: about 49 s, as AC12.

## 7. Gates

`memory hygiene` · `shell hygiene (a loop fed by a command substitution)` · `install-prefix (shipped surface)` · `govkit selftest` · `policy fixtures` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `recall floor` · `upgrade-walk` · `python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `spec tokens (a spec's own names resolve)`

New arm: tools/push-main.test.sh · covers AC8 · arms 25 and 35 count their lines from a scratch file; one staged red per arm. Cutting the `printf` line above arm 35's loop prints `FAIL — 35 the skip line was printed 0 time(s)`, measured on a cut copy. Cutting the `printf` line above arm 25's loop prints `FAIL — 25 lexicon-skip=1 govkit-skip=1 dead-or-refused=0 gov-first-skip-lines=0`, derived and not measured; arm 25 runs on node a, where both its kits sit beside the lander · none

New arm: tools/lib/resolve-python.test.sh · covers AC9 · the floor check's seven pinned statements are counted from a scratch file; staged red by cutting the `printf` line, which prints `FAIL python_floor.py check --rev 3708a705 did not print the seven pinned statements`, measured on a cut copy · none

New arm: tools/govkit/upgrade_walk.py · covers AC12 · the release-engine and plant-root graders over derived names; staged red by spelling `want` under a kit name other than `gkn`, run with the kit's `__pycache__` removed first and matched to the `grader · release-engine · RED` line, never to the exit status alone, derived and not measured · none

New arm: tools/govkit/selftest.py · covers AC13 · the `[dSP-92]` checks over a stub named by `HERE.name`; staged red by naming the stub other than the kit directory, run under `python -B` with the kit's `__pycache__` removed first and matched to a `[dSP-92]` FAIL line, never to the exit status alone, derived and not measured · none

The first three legs are the ones that red at `70273a468`. The next six are the non-broad legs
that the paths of §4's estimate trip, printed by
`python tools/check-spec-tokens.py --legs-for` over those paths on 2026-11-01. The two suites trip
only broad guards. `upgrade-walk` carries no guard, and it runs both graders S6 changes. The resolver
leg, the lander suite's leg and the three-prefix leg run S5's arms. `spec tokens (a spec's own names
resolve)` grades this spec, and `memory hygiene` also grades the ledgers. The staged reds on the two
govkit files clear the cache because Python's cache check reads a whole-second mtime and the size, so
a same-length edit made within one second can run the previous bytecode
(`memory/gotchas/staged-break-runs-stale-bytecode.md`).

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-101-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-101-spec-brief.md`.
  The brief's finding: the close's merge bar at `70273a468` ran 1237 s and exited 1, red on 4 of 75
  legs. The spawn budget, and the three `ceiling-evidence.txt` lines of install-prefix, are the ask
  TOOL-dSafePassage-85's owner rows and out of scope. The other three legs are this build's own,
  adopted under UNATTENDED-PROTOCOL §11 as a measured red. Items: id 1 is S1, id 2 is S2 and S3,
  id 3 is S5 and id 4 is S6. S4 is not in the brief: the memory hygiene leg also reds on check 15
  rule 1 at `memory/builds/dSafePassage/BACKLOG.md` line 7, and the leg cannot go green without it.
  The brief's id 1 asks for a rev bump on 99. S1 assigns it to a gov-spec-writer pass committed
  before this unit's build, because scratch-guard gates the spec class by role, as
  TOOL-dSafePassage-83's S1 did. The write sets split into two disjoint halves, which §4 "Write sets"
  records. This unit stays one, by the brief's default. Every cited line was read at `70273a468`.
- rev-2 · 2026-11-01 · §2 · §3 · §4 · §5 · §7 · §10 · S1 · S2 · S3 · S5 · S6 · AC1 · AC2 · AC3 ·
  AC4 · AC6 · AC8 · AC10 · AC12 · AC13 · AC14 · AC15 · AC16 · AC17 · folded the round-1 spec audit
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-101-spec-audit-round1.md`
  (CLEAN WITH FIXES, 6 medium and 7 low) under the brief
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-101-audit-fold-brief.md`,
  every item at the fix its skeptic judged sound. M1 and L1: 59/AC12's path goes on a new
  continuation line 38, its line 37 unchanged and AMENDED for both readers, with the resulting text
  quoted, and AC3 gains a probe that line 37 holds no backtick. M2: AC14 reads the required clauses
  of the 80/AC2, 95/AC4 and 96/AC4 lines. M3: AC15 runs the graders and the `[dSP-92]` checks from a
  copy with the govkit directory renamed, and AC16 reads the after-lines' spelling. M4: the grader
  loop's tuple at upgrade_walk.py:1154 widens to catch `LookupError` and `RuntimeError`, §5 states
  it, AC12 names the red line, and AC17 stages a missing policy kit. M5: "The edge ruling" answers
  TOOL-dSafePassage-83's three reasons by name, and TOOL-dSafePassage-70 is no longer cited as a
  precedent, here or in §10. M6: AC1 observes 99's rev-3 header, its §9 rev-3 line and the Edges
  block's `none` at `a78d6affc`, with the skeptic's Edges-scoped check written as a pathspec
  `git grep`. L2: the 80/AC2 provenance is restated as measured, one `reads` line changed in the
  manifest and 148 ceilings read. L3: AC2 uses check 23's own predicate. L4: AC8 cuts arm 25's feed,
  the lander's `New arm:` line names arm 25's staged red, and AC8 quotes the suite's two leading
  spaces. L5: the plant-root grader's kit name is `poln`, and the Inventory names each function's
  existing bindings. L6: AC12 and AC13 run under `python -B`, and the two govkit `New arm:` lines
  clear the cache and match a named line. L7: AC1 greps `a78d6affc`, the other grep criteria grep
  `HEAD` at the build commit, and §3 Edges is reworded. Every newly cited line was read at
  `a78d6affc`, where nothing under the tool root, no ledger and no `BACKLOG.md` differs from
  `70273a468`.

## 10. Reuse audit

The seams are the remedies each leg names, applied with idioms that already sit in the files. For
`tools/govkit/`: `HERE.name` as `build_staged_copy` spells it (selftest.py:3658), `GOVKIT_DIR.name`
(upgrade_walk.py:1097), `gk.derive_tool_root(gk.repo_root())` (upgrade_walk.py:143),
`resolve_kit_dir` as `derive_policy_adopter` calls it (upgrade_walk.py:213), and the grader loop's
own handler (upgrade_walk.py:1154), widened rather than duplicated inside a grader. For
`tools/lib/`: the resolver suite's own `$TMP` (resolve-python.test.sh:33). The lander suite reuses
its own `$tmp` (push-main.test.sh:177). `tools/push-main.sh` is not touched. For the records, the
seams are TOOL-dSafePassage-83's S2 and S3, which gave check 23's lines their legal forms in this
build, and the `none` Edges body that `memory/TEMPLATE-SPEC.md` §3 admits.
`python tools/codebase-map/reuse_lookup.py "feed a shell loop from a scratch file instead of a here-string over a command substitution, and derive a kit directory name from the file's own location"`
ranked `resolve_kit_dir` first as a SEAM, with fan-in 44 and 103 installs, and `derive_tool_root` as
a SEAM with fan-in 8. S6 calls both, so no new helper is added. The shell remedy has no helper to
reuse: it is two lines of builtin shell. The recall probe ranked TOOL-dSafePassage-82 first, the
unit that cleared six lint legs in one unit. It also ranked TOOL-aBriskPreflight-2, which records
that "a loop fed by a FILE redirect is its own named remedy", and TOOL-dRedressedBar-27, which put
37 ledger lines in a legal form.

Recall terms used: `python tools/memory-recall/query.py "how is a bar leg this build turned red cleared by its own named remedy, a ledger line given its legal form and a loop fed from a scratch file" --terms "ledger OBSERVED AMENDED check 23 consumes-from hands-off reciprocity scratch FILE here-string install-prefix resolve_kit_dir derive_tool_root"`
