**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46

# Brief: dCalibratedLens's specs re-grounded against its parents' specs

## The prompt

> If there are mismatches, write a re-ground brief in `prompts/`. `gov-spec-writer` agents fold it,
> with rev bumps, §9 lines and spec-revised deviation records. […] Text that is wrong in a PARENT
> spec is reported, never edited.

— the dClosedLoop session's hand-off to this session, 2026-11-03, relaying the owner's ask for a full
cross-read of dCalibratedLens against its parents.

## The brief

### Goal

Revise the dCalibratedLens specs your group names so that every MISMATCH row of the cross-check
record says what the parents' DEFERRED specs say on origin/main at `66c5b8dbf`. Each spec keeps its own
design. Only what a parent's text contradicts changes, by the smallest change that agrees with the
parent.

### Items

Read the cross-check record first:
`memory/builds/dCalibratedLens/build/2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck.md`.
Its summary table numbers every row. Section 2 of each group's return, in
`memory/builds/dCalibratedLens/build/2026-11-03-build-TOOL-dCalibratedLens-1-crosscheck-returns.md`,
quotes both sides of each MISMATCH and states its `Change:`. Re-read both sides before you edit. If
the parent's text does not bear a row out, do not edit it. Return it as refused, with the line that
refutes it.

Where the return offers two routes, take the one that conforms to the parent text with the smaller
change. Where both conform, take the first.

A §8 mark reading `RESOLVED (agent, <date>, delegated)` may be re-picked or re-worded when the
parent's text forces it. The new mark reads `RESOLVED (agent, 2026-11-03, delegated)`, keeps its rung
and its `widens:` and `relaxes:` values on one line, and is named in §9. A mark resolved by the
owner is never changed. A row that would need one changed, or a new fork, is returned as parked,
with its options, and is not edited.

Groups, one writer each. The spec your task block's `input:spec` names leads one group. Edit only
that group's specs:

- **Group W1, led by spec 1:** specs 1, 13, 24 and 30.
  - cl1 rows 4, 6, 9, 10, 13, 16 and 17:
    - eight literals, with fh18 and fh23 among the preconditions;
    - file-order slots;
    - `--stage` admits only `REVIEW_STAGES` members;
    - `render_lenses.py --markers` (fh23 S35);
    - only rp6 AC1's arm flips;
    - id3 AC7's literal key reads;
    - AC3 through `check-verifier-fanout.js --hook` (fh16).
  - cl13 rows 115 and 116: `LENS_SLOTS` in `check-verifier-fanout.js` (fh23 S42); a tag addresses
    every row of its key, and AC1 and AC7 count distinct keys.
  - cl24 row 156: the red twin through `check-verifier-fanout.js --hook` (fh16 S2, S5, AC2).
  - cl30 row 162: re-word its rp6 sentence to match cl1's row-13 fold. If the fold leaves cl30 true,
    leave it and say so.
- **Group W2, led by spec 10:** specs 10, 23 and 36.
  - cl10 rows 91, 92, 94, 95, 96, 97, 98 and 102:
    - arms in `replay_scorer.run_selftest` under `ARMS_DECLARED` (fh12 S8, F3);
    - the `case_evidence` hook (fh14 S2);
    - cases from a finding scoped to tagged refs, or an address check of their own;
    - the known set's `n`, with `0/59` made consistent;
    - which of fh25's two runs seeds the case;
    - `**Replayed:**` as fh32 S14's orchestrating commit;
    - the README replay procedure (fh23 S17, fh32 S17-S18);
    - the leg as one whole `[[exempt_leg]]` row through `leg_factory.py` (tc7 S4, wb11).
  - cl23 rows 152, 153 and 154, and cl36 rows 164 and 165: the same score, sha and arm corrections.
    The edits since the replay count the parents' template edits after fh25 (fh27, fh30, fh35,
    fh32, fh37, fh40).
