# TOOL-dIndexedDesign-48 — the composed THIN site opens with a literal run no other `fail` message or arm line carries, and the THIN arm is re-pinned to it

**Status:** DEFERRED · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 19 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-48-deviation-481.md](../build/2026-10-28-build-TOOL-dIndexedDesign-48-deviation-481.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 39 to 46
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md`)
confirmed finding **id 10 at HIGH**, report item **H1**, which it shares with ids 1 and 19
(`TOOL-dIndexedDesign-47` and `TOOL-dIndexedDesign-49`). `TOOL-dIndexedDesign-41` S1 composes the THIN
site as `fail 49 "--dispatch declares a build pass for a unit $_d_why: $unit ($_d_spec)"`. Its signature,
the longest literal run, is `--dispatch declares a build pass for a unit`, which five arm lines of
`tools/unattended/unattended.test.sh` carry. The site therefore reads armed by the MISSING,
consumes-from and ask-held arms as well as the THIN one.

This unit takes id 10's sound fix. The composed site opens with a literal run that no other `fail`
message in `unattended.sh` and no other arm line holds, and the THIN arm is re-pinned to it. It repairs
`TOOL-dIndexedDesign-41` and takes order 19, one above unit 41's 18.

## 2. Scope (IN)

- **S1** — In unit 16's pass commit, an act ahead of this unit's order. Unit 41 S1's composed THIN site
  is written as
  `fail 49 "--dispatch refuses a build pass for a unit not ready to build: $_d_why: $unit ($_d_spec)"`,
  which supersedes the literal unit 41 S1 spells. For a THIN spec, `_d_why` holds the clause the site
  prints today, from `whose spec grades THIN` to `what done MEANS for it`; otherwise it holds `_dx_msg`.
  The site's signature is the run `--dispatch refuses a build pass for a unit not ready to build`.
  Observed by AC1 and AC2.
- **S2** — In the same commit, the THIN arm at `tools/unattended/unattended.test.sh:6336` asserts the new
  printed text, the literal run followed by the THIN clause. It is the one non-comment line of the suite
  carrying the run. Observed by AC2.
- **S3** — Unit 41's acceptance ledger carries the note `TOOL-dIndexedDesign-48 S3` under AC2's answer,
  naming the literal run as the site's signature. Observed by AC3.

## 3. Non-goals (OUT)

- The staged break that proves the THIN arm is the site's only arm: `TOOL-dIndexedDesign-47`, id 1.
- The arm for the design-exit cause, which a shared site cannot give: `TOOL-dIndexedDesign-49`, id 19.
- A site of its own for the design-exit refusal. It takes the census to 324 against the ceiling of 323,
  the defect unit 41 exists to cure.
- The MISSING, consumes-from and ask-held sites and their arms: unchanged.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-16` — S7's `--dispatch` call of `check_design_exit` after the THIN case, in whose pass commit S1 and S2 land (id 10)
- **consumes-from** `TOOL-dIndexedDesign-41` — S1's composed THIN site and `_d_why`, whose literal S1 supersedes, and AC2, whose ledger answer S3 annotates (id 10)
- **hands-off** `TOOL-dIndexedDesign-47` — the site's own literal run and the re-pinned THIN arm, against which that unit's staged break deletes the THIN arm (id 1)
- **hands-off** `TOOL-dIndexedDesign-51` — the literal run, which that unit's AC2 reads in the refusal of a `--design-exit` exit 2 (id 20)

## 4. Design

### Evidence

- `tools/memory-tree/check-arms.py:131`, `FAIL_RE`, finds a site. `:204-221`, `signature`, keeps the longest
  literal run after splitting on interpolations, trimming only `:`, `"` and spaces. `:261-264` refuse a run
  shorter than 12 characters. `:791` arms a site on the first test line holding its signature as a substring.
- `tools/unattended/unattended.sh:13655` is the THIN site at base, and
  `tools/unattended/unattended.test.sh:6336` its arm. `git grep` outside `memory/builds` finds the THIN
  text in those two files only, read 2026-10-28.
- `grep -c "refuses a build pass for a unit not ready to build"` prints 0 over both files at base,
  read 2026-10-28. The run is 61 characters, above the 12-character floor.

### Inventory

Minted: no identifier. One message literal.

### Migration

None: the printed THIN text gains a prefix, and the only assertion on it is the arm S2 re-pins.

### Rollout

S1 and S2 land in unit 16's pass, order 3, ahead of this unit's order. Unit 16's Edges block names them,
and its builder reads them there. S3 and AC1 to AC3 are this unit's own pass at order 19, beside
`TOOL-dIndexedDesign-47`, `-49` and `-51`, and before 47 and 51, which consume from it.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1, in unit 16's pass
- `tools/unattended/unattended.test.sh`: S2, in unit 16's pass
- `memory/builds/dIndexedDesign/build/`: S3's ledger note

### Alternatives rejected

- **Keep the shared prefix and add a per-cause stem inside `_d_why`.** Lost to `check-arms.py:204-221`:
  interpolated text never enters a signature, so the stem arms nothing.
- **Keep THIN as its own literal site and compose only the design-exit message elsewhere.** The skeptic
  admitted it, but it needs an existing site whose run is unique to host the design-exit text, and the
  folded refusal still needs `TOOL-dIndexedDesign-49`'s text arm. It moves more sites for the same proof.

## 5. Production-readiness checklist

- security — no refusal is removed or weakened; the THIN refusal prints the same clause.
- perf / scale — none.
- error / empty / loading states — the THIN refusal still names the unit and its spec path.
- observability — `check-arms.py --report` names the site by the new run.
- risks — an arm that copies the full dispatch message re-arms the site. AC2 counts the run's carriers.
- testing — AC1 and AC2 by `check-arms.py` and `grep` at unit 16's pass commit, AC3 by a ledger grep.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/check-arms.py --report` runs in a worktree at unit 16's pass
  commit, the row for the composed `fail 49` site of `verb_dispatch` prints the signature
  `--dispatch refuses a build pass for a unit not ready to build`.
  Red when: the row prints `--dispatch declares a build pass for a unit`, or any run another site shares.
- **AC2** — When `grep -c "refuses a build pass for a unit not ready to build"` runs over
  `tools/unattended/unattended.sh` at that commit, it prints 1. When
  `grep -v '^[[:space:]]*#' tools/unattended/unattended.test.sh | grep -c "refuses a build pass for a unit not ready to build"`
  runs there, it prints 1, and that line also carries `whose spec grades THIN`.
  Red when: either count is not 1, or the one test line is not the THIN arm.
- **AC3** — When `grep -n "TOOL-dIndexedDesign-48 S3"` runs over unit 41's acceptance ledger, it prints
  the note under AC2's answer, naming the literal run.
  Red when: the note is missing or stands as its own `- AC` line.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `unattended kit gate` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC2 · the THIN arm re-pinned to the composed site's own run, staged by restoring the shared `--dispatch declares a build pass for a unit` prefix · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 39 to 46, id 10
  (HIGH, item H1, shared with ids 1 and 19), on its sound fix, repairing TOOL-dIndexedDesign-41 S1.

## 10. Reuse audit

The seam is unit 41 S1's composed site and `check-arms.py`'s `signature` (`:204-221`) as the measure. No
new refusal mechanism is written: one literal changes and one arm is re-pinned. The probe
`python tools/codebase-map/reuse_lookup.py "assert each composed refusal cause by its own test line when several causes share one fail site"`
ranked `fail`, `refusal`, `Refusal`, `DesignRefusal` and `check_line`. None gives a site a unique literal,
so no existing seam fits beyond the site itself.

Recall terms used: `python tools/memory-recall/query.py "how is a composed fail site armed when several refusals share one message" --terms "check-arms signature composed site armed substring arm line THIN dispatch fail 49 census"`
