# TOOL-dWitnessedBar-76 — the canary's `rec_fp` byte check is seen red on every run, against a variant whose `fingerprint` value alone loses its CR

**Status:** DEFERRED · rev-4 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-76-deviation-761.md](../build/2026-10-25-build-TOOL-dWitnessedBar-76-deviation-761.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-76-deviation-762.md](../build/2026-10-25-build-TOOL-dWitnessedBar-76-deviation-762.md) | deviation | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-76-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-76-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-76-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-76-reground-spec-writer.md) | journal | — |
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
sourced mutant gave `rec_sha` 41 bytes and `rec_fp` 40 (id 9). The canary fails at its count before
it reaches the `rec_fp` comparison, so that comparison is never seen red, and a canary that checks
`rec_sha` alone, unit 72 AC1's own Red-when, passes AC1.

This unit gives `rec_fp`'s comparison the red `TOOL-dWitnessedBar-74` gives `rec_sha`'s. The canary's
checks become one function over one list of keys, and each key's liveness variant loses only its own
key's CR, so the canary must name exactly that key. It repairs `TOOL-dWitnessedBar-72` and builds one
step after it (order 41).

## 2. Scope (IN)

- **S1** — One list of the canary's keys. `tools/run-gates/run-gates.gov.test.sh` holds the pairs
  `sha:rec_sha` and `fingerprint:rec_fp` once, in that order, as `CANARY_KEYS`. Observed by AC1.
- **S2** — One function runs the canary's checks. `check_canary_keys <file> <record>`, defined at the
  suite's top level, calls `TOOL-dWitnessedBar-74`'s `check_cr_reached` once for each variable in
  `CANARY_KEYS`, in the list's order, and prints, one per line, each variable whose CR did not
  arrive. It spells no CR of its own, so a call inside `$(...)` measures what a direct call does
  (§4 Evidence). The canary calls it once on its mutant's file, `$rgf_t/cut-mut.sh`, and holds only
  when it prints nothing. That call replaces the canary's `check_cr_reached ... rec_sha` call and the
  inline `rgf_mr` measure of `rec_fp` that unit 72 S1 landed; `rgf_crb`, which only `rgf_mr` reads,
  goes with it. When the count held, `TOOL-dWitnessedBar-75`'s `rgf_what` is the first variable the
  call prints, so the canary's line names `rec_sha` before `rec_fp`, as before (§8 F3). No line
  outside `check_cr_reached`'s body measures `rec_fp`'s bytes. Observed by AC1 and AC2.
- **S3** — Per-key liveness, through the same function. Unit 74 S2's `sha` variant becomes one loop
  over `CANARY_KEYS`. For each pair `<key>:<var>` the arm writes under `$rgf_t` a variant of the cut
  whose `<key>)` assignment `<var>=$_rg_v` reads `<var>=${_rg_v%?}`, from one `sed` whose replacement
  text the loop spells once, and keeps unit 74 S2's two one-line counts, the second over the canary's
  `sed 's/%[$].[\]r.}/}/'`. On that variant's mutant, `check_canary_keys` must print exactly `<var>`.
  Otherwise the arm prints
  `gov-canary: the <var> byte check was not seen red on its liveness variant (<reason>)` and sets
  `fail=1`. `<reason>` names the first of these to fail: `variant changed <n> lines`,
  `mutant changed <n> lines`, `it passed a value that lost its CR` when `<var>` is absent from the
  output, and `it named <other> whose CR arrived` when the output holds another variable, `<other>`
  being those variables space-separated. A key that fails leaves its own compare uncounted: unit 66
  S2's for `rec_sha`, as unit 74 S3 does, and unit 67 S2's for `rec_fp`, which HEAD gates on `rgf_ok`
  alone. The loop gates counts and adds none. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- The failure line's `rec_fp` value, one line per failing variable, and the record of unit 72 AC1's
  break with its printed line. All are `TOOL-dWitnessedBar-77`'s.
- `check_canary_keys`'s return codes, `TOOL-dWitnessedBar-88` S3's with `TOOL-dWitnessedBar-84` S13's
  read-failure value, and the count of pairs each loop visits, `TOOL-dWitnessedBar-84` S14's. This
  unit fixes the function's output alone.
- A pair for the five other keys `read_green_file` reads (`manifest_blob`, `manifest`, `selftests`,
  `reused`, `reused_cache`). The AC12 record plants a CR line on `sha` and `fingerprint` for the
  canary; `TOOL-dWitnessedBar-73` S9 plants every key in a second record and grades the values, not
  the canary.
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

`TOOL-dWitnessedBar-75`'s `rgf_what`, which S2 feeds, is named in prose and carries no edge (§8 F4).

## 4. Design

### Evidence

