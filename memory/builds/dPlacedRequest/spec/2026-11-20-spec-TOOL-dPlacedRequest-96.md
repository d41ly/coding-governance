# TOOL-dPlacedRequest-96 — a foreign stale lease can be taken over again, and its hint prints

**Status:** CLOSED · rev-2 · 2026-11-20 · node d · Tier-2 · base 95c3103a · streams tooling · order 37

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dPlacedRequest-96-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-96-1-acceptance-ledger.md) | journal | — |
| [2026-11-20-build-TOOL-dPlacedRequest-96-red-fix-33.md](../build/2026-11-20-build-TOOL-dPlacedRequest-96-red-fix-33.md) | red-fix | — |
| [2026-11-21-build-TOOL-dPlacedRequest-96-deviation-731.md](../build/2026-11-21-build-TOOL-dPlacedRequest-96-deviation-731.md) | deviation | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-96-closing-review-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-96-closing-review-spec-brief.md) | research | — |
| [2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-97 TOOL-dPlacedRequest-98 TOOL-dPlacedRequest-99 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md`),
confirmed item **H2** at HIGH, finding id 3, and the round-2 exit promoted it to this unit. Commit
b7e369eeb put the `lease:foreign-released` row of `check_claim_writable` in place of the
`lease:foreign-stale` row instead of beside it, so a dead holder's lease falls to the `lease:*`
catch-all for every act. `--lease take-over` can no longer take a stale lease, and `--lease acquire`
never prints its take-over hint. This unit restores the row and gates the class. The third loss the
record names, `--entry-claim` waiting on a stale build lease as on a live one, is not cured by the row
alone: the entry claim routes the refusal's cause word, which stays `live-holder`. That route is
`TOOL-dPlacedRequest-100`'s, which reads the hint this row sets.

## 2. Scope (IN)

- **S1** — H2, closed by the record's fix, which the skeptic judged SOUND. The lease column of
  `check_claim_writable` in `tools/unattended/unattended.sh` regains its stale row beside the
  released row and above `lease:*`: `take-over` writes as `take-announced`; `acquire` refuses
  `live-holder` with `CW_HINT=take-over`; every other act refuses `live-holder`. The left-shift the
  record names lands with it, both halves in the unattended kit's suite: a probe arm over a stale
  build lease through the `--lease` verbs, and a static arm asserting every `CW_*` name the verbs
  read is assigned inside `check_claim_writable`. Observed by AC1.

## 3. Non-goals (OUT)

- No change to the run columns' stale rows, `preflight:foreign-stale` and `take-over:foreign-stale`,
  which stand at the base.
- No change to how a lease becomes stale: `leases.expiry-hours` and the observer-clock sighting stay
  `TOOL-dPlacedRequest-17`'s.
- No new act and no new refusal cause; the row restores what `tools/unattended/STOPS.template.md`
  section 7's table already states.
- No change to `tools/unattended/unattended.sh#run_entry_claim`: its routing of a stale build lease is
  `TOOL-dPlacedRequest-100`'s.

### Edges

- **consumes-from** external — the lease column this build's lease-grammar and hand-over units built
  and CLOSED; this unit restores one row in the landed code, and those specs stay frozen
- **hands-off** `TOOL-dPlacedRequest-100` — the entry claim's route for a stale build lease, which reads
  the take-over hint this unit's row sets on an acquire refusal and runs the take-over it lets write

## 4. Design

### The row

```
lease:foreign-released) ...as at the base...
lease:foreign-stale) case "$la" in
    take-over) CW_ACT=take-announced ;;
    acquire)   CW_CAUSE=live-holder; CW_HINT=take-over; return 1 ;;
    *)         CW_CAUSE=live-holder; return 1 ;;
  esac ;;
lease:foreign-tombstone) ...as at the base...
lease:*) CW_CAUSE=live-holder; return 1 ;;
```

It is the row commit 71f85d59f added, byte for byte, read by `git show 71f85d59f`. The verb's
refusal line already appends ` · stale, so --lease take-over takes it` when `CW_HINT` is set, and the
writer already announces a `take-announced` act and raises the epoch, so nothing else moves.

Cited at the base: the released row is `tools/unattended/unattended.sh@0e8038fd:2912` and the
catch-all `tools/unattended/unattended.sh@0e8038fd:2926`, inside
`tools/unattended/unattended.sh#check_claim_writable`; the hint is read in
`tools/unattended/unattended.sh#run_lease_verb` at `tools/unattended/unattended.sh@0e8038fd:4235`; the
announced take is `tools/unattended/unattended.sh#write_claim`'s; the run columns' stale rows stand at
`tools/unattended/unattended.sh@0e8038fd:2943`.

### The arms

- **Probe arm.** Over the bare-remote fixture `TOOL-dPlacedRequest-17` AC2 already builds in
  `tools/unattended/unattended.test.sh`, with its helpers `add_lease_commit` and `add_claim_sighting`:
  a build lease written by another session and first sighted 25 hours ago, past the catalogue's
  24-hour `leases.expiry-hours`. From a second session, `--lease acquire build <slug>` exits 1 with
  the stale hint, and `--lease take-over build <slug>` exits 0, prints the take, raises the epoch by
  one and logs `claim taken over`. The status table that asserts a lease-mode refusal for
  `foreign-stale` stays; it cannot see this loss, because acquire refuses either way.
- **Static arm.** Every `CW_*` name the lease verbs read, collected from the bodies of
  `run_lease_verb` and `write_fence_beat` by one `grep -o`, is assigned at least once inside
  `check_claim_writable`'s body, outside the reset block at its head. The reset block is defined by
  content, not by a line count: every line after the `local` lines whose every statement is a bare
  `CW_<NAME>=` assignment, up to the first line that is not. At the base it is two lines, and
  `CW_HINT=` sits only on the second, so a one-line exclusion would count it assigned. Staged against
  the column at 95c3103ad, the arm names `CW_HINT` as read and never assigned; that reading is
  recorded as its RED-first one.

The unattended kit's own suites are waived for this build's landing (README rule 8): the arms are
written and their clean reading is owed with PLAY-dClosedLoop-14, and AC1 observes the change by a
direct probe of the driver.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the restored row
- `tools/unattended/unattended.test.sh`: the probe arm and the static arm
- the unattended kit's version carrier, moved once by the kit-epoch rule

### Alternatives rejected

- **Fold the stale case into `lease:*` with a hint.** It keeps take-over refused, which contradicts the
  stops guide's table and the function's own header.

## 5. Production-readiness checklist

- security — restores a documented recovery act; a take-over still needs the lease stale by the
  observer's own clock, and is announced.
- perf / scale — one `case` arm; nothing measurable.
- error / empty / loading states — a stale lease reads as the stops guide's table states again.
- observability — the acquire refusal names the stale state and the verb that takes it.
- risks — a lease taken over by a node whose clock reads it stale early; that bound is
  `TOOL-dPlacedRequest-17`'s observer clock, unchanged.
- testing — AC1's probe and the arms in §7.
- migration — none.
- user docs — none: `memory/guides/UNATTENDED-STOPS.md` section 7 already states the row, and
  `help/loop.md` names no lease column.

## 6. Acceptance criteria

- **AC1** — When a scratch clone with a bare origin and `RUN_CLAIMS=on` holds a build lease written by
  session `s1` whose first sighting is planted 25 hours back, and `bash tools/unattended/unattended.sh
  --lease acquire build tStale` runs under session `s2`, it exits 1 printing `stale, so --lease
  take-over takes it`; and `--lease take-over build tStale` under `s2` then exits 0 printing
  `take-announced`, the remote lease's `epoch:` one above the planted one.
  Red when: the stale row is absent; the driver at 95c3103ad is that break, and there acquire prints
  `live-holder` with no hint and take-over exits 1, its RED-first reading.
  fixture: the scratch clone and origin, built by the probe; the tree holds none.
  permission: the suite that carries the arm is waived for this landing by README rule 8, so this probe
  observes the driver directly.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `scratch-guard self-test` · `tier2-review self-test` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC1 · the stale build lease taken over and the static CW_* join, staged against the lease column at 95c3103ad that lacks the stale row, where the static arm names CW_HINT read and never assigned · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft, promoted from the closing diff review round 1, item H2 (HIGH,
  finding id 3), by the round-2 exit's disposition.
- rev-2 · 2026-11-20 · §4 · §7 · folded 2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit finding
  id 12 (M8): the static arm's reset exclusion is defined by content, and its red reading at
  95c3103ad names `CW_HINT`. §1 · §3 · repair unit `TOOL-dPlacedRequest-100`, promoted by the same
  record's finding id 29 (H4): the Goal no longer claims the entry claim is repaired here, a non-goal
  leaves `run_entry_claim` to that unit, and the edge to it is declared.

## 10. Reuse audit

The seam extended is the lease column of `tools/unattended/unattended.sh#check_claim_writable`, and
the row restored is the one 71f85d59f wrote; the arm reuses `TOOL-dPlacedRequest-17` AC2's fixture
helpers rather than a new clock plant. `python tools/codebase-map/reuse_lookup.py "lease classified
stale is taken over"` ranked `resolveLease` in `tools/unattended/run-lease.js` and
`check_lease_only_diff`, name stems only, neither a seam for this row. The recall query below returned
the round-1 record's H2; none disagrees with the source read above.

Recall terms used: check_claim_writable lease column foreign-stale take-over take-announced CW_HINT acquire stale hint expiry-hours run_lease_verb
