# Tags and the resolver: `gov tag`

**What it is.** A tag names one thing in the repository: `doc.build-method` is the build method
guide, `doc.build-method#m5-recall-and-reuse` its `## M5` section. A tag is `<ns>.<seg>(.<seg>)*`,
lower-case, at most 64 bytes, and its namespace is a row of `tools/playbook/namespaces.toml`. Ten
namespaces are registered today, each read from the file that declares its members:

| Namespace | Its members come from |
|---|---|
| `doc` | the charter, each guide under `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`, one section per `##` heading; each `[[document]]` row of `tools/playbook/documents.toml` none of those already names; and each reference page's `registry` tag, such as `doc.reference.kinds`, declared at its row of `tools/playbook/references.toml` |
| `unit` | each `[[unit]]` row of a kit's `instructions.toml` |
| `reader` | `tools/playbook/readers.toml`: `reader.every`, `reader.driver` and `reader.subagent` |
| `practice` | `tools/playbook/practices.toml` |
| `level` | `LEVELS` in `tools/playbook/instruction_units.py` |
| `layer` | each `[[layer]]` row of `tools/playbook/layers.toml` |
| `principle` | `tools/playbook/principles.toml` |
| `kind` | `tools/playbook/kinds.toml` |
| `kit` | the `id` of each `kit.toml` and `*.kit.toml` descriptor |
| `repo` | the units of `.governance/instructions.toml` |

A namespace whose file declares nothing yet prints as `unarmed`, and nothing in it is graded. A tag in
a namespace no row registers, such as `step.build`, is red: `step`, `item` and `policy` join when
dDeclaredLoop registers them, `role` with dBoundRoles and `record` with dTotalRecall.

The resolver is `tools/playbook/gov_tag.py`, which stands in for `gov tag`. It reads a derived index,
`<git-common-dir>/gov/index-s<n>.db`, `<n>` the index's format number: one SQLite file per machine
that every worktree shares, built on first use, never committed. A commit re-parses only the files it
changed, and a worktree's uncommitted edits are served to that worktree alone. A newly registered or
edited extractor re-reads the files it reads on the next build, and so does one whose imported helper
module was edited. A new format reads a file of its own name; a file stamped with another format is
rebuilt in place, never deleted, so a session reading it keeps it, printing
`tag-index — rebuilt: schema <old> to <new>`. An older format's file is left behind, unread, until you
delete it. Deleting the file costs one rebuild. Two worktrees whose
extractor code differs keep their rows side by side in the one file, and each is served only the rows
its own extractor code wrote, so switching between them re-parses nothing.

## How to use it

- **Find a tag:** `python tools/playbook/gov_tag.py where doc.build-method` prints
  `tags: memory/guides/BUILD-METHOD.md:1`. A positional label works too, through
  `tools/playbook/aliases.toml`: `python tools/playbook/gov_tag.py where "BUILD-METHOD M5"` prints the
  line of `## M5`. <!-- usage: script:tools/playbook/gov_tag.py#where 9a2511d8 -->
- **Read it:** `python tools/playbook/gov_tag.py show doc.build-method#m5-recall-and-reuse` prints the
  section's lines. <!-- usage: script:tools/playbook/gov_tag.py#show 09500daf --> A tag a change record
  retired has no definition, so `show` prints its `retired` row instead and exits 0: kind `retired`, then
  `**Successor:** <value>`, one tag for a rename, the list for a split and `none` for a removal. `where`
  and every resolver still find nothing for it, so a retired tag never resolves as live.
- **See who cites it:** `python tools/playbook/gov_tag.py refs doc.build-method` prints `path:line`
  for every citation, a build record's included. <!-- usage: script:tools/playbook/gov_tag.py#refs c503761e -->
- **Check the tree:** `python tools/playbook/gov_tag.py check` runs the checks below; the `tags` leg
  of the merge bar runs the same command. `--base <rev>` names the revision new text is measured
  against; without it the merge bar's compare base is used. <!-- usage: script:tools/playbook/gov_tag.py#check 5c4c67e4 -->
- **Rebuild, collect, list, plant:** `python tools/playbook/gov_tag.py --rebuild` rebuilds the index
  from nothing; `python tools/playbook/gov_tag.py --gc` deletes the rows of extractor code no live
  worktree carries any more, printing `tag-index — collected: <n> rows of <m> versions`, and refuses
  when a worktree's registry cannot be read; `python tools/playbook/gov_tag.py --list-positional`
  prints one `<path>` TAB `<ref>` row per positional reference, the rows
  `memory/project/positional-refs.txt` keeps; and
  `python tools/playbook/gov_tag.py --fixture --plant scope` runs one planted case in a scratch
  repository. <!-- usage: script:tools/playbook/gov_tag.py 6cb6638a -->

