# TOOL-aMendedFleet-14 — bulk backlog triage: aged unlabelled asks deferred on one triage ask, and five fixed-but-OPEN asks disposed

**Status:** CLOSED · rev-2 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · advances TOOL-aMendedFleet-106 · ratified 2026-10-04 · order 14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aMendedFleet-14-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aMendedFleet-14-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

452 of the 457 live asks carry no severity, and 266 of them have sat OPEN with no severity, no hold
and no linked spec for thirty days or more, so OPEN no longer separates the asks somebody will act
on from the ones nobody has looked at. This unit parks every such aged ask as DEFERRED on ONE new
triage ask, so the owner releases all of them with a single disposition, and it disposes the five
OPEN asks whose defect is already fixed or duplicated. It writes records only.

## 2. Scope (IN)

- **S1** — The DEFERRAL POPULATION is DERIVED at the pass and never typed: every row of
  `python tools/memory-tree/gen_build_index.py --asks --json` whose `status` is `OPEN`, whose `sev`
  is `unlabelled`, whose `holds` and `live_specs` are empty, and whose `filed` date is at least 30
  days before the pass date, less the five asks S3 disposes. The pass records the date, the cutoff
  date and the count in its commit's `Decided:` trailer. Observed by AC1.
- **S2** — One `DEFERRED` row per member, `DEFERRED · <id> · until <triage-id> · <why>`, rendered by
  `render_status_row` in `tools/memory-tree/backlog.py` and never typed, under `## Dispositions` in
  this build's own `BACKLOG.md`, ordered by id. The WHY names the ask's filed date and the three
  facts S1 read. Observed by AC1, AC2 and AC5.
- **S3** — Five dispositions, each re-verified at the pass against the source the WHY cites:
  - `TOOL-aUnblockedFleet-7` CLOSED by `TOOL-aWokenSentinel-16`: check 34 of `--landed` reads
    containment, so a second landing that overwrites the shared lander marker still contains the
    first run's witness.
  - `TOOL-dUnstalledConvoy-38` CLOSED by `TOOL-aWokenSentinel-16`, whose own README row names it as
    the defect that unit fixed. The report did not name it; it is a discovery, adopted.
  - `TOOL-aUnblockedFleet-8` CLOSED by `TOOL-dDerivedDocket-27`: the bar's bound became wall plus
    queue plus margin for a repository declaring `GATE_PROFILE_CMD`, which `.unattended.conf` does.
  - `TOOL-aWeighedCompass-16` WONTDO, the WHY naming it a duplicate of `TOOL-aProbedToolkit-10`,
    which stays live.
  - `TOOL-aReplayedCard-9` WONTDO, per §8 F3.
  Observed by AC3.
- **S4** — The TRIAGE ASK, filed in this build's `BACKLOG.md` under the id the orchestrator mints
  and writes into this unit's brief: an ask row whose text names the owner's triage of the asks
  deferred on it and the release act, carrying an `accept` clause; a `SEV` row at `LOW`; and a `KEEP`
  row. This spec's status header gains `advances <triage-id>` in a rev bump with its §9 line, so the
  unattended `asks-disposed` item reads the ask as KEEP after a CLOSED unit that advances it.
  Observed by AC4 and AC6.
- **S5** — This build's `BACKLOG.md` stays within `INDEX_CAP_BYTES` from `.memory-tree.conf`, the
  row-class cap hygiene check 6 applies to it. Observed by AC5.

## 3. Non-goals (OUT)

- A writer mode in `gen_build_index.py` or `backlog.py` that defers aged asks on demand (§8 F1).
- Re-arming the shrink-only pin on the unlabelled count, which is `TOOL-aMendedFleet-15`. A DEFERRED
  ask is still live and still unlabelled, so this unit moves that count by the S3 dispositions only.
- Labelling any ask with a severity. Severity is a judgement about one ask, and this unit judges
  none; the triage ask is where that judgement is owed.
- Deferring the KEEP rows that carry no evidence, which the report also names. A KEEP derives no
  status, so the S1 predicate already reaches every KEEP-only ask that is aged and unlabelled.
- Collapsing `row_grammar.py`'s "NOT MEASURED" lines, and dropping KEEP rows: wave 1 lists both under
  the same triage item, and neither is in this unit's roster row.
- Executing `TOOL-aUnblockedFleet-7` or `-8`: the report rules both fixed in code.

### Edges

- **hands-off** `TOOL-aMendedFleet-15` — the unlabelled count this unit's dispositions leave, which
  that unit pins.
- **consumes-from** external — an ask id the orchestrator mints for the triage ask before dispatch.
  Fan-out children never mint ids, so a pass whose brief names none parks with that reason.

## 4. Design

### Evidence

Read at base `7af5f564` on 2026-10-04, PINNED to that date; the pass re-derives every figure.

