**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-42

# Brief: dCalibratedLens's specs re-grounded against dTotalRecall and dDeclaredLoop, with the owner's row-9 pick

## The prompt

> go with (b) for row 9, rest with recommendations

— the owner, 2026-11-03, answering the parents cross-check's parked items. Row 9 is the first pass's
`--stage` kit edge; "the rest" includes the second pass over dTotalRecall and dDeclaredLoop, whose
mismatches this brief folds.

## The brief

### Goal

Revise the dCalibratedLens specs your group names so that every MISMATCH row of the ancestors
cross-check record says what dTotalRecall's and dDeclaredLoop's DEFERRED specs say on origin/main at
`0d1c1dda4`, and so that spec 1 carries the owner's pick on the first pass's row 9. Each spec keeps its
own design. Only what an ancestor's text contradicts changes, by the smallest change that agrees with
the ancestor.

### Items

Read the ancestors cross-check record first:
`memory/builds/dCalibratedLens/build/2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck.md`.
Its table numbers every row. Section 2 of each group's return, in
`memory/builds/dCalibratedLens/build/2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-returns.md`,
quotes both sides of each MISMATCH and states its `Change:`. Re-read both sides before you edit. If
the ancestor's text does not bear a row out, do not edit it. Return it as refused, with the line that
refutes it.

Where the return offers two routes, take the one that conforms to the ancestor text with the smaller
change, unless a rule below decides it. Where both conform, take the first.

Rules that bind every group, so that specs which share a fact fold it one way:

