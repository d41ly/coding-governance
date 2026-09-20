# TOOL-dDerivedDocket-51 — an admitted example family for the kit's scratch fixtures

**Status:** SPECCED · rev-1 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 14

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The id grammar is an allowlist of the conf's declared families, and the example ids this corpus
writes into fixtures sit in a family no conf declares, so a criterion asserting that a generated
build README anchors nothing is true before the generator writes a line and its stated break cannot
fire. Give the kit's scratch fixtures a conf that declares the example family, so a fixture id is
anchorable inside the fixture and still inert in the tracked corpus, and pin the arm to a staged RED
that proves it.

## 2. Scope (IN)

- **S1** — `EXAMPLE_ROW`, a module constant in `tools/memory-tree/gen_build_index.py` holding the
  one `<discipline>:<FAMILY>` pair the kit's scratch fixtures may declare, and the matching
  discipline token. One carrier, because the pair is written into a conf in two fields and two
  spellings of one value is how they stop agreeing. Observed by AC1.
- **S2** — the opt-in on the fixture helper. `_fixture` (`tools/memory-tree/gen_build_index.py:1911`)
  takes a keyword argument, default OFF, that adds S1's pair to the `DISCIPLINES` and `FAMILIES`
  values it writes into the scratch `.memory-tree.conf` (`:1915-1916`). Default OFF is the whole
  blast-radius answer: every arm that does not ask for it keeps the conf it has today, so no
  existing roster, alternation or enum verdict moves. Observed by AC2 and AC6.
- **S3** — what the declaration buys, in one fixture, stated as the three readers it unblocks: the
  roster refusal (`:788`) and the streams refusal (`:785`), which reject a scaffolded README whose
  values are outside the declared sets, and the conf-bound id alternation, which is rebuilt per root
  by the accessor `TOOL-dDerivedDocket-50` routes to. Observed by AC3 and AC4.
- **S4** — the staged RED, written into the criterion rather than only performed once. Unit 15's
  AC13 gains a `new arm:` clause requiring the arm to have been observed RED over a generated body
  line the fixture's own grammar anchors, in the shape this build already uses at unit 28's AC13 and
  unit 19's AC11. That spec's header rev bumps and its §9 gains the entry, in this unit's commit.
  Observed by AC4 and AC5.
- **S5** — the two-tree property, asserted rather than assumed: the example family is declared by a
  scratch conf and never by this repository's own, so an example id written into a tracked spec or
  record still anchors nothing and check 13's cited-id population does not grow. Observed by AC7.
- **S6** — the carriers, and what they do NOT move. `memory/map/generated/` is re-derived and staged
  in the same commit as the `.py`, because the pre-commit fast leg runs the codebase-map gate
  whenever a `.py` is staged and refuses a stale or unstaged artifact. It is expected back
  BYTE-IDENTICAL, and that is a measurement rather than a hope: the Python extractor records public
  module-level `def` and `class` nodes plus statically-listed `__all__` names and nothing else
  (`tools/codebase-map/map_lib.py:342-351`), no memory-tree module declares an `__all__`, and this
  unit's two carriers are a module CONSTANT and a keyword on a PRIVATE helper. Neither is a symbol
  the map can see. Observed by AC8.

## 3. Non-goals (OUT)

- **This repository's own `FAMILIES`.** `.memory-tree.conf:15` is not touched. An example family
  declared there would make every example id in every tracked spec an anchored record, which is the
  opposite of what the example family is for, and check 13 and check 14 would then count them.
- **The other kits' scratch confs.** `corpus_ids.py`'s own `_scratch` writes its own conf
  (`tools/memory-tree/corpus_ids.py:768`) and keeps it: its arms assert an exact defined-id set, and
  widening the alternation under them would change what they measure while their assertions stayed
  still. The same holds for the memory-hygiene self-test's scratch trees.
- **A general rule for every negative criterion.** The standing shape — a criterion asserting a
  population is EMPTY must be seen RED over a member that could have entered it — is the G3 record's
  left-shift class, and it reaches specs this unit does not own. This unit writes it into the one
  criterion the finding names. A sweep over the other groups stays a review class.