- `--asks --json` returns 457 live asks: 452 OPEN, 4 DEFERRED and 1 INPROGRESS; 452 unlabelled.
  With S1's predicate the population is 266 at a cutoff of 2026-09-04, 251 TOOL and 15 DEPL, across
  56 build folders. At 14, 21 and 45 days it is 420, 367 and 107.
- A disposition row sits in its WRITER's own `BACKLOG.md`, never the ask's home file
  (`tools/memory-tree/README.md`, "Row kinds"). So every row here lands in one file this unit owns.
- `DEFERRED` takes `until <id>`, and that id must be a filed ask or a spec H1, else V6. The fold
  holds the ask while the target is live and releases it to OPEN the moment the target is terminal
  (`derive_statuses`, stratum 2). One live triage ask therefore holds them all, and closing it
  releases them all. `TOOL-dDerivedDocket-66` is the precedent: five legacy holds on one triage ask.
- An ask filed on or after `ASK_CUTOFF` owes a `SEV` row (V12) and an `accept` clause or a
  `seen … run` (V14). The triage ask is filed after it.
- The unattended Definition of Done's `asks-disposed` accepts an ask this build filed only when it
  is terminal, held by this build's own row, or KEEP after a CLOSED unit that advances it. S4's
  header verb and KEEP row are what make the triage ask the third.
- The report's fix for `TOOL-aUnblockedFleet-7` was "dUnstalledConvoy-38", which is itself an OPEN
  ask; the commit that fixed both is `6bb7ac756`, under `TOOL-aWokenSentinel-16`, CLOSED.
- The row shape measured about 100 to 150 bytes, so 266 rows are 27 to 40 KB against a 61440-byte cap.

### The pass

1. Read the minted triage id from the brief; park if absent.
2. Re-verify each S3 ask: read the fixing spec's status header and the line its WHY cites.
3. Run `--asks --json`, apply S1, and render S2's rows and S3's five rows with the `backlog.py`
   renderers from a scratch script under the scratchpad, never committed.
4. Write the triage ask, its `SEV` and `KEEP` rows, the S2 and S3 rows, and this spec's header verb.
5. Run `gen_build_index.py --write`, then `--check`, and commit once with the unit id in the subject
   and one `Decided:` line carrying S1's date, cutoff and count.

### Files touched (estimate)

- `memory/builds/aMendedFleet/BACKLOG.md`
- `memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-14.md`
- `memory/builds/aMendedFleet/README.md`
- `memory/backlog/TOOL.md`
- `memory/backlog/DEPL.md`

The last three are generated; the dispatch declares them as the generator's writes.

### Alternatives rejected

- **Writing each row in the ask's home file.** The row-kinds rule puts a disposition in its writer's
  file, and 56 home files would put this unit in conflict with every live build that owns one.
- **Holding on this unit's own id.** The hold releases when this spec closes, at this build's own
  close, so the asks would read OPEN again on the day the build lands.
- **Holding on `TOOL-dDerivedDocket-66`.** Its text scopes it to five named legacy holds.

## 5. Production-readiness checklist

- security — N/A — records only, written to this build's own folder.
- perf / scale — one `--asks --json` read of about 2.5 s; the fold re-reads 270 more rows.
- error / empty / loading states — an empty S1 population is a park, not a commit: it means the
  predicate or the projection broke, and AC1's non-zero half reds on it.
- observability — every deferred ask shows DEFERRED, decided by the triage ask, in the family views
  and in `--asks <id>`.
- risks — the views' row count is unchanged, because a DEFERRED ask is still live; what moves is the
  status column. A wrong S3 disposition is undone by a `REOPEN` row naming this build.
