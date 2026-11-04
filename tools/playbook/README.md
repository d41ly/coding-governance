# playbook — the charter renderer

Fills `coding-governance-agents.template.md` into a target repo's charter, as a re-renderable region.

```bash
python <prefix>/govkit/govkit.py intake --target <repo> --kits playbook,playbook-render,…
bash  <prefix>/playbook/adopt-playbook.sh --target <repo>
bash  <prefix>/playbook/adopt-playbook.sh --target <repo> --check
```

## Why this exists

The charter used to ship with a prose companion telling an agent to fill every placeholder by hand
and delete the conditional blocks their project had no kit for. A catalogue and a program are two
answers to one question, and the catalogue is the copy that rots — so the catalogue is now a
declaration the engine reads, and what a program genuinely cannot decide moved to
`WIRE-INTO-PROJECT.md`.

## What it refuses

It never guesses. Every refusal names what the operator must supply:

- a placeholder the descriptor declares nowhere;
- an `asked` placeholder with no answer in `deploy.toml`;
- a `derived` placeholder whose probe returned nothing and that nothing answers — it does NOT fall
  back to a default it never declared, because a probe quietly returning the empty string is how a
  charter ships with a blank where a branch name belongs;
- a template that is its own charter: `playbook_path` resolving to the `--charter` file;
- a `[charter]` entry that fails its grading (below);
- a `kit:` fence naming something that is not a registry entry;
- a `when:` fence naming a block the descriptor does not declare;
- a `drop_blocks` member that matches no fence.

## Where a value comes from

In order: `deploy.toml`'s `[charter]` table, then `[answers]`, then the probe for a `derived`
placeholder or the declared default for a `defaulted` one. **An answer outranks a probe**, so a probe
that answers wrongly can be corrected without forking the descriptor. The render prints the answer
beside what the probe would have derived, and says when the two are equal. That is a note, never a
failure.

## `playbook_path` has two modes

With `playbook-render` selected, `playbook_path` is where the TEMPLATE lives, and the render writes
the charter named by `--charter` (default `AGENTS.md`). The two may not be one file. Without
`playbook-render`, `playbook_path` is the copied charter itself, and the `playbook-placeholders`
hole probes it for a surviving `{{`. In render mode that hole stands down, because the template
always carries placeholders and `--check` already reports one that survives.

## The `[charter]` table

`[charter]` holds values whose only consumer is this renderer. govkit's token context never reads
it, so nothing in it reaches an argv, and it may carry prose `[answers]` refuses: an em dash, a
backtick, angle brackets. That is where a commit trailer such as
`Co-Authored-By: Name <address>` belongs. The render refuses, naming the key:

- a key that names no declared placeholder;
- a key that names a token an argv or destination needs (it belongs in `[answers]`, where the argv
  can read it; `govkit check` makes the same join over every selected kit);
- a control character other than a newline, the `{{` opener, or a `gov:playbook` region marker.

## One-line regions, and section 2

A region between `<!-- one-line -->` and `<!-- /one-line -->` holds rules a reader takes in at a
glance. After substitution, every non-blank line in one must be a `- ` bullet of at most
`ONE_LINE_MAX` characters; a continuation line, an over-length rule, a nested opener or an unclosed
region is a refusal naming the line. The template fences its governing practices this way, and
section 2 around `{{ADOPTER_RULES}}`, which a target answers as a multi-line `[charter]` string:

```toml
[charter]
adopter_rules = """
- Mobile-first: every screen is designed at 375 px before any wider breakpoint.
- Every design starts as a Figma frame, and the code follows the frame.
"""
```

Unanswered, it renders a single `- none` line. The markers survive into the charter, so a reader
can see where the shape applies.

## Nodes — one tag per machine, in every repository

`fleet.toml` beside the engine names every node once: its tag, user, host, the directory its
checkouts sit under, and its machine-level quirks. Gov is the only place a tag is handed out, and the
file ships into every adopter with this kit, so `{{NODE_TABLE}}` renders the same tag for the same
machine everywhere. A new node claims its tag in gov's own checkout, then every repository it works
in re-renders:

```bash
python <prefix>/playbook/render_playbook.py --claim-node --user <user> --host <host> --projects-root <dir>
```

