# roles — the role catalogue: agent definitions, the workflow table, and the checker that keeps them agreeing

```toml
feature = "roles"
title = "The role catalogue: one owner-editable agent definition per role with an empty house overlay beside it, the table of the workflows a governed session runs its LLM work through, the library every consumer reads them by, and the leg that holds the three and the governing doc to one another"
status = "building"
streams = ["tooling"]
decisions = ["TOOL-aOrientedCast-1"]

[claims]
gate-legs = ["roles catalogue"]
kits = ["roles"]
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/roles/**",
]
```

The prompts an agent starts from were either freeform or string literals inside a harness the owner
could not adjust. This kit makes each role a FILE: a constant block in Claude Code's own agent
format, front matter saying which workflow it serves, which inputs it reads, which path class it
writes and which governing-doc sections it needs, and an overlay the owner edits instead of the base.
It is inert until a consumer reads it: nothing spawns from a role file yet, and the leg is the only
moving part (TOOL-aOrientedCast-1).

## Constraints & why

**One reader, and one composition.** `roles_lib.py` is the only parser of the role files, the
workflow table, the memory-tree conf and the governing doc's sections, and `render_role` is the only
place a role meets its overlay. Every route that hands a role to an agent calls it, so two routes
cannot render one role two ways.

**Front matter is one `key: value` line per key at column 0, values raw, lists comma-joined.** It is
the form Claude Code's own `tools:` already takes, so one reader serves both key families and the
file stays a valid agent definition. An indented, repeated or unknown key is refused: a simple parser
drops an indented key without a word, and a repeated one silently keeps the last.

**The governing doc is located by the memory-tree conf's `CHARTER` key, never by following an
import or assuming a filename.** That declaration already names the file the agent-instructions kit
makes canonical; an absent key is an unarmed check, exit 2, rather than a guess.

**A harness stage key meets its role in the workflow table's `stages`, not in a renderer.** Deriving
it from the slot name fails for most mappings (`synthesis` is the synthesizer, `disposal` spawns as
the spec writer), and a renderer constant is a second home for a workflow fact this checker cannot
see.

**Body ceilings live in the checker, keyed by slot.** A bound an owner edits beside the body it
bounds moves with the thing it bounds; a constant moves only by a reviewed change, and a slot with no
row is refused, so a new role is priced when it is added. Overlays are never bounded: they are the
adopter's own text, and their bytes are printed on every run.

**A well-formed harness the tree does not hold is a note, not a defect.** An adopter may install the
catalogue without the review or build harness kits; whether it should is the wiring check's question.

**The README's catalogue region is rendered, never typed.** A table stated beside the source that
owns it rots; `--write` renders it and every run compares it, so a table edit without a re-render
reds the leg even where every other rule passes.

## Shared seams

- The front-matter rule is ported from the memory-tree gotcha reader's `parse_front_matter`, and the
  conf grammar line for line from the hooks kit's `readConfKey`, rather than imported: a kit file
  names nothing outside itself.
- `resolve_kit_dir` is carried inline under the lib dir's parity table, as every consumer carries it.
- The governing doc's `## §<n> — ` headings are the only contract read from outside the kit; a
  charter rewrite that renumbers sections reds this leg, which is the intended signal.

## Gaps

- No `[[files]]` rule and no registry entry yet, so the deployer reports the directory as unclaimed
  surface until the kit is wired into it.
- `enforced-by` is graded for presence only: the hook arms and legs it names land with later units of
  the same build, and nothing yet proves each one refuses what it claims.
- The checker grades shape, cross-references and size, never what a body means.

## Reuse affordance

seam: `roles_lib.render_role` — reuse for any route that hands a role to an agent or a prompt file;
extend via the house overlay, never a second composition.
seam: `roles_lib.load_workflows` + `workflows.toml` — reuse for any consumer that needs which roles
drive a workflow or which stage key spawns as which role; extend via a new key graded by the checker.
