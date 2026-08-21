# playbook mode — the `recipe` authorization discipline and its validity gate

```toml
feature = "playbook-mode"
title = "A third authorization mode for repeatable content, and the playbook it follows"
status = "building"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = ["playbook validity gate", "playbook validity selftest"]
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = ["PLAYBOOK-TEMPLATE.md"]
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/unattended/check-playbook.sh",
  "tools/unattended/check-playbook.test.sh",
  "tools/unattended/PLAYBOOK-TEMPLATE.template.md",
  "tools/unattended/playbook.fixture.md",
  "tools/unattended/fixture-pieces/",
  "tools/unattended/fixture-records/",
]
```

## Constraints & why

**The mode is `recipe`; the artifact is a PLAYBOOK.** Two nouns for two things. The mode names the
authorization discipline, exactly as `slug` and `prompt` do without naming any artifact; the playbook
names the document a `recipe`-mode run follows. `playbook` was rejected as the mode value because it
collided with the `DISCIPLINES` enum, the `PLAY` family and the charter-renderer kit — none a machine
collision, but four unrelated subjects answering one grep.

**The population is TREE-DERIVED, never seam-derived.** A tracked file is a playbook when it carries
the declaration block. Defining it as "what the build README's `playbook:` names" was the first cut
and it excluded three things at once: the fixture this kit ships, a freshly authored playbook no
README names yet, and the rule that a tracked playbook is graded from the moment it is tracked.

**The canon is DERIVED from the shipped template's own section table**, and the self-test proves it by
removing a row and asserting the leg demands one fewer. A canon spelled in both the template and the
checker is two answers to one question, and the checker is the copy that rots.

**The template is NOT in the population.** Its declaration block is a specimen with empty values;
grading it reds on every field it deliberately leaves for an author. Found by running the predicate
over the real tree before wiring it, which is the rule that exists for exactly this.

**A section's NAME is the canon; its number is cosmetic.** Coupling the two was the first cut, and
this leg's own self-test caught it: shrinking the canon by one row would then have forced every
playbook in every adopter to renumber, and a canon change that rewrites its subject is the shape a
derived vocabulary must not have.

**An empty PLAYBOOK population REDS; an empty PIECE population does not.** The leg carries this mode's
whole enforcement, so printing `GATE ok` over no playbooks is the green-by-absence class by name.
A zero-piece enumeration is a different fact — the reader classifies and never grades, and only
`--close` blocks on it. The two rules were one rule in the first cut, which either red the dogfood bar
permanently or re-opened the hole.

## What this gate does NOT check

Its own header carries this, and it is repeated here because a structural check reads as a semantic
one to everybody who did not write it: whether a `CHECK`'s stated reason is true, whether a `GATE`'s
named leg tests what its step says, whether a step followed in letter was followed in spirit, and
whether the playbook is right about its subject. The witness drain census is the only quantitative
handle on the third, and it REPORTS rather than reds so a playbook can adopt the witness a step at a
time instead of in one migration.

## Shared seams

The leg reads `git ls-files`, so it grades TRACKED files only — staging is a precondition, which is
the same trap the memory-hygiene gate records. The adopter installs the template as a third artifact
beside the Skill and the protocol, copied rather than rendered because it carries no placeholder.

## Reuse affordance

seam: `check-playbook.sh` canon derivation — reuse for any gate whose vocabulary must come from a
  shipped document rather than a constant; extend via the template's section table, which is the one
  place the canon is written.
seam: the leg's staged-break self-test — reuse for any new gate; extend via `probe`, which asserts
  BOTH the check number and the branch message, so a wrong arm firing and a drifted message are
  distinguishable failures rather than one green.
seam: the tracked FIXTURE pattern — reuse for any leg whose population can legitimately be empty in
  the repo that ships it; extend by shipping one conforming instance so the empty-population refusal
  is a real state rather than the ordinary one.

## Gaps

- The leg grades SHAPE only, and its header enumerates the four semantic questions it cannot reach.
- The scope refusal (unit 8) cannot evaluate on the attended entry point at all: both its inputs, the
  recorded mode and the run's commit set, exist only through the driver.
- The per-piece RECORDS ROOT is declared by the playbook, not by the kit. Found by building: the
  spec put these under the build folder, and the memory-tree gate refuses both a new subdir there and
  a new top-level directory — its structure is closed and owned by another kit. A piece record is
  evidence about CONTENT and belongs with the project that owns the content.
- `PLAYBOOK_GLOB` is read from the conf and is not yet used to widen the population — a playbook that
  carries no declaration block is invisible, which is intended for now and is the reason the block is
  what defines membership.
- Units 5 through 8 and 10 are specced and unbuilt, so the piece-level halves this leg is designed to
  carry — the record reader, the piece count, the set checks, the scope refusal — are absent. The leg
  is honest about its population today and will grow.
