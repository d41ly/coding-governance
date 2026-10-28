# TOOL-dIndexedDesign-40 — the three new cutoff keys ship blank in the passes that add them, so `cutoff_keys_armed` holds its pin of 36 at every pass tip

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 18 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 31 to 38
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md`)
confirmed finding **id 2 at HIGH**, report item **H2**, the item's only id.
`tools/drift-audit/drift_report.py:2158-2177` counts non-blank `_CUTOFF` keys over the tracked root
confs, and `tools/drift-audit/drift_signals.py:351` pins that count, `cutoff_keys_armed`, at 36.
`TOOL-dIndexedDesign-6` S9 (order 7) sets `SPEC_AGREEMENT_CUTOFF` in `.memory-tree.conf`,
`TOOL-dIndexedDesign-8` S12 (order 8) sets `SPEC_FORK_RECORD_CUTOFF`, and `TOOL-dIndexedDesign-4` S5
(order 11) declares `SPEC10_PROBE_CUTOFF`. `TOOL-dIndexedDesign-38` S15 to S17 blank the three only at
order 17. The unguarded `drift-audit records` leg reads 37 against 36 from unit 6's pass until then.

This unit moves S15 to S17 into the passes that add the keys. Each of those passes ships its key
blank in `.memory-tree.conf`, and its own fixtures arm the key in their scratch confs. Its own pass
then reads the count at all three pass tips. It repairs `TOOL-dIndexedDesign-38` and takes order 18,
one above unit 38's 17.

## 2. Scope (IN)

- **S1** — `SPEC_AGREEMENT_CUTOFF=""` in `.memory-tree.conf`, written in unit 6's pass commit, an act
  ahead of this unit's order. Unit 6 S9's "gov sets the cutoff strictly ahead of its corpus" waits for
  an owner-attended landing, the route unit 38 §8 F3 resolved. Unit 6's criteria that need the key armed
  arm it in their fixture confs. Observed by AC1 and AC2.
- **S2** — `SPEC_FORK_RECORD_CUTOFF=""`, written in unit 8's pass commit on the same terms. Observed by
  AC1 and AC2.
- **S3** — `SPEC10_PROBE_CUTOFF=""`, written in unit 4's pass commit on the same terms. Observed by AC1
  and AC2.
- **S4** — Unit 38 S15 to S17 are true before unit 38's pass, so that pass writes nothing for them. Its
  AC12 observes them as already true, and its ledger carries the note `TOOL-dIndexedDesign-40 S4` under
  AC12's answer. Observed by AC3.

## 3. Non-goals (OUT)

- Raising the pin to 39: an owner ruling, every past raise being one (`drift_signals.py:337-350`), and
  unit 38 §8 F3 already refused it.
- Arming the three keys: an ask of this build, as unit 38 §8 F3 records.
- Any other `_CUTOFF` key, and the signal's reader.
- The report's left-shift checklist entry. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-6` — S9's `SPEC_AGREEMENT_CUTOFF`, which S1 keeps blank in that unit's own pass commit (id 2)
- **consumes-from** `TOOL-dIndexedDesign-8` — S12's `SPEC_FORK_RECORD_CUTOFF`, which S2 keeps blank in that unit's own pass commit (id 2)
- **consumes-from** `TOOL-dIndexedDesign-4` — S5's `SPEC10_PROBE_CUTOFF`, which S3 keeps blank in that unit's own pass commit (id 2)
- **consumes-from** `TOOL-dIndexedDesign-38` — S15 to S17 and AC12, which S4 finds true before that unit's pass (id 2)

## 4. Design

### Evidence

- `tools/drift-audit/drift_report.py:2158-2177`, `build_cutoff_keys_armed`, lists tracked files matching
  `\.[^/]+\.conf` and counts each `_CUTOFF` key with a non-blank value. The report's count over the five
  tracked root confs printed 36, read 2026-10-28; PINNED, and AC2 re-derives it.
- `tools/drift-audit/drift_signals.py:351` holds `"cutoff_keys_armed": 36`. The comment above it records
  each raise with its owner ruling or decision.
- `tools/gate-legs.json:1053-1068` holds the `drift-audit records` leg with no guard.

### Inventory

Minted: no identifier. Three blank conf values and one ledger note.

### Migration

None: each key is new in its own pass, so no armed value is ever withdrawn.

