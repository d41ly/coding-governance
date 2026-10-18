**Serves:** research TOOL-aScoutedSeam-3

# The reuse workflow design set — the measured best settings, and how a session adopts them

This document holds the reuse workflow at the settings that measured best, and the method that measured
them. Another session can follow it to run a reuse orientation and a diff check, or to tune its own
agent prompts the same way. It is self-contained. Each instrument it names is committed beside it in
this folder, and the measured basis is
`2026-10-18-build-TOOL-aScoutedSeam-3-1-system-and-held-out.md`.

The product units that build this workflow into the kits are still SPECCED, not built:
TOOL-aScoutedSeam-1 (the orientation scout), TOOL-aScoutedSeam-3 (diff mode), KICK-aScoutedSeam-1
(kickoff wiring) and DEPL-aScoutedSeam-1 (adopters). Until they land, run the instruments here by hand,
as this build did.

## 1. The measured basis

These are blind-judged figures: a `gov-skeptic` saw every arm under a rotated label and decided whether
each covered the case's primary seam. Each set ran once, with one judge per case.

| arm | tuning, 23 diff cases | held-out, 12 untuned cases | both |
|---|---|---|---|
| orientation scout alone (M1c) | 15 | 8 | 23 of 35 |
| diff check T1, no card | 13 | — | — |
| diff check T1 + the orientation card | 20 | 11 | 31 of 35 |
| diff check T2 + the orientation card | 20 | 11 | 31 of 35 |
| **system: orientation, then T1 with its card** | **21** | **12** | **33 of 35 (94%)** |

Read the table this way:
- **The diff check carries recall.** T1, the enumerated per-unit diff check, is the strongest single
  arm on both sets.
- **The orientation carries the early, cheap catch.** It runs before a line is written, and on the
  held-out set it found the one case T1 missed. Its wrong-seam count is inflated, because it is judged
  against a diff it never saw.
- **The card is the biggest lever.** Handing T1 the orientation's MUST seams as wiring rows took it from
  13 to 20 of 23, with nothing else changed. The stages feed each other, so run them in order.
- **The union is the system.** Orientation plus T1 is the design, and it held on the untuned set: 12 of
  12. The two cases no arm solved are visual conventions in a package over a host core: a DSL `media`
  field kind, and a Section width with a flat eyebrow.
- **`low` effort does not hold the gain.** T1 at `low` covered 8 of 23 where `medium` covered 14, and
  bound the most misleading seams (`2026-10-18-build-TOOL-aScoutedSeam-1-12-judge-and-low.md`).

## 2. The workflow

```
request ──► [1] orientation scout ──► ## reuse card ──► spec ──► build ──► diff
                                          │                                 │
                                          └──────────► [2] diff check ◄─────┘
                                                        (T1, card MUSTs as wiring rows)
                                                        [2b] T2 pass, optional, unioned
```

### Stage 1 — the orientation scout (M1c)

- **When.** At kickoff, before the spec writer is dispatched.
- **Who.** One `gov-reuse-scout` at `medium`, read-only, inside the tree as it stands when the request
  arrives.
- **Input.** The request text, the tree path (plus the host core tree for a package), and a generated
  house index of the tree.
- **The prompt.** `render_orient_question` in `2026-10-18-build-TOOL-aScoutedSeam-1-13-system.py`,
  built from `ORIENT_STEPS`. In order, it asks the scout to:
  1. Read the house index.
  2. Orient on the charter and the codebase map.
  3. Frame 3 to 10 needs, including implied ones, and sketch 6 to 15 concrete components.
  4. Resolve every named anchor, and the canonical implementation of the same kind.
  5. Run a convention census across five or more siblings.
  6. Search each sketched component by concept across all file types.
  7. Read the design system when any need is visual.
  8. Read the records.
  9. Self-refute each candidate.
- **The output.** One JSON block with needs, sketch, census, at most 12 seams (each `MUST` or `SHOULD`
  with path, symbol, need, how, evidence and not), at most 5 constraints, and the unmet needs.
- **The card.** `render_card` turns the MUST and SHOULD seams into the `## reuse` lines of the kickoff
  card, which the spec writer, builder and reviewers read by heading. TOOL-aScoutedSeam-1 caps MUST at
  five. A MUST must name the existing implementation that new code would duplicate.

### Stage 2 — the diff check (T1, with the card as wiring)

- **When.** Once the build has a diff, before the closing review and the landing.
- **Who.** One `gov-reuse-scout` at `medium`, read-only, in the tree at the diff's parent.
- **The lister.** `extract_units` in `2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2.py` lists every unit
  the diff adds: definitions, constants, shell functions, CSS custom properties and rules, schema
  fields, named JSON nodes, and any hunk of 4 or more added lines that holds no named unit. It skips
  tests, docs, memory, lock files and images. It lists at most 60 units, then adds "... and N more".
