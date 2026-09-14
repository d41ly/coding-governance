# TOOL-aProbedUnit-3 — `--audit <slug>`, the dispatched-unit stall probe, and the keepalive that runs it

**Status:** CLOSED · rev-4 · 2026-09-14 · node a · Tier-2 · base 1b000d1a · streams tooling · order 3 · ratified 2026-09-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-aProbedUnit-3-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-aProbedUnit-3-1-acceptance-ledger.md) | journal | — |
| [2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md) | journal | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |
| [2026-09-14-prompt-TOOL-aProbedUnit-3-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-3-1-build-brief.md) | journal | — |
| [2026-09-14-review-TOOL-aProbedUnit-1-diff-review-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-diff-review-round1.md) | diff-review | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round2.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round2.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing observes a live unit from outside: the keepalive fires every ten minutes while a `Workflow`
runs in the background and does nothing with the turn. `tools/unattended/unattended.sh` gains a
read-only verb, `--audit <slug>`, that prints one line per dispatched-and-open unit with how long the
tree has been idle and a `PROGRESSING` or `STALLED` verdict against a declared `UNIT_STALL_BOUND`,
and the unattended Skill makes that verb the keepalive's prompt, so the turn that already fires has
something to do with itself.

## 2. Scope (IN)

- **S1** — `--audit` joins `VERBS_SLUG`, the header's invocation lines, and the dispatch `case` of
  `tools/unattended/unattended.sh`, with a `verb`-carrier entry in `tools/unattended/VERBS.template.md`
  and an invocation in `tools/unattended/SKILL.template.md`, which is what check 26 of the kit gate
  joins. Observed by AC1 and AC6.
- **S2** — For every unit whose LATEST `dispatch · item <grp> <id> · reason …` row in the run-state
  file is still OPEN, the verb prints exactly one line of the shape in section 4, and the openness
  predicate is the one `verb_dispatch` already applies to its sibling set — `pass_commit` from the
  kit library plus the declared-set overlap — hoisted into one function both call rather than
  copied. Observed by AC1, AC2 and AC3.
- **S3** — `STALLED` when BOTH the newest write in the tree and the newest commit are older than
  `UNIT_STALL_BOUND` seconds; `PROGRESSING` otherwise; a clean tree has no newest write and reads as
  older than any bound. A listed path deleted from disk is skipped, not a dead probe. A `STALLED`
  line is followed by one remedy line. Observed by AC1, AC2 and AC8.
- **S4** — `UNIT_STALL_BOUND` is read through `read_bound_key`, the `GATE_BOUND` conf read hoisted
  into a function this unit owns, with the same three outcomes: absent takes the kit default of 1800
  and says so on stderr, a non-integer or zero is a refusal at exit 2, a positive integer is the
  bound. It is declared in `.unattended.conf` and `tools/unattended/.unattended.conf.example` with
  the reason beside it, documented in `tools/unattended/PROTOCOL.template.md` section 8's key table,
  and listed in `tools/unattended/kit.toml` `optional_keys`. Observed by AC4 and AC6.
- **S5** — Three refusals under check 51, each a `fail` branch with an arm in
  `tools/unattended/unattended.test.sh`: no run-state file; a terminal record; a node whose clock or
  mtime probe cannot answer. With no open dispatched unit the verb prints one line and exits 0. The
  suite's own assertion floors rise by the arms this unit adds. Observed by AC3, AC5 and AC9.
- **S6** — The Skill's keepalive section names the prompt the agent schedules — the audit verb, once
  the run has a slug — and what the main session does with each verdict; the Skill's render
  `.claude/skills/unattended/SKILL.md`, the protocol's and the verb carrier's renders under
  `memory/guides/` are re-made in the same commit. Observed by AC6.
