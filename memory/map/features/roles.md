# roles — the role catalogue: agent definitions, the workflow table, and the checker that keeps them agreeing

```toml
feature = "roles"
title = "The role catalogue: one owner-editable agent definition per role with an empty house overlay beside it, the table of the workflows a governed session runs its LLM work through, the library every consumer reads them by, and the leg that holds the three and the governing doc to one another"
status = "building"
streams = ["tooling"]
decisions = ["TOOL-aOrientedCast-1", "TOOL-aOrientedCast-2", "TOOL-aOrientedCast-3", "KICK-aOrientedCast-2", "TOOL-aOrientedCast-8", "TOOL-aOrientedCast-10"]

[claims]
gate-legs = ["roles adopter self-test", "roles catalogue", "roles render selftest", "roles render wiring"]
kits = ["roles"]
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = ["build"]
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
moving part (TOOL-aOrientedCast-1). The handoff renderer, `handoff.py`, is its first consumer: it
composes a role with a task block read from the session card, the build's brief record, the
governing doc and the caller's arguments into one hashed prompt file under the build's `prompts/`,
checks such a file's hashes, and prints the stage-to-role map a harness takes (TOOL-aOrientedCast-2).
The agent-type renderer, `render_agents.py`, is its second: it renders each `agent`-true role into a
Claude Code agent type under `.claude/agents/`, trimmed of the charter by `omitClaudeMd: true` and
carrying the charter sections the role names instead, beside the generated index `.claude/roles.json`
the hooks read; its `--check` is the `roles render wiring` leg (TOOL-aOrientedCast-3). The kit's
adopter, `adopt-roles.sh`, renders the `/build` Skill from `SKILL.template.md`: the router an
attended session follows after kickoff's go, whose `## Stage` headings the render binds to the
workflow table's stages, and whose `--check` byte-compares the committed render (KICK-aOrientedCast-2). The
kit is a default adopter kit: govkit installs it, seeds the house overlays once, and its adopter
renders all three artifacts at install and update behind the one `roles render wiring` leg; with no
governing doc at `CHARTER` it renders the Skill alone and exits 3, an accepted outcome, and
`check-wiring.sh` reports the install `UNWIRED` naming the doc (TOOL-aOrientedCast-8).
Every agent type carries the reasoning effort the seeded `house/policy.toml` sets for its role,
read by `roles_lib.load_policy` and graded as R12, and `handoff.py stage-efforts <workflow>` prints
the per-stage levels a harness call passes as `efforts`, so one role runs at a workflow's own level
(TOOL-aOrientedCast-10).

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

**Effort lives in one seeded policy file, never in a role's front matter.** The owner edits one
file an update keeps; a key in each role would be nine engine files an update overwrites and a
second answer to one question. An absent file refuses rather than falling back, so a deleted seed
cannot silently drop every level the owner set.

**Body ceilings live in the checker, keyed by slot.** A bound an owner edits beside the body it
bounds moves with the thing it bounds; a constant moves only by a reviewed change, and a slot with no
row is refused, so a new role is priced when it is added. Overlays are never bounded: they are the
adopter's own text, and their bytes are printed on every run.

**A well-formed harness the tree does not hold is a note, not a defect.** An adopter may install the
catalogue without the review or build harness kits; whether it should is the wiring check's question.

**The README's catalogue region is rendered, never typed.** A table stated beside the source that
owns it rots; `--write` renders it and every run compares it, so a table edit without a re-render
reds the leg even where every other rule passes.

**The renderer asks the kickoff checker where the card is, and never joins the path itself.** The
card's location is that checker's rule; spelling it here too would be a second home for it. The
checker is resolved through the inline kit resolver, then the one tracked file of its name, because
gov homes it under `skills/`, where no probe walks.

**A `task:` value is read by the kickoff checker's field grammar, ported, not called.** That grammar
is an awk program inside a shell script; the port is the second implementation, and the renderer's
fixture renders values from a card that checker accepted, which is the cross-check.

**Each section is hashed on its own, CRLF folded.** The marker sits inside the file, so a
whole-file hash would contain itself, and a typed agent spawn carries the task section alone; a
CRLF working copy hashes like its blob.

## Shared seams

- The front-matter rule is ported from the memory-tree gotcha reader's `parse_front_matter`, and the
  conf grammar line for line from the hooks kit's `readConfKey`, rather than imported: a kit file
  names nothing outside itself.
- `resolve_kit_dir` is carried inline under the lib dir's parity table, as every consumer carries it.
- The governing doc's `## §<n> — ` headings are the only contract read from outside the kit; a
  charter rewrite that renumbers sections reds this leg, which is the intended signal.

**The renderer owns the catalogue's names plus the on-disk index's, never the directory.** An
adopter keeps agent definitions of its own under `.claude/agents/`; the index already records every
name a previous render wrote, so a stale type is unlinkable without a marker key in each file.

## Gaps

- `enforced-by` is graded for presence only: the hook arms and legs it names land with later units of
  the same build, and nothing yet proves each one refuses what it claims.
- The checker grades shape, cross-references and size, never what a body means.

## Reuse affordance

seam: `roles_lib.render_role` — reuse for any route that hands a role to an agent or a prompt file;
extend via the house overlay, never a second composition.
seam: `roles_lib.load_workflows` + `workflows.toml` — reuse for any consumer that needs which roles
drive a workflow or which stage key spawns as which role; extend via a new key graded by the checker.
seam: `handoff.py render` / `harness-args` — reuse for any route that hands an agent its prompt or a
harness its roles; extend via a new `reads` source in the renderer, never a hand-written prompt.
