# TOOL-dWitnessedBar-84 — the round-1 audit of units 74 to 78, 16 minors batched: single-copy checks reading what exists, a sed admitting the quoted arm, honest return codes, counted loops, one key derivation, the guide guarded, records on one line

**Status:** CLOSED · rev-5 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 44 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-83-round9-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-83-round9-fix-return.md) | research | TOOL-dWitnessedBar-83 |
| [2026-10-25-build-TOOL-dWitnessedBar-84-carry-h1-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-84-carry-h1-return.md) | research | — |
| [2026-10-25-build-TOOL-dWitnessedBar-84-deviation-841.md](../build/2026-10-25-build-TOOL-dWitnessedBar-84-deviation-841.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-84-deviation-842.md](../build/2026-10-25-build-TOOL-dWitnessedBar-84-deviation-842.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-84-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-84-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-84-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-84-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-84-widen-23.md](../build/2026-11-21-build-TOOL-dWitnessedBar-84-widen-23.md) | widen | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-83-round9-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-83-round9-fix-brief.md) | research | TOOL-dWitnessedBar-83 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-84-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-84-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-84-carry-h1-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-84-carry-h1-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-88 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-52-rename-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-52-rename-brief.md) | journal | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-62 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-84-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-84-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-84-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-84-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-84-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-84-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 74 to 78
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md`)
exited CONVERGED with 21 confirmed findings: no BLOCKER; five HIGH, ids 7, 18, 1, 2 and 14, which
`TOOL-dWitnessedBar-79`, `-80`, `-81`, `-82` and `-83` take; and 16 minors. BUILD-METHOD M4 batches
every MEDIUM and LOW into one unit, or two only where they split into disjoint write sets by M6's
clauses so that both build concurrently. §4 "Why one unit" says why these stay one. Each finding is
named by report id and is its own scope item, including where the report merged ids into one item.
The minors land on units 72 and 74 to 78, so this unit repairs no single unit. It builds at order
44, after every unit it repairs, and first of units 84, 85 and 86, which all touch the gov suite or
its records and build one at a time in that order.

| Report item | Severity | Report id | Lands on | Scope item |
|---|---|---|---|---|
| M1 | MEDIUM | 3 | unit 74 S1, AC1, §4 Rollout | S1 |
| M1 | MEDIUM | 8 | unit 74 S1, AC1 | S2 |
| M1 | MEDIUM | 20 | unit 74 S1, AC1, §4 Rollout | S3 |
| L2 | LOW | 10 | unit 74 AC1 | S4 |
| M2 | MEDIUM | 4 | unit 77 S1, S2; unit 72 AC1 | S5 |
| M3 | MEDIUM | 6 | unit 74 S2, AC3, §3; unit 76 S3 | S6 |
| M4 | MEDIUM | 15 | units 74 and 76, §4 and §7 | S7 |
| L1 | LOW | 5 | units 74 and 76, §7 | S8 |
| M5 | MEDIUM | 9 | unit 78 S6, §8 F3 | S9 |
| M6 | MEDIUM | 13 | unit 78 S7, §4 Inventory, §10 | S10 |
| M10 | MEDIUM | 22 | unit 78 S7, AC8 | S11 |
| M7 | MEDIUM | 16 | unit 75 AC3; unit 77 AC2; unit 78 AC2, AC3, AC13, AC15, AC16, AC19 | S12 |
| M8 | MEDIUM | 19 | unit 74 S1 to S3; unit 75 S1; unit 76 S2 | S13 |
| M9 | MEDIUM | 21 | unit 76 S2, S3, §5, AC1 | S14 |
| L3 | LOW | 11 | unit 75 §4; unit 77 §4 | S15 |
| L4 | LOW | 12 | unit 78 S3, S4, AC4, AC5, AC7, §10 | S16 |

That is 12 MEDIUM and 4 LOW findings by raw id. Ids 3, 8 and 20 share item M1, whose low-graded
spelling half is L2 (id 10). Id 15 (M4) and id 5 (L1) are one defect at two grades. Item M10's
left-shift folds into M6's helper, so S11 builds on S10.

## 2. Scope (IN)

- **S1** — id 3. Unit 74's acceptance ledger beside AC1 records that its no-second-copy clause is
  graded for `rec_sha`, the one key `check_cr_reached` served at unit 74's pass. It states that unit
  72's inline `rec_fp` comparison, present at that pass
  (`tools/run-gates/run-gates.gov.test.sh@7c579ad47:889-890`), is the copy
  `TOOL-dWitnessedBar-76` S2 moved, and names unit 76 AC1 and this unit's AC2 as the whole-suite
  observation. Observed by AC1.
- **S2** — id 8. The whole-suite single-copy claim is observed with no spelling fixed. A probe prints
  every line of `tools/run-gates/run-gates.gov.test.sh` outside `check_cr_reached`'s body that names
  `rec_sha` or `rec_fp` together with a byte measure: `wc -c`, `tail -c`, `od`, `cut -c`, a `${#`
  expansion or a `: -1}` slice. The body is a `( ... )` subshell, so the cut runs from its
  `check_cr_reached()` line to the first line opening `)`; a cut ending at `}` runs on through
  `check_canary_keys` (§4 Evidence). On the built tree the probe prints nothing; on a planted copy
  it prints the planted line. Observed by AC2.
- **S3** — id 20. Unit 74 AC1 is observed at unit 74's own pass commit, `7c579ad47`, with checks that
  exist at order 40. In the suite as that commit holds it, the lines calling `check_cr_reached` for
  `rec_sha` number 2 (PINNED 2026-11-21, §4 Evidence), the canary's assertion and the liveness call,
  and S2's probe restricted to `rec_sha` prints nothing. Neither check reads `CANARY_KEYS`, which unit 76 mints at order 41. Unit
  74's ledger beside AC1 records both. Observed by AC3.
- **S4** — id 10. Since unit 74 rev-3 §8 F3, no `tail -c1` grep stands for this item to answer: unit
  74 AC1 greps lines naming `rec_sha` for `wc -c`, `tail -c`, `${#` or `: -1}`. Unit 74's ledger
  beside AC1 records that this grep reads one key and four measures and misses `od` and `cut -c`, and
  names S2's probe, which reads both keys and every byte measure, as the observation of AC1's
  Red-when for a second copy in any spelling. Observed by AC4.
- **S5** — id 4. Unit 72's ledger beside AC1 records that its `$(awk ...)`-plus-strip break prints
  `for count 2` by design, under `TOOL-dWitnessedBar-75` S1 and `TOOL-dWitnessedBar-77` S1, and that
  `TOOL-dWitnessedBar-76` S3's `fingerprint` variants are AC1's byte-arm red, recorded by unit 77 S2
  and `TOOL-dWitnessedBar-81`. At the close the main loop stages that break and the ledger quotes the
  line it printed. Observed by AC5.
- **S6** — id 6. The liveness edit's `<key>)` match admits the quoted assignment. The match is the
  one `sed` in `tools/run-gates/run-gates.gov.test.sh#check_key_variant`, so the tail and length
  variants both take it: `\(<key>) <var>=\)"\{0,1\}\$_rg_v"\{0,1\}`, so both `<var>=$_rg_v` and
  `<var>="$_rg_v"` are edited, and the replacement is written unquoted. An arm split across two
  lines still matches nothing and prints the `tail variant changed 0 lines` and
  `length variant changed 0 lines` reasons of `TOOL-dWitnessedBar-79` and `TOOL-dWitnessedBar-80`.
  Unit 74's ledger beside AC3 records that its quoted-spelling red is superseded by this item.
  Observed by AC6.
- **S7** — id 15. The symbol tier already holds `check_cr_reached` and `check_canary_keys`: units 74
  and 76 each ran `python tools/codebase-map/gen_map.py --write` at their passes, `7c579ad47` and
  `bdc10a4df`, so this unit renders nothing. The ledgers of units 74 and 76 beside AC1 each name the
  key, the commit that rendered it and this unit. Observed by AC7.
- **S8** — id 5. This unit's §7 names `codebase-map coverage + freshness`, the unguarded leg the two
  minted functions move, with `recall floor` and `recall floor arms` for the paths under `memory/`.
  The ledgers of units 74 and 76 beside AC1 name that leg as the one the close ran for their
  functions. Observed by AC8.
- **S9** — id 9. The `run-gates gov canary` row's `guard` in `tools/govkit/registry.toml` gains
  `memory/guides/MERGE-BAR.md`, and `python tools/run-gates/leg_factory.py --write` renders it into
  `tools/gate-legs.json`, which is never hand-edited. The suite tests the guide at
  `tools/run-gates/run-gates.gov.test.sh@fe6302db3:437` and greps it at `:456` to `:469`, and
  govkit's guard taxonomy puts the entry in its `memory-root-relative` class. The entry reaches four
  DEFERRED specs that name the guide under Files touched: `TOOL-dBoundRoles-25`,
  `PLAY-dConvergedCharter-1`, `PLAY-dConvergedCharter-7` and `PLAY-dConvergedCharter-19`. This unit
  files one ask row for each in that spec's build `BACKLOG.md`, under the next free id of that build's
  family, each naming the token `run-gates gov canary <- memory/guides/MERGE-BAR.md` with a `SEV`
  disposition line, in the shape of unit 78 S9's `PLAY-dConvergedCharter-42`. `TOOL-dFairHearing-40`
  names the guide in prose only and is outside the population. The charter half is §8 F2's: one ask
  row in `memory/builds/dWitnessedBar/BACKLOG.md` under the next free id. Observed by AC9.
- **S10** — id 13. One case-label derivation. The suite derives each reader's keys twice today, as
  `rgf_pairs` (`tools/run-gates/run-gates.gov.test.sh@fe6302db3:977`) for `TOOL-dWitnessedBar-73`
  S9's arm and `rbf_pairs` (`:994`) for `TOOL-dWitnessedBar-78` S7's, one anchored `sed` with its
  prefix changed. The suite defines the private helper `_derive_case_keys <cut-file> <prefix>`, which
  prints one `<key> <var>` line per `<label>) <prefix><name>=` assignment in the cut, every one on a
  line and not only the first. Both arms call it, one with `rec_` and one with `bg_`, and neither
  keeps a derivation of its own. Each keeps its pairs file, so no `while` loop reads a here-string fed
  by a substitution. Unit 78's ledger beside AC8 names the helper as the seam its §10 claimed.
  Observed by AC10.
- **S11** — id 22. The derivation is counted. `_derive_case_keys` compares the number of lines it
  prints with an independent count of `<label>) <prefix>` assignments in the cut. On a difference it
  prints a line naming the cut and both numbers on stderr and returns 1. Each caller's existing
  assertion requires a return of 0, so both inherit the check and `a` gains nothing from it. Unit 78
  AC8's derived list then holds as many keys as `read_bar_file` assigns, derived and never typed.
  Observed by AC11.
- **S12** — id 16. Records on one line. The ledger answers to unit 75 AC3, unit 77 AC2 and unit 78
  AC2, AC3, AC13, AC15, AC16 and AC19 each carry every backticked token their criterion's grep needs
  on the bullet's first physical line, however long, and wrap only prose after it, as
  `memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md` records. Observed by AC12.
- **S13** — id 19. A read failure is not a red. `check_cr_reached` unsets `read_green_file` in its
  subshell, then returns 2 when `<file>` cannot be sourced, when `read_green_file` is not defined
  after sourcing, or when `<record>` is not a regular file; 1 only after the value was measured and
  failed; 0 when it passed. `check_canary_keys` prints a variable only when its call returned 1, and
  returns 2 when any call returned 2. `check_key_variant` (`TOOL-dWitnessedBar-79` S1), on a 2 from
  its `check_canary_keys` call, prints the reason `<label>variant could not be sourced or read (rc 2)`
  after its two count reasons and before its others, so `TOOL-dWitnessedBar-74` S3's line ends
  `(tail variant could not be sourced or read (rc 2))`. On a 2 the canary prints
  `TOOL-dWitnessedBar-75` S1's line once, with `<what>` set to `unread`, never a variable name.
  Observed by AC13.
- **S14** — id 21. Loops that count what they visit. `check_canary_keys` and the liveness loop each
  count the `CANARY_KEYS` pairs they visit. Each fails with
  `gov-canary: the <canary|liveness loop> visited <n> of <m> CANARY_KEYS pairs` unless `<n>` equals
  `<m>` and `<m>` is at least 2, where `<m>` is the number of words in `${CANARY_KEYS[*]}`. Every
  `check_canary_keys` call runs inside a `$(...)` (`tools/run-gates/run-gates.gov.test.sh@fe6302db3:895`
  and `:939`), so its check prints that line on stderr, which `tools/run-gates/run-gates.sh#runleg`
  captures with stdout, and returns 2 (§8 F4). The liveness loop's check runs at the top level after
  the loop. Each check adds one to `a` at the top level, the canary's beside its one
  `check_canary_keys` call and the loop's after the loop. Since this unit adds arms after
  `TOOL-dWitnessedBar-82`'s restatement, its builder restates `FLOOR_ASSERTIONS` absolutely by unit
  82 S1's rule: the floor read from the file plus these two checks, the only increments this unit
  adds. Its `# RAISED <old> -> <new> by TOOL-dWitnessedBar-84` comment goes on the line below the
  constant, above unit 82's. The line above the constant is left as it stands, the derived owner's
  line, which `TOOL-dWitnessedBar-83` S1 gives to `TOOL-dWitnessedBar-90`. Observed by AC14 and AC17.
- **S15** — id 11. Citations by section label. Unit 75 rev-3 and unit 77 rev-4 re-grounded their §4
  onto section labels, 70 S2, 72 S1, 72 §4 Inventory, 72 §5 observability and 72 AC1, and neither
  spec cites a line of unit 70's or unit 72's spec (§4 Evidence). The ledgers of unit 75 beside AC2
  and unit 77 beside AC1 record that and name the revision that closed it. Observed by AC15.
- **S16** — id 12. Unit 78's guard probes are observed through the shipped query. Unit 78's ledger
  beside AC4, AC5 and AC7 records the output of `python tools/check-spec-tokens.py --legs-for`, whose
  `print_legs_for` joins a path to a leg's guard through
  `tools/memory-tree/design_lib.py#check_guard_trips`, the runner's literal rule, and names that
  query as the seam unit 78 §10 omitted. Observed by AC16.

## 3. Non-goals (OUT)

- Rewording the spec text of units 72 and 74 to 78. Each item is closed by what this pass builds or
  observes, and a claim or criterion it answers is answered in that unit's acceptance ledger by name,
  as `TOOL-dWitnessedBar-78` §3 does for units 68 to 73.
- The gov canary's guard entry for the charter, `AGENTS.md`. §8 F2 says why it waits and S9 files the
  ask that carries it.
- The left-shift gates the report names: the checklist entries, a pre-commit map check over `*.sh`, a
  gate leg deriving a held suite's `$ROOT` reads, a hygiene check resolving sibling-spec citations,
  and the template's physical-line rule. No clause of this build names them. S2's probe, S11's count
  and S14's visited counts are the regressions this batch builds.
- The floor after unit 78, which `TOOL-dWitnessedBar-82` restated, and the derived owner's line
  above the constant, which `TOOL-dWitnessedBar-83` S1 gives to `TOOL-dWitnessedBar-90`. S14
  restates the floor only for the arms this unit adds.
- A visited failure's own return code and the canary's `unread` line on it, which are
  `TOOL-dWitnessedBar-89` S4's at order 46. S14 returns 2 until then (§8 F4).
- `TOOL-dWitnessedBar-28`'s gov-canary arm. Unit 28 is not built: it waits on three dOrderedCharter
  changes (asks `TOOL-dWitnessedBar-101` to `-103`) and this run defers it, so S14's count leaves
  its arm out, and the floor for it waits with unit 28.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-69` — S1's `<key>)` case arm in `read_green_file`, whose quoted spelling S6's edit admits (id 6)
- **consumes-from** `TOOL-dWitnessedBar-72` — AC1's `$(awk ...)` break and its ledger line, which S5 records as a count failure by design (id 4)
- **consumes-from** `TOOL-dWitnessedBar-73` — S9's every-key arm, which S10's helper serves and S11's count checks (ids 13 and 22)
- **consumes-from** `TOOL-dWitnessedBar-74` — `check_cr_reached`, its liveness check and its ledger lines for AC1 and AC3, which S1 to S4, S6 to S8 and S13 answer or amend (ids 3, 5, 6, 8, 10, 15, 19, 20)
- **consumes-from** `TOOL-dWitnessedBar-75` — the slot of the canary's failure line and its ledger lines for AC2 and AC3, which S12, S13 and S15 extend or answer (ids 11, 16, 19)
- **consumes-from** `TOOL-dWitnessedBar-76` — `CANARY_KEYS`, `check_canary_keys` and the per-key liveness loop, which S6, S7, S8, S13 and S14 amend or answer (ids 5, 6, 15, 19, 21)
- **consumes-from** `TOOL-dWitnessedBar-77` — S1's one line per value of `rgf_whats` and its ledger lines for AC1 and AC2, which S5, S12, S13 and S15 answer or extend (ids 4, 11, 16, 19)
- **consumes-from** `TOOL-dWitnessedBar-78` — S6's guard row, S7's derived planting, AC8 and the guard probes of S3, S4 and AC7, which S9 to S12 and S16 widen, count or answer (ids 9, 12, 13, 16, 22)
- **consumes-from** `TOOL-dWitnessedBar-79` — `check_key_variant` and the length variant, held to an exact return by S13 and edited through S6's match (ids 6 and 19)
- **consumes-from** `TOOL-dWitnessedBar-80` — the tail variant, held to an exact return by S13 and edited through S6's match (ids 6 and 19)
- **consumes-from** `TOOL-dWitnessedBar-82` — the restatement rule and its comment below the constant, which S14 applies for the arms this unit adds (id 21)
- **consumes-from** `TOOL-dWitnessedBar-83` — the derived owner, `TOOL-dWitnessedBar-90`, whose line above the constant S14 leaves alone (id 21)
- **hands-off** `TOOL-dWitnessedBar-85` — S14's restated floor and its visited counts, which unit 85 counts and restates after (id 1 of the round-1 spec audit of units 79 to 84)
- **hands-off** `TOOL-dWitnessedBar-88` — S2's probe, S6's match, S7's map record, S9's guard, S13's return codes, S14's restatement and AC3, AC10, AC16 and AC17, which unit 88 widens, counts or answers (ids 3, 4, 5, 9, 11, 14, 15, 18, 19 and 21 of the same audit)
- **hands-off** `TOOL-dWitnessedBar-89` — S13's return codes and S14's visited counts with their increments, which unit 89 pins against 87's break, gives return code 3 on stderr and places once per loop (ids 2, 6, 7 and 16 of the round-1 spec audit of units 85 to 88)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. The suite half, S2, S6, S10,
S11, S13 and S14, writes `tools/run-gates/run-gates.gov.test.sh`. S9 writes the registry row and
renders `tools/gate-legs.json`, which the suite reads as its manifest, M6 clause 2. The ledger items
write acceptance records the suite half's AC runs feed. No split leaves two disjoint write sets, and
dispatch is strictly sequential, a shared order included
(`tools/workflows/unattended-build.js@fe6302db3:78`), so a split would buy no concurrency. One unit
holds all 16 findings, as `TOOL-dWitnessedBar-78` §4 held its 20.

### Evidence

Read at `fe6302db3` on 2026-11-21 under GNU bash 5.3.9 `x86_64-pc-cygwin` and GNU sed 4.9 (PINNED
2026-11-21), unless a line names another commit.

- `memory/map/generated/symbols.json` lists `check_cr_reached`, `check_canary_keys` and
  `check_key_variant` once each, added at `7c579ad47`, `bdc10a4df` and `08f226f3d`, and
  `python tools/codebase-map/gen_map.py --check` exits 0 (PINNED 2026-11-21).
  `tools/codebase-map/map_extractors.py#scan_shell_layer` skips a name opening with `_` as private,
  so S10's helper adds no symbol-tier key. `.githooks/pre-commit` runs no map check, and the leg
  `codebase-map coverage + freshness` carries no guard, so it runs on every bar.
