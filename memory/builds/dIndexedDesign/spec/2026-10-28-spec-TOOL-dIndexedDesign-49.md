# TOOL-dIndexedDesign-49 — every cause composed into the `--dispatch` refusal is armed by its own clause text, and the cause list is derived from the code

**Status:** DEFERRED · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 19 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-47-promoted-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-47-promoted-fix-return.md) | research | TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-47-promoted-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-47-promoted-fix-brief.md) | research | TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-49-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-49-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 39 to 46
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md`)
confirmed finding **id 19 at HIGH**, report item **H1**, which it shares with ids 1 and 10
(`TOOL-dIndexedDesign-47` and `TOOL-dIndexedDesign-48`). Its finder graded it blocker and the skeptic
high. `TOOL-dIndexedDesign-41` S1 routes the design-exit refusal through the THIN site by `_d_why`, and S2
composes unit 1's two hand-off refusals into `_dx_msg`. `check-arms.py` arms a SITE, by its literal run
(`tools/memory-tree/check-arms.py:204-221`, `:791`), and interpolated text never enters that run. So any
fold gives its causes one signature, and no reading of `check-arms.py` can say whether the design-exit
cause has an arm.

This unit carries the skeptic's corrected fix. Each cause composed into the site is armed by a test line
carrying that cause's own clause text, and the list of causes is derived from the assignments in
`unattended.sh`, never typed. It repairs `TOOL-dIndexedDesign-41` and takes order 19, one above unit 41's
18.

## 2. Scope (IN)

- **S1** — In unit 16's pass commit, an act ahead of this unit's order. The `--dispatch` arm unit 16 §7
  declares for the design-exit refusal asserts the clause `_dx_msg` holds for the coverage refusal, and
  not the composed site's literal run. That clause opens with a literal run of 12 characters or more
  naming `design.coverage`, which unit 16 S7 already requires the refusal to name. Observed by AC1 and
  AC2.
- **S2** — The derived cause list. A cause is a double-quoted assignment to `_d_why` or `_dx_msg` in
  `tools/unattended/unattended.sh` whose `signature`, by `check-arms.py`'s own function, is 12 characters
  or longer. A pass-through such as `_d_why="$_dx_msg"` has no such run and is no cause. Each cause's
  signature must sit in at least one non-comment line of `tools/unattended/unattended.test.sh` that is not
  a `miss` assertion. At unit 16's pass commit the list holds the THIN clause and unit 16's coverage
  clause. At unit 1's pass commit it also holds unit 1's two hand-off clauses, which unit 1's own arms
  assert by their text. Observed by AC1 and AC2.
- **S3** — Unit 16's acceptance ledger carries the note `TOOL-dIndexedDesign-49 S3` under AC7's answer,
  naming each cause and the test line that arms it. Observed by AC3.

## 3. Non-goals (OUT)

- The site's literal run: `TOOL-dIndexedDesign-48`, id 10. The staged break on the THIN arm:
  `TOOL-dIndexedDesign-47`, id 1.
- A site per cause. It takes the census past the ceiling of 323, the defect unit 41 cures.
- A check-arms mode reading composed causes. It is a separate gate, and §4 Alternatives rejected says why
  it is not this unit's.
- The `fail 55` composition of unit 3's refusal: report id 18, MEDIUM, in `TOOL-dIndexedDesign-53`.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-16` — S7's design-exit refusal at `--dispatch` and the arm its §7 declares, which S1 has assert the clause text in that unit's pass commit (id 19)
- **consumes-from** `TOOL-dIndexedDesign-1` — its `_hov` policy-read and per-unit hand-off refusals, composed into `_dx_msg`, whose arms S2 counts at its pass commit (id 19)
- **consumes-from** `TOOL-dIndexedDesign-41` — S1's `_d_why` and S2's `_dx_msg`, whose assignments are S2's cause list (id 19)
- **hands-off** `TOOL-dIndexedDesign-47` — the design-exit arm carrying its clause and not the site's literal run, so that unit's deletion of the THIN arm leaves the site unarmed (id 1)

## 4. Design

### Evidence

- `tools/memory-tree/check-arms.py:204-221`: `signature` splits a message on `INTERP_RE` and keeps the
  longest literal part, so a cause held in a variable is invisible to a site's signature.
