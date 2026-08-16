# TOOL-aTetheredRecord-4 — check 21: the binding becomes the merge bar

**Status:** SPECCED · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Turn the binding from a convention into a gate. Three `fail` branches in the tracked shell engine —
the only place the harness meta-gate can count them — enforce that every record carries a conformant
line, that every id it names resolves to a SPEC, and that the unbound escape stays bounded.

## 2. Scope (IN)

- **S1** — A new precondition beside the existing four in `tools/memory-tree/check-memory-hygiene.sh`:
  tracked files under a build's non-spec subfolders. It is deliberately coarser than the check's own
  population and reads zero on a freshly scaffolded tree.
- **S2** — The check-21 block, placed after check 12. Its population is any tracked file at any depth
  under a build's `build/`, `prompts/` or `reviews/` folder, with NO extension filter. It carries the
  population guard, skips under the staged-diff mode, and delegates the parse to the module from
  `TOOL-aTetheredRecord-2` in the shape check 9 already uses.
- **S3** — Three `fail 21` branches, each with a distinctive longest literal run so the sibling test
  can assert it verbatim.
- **S4** — `RECORD_UNBOUND_PIN` in `.memory-tree.conf`, MEASURED against this corpus by
  `TOOL-aTetheredRecord-3`, with its measurement note; blank in the shipped example conf; and a
  ratchet row in `tools/drift-audit/drift_signals.py` declaring that raising it is the weakening
  direction.
- **S5** — `ARMS_FLOORS` for the hygiene engine moves from its current pair to three more branches,
  all armed.
- **S6** — Fixtures and three arms in `tools/memory-tree/check-memory-hygiene.test.sh`, each asserted
  inside check 21's own output block rather than against a global hit.
- **S7** — Rename the leg and every carrier of its check count. Measured: eight spellings across
  seven files, of which six are authored and two re-render.
- **S8** — Correct `memory/project/unarmed-branches.txt`'s header, which declares the file empty
  while carrying a row, and the same claim in `memory/HYGIENE.md` and its shipped template.

## 3. Non-goals (OUT)

- **No filename change.** Fork A in §8 is the owner's, and this unit ships the recommended option:
  one sentence stating that the ordinal is an ordinal.
- **No render change** — that is `TOOL-aTetheredRecord-5`.
- **No relation kind.** The check reads which ids a record names, never what it did to them.
- **No widening of the harness meta-gate beyond shell.** Recommended separately; this unit keeps its
  branches in the shell precisely so it does not depend on that change.
- **No new gate leg.** Check 21 rides the leg that already exists, which is why this unit does not
  pay the codebase-map coverage assert or the drift-audit leg-count signal.

## 4. Design

### The three branches, and why the second is not redundant

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

### The literal messages

`check-arms.py:104-113` takes a branch's signature as the LONGEST literal run between interpolations,
stripped of trailing punctuation. Each message below therefore carries one long, distinctive run, and
the interpolated list follows it:

- `records under build/, prompts/ or reviews/ whose head carries no conformant Serves line:`
- `Serves or Commissions lines naming an id that no spec in this tree defines:`
- `records carrying the unbound Serves form outnumber RECORD_UNBOUND_PIN — bind them, or move the pin recording the old and new values beside it:`

None contains a positional parameter, which `check-arms.py` would read as literal text inside the
signature and no assertion could ever emit.

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
  three more branches than today and all of them armed, and `ARMS_FLOORS` matches.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, it is green, and each of
  the three arms asserts inside check 21's own output block rather than against a global hit.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs against a scratch tree holding
  one build, one spec and zero records, it exits 0 and prints no check-21 line in the missing-
  population report.
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

**Fork A — does the filename carry the binding?** The owner's ask named filenames first, and today
`2026-08-09-review-aBatchedTribunal-7.md` keeps spelling a 7 that is not the id it serves.

- *Option 1 (RECOMMENDED)* — filenames stay ordinals, and one sentence in the hygiene doc says so
  plainly. Cost: the ordinal keeps disagreeing until a reader opens the file or reads the build
  README table.
- *Option 2* — rename all 76. Delivers the literal ask. Costs 103 cross-referring lines in 62 files,
  eight tracked spellings of the name grammar, collapse of the closed family alternation for the
  whole non-spec population, and a permanent rename discipline no gate enforces.
- *Option 3 (second choice)* — a narrow follow-up renaming ONLY the ordinals that collide with a real
  different id in the same build. Most of the glanceability, a fraction of the blast radius. This is
  the better backlog row if option 1 leaves the owner unsatisfied.

**Fork D — bound the unbound form by a count or a registry?** RECOMMENDED: the count, per §4's
rejected alternative. A registry buys information already visible inline.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the adversarial design pass recorded under this build's
  `build/` folder.

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
