# TOOL-dWitnessedBar-80 — the liveness variant that failed both conditions becomes a tail variant, so a check that lost its last-byte test is seen red on every run

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 |
| [2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 74 to 78
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md`)
confirmed finding **id 18 at HIGH**, report item **H1**. Ids 1 and 7 share that item and take
`TOOL-dWitnessedBar-81` and `TOOL-dWitnessedBar-79`.

`TOOL-dWitnessedBar-74` S2's variant edits the `sha)` assignment to `${_rg_v%?}`, and unit 76 S3
carries the same edit to every key. On the canary's mutant that value is forty bytes ending in the
key's last data byte, so it fails the length test and the tail test together. The report's id 18
skeptic probed it with the tail test taken out of `check_cr_reached`: the variant still returned 1,
because it is also forty bytes. So no run sees the tail test red, and `${_rg_v%?}` isolates neither
condition.

This unit makes that variant fail the tail test alone. Its replacement text becomes `${_rg_v%?}x`, a
value of forty-one bytes whose last byte is `x`. With `TOOL-dWitnessedBar-79`'s length variant, each
condition of `check_cr_reached` has a variant that only it rejects. It repairs `TOOL-dWitnessedBar-74`
and builds one step after it (order 41).

## 2. Scope (IN)

- **S1** — The tail variant. In the per-key liveness loop of `tools/run-gates/run-gates.gov.test.sh`,
  the variant unit 74 S2 introduced writes each `<key>)` assignment as `<var>=${_rg_v%?}x`, in place
  of `<var>=${_rg_v%?}`. The edit is the loop's existing `<key>)` edit with that one replacement text,
  spelled once for every key, and the suite holds no `${_rg_v%?}` replacement that lacks the `x`.
  Observed by AC1 and AC3.
- **S2** — The variant is held to unit 74 S2's two one-line counts, and then to the byte check. On its
  mutant `check_canary_keys` must print exactly `<var>`. Observed by AC1 and AC2.
- **S3** — The failure names the variant and the condition. The arm prints unit 74 S3's line for
  `<var>` with the reason `tail variant changed <n> lines` or `tail mutant changed <n> lines` when a
  count is not one, and `the tail variant passed a value whose last byte is not CR` when the mutant
  passes `<var>`'s byte check. That reason stands where unit 74 S3 wrote
  `it passed a value that lost its CR`, which named no condition; unit 74 AC2's quote of it is
  answered by `TOOL-dWitnessedBar-81`. Each sets `fail=1` and leaves unit 66 S2's assertion
  uncounted. Observed by AC2.

## 3. Non-goals (OUT)

- The length variant, which is `TOOL-dWitnessedBar-79`'s for id 7.
- The record of each staged break with the line it printed, in the ledgers of units 74 and 76, which
  is `TOOL-dWitnessedBar-81`'s for id 1.
- A distinct return code for a variant that could not be sourced, and a sed that admits a quoted
  assignment, which are `TOOL-dWitnessedBar-84`'s for ids 19 and 6.
- The assertion floor, which `TOOL-dWitnessedBar-82` restates after this unit lands.
- The report's left-shift text, a checklist entry for one variant per condition, and its promotion
  into the spec template's New-arm line. No clause of this build names them. S1 is the regression
  this unit builds, and it runs on every bar.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-74` — S2's `${_rg_v%?}` variant and S3's failure line, which S1 makes fail the tail test alone and S3 gives a reason naming that condition (id 18)
- **consumes-from** `TOOL-dWitnessedBar-76` — the per-key liveness loop over `CANARY_KEYS`, whose one replacement text S1 changes for every key (id 18)
- **hands-off** `TOOL-dWitnessedBar-81` — the tail variant and its reason, whose staged red with no tail test unit 81 records in the ledgers of units 74 and 76 (ids 18 and 1)
- **hands-off** `TOOL-dWitnessedBar-84` — the tail variant's mutant, held to an exact return of 1 by id 19's item, and its `<key>)` edit, widened to a quoted assignment by id 6's item
- **hands-off** `TOOL-dWitnessedBar-85` — the tail variant and its seen-red test, on whose success unit 85 adds one to `a` per key (id 1 of the round-1 spec audit of units 79 to 84)
- **hands-off** `TOOL-dWitnessedBar-86` — the tail variant and the New-arm line's floor clause, which unit 86 stages absent and answers in this unit's ledger (id 17 of the same audit)
- **hands-off** `TOOL-dWitnessedBar-87` — S3's tail reason, which stands where 76 AC2's quoted reason stood and which unit 87 requires that break to print (id 7 of the same audit)
- **hands-off** `TOOL-dWitnessedBar-88` — S3's tail reason and S1's replacement text, whose readers unit 88 answers in the ledgers of units 80, 76 and 72 (ids 2 and 13 of the same audit)

## 4. Design

### Evidence

Probed on this node on 2026-10-25 (GNU bash 5.3.9 `x86_64-pc-cygwin`, GNU sed 4.9), over the
prototype and record of `TOOL-dWitnessedBar-79` §4 Evidence:

- `sed 's/\(sha) rec_sha=\)\$_rg_v/\1${_rg_v%?}x/'` changed one line of the cut, and the canary's
  `sed` changed one line of that variant. Its mutant gave `rec_sha` 41 bytes whose last byte is `x`,
  and `rec_fp` 41 bytes ending in `\r`. On the `fingerprint)` arm it gave `rec_fp` 41 bytes ending in
  `x` and `rec_sha` 41 ending in `\r`.