- **The route.** How the kit reaches the anchor predicate at all is the previous unit's question.
  This unit decides only which ids that predicate can see inside a fixture.
- **The kit version.** This unit moves no version marker. `TOOL-dDerivedDocket-36` moves
  `KIT_MEMORY_TREE_VERSION` once for this build and these bytes ride that move.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-50` — the root-bound anchor route. The accessor that unit
  adds resolves the grammar against an EXPLICIT root, which is what makes a scratch conf's families
  the ones an arm is graded by; without it the predicate binds to the repository the kit is
  installed in and this unit's declaration is read by nobody.
- **hands-off** `TOOL-dDerivedDocket-15` — the fixture its AC10 and AC13 run over. The scaffold
  writes a README whose roster and streams come from the asks' families, so `EXMP-aFoo-3` needs a
  fixture conf that declares that family before `gen_build_index.py` will accept the README it just
  wrote, and AC13's `anchor_at` assertion needs it before the criterion can fail at all.

## 4. Design

### What the grammar admits, and why the example family is outside it

The id alternation is built from the conf's declared families and nothing else
(`tools/memory-recall/extract.py:68` and `:106`), and the four anchor patterns are compiled from
that alternation (`:116-121`). The allowlist is deliberate: a bare two-to-eight capital run also
matches `AC`, `WU`, `JSON` and a dozen other tokens that outnumber several real families, and the
module's own comment says so.

This repository declares four families (`.memory-tree.conf:15`) and the example family is not among
them, which is exactly why this corpus writes example ids in it: an example id in a tracked spec
anchors nothing, defines nothing and is cited by nobody, so no gate over the id corpus counts it.
The property is load-bearing and this unit keeps it.

It is also why a criterion asserting that a generated body anchors nothing passes before the
generator has written a line. The G3 round-2 record measured that by running the function rather
than reading it: an example-family bullet answered nothing and a declared-family bullet answered its
id.

### The fixture conf

`grammar_for(root)` re-resolves the conf at an explicit root and rebuilds the alternation, the eras
and all four anchor patterns from it (`tools/memory-recall/extract.py:478-505`), and the resolver it
calls reads `.memory-tree.conf` at that root rather than walking to the kit
(`tools/memory-recall/recall_conf.py:246-249`). So a scratch tree's own conf decides what a fixture
id is, and the declaration is local to the fixture by construction.

```
_fixture(tmp, example_family=True) writes, instead of today's two lines:
    DISCIPLINES="arch example"
    FAMILIES="arch:ARCH example:EXMP"
