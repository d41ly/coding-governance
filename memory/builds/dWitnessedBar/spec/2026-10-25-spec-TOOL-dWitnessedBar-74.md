# TOOL-dWitnessedBar-74 — the canary's `rec_sha` byte check is seen red on every run, against a one-line variant whose `sha` value loses its CR after the read

**Status:** DEFERRED · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 40 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
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
lines, so the canary fails at its one-line count before its 41-byte comparison runs. Neither of AC2's
plants reaches that comparison, so a vacuous or off-by-one comparison would land with AC1 and AC2
green.

This unit gives the comparison a red it reaches, on every run. A variant of the cut function differs
from it in one line, and its `sha` value loses its CR after the read. The canary's own `sed` still
changes one line of the variant, so only the byte comparison can tell the variant's mutant from the
real one. It repairs `TOOL-dWitnessedBar-70` and builds one step after it (order 40).

## 2. Scope (IN)

- **S1** — One comparison. The canary's test that a value is forty-one bytes whose last byte is CR
  (unit 70 S1) is the suite function `check_cr_reached <file> <record> <var>` in
  `tools/run-gates/run-gates.gov.test.sh`. It sources `<file>` in a subshell, calls
  `read_green_file <record>`, and returns 0 only when `<var>` holds forty-one bytes ending in CR. Unit
  70 S1's `rec_sha` assertion calls it on the canary's mutant, and the suite holds no second copy of
  the comparison. Observed by AC1.
- **S2** — The liveness variant. On every run, before unit 66 S2's assertion is counted, the arm writes
  a variant of the cut function in which the `sha` case's assignment `rec_sha=$_rg_v` reads
  `rec_sha=${_rg_v%?}`, made by `sed 's/\(sha) rec_sha=\)\$_rg_v/\1${_rg_v%?}/'`. It asserts that the
  variant differs from the cut in one line. It applies unit 70 S1's `sed 's/%[$].[\]r.}/}/'` to the
  variant and asserts that this also changes one line. It then calls `check_cr_reached` on that result for
  `rec_sha` and requires a non-zero return. Observed by AC1 and AC2.
- **S3** — The liveness failure is loud. When either count is not one, or `check_cr_reached` returns 0 on
  the variant's mutant, the arm prints
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (<reason>)`, sets
  `fail=1`, and does not count unit 66 S2's assertion. `<reason>` is `variant changed <n> lines`,
  `mutant changed <n> lines` or `it passed a value that lost its CR`. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- The slot in unit 70 S2's failure line that tells a count failure from a byte failure, and the
  record of unit 70 AC2's breaks with the line each printed. Both are `TOOL-dWitnessedBar-75`'s.
- The `fingerprint` key's liveness, which is `TOOL-dWitnessedBar-76`'s. It extends S1's function and
  S2's check to `rec_fp` as one loop over the canary's keys.
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

Probed on this node on 2026-10-25 (GNU bash 5.3.9 `x86_64-pc-cygwin`, GNU Awk 5.4.0, GNU sed 4.9),
over a prototype of unit 69 S1's loop and a record holding `sha<TAB>` forty `a` `<LF>`, `sha<TAB>`
forty `b` `<CR><LF>` and `fingerprint<TAB>` forty `c` `<CR><LF>`:

- The canary's `sed` over the cut prototype changed one line, and its mutant gave `rec_sha` 41 bytes
  and `rec_fp` 41 bytes.
- S2's `sed` over the cut changed one line. The canary's `sed` over that variant changed one line,
  and its mutant gave `rec_sha` 40 bytes and `rec_fp` 41. So the variant passes the count and
  reaches the byte comparison, and only for `rec_sha`.
- `${_rg_v%?}` holds no `%$'`, so the canary's pattern `%[$].[\]r.}` does not match it.
- The report's skeptics reproduced unit 70 AC2's construction: a `$(awk ...)` read with its own strip
  beside the loop's changes two lines under the canary's `sed` (report ids 2, 10 and 24).
