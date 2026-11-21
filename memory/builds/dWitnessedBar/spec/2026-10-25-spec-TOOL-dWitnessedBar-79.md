# TOOL-dWitnessedBar-79 — the canary's liveness loop gains a length variant, so a vacuous or off-by-one byte count is seen red on every run

**Status:** CLOSED · rev-3 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-79-deviation-791.md](../build/2026-10-25-build-TOOL-dWitnessedBar-79-deviation-791.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-79-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-79-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-79-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-79-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md](../build/2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-11-21-build-TOOL-dWitnessedBar-79-widen-20.md](../build/2026-11-21-build-TOOL-dWitnessedBar-79-widen-20.md) | widen | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-79-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-79-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-79-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-79-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-79-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-79-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 74 to 78
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md`)
confirmed finding **id 7 at HIGH**, report item **H1**. Ids 1 and 18 share that item and take
`TOOL-dWitnessedBar-81` and `TOOL-dWitnessedBar-80`.

`TOOL-dWitnessedBar-74` S1's `check_cr_reached` (`tools/run-gates/run-gates.gov.test.sh#check_cr_reached`)
passes a value only when it is forty-one bytes AND its last byte is CR. Its liveness variant, which
`TOOL-dWitnessedBar-76` S3 carried to each `CANARY_KEYS` pair, edits the `<key>)` assignment to
`${_rg_v%?}`: forty bytes ending in the key's last data byte, failing both conditions at once. A count
comparison made vacuous, `-ge 0` in place of forty-one, still rejects that value through the tail
test, so the liveness check passes and no run sees the count red. That is the hole unit 74 §1 says it
closes.

This unit gives the count its own variant. For every pair of the canary's keys, the liveness loop
also edits the `<key>)` assignment to `${_rg_v:1}`, a value of forty bytes still ending in CR, which
fails the count alone. It repairs `TOOL-dWitnessedBar-74` and builds at order 41, after it.

## 2. Scope (IN)

- **S1** — The length variant, through one variant function. The body of the per-key liveness loop
  (`tools/run-gates/run-gates.gov.test.sh@648a4d5d5:915-932`) moves into a new top-level function,
  `check_key_variant <key>:<var> <replacement> <label> <passed reason> <other lead>`. It reads the
  arm's `rgf_fn`, `rgf_t` and `rgf_rec`, keeps every variable of its own `local`, and does what the
  loop body does at HEAD: it writes `$rgf_t/cut-var.sh`, the cut with its `<key>)` assignment
  `<var>=$_rg_v` edited to `<var>=<replacement>` by the loop's one `sed`, then `$rgf_t/cut-var-mut.sh`
  under the canary's `sed 's/%[$].[\]r.}/}/'`, counts each `diff`'s `>` lines, and calls
  `tools/run-gates/run-gates.gov.test.sh#check_canary_keys` on the mutant over `$rgf_rec`. It prints
  nothing and returns 0 when the variant was seen red, else prints one reason and returns 1. The loop
  calls it twice per pair: first with `${_rg_v%?}`, an empty label, `it passed a value that lost its CR`
  and `it named`, so the tail variant's four reasons stay byte-identical to unit 76 S3's; then with
  `${_rg_v:1}`, the label `length `, S3's passed reason and `it named` (§8 F3, F4). The suite spells
  `${_rg_v:1}` once, on that call; the arm's header comment names it as the length variant and states
  what it does not check (§3). Observed by AC1 and AC3.
- **S2** — The variant is held to unit 74 S2's two one-line counts, then to the byte check. The
  variant must differ from the cut in one line, and the canary's `sed` must change one line of it.
  On that mutant `check_canary_keys` must print exactly `<var>`. Observed by AC1 and AC2.
- **S3** — The failure is loud and names the variant. The arm prints unit 74 S3's line,
  `gov-canary: the <var> byte check was not seen red on its liveness variant (<reason>)`, with
  `length variant changed <n> lines` or `length mutant changed <n> lines` when a count is not one, and
  `the length variant passed a value one byte short` when the mutant's `check_canary_keys` output
  lacks `<var>`; a name printed beside `<var>` prints `it named <other> whose CR arrived`, unit 76
  S3's reason, until `TOOL-dWitnessedBar-88` S17 gives the length variant its own. Each sets `fail=1`
  and keeps `<var>` out of `rgf_seen`, so that key's compare stays uncounted: unit 66 S2's for
  `rec_sha`, unit 67 S2's for `rec_fp`. A key joins `rgf_seen` only when both its variants were seen
  red. Observed by AC2.

## 3. Non-goals (OUT)

- The tail-only variant that stands in for unit 74 S2's `${_rg_v%?}`, which is
  `TOOL-dWitnessedBar-80`'s for id 18; it changes the tail call's replacement, label and passed reason.