```

Both fields move together, from S1's one constant. The discipline half is not decoration: a build
README carries `streams` as well as `roster`, and the generator refuses a value outside either
declared set — `streams` at `tools/memory-tree/gen_build_index.py:785` and `roster` at `:788`. A
scaffold run over example-family asks writes both, so a fixture that declared the family and not the
discipline would trade one refusal for the other and the criterion would still never reach its
subject.

Default OFF, and the reason is measurable rather than cautious: every arm that reaches `collect()`
goes through this one helper, so flipping the conf for all of them changes the alternation under
arms whose assertions were written against the narrow one. The keyword makes the widening a property
of the arms that ask for it, and the untouched arms are the control that says nothing else moved.

### The staged RED

With the family declared, the criterion can fail, so it is required to have failed once. The break
is one generated body line in the fixture's README, staged, the arm observed RED, then unstaged:

```
- EXMP-aFoo-3 — the ask
```

That line matches the bullet anchor pattern compiled for the fixture's root, so the anchor predicate
answers the id and the assertion that the generated bodies anchor nothing goes red naming it. This
is the charter's rule that a gate whose failing case has never been observed is an assertion about
nothing, and it is the shape this build already writes at unit 28's AC13 and unit 19's AC11.

Note for whoever stages it: the break is a line of the WRITTEN README, not of the spec. A body line
in a spec would anchor nothing in this repository whatever this unit does, which is the two-tree
property S5 asserts and the reason the break has to live in the fixture.

### Rollout

**Order 14, shared with unit 14 and with `TOOL-dDerivedDocket-53`.** Unit 15 consumes this
declaration and is order 15, and `TOOL-dDerivedDocket-50`, which this unit consumes, is order 13, so
14 is the only step between them and every order from 1 to 38 is taken. Sharing is legal where it
matters: check 12 reds a `consumes-from` target whose order is AFTER the unit naming it, never one
below it (`tools/memory-tree/check-memory-hygiene.sh:1795`), and unit 50 at 13 is below. Disjointness
is NOT claimed. Unit 14 is WONTDO and carries no pass, but `TOOL-dDerivedDocket-53` was promoted to
this same step in the same pass and writes `tools/memory-tree/gen_build_index.py` and its selftest
too, so M6 in `memory/guides/BUILD-METHOD.md` answers no on clause 1 — one file, two write sets —
before clause 3 is even reached. The two run in sequence, which is what the driver does anyway:
dispatch is strictly sequential including within a shared order
(`tools/workflows/unattended-build.js:70`) over a roster sorted by step and then by id as a STRING
(`:314-318`), which puts this unit before `TOOL-dDerivedDocket-53`. No edge requires that order
either way; both need only to precede unit 15.

1. The constant and the keyword, default OFF, with the existing arms untouched and the whole
   selftest green — that run is the control.
2. The fixture opted in for the scaffold arms, the break of the block above staged, the arm observed
   RED, the break unstaged.
3. Unit 15's AC13 `new arm:` clause and the rev entry, in this unit's commit.
4. `memory/map/generated/` re-derived and staged with the `.py`, and confirmed byte-identical.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `EXAMPLE_ROW` | module constant in `gen_build_index.py` | no cell grades it: `.lexicon.conf` declares `js.function`, `py.function`, `py.type` and `sh.function`, and no constant row |
| the `_fixture` keyword | keyword argument | no cell grades a parameter name |

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` (S1, S2, and the selftest arms) ·
`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md` (S4) ·
`memory/map/generated/` (S6, re-derived and expected unchanged). This repository's own
`.memory-tree.conf` is deliberately not in this list; see §3.

### Alternatives rejected

- **File the fixture asks under a declared family.** The record offers it as the first of two
  spellings and it is cheaper in code. Rejected: a fixture ask filed under one of the four families
  this repository declares is a real-family id, and hygiene check 14 counts every real-family id a
  tracked record cites and nothing defines — so the fixture would either define a phantom record or
  orphan one. This paragraph deliberately does not SPELL such an id, because writing one here would
  make this spec the tracked record that cites it and check 14 would count it against the
  shrink-only `ORPHAN_ID_PIN`. `TOOL-dDerivedDocket-35` records the same decision for its scratch
  clone and takes the same way out.
- **Widen the fixture conf for every arm.** Rejected on blast radius: the arms that assert a roster
  or a defined-id set were written against the narrow alternation, and nothing in the suite would
  tell a reader which of them changed meaning.
- **Substitute the families in the process rather than in a conf.** Rejected: the resolver reads the
  conf at the root it is given, so a monkey-patched module constant would be a second grammar living
  beside the one the accessor builds — the two-answers class the sibling kit's own accessor exists
  to prevent.

## 5. Production-readiness checklist

- security — none. A conf written into a temporary directory by a self-test, read back by the same
  process, and deleted with the directory.
- perf / scale — one extra family in one alternation; the conf is resolved once per root by the
  accessor this unit consumes.
- error / empty / loading states — a fixture that declares the family and writes no example id is a
  legal empty case and the arm passes on it, which is precisely why the staged RED is required
  rather than recommended.
- observability — the arm names the id it found when it reds, so the failure says which body line
  anchored rather than that a count was wrong.
- risks — the risk is the widening reaching an arm that did not ask for it. The default-OFF keyword
  bounds it, and AC6 is the control that says the untouched arms still pass unchanged.
