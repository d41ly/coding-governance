# TOOL-dWitnessedBar-96 — unit 92's note check reads a token's value through an optional pattern column, so a derivation note must name the launcher and exit 0

**Status:** CLOSED · rev-2 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 49 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-96-deviation-961.md](../build/2026-10-25-build-TOOL-dWitnessedBar-96-deviation-961.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-96-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-96-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-96-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-96-1-builder-return.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-96-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-96-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-96-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-96-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-96-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-96-reground-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 91 and 92
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-91-spec-audit-round1.md`)
confirmed finding **id 15 at HIGH**, report item **H4**. Ids 2 and 6 are the same defect, found by the
coherence and grounding lenses at MEDIUM, item M1. The report asks that the three corrections be
reconciled into one note spelling. This unit settles that spelling and grades it, and
`TOOL-dWitnessedBar-97` takes ids 2 and 6 and adds the staged reds only their fixes name.

`TOOL-dWitnessedBar-92` §4 "The note check" tests a row's token with `index($0, t)` (spec-92 line
321 at `d31ee066d`), which asks only that the literal appears. 92 S4 asks each close-time derivation
note to quote what `resolve_python` printed and the derivation's exit, and the four rows that grade
those notes carry the bare token `resolve_python:` (spec-92 lines 296-299 at `d31ee066d`). A note
reading `resolve_python: , exit 0` passes, so 92 AC4's staged break cannot print its `NO NOTE`. The
same presence test passes row `90|S10` on a note that lists `AC1` beside the five criteria it names.

This unit adds an optional sixth field to the note table's rows, a pattern the note's line must
match, and gives it to the five rows where presence is not enough. It repairs `TOOL-dWitnessedBar-92`
and builds one step after it (order 49).

## 2. Scope (IN)

- **S1** — id 15. The pattern column. A note-table row becomes
  `<unit>|<item>|<ledger unit>|<answer>|<token>[|<pattern>]`. In 92 §4's note check, three fragments
  are rewritten, and nothing else moves:
  - on spec-92 line 317 at `d31ee066d`, `read -r u s l a t; do` becomes `read -r u s l a t p; do`;
  - on spec-92 line 321, `-v t="$t" '` becomes `-v t="$t" -v p="$p" '`;
  - on spec-92 line 321, `index($0, t))` becomes `index($0, t)) && (p == "" || $0 ~ p)`.

  A row with no pattern is graded as before. A row with one selects a note only when its line holds
  the token and matches the pattern as an awk extended regular expression. A pattern holds no `|`,
  because `|` delimits the row. `TOOL-dWitnessedBar-93`, `TOOL-dWitnessedBar-94` and
  `TOOL-dWitnessedBar-97` each rewrite other fragments of the same script, and none of them touches
  these three. Observed by AC1, AC2 and AC3.
- **S2** — ids 15, 2 and 6 reconciled. The derivation note's spelling. Each close-time run of the
  owner derivation that 92 S4 records is a continuation line under its criterion's answer, opening
  with the label `TOOL-dWitnessedBar-92 S4` and holding, on that one physical line, the backticked
  `resolve_python: <value> exit <rc>`. `<value>` is the one line `resolve_python` printed on stdout
  (`tools/lib/resolve-python.sh#resolve_python`): an override, the caller's argument or
  `GOV_PYTHON`, as given; the bar's memo launcher, absolute; or, for a launcher name, the
  forward-slashed executable its probe named when that is a file, and the name otherwise. `<rc>` is
  the derivation's exit. This settles 92 S4's "`resolve_python: <the path it printed>` and the
  derivation's exit" into one span: the value is a path only where the probe or the memo gave one.
  Observed by AC1.
