**Serves:** research PLAY-dOrderedCharter-34

# Brief: spec 34 — the second hand-back, on the template an install reads

## The prompt

> Resume the build, it's no longer paused

— owner, 2026-11-08. Unit 34's builder handed back a second divergence before writing any code. This is the spec's last repair round
in this run: a third hand-back parks the unit for the owner.

## The brief

### Goal

Revise spec 34 so a builder can build it as written over this tree, with no install left reading a template nothing ships.

### Items

1. **S5 retires the seeded template as the render's input, and nothing ships the template an install would then read.**
   `tools/playbook/render_playbook.py#resolve_template_path` would always read the template at `gov_root`, which `main` derives as the
   engine's parent's parent, the target's own root in an install. The playbook entry seeds the template only to its `playbook_path`
   (`tools/govkit/entries/playbook.kit.toml`), the renderer kit ships no template (`tools/playbook/kit.toml`), and unit 31's S5 removes the
   seed rule without a replacement. Every install, update and check of the renderer would then refuse, and F7's remedy of planting the
   template at the matrix's root by hand would hide the break. Weigh under the fork rule, at least:
   - the renderer kit ships the template beside the engine through a root-relative files rule, and the reader looks there first and at
     `gov_root` second, as `resolve_declaration_paths` does for a descriptor;
   - S5 and F7 leave this unit for unit 31, which removes the seed rule, so the input's retirement and its replacement land together, with
     the edge mirrored on spec 31;
   - any option you find narrower. Record the pick in section 8; if every option trips the second or third veto, leave the fork open.
2. **Fixtures reaching the render through `main`.** `tools/playbook/instruction_units.py#run_render`, the edit verb's own re-render
   `tools/playbook/instructions_edit.py#run_render`, and the overlay fixture's command-line run take no `gov_root`. If S5 stays, name their
   seam.
3. **`tools/playbook/overlay.py`.** Its fixture answers `playbook_path` in four arms; if S5 stays, it joins S5's by-value readers and Files
   touched.
4. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

In each spec you change:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance bullets, which
  spell plain tracked paths and never a file not yet tracked. New text names a section in words, and a check by what it checks. A sha
  written in section 2 stays out of backticks, and a Readers clause names readers only, never the command that found them. Every new
  fact a record states is pinned, keyed or marked PINNED or DERIVED; name a unit by its id. Every function name it mints passes
  `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Spec 34 builds as written over HEAD, every edge it gains is mirrored, and each change has a history line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### Gates

Memory hygiene, as your role runs it, its Readers check included.

### Non-goals

- No code. No edit to a spec other than 34 and, where a pick hands it work, 31.
