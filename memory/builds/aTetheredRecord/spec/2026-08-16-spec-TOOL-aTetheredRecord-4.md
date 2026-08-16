# TOOL-aTetheredRecord-4 — check 21: the binding becomes the merge bar

**Status:** SPECCED · rev-3 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling · ratified 2026-08-17

## 1. Goal

Turn the binding from a convention into a gate. Four `fail` branches in the tracked shell engine —
the only place the harness meta-gate can count them — enforce that every record carries a conformant
line, that every id it names resolves to a SPEC, that the unbound escape stays bounded, and that the
filename agrees with the header it projects.

## 2. Scope (IN)

- **S1** — `PRE_BINDABLE`, a new precondition beside the existing four at
  `tools/memory-tree/check-memory-hygiene.sh:131-134`, in `PRE_RECORD`'s shape: a count over `$FILES`
  of paths matching `/(build|prompts|reviews)/`, deliberately UN-anchored to the
  `<memory root>/builds/<slug>/` prefix. The anchoring is the whole point — a precondition that
  restates the check's own population can never differ from it, so `pop_guard` becomes unreachable
  and the vacuity guard is decoration. Un-anchored, a record left at a pre-flatten path counts toward
  the precondition and not the population, which is exactly the mis-segmentation the guard exists to
  name.
- **S2b** — Extend `--print-bindings` with one row per BOUND record carrying its kind and its
  resolved id set, so branch 4 computes filename-versus-header membership from the module's output
  instead of parsing every record a second time. This AMENDS `TOOL-aTetheredRecord-2` S3, which
  shipped before Fork A created branch 4: a conformant record is not a finding, so the original
  output described one nowhere. The amendment is recorded here, and that unit's §9 points at it.
- **S2** — The check-21 block, placed after check 12. Its population is any tracked file at any depth
  under a build's `build/`, `prompts/` or `reviews/` folder, with NO extension filter. It carries the
  population guard, skips under the staged-diff mode, and delegates the parse to the module from
  `TOOL-aTetheredRecord-2` in the shape check 9 already uses.
- **S3** — Four `fail 21` branches, each with a distinctive longest literal run so the sibling test
  can assert it verbatim. The fourth binds the filename to the header and exists because Fork A
  ratified the rename.
- **S4** — `RECORD_UNBOUND_PIN` in `.memory-tree.conf`, MEASURED against this corpus by
  `TOOL-aTetheredRecord-3`, with its measurement note; blank in the shipped example conf; and a
  ratchet row in `tools/drift-audit/drift_signals.py` declaring that raising it is the weakening
  direction.
- **S5** — `ARMS_FLOORS` for `tools/memory-tree/check-memory-hygiene.sh` moves from `14:14` to
  `18:18`, stated as a literal here because `check-arms.py` compares one-sidedly: an UNDER-set floor
  passes silently, so the value has to be asserted rather than derived from a passing run.
- **S9** — Bump `KIT_MEMORY_TREE_VERSION` and every `gov:kit memory-tree@` marker, re-rendering the
  three doc pairs. A non-comment change to the engine is exactly what `check-verdict-epoch.sh` dates,
  and this unit moves the engine. (`TOOL-aTetheredRecord-2` already spent 2.17, so this unit spends
  the next one.)
- **S6** — Fixtures and four arms in `tools/memory-tree/check-memory-hygiene.test.sh`, each asserted
  inside check 21's own output block rather than against a global hit. Branch 4 needs three fixtures,
  because it is the branch with three ways to be wrong: an ordinal naming a real id the header omits;
  a CROSS-BUILD record whose filename correctly takes the SERVED id's slug rather than its housing
  build's, which must stay GREEN; and a bound record whose filename carries no family qualifier.
- **S7** — Rename the leg and every carrier of its check count. Measured: eight spellings across
  seven files, of which six are authored and two re-render.
- **S8** — Correct `memory/project/unarmed-branches.txt`'s header, which declares the file empty
  while carrying a row, and the same claim in `memory/HYGIENE.md` and its shipped template.

## 3. Non-goals (OUT)

- **No filename MOVES.** `TOOL-aTetheredRecord-7` performs them. This unit ships §4's redefinition of
  what the ordinal MEANS and branch 4, which enforces it. (This non-goal previously described Fork A's
  losing option as the one shipping — it was written before the owner resolved the fork.)
