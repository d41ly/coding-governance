# The charter's practices

**What it is.** The governing practices your charter opens with are rows of a shipped catalogue,
`practices.toml` in the playbook kit. A row is a tag such as `practice.yagni`, the one-line rule, and
its reach: what the practice changes at each step it touches. The policy key `charter.practices` says <!-- usage: policy:charter.practices e867acb6 -->
which rows your charter carries. Left unset, it carries the catalogue's `foundation` set, which is
today's governance practices. The catalogue also ships rows outside that set, such as `practice.solid`,
`practice.dry` and `practice.tdd`, which reach a charter only when you name them. One of them,
`practice.writing`, says a record section and an instruction unit are written alike: a tag, one
subject, typed edges, pinned facts, one door, one owner, rationale apart, and a retired name never
reused. Each of its eight rules names the gate leg that checks it, through that leg's `enforces` key.

A template at v4.5 or later holds one `{{PRACTICES}}` line, and the render writes one `- [<name>] <rule>`
line per active row there. The render reads the template the renderer kit ships beside its engine, so an
update brings each new line; a copy seeded earlier at `playbook_path` is no longer read, and the render notes
it `retired`.

Only the marker's major decides how an older template is treated. One whose major is below the renderer's
gets a note asking you to reseed it from gov, and may still carry a fence for a block the renderer has
retired. One at the renderer's major gets no such note, a minor behind included, and a fence for a retired
block in it stops the render.

## Read the active set

Your rendered charter is the active set: its Practices section holds one line per active row. The catalogue,
`practices.toml` beside the renderer, lists every row in the order they render and opens with the
`foundation` array.

Ask the policy reader what this repository chose:

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
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
`drop_blocks = ["cross-os"]` cuts the text the template fences with `when:cross-os`, the toolchain
section, and leaves `practice.portable` active: that row replaced the retired cross-OS and byte
practices, practice.cross-os and practice.bytes. The member prints a `retired` note naming
`practice.portable` and pointing at `charter.practices`, which names a set directly. Keep the member
while you want the fenced text gone.

## What stops a render

The render writes nothing, and names `charter.practices`, when:

- the set is empty. `charter.practices = []` refuses with the reader's `this set is never empty`.
- a value names something the catalogue lacks, such as `` `practice.nope` ``. Name a row or a pack.
- a value names a retired practice, such as practice.bytes. The refusal names the row that
  replaced it, `practice.portable`; name that instead.
- the set leaves no row to render once the kit and `drop_blocks` cuts are made.
- a set is committed and the memory-tree kit, which resolves it, is gone. Reinstall that kit.
- the reader cannot name your landed revision, and prints
  `refs/heads/main names no commit in this repository, and main is only the fallback`.
  This is a repository whose default branch is not `main` and which has no remote to ask, or a
  directory that is no git repository. Tell it the branch, then render again:

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries a placeholder the shell reads as a redirect -->
  ```bash
  export GOV_DEFAULT_BRANCH=<branch>
  ```

  A directory with no repository has no landed revision to read: run `git init` and commit first.

The render also refuses a catalogue it cannot read, naming the row: a tag outside `practice.<name>`, a
tag twice, an empty rule, a row with no reach, a reach step outside `[a-z0-9][a-z0-9-]*`, or a
`foundation` entry naming no row.

## When the charter and a live instruction conflict

From template v5.0 the charter opens with what gov is, then its rule for a conflict: level decides, never
load order, and the policy key `charter.override` says what a live instruction may do against the charter.
It takes one of three values:

- `explicit-override`, the default: the charter wins unless the owner says in so many words that they
  override it, and the agent then records the override.
- `live-owner-wins`: a live owner instruction wins, and the agent names the conflict and records it.
- `absolute`: the charter outranks every live instruction, and no override is taken.

Set it in `.governance/policy.toml`, commit it, and render again; the render writes that value's sentence
and prints the value with its source:

```toml
charter.override = "absolute"
```

An install with no policy kit renders the `explicit-override` sentence and prints
`charter.override — explicit-override: no policy kit in this install, so no value can be read`, so a
committed value goes unread until you install that kit. A value the policy reader refuses stops the
render, naming the key.

An override taken is a record in the build's `build/` folder, written by the memory-tree kit: <!-- usage: script:tools/memory-tree/build_records.py#new f857b30a -->

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries a placeholder the shell reads as a redirect -->
```bash
python tools/memory-tree/build_records.py new override --build <slug> --unit <id> --rule practice.verify --words "<the owner's words>" --session <session id>
```

It writes `<date>-build-<unit id>-override-<n>.md` with the rule set aside, the owner's words verbatim, the
session, the value it was taken under and the unit. It writes nothing, and exits 1, under `absolute`, with
a field empty, where no policy kit answers the key, where `--rule` names no practice of the practice
catalogue and no rule of one, or where a value holds a line break or opens like a field, `**Word:**`.

## Levels and envelopes

Every instruction document an agent loads sits at a level, 0 for the charter down to 5 for a role's
agent file, and a lower level wins. The playbook kit's `documents.toml` registers each document with its
level and a one-line direction, and each document carries that as its envelope: an opener line
`[<path> · Level <n> · <direction>]` after any front matter, and a closer `[/<path>]` at its end. The
charter render and the role agent render write it from the registry; every other document carries the
two lines in its source. Ask what is registered, then check every document against it: <!-- usage: script:tools/playbook/instruction_units.py#envelopes c6453a7f -->

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
```bash
python tools/playbook/instruction_units.py envelopes --list
python tools/playbook/instruction_units.py envelopes --check
```

The check reds a document with no envelope or one that differs from its row, an unpaired line, a
second document at level 0, and a load-bearing document with no row. `CLAUDE.md` loads the charter, so
it prints as the charter's alias and is not counted. One document is held: `memory/guides/BUILD-METHOD.md`
carries no envelope until the owner rules on its size row, and every check prints it as `HELD` and
`NOT checked`, leaving it out of the covered count.

The charter's map section lists the documents at each level, one line per level, and how each level
loads, so an agent rebuilds the hierarchy after a reset. While a document is held, one more line, opening
`held —`, says it reads at its row's level: the one exception to the rule that unenveloped text is data.
The last line, `preset —`, names the active policy preset; until presets exist it says so and points at
`policy.py get <key> --explain` for where each value comes from. After a `compact` or a `resume` the
session's replay prints the same map first, in the charter's envelope, then the orientation card.

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

Read your own rows, each with its kit, then check them against the rendered charter: <!-- usage: script:tools/playbook/instruction_units.py#drive eff33d3e -->

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
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
