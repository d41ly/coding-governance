# TOOL-dWitnessedBar-76 — the canary's `rec_fp` byte check is seen red on every run, against a variant whose `fingerprint` value alone loses its CR

**Status:** DEFERRED · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-76-deviation-761.md](../build/2026-10-25-build-TOOL-dWitnessedBar-76-deviation-761.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-76-deviation-762.md](../build/2026-10-25-build-TOOL-dWitnessedBar-76-deviation-762.md) | deviation | — |
| [2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 68 to 73
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md`)
confirmed finding **id 9 at HIGH**, report item **H2**. Id 25 shares that item and takes
`TOOL-dWitnessedBar-77`. Report item M1, id 2, states the same defect across units 70 and 72 at
MEDIUM, and `TOOL-dWitnessedBar-78` takes it.

`TOOL-dWitnessedBar-72` AC1 stages a scratch hook whose `fingerprint` read is `$(awk ...)` followed
by the strip. The canary must still read `rec_sha`, so the copy keeps `TOOL-dWitnessedBar-69`'s loop
and its strip, and the canary's `sed` changes two lines. The report's probes printed 2, and the
sourced mutant gave `rec_sha` 41 bytes and `rec_fp` 40. The canary fails at its count before it
reaches the `rec_fp` comparison, so that comparison is never seen red, and a canary that checks
`rec_sha` alone, unit 72 AC1's own Red-when, passes AC1.

This unit gives `rec_fp`'s comparison the red `TOOL-dWitnessedBar-74` gives `rec_sha`'s. The canary's
checks become one function over one list of keys, and each key's liveness variant loses only its own
key's CR, so the canary must name exactly that key. It repairs `TOOL-dWitnessedBar-72` and builds one
step after it (order 41).

## 2. Scope (IN)

- **S1** — One list of the canary's keys. `tools/run-gates/run-gates.gov.test.sh` holds the pairs
  `sha:rec_sha` and `fingerprint:rec_fp` once, as `CANARY_KEYS`. Observed by AC1.
- **S2** — One function runs the canary's checks. `check_canary_keys <file> <record>` calls
  `TOOL-dWitnessedBar-74`'s `check_cr_reached` for each variable in `CANARY_KEYS` and prints the name of
  each variable whose CR did not arrive. Unit 70 S1's canary requires empty output on its mutant.
  Unit 72 S1's `rec_fp` assertion is this call, and the suite holds no inline copy of it. Observed by
  AC1 and AC2.
- **S3** — Per-key liveness, through the same function. For each pair `<key>:<var>` in
  `CANARY_KEYS`, the arm writes a variant of the cut function whose `<key>)` assignment `<var>=$_rg_v`
  reads `<var>=${_rg_v%?}`, under `TOOL-dWitnessedBar-74` S2's two one-line counts. On that variant's
  mutant, `check_canary_keys` must print exactly `<var>`. Otherwise the arm prints
  `TOOL-dWitnessedBar-74` S3's line with `<var>` in place of `rec_sha`, and with the reason
  `it passed a value that lost its CR` when `<var>` is absent from the output or
  `it named <other> whose CR arrived` when another variable is present. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- The failure line's `rec_fp` value, and the record of unit 72 AC1's break with its printed line.
  Both are `TOOL-dWitnessedBar-77`'s.
- A pair for the five other keys `read_green_file` reads. The AC12 record plants a CR line on `sha`
  and `fingerprint` for the canary; `TOOL-dWitnessedBar-73` S9 plants every key in a second record and
  grades the values, not the canary.
- The read form, which is `TOOL-dWitnessedBar-69`'s. This unit changes nothing in `.githooks/pre-push`.
- The report's left-shift text, the checklist entries of items H1 and H2. No clause of this build
  names them. S3 is the regression this unit builds, and it runs on every bar.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-72` — S1's `rec_fp` comparison and AC1's staged break, which S2 moves onto one function and S3 makes able to red (id 9)
