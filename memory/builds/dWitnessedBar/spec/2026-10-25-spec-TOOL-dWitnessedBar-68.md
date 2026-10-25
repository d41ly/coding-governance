# TOOL-dWitnessedBar-68 — the CRLF record arm writes a record the local-hook reader admits, where that reader looks, and grades it on the state the CLI prints

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 39 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md) | research | TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-68-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md) | research | TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 66 and 67
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**. No other id shares that item.

`TOOL-dWitnessedBar-66` S1 fixes its record at three lines: `verdict`, `sha`, `sha`. S3 and AC3 then
expect `read --backend local-hook` to read that record as `GREEN` with `sha` as forty `b` characters.
On a correct build of `TOOL-dWitnessedBar-56`, `read_local_verdict` reads `NONE` for a record with
neither `reused` nor `reused_cache` (S7) and for one with no `selection` key (S8). The CLI reads
`<common-dir>/gate-verdict/<tree hash>`, not a scratch file, and prints the QUERIED SHA, never the
record's `sha` key (`TOOL-dWitnessedBar-6` S3, S4). So AC3 cannot pass as written, and unit 65's AC12
carries the same expectation.

This unit builds the record from the plant the local-hook reader admits, puts it where that reader
looks, and grades the local-hook half on the state the CLI prints. The reader's CR strip and
last-wins rule are graded through keys that change that state. It repairs `TOOL-dWitnessedBar-66` and
builds one step after it (order 39).

## 2. Scope (IN)

- **S1** — The record. The AC12 arm in `tools/run-gates/run-gates.gov.test.sh` builds its record with
  `python verdict_backends.py --fixture --plant clean`, the plant unit 56's AC6 reads as `GREEN`. The
  record therefore carries every line that plant writes, among them `reused 0`, `reused_cache 0` and
  `selection none` (unit 56 S4). It sits at the fixture's `<common-dir>/gate-verdict/<tree hash>`,
  where `<tree hash>` is the fixture HEAD's tree (unit 6 S4). The arm then replaces three of the
  plant's keys. The plant's other lines come first, then these lines in this order:

  | line | bytes |
  |---|---|
  | 1 | `verdict<TAB>GREEN<CR><LF>` |
  | 2 | `sha<TAB>` followed by forty `a` characters, then `<LF>` |
  | 3 | `sha<TAB>` followed by forty `b` characters, then `<CR><LF>` |
  | 4 | `reused_cache<TAB>1<LF>` |
  | 5 | `reused_cache<TAB>0<CR><LF>` |

  Observed by AC1.
- **S2** — The hook half reads the same file. Unit 66 S2's call `read_green_file` is given the path of
  S1's record, so both halves read one file. Unit 66 S2's assertion on `rec_sha` is unchanged.
  Observed by AC2.
- **S3** — The local-hook half is graded on the state the CLI prints. `read --backend local-hook`, run
  over S1's fixture as unit 56's AC6 runs the `clean` case, prints one line of unit 6 S3's form. Its
  state field reads `GREEN`. The half asserts nothing about the record's `sha` key, which the CLI line
  does not print. Two lines of S1 make that state depend on the reader's normalisations:
  - line 1 reads `GREEN` only when the reader strips the CR;
  - lines 4 and 5 read as an admitted `reused_cache 0` only when the last line wins, because a kept
    `1` is a non-zero `reused_cache`, which unit 56 S7 reads as `NONE`.

  Observed by AC3.
- **S4** — The two criteria that expected the record's `sha` from the CLI are answered by name. The
  acceptance ledger of `TOOL-dWitnessedBar-66` answers its AC3, and that of `TOOL-dWitnessedBar-65`
  answers the local-hook half of its AC12, each naming this unit's AC3 as the observation that
  replaces "the same `sha` value". Observed by AC4.

## 3. Non-goals (OUT)

- A Python function that returns the parsed record so the two readers' `sha` values can be compared.
  §8 F2 says why none is minted.
- Loosening unit 56's S7 or S8 refusals so a three-line record reads `GREEN`.
- Making the planted CR reach either reader's strip. The read form that keeps the CR is
  `TOOL-dWitnessedBar-69`'s, and the arm's proof that it reaches the hook's strip is
  `TOOL-dWitnessedBar-70`'s.
- The `fingerprint` line beside this record, which is `TOOL-dWitnessedBar-67`'s S2 and
  `TOOL-dWitnessedBar-72`'s.