- **Group W3, led by spec 3:** specs 3, 8 and 11.
  - cl3 row 41: adopt tc48 S28's re-run journal, or say why a second `seen` receipt is harmless. Stop
    calling the walk tc1 S2's.
  - cl3 row 46: land the record as tc49 S4 and tc71 do, or cap it at `INTAKE_CAP_BYTES`, and add the
    criterion over 64 KiB. cl3 is 45186 bytes, so keep the fold short.
  - cl8 row 76: the view is the slices plus the `map` and `code` slot bodies, or every slot's paths
    with §5's over-read risk widened.
  - cl8 row 80: fh12 S2's move of the appendix parser into `replay_scorer.py`.
  - cl11 row 107: all four of rp13 S2's refusals, or rp13's own check.
- **Group W4, led by spec 9:** specs 9 and 16.
  - Row 83: wm53's `read_act_records` widened to read `Act`, naming wm53 S4. cl16's map follows it.
  - Row 84: id 51's `git ls-files` route dropped for `read_act_records` over `find --all`, the
    owner's wm32 F6 (b).
  - Row 87: F4 re-worded to wm12 S8's position-item fallback.
  - cl16 row 136: wm6 S12's act classes in `NOT_TRENDED`, or the reason each is trended.
  - cl16 row 142: `cycle` read from wm50's cycle owner item, since wm50 §3 writes no journal line.
- **Group W5, led by spec 2:** specs 2, 4, 15, 41 and 46.
  - cl2 row 25: `--key` only with `--dry-run`, and `refused: no key` otherwise (tc1 S2, AC3).
  - cl2 row 26: name cl3 §8 F2's ask as the only source of the monthly and `n<k>` forms.
  - cl4 row 59: wm53 S4.
  - cl15 row 131: extend tc9 S1's `reads` and `measure_path_reads`, or rename the verb with a reason.
    Drop "no seam counts a document's reads".
  - cl41 row 167 and cl46 row 168: name fh17 S5. The guard keeps `{prefix}/unattended/unattended.sh`
    beside the new entries, and is re-read at the pass and never rewritten from the base list.

Each revision:

- bumps the **Status:** line by one rev, with date `2026-11-03`, leaving every other field;
- adds one §9 line in the spec's existing form: `- rev-<n> · 2026-11-03 · <sections> · re-grounded
  against the parents' specs, <what moved>, by the brief
  prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md (cross-check rows <ids>)`;
- keeps any line it moves in the parent's spelling, quoting the parent's surface names exactly.

Return, in this shape and nothing else:

1. One bullet per row you were given: the row id and spec, `folded`, `refused` or `parked`, the sections
   it moved, and for a refused or parked row the line that decides it.
2. One line per spec edited: its new rev and its byte count.
3. The hygiene run's command and what it printed.
4. Parent text that looks wrong, one line each with `file:line`.

### Acceptance

- `wc -c <spec>` is under 49152 for every spec you edit.
- Each edited spec's **Status:** line carries its new rev, and §9 holds the new line.
- For each row you fold, the probe the return quotes from the child side no longer prints the
  contradicted text: a `grep -n` of the quoted phrase.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged` runs over a copy of the index with only
  your group's specs staged into it through `GIT_INDEX_FILE`, and names nothing of your specs. Delete
  the copy after. Findings that only a `gen_build_index.py --write` render cures belong to the main
  loop: name them and leave them.

### Gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### Non-goals

- No file outside your group's specs. No commit, no stage into the real index, no deviation record:
  the main loop writes those.
- No file of any parent or ancestor build. Parent text that looks wrong is a line in your return, not
  an edit.
- No change to what a unit builds beyond what the parent's text forces, and no new unit.
- No row outside your group, and no row the record marks AGREES or UNKNOWN UNTIL BUILT, apart from
  W1's row 162, which follows row 13.

### Reuse

The parents' specs are the interface, and the cross-check record is the map of what disagrees. The
precedent for a re-ground revision is
`memory/builds/dWellOiledMachine/prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md`.
