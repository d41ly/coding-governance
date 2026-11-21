# TOOL-dWitnessedBar-72 — the `fingerprint` CRLF line's strip is proven reachable by the same canary, so unit 67's `rec_fp` break can turn red on Windows

**Status:** CLOSED · rev-4 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 40 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-73 |
| [2026-10-25-build-TOOL-dWitnessedBar-72-deviation-721.md](../build/2026-10-25-build-TOOL-dWitnessedBar-72-deviation-721.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-72-deviation-722.md](../build/2026-10-25-build-TOOL-dWitnessedBar-72-deviation-722.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-72-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-72-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-72-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-72-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-72-widen-14.md](../build/2026-11-21-build-TOOL-dWitnessedBar-72-widen-14.md) | widen | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-73 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-72-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-72-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-72-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-72-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-72-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-72-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-73 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 66 and 67
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md`)
confirmed finding **id 20 at HIGH**, report item **H4**. No other id shares that item; it is the same
platform fact as id 10 (B1) and id 19 (H3), in a separate clause of a separate spec.

`TOOL-dWitnessedBar-67` S2 plants `fingerprint<TAB>` forty `c` `<CR><LF>` and stages the break "a
`read_green_file` whose `fingerprint` read keeps the CR", which should turn the arm red naming
`rec_fp`. The base read was `rec_fp=$(awk -F'\t' '$1=="fingerprint"{print $2}' "$1" 2>/dev/null)`
(`.githooks/pre-push@df0a656d:1355`). On Git for Windows, gawk's text-mode input and `$(...)` both
drop that CR, so `rec_fp` was forty bytes whether or not the strip existed, and unit 67's AC2 break
could not go red on any Windows node or on `windows-latest` CI.

`TOOL-dWitnessedBar-69` (`298369174`) made `fingerprint` one case of a whole-line read loop with one
strip, and unit 67's builder saw the break red on `rec_fp` on this node (its ledger, AC2). Nothing
keeps it so. `TOOL-dWitnessedBar-70`'s canary (`09718851e`) proves the CR reaches the read for
`rec_sha` alone, and counts unit 67 S2's `rec_fp` compare uncanaried. A later `fingerprint` read
through a bare `$(awk ...)` leaves the whole arm green on this node (§4 Evidence).

This unit puts the `fingerprint` line under that canary, over unit 69's read, and records AC2's
break with its failing line. It repairs `TOOL-dWitnessedBar-67` and builds one step after it
(order 40).

## 2. Scope (IN)

- **S1** — The canary covers `rec_fp`. Over the record holding unit 67 S2's `fingerprint` line, unit
  70 S1's mutant, which lacks the CR strip, gives `rec_fp` forty-one bytes whose last byte is CR, and the canary
  asserts it beside its `rec_sha` assertion. The subshell that measures the mutant's `rec_sha`
  (`rgf_mr`) measures `rec_fp` the same way, its CR test reading `rgf_crb`, which is set outside the
  subshell because this node's bash reads a `$'\r'` spelled inside `$(...)` as empty. `rgf_ok` is set
  only when the count is one and both values are forty-one bytes ending in CR. When it does not hold,
  the canary prints unit 70 S2's failure line, which names no key at HEAD; the slot that names `rec_fp`
  is `TOOL-dWitnessedBar-75`'s and `TOOL-dWitnessedBar-77`'s. It sets `fail=1`, and unit 67 S2's
  assertion is not counted: its `a=$((a+1))` is gated on `rgf_ok` as the `rec_sha` compare's is, and
  the compare still runs and prints its own line. The arm's comment names the `rec_fp` grading as
  canaried, in place of "uncanaried". Observed by AC1.
- **S2** — The `fingerprint` read is the `fingerprint` case of unit 69 S1's loop, with no read of its
  own. This holds at HEAD since unit 69 (`298369174`); this unit changes nothing in
  `.githooks/pre-push`. Observed by AC2.
- **S3** — Unit 67 AC2's break is recorded with its failing line. At the close, on a Windows node, the
  main loop stages a `read_green_file` that lacks its CR strip, since unit 69 the one strip for every
  key. Unit 67's acceptance ledger records it beside AC2 with the arm's failing line, which
  names `rec_fp`, and the `uname -s` it ran under. Unit 67's own AC2 line quotes that red with no
  `uname -s` and no unit 72, so S3's is a second line opening `- AC2 — ` under its
  `**Evidences:** TOOL-dWitnessedBar-67` block, as unit 70 S3 adds to unit 66's. Observed by AC3.

## 3. Non-goals (OUT)

- The read form, which is `TOOL-dWitnessedBar-69`'s, and the canary's mechanism, which is
  `TOOL-dWitnessedBar-70`'s. This unit adds one key to what the canary checks.
- The canary's one check function, `TOOL-dWitnessedBar-74` S1's and `TOOL-dWitnessedBar-76` S2's, and
  the failure line's slot, `TOOL-dWitnessedBar-75` S1's. Both build after this unit, so S1's `rec_fp`
  test is inline, the copy unit 76 S2 moves.
- A CRLF line for the five other keys `read_green_file` reads, which is `TOOL-dWitnessedBar-73` S9's.
- The report's left-shift text, the checklist entry and selftest grep item H3 names. No clause of this
  build names them.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-67` — S2's `fingerprint` line and AC2's staged break, which this unit makes able to turn red on the bar's platform (id 20)
