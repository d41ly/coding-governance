# The docs leg

**What it is.** The `docs` leg keeps the pages under `help/` current with the surfaces they
document. Each user-facing member's usage is a declared row: a CLI verb and its flags, a key with
its values and default, a hook's event and matcher, a reference row's summary and usage. The page that documents a member carries that
row's fingerprint in an anchor. When the row moves and the page does not, the leg reds the landing.
It also tests each command a page shows against the rows, and checks each relative link offline.

The leg is `<prefix>/govkit/docs_leg.py`, which is `tools/govkit/docs_leg.py` in this repository.
It grades gov's own pages against gov's own members, and it never travels into an adopter.

## How to use it

- **Run it:** `python tools/govkit/docs_leg.py` prints the mode line, `docs: help.enforce = <value>`
  with where the value came from, then one summary line and one line per finding. <!-- usage: script:tools/govkit/docs_leg.py 68cabb59 -->
- **See every row and its page:** `python tools/govkit/docs_leg.py --list` prints each member and
  `script:` row with its shape, its fields and the page that anchors it, or `listed`. With
  `--undocumented` it prints only the ids no page anchors, one per line.
- **See it red:** `python tools/govkit/docs_leg.py --fixture --plant stale-page` builds a scratch
  repository, changes one row and leaves its page alone, and exits 1 with a `docs: STALE` line.
  `--enforce warn` or `--enforce off` grades the same fixture under the other modes; it is honoured
  under `--fixture` only.
- **Run every page command:** `python tools/govkit/docs_leg.py --run` runs each fenced `bash`, `sh` and
  `console` block of every page under `help/`, in order, in one fresh scratch repository per page, with
  `GOV` set to this checkout and the scratch repository as each command's working directory.
  `--page <path>` runs one page. It prints each block marked `run: no` with its reason, then a summary of the
  commands run and the blocks marked, and a `docs: RUN` line naming the page, the line and the command
  for each command that exits other than its block declares.
- **Read the fingerprints:** `python tools/govkit/docs_leg.py --fingerprints` prints one line per row,
  its id, its fingerprint and the pages anchoring it, tab-separated, `-` for none. The reference pages
  under `help/reference/` take their anchors from it.

## What it reds

- `STALE` — an anchor whose fingerprint is not the one its row has now. The line names the page, the
  id, the fingerprint the page holds and the one the row has.
- `COMMAND` — a page command whose verb is not declared for its script, or a `--flag` that is not
  declared for that verb.
- `UNROWED` — a page command whose script is tracked and has no row and no list row.
- `RUN` — under `--run`, a page command that exits other than its block declares: 0, or the code an
  `<!-- expect: <code> -->` line directly above the block states.
- `LINK` and `FRAGMENT` — a relative link to no tracked path, or a `#fragment` that is no heading
  or `<a id>` of its page. An `http` or `https` link is counted and never fetched.
- `UNDOCUMENTED` — a member no page anchors and the list does not name. `DRAINED` — a list row for a
  member a page now anchors. `GROWN` — the list holds more rows than its low-water.
- `ORPHAN` — an anchor or a row naming nothing. `TWICE` — a member anchored in more than one place.
  `RESTATED` — a `[[usage]]` row for a member whose own registry states its usage. `CLASS` — a class
  of the step gate's registry with no `[[class]]` row, or a row that does not fit its shape.

A shaped class with no member, pages whose commands none was tested, or a declaration that will not
read is not a verdict: the leg exits 2 and says why.

## How to answer a stale page

Read the line: it prints the fingerprint the row has now. Update the page's prose for the change,
then put that fingerprint in the anchor. An anchor is an HTML comment, invisible on the page:

```text
<!-- usage: <id> <fingerprint> -->
<!-- usage: <id> -->
```

The second form is for a member graded for presence only, a role agent or a registry entry. Each
member is anchored on exactly one page. A member no page documents yet is a row of
`memory/project/docs-undocumented.txt`, `<id>` and a reason separated by a tab. The list only
shrinks: the commit that documents a member removes its row, and a new member must be documented.

## `help.enforce`

`help.enforce` in `.governance/policy.toml` says what a finding does. <!-- usage: policy:help.enforce 900c96e8 -->

| Value | What the leg does |
|---|---|
| `refuse` | the default: any finding exits 1, so the landing is refused |
| `warn` | each finding prints as a `docs: WARN` line and the leg exits 0 |
| `off` | the leg prints its mode line, reads nothing else and exits 0 |

The leg reads the key once, at the landed revision, so a branch's own edit of the policy file
does not relax the leg that grades it.

## How a later class joins

The classes are the step gate's (see [the step gate](step-gate.md)). A class that joins there adds
its `[[class]]` row to `tools/govkit/usage.toml` in the same landing, naming its usage shape. Where
its registry already states each member's usage, its `rows` names a reader over that registry,
`<path under the tool root>:<function>`, and no `[[usage]]` row restates it. Where nothing states
it, `rows` is `usage.toml` and each documented member gets a `[[usage]]` row there.

## Marking a block the run arm cannot run

A block that cannot run in a scratch repository, because it runs a kit by its path in gov's checkout or
carries a placeholder, takes one line directly above its fence:

```text
<!-- run: no — <reason> -->
```

The run arm prints the reason and counts the block, and never reads it as run. A run in which no page
shows a runnable command is not a verdict: the arm exits 2.

## What it does not check

Prose: an anchor whose fingerprint is current over a paragraph that is wrong passes. The default run
runs no page command, `--run` runs no block marked `run: no`, neither fetches an external link, and the
`file` and `installable` classes have no usage shape.
