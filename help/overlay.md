# The instruction overlay

Your repository's own instructions live in one file, `.governance/instructions.toml`. Gov's units ship
in each kit's manifest and are overwritten at every update; the overlay is yours, and it is how you add
a rule, change or replace one of gov's, drop one, or declare a policy key of your own.

## Add a unit

A `[[unit]]` row in the kit manifests' row grammar, its tag in the `repo.` namespace. It renders by its
`level`, its `scope` (which documents select it) and its `trigger`, after gov's units at the same level.
Levels 1, 6 and 7 are refused: the repository writes neither the card, the task nor memory.

```toml
[[unit]]
tag = "repo.verify-staged"
level = 3
type = "directive"
scope = ["reader.every"]
trigger = "before every pass commit"
text = "MUST verify against the staged bytes."
```

## Amend or replace one of gov's units

Give your unit an `edges` entry naming gov's unit, pinned to its text as `<tag>@<hash8>`; `python
tools/playbook/instructions_edit.py list` prints each gov unit's pin.

- `amends=<tag>@<hash8>` renders your unit right after gov's, which keeps rendering.
- `supersedes=<tag>@<hash8>` renders your unit in gov's unit's place.

## Exclude one of gov's units

List its tag in `instructions.exclude` in `.governance/policy.toml`:

```toml
[instructions]
exclude = ["unit.some-rule"]
```

## What you cannot change

A fixed unit refuses all three. A gov unit is fixed when it is a `principle.` unit, when its `fixed-by`
names a source that resolves (`principle=<tag>`, `floor=<tag>`, `parser=<path#symbol>`), or when it
declares no class. It is open only when it declares `class = "open"` and nothing fixes it. A refusal
names the unit and the source that fixes it.

## Declare a key of your own

A `[[policy]]` row declares a key under `adopter.`, its closed `values`, its `default`, a `summary` and
a `usage`. Set its value under `[adopter]` in `.governance/policy.toml`, and read it with `python
tools/policy/policy.py get adopter.<name>`. A key outside `adopter.` is refused, so the overlay never
redeclares one of gov's keys. A repository unit reads the key in its `trigger` as
`policy.adopter.<name>.<value>`, and composes only while the key holds that value.

```toml
[[policy]]
key = "adopter.release-train"
values = ["weekly", "monthly"]
default = "weekly"
summary = "how often this repository cuts a release"
usage = "set [adopter] release-train in .governance/policy.toml"
```

Changing the overlay stales the policy mirror `.governance/policy.json`, since it records the overlay's
blob; the landing regenerates it.

## When gov changes a unit you pinned

Every change gov makes to a unit carries a change record marked `editorial` or `semantic`. `editorial`
is admitted only where the change is mechanical: whitespace, punctuation, or a respelling gov's
`spelling-map.toml` declares, or where the record carries the owner's ruling with its proof. A record
marked `editorial` over a change of meaning is refused, naming the record, the unit and the first word
that differs. At each `update` your pinned edges are walked from the pin to gov's current text:

- behind editorial records only, the edge stands and nothing is said beyond its `amended` or
  `replaced` line;
- behind a `semantic` record, the edge is `stale`;
- a unit gov renamed re-points your edge to the new tag, its pin kept;
- a unit gov split or retired orphans your edge: an orphaned `amends` stops rendering, an orphaned
  `supersedes` renders alone as your unit.

What a stale edge does is yours to choose with `instructions.stale` in `.governance/policy.toml`, read
at your HEAD:

```toml
[instructions]
stale = "warn"
```

- `order`, the default: gov's new text and your unit both render, and `update --write` writes an order
  `.governance/outbox/update-unit-<slug>.md` naming the edge, gov's old and new text, and the command
  that re-pins it.
- `refuse`: the update writes nothing and exits 1, naming each stale or orphaned edge, until you re-pin.
- `warn`: both render, the edge is printed, and `update --write` appends one line to
  `.governance/journal/stale-edges.tsv` with no order.

An orphaned edge files an order under `order` and `warn` alike. The update also lists, as `new-beside`,
each unit gov added at a level and a selection one of your units holds, so you can see whether yours
still says something gov does not. Re-pin an edge through `instructions_edit.py edit --manifest overlay
--tag <your tag> --edges amends=<gov tag>@<hash8>`.

## Check it

`python tools/playbook/overlay.py check` prints each gov unit's class, each of your keys with its tag
`policy.adopter.<name>`, and each gov unit's state (`unchanged`, `amended`, `replaced` or `excluded`),
and exits 1 naming every refusal.

The overlay is a guarded file: write it at your terminal, or through `instructions_edit.py add
--manifest overlay`, which keeps the rows ordered by level then tag.