- **No render change** — that is `TOOL-aTetheredRecord-5`.
- **No relation kind.** The check reads which ids a record names, never what it did to them.
- **No widening of the harness meta-gate beyond shell.** Recommended separately; this unit keeps its
  branches in the shell precisely so it does not depend on that change.
- **No new gate leg.** Check 21 rides the leg that already exists, which is why this unit does not
  pay the codebase-map coverage assert or the drift-audit leg-count signal.

## 4. Design

### The four branches, and why the second is not redundant

**Branch 1 — presence.** A record whose head carries no conformant line. The population is the
extension-agnostic one from S2, because the corpus contains a shell-script record and an
extension-scoped rule would structurally exclude the one file most likely to be forgotten.

**Branch 2 — the id resolves to a SPEC.** Check 14 already reds an id cited and never defined, and a
binding line's ids are ordinary citations, so typo resolution is free. But check 14's definition set
is wider than this rule needs: `corpus_ids.py` records a definition from a decision-row anchor as
well as from a spec H1. An id defined only by a decision row therefore satisfies check 14 while
naming no spec at all. Branch 2 narrows resolution to the spec-defined set and closes exactly that
gap. This is the whole of the delta between the free check and the needed one.

**Branch 3 — the escape stays bounded.** Records carrying the unbound form are counted against a
shrink-only scalar. The reason prose is mandatory at parse time, so the escape is never silent; the
pin is what stops it becoming the default.

**Branch 4 — the filename agrees with the header.** Fork A ratified renaming every record, so the
filename now carries a binding too and two carriers can disagree. This branch is what keeps that from
being a second answer: the filename is a PROJECTION of the header, and the check asserts the
projection is a member of the set it projects from. Its input is S2b's per-record row — a bound
record is not a finding, so nothing else in the mode's output describes one.

The projection is a WHOLE id: family, slug and ordinal together. Family-and-ordinal alone would let a
record housed in one build match a same-numbered id in another, which is the collision this build
exists to remove rather than relocate. A record whose binding is not `none` and whose filename
carries no family qualifier reds here too — the qualifier is optional in check 5's grammar and
mandatory for a bound record, because two thirds of an id is not a projection of it.

### The ordinal is REDEFINED, not widened — and that is what makes the rename safe

The design pass killed the filename carrier partly on a real blocker: widening check 5's ordinal slot
to admit an id LIST would make the closed family alternation vacuous for the whole non-spec
population, flipping a live fixture from red to green. That blocker is avoided rather than accepted,
because the rename does not widen anything.

The recording-name grammar keeps its exact shape. What changes is what the ordinal MEANS: today it is
a per-kind round counter, and after the rename it is the sequence number of a spec the record serves.
The family qualifier, already optional in the grammar, becomes REQUIRED for every bound record —
not only in a multi-family build. A carve-out would make branch 4 partial, and a partial projection
is one a reader cannot trust without first knowing which case they are in.

The filename's `<kind>` remains the one check 5 derives from the SUBFOLDER. It is NOT the Fork E
relation kind, which is header-only: `spec-audit` in a filename would red check 5 and branch 4 at
once. Two vocabularies named "kind" now exist in this build and they never meet.

Three cases follow, and none needs a grammar change:

| Case | Filename | Why it is unambiguous |
|---|---|---|
| serves one spec | family and seq of that spec, with the existing optional tail distinguishing several records on one spec | the projection is the whole set |
| serves several specs | family, slug and seq of the LOWEST id in the header's list, tail distinguishing | the header is authoritative for the set; the filename names its least member, and branch 4 asserts membership. LOWEST is a TOTAL order and must be: family by its position in `.memory-tree.conf`'s `FAMILIES`, then slug bytewise, then ordinal numerically. Lexicographic family order disagrees with the declared order, and five builds in this corpus hold multi-family spec sets, so an unstated tie-break is a decision the builder would invent and bake into 77 filenames |
| serves none | the build-scoped ordinal it has today | branch 4 skips a record whose header says `none`, because there is no id to project |

This is a projection with a gate, not two answers to one question. The header remains the single
authored source; the filename is derived from it and mechanically checked against it, which is the
same relationship the generated index has to the specs.

### The literal messages

`check-arms.py:104-113` takes a branch's signature as the LONGEST literal run between interpolations,
stripped of trailing punctuation. Each message below therefore carries one long, distinctive run, and
the interpolated list follows it:

- `records under build/, prompts/ or reviews/ whose head carries no conformant Serves line:`
- `Serves or Commissions lines naming an id that no spec in this tree defines:`
- `records carrying the unbound Serves form outnumber RECORD_UNBOUND_PIN — bind them, or move the pin recording the old and new values beside it:`
- `record filenames whose family, slug and ordinal name an id their own Serves line does not list:`

None contains a positional parameter, which `check-arms.py` would read as literal text inside the
signature and no assertion could ever emit. Each message is written so its interpolation FOLLOWS the
whole literal run: `signature()` takes the LONGEST run between interpolations, so a message with a
value in the middle arms on whichever half is longer, which is not a choice anyone made. The four
strings above ARE the four signatures, and each sibling arm must contain its own verbatim.

### The vacuity guard

`pop_guard` compares a PRECONDITION against a POPULATION so a young tree and a mis-segmented selector
are distinguishable. The precondition here must be coarser than the population and must not be the
existing record precondition, which counts specs and READMEs too — reusing it would make a
freshly-scaffolded adopter tree with a spec but no records look mis-segmented. S1's precondition
reads zero on a tree with no records, so the check is silently skipped there, and non-zero with an
empty population only when the selector is wrong.

### Rollout

Check 21 lands LAST, after `TOOL-aTetheredRecord-3` has made the corpus conformant, so the tree is
never left weaker mid-run and never red between commits. This ordering is available only because the
owner put the retrofit in scope; with a cutoff it would have been the other way around.

### Inventory — the check-count carriers

| Carrier | Form | Authored or generated |
|---|---|---|
| `tools/gate-legs.json:3` | the leg name | authored — the single source |
| `AGENTS.md:94` | prose | authored |
| `README.md:33` | hyphenated prose | authored |
| `tools/memory-tree/README.md:6` | hyphenated prose | authored |
| `tools/memory-tree/README.md:18` | the kit table row | authored |
| `memory/map/baseline.toml:30` | the map baseline key | authored |
| `memory/map/generated/MAP.md:39` | the map render | generated — re-renders |
| `memory/map/generated/inventories.json:32` | the map render | generated — re-renders |

A `20 checks` search finds six of the eight and misses both hyphenated spellings. The predicate must
match a digit run followed by either a space or a hyphen and the word check; a prior review in this
corpus used exactly that pattern for exactly this reason.

### Alternatives rejected

**A third call site behind check 5.** The test harness re-arms on each check's failure header, so a
second unrelated predicate behind one number destroys attribution between the name-grammar branch and
the binding branch. Check 21 gets its own number.

**A seventh registry instead of a scalar pin.** The registry buys "which files", which is already
visible inline in each record. It costs the structure-lint whitelist arm, the word naming how many
registries exist in the charter and in the hygiene doc and its shipped template and their rendered
mirrors, the memory root's own index, the copy the adopter script writes, plus heredocs and fixtures
— a sweep a prior unit measured and concluded is not a small edit.

## 5. Production-readiness checklist

- security — N/A; the check reads tracked text.
- perf / scale — one bounded head parse per record, delegated to a module the gate already calls.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a tree with no records skips the check via the population guard; a
  malformed line is branch 1, not a crash.
- observability — the read-only mode from `TOOL-aTetheredRecord-2` reports the same classification
  the gate acts on.
- risks — the population guard is the failure mode that matters: too narrow a precondition disarms
  the check silently. Its arm is an explicit scratch-tree case. The pin is the second: it is
  shrink-only and its raise direction is declared to drift-audit.