- **S3** — id 15. Five rows restated. These rows stand in place of the rows of 92 §4's note table that share
  their first four fields. The four `92|S4` rows grade S2's spelling with an exit of 0; the `90|S10`
  row grades 90 S10's list as one backticked span, so a sixth criterion beside it reads as no note.

  ```text
  92|S4|88|AC6|resolve_python:|resolve_python: [^ ,]*py[^ ,]* exit 0([^0-9].*)?$
  92|S4|88|AC18|resolve_python:|resolve_python: [^ ,]*py[^ ,]* exit 0([^0-9].*)?$
  92|S4|89|AC9|resolve_python:|resolve_python: [^ ,]*py[^ ,]* exit 0([^0-9].*)?$
  92|S4|89|AC12|resolve_python:|resolve_python: [^ ,]*py[^ ,]* exit 0([^0-9].*)?$
  90|S10|89|AC12|AC4 AC6 AC7 AC10 AC12|`AC4 AC6 AC7 AC10 AC12`
  ```

  `[^ ,]*py[^ ,]*` asks for one run holding `py` and no space or comma: a launcher name holds it, and
  so does the executable path node d's resolver prints (§4 Evidence). Every refusal line
  `resolve_python` writes to stderr fails it, the first opening `resolve_python: no usable python
  launcher` and the last `resolve_python: tried:` included, and so do an empty value and any exit but
  0. A value holding a space or a comma fails it too (§8 F4). Observed by AC1, AC2 and AC3.
- **S4** — id 15. 92 AC4's staged break restated. In place of "a note that has lost its
  `resolve_python:` path", the break is a note reading `resolve_python: , exit 0`, which prints
  `NO NOTE 92 S4 resolve_python:`. Observed by AC2.
- **S5** — Unit 92 answered. Unit 92's acceptance ledger records AC2's output as a note under its
  `- AC4` answer. The note is a continuation line, two spaces in, opening with the label
  `TOOL-dWitnessedBar-96 S5` and carrying the backticked `resolve_python: , exit 0` on that one
  physical line. Observed by AC4.

## 3. Non-goals (OUT)

- Rewording the spec text of unit 92. Its S4 spelling, its five rows and its AC4 staged break are
  superseded by name here and answered in its ledger, as `TOOL-dWitnessedBar-92` §3 does for unit 90.
- The staged reds only ids 2 and 6 name: a pasted refusal line and a non-zero exit, and the correction
  of 92 AC4's Red-when. `TOOL-dWitnessedBar-97` takes them.
- Two note-table rows per run, `py=` and `exit 0`, the way id 6's fix offered. §4 "Alternatives
  rejected" says why.
- The placement test (`TOOL-dWitnessedBar-93`), the label anchor (`TOOL-dWitnessedBar-94`) and the
  ledgers the check reads (`TOOL-dWitnessedBar-97`).
- The report's left-shift text, the checklist class `staged-break-substitutes-a-synthetic-value` as a
  spec-lint rule. No clause of this build names it.
