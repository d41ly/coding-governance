# TOOL-dWitnessedBar-80 — the liveness variant that failed both conditions becomes a tail variant, so a check that lost its last-byte test is seen red on every run

**Status:** DEFERRED · rev-3 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-80-deviation-801.md](../build/2026-10-25-build-TOOL-dWitnessedBar-80-deviation-801.md) | deviation | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-80-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-80-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-80-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-80-reground-spec-writer.md) | journal | — |
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

- **S1** — The tail variant. In the per-key liveness loop over `CANARY_KEYS` in
  `tools/run-gates/run-gates.gov.test.sh`, the variant unit 74 S2 introduced and unit 76 S3 carried
  to every key writes each `<key>)` assignment as `<var>=${_rg_v%?}x`, in place of `<var>=${_rg_v%?}`.
  The edit is the loop's one `sed` replacement text, `\1${_rg_v%?}x`, spelled once for every key
  (`tools/run-gates/run-gates.gov.test.sh@648a4d5d5:917`). The canary's header comment names the
  variant as `<var>=${_rg_v%?}` (`tools/run-gates/run-gates.gov.test.sh@648a4d5d5:845`). That
  comment is prose, outside the variant population, and is rewritten to the new text because AC3's
  whole-file grep reads it. After S1 the suite holds no `${_rg_v%?}` that lacks the `x`. Observed by
  AC1 and AC3.
- **S2** — The variant is held to unit 74 S2's two one-line counts, and then to the byte check. On its
  mutant `check_canary_keys` must print exactly `<var>`. Observed by AC1 and AC2.
- **S3** — The failure names the variant and the condition. Unit 76 S3's reason chain
  (`tools/run-gates/run-gates.gov.test.sh@648a4d5d5:925-929`) reads, for this variant,
  `tail variant changed <n> lines` or `tail mutant changed <n> lines` when a count is not one, and
  `the tail variant passed a value whose last byte is not CR` when the mutant passes `<var>`'s byte
  check. That last reason stands where unit 74 S3 wrote `it passed a value that lost its CR`, which
  named no condition. Unit 74 AC2's quote of it is answered by `TOOL-dWitnessedBar-81`, and unit 76
  AC2's by `TOOL-dWitnessedBar-87`. The chain's fourth reason, `it named <other> whose CR arrived`,
  stays as unit 76 S3 landed it. Each reason prints unit 74 S3's line for `<var>`, sets `fail=1` and
  leaves `<var>` out of `rgf_seen`, so that key's compare goes uncounted: unit 66 S2's for `rec_sha`,
  unit 67 S2's for `rec_fp`. Observed by AC2.

## 3. Non-goals (OUT)

- The length variant, which is `TOOL-dWitnessedBar-79`'s for id 7.
- The record of each staged break with the line it printed, in the ledgers of units 74 and 76, which
  is `TOOL-dWitnessedBar-81`'s for id 1.
- A distinct return code for a variant that could not be sourced, and a sed that admits a quoted
  assignment, which are `TOOL-dWitnessedBar-84`'s for ids 19 and 6.
- The other-variable reason `it named <other> whose CR arrived`, which unit 76 S3 landed and
  `TOOL-dWitnessedBar-88` S2 qualifies per variant.
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

Probed at `648a4d5d5` on 2026-11-21 under GNU bash 5.3.9 `x86_64-pc-cygwin` and GNU sed 4.9
(PINNED 2026-11-21). The probe cut the hook's `.githooks/pre-push#read_green_file`, ran the loop's
`sed` with each replacement text for each `CANARY_KEYS` pair, then the canary's
`sed 's/%[$].[\]r.}/}/'`. On each mutant it called a copy of
`tools/run-gates/run-gates.gov.test.sh#check_cr_reached`, and a copy with its last-byte test taken
out, once per pair as `check_canary_keys` does. The record was hand-built in the AC12 arm's layout;
the arm's own record, from `run_local_plant`, is the main loop's at the close.

| Text · key | Variant count | Mutant count | `rec_sha` · `rec_fp` bytes, last byte | Real check names | Count-only check names | Pin |
|---|---|---|---|---|---|---|
| `${_rg_v%?}x` · `sha` | 1 | 1 | 41 `x` · 41 `\r` | `rec_sha` | nothing | PINNED 2026-11-21 |
| `${_rg_v%?}x` · `fingerprint` | 1 | 1 | 41 `\r` · 41 `x` | `rec_fp` | nothing | PINNED 2026-11-21 |
| `${_rg_v%?}` · `sha` | 1 | 1 | 40 `b` · 41 `\r` | `rec_sha` | `rec_sha` | PINNED 2026-11-21 |
| `${_rg_v%?}` · `fingerprint` | 1 | 1 | 41 `\r` · 40 `c` | `rec_fp` | `rec_fp` | PINNED 2026-11-21 |
| the canary's mutant | — | — | — | nothing | nothing | PINNED 2026-11-21 |