- The suite sets `BAR_GUIDE` to the guide at `tools/run-gates/run-gates.gov.test.sh@fe6302db3:435`,
  tests it at `:437` and greps it at `:456`, `:460`, `:465` and `:469`. The gov canary's guard is
  `["{prefix}/", "{prefix}/run-gates/", "{prefix}/gate-legs.json", ".githooks/pre-push"]`
  (`tools/govkit/registry.toml@fe6302db3:836`), rendered by `tools/run-gates/leg_factory.py`.
  `--legs-for memory/guides/MERGE-BAR.md` printed no leg, and `--legs-for AGENTS.md` printed only
  `policy fixtures <- AGENTS.md` (PINNED 2026-11-21).
- `tools/govkit/govkit.py#selfcheck` (check 7c) classes each guard pathspec into exactly one class. A
  path under `memory/` is `memory-root-relative`. `AGENTS.md` is `exempt`, through the
  `[[exempt]]` row `path = "AGENTS.md"` (`tools/govkit/registry.toml@fe6302db3:376`, by
  `TOOL-dGroundRules-79`), so no new class is owed for it; `derive_root_confs` derives five confs,
  none the charter (PINNED 2026-11-21).
- Live specs naming `AGENTS.md` under Files touched and dated on or after
  `SPEC_GUARD_LEGS_CUTOFF="2026-09-22"` (`.memory-tree.conf@fe6302db3:356`): `TOOL-aScoutedSeam-1`
  (SPECCED) alone, whose leg line lacks `run-gates gov canary` (PINNED 2026-11-21). No live spec names
  the guide under Files touched. The DEFERRED ones are `TOOL-dBoundRoles-25`,
  `PLAY-dConvergedCharter-1`, `PLAY-dConvergedCharter-7` and `PLAY-dConvergedCharter-19`;
  `TOOL-dFairHearing-23` and `PLAY-dOrderedCharter-3`, rev-4's population, are CLOSED (PINNED
  2026-11-21). `LIVE` (`tools/check-spec-tokens.py@fe6302db3:616`) excludes DEFERRED and CLOSED.