- **The prompt.** `render_question` in the same file, plus `WIRING` from `-1-13-system.py` when a card
  exists. It is the enumerated-coverage recipe of
  `2026-10-18-build-TOOL-aScoutedSeam-1-11-prompt-method.md`:
  - **One row per listed unit, in order.** Each row carries `nearest`, an existing `path::symbol` or
    `none` with what was searched.
  - **A closed verdict set:** `duplicate`, `should-extend`, `new` or `not-a-unit`.
  - **Added rows,** marked `added`, for what the lister cannot see: repeated literals, hardcoded design
    values beside a token, renamed copies, and rebuilt JSON nodes.
  - **An explicit no-stop line.**
  - **One wiring row per card MUST:** `used`, `bypassed` or `not-applicable`. A bypassed MUST is also
    reported as a duplicate.
- **The output.** The rows, the seams derived from them (MUST for `duplicate`, SHOULD for
  `should-extend`), the wiring rows, and `duplicates-found` or `clean`.

### Stage 2b — the T2 pass (optional)

T2 is T1 plus a house index, an extended lister and six general rules (`T2_RULES`, `extract_units_t2`):
- **The extended lister** adds a spec diff's scope items, and every CSS literal equal to a token's value.
- **The six rules:**
  - a value-type census for every added field;
  - a read of same-module siblings;
  - reachability, so a seam in another kit is `should-extend` through the sanctioned sharing route;
  - dossier and generator binding;
  - distrust of the diff's own comments;
  - spec items judged as code.

T2 tied T1 on coverage (31 of 35), bound slightly more misleading seams (28 against 24), and missed
different cases. Run T2 as a second, independent pass when a miss is expensive, and union its MUSTs with T1's.
Do not replace T1 with it.

## 3. The settings

| setting | value | basis |
|---|---|---|
| effort, both stages | `medium` | `low` loses 6 of 14 primaries; `extra` bought less than the prompt change |
| model | the session's default Opus | every arm ran on `claude-opus-5-5` |
| orientation seams | at most 12, best first | the M1c contract |
| orientation MUSTs | at most 5 | TOOL-aScoutedSeam-1 precision rule |
| lister cap | 60 units | the method record, item 8 |
| unnamed hunk floor | 4 added lines | `HUNK_MIN_ADDED` |
| concurrent agents | at most 5 | the charter's `[bound]` |
| judge | one `gov-skeptic` per case, labels rotated | `-1-10-judge-task.md` |

## 4. Known limits

- **The lister skips tests.** It still found the three held-out test-scaffolding reinventions through
  the open search and the added rows, but no listed unit points at them. A repository whose
  reinventions are mostly in test code should drop `tests?/` from `SKIP_PATH` and re-measure.
- **The lister can return nothing.** On a probe plus spec diff it listed 0 units, and the scouts found
  the primary anyway, from the hunks. The prompt says to enumerate from the hunks when the list is
  empty.
- **Precision costs volume.** T1 binds about 8% misleading seams. A MUST is a reviewer's lead, not a
  verdict. The builder reads the seam, and a reviewer rejects a MUST that names no existing duplicate.
- **One run per arm.** Every figure here is a single run. A difference of one or two cases is noise.

## 5. How to adopt it in another session

1. **Orient.** Render the M1c question for your request (`-1-13-system.py orient-q`, or by hand from
   `ORIENT_STEPS`). Spawn one `gov-reuse-scout` at `medium` with it. Write its MUST and SHOULD seams
   as the card's `## reuse` (`card`).
2. **Spec and build** with the card in the spec writer's and builder's inputs.
3. **Diff check.** List the units (`d1v2.py extract_units`, or `units-t2`). Render T1 with the card
   (`diff-q <root> <out> t1 <results> <orient-arm>`), and spawn one `gov-reuse-scout` at `medium`.
4. **Act on it.** Every `duplicate` row and every bypassed MUST is a fix before landing, or a stated
   reason in the spec. A `should-extend` row is a strong default.
5. **Optional second pass.** Render T2 the same way, and union its findings with T1's.

## 6. How to measure and adjust your own process

The method that produced these numbers transfers to any agent question:
1. **Mine cases with objective evidence.** Each case needs a reinventing commit, proof of the
   duplication (a later dedupe commit, a review finding, or a verified near-copy), and ground-truth
   seams verified at the parent. Phrase the request as it was before the spec, without naming the seam.
   See `-1-3-cases.json` and `-1-13-held-out-cases.json`.
2. **Freeze a held-out set before tuning, and never read it to change a prompt.** Write every prompt
   for the general case. A held-out figure far below the tuning figure means the prompt overfit.
3. **Change one variable per arm.** Effort, prompt and lister are separate arms. An arm must prove it
   ran: count parsed replies before reading a score.
4. **Enumerate outside the model.** When the answer is "every X with property P", hand the agent a
   deterministic list of X and demand one closed-vocabulary row per X (`-1-11-prompt-method.md`).
5. **Judge blind.** One judge per case sees every arm under a rotated label, with the rubric in
   `-1-10-judge-task.md`. Read primary coverage first, then the wrong seams.
6. **Read the union.** Arms that miss different cases are complementary stages, not competitors.
