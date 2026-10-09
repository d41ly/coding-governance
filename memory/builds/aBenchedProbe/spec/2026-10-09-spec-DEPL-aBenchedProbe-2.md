# DEPL-aBenchedProbe-2 — a descriptor leg's `ceiling` travels into the adopter's manifest

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-2 · base 2b26f187 · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-DEPL-aBenchedProbe-2-1-acceptance-ledger.md](../build/2026-10-09-build-DEPL-aBenchedProbe-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aBenchedProbe-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-1-spec-brief.md) | journal | TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 DEPL-aBenchedProbe-1 |
| [2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md) | journal | TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 DEPL-aBenchedProbe-1 |
| [2026-10-09-prompt-TOOL-aBenchedProbe-1.md](../prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1.md) | research | TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 DEPL-aBenchedProbe-1 |

<!-- /gen:spec-records -->

## 1. Goal

An adopter's copy of a gov leg runs unbounded today, because the deployer writes no `ceiling` into
the manifest it emits. This unit lets a `[[gate_leg]]` declare one, declares 1780 s on the
`pre-push self-test` leg the owner named, and carries it into every adopter whose runner reads the
key, so a self-test that quadruples in cost reds instead of passing unnoticed.

## 2. Scope (IN)

- **S1** — `tools/govkit/entries/push-main.kit.toml`: the `pre-push self-test` row gains
  `ceiling = 1780`, equal to the value `tools/gate-legs.json` already carries for that leg. Observed
  by AC1 and AC6.
- **S2** — `tools/govkit/govkit.py`: a constant `CEILING_FLOOR_RUN_GATES = (1, 2)` beside
  `DOC_READS_FLOOR_RUN_GATES`, with a comment stating its provenance: the canary's key set gained
  `ceiling` in `db3616531` while the runner still read 1.1, and `836e4e27b` is the first commit at
  1.2, so 1.2 is the first version that certainly admits the key. Observed by AC2.
- **S3** — `write_gate_legs` in `tools/govkit/govkit.py` sets the row's `ceiling` from the
  descriptor when the descriptor declares one AND `check_target_reads_subject` holds at
  `floor=CEILING_FLOOR_RUN_GATES`. The receipt's `emitted` row gains a `ceiling` field holding the
  value gov computed, which is `None` when the descriptor declares none or the floor fails. Observed
  by AC1, AC2 and AC3.
- **S4** — the keep rule, at the same site. When the target's existing row carries a `ceiling` that
  differs from the receipt's recorded `ceiling` for that leg (absent counts as `None`), the written
  row carries the TARGET's value and the run prints one line naming the leg and both values. The rule
  sits outside the `argv`/`guard`/`doc_reads` drift comparison, so it never refuses the row and never
  withholds the manifest. A comment at the site states what it does not do (§3 N3, N4). Observed by
  AC4 and AC5.
- **S5** — `selfcheck` check 7h in `tools/govkit/govkit.py`, beside the `doc_reads` clause: a
  descriptor that declares `ceiling` must declare a positive `int` that is not a `bool` and EQUALS
  the manifest's `ceiling` for that leg, or it reds naming the entry, the leg and both values. A
  descriptor that declares none is not compared. Observed by AC6.
- **S6** — a module-level function `check_ceiling_emission(tmp)` in `tools/govkit/selftest.py`,
  called from `main()` beside the D4 block, holding the fixture arms AC1 to AC5 observe. It is
  module-level so a pass can run it alone. Observed by AC1, AC2, AC3, AC4 and AC5.
- **S7** — `tools/run-gates/README.md`, in "Every leg may declare a `ceiling`": one sentence saying
  the deployer carries a kit leg's `ceiling` into an adopter's manifest only where the kit's
  descriptor declares one and the adopter's runner is 1.2 or later, and keeps a value the adopter set
  by hand. Observed by AC7.

## 3. Non-goals (OUT)

- **N1** — no `ceiling` on any other descriptor leg. The owner's scope (d) names `pre-push.test.sh`
  alone; `pre-push bar self-test` and `push-main self-test` have no adopter measurement. The remainder
  of `TOOL-aBoundedCeiling-13` (a ceiling on every descriptor leg, and redding a descriptor leg that
  declares none) stays with that ask.
- **N2** — no `KIT_RUN_GATES_VERSION` bump for the floor. `TOOL-aBoundedCeiling-5` S4 needed one
  because the key entered at 1.1 unbumped; 1.2 has existed since `836e4e27b`, so the floor
  discriminates without one. The build's one bump per touched kit happens after the last unit, at
  the main loop, never in this pass.
