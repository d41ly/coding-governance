---
slug: aLoosenedCeiling
node: a
opened: 2026-08-18
streams: tooling
roster: TOOL
ids: TOOL-aLoosenedCeiling-1 TOOL-aLoosenedCeiling-2 TOOL-aLoosenedCeiling-3 TOOL-aLoosenedCeiling-4
---

# aLoosenedCeiling — the read-path budget's last hardcoded numbers become adopter declarations

Node `a` · opened 2026-08-18 · streams tooling.

The read-path ceiling is already a per-adopter declaration: `READ_PATH_CEILING` is a
`.memory-tree.conf` key and blanking it turns check 16 off. What is NOT adjustable is everything
that PRODUCES a ceiling and everything check 16 leans on to decide a member is watched:

| number | where it is hardcoded today | what it governs |
|---|---|---|
| 20480 B headroom | `corpus_ids.py` `do_measure` | the ceiling `--measure` tells every adopter to write |
| 20480 B / 250 lines | `check-memory-hygiene.sh` check 6 awk | a row document's cap |
| 61440 B / 750 lines | same awk | a guide's cap — and a guide is the read path's biggest class |
| 25600 B / no line cap | same awk | a build README's cap |

An adopter can therefore raise the aggregate budget and still be unable to let a single guide grow,
because the per-member cap that check 16 rule 3 cross-references is a constant in someone else's
repo. This build makes all four adjustable, raises the shipped headroom default, and re-derives the
two live ceilings that are at the wall.

## Why now — both live ceilings are one edit from red

| repo | read path | ceiling | headroom left |
|---|---|---|---|
| coding-governance | 86394 B over 6 files | 86476 | **82 B** |
| NicoCares (`incms/main/vendor/nicocares-package`) | 109998 B over 7 files | 110000 | **2 B** |

## Units

| id | mechanism | carrier |
|---|---|---|
| `TOOL-aLoosenedCeiling-1` | `READ_PATH_HEADROOM`, and the shipped default rises 20480 → 25600 | `tools/memory-tree/corpus_ids.py` |
| `TOOL-aLoosenedCeiling-2` | the six per-class cap keys check 6 reads | `tools/memory-tree/check-memory-hygiene.sh` |
| `TOOL-aLoosenedCeiling-3` | this repo's own ceiling, re-derived at the new headroom | `.memory-tree.conf` |
| `TOOL-aLoosenedCeiling-4` | the NicoCares adopter's ceiling, 110000 to 241070, from its own measured burn | a separate repo |

Units 1 and 2 are independent mechanisms in two different languages, and are Tier-2 because each
changes a kit's contract. Units 3 and 4 are Tier-1: each moves one declared value and its
justification. Unit 3 depends on unit 1, in that its number is what the new default produces. Unit
4 depends on nothing here.

## What the pre-build survey changed

Four probes ran before any spec was reviewed — over the doc carriers, the gate legs, the two test
harnesses, and the adopter repo. Three findings changed a spec rather than confirming one.

| finding | where it landed |
|---|---|
| The Python loader indexes its conf dict directly, so a key absent from the defaults dict is a crash and not a missing setting | unit 1, S1 |
| `do_measure` has no test arm at all today — the constant this build replaces has never been exercised | unit 1, Inventory: S4 is first coverage, not an extension |
| Check 6's failure message is itself an armed signature; rewording it silently disarms the meta-gate | unit 2, S9 |
| No arm exists anywhere for the build-README cap tier, already filed as a medium finding by a prior review | unit 2, Inventory: the knob would otherwise ship over the same hole |
| The adopter's rotation reserve is SPENT — 646 B, not the 16403 B its own conf comment still advertises | unit 4, and it is what makes the raise the documented last resort rather than the first |
| The adopter's kit is seventeen releases behind and its `do_measure` still carries the literal, so declaring the new headroom key there would be inert | unit 4, non-goal: the key is deliberately NOT set there |
| A citation gate in the adopter repo holds a governing doc to the conf's current value | unit 4, S3: the doc line moves in the same commit or CI reds |

The survey also confirmed, by measurement rather than by assumption, that parameterizing check 6's
awk adds no branch to the harness meta-gate's population, and that every scratch conf in the hygiene
harness declares none of the new keys — so the existing arms keep their verdicts.

<!-- gen:build-index -->
**Build status:** OPEN · 4 unit(s) · node a · opened 2026-08-18 · streams tooling
ids TOOL-aLoosenedCeiling-1 TOOL-aLoosenedCeiling-2 TOOL-aLoosenedCeiling-3 TOOL-aLoosenedCeiling-4

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aLoosenedCeiling-1 — the read-path headroom becomes a declaration, and its default rises](spec/2026-08-18-spec-TOOL-aLoosenedCeiling-1.md) | OPEN | rev-2 | 2026-08-18 |
| [TOOL-aLoosenedCeiling-2 — check 6's per-class caps become adopter declarations](spec/2026-08-18-spec-TOOL-aLoosenedCeiling-2.md) | OPEN | rev-2 | 2026-08-18 |
| [TOOL-aLoosenedCeiling-3 — this repo's read-path ceiling, re-derived at the new headroom](spec/2026-08-18-spec-TOOL-aLoosenedCeiling-3.md) | OPEN | rev-1 | 2026-08-18 |
| [TOOL-aLoosenedCeiling-4 — the NicoCares adopter's read-path ceiling, raised against its measured growth](spec/2026-08-18-spec-TOOL-aLoosenedCeiling-4.md) | OPEN | rev-1 | 2026-08-18 |

Records live under `spec/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-18-spec-TOOL-aLoosenedCeiling-1.md](spec/2026-08-18-spec-TOOL-aLoosenedCeiling-1.md)
  - [2026-08-18-spec-TOOL-aLoosenedCeiling-2.md](spec/2026-08-18-spec-TOOL-aLoosenedCeiling-2.md)
  - [2026-08-18-spec-TOOL-aLoosenedCeiling-3.md](spec/2026-08-18-spec-TOOL-aLoosenedCeiling-3.md)
  - [2026-08-18-spec-TOOL-aLoosenedCeiling-4.md](spec/2026-08-18-spec-TOOL-aLoosenedCeiling-4.md)
<!-- /gen:build-docs -->
