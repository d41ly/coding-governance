# TOOL-dWitnessedBar-75 — the CR-reach canary's failure line names the check that failed, so a red at its line count cannot pass for a red at its byte check

**Status:** DEFERRED · rev-3 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 40 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-75-deviation-751.md](../build/2026-10-25-build-TOOL-dWitnessedBar-75-deviation-751.md) | deviation | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-75-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-75-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-75-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-75-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 68 to 73
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md`)
confirmed finding **id 24 at HIGH**, report item **H1**. Id 10 shares that item and takes
`TOOL-dWitnessedBar-74`.

`TOOL-dWitnessedBar-70` S2 prints one fixed line for every way the canary fails, and its AC2 demands
that same line for both of its staged breaks. A break that trips the one-line count and a break that
reaches the 41-byte comparison (`TOOL-dWitnessedBar-70` S1) therefore print the same bytes. AC2 passes
whichever check fired, and unit 70's ledger records its print-every-match break, which reaches the
byte check, with the same line as its count breaks.

This unit gives the line a slot naming the check that failed, keeps unit 70 AC2's prefix, and records
unit 70 AC2's strip-less break and the byte-arm break `TOOL-dWitnessedBar-74` S2 supplies, each with
the line it printed. It repairs `TOOL-dWitnessedBar-70` and closes order 40, after
`TOOL-dWitnessedBar-74` within that order.

## 2. Scope (IN)

- **S1** — The slot. Unit 70 S2's line, at one site in `tools/run-gates/run-gates.gov.test.sh`,
  reads
  `gov-canary: the planted CR never reached read_green_file on <uname -s> for <what>; the CR-strip assertion is not counted`.
  `<what>` is `count <n>` when the canary's mutant changed `<n>` lines and `<n>` is not 1. It is
  `rec_sha` when the count held and `TOOL-dWitnessedBar-74`'s `check_cr_reached`, called on the
  mutant's file for `rec_sha`, returned non-zero. It is `rec_fp` when both held and the canary's
  `rec_fp` measure (`TOOL-dWitnessedBar-72` S1) is not forty-one bytes ending in CR (§8 F3). A cut
  that finds no `read_green_file` differs from its mutant in no line, so it reads `count 0`. The text
  up to and including `on <uname -s>` is unit 70 AC2's prefix, unchanged. Observed by AC1 and AC2.
- **S2** — One emission site, one check per failure. The arm sets `<what>` in one variable,
  `rgf_what`, by testing the count, then `rec_sha`, then `rec_fp`, and naming the first that failed,
  as unit 74's liveness check names its `rgf_why`. The canary holds when `rgf_what` is empty, and
  `rgf_ok` stays the flag the `rec_sha` and `rec_fp` compares' counts read. The suite prints the line
  from one statement, with `$rgf_what` in the slot, so the line has one spelling. When the count
  fails, `check_cr_reached` is not called and the `rec_fp` measure is not compared; when `rec_sha`
  fails, the `rec_fp` measure is not compared. The measure itself runs where unit 72 put it. Unit
  74's liveness line and its gate on the `rec_sha` count are unchanged. Observed by AC1 and AC2.
- **S3** — Unit 70 AC2's staged reds are recorded with the line each printed. At the close, on a
  Windows node, the main loop stages two breaks in scratch clones: a `.githooks/pre-push` whose
  `read_green_file` lacks the line `    _rg_v=${_rg_v%$'\r'}`, and one whose `sha` case carries
  `TOOL-dWitnessedBar-74` S2's variant, `sha) rec_sha=${_rg_v%?} ;;`. Unit 70's acceptance ledger,
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-70-1-acceptance-ledger.md`,
  records each beside AC2 with its printed line, `for count 0` and `for rec_sha` respectively, and
  the `uname -s` it ran under. Observed by AC3.

## 3. Non-goals (OUT)

- One line per failing variable, through `TOOL-dWitnessedBar-76`'s `check_canary_keys`, and the
  record of unit 72 AC1's break with its printed line. Both are `TOOL-dWitnessedBar-77`'s. This unit
  names `rec_fp` only when it is the first check to fail (§8 F3).
- The liveness variant and `check_cr_reached`, which are `TOOL-dWitnessedBar-74`'s, CLOSED at
  `7c579ad47`.