- **N3** — the keep rule does not preserve a DELETED key. An adopter who removes `ceiling` from a
  gov-owned row gets gov's value back on the next update; the lever is a raised value, not an absent
  one.
- **N4** — no value is validated at emission. The descriptor is gov-authored and S5 grades its shape
  on every gov bar, so the emitter carries it verbatim; a malformed value in an adopter's own row is
  kept by S4 and read by their runner, which treats a non-positive or non-integer ceiling as none.
- **N5** — no edit to `.githooks/`, to `tools/run-gates/run-gates.sh`, or to `WIRE-INTO-PROJECT.md`.
  The first two belong to the concurrent run aThriftyLanding and TOOL-aBenchedProbe-2; the third is a
  governance carrier (M3 veto 2).

### Edges

- **consumes-from** external — an adopter runner at run-gates 1.2 or later. Measured 2026-10-09:
  both registered adopters run 1.31, and neither carries a `ceiling` on the three push-main rows in
  its manifest or its receipt, so the first update after this lands writes 1780 under S3 and S4 alike.
- **hands-off** external — `TOOL-aBoundedCeiling-13` keeps the ceilings for the other descriptor legs
  and the missing-ceiling red; this unit advances it without closing it.

## 4. Design

### The emission, at the existing seam

`write_gate_legs` already carries two optional keys behind a runner-version floor: `subject` at
`SUBJECT_FLOOR_RUN_GATES` and `doc_reads` at `DOC_READS_FLOOR_RUN_GATES`, both through
`check_target_reads_subject(target, deploy, descs, floor=...)`. `ceiling` is the third, in the same
shape and directly after the `doc_reads` lines (~4027-4036 at BASE):

```python
_ce = leg.get("ceiling") if check_target_reads_subject(
    target, deploy, descs, floor=CEILING_FLOOR_RUN_GATES) else None
if _ce is not None:
    row["ceiling"] = _ce
```

### The keep rule

Inside `if nm in by_name:`, after the existing drift `continue` and before
`existing[by_name[nm]] = row` (~4064-4075 at BASE), where `tgt` and `prev` are already bound:

```python
if "ceiling" in tgt and tgt["ceiling"] != (prev or {}).get("ceiling"):
    row["ceiling"] = tgt["ceiling"]
    print(f"govkit {verb} — gate leg '{nm}': kept the target's ceiling {tgt['ceiling']!r} "
          f"(gov's is {_ce!r}); a ceiling the receipt did not record is the target's own")
```

The receipt records `_ce`, gov's value, never the kept one. Recording the kept value would make the
next run see target and receipt agree and overwrite the adopter's bound, so the lever would last one
update. With gov's value recorded, a kept bound keeps differing and stays kept, and a target that
never touched the row always matches, so a new gov value lands. That is the
`DEPL-cMendedVintage-22` discipline: the TARGET is the comparison subject, and an untouched row
cannot wedge.

### The agreement arm

Check 7h builds `manifest_doc_reads` from `_legs_json` (~2683); a `manifest_ceiling` map joins it,
and the clause sits after the `doc_reads` comparison (~2741-2750). The local names are new in
`selfcheck` at BASE; the builder greps that function for them before adding them, because
`a-new-local-collides-in-a-long-function` selects this file.

### Inventory

