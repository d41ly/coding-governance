# TOOL-aPrimedKeepalive-7 — the DRIVER's live-run count takes the same exclusion the leg just got

**Status:** INPROGRESS · rev-3 · 2026-08-27 · node a · Tier-2 · base b4e1d5be · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md) | journal | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-8 TOOL-aPrimedKeepalive-9 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round2.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round2.md) | spec-audit | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round3.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round3.md) | spec-audit | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-6 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aPrimedKeepalive-4` stopped the merge-bar LEG from counting a `LANDING` record whose work is
already on the remote. The DRIVER's `check_single_live` still counts it, so the next `--preflight` on
this repo refuses while `memory/builds/dTieredTribunal/RUN.md` sits at `LANDING`. Fixing one half of
a two-half wedge leaves the wedge.

## 2. Scope (IN)

- **S1** — `check_single_live` in `tools/unattended/unattended.sh` applies the same exclusion leg
  check 7 applies: a record whose phase is exactly `LANDING`, whose witness resolves, and whose
  witness is an ancestor of the anchor the run already observed is not counted.
- **S2** — the exclusion is REPORTED on stdout with the record, its witness and the anchor, so a
  refusal that did not happen is still visible.
- **S3** — it FAILS CLOSED: with no observed anchor, **an anchor naming a commit this clone has not
  fetched**, an unresolvable witness, or any phase other than `LANDING`, the record counts exactly as
  it does today, and the reason is printed. The fetched-anchor cause is the same one
  `TOOL-aPrimedKeepalive-4` rev-3 added to its S3; the two units share one predicate and a cause named
  in only one of them is the `amendment-leaves-its-other-half-standing` class.
- **S4** — `TOOL-aPrimedKeepalive-4`'s §3 is corrected as a `rev-2`. It currently names this a
  non-goal on the ground that the driver "already admits the ordinary second run", which is FALSE and
  was disproved by observation before this spec was written.

## 3. Non-goals (OUT)

- Any change to what `check_single_live` does for a genuinely live second run. Two `BUILDING`
  records still refuse, which is the rule's whole purpose.
- Making `LANDING` terminal, or writing any phase. The driver's own comment is the rule: a terminal
  phase is a PRODUCER's to write.
- Sharing one implementation between the driver and the leg. They are copy-installed standalone and
  the leg reads the driver as DATA, never sources it; the kit's own normalisation comment says the
  duplication is deliberate. Two spellings of one predicate is a cost this unit accepts and names.

## 4. Design

### The observation that produced this unit

Verifying `TOOL-aPrimedKeepalive-3` AC6, `--preflight` was invoked with a waiver on a live run. It
printed, among its refusals:

```
UNATTENDED check 5 FAILED — more than one run-state file is in a non-terminal phase, so 'the run'
is not well-defined: 2 live, memory/builds/aPrimedKeepalive/RUN.md memory/builds/dTieredTribunal/RUN.md
```

So the driver counts this run's own record plus the wedged one. `check_single_live` walks
`GIT ls-files`, and a run's record becomes tracked the moment its first commit lands — which is
before any later `--preflight`, `--resume` after a compaction included.

### Where the anchor comes from

`verb_preflight` calls `observe_anchor || true` BEFORE `check_single_live`, so `ASHA` is already
populated when the count runs. That ordering is what makes the exclusion computable in the driver at
all, and it is asserted rather than assumed: with `ASHA` empty the exclusion is skipped and says so.

### Files touched (estimate)

`tools/unattended/unattended.sh` — `check_single_live` alone.
`memory/builds/aPrimedKeepalive/spec/2026-08-27-spec-TOOL-aPrimedKeepalive-4.md` — the §3 correction.

### Alternatives rejected

**Leave the driver alone and let a later run meet the refusal.** That is the state this build was
started in, and it is what made a build about not-stalling spend its own owner turn on a stall.

**Have the driver source the leg's predicate.** The leg reads the driver as data and never the
reverse; a dependency in that direction would make the driver unrunnable without its own gate.

## 5. Production-readiness checklist

- security — N/A. A read-only ancestry test against an anchor the verb already observed.
- perf / scale — no new network call; `observe_anchor` has already run.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — S3 is the error state and each cause prints its own reason.
- observability — S2 reports every exclusion with its evidence.
- risks — over-excluding and admitting a genuinely live second run. The phase guard plus the
  ancestry test bound it, and the failing case is observed rather than assumed.
- testing + left-shift gates — the kit's own `unattended.test.sh` covers `check_single_live` and is
  run through `run-unattended-gates.sh`, which is the compensating check the kit descriptor names.
- migration / rollback — one predicate; revert is the rollback.
- user docs — none. The driver's own comment states what the exclusion does not claim.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --preflight` runs on a clean tree with
  `memory/builds/dTieredTribunal/RUN.md` at `LANDING` and this run's own record live, `check 5` does
  NOT fire, and stdout names the excluded record with its witness and the anchor.