So the landed variant is named under a check with no last-byte test, and no run sees that test red.
The tail variant is named only by the real check, so its key reaches S3's last reason under that
break.

- The pattern `%[$].[\]r.}` needs `$` after `%`; `${_rg_v%?}x` has `?` there, so the canary's `sed`
  leaves the edited line alone, as the mutant counts above show.
- At HEAD the loop's `sed` spells `\1${_rg_v%?}/` and the header comment `<var>=${_rg_v%?}`, and
  `grep -cE '_rg_v%\?\}($|[^x])'` over the suite prints 2 (PINNED 2026-11-21), those two lines.
  No file outside the suite spells the text or the three reasons S3 replaces (PINNED 2026-11-21,
  `git grep` over `tools/`, `help/` and `.githooks/`).
- `tools/gate-lint/sh_hygiene.py#measure_code_lines` reads the suite at 784 (PINNED 2026-11-21), the
  count on its `memory/project/shell-role.txt` row. S1 and S3 rewrite existing lines in place, so the
  count does not move and the row is not touched.

### Inventory

Minted: the replacement text `${_rg_v%?}x`, and S3's three reasons. No function, constant, plant,
flag or file. Naming cells: none apply, since no function is introduced.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 41. Its units 73 and 76 are CLOSED at `71f212ad1` and `bdc10a4df`.
Units 77, 79, 80 and 81 remain, and each edits `tools/run-gates/run-gates.gov.test.sh`, so they
build one at a time. Dispatch is strictly sequential and sorts a tie by id string
(`tools/workflows/unattended-build.js@648a4d5d5:78-82`, `:692-697`), so units 77 and 79 build before
this unit and unit 81 after it. The builder reads the loop as those passes leave it. Once unit 79
has landed, its length variant sits beside the variant S1 edits, and S1 changes only the
`${_rg_v%?}` text.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`: S1's replacement text and header comment, S3's three
  reasons. No other file: the shell-role row does not move (§4 Evidence), and no symbol is minted.

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
  `printf %s "$rec_sha" | tail -c1 | od -c` showing `x`, and `rec_fp` forty-one bytes ending in `\r`.
  The same probe on the `fingerprint` arm gives `rec_fp` forty-one bytes ending in `x`, and `rec_sha`
  forty-one ending in `\r`.
  Red when: the variant is forty bytes, so it fails the count as well as the tail.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
- **AC2** — When the arm runs over the built tree, it prints no `tail variant` line. In a scratch clone
  whose suite copy has `check_cr_reached` test the count alone, with no last-byte test, the arm prints
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (the tail variant passed a value whose last byte is not CR)`
  and the same line for `rec_fp`, and exits non-zero.
  Red when: a check that lost its tail test passes with the arm green.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When `grep -v '^[[:space:]]*#' tools/run-gates/run-gates.gov.test.sh | grep -c '_rg_v%?}x'`
  runs on the built tree it prints 1, and `grep -cE '_rg_v%\?\}($|[^x])' tools/run-gates/run-gates.gov.test.sh`
  prints 0.
  Red when: the two-condition variant is kept beside the tail variant, in code or in the header
  comment, or the tail variant is spelled once per key.

## 7. Gates

`run-gates gov canary` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh#derive_hold_source`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf@648a4d5d5:40`).

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
- rev-3 · 2026-11-21 · §2 to §10 · S1 · S3 · AC3 · re-grounded over units 74 and 76 as landed, per
  2026-11-19-prompt-TOOL-dWitnessedBar-80-reground-brief. S1 names the loop's one `sed` text and the
  header comment, the two spellings at HEAD. S3 names unit 76 AC2's quote, answered by unit 87, keeps
  unit 76's other-variable reason, and leaves each failing key out of `rgf_seen`. §3 leaves that
  reason to unit 88. AC3 counts code lines for the new text and the whole file for the old one. §4
  Evidence re-probes at HEAD; Rollout names units 77 and 79 ahead and the shared suite. Citations
  move to `path#symbol` or blob-pinned lines.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-76`'s per-key liveness loop over `CANARY_KEYS` in
`tools/run-gates/run-gates.gov.test.sh`, whose one replacement text changes, with the liveness control
of `tools/run-gates/run-gates.evidence.test.sh@648a4d5d5:2327-2336`.
`python tools/codebase-map/reuse_lookup.py "prove each condition of a two-condition check can fail on its own variant"`,
re-run at `648a4d5d5` on 2026-11-21, ranked `check`, `fail`, `checks` and `check_line` first, none a
variant that isolates one condition of a comparison, so no existing seam fits beyond the loop named
above.

Recall terms used: `python tools/memory-recall/query.py "how is each condition of a canary byte check seen red, and who restates the assertion floor" --terms "canary liveness variant length tail CR byte check FLOOR_ASSERTIONS restated floor owner seen red"`