- `memory/builds/aScoutedSeam/` holds no `BACKLOG.md`, and the build README allows outside writes
  only as an ask row in another build's `BACKLOG.md`. Unit 78 S9 filed `PLAY-dConvergedCharter-42`
  in `memory/builds/dConvergedCharter/BACKLOG.md` at `253e21771`, under that build's family.
- `tools/check-spec-tokens.py#print_legs_for` resolves each guard through `resolve_prefix_token`
  against `derive_legs_path`'s tool root and joins through `derive_tripped_legs`. On 2026-11-21
  `--legs-for .githooks/pre-push` printed `run-gates gov canary <- .githooks/pre-push [selftests/repo]`
  and `--legs-for tools/hooks/kit.toml` printed `run-gates gov canary <- tools/ [selftests/repo] broad`.
- `sed 's/\(sha) rec_sha=\)"\{0,1\}\$_rg_v"\{0,1\}/\1${_rg_v%?}x/'` changed one line of the cut
  `.githooks/pre-push#read_green_file` and of a copy whose arm reads `rec_sha="$_rg_v"`, writing
  `sha) rec_sha=${_rg_v%?}x ;;`; the `${_rg_v:1}` replacement did the same (PINNED 2026-11-21).
- `.githooks/pre-push#read_green_file` returns 0 on an absent file, and
  `tools/run-gates/run-gates.gov.test.sh#check_cr_reached` returns 1 when `. "$1"` fails, so today an
  unread value fails as a measured one. The suite defines `read_green_file` only inside `$(...)`
  and `bash -c`, never at its top level.
