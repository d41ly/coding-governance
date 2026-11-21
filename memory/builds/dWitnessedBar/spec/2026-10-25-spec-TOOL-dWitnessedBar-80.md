# TOOL-dWitnessedBar-80 — the liveness variant that failed both conditions becomes a tail variant, so a check that lost its last-byte test is seen red on every run

**Status:** CLOSED · rev-4 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-80-deviation-801.md](../build/2026-10-25-build-TOOL-dWitnessedBar-80-deviation-801.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-80-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-80-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-80-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-80-1-builder-return.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-80-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-80-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-80-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-80-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-80-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-80-reground-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-80-reground2-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-80-reground2-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-80-reground2-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-80-reground2-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

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
condition of `check_cr_reached` has a variant that only it rejects; both run through unit 79's
`check_key_variant`, so the change is the tail call's arguments. It repairs `TOOL-dWitnessedBar-74`
and builds one step after it (order 41).

## 2. Scope (IN)

- **S1** — The tail variant. The per-key liveness loop over `CANARY_KEYS` in
  `tools/run-gates/run-gates.gov.test.sh` calls `tools/run-gates/run-gates.gov.test.sh#check_key_variant`
  twice per pair, the tail call first (`tools/run-gates/run-gates.gov.test.sh@08f226f3d:948`). That
  call's replacement argument `'${_rg_v%?}'` becomes `'${_rg_v%?}x'`, so the function's one `sed`
  writes each `<key>)` assignment as `<var>=${_rg_v%?}x` for every key. No line of the function's body
  changes, and the length call's `'${_rg_v:1}'` is untouched. The arm's header comment names the
  variant as `<var>=${_rg_v%?}` (`tools/run-gates/run-gates.gov.test.sh@08f226f3d:845`) and says it
  fails the count and the tail test at once (`tools/run-gates/run-gates.gov.test.sh@08f226f3d:849-850`).
  Both are prose, outside the variant population, and both are rewritten: the first to
  `<var>=${_rg_v%?}x`, because AC3's whole-file grep reads it, and the second to say the tail variant
  fails the tail test alone. After S1 the suite holds no `${_rg_v%?}` that lacks the `x`. Observed by
  AC1 and AC3.
- **S2** — The variant is held to unit 74 S2's two one-line counts, and then to the byte check, as
  `check_key_variant` holds every variant. On its mutant `check_canary_keys` must print exactly
  `<var>`. Observed by AC1 and AC2.
- **S3** — The failure names the variant and the condition. The tail call's label argument, empty at
  HEAD, becomes `tail `. The function's count reasons
  (`tools/run-gates/run-gates.gov.test.sh@08f226f3d:892-893`) then read `tail variant changed <n> lines`
  and `tail mutant changed <n> lines`, as the length call's `length ` label already makes them read.
  The call's passed-reason argument becomes `the tail variant passed a value whose last byte is not CR`,
  printed when the mutant passes `<var>`'s byte check. That reason stands where unit 74 S3 wrote
  `it passed a value that lost its CR`, which named no condition. Unit 74 AC2's quote of it is
  answered by `TOOL-dWitnessedBar-81`, and unit 76 AC2's by `TOOL-dWitnessedBar-87`. The other-lead
  argument `it named` stays, so the fourth reason, `it named <other> whose CR arrived`, stays as unit
  76 S3 landed it. Each reason prints unit 74 S3's line for `<var>`, sets `fail=1` and leaves `<var>`
  out of `rgf_seen`, as the loop does for any failed call (unit 79 S3). So that key's compare goes
  uncounted: unit 66 S2's for `rec_sha`, unit 67 S2's for `rec_fp`. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- The length variant and `check_key_variant` itself, which are `TOOL-dWitnessedBar-79`'s for id 7.
  This unit passes the function new arguments and edits no line of its body. `TOOL-dWitnessedBar-79`
  §8 F5 names that dependence in prose, with no Edges bullet.
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
- **consumes-from** `TOOL-dWitnessedBar-76` — the per-key liveness loop over `CANARY_KEYS`, whose tail call's replacement text S1 changes for every key (id 18)
- **hands-off** `TOOL-dWitnessedBar-81` — the tail variant and its reason, whose staged red with no tail test unit 81 records in the ledgers of units 74 and 76 (ids 18 and 1)
- **hands-off** `TOOL-dWitnessedBar-84` — the tail variant's mutant, held to an exact return of 1 by id 19's item, and its `<key>)` edit, widened to a quoted assignment by id 6's item
- **hands-off** `TOOL-dWitnessedBar-85` — the tail variant and its seen-red test, on whose success unit 85 adds one to `a` per key (id 1 of the round-1 spec audit of units 79 to 84)
- **hands-off** `TOOL-dWitnessedBar-86` — the tail variant and the New-arm line's floor clause, which unit 86 stages absent and answers in this unit's ledger (id 17 of the same audit)
- **hands-off** `TOOL-dWitnessedBar-87` — S3's tail reason, which stands where 76 AC2's quoted reason stood and which unit 87 requires that break to print (id 7 of the same audit)
- **hands-off** `TOOL-dWitnessedBar-88` — S3's tail reason and S1's replacement text, whose readers unit 88 answers in the ledgers of units 80, 76 and 72 (ids 2 and 13 of the same audit)

## 4. Design

### Evidence

Probed at `09179148e` on 2026-11-21 under GNU bash 5.3.9 `x86_64-pc-cygwin` and GNU sed 4.9
(PINNED 2026-11-21). The probe cut the hook's `.githooks/pre-push#read_green_file` and evaluated the
suite's `check_cr_reached`, `CANARY_KEYS`, `check_canary_keys` and `check_key_variant` as landed. It
called `check_key_variant` for each pair with S1's replacement and S3's label and passed reason, then
with the two landed replacements. It ran once with the real
`tools/run-gates/run-gates.gov.test.sh#check_cr_reached` and once with a copy whose last-byte test is
taken out. The record was hand-built in the AC12 arm's layout; the arm's own record, from
`run_local_plant`, is the main loop's at the close. A return of 0 is a variant seen red, both counts
one.

| Replacement · key | `rec_sha` · `rec_fp` bytes, last byte | Real check | Count-only check | Pin |
|---|---|---|---|---|
| `${_rg_v%?}x` · `sha` | 41 `x` · 41 `\r` | 0 | 1, S3's passed reason | PINNED 2026-11-21 |
| `${_rg_v%?}x` · `fingerprint` | 41 `\r` · 41 `x` | 0 | 1, S3's passed reason | PINNED 2026-11-21 |
| `${_rg_v%?}` · `sha` | 40 `b` · 41 `\r` | 0 | 0 | PINNED 2026-11-21 |
| `${_rg_v%?}` · `fingerprint` | 41 `\r` · 40 `c` | 0 | 0 | PINNED 2026-11-21 |
| `${_rg_v:1}` · `sha` | 40 `\r` · 41 `\r` | 0 | 0 | PINNED 2026-11-21 |
| `${_rg_v:1}` · `fingerprint` | 41 `\r` · 40 `\r` | 0 | 0 | PINNED 2026-11-21 |
| the canary's mutant, `check_canary_keys` direct | 41 `\r` · 41 `\r` | names nothing | names nothing | PINNED 2026-11-21 |

So at HEAD both landed variants are seen red by the count alone under a check with no last-byte
test, and no run sees that test red. The tail variant is caught only by the real check, so its key
reaches S3's passed reason under that break.

- The pattern `%[$].[\]r.}` needs `$` after `%`; `${_rg_v%?}x` has `?` there, so the canary's `sed`
  leaves the edited line alone, as the real-check returns above show.
- A cut whose `sha)` assignment is quoted makes the tail call, with S3's label, print
  `tail variant changed 0 lines` (PINNED 2026-11-21, same probe).
- At HEAD `grep -nE '_rg_v%\?\}($|[^x])'` over the suite prints the header comment and the tail call
  (`tools/run-gates/run-gates.gov.test.sh@08f226f3d:845`, `:948`), and `grep -n 'lost its CR'` prints
  the tail call alone. No file outside the suite spells `_rg_v%?}`, `variant changed`,
  `mutant changed` or `lost its CR` (PINNED 2026-11-21, `git grep` over `tools/`, `help/` and
  `.githooks/`).
- `tools/gate-lint/sh_hygiene.py#measure_code_lines` reads the suite at 797 (PINNED 2026-11-21), the
  count on its `memory/project/shell-role.txt` row as unit 79 widened it. S1 and S3 rewrite existing
  lines in place, and the measure counts no comment line, so the count does not move and the row is
  not touched. `memory/map/generated/symbols.json` records no line number, so no symbol moves.

### Inventory

Minted: the replacement text `${_rg_v%?}x`, the label `tail ` and S3's passed reason. No function,
constant, plant, flag or file. Naming cells: none apply, since no function is introduced.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 41. Units 73, 76, 77 and 79 are CLOSED at `71f212ad1`, `bdc10a4df`,
`7228b0a9a` and `08f226f3d`. Unit 81 remains at order 41 and also edits
`tools/run-gates/run-gates.gov.test.sh`. Dispatch is strictly sequential and sorts a tie by id
string (`tools/workflows/unattended-build.js@648a4d5d5:78-82`, `:692-697`), so unit 81 builds after
this unit and reads the tail call as S1 and S3 leave it. Unit 79's `check_key_variant` carries both
variants, so this unit edits the tail call's three arguments and the header comment, no line of the
function's body. That is the dependence `TOOL-dWitnessedBar-79` §8 F5 names in prose, with no Edges
bullet.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`: the tail call's replacement, label and passed reason, and
  the header comment's two clauses on the tail variant. No other file: the shell-role row does not
  move and the symbol map holds no line (§4 Evidence), and no symbol is minted.

### Alternatives rejected

- **Keep `${_rg_v%?}` beside the tail variant.** It fails both conditions, so its red proves nothing
  the other two variants do not, and it costs a third `check_key_variant` call per key.
- **A tail-only parameter or copy of `check_key_variant`.** The function already takes a
  replacement, label and reason per call, so the call's arguments carry the change; a copy is the
  second instance the charter's reuse rule refuses.
- **A tail variant through the input path, `tr -d '\r'` on the record.** It strips every key's CR, so
  its red cannot show which key's check fired, and unit 74 §4 found key-selective filters in a process
  substitution resting on platform CR handling.
- **A tail variant that keeps forty bytes, `${_rg_v%??}x`.** It is forty bytes ending in `x`, so it
  fails both conditions, the defect this unit exists to remove.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — none added: the loop's `check_key_variant` calls per key are unchanged by S1.
- error / empty / loading states — S3's label and passed reason name the three ways the tail variant
  fails, and the fourth reason stays unit 76's.
- observability — S3's reason names the tail condition, so its red reads apart from the length
  variant's.
- risks — a reader rewritten so an assignment is spelled differently fails with
  `tail variant changed 0 lines` (§4 Evidence).
- testing — AC1 and AC3 by probe and grep, AC2 by scratch clone at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe applies S1's edit for `sha`, `sed 's/\(sha) rec_sha=\)\$_rg_v/\1${_rg_v%?}x/'`,
  to the function cut by `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` on the built tree,
  then the canary's `sed 's/%[$].[\]r.}/}/'` to the result, each `diff` counts one changed line. The
  sourced mutant, called on the AC12 record, gives `printf %s "$rec_sha" | wc -c` as 41 (PINNED 2026-11-21) with
  `printf %s "$rec_sha" | tail -c1 | od -c` showing `x`, and `rec_fp` forty-one bytes ending in `\r`.
  The same probe on the `fingerprint` arm gives `rec_fp` forty-one bytes ending in `x`, and `rec_sha`
  forty-one ending in `\r` (§4 Evidence).
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
  and `grep -cF "'tail ' 'the tail variant passed a value whose last byte is not CR' 'it named'" tools/run-gates/run-gates.gov.test.sh`
  run on the built tree, each prints 1 (PINNED by S1 and S3), and
  `grep -cE '_rg_v%\?\}($|[^x])' tools/run-gates/run-gates.gov.test.sh` and
  `grep -c 'lost its CR' tools/run-gates/run-gates.gov.test.sh` each print 0 (PINNED by S1 and S3).
  The first grep drops comment lines, so the header comment's `<var>=${_rg_v%?}x` is not counted;
  the third reads the whole file, comment included.
  Red when: the two-condition variant is kept beside the tail variant, in code or in the header
  comment, the tail variant is spelled once per key, or the tail call keeps its empty label or unit
  74 S3's reason.

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
- rev-4 · 2026-11-21 · §1 to §10 · S1 · S3 · AC1 · AC3 · re-grounded over unit 79 as landed at
  `08f226f3d`, per 2026-11-19-prompt-TOOL-dWitnessedBar-80-reground2-brief. S1 and S3 become the tail
  call's three arguments to `check_key_variant` (replacement, label `tail `, passed reason), with the
  header comment's two clauses on the tail variant; §3 names the function as unit 79's (its §8 F5).
  AC1 spells its edit; AC3 adds the call's label and reason and the old reason's absence. §4 Evidence
  re-probes through the landed function at HEAD, with the row at 797; Rollout names unit 81 alone
  ahead.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-79`'s `tools/run-gates/run-gates.gov.test.sh#check_key_variant`,
called from `TOOL-dWitnessedBar-76`'s per-key liveness loop over `CANARY_KEYS`, whose tail call's
arguments change, with the liveness control of
`tools/run-gates/run-gates.evidence.test.sh@648a4d5d5:2327-2336`.
`python tools/codebase-map/reuse_lookup.py "prove each condition of a two-condition check can fail on its own variant"`,
re-run at `09179148e` on 2026-11-21, ranked `check`, `fail`, `checks` and `check_line` first, none a
variant that isolates one condition of a comparison, so no existing seam fits beyond the function
named above.

Recall terms used: `python tools/memory-recall/query.py "how is each condition of a canary byte check seen red, and who restates the assertion floor" --terms "canary liveness variant length tail CR byte check FLOOR_ASSERTIONS restated floor owner seen red"`