- **S7** — The `.unattended.conf` edit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`
  in the same commit with a delta line in the subject, because that file is on the manifest's
  `watch` line. The dossier `memory/map/features/unattended.md` names the verb in its keepalive
  paragraph without growing past its cap. Observed by AC7.

## 3. Non-goals (OUT)

- **What the verb does not know, stated in its own header.** It cannot see what the unit is doing,
  whether a process is stuck, or which command it is sitting on. Its three figures are properties of
  the TREE — with two open units in one worktree, `last-write` and `last-commit` are the same two
  numbers on both lines and only `elapsed` differs. A dispatched unit whose declared write set
  names a path the tree never wrote is not a verdict here; check 23 of `tools/unattended/check-unattended.sh`
  grades declarations against commits, after the fact.
- **No process-side probe, no pointer to one.** The brief asked for a pointer line naming
  `tools/process-monitor/census.py` where it is tracked. Section 8 F1 records why no such line is
  printed: every carrier for it is either a kit literal the charter bans or a second conf key the
  mandate did not price. The Skill's remedy prose names the process-monitor KIT by name, which
  `tools/check-install-prefix.sh` explicitly does not grade, and points nowhere.
- **No stop, no re-dispatch, no park written by the verb.** It reads and prints. The remedy line
  tells the main session what to do; the acts are the session's, through `TaskStop`, `--park` or a
  brief, and nothing here claims an effect a script cannot produce.
- **No per-key bound reader.** `UNIT_STALL_BOUND` is the second instance of the
  defaulted-validated-announced conf read `GATE_BOUND` established at
  `tools/unattended/unattended.sh:305`, and the charter's section 12 extracts at the second instance.
  This unit lands first, so the extraction is this unit's: the block becomes `read_bound_key`
  (section 4, "The bound") with two callers here, and `TOOL-aProbedUnit-6`'s `REVIEW_ROUNDS` is its
  third CALLER, never a third copy. Nothing about that helper is left for unit 6 to decide.
- **No kit version bump, no `ARMS_FLOORS` raise.** The closing pass bumps unattended 1.21 to 1.22
  once. The driver's arms floor in `.memory-tree.conf` reads `104:101` against a measured
  `branches 194 · armed 188` from `python3 tools/memory-tree/check-arms.py --report` on 2026-09-14,
  so three more branches move nothing a floor already ninety slack would catch, and the file is on
  the manifest's watch line. That is the BRANCH floor; the suite's own executed-assertion floors are
  a different pin and do move, AC9.
- **The suite is not run whole inside the pass.** Build-level rule three: the arms are observed by
  running the driver over the fixture directly, and `tools/unattended/unattended.test.sh` runs at
  the close under `bash tools/unattended/run-unattended-gates.sh` on a frozen clone.

### Edges

- **consumes-from** external — `pass_commit` in `tools/unattended/lib-unattended.sh:164` and the
  overlap test at `tools/unattended/unattended.sh:4802` to `:4815`, which together are what
  "open" means to `--dispatch`. If either changed what a pass commit is, the audit's population
  would change with it, which is the point of sharing them rather than a defect.
- **hands-off** `TOOL-aProbedUnit-6` — one call, `read_bound_key REVIEW_ROUNDS <default> rounds
  <note>`, placed after this unit's two calls; the helper, its signature and its two sentences are
  decided in section 4, "The bound", and unit 6 writes no reader of its own. Unit 6 also edits the
  same section 8 table, the same `optional_keys` list and the same two conf files, after this
  unit; it adds its rows beside these and moves none of them. The suite's fixture is one more
  shared slot: this unit takes the SIXTH positional of `mkconf` for `UNIT_STALL_BOUND` (section 4,
  "The fixture"), so unit 6 takes the SEVENTH for `REVIEW_ROUNDS`, and neither renumbers the
  other's.
- **hands-off** external — the kit version bump across every carrier
  `bash tools/check-kit-versions.sh` names, the closing pass's, once.

## 4. Design

### The verb, in the driver

`--audit` is a slug verb: it joins `VERBS_SLUG` at `tools/unattended/unattended.sh:87`, gains the
header line `#   unattended.sh --audit <slug>` after the `--status` line at `:8` so `usage()` at
`:108` renders it, and a `--audit) print_audit "$SLUG" ;;` arm in the dispatch `case` at `:5042`.
The function is named `print_audit` and not `verb_audit`: `.lexicon.conf` pins the verb-offender
count as a two-sided equality at 984 and `verb` is in no declared row, so the file's own `verb_*`
convention costs a pin re-paste that is read off the lexicon leg — a leg this pass may not run.
`print` is the declared verb for "write to stdout for a human", which is all this function does.
`python tools/lexicon/lexicon.py --suggest print_audit --as sh.function` answers OK.

The body, in order:

1. `check_slug`, then `rel=$(runmd_of "$slug")`. No file: `fail 51`, the first branch. A phase
   `is_terminal` reports true for: `fail 51`, the second branch, its own sentence — a finished run
   has no unit that can be dispatched and open, and a keepalive still firing over it should have
   been reaped. Neither reuses `refuse_if_terminal` at `:1610`: its message says the verb "would
   rewrite" the record, and this verb rewrites nothing, so the sentence would be false.