- `.githooks/pre-push#read_bar_file` holds one `case` arm per line since unit 78 S7. Its cut gives
  16 assignments (PINNED 2026-11-21) both to the anchored `sed` at `:994` and to
  `grep -oE '[a-z_]+\) bg_[a-z_]+='`, and `read_green_file`'s gives 7 (PINNED 2026-11-21) both ways.
  A cut whose line holds two arms is where a first-label rule and the count part.
- At `7c579ad47`, `grep -c 'check_cr_reached .*rec_sha'` prints 2 (PINNED 2026-11-21). S2's probe cut at
  the first `)` line prints nothing for `rec_sha` and prints `:890`, unit 72's inline `rec_fp`
  measure, for `rec_fp`; cut at `}` it prints nothing for either. At `fe6302db3` both cuts print
  nothing, and a planted `[ "$(printf %s "$rec_fp" | wc -c)" -eq 41 ]` at the file's end prints
  (PINNED 2026-11-21).
- `FLOOR_ASSERTIONS=74` sits at `tools/run-gates/run-gates.gov.test.sh@fe6302db3:246` with unit 82's
  `# RAISED 72 -> 74` comment on the line below and `TOOL-aShardedFloor-2`'s comment above (PINNED
  2026-11-21).
- `grep -cE '7[02]\.md:[0-9]'` prints 0 (PINNED 2026-11-21) over the specs of unit 75 (rev-3) and
  unit 77 (rev-4), which cite units 70 and 72 by section label.

