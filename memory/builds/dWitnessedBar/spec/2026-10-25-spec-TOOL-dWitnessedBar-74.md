# TOOL-dWitnessedBar-74 — the canary's `rec_sha` byte check is seen red on every run, against a one-line variant whose `sha` value loses its CR after the read

**Status:** CLOSED · rev-3 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 40 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-74-deviation-741.md](../build/2026-10-25-build-TOOL-dWitnessedBar-74-deviation-741.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-74-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-74-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-74-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-74-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-74-widen-15.md](../build/2026-11-21-build-TOOL-dWitnessedBar-74-widen-15.md) | widen | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-74-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-74-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-74-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-74-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-74-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-74-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 |

<!-- /gen:spec-records -->


## 1. Goal

The round-1 spec audit of units 68 to 73
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md`)
confirmed finding **id 10 at HIGH**, report item **H1**. Id 24 shares that item and takes
`TOOL-dWitnessedBar-75`. Report item M1, id 2, states the same defect across units 70 and 72 at
MEDIUM, and `TOOL-dWitnessedBar-78` takes it.

`TOOL-dWitnessedBar-70` AC2 stages its byte-check red with a scratch hook whose `sha` read is
`rec_sha=$(awk ...); rec_sha=${rec_sha%$'\r'}`. Built from the hook `TOOL-dWitnessedBar-69` leaves,
that copy still holds the loop's own `_rg_v=${_rg_v%$'\r'}`. The canary's `sed` then changes two
lines, so the canary fails at its one-line count before its 41-byte comparison runs, as unit 70's
builder measured (`memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-70-1-builder-return.md`).
Neither of AC2's plants reaches that comparison, so a vacuous or off-by-one comparison would land with
AC1 and AC2 green.

This unit gives the comparison a red it reaches, on every run. A variant of the cut function differs
from it in one line, and its `sha` value loses its CR after the read. The canary's own `sed` still
changes one line of the variant, so only the byte comparison can tell the variant's mutant from the
real one. It repairs `TOOL-dWitnessedBar-70`, CLOSED at `09718851e`, and builds at order 40 after
`TOOL-dWitnessedBar-72`.

## 2. Scope (IN)

- **S1** — One comparison. The canary's test that a value is forty-one bytes whose last byte is CR
  (unit 70 S1) is the suite function `check_cr_reached <file> <record> <var>` in
  `tools/run-gates/run-gates.gov.test.sh`, defined at the suite's top level. In a `( ... )` subshell
  it sets `LC_ALL=C`, sources `<file>`, calls `read_green_file <record>`, and returns 0 only when
  `<var>`, read by name, holds forty-one bytes ending in CR. Its CR is spelled `$'\r'` in its own
  body and never inside a `$(...)`, which reads that spelling as empty on this node (§4 Evidence).
  Unit 70 landed the test inline: an `eval "$rgf_mut"` inside `$(...)` whose `case` measures
  `${#rec_sha}` against `rgf_crb`. The arm now writes the canary's mutant to a file under its scratch
  `$rgf_t`, and unit 70 S1's `rec_sha` assertion calls `check_cr_reached` on that file. No line
  outside the function's body measures `rec_sha`'s bytes. Observed by AC1.
- **S2** — The liveness variant. On every run, before unit 66 S2's assertion is counted (the
  `rec_sha` compare's count, which unit 70 S2 gates on the canary), the arm writes under `$rgf_t` a
  variant of the cut function in which the `sha` case's assignment `rec_sha=$_rg_v` reads
  `rec_sha=${_rg_v%?}`, made by `sed 's/\(sha) rec_sha=\)\$_rg_v/\1${_rg_v%?}/'`. It asserts that the
  variant differs from the cut in one line. It applies unit 70 S1's `sed 's/%[$].[\]r.}/}/'` to the
  variant and asserts that this also changes one line. It then calls `check_cr_reached` on that result for
  `rec_sha` and requires a non-zero return. Each count reads `diff` lines opening `>`, as the canary's
  does. Observed by AC1 and AC2.