### Rollout

S1 lands in unit 6's pass (order 7), S2 in unit 8's (order 8) and S3 in unit 4's (order 11), each ahead
of this unit's order. Each unit's Edges block names its item, and its builder reads it there. S4 and
AC1 to AC3 are this unit's own pass at order 18, beside `TOOL-dIndexedDesign-41`. That unit writes no
conf, so the two write sets do not meet.

### Files touched (estimate)

- `.memory-tree.conf`: S1 to S3, in the passes of units 6, 8 and 4
- `memory/builds/dIndexedDesign/build/`: S4's ledger note and the recorded counts

### Alternatives rejected

- **Raise `cutoff_keys_armed` in each pass.** Lost to the owner-ruling history of every raise (M3 veto 2).
- **Leave S15 to S17 at order 17.** Lost to the confirmed finding: the leg reads red at every tip from
  order 7 to 16.
- **Arm each key in its pass and blank it in this unit.** Lost for the same reason, at more tips.

## 5. Production-readiness checklist

- security — N/A: three blank conf values.
- perf / scale — none.
- error / empty / loading states — a blank key turns its check off, which each check already announces
  (unit 6 AC3's `off` line, for one).
- observability — the drift report names every armed key with its file.
- risks — a builder reading only S9, S12 or S5 would set the key. AC1 reads each pass commit.
- testing — AC1 to AC3 by `git show`, `grep` and a count. No arm moves.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `git show <p>:.memory-tree.conf` is piped to
  `grep -E '^(SPEC_AGREEMENT|SPEC_FORK_RECORD|SPEC10_PROBE)_CUTOFF='` at the pass commits of units 6, 8
  and 4, each key present at a tip reads `=""`.
  Red when: a pass commit sets its key.
- **AC2** — When a `python -c` over `git ls-files` at each of those three pass commits counts the
  non-blank `_CUTOFF` keys of the tracked root `.*.conf` files, as `build_cutoff_keys_armed` reads them,
  it prints at most 36 each time. With one of the three keys set in a scratch copy of the conf, it
  prints one more.
  Red when: a tip counts above the pin, or the count does not move on the planted key.
  figure: 36 is PINNED by `drift_signals.py:351`.
- **AC3** — When `git show --stat <p>` runs at unit 38's pass commit `<p>`, it lists no change to
  `.memory-tree.conf` for S15 to S17. When `grep -n "TOOL-dIndexedDesign-40 S4"` runs over unit 38's
  acceptance ledger, it prints the note under AC12.
  Red when: unit 38's pass writes a key S1 to S3 already wrote, or the note is missing.
  permission: at this unit's pass, after unit 38's.

## 7. Gates

`drift-audit records` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `memory hygiene`

## 8. Open questions

- **F1 — How do three items land ten orders before this unit, when the harness places a repair after the
  unit it repairs?** Options: (a) each item is an act in the pass that adds its key, named in that unit's
  Edges and this Rollout, with AC1 reading each pass commit. (b) This unit at order 7 alone. (c) Raise
  the pin. (b) still leaves units 8 and 4 arming their keys after it. (c) is an owner turn (veto 2).
  RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, the one survivor, the act-ahead form unit 38 S2
  uses. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 31 to 38, id 2
  (HIGH, item H2), on the skeptic's corrected fix, repairing TOOL-dIndexedDesign-38 S15 to S17.

## 10. Reuse audit

The seam is the conf's own blank-means-off convention, which unit 38 §8 F3 already chose, read by
`build_cutoff_keys_armed` (`tools/drift-audit/drift_report.py:2158`). AC2 counts the way that function
does, and no new counter is written. The probe
`python tools/codebase-map/reuse_lookup.py "keep a conf key blank so the armed cutoff count stays at its pin"`
ranked `key`, `counts`, `keys`, `arm` and `load_conf`. None is a pin-keeping seam, so no existing seam
fits beyond the conf and the signal. The recall query returned dWitnessedBar scout C's note placing
`build_cutoff_keys_armed` and the pin, which agrees with source.

Recall terms used: `python tools/memory-recall/query.py "who keeps a new cutoff key blank under the cutoff_keys_armed pin" --terms "cutoff_keys_armed pin drift_signals drift-audit records armed cutoff keys conf blank owner ruling"`
