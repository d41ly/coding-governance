**Serves:** research PLAY-dOrderedCharter-31

# Brief: spec 31 — the second hand-back, on the adopter-rules step losing and reordering rules

## The prompt

> interrupted, rearm and resume unattended

— owner, 2026-11-09. Unit 31's builder handed back a second divergence before writing any code, with probes. This is the spec's last
repair round in this run: a third hand-back parks the unit for the owner.

## The brief

### Goal

Revise spec 31's adopter-rules step so it meets AC7 as written: the project block holds the same lines in the same order after the up.

### Items

1. **Rules lost.** The step's row carries no scope. `tools/playbook/render_playbook.py#build_project_block` renders only units
   `tools/playbook/instruction_units.py#derive_unit_selection` keeps under its every-reader selector, which keeps a unit only when its
   scope holds the selector or `reader.every`; a scope-less row is dropped. State that each converted row carries
   `scope = ["reader.every"]`, and add it to the rows design and AC7's plant.
2. **Rules reordered.** `tools/playbook/overlay.py#derive_overlay_text`, which `write_overlay_units` calls, places new rows by level then
   tag, and the step derives the tag from the rule's text, so the rendered order turns alphabetical. The main loop's ruling under the fork
   rule, since it keeps the stated edge to unit 32's writer and adds no surface: the converted tag carries an ordinal segment that sorts in
   rule order, for example `repo.rule-NN-<seg>` with a zero-padded two-digit ordinal (gov's own key holds nine rules); state the grammar,
   its width rule if a key ever holds more, and AC7's reorder plant. If you find this trips a veto, say which and leave the fork open.
3. **What the builder confirmed for the rebuild**, kept as written: the Codex constant moves into the renderer and `budgets.py home` reads
   it; the retired step id with `successor = "none"` is accepted; the four names `tools/codebase-map/map_lib.py` re-exports; the one-line
   cap row the step refuses over; unit 39 re-adds the wiring leg by name.
4. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief. The parked forks F8
  and F9 stay as they are.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance bullets, which
  spell plain tracked paths and never a file not yet tracked. New text names a section in words, and a check by what it checks. A sha
  written in section 2 stays out of backticks, and a Readers clause names readers only, never the command that found them. Every new
  fact a record states is pinned, keyed or marked PINNED or DERIVED; name a unit by its id. Every function name it mints passes
  `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Spec 31 builds as written over HEAD, and each change has a history line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### Gates

Memory hygiene, as your role runs it, its Readers check included.

### Non-goals

- No code. No edit to another spec.