- **S3** — The liveness failure is loud. When either count is not one, or `check_cr_reached` returns 0 on
  the variant's mutant, the arm prints
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (<reason>)`, sets
  `fail=1`, and does not count unit 66 S2's assertion. `<reason>` is `variant changed <n> lines`,
  `mutant changed <n> lines` or `it passed a value that lost its CR`. Like unit 70's canary, S2 gates
  a count and adds none of its own. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- The slot in unit 70 S2's failure line that tells a count failure from a byte failure, and the
  record of unit 70 AC2's breaks with the line each printed. Both are `TOOL-dWitnessedBar-75`'s.
- The `fingerprint` key's liveness, which is `TOOL-dWitnessedBar-76`'s. It extends S1's function and
  S2's check to `rec_fp` as one loop over the canary's keys. The `rec_fp` half of the canary, which
  `TOOL-dWitnessedBar-72` lands before this unit, stays as that unit leaves it.
- A staged break per condition of `check_cr_reached`, and the length and tail variants each one
  reaches, which are `TOOL-dWitnessedBar-81`'s, `TOOL-dWitnessedBar-79`'s and `TOOL-dWitnessedBar-80`'s
  at order 41. S2's one variant fails both conditions, so AC2 stages a comparison that passes every
  value (§8 F3).
- The read form, which is `TOOL-dWitnessedBar-69`'s. This unit changes nothing in `.githooks/pre-push`.
- The report's left-shift text, a checklist entry that a staged break claimed to reach an assertion
  passes every earlier one. No clause of this build names it. S2 is the regression this unit builds,
  and it runs on every bar.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-70` — the canary, its mutant `sed` and its `rec_sha` comparison, which S1 makes one function and S2 proves able to red (id 10)
- **consumes-from** `TOOL-dWitnessedBar-69` — the loop's `sha) rec_sha=$_rg_v` case assignment, which S2's variant edits; another spelling makes S3 report `variant changed 0 lines` (id 10)
- **hands-off** `TOOL-dWitnessedBar-75` — S2's `sha` variant, which its S3 stages in a scratch hook to record the `for rec_sha` failure line (ids 10 and 24)
- **hands-off** `TOOL-dWitnessedBar-76` — `check_cr_reached` and S2's liveness check, which it turns into one loop over the canary's keys with `rec_fp` beside `rec_sha` (ids 10 and 9)
- **hands-off** `TOOL-dWitnessedBar-78` — the `diff` count of each byte-arm break, recorded in unit 70's ledger to answer its New-arm claim, which names this unit's AC2 (id 2)
- **hands-off** `TOOL-dWitnessedBar-79` — `check_cr_reached`, S2's two one-line counts and S3's failure line, which unit 79 extends with a length variant that fails the count alone (id 7 of the round-1 spec audit of units 74 to 78, item H1)
- **hands-off** `TOOL-dWitnessedBar-80` — S2's `${_rg_v%?}` variant and S3's failure line, which unit 80 makes fail the tail test alone with a reason naming that condition (id 18, item H1)
- **hands-off** `TOOL-dWitnessedBar-81` — AC2 and the §7 New-arm claim, which unit 81 restates as one staged break per condition and answers in this unit's ledger (id 1, item H1)
- **hands-off** `TOOL-dWitnessedBar-84` — `check_cr_reached`'s return codes, the liveness edit's match and the ledger lines for AC1 and AC3, which unit 84 amends or answers (ids 3, 5, 6, 8, 10, 15, 19, 20 of the round-1 spec audit of units 74 to 78)

## 4. Design

### Evidence

Probed at `921f83fff` on 2026-11-21 under `uname -s` `MINGW64_NT-10.0-22621`, GNU bash 5.3.9
`x86_64-pc-cygwin`, GNU Awk 5.4.0 and GNU sed 4.9 (PINNED 2026-11-21). The probe cut HEAD's
`.githooks/pre-push#read_green_file` and read a hand-built record laid out as the AC12 arm's:
`verdict<TAB>GREEN<CR>`, `sha<TAB>` forty `a` `<LF>`, `sha<TAB>` forty `b` `<CR><LF>`,
`reused_cache` 1 then 0`<CR>`, and `fingerprint<TAB>` forty `c` `<CR><LF>`. The record is synthetic,
so the arm's run over `run_local_plant`'s record at the close is the real observation. A prototype of
S1's function sourced each mutant from a file:

- The canary's `sed` over the cut changed one line, and the prototype returned 0 on its mutant for
  `rec_sha` and for `rec_fp` (PINNED 2026-11-21, this probe).
- S2's `sed` over the cut changed one line. The canary's `sed` over that variant changed one line,
  and its mutant gave `rec_sha` 40 bytes and `rec_fp` 41 (PINNED 2026-11-21). The prototype returned 1
  on it for `rec_sha` and 0 for `rec_fp`. So the variant passes the count and reaches the byte
  comparison, and only for `rec_sha`.
- With the prototype's count read as `-ge 0` and its tail test kept, it still returned 1 on the
  variant's mutant, so rev-2's AC2 break printed no line on a correct build. With its comparison
  replaced by `true` it returned 0 (PINNED 2026-11-21, this probe), the red AC2 now stages (§8 F3).
- A hook copy one `diff` line from the hook, whose `sha` case reads `rec_sha="$_rg_v"`, gave S2's
  `sed` 0 changed lines (PINNED 2026-11-21, this probe).
- A `z=$'\r'` assigned inside `$(...)` printed nothing. The prototype's `$'\r'`, in a function body
  defined at the script's top level, told the two mutants apart when called directly and when called
  inside `$(...)` (PINNED 2026-11-21, this probe). Unit 70's builder return records the same
  `$(...)` fact, which is why the landed canary reads its CR from `rgf_crb`.
- `${_rg_v%?}` holds no `%$'`, so the canary's pattern `%[$].[\]r.}` does not match it.
- The report's skeptics reproduced unit 70 AC2's construction: a `$(awk ...)` read with its own strip
  beside the loop's changes two lines under the canary's `sed` (report ids 2, 10 and 24).
- On 2026-10-25 (PINNED), an input-path variant, `done 2>/dev/null < <(tr -d '\r' < "$1")`, changed one line and gave both
  values 40 bytes. On this node `sed` inside a process substitution lost the CR from every line,
  `fingerprint` included, and `${_x//$'\r'/}` inside a process substitution in a script file kept it.
  So a key-selective variant in the input path rests on how the platform's tools and bash treat a CR.
- At HEAD the canary's byte test is inline:
  `grep -n 'rec_sha' tools/run-gates/run-gates.gov.test.sh | grep -E 'wc -c|tail -c|[$][{]#|: -1[}]'`
  prints one line, `tools/run-gates/run-gates.gov.test.sh@921f83fff:874`, and the suite holds no
  `tail -c` (PINNED 2026-11-21). Rev-2's AC1 grep for `tail -c1` would pass over that inline copy.
- The suite counts executed assertions in `a` (`tools/run-gates/run-gates.gov.test.sh@921f83fff:243`)
  against `FLOOR_ASSERTIONS`, whose value the suite file owns. Its helpers
  `tools/run-gates/run-gates.gov.test.sh#read_derivation` and
  `tools/run-gates/run-gates.gov.test.sh#check_bar_scrub_parity` are the snake_case function shape
  S1 follows, the second with the `check` verb of `.lexicon.conf`'s VERBS table.
- `tools/run-gates/run-gates.evidence.test.sh@921f83fff:2327-2336` holds a liveness control of the
  same kind: an assertion re-run on an input where it must fire, so a check that was deleted cannot
  read as one that moved.

### Inventory