### Inventory

Minted: the private suite helper `_derive_case_keys` and its count line; S13's return code 2, its
slot value `unread` and its reason; S14's two visited-count lines; the restated `FLOOR_ASSERTIONS`
and its comment; the `memory/guides/MERGE-BAR.md` guard entry; and S9's five ask rows, each under
the next free id of its build's family, DERIVED at the pass. No plant, flag or file. Naming cells:
`_derive_case_keys` under `sh.function`, which
`python tools/lexicon/lexicon.py --suggest _derive_case_keys --as sh.function` read as OK on
2026-11-21, leading with the declared verb `derive`.

### Migration

None: no stored data changes. S9 widens when one leg runs and narrows nothing.

### Rollout

Live at landing, at order 44, the first of units 84, 85 and 86, after every unit it consumes from,
each CLOSED. S1, S3 to S5, S7, S8, S10, S12, S15 and S16 are answered in other units' ledgers at the
close.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `tools/govkit/registry.toml`: S9's guard entry, in the `run-gates gov canary` row.
- `tools/gate-legs.json`: rendered by `python tools/run-gates/leg_factory.py --write`.
- `memory/project/shell-role.txt`: the suite grows past its row, read from the file, and the builder
  widens it with `python tools/memory-tree/ratchet.py widen shell-role`, as unit 78 did.
- `memory/builds/dBoundRoles/BACKLOG.md`
- `memory/builds/dConvergedCharter/BACKLOG.md`
- `memory/builds/dWitnessedBar/BACKLOG.md`
- `memory/builds/dWitnessedBar/build/`: the ledgers this unit answers in, its own ledger, and the
  widen record.

### Alternatives rejected

- **Two batches, suite half and the rest.** §4 "Why one unit".
- **Add the case-arm spelling to unit 69's built text through a grep criterion (id 6's first
  option).** This unit builds at order 44, after units 74, 76, 79 and 80 have run the edit, so a
  criterion here cannot prevent the stall it guards against; §8 F3.
- **Count against `CANARY_KEYS` for unit 74's single-copy check.** Unit 76 mints it at order 41, so
  it does not exist at unit 74's pass, the report's id 20 correction.
- **Rewrite unit 78's probes as new probes of this unit.** They are unit 78's acceptance; S16 records
  them through the shipped query in that unit's ledger rather than adding a second set.

## 5. Production-readiness checklist

- security — no new write path. S9 writes only ask rows outside this build, as the build README
  allows.
- perf / scale — S14 adds two counts per run; S11 one count per derivation; S9 runs the gov canary on
  a guide-only change once GATE_SELFTESTS is set.