A node's primary tree is `<projects_root>/<checkout_dir>`, where `checkout_dir` is an `[answers]`
key defaulting to `project_name`: a committed answer, never the directory the rendering clone
happens to sit in, so every node renders the same charter.

One user holds one tag. Every reader of the table matches the user alone, so a second row for the
same user, or one user name inside another, is refused: the readers could not tell them apart.
Claiming in gov also means rendering gov's own charter again in the same commit: `govkit update`
never reaches gov.

The claim takes the lowest letter the fleet has not used and refuses a second claim for one identity.
In an installed copy it refuses outright, because the next update would overwrite the edit. A
repository overrides one node's `primary_tree`, `worktree_root` or `variances` under
`[nodes.<tag>]` in its own `deploy.toml`. The render notes, rather than refuses, a `drop_blocks`
member naming a block v4.0 retired, and notes a `## Node registry` the charter carries outside the
region, which readers would take first.

## The role roster

`{{ROLE_ROSTER}}` is filled by the roles kit's own `roster` verb, found through the sibling
resolver as the gate runner is, so this kit names no sibling kit by literal and the roles kit stays
the one reader of role files. The verb's lines arrive verbatim: this engine adds no `- `, cuts
nothing and reorders nothing, and the one-line region grades the result. A missing kit, a verb that
cannot start, a non-zero exit or an empty stdout prints a `render-playbook: ROLE_ROSTER:` line naming
the cause, and the render refuses unless `role_roster` is answered. A role edit that changes the
roster stales the region, which `--check` reports.

## Two namespaces, and neither reads a boolean

`kit:<id>` drops when the target did not select that kit. `when:<name>` drops when the name is a
MEMBER of `drop_blocks`. Membership rather than truthiness is load-bearing: govkit writes every
answer as a quoted string, so a key "answered false" would arrive as the string `false`, read as
true, and leave the block standing.

## `--check` asserts two things, separately

Region parity and placeholder completeness are different questions, and they fail with different
messages. A target whose descriptor declares nothing for a key renders a region that is perfectly in
sync and still tells the agent to invoke a placeholder's name. The comparison normalises line
endings first — this fleet runs `core.autocrlf=true`, and a charter with no `eol` attribute holds
CRLF in the worktree against an LF blob.

Because that comparison is against a FRESH render, a new renderer makes the old region drift. The
descriptor therefore declares a `[[regenerate]]` block, the adopter's own write mode, and govkit's
`update` runs it after landing a new engine unless GOVKIT_RERENDER=0 is exported
(DEPL-aHalvedInstall-3). Without it every renderer change rolled this kit back at every adopter.

## The region reader is this kit's own

The memory-tree kit's region helper raises when no marker pair is present, so it serves neither the
absent-charter nor the charter-without-a-region state. This engine CONFORMS to the marker-region
contract and is a fifth reader in its case table; it does not import that implementation, which
would be the cross-kit edge the contract forbids.

## The layer register and the layer check

`layers.toml` beside the engine is the product's layer register (PLAY-dOrderedCharter-16): one
`[[layer]]` row per layer, with its `tag` (`layer.<seg>(.<seg>)*`), its `kind` (`core`, `optional`
or `expansion`), `of` (the core row an `optional` row belongs to), its `definition`, the extension
points it `declares` and the ones it `uses`, and `homes` for a tool directory with no descriptor. A
top-level `shared` list names the directories of inline-copied primitives, which hold no layer.

Every kit descriptor joins a layer with two keys of its own, so a layer's kits are derived and never
typed in the register:

```toml
layer = "layer.memory"
optional = [{ part = "gen_build_index.py", point = "point.memory.live-column", fallback = "the Landed-unclosed column renders not-installed: drift-audit" }]
```

`optional` is a core kit's declared slot: an edge from the file it names as `part` to a non-core kit
is allowed, its `point` declared by exactly one core row, its `fallback` what the core does when the
component is absent. A `part` is relative to the kit's home; a flat entry, `home = "."` under
`govkit/entries/`, spells a file under the tool root `{prefix}/<file>`, and a part spelling the tool
root literally is a contract red that names the spelling to write.

