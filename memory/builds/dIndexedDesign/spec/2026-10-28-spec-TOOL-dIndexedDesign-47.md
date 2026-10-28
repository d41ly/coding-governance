# TOOL-dIndexedDesign-47 — unit 41 AC2's armed half becomes a staged break: with the THIN arm deleted in a scratch clone, the composed THIN site reads UNARMED

**Status:** DEFERRED · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 19 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-47-deviation-471.md](../build/2026-10-28-build-TOOL-dIndexedDesign-47-deviation-471.md) | deviation | — |
| [2026-10-28-build-TOOL-dIndexedDesign-47-promoted-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-47-promoted-fix-return.md) | research | TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-47-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-47-1-spec-writer.md) | journal | — |
| [2026-10-28-prompt-TOOL-dIndexedDesign-47-promoted-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-47-promoted-fix-brief.md) | research | TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 39 to 46
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**, which it shares with ids 10 and 19
(`TOOL-dIndexedDesign-48` and `TOOL-dIndexedDesign-49`). `TOOL-dIndexedDesign-41` AC2 requires the
composed THIN site of `verb_dispatch` to "read armed" under `check-arms.py --report`. A site reads armed
when its signature is a substring of any non-comment test line (`tools/memory-tree/check-arms.py:791`),
and five arm lines of `tools/unattended/unattended.test.sh` carry the site's shared prefix (`:6315`,
`:6336`, `:6411`, `:6487`, `:12684`). So AC2's armed half cannot go red, whatever arm is missing.

This unit carries the skeptic's corrected fix for id 1. AC2's armed half is replaced by a staged break the
build runs: in a scratch clone with the THIN arm deleted, the composed site must read UNARMED. That break
can fail only once the site's literal run is its own (`TOOL-dIndexedDesign-48`) and the design-exit arm
carries no copy of it (`TOOL-dIndexedDesign-49`). It repairs `TOOL-dIndexedDesign-41` and takes order 19,
one above unit 41's 18.

## 2. Scope (IN)

- **S1** — The break. At this unit's pass, a scratch clone at unit 16's pass commit has the THIN arm line
  deleted from its working copy of `tools/unattended/unattended.test.sh`. Run with the clone as its cwd,
  `check-arms.py --report` reads the composed `fail 49` site of `verb_dispatch` UNARMED. With the line
  restored, the same run reads it armed. Both readings are recorded in this unit's ledger. Observed by
  AC1.
  **Readers:** by name: `dispatch: a THIN unit is refused`, the arm's label, which only
  `tools/unattended/unattended.test.sh:6336` spells at HEAD. The deletion touches only the clone's
  working copy, so no tracked file loses the line. by value: `tools/memory-tree/check-arms.py`, whose
  `armed_signatures` read of the gate's sibling test file (`:779`) and substring test (`:791`) are the
  two readings S1 records; the suite reads it too, and the suite is never run in the clone.
- **S2** — The supersession. Unit 41's acceptance ledger carries the note `TOOL-dIndexedDesign-47 S2`
  under AC2's answer. It replaces AC2's armed half for the composed THIN site, "read armed", with S1's
  two readings. AC2's clause for the folded `fail 31` site is unchanged. Observed by AC2.

## 3. Non-goals (OUT)