- **consumes-from** `TOOL-dWitnessedBar-69` — the whole-line read whose `fingerprint` case carries the CR to the strip (id 20)
- **consumes-from** `TOOL-dWitnessedBar-70` — the CR-reach canary and its failure line, which S1 extends to `rec_fp` (id 20)
- **hands-off** `TOOL-dWitnessedBar-76` — S1's `rec_fp` comparison moved onto the canary's one check function and seen red on every run by a `fingerprint` variant, in place of AC1's `$(awk ...)` plant (id 9 of the round-1 spec audit of units 68 to 73, item H2)
- **hands-off** `TOOL-dWitnessedBar-77` — the `rec_fp` value of the canary line's slot, which S1 leaves to it, and AC1's red recorded with that line (id 25, item H2)
- **hands-off** `TOOL-dWitnessedBar-78` — the ledger lines for AC1 and AC3: the `diff` count, the strip-less break's two lines, the Inventory answered and S3's reason stated (ids 1, 2, 8, 17)
- **hands-off** `TOOL-dWitnessedBar-84` — AC1's `$(awk ...)` break, recorded in this unit's ledger as a count failure printing `for count 2` by design (id 4 of the round-1 spec audit of units 74 to 78)

## 4. Design

### Evidence

- `.githooks/pre-push@df0a656d:1355` reads `rec_fp=$(awk -F'\t' '$1=="fingerprint"{print $2}' "$1" 2>/dev/null)`.
- On this node (GNU Awk 5.4.0, bash 5.3.9 `x86_64-pc-cygwin`), a `fingerprint<TAB>` forty `c`
  `<CR><LF>` line read by `awk -F'\t' '$1=="fingerprint"{print length($2)}'` printed 40 (PINNED
  2026-10-25).
- At HEAD `921f83fff`, `.githooks/pre-push#read_green_file` reads `fingerprint` as the case
  `fingerprint) rec_fp=$_rg_v ;;` of its loop, and AC2's two greps print 1 and 0 (PINNED 2026-11-21).
- The suite counts unit 67 S2's compare with a bare `a=$((a+1))`
  (`tools/run-gates/run-gates.gov.test.sh@921f83fff:882`), where the `rec_sha` compare's is gated on
  `rgf_ok` (`:879`), and the arm's comment calls the `rec_fp` grading uncanaried (`:836`).
