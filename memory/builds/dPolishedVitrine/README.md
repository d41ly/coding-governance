---
slug: dPolishedVitrine
node: d
opened: 2026-09-12
streams: tooling+deployer
roster: TOOL+DEPL
authorized-by: prompt
ids: DEPL-dPolishedVitrine-1 DEPL-dPolishedVitrine-2 DEPL-dPolishedVitrine-3 TOOL-dPolishedVitrine-1 TOOL-dPolishedVitrine-2 TOOL-dPolishedVitrine-3 TOOL-dPolishedVitrine-4 TOOL-dPolishedVitrine-5 TOOL-dPolishedVitrine-6 TOOL-dPolishedVitrine-7 TOOL-dPolishedVitrine-8 TOOL-dPolishedVitrine-9 TOOL-dPolishedVitrine-10 TOOL-dPolishedVitrine-11 TOOL-dPolishedVitrine-12
---

# dPolishedVitrine — the build harness is rendered at install, so its paths name the adopter's tree

## The problem this build exists to solve

`unattended-build.js` shipped as an engine file, and apply writes those verbatim. Its four install
paths name the driver, the bug-class checklist, the review sub-workflow and the child it hands out,
and every one reads `tools/…`. Both measured adopters install at `scripts`, so in their trees the
AUDIT stage cannot reach its callee. They also install the memory-tree kit flat, so a fix that
derived only the prefix would still name a checklist neither tree has. The unattended Skill spells
the same checklist path, and it breaks the same way.

## Expected improvements

- The harness names files the installing tree actually has, at any prefix and any memory-tree layout.
- One kit release fixes both adopters, with no hand-repath and no untagged delta.
- A missing checklist script is a refusal at render time, never a command that runs nothing.

## Detriments if this is not built

- Every adopter at a non-`tools` prefix keeps a harness whose AUDIT stage cannot run.
- Each adopter keeps repathing by hand, and re-pulling rolls those hand-edits back.

## Build-level rules

- **Derive, never guess.** The checklist's directory is probed from the tracked tree. A path nobody
  has proved exists is a refusal that names the override.
- **Every new arm is observed red before it lands.** HEAD's verbatim harness is the staged break.
- **Consumers are not touched here.** Core and NicoCares re-pull this release later, and their own
  records carry that.

## Parked decisions

- **The lander must take unattended to 1.20.** `main` gained its own unattended 1.19 at `09a22d2b`
  while this branch was open, and this branch bumps 1.18 to 1.19 for other content. The two merge
  cleanly byte for byte, so two different kits would ship as 1.19 and the version gate would pass.
- **The lexicon pin rose 984 -> 986** for the template's two helper names, which `agent-cap.js`
  recognises by name. The agent resolved it under the brief; `TOOL-aWeldedTribunal-12` keeps the
  underlying tension, every conforming harness costing two offenders, for the owner.
- **`update` still keeps a schema-3 receipt's `engine` role** when a kit makes that destination
  `rendered`. Round 1 repaired it for this release by a fixture-verified consumer migration.
  `DEPL-dPolishedVitrine-1` holds the govkit move, whose blast radius is the owner's to rule on.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dPolishedVitrine-1` | 2 | render the harness and the Skill's checklist line at install, with the memory-tree directory probed |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node d · opened 2026-09-12 · streams tooling+deployer
ids DEPL-dPolishedVitrine-1 DEPL-dPolishedVitrine-2 DEPL-dPolishedVitrine-3 TOOL-dPolishedVitrine-1 TOOL-dPolishedVitrine-2 TOOL-dPolishedVitrine-3 TOOL-dPolishedVitrine-4 TOOL-dPolishedVitrine-5 TOOL-dPolishedVitrine-6 TOOL-dPolishedVitrine-7 TOOL-dPolishedVitrine-8 TOOL-dPolishedVitrine-9
ids TOOL-dPolishedVitrine-10 TOOL-dPolishedVitrine-11 TOOL-dPolishedVitrine-12

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dPolishedVitrine-1 — the build harness is rendered at install, and its paths are derived](spec/2026-09-12-spec-TOOL-dPolishedVitrine-1.md) | — | 2 | INPROGRESS | rev-5 | 2026-09-12 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dPolishedVitrine-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
