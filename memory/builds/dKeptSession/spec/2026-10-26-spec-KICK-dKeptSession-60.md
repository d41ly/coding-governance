# KICK-dKeptSession-60 — the policy kit's rule for a new mirror input names both lists and the case that holds them equal

**Status:** DEFERRED · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 6 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-60-deviation-601.md](../build/2026-10-26-build-KICK-dKeptSession-60-deviation-601.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-57-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-57-spec-audit.md) | spec-audit | KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-61 KICK-dKeptSession-57 KICK-dKeptSession-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's twelve round-2 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`)
confirmed finding **id 23 at HIGH**, report item **H3**. Id 10 shares the item and is promoted as
`KICK-dKeptSession-59`, the parity case's half.

dGroundRules' `tools/policy/README.md` states "THE RULE: a unit adding a resolution input adds its
path to `LEGACY_INPUTS`", and `policy.py`'s comment above that tuple says the same. After
`KICK-dKeptSession-40` and `KICK-dKeptSession-49`, a kit-relative input lives in
`derive_mirror_inputs` and in the JS reader's `MIRROR_KIT_INPUTS`, which neither text names, and
unit 49's Files touched does not list the README. The next input added the documented way therefore
reaches one list, and a mirror rendered before it reads FRESH in JS. This unit states the rule once,
naming both lists and the case that reds them apart. It repairs `KICK-dKeptSession-49` and builds
one step after it (order 6).

## 2. Scope (IN)

- **S1** — id 23. The rule. In `tools/policy/README.md`'s "The mirror" section, THE RULE reads: a unit
  adding a repository-relative resolution input adds its path to `LEGACY_INPUTS`; a unit adding a
  kit-relative input adds its name to `derive_mirror_inputs` in `policy.py` and to
  `MIRROR_KIT_INPUTS` in `policy-mirror.js`, and `python check_policy.py --fixture
  mirror-input-parity` (`KICK-dKeptSession-59`) reds the two lists apart. Observed by AC1.
- **S2** — id 23. One statement. `policy.py`'s comment above `LEGACY_INPUTS` stops restating the
  rule and points at the README's: the tuple holds the repository-relative inputs, and the rule for
  adding one is THE RULE in `tools/policy/README.md`. Observed by AC2.
- **S3** — id 23. The write set named. The README edit the report asks of unit 49's Files touched is
  this unit's, so unit 49's write set stays as its spec states. NOT OBSERVED: a placement of work,
  with no behaviour; S1's criterion observes the edit itself.

## 3. Non-goals (OUT)

- The parity case itself: id 10, `KICK-dKeptSession-59`.
- The README's upgrade sentence for a pre-unit mirror: `KICK-dKeptSession-50` S3, unchanged.
- The README's mirror text the batch's item for id 41 names: `KICK-dKeptSession-56` S42.
- The report's left-shift hygiene arm, that a non-goal handing work to a unit whose spec does not
  name it reds. It is a separate gate, so a separate unit by M2, and no clause of this build names
  it.

### Edges

- **consumes-from** `KICK-dKeptSession-49` — `MIRROR_KIT_INPUTS`, the JS list this unit's rule names beside Python's (id 23)
- **consumes-from** `KICK-dKeptSession-59` — the `mirror-input-parity` case, which the rule names as the check a new input meets (id 23)
- **hands-off** `KICK-dKeptSession-63` — S1's rule, AC1 and §7's leg line, which the batch's S4 widens to `MIRROR_LEGACY_INPUTS`, its S10 reads by paragraph and its S13 completes at reconcile (ids 2, 12, 18)

## 4. Design

### Evidence

- `tools/policy/README.md` at `3c8c4718a`, "The mirror", line 290-291: "THE RULE: a unit adding a
  resolution input adds its path to `LEGACY_INPUTS`, so its blob joins this map."
- `policy.py` at `3c8c4718a`, lines 810-813: "A unit adding a resolution input adds its path here
  (TOOL-dGroundRules-21 S17)", then `LEGACY_INPUTS = (LEGACY_FANOUT,)`.
- spec-49 §4 Files touched lists `policy-mirror.js` and `check_policy.py` only.

### Inventory

No identifier is minted.

### Migration

None: two texts change.

### Files touched (estimate)

- `tools/policy/README.md`: S1
- `tools/policy/policy.py`: S2, the comment only

### Alternatives rejected

- **Amending only the README.** The comment beside the tuple is the text a maintainer reads at the
  edit, and it would still give the one-list rule; two statements of one rule is the defect.
- **Amending only the comment.** The README is the kit's documented contract, which the report
  names as the source a later unit follows.

## 5. Production-readiness checklist

- security — none: documentation and a comment.
- perf / scale — none.
- error / empty / loading states — none.
- observability — the rule names the case whose red explains a one-sided edit.
- risks — none.
- testing — the criteria of §6; no arm is added.
- migration — none.
- user docs — `tools/policy/README.md`, S1; `help/policy.md` does not describe the mirror's inputs.

## 6. Acceptance criteria

The fixture is the policy kit's checkout once dGroundRules has landed it.

- **AC1** — When `grep -n "MIRROR_KIT_INPUTS" README.md` runs in the policy kit, it prints THE RULE's
  sentence, which also names `LEGACY_INPUTS`, `derive_mirror_inputs` and `mirror-input-parity`.
  Red when: the rule names `LEGACY_INPUTS` alone.
- **AC2** — When `grep -c "adds its path here" policy.py` runs in the policy kit, it prints `0`, and
  `grep -n "README.md" policy.py` prints the comment above `LEGACY_INPUTS`.
  Red when: the comment still states its own version of the rule.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-2 promotions' audit, H3 (id 23).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is dGroundRules' own rule paragraph in `tools/policy/README.md` ("The mirror", at
`3c8c4718a`) and the comment above `LEGACY_INPUTS` in `policy.py`; no new document is written.
`python tools/codebase-map/reuse_lookup.py "rule paragraph naming which list a new mirror input
joins"` returned name-stem candidates only; the policy kit is not at this base, so no existing seam
in the tree fits and the branch's README is the one extended.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted unit placed when it
repairs an earlier unit's pass" --terms "promoted order pass commit ledger superseded batch minors
hands-off consumes-from parity mirror"`