- The slot's `unread` value for a read failure, which is `TOOL-dWitnessedBar-84` S13's.
- Whether unit 66 S2's own assertion still runs and prints after the canary fails, which
  `TOOL-dWitnessedBar-78` S1 states for id 1.
- Unit 70 AC2's `$(awk ...)` break, recorded in unit 70's ledger already. It reaches the count at
  `count 2` (§4 Evidence), and `TOOL-dWitnessedBar-84` S5 records that line for unit 72.
- The report's left-shift text, a checklist entry that a criterion requiring a printed line to name a
  value cites a line with a slot for it. No clause of this build names it. S2's one emission site is
  the regression this unit builds.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-70` — S2's failure line and AC2's two breaks, which S1 gives a slot and S3 records with their printed lines (id 24)
- **consumes-from** `TOOL-dWitnessedBar-74` — `check_cr_reached`, whose return decides the `rec_sha` value, and S2's `sha` variant, which S3 stages as the byte-arm break (ids 24 and 10)
- **hands-off** `TOOL-dWitnessedBar-77` — one slotted line per failing variable and the record of unit 72 AC1's break with the line it printed; the `rec_fp` value itself lands here, as the arm at HEAD already fails on it (ids 24 and 25, §8 F3)
- **hands-off** `TOOL-dWitnessedBar-78` — the strip-less break's ledger lines for unit 70 AC3 and unit 72 AC3, which quote this line beside the compare's own, and unit 72's Inventory answered with the slot (ids 1 and 17)
- **hands-off** `TOOL-dWitnessedBar-84` — the slot's `unread` value for a read failure, and the ledger lines for AC2 and AC3 kept on one physical line and cited by section label (ids 11, 16, 19 of the round-1 spec audit of units 74 to 78)

## 4. Design

### Evidence

Probed at `d3b748b94` on 2026-11-21 under `uname -s` `MINGW64_NT-10.0-22621` and GNU bash 5.3.9
`x86_64-pc-cygwin` (PINNED 2026-11-21). The probe cut `tools/run-gates/run-gates.gov.test.sh#check_cr_reached`
and the canary's own `sed`, `diff` count and `rgf_mr` measure, and read a hand-built record laid out
as the AC12 arm's: `verdict<TAB>GREEN<CR>`, two `sha` lines the second CR-ended, `reused_cache` 1
then 0`<CR>`, a CR-ended `fingerprint`. The arm's own record, from `run_local_plant`, is the main
loop's at the close. S2's test order, over copies of `.githooks/pre-push`, named (PINNED 2026-11-21,
this probe):

| Hook copy | Count | `<what>` | Liveness line (`TOOL-dWitnessedBar-74` S3) |
|---|---|---|---|
| HEAD's hook | 1 | none, the canary holds | none |
| no `    _rg_v=${_rg_v%$'\r'}` line | 0 | `count 0` | `mutant changed 0 lines` |
| `sha) rec_sha=${_rg_v%?} ;;` | 1 | `rec_sha` | `variant changed 0 lines` |
| `fingerprint) rec_fp=${_rg_v%?} ;;` | 1 | `rec_fp`, its measure `40` | none |
| unit 70 AC2's `$(awk ...)` read plus strip | 2 | `count 2` | `variant changed 0 lines` |
| no `read_green_file` at all | 0 | `count 0` | not probed |

No liveness line holds `for rec_sha`, `for rec_fp` or `for count`, so AC2's absence tests read the
canary's line alone.

- At HEAD the canary is one `&&` chain, `[ -n "$rgf_fn" ] && [ "$rgf_n" = 1 ] && check_cr_reached ... rec_sha && [ "$rgf_mr" = "41 cr" ] && rgf_ok=1`,
  then one failure statement with no slot (`tools/run-gates/run-gates.gov.test.sh@d3b748b94:891-895`).
  `grep -c 'the planted CR never reached read_green_file on' tools/run-gates/run-gates.gov.test.sh`
  prints 1 (PINNED 2026-11-21), so the line already has one site; the slot is what is missing.
- Unit 72 put the `rec_fp` compare inside that chain (`TOOL-dWitnessedBar-72` S1, `e0cf5fa91`), so a
  `fingerprint` CR that did not arrive already fails the canary before unit 77 builds, and with S1's
  first two values alone it would have nothing to print in the slot (§8 F3).