Probed at `d3b748b94` on 2026-11-21 under GNU bash 5.3.9 `x86_64-pc-cygwin` and GNU sed 4.9
(PINNED 2026-11-21). The probe cut `tools/run-gates/run-gates.gov.test.sh#check_cr_reached` and the
hook's `read_green_file`, defined a prototype of S2's function over S1's two pairs, and read a
hand-built record laid out as the AC12 arm's: `verdict<TAB>GREEN<CR>`, two `sha` lines the second
CR-ended, `reused_cache` 1 then 0`<CR>`, a CR-ended `fingerprint`. The arm's own record, from
`run_local_plant`, is the main loop's at the close. Each call ran inside `$(...)` (PINNED 2026-11-21,
this probe):

| File | Variant count | Mutant count | `rec_sha` · `rec_fp` bytes | `check_canary_keys` printed | Pin |
|---|---|---|---|---|---|
| the canary's mutant | — | 1 | — | nothing | PINNED 2026-11-21 |
| `sha` variant's mutant | 1 | 1 | 40 · 41 | `rec_sha` | PINNED 2026-11-21 |
| `fingerprint` variant's mutant | 1 | 1 | 41 · 40 | `rec_fp` | PINNED 2026-11-21 |

So each variant fails exactly its own key, which is what lets S3 tell a canary that checks one key
from one that checks both. The variant `sed` was spelled
`sed 's/\('"$k) $v"'=\)\$_rg_v/\1${_rg_v%?}/'`, `k` and `v` the pair's halves, and changed the line
`fingerprint) rec_fp=${_rg_v%?} ;;` for `fingerprint`.

- At HEAD the canary is one `&&` chain whose `rec_sha` test is `check_cr_reached` on
  `$rgf_t/cut-mut.sh` and whose `rec_fp` test is `rgf_mr`, an `eval` inside `$(...)` measured against
  `rgf_crb` (`tools/run-gates/run-gates.gov.test.sh@d3b748b94:884-893`). Unit 74's liveness check
  is one `sha` variant written to `cut-var.sh` and `cut-var-mut.sh`, its `if`/`elif` chain setting
  `rgf_why`, and only the `rec_sha` compare's count reads `rgf_live`
  (`tools/run-gates/run-gates.gov.test.sh@d3b748b94:896-911`).
- `grep -n 'rec_fp' tools/run-gates/run-gates.gov.test.sh | grep -E 'wc -c|tail -c|[$][{]#|: -1[}]'`
  prints line 890 (PINNED 2026-11-21), the `rgf_mr` measure, and `rgf_crb` appears on two lines
  (PINNED 2026-11-21), its set and that measure.
- Unit 74's builder return records `check_cr_reached` returning 0 on the canary's mutant and 1 on the
  variant's (DERIVED from that builder's probe), called directly or inside `$(...)`
  (`memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-74-1-builder-return.md`).
- The hook's loop reads seven keys (`.githooks/pre-push#read_green_file`), so five sit outside
  S1's list.
