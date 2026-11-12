# Overlay rows — changing one of gov's structured rows

Gov ships structured rows as well as instruction units: a kind the kinds register lists with a `schema`
(`tools/playbook/kinds.toml`) has rows your repository may add, amend, replace or exclude. You do it the
way you change a unit (see [the instruction overlay](overlay.md)): from your own row in
`.governance/instructions.toml`, never by editing gov's row, which the next update overwrites.

No real kind registers a schema yet; the mechanism ships dark, proven on a fixture kind, and each kind's
own build arms it. The examples use a kind `fixture` whose schema declares the open set fields `grants`
and `needs`, the open scalar `ceiling`, and its owner seat at segment 1.

## Your own tag

A row of yours is tagged with `adopter` at the seat the kind's schema declares (`owner-seat`), for
example `fixture.adopter.extra`, so it never collides with a gov tag. Gov's packs never ship that seat,
and a row of yours without it is refused under `owned`. You never write `origin`: every row read from
the overlay is the repository's, and a row typing `origin` is refused.

## Add a row

A `[[<kind>]]` table holding `tag` and the fields the schema declares; any other key is refused.

```toml
[[fixture]]
tag = "fixture.adopter.extra"
grants = ["read"]
ceiling = "low"
```

## Amend one of gov's rows

`edges = "amends=<tag>@<hash8>"` names gov's row and patches only the fields you name. A set field takes
`add` and `remove` lists; a scalar takes its new value. Every other field stays gov's as shipped.

```toml
[[fixture]]
tag = "fixture.adopter.alpha-tuned"
edges = "amends=fixture.alpha@1a2b3c4d"
add = { grants = ["write"] }
remove = { needs = ["fixture.beta"] }
ceiling = "high"
```

`add` or `remove` naming a scalar or an undeclared field is refused, naming the field.

## Replace one of gov's rows

`edges = "supersedes=<tag>@<hash8>"` puts your whole row in gov's place: it answers to gov's tag, so
every row naming gov's tag resolves to yours.

## Exclude one of gov's rows

List its tag in `instructions.exclude` in `.governance/policy.toml`, the same key that excludes units:

```toml
[instructions]
exclude = ["fixture.beta"]
```

The row is absent from the composition and its state reads `excluded`. A listed tag no gov row holds is
refused.

## Pins

A pin is the first eight hex digits of a hash over the row's canonical form: its fields as JSON, keys and
set values sorted, each string's whitespace folded. Reordering gov's keys or re-wrapping a string does
not move it. A pin with no `@`, one that is not eight hex digits, and one matching no revision of gov's
row are each refused.

## When gov changes a row you pin — instructions.stale

Gov's change records say whether each change to a row was `editorial` or `semantic`. Behind editorial
records only, your pin stands and nothing flags. A renamed row takes your edge with it, keeping the pin;
a split or removed row orphans it: an orphaned amendment is held out, an orphaned replacement runs on
its own, and each files an order. Behind a semantic record the edge is stale, and the
`instructions.stale` policy key decides what update does:

- `order` (the default) applies your patch over gov's new row and files an order to review it;
- `warn` applies it, prints the stale edge and journals it in `.governance/journal/stale-edges.tsv`,
  filing no order;
- `refuse` holds the update until you re-pin the edge with `instructions_edit.py`.

Under `order` and `warn`, a patch that no longer applies (gov's new row lacks a field you patch) is held
and gov's row runs as shipped, the order or the warning naming the field.

Each gov row's state is one of `unchanged`, `amended`, `replaced`, `excluded`, `stale` and `orphaned`.

## What you may not change, and how a widening is reported

A kind's schema says, field by field, what your rows may touch. A field is **open** when it declares
`widens`, the direction that widens it: `add` on a permission set such as `grants`, `remove` on a
constraint set such as `needs`, or an ordered list on a scalar such as `ceiling = ["low", "mid", "high"]`,
where a later value is wider. Every other field is **fixed**: one whose `fixed-by` names what fixes it (a
principle, a floor item, or a parser of gov's tools), and one that declares neither, which reads fixed
by default. A schema may also list whole fixed rows under `[[fixed-row]]`. Nobody types the class: a
schema writing `class` is refused.

Update refuses the composition, naming the row, the field and what fixes it, when your overlay:

- amends a fixed field, whether or not gov's row ships it;
- amends or supersedes a fixed row, the refusal saying `a widening` when the patch would widen it;
- supersedes a row with a fixed field changed or dropped;
- excludes a fixed row;
- sets an ordered scalar to a value outside its order.

An exclusion is also refused while something still relies on the excluded tag: another active row of any
kind holding it in a field whose schema `ref` role is `needs`, `actor` or `grants` (the refusal names the
row and the field), or a tag-valued policy key naming it, such as `roles.harness.builder` (the refusal
names the key). Take the tag from that row or key first, for example with an `amends` whose `remove`
drops it from `needs`.

Every patch operation the composition applies is classified `widens` or `narrows` from the field's
declared direction alone; a value equal to gov's is no operation. Where gov's own value sits outside
the field's order, any listed value reads `widens`. The composition lists each widening with its row,
field, operation and gov's value, the one list the update's delta report prints, so what your
repository widened is never a guess.