- **AC2** — When the same invocation runs against a `LANDING` record whose witness is NOT an ancestor
  of the observed anchor, `check 5` still fires. Observed by staging a fixture record and removing it.
- **AC3** — When `ASHA` is empty, or names a commit this clone cannot resolve, every record counts
  and the driver prints that the exclusion was unavailable — read from the predicate, since a run that
  cannot reach its remote refuses earlier for other reasons. The line is emitted unconditionally when
  it would have mattered, never behind an opt-in flag.
- **AC4** — When `memory/builds/aPrimedKeepalive/spec/2026-08-27-spec-TOOL-aPrimedKeepalive-4.md` is
  read, its §3 no longer claims the driver "already admits the ordinary second run", and its §9
  carries the `rev-2` line saying what disproved it.
- **AC5** — When `bash tools/unattended/check-unattended.sh` runs, it stays green, proving the
  driver edit did not break the constants the leg reads out of it with `core_of`.
- **AC6** — When a record whose phase is `BUILDING` and whose witness IS an ancestor of the observed
  anchor is placed beside this run's own, `--preflight` still fires `check 5` and prints no `EXCLUDED`
  line. This grades the PHASE guard, which is the single predicate keeping a genuinely concurrent run
  from being excluded, and AC1 cannot stand in for it: `check 5` fires only above one live record, so a
  driver with no phase guard yields a count of one and AC1 passes anyway. The kit's own check-5
  fixture cannot reach it either — `runmd()` at `tools/unattended/unattended.test.sh:473` writes no
  `witness` fact, so the exclusion takes the empty-witness branch whether or not the phase guard
  exists. Observed with a staged fixture, then removed.

## 7. Gates

`unattended kit gate` · `unattended skill wiring`, and `bash tools/run-gates/run-gates.sh` at the
push boundary. Compensating check: `bash tools/unattended/run-unattended-gates.sh`.

## 8. Open questions

none

## 9. Revision log

- rev-3 · 2026-08-27 · folded spec-audit round 2, finding 2. S3 names four fail-closed causes and §6
  graded two; the PHASE guard — the clause that keeps a live `BUILDING` record from being excluded —
  had no observation behind it at all. AC6 added and observed.
- rev-2 · 2026-08-27 · folded spec-audit round 1's findings 25 and 26 from its sibling, which the
  audit named explicitly: unit 7 was outside the subject set, and fixing the predicate in unit 4 alone
  would leave the two copies disagreeing.
- rev-1 · 2026-08-27 · initial draft. ADOPTED mid-build under protocol section 11, the rule this
  build is writing, recorded by `--rescope --act add`. The discovery came from verifying another
  unit's acceptance criterion, which is where a spec's own reasoning gets tested against the machine.

## 10. Reuse audit

The seam is `TOOL-aPrimedKeepalive-4`'s own predicate, three hours old and in the sibling file:
`tools/unattended/check-unattended.sh`, the `c7keep`/`c7drop` walk before check 7. This unit
transcribes that predicate into `check_single_live` rather than inventing a second shape, and §3
records why transcription rather than sharing is correct here — the leg reads the driver as data and
a dependency the other way would make the driver need its own gate to run.

The anchor variable is `ASHA`, already populated by `observe_anchor` at `verb_preflight`'s top, which
is the same value `check_authorization` and `trusted_base` consume. No new observation is added.

Recall terms used: `check_single_live preflight live run-state non-terminal LANDING witness ancestor
anchor observe_anchor wedge fleet bar deadlock`. The query returns the same three rows unit 4 cites —
`TOOL-aBoundedVerdict-24`, `TOOL-aFusedCharter-4`, `TOOL-dUnstalledConvoy-38` — none of which
distinguishes the driver's half of the wedge from the leg's.
