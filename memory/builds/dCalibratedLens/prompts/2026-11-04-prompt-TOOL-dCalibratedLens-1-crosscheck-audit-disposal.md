**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-24

# Brief: the disposal of the cross-check folds' spec audit, every item folded

## The prompt

> go with (b) for row 9, rest with recommendations

— the owner, 2026-11-03. One recommendation was a spec-audit round over the cross-check fold text
before the build run. That round ran on 2026-11-04 and its record is
`memory/builds/dCalibratedLens/reviews/2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit.md`.

## The brief

### Goal

Fold every item of that review record into the specs it touches. The verdict is CLEAN WITH FIXES:
no blocker, no high, twelve medium (M1-M12) and nine low (L1-L9). Every item's fix amends spec text
and adds no document, gate, adopter, generated artifact, verb or write path outside its unit's own
Scope. Each is therefore LOCAL under BUILD-METHOD M4's nature rule, and folds at the disposal with a
rev bump and a revision-log line naming the record and the item. Nothing is promoted, and the chain
stops here: no blocker or high, nothing promoted.

### Items

Read the review record first. Each item quotes its finding, its consequence and the fix a skeptic
judged sound. Its appendix carries every finding with its `ref`. Apply the fix as the item states it.
Where an item offers options, take the one this brief names below. Where the brief names none, take
the one that conforms to the cited parent text with the smaller change.

Decisions this brief makes for the items that offer options:

- **M2 (cl14):** widen `compare_path` in this build. Record a new §8 item, PRIMITIVE GAP, with the
  item's three options, marked `RESOLVED (agent, 2026-11-04, delegated)` with the in-build widening.
  The reason is the owner's rule that no plan counts on a foreign build for functionality it can fold
  in. Its rung is the one the spec's other primitive gaps carry. Add `tools/loop/adapt.py` and the
  widening to F8's `grants:`, and fix §4 "Waits on".
- **M4 (cl9):** the widened `read_act_records` reads the window's rows in one batch, so the 60 s
  bound stands as sized. If the parent text gives the door no batch read, re-derive the bound for one
  `show` per act instead, and say so.
- **M7 (cl1):** run `--trigger` only for a review breakpoint, by the parent's own review names and
  the `placement` cause. Pass `--cause` from the line's `cause` field. Also state the outcome for a
  step outside `REVIEW_STAGES`.
- **M8 (cl1):** state that a `REVIEW_STAGES` member with no literal read raises a `RolesError` naming
  the stage, and add that case to the adopt-roles arm. Add no parity gate.
- **M9 (cl10):** take option (b), cl46's and cl47's two-case form, so the three specs fold the
  `leg_factory.py` presence one way.
- **M10 (cl1):** state in S5 how `--trigger` finds `handoff.py` (inline `resolve_kit_dir`) and what
  it prints with roles absent. Add no kit edge.
- **M11 (cl1):** parse the `^REVIEW_STAGES = ` line as text. Name each failure class with its
  message, and extend AC8.
- **L5 (cl9, cl7):** re-word to the `find --all` and `show` route the owner's wm32 F6 (b) pick
  names, in both specs.

Groups, one writer each. The spec your task block's `input:spec` names leads one group. Edit only
that group's specs:

- **Group D1, led by spec 1:** specs 1 and 24. Items M7, M8, M10, M11 and L9 on cl1, and L1 on
  cl24. cl1 is 48632 bytes. No gate caps a spec's size, but keep the fold tight.
- **Group D2, led by spec 3:** specs 3, 2, 5 and 19. Items:
  - M1 on cl3.
  - M5 on cl3 and cl2, one wording in both.
  - M6 on cl5 and cl19, naming the dTotalRecall BACKLOG row filed 2026-11-03 for the record-kind
    check, ask 108.
  - L4 on cl2.
- **Group D3, led by spec 16:** specs 16, 12 and 17. Items M3, M12 and L2 on cl16, and L2's
  alignment on cl12 and cl17.
- **Group D4, led by spec 14:** specs 14, 10, 15 and 8. Items:
  - M2 and L8 on cl14;
  - M9 and L3 on cl10;
  - L6 on cl15;
  - L7 on cl8.
- **Group D5, led by spec 9:** specs 9 and 7. Items M4 and L5 on cl9, and L5 on cl7.

Each revision:

- bumps the **Status:** line by one rev, with date `2026-11-04`, leaving every other field;
- adds one §9 line in the spec's existing form: `- rev-<n> · 2026-11-04 · <sections> · the
  cross-check folds' spec audit disposed, <what moved>, by the brief
  prompts/2026-11-04-prompt-TOOL-dCalibratedLens-1-crosscheck-audit-disposal.md (review
  2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit, items <ids>)`;
- keeps any line it moves in the parent's spelling, quoting the parent's surface names exactly;
- writes no list item or table cell that opens with another build's unit id followed by a separator,
  because hygiene check 13 reads that shape as defining the id. Lead with a word, or with the short
  alias.

Return, in this shape and nothing else:

1. One bullet per item you were given: the item id and spec, `folded`, `refused` or `parked`, the
   sections it moved, and for a refused or parked item the line that decides it.
2. One line per spec edited: its new rev and its byte count.
3. The hygiene run's command and what it printed.
4. Parent text that looks wrong, one line each with `file:line`.

### Acceptance

- Each edited spec's **Status:** line carries its new rev, and §9 holds the new line.
- For each item you fold, the text the item quotes as the defect no longer stands: a `grep -n` of the
  quoted phrase, or a re-read of the section where the phrase was a paraphrase.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged` runs over a copy of the index with only
  your group's specs staged into it through `GIT_INDEX_FILE`, and names nothing of your specs. Delete
  the copy after. Findings that only a `gen_build_index.py --write` render cures belong to the main
  loop: name them and leave them.

### Gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### Non-goals

- No file outside your group's specs. No commit, no stage into the real index, no deviation record,
  no BACKLOG row: the main loop writes those.
- No file of any parent or ancestor build.
- No item outside your group, no new unit, and no change beyond what the item's fix states.
- No owner-resolved §8 mark changed.

### Reuse

The review record is the map of what to change. The precedent is this build's own re-ground briefs,
`memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md`
and `...-1-ancestors-reground.md`.