- The report's left-shift text, a checklist entry for "an AC's expected output must be one the named
  actor emits". No clause of this build names that gate. AC3's state-field grading is the regression
  this unit builds.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-56` — the `clean` plant and `read_local_verdict`'s reuse-pair refusal (S4, S7), which S1's record is built from and S3's repeated `reused_cache` rests on (id 1)
- **consumes-from** `TOOL-dWitnessedBar-66` — S1's record and the S2 and S3 halves, which this unit re-sites onto the plant's path and regrades on the printed state (id 1)
- **hands-off** `TOOL-dWitnessedBar-78` — S1's plant call spelled through the suite's `PYBIN`, and the registry the local-hook read globs covered by the gov canary's guard (ids 23 and 5 of the round-1 spec audit of units 68 to 73)

## 4. Design

### Evidence

- Unit 56 S4 has the adopt plants carry `reused 0`, `reused_cache 0` and `selection none`
  (`spec/2026-10-25-spec-TOOL-dWitnessedBar-56.md:63-65`). S7 reads `NONE` for a non-zero
  `reused_cache`, a `reused` with no `reused_cache`, or neither key (`:72-74`). S8 reads `NONE` for no
  `selection` key (`:75-77`). AC6 reads `clean` as `GREEN` (`:253-257`).
- Unit 6 S3 prints `verdict: <backend> · <state> · <sha8> · <why>` for `--sha <sha>`
  (`spec/2026-10-25-spec-TOOL-dWitnessedBar-6.md:49-53`). S4 reads
  `<common-dir>/gate-verdict/<tree hash>` and stands on a `verdict` line reading `GREEN` (`:54-56`).
- No clause of units 6, 40, 41 or 56 has `read_local_verdict` read the record's `sha` key. A grep of
  those four specs for `read_local_verdict` finds S4 of unit 6 and S7 and S8 of unit 56, none of which
  names `sha`.
- `tools/run-gates/verdict_backends.py` is not in the tree at `df0a656d`, so the plant and the reader
  exist only as those specs state them.

### Inventory

Minted: nothing. No function, constant, plant, flag or file. S1's lines are fixture data inside an
existing arm. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 39, after `TOOL-dWitnessedBar-66` (38). Order 39 is shared with
`TOOL-dWitnessedBar-67`, `TOOL-dWitnessedBar-69` and `TOOL-dWitnessedBar-70`, and M6's first condition
fails for it, since 67, 68 and 70 all write `run-gates.gov.test.sh`. Dispatch is strictly sequential
and sorts a tie by id string (`tools/workflows/unattended-build.js:76-80`, `:612`), so the tie is
recorded and not acted on, as unit 67 S16 recorded order 6's.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **Keep the three-line record and grade the local-hook half `NONE`.** It observes unit 56's refusal,
  not the CR strip or the last-wins rule, which is what AC12 exists to grade.
- **Write the record in the suite's scratch directory and point the reader at it.** The CLI takes a
  SHA and resolves the path itself (unit 6 S3, S4), so a path flag would be a new public surface.

## 5. Production-readiness checklist

- security — no new write path. The arm writes one record inside its own fixture.
- perf / scale — one plant call and one CLI read per run.
- error / empty / loading states — N/A: the arm reads a fixture it writes itself.
- observability — the failure line names the state the CLI printed and the line of S1 that decides it.
- risks — a later change to the `clean` plant's key set flows into S1 unchanged, since S1 replaces only
  three keys.
- testing — AC1 to AC3 by fixture and scratch copy, AC4 by ledger. The arm under §7 at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the arm has built S1's record, `od -c` over `<common-dir>/gate-verdict/<tree hash>`
  shows `\r \n` after `GREEN`, after the forty `b` characters and after the `reused_cache` value `0`.
  `grep -c '^reused_cache' <record>` prints 2, and `grep -c '^selection' <record>` prints at least 1.
  The path's last segment equals `git rev-parse HEAD^{tree}` run in the fixture.
  Red when: the record lacks a key the `clean` plant writes, or sits at a path the reader never reads.
  fixture: the `clean` plant, which `TOOL-dWitnessedBar-56` builds at order 32.
- **AC2** — When the arm calls the sourced `read_green_file` with S1's record path, `rec_sha` is forty
  `b` characters and `printf %s "$rec_sha" | wc -c` prints 40.
  Red when: the hook half reads a different file from the local-hook half.
- **AC3** — When `read --backend local-hook` runs over S1's fixture, the line it prints carries
  `· GREEN ·` as its state field. Against a scratch copy of `verdict_backends.py` whose
  record read keeps the first of a repeated key, the same read prints `· NONE ·`.
  Red when: the reader keeps the first `reused_cache` line, or the half asserts a value the CLI line
  does not print.
- **AC4** — When `grep -n 'AC3' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-66*acceptance-ledger*`
  and `grep -n 'AC12' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-65*acceptance-ledger*` run at
  the close, each line names `TOOL-dWitnessedBar-68` and its AC3.
  Red when: either criterion is recorded green on a `sha` value the CLI never printed.

## 7. Gates

`run-gates gov canary` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close, as every leg
whose subject is `kit` or whose chunk is `selftests` is (`tools/run-gates/run-gates.sh:3129-3131`).
The close sets it through `SELFTESTS_OWED_PATHS="tools/"` (`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC3 · the AC12 record re-sited onto the `clean` plant with its CRLF `verdict` line and repeated `reused_cache`, staged red by a scratch `verdict_backends.py` whose record read keeps the first of a repeated key (reaches the printed state) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 66 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — How is the local-hook half's agreement with the hook half graded (id 1)?** Options: (a) grade
  the printed state alone, with the CR strip and last-wins rule read through the `verdict` and
  `reused_cache` lines that decide it; (b) mint a function in `verdict_backends.py` that returns the
  parsed record and assert its `sha` field. No clause has `read_local_verdict` read `sha` (§4
  Evidence), so (b) compares a value no local-hook decision uses, and its red would flag no wrong
  verdict. (a) grades both normalisations on keys whose value changes the verdict. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3. It satisfies AC1 to AC4 and is tie-broken by fewer open
  questions, since it mints no identifier.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 66 and 67, id 1
  (HIGH, item H1).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-78, promoted by the round-1 spec audit of units 68 to 73; nothing else
  moved.

## 10. Reuse audit

The seam is unit 66's replanted AC12 arm in `tools/run-gates/run-gates.gov.test.sh`, extended in
place, and unit 56's `clean` plant, reused as the record's base rather than restating its keys.
`python tools/codebase-map/reuse_lookup.py "read a tab separated key value record file line by line keeping carriage return"`
ranked `read`, `read_text`, `key`, `keys` and `records`, none of which reads the per-tree verdict, so
no existing seam fits beyond the two named above.

Recall terms used: `python tools/memory-recall/query.py "how does the green record reader keep a CR so the strip is exercised on Git for Windows" --terms "read_green_file rec_sha CR strip CRLF gawk text mode command substitution read -r canary staged red"`
