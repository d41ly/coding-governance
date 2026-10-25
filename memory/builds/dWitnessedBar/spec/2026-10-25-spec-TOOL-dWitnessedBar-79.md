# TOOL-dWitnessedBar-79 — the canary's liveness loop gains a length variant, so a vacuous or off-by-one byte count is seen red on every run

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 |
| [2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 74 to 78
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md`)
confirmed finding **id 7 at HIGH**, report item **H1**. Ids 1 and 18 share that item and take
`TOOL-dWitnessedBar-81` and `TOOL-dWitnessedBar-80`.

`TOOL-dWitnessedBar-74` S1's `check_cr_reached` passes a value only when it is forty-one bytes AND
its last byte is CR. Its S2 liveness variant, `${_rg_v%?}`, yields forty bytes ending in `b`, which
fails both conditions at once. A count comparison made vacuous, `-ge 0` in place of forty-one, still
rejects that value through the tail test, so the liveness check passes and no run sees the count red.
That is the hole unit 74 §1 says it closes.

This unit gives the count its own variant. For every pair of the canary's keys, the liveness loop
also edits the `<key>)` assignment to `${_rg_v:1}`, a value of forty bytes still ending in CR, which
fails the count alone. It repairs `TOOL-dWitnessedBar-74` and builds one step after it (order 41).

## 2. Scope (IN)

- **S1** — The length variant. For each `<key>:<var>` pair in `TOOL-dWitnessedBar-76`'s
  `CANARY_KEYS`, the per-key liveness loop of `tools/run-gates/run-gates.gov.test.sh` writes, beside
  the variant unit 74 S2 writes, a variant of the cut function whose `<key>)` assignment
  `<var>=$_rg_v` reads `<var>=${_rg_v:1}`. The edit is the loop's existing `<key>)` edit with the
  replacement text `${_rg_v:1}`, spelled once for every key. Observed by AC1 and AC3.
- **S2** — The variant is held to unit 74 S2's two one-line counts, and then to the byte check. The
  variant must differ from the cut in one line, and the canary's `sed 's/%[$].[\]r.}/}/'` must
  change one line of it. On that mutant `check_canary_keys` must print exactly `<var>`. Observed by
  AC1 and AC2.
- **S3** — The failure is loud and names the variant. When a count is not one, the arm prints unit
  74 S3's line for `<var>` with the reason `length variant changed <n> lines` or
  `length mutant changed <n> lines`. When the mutant passes `<var>`'s byte check, the reason is
  `the length variant passed a value one byte short`. Each sets `fail=1` and leaves unit 66 S2's
  assertion uncounted. Observed by AC2.

## 3. Non-goals (OUT)

- The tail-only variant that stands in for unit 74 S2's `${_rg_v%?}`, which is
  `TOOL-dWitnessedBar-80`'s for id 18.
- The record of unit 74 AC2's and unit 76 AC2's staged breaks with the line each printed, which is
  `TOOL-dWitnessedBar-81`'s for id 1.
- A distinct return code for a variant that could not be sourced, and a sed that admits a quoted
  assignment, which are `TOOL-dWitnessedBar-84`'s for ids 19 and 6.
- The assertion floor, which `TOOL-dWitnessedBar-82` restates after this unit lands.
- The report's left-shift text, a checklist entry that a liveness variant for a multi-condition check
  fails exactly one condition. No clause of this build names it. S1 is the regression this unit
  builds, and it runs on every bar.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-74` — `check_cr_reached`, S2's two one-line counts and S3's failure line, which S1 to S3 extend with a variant that fails the count alone (id 7)
- **consumes-from** `TOOL-dWitnessedBar-76` — `CANARY_KEYS`, `check_canary_keys` and the per-key liveness loop, inside which S1's variant runs for every key (id 7)
- **hands-off** `TOOL-dWitnessedBar-81` — the length variant and its reason, whose staged `-ge 0` red unit 81 records in the ledgers of units 74 and 76 (ids 7 and 1)
- **hands-off** `TOOL-dWitnessedBar-84` — the length variant's mutant, held to an exact return of 1 by id 19's item, and its `<key>)` edit, widened to a quoted assignment by id 6's item
- **hands-off** `TOOL-dWitnessedBar-85` — the length variant and its seen-red test, on whose success unit 85 adds one to `a` per key (id 1 of the round-1 spec audit of units 79 to 84)
- **hands-off** `TOOL-dWitnessedBar-86` — the length variant and the New-arm line's floor clause, which unit 86 stages absent and answers in this unit's ledger (id 17 of the same audit)
- **hands-off** `TOOL-dWitnessedBar-87` — the length variant's reason, which unit 87 requires 76 AC2's skip-`rec_fp` break to print (id 7 of the same audit)
- **hands-off** `TOOL-dWitnessedBar-88` — the length variant and S3's reasons, which unit 88 extends with the case where another variable is named (ids 12 and 20 of the same audit)

## 4. Design

### Evidence

Probed on this node on 2026-10-25 (GNU bash 5.3.9 `x86_64-pc-cygwin`, GNU sed 4.9), over a prototype
of unit 69 S1's loop and unit 74 §4's record, `sha<TAB>` forty `a` `<LF>`, `sha<TAB>` forty `b`
`<CR><LF>` and `fingerprint<TAB>` forty `c` `<CR><LF>`:

- `sed 's/\(sha) rec_sha=\)\$_rg_v/\1${_rg_v:1}/'` changed one line of the cut, and the canary's `sed`
  changed one line of that variant. Its mutant gave `rec_sha` 40 bytes whose last byte is `\r`, and
  `rec_fp` 41 bytes. The same edit on the `fingerprint)` arm gave `rec_fp` 40 bytes ending in `\r`
  and `rec_sha` 41.