- Unit 74's liveness check names its reason through an `if`/`elif` chain setting `rgf_why`, printed
  by one statement (`tools/run-gates/run-gates.gov.test.sh@d3b748b94:901-907`), the shape S2 copies.
- The suite prints each failure with `echo "gov-canary: ..."` and sets `fail=1`, as that statement
  does.
- Unit 70's ledger beside AC2 quotes the slotless line for its `$(awk ...)`, strip-less and
  print-every-match breaks (`memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-70-1-acceptance-ledger.md`),
  the print-every-match one at a count of 1 with an 82-byte mutant.

### Inventory

Minted: the `for <what>` slot of unit 70 S2's line, with the values `count <n>`, `rec_sha` and
`rec_fp`, and the arm variable `rgf_what`. No function, constant, plant, flag or tracked file.
Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 40, after `TOOL-dWitnessedBar-70` (39, CLOSED at `09718851e`). Order 40 is
shared with `TOOL-dWitnessedBar-71` (CLOSED at `ced984440`), `TOOL-dWitnessedBar-72` (CLOSED at
`e0cf5fa91`) and `TOOL-dWitnessedBar-74` (CLOSED at `7c579ad47`). Dispatch is strictly sequential
and sorts a tie by id string (`tools/workflows/unattended-build.js@d3b748b94:78-82`, `:692-697`), so
this unit builds last of the four and alone, after unit 74, whose function and variant it reads.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `memory/project/shell-role.txt`: the suite's row reads 735 at `d3b748b94`, and `sh_hygiene.py`'s
  `measure_code_lines` measures the suite at 735 (PINNED 2026-11-21, widened by unit 74), so S2's
  chain grows it past the row. The pass reads the row from the file and widens it with
  `python tools/memory-tree/ratchet.py widen shell-role`, which writes its widen record under
  `memory/builds/dWitnessedBar/build/`, declared through `--dispatch` before staging, as unit 74 did.

### Alternatives rejected

- **A count-failure line with its own prefix.** Unit 70 AC2 grades the prefix
  `...read_green_file on ` followed by the `uname -s` value for both of its breaks, so a second prefix
  leaves AC2 unmet on the count break.
- **Keep one line and record which check fired in the ledger alone.** The ledger would then carry a
  distinction the arm never printed, so the record could not be checked against the run.
- **Keep the `&&` chain and derive `<what>` after it from the values it read.** The chain stops at
  the first failure and records none of them, so the value would be re-derived by a second copy of
  each test, the shape `TOOL-dWitnessedBar-74` S1 rules out for the byte check.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — none: the slot is a value in an existing line, and each test still runs at most once.
- error / empty / loading states — S1 names each failure mode and an empty cut, and S2 keeps a count
  failure from also reporting a byte failure it never measured.
- observability — the slot names the check, so a red record says which assertion fired.
- risks — a reader of the old line's exact text would miss the slot; AC1's grep finds the one site.
- testing — AC1 by grep, AC2 by scratch clone at the close, AC3 by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'the planted CR never reached read_green_file on' tools/run-gates/run-gates.gov.test.sh`
  runs on the built tree, it prints one line, and that line holds ` for $rgf_what;`.
  Red when: two statements print the line, so it can be spelled two ways, or the slot is typed in.
  figure: one line, PINNED by S2.
- **AC2** — When the arm runs over the built tree, it prints no line holding
  `never reached read_green_file`. In a scratch clone whose `.githooks/pre-push` lacks the line
  `    _rg_v=${_rg_v%$'\r'}`, the arm prints `gov-canary: the planted CR never reached read_green_file on `
  followed by the `uname -s` value and ` for count 0;`, and no line holding `for rec_sha` or
  `for rec_fp`. In a clone whose `sha` case reads `sha) rec_sha=${_rg_v%?} ;;`, it prints the same
  prefix with ` for rec_sha;`, and no line holding `for count` or `for rec_fp`. In a clone whose
  `fingerprint` case reads `fingerprint) rec_fp=${_rg_v%?} ;;`, it prints the prefix with
  ` for rec_fp;`, and no line holding `for count` or `for rec_sha`.
  Red when: two of the breaks print the same line.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-70*acceptance-ledger*`
  runs at the close, it prints one red record quoting `for count 0` and one quoting `for rec_sha`, each
  with a `uname -s` value beginning `MINGW` or `MSYS`, and each naming `TOOL-dWitnessedBar-75`.
  The builder's slotless AC2 line already there is not one of them.
  Red when: a staged break is recorded with no printed line, or both records quote the same line.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `memory hygiene`

