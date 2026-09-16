# DEPL-cMendedVintage-16 — the lexicon outcome block cannot accept a failed first scaffold

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 25

<!-- gen:spec-records -->

*No record names this unit.*

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
- **S2** `tools/govkit/govkit.py`'s outcome probe honours `must_exist` beside `must_not_exist` in the
  same block, both resolved against the target through `target_context`, with the block matching only
  when EVERY declared term holds. A block declaring both today matches on the second term alone.
  Observed by AC3.
- **S3** `tools/govkit/matrix.py` gains one arm that stages a scaffold failure — `scaffold_lexicon.py`
  pointed at a destination it cannot write — and asserts `apply` reports lexicon as NOT adopted.
  Observed by AC1.
- **S4** The same file gains the CLASS assertion one level up: for every registry entry declaring an
  `[[outcome]]` with `ok = true` and a `must_not_exist` term, the named path may not be a file that
  entry's own `[adopt]` argv creates. Observed by AC4.

## 3. Non-goals (OUT)

- No per-step outcome scoping. Giving `[[outcome]]` a `steps = ["regenerate"]` key would let a kit
  declare one acceptance for `apply` and another for `update`, which is a descriptor-language
  widening and an owner turn under the fork rule's second veto. The narrowing in S1 closes the defect
  without it.
- No `[[outcome]]` for `memory-recall` or `drift-audit`. `DEPL-cMendedVintage-5` §3 refuses both and
  this unit does not re-adjudicate either.
- No change to `adopt-lexicon.sh`. Its exit code and its `|| exit 1` are correct; what is wrong is the
  descriptor that reads them.
- No change to what `classify_outcome` RETURNS or to `outcome_accepted`'s contract. S2 widens which
  terms a block may carry, not what an accepted outcome means.

### Edges

- **consumes-from** `DEPL-cMendedVintage-5` — that unit ships the block this unit narrows. The defect
  exists in the tree between that unit's landing and this one, which is stated rather than implied:
  both land inside this build and neither is pushed alone.
- **hands-off** external — nothing else in this build reads the outcome probe.

## 4. Design

### Why the shipped probe cannot tell the two states apart

The two states differ in exactly one observable, and the shipped probe reads the wrong one.

| state | `.lexicon.conf` | the rendered Skill | exit |
|---|---|---|---|
| unconfigured posture, `--render` declines | absent | absent | 1 |
| failed first scaffold | absent | absent | 1 |

That table is the finding, and it says the `must_exist` term in S1 cannot be the Skill after all: a
target that never configured lexicon has no Skill either. The discriminator that does exist is the
kit's own adoption marker — the file `adopt-lexicon.sh` writes BEFORE it reaches the scaffold, which
a target holding lexicon at all carries and a first install that died in the scaffold does not. S1's
`must_exist` term names that marker, and it is derived at build time from the adopter rather than
pinned here, because naming a path in a spec beside the script that owns it is the class this repo
already gates elsewhere.

If the build-time reading finds no such marker — that is, the adopter writes nothing before the
scaffold — then the two states are genuinely indistinguishable by a file probe and the unit's answer
is the second one in §4 Alternatives: the block is withdrawn and lexicon's decline is a loud failure,
matching `memory-recall`. That branch is written down because a builder who discovers it must not
have to invent a disposition.

### The probe change

`must_not_exist` is read today and `must_exist` is not, so S2 is an addition rather than a rewrite.
The rule between terms is AND: every declared term holds or the block does not match. An OR would let
a two-term block match on its weakest term, which is the defect this unit closes arriving through the
engine instead of through the descriptor.

### Inventory

| identifier | kind | where |
|---|---|---|
| `must_exist` | `[[outcome]]` key | `tools/govkit/govkit.py`'s outcome probe and `tools/lexicon/kit.toml` |

No function, flag or file is minted. A TOML key is not a cell this repo's lexicon declaration grades.

### Migration

None. No shipped `[[outcome]]` block carries a `must_exist` term today, so every existing block reads
identically after S2. A receipt is untouched.

### Rollout