- **consumes-from** `TOOL-dWitnessedBar-74` — `check_cr_reached`, the `sha` liveness check and its failure line, which S2 and S3 turn into one function and one loop over the canary's keys (ids 9 and 10)
- **consumes-from** `TOOL-dWitnessedBar-69` — the loop's `fingerprint) rec_fp=$_rg_v` case assignment, which S3's `fingerprint` variant edits (id 9)
- **hands-off** `TOOL-dWitnessedBar-77` — S3's `fingerprint` variant, which it stages in a scratch hook to record the `for rec_fp` line, and `check_canary_keys`, whose output names the variables that line reports (ids 9 and 25)
- **hands-off** `TOOL-dWitnessedBar-78` — the `diff` count of unit 72's byte-arm break, recorded in its ledger to answer its New-arm claim, which names this unit's AC2 (id 2)
- **hands-off** `TOOL-dWitnessedBar-79` — `CANARY_KEYS`, `check_canary_keys` and the per-key liveness loop, inside which unit 79's length variant runs for every key (id 7 of the round-1 spec audit of units 74 to 78, item H1)
- **hands-off** `TOOL-dWitnessedBar-80` — the per-key liveness loop, whose one replacement text unit 80 makes the tail variant `${_rg_v%?}x` (id 18, item H1)
- **hands-off** `TOOL-dWitnessedBar-81` — AC2 and the §7 New-arm claim for `rec_fp`, which unit 81 answers in this unit's ledger with one staged break per condition (id 1, item H1)
- **hands-off** `TOOL-dWitnessedBar-82` — the per-key loop's assertions and the New-arm claim, which unit 82's restated floor counts and answers in this unit's ledger (id 2, item H2)
- **hands-off** `TOOL-dWitnessedBar-84` — `check_canary_keys` and the liveness loop, which unit 84 makes count the pairs they visit and return 2 on a read failure, and the ledger line for AC1 (ids 5, 6, 15, 19, 21 of the round-1 spec audit of units 74 to 78)
- **hands-off** `TOOL-dWitnessedBar-87` — AC2's skip-`rec_fp` break and its New-arm claim, which unit 87 stages after units 79 and 80 and answers in this unit's ledger (id 7 of the round-1 spec audit of units 79 to 84)
- **hands-off** `TOOL-dWitnessedBar-88` — `check_canary_keys`, S3's other-variable reason and the ledger lines for AC1 and AC3, which unit 88 gives a full return contract, records against 76 AC3's break and names by the tail variant's text (ids 3, 12 and 13 of the same audit)

## 4. Design

### Evidence

Probed on this node on 2026-10-25 (GNU bash 5.3.9 `x86_64-pc-cygwin`, GNU sed 4.9), over a prototype
of unit 69 S1's loop and the record of `TOOL-dWitnessedBar-74` §4 Evidence:

- `sed 's/\(fingerprint) rec_fp=\)\$_rg_v/\1${_rg_v%?}/'` over the cut changed one line. The canary's
  `sed` over that variant changed one line, and its mutant gave `rec_sha` 41 bytes and `rec_fp` 40.
- The `sha` variant's mutant gave `rec_sha` 40 bytes and `rec_fp` 41 (that spec's §4 Evidence). So
  each variant fails exactly its own key, which is what lets S3 tell a canary that checks one key from
  one that checks both.
- The report's verdict on id 9 records unit 72 AC1's construction: `sed` changed 2 lines and the
  sourced mutant gave `sha 41 fp 40`.

### Inventory

Minted: the list `CANARY_KEYS`, the suite function `check_canary_keys`, and the reason
`it named <other> whose CR arrived` of `TOOL-dWitnessedBar-74` S3's line. No plant, flag or file.
Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 41, after `TOOL-dWitnessedBar-72` (40) and `TOOL-dWitnessedBar-74` (40).
Order 41 is shared with `TOOL-dWitnessedBar-73` and `TOOL-dWitnessedBar-77`. Dispatch is strictly
sequential and sorts a tie by id string (`tools/workflows/unattended-build.js:608-613`), so unit 73
builds first and unit 77 after this unit.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **Stage unit 72 AC1's break as the report's scratch hook, a `fingerprint` read through
  `$(awk ...)` with no strip and its `case` label taken out of the loop.** It reaches the comparison
  only where gawk keeps the CR, which Git for Windows does not, and only at the close.
