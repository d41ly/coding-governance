# TOOL-aGraftedHelix-38 — three checks that went blind when units 32 to 36 moved code into helpers

**Status:** CLOSED · rev-2 · 2026-10-06 · node a · Tier-2 · base 290d0d2d · streams tooling · order 22 · ratified 2026-10-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-38-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-38-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-prompt-TOOL-aGraftedHelix-38-1-spec-brief.md](../prompts/2026-10-06-prompt-TOOL-aGraftedHelix-38-1-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

At VERIFYING, the owed unattended suites ran once as a pooled calibrate on a frozen clone at
`eb96ea8b2`, and 11 of 20 rows went red. Every one of the 58 failing arm lines traces to one of three
defects this build brought in. In each, a check that reads source by function went blind when a unit
moved code into a new function. This unit fixes each check at its root and leaves a gate behind for
each class, so the next helper extraction reds with a remedy instead of reaching a calibrate.

## 2. Scope (IN)

- **S1** — Check 51 in `tools/unattended/check-unattended.sh` counts a claim write made through a
  DECLARED helper. A new constant, `TERMINAL_CLAIM_HELPER_FNS`, sits beside
  `TERMINAL_CLAIM_EXEMPT_FNS` and ships naming `write_settle_claim`, with a comment line above it
  giving that entry's reason. A non-comment line of a function that calls a listed name sets the
  function's claim-write flag exactly as a `write_claim` call does. The list is graded in both
  directions: a listed name that is no function of the check's population, or whose own body holds
  no `write_claim` call, is a hit naming that entry. A helper of a helper does not count. Observed by
  AC1 and AC2.
- **S2** — Check 51's header and report line say what S1 changed. PREDICATE names the declared
  helper and the one level it reaches. "What this does NOT check" adds three gaps: a helper whose
  `write_claim` sits on a path its caller never reaches, the status a helper writes, and a call to
  any function the list does not name, however that function writes a claim. The report line keeps
  its text through `0 exempt` and appends the count of terminal writers passed through a declared
  helper. Observed by AC1 and AC3.
- **S3** — Check 51's arm block in `tools/unattended/check-unattended.test.sh` gains five arms,
  staged as the existing ones are: a function appended to the fixture's tracked lib by sed's `r`,
  with the terminal write spelled from fragments. (a) A terminal writer that calls an unlisted helper
  holding no claim write is a hit naming the writer. (b) The same helper put on the list is a hit
  naming the list entry. (c) A terminal writer that calls `run_hold`, which calls `write_claim`
  itself and is not on the list, is a hit naming the writer. (d) A terminal writer calling a listed
  helper that calls `write_claim` is silent. (e) A list entry naming `ghosthelper` is a hit naming it.
  The floors of the shard holding the block and `FLOOR_ASSERTIONS` rise by exactly the assertions
  the five arms add. Observed by AC2 and AC9.
- **S4** — Rule 2 of `tools/unattended/unattended.test.sh`, a parking function carries the
  bypass-flag guard, takes its one exemption as a declared pair: the parking function
  `write_preflight_record()` and the guard function `check_waivers`, held in shell variables the
  rule's awk programs read, its red fixture's copy included. The comment above it states the call
  structure the pair rests on. Two inline arms join it. (a) The exempted function parks under the
  rule's own framing, or the arm fails naming the stale name. (b) At least one function calls the
  exempted function, every such caller calls the guard function on an earlier line, and the guard
  function carries the bypass token, or the arm fails naming the caller. The suite's floors rise by
  exactly the assertions added. Observed by AC4 and AC9.
- **S5** — The arms-groups linter, `tools/unattended/check-arms-groups.sh`, frames a function's span
  without counting braces inside a single-quoted string that spans lines. Per line, single-quoted
  pairs are cleared FIRST, then the strings and expansions the shipped `strip` already clears, and a
  single quote left over opens a string whose state is carried to the next line. The order matters:
  `strip` clears `"…"` pairs before `'…'` pairs, and a `"…"` pair can straddle a single-quoted
  string's closing quote, which leaves a quote that opens nothing (§4). While the state is open a
  line contributes no brace until its closing quote, and the comment tail is cut only outside the
  quote. A span closes when its depth reaches zero with no quote open. The idiom `'\''` is cleared
  before the count. The helper doing this is awk-local and named `extract_counted`. Observed by AC6
  and AC7.
- **S6** — The same linter REFUSES, exit 2, a function span that reaches the end of the file
  unclosed or holds, after its first line, a column-0 function definition or a column-0
  `if in_shard` seam. The refusal names the function, the line it opened on and the first line it
  swallowed. It is checked after pass 1 and before any group is cut, so no verdict is printed over a
  mis-framed file. The header's WHAT IT DOES NOT GRADE adds the framing's remaining blind spot: a
  multi-line double-quoted string or heredoc body carrying an unbalanced brace, refused only when it
  swallows a definition or a seam. Observed by AC7.
- **S7** — `tools/unattended/check-arms-groups.test.sh` gains a FRAME block of synthetic fixtures:
  (a) a function holding a multi-line single-quoted awk program with an escaped brace in a regex,
  followed by a seam and one arm, reads GREEN with its seam counted; (b) a function whose multi-line
  double-quoted string carries a brace and swallows the seam after it exits 2 naming the function and
  the seam's line; (c) a function never closed before the end of the file exits 2 naming it.
  `FLOOR_ASSERTIONS` rises by exactly the assertions the block adds. Observed by AC7 and AC9.
- **S8** — The class records. A new class record, `a-helper-extraction-blinds-a-per-function-rule`,
  names the two instances S1 and S4 close, their gates, the per-function rules of this kit that read
  the same way and are not red today, and why the two instances do not share one mechanism (§8 F2).
  Its Related line points at `two-guards-one-question-two-answers`, whose one-derivation remedy F2
  measured and found does not apply. The `unattended` dossier's gotcha classes claim it. The record `a-pair-exists-and-it-is-the-wrong-one`
  gains the S5 instance under its "Where it bit" and S6 and S7 as its gate. The gotcha index is
  regenerated. Observed by AC10.
- **S9** — The `unattended` kit's version moves once, after the unit's last edit to a shipped file,
  in every carrier `tools/check-kit-versions.sh` pairs, and the installed guides are re-adopted from
  their templates. Observed by AC11.
- **S10** — Every failing arm line in the calibrate's outputs is attributed to one of the three
  defects, and the acceptance ledger records the table §4 gives. An arm none of them explains would
  join this unit; the spec-time read found none. Observed by AC8.

## 3. Non-goals (OUT)

- **No change to the driver's behaviour.** `run_settle`, `write_settle_claim`,
  `write_preflight_record`, `verb_preflight` and `check_waivers` keep their bytes. The code each
  check reads is correct and the checks are wrong. The one edit to `tools/unattended/unattended.sh`
  is S9's version constant.
- **No change to the suite's `check_helpers_hoisted`.** Its awk program is legal shell, and the
  linter's brace count was never stated as a contract on suite authors (§8 F3).
- **No call-graph engine and no library shared by check 51 and rule 2.** The two follow calls in
  opposite directions (§8 F2), so one mechanism would have to answer a question neither asks.
- **No audit of the kit's other per-function rules.** Rule 1, check 39 and check 48 read a function
  the same way and are green today. S8's class record names them as its documented check.
- **No change to the linter's subject, rules or findings.** It still lints
  `tools/unattended/check-unattended.test.sh` by default, and the findings the fix un-hides are
  reported and never waived, as its header already says.
- **No new leg, project conf key or environment override.** `TERMINAL_CLAIM_HELPER_FNS` is a
  constant inside the leg, as its sibling list is, and moves only by a fixture's `sed`.
- **The owed suites are not run here.** The main loop runs them once at VERIFYING, after this unit
  is terminal.

### Edges

- **consumes-from** external — check 51 as unit 31 built it, `write_settle_claim` and
  `check_helpers_hoisted` as unit 36 added them, and `write_preflight_record` as unit 32 split it
  out, all as they stand at `eb96ea8b2`; this unit builds none of them.
- **hands-off** external — the re-run of the owed unattended suites, which the main loop makes once
  at VERIFYING and which observes the 11 red rows go green.

## 4. Design

### What the calibrate outputs say

Read whole at spec time: the 20 outputs under the clone's `.git/gate-logs/selftests/`, the clone at
`%TEMP%/aghv` checked out at `eb96ea8b2`. A line opening `FAIL` is a failing arm. 58 such lines sit
in 11 outputs, and the other nine outputs end in PASS or `exit 0`.

| Output | FAIL lines | Defect |
|---|---:|---|
| `unattended_gate_selftest_shard_<k>_8.out`, k = 1..8 | 35 | 1, check 51 |
| `unattended_cross-component.out` | 6 | 1, check 51 |
| `unattended_driver_selftest.out` | 1 | 2, the parking guard |
| `unattended_arms-groups_selftest.out` | 16 | 3, the linter's framing |

Of the 41 defect-1 lines, 35 carry check 51's own text: 33 quote `UNATTENDED check 51 FAILED`,
including every `check_emitted` line, whose `missing:` field is empty and whose `unexplained:` field
is check 51 alone, and shard 7's two `miss` arms quote its hit text. The other six are exit-code arms
that print no cause: cross-component arms 3 and 3b, shard 1's conforming tree and young tree,
shard 3's LANDED record, and shard 4's nine-mutation tree. Each runs the leg over a fixture that
copies the real driver, and no FAIL line in any output names a check other than 51. S10's ledger
confirms those six by slice after the fix.

### Defect 1 — check 51 cannot see `write_settle_claim`

Check 51 reads, per function, a terminal `set_fact … phase LANDED|ABORTED` and a `write_claim` call
on a non-comment line of the same function. Unit 31 built it when `run_settle` wrote the claim
inline. Unit 36 S4 moved that write into `write_settle_claim`, called from the settle's `first` path
and its already-settled `retry` path, so one implementation serves both. The predicate does not
follow the call. `bash tools/unattended/check-unattended.sh` at `65a8f167` exits 1 with the single
hit `tools/unattended/unattended.sh:6138 run_settle()`, and its report line reads `364 function(s)
in 10 shell file(s) of this kit, 4 writing a terminal phase, 0 exempt` (637 s on node `a`,
2026-10-06, under concurrent load).

The candidates the brief names, tested by a probe that copies check 51's framing and predicate and
reproduces its counts exactly (364 functions, 10 files, 4 writers):

| Candidate | `run_settle` | planted `c51nohelper` | planted `c51hold` |
|---|---|---|---|
| C1, one level into any function that calls `write_claim` | passes | red | passes |
| C2, the transitive closure over the population | passes | red | passes |
| C3, a declared helper list, each entry graded to call `write_claim` | passes | red | red |

`c51nohelper` writes `ABORTED` and calls `read_claims`, which writes no claim. `c51hold` writes
`ABORTED` and calls `run_hold`, which writes a `held` claim. That is the H3 shape check 51 exists
for: a terminal record over a claim reading `held`, which never ages. Ten functions call
`write_claim` directly: `write_settle_claim`, `write_claim_beat` and eight verbs or `run_*`
functions. The closure adds `run_handoff` and `run_settle`. Under C1 or C2, any terminal writer that
calls one of those verbs for its own reasons passes. C3 passes only a call to a function someone
declared to be a claim writer, and the grade on the list stops that declaration from naming one that
writes none. C4, putting the `write_claim` call back inline in `run_settle`, fixes the instance and
splits unit 36's one helper back into two copies; it is rejected.

Implementation, for the builder: a second awk variable carries the list, and `scan()` sets `cw` on a
listed name with the same boundary rule it applies to `write_claim`. A separate per-function flag
records a DIRECT `write_claim` call, and the END block grades each listed name against the functions
seen and that flag, appending a hit line in the shape the exempt list's stale line already uses.
The NO-WRITER liveness refusal is unchanged.

### Defect 2 — rule 2's exemption names a function that no longer parks

Rule 2 reads, per function, a `park "$rel"` call and a `BYPASS_BAN` token, and exempts
`verb_preflight()` by literal because its guard lives in `check_waivers`, which it calls. Unit 32
moved the waiver `park` into `write_preflight_record`, which `verb_preflight` calls at `:6416` after
`check_waivers` at `:6314` and after the `status` gate at `:6394` that ends the verb on any refused
precondition. The exemption was keyed on a name, so the move left it naming a function that parks
nothing and left the new parking function unguarded in the rule's eyes. Measured at `65a8f167` under
the rule's framing: eleven functions park, ten carry the token, and the one that does not is
`write_preflight_record()`. Its callees carry no `BYPASS_BAN` token, and `check_waivers` does.

The guard sits BESIDE the park, in the caller's earlier callee, not below it. Following
`write_preflight_record`'s own calls, one level or transitively, never reaches `check_waivers`, so
the call-following check 51 needs does not serve here (§8 F2). S4 keeps one declared exemption and
makes its stated reason a graded fact: the pair names the guard function, arm (b) derives the
callers and checks the order, and arm (a) is the stale-entry arm whose absence let `verb_preflight()`
sit stale.

### Defect 3 — the linter's brace count runs off the end of the suite

Pass 1 of the linter frames function spans by counting braces over lines with quoted strings,
`${…}` and comment tails stripped one line at a time. Unit 36 S11 added `check_helpers_hoisted` at
`tools/unattended/check-unattended.test.sh:789`. Its awk program is a single-quoted string spanning
four lines, and one line carries the regex `\(\) *\{`, whose brace opens nothing but is counted. The
span never closes, runs to line 6728, and marks every later line a function body. The linter then
cuts 0 groups and 0 arms and REFUSES. Unit 34's region re-cut and unit 36's nine `read_topo` seams
did not move the anchor: the suite at `910b8608`, unit 36's parent, frames 76 functions with none
running off, and the shipped linter over it prints RED with 25 findings. That answers §8 F5.

Candidates, each run over all thirteen `*.test.sh` files of the kit and over the suite at `910b8608`,
comparing every function's span with the shipped framing:

| Candidate | `check_helpers_hoisted` | other spans moved | lost on |
|---|---|---|---|
| P2, a span ends at the first column-0 `}` | closes | 14 functions merged into neighbours | `_bm_sections` swallows four, `pedit` six |
| P3, escaped braces stripped before the count | closes | `scan_exit_sites` in `runlog-writer.test.sh` ends at 379, one line early | the `(\{\|then\|else\|do)` regex at its line 369, which the shipped count balances |
| P4, the suite rewrites its regex outside the count | closes | none | the next author's multi-line program |
| P5, no brace counts inside a single-quoted string spanning lines | closes | none in twelve files; in the driver suite, `dodarm` stops running off | — |

P5 agrees with the shipped framing on every function the shipped framing frames correctly, and
corrects the two that run off: `check_helpers_hoisted` here and `dodarm` in
`tools/unattended/unattended.test.sh`, which the linter does not lint. A scratch copy of the linter
with P5 as pass 1 reads the tracked suite as `boundaries 563 (17 seams) · groups 563 · with arms 462 ·
arms 920 · batched 14 · sentinels 0` and RED with 25 findings, rule A 0, rule B 24 and rule C 1, the
pre-unit-36 figures. Over a synthetic file holding the defect's shape, the shipped linter REFUSES and
the P5 copy reads GREEN.

P5 as rev-1 first worded it, the odd count read AFTER `strip`, moves one span the shipped framing
frames correctly: `seed` in `tools/unattended/adopt-unattended.test.sh`, 146 to 224 under the shipped
framing and 146 to 214 under it. Its line 187 reads `sed -n 's/^…"event":…"\([^"]*\)".*/\1/p' "$_fr"`;
`strip` pairs the double quote after `\)` with the one opening `"$_fr"`, which swallows the closing
single quote between them, so one quote is left over and reads as opening a string the line closes.
That is the `a-pair-exists-and-it-is-the-wrong-one` class again. Clearing single-quoted pairs first
moves no correct span: measured at rev-2 over the thirteen suites and the suite at `910b8608`, the
only spans that move are the two run-offs.

S6's refusal is the left-shift. Under the shipped framing it fires on the tracked suite, naming the
17 seams that `check_helpers_hoisted` swallowed. Under P5 it fires on none of the thirteen suites and
on none at `910b8608`, so it reds nothing that frames correctly today. It turns the framing's
remaining blind spot into a named refusal rather than the anonymous `parsed 0 group(s)` this defect
produced.

### Inventory

| identifier | where | cell |
|---|---|---|
| `TERMINAL_CLAIM_HELPER_FNS` | `tools/unattended/check-unattended.sh` | constant, no naming cell grades it |
| `extract_counted` | the awk program of `tools/unattended/check-arms-groups.sh` | awk-local, named with a declared verb |
| `check_span_integrity` | the same awk program, if S6 is written as a function | awk-local, named with a declared verb |
| `park_exempt_fn`, `park_exempt_guard` | the rule 2 block of `tools/unattended/unattended.test.sh` | top-level shell variables |
| `a-helper-extraction-blinds-a-per-function-rule` | the gotcha catalogue | class record |

Both awk names were asked of `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` on
2026-10-06 and answered OK. No shell function, check number, leg or conf key is minted.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-arms-groups.sh`
- `tools/unattended/check-arms-groups.test.sh`
- `tools/unattended/unattended.sh`, the version constant only
- `memory/gotchas/a-pair-exists-and-it-is-the-wrong-one.md`
- `memory/gotchas/INDEX.md`
- `memory/map/features/unattended.md`
- the new class record under the gotcha catalogue, and every other version carrier
  `tools/check-kit-versions.sh` pairs for the `unattended` kit, with the guides
  `tools/unattended/adopt-unattended.sh` re-adopts from them

### Rollout

One pass, in this order, each step verified by its own criteria before the next:

1. S10's attribution, read from the clone before any edit.
2. S5, S6 and S7, the linter and its fixtures, so the arms S3 adds are linted as they are written.
3. S1, S2 and S3, check 51 and its arms.
4. S4, rule 2 and its arms.
5. S8, the class records, the dossier claim and the index.
6. S9, the version, last.

### Alternatives rejected

- **C1 and C2 for check 51**, by the `c51hold` plant above, which both pass.
- **A guard of its own inside `write_preflight_record`**, as §8 F2 records.
- **P2, P3 and P4 for the linter**, by the measurements above.
- **Putting the linter's suite on the bar**, which would have caught defect 3 before VERIFYING. It is
  a kit self-test, and the owner ruled kit self-tests off the bar on 2026-08-23.

## 5. Production-readiness checklist

- security — No credential, endpoint or write path. Check 51 grades the kit's own source, and the
  helper list can only make it stricter than a derived rule would be.
- perf / scale — Check 51 adds one array lookup per word of a function line it already scans. The
  linter's pass 1 adds one `index` per line inside a function. Both stay one awk process.
- error / empty / loading states — A helper list entry that names nothing is a hit, never a silent
  pass. A linter span it cannot close is a named refusal, never a verdict. Rule 2's caller arm fails
  when the exempted function has no caller, so it cannot pass by finding nothing.
- observability — Check 51's report line counts the writers passed through a helper. The linter's
  refusal names a function and two line numbers.
- risks — Edits to `tools/unattended/check-unattended.sh` move lines under the install-prefix
  waivers, which are line-keyed, so the builder reads that leg and re-keys any moved row. The new
  check 51 arms must add no rule A, B or C finding to the linter's reading of the gate suite, which
  AC9 compares. Correcting the framing un-hides the suite to the linter, and its findings return to
  25, which are reported, not graded.
- testing — Every new arm is observed red on a staged break before it lands. Each defect is first
  reproduced: AC1 over the parent's leg, AC4 over the parent's driver and AC6 over the parent's
  linter. The owed suites run once at VERIFYING, at the main loop.
- migration — None. The helper list ships the one entry the real tree needs, and the rule 2 pair
  names the function the real driver holds.
- user docs — The two gotcha records. The kit README describes neither check and is not edited.

## 6. Acceptance criteria

Criteria naming a slice run it from the session scratchpad under a name that is not a suite name. A
slice is the suite's prologue plus the block the criterion names. Each staged break is made in a
scratch copy and undone before the next criterion, which `git diff --quiet` against the pass's
commit confirms. "The parent" is the pass's parent commit. The gate suite, the driver suite and the
linter suite are the three files §7's `New arm:` lines name, in that order.

- **AC1** — When `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh` runs at the
  pass's commit, no line carries `check 51 FAILED`. The check 51 report line still carries `4 writing
  a terminal phase, 0 exempt`, and its appended count of writers passed through a declared helper
  reads 1. The same command at the parent exits 1 naming `run_settle()`.
  Red when: the list is empty or `scan()` never reads it, so `run_settle()` is named again.
  cost: about 11 minutes on node `a` under concurrent load, measured 2026-10-06; run it once.
  figure: the counts are DERIVED at observation; 364 functions and 4 writers are PINNED at `65a8f167`.
- **AC2** — When a slice of the gate suite runs check 51's block at the pass's commit, every
  assertion passes: arms (a), (b), (c) and (e) are hits naming the planted
  writer or entry, and arm (d) is silent. Each arm is observed red on its own break in a scratch copy
  of `tools/unattended/check-unattended.sh`: (a) a `scan()` that sets `cw` on any called function;
  (b) and (e) the list's grade cut; (c) the list set to all ten direct `write_claim` callers, which
  is C1 written as data; (d) the helper match cut.
  Red when: arm (c) passes on the C1 copy, which would mean the arm cannot tell a declared helper
  from an arbitrary claim-writing call.
- **AC3** — When `grep -n "TERMINAL_CLAIM_HELPER_FNS" tools/unattended/check-unattended.sh` runs, it
  prints the declaration, its reason line and at least one header line, and the comment block above
  the declaration names one declared level and the three gaps S2 lists.
  Red when: the header still describes a claim write as a `write_claim` call on a line of the same
  function and nothing else.
- **AC4** — When a slice of the driver suite holding its variable prologue and
  rule 2's block runs at the pass's commit, no line opens `FAIL`. With `park_exempt_fn` set to
  `verb_preflight()`, arm (a) fails naming it. Over a copy of `tools/unattended/unattended.sh` with
  `verb_preflight`'s `check_waivers` call cut, arm (b) fails naming `verb_preflight()`. The existing
  red fixture still fires on a copy with every bypass guard cut. The parent's rule 2 over the
  parent's driver names `write_preflight_record()`.
  Red when: the exemption names a function that parks nothing and no arm says so.
- **AC5** — When `awk` prints every function the pass's rule 2 framing finds parking, over
  `tools/unattended/unattended.sh`, the list holds `write_preflight_record()` and not
  `verb_preflight()`, and the exemption variable names the first.
  Red when: the pair names `verb_preflight()`, whose body holds no `park "$rel"` line.
- **AC6** — When `bash tools/unattended/check-arms-groups.sh` lints the tracked gate suite at the
  pass's commit, it exits 0 or 1, prints no `REFUSED`, and its liveness line reports more than zero
  groups and `(17 seams)`. The parent's linter over the same file prints `REFUSED — parsed 0
  group(s)`.
  Red when: pass 1 counts the brace in `check_helpers_hoisted`'s regex again and the run refuses.
  figure: the seam count is DERIVED by `grep -c "^if in_shard" tools/unattended/check-unattended.test.sh`;
  563 groups, 920 arms and the 25 findings are PINNED at `65a8f167` from the P5 probe, and the
  ledger records the pass's own reading beside them.
- **AC7** — When `bash tools/unattended/check-arms-groups.sh` lints each of S7's three fixtures,
  written to the scratchpad by the bytes S7's block writes: fixture (a) prints `GREEN` with `(1
  seams)`, and the parent's linter refuses it; fixture (b) exits 2 naming the function and the line
  of the seam it swallowed; fixture (c) exits 2 naming the unclosed function.
  Red when: S6's refusal is cut from a scratch copy of the linter, so fixture (b) refuses only as
  `parsed 0 group(s)` and names no function.
- **AC8** — When `grep -h "^FAIL" $TEMP/aghv/.git/gate-logs/selftests/*.out | wc -l` runs, it prints
  58, and sorting those lines by §4's classifier leaves none unclassified. A slice of each of the six
  exit-code arms §4 names, run at the pass's commit, passes. The acceptance ledger records the table.
  Red when: a FAIL line carries none of the three causes, or an exit-code arm still fails after the
  fix, either of which names a fourth cause that joins this unit.
  fixture: the clone at `%TEMP%/aghv`, at `eb96ea8b2`, holds the outputs today; nothing else does.
  cost: shard 4's nine-mutation arm runs the leg nine times over a fixture, minutes on node `a`.
- **AC9** — When `git diff` from the parent over each of the three suites is filtered for the
  assertion lines it adds, the counts equal the rise of each suite's floors: `hit`, `miss`, `same`
  and `mutate` lines in the gate suite, `n=$((n+1))` lines in the driver suite, and `check_has`,
  `check_lacks` and `check_same` lines in the linter suite. The pass's
  `bash tools/unattended/check-arms-groups.sh` reports the same rule A, B and C counts over the
  parent's gate suite, written to the scratchpad by `git show`, as over the pass's own.
  Red when: a floor rises by a number its block does not carry, or the new check 51 arms add a
  linter finding.
- **AC10** — When `python tools/memory-tree/gotchas.py --check` runs, it exits 0.
  `grep -c "a-helper-extraction-blinds-a-per-function-rule" memory/gotchas/INDEX.md` prints at least
  1, `grep -c "check-arms-groups" memory/gotchas/a-pair-exists-and-it-is-the-wrong-one.md` prints at
  least 1, and every line of `python tools/codebase-map/test_codebase_map.py` reads `ok`.
  Red when: the new class is unclaimed by a dossier, so the map's coverage test names it.
- **AC11** — When `python tools/govkit/govkit.py epoch --base <the parent>` runs at the pass's
  commit, its `unattended` line reads `clean` at the bumped version, and
  `bash tools/check-kit-versions.sh` and `bash tools/unattended/adopt-unattended.sh --check` each
  exit 0.
  Red when: the kit's shipped bytes moved and its version did not, or an installed guide differs
  from its template.
  figure: the version is DERIVED from the parent at observation.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `gotchas selftest` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `line length` · `recall floor` · `recall floor arms` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-unattended.test.sh · check 51 arms (a) to (e), each staged as AC2 names · the shard holding check 51's block and FLOOR_ASSERTIONS, by the assertions added
New arm: tools/unattended/unattended.test.sh · rule 2 arms (a) and (b), staged as AC4 names · the driver suite's floors, by the assertions added
New arm: tools/unattended/check-arms-groups.test.sh · FRAME fixtures (a) to (c), staged as AC7 names · FLOOR_ASSERTIONS, by the assertions added

None of the three suites is on the bar. A pass runs every criterion above directly, through the
leg's script, the linter and slices, and the main loop runs the owed suites once at VERIFYING.

## 8. Open questions

- **F1 — How does check 51 recognise a claim write it does not see inline?** The options are the
  brief's three: one level into any function that calls `write_claim` (C1), the transitive closure
  (C2), or a declared helper list graded to call `write_claim` (C3), plus C4, moving the call back
  inline. The brief's criterion is the option that cannot pass a terminal writer that writes no
  claim of its own. §4's probe shows C1 and C2 both pass `c51hold`, a terminal writer whose only
  claim write is `run_hold`'s `held`, the shape check 51 was built against. C4 fixes the instance and
  duplicates unit 36's one helper. C3 trips no veto: the list is a constant inside an existing leg.
  RESOLVED (agent, 2026-10-06, delegated): C3, `TERMINAL_CLAIM_HELPER_FNS`, one declared level, each
  entry graded to call `write_claim` itself.
- **F2 — Does `write_preflight_record` carry the guard, or does rule 2 follow the call as check 51
  now does, and do the two share one question?** The options: (a) a `BYPASS_BAN` test of its own
  inside `write_preflight_record`; (b) rule 2 follows calls as check 51 does; (c) the exemption moves
  to the function that parks, declared with its guard, and the call structure it rests on is graded.
  (a) is a second derivation of `check_waivers`' refusal 41, the two-guards class itself, placed
  after the claim write and unreachable, since the `status` gate at `:6394` ends the verb first. (b)
  does not reach the guard: `write_preflight_record`'s callees carry no `BYPASS_BAN` token, because
  the guard is in its caller's earlier callee. Check 51 follows a call DOWN to a helper and rule 2's
  guard sits BESIDE the park, so the two questions differ, and one mechanism for both would answer a
  question neither asks. (c) trips no veto and adds the stale-entry arm the old exemption lacked.
  RESOLVED (agent, 2026-10-06, delegated): (c), the pair `write_preflight_record()` and
  `check_waivers` with arms (a) and (b), and no shared mechanism; S8's class record states why.
- **F3 — Is the parser or the suite fixed?** The linter's header never states its brace count as a
  contract on suite authors, and the suite's multi-line awk program is legal shell, so the suite's
  shape is legitimate. P4 fixes this regex and leaves the next one to the next author. Among the
  parser fixes, §4's measurement rejects P2, which merges 14 spans, and P3, which mis-frames a
  function the shipped framing frames right. P5 moves no correct span and fixes both run-offs.
  RESOLVED (agent, 2026-10-06, delegated): fix the parser, with P5.
- **F4 — Does the linter refuse a span that swallows a definition or a seam, or only report it?**
  A refusal is exit 2, so a suite carrying a mis-framed function gets no verdict at all. Reporting it
  beside a verdict would print a GREEN or RED graded over a population the linter knows it cut
  wrong, which is the green-by-absence class. The refusal fires on no suite of the kit under P5.
  RESOLVED (agent, 2026-10-06, delegated): refuse, naming the function and both lines.
- **FACT-QUESTION · F5 — Which change moved what the linter anchors on?** Probe: the shipped linter
  and a span printer copying its pass 1, run over the suite at each of `910b8608` and `65a8f167`.
  Liveness: the span printer reports a run-off when one exists, shown by `check_helpers_hoisted`
  running from 789 to 6728 at `65a8f167`. Observation: at `910b8608`, 76 functions and no run-off,
  and the linter prints RED with 25 findings; at `65a8f167`, one run-off, at the function unit 36
  S11 added.
  RESOLVED (agent, 2026-10-06, delegated): unit 36's `check_helpers_hoisted`, not unit 34's re-cut or
  the `read_topo` seams.

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, from the unit 38 spec brief, grounded at `65a8f167`, which
  carries the kit bytes of `eb96ea8b2`, with the calibrate's 20 outputs read whole and the check 51,
  rule 2 and framing probes run on node `a`.
- rev-2 · 2026-10-06 · node a · at the build, before the code commit: S5 clears single-quoted pairs
  BEFORE the strings `strip` clears, because rev-1's wording, the odd count read after `strip`,
  disagreed with §4's own measurement: built as worded, it moved `seed` in
  `tools/unattended/adopt-unattended.test.sh`, a span the shipped framing frames correctly, through a
  `"…"` pair straddling a single quote. §4 records the measurement, and the kit holds thirteen
  `*.test.sh` files, not twelve.

## 10. Reuse audit

The map probes were these two:

```bash
python tools/codebase-map/reuse_lookup.py "follow a function call to find a write a helper performs"
python tools/codebase-map/reuse_lookup.py "frame shell function bodies by brace balance skipping quoted text"
```

Both ranked name-stem neighbours only, `write`, `write_text` and `read_text` first, and both printed
`unscanned layers: .sh`, so their miss is no evidence about the three shell files this unit edits,
which were read by hand. The second surfaced `parse_shell_defs` in `tools/lexicon/lexicon.py`, a
tokenizer that tracks quotes and heredocs across lines. It is another kit's Python, so the linter
cannot call it (shared invariant 2), and P5 takes its idea in the smallest form the measured
population needs. The seams this unit extends are check 51's awk predicate and its declared
exempt-list pattern, which S1's helper list copies, including the stale-entry hit; rule 2's awk
block and its red fixture; and the linter's pass 1 and its `strip`. No existing seam fits the
cross-direction question of F2, recorded there.

Recall surfaced the unit 38 brief and README row first, then `TOOL-aGraftedHelix-31`'s brief asking
for check 51 as a class gate with a named exemption, `TOOL-aBoundedVerdict-15` S4, which built
rules 1 and 2 as one-line rules over a single file, the aBatchedArm-2 acceptance ledger, which
describes pass 1's brace count over stripped lines, and `TOOL-aLexedStripper-4`, an open ask about
quote state leaking across lines in the hook kit's own scanner, the same family as defect 3 in
another kit.

Recall terms used: `python tools/memory-recall/query.py "how does a per-function source rule see a write or guard that a refactor moved into a helper function" --terms "check 51 write_claim terminal phase helper function call exemption bypass guard park rule arms-groups delimiter"`