- Probed at `921f83fff` under `uname -s` `MINGW64_NT-10.0-22621` and git 2.54.0.windows.1 (PINNED
  2026-11-21): the arm's own lines, cut from `rgf_t=$(mktemp -d)` to `rm -rf "$rgf_t"`, over the
  record `run_local_plant` builds, then the arm's mutant sourced once more to measure `rec_fp`. Each
  copy of the hook is one `diff` line from it:
  - HEAD's hook: count 1, the mutant's `rec_sha` and `rec_fp` each 41 bytes ending `\r`, the arm
    holds (PINNED 2026-11-21, this probe).
  - `fingerprint) rec_fp=$(awk -F'\t' '$1=="fingerprint"{print $2}' "$1") ;;`: count 1, `rec_sha`
    41 bytes ending `\r`, `rec_fp` 40 ending `c`; the arm holds with `fail` 0 (PINNED 2026-11-21,
    this probe). This is the break S1 exists for.
  - the same read followed by `rec_fp=${rec_fp%$'\r'}`: count 2, so the canary prints its line before
    any byte test, as unit 84 S5 records by design (PINNED 2026-11-21, this probe).
  - `fingerprint) rec_fp=${_rg_v%?} ;;`: count 1, `rec_fp` 40 ending `c`; no canary line, and unit 67
    S2's compare reds at thirty-nine `c` (PINNED 2026-11-21, this probe).
- `grep -c 'runs-on: windows-latest' .github/workflows/remote-ci.yml` prints 4 (PINNED 2026-11-21).
- `tools/gate-lint/sh_hygiene.py#measure_code_lines` measures the suite at 715, its row in
  `memory/project/shell-role.txt` (PINNED 2026-11-21), so a line S1 adds widens that row.

### Inventory