- **A second liveness check, written for `rec_fp` beside unit 74's for `rec_sha`.** Two copies of one
  check is the shape the charter's reuse rule refuses at the second instance; S3 is the loop.
- **Derive `CANARY_KEYS` from the AC12 record's CR lines.** The record also plants `reused_cache` with
  a CR (`TOOL-dWitnessedBar-68` S1), whose value is not forty bytes, so `check_cr_reached`'s comparison
  would need a per-key length the list then has to carry anyway.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — one more variant, two `sed`, two `diff` and one sourced call per run.
- error / empty / loading states — S3 names a missed key and a wrongly named key apart.
- observability — the line names the variable whose check was not seen red.
- risks — a reader rewritten so the `fingerprint` assignment is spelled differently fails with
  `variant changed 0 lines`, as unit 74's `sha` variant does.
- testing — AC1 by probe and grep, AC2 and AC3 by scratch clone at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe applies S3's `fingerprint` edit to the function cut by
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` on the built tree, then the canary's
  `sed 's/%[$].[\]r.}/}/'`, each `diff` counts one changed line, and the sourced result gives
  `printf %s "$rec_fp" | wc -c` as 40 and `rec_sha` as 41 bytes over the AC12 record.
  `grep -n 'fingerprint:rec_fp' tools/run-gates/run-gates.gov.test.sh` names the `CANARY_KEYS` line,
  and `grep -c '^check_canary_keys()' tools/run-gates/run-gates.gov.test.sh` prints 1.
  Red when: the list holds `sha:rec_sha` alone, or `rec_fp`'s comparison is an inline copy outside
  `check_canary_keys`.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
- **AC2** — When the arm runs over the built tree, it prints no `byte check was not seen red` line.
  In a scratch clone whose suite copy has `check_canary_keys` skip `rec_fp`, the arm prints
  `gov-canary: the rec_fp byte check was not seen red on its liveness variant (it passed a value that lost its CR)`
  and exits non-zero.
  Red when: a canary that checks `rec_sha` alone stays green.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — In a scratch clone whose suite copy has `check_canary_keys` print `rec_sha` whenever it
  prints `rec_fp`, the arm prints the `rec_fp` line with `it named rec_sha whose CR arrived`.
  Red when: a check that reports every key on any failure passes as key-selective.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC3 · the per-key liveness loop over `CANARY_KEYS`, staged red by a scratch suite whose `check_canary_keys` skips `rec_fp` (reaches `it passed a value that lost its CR`) and by one that reports `rec_sha` beside `rec_fp` (reaches `it named rec_sha whose CR arrived`) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 72 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — How is `rec_fp`'s comparison seen red (id 9)?** Options: (a) a per-key liveness variant
  through the canary's own check function, run on every bar; (b) the report's scratch hook with a
  strip-less `$(awk ...)` read of `fingerprint`, staged once at the close. (b) loses the CR to gawk
  on Git for Windows whatever the comparison does, and is seen once, so it fails AC2's Red-when on
  the bar's platform; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the
  one survivor, tie-broken by reuse of `TOOL-dWitnessedBar-74`'s variant.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 68 to 73, id 9
  (HIGH, item H2, shared with id 25).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-79, TOOL-dWitnessedBar-80, TOOL-dWitnessedBar-81,
  TOOL-dWitnessedBar-82 and TOOL-dWitnessedBar-84, promoted by the round-1 spec audit of units 74 to
  78; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-87 and TOOL-dWitnessedBar-88, promoted by the round-1 spec audit of
  units 79 to 84; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-74`'s `check_cr_reached` and liveness check in
`tools/run-gates/run-gates.gov.test.sh`, made one loop at its second key, with the liveness control
of `tools/run-gates/run-gates.evidence.test.sh:1884-1892`.
`python tools/codebase-map/reuse_lookup.py "prove a byte comparison can fail by running it on a variant that loses the byte"`
ranked `fail`, `stage_or_fail`, `no_row_loss` and `print_fail`, none a liveness check over a
comparison, so no existing seam fits beyond those named above.

Recall terms used: `python tools/memory-recall/query.py "how is a canary assertion proven able to fail on every run rather than once at the close" --terms "canary liveness variant mutant staged red byte check rec_sha rec_fp CR strip seen red failure line"`