Lands directly. S2 can only narrow which runs a block matches, and the only block carrying the new
term is the one S1 writes, so no other kit's acceptance moves.

### Alternatives rejected

- **Leave the block and accept the widening, documenting why lexicon may differ from memory-recall.**
  The spec-audit finding is that a decline reported as a success is the class this build exists to
  close. Shipping one inside it, with a paragraph, is the paragraph doing the work a probe should.
- **Withdraw the block entirely and let lexicon fail loudly, as memory-recall does.** This is the
  fallback §4 names if no marker exists. It is not the first choice, because an unconfigured lexicon
  IS a posture — the kit is installed and the project has declared no naming layer — and reporting it
  as a failed update reds every adopter who made that choice deliberately.
- **Discriminate on the exit code.** Both states exit 1, from the same `|| exit 1`. The code is the
  reason the descriptor needs a file probe at all.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the `must_exist` term in the outcome probe |
| `tools/lexicon/kit.toml` | the narrowed block, version bump |
| `tools/govkit/matrix.py` | the staged-failure arm and the class assertion |

## 5. Production-readiness checklist

- security — the probe reads file existence under the target root through `target_context`, the same
  resolution `must_not_exist` already uses. No new path class, no execution.
- perf / scale — one more `is_file()` per declared term.
- error / empty / loading states — a block declaring neither term matches on the code alone, which is
  BASE behaviour; a term naming a path outside the target resolves through the same containment the
  existing term uses.
- observability — a block that does not match reports the raw exit as an unaccepted failure naming
  the kit, which is what a failed first scaffold now produces.
- risks — the sharp one is in §4: if the adopter writes no marker before the scaffold, S1 has no
  discriminator and the unit falls to its withdrawal branch. That is a build-time reading, and the
  disposition for both outcomes is written above so neither needs an owner turn. Second: an AND rule
  between terms makes an over-declared block silently stop matching, which is a visible failure and
  not a silent acceptance.
- testing — AC1 through AC4; AC1 and AC2 against scratch fixture targets, AC3 and AC4 as arms over
  the shipped registry.
- migration — none; §4 states why.
- user docs — `tools/lexicon/README.md`'s adoption section gains one sentence on what the accepted
  stop means and what it deliberately does not cover.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target is taken through
  `python tools/govkit/govkit.py apply --target <fixture> --write` with `scaffold_lexicon.py` staged
  to fail, the run reports lexicon as not adopted and names the kit.
  Red when: the block still matches on `must_not_exist` alone, in which case the run classifies the
  failed install as the accepted stop `no-project-layer` and reports a kit that is not there.
  fixture: a scratch fixture target under the run's scratch root; this repo keeps no `.governance/`
  receipt and can host no criterion in this section.
- **AC2** — When the same command runs against a fixture whose lexicon is installed and whose
  `.lexicon.conf` was never written, the run reports the declared meaning `no-project-layer` and does
  not raise an unaccepted-exit failure.
  Red when: the narrowing is written so that the posture stops matching too, which turns a deliberate
  declaration into a red on every adopter who made it.
- **AC3** — When an `[[outcome]]` block declaring both a `must_exist` and a `must_not_exist` term is
  evaluated against a target satisfying only the second, `python tools/govkit/govkit.py selfcheck`
  reports the block as not matched.
  Red when: the terms are combined with OR, so a two-term block matches on its weakest term and the
  engine reproduces the descriptor defect one layer down.
- **AC4** — When the class arm at `tools/govkit/matrix.py` runs over `tools/govkit/registry.toml`, no
  entry declaring an `[[outcome]]` with `ok = true` and a `must_not_exist` term names a path that
  entry's own `[adopt]` argv creates, and staging one such entry turns the arm RED.
  Red when: the assertion is written against the lexicon entry by name, which certifies the one entry
  that exists and says nothing about the next one.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `lexicon wiring` · `kit version markers`

New arm: `tools/govkit/matrix.py` · a staged `scaffold_lexicon.py` failure asserted to report lexicon
as not adopted, beside the registry-wide class assertion staged by one conforming entry · no
assertion floor to move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

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