| identifier | where | cell |
|---|---|---|
| `CEILING_FLOOR_RUN_GATES` | `tools/govkit/govkit.py` | module constant, not lexicon-graded |
| `check_ceiling_emission` | `tools/govkit/selftest.py` | `py.function`, verb `check`, confirmed by `lexicon.py --suggest` |
| `ceiling` | descriptor `[[gate_leg]]` key, receipt `emitted` row field | data keys |

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/govkit/entries/push-main.kit.toml`
- `tools/run-gates/README.md`

### Rollout

Order 3: it writes `tools/govkit/govkit.py` after DEPL-aBenchedProbe-1 and the push-main descriptor
after TOOL-aBenchedProbe-1. The pass runs `python tools/codebase-map/gen_map.py --write` after adding
`check_ceiling_emission`, because a new function stales the map's symbol set. Comments added to
`tools/govkit/govkit.py` name no adopter brand: the adopter ban in `tools/govkit/adopters.toml`
covers shipped files, and "adopter nc" is the sanctioned spelling.

### Alternatives rejected

- **Read the value from gov's manifest at emission**, with no descriptor key. It is one source
  instead of two, but every descriptor leg already has a manifest ceiling, so it ships a bound on
  every emitted leg rather than the one the owner named: 18 descriptor legs, all 18 with a manifest
  ceiling (DERIVED by a probe joining `tools/govkit/entries/*.kit.toml` to `tools/gate-legs.json`).
  gov's figures are also re-derived from node a's ledger, so each re-derivation would move adopters'
  bounds with no descriptor diff. Rejected under F2.
- **Refuse a differing ceiling as drift**, as `doc_reads` is refused. Rejected under F1.

## 5. Production-readiness checklist

- **security** — N/A — no new trust boundary. A gov-authored integer moves from a tracked descriptor
  into a manifest the emitter already writes.
- **perf / scale** — one integer per declaring leg, written once per apply or update.
- **error / empty / loading states** — a below-floor target gets no key (S3); a descriptor with no
  `ceiling` emits none (AC3); a target row with a hand-set value keeps it with one printed line (S4).
- **observability** — the keep rule prints one line naming the leg and both values. A below-floor
  withhold prints nothing, which matches the `subject` precedent and is stated here, not implied.
- **risks** — on the owner's six measured adopter nc runs of this leg (815, 1420, 1469, 2135, 1815
  and 3500+ seconds, PINNED from the prompt of 2026-10-09), three exceed 1780, so an adopter's
  `GATE_SELFTESTS=1` run there would red after its serial retry. That is the verdict the owner asked
  for; the lever is S4, a raised value the deployer keeps. After TOOL-aBenchedProbe-1 the leg is held
  on an adopter's default bar, so no default bar reds on it.
- **testing** — AC1 to AC5 run the one function S6 adds, sliced; AC6 is a staged break under
  `govkit selfcheck`; AC7 is a grep. No suite and no bar runs in the pass.
- **migration** — additive. Removing the S3 lines restores today's emitter exactly; a target already
  holding a `ceiling` keeps it, and a receipt without the field reads as `None`.
- **user docs** — S7, in the run-gates kit README beside the existing `ceiling` contract.

## 6. Acceptance criteria

The slice `S` below is
`python -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.check_ceiling_emission(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`,
run from the repo root. It runs the one function S6 adds and nothing else.

- **AC1** — When the slice `S` applies `push-main` into a fixture whose runner check holds (a
  D4-shaped target with a manifest-kind `[gate_runner]` and no run-gates installed), the
  `pre-push self-test` row of the written manifest carries `"ceiling": 1780` and the receipt's
  `emitted` row for that leg carries `ceiling` 1780; `S` prints an empty `FAILURES` list. With the S3
  lines absent from `write_gate_legs`, the same arm prints FAIL, which is the BASE emitter observed red.
  Red when: the row or the receipt row lacks `ceiling`, or the arm passes against the BASE emitter.
  cost: the fixture applies one kit; budget a minute on a contended host.
  fixture: built under the default `%TEMP%`, never the session scratchpad, whose path length
  false-reds govkit fixtures.
- **AC2** — When the slice `S` runs, its floor arms observe `check_target_reads_subject` at
  `floor=govkit.CEILING_FLOOR_RUN_GATES` answer False for a fixture runner declaring
  `KIT_RUN_GATES_VERSION=1.1` and True for 1.2, the constant equal `(1, 2)`, and the `govkit.py`
  source route the write through `floor=CEILING_FLOOR_RUN_GATES`. A below-floor full apply is not
  observed, for the reason the D4 comment gives: a fixture holding a run-gates install needs a receipt
  claim it cannot plant.
  Red when: 1.1 is accepted, 1.2 is refused, or the writer passes `SUBJECT_FLOOR_RUN_GATES` or no floor.
- **AC3** — When the slice `S` reads AC1's manifest, the `push-main self-test` and
  `pre-push bar self-test` rows carry no `ceiling` key.
  Red when: either row carries one, which is a default or a manifest fallback the design rejects.
- **AC4** — When the slice `S` sets that fixture's `pre-push self-test` ceiling to 3600, commits it,
  and applies `push-main` again, the apply exits 0, the row still reads 3600, stdout carries the
  `kept the target's ceiling` line naming the leg, and no `differs from what the receipt recorded`
  line prints.
  Red when: 3600 becomes 1780, or the apply refuses the row as drift.
- **AC5** — When the slice `S` sets both that fixture's row ceiling and the receipt's recorded
  `emitted` ceiling for the leg to 1000, commits, and applies `push-main` again, the row reads 1780.
  This is the arm that keeps AC4 from passing on a rule that keeps every value.
  Red when: the row stays 1000.
  fixture: the receipt edit must leave the apply's receipt preamble satisfied; if it does not,
  the govkit selftest's `write_vintage_receipt` helper is the precedent for a legal rewind.
- **AC6** — When the push-main descriptor's `pre-push self-test` ceiling is set to 1781 in the
  working copy and `python tools/govkit/govkit.py selfcheck` runs, it prints a 7h ceiling refusal
  naming entry `push-main`, the leg, 1781 and 1780; set to `true`, it prints the refusal again;
  restored, it prints no ceiling refusal.
  Red when: either staged break prints no ceiling refusal, or the restored tree prints one.
  cost: one selfcheck run per state, each under the leg's 310 s ceiling.
  fixture: other selfcheck arms may red on the same tree during the build; only the ceiling line is
  this criterion's.
- **AC7** — When `grep -n "1.2" tools/run-gates/README.md` runs after the pass, a line in the
  `ceiling` section names the deployer carrying a kit leg's `ceiling` and the 1.2 floor.
  Red when: no such line prints.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates`

New arm: tools/govkit/selftest.py check_ceiling_emission · covers AC1 AC2 AC3 AC4 AC5 · the S3 lines absent, the floor constant at (1, 1), and the keep rule inverted · none
New arm: tools/govkit/govkit.py selfcheck 7h ceiling agreement · covers AC6 · the push-main descriptor's ceiling set to 1781 and to true · none

The guarded legs above are the ones the estimate's `tools/govkit/` paths trip; `tools/` and
`tools/run-gates/` are broad guards the checker excludes. The last two legs grade the new function's
name and the map's symbol set. The close runs them; no pass does.

## 8. Open questions

- **F1 — What does an adopter's hand-set `ceiling` on a gov-owned row get at the next update?**
  Options: (a) not compared, so gov's value overwrites it; (b) added to the `argv`/`guard`/`doc_reads`
  drift comparison, so the row is refused and the whole manifest withheld; (c) the keep rule, which
  writes the target's value and lands everything else. The discriminating probe read both adopters'
  manifests and receipts: neither carries a `ceiling` on the three push-main rows, so all three
  options write 1780 on the first update and none fails a criterion today. They differ on a later
  hand-raise: (a) undoes it silently, (b) holds every gov leg update in that target hostage to one
  raised bound, which would also block a future subject flip like TOOL-aBenchedProbe-1's, and (c)
  keeps it and reports it. (c) is the predicate `TOOL-aBoundedCeiling-5` S7 settled over two audit
  rounds. No veto applies to (c): no dependency, no carrier, and it writes less than (a).
  Recommendation: (c).
  RESOLVED (agent, 2026-10-09, delegated): (c), the keep rule of S4, with the receipt recording gov's
  value so a kept bound stays kept.
- **F2 — Does the emitted value come from a descriptor key or from gov's manifest?**
  The manifest route is one source instead of two, and the descriptor route needs S5's agreement arm.
  The probe in §4 Alternatives rejected measured the difference: the manifest route bounds all 18
  descriptor legs on every adopter's bar, 17 more than the owner named, with values re-derived from
  node a's ledger. That widens the verdict surface the deployer writes into adopters beyond what this
  unit priced, which is M3 veto 3 and an owner turn. Recommendation: the descriptor key.
  RESOLVED (agent, 2026-10-09, delegated): the descriptor key, gated equal to gov's manifest by S5.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The seam is `check_target_reads_subject` in `tools/govkit/govkit.py` with its `floor` parameter, the
reader `subject` and `doc_reads` already use inside `write_gate_legs`; this unit is its third caller
and adds a constant, not a mechanism. `tools/codebase-map/reuse_lookup.py`, asked "carry a gate
leg field into the adopter manifest above a runner version floor", did not surface it (it ranked
name stems such as `legs`, `manifest` and `derive_carry_map`), so the seam was confirmed by reading
`tools/govkit/govkit.py` at ~3861-4095 and ~5561-5640 at BASE. The recall probe found the prior
design: `TOOL-aBoundedCeiling-5`, retired WONTDO with only its S6 built, and its carry-forward ask
`TOOL-aBoundedCeiling-13`, now DEFERRED. This spec takes that design's floor shape, its 7h parity arm
and its S7 keep predicate, and departs in three places, each stated above: one leg rather than every
descriptor leg (N1), no version bump (N2), and no red for a descriptor leg that declares none.
Where the record was STALE: its S4 bump and its "every current adopter is below the floor" premise
no longer hold, because 1.2 exists and both adopters run 1.31. `TOOL-dThriftyLanding-4` is the
`doc_reads` precedent the emission copies line for line.

Recall terms used: `ceiling emitter gate_leg descriptor adopter floor canary doc_reads drift receipt unbounded wall-clock subject`,
with the question "does the deployer carry a leg's wall-clock ceiling into an adopter's gate-legs
manifest, and at which runner floor" passed to `tools/memory-recall/query.py`.
