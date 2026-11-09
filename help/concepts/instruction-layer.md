# The instruction layer

Everything an agent is told comes from instruction units placed on one ladder, composed with your
repository's own units, and rendered into the documents an agent loads. This page explains the four
parts and links the reference pages rendered from the registries that define them.

## The ladder

Every instruction sits at a level, 0 to 7, the one term for where an instruction sits on the ladder.

| Level | Name | What sits there |
|---|---|---|
| 0 | charter | the charter |
| 1 | card | the build's card |
| 2 | loop | the loop and the policy values |
| 3 | methods | methods, protocols and templates, and reuse entries |
| 4 | runbooks | runbooks, Skills and path rules |
| 5 | role | the role's static instructions |
| 6 | task | the task |
| 7 | records | records and memory, evidence only |

The harness's own instructions sit above the ladder and hold no level.

## Units

A unit is one `[[unit]]` row of a kit's `instructions.toml`: its tag, its level, its type, the documents
its `scope` selects, its `trigger`, its `text`, and a `usage` where a user acts on it. Gov's units ship
in each kit and are overwritten at every update. A kind of extension, such as a unit, a Skill or a
charter practice, is a row of the kinds register; [the kinds page](../reference/kinds.md) lists each kind
and how a member of it is made.

## The overlay

Your repository's own units live in one file, `.governance/instructions.toml`, read at your last commit.
A unit there adds a rule, amends or replaces one of gov's, and a policy value excludes one. See
[the instruction overlay](../overlay.md) for the rows, and [change a gov rule](../tasks/change-a-gov-rule.md)
for the commands. Every policy key a unit or a gate reads is on [the policy page](../reference/policy.md).

## Composition

The charter renderer composes gov's units and yours into each document, places your level-0 units in the
charter's own rules section and your level-3 to level-5 units where a unit slot selects them, measures
each document against its cap, and prints a delta report naming what each unit did. See
[composition](../composition.md). The charter's drive section, the commands that start and advance the
loop, is rendered from the selected kits' drive rows; [the drive page](../reference/drive.md) lists each
stage and role. [Adopt gov](../tutorial/adopt-gov.md) walks the whole path once in an empty repository.

## The reference pages

The pages under `help/reference/` are rendered, never written by hand, each from the registry row that
defines what it documents, so a page cannot say something its row does not. In gov's checkout,
`python tools/playbook/render_playbook.py --reference` writes them, and
`python tools/playbook/render_playbook.py --reference --check` exits 1 naming each page that differs from
its render. <!-- usage: script:tools/playbook/render_playbook.py 915d9434 -->

Each page is declared by one row of `tools/playbook/references.toml`, naming the registry, the reader
that returns its rows and the page. A row lacking a summary or a usage stops the render, but on the
policy page, which lists such keys under `Not yet summarised`. To change a reference page, change the
registry row and render again.