Every command takes `--json` for machine output, the index's only JSON.

## What a citation is

A citation is the whole text of a backticked span, or of a bracketed span, in a tracked Markdown
file, outside code fences, that is a tag of a registered namespace: `` `doc.build-method` `` or
`[doc.hygiene#rules]`. Nothing in a `.py`, `.sh`, `.js`, `.toml` or `.json` file is one. To write a
tag-shaped word that is not a citation, quote it another way, with doubled backticks for example.

## What `check` reds

`check` grades the citations outside `memory/builds/`, where frozen records and unbuilt specs sit:

- **unresolved** — a citation that names no row, such as `` `doc.no-such-doc` `` in a guide.
- **retired** — new text citing a retired tag, as `tags.retired-cites` says; and a retired name
  minted again, under every value.
- **bare** — a bare name, a tag less its namespace, as `tags.bare-refs` says.
- **owned** — a tag minted in a core layer's namespace by a kit whose layer is optional or an
  expansion.
- **shape** — a defined tag, or a value a unit's `scope` selects, in an unregistered namespace, with a
  segment outside `[a-z0-9][a-z0-9-]*`, longer than 64 bytes before any `#`, or whose first segment is
  itself a namespace word, such as `` `practice.repo.x` ``.
- **join** — a citation that is no member of its namespace, such as `` `layer.nowhere` ``; and a
  `reader` or `practice` member no unit selects, once some unit's `scope` names a tag of its namespace.
  Until then the namespace prints `selects · unarmed`. A describing namespace's unused members are
  listed, never red.
- **purpose** — a namespace row whose `purpose-source` a member lacks; a chain registry row naming no
  build of the design view, a design build with no row, and a row with no `purpose` for a build v2's
  `[chain]` did not name at the baseline. A row whose `owner` the chain registry does not hold is
  printed `tags: purpose · owner '<owner>' · unarmed: no build of <chain registry>, <n> namespace row(s)
  not graded for it` and is never red; at a repository that installed the kit, which holds no chain
  registry of its own, that is every owner. See "Where a purpose is read" below.
- **positional** — a positional reference the list `memory/project/positional-refs.txt` does not
  hold, or a row the tree no longer cites; an absent list is red. Where the list's folder,
  `<MEMORY_ROOT>/project/`, is absent too, as at a repository with no memory tree adopted, the arm
  prints `tags: positional · unarmed: <MEMORY_ROOT>/project is absent, so no memory tree is adopted
  here` and is never red.
- **unclosed fence** — a Markdown file that opens a code fence and never closes it, printed as
  `<path>:<line> · unclosed fence ·` at the line the fence opens. Every line after it is inside the
  fence, so a citation there goes unread; close the fence. Under `memory/builds/` the file is a frozen
  record, so it is printed as `tags: unclosed fence, frozen record, printed` and never red.

A backticked span that is the file name of a tracked file, such as `` `kit.toml` ``, is a file name,
not a citation: it is counted as `<n> file names not graded` and never red. The same span with no such
file tracked is red as unresolved.

Where the lexicon kit is installed, `check` also hands every tag it grades to the lexicon's tag-name
check and prints `slot point.instruction.name-check · searched-empty`, or `· filled` with its findings
as reds. Without the lexicon it prints `· not-installed: the shape check stands alone`, and the shape
check decides alone.

Nothing it skips is silent. The summary line counts the citations graded, the unresolved, the
retired cited, the bare references, the citations in build records not graded and the paths outside
Markdown not read, and prints `tags: unarmed <ns> (<n> not graded)` for each empty namespace.

## Where a purpose is read

Every row of `tools/playbook/namespaces.toml` carries two fields the `purpose` arm grades:

- **`owner`** — the chain build that owns the namespace, a `slug` of `memory/project/chain.toml`. An
  owner the registry does not hold is printed `unarmed`, never red.
- **`purpose-source`** — where the namespace's members say what they are for, in one of three forms:

| Form | Example | What is graded |
|---|---|---|
| `<path>` | `tools/govkit/registry.toml` | the path is tracked; no member is graded, and the row prints as path-only |
| `<path>#<field>` | `tools/playbook/readers.toml#why` | every member at a `.toml` path carries the field on its row; a `.py` path assigns it at the top level. A path of any other suffix is red |
| `#<field>` | `#h1` | every member's own file carries it: its TOML row's key, or for `h1` a Markdown file's first `# ` line outside a code fence |

