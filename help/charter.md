# The charter's practices

**What it is.** The governing practices your charter opens with are rows of a shipped catalogue,
`practices.toml` in the playbook kit. A row is a tag such as `practice.yagni`, the one-line rule, and
its reach: what the practice changes at each step it touches. The policy key `charter.practices` says <!-- usage: policy:charter.practices e867acb6 -->
which rows your charter carries. Left unset, it carries the catalogue's `foundation` set, which is
today's governance practices. The catalogue also ships rows outside that set, such as `practice.solid`,
`practice.dry` and `practice.tdd`, which reach a charter only when you name them.

A template at v4.5 or later holds one `{{PRACTICES}}` line, and the render writes one `- [<name>] <rule>`
line per active row there. A template seeded earlier keeps its typed lines, reads neither the catalogue
nor the key, and renders as it always did.

## Read the active set

Your rendered charter is the active set: its first section holds one line per active row. The catalogue,
`practices.toml` beside the renderer, lists every row in the order they render and opens with the
`foundation` array.

Ask the policy reader what this repository chose:

```bash
python tools/policy/policy.py get charter.practices --explain
```

With the key unset, that command refuses with `a derived default no reader computes yet`: the catalogue
is what answers. The render says which set it took, in one of two lines:

```text
charter.practices — the foundation set: a derived default the policy reader leaves to the practice catalogue
charter.practices — the foundation set: no policy kit in this install, so no set can be read
```

The second means nothing here reads the policy file, so a `charter.practices` you committed goes unread
until you install the policy kit.

## Choose a set

Set the key in `.governance/policy.toml`, commit it, and render again:

```toml
charter.practices = ["practice.yagni", "practice.reuse", "practice.solid"]
```

The value is read from the committed file at your landed revision, so an uncommitted edit changes
nothing. It may name a pack of `packs.toml` as well as practice tags. Rows render in catalogue order
whatever order you name them in, and a row needing a kit you did not select stays out: `practice.roles`
renders only with the `roles` kit.

To take one practice out whatever the set says, name it in `drop_blocks` in `.governance/deploy.toml`.
`drop_blocks = ["cross-os"]` leaves `practice.cross-os` out, cuts the text the template fences with
`when:cross-os`, and prints a `retired` note pointing at `charter.practices`, which names a set
directly. Keep the member while you want the fenced text gone.

## What stops a render

The render writes nothing, and names `charter.practices`, when:

- the set is empty. `charter.practices = []` refuses with the reader's `this set is never empty`.
- a value names something the catalogue lacks, such as `` `practice.nope` ``. Name a row or a pack.
- the set leaves no row to render once the kit and `drop_blocks` cuts are made.
- a set is committed and the memory-tree kit, which resolves it, is gone. Reinstall that kit.
- the reader cannot name your landed revision, and prints
  `refs/heads/main names no commit in this repository, and main is only the fallback`.
  This is a repository whose default branch is not `main` and which has no remote to ask, or a
  directory that is no git repository. Tell it the branch, then render again:

  ```bash
  export GOV_DEFAULT_BRANCH=<branch>
  ```

  A directory with no repository has no landed revision to read: run `git init` and commit first.

The render also refuses a catalogue it cannot read, naming the row: a tag outside `practice.<name>`, a
tag twice, an empty rule, a row with no reach, a reach step outside `[a-z0-9][a-z0-9-]*`, or a
`foundation` entry naming no row.