- The `${_rg_v%?}` variant of unit 74 S2 gave `rec_sha` 40 bytes ending in `b`, failing both
  conditions, as the report's ids 1, 7 and 18 record.
- `${_rg_v:1}` holds no `%$'`, so the canary's pattern `%[$].[\]r.}` does not match the edited line.
- A comparison whose count reads `-ge 0` with its tail test kept passes a 40-byte value ending in CR,
  so the length variant's mutant returns 0 there and S3's line prints. The report's id 1 skeptic
  probed the same: real check rc=1, `-ge 0` break rc=0.
- The suite counts executed assertions in `a` (`tools/run-gates/run-gates.gov.test.sh:91`) and checks
  them against `FLOOR_ASSERTIONS` only as a minimum (`:459`).

### Inventory

Minted: the length variant's replacement text `${_rg_v:1}`, and S3's three reasons. No function,
constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 41. Order 41 holds `TOOL-dWitnessedBar-73`, `-76`, `-77`, `-80` and `-81`.
Dispatch is strictly sequential and sorts a tie by id string
(`tools/workflows/unattended-build.js:76`, `:608-613`), so units 73, 76 and 77 build before this
unit, and units 80 and 81 after it. The per-key loop S1 extends therefore exists at this pass.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **Stage a `-ge 0` break once at the close and record it.** The count is then seen red once, and a
  later edit that makes it vacuous lands green with nobody staging the break. Unit 74 §4 rejected a
  close-only break for the same reason.
- **A length variant for `rec_sha` alone.** `rec_fp`'s count would stay unobserved, and the loop
  unit 76 S3 built would hold one key's variant beside another's. One replacement text in the loop
  serves every key.
- **`${_rg_v}x` for the length half.** A value of forty-two bytes ending in `x` fails both
  conditions again, the defect this unit exists to remove.

## 5. Production-readiness checklist

- security — no new write path. The variant and its mutant are written in the suite's scratch
  directory.
- perf / scale — one more variant per key: two `sed`, two `diff` and one sourced call each.
- error / empty / loading states — S3 names the three ways the length variant fails.
- observability — S3's reason names the length variant, so its red reads apart from the tail
  variant's.
- risks — a reader rewritten so an assignment is spelled differently fails with
  `length variant changed 0 lines`, as unit 74's variant does.
- testing — AC1 and AC3 by probe and grep, AC2 by scratch clone at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe applies S1's edit for `sha` to the function cut by
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` on the built tree, then the canary's
  `sed 's/%[$].[\]r.}/}/'` to the result, each `diff` counts one changed line. The sourced mutant,
  called on the AC12 record, gives `printf %s "$rec_sha" | wc -c` as 40 with
  `printf %s "$rec_sha" | tail -c1 | od -c` showing `\r`, and `rec_fp` as 41 bytes. The same probe on
  the `fingerprint` arm gives `rec_fp` 40 bytes ending in `\r` and `rec_sha` 41.
  Red when: the variant fails the tail test too, so the count is never isolated.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
- **AC2** — When the arm runs over the built tree, it prints no `length variant` line. In a scratch
  clone whose suite copy has `check_cr_reached` compare the byte count with `-ge 0` in place of
  forty-one, the arm prints
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (the length variant passed a value one byte short)`
  and the same line for `rec_fp`, and exits non-zero.
  Red when: a vacuous count comparison passes with the arm green.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When `grep -c '_rg_v:1}' tools/run-gates/run-gates.gov.test.sh` runs on the built tree, it
  prints 1.
  Red when: the length variant is spelled once per key, so the two copies can drift.

## 7. Gates

`run-gates gov canary` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC2 · the length variant of the per-key liveness loop, run on every bar, staged red by a scratch suite whose `check_cr_reached` compares the count with `-ge 0` (defeats the length condition, reaches `the length variant passed a value one byte short` for `rec_sha` and `rec_fp`) · the floor is restated after this unit by `TOOL-dWitnessedBar-82` S1, which builds at order 43

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 74 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which value isolates the count (id 7)?** Options: (a) `${_rg_v:1}`, forty bytes ending in CR,
  the report's first variant; (b) `${_rg_v#?}`, the same value spelled as a prefix strip; (c) a
  value of forty-two bytes ending in CR, `${_rg_v}` with a byte prepended. (c) reaches the count but
  its prepend needs a second expansion whose quoting the sed replacement must carry, a second spelling
  for no added coverage. (b) holds a `#`, which a `case` pattern or a comment-stripping read of the
  suite can take for a comment. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, tie-broken by
  fewer open questions; it is the value the report's skeptic probed.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 74 to 78, id 7
  (HIGH, item H1, shared with ids 1 and 18).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-85, TOOL-dWitnessedBar-86, TOOL-dWitnessedBar-87 and
  TOOL-dWitnessedBar-88, promoted by the round-1 spec audit of units 79 to 84; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-76`'s per-key liveness loop over `CANARY_KEYS` in
`tools/run-gates/run-gates.gov.test.sh`, given one more replacement text, with the liveness control
of `tools/run-gates/run-gates.evidence.test.sh:1884-1892`.
`python tools/codebase-map/reuse_lookup.py "prove each condition of a two-condition check can fail on its own variant"`
ranked `check`, `fail`, `checks` and `check_line`, none a variant that isolates one condition of a
comparison, so no existing seam fits beyond the loop named above.

Recall terms used: `python tools/memory-recall/query.py "how is each condition of a canary byte check seen red, and who restates the assertion floor" --terms "canary liveness variant length tail CR byte check FLOOR_ASSERTIONS restated floor owner seen red"`
