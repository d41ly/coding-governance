# DEPL-cMendedVintage-16 — the lexicon outcome block cannot accept a failed first scaffold

**Status:** CLOSED · rev-2 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-DEPL-cMendedVintage-16-acceptance-ledger.md](../build/2026-09-16-build-DEPL-cMendedVintage-16-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-16-2-build-brief.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-16-2-build-brief.md) | journal | — |
| [2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md](../reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 |
| [2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md](../reviews/2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 DEPL-cMendedVintage-22 DEPL-cMendedVintage-23 DEPL-cMendedVintage-24 DEPL-cMendedVintage-25 DEPL-cMendedVintage-26 DEPL-cMendedVintage-27 DEPL-cMendedVintage-28 DEPL-cMendedVintage-29 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 TOOL-cMendedVintage-11 TOOL-cMendedVintage-12 TOOL-cMendedVintage-13 TOOL-cMendedVintage-14 TOOL-cMendedVintage-15 TOOL-cMendedVintage-16 TOOL-cMendedVintage-17 TOOL-cMendedVintage-18 TOOL-cMendedVintage-19 |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-cMendedVintage-5` S4 declares a lexicon `[[outcome]]` of `code = 1` plus
`must_not_exist = ".lexicon.conf"` plus `ok = true`. `classify_outcome` reads the kit-level
`desc["outcome"]` list (`tools/govkit/govkit.py:3750`) with no per-step scoping, so `apply`'s
CONFIGURE consults it too — and `adopt-lexicon.sh:497` exits 1 with `.lexicon.conf` absent when the
first scaffold FAILS, because the conf is what the failed program was writing. Narrow the probe so
the accepted stop is the unconfigured posture and not the failed install.

## 2. Scope (IN)

- **S1** The lexicon `[[outcome]]` block gains a `must_exist` term naming the rendered Skill that a
  `--render` decline leaves on disk and a failed first scaffold never writes, so the block matches
  the posture and not the failure. Observed by AC1 and AC2.
- **S2** ~~`tools/govkit/govkit.py`'s outcome probe honours `must_exist` beside `must_not_exist`~~ —
  **rev-2: ALREADY SHIPPED, no code written.** `classify_outcome` loops
  `(("must_exist", True), ("must_not_exist", False))` and breaks out on the first term that fails, so
  a two-term block already matches only when EVERY term holds. rev-1's premise — "a block declaring
  both today matches on the second term alone" — is false against this tree and was measured false
  before anything was edited. Two shipped blocks already depend on the conjunction
  (`memory-tree`, `codebase-map` each declare both terms), which is the second, independent proof.
  Observed by AC3.
- **S3** `tools/govkit/matrix.py` gains one arm that puts the SHIPPED lexicon descriptor through
  `classify_outcome` + `outcome_accepted` in both states — no Skill and no conf (the failed first
  scaffold) must be REFUSED, a rendered Skill with no conf (the posture) must be ACCEPTED.
  Observed by AC1 and AC2.
- **S4** The same file gains the CLASS assertion one level up: **every** registry entry's
  `[[outcome]]` block carrying `ok = true` must declare a `must_exist` term. An accepted stop
  declared by an ABSENCE alone is satisfied by every run that died before writing. Observed by AC4.

## 3. Non-goals (OUT)

- No per-step outcome scoping. Giving `[[outcome]]` a `steps = ["regenerate"]` key would let a kit
  declare one acceptance for `apply` and another for `update`, which is a descriptor-language
  widening and an owner turn under the fork rule's second veto. The narrowing in S1 closes the defect
  without it.
- No `[[outcome]]` for `memory-recall` or `drift-audit`. `DEPL-cMendedVintage-5` §3 refuses both and
  this unit does not re-adjudicate either.
- No change to `adopt-lexicon.sh`. Its exit code and its `|| exit 1` are correct; what is wrong is the
  descriptor that reads them.
- No change to what `classify_outcome` RETURNS or to `outcome_accepted`'s contract — and as of rev-2
  no change to `classify_outcome` at all.

### Edges

- **consumes-from** `DEPL-cMendedVintage-5` — that unit ships the block this unit narrows. The defect
  exists in the tree between that unit's landing and this one, which is stated rather than implied:
  both land inside this build and neither is pushed alone.
- **hands-off** external — nothing else in this build reads the outcome probe.

## 4. Design

### Why the shipped probe cannot tell the two states apart

**rev-2 replaces this section's table.** rev-1 compared the failed scaffold against an
"unconfigured posture" with no Skill, concluded the Skill could not be the discriminator, and routed
the unit at its withdrawal branch. That comparison is against a state `govkit` cannot produce. The
build-time reading:

| state | `.lexicon.conf` | the rendered Skill | exit | reachable how |
|---|---|---|---|---|
| declaration removed after an adopt | absent | **present** | 1 | the operator deletes the conf |
| failed first scaffold | absent | absent | 1 | `scaffold_lexicon.py` dies |
| never ran the adopter | absent | absent | 1 | `cp -r` copy-install |

`apply` never lands the Skill — `rendered` is absent from `LANDABLE_ROLES`, which is the whole reason
that role exists — so only `adopt-lexicon.sh` writes it, in the same `--scaffold` run that writes the
conf. A target that holds a Skill therefore got through the scaffold once, and that is the
discriminator rev-1 went looking for the adopter's own marker to find. There is no such marker (the
`--scaffold` branch writes nothing before `scaffold_lexicon.py`), but none is needed.

Row 3 is accepted collateral and is stated rather than hidden: it is byte-identical to row 2, so no
file probe separates them, and this unit reds it. Under `govkit` it is not reachable — lexicon
declares no `blocks_adopt` hole, so `apply` always runs CONFIGURE — and a `cp -r` install has no
receipt for `update` to iterate. The withdrawal branch below is therefore NOT taken.

### The probe change

**rev-2: there is no probe change.** rev-1 asserted `must_not_exist` is read today and `must_exist`
is not. Both are read, by one loop, with AND between them — a block matches only when every declared
term holds. So the engine already had the semantics S1 needs, and this unit writes zero lines of
`tools/govkit/govkit.py`. The conjunction is verified directly rather than assumed (AC3).

### Inventory

| identifier | kind | where |
|---|---|---|
| `must_exist` | `[[outcome]]` key, ALREADY READ by the engine | added to the block in `tools/lexicon/kit.toml` |
| `check_outcome_probes` | function | `tools/govkit/matrix.py` |

rev-2: one function is minted after all, leading with `check` from the declared verb table. The
offender pin is a two-sided equality, re-measured at 983 and unmoved.

### Migration

None. The term S1 adds is already honoured, two other shipped blocks already declare it, and no
descriptor outside `tools/lexicon/kit.toml` is edited. A receipt is untouched.

### Rollout

Lands directly. The only block whose acceptance moves is lexicon's, and it moves in the narrowing
direction: a state that was accepted is now refused, never the reverse.

### Alternatives rejected

- **Leave the block and accept the widening, documenting why lexicon may differ from memory-recall.**
  The spec-audit finding is that a decline reported as a success is the class this build exists to
  close. Shipping one inside it, with a paragraph, is the paragraph doing the work a probe should.
- **Withdraw the block entirely and let lexicon fail loudly, as memory-recall does.** rev-1's
  fallback if no discriminator existed. NOT TAKEN: one exists, and withdrawal would additionally red
  a state `adopt-lexicon.sh --check` itself calls "a legal state, not a defect" on exit 0 — govkit
  refusing what the kit's own check blesses.
- **Discriminate on the exit code.** Both states exit 1, from the same `|| exit 1`. The code is the
  reason the descriptor needs a file probe at all.

### Files touched (estimate)

| Path | Change |
|---|---|
| ~~`tools/govkit/govkit.py`~~ | rev-2: NOT TOUCHED — the conjunction already shipped |
| `tools/lexicon/kit.toml` | the narrowed block |
| `tools/govkit/matrix.py` | the two-state arm and the class assertion |
| `tools/lexicon/README.md` | what the accepted stop means, and what it does not cover |

rev-2 drops the version bump rev-1 estimated. No gate asks for one (`check-kit-versions.sh` grades
presence and marker/constant agreement, never "bumped on change"), a descriptor is re-read from the
gov tree on every run so nothing detects by version, and `DEPL-cMendedVintage-5` — which introduced
the block this unit narrows — already moved `KIT_LEXICON_VERSION` to 1.5 inside this same build. Both
units land together, so 1.5 dates both. Bumping again would ripple through four `gov:kit lexicon@`
carriers and force a Skill re-render for no reader.

## 5. Production-readiness checklist

- security — the probe reads file existence under the target root through `target_context`, the same
  resolution `must_not_exist` already uses. No new path class, no execution.
- perf / scale — one more `is_file()` per declared term.
- error / empty / loading states — a block declaring neither term matches on the code alone, which is
  BASE behaviour; a term naming a path outside the target resolves through the same containment the
  existing term uses.
- observability — a block that does not match reports the raw exit as an unaccepted failure naming
  the kit, which is what a failed first scaffold now produces.
- risks — rev-2: the marker risk above resolved to "no marker exists and none is needed" (§4). What
  is left is the cost §4 row 3 names — a tree that never ran the adopter now reds — and it is
  deliberate, stated, and unreachable through `apply`. Second: an over-declared block silently stops
  matching, which surfaces as a visible unaccepted failure and not as a silent acceptance.
- testing — AC1 through AC4, all four as arms in `check_outcome_probes` over the shipped registry
  and a scratch directory; each observed RED on a staged break before it was called done.
- migration — none; §4 states why.
- user docs — `tools/lexicon/README.md`'s adoption section gains one sentence on what the accepted
  stop means and what it deliberately does not cover.

## 6. Acceptance criteria

*rev-2 restates AC1–AC3 against the seam they actually grade. rev-1 spent all of AC1 and AC2 on a
full `apply` with a sabotaged `scaffold_lexicon.py`; what that would decide is `classify_outcome`'s
verdict over a target with no conf, which is reachable in one call with the SHIPPED descriptor. The
end-to-end plumbing between `apply` and that predicate is already graded by the deployability leg and
by `selftest.py`, and paying for a scratch install per arm is the "whole subject per arm" cost §7
names. The fixture is a scratch directory, not an install.*

- **AC1** — When `check_outcome_probes` in `tools/govkit/matrix.py` puts the shipped `lexicon`
  descriptor through `classify_outcome` + `outcome_accepted` at exit 1 against a target holding
  neither `.lexicon.conf` nor a rendered Skill — the failed first scaffold — the outcome is REFUSED.
  Red when: the block still matches on `must_not_exist` alone, in which case a failed install
  classifies as the accepted stop `no-project-layer` and the receipt is stamped for a kit that is not
  there. **Observed:** RED before the narrowing (`means='no-project-layer' accepted=True`), green
  after, and RED again with the `must_exist` term staged back out.
- **AC2** — Against a target holding a rendered `.claude/skills/lexicon/SKILL.md` and no
  `.lexicon.conf` — the declaration removed after an adopt — the same call reports
  `no-project-layer` and is ACCEPTED.
  Red when: the narrowing is written so the posture stops matching too, which turns a deliberate
  removal into a red on every adopter who made it.
- **AC3** — The conjunction itself: a block declaring both terms, evaluated against a target
  satisfying only `must_not_exist`, does not match. AC1's green IS this observation — lexicon's
  narrowed block is exactly that shape and the failed-scaffold state is exactly that target — so no
  separate fixture is owed.
  Red when: the terms are combined with OR, so a two-term block matches on its weakest term and the
  engine reproduces the descriptor defect one layer down.
- **AC4** — When the class arm runs over `tools/govkit/registry.toml`, every entry declaring an
  `[[outcome]]` with `ok = true` also declares a `must_exist` term, the arm refuses to grade an empty
  population, and staging a conforming entry turns it RED.
  Red when: the assertion is written against the lexicon entry by name, which certifies the one entry
  that exists and says nothing about the next one. **Observed:** three entries graded
  (`codebase-map`, `lexicon`, `memory-tree`); the liveness arm RED with the population emptied; the
  class arm RED with lexicon's `must_exist` staged out — the defect as `DEPL-cMendedVintage-5`
  shipped it.

rev-2 also narrows AC4's rule. rev-1 asked that the `must_not_exist` path not be one the entry's own
`[adopt]` argv creates. That rule is both undecidable statically — it needs a reading of a shell
script — and, taken literally, RED against the block S1 writes, whose `must_not_exist` is still
`.lexicon.conf`. What closes the class is the presence term: a block that also names a file that must
EXIST cannot be satisfied by a run that wrote nothing.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `lexicon wiring` · `kit version markers`

New arms, all in `check_outcome_probes` on the EXISTING `govkit acceptance matrix` leg — no new leg,
which is the cheaper side of the meta-gate trade: the two lexicon states over the shipped descriptor,
beside the registry-wide class assertion and its own non-empty-population arm · no assertion floor to
move.

Run in this pass, bounded, one question each: `check_outcome_probes` alone (six arms green, then RED
on each of three staged breaks), `python tools/govkit/govkit.py selfcheck` (rc 0 over the edited
descriptor) and `python tools/lexicon/lexicon.py` (`lexicon OK`, offender pin 983 unmoved by the new
function). The full matrix, `govkit selftest` and the bar itself belong to the run's closing bar.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-16 · build-time reading, four divergences. (1) S2 was already shipped: the outcome
  probe ANDs `must_exist` with `must_not_exist` today, measured before any edit, so no line of
  `govkit.py` moves. (2) §4's state table compared against a posture `govkit` cannot produce; `apply`
  does not land the Skill, so a Skill on disk proves the adopter got through `--scaffold` once and IS
  the discriminator §4 went hunting a marker for. The withdrawal branch is not taken. (3) S3's arm
  grades `classify_outcome` over the shipped descriptor instead of staging a sabotaged scaffold
  through a full `apply`. (4) S4's class rule becomes "an accepted stop must declare a `must_exist`
  term" — rev-1's argv-derived rule is statically undecidable and reds the block S1 writes. Also:
  no version bump, §4 says why. §3, §4's inventory / migration / rollout / alternatives, §5 and §7
  were then swept for halves left standing under rev-1's wording; the `--for-diff` checklist names
  that class and the sweep is what it bought.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "restore a snapshot entry whose kit key no rollback loop
selects"` was the probe run for this promoted set and it returned no seam for any member; its ranked
rows are name-token neighbours on the stems `kit` and `key`, and it named `.sh` as an unscanned
layer, so every adopter script this unit reasons about is outside the map's corpus by construction.
The seam this unit extends was read from source: `classify_outcome` at
`tools/govkit/govkit.py:3750`, which already resolves one file-existence term against the target and
is called from `apply`'s CONFIGURE at `:4894`, from `check` at `:2970` and from the re-render stage
at `:7438` — three callers of one predicate, which is what makes adding a second term cheaper than
adding a second probe. The recall probe returned `DEPL-cMendedVintage-5`'s own brief, which records
that lexicon's block is modelled on `tools/unattended/kit.toml`; reading that descriptor is where the
build-time marker question in §4 gets its answer, because that kit's block is the one shipped example
of a declared accepted stop.

Recall terms used: `--terms "govkit rollback snapshot attributes receipt row kit orphan restore
touched_kits claimed verify outcome regenerate"`, with the question "what decided how govkit rollback
selects snapshot entries by kit and what owns the synthetic attributes row".