- error / empty / loading states — S13 names a read failure apart from a failed check; S14 names an
  empty or partly visited list; S11 names a derivation that missed an arm.
- observability — S13's `unread` slot and reason, S14's visited counts and S11's two numbers each say
  which population fell short.
- risks — S2's probe can print a legitimate measure of a key's value outside the function; its
  Red-when is a planted copy, and a builder who finds such a line routes it through
  `check_cr_reached`.
- testing — AC2, AC6, AC10, AC11, AC13, AC14 and AC16 by probe, fixture or scratch clone; the rest by
  ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'AC1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-74*acceptance-ledger*`
  runs at the close, one printed line names `rec_sha`, `TOOL-dWitnessedBar-76` AC1 and
  `TOOL-dWitnessedBar-84`.
  Red when: unit 74 AC1 is recorded against unit 72's inline copy, or green on a claim it did not
  scope.
  permission: the ledger is written at the close.
- **AC2** — When
  `awk '/^check_cr_reached\(\)/,/^\)/{next} /rec_(sha|fp)/ && /wc -c|tail -c|od |cut -c|\$\{#|: -1\}/' tools/run-gates/run-gates.gov.test.sh`
  runs on the built tree, it prints nothing. Over a scratch copy holding the planted line
  `[ "$(printf %s "$rec_fp" | wc -c)" -eq 41 ]` outside the function, it prints that line.
  Red when: a second copy of the comparison stands outside `check_cr_reached` with the probe silent.
  fixture: a scratch copy under `%TEMP%/<short-name>`.
- **AC3** — When the first line of
  `git log --reverse --format='%H %s' -- tools/run-gates/run-gates.gov.test.sh | grep 'TOOL-dWitnessedBar-74'`
  names unit 74's pass commit, `7c579ad47`, `git show <sha>:tools/run-gates/run-gates.gov.test.sh | grep -c 'check_cr_reached .*rec_sha'`
  prints 2, and AC2's probe over that blob, with `rec_(sha|fp)` read as `rec_sha`, prints nothing.
  Unit 74's ledger line for AC1 quotes both results.
  Red when: unit 74 AC1 is graded against `CANARY_KEYS`, which its pass did not hold.
  permission: the ledger is written at the close.
- **AC4** — When `grep -n 'cut -c' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-74*acceptance-ledger*`
  runs at the close, it prints a line naming this unit's AC2.
  Red when: unit 74 AC1's no-second-copy Red-when rests on a grep of one key and four measures.
  permission: the ledger is written at the close.
- **AC5** — In a scratch clone whose `.githooks/pre-push` reads `fingerprint` through
  `$(awk -F'\t' '$1=="fingerprint"{print $2}' "$1")` followed by the strip, as unit 72 AC1 stages it,
  the arm prints a line holding `for count 2` and none holding `for rec_fp`. When
  `grep -n 'AC1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-72*acceptance-ledger*` runs,
  one printed line holds `for count 2` and `TOOL-dWitnessedBar-84`.
  Red when: unit 72 AC1 stands demanding a `rec_fp` line from a break that fails at the count.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC6** — In a scratch clone whose `.githooks/pre-push` spells the `sha` arm `rec_sha="$_rg_v"`, the
  arm prints no line holding `variant changed 0 lines` and no `byte check was not seen red` line. In
  one whose `sha)` arm is split across two lines, it prints a line holding
  `length variant changed 0 lines`.
  Red when: a quoted assignment stalls the liveness loop, or an unmatched arm is skipped silently.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC7** — When `grep -c '"id": "check_cr_reached"' memory/map/generated/symbols.json` and the same
  grep for `check_canary_keys` run on the built tree, each prints 1, and
  `python tools/codebase-map/gen_map.py --check` exits 0.
  Red when: a function minted in the suite leaves the symbol tier stale.
- **AC8** — When `grep -n 'codebase-map coverage' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-7[46]*acceptance-ledger*`
  runs at the close, it prints one line in each ledger naming `TOOL-dWitnessedBar-84`.
  Red when: a unit minting a shell function closes green on a gate list that omits the leg its
  function moves.
  permission: the ledgers are written at the close.
- **AC9** — When `python tools/check-spec-tokens.py --legs-for memory/guides/MERGE-BAR.md` runs on the
  built tree, it prints a line holding `run-gates gov canary <- memory/guides/MERGE-BAR.md`, and
  `python tools/run-gates/leg_factory.py --check` exits 0. When
  `set -- memory/guides/MERGE-BAR.md ; grep -n "run-gates gov canary <- $1" memory/builds/dBoundRoles/BACKLOG.md memory/builds/dConvergedCharter/BACKLOG.md`
  runs, it prints ask rows naming `TOOL-dBoundRoles-25`, `PLAY-dConvergedCharter-1`,
  `PLAY-dConvergedCharter-7` and `PLAY-dConvergedCharter-19`, and
  `grep -n 'AGENTS.md' memory/builds/dWitnessedBar/BACKLOG.md` prints the charter half's ask row.
  Red when: a guide-only change leaves the gov canary unselected, or the wider guard lands with no ask
  row for a spec it reaches.
- **AC10** — When `grep -c '^_derive_case_keys()' tools/run-gates/run-gates.gov.test.sh` runs on the
  built tree it prints 1, and `grep -c '_derive_case_keys "' tools/run-gates/run-gates.gov.test.sh`
  prints 2, one call passing `rec_` and one `bg_`.
  Red when: the two arms keep two derivations, so the next rule change has two copies to keep in
  step.