Minted: the suite function `check_cr_reached`, and S3's failure line with its three reasons. No
constant, plant, flag or tracked file; the variant and the mutants are scratch files under `$rgf_t`.
Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 40, after `TOOL-dWitnessedBar-70` (39, CLOSED at `09718851e`). Order 40 is
shared with `TOOL-dWitnessedBar-71` (CLOSED at `ced984440`), `TOOL-dWitnessedBar-72` and
`TOOL-dWitnessedBar-75`. Dispatch is strictly sequential and sorts a tie by id string
(`tools/workflows/unattended-build.js@921f83fff:78-82`, `:692-697`), so unit 72 builds before this
unit and unit 75 after it. Units 72, 74 and 75 all edit the gov suite, so they build one at a time.
Unit 72's `rec_fp` comparison is then inline, and `TOOL-dWitnessedBar-76` moves it onto S1's function
at order 41.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `memory/project/shell-role.txt`: S1 to S3 grow the suite past its row, 715 at `921f83fff` (PINNED
  2026-11-21 by `memory/project/shell-role.txt`, widened by unit 70). Unit 72 may widen it first, so
  the pass reads the row from the file. It widens that row with
  `python tools/memory-tree/ratchet.py widen shell-role`, which writes its widen record under
  `memory/builds/dWitnessedBar/build/`, declared through `--dispatch` before staging, as unit 70 did.

### Alternatives rejected

- **Stage the report's input-path break once at the close, a scratch hook reading
  `done < <(tr -d '\r' < "$1")`.** It reaches the comparison only at the close. A later edit that
  makes the comparison vacuous then lands green with nobody staging the break, the reason unit 70 §4
  rejected a close-only strip break.
- **Write the variant in the input path.** Whole-input `tr -d '\r'` loses every key's CR, so its red
  cannot show which key's comparison fired, and a key-selective filter in a process substitution
  rests on platform CR handling (§4 Evidence).
- **Restate unit 70 AC2's plant as a `sha`-only `$(awk ...)` read with no strip.** gawk's text mode
  loses the CR on Git for Windows and keeps it elsewhere, so the variant's red would depend on the
  platform.
- **Have `check_cr_reached` take the function's text and `eval` it, as the landed canary evals
  `$rgf_mut`.** `TOOL-dWitnessedBar-84` S13 grades a `<file>` that cannot be sourced, and units 75 and
  76 read S1's signature as written; the arm's `$rgf_t` already holds its scratch, so a file costs one
  write per mutant.

## 5. Production-readiness checklist

- security — no new write path. The variant and its mutants are written in the arm's scratch
  directory `$rgf_t`, which the arm removes.
- perf / scale — two `sed`, two `diff` and one sourced call in a subshell per run.
- error / empty / loading states — S3 names the three ways the liveness check fails.
- observability — S3's line names its reason, so a variant edit that no longer matches reads
  differently from a comparison that passed.
- risks — a reader rewritten so the `sha` assignment is spelled differently fails S3 with
  `variant changed 0 lines`, the prompt to update the variant with the reader.
- testing — AC1 by probe, AC2 and AC3 by scratch copy at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe applies S2's `sed` to the function cut by
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` on the built tree, then the canary's
  `sed 's/%[$].[\]r.}/}/'` to the result, each `diff` counts one changed line. The sourced result,
  called on the AC12 record, gives `printf %s "$rec_sha" | wc -c` as 40 and `rec_fp` as 41 bytes.
  `grep -c '^check_cr_reached()' tools/run-gates/run-gates.gov.test.sh` prints 1, and
  `grep -nE 'check_cr_reached +"[^"]+" +"[^"]+" +rec_sha' tools/run-gates/run-gates.gov.test.sh`
  names two lines, the canary's call and S2's.
  `grep -n 'rec_sha' tools/run-gates/run-gates.gov.test.sh | grep -E 'wc -c|tail -c|[$][{]#|: -1[}]'`
  prints nothing, where at `921f83fff` it prints line 874 (PINNED 2026-11-21).
  Red when: the variant stops at the canary's count step, or the comparison has a second copy the
  liveness check never runs.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
- **AC2** — When the arm runs over the built tree, it prints no `gov-canary: the rec_sha byte check`
  line. In a scratch clone whose suite copy has `check_cr_reached`'s comparison replaced by `true`, so
  that it returns 0 on every value it reads, the arm prints
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (it passed a value that lost its CR)`
  and exits non-zero. A copy whose count reads `-ge 0` is not this criterion's break, since S2's
  variant fails the tail test as well (§4 Evidence).
  Red when: a vacuous comparison passes with the arm green.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — In a scratch clone whose `.githooks/pre-push` spells the `sha` assignment
  `rec_sha="$_rg_v"`, the arm prints the S3 line with `variant changed 0 lines`.
  Red when: the liveness check is skipped silently when its edit matches nothing.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `memory hygiene`

