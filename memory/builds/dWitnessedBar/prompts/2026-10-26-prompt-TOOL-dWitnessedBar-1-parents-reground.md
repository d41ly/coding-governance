**Serves:** research TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56

# Brief: dWitnessedBar's specs re-grounded against dOrderedCharter's and dDeclaredLoop's landed specs

## The prompt

> Then dWitnessedBar (26 of 88 exposed) and dPlacedRequest (12 of 63 exposed). [...] Have
> `gov-spec-writer` agents revise only the mismatched specs.

— the dClosedLoop housekeeping session, 2026-10-25, relaying the owner's hold on the dBoundRoles,
dTotalRecall and dKeptSession spec runs until this re-ground lands.

## The brief

### Goal

Revise the 15 dWitnessedBar specs that the cross-check record names under "For the re-ground". Each
one should state dOrderedCharter's and dDeclaredLoop's surfaces the way their specs now spell them:
dOrderedCharter at `462d20f35`, and dDeclaredLoop at its re-ground commit `783f1ad3a`. Each spec keeps
its own design, and only its assumptions about the two parents change.

### Items

Read the cross-check record first,
`memory/builds/dWitnessedBar/build/2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck.md`.
Its summary table numbers every assumption (rows 1 to 100), and "The mismatches, both sides quoted"
gives both sides of each MISMATCH. Rows 77 and 100 are the main loop's, explained in its Method. Read
each parent spec the record cites, at the lines it cites. This brief summarises them, and where the
two differ, the specs win. Before you edit for a row, re-read both sides. A row the parent's text
does not bear out is not edited: return it as refused, with the line that refutes it.

Facts every revision uses:

- **A typed record kind.** dOrderedCharter unit 42 S2 makes `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the record factory's kind list. `build_records.py` refuses at import
  any kind table that differs from it (oc42:40-44). Under S3, a `-<kind>-<n>.md` file in `build/` whose
  Serves kind is not `<kind>` is malformed (oc42:45-49). S5 keeps the closed kind list in
  `tools/memory-tree/HYGIENE.template.md`. A unit that adds a kind adds it to all three in its own pass,
  and its records serve as `<kind> <id>`, never `journal`. One criterion observes the record bind:
  `gen_build_index.py --print-bindings` names it. dDeclaredLoop's specs 3, 16, 17 and 22 now read this
  way at rev-3: copy their wording. Whether `build_records.py new <kind>` is generic per kind is
  unknown until dOrderedCharter unit 7 builds. State the flags your unit passes, and claim no door.
- **A sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-203; dl12 S4 at
  rev-3). Code in `tools/run-gates/` or `tools/govkit/` reaches a playbook, loop or policy module by
  subprocess, finding it through an inline `resolve_kit_dir`. Where the verb it needs does not exist,
  write a §8 fork open for the owner. The options are an ask to the parent for the verb, or a declared
  `requires_if` import row like `tools/memory-tree/kit.toml:8`, with the reason the rule admits it.
  Recommend one. dDeclaredLoop's specs 12 F5, 18 F5, 26 F5 and 34 F6 are the precedent.
- **The overlay composition.** dOrderedCharter unit 35 S5 reads `instructions.exclude` at `--rev HEAD`
  (oc35:64-67), as unit 46 S6 rules for every read the composition makes (oc46:65-71), with an unborn
  `HEAD` reading the default `[]`. Unit 35 S7 and S8 apply a stale patch under `order` and `warn`,
  hold it under `refuse`, and file an order through `write_row_order` for each held or orphaned patch
  (oc35:84-94). `instructions.stale` is read at the target's `HEAD` (oc33:362).
- **A new leg's `enforces`.** dOrderedCharter unit 7 S3 reds a leg with no `enforces`, and the
  pending list only shrinks (oc7:58-63, :228). Under `core.bypass = never`, the meta-check also reds
  any leg whose `enforces` is non-empty and that carries a `guard` (oc7:109-111).
- **dDeclaredLoop's program rules.** dl12 S1 to S3, at `783f1ad3a`: an item belongs to its own step's
  table, and adopt, entry, lifecycle and probe items are never steps of the five (dl12:80-81). Every
  input names a layer tag of `tools/playbook/layers.toml` (dl12:43). `returns` names a
  `record-kind.*` tag (dl12:113). `routes` holds exactly the outcomes as keys (dl12:147-148). Run
  `python loop_lib.py --check` in the criterion that observes a row.
- **dDeclaredLoop's guard.** dl2's `guard.py --staged` runs at pre-commit, only when a guarded path is
  staged and stderr is not a terminal, so no commit message exists to read (dl2:177-178). The
  `Gov-Policy:` trailer is checked by `--push-range` (dl2:76-80). The owner proof tests stderr (dl2 S5,
  oc15 F4).
- **An ask.** No dWitnessedBar spec files a row in another build's `BACKLOG.md`. Where a fix needs a
  parent change, write a §8 fork open for the owner, with its options and a recommendation, and name
  the ask the build run would file.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every
spec of that group, and no other:

- **Group A, records and legs, led by spec 1:** specs 1, 8, 11, 14, 25 and 51.
- **Group B, loop rows and the guard, led by spec 3:** specs 3, 6, 12, 15, 23 and 56.
- **Group C, composition and lists, led by spec 28:** specs 16, 18 and 28.

The spec files are `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md`.
Write probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-amazing-roentgen-42b269/e5868d60-4c6d-4ccd-a640-f987e8390bd7/scratchpad/wb-w<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; the sections moved; each fork
you added or re-resolved, with its mark; each record row you refused, and why; its byte count; and
any parent spec that looks wrong.

Per spec, by the record's rows:

1. **Specs 1, 8, 14 and 25** (rows 2, 18, 41, 77). The kinds `gate-health`, `flake`, `widen` and
   `leg-tail` each join `TYPED_RECORD_KINDS` and the HYGIENE kind list, and serve as their own kind.
   Each spec adds `tools/memory-tree/tree_lib.py` and the HYGIENE template to Files touched, and adds
   the binding criterion. wb8:98's hand-off of a `journal` binding goes.
2. **Spec 51** (row 100). S7's `journal` binding is overturned by the kind facts above. S7 states that
   the flake and gate-health records serve as their own kinds, joined by specs 8 and 1, and AC4
   checks that. It is at 48719 bytes, so replace text and do not append.
3. **Spec 11** (rows 24, 29). §5 and §6 state how `enforces` on every leg interacts with
   `core.bypass = never`, which reds a guarded leg whose `enforces` is non-empty. Add a criterion that
   runs oc7's `bypass-never` plant over the generated manifest, or write the fork for an ask that
   narrows oc7's core-leg predicate. F2's rung-1 precedent is re-cited to
   `TOOL-dDeclaredLoop-6`, the spec that spells `kind.policy-key`, keeping oc7:133 as the source of
   the kind's name.
4. **Spec 3** (rows 4, 6).
   - The owner-exception alternative is narrowed to what oc7 S9's register excuses: a red of a core
     gate, matched by principle and part. Say that under `owner-only-expiring` no exception is
     admitted until unit 15's check lands, or write the fork for an ask that the bar's landing readers
     read the register.
   - `judge` reaches dl12's item rows by subprocess, through the sibling-kit fact. `loop_lib.py` has
     only `--check` and `--fixture`, so write the fork for a read verb.
5. **Spec 6 and spec 56** (rows 13, 98). S9's `--staged` refuses every agent-staged change to an
   `OWNER_ONLY_KEYS` key under every value, naming the key, as dl2's guard-self step does
   (dl2:182-185). The trailer stays with `--push-range`. AC8's fixture sets
   `policy-file.guard = "agents-with-reason"`. Spec 56's AC16 checks that key-level refusal.
6. **Spec 12** (row 37). A leg tag's rename or retirement has no write path in oc15, whose write
   verbs and `Unit` field are instruction units' (oc15:55-57, :96-99, :180). Name the path as unowned:
   either the fork for an ask that the change door accept a `leg.*` tag, or a hand-off to spec 11's
   leg factory, with oc15 S9 named only as the reader of retired rows.
7. **Spec 15** (rows 44, 45, 46). `item.test.seed` is an adopt-program item outside the five steps,
   or the fork for where adopt items are declared. Name a registered layer tag, or derive it from
   `layers.toml` at the pass. `returns` names a `record-kind.*` tag, or states that the item writes
   none and which value dl12 admits for that.
8. **Spec 23** (row 69). S7 re-keys `[item.routes]` in the same edit that changes the outcomes, and
   AC6 also runs `python loop_lib.py --check`, requiring exit 0.
9. **Spec 28** (rows 85, 86, 87).
   - S5 reads `instructions.exclude` at the target's `--rev HEAD`, refusing on exit 2 and passing
     `[]` on an unborn `HEAD`.
   - S5 reaches the composer only by subprocess, and names the verb.
   - S5 says which composition governs, so that gate-leg rows are composed once, beside unit 33's
     drift row pass.
   - S5 follows unit 35's stale and orphan modes, files their orders, and records any
     "no refusal withholds another leg" departure as a fork.
   - Add the plants these need.
10. **Spec 16** (row 49). S6's readers gain `tools/run-gates/owed_rows.py`, through oc50 S2's
    leg-removed population and its `--selftest` plant. Files touched gains it, and a criterion runs
    `owed_rows.py --selftest` after the rename.
11. **Spec 18** (row 59). S5 adds `positional.py seed` and `pin`, the `positional-*` fixture writer
    under `gov_tag.py --fixture`, and `instruction_units.py fixture --plant legacy` to its readers. It
    lists both modules in Files touched, and puts `tags positional selftest` on its gate line.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-26, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record, with its row numbers.
- Replace each now-false sentence where it stands.
- A resolved fork whose chosen option a parent now rules out is re-resolved on rung 1, naming the
  parent, and marked `RESOLVED (agent, 2026-10-26, delegated)`. A fork this brief tells you to leave
  open for the owner stays open, with its recommendation. Re-open no other fork.
- Spell a `tools/` path inside an acceptance criterion as the spec already does.
- Stay under the class cap of 49152 bytes.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>`, and §9 holds the new line.
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `wbN:L`
  prints nothing, or prints only the corrected sentence.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows. The main loop runs the rest
and renders the index.

### Non-goals

- No file outside the spec files of your group. No commit, no stage into the real index, no
  deviation record: the main loop writes those.
- No file of dOrderedCharter, dDeclaredLoop, dSafePassage or dGroundRules. A parent spec that looks
  wrong is a line in your return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### Reuse

The parents' specs as the interface. The cross-check record as the map of what moved. dDeclaredLoop's
re-ground brief,
`memory/builds/dDeclaredLoop/prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md`,
and its rev-3 specs, as the precedent for how a revised spec reads.