- **The asks are filed.** The main loop filed every ask these specs rely on, on 2026-11-03, in the
  target build's `BACKLOG.md`:
  - TOOL-dDeclaredLoop-109, DERIVE_BREAKPOINTS READS NO REVIEW.MAINTAIN (spec 1 §8 F4).
  - TOOL-dDeclaredLoop-110, THE LOOP KIT REFUSES A CADENCE STEP VALUE (spec 3 §8 F5, which specs 2 and
    5 also wait on).
  - TOOL-dDeclaredLoop-111, REVIEW.COST WRITES NO SHAPE-RUN RECORD (spec 7's review rows).
  - TOOL-dTotalRecall-107, THE ITEM BUDGET HAS NO PER-ROLE FORM (spec 6 §8 F4).
  - TOOL-dTotalRecall-108, THE RECORD-KIND CHECK READS NO SERVES LINE OUTSIDE THE BUILD FOLDERS (spec
    20's hands-off, which spec 42 also needs).
  - TOOL-dWellOiledMachine-128, THE PERIOD KEY HAS NO MONTH AND NO LANDING COUNT (spec 3 §8 F2, cited
    by spec 2).
  - TOOL-dWellOiledMachine-129, TWO STALL AND LOOP CLASSES HAVE NO WRITER (spec 16 §8 F1).

  Where a spec says "the main loop files" an ask, re-word it to name the filed id and its build's
  `BACKLOG.md`, and list it among the build-run preconditions. Spec 20's hands-off becomes a
  precondition, not a contingency.
- **`unarmed` (TOOL-dTotalRecall-42 S2).** A row's `unarmed` reason names the writer that arms it. The
  commit that lands a kind's first tracked record drops that row's `unarmed` key in the same commit,
  and an AC observes the dropped key. A plant that commits a record in a scratch worktree removes
  `unarmed` from its scratch registry rows first, naming tr42 S2, and its exit-0 expectation then
  holds. This applies to specs 2, 3, 5, 19 and 20.
- **`TYPED_RECORD_KINDS`.** A kind homed under `memory/loop-review/` does not join
  `TYPED_RECORD_KINDS`, because PLAY-dOrderedCharter-42 S2 and S3 tie that tuple to the record
  factory's file-name form. It binds through the untyped part of `RECORD_KIND_TOKENS`
  (TOOL-dTotalRecall-18 S7), naming tr1 S2 and dOC-42 S2-S3. The home stays where it is. This applies
  to specs 2, 3, 5 and 20.
- **The item row form (TOOL-dDeclaredLoop-12 §4, dl9).** An `item.loop.*` row with a non-role actor
  carries `inputs`, `allowance`, `returns` spelled `record-kind.<name>`, and `witness`. This applies to
  specs 2, 3 and 5.

A §8 mark reading `RESOLVED (agent, <date>, delegated)` may be re-picked or re-worded when the
ancestor's text forces it, or to name a filed ask. The new mark reads
`RESOLVED (agent, 2026-11-03, delegated)`, keeps its rung and its `widens:` and `relaxes:` values on
one line, and is named in §9. A mark resolved by the owner is never changed. A row that would need one
changed, or a new fork, is returned as parked, with its options, and is not edited. The one exception
is the owner's own pick in W1.

Groups, one writer each. The spec your task block's `input:spec` names leads one group. Edit only
that group's specs:

- **Group W1, led by spec 1:** specs 1 and 42.
  - The first pass's row 9, the owner's pick. cl1 S3's `--stage` admits only `REVIEW_STAGES` members.
    Under option (b) `REVIEW_STAGES` moves to `tools/workflows/review_pin.py` as its one home.
    `roles_lib.py` reaches it through the inline `resolve_kit_dir`, along the existing roles →
    review-harness `requires_if` edge (`tools/roles/kit.toml:19`). Say what `roles_lib.py` does when
    review-harness is absent. Add a §8 fork with the three options of the first-pass record's
    "Parked" section, marked `RESOLVED (owner, 2026-11-03): (b)`, quoting "go with (b) for row 9".
    Move the constant's row in §4's naming table, its Files touched and its ACs.
  - cl1 rows 2, 3, 4 and 7:
    - `unclassed` joins the `--trigger` key set;
    - the caller that runs `--trigger` at a placed breakpoint is named, and the stage is taken from
      the position's step segment;
    - the Maintain boundary is TOOL-dTendedCadence-1 S1's `item.maintain.*` rows, a build-run
      precondition, and §1 says "the five stages dl19 reads";
    - F4 names TOOL-dDeclaredLoop-109.
  - cl42 row 157: state the departure from tr53 S21's caller rule; the case proves the row lookup only,
    and TOOL-dTotalRecall-108 is what makes the real check grade these records.
- **Group W2, led by spec 2:** specs 2, 4, 19 and 20.
  - cl2 rows 11, 13, 14, 16 and 20 (cl4 shares row 14):
    - the item row form;
    - AC8's precondition is TOOL-dDeclaredLoop-110;
    - the legs are claimed in dl1 S7's `memory/map/features/loop.md`, not a new `loop-review.md`;
    - `value-ledger` binds through `RECORD_KIND_TOKENS`;
    - `unarmed` dropped by the first snapshot's commit.
  - cl19 row 126: the `three-homes` plant strips `unarmed` from its scratch rows (tr42 S2).
  - cl20 rows 129, 130, 131, 133 and 134:
    - re-ground on tr53 S21 (the kind comes from `read_bindings`), with TOOL-dTotalRecall-108 as a
      build-run precondition;
    - the three kinds bind through `RECORD_KIND_TOKENS`;
    - cite tr42 S5 rather than "§4 'The kind decides'";
    - AC2 strips `unarmed` from the scratch registry.
- **Group W3, led by spec 3:** specs 3, 5 and 7.
  - cl3 rows 24, 26, 30 and 31:
    - the item row form;
    - F5 names TOOL-dDeclaredLoop-110 and F2 names TOOL-dWellOiledMachine-128;
    - id 37's `unarmed` reason names `loop_review.py record`, and S8's patch build drops the key;
    - `loop-review` binds through `RECORD_KIND_TOKENS`.

    cl3 is the largest spec, so keep the fold short.
  - cl5 rows 38, 40 and 41:
    - AC9 and the keep row follow the `unarmed` rule;
    - S9's row takes the item row form and names TOOL-dDeclaredLoop-110;
    - :147 drops the forward claim and says the owner runs `keep`;
    - `keep` binds through `RECORD_KIND_TOKENS`.
  - cl7 row 61: dl20 S3 is the source of the line's four fields only. The review-act writer is
    TOOL-dDeclaredLoop-111, a build-run precondition, and S6's "two writers" follows.
- **Group W4, led by spec 16:** specs 16, 9 and 11.
  - cl16 rows 110, 113, 114, 115 and 116:
    - the `+`-joined scenario list (say what the tuple keys on, with a two-scenario plant);
    - the rework-budget evidence counted with its `exhausted` refusals, or stated as censored at the
      base, and AC7's plants inside the total;
    - route-backs as `count_returns`'s draws of any cause;
    - "ran under" read at the freeze row's commit;
    - late patch draws (dl30 S7) handled or named.

    F1 names TOOL-dWellOiledMachine-129.
  - cl9 rows 77, 79 and 80:
    - `find --all` is wm32 F6's ask, which dWellOiledMachine's build run files. It is a build-run
      precondition, and the interim refusal is kept.
    - "output tokens only, no input-token field";
    - real dDeclaredLoop item tags in the example.
  - cl11 row 84: dl32 S5's `fix-pass` row is no review row; say how `route-backs-per-build` treats it.
- **Group W5, led by spec 14:** specs 14, 13, 6 and 8.
  - cl14 rows 94, 95 and 97:
    - the `+`-joined `scenario=` list (key the candidate, say which tag fills `extends`, or refuse
      multi-scenario carriers);
    - the schema's `activatable` list;
    - a comparison that takes the promoted composition and files nothing.
  - cl13 row 86: TOOL-dDeclaredLoop-26 §8 F5 is OPEN for the owner and its `compose` verb is no filed
    ask. The precondition is the owner's F5 pick. If S3 then needs a behaviour under F5 (b) that no
    text gives, return it as parked rather than inventing one.
  - cl6 rows 46, 48 and 50:
    - cite tr9 S8 and §10;
    - `gov_record.py` is TOOL-dTotalRecall-2's door, and `budget` is tr9 S6's verb;
    - F4 names TOOL-dTotalRecall-107.
  - cl8 row 69: on `lose`, S3's view drops only the map slot, which is not "the slice manifest alone".
    Restrict the view to the slices on `lose`, or name the departure.

Each revision:

- bumps the **Status:** line by one rev, with date `2026-11-03`, leaving every other field;
- adds one §9 line in the spec's existing form: `- rev-<n> · 2026-11-03 · <sections> · re-grounded
  against dTotalRecall's and dDeclaredLoop's specs, <what moved>, by the brief
  prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground.md (cross-check rows <ids>)`,
  where W1's spec 1 line also names the owner's row-9 pick;
- keeps any line it moves in the ancestor's spelling, quoting the ancestor's surface names exactly.

Return, in this shape and nothing else:

1. One bullet per row you were given: the row id and spec, `folded`, `refused` or `parked`, the
   sections it moved, and for a refused or parked row the line that decides it.
2. One line per spec edited: its new rev and its byte count.
3. The hygiene run's command and what it printed.
4. Ancestor text that looks wrong, one line each with `file:line`.

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

- No file outside your group's specs. No commit, no stage into the real index, no deviation record,
  no BACKLOG row: the main loop writes those.
- No file of any ancestor or parent build. Ancestor text that looks wrong is a line in your return,
  not an edit.
- No change to what a unit builds beyond what the ancestor's text or the owner's pick forces, and no
  new unit.
- No row outside your group, and no row the record marks AGREES or UNKNOWN UNTIL BUILT.

### Reuse

The ancestors' specs are the interface, and the cross-check record is the map of what disagrees. The
precedent is this build's own first-pass brief,
`memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md`.