2. The latest PASS per unit, by the `awk` shape `verb_status` already uses for brief rows
   at `:2865` to `:2867`: split on ` · `, keep rows whose first field ends ` dispatch`, take the
   `item` field as `<grp> <unit>` and the `reason` field as the declared set, and UNION every row
   at the unit's newest anchor, a new anchor replacing — check 23's `(anchor, unit)` key
   (rev-4; rev-3 kept the LAST row seen per unit, `last[u]`, which asked whether the pass wrote
   its last path and graded a finished unit open). The row is written by `park()` at `:3911` with
   `date -u +%Y-%m-%dT%H:%M:%SZ` as its first token, and the first row's ISO at that anchor is
   what `elapsed` is measured from. Before the openness test, a unit whose spec status is
   terminal (`CLOSED`/`WONTDO`) is dropped, the status resolved the way `--plan` resolves it —
   `load_spec_facts` over the tracked spec set, `SPEC_PATH` then `SPEC_ST` — so `--plan` and
   `--audit` cannot grade one unit DONE and STALLED.
3. Openness, through `check_pass_open <grp> <unit> <rel> <declared>`, a new function that is the
   body of `verb_dispatch`'s sibling loop at `:4802` to `:4815` moved verbatim: `pass_commit`
   answers which commit named the unit after the anchor, and the pass is closed only when that
   commit also wrote inside the declared set through `overlaps`. `verb_dispatch` calls the function
   where the block was, so `--dispatch` and `--audit` cannot disagree about whether a pass is open;
   `check` is the declared verb for "assert a predicate and return a verdict".
