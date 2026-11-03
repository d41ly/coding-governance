# Tags and the resolver: `gov tag`

**What it is.** A tag names one thing in the repository: `doc.build-method` is the build method
guide, `doc.build-method#m5-recall-and-reuse` its `## M5` section. A tag is `<ns>.<seg>(.<seg>)*`,
lower-case, at most 64 bytes, and its namespace is a row of `tools/playbook/namespaces.toml`. Ten
namespaces are registered today, each read from the file that declares its members:

| Namespace | Its members come from |
|---|---|
| `doc` | the charter, each guide under `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`, one section per `##` heading |
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
`<git-common-dir>/gov/index.db`: one SQLite file per machine that every worktree shares, built on
first use, never committed. A commit re-parses only the files it changed, and a worktree's
uncommitted edits are served to that worktree alone. Deleting the file costs one rebuild.

## How to use it

- **Find a tag:** `python tools/playbook/gov_tag.py where doc.build-method` prints
  `tags: memory/guides/BUILD-METHOD.md:1`. A positional label works too, through
  `tools/playbook/aliases.toml`: `python tools/playbook/gov_tag.py where "BUILD-METHOD M5"` prints the
  line of `## M5`. <!-- usage: script:tools/playbook/gov_tag.py#where 9a2511d8 -->
- **Read it:** `python tools/playbook/gov_tag.py show doc.build-method#m5-recall-and-reuse` prints the
  section's lines. <!-- usage: script:tools/playbook/gov_tag.py#show 09500daf -->
- **See who cites it:** `python tools/playbook/gov_tag.py refs doc.build-method` prints `path:line`
  for every citation, a build record's included. <!-- usage: script:tools/playbook/gov_tag.py#refs c503761e -->
- **Check the tree:** `python tools/playbook/gov_tag.py check` runs the checks below; the `tags` leg
  of the merge bar runs the same command. `--base <rev>` names the revision new text is measured
  against; without it the merge bar's compare base is used. <!-- usage: script:tools/playbook/gov_tag.py#check 5c4c67e4 -->
- **Rebuild, list, plant:** `python tools/playbook/gov_tag.py --rebuild` rebuilds the index from
  nothing; `python tools/playbook/gov_tag.py --list-positional` prints one `<path>` TAB `<ref>` row
  per positional reference, the rows `tools/playbook/positional-refs.txt` keeps; and
  `python tools/playbook/gov_tag.py --fixture --plant scope` runs one planted case in a scratch
  repository. <!-- usage: script:tools/playbook/gov_tag.py b39584ac -->

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
  itself a namespace word, such as `practice.repo.x`.
- **join** — a citation that is no member of its namespace, such as `` `layer.nowhere` ``; and, once
  unit rows exist, a `reader` or `practice` member no unit selects. A describing namespace's unused
  members are listed, never red.

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
backticked or bracketed span is not read at all.