- Unit 28, deferred unbuilt on asks TOOL-dWitnessedBar-101 to -103. No item here waits on it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-92` — §4's note check, whose row read and token test S1 extends, its note table's four `92|S4` rows and `90|S10` row, which S3 restates, S4's note spelling, which S2 replaces, and AC4's staged break, which S4 restates (id 15)
- **hands-off** `TOOL-dWitnessedBar-97` — the staged reds only ids 2 and 6 name, a pasted refusal line and a non-zero exit, each graded through S3's pattern, the correction of 92 AC4's Red-when, the script token on S2's note, and the composition of S1's fragments and S3's rows into the note check every close-time run uses (ids 2, 3 and 6)

## 4. Design

### Evidence

Read on 2026-11-21 at `d31ee066d`. Unit 92 is CLOSED (`186cad841`), records only. Its rev-3
re-ground left §4's note check byte-identical and its four `92|S4` rows and `90|S10` row unchanged,
moving only their line numbers (DERIVED 2026-11-21, §4 diffed against `a34fd39d9~1`).

- `tools/lib/resolve-python.sh@d31ee066d:50` tries `"${1:-}" "${GOV_PYTHON:-}" python3 python py`
  in order, and `:68` prints an override as given and, for the three launcher names, the
  forward-slashed `sys.executable` its probe printed when `[ -f ]` holds, else the name. `:42-48`
  print the memo launcher of `GATE_RESOLVED_PY`, which `:42` admits only absolute. Every refusal
  line, in `:80-185`, opens `resolve_python: ` and goes to stderr. Sourced on node d with no
  `GOV_PYTHON` and no memo, it printed an absolute `.../python.exe` path holding `py` and no space or
  comma, exit 0 (DERIVED 2026-11-21).
- Spec-92 line 321 at `d31ee066d` tests `(t == "" || index($0, t))`, line 317 reads
  `read -r u s l a t; do`, lines 296-299 give each `92|S4` row the token `resolve_python:`, and line
  284 gives row `90|S10` the token `AC4 AC6 AC7 AC10 AC12`.
- Probed on 2026-11-21 at `d31ee066d` against a scratch 88 ledger whose `- AC6` answer carries one
  continuation note labelled `TOOL-dWitnessedBar-92 S4`. Through spec-92's script with the row
  `92|S4|88|AC6|resolve_python:`, a note holding `resolve_python: , exit 0` printed `NOTES OK 1`.
  Through the script with S1's fragments and S3's row, notes holding `resolve_python: python3 exit 0`,
  `resolve_python: python exit 0`, `resolve_python: py exit 0` and the path node d's resolver printed
  then `exit 0` each printed `NOTES OK 1`. Notes holding `resolve_python: , exit 0`,
  `resolve_python: exit 0`, `resolve_python: none exit 0`, `resolve_python: python3 exit 5`,
  `resolve_python: python3 exit 05`, `resolve_python: C:/Program Files/Python315/python.exe exit 0`,
  and the resolver's first refusal line, its `tried: python3 python py` line or a `did not run` line
  each followed by `exit 0`, each printed `NO NOTE 92 S4 resolve_python:`. Each held with the
  fragments of 93 S1, 94 S1 and 97 S8, as their specs read on 2026-11-21, applied beside S1's.
- On the same date, a scratch 89 ledger whose `- AC12` note held the backticked
  `AC1 AC4 AC6 AC7 AC10 AC12` printed `NOTES OK 1` through spec-92's script and
  `NO NOTE 90 S10 AC4 AC6 AC7 AC10 AC12` through S1's with S3's row, as did one holding
  `AC4 AC6 AC7 AC10 AC12 AC13`. The backticked `AC4 AC6 AC7 AC10 AC12` printed `NOTES OK 1` through
  both.
- On the same date, a scratch 92 ledger whose `- AC4` answer carries a continuation note labelled
  `TOOL-dWitnessedBar-96 S5` and holding the backticked `resolve_python: , exit 0` printed
  `NOTES OK 1` for row `96|S5|92|AC4|resolve_python: , exit 0` through S1's script.
  `2026-11-19-build-TOOL-dWitnessedBar-92-1-acceptance-ledger.md` is the one file
  `*TOOL-dWitnessedBar-92-*acceptance-ledger*` matches, and its one `- AC4` answer reads OWED to the
  close (PINNED 2026-11-21 by `grep -cE '^- AC4 '`).
- In awk, `-v` processes escape sequences in its value. No pattern of S3 holds a backslash.

### Inventory

Minted: the note table's optional pattern field; the ledger note labelled
`TOOL-dWitnessedBar-96 S5`. No function, constant, plant, flag or file in the product. Naming cells:
none apply.

### Migration

None: no stored data changes. A five-field row reads as before, so 92's other rows are unchanged.

### Rollout

The pass takes order 49, one above unit 92's 48, beside units 93, 94 and 95, and writes this unit's
acceptance ledger with AC1 to AC4 owed, as units 91 and 92 did (`b7e2e3d8d`, `186cad841`). At the
close, after every unit is terminal, AC1 to AC3's fixtures run, S5's note is written and AC4 reads
it. Every derivation note is 92 S4's, written at the close in S2's spelling in the ledgers of units
88 and 89; this unit writes none of them. `TOOL-dWitnessedBar-97` S8, at order 50, composes S1's
fragments and S3's rows into the note check every close-time run uses.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/`, this unit's acceptance ledger at the pass, and S5's note in
  `2026-11-19-build-TOOL-dWitnessedBar-92-1-acceptance-ledger.md` at the close
- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-96.md`, its status header
- `memory/builds/dWitnessedBar/RUN.md`
- `memory/builds/dWitnessedBar/README.md`, `memory/backlog/TOOL.md` and `memory/LIVE.md`, rendered
  by `gen_build_index.py --write`, with any `gen:spec-records` region the `--write` moves
  (`TOOL-dWitnessedBar-92` S5)

### Alternatives rejected

- **Two rows per run, `py=` and `exit 0`, id 6's fix.** It moves 92 AC4's count from 5 to 9 and AC12's
  from 29 to 33, and grades the word and the exit on separate substrings, so `py= exit 0` passes. One
  pattern grades both on one span.
- **`resolve_python: (python3?|py|[^ ,]+)[ ,].*exit 0`, the report's pattern.** It holds `|`, which
  splits the row, and its `[^ ,]+` arm admits every word, so the alternation adds nothing.
- **Require an absolute path after `resolve_python:`.** `resolve_python` prints an override as given,
  and a launcher name where its probe named no file, so a correct build would red, as the report's
  skeptic notes.

## 5. Production-readiness checklist

- security — no new write path. The fixture ledgers sit under the run's scratch directory.
- perf / scale — one more regular-expression test per row that carries a pattern.
- error / empty / loading states — an empty value, a refusal line and a non-zero exit each print
  `NO NOTE`.
- observability — a derivation note names the resolver's value and the exit on one line.
- risks — a value holding no `py`, or a space or a comma, reds a correct note: an override such as a
  `GOV_PYTHON` without `py`, or an executable under a directory whose name holds a space. Node d's
  resolver prints neither, and this build sets no `GOV_PYTHON` (§4 Evidence, §8 F4).
- testing — AC1 to AC3 by fixture at the close; AC4 by ledger.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch root holding one
  `memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-88-*acceptance-ledger*` file whose `- AC6`
  answer carries one continuation line, two spaces in, opening `TOOL-dWitnessedBar-92 S4` and holding
  the backticked `resolve_python: python3 exit 0`, 92 §4's note check with S1's fragments, run from
  that root and fed S3's row for `92|S4|88|AC6`, prints `NOTES OK 1` and exits 0.
  Red when: a note in S2's spelling, with a value `resolve_python` prints, reads as no note.
  fixture: a scratch root under the run's scratch directory.
- **AC2** — In the same scratch root with the note holding `resolve_python: , exit 0` instead, the
  check with S1's fragments and S3's row prints `NO NOTE 92 S4 resolve_python:` and exits 1. Spec-92's
  unreplaced script fed `92|S4|88|AC6|resolve_python:` prints `NOTES OK 1` on the same ledger.
  Red when: a note that names no interpreter passes the derivation's row.
  fixture: a scratch root under the run's scratch directory.
- **AC3** — In a scratch root holding one
  `memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89-*acceptance-ledger*` file whose `- AC12`
  answer carries a continuation line opening `TOOL-dWitnessedBar-90 S10` and holding the backticked
  `AC1 AC4 AC6 AC7 AC10 AC12`, the check with S1's fragments and S3's `90|S10` row prints
  `NO NOTE 90 S10 AC4 AC6 AC7 AC10 AC12` and exits 1. With the backticked span reading
  `AC4 AC6 AC7 AC10 AC12`, it prints `NOTES OK 1`.
  Red when: a note listing a criterion beyond the five passes as 90 S10's list.
  fixture: a scratch root under the run's scratch directory.
- **AC4** — When 92 §4's note check with S1's fragments is fed
  `96|S5|92|AC4|resolve_python: , exit 0`, it prints `NOTES OK 1`.
  Red when: unit 92 AC4 is recorded against the presence-only token.
  permission: the ledger is written at the close.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` are owed for the ledgers under `memory/`. AC1 to AC3 run by