- The report's verdict on id 9 records unit 72 AC1's construction: `sed` changed 2 lines and the
  sourced mutant gave `sha 41 fp 40` (DERIVED from id 9's verdict).

### Inventory

Minted: the list `CANARY_KEYS`, the suite function `check_canary_keys`, and the reason
`it named <other> whose CR arrived` of `TOOL-dWitnessedBar-74` S3's line. No plant, flag or file.
Naming cells: `check_canary_keys` opens with `check`, a VERBS entry of `.lexicon.conf`; it nests no
helper.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 41, after `TOOL-dWitnessedBar-72` and `TOOL-dWitnessedBar-74` (order 40,
CLOSED at `e0cf5fa91` and `7c579ad47`) and `TOOL-dWitnessedBar-75`, order 40's last unit, whose
`rgf_what` chain S2 changes. Order 41 is shared with `TOOL-dWitnessedBar-73`, `-77`, `-79`, `-80`
and `-81`. Dispatch is strictly sequential and sorts a tie by id string
(`tools/workflows/unattended-build.js@d3b748b94:78-82`, `:692-697`), so unit 73 builds first and
edits this suite too, and units 77, 79, 80 and 81, which consume this unit, build after it. The
builder reads the canary as units 73 and 75 leave it.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`: S1's list, S2's function and call, S3's loop.
- `memory/project/shell-role.txt`: the suite's row reads 735 at `d3b748b94` (PINNED 2026-11-21), and
  `sh_hygiene.py`'s `measure_code_lines` measures the suite at 735 (PINNED 2026-11-21). Unit 75 widens the row before
  this unit, so the pass reads it from the file; when S1 to S3 grow the suite past it, it widens it
  with `python tools/memory-tree/ratchet.py widen shell-role --key tools/run-gates/run-gates.gov.test.sh --unit TOOL-dWitnessedBar-76`,
  which writes its widen record under `memory/builds/dWitnessedBar/build/`, as unit 74 did.
- `memory/map/generated/symbols.json`: the codebase map's generator, run with `--write`, adds
  `check_canary_keys`, as unit 74's commit added `check_cr_reached`.

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
- perf / scale — one more variant with its two `sed` and two `diff`; `check_canary_keys` sources its
  file once per key, so the canary and the loop source six times a run where HEAD sources three.
- error / empty / loading states — S3 names a missed key and a wrongly named key apart.
- observability — the line names the variable whose check was not seen red.
- risks — a reader rewritten so a key's assignment is spelled differently fails with
  `variant changed 0 lines`, as unit 74's `sha` variant does.
- testing — AC1 by probe and grep, AC2 and AC3 by scratch clone at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe applies S3's `fingerprint` edit to the function cut by
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` on the built tree, then the canary's
  `sed 's/%[$].[\]r.}/}/'`, each `diff` counts one changed line, and the sourced result gives
  `printf %s "$rec_fp" | wc -c` as 40 and `rec_sha` as 41 bytes over the AC12 record (PINNED 2026-11-21, §4 Evidence).
  `grep -n 'fingerprint:rec_fp' tools/run-gates/run-gates.gov.test.sh` names the `CANARY_KEYS` line,
  and `grep -c '^check_canary_keys()' tools/run-gates/run-gates.gov.test.sh` prints 1 (PINNED by S2).
  `grep -n 'rec_fp' tools/run-gates/run-gates.gov.test.sh | grep -E 'wc -c|tail -c|[$][{]#|: -1[}]'`
  prints nothing, where at `d3b748b94` it prints line 890 (PINNED 2026-11-21).
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

`run-gates gov canary` · `portability (shell lines only shrink)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene`

`portability (shell lines only shrink)` reads the widened shell-role row and checks a count, never the
arm. `codebase-map coverage + freshness` grades the regenerated `symbols.json`. The two recall legs are
named because their guards name `memory/`, where the row, the widen record and the map sit.
`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh#derive_hold_source`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf@d3b748b94:40`).

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
- **F3 — What does `TOOL-dWitnessedBar-75`'s `rgf_what` read once the canary is one
  `check_canary_keys` call?** Unit 75 S2 tests `rec_sha` through `check_cr_reached` and then the
  `rgf_mr` measure, which S2 here removes, and that re-ground postdates this spec's rev-3. Options:
  (a) the first variable the call prints, so unit 75's line and its AC2 cases read as before, and
  unit 75's "`rec_fp` is not compared after `rec_sha` fails" becomes measured but not named;
  (b) a `check_canary_keys` that stops at its first failure, which leaves S3's exact-output test unable
  to catch a check that names every key, AC3's break; (c) keep `rgf_mr` beside the call, the inline
  copy AC1's Red-when forbids. Veto 1 discards (b) and (c). RESOLVED (agent, 2026-11-21, delegated):
  (a), the one survivor; unit 77 prints one line per variable after it.
  widens: none · relaxes: none
- **F4 — Does S2's change to unit 75's chain carry an Edges bullet?** Memory hygiene check 12 reds a
  **consumes-from** edge whose target declares no **hands-off** back, and unit 75's spec, re-grounded
  in parallel, declares none and is outside this brief. Options: (a) name the dependence in §3 prose,
  §4 Rollout and F3, with no bullet; (b) add the bullet, which reds check 12 until unit 75 mirrors it.
  (b) fails this brief's acceptance; veto 1 discards it. RESOLVED (agent, 2026-11-21, delegated): (a),
  the one survivor; the dispatcher may add the pair to both specs in one commit.
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
- rev-4 · 2026-11-21 · §2 to §10 · S1 to S3 · AC1 · re-grounded over units 72 and 74 as landed and
  unit 75 as re-grounded, per 2026-11-19-prompt-TOOL-dWitnessedBar-76-reground-brief. S2 names the
  calls, `rgf_mr` and `rgf_crb` it replaces and `rgf_what`'s input (§8 F3, F4). S3 spells the loop's
  reason order and gates `rec_fp`'s count on its own liveness. §3 names the five other keys and leaves
  return codes to units 84 and 88. AC1 adds the inline-measure grep. §4 Evidence re-probes at HEAD;
  the shell-role widen and the symbol map join §4 and §7. Citations move to `path#symbol` or
  blob-pinned lines.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-74`'s `check_cr_reached` and liveness check in
`tools/run-gates/run-gates.gov.test.sh`, made one loop at its second key, with the liveness control
of `tools/run-gates/run-gates.evidence.test.sh@d3b748b94:2327-2336`.
`python tools/codebase-map/reuse_lookup.py "prove a byte comparison can fail by running it on a variant that loses the byte"`
ranked `read_bytes`, `fail`, `stage_or_fail`, `check_runner` and `no_row_loss` first (PINNED
2026-11-21), none a liveness check over a comparison, so no existing seam fits beyond those named
above.

Recall terms used: `python tools/memory-recall/query.py "how is a canary assertion proven able to fail on every run rather than once at the close" --terms "canary liveness variant mutant staged red byte check rec_sha rec_fp CR strip seen red failure line"`