Minted: nothing. No function, constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 40, after `TOOL-dWitnessedBar-67`, `TOOL-dWitnessedBar-69` and
`TOOL-dWitnessedBar-70`, order 39, CLOSED at `e1d569fc9`, `298369174` and `09718851e`. The dispatch
edge refusal (`tools/unattended/unattended.sh#verb_dispatch`) holds this unit until all three are
CLOSED, and they are. Order 40's `TOOL-dWitnessedBar-71`, CLOSED at `ced984440`, wrote
`tools/lib/resolve-python.test.sh`, apart from this unit's set. `TOOL-dWitnessedBar-74` and
`TOOL-dWitnessedBar-75` edit this unit's suite and build after it, one at a time: 72, then 74, then 75.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `memory/project/shell-role.txt`: where S1 grows the suite past its row, 715 (PINNED 2026-11-21 by
  the gate-lint kit's `shell-role` seed), the pass widens it by `python tools/memory-tree/ratchet.py widen`
  and declares the widen record under `memory/builds/dWitnessedBar/build/` through `--dispatch`, as
  unit 70 did.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-67-1-acceptance-ledger.md`:
  S3's line, the main loop's at the close.

### Alternatives rejected

- **A second, `fingerprint`-only canary.** It would repeat unit 70's mutant and count for one more key;
  one canary over both keys reads the same mutant once.
- **Drop unit 67 S2's `fingerprint` line now that one strip serves every key.** The line is what makes
  a reader that strips `sha` alone visible, and unit 73 S9 widens it to every key.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — one more measurement in the subshell the canary already runs over its mutant.
- error / empty / loading states — N/A: the arm reads a fixture it writes itself.
- observability — unit 70 S2's failure line prints when the `rec_fp` CR did not arrive; it names no
  key until `TOOL-dWitnessedBar-77`, and the `rec_fp` compare prints its own line naming `rec_fp`.
- risks — none beyond unit 70's.
- testing — AC1 by probe over staged copies, AC2 by grep, AC3 by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the canary runs over the built tree on this Windows node, the mutant's
  `printf %s "$rec_fp" | wc -c` prints 41 with `tail -c1 | od -c` showing `\r`, and no
  `gov-canary: the planted CR` line prints. With `ROOT` at a scratch tree whose `.githooks/pre-push`
  reads `fingerprint) rec_fp=$(awk -F'\t' '$1=="fingerprint"{print $2}' "$1") ;;`, the arm prints
  `gov-canary: the planted CR never reached read_green_file on ` followed by the `uname -s` value,
  sets `fail` to 1, and `a` counts two fewer than over the hook, the `rec_sha` and `rec_fp` compares
  both uncounted. Against a copy whose `fingerprint` read is `$(awk -F'\t' '$1=="fingerprint"{print $2}' "$1")`
  followed by the strip, the arm prints the same line at the canary's count of 2. Each copy is one
  `diff` line away from the hook.
  Red when: the canary checks `rec_sha` alone, so a `fingerprint` read that eats the CR stays green.
  fixture: scratch copies of `.githooks/pre-push` under `%TEMP%/<short-name>`.
  figure: 41 is PINNED by S1, forty `c` and its CR.
- **AC2** — When `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` is piped to
  `grep -c 'fingerprint)'`, it prints 1, and piped to `grep -c '"fingerprint"'`, it prints 0.
  Red when: `fingerprint` is read by a command of its own again.
- **AC3** — When `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-67*acceptance-ledger*`
  runs at the close, the line quotes a failing line naming `rec_fp` and a `uname -s` value beginning
  `MINGW` or `MSYS`, and names `TOOL-dWitnessedBar-72`.
  Red when: AC2's break is recorded red with no captured line, or from no Windows node.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh#derive_hold_source`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf@921f83fff:40`). `portability (shell lines only shrink)` reads the widened
`memory/project/shell-role.txt` row and checks a count, never the canary. The two recall legs are
named because their guards name `memory/`, where the row and unit 67's ledger sit.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 · the canary's `rec_fp` assertion over unit 67's `fingerprint` line, staged red by a scratch hook whose `fingerprint` read is a bare `$(awk ...)` (reaches the 41-byte assertion on `rec_fp`, its mutant reading 40 bytes, PINNED 2026-11-21) and by one whose `$(awk ...)` read keeps the strip (reaches the one-line count, at two lines) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 67 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which staged copy reds the canary's `rec_fp` assertion (forced by the re-ground)?** Rev-3's
  copy, a `$(awk ...)` read followed by its own strip, gives the canary's `sed` two lines to change
  over unit 69's loop, so it stops at unit 70's count before any byte test, and a canary checking
  `rec_sha` alone reds on it too (§4 Evidence). Options: (a) keep that copy alone; (b) replace it
  with the bare `$(awk ...)` read, one `sed` line, which leaves the arm green at HEAD; (c) stage both,
  the bare read as the byte-arm red and the stripped read as the count red unit 84 S5 records. (a)
  never observes AC1's Red-when; veto 1 discards it. (b) drops the copy unit 84 S5 and AC5 name.
  RESOLVED (agent, 2026-11-21, delegated): (c), the most feature-rich survivor, meeting AC1's
  Red-when and keeping unit 84's referent.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 66 and 67, id 20
  (HIGH, item H4).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-76, TOOL-dWitnessedBar-77 and TOOL-dWitnessedBar-78,
  promoted by the round-1 spec audit of units 68 to 73; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-84, promoted by the round-1 spec audit of units 74 to 78; nothing else
  moved.
- rev-4 · 2026-11-21 · §1 · §3 · §4 · §5 · §7 · §8 · §10 · S1 · S2 · S3 · AC1 · re-grounded over units
  67, 69 and 70 as landed, per 2026-11-19-prompt-TOOL-dWitnessedBar-72-reground-brief. The Goal states
  that unit 69's loop already reds the break and unit 70's canary covers `rec_sha` alone. S1 names
  `rgf_mr`, `rgf_crb` and the gated count, and says unit 70's line names no key, the slot being units
  75's and 77's. S2 holds at HEAD; S3 adds a second `- AC2 — ` line. §3 names the check function and
  slot as later units'. §4 Evidence is re-probed and blob-pinned; Rollout, Files touched and the leg
  line gain the shell-role row and unit 67's ledger. AC1 gains the bare-read copy (§8 F2).

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-70`'s CR-reach canary in `tools/run-gates/run-gates.gov.test.sh`,
extended by one key over the mutant it already builds.
`python tools/codebase-map/reuse_lookup.py "assert a planted fixture byte survives the read before counting a mutation red"`
ranked `read_text`, `read`, `read_bytes`, `before`, `counts` and `fixture` first (PINNED 2026-11-21),
none a mutation check, so no existing seam fits beyond the canary named above.

Recall terms used: `python tools/memory-recall/query.py "how does the green record reader keep a CR so the strip is exercised on Git for Windows" --terms "read_green_file rec_sha CR strip CRLF gawk text mode command substitution read -r canary staged red"`