- An input-path variant, `done 2>/dev/null < <(tr -d '\r' < "$1")`, changed one line and gave both
  values 40 bytes. On this node `sed` inside a process substitution lost the CR from every line,
  `fingerprint` included, and `${_x//$'\r'/}` inside a process substitution in a script file kept it.
  So a key-selective variant in the input path rests on how the platform's tools and bash treat a CR.
- The suite counts executed assertions in `a` (`tools/run-gates/run-gates.gov.test.sh:91`), and its
  helper `read_derivation` (`:167`) is the snake_case function shape S1 follows.
- `tools/run-gates/run-gates.evidence.test.sh:1884-1892` holds a liveness control of the same kind: an
  assertion re-run on an input where it must fire, so a check that was deleted cannot read as one
  that moved.

### Inventory

Minted: the suite function `check_cr_reached`, and S3's failure line with its three reasons. No constant,
plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 40, after `TOOL-dWitnessedBar-70` (39). Order 40 is shared with
`TOOL-dWitnessedBar-71`, `TOOL-dWitnessedBar-72` and `TOOL-dWitnessedBar-75`. Dispatch is strictly
sequential and sorts a tie by id string (`tools/workflows/unattended-build.js:76-80`, `:608-613`), so
units 71 and 72 build before this unit and unit 75 after it. Unit 72's `rec_fp` comparison is then
inline, and `TOOL-dWitnessedBar-76` moves it onto S1's function at order 41.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

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

## 5. Production-readiness checklist

- security — no new write path. The variant and its mutant are written in the suite's scratch
  directory.
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
  `grep -n 'tail -c1' tools/run-gates/run-gates.gov.test.sh` names lines inside `check_cr_reached` only.
  Red when: the variant stops at the canary's count step, or the comparison has a second copy the
  liveness check never runs.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
- **AC2** — When the arm runs over the built tree, it prints no `gov-canary: the rec_sha byte check`
  line. In a scratch clone whose suite copy has `check_cr_reached` compare the byte count with `-ge 0` in
  place of forty-one, the arm prints
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (it passed a value that lost its CR)`
  and exits non-zero.
  Red when: a vacuous comparison passes with the arm green.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — In a scratch clone whose `.githooks/pre-push` spells the `sha` assignment
  `rec_sha="$_rg_v"`, the arm prints the S3 line with `variant changed 0 lines`.
  Red when: the liveness check is skipped silently when its edit matches nothing.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC3 · the liveness variant of the canary's `rec_sha` comparison, run on every bar, staged red by a scratch suite whose `check_cr_reached` compares with `-ge 0` (reaches `it passed a value that lost its CR`) and by a scratch hook whose `sha` assignment reads `rec_sha="$_rg_v"` (reaches `variant changed 0 lines`) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

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

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 68 to 73, id 10
  (HIGH, item H1, shared with id 24).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-79, TOOL-dWitnessedBar-80, TOOL-dWitnessedBar-81 and
  TOOL-dWitnessedBar-84, promoted by the round-1 spec audit of units 74 to 78; nothing else moved.

## 10. Reuse audit

The seam is unit 70's CR-reach canary in `tools/run-gates/run-gates.gov.test.sh`, extended in place,
with the liveness control of `tools/run-gates/run-gates.evidence.test.sh:1884-1892` and the
broken-copy count of `:2169-2177`.
`python tools/codebase-map/reuse_lookup.py "prove a byte comparison can fail by running it on a variant that loses the byte"`
ranked `fail`, `stage_or_fail`, `no_row_loss` and `print_fail`, none a liveness check over a
comparison, so no existing seam fits beyond the three named above.

Recall terms used: `python tools/memory-recall/query.py "how is a canary assertion proven able to fail on every run rather than once at the close" --terms "canary liveness variant mutant staged red byte check rec_sha rec_fp CR strip seen red failure line"`