- testing — AC1 to AC6 read the generator's own projection and a throwaway clone; no suite runs.
- migration — N/A — no data shape changes.
- user docs — N/A — the triage ask's text is the owner's instruction.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --asks --json` runs after the pass, no
  row satisfies S1's predicate at the pass date, and the number of rows reading `DEFERRED` with the
  triage ask as `decided_by` equals the count of `DEFERRED` rows in this build's `BACKLOG.md` and the
  count the `Decided:` trailer records, which is above zero.
  Red when: an aged unlabelled ask still reads OPEN, or the deferred count is zero because the
  predicate matched nothing.
  figure: every count DERIVED at observation time.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --check` runs after the pass, its
  backlog line reports `0 verdict(s)`.
  Red when: a row names an unfiled target, a hold cycles, or the triage ask lacks its `SEV` row or
  its `accept` clause.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --asks <id>` runs for each S3 ask, it
  prints CLOSED decided by `TOOL-aWokenSentinel-16` for `TOOL-aUnblockedFleet-7` and
  `TOOL-dUnstalledConvoy-38`, CLOSED decided by `TOOL-dDerivedDocket-27` for
  `TOOL-aUnblockedFleet-8`, and WONTDO decided by `aMendedFleet` for `TOOL-aWeighedCompass-16` and
  `TOOL-aReplayedCard-9`; and `TOOL-aProbedToolkit-10` is not terminal.
  Red when: any of the five reads otherwise, or the duplicate's survivor was closed with it.
- **AC4** — When `python tools/memory-tree/gen_build_index.py --asks <triage-id>` runs after the
  pass, it prints `sev LOW` and an `accept` clause; and with this spec's status read as `SPECCED`,
  it prints `TOOL-aMendedFleet-14` among its live specs and as its decider. A CLOSED spec is not
  live, so the pass commit's own header cannot show the second half; the KEEP row carries it.
  Red when: the ask carries no severity or acceptance, or this spec's header does not advance it.
- **AC5** — When `wc -c` runs over this build's `BACKLOG.md` after the pass, the byte count is below
  the `INDEX_CAP_BYTES` value `.memory-tree.conf` declares.
  Red when: the rows overflow the row-class cap, which hygiene check 6 refuses on this branch.
  figure: the cap DERIVED from the conf at observation time.
- **AC6** — When a `CLOSED · <triage-id> · by <sha> · <why>` row is appended to this build's
  `BACKLOG.md` in a throwaway clone of the pass commit and `gen_build_index.py --asks --json` runs
  there, every ask AC1 counted reads OPEN again.
  Red when: any of them stays DEFERRED, so the owner's one act would not release them.
  fixture: a `git clone --local` under a short `%TEMP%` root; the tree holds none today.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `drift-audit records` · `spec tokens (a spec's own names resolve)`

The pass writes records only. Its paths trip the two recall-floor guards, and `drift-audit records`
reads the same ask projection through its backlog signals.

## 8. Open questions

- **F1 — A one-shot pass, or a writer mode that defers aged asks on demand?**
  Options: render the rows once from the projection with the existing renderers; or add a
  `--defer-aged` mode to the generator. The mode is re-runnable, and it is a new public surface on a
  shipped kit, which M3's veto 2 refuses.
  RESOLVED (agent, 2026-10-04, delegated): one pass with the existing renderers, its predicate
  recorded in S1 so a later triage can re-derive it.
- **F2 — How old is aged?**
  Options: 14, 21, 30 or 45 days, which defer 420, 367, 266 or 107 asks on 2026-10-04. The two
  shorter windows reach asks filed in the last three weeks, while their builds may still be landing.
  RESOLVED (agent, 2026-10-04, delegated): 30 days, measured from the pass date.
- **F3 — Does `TOOL-aReplayedCard-9` close WONTDO?**
  Options: WONTDO now; keep it OPEN until a tokens-to-READY baseline is read. The report recommends
  WONTDO unless that baseline shows orientation is worth an eight-arm matrix. The matrix needs a
  session started with an agent definition already installed, which no unattended pass can take,
  and this build's context-diet units measure orientation cost on the live path instead.
  RESOLVED (agent, 2026-10-04, delegated): WONTDO, the WHY naming both reasons; a `REOPEN` row naming
  `aMendedFleet` restores it.
- **F4 — Is a duplicate CLOSED or WONTDO?**
  Options: CLOSED by `TOOL-aProbedToolkit-10`, which reads as resolved while the defect stands; or
  WONTDO naming the survivor.
  RESOLVED (agent, 2026-10-04, delegated): WONTDO naming the survivor, which stays live.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the live ask projection, the fold and the row-kinds rule
  at base.
- rev-2 · 2026-10-05 · S4's header verb: the status header advances `TOOL-aMendedFleet-106`, the
  triage ask id the orchestrator minted into this unit's brief. The pass re-derived S1 at 2026-10-05
  with a cutoff of 2026-09-05: 298 asks, 277 TOOL and 21 DEPL across 61 home folders, above the
  pinned 266 chiefly because the cutoff moved a day and admitted the 50 asks filed 2026-09-05.
  AC4 reworded: its live-spec half reads a status this same commit flips to CLOSED, so it is now
  observed with the header read as `SPECCED`, which is what it always measured.

## 10. Reuse audit

The seams reused are `render_status_row`, `render_ask_row` and `render_sev_row` in
`tools/memory-tree/backlog.py` for every row, and the generator's `--asks --json` projection for the
population, so no second fold is written. `python tools/codebase-map/reuse_lookup.py "write
disposition rows deferring many backlog asks at once"` named those renderers and no bulk writer, so
no writer exists to extend and none is added (§8 F1). Recall named `TOOL-dDerivedDocket-66`, the
one-triage-ask hold this unit copies, and `TOOL-dDerivedDocket-33`'s signed triage tables, which
disposed legacy rows by rule at the switch-over. Where the report and the tree disagree: the report
names "dUnstalledConvoy-38" as the fix for `TOOL-aUnblockedFleet-7`, and the tree shows it is an
OPEN ask fixed by the same commit.

Recall terms used: `python tools/memory-recall/query.py "how were stale or aged backlog asks bulk
triaged or deferred before" --terms "aged unlabelled asks DEFERRED until triage KEEP disposition
rows backlog switch-over severity SEV owner triage"`