- The record of unit 74 AC2's and unit 76 AC2's staged breaks with the line each printed, which is
  `TOOL-dWitnessedBar-81`'s for id 1.
- The length variant's own reason when another variable is named,
  `the length variant named <other> whose CR arrived`, which is `TOOL-dWitnessedBar-88` S17's (id 20
  of the round-1 spec audit of units 79 to 84).
- A distinct return code for a variant that could not be sourced, and a sed that admits a quoted
  assignment, which are `TOOL-dWitnessedBar-84`'s for ids 19 and 6.
- The assertion floor, which `TOOL-dWitnessedBar-82` restates after this unit lands, and a count per
  variant, which is `TOOL-dWitnessedBar-85`'s.
- A comparison that still rejects forty bytes but admits more than forty-one, `-ge 41`: neither
  variant reaches it (§4 Evidence), and the arm's header comment names it as not checked.
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

Probed at `648a4d5d5` on 2026-11-21 under GNU bash 5.3.9 `x86_64-pc-cygwin` and GNU sed 4.9
(PINNED 2026-11-21). The probe cut the hook's `read_green_file` (`.githooks/pre-push#read_green_file`)
and read a hand-built record laid out as the AC12 arm's: `verdict<TAB>GREEN<CR>`, two `sha` lines the
second CR-ended, `reused_cache` 1 then 0`<CR>`, a CR-ended `fingerprint` (PINNED 2026-11-21). It
defined `check_cr_reached` and `check_canary_keys` as the suite does and a prototype of S1's function
and two calls. The arm's own record, from `run_local_plant`, is the main loop's at the close.

| Mutant of | Variant · mutant count | `rec_sha` · `rec_fp` bytes, last byte | `check_canary_keys` printed | Pin |
|---|---|---|---|---|
| `sha` length variant | 1 · 1 | 40 `\r` · 41 `\r` | `rec_sha` | PINNED 2026-11-21 |
| `fingerprint` length variant | 1 · 1 | 41 `\r` · 40 `\r` | `rec_fp` | PINNED 2026-11-21 |

- The `sha` edit wrote `sha) rec_sha=${_rg_v:1} ;;`, and `${_rg_v:1}` holds no `%$`, so the canary's
  pattern `%[$].[\]r.}` leaves the edited line alone (PINNED 2026-11-21, this probe).
- Over the real comparison the two calls printed no line and `rgf_seen` held both variables. With
  the comparison at `-ge 0`, tail test kept, the length call printed
  `(the length variant passed a value one byte short)` for `rec_sha` and `rec_fp`, the tail call
  printed nothing, and `rgf_seen` was empty. With it at `-ge 41`, no call printed a line: the hole §3
  names (PINNED 2026-11-21, this probe).
- At HEAD the loop body is inline: one `sed` edit, two `diff` counts, one `check_canary_keys` call, a
  name split into `rgf_has` and `rgf_oth`, and an `if`/`elif` chain setting `rgf_why`
  (`tools/run-gates/run-gates.gov.test.sh@648a4d5d5:915-932`). `grep -cF '=\)\$_rg_v/\1'` over the
  suite prints 1 (PINNED 2026-11-21), the loop's edit, and `grep -c '_rg_v:1}'` prints 0
  (PINNED 2026-11-21). Unit 76's builder return records the loop's reasons as built
  (`memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-76-1-builder-return.md`).
- The suite counts executed assertions in `a` (`tools/run-gates/run-gates.gov.test.sh@648a4d5d5:243`)
  and checks them against `FLOOR_ASSERTIONS`, set at `@648a4d5d5:246`, only as a minimum (`:1204`).
  The two compares count only for a variable in `rgf_seen` (`@648a4d5d5:933`, `:936`).
- `tools/gate-lint/sh_hygiene.py#measure_code_lines` measures the suite's code lines at 784 (PINNED
  2026-11-21), the count its `memory/project/shell-role.txt` row holds at `648a4d5d5`.