4. The tree's two clocks, once, before the per-unit loop. `last-commit` is `GIT log -1 --format=%ct`.
   `last-write` is the newest `stat -c %Y` over the dirty-and-untracked set, which is
   `check_clean`'s own listing at `:1077` to `:1079` — refresh the index, then `diff`, `diff
   --cached` and `ls-files --others --exclude-standard` — hoisted into `scan_dirty_paths` so that
   `check_clean` counts its lines and this verb reads them; `scan` is the declared verb for "walk a
   population looking for matches". The listing is the seam rather than `git status --porcelain`
   because `check_clean`'s comment records why porcelain alone is wrong on a linked worktree. A
   listed path that no longer exists — a deletion — has no mtime and is skipped. An empty set, or a
   set with nothing left after skipping, gives `last-write none`.
5. Liveness. `date -u -d "$iso" +%s` on the row's timestamp, `stat -c %Y` on an existing listed
   path, or `GIT log -1 --format=%ct` answering nothing is the third `fail 51` branch: the audit
   cannot measure idle time on this node, so both verdicts are unanswerable, and the message names
   which probe died. A zero from a dead probe would read as "written just now", which is
   `PROGRESSING` forever, and is the reassuring-zero class the charter's section 7 refuses.
6. Per open unit, one line:

   ```
   unattended-audit: <id> · dispatched <ISO> · elapsed <s>s · last-write <s>s ago|none · last-commit <s>s ago · PROGRESSING|STALLED
   ```

   `STALLED` when `now - last-commit > UNIT_STALL_BOUND` AND (`last-write` is `none` OR `now -
   last-write > UNIT_STALL_BOUND`). Every other combination is `PROGRESSING`. After a `STALLED`
   line, one more:

   ```
   unattended-audit: remedy — stop the unit's task, then re-dispatch <id> with a brief naming what stalled and that it is skipped
   ```

   No open unit: `unattended-audit: no unit is dispatched and open`. Every verdict exits 0; only
   the three refusals exit 1. The verb writes nothing and stages nothing.

The header comment carries the three figures' tree-scope and the non-goals' first bullet verbatim
in spirit: what the verb does not check is said where the verb is read.

### The bound

Read where `GATE_BOUND` is, through one function this unit hoists from the `case` at `:305` to
`:311`: `read_bound_key <NAME> <DEFAULT> <UNIT> <NOTE>`. Its three arms are that block's bytes with
the key name lifted out. Blank writes `<DEFAULT>` into `<NAME>` by `printf -v` and prints
`unattended: NOTE - this project declares no <NAME>, so <NOTE>. Declare one in $CONF to change it.`
on stderr; `*[!0-9]*|0` prints `unattended: REFUSING - <NAME> is declared as '<value>', which is
not a positive integer of <UNIT>. A bound that cannot be parsed is a bound nobody set, and 0 means
no bound at all.` and exits 2; a positive integer stands. Two calls replace the block, `GATE_BOUND`
first with `seconds` and its present note, so the sentences the suite already asserts at
`tools/unattended/unattended.test.sh:5197`, `:5201` and `:5219` are the same bytes after the hoist;
then `UNIT_STALL_BOUND` with `seconds` and the note `a dispatched unit reads STALLED after the kit
default of 1800s with no write and no commit`. `<UNIT>` is an argument because the third caller
counts rounds, and a refusal that says `seconds` about a round count is a false sentence.

The hoist is the charter's section 12 instance-two rule, taken here because this unit lands before
`TOOL-aProbedUnit-6`, whose `REVIEW_ROUNDS` becomes the third call and not a third `case`. It is
legal under `python3 tools/memory-tree/check-arms.py`: the block refuses with `echo` and `exit 2`
and carries no `fail <n>` branch, so the meta-gate counts nothing inside it before or after the
move. `read` is the declared verb for "pull bytes or records from a named source", and the source
here is the conf; `python tools/lexicon/lexicon.py --suggest read_bound_key --as sh.function`
answers OK.

`UNIT_STALL_BOUND_DEFAULT=1800` sits beside `GATE_BOUND_DEFAULT` at `:213`. `UNIT_STALL_BOUND=""`
joins the initialiser line at `:292`, which is where a conf-sourced key must be seeded under
`set -u`. 1800 is the owner's figure from the build README's rules: three keepalive cadences at
this repo's ten-minute interval, so a verdict is never one missed tick.

### The fixture

`mkconf` at `tools/unattended/unattended.test.sh:108` writes the suite's conf from five positionals,
`${1-true}` to `${5-}`, and every fixture routes through it via `reset_tree`. Leaving it alone is not
neutral: `run` merges stderr, so a conf with no `UNIT_STALL_BOUND` would put the new key's NOTE line
ahead of every verb's output and red any arm that compares a whole line. So `mkconf` gains
`UNIT_STALL_BOUND="${6-1800}"` as its SIXTH positional, on the file's own `${4-3600}` convention,
written after the `GATE_BOUND` line; every existing fixture then declares the key at the kit default
and announces nothing. AC1 and AC4 set the slot explicitly — `mkconf "true" "true" "" "3600" "" "60"`
for the bound AC1 measures against, `"abc"` and `"0"` for AC4's refusals. The one fixture that WANTS
the NOTE is the `NOCONF` heredoc at `:5206` to `:5217`, which omits `GATE_BOUND` by hand and now omits
`UNIT_STALL_BOUND` the same way; its arm gains a second `hit` beside the one at `:5219`, on this
key's NOTE sentence. `TOOL-aProbedUnit-6` takes the SEVENTH positional for `REVIEW_ROUNDS`, after
this one lands (section 3, Edges).

### The carriers

| Carrier | Edit |
|---|---|
| `tools/unattended/VERBS.template.md` | one `- `--audit` — ` bullet in the verb list, after `--status` |
| `tools/unattended/SKILL.template.md` keepalive section, `:19` to `:46` | the scheduled prompt is `bash {{KIT_DIR}}/unattended.sh --audit <slug>`; before `--preflight` no slug exists, so the prompt reads "once the run has a slug, run …"; on `STALLED` the main session stops the unit's task, records a `--park` or a brief note, and re-dispatches that unit with a brief naming the stalled command as skipped — `re-dispatch` is the phrase AC6 pins, and the Skill carries it nowhere else at base; on `PROGRESSING` it does nothing |
| `tools/unattended/SKILL.template.md` | the `--audit` invocation line check 26 requires, in the "Check yourself" bullet at `:594` beside `--status` |
| `tools/unattended/PROTOCOL.template.md` section 8 | one table row for `UNIT_STALL_BOUND`, OPTIONAL, on `GATE_BOUND`'s pattern |
| `tools/unattended/kit.toml` | `UNIT_STALL_BOUND` appended to `optional_keys` at `:92` |
| `.unattended.conf` and `tools/unattended/.unattended.conf.example` | `UNIT_STALL_BOUND="1800"` with the reason beside it, after `GATE_BOUND` |
| `memory/map/features/unattended.md` | the keepalive paragraph at `:90` names `--audit` as what the keepalive runs, within the cap |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamped |
| `tools/unattended/unattended.test.sh` | `mkconf` at `:108` gains `UNIT_STALL_BOUND="${6-1800}"` as its sixth positional; the `NOCONF` arm gains a second `hit` beside `:5219` on this key's NOTE; the section 6 arms sit in region two beside the `--dispatch` arms |

The driver spells the token `{{KIT_DIR}}` for itself throughout the Skill, at `:175`, `:546` and
`:594`; the brief's `{{TOOL_ROOT}}` is the token the Skill uses for the workflow scripts at `:558`
and `:560`, and the keepalive prompt follows the driver's spelling.

### Inventory

Four shell functions minted, each leading with a declared verb: `print_audit`, and three hoists of
bytes the driver already runs, `check_pass_open`, `scan_dirty_paths` and `read_bound_key`. One conf
key, `UNIT_STALL_BOUND`, and one constant, `UNIT_STALL_BOUND_DEFAULT`. One check number, 51, with
three branches. One verb, `--audit`. No gate leg, no kit, no workflow script, no guide, so no
codebase-map inventory key moves.

### Files touched (estimate)

- `tools/unattended/unattended.sh` — the verb, three hoisted helpers, the two bound calls, the
  header line, the dispatch arm. About a hundred lines, forty of them comment.
- `tools/unattended/unattended.test.sh` — `mkconf`'s sixth positional, the second `hit` in the
  `NOCONF` arm, and the arms in section 6, beside the `--dispatch` arms.
- `tools/unattended/SKILL.template.md`, `VERBS.template.md`, `PROTOCOL.template.md`, `kit.toml`,
  `.unattended.conf.example`, and the three renders under `memory/guides/` and `.claude/skills/unattended/`.
- `.unattended.conf`, `memory/guides/SESSION-KICKOFF.md`, `memory/map/features/unattended.md`.

### Alternatives rejected

- **`verb_audit`.** The file's convention, and a lexicon pin re-paste this pass cannot read off.
- **`refuse_if_terminal` for the terminal case.** Its sentence describes a rewriting verb.
- **`git status --porcelain` for the write set.** `check_clean` records the stale-stat-cache case it
  misreads on a linked worktree; sharing its listing costs one hoist and no second answer.
- **A copy of the openness test.** Two definitions of "open" between `--dispatch` and `--audit` is
  the two-answers class; the hoist is the same bytes with a name.
- **A second inline `case` for `UNIT_STALL_BOUND`, leaving the hoist to unit 6.** The decision was
  delegated in rev-1 and taken nowhere, so the third copy would have landed with no recorded
  reason. The unit that lands first owns the extraction; the one that lands last owns a call.
- **Exit 1 on `STALLED`.** A verdict is not a refusal, and the keepalive reads the token, not the
  status; a non-zero exit would make a stalled unit look like a broken verb to any shell caller.

## 5. Production-readiness checklist

- security — read-only; the verb writes no row and stages nothing, so a keepalive firing it every
  ten minutes leaves no record behind. A forged dispatch row can only make the audit report a unit
  the run itself declared, which is the trust level every reader of that file already has.
- perf / scale — one `pass_commit` walk per latest dispatch row, one `stat` per dirty path, one
  `git log`. Per keepalive tick, seconds; the same order as `--status`.
- error / empty / loading states — no open unit is one line and exit 0; a clean tree is `last-write
  none`; a deleted-but-listed path is skipped; a dead clock or mtime probe is a named refusal.
- observability — every verdict line carries the three figures it was decided from, so a reader
  can re-derive the token; the defaulted bound announces itself on stderr.
- risks — `stat -c` and `date -d` are GNU spellings, live on every registered node and on this one
  measured 2026-09-14; a BSD node hits the liveness refusal rather than a wrong verdict.
  `check_pass_open`, `scan_dirty_paths` and `read_bound_key` move bytes `--dispatch`, `--preflight`
  and every verb's conf read depend on; each move is verbatim and the existing `--dispatch`
  collision arms, `check_clean` arms and `GATE_BOUND` sentence arms stand.
- testing — section 6; every arm observes the driver over a fixture, never the suite whole. The
  one criterion that IS a suite run, AC9, is the close's.
- migration — N/A. No record shape changes; an existing run-state file audits as it is.
- user docs — the verb carrier, the protocol's key table and the Skill are the docs, all edited
  here and byte-compared to their renders by the kit gate.

## 6. Acceptance criteria

The suite that carries the arms is on no bar leg — `tools/unattended/kit.toml` records the 2026-08-23
ruling — and build-level rule three keeps it out of the pass. So each criterion below is observed by
running the driver over a fixture in a scratch clone, exactly as the arm does, and the arms exist so
`harness arms (fail branches armed or pinned)` counts them at the close. AC9 is the exception the
build's own rule names: its observation is the suite, so the pass observes the grep half and the
suite half is `--close`'s, and its ledger row reads `observed at --close`. The fixture is the suite's
`tRun` build: `reset_tree`, `run --preflight tRun --keepalive-id k1`, a spec that grades READY, and
`run --dispatch tRun --pass ARCH-tRun-1 --writes work/one.txt`.

- **AC1** — When the fixture's dispatch row is rewritten with a timestamp an hour old, the fixture
  commit is made with `GIT_COMMITTER_DATE` an hour old, the tree is clean, and the fixture conf
  carries `UNIT_STALL_BOUND=60` through `mkconf`'s sixth positional — `mkconf "true" "true" ""
  "3600" "" "60"` — `run --audit tRun` prints a line beginning `unattended-audit:
  ARCH-tRun-1 · dispatched` and ending ` · STALLED`, carrying `last-write none`, followed by the
  `unattended-audit: remedy —` line, and exits 0.
  Red when: the verdict reads `PROGRESSING`, which means `last-write none` was read as "now" or
  the commit clock was not consulted; or no line prints, which means the openness test closed a
  pass that has no build commit.
  fixture: the suite's own scratch repo; no live fixture in this tree.
- **AC2** — When the same fixture then gains one untracked file under the declared `work`
  directory, made with `touch`, the same invocation prints the same unit's line ending
  ` · PROGRESSING` with a numeric `last-write`, and no remedy line.
  Red when: the untracked file is not in the write set, which means the listing dropped
  `ls-files --others`, or the verdict stays `STALLED` because only the commit clock is read.
- **AC3** — When the fixture holds no dispatch row, or its one row's unit has a later commit
  naming the unit and touching a declared path, `run --audit tRun` prints exactly
  `unattended-audit: no unit is dispatched and open` and exits 0; when the commit names the unit
  but touches only the run-state file, the unit still prints as open. And the openness test is
  shared, not copied: `grep -c 'check_pass_open' tools/unattended/unattended.sh` prints at least 3
  — one definition, one call in `verb_dispatch`, one in `print_audit` — and
  `grep -c 'scan_dirty_paths' tools/unattended/unattended.sh` prints at least 3, with `check_clean`
  as its second caller; both print 0 at base.
  Red when: a declaration commit closes the pass, which is the overlap refinement missing; or the
  no-unit line is absent and the verb exits 0 over nothing; or either count is 2, which means the
  block was copied into the verb and the sibling kept its own.
- **AC4** — When the fixture conf declares no `UNIT_STALL_BOUND` — the `NOCONF` heredoc, which
  omits the key by hand exactly as it omits `GATE_BOUND` — stderr carries `declares no
  UNIT_STALL_BOUND, so a dispatched unit reads STALLED after the kit default of 1800s`, asserted by
  a second `hit` in that arm beside the `GATE_BOUND` one at `tools/unattended/unattended.test.sh:5219`;
  when it declares `UNIT_STALL_BOUND="abc"` or `"0"` — `mkconf`'s sixth positional set to `"abc"`
  or `"0"` — the driver prints `REFUSING - UNIT_STALL_BOUND is declared as` and `which is not a
  positive integer of seconds` and exits 2 before any verb runs. Every other fixture declares the
  key at the kit default through the positional's `${6-1800}`, so no existing arm sees a NOTE it
  did not see at base. Both keys read through one function: `grep -c 'read_bound_key'
  tools/unattended/unattended.sh` prints at least 3 — the definition and two calls — and prints 0
  at base; and with the fixture conf declaring `GATE_BOUND="abc"`, the driver still prints `which
  is not a positive integer of seconds`, which is the sentence the existing arm at
  `tools/unattended/unattended.test.sh:5197` asserts.
  Red when: a blank is silent, or junk is coerced to a number and the verb runs; or the count is 1
  or 2, which means a key kept its own `case`; or `GATE_BOUND`'s sentence changed bytes; or an arm
  comparing a whole `--status` line by `same` reds, which means a fixture was left with no
  `UNIT_STALL_BOUND` and the NOTE landed ahead of the verb's output.
- **AC5** — When `run --audit tNoRun` runs with no run-state file, when the fixture's phase is
  rewritten to `LANDED`, and when `stat` is shadowed on `PATH` by a stub that exits 1 with a dirty
  tree, each prints its own `UNATTENDED check 51 FAILED` sentence and exits 1, and each sentence is
  asserted verbatim by an arm in `tools/unattended/unattended.test.sh` so
  `python3 tools/memory-tree/check-arms.py --report` lists three `check 51` branches for the driver
  as `ARMED`.
  Red when: any of the three prints a verdict line instead; or `--report` shows a `check 51`
  branch unarmed, which means an arm quotes the wrong sentence.
- **AC6** — When `bash tools/unattended/adopt-unattended.sh --check` runs after the render, it
  exits 0, and `grep -c 'unattended.sh --audit'` over `tools/unattended/SKILL.template.md` is at
  least 2 — the keepalive prompt and the check-yourself line — and prints 0 at base; that grep is
  the Skill's only, because VERBS bullets carry no `unattended.sh`. The verb carrier is grepped in
  its own form: `grep -cP '^- \x60--audit\x60' tools/unattended/VERBS.template.md` — `\x60` is
  the backtick, spelled so the pattern holds none — prints 1 at the tip and 0 at base, which is the
  backticked-verb bullet shape check 26 joins and the `--status` bullet at
  `tools/unattended/VERBS.template.md:72` already has; the same grep for `--status` prints 1 at
  base on this node. The keepalive section's remedy prose is
  grepped for one pinned phrase: `grep -c 're-dispatch' tools/unattended/SKILL.template.md` prints
  1 at the tip and 0 at base, and the one hit sits in the keepalive section, `:19` to `:46` at
  base, so a Skill that names the prompt and says nothing about verdicts cannot pass. The section 8
  table of `tools/unattended/PROTOCOL.template.md` carries a `UNIT_STALL_BOUND` row, and the key is
  in `tools/unattended/.unattended.conf.example`, which is the pair check 22 of the kit gate joins.
  The fourth carrier check 22 does not join is grepped directly:
  `grep -c UNIT_STALL_BOUND tools/unattended/kit.toml` prints 1 — the `optional_keys` line and no
  other — and prints 0 at base.
  Red when: `--check` reports a drifted render; or check 26's three carriers or check 22's two
  disagree, observed at the close by `unattended kit gate`; or the VERBS count is 0, which means
  the bullet was spelled to some other grep and not to the carrier's form; or the `re-dispatch`
  count is 0, which means the keepalive got a probe and no remedy; or the `kit.toml` count is 0,
  which means the key is documented and declared but not listed, and no gate would say so.
- **AC7** — When `git show --stat HEAD` of the pass commit is read, it lists `.unattended.conf`
  together with `memory/guides/SESSION-KICKOFF.md`, and `wc -c` of `memory/map/features/unattended.md`
  is at most 20480, the `DOSSIER_CAP_BYTES` in `.memory-tree.conf`, while
  `grep -c -- '--audit' memory/map/features/unattended.md` prints at least 1 and prints 0 at base.
  Red when: the conf moved without the stamp, which `kickoff-manifest ratchet` reds at the close;
  or the dossier grew past its cap, which `memory hygiene` reds; or the `--audit` count is 0, which
  means the dossier was left untouched and its cap was satisfied by saying nothing.
  figure: the cap is DERIVED from `.memory-tree.conf` at observation; the dossier measured 20470
  bytes at base, PINNED here so the ten-byte headroom is not a surprise.
- **AC8** — When AC2's fixture — the untracked `touch` under the declared `work` directory — also
  has a tracked file removed from disk with `rm`, the `memory/guides/BUILD-METHOD.md` stub the
  fixture's base commit tracks and only `--preflight`'s `check_method` at
  `tools/unattended/unattended.sh:1149` reads, `run --audit tRun` prints the same unit's line ending
  ` · PROGRESSING` with a numeric `last-write`, exits 0, and prints no `UNATTENDED check 51 FAILED`
  sentence. `git rm --cached` is not this fixture: it leaves the file on disk, so `stat` answers
  and the branch under test is never reached.
  Red when: the liveness refusal prints, which means a `stat` failing on a listed path was read as a
  dead probe instead of a deletion; or the line reads `STALLED` with `last-write none`, which means
  the skip discarded the whole set rather than the one path.
- **AC9** — When `bash tools/unattended/unattended.test.sh` runs unsharded and as `--shard 2/2` at
  the landed tip, neither prints a `FAIL executed` line, and `FLOOR_ASSERTIONS` at
  `tools/unattended/unattended.test.sh:5434` and `FLOOR_SHARD_2` at `:5461` each stand exactly this
  unit's arms' executed assertions above their base values of 706 and 510, while `FLOOR_SHARD_1` at
  `:5458` and the shadowed 675 at `:5403` are unchanged, because the arms sit in region two beside
  the `--dispatch` arms. Observed at `--close`; its ledger row reads `observed at --close`.
  Red when: a floor did not move, so a stranded or unreachable check-51 arm is invisible and unit
  6's "exactly the added arms above 706" measures against a base already carrying these; or a floor
  moved by more than the arms added, which means the count was read off the file and not off a run.
  figure: the added-arm count is DERIVED from the suite's floor-breach line with the floor
  over-pinned, the method `TOOL-aRatifiedRulings-2` AC6 records and `TOOL-aProbedUnit-6` AC12
  cites; the floors are then PINNED. 706, 510, 208 and 675 are PINNED, read at base on 2026-09-14.
  cost: minutes; the suite is on no bar leg and is `--close`'s compensating run via
  `bash tools/unattended/run-unattended-gates.sh` on a frozen clone.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `kickoff-manifest ratchet` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness`