A slotted site prints its state on one line, one spelling for every site, after the site's own
prefix (PLAY-dOrderedCharter-17): `slot <point> · <state>`, the state `filled` when the optional
kit returned something, `searched-empty` when it ran and found nothing, or
`not-installed: <fallback>` when it is absent, and never an empty result. The `not-installed` line
takes the place of the site's free-worded skip; a site that printed nothing on success prints
`filled` on stderr, so stdout contracts are unchanged, and every site keeps its exit code. A test
suite's arm that needs an absent kit skips with the same line and counts its assertions.

```
python check_layers.py                 # the gate: the contract, the edges and EX-1 over the tree
python check_layers.py --list          # every row, every descriptor and every edge, allowed or red
python check_layers.py --new <tag> --kind <kind> [--of <tag>] --definition <text>
python check_layers.py --fixture [--plant <case>] [--list]
```

The check reds a row the contract refuses, a descriptor with no layer or an unknown one, a tool
directory nothing claims, a core layer with no kit, a point declared by a non-core row or used where
no single core row declares it (EX-1), and every edge from a file a core kit ships to a non-core kit
that no `optional` row allows. Edges are found by kind: `import`, `dynamic`, `probe`, `copy`,
`shell` and `requires-if`. A spelled path `<home>/<rest>` is an edge only when `<rest>` names a
file the tree tracks under that home, or a directory or glob matching one, that no core kit owns; an
empty `<rest>`, or one opening on a variable, names the home itself and stays an edge. A bare kit
name in a shell file is read from the code memory-tree's `scan_shell_lines` leaves, its quoting
carried across lines; a script whose quoting does not balance is read line by line and named on a
`layers:` line. It does not read a path computed at run time, JavaScript, a file no descriptor
claims, a path that names no file the kit ships (a journal under the git directory, an id shaped
like a path, a file a non-core kit writes but does not track), or a bare kit name inside a string or
a here-document, and says so on every run. `--new` appends a row the contract admits and prints the
descriptor key a kit adds to join it. The imports come from memory-tree's `import_walk.py`, the walk
the verdict-epoch gate shares, and the shell lexer from its `check-arms.py`. The leg is gov's own; `adopt-playbook.sh --selftest` runs every
fixture plant.

## Tags, the index and the resolver

PLAY-dOrderedCharter-19. A tag is `<ns>.<seg>(.<seg>)*`, each segment `[a-z0-9][a-z0-9-]*`, at most 64
bytes; `tag_index.py` compiles it once as `TAG_RE` and `TAG_MAX_BYTES`, and `parse_tag` names the rule a
string breaks. The namespace words are the rows of `namespaces.toml`, each with its `owner`, `layer`,
`source`, `extractor` (`<module>:<function>`), `role`, `purpose-source` and `join-armed-by`, read by
`read_namespaces`. This kit registers `doc` (the charter, the guides, `HYGIENE.md` and
`TEMPLATE-SPEC.md`, a section per `##` heading) and `unit` (each `[[unit]]` row of a kit's
`instructions.toml`, its `scope` values as selector rows, empty and printed `unarmed` until rows land).