- Unit 76 §4 Evidence and unit 74's builder return record `check_cr_reached` called inside `$(...)`
  returning as it does directly (DERIVED from those builders' probes), so S1's calls may capture the
  reason with `$(...)`; the CR stays spelled in `check_cr_reached`'s top-level body.

### Inventory

Minted: the suite function `check_key_variant`, the replacement text `${_rg_v:1}`, the label `length `
and S3's three reasons. No constant, plant, flag or file. Naming cells: `check_key_variant` opens with
`check`, a VERBS entry of `.lexicon.conf`; it nests no helper.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 41. Order 41 holds `TOOL-dWitnessedBar-73` and `-76`, CLOSED at
`71f212ad1` and `bdc10a4df`, and `-77`, `-79`, `-80` and `-81`. Dispatch is strictly sequential and
sorts a tie by id string (`tools/workflows/unattended-build.js@648a4d5d5:78-82`, `:692-697`), so unit
77 builds before this unit and units 80 and 81 after it. Units 77 and 80 name this suite in their
Files touched, so the three build one at a time and the builder reads the loop as unit 77 leaves it.
Unit 80 then edits the tail call's arguments, not an inline body (§8 F5).

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`: S1's function, the loop's two calls and the arm's header comment.
- `memory/project/shell-role.txt`: the suite's row reads 784 at `648a4d5d5` (PINNED 2026-11-21), the
  count the suite measures (§4 Evidence), so the row has no headroom. When S1 grows the suite past
  it, the pass widens it with
  `python tools/memory-tree/ratchet.py widen shell-role --key tools/run-gates/run-gates.gov.test.sh --reason "TOOL-dWitnessedBar-79 S1: the length variant through check_key_variant" --unit TOOL-dWitnessedBar-79`
  and sets the count to the measured value, as unit 76's builder return records doing.
- `memory/builds/dWitnessedBar/build/`: the widen record that command writes.
- `memory/map/generated/symbols.json`: the codebase map's generator, run with `--write`, adds
  `check_key_variant`, as unit 76's commit added `check_canary_keys`.

### Alternatives rejected

- **Stage a `-ge 0` break once at the close and record it.** The count is then seen red once, and a
  later edit that makes it vacuous lands green with nobody staging the break. Unit 74 §4 rejected a
  close-only break for the same reason.
- **A length variant for `rec_sha` alone.** `rec_fp`'s count would stay unobserved, and the loop
  unit 76 S3 built would hold one key's variant beside another's. One call in the loop serves every key.
- **A second inline block for the length variant beside the tail's.** Two copies of one check is the
  shape the charter's reuse rule refuses at the second instance, as unit 76 §4 rejected it (§8 F4).
- **`${_rg_v}x` for the length half.** A value of forty-two bytes ending in `x` fails both
  conditions again, the defect this unit exists to remove.

## 5. Production-readiness checklist

- security — no new write path. The variant and its mutant are written in the arm's scratch
  directory, `$rgf_t`.
- perf / scale — one more variant per key: two `sed`, two `diff`, one `check_canary_keys` call and one
  subshell each.
- error / empty / loading states — S3 names the ways the length variant fails.
- observability — S3's reason names the length variant, so its red reads apart from the tail
  variant's.
- risks — a reader rewritten so an assignment is spelled differently fails with
  `length variant changed 0 lines`, as the tail variant does with `variant changed 0 lines`.
- testing — AC1 and AC3 by probe and grep, AC2 by scratch clone at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe applies S1's edit for `sha`, `sed 's/\(sha) rec_sha=\)\$_rg_v/\1${_rg_v:1}/'`,
  to the function cut by `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` on the built tree,
  then the canary's `sed 's/%[$].[\]r.}/}/'` to the result, each `diff` counts one changed line. The
  sourced mutant, called on the AC12 record, gives `printf %s "$rec_sha" | wc -c` as 40 with
  `printf %s "$rec_sha" | tail -c1 | od -c` showing `\r`, and `rec_fp` as 41 bytes (PINNED 2026-11-21).
  The same probe on the `fingerprint` arm gives `rec_fp` forty bytes ending in `\r` and `rec_sha`
  forty-one (PINNED 2026-11-21, §4 Evidence).
  Red when: the variant fails the tail test too, so the count is never isolated.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
- **AC2** — When the arm runs over the built tree, it prints no `length variant` line. In a scratch
  clone whose suite copy has `check_cr_reached` compare the byte count with `-ge 0` in place of
  forty-one, the arm prints
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (the length variant passed a value one byte short)`
  and the same line for `rec_fp`, prints no tail-variant reason, and exits non-zero.
  Red when: a vacuous count comparison passes with the arm green.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When `grep -c '_rg_v:1}' tools/run-gates/run-gates.gov.test.sh`,
  `grep -cF '=\)\$_rg_v/\1' tools/run-gates/run-gates.gov.test.sh` and
  `grep -c '^check_key_variant()' tools/run-gates/run-gates.gov.test.sh` run on the built tree, each
  prints 1 (PINNED by S1).
  Red when: the length variant is spelled once per key, or its edit is a copy beside the tail
  variant's, so the copies can drift.

## 7. Gates

`run-gates gov canary` · `portability (shell lines only shrink)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene`

`portability (shell lines only shrink)` reads the widened shell-role row and checks a count, never the
arm. `codebase-map coverage + freshness` grades the regenerated `symbols.json`, and
`lexicon naming predicates` grades `check_key_variant`'s verb. The two recall legs are named because
their guards name `memory/`, where the row, the widen record and the map sit. Other legs whose guard
names `tools/` or `tools/run-gates/` run on the bar and are none of them this unit's observation.
`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh#derive_hold_source`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf@648a4d5d5:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC2 · the length variant of the per-key liveness loop, run on every bar through `check_key_variant`, staged red by a scratch suite whose `check_cr_reached` compares the count with `-ge 0` (defeats the length condition, reaches `the length variant passed a value one byte short` for `rec_sha` and `rec_fp`) · the floor is restated after this unit by `TOOL-dWitnessedBar-82` S1, which builds at order 43

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
- **F3 — What does the length variant print when its mutant's output names `<var>` and another
  variable?** Unit 76 landed `it named <other> whose CR arrived` for the tail variant after this spec's
  rev-2, which defined no reason for the case, and `TOOL-dWitnessedBar-88` S17 later mints the length
  variant's own. Options: (a) the tail's reason, through the same `it named` lead, so S2's "exactly"
  holds now and the line prints once per variant until 88 S17; (b) no reason here, testing presence
  alone, which drops S2's "exactly"; (c) 88 S17's reason now, which violates §3's non-goal. Veto 1
  discards (c); (a) satisfies S2 and (b) does not. RESOLVED (agent, 2026-11-21, delegated): (a),
  rung 3, the most feature-rich survivor; 88 S17 changes one argument.
  widens: none · relaxes: none
- **F4 — How does the length variant enter the loop unit 76 landed inline?** Options: (a) the loop
  body becomes `check_key_variant`, called once per variant; (b) a second inline block beside the
  tail's; (c) an inner loop over a table of variants, each row packing four fields into one string.
  (b) is the copy the charter's `[reuse]` rule refuses at the second instance. (c) needs a separator
  absent from every replacement and reason, an open question the function's positional arguments do
  not have. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, tie-broken by fewer open questions
  and by reuse of the loop's own body.
  widens: none · relaxes: none
- **F5 — Does S1's function, which unit 80 then edits, carry an Edges bullet?** Memory hygiene check
  12 joins each edge to its counterpart, and unit 80's spec, re-grounded in parallel and outside this
  brief, declares no edge to this unit. Options: (a) name the dependence in §3 and §4 Rollout, with no
  bullet; (b) add a hands-off bullet to unit 80, which no consumes-from mirrors. (b) risks check 12
  failing this brief's acceptance; veto 1 discards it. RESOLVED (agent, 2026-11-21, delegated): (a),
  the one survivor; the dispatcher is told in this re-ground's return.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 74 to 78, id 7
  (HIGH, item H1, shared with ids 1 and 18).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-85, TOOL-dWitnessedBar-86, TOOL-dWitnessedBar-87 and
  TOOL-dWitnessedBar-88, promoted by the round-1 spec audit of units 79 to 84; nothing else moved.
- rev-3 · 2026-11-21 · §1 to §10 · S1 to S3 · AC1 to AC3 · re-grounded over units 74 and 76 as
  landed, per 2026-11-19-prompt-TOOL-dWitnessedBar-79-reground-brief. S1 moves the inline loop body
  into `check_key_variant`, called for the tail and the length variant (§8 F4); S3 gives the length
  variant the tail's other-variable reason until unit 88 S17 (§8 F3) and names each key's compare.
  §3 names the reasons 88 and 85 own and the `-ge 41` hole. §4 Evidence re-probes at HEAD; the
  shell-role widen, its record and the symbol map join Files touched and §7. AC3 adds the one-edit and
  one-function greps. Citations move to `path#symbol` or blob-pinned lines.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-76`'s per-key liveness loop over `CANARY_KEYS` in
`tools/run-gates/run-gates.gov.test.sh` (`@648a4d5d5:915-932`), whose body S1 extracts into
`check_key_variant` and calls once per variant, with the liveness control of
`tools/run-gates/run-gates.evidence.test.sh@648a4d5d5:2327-2336`.
`python tools/codebase-map/reuse_lookup.py "prove each condition of a two-condition check can fail on its own variant"`
ranked `check`, `fail`, `checks` and `check_line` on 2026-11-21, and
`python tools/codebase-map/reuse_lookup.py "run one liveness variant of a cut function and print why it was not seen red"`
ranked `run`, `note`, `run_git` and `run_probe`, none a variant that isolates one condition of a
comparison, so no existing seam fits beyond the loop named above.

Recall terms used: `python tools/memory-recall/query.py "how is each condition of a canary byte check seen red, and who restates the assertion floor" --terms "canary liveness variant length tail CR byte check FLOOR_ASSERTIONS restated floor owner seen red"`