These are what `--close` runs, once, on the whole bar. The pass runs none of them: it verifies with
the driver invocations section 6 names over a scratch clone, and `python3
tools/memory-tree/check-arms.py --report` filtered to the driver, which is the meta-gate's report
mode and not its leg. Under `unattended kit gate`, checks 22 and 26 are the joins this unit moves.

New arm: `tools/unattended/unattended.test.sh` · the three check-51 refusals, each observed by the
fixture in AC5 against the driver before the branch exists — a missing file, a `LANDED` phase, a
shadowed `stat` — plus the STALLED, PROGRESSING, no-unit and deletion fixtures of AC1 to AC3 and
AC8 and the two bound arms of AC4 · `FLOOR_ASSERTIONS` at `:5434` and `FLOOR_SHARD_2` at `:5461`
rise by the arms' executed assertions, AC9; `FLOOR_SHARD_1` at `:5458` does not move, and the
assignment at `:5403` is the shadowed one the file marks as inert.

## 8. Open questions

- **F1 — the process-side pointer line.** The brief: where `tools/process-monitor/census.py` is
  tracked, print one line naming it as the process-side probe; where not, nothing. Three ways to
  know "tracked" from inside a shipped kit file. (a) A second optional conf key on `RECALL_CLI`'s
  pattern, blank meaning the kit is absent. (b) A `git ls-files` glob for the file, spelled with a
  leading `*/` so `tools/check-install-prefix.sh`'s lead-character class does not match it. (c) No
  line: the Skill's remedy prose names the process-monitor kit by name, and the verb's header says
  the process side is not its question. Recommendation: (c).
  RESOLVED (agent, 2026-09-14, delegated): (c). (a) is a new public surface the mandate priced
  only `UNIT_STALL_BOUND` for, which is M3's second veto. (b) evades the carried-prefix ratchet's
  predicate while breaking the rule it enforces — a kit file names nothing outside itself by
  literal — and a rule broken where its gate cannot see is worse than one the gate reds. (c) fails
  no acceptance criterion, needs nothing new, and `TOOL-aQuenchedHarness-12` already records the
  process-liveness build the prose points at.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.