A source not in the tree yet, or a `#<field>` namespace with no member, prints as
`tags: purpose · pending <ns> · <source>` and is counted, never graded. Once the file lands, its row is
graded with no edit to the registry, and a member lacking the field is red. Either field left empty
stops `check` at once, exit 2, naming the row.

**The chain registry**, `memory/project/chain.toml`, holds one `[[build]]` row per chain build, a
`slug` and a `purpose`:

```toml
[[build]]
slug = "dOrderedCharter"

[[build]]
slug = "dExampleMoved"
purpose = "a build no baseline row names must declare one"
```

Its slugs must match the builds of the design view (`DESIGN_VIEW` in `.memory-tree.conf`) both ways.
A build that v2's `[chain]` named at `DESIGN_BASELINE` may leave `purpose` out until dTotalRecall's
PM-5 unit reviews it, and is counted as awaiting that review; any other row needs one. The summary
prints `<n> registry rows joined to <n> view builds, <n> rows awaiting PM-5's review`. Where the four
`DESIGN_*` keys are blank, as in a project that adopted the kit, `check` prints
`tags: purpose · no chain to read` and grades only the namespace rows.

## Edges: typed relations between tagged things

An edge says how one thing relates to another, by type: `implements`, `tests`, `amends`. The types
form one closed set, the rows of `tools/playbook/edges.toml`. Each type's inverse is derived from its
row and never written: declaring `tests=kit.y` gives `` `kit.y` `` its `tested-by` edge.

In a Markdown file an edge is one line at column 0, outside a code fence, one line per type:

```text
**Edges:** implements=feature.x
**Edges:** tests=kit.y,kit.z
```

A target holds no space, comma or bracket. It is a tag (`` `kit.y` ``), a section (`` `doc.hygiene#rules` ``), a
native id (`PLAY-dOrderedCharter-24`), an id's section (`PLAY-dOrderedCharter-24#goal`), or a tag or
id pinned to a hash (`kit.y@1a2b3c4d`). The set, as `--list` prints it:

| Type | Inverse | From | To | Pin |
|---|---|---|---|---|
| `part-of` | `has-part` | any | any | none |
| `implements` | `implemented-by` | any | `feature`, `spec` | none |
| `tests` | `tested-by` | any | any | none |
| `decides` | `decided-by` | `decision` | any, `commit`, `item` | none |
| `instructs` | `instructed-by` | `unit` | `selects` | none |
| `enforces` | `enforced-by` | any | `unit`, `practice` | none |
| `after` | `before` | `build`, `session` | `build`, `session` | none |
| `supersedes` | `superseded-by` | any | any | tag |
| `amends` | `amended-by` | any | any | tag |
| `patches` | `patched-by` | `build` | `build`, `item` | none |
| `owner` | `owns` | any | `build`, `layer` | none |
| `layer` | `in-layer` | `kit` | `layer` | none |
| `cites` | `cited-by` | any | any | none, and derived from the text |
| `serves` | `served-by` | `record`, `work-order`, `commit` | `family-id`, `item`, `build` | none |
| `made-by` | `made` | `commit`, `record` | `act`, `owner` | none |
| `caused-by` | `causes` | `record` | any | none |
| `follows` | `followed-by` | `act` | `work-order` | none |
| `answers` | `answered-by` | `return`, `answer` | `work-order`, `fork` | none |
| `runs-in` | `hosts` | `act`, `claim`, `commit` | `session` | none |
| `carries` | `carried-by` | `landing` | `family-id`, `commit` | none |
| `carries-clause` | `carried-in` | `family-id` | `clause-id` | clause |
| `pinned-at` | `pinned-by` | `record`, `probe`, `claim` | `commit`, `tree` | none |
| `reads` | `read-by` | `item`, `role` | `kind` | none |
| `writes` | `written-by` | `item`, `role` | `kind` | none |
| `promoted-from` | `promoted-to` | `unit`, `scenario` | any | none, and written by `instructions.edit` alone |

`any` is every registered namespace and every native id. `selects` is every namespace whose row in
`namespaces.toml` has `role = "selects"`, so a selector namespace a later build registers is an
`instructs` target without a change to `edges.toml`. A word no row registers yet, such as `feature`,
`item`, `commit` or `session`, admits nothing until its build registers it, and an id under such a
word is counted `unarmed`.

**Native ids.** An id that is no tag belongs to a native class, one `[[native]]` row of
`namespaces.toml` naming its `owner`, the `pattern` that compiles it and the `resolver` that lists its
members. Two are registered: `family-id`, the `PLAY-dOrderedCharter-24` ids, owner dOrderedCharter,
resolved against the ids a spec defines; and `clause-id`, the `cl-dTrueNorth-0001` clause ids, owner
dTrueNorth, resolved against the design view. `python tools/playbook/gov_tag.py check` prints each
class with its owner and its member count. A class whose owner the chain registry does not hold prints
`tags: native · <class> (owner <owner>) · unarmed: no build of the chain registry` and runs no
resolver, the same way the `purpose` arm prints such an owner unarmed, so its members are not counted.

