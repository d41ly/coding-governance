# TOOL-dWellOiledMachine-75 — an intake that cannot be written fails its pack, so the dispatcher refuses the prompt

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 41 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-75-deviation-751.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-75-deviation-751.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 60, item H12, at HIGH. TOOL-dWellOiledMachine-4 S5 declares the intake pack class `record`
and has it refuse by exiting 2 on any write error; TOOL-dWellOiledMachine-10 S2 reads exit 2 as a
verdict, never lets a `record` pack block, and S6 counts a pack failed only on an exit other than 0
or 2. So when `requests/` is unwritable the prompt passes with no receipt and the owner's mandate is
lost silently, the outcome the unit exists to prevent. This unit makes a write error a failed pack,
which `runtime.hook-failure` `closed` refuses, and pins at the dispatcher that a `record` pack's exit
2 never blocks. The same mismatch in TOOL-dWellOiledMachine-8's returns pack is finding 13, carried
by the minors batch TOOL-dWellOiledMachine-79.

## 2. Scope (IN)

- **S1** — The failure exit. `intake.py hook` (`tools/runtime/intake.py`) exits 1 with one stderr line
  `intake — not written · <why>` on any error of `write_intake` or of its receipt append, and never
  exits 2. Under `runtime.hook-failure` `closed` the dispatcher then refuses the prompt with
  `BLOCKED by dispatch: pack intake failed (<why>) · hook-failure closed` (10 S6); under `open` it
  admits the prompt and journals `hook-failure`, the owner's chosen trade. Observed by AC1, AC2.
- **S2** — The sketch corrected. Spec 4's §4 "The hook" reads `any error -> exit 2, the dispatcher
  refuses the prompt`; spec 4 takes a rev bump at this unit's pass reading `any error -> exit 1, a
  failed pack`, its §9 line naming this unit and finding 60. Observed by AC4.
- **S3** — The dispatcher pins the rule. The dispatcher fixture of TOOL-dWellOiledMachine-10 gains a
  case in which a `record` pack exits 2 on `UserPromptSubmit`: the prompt is admitted and no
  `hook-failure` line is written, so a record pack can never be relied on to block by exit 2.
  Observed by AC3.

## 3. Non-goals (OUT)

- No change of the pack's class to `refuse`: §8 F1.
- No change to the payload-field handling: an absent field or unparsable stdin is finding 61, in the
  minors batch TOOL-dWellOiledMachine-79.
- No change to the returns pack: finding 13, in the same batch.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-4` — `intake.py hook` and its pack, whose error exit this unit changes
- **consumes-from** `TOOL-dWellOiledMachine-10` — the dispatcher's failed-pack rule (S6) and its fixture, which this unit's case extends

## 4. Design

### Evidence

- 4 S5 declares `class record`, `failure closed` (`spec-4.md:57-66`), and its sketch maps any error to
  exit 2 (`spec-4.md:118`).
- 10 S2 says `warn` and `record` packs never block (`spec-10.md:44-52`); 10 S6 counts a pack failed
  on an exit other than 0 or 2 (`spec-10.md:71-76`).
- 4 AC5 expects `BLOCKED by dispatch: pack intake failed` and is deferred to unit 10
  (`spec-4.md:183-187`).

### Files touched (estimate)

- `tools/runtime/intake.py`: S1
- `tools/runtime/dispatch.test.sh`: S3's case
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-4.md` (S2's rev bump)

### Alternatives rejected

- **Class `refuse` with a refusal row.** §8 F1.

## 5. Production-readiness checklist

- security — an owner prompt with no receipt is refused under the default `closed`, never passed.
- perf / scale — none.
- error / empty / loading states — the failed-pack line names the cause.
- observability — under `open`, one `hook-failure` journal line per lost intake.
- risks — under `open`, a lost intake still passes; that is the owner's setting, journaled.
- testing — AC1 to AC4 and the arms in §7.
- migration — none.
- user docs — `help/runtime.md`'s intake section (4 S7) names the refused prompt.

## 6. Acceptance criteria

- **AC1** — When `python intake.py fixture --case unwritable` makes `requests/` read-only and pipes an
  owner prompt to `intake.py hook`, it exits 1 printing `intake — not written`.
  Red when: the hook exits 2 or 0 on a write error.
- **AC2** — When the same case runs the pack through `node dispatch.js UserPromptSubmit` under
  `runtime.hook-failure = "closed"`, the prompt is refused with `BLOCKED by dispatch: pack intake
  failed`.
  Red when: the prompt passes with no receipt.
- **AC3** — When the dispatcher fixture runs a planted `record` pack that exits 2 on
  `UserPromptSubmit`, the prompt is admitted and no `hook-failure` journal line is written.
  Red when: a `record` pack's exit 2 blocks.
- **AC4** — When `grep -n "exit 1, a failed pack" 2026-10-26-spec-TOOL-dWellOiledMachine-4.md` runs over
  spec 4, it prints the corrected sketch line, and §9 names this unit.
  Red when: the sketch still promises a refusal by exit 2.

## 7. Gates

`check-wiring self-test` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/runtime/selftest.py · covers AC1 · the unwritable case staged against a hook that exits 2 · none
New arm: tools/runtime/dispatch.test.sh · covers AC2 AC3 · the intake pack's failure and a planted record pack's exit 2, staged against a dispatcher that blocks on a record pack's exit 2 · none

## 8. Open questions

- **F1 — How does an unwritable intake refuse the prompt?** (a) The hook exits 1, a failed pack,
  refused under `runtime.hook-failure` `closed`; (b) the pack becomes class `refuse` and refuses by
  exit 2 with a refusal row. (b) makes intake refuse by its own verdict whatever `runtime.hook-failure`
  says, overriding the owner's `open` choice for one pack, and adds a refusal row whose remedy an
  owner cannot act on mid-prompt; (a) routes the failure through the one rule every pack's failure
  takes. Rung 3, the option that reuses the dispatcher's seam. RESOLVED (agent, 2026-10-27,
  delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 60 (H12).

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-10 S6's failed-pack rule, the one path by which any pack's
failure is refused or journaled. The probe
`python tools/codebase-map/reuse_lookup.py "refuse a prompt when its intake record cannot be written"`
ranked `records`, `CensusRefused`, `ScopeRefused` and `write_record` by name stem, none a hook's
failure path, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "what happens to an owner prompt when intake
write fails" --terms "intake pack UserPromptSubmit record class exit code failed pack hook-failure
closed refuse"`