`portability (shell lines only shrink)` reads the widened shell-role row and checks a count, never the
arm. The two recall legs are named because their guards name `memory/`, where the row and the widen
record sit. `run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh#derive_hold_source`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf@921f83fff:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC3 · the liveness variant of the canary's `rec_sha` comparison, run on every bar, staged red by a scratch suite whose `check_cr_reached` comparison is `true` (reaches `it passed a value that lost its CR`) and by a scratch hook whose `sha` assignment reads `rec_sha="$_rg_v"` (reaches `variant changed 0 lines`) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 70 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Where is the comparison's red observed (id 10)?** Options: (a) a liveness variant inside the
  arm, run on every bar; (b) the report's input-path break, staged once at the close; (c) both. (b)
  sees the comparison red once, so a later edit that makes it vacuous lands green, which fails AC2;
  veto 1 discards it. (c) adds a close-time copy of what (a) observes on every run, and
  `TOOL-dWitnessedBar-75` S3 already records the variant's printed line at the close. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3. It meets AC1 to AC3 and is tie-broken by fewer open questions.
  widens: none · relaxes: none
- **F3 — Which break does AC2 stage at this unit's pass (id 1 of the round-1 spec audit of units 74
  to 78)?** Rev-2 staged a count of `-ge 0`, and S2's variant, failing both conditions, leaves that
  break printing no line (§4 Evidence). Options: (a) keep the `-ge 0` break; (b) a comparison replaced
  by `true`, which passes every value; (c) a second variant that fails the count alone, built here.
  (a) is red on a correct build and fails AC2; veto 1 discards it. (c) is `TOOL-dWitnessedBar-79`'s
  length variant at order 40, a §3 Non-goal; veto 1 discards it. RESOLVED (agent, 2026-11-21,
  delegated): (b), the one survivor. It meets AC2's Red-when as written, and
  `TOOL-dWitnessedBar-81` stages the per-condition breaks once units 79 and 80 land their variants.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 68 to 73, id 10
  (HIGH, item H1, shared with id 24).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-79, TOOL-dWitnessedBar-80, TOOL-dWitnessedBar-81 and
  TOOL-dWitnessedBar-84, promoted by the round-1 spec audit of units 74 to 78; nothing else moved.
- rev-3 · 2026-11-21 · §1 to §10 · S1 to S3 · AC1 to AC3 · re-grounded over units 69 to 71 as landed,
  per 2026-11-19-prompt-TOOL-dWitnessedBar-74-reground-brief. S1 names the inline test unit 70
  landed, keeps the `<file>` signature by writing each mutant under `$rgf_t`, and spells the CR
  outside any `$(...)`. AC1's single-copy grep reads every byte measure, since the landed test holds
  no `tail -c1`. AC2 stages a comparison passing every value (§8 F3). §4 Evidence re-probes at
  HEAD. §3 names units 72, 79, 80 and 81's shares. The shell-role widen and its legs join §4 and §7.
  Citations move to `path#symbol` or blob-pinned lines.

## 10. Reuse audit

The seam is unit 70's CR-reach canary in `tools/run-gates/run-gates.gov.test.sh`, extended in place,
with the liveness control of `tools/run-gates/run-gates.evidence.test.sh@921f83fff:2327-2336` and the
broken-copy count of `tools/run-gates/run-gates.evidence.test.sh@921f83fff:2983-2985`.
`python tools/codebase-map/reuse_lookup.py "prove a byte comparison can fail by running it on a variant that loses the byte"`
ranked `read_bytes`, `fail`, `stage_or_fail`, `check_runner`, `derive_runner_verbs`, `no_row_loss`
and `print_fail` (PINNED 2026-11-21), none a liveness check over a comparison, so no existing seam
fits beyond the three named above.

Recall terms used: `python tools/memory-recall/query.py "how is a canary assertion proven able to fail on every run rather than once at the close" --terms "canary liveness variant mutant staged red byte check rec_sha rec_fp CR strip seen red failure line"`
