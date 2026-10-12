# Brief — aDistilledCharter: the micro-formats bind every final message

**Serves:** research PLAY-aDistilledCharter-6

## The prompt

> The new template is landed but 'microformats' appears to be a glaring weak point of it now - I'm seeing the sessions running with the new instructions to completely ignore that block and output no microformat updates predominantly. First of all, reopen the build to amend the template to instruct microformats as being NON-NEGOTIABLE. Neither in gov, nor in any in their adopters. The microformats are currently the only concise way to have a build overview status at a glance, without going through a ton of prose. It must NEVER be omitted. In addition, I remember another build working on mechanical enforcement of that rule - is it actually possible? Was it built before?

## The brief

### Goal
Reopen aDistilledCharter for one unit that makes the charter's micro-formats a section-1 rule binding every final message, in gov and in every adopter that renders the template.

### Items
1. The definition block and its rules move into section 1, with the definitions' bytes unchanged.
2. One-line rules state that the shapes are non-negotiable in every final message, and close the readings that let a session drop them.

### Acceptance
The render check passes with the definitions above section 2, the micro-format gate passes with the definitions byte-identical to BASE, and the section-1 text carries the new rules, each on one line.

### Gates
`playbook render wiring` · `micro-format definitions` · `template size <=48KiB` · `line length` · `playbook parity` · `kickoff-manifest ratchet` · `memory hygiene` · `recall floor` · `recall floor arms`

### Non-goals
No `Stop`-hook emission validator; that is asked separately. No change to a definition's bytes or to the micro-format gate. No adopter rollout. No version bump.

### Limitations
The template is a routed path, so every write needs this unit's route on the session card. Every rule stays one line under the renderer's grading. The kit versions are minted at the landing, never on the branch.

### Reuse
The renderer's one-line regions and the existing `<!-- microformats -->` fence carry the change; no new mechanism. The recall query returned PLAY-aFusedCharter-2 and TOOL-aFusedCharter-2, whose owner ruling of 2026-08-18 left the emission validator as a follow-up, and TOOL-aHonedRuleset-2, which kept it there.

## Drawn from the session

> It must NEVER be omitted.
— owner, 2026-10-11

## Owner confirmation

Asked: none — the owner ordered the change directly in the prompt above.
Answer: First of all, reopen the build to amend the template to instruct microformats as being NON-NEGOTIABLE.

## route
- build: aDistilledCharter
- unit: PLAY-aDistilledCharter-6 · spec memory/builds/aDistilledCharter/spec/2026-10-11-spec-PLAY-aDistilledCharter-6.md
- brief: memory/builds/aDistilledCharter/prompts/2026-10-11-prompt-PLAY-aDistilledCharter-6-brief.md