- rev-2 · 2026-09-14 · §2 S3 S4 S5 · §3 · §4 · §5 · §6 AC3 AC4 AC6 AC7 AC8 AC9 · §7 · folded round-1 spec-audit clusters F (spec-3 half: this unit owns `read_bound_key`), I (id 9), M (ids 10, 11, 13) and N (id 12).
- rev-3 · 2026-09-14 · §3 Edges · §4 · §6 AC1 AC4 AC6 · folded round-2 spec-audit clusters E (id 2: the VERBS half of AC6 greps the bullet's own form), I (id 7: AC6 pins `re-dispatch` in the keepalive section) and K (id 15: the fixture interface — `mkconf`'s sixth positional, the second `NOCONF` hit, unit 6 takes the seventh).
- rev-4 · 2026-09-14 · §4 item 2 · folded the closing diff review round 1, cluster A (ids 19, 1, 6): `print_audit` unions a unit's same-anchor dispatch rows with a new anchor replacing, mirroring check 23's key, and skips a unit whose spec status is terminal the way `--plan` resolves it; the `verb_dispatch` sentence claiming the two verbs cannot disagree is rewritten to state the two populations (per row for the disjointness proof, the union for the stall clock); two red-first arms in `unattended.test.sh` beside AC3 — two same-anchor rows with a pass commit inside the first, and a CLOSED spec with an open row, both printing `no unit is dispatched and open` — observed red against a frozen copy of the base kit. Floors +2 of the +19 the fold adds.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "report a dispatched unit idle past a declared bound from the run-state file"`
returned no shell seam — its own header prints `unscanned layers: .sh` — and its top symbol hits
(`run`, `report`, `run_bounded` in `tools/process-monitor/census.py`) are Python. The seams this
unit extends were found by reading the driver and are cited by line in section 4: `pass_commit` at
`tools/unattended/lib-unattended.sh:164`, the sibling-openness block at
`tools/unattended/unattended.sh:4802`, `check_clean`'s listing at `:1077`, `verb_status`'s brief-row
`awk` at `:2865`, and the `GATE_BOUND` read at `:305`. Two disagreements with the brief, both
settled by source: the brief names `check-brief-recorded.sh` and `check-pass-order.sh` as the join
to reuse, and both call `build_commit`, which answers "which commit BUILT a CLOSED unit" over a
range with exclusions; "is this pass still open" is `pass_commit` with the overlap test, the join
`--dispatch` makes, so that is the one shared. And the brief spells the driver token as
`{{TOOL_ROOT}}`; the Skill spells the driver `{{KIT_DIR}}` at every invocation. The memory-recall
hit `TOOL-aQuenchedHarness-12` records a prior reuse audit missing the process-monitor build, which
F1 cites rather than repeats.

Recall terms used: `dispatch row unit stall elapsed idle keepalive cron audit probe process-monitor census bound conf`