- testing + left-shift gates — three arms, each inside check 21's own output block.
- migration / rollback — lands last, onto a conformant corpus; revertible as one commit.
- user docs — the catalog entry lands in `TOOL-aTetheredRecord-2`; this unit renames the leg.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/check-arms.py --report` runs, the hygiene engine shows
  four more branches than today and all of them armed, and `ARMS_FLOORS` matches.
- **AC1b** — When a record is renamed so its ordinal names a real id its own `Serves` line omits,
  `bash tools/memory-tree/check-memory-hygiene.sh` reds on branch 4 and not on branch 2.
- **AC1c** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, it covers the
  per-bound-record row S2b adds, and `--print-bindings` still exits 0 and leaves
  `git status --porcelain` empty.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, it is green, and each of
  the three arms asserts inside check 21's own output block rather than against a global hit.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs against a scratch tree holding
  one build, one spec and zero records, it exits 0 and prints no check-21 line in the missing-
  population report.
- **AC3b** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs against a scratch tree
  holding a record at a PRE-FLATTEN path, its missing-population report DOES name check 21. AC3
  covers only the quiet direction, and a guard never observed firing is the vacuity class this check
  is supposed to be immune to.
- **AC4** — When `python tools/drift-audit/drift_report.py --check` runs, it is green, and the new
  ratchet row reds against a hand-raised `RECORD_UNBOUND_PIN`.
- **AC5** — When `git grep -nE '[0-9]+[- ]check'` runs over the tracked tree, every live carrier
  reads the new count and none reads the old one.
- **AC6** — When `python tools/codebase-map/test_codebase_map.py` runs after the leg rename and the
  map re-render, it is green.
- **AC7** — When `bash tools/run-gates.sh` runs, every leg is green.

## 7. Gates

`memory hygiene` — its own new check · `harness meta-gate (check-arms)` · `drift-audit records` ·
`codebase-map coverage + freshness` · `kit/dogfood doc parity` · `bash tools/run-gates.sh` at the
push boundary.

## 8. Open questions

none — the forks below are RESOLVED and kept for the record.

**Fork A — does the filename carry the binding?** Today `2026-08-09-review-aBatchedTribunal-7.md`
spells a 7 that is not the id it serves.

- *Option 1* — filenames stay ordinals, documented as such.
- *Option 2* — rename every record so the filename names a spec.
- *Option 3* — rename only the ordinals that collide with a real different id in the same build.

RESOLVED (owner, 2026-08-17): option 2, against the recommendation on this spec, which argued for
option 1. The owner's original ask named filenames first and the resolution holds them to it.

Two consequences are absorbed rather than argued with. The blocker that killed this carrier in the
design pass is DESIGNED AROUND by §4's redefinition — the ordinal changes meaning, the grammar does
not change shape, so the closed family alternation never goes vacuous. The residual cost is real and
is now `TOOL-aTetheredRecord-7`: 103 referencing lines across 62 citing files at BASE — re-measured by the unit rather than carried forward, because this build added records of its own the same day — none of them
in an append-only area, so every one is legally repairable. The permanent rename discipline that
option 1 warned had no gate now HAS one — branch 4.

**Fork D — bound the unbound form by a count or a registry?** RESOLVED (owner, 2026-08-17): the
count, per §4's rejected alternative. A registry buys information already visible inline and costs
the six-file sweep a prior unit measured and rejected.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the adversarial design pass recorded under this build's
  `build/` folder.
- rev-2 · 2026-08-17 · folded the owner's fork resolutions. Fork A ratified RENAME-ALL against this
  spec's recommendation, adding branch 4, its arm, the ordinal redefinition in §4 that avoids the
  alternation blocker, and the rename itself as `TOOL-aTetheredRecord-7`. Fork D ratified the count.
- rev-3 · 2026-08-17 · folded the M4 audit, which returned BLOCKED with this unit holding one of the
  three blockers. **B2:** branch 4 had NO INPUT — the mode `TOOL-aTetheredRecord-2` shipped emits
  nothing for a conformant record, so S2b now amends it. **B3:** branch 4's projection is a whole id
  and LOWEST needed a stated total order; both are now in §4, along with the fact that the filename's
  kind is check 5's subfolder kind and never Fork E's relation kind. **H1** three→four throughout,
  **H2** the §3 non-goal had been left describing Fork A's losing option, **H4** the precondition was
  a restatement of the population and so could never fire. S5 states the arm floor as a literal, S9
  adds the version bump the engine change obliges, and §4 pins the four signature strings.

## 10. Reuse audit

Four seams, none new:

1. **`pop_guard`** — the precondition/population split that distinguishes a young tree from a
   mis-segmented selector. Reused verbatim; only a new precondition is added.
2. **Check 9's delegation shape** — the shell engine calling the Python module and reporting its
   findings. Copied structurally, so the check costs no new leg.
3. **Check 14's citation resolution** — free typo-checking on every id a binding names, as described
   in `TOOL-aTetheredRecord-2` §10. Branch 2 exists only for the residue check 14 cannot see.
4. **The shrink-only pin pattern** — a scalar in the repo conf plus a declared ratchet direction, the
   same shape as the four pins already in that file.

Recall terms: `build slug spec artifact filename header adversarial review closeout journal
bookkeeping convergence naming hygiene`.