- **AC11** — When a probe sources `_derive_case_keys` and runs it with `bg_` on the function cut by
  `awk '/^read_bar_file\(\)/,/^}/' .githooks/pre-push`, it prints as many lines as
  `grep -oE '[a-z_]+\) bg_[a-z_]+=' <cut> | wc -l` counts, and returns 0. Over a scratch copy of that
  cut whose `tree)` and `kind)` arms share one line, the built helper still prints the full count,
  and a scratch helper reading only the first label of each line returns 1 naming the cut and both
  numbers.
  Red when: a derivation misses an arm that shares a line with another, with the arm green.
  figure: the count is DERIVED from the cut at observation time; it read 16 at `fe6302db3` (PINNED
  2026-11-21).
- **AC12** — When each of the eight greps that unit 75 AC3, unit 77 AC2 and unit 78 AC2, AC3, AC13,
  AC15, AC16 and AC19 name runs at the close, every line it prints carries every token its criterion
  requires. `grep -n 'AC12' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-84*acceptance-ledger*`
  prints one line naming the eight.
  Red when: a correct record wraps a required token onto a continuation line and reads red.
  permission: the ledgers are written at the close.
- **AC13** — When a probe sources the suite's `check_cr_reached` and calls it with a `<file>` that
  does not exist, with a `<file>` that defines no `read_green_file`, and with a `<record>` that does
  not exist, it returns 2 each time, and on the length variant's mutant over the AC12 record it
  returns 1. In a scratch clone whose `check_key_variant` passes `check_canary_keys` a path it never
  wrote, the arm prints a line holding `could not be sourced or read (rc 2)`.
  Red when: a read failure counts as the byte check seen red, or prints as `for rec_sha`.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
- **AC14** — In a scratch clone whose suite copy holds an empty `CANARY_KEYS`, the arm prints
  `gov-canary: the canary visited 0 of 0 CANARY_KEYS pairs` and exits non-zero. In one whose two loops
  each stop after the list's first pair, it prints a line holding `the canary visited 1 of 2` and one
  holding `the liveness loop visited 1 of 2`.
  Red when: an emptied or mis-iterated list reads as coverage.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC15** — When `grep -cE '7[02]\.md:[0-9]'` runs over the specs of units 75 and 77 it prints 0 for
  each, and `grep -n 'TOOL-dWitnessedBar-84' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-7[57]*acceptance-ledger*`
  prints a line in each ledger naming `70 S2` or `72 S1`.
  Red when: a reader following unit 75's or unit 77's evidence lands on the wrong text, with no
  section-label citation recorded.
  permission: the ledgers are written at the close.
- **AC16** — When `python tools/check-spec-tokens.py --legs-for .githooks/pre-push` runs on the built
  tree it prints a line holding `run-gates gov canary <- .githooks/pre-push`, and
  `--legs-for tools/hooks/kit.toml` prints one holding `run-gates gov canary <- tools/` and no
  `UNEVALUATED run-gates gov canary` line. In a scratch clone whose manifest lacks the hook entry,
  and in one spelling it `{prefix}/.githooks/pre-push`, `--legs-for .githooks/pre-push` prints no
  `run-gates gov canary` line. Unit 78's ledger lines for AC4, AC5 and AC7 each name `--legs-for`.
  Red when: unit 78's guard is observed through a second copy of the join.
  fixture: scratch clones under `%TEMP%/<short-name>`.
- **AC17** — In a scratch clone checked out at this unit's pass commit, the arm prints
  `PASS (<n> assertions)` with `<n>` equal to the `FLOOR_ASSERTIONS` value there.
  `grep -A1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | tail -1` names
  `TOOL-dWitnessedBar-84`, and `grep -B1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | head -1`
  prints the line it printed at `fe6302db3`.
  Red when: the arms this unit adds sit above the floor and can be deleted with the canary green.
  figure: both numbers are DERIVED at observation time.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `codebase-map coverage + freshness` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `gate-leg conformance` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `portability (shell lines only shrink)` · `ratchet (never gains)` · `recall floor` · `recall floor arms` · `policy fixtures` · `memory hygiene`

