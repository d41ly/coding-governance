# TOOL-dWitnessedBar-72 — the `fingerprint` CRLF line's strip is proven reachable by the same canary, so unit 67's `rec_fp` break can turn red on Windows

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 40 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-73 |
| [2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-73 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-73 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 66 and 67
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md`)
confirmed finding **id 20 at HIGH**, report item **H4**. No other id shares that item; it is the same
platform fact as id 10 (B1) and id 19 (H3), in a separate clause of a separate spec.

`TOOL-dWitnessedBar-67` S2 plants `fingerprint<TAB>` forty `c` `<CR><LF>` and stages the break "a
`read_green_file` whose `fingerprint` read keeps the CR", which should turn the arm red naming
`rec_fp`. The base read is `rec_fp=$(awk -F'\t' '$1=="fingerprint"{print $2}' "$1" 2>/dev/null)`
(`.githooks/pre-push:1355`). On Git for Windows, gawk's text-mode input and `$(...)` both drop that
CR, so `rec_fp` is forty bytes whether or not the strip exists, and unit 67's AC2 break cannot go red
on any Windows node or on `windows-latest` CI.

This unit puts the `fingerprint` line under the CR-reach canary `TOOL-dWitnessedBar-70` builds, over
the read `TOOL-dWitnessedBar-69` builds, and records AC2's break with its failing line. It repairs
`TOOL-dWitnessedBar-67` and builds one step after it (order 40).

## 2. Scope (IN)

- **S1** — The canary covers `rec_fp`. Over the record holding unit 67 S2's `fingerprint` line, unit
  70 S1's mutant, which lacks the CR strip, gives `rec_fp` forty-one bytes whose last byte is CR, and the canary
  asserts it beside its `rec_sha` assertion. When it does not hold, unit 70 S2's failure line names
  `rec_fp` and unit 67 S2's assertion is not counted. Observed by AC1.
- **S2** — The `fingerprint` read is the `fingerprint` case of unit 69 S1's loop, with no read of its
  own. Observed by AC2.
- **S3** — Unit 67 AC2's break is recorded with its failing line. At the close, on a Windows node, the
  main loop stages a `read_green_file` that lacks its CR strip, since unit 69 the one strip for every
  key. Unit 67's acceptance ledger records it beside AC2 with the arm's failing line, which
  names `rec_fp`, and the `uname -s` it ran under. Observed by AC3.

## 3. Non-goals (OUT)

- The read form, which is `TOOL-dWitnessedBar-69`'s, and the canary's mechanism, which is
  `TOOL-dWitnessedBar-70`'s. This unit adds one key to what the canary checks.
- A CRLF line for the five other keys `read_green_file` reads, which is `TOOL-dWitnessedBar-73` S9's.
- The report's left-shift text, the checklist entry and selftest grep item H3 names. No clause of this
  build names them.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-67` — S2's `fingerprint` line and AC2's staged break, which this unit makes able to turn red on the bar's platform (id 20)
- **consumes-from** `TOOL-dWitnessedBar-69` — the whole-line read whose `fingerprint` case carries the CR to the strip (id 20)
- **consumes-from** `TOOL-dWitnessedBar-70` — the CR-reach canary and its failure line, which S1 extends to `rec_fp` (id 20)

## 4. Design

### Evidence

- `.githooks/pre-push:1355` reads `rec_fp=$(awk -F'\t' '$1=="fingerprint"{print $2}' "$1" 2>/dev/null)`
  at `df0a656d`.
- On this node (GNU Awk 5.4.0, bash 5.3.9 `x86_64-pc-cygwin`), a `fingerprint<TAB>` forty `c`
  `<CR><LF>` line read by `awk -F'\t' '$1=="fingerprint"{print length($2)}'` printed 40. A prototype of
  unit 69 S1's loop gave `rec_fp` 40 bytes, and its strip-deleted mutant 41 bytes.
- `grep -n runs-on .github/workflows/remote-ci.yml` prints four `windows-latest` lines.

### Inventory

Minted: nothing. No function, constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 40, after `TOOL-dWitnessedBar-67` (39), `TOOL-dWitnessedBar-69` (39) and
`TOOL-dWitnessedBar-70` (39). Order 40 is shared with `TOOL-dWitnessedBar-71`, whose write set,
`tools/lib/resolve-python.test.sh`, does not meet this unit's.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **A second, `fingerprint`-only canary.** It would repeat unit 70's mutant and count for one more key;
  one canary over both keys reads the same mutant once.
- **Drop unit 67 S2's `fingerprint` line now that one strip serves every key.** The line is what makes
  a reader that strips `sha` alone visible, and unit 73 S9 widens it to every key.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — one extra assertion on a mutant the canary already sources.
- error / empty / loading states — N/A: the arm reads a fixture it writes itself.
- observability — unit 70 S2's failure line names `rec_fp` when its CR did not arrive.
- risks — none beyond unit 70's.
- testing — AC1 and AC2 by probe, AC3 by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the canary runs over the built tree on this Windows node, the mutant's
  `printf %s "$rec_fp" | wc -c` prints 41 with `tail -c1 | od -c` showing `\r`. Against a scratch copy
  of `.githooks/pre-push` whose `fingerprint` read is `$(awk -F'\t' '$1=="fingerprint"{print $2}' "$1")`
  followed by the strip, the canary's failure line names `rec_fp`.
  Red when: the canary checks `rec_sha` alone, so a `fingerprint` read that eats the CR stays green.
- **AC2** — When `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` is piped to
  `grep -c 'fingerprint)'`, it prints 1, and piped to `grep -c '"fingerprint"'`, it prints 0.
  Red when: `fingerprint` is read by a command of its own again.
- **AC3** — When `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-67*acceptance-ledger*`
  runs at the close, the line quotes a failing line naming `rec_fp` and a `uname -s` value beginning
  `MINGW` or `MSYS`, and names `TOOL-dWitnessedBar-72`.
  Red when: AC2's break is recorded red with no captured line, or from no Windows node.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 · the canary's `rec_fp` assertion over unit 67's `fingerprint` line, staged red by a scratch hook whose `fingerprint` read goes through `$(awk ...)` with the strip kept (reaches the 41-byte assertion on `rec_fp`) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 67 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 66 and 67, id 20
  (HIGH, item H4).

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-70`'s CR-reach canary in `tools/run-gates/run-gates.gov.test.sh`,
extended by one key over the mutant it already builds.
`python tools/codebase-map/reuse_lookup.py "assert a planted fixture byte survives the read before counting a mutation red"`
ranked `read`, `read_text`, `before` and `counts`, none a mutation check, so no existing seam fits
beyond the canary named above.

Recall terms used: `python tools/memory-recall/query.py "how does the green record reader keep a CR so the strip is exercised on Git for Windows" --terms "read_green_file rec_sha CR strip CRLF gawk text mode command substitution read -r canary staged red"`