- testing — arms in the build-index selftest for S1 through S4, one of them observed RED against the
  staged break before it is allowed to pass; AC6 re-runs the whole selftest as the control.
- migration — none. No tracked conf changes and no landed record's ids change meaning.
- user docs — none. The constant and the keyword are self-test surface and reach no adopter-facing
  page.

## 6. Acceptance criteria

- **AC1** — When the selftest reads `EXAMPLE_ROW`, the discipline and family halves it yields are
  the ones the opted-in fixture's `DISCIPLINES` and `FAMILIES` values carry, read back out of the
  written `.memory-tree.conf` rather than restated in the assertion.
  Red when: the pair is spelled a second time at the fixture writer, so one half can be changed
  without the other and the fixture declares a family under a discipline it never added.
- **AC2** — When a fixture is built with the keyword omitted, the scratch `.memory-tree.conf` it
  writes is byte-identical to the one built at this unit's parent commit; with the keyword set, it
  carries both halves of the pair.
  Red when: the widening applies to every fixture, so an arm that never asked for the example family
  is graded by a different alternation than the one it was written against.
  cost: one kit selftest run, whose declared ceiling on the `build-index selftest` row of
  `tools/gate-legs.json` is inside what a pass can hold.
- **AC3** — When the scaffold arm writes a build README from example-family asks into an opted-in
  fixture and `gen_build_index.py --check` runs over it, it exits 0; with the keyword omitted it
  refuses naming the streams value and the `DISCIPLINES` enum, and over a fixture carrying the
  discipline half alone it refuses naming the roster value and the `FAMILIES` set. The order is the
  generator's own: `tools/memory-tree/gen_build_index.py:785` validates streams before `:788`
  validates roster, so the streams refusal hides the roster one until both halves are declared.
  Red when: the arm asserts only that SOME refusal fired, so a fixture carrying one half of the pair
  passes it while the anchor assertion the arm exists to reach is still unreachable.
- **AC4** — When the anchor predicate is resolved against the opted-in fixture's root and run over
  every line the scaffold wrote, it returns no anchor; and when the body line of §4's staged break
  is added to that README, the same run answers `EXMP-aFoo-3` and the arm reds naming it.
  Red when: the arm passes over a fixture whose ids could never have entered the population, which
  is the state this unit exists to leave — a green run that is not evidence.
  permission: the FLAG form `python3 tools/memory-tree/gen_build_index.py --selftest` is the direct
  check this pass may make, in the shape unit 15's AC12 states; that the same argv is also a HELD
  leg under `chunk = selftests` defers the BAR's run to the orchestrator at VERIFYING, never this
  one. The RED above is observed by hand against the staged break.
- **AC5** — When unit 15's spec is read at this unit's commit, its AC13 carries a `new arm:` clause
  naming the staged break, and that spec's §9 carries a new rev entry whose scope names AC13.
  Red when: the fixture is widened and the criterion keeps the text that says a green run of the arm
  is not evidence, so nothing records that it now is.
- **AC6** — When `python3 tools/memory-tree/gen_build_index.py --selftest` runs at this unit's
  commit it reaches its PASS line, and the count of `arm(` call sites in that file is not lower at
  this unit's commit than at its parent. The suite prints no count of its own, so the population is
  counted from the source rather than read off the output.
  Red when: an arm is silently retired to make the widened fixture green, which is the cheapest way
  to make this change look free.
  figure: both counts are DERIVED at observation time from the file at each commit, never pinned
  here.
  permission: as AC4 — the same flag in the pass, the leg deferred to VERIFYING.
- **AC7** — When `FAMILIES` is read out of `.memory-tree.conf` at this unit's commit, it declares the
  same four families it declares at the parent commit and no example family, and the anchor predicate
  resolved against this repository's root returns nothing for an example-family bullet.
  Red when: the example family is declared in the tracked conf, so every example id in every tracked
  spec becomes an anchored record and the id-corpus checks start counting them.