`run-gates canary`, `run-gates gov canary`, `measure-legs selftest` and `policy fixtures` are owed
for `tools/gate-legs.json`; `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`,
`policy fixtures` and `recall floor arms` for `tools/govkit/registry.toml`; `recall floor` and
`recall floor arms` for the paths under `memory/`. `codebase-map coverage + freshness` is S7's and
S8's and has no guard. `govkit selfcheck` grades S9's entry's class, `gate-leg conformance` the
rendered manifest, and `spec tokens (a spec's own names resolve)` reads S9's entry in its guards
join. `lexicon naming predicates` grades S10's helper name, and `portability (shell lines only
shrink)` with `ratchet (never gains)` the widened shell-role row. The held legs run only when the
main loop sets GATE_SELFTESTS at the close (`tools/run-gates/run-gates.sh#derive_hold_source`), which
`SELFTESTS_OWED_PATHS="tools/"` does (`.unattended.conf@fe6302db3:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC11 AC13 AC14 AC17 · the case-key count, the read-failure return and the two visited counts, staged red by a helper reading one label per line over a cut with two arms on a line (reaches the cut and both numbers), by a variant path never written (reaches `could not be sourced or read (rc 2)`), by an empty `CANARY_KEYS` (reaches `visited 0 of 0`) and by loops that stop after the first pair (reach `visited 1 of 2`) · FLOOR_ASSERTIONS restated absolutely by S14 for this unit's two checks; the derived owner is `TOOL-dWitnessedBar-90` by `TOOL-dWitnessedBar-83` S1

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. Units 72 to 78 are
  themselves derived and carry no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which guard entries close the gov canary's unguarded reads of the charter and the merge-bar
  guide (id 9)?** Options: (a) `memory/guides/MERGE-BAR.md` and `AGENTS.md`, the report's corrected
  fix; (b) `memory/guides/MERGE-BAR.md` now, with the charter entry filed as an ask that names its
  precondition; (c) a glob spelling of the charter that govkit's classes and the spec-tokens join do
  not read. Rev-4's class precondition for (a) is gone, since the `[[exempt]]` row classes
  `AGENTS.md` (§4 Evidence). (a): the spec-tokens join would then owe `run-gates gov canary` on
  `TOOL-aScoutedSeam-1`, a live spec of another build that this run may not edit and whose build
  holds no `BACKLOG.md`; the bar's `spec tokens` leg would red at the close until a waiver row relaxed
  it, which widens a gate beyond this unit's tier; veto 3 discards it. (c): the reuse slice compares a
  guard literally (`tools/run-gates/run-gates.sh#build_input_keys`), so a glob moves no reuse key and a stale green is carried forward, which fails S9's Red-when; veto 1 discards
  it. RESOLVED (agent, 2026-10-25, delegated): (b), rung 3, the one survivor; its follow-up is the ask
  row S9 files, whose precondition is `TOOL-aScoutedSeam-1` naming the leg or closing. Re-checked at
  `fe6302db3` on 2026-11-21, per 2026-11-19-prompt-TOOL-dWitnessedBar-84-reground-brief.
  widens: none · relaxes: none
- **F3 — Where is the case-arm spelling the liveness edit consumes fixed (id 6)?** Options: (a) a grep
  criterion on unit 69's built text, through this unit; (b) the edit derived from the cut's `<key>)`
  arm, admitting the quoted assignment. (a) is observed at order 44, after units 74, 76, 79 and 80 have
  already run the edit at orders 40 and 41, so it cannot keep their passes from stalling, which fails
  AC6's Red-when; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (b), rung 3, the one
  survivor.
  widens: none · relaxes: none
- **F4 — Where does `check_canary_keys`'s visited failure report, given that every call of it runs
  inside a `$(...)` at HEAD (id 21)?** Forced by the re-ground: a line it printed on stdout would be
  read as variable names, and an `a` or `fail` it set would be lost in the subshell. Options: (a) the
  line on stderr and return 2, the one non-measure code S13 defines, with the `a` increment at the
  top-level call site; (b) the line on stderr and a return of 3; (c) return 1 with no variable
  printed. (c) leaves the canary's `rgf_whats` empty, so it reads as a pass, which fails AC14's
  Red-when; veto 1 discards it. (b) is `TOOL-dWitnessedBar-89` S4 at order 46, a §3 Non-goal here;
  veto 1 discards it. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, the one survivor. The
  canary prints its `unread` line beside the visited line until unit 89 gives the failure its code.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 74 to 78: 12
  MEDIUM and 4 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-85 and TOOL-dWitnessedBar-88, promoted by the round-1 spec audit of
  units 79 to 84; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-89, the minors batch of the round-1 spec audit of units 85 to 88;
  nothing else moved.
  The H1 is shortened to fit the build index's row cap; nothing else moved.
- rev-4 · 2026-11-19 · §7 · the leg line gains `policy fixtures`, whose manifest guard holds the §4 path
  `tools/gate-legs.json`, per brief 2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief; nothing else
  moved.
- rev-5 · 2026-11-21 · §1 · S2 · S4 · S6 · S7 · S9 to S11 · S13 to S16 · §3 · §4 · AC2 · AC3 · AC4 · AC9 · AC11 · AC13 · AC15 · AC17 · §7 · §8 · §10 · re-grounded at `fe6302db3` per 2026-11-19-prompt-TOOL-dWitnessedBar-84-reground-brief. S2's cut ends at the `)` closing `check_cr_reached`. S4 answers unit 74 rev-3's grep. S7 renders nothing. S9 edits the registry row and renders the manifest, its population re-derived to four DEFERRED specs. S10 and S11 extract the two landed derivations, now 16 keys (PINNED 2026-11-21). S13 and S14 fit `check_key_variant` and the `$(...)` calls (§8 F4). S14's comment goes below the constant, the owner unit 90. S15 is answered by units 75's and 77's re-grounds. §3 names unit 28's and unit 89's shares; the §7 legs follow Files touched.

## 10. Reuse audit

Each item extends the seam its finding names. S6 widens the existing `<key>)` edit in
`tools/run-gates/run-gates.gov.test.sh#check_key_variant`. S7 rests on the map's own renderer,
`tools/codebase-map/gen_map.py`, which units 74 and 76 ran. S9 adds an entry to the existing
registry row, rendered by `tools/run-gates/leg_factory.py` and classed by govkit's existing
`memory-root-relative` rule, and files ask rows as `TOOL-dWitnessedBar-78` S9 does. S10 extracts the
derivation units 73 and 78 each landed into one private helper at its second instance. S13 and S14
extend `check_cr_reached`, `check_canary_keys` and `check_key_variant`. S16 reuses
`tools/check-spec-tokens.py#print_legs_for` and `tools/memory-tree/design_lib.py#check_guard_trips`.
S14's restatement follows `TOOL-dWitnessedBar-82` S1's rule.
`python tools/codebase-map/reuse_lookup.py "derive the keys a shell case statement assigns from its labels"`
ranked `key`, `keys`, `run_selftest_cases` and `derive_tool_root` on 2026-11-21 (PINNED), none a
reader of a shell `case`, so no existing seam fits beyond those named above.

Recall terms used: `python tools/memory-recall/query.py "how is each condition of a canary byte check seen red, and who restates the assertion floor" --terms "canary liveness variant length tail CR byte check FLOOR_ASSERTIONS restated floor owner seen red"`