- `check-arms.py:791` arms a site on any numbered non-comment test line holding its signature. A negative
  assertion does not arm, as `TOOL-dRedressedBar-6` records of `armed_signatures`.
- At base `unattended.sh` holds no `_d_why` and no `_dx_msg`; units 16, 41 and 1 add them. Read
  2026-10-28.

### Data model

```
causes  = [assignment text of _d_why= / _dx_msg= in unattended.sh,  signature(text) >= 12 chars]
armed   = cause whose signature sits in >= 1 test line not starting with '#' or 'miss'
verdict = every cause armed, and len(causes) >= the floor the AC names
```

### Inventory

Minted: no identifier. One probe in the run's scratch, and one ledger note.

### Migration

None.

### Rollout

S1 lands in unit 16's pass, order 3. Unit 16's Edges block names it, and unit 1's names S2's count over
its two clauses. S3 and AC1 to AC3 are this unit's own pass at order 19, beside `TOOL-dIndexedDesign-47`,
`-48` and `-51`, and before 47, which consumes from it.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`: S1's arm, in unit 16's pass
- `memory/builds/dIndexedDesign/build/`: S3's ledger note and the recorded probe

### Alternatives rejected

- **Teach `check-arms.py` to read `_d_why` assignments as causes.** It changes a repo-wide meta-gate for
  one site, and the variable names are this build's local spelling. A probe over the two files proves the
  same thing for this site.
- **Arm each cause by the full printed message.** Lost to `TOOL-dIndexedDesign-47`: a line carrying the
  site's literal run arms the site, so the THIN deletion could no longer unarm it.

## 5. Production-readiness checklist

- security — N/A: no refusal changes; one arm's assertion text and a probe.
- perf / scale — one regex pass over two files per commit read.
- error / empty / loading states — an empty cause list is red, never a pass.
- observability — the recorded probe names each cause and the line that arms it.
- risks — a cause written by a later unit outside `_d_why` or `_dx_msg` escapes the list. The list floor
  in AC1 and AC2 reds on a missing known cause.
- testing — AC1 and AC2 by the probe and a staged break, AC3 by a ledger grep.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe that loads `tools/memory-tree/check-arms.py` by path runs S2's
  derivation over a worktree at unit 16's pass commit, taking S2's two files, the driver and its test
  file, as its two path arguments and reading them as text, it lists at least two causes, the THIN
  clause and the coverage clause naming `design.coverage`, and every cause counts at least one arming
  line.
  Red when: a cause counts 0, or the list holds fewer than two.
  figure: the list is DERIVED at each commit read; the floor of two is PINNED by unit 16 S7 and unit 41 S1.
- **AC2** — When AC1's `python -c` probe runs at unit 1's pass commit, it lists at least four causes,
  each armed. When the same probe runs with its second path argument pointed at a scratch copy of that
  commit's test file, the design-exit arm line deleted from the copy, the coverage clause counts 0.
  Red when: a cause counts 0 at the commit, or the deletion leaves the coverage clause armed.
- **AC3** — When `grep -n "TOOL-dIndexedDesign-49 S3"` runs over unit 16's acceptance ledger, it prints
  the note under AC7's answer, naming `design.coverage`.
  Red when: the note is missing or stands as its own `- AC` line.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `unattended kit gate` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · the design-exit refusal at `--dispatch` asserted by its clause text, staged by deleting that arm line · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 39 to 46, id 19
  (HIGH, item H1, shared with ids 1 and 10), on the skeptic's corrected fix, repairing
  TOOL-dIndexedDesign-41 S1 and S2.

## 10. Reuse audit

The seam is `check-arms.py`'s own `signature` function, loaded by path, so the probe measures a cause
exactly as the gate measures a site. The probe
`python tools/codebase-map/reuse_lookup.py "assert each composed refusal cause by its own test line when several causes share one fail site"`
ranked `fail`, `refusal`, `Refusal`, `DesignRefusal` and `check_line`. None enumerates composed causes,
so no existing seam fits beyond `signature`.

Recall terms used: `python tools/memory-recall/query.py "how is a composed fail site armed when several refusals share one message" --terms "check-arms signature composed site armed substring arm line THIN dispatch fail 49 census"`