- **AC8** — When the codebase-map artifacts are re-derived at this unit's commit they are
  byte-identical to the ones at its parent commit, and `memory/map/generated/symbols.json` carries no
  row for `EXAMPLE_ROW` — that artifact carrying no Python module constant at all, measured on this
  tree on 2026-09-20, because the extractor captures only public module-level defs and classes plus
  statically-listed `__all__` names (`tools/codebase-map/map_lib.py:342-351`) and no memory-tree
  module declares an `__all__`.
  Red when: the criterion asserts instead that the constant APPEARS in `symbols.json`, which that
  extractor cannot produce, so a correct implementation reds and the cheapest way to green it is an
  `__all__` this unit has no reason to add; or the artifacts DO move and are regenerated in a later
  commit than the `.py`, which the pre-commit map leg refuses.

## 7. Gates

`build-index selftest` · `memory hygiene` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/memory-tree/gen_build_index.py --selftest` · a fixture opted into the example family with the generated body line of §4 staged into its README · none

## 8. Open questions

- **F1 — one constant or two?** The pair could be two constants, one per conf field, or one row in
  the `<discipline>:<FAMILY>` spelling `FAMILIES` already uses.
  RESOLVED (agent, 2026-09-20, delegated): one row in that spelling, split where it is written. The
  conf's own format already joins them, AC1 reads both halves back out of the written file, and two
  constants are two places to edit for one change.
- **F2 — should the keyword default ON?** Defaulting ON would let any future arm write an example id
  without asking, which is convenient and is also how the widening reaches an arm nobody reviewed.
  RESOLVED (agent, 2026-09-20, delegated): OFF. The untouched arms are the control this unit needs,
  and a default that changes what existing assertions measure buys convenience with the one thing
  the change has to prove.
- **F3 — does the staged RED belong in the criterion or in the arm's comment?** A comment is cheaper
  and is read by nobody who is not already there.
  RESOLVED (agent, 2026-09-20, delegated): in the criterion's `new arm:` clause, which is where this
  build already writes it and where the next round's reader looks.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, promoted from the G3 round-2 spec audit's H3 at its BOUNDED
  exit.
- rev-1 · 2026-09-20 · S6 · §4 Rollout · §4 Files touched · AC8 · close-out of the same rev. The
  promotion pass's verifier found no problem in this unit, so nothing of the mechanism, the criteria
  or the forks moved for it; what it added is the order paragraph this spec owed — order 14 is
  shared, `TOOL-dDerivedDocket-53` landed on the same step in the same pass and writes the same
  module, and the pair is sequenced rather than assumed disjoint. The close-out's own verifier then
  corrected S6 and AC8, which asserted that the new module constant appears in `symbols.json`: the
  map's Python extractor records public defs, classes and `__all__` names only, so a correct
  implementation redded that criterion, and AC8 additionally ran a real-tree gate leg with no
  `permission:` line. Both now assert the measured state — the artifacts do not move — and the
  criterion is a read rather than a run.

## 10. Reuse audit

No new mechanism fits here and none is built: the declaration route already exists and this unit
uses it. `python tools/codebase-map/reuse_lookup.py "anchor_at grammar_for in-kit route"` ranks
`grammar_for` a SEAM at fan-in 4 in `tools/memory-recall/extract.py`, and that accessor already
re-resolves a conf at an explicit root, which is the entire mechanism this unit needs; the fixture
helper `_fixture` at `tools/memory-tree/gen_build_index.py:1911` is the one place every arm's
scratch conf is written, so the opt-in has a single home. The pattern itself is this build's own
prior art rather than an invention: `TOOL-dDerivedDocket-35` declares one extra example family in
its scratch clone's conf so that its fixtures parse while this repository's id checks ignore them,
and the reasoning in that spec's §4 is the same one restated for a self-test fixture.

Recall terms used: `EXMP example family FAMILIES allowlist anchor_at grammar_for fixture conf
scratch repo orphan id staged RED could-not-fail`, passed to
`python tools/memory-recall/query.py "why do example ids in specs use a family the id grammar does not admit, and how does a fixture declare its own families"`.
