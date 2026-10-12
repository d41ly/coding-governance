# PLAY-aDistilledCharter-6 — the micro-formats are a section-1 rule that binds every final message

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-1 · base 9b743831 · streams playbook · order 18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-PLAY-aDistilledCharter-6-landing.md](../build/2026-10-12-build-PLAY-aDistilledCharter-6-landing.md) | journal | — |
| [2026-10-11-prompt-PLAY-aDistilledCharter-6-brief.md](../prompts/2026-10-11-prompt-PLAY-aDistilledCharter-6-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Sessions on the v4 charter leave the micro-formats out of most final messages, and those shapes are
the only at-a-glance status a reader gets. The v4 render puts them at the foot of the generated
block as a reference list, where a reader takes them for data rather than a rule. This unit moves
them into section 1 and states, in one line each, that every final message carries them.

## 2. Scope (IN)

- **S1** — The definition block and its rules move from the foot of section 3 into section 1, under
  a `### Micro-formats` heading placed before `## 2. This repository`. The eleven definitions keep
  their bytes. Observed by AC1 and AC2.
- **S2** — The rules state that the shapes are NON-NEGOTIABLE in every final message: `[formats]`
  says so in the practices, `[never-omit]` says a short answer still ends with the state block and
  that repeating it is not saying a thing twice, `[events]` maps each event to its shape, and
  `[pair]` binds `BUILD` and `SPEC` to every final message of a build in progress. Observed by AC3.

## 3. Non-goals (OUT)

- A `Stop`-hook emission validator. Whether a final message carried its shapes is a hook's question,
  and building one is the owner's call, asked separately.
- Any change to a definition's bytes, its grammar, or `tools/check-microformats.sh`.
- Rolling the change out to adopters. It reaches each one as a `govkit update`.
- A version bump. The template marker is minted at the landing.

### Edges

none

## 4. Design

Section 1 gains a `### Micro-formats` subsection after its practices region: the `<!-- microformats -->`
fence unchanged, then a one-line region holding `[never-omit]`, `[events]`, `[pair]`, `r1`, `grammar`,
`fields`, `gates-line`, `state` and `links`. The old `## Micro-formats` heading at the foot of section 3
goes away with the block. `[formats]` stops pointing at section 3 and states the rule itself.

`[never-omit]` answers the reading that `[signal]`'s "nothing said twice" licenses dropping a
repeated state block. `[events]` answers the reading that a shape is owed only when a reader asks.
Every rule stays one line, under the renderer's one-line grading.

### Files touched (estimate)

- `coding-governance-agents.template.md`
- `AGENTS.md`
- `tools/template-size-highwater.txt`
- `memory/guides/SESSION-KICKOFF.md`

## 5. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --target . --check` runs, it reports the
  region matches a fresh render, and in `AGENTS.md` the `BUILD — ` definition line sits above the
  `## 2. This repository` heading.
  Red when: the block is rendered below section 2, or the region drifts from the template.
- **AC2** — When `bash tools/check-microformats.sh` runs, it exits 0, and the lines between the
  `<!-- microformats -->` fence pair are byte-identical to BASE `9b743831`'s.
  Red when: a definition byte changes, or the fence pair is lost.
- **AC3** — When the template's section-1 text is read, it carries `[never-omit]`, `[events]` and a
  `[pair]` line binding `every final message`, and `[formats]` names no section number.
  Red when: any of the four is missing, or a rule spans two lines.

## 6. Gates

`playbook render wiring` · `micro-format definitions` · `template size <=48KiB` · `line length` · `playbook parity` · `kickoff-manifest ratchet` · `memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-11 · initial draft, from the owner's report that sessions on v4 omit the micro-formats.