`portability (shell lines only shrink)` reads the widened shell-role row and checks a count, never the
arm. The two recall legs are named because their guards name `memory/`, where the row, the widen
record and unit 70's ledger sit. `run-gates gov canary` is held unless the main loop sets
GATE_SELFTESTS at the close (`tools/run-gates/run-gates.sh#derive_hold_source`), which
`SELFTESTS_OWED_PATHS="tools/"` does (`.unattended.conf@d3b748b94:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 · the slotted failure line, staged red by a hook whose `read_green_file` holds no strip (reaches `for count 0`), by `TOOL-dWitnessedBar-74`'s `sha` variant in the hook (reaches `for rec_sha`) and by the same edit on the `fingerprint` case (reaches `for rec_fp`) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 70 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — What form does the slot take (id 24)?** Options: (a) ` for <what>` after the `uname -s` value,
  `<what>` a count or a variable name, the report's corrected fix for item H2; (b) a parenthesised
  `(<var>|no strip line to mutate)`, the corrected fix for item M2; (c) a separate count-failure line.
  (c) fails unit 70 AC2's shared prefix (§4 Alternatives rejected); veto 1 discards it. (b) cannot
  report a count of two, the shape the report's probes found. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the most feature-rich survivor, since it names every count.
  widens: none · relaxes: none
- **F3 — What does the slot name when the count and `rec_sha` hold and `rec_fp` fails?** Unit 72
  landed the `rec_fp` test inside the canary before this unit (§4 Evidence), which rev-2's §3, giving
  that value to `TOOL-dWitnessedBar-77`, did not meet. Options: (a) `rec_fp`, this unit's third value,
  §3 narrowed to unit 77's one line per variable and its record, an M2 AMEND inside the delegated
  scope; (b) the slotless line for that case until unit 77, a second spelling that fails AC1;
  (c) `rec_sha` or a count, a value whose check passed, which fails S1's definitions that AC2
  observes; (d) a separate `rec_fp` line, a second emission site that fails AC1. Veto 1 discards
  (b) to (d). RESOLVED (agent, 2026-11-21, delegated): (a), the one survivor. Unit 77's own
  re-ground settles its S1 and Inventory against it.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 68 to 73, id 24
  (HIGH, item H1, shared with id 10).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-84, promoted by the round-1 spec audit of units 74 to 78; nothing else
  moved.
- rev-3 · 2026-11-21 · §1 to §10 · S1 to S3 · AC1 to AC3 · re-grounded over units 70, 72 and 74 as
  landed, per 2026-11-19-prompt-TOOL-dWitnessedBar-75-reground-brief. S1 gains the `rec_fp` value the
  landed canary needs (§8 F3) and names an empty cut. S2 names `rgf_what`, the test order and unit 74's
  `rgf_why` shape. S3 spells both breaks and names unit 70's ledger. AC1 grades the slot variable, AC2
  adds the built-tree and `fingerprint` cases. §4 Evidence re-probes at HEAD. The shell-role widen and
  its legs join §4 and §7. Citations move to `path#symbol` or blob-pinned lines.

## 10. Reuse audit

The seam is unit 70 S2's failure line in `tools/run-gates/run-gates.gov.test.sh`, extended by a slot
in place, with `TOOL-dWitnessedBar-74` S3's `rgf_why` reason chain
(`tools/run-gates/run-gates.gov.test.sh@d3b748b94:901-907`) as the shape of S2's `rgf_what`, and the
suite's `echo "gov-canary: ..."` plus `fail=1` idiom.
`python tools/codebase-map/reuse_lookup.py "name which check failed in one failure line of a canary"`
ranked `check`, `fail`, `checks`, `check_line`, `unfenced_lines` and `check_loop` first (PINNED
2026-11-21), none a failure line naming the check that fired, so no existing seam fits beyond the
two named above.

Recall terms used: `python tools/memory-recall/query.py "how is a canary assertion proven able to fail on every run rather than once at the close" --terms "canary liveness variant mutant staged red byte check rec_sha rec_fp CR strip seen red failure line slot"`