- The site's literal run and the THIN arm's re-pin: `TOOL-dIndexedDesign-48`, id 10.
- The arm for each cause composed into the site: `TOOL-dIndexedDesign-49`, id 19.
- AC2's census sentence and its fixture: `TOOL-dIndexedDesign-51` S4 and `TOOL-dIndexedDesign-53`, id 13.
- The report's left-shift gate, a check-arms AMBIGUOUS mode. §4 Alternatives rejected says why it is not
  built here.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-41` — S1's composed THIN site and AC2, whose armed half S2 replaces with the staged break (id 1)
- **consumes-from** `TOOL-dIndexedDesign-48` — the composed site's own literal run and the re-pinned THIN arm, without which deleting the THIN arm leaves the site armed by the shared prefix (id 1)
- **consumes-from** `TOOL-dIndexedDesign-49` — the design-exit arm asserting its clause text and not the site's literal run, without which deleting the THIN arm leaves the site armed by that line (id 1)

## 4. Design

### Evidence

- `tools/memory-tree/check-arms.py:204-221`, `signature`, keeps the longest literal run of a message.
  `:791` sets `b["armed"]` to the first numbered test line holding `b["sig"]` as a substring.
- `check-arms.py:1673` takes the root from `git rev-parse --show-toplevel` in the cwd, and `discover`
  (`:224-240`) reads gates from `git ls-files` there. A clone run as the cwd is therefore read whole, and
  a deleted line in its working copy is seen, since `branches` and the arm reader open files under the root.
- At base the THIN site is `tools/unattended/unattended.sh:13655` and its arm is
  `tools/unattended/unattended.test.sh:6336`. Read 2026-10-28.

### Inventory

Minted: no identifier. One staged break, its two recorded readings and one ledger note.

### Migration

None.

### Rollout

The whole unit is its own pass at order 19, after `TOOL-dIndexedDesign-48` and `TOOL-dIndexedDesign-49`,
whose producers sit at the same order. It writes only the build's ledgers, so it meets no write set of
units 48, 49 or 51.

### Files touched (estimate)

- `memory/builds/dIndexedDesign/build/`: S1's recorded readings and S2's ledger note

### Alternatives rejected

- **A check-arms AMBIGUOUS mode, the report's left-shift gate.** Lost on the real tree: a scratch probe
  run on 2026-10-28 that loads `check-arms.py` and flags each site whose signature sits inside another
  site's message in the same gate found 13 of 715 sites already ambiguous, 10 of them in `unattended.sh`.
  Such a gate reds the tree on its first run, and it is a separate gate unit that no clause of this build
  names.
- **Delete the design-exit arm and require UNARMED.** Lost to the shared site: one site serves both causes,
  so deleting one cause's arm can never unarm it. `TOOL-dIndexedDesign-49` arms that cause by its text.

## 5. Production-readiness checklist

- security — N/A: no code changes; a probe in a scratch clone.
- perf / scale — one clone and two `check-arms.py --report` runs.
- error / empty / loading states — a clone that cannot be made is a red AC1, never a skip.
- observability — the recorded readings name the site row and its armed or UNARMED verdict.
- risks — a later arm that copies the full dispatch message would re-arm the site silently. AC1 re-reads
  the arm set at unit 16's pass commit, and `TOOL-dIndexedDesign-48` AC2 counts the run's carriers.
- testing — AC1 by the staged break, AC2 by a ledger grep.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — In a scratch clone at unit 16's pass commit,
  `sed -i '/refuses a build pass for a unit not ready to build/d' tools/unattended/unattended.test.sh`
  deletes the THIN arm, the one non-comment test line holding the site's literal run
  (`TOOL-dIndexedDesign-48` AC2). When `python <repo>/tools/memory-tree/check-arms.py --report` then runs
  with the clone as its cwd, the composed `fail 49` row of `verb_dispatch` reads UNARMED. After
  `git checkout -- tools/unattended/unattended.test.sh` restores the line, the same run reads it armed.
  Red when: the row reads armed with the THIN arm deleted, or UNARMED with it restored.
  fixture: a scratch clone under `%TEMP%/<short-name>`, which the tree does not hold today.
- **AC2** — When `grep -n "TOOL-dIndexedDesign-47 S2"` runs over unit 41's acceptance ledger, it prints
  the note under AC2's answer, and that line names `check-arms.py`.
  Red when: the note is missing or stands as its own `- AC` line.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `unattended kit gate` · `memory hygiene` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 39 to 46, id 1
  (HIGH, item H1, shared with ids 10 and 19), on the skeptic's corrected fix, repairing
  TOOL-dIndexedDesign-41 AC2.

## 10. Reuse audit

The seam is `check-arms.py --report` itself, run over a scratch clone, so no second arming reader is
written. The probe
`python tools/codebase-map/reuse_lookup.py "assert each composed refusal cause by its own test line when several causes share one fail site"`
ranked `fail`, `refusal`, `Refusal`, `DesignRefusal` and `check_line`. None stages a break against an arm
set, so no existing seam fits beyond the checker. The recall query returned `TOOL-dRedressedBar-6`'s
reading that a negative assertion never arms a site, which S1's restored reading relies on.

Recall terms used: `python tools/memory-recall/query.py "how is a composed fail site armed when several refusals share one message" --terms "check-arms signature composed site armed substring arm line THIN dispatch fail 49 census"`