**Pinned forms.** A pin is written `@` and eight hex digits. A pinned tag (`kit.y@1a2b3c4d`) is
legal only on `amends` and `supersedes`, and resolves when some committed revision of the tag's unit
text hashes to it. A pinned clause id (`cl-dTrueNorth-0001@1a2b3c4d`) is legal only on
`carries-clause`, and resolves when the clause's text at the design baseline or in some committed
revision of the design view hashes to it, so a pin written before a deviation moved the clause still
resolves.

**Where edges are read.** Beyond the `**Edges:**` line: a record's `**Serves:**` line as `serves` and
its `**Caused-by:**` and `**Made-by:**` lines; a spec's `**Carries:**` line as `carries-clause`; a
work order's `gov:handoff` marker's `unit=` and `build=` as `serves`; an instruction unit's `edges`,
`scope`, `required-by` and `enforced-by`; a code note's `refs=` segment; and a commit's trailers,
`Pass:`, `Gov-Unit:` and `Gov-Item:` as `serves`, `Gov-Act:` as `made-by`, `Gov-Session:` as
`runs-in` and `Decided:` as `decides`. The trailer keys are the `[[trailer]]` rows of `edges.toml`. A
`serves` trailer is read as edges only when every comma-separated target is a well-formed address; a
value of prose, or `none`, is counted unread and is neither an edge nor a red, and `--check` prints the
count. A spec's `### Edges` block declares `consumes-from` and `hands-off` between unit ids, whose
inverses are `consumed-by` and `receives-from`; the memory hygiene check parses that block.

These lines are red: a malformed edge line, every one named in a single refusal; a type the set does
not hold; a declared inverse or a declared `cites`; a target outside its type's `To`; a pin on any
type but the two above, or one written behind `:`, `/` or `=`, or with a hash that is not eight hex
digits; a pin that matches no revision; a `promoted-from` edge anywhere but `instructions.edit`'s
change record; and a target that resolves to nothing. A `serves` id no spec defines is counted, not
red, since the hygiene check already reds it. Nothing grades an edge's source against `From`, and an
id's section (`PLAY-dOrderedCharter-24#goal`) stays `unarmed`.

- **List the set:** `python tools/playbook/edge_grammar.py --list` prints each type with its inverse,
  `From`, `To` and `Pin`, then `edges: 27 types, 26 declared, 1 derived` and the trailer keys.
- **Check a file:** `python tools/playbook/edge_grammar.py --parse memory/guides/BUILD-METHOD.md`
  prints each edge and each red, then the derived inverses or the red count. It exits 1 on a red.
- **Check the tree:** `python tools/playbook/edge_grammar.py --check` reads every site and the commit
  trailers since the compare base (`--base <rev>` names another), resolves every target, and prints one
  line per red, then the edges by type and by site. The `edges` leg of the `tags` pack runs it.
- **See it red:** `python tools/playbook/edge_grammar.py --fixture --plant outside-to` checks a planted
  `layer=kit.x` and exits 1. <!-- usage: script:tools/playbook/edge_grammar.py 71d8d8a6 -->

## The three keys

Each is set in `.governance/policy.toml` and read at the landed revision with `policy.py get`.

| Key | Values | Default | What it does |
|---|---|---|---|
| `tags.slice` | `leaf`, `subtree` | `leaf` | `show` returns the tag's row alone, or every tag with it as a dot-prefix too. <!-- usage: policy:tags.slice ab6b3cdb --> |
| `tags.retired-cites` | `refuse-new`, `warn`, `allow` | `refuse-new` | New text citing a retired tag: red, a `WARN` line, or silent. Text already at the base is never red. <!-- usage: policy:tags.retired-cites 48b48173 --> |
| `tags.bare-refs` | `charter-only`, `unique`, `never` | `charter-only` | A bare name resolves to the `practice` namespace alone; against every namespace, red where two match; or is red anywhere outside the charter. <!-- usage: policy:tags.bare-refs e06fd8cb --> |

```toml
[tags]
slice = "subtree"
```

## What it does not check

It reads no code, grades no citation under `memory/builds/`, and grades no citation into an
`unarmed` namespace; each is counted in the summary. A tag-shaped word in prose that is not in a
backticked or bracketed span is not read at all. A pending `purpose-source` whose file never lands
stays pending, printed by name on every run and never red, and a path-only source grades no member.