fixture at the close. This unit adds no arm and moves none, so it declares no `New arm:` line, and
`TOOL-dWitnessedBar-92` §4's owner derivation, which takes the place of 88 S6's (92 S12), still names
unit 90 the floor's owner: run at `d31ee066d` it printed 28 and
`spec/2026-10-25-spec-TOOL-dWitnessedBar-90.md`, exit 0 (PINNED 2026-11-21).

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 92 is itself
  derived and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-90` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which note spelling reconciles ids 15, 2 and 6?** Options: (a) one backticked
  `resolve_python: <word> exit <rc>` graded by one pattern; (b) `py=<word> exit <rc>` graded by two
  rows, id 6's fix; (c) the launcher word alone, with the Red-when's exit claim dropped, id 2's first
  fix. (c) leaves the exit ungraded, which 92 S4 asks to record, so veto 1 discards it. (b) admits a
  word and an exit graded apart. (a) grades both on one span and keeps 92's counts. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the most feature-rich survivor. S2 now spells the word
  `<value>` (F4).
  widens: none · relaxes: none
- **F3 — Which unit takes ids 2 and 6, the medium-graded item of the same defect?** Options: (a) this
  unit; (b) the minors batch, as M4 places every MEDIUM. The task's disposal rule puts every MEDIUM in
  the batch, so (a) fails it; veto 1 discards it. Under (b) this unit settles the spelling and the
  batch adds the reds only ids 2 and 6 name. RESOLVED (agent, 2026-10-25, delegated): (b), rung 3,
  the one survivor, the precedent `TOOL-dWitnessedBar-91` §8 F2 set.
  widens: none · relaxes: none
- **F4 — Which value does S3's pattern admit, now that `resolve_python` may print an executable
  path?** Options: (a) keep `[^ ,]*py[^ ,]*`, one run with no space or comma; (b) a run closed by the
  span's backtick, so a value may hold spaces when its last word holds `py`. Both meet AC1 to AC4
  (§4 Evidence). (b) admits a path holding a space, but also the refusal's last line
  `resolve_python: tried: python3 python py` before `exit 0`, so a pasted refusal passes, the case S3
  names as failing and unit 97 stages. (a) refuses every refusal line and reds a correct note only on
  a value holding a space or a comma, which node d's resolver does not print. RESOLVED (agent,
  2026-11-21, delegated): (a), rung 3, the most feature-rich survivor: it keeps S3's refusal clause,
  which (b) loses.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 91 and 92, id 15
  (HIGH, item H4; ids 2 and 6 are its medium-graded item M1, batched into TOOL-dWitnessedBar-97).
- rev-2 · 2026-11-21 · §1 to §8 · §10 · re-grounded at `d31ee066d` per
  2026-11-19-prompt-TOOL-dWitnessedBar-96-reground-brief. Spec-92 citations move to rev-3's lines;
  `resolve_python` now prints an override, a memo launcher or an executable path, so S2 spells
  `<value>` and S3's claims follow, with §8 F4 keeping S3's pattern; the pattern is a sixth field;
  Evidence re-probed and re-pinned; Files touched listed exactly; criteria unchanged.

## 10. Reuse audit

The seam is 92 §4's note check and its note table; S1 widens the row by one optional field and adds
no reader. `resolve_python` (`tools/lib/resolve-python.sh`) is the one interpreter resolver, and S2
quotes what it prints. `python tools/codebase-map/reuse_lookup.py "match a ledger note token value against a pattern not only its presence"`
ranked `note`, `resolve_prefix_token`, `read_policy_value` and `read_ledger` first on 2026-11-21,
then `match_expr` and `resolve_pattern_sets`. None reads acceptance-ledger notes:
`tools/lib/legacy_ledger.py#read_ledger` reads a registered row file. So no existing seam fits
beyond 92's script and the resolver named above.

Recall terms used: `python tools/memory-recall/query.py "how does a ledger note record the interpreter resolve_python printed and the exit" --terms "resolve_python launcher word note token pattern exit code ledger presence value bare launcher refusal"`
