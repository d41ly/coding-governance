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

## The verb set, and why it is one line

The driver's verbs were spelled in five places and three were stale on the day unit 9 landed —
`--record-set` had shipped into the dispatch alone. The fix is not a re-synchronisation, which is
what the previous fix was and it lasted exactly one verb. `VERBS_SLUG` is now READ by the dispatch,
so a verb missing from it does not read wrong, it does not run; refusal 14 renders from that
declaration; and the usage text renders from the header docstring, which is the only place a verb's
ARGUMENTS are spelled. The two carriers in other files — the protocol's verb section and the Skill's
invocations — are joined to the declaration by leg check 22, because no runtime derivation crosses a
file boundary.

The same shape one level down: `PARK_KINDS` is the parked-region vocabulary, the `--status`
alternation is derived from it, and check 23 joins it to the `park()` call sites in BOTH directions.
The reverse direction is not theoretical — this kit declared a DECISION kind that no verb wrote for
as long as its contract had instructed runs to park one.

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
- The output-scope refusal (unit 8) is WITHDRAWN, not deferred. It found two real defects — the globs
  were read from the wrong blob so every run reached the no-globs branch, and
  `git diff --name-only --first-parent -m` silently ignores both flags while its comment claims a
  first-parent walk — and both are fixed and recorded. What could not be done is fire its hermetic
  arm, and a check whose failing case nobody has observed is an assertion about nothing. It is also
  unevaluable on the attended entry point by construction: both its inputs, the recorded mode and the
  run's commit set, exist only through the driver.
- `--propose` requires a run-state file, so the ATTENDED path has no proposal channel. The same
  asymmetry was solved for the piece record by giving its writer a second caller; it was left here
  deliberately, because an attended run has an owner in the loop and can say the thing.
- The per-piece RECORDS ROOT is declared by the playbook, not by the kit. Found by building: the
  spec put these under the build folder, and the memory-tree gate refuses both a new subdir there and
  a new top-level directory — its structure is closed and owned by another kit. A piece record is
  evidence about CONTENT and belongs with the project that owns the content.
- `PLAYBOOK_GLOB` is read from the conf and is not yet used to widen the population — a playbook that
  carries no declaration block is invisible, which is intended for now and is the reason the block is
  what defines membership.
- Unit 10 is specced and unbuilt: the Skill's routing preamble with its four start paths, and the two
  playbook-scoped directives. A reader arriving with no playbook reaches the creation section by
  reading the Skill in order rather than by being routed there.
- **A run authoring BOTH its own build folder and its own playbook, under `published`, is refused by
  nothing.** Measured while building unit 11, against a spec sentence claiming the opposite in a wider
  form. `resolve_base` reaches the second anchor only when the build README fails to resolve at the
  merge-base, so the ordinary case keeps its refusal and the both-halves case does not. The protocol
  records the reach and the Skill states the CHECK; there is no machine half for that one state.
