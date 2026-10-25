# TOOL-dWitnessedBar-66 — the CRLF record arm plants its CR on a key `read_green_file` reads, so removing the hook's CR strip turns the arm red

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 38 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 |
| [2026-10-25-build-TOOL-dWitnessedBar-66-round6-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-66-round6-fix-return.md) | research | TOOL-dWitnessedBar-67 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-66-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-66-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-66-round6-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-66-round6-fix-brief.md) | research | TOOL-dWitnessedBar-67 |
| [2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 64 and 65
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md`)
confirmed finding **id 6 at HIGH**, its item **H1**. The report keeps it apart from item M1 (ids 1
and 12), which describes the same AC12 defect at MEDIUM and which `TOOL-dWitnessedBar-67` takes.

`TOOL-dWitnessedBar-65` AC12 plants its only CR on a `verdict<TAB>GREEN<CR>` line. The hook's
`read_green_file` (`.githooks/pre-push:1351-1369`) reads seven keys, and `verdict` is not one of them.
So §7's staged red "removing the hook's CR strip" leaves the arm green, and the arm certifies a strip
it never exercises. This unit moves the hook half's CR onto the `sha` key, which `read_green_file`
reads into `rec_sha`, and names that variable as the one each staged break reaches. It repairs
`TOOL-dWitnessedBar-65` and builds one step after it (order 38).

## 2. Scope (IN)

- **S1** — The record the hook half reads. Unit 65's AC12 arm in
  `tools/run-gates/run-gates.gov.test.sh` writes, in the suite's scratch directory, a record holding
  these lines in this order:

  | line | bytes |
  |---|---|
  | 1 | `verdict<TAB>GREEN<CR><LF>` |
  | 2 | `sha<TAB>` followed by forty `a` characters, then `<LF>` |
  | 3 | `sha<TAB>` followed by forty `b` characters, then `<CR><LF>` |

  The only CR the hook half depends on sits on line 3, a key `read_green_file` reads. Line 1 stays for
  the local-hook reader only. Observed by AC1 and AC3.
- **S2** — The hook half's assertion. The arm cuts `read_green_file` with
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push`, sources it, calls it on S1's record, and
  asserts that `rec_sha` equals forty `b` characters exactly. That one compare fails on a kept CR,
  since the value is then forty-one bytes, and on a kept first line, since the value is then two
  lines. The arm asserts nothing about `GREEN` on the hook side. Observed by AC1.
- **S3** — The local-hook half. Over the same record, `read --backend local-hook`, set up as unit
  65's AC12 sets it up, reads `verdict` as `GREEN` and `sha` as forty `b` characters. Observed by AC3.
- **S4** — Each staged break names the variable its plant reaches. The comment above the arm's
  assertion names `rec_sha` and the two breaks that turn it red: a `read_green_file` whose `sha` read
  keeps the CR, and one whose `sha` read prints every match again. Unit 65's §7 New-arm
  line for this suite stages its hook half red by these two breaks, observed on a scratch copy of
  `.githooks/pre-push`, and never on the `verdict` line. Observed by AC2.

## 3. Non-goals (OUT)

- The CR strip and the last-wins rule inside `read_green_file`. Those are unit 65's S15, and this unit
  only makes the arm able to see them.
- A `verdict` read in the hook's adoption path. Nothing in this build designs one, and the hook reads
  `verdict` only from a run dir's file (`.githooks/pre-push:2236`, `:2274`). The no-read assertion and
  the CRLF `fingerprint` line are `TOOL-dWitnessedBar-67`'s item for ids 1 and 12.
- The report's left-shift text, a checklist entry for "a staged red whose plant sits on input the
  changed code never reads". No clause of this build names that gate. S4's named variable is the
  regression this unit builds.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-65` — S15's CR strip and last-wins rule in `read_green_file`, and AC12's arm in `run-gates.gov.test.sh`, whose hook half this unit replants on `sha` (id 6)
- **hands-off** `TOOL-dWitnessedBar-67` — the CRLF `fingerprint` line beside this record and the assertion that the hook reads no `verdict` key, which the minors batch adds for the same AC12 defect at MEDIUM (ids 1 and 12, report item M1)
- **hands-off** `TOOL-dWitnessedBar-68` — the record, re-sited onto unit 56's `clean` plant at the path the local-hook reader reads, and AC3, regraded on the state the CLI prints (id 1 of the round-1 spec audit of units 66 and 67, item H1)
- **hands-off** `TOOL-dWitnessedBar-70` — the CR-reach canary that proves S1's CR reaches `read_green_file` before S2's compare counts, the staged reds of §7 recorded with their failing line from a Windows node, and §4 Evidence's "keeps a CR" answered in this unit's ledger (id 10, item B1)
- **hands-off** `TOOL-dWitnessedBar-73` — the every-key record beside S1, the gov canary guard naming `.githooks/pre-push`, the floor stated as a number, and the held-leg statement for §7 (ids 5, 12, 15 and 22 of the round-1 spec audit of units 66 and 67)

## 4. Design

### Evidence

- `read_green_file` sets `rec_sha`, `rec_fp`, `rec_blob`, `rec_man`, `rec_st`, `rec_reused` and
  `rec_reused_cache` from the keys `sha`, `fingerprint`, `manifest_blob`, `manifest`, `selftests`,
  `reused` and `reused_cache` (`.githooks/pre-push:1351-1369`).
  `sed -n 1351,1369p .githooks/pre-push | grep -c verdict` prints 0 at `2a8eed0d`.
- At the base each read is `awk -F'\t' '$1=="<key>"{print $2}'` (`.githooks/pre-push:1354`, `:1355`).
  It prints every match and keeps a CR. So S1's record gives `rec_sha` two lines, the second ending in
  CR, and S2's compare is red at the base. That is the arm's RED-first state before units 63 and 65
  build.
- The hook calls `read_green_file` once, at `.githooks/pre-push:1668`.
- The suite's floor is `FLOOR_ASSERTIONS=16` at the base (`tools/run-gates/run-gates.gov.test.sh:94`),
  stated absolutely beside the unit that last raised it.

### Inventory

Minted: nothing. No function, constant, plant, flag or file. The record of S1 is fixture data inside an
existing arm. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-65` (order 37). `TOOL-dWitnessedBar-67` builds at
order 39 and adds its lines beside this arm.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **Add a `rec_verdict` read to `read_green_file`** so the original AC12 could pass. That changes what
  the pre-push hook reads to decide a push, with no design and no consumer behind it.
- **Plant the CR on `fingerprint` instead of `sha`.** It reaches the strip as well. `sha` is chosen
  because S1 already needs two `sha` lines for last-wins, so one key carries both breaks and one
  compare grades both. The `fingerprint` line goes to unit 67 as a second key.
- **Keep the CR on `verdict` and assert the hook ignores it.** An assertion that a value is absent
  cannot go red when the strip is removed, which is the finding.

## 5. Production-readiness checklist

- security — no new write path. The arm writes one record in the suite's scratch directory.
- perf / scale — one sourced function and one Python read over a three-line file.
- error / empty / loading states — N/A: the arm reads a fixture it writes itself.
- observability — the failure line names `rec_sha` and prints its value with CR made visible.
- risks — a later rewrite that renames `rec_sha` reds the arm loudly, at its sourced call.
- testing — AC1 to AC3 by fixture and scratch copy. The arm under §7 at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the arm sources `read_green_file`, cut by `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push`
  from the built tree, and calls it on S1's record, `rec_sha` is forty `b` characters and
  `printf %s "$rec_sha" | wc -c` prints 40. `grep -n 'rec_sha' tools/run-gates/run-gates.gov.test.sh`
  names the arm's assertion.
  Red when: `read_green_file` keeps the CR on `sha`, or keeps the first of two `sha` lines.
  fixture: S1's record, written by the arm in the suite's scratch directory.
- **AC2** — When the same assertion runs against a scratch copy of `.githooks/pre-push` whose
  `read_green_file` has the CR strip removed from its `sha` read, it fails, and its failure line names
  `rec_sha`. It fails the same way against a scratch copy whose `sha` read prints every match.
  Red when: the arm stays green with the hook's CR strip removed, which means its plant sits on a key
  the hook never reads.
  fixture: scratch copies of `.githooks/pre-push` under `%TEMP%/<short-name>`.
- **AC3** — When `read --backend local-hook` reads S1's record, as unit 65's AC12 sets it up, it
  reads `verdict` as `GREEN` and `sha` as forty `b` characters, the same `sha` value AC1 reads.
  Red when: the local-hook reader keeps the CR on `verdict`, or the two readers part on `sha`.

## 7. Gates

`run-gates gov canary` · `pre-push self-test` · `memory hygiene`

`pre-push self-test` is named because S2 sources the hook's own `read_green_file`, and that leg
observes the hook's existing reads.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC3 · the hook half replanted on `sha`, staged red on a scratch copy of `.githooks/pre-push` by removing the CR strip from `read_green_file`'s `sha` read and by restoring print-every-match · FLOOR_ASSERTIONS raised by these assertions

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 65 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which key carries the hook half's CR (id 6)?** Options: (a) the second `sha` line; (b) a
  `fingerprint` line; (c) a new `verdict` read in `read_green_file`. (c) adds an undesigned read to the
  push decision, which widens what the hook reads beyond this unit's tier; veto 3 discards it. (a) and
  (b) both reach the strip. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. It grades the CR
  strip and last-wins with one compare on one variable, so it leaves the fewest open questions, and (b)
  is kept as unit 67's second key.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 64 and 65, id 6
  (HIGH, item H1).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-68, TOOL-dWitnessedBar-70 and TOOL-dWitnessedBar-73, promoted by the
  round-1 spec audit of units 66 and 67; nothing else moved.

## 10. Reuse audit

The seam is unit 65's AC12 arm in `tools/run-gates/run-gates.gov.test.sh`, extended in place, and the
cut-and-source idiom unit 65 already names for both hook and runner readers
(`awk '/^read_green_file\(\)/,/^}/'`). `python tools/codebase-map/reuse_lookup.py "strip a trailing carriage return from a key value record line"`
ranked `key`, `keys`, `records` and `read_conf_key`. None of them reads the green stamp, so no existing
seam fits beyond the arm named above. The runner's own strip is `${_rk_v%$'\r'}`
(`tools/run-gates/run-gates.sh:2393`), which unit 65 S14 keeps and this unit does not touch.

Recall terms used: `python tools/memory-recall/query.py "how does a staged red reach the variable the plant changes in the hook's green-stamp reader" --terms "staged red plant read_green_file rec_sha CR strip last key wins verdict record hook adoption"`