PLAY-dOrderedCharter-10 registers eight more, each read from its declaring source by an `extract_<ns>`
function in `tag_index.py` and printed `unarmed` while that source declares nothing: `reader`
(`readers.toml`: `reader.every`, `reader.driver`, `reader.subagent`), `practice` (`practices.toml`),
`level` (`LEVELS` in `instruction_units.py`), `layer` (`layers.toml`), `principle` (`principles.toml`),
`kind` (`kinds.toml`), `kit` (the top-level `id` of every `kit.toml` and `*.kit.toml`, in
`layer.distribution`) and `repo` (`.governance/instructions.toml`'s units). `check` adds the shape check
(every defined tag and selector value in a registered namespace, every segment in shape, at most 64
bytes before any `#`, no first segment that is a namespace word, a registry word outside the segment
shape a red and never a word), the joins (every citation a member; every `reader` and `practice` member
selecting a unit once unit rows exist) and the name-check slot, `point.instruction.name-check`, where the
lexicon's `--tags` grades the same names. A cited span that is the base name of a tracked file is counted
as a file name, never red. The later namespaces are not registered, so their tags red until the build
that arms each adds its row:

| Namespace | Armed by |
|---|---|
| `step`, `item`, `policy` | dDeclaredLoop |
| `role` | dBoundRoles |
| `record` | dTotalRecall |

The index is `<git-common-dir>/gov/index.db`, one SQLite file per node shared by every worktree, never
committed. Rows are keyed by blob, so a commit re-parses only the blobs it changed and one blob at two
paths is parsed once; a worktree's uncommitted edits are its own `dirty_path` rows, served to it alone.
Freshness is keyed on the blob, the extractor and the extractor's version, the first 12 hex of the
SHA-256 of its module file, in `blob_parsed`, written when a run yields no row too: a newly registered
extractor reads the old blobs, an edited module re-runs its extractors, and a blob that yields nothing is
not read again (PLAY-dOrderedCharter-44). Each version's rows stand apart (PLAY-dOrderedCharter-51): two
worktrees whose extractor bytes differ share the file, so `blob_row`, `path_row` and `blob_parsed` carry
the version, a build never deletes another version's rows, and every read is joined to the reading
worktree's own `{extractor: version}` map, so a worktree is served only rows its own extractors wrote. A
tree is fresh under `tree_built(tree, versions)`, `versions` the first 12 hex of the SHA-256 of that map's
sorted `extractor=version` lines. `gov_tag.py --gc` deletes the rows of every version no worktree
`git worktree list` names derives, each read from that worktree's own registry and modules, and refuses,
exit 2, when one of them cannot be read; it prints `tag-index — collected: <n> rows of <m> versions`. A
plain build collects nothing, and a worktree deleted without `git worktree prune` keeps its rows until it
is pruned. A helper imported from another
module is outside that version, so its edit needs `--rebuild`. The file is stamped `user_version` =
`INDEX_SCHEMA`; a file of another stamp is rebuilt from nothing, printing `tag-index — rebuilt: schema
<old> to <new>`.
Blobs are read through memory-tree's `tree_lib.read_blobs_at` and the conf through its `id_grammar`, both
reached with the inline `resolve_kit_dir`, as `policy_value.py` reaches the policy kit's `policy.py get`.

`gov_tag.py` is the resolver, standing in for `gov tag`: `show`, `where`, `refs` and `check`, with
`--rebuild`, `--gc`, `--list-positional` and `--fixture --plant <case>`. `check` grades the backticked and
bracketed Markdown spans outside `<MEMORY_ROOT>/builds/` (`resolves`, `retired`, the bare-name rule and
`owned`) and counts what it does not grade. `aliases.toml` maps each positional label that never moved
to its section; `positional-refs.txt` keeps the live positional references, one `<path>` TAB `<ref>` row
each, as `--list-positional` prints them. An unlisted file:line citation in a `<MEMORY_ROOT>/builds/`
record is printed `positional — grandfathered: <path>:<line>` and never red when every line holding
it was written, as `git blame -M` over the working tree reads it, by a commit that does not descend
from the commit that added `positional.py`, since it was written on a branch that never held the check
(PLAY-dOrderedCharter-47, -53). The key is the line's commit, never the file's: a citation appended
to an old record later, or not yet committed, is graded, and a rename keeps each line's first writer. The sources that tell a writer what to cite are a query, not a list:
`positional.py producers` prints every line of the directive sources (`PRODUCER_PATHSPECS`: the role and
workflow sources, `skills/`, the charter template and the kits' `.template.` sources) spelling
`file:line`, `path and line` or `<path>:<line>`, a render's lines carried by its `.template.` source.
`positional-producers.txt` keeps the hits that direct no line citation, one `<path>` TAB `<line text>`
row each under a `# ` reason, seeded once by `producers --seed`; the arm's `producers` limb reds a hit
neither kept nor naming `path#symbol` or a blob-pinned line, and a kept row no hit carries
(PLAY-dOrderedCharter-48). The `tags` leg runs `check`; the user page is `help/tags.md`.

PLAY-dOrderedCharter-22 adds the `purpose` arm to `check`. Each registry row's `owner` names a build of
the chain registry, `memory/project/chain.toml` (one `[[build]]` row per build, its `slug` and its
`purpose`), and its `purpose-source` grades the namespace's members: `<path>` a tracked file, read
path-only; `<path>#<field>` a field each member's row carries in a `.toml` file or an assignment in a
`.py` file; `#<field>` a field each member's own file carries, `h1` being a Markdown file's first `# `
line. A source the tree does not hold yet is printed `pending` and never graded. Where the conf declares
the design (`DESIGN_RECORD`, `DESIGN_BASELINE`, `DESIGN_VIEW`, `DESIGN_NODES`), the chain registry's
slugs are joined both ways with the design view's builds, and a row with no `purpose` is legal only for a
build the baseline already names; with those keys blank `check` prints that there is no chain to read.

## Edges, their registry and their parser

PLAY-dOrderedCharter-24. `edges.toml` is the edge-type registry: one `[[edge]]` row per type of one
closed set, with `type`, `inverse`, `from`, `to`, `pin` (`none`, `tag` or `clause`), `status`
(`declared` or `derived`) and `declared-at`, read by `edge_grammar.read_edge_types`. It holds P33's
twelve declared types and the derived `cites`; an inverse is derived from its row by
`derive_inverse_edges`, never declared. A row's `to` names namespace words, `any` (every registered
namespace and every native id) or `selects` (every namespace whose `namespaces.toml` row has
`role = "selects"`), so a later selector namespace needs no edit here; a word not registered yet admits
nothing. At a Markdown site an edge is a column-0 line `**Edges:** type=target[,target]`, one per type;
`parse_edge_lines` walks memory-tree's `tree_lib.unfenced_lines` and names every malformed line in one
refusal, and `parse_edge_target` classifies a target as `tag`, `pinned-tag`, `section`, `id`, `id#tag`
or `pinned-id`. `check_edges` reds an unregistered type, a declared inverse or `cites`, a target outside
its row's `to` and a pin on a `pin = "none"` row. `edge_grammar.py --list`, `--parse <file>` and
`--fixture --plant <case>` are its CLI, and the selftest runs every plant. A pin's hash is
`design_lib.derive_pin_hash`, memory-tree's one normaliser, which `derive_clause_hash` calls.

PLAY-dOrderedCharter-28 adds the memory plan's twelve types (`serves`, `made-by`, `caused-by`, `follows`,
`answers`, `runs-in`, `carries`, `carries-clause`, `pinned-at`, `reads`, `writes`, `promoted-from`),
widens `decides` and `after`, and gives a row an optional `writer`: `promoted-from`'s is
`instructions.edit`, so the type read at any other site is red. `edges.toml`'s `[[trailer]]` rows map each
commit trailer key to its type, read by `read_trailer_keys`. `namespaces.toml`'s `[[native]]` rows
register the native-id classes, `family-id` (pattern `id_grammar:grammar_for`, resolver `corpus_ids.py
--print-defined-ids`) and `clause-id` (pattern `design_lib:_CL`, resolver `read_design_view`), read by
`read_native_classes`; `gov_tag.py check` prints each with its owner and population
(`check_native_classes`). A pinned tag is legal only where a row's `pin` is `tag` and resolves when some
committed revision of its unit's text hashes to it (`read_text_history` over `tree_lib.read_blobs_at`);
a pinned clause id only where `pin` is `clause`, resolving against every committed revision of the
design view, the baseline's included. One adapter per site reads edges: `read_header_edges`
(`**Serves:**` through `tree_lib.read_bindings`, `**Caused-by:**`, `**Made-by:**`), `read_section_edges`,
`read_unit_edges`, `read_note_refs`, `read_trailer_edges`, `read_handoff_edges` (the roles kit's
`MARKER_RE`) and `read_carries_edges` (`design_lib.parse_binding_lines`, the carries line's one parser).
`resolve_edge` resolves one target; `--check [--base <rev>]` runs every adapter over the tree and the
trailers since the compare base, and is the `edges` leg of the `tags` pack. It does not grade an edge's
`from`, since no source namespace is registered, nor resolve an `id#tag` target, `unarmed` until
dTotalRecall arms the record namespace; a `serves` id no spec defines is counted, check 21's verdict.
