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

Only the marker's major decides how an older template is treated. One whose major is below the renderer's
gets a note asking you to reseed it from gov, and may still carry a fence for a block the renderer has
retired. One at the renderer's major gets no such note, a minor behind included, and a fence for a retired
block in it stops the render.

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

## Levels and envelopes

Every instruction document an agent loads sits at a level, 0 for the charter down to 5 for a role's
agent file, and a lower level wins. The playbook kit's `documents.toml` registers each document with its
level and a one-line direction, and each document carries that as its envelope: an opener line
`[<path> · Level <n> · <direction>]` after any front matter, and a closer `[/<path>]` at its end. The
charter render and the role agent render write it from the registry; every other document carries the
two lines in its source. Ask what is registered, then check every document against it:

```bash
python tools/playbook/instruction_units.py envelopes --list
python tools/playbook/instruction_units.py envelopes --check
```

The check reds a document with no envelope or one that differs from its row, an unpaired line, a
second document at level 0, and a load-bearing document with no row. `CLAUDE.md` loads the charter, so
it prints as the charter's alias and is not counted. One document is held: `memory/guides/BUILD-METHOD.md`
carries no envelope until the owner rules on its size row, and every check prints it as `HELD` and
`NOT checked`, leaving it out of the covered count.

## The drive section

The charter's `## Drive — how to start and advance the loop` section says how a session starts, by
situation, and which command advances each stage of the loop for each role. It is composed, never typed:
each kit's descriptor, `kit.toml` in its directory or the flat entry's own descriptor, may carry `[[drive]]`
rows, each a `stage`, a `role`, a `command` and a `when`:

```toml
[[drive]]
stage = "build"
role = "gov-builder"
command = "python <prefix>/roles/handoff.py render --role gov-builder --build <slug> --unit <id>"
when = "a unit whose spec is READY"
```

`stage` names a workflow of the roles kit's `workflows.toml`, or `start` for how a session begins; `role`
is a role slot, or `main` for the main session. Where your template holds a `{{DRIVE}}` line, as gov's
does, the render writes one line per row of the kits your `.governance/deploy.toml` selects there: the
`start` rows first, then by the workflow's stage, then kit and row order. A kit you did not select adds
nothing, and a selection with no rows renders no section. A subagent's handoff carries its own role's
lines under `### Drive`, so it holds the line the main session does.

Read your own rows, each with its kit, then check them against the rendered charter:

```bash
python tools/playbook/instruction_units.py drive --list
python tools/playbook/instruction_units.py drive --check
```

The check reds a row whose stage, role or other field is wrong or empty, a role of the workflow list
no row names, a line in the charter's drive region no row renders, a row whose line the region lacks,
and a flat entry whose descriptor the playbook kit does not ship beside the renderer. A render refuses,
naming the kit, when a selected kit's descriptor is found neither beside the renderer nor in gov's tree.

## Raising a charter cap

A run's raise of a charter cap is owed only under the four conditions the header of
[the size limits file](../tools/template-size-limits.txt) states, argued in place above the row as
`RAISED <old> -> <new>` with a `memory/DECISIONS.md` row in the same commit, the change record
`cl-dClosedLoop-0012` names for this build; once a row is under `budgets.*`, the raise goes through the
one write shape the minimal guard admits, as
[who may change the policy file](policy.md#who-may-change-the-policy-file) states. Whatever the cap, the
size gate refuses a cap on `AGENTS.md` above the smallest harness's limit, Codex's `CODEX_MAX`.