- The `${_rg_v%?}` variant gave `rec_sha` 40 bytes ending in `b` and, on the `fingerprint)` arm,
  `rec_fp` 40 bytes ending in `c`, so it fails both conditions on either key.
- The pattern `%[$].[\]r.}` needs `$` after `%`; `${_rg_v%?}x` has `?` there, so the canary's `sed`
  leaves the edited line alone.
- A `check_cr_reached` with its tail test taken out and its count kept at forty-one passes a 41-byte
  value, so the tail variant's mutant returns 0 there and S3's line prints. The length variant's
  mutant, 40 bytes, still returns 1 under that break, so it cannot stand in for this one.

### Inventory

Minted: the replacement text `${_rg_v%?}x`, and S3's three reasons. No function, constant, plant,
flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 41. Dispatch is strictly sequential and sorts a tie by id string
(`tools/workflows/unattended-build.js:608-613`), so units 73, 76, 77 and 79 build before this unit
and unit 81 after it. The loop S1 edits holds unit 74's variant and unit 79's at this pass.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **Keep `${_rg_v%?}` beside the tail variant.** It fails both conditions, so its red proves nothing
  the other two variants do not, and it costs two `sed`, two `diff` and one sourced call per key.
- **A tail variant through the input path, `tr -d '\r'` on the record.** It strips every key's CR, so
  its red cannot show which key's check fired, and unit 74 §4 found key-selective filters in a process
  substitution resting on platform CR handling.
- **A tail variant that keeps forty bytes, `${_rg_v%??}x`.** It is forty bytes ending in `x`, so it
  fails both conditions, the defect this unit exists to remove.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — none added: the loop's variant count per key is unchanged by S1.
- error / empty / loading states — S3 names the three ways the tail variant fails.
- observability — S3's reason names the tail condition, so its red reads apart from the length
  variant's.
- risks — a reader rewritten so an assignment is spelled differently fails with
  `tail variant changed 0 lines`.
- testing — AC1 and AC3 by probe and grep, AC2 by scratch clone at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe applies S1's edit for `sha` to the function cut by
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` on the built tree, then the canary's
  `sed 's/%[$].[\]r.}/}/'` to the result, each `diff` counts one changed line. The sourced mutant,
  called on the AC12 record, gives `printf %s "$rec_sha" | wc -c` as 41 with
  `printf %s "$rec_sha" | tail -c1 | od -c` showing `x`, and `rec_fp` 41 bytes ending in `\r`. The
  same probe on the `fingerprint` arm gives `rec_fp` 41 bytes ending in `x`.
  Red when: the variant is forty bytes, so it fails the count as well as the tail.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
- **AC2** — When the arm runs over the built tree, it prints no `tail variant` line. In a scratch clone
  whose suite copy has `check_cr_reached` test the count alone, with no last-byte test, the arm prints
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (the tail variant passed a value whose last byte is not CR)`
  and the same line for `rec_fp`, and exits non-zero.
  Red when: a check that lost its tail test passes with the arm green.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When `grep -c '_rg_v%?}x' tools/run-gates/run-gates.gov.test.sh` runs on the built tree it
  prints 1, and `grep -cE '_rg_v%\?\}($|[^x])' tools/run-gates/run-gates.gov.test.sh` prints 0.
  Red when: the two-condition variant is kept beside the tail variant, or the tail variant is spelled
  once per key.

## 7. Gates

`run-gates gov canary` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC2 · the tail variant of the per-key liveness loop, run on every bar, staged red by a scratch suite whose `check_cr_reached` has no last-byte test (defeats the tail condition, reaches `the tail variant passed a value whose last byte is not CR` for `rec_sha` and `rec_fp`) · the floor is restated after this unit by `TOOL-dWitnessedBar-82` S1, which builds at order 43

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 74 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Does the tail variant stand in for `${_rg_v%?}` or sit beside it (id 18)?** Options: (a) in
  its place, the report's corrected fix ("do not keep `${_rg_v%?}` as the CR-isolating variant");
  (b) beside it, three variants per key. (b) keeps a variant whose red no break can attribute to one
  condition, so a reason it prints names no condition, and AC3's Red-when holds against it; veto 1
  discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the one survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 74 to 78, id 18
  (HIGH, item H1, shared with ids 1 and 7).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-85, TOOL-dWitnessedBar-86, TOOL-dWitnessedBar-87 and
  TOOL-dWitnessedBar-88, promoted by the round-1 spec audit of units 79 to 84; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-76`'s per-key liveness loop over `CANARY_KEYS` in
`tools/run-gates/run-gates.gov.test.sh`, whose one replacement text changes, with the liveness control
of `tools/run-gates/run-gates.evidence.test.sh:1884-1892`.
`python tools/codebase-map/reuse_lookup.py "prove each condition of a two-condition check can fail on its own variant"`
ranked `check`, `fail`, `checks` and `check_line`, none a variant that isolates one condition of a
comparison, so no existing seam fits beyond the loop named above.

Recall terms used: `python tools/memory-recall/query.py "how is each condition of a canary byte check seen red, and who restates the assertion floor" --terms "canary liveness variant length tail CR byte check FLOOR_ASSERTIONS restated floor owner seen red"`
