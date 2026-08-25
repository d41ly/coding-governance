# TOOL-dScaffoldedMirror-11 — the scoped extractor, and the one predicate it makes possible

**Status:** DEFERRED · rev-1 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams tooling · visitor + exemption class survive as correctness work; the fourth pin is cut

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md](../build/2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md) | spec-audit | TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-4 TOOL-dScaffoldedMirror-5 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-9 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-13 TOOL-dScaffoldedMirror-14 TOOL-dScaffoldedMirror-15 |

<!-- /gen:spec-records -->

## 1. Goal

`_python_defs` walks the tree with `ast.walk` and keeps four node types as `(name, line)` pairs
(`lexicon.py:140-169`), so the extractor is scope-blind BY CONSTRUCTION: it cannot tell a
module-level function from a method from a closure, and it cannot see how long the scope enclosing a
name is. Replace it with an `ast.NodeVisitor` that emits scope and span, then add exactly ONE
predicate over the result — a short name in a wide scope. The span condition is the whole design and
it is measured: the same rule fires 51 times above the cut line and 1,033 times below it. The scope
information also lands the kit-owned structural exemption class that `-9` cannot start without.

## 2. Scope (IN)

- **S1** — the structural exemption class, which lands FIRST inside this unit: the `visit_`-prefixed
  dispatch methods, `generic_visit`, and the `-19` noun-led exemption (`@property`,
  `@cached_property`, a zero-argument accessor). Kit-owned and closed, never a waiver pile. It
  carries the unselective-rule refusal — a shape matching zero definitions REDS — and prints an
  exemption total on every run.
- **S2** — `_python_defs` becomes an `ast.NodeVisitor` maintaining a scope stack, emitting a record
  per binding with `name`, `line`, `kind`, `scope`, `span` and `public`.
- **S3** — `extract()` widens from a 3-tuple of 2-tuples to a flat record list. FOUR call sites read
  it and all four move in the same commit; §4 gives the verified inventory, which corrects the
  research pass.
- **S4** — P6: the underscore-stripped name is at least 3 characters, unless the name is in a
  kit-owned 14-name allowlist (`i j k n x y z id db fn ok rc ts fd`) or the enclosing scope is at
  most 10 lines. Graded only over the reach-≥2 population.
- **S5** — the two thresholds and the allowlist are KIT CONSTANTS in `lexicon.py`, never
  `.lexicon.conf` keys.
- **S6** — P6's own pin key, measured at landing, plus the header text stating what P6 does NOT
  check.
- **S7** — `tools/lexicon/README.md` and `tools/lexicon/LEXICON.md` gain P6, the exemption class and
  the cut line.

## 3. Non-goals (OUT)

- **Never gate the converged populations, and the reason is that they are converged.** Comprehension
  targets are 764 occurrences over 65 distinct names; except-aliases 88 over 3; with-aliases 62 over
  7; for-targets 870 over 189; locals 4,000, of which 865 are already under 3 characters. A predicate
  over an already-converged population is a check that cannot fail, and one over the locals is a
  predicate that reds four thousand sites nobody will rename. The cut line is reach ≥ 2 — 2,349 of
  8,249 bindings — and it is the reusable result of the design pass, not a tuning choice.
- **No second, third or fourth predicate.** Three others were proposed and P6 is the only one whose
  adopter number stays in three figures. The others are follow-ups at best and none is filed.
- **No conf keys for the knobs.** S5, and §4 says why at length.
- **No casing predicate, no noun table, no synonym groups as a gate.** All three killed in the
  research pass; re-opening any is a fork with the killing argument quoted, not a design choice.
- **No `.ts`/`.tsx` extraction.** `-13` owns that and it is the larger hole.
- **No waiver for a `visit_` name.** The exemption is structural precisely so that `-9`'s first act
  is not 16 to 18 waiver rows in the design whose thesis is that the waiver is the last escape hatch.
- **No JavaScript scope model.** The probe extractor is regex-based and cannot carry a scope stack;
  P6 grades Python only, and that is stated in the gate header rather than left for a reader to
  discover.

## 4. Design

### What the walk destroys

`ast.walk` yields nodes breadth-first with no parent link. A `FunctionDef` arriving from it carries
its own name and line and nothing about where it sits, so `_python_defs` cannot answer "is this a
method?", "how long is the scope that encloses this parameter?" or "does this definition take
arguments?" — and those three questions are the entire content of both S1 and S4. A `NodeVisitor`
answers all three for free, because the visitor is the thing that knows its own descent.

### Data model

One record type for every binding the extractor emits:

```
Definition(name, line, kind, scope, span, public)
```

- `kind` ∈ `{func, method, class, param, module_const, class_attr, import}`. Imports keep their
  target in `name`, so P3 reads records like everything else rather than a separate channel.
- `scope` is the dotted path of enclosing definitions, empty at module level. It is what separates a
  method from a module-level function, which is the discriminator S1 turns on.
- `span` is the enclosing scope's `end_lineno - lineno + 1` for a binding, and the definition's own
  for a definition. It is what makes P6's second arm possible.
- `public` is `not name.startswith("_")`, carried because it is free here and expensive to
  reconstruct later.

### The four call sites, verified — and the research pass is wrong about one of them

The research pass states that three call sites unpack `extract()` and that the third,
`drift_report.py:715`, "is index-based and survives". **Verified against the tree at HEAD, and it
does not survive.**

| site | how it reads the result | survives? |
|---|---|---|
| `lexicon.py:448` | `funcs, types_, imports = got` at `:454` | no — internal |
| `scaffold_lexicon.py:72` | `funcs, types_, _ = got` at `:79` | no |
| `codebase-map/selftest.py:1129` | `fns, types, _imports = lx.extract(...)` | no |
| `drift-audit/drift_report.py:710` | `for nm, _ln in got[0]` at `:715` | **no** |

The last row is the correction. `got[0]` is index-based on the OUTER container, but the loop body
unpacks each ELEMENT as a 2-tuple, and R10 widens the element from `(name, line)` to a six-field
record. Under a flat record list it is worse still: `got[0]` becomes the first RECORD and the loop
tries to unpack its six fields two at a time. Either way it raises, and it raises OUTSIDE the
`except (SyntaxError, OSError)` at `:711`, which guards only the call.

Where that lands is worth stating, because it is the opposite of the usual answer. The break is
caught LOUDLY by an unguarded bar leg: `drift_report.py:1143` is `out = [s(ctx) for s in SIGNALS]`
with no exception guard, and `drift-audit records` runs `python tools/drift-audit/drift_report.py
--check` with no `guard` key in `tools/gate-legs.json`. So the bar reds with a traceback rather than
a finding. The two sites that are NOT caught by a default bar are `tools/codebase-map/selftest.py`,
whose leg is guarded on the map kit and held with the other kit self-tests, and `scaffold_lexicon.py`
if `-8` has not yet deleted the derivation loop that calls it. All four move in one commit; none is
left to be discovered.

A fifth grep hit, `tools/codebase-map/map_lib.py:284`, is a homonym — `extract` there is a PARAMETER
of `json_artifact_inventory` — and is untouched. The map reports `extract` at fan-in 9, which counts
name references across the corpus including prose in this build's own records; the resolved call
sites are the four above.

### The exemption class, and the two shapes it must carry as ONE rule

Measured on this worktree at HEAD with the kit's own splitter: 735 tracked Python function
definitions, and 418 of the corpus's 463 offenders are Python (the other 45 are JavaScript, confirmed
by `python tools/lexicon/lexicon.py --list`).

| shape | offenders today | members |
|---|---|---|
| `^visit_[A-Z]` and `generic_visit` | **0** | none exist yet |
| `@property` | **3** | `has_block`, `clean` (`map_lib.py`), `empty` (`reuse_lookup.py`) |
| `@cached_property` | **0** | none |
| zero-argument METHOD, non-property | **4** | `_find_charter`, `emit`, `__str__`, `digest` |
| zero-argument ANY definition | 81 | the 4 above plus 77 module-level functions |

Three things follow, and each is load-bearing.

**One rule, not four.** Declared as separate rules, the `visit_` shape and `@cached_property` each
match zero definitions and each REDS by the unselective-rule refusal S1 itself installs. Declared as
ONE exemption class with one population, the class is armed at 7 today and the refusal fires only if
the whole class goes empty. That is the design, and it is why the class is a class.

**The `visit_` shape has no population until this unit creates it.** Nothing in the tree defines a
`visit_*` or `generic_visit` method today — verified by `git grep`. So the exemption cannot land as
its own unit ahead of the visitor: separated in time it reds by its own refusal on day one. It lands
first INSIDE this unit, in the same commit as the rewrite that gives it 17 or 18 members, and the
research pass's staged 8-method visitor that reds the gate at 471 over 463 is the failing case that
re-runs green.

**The `-19` ruling's third arm must be read as "zero-argument METHOD", not "zero arguments".** Read
literally it exempts 81 of 418 Python offenders — 19.4% — pre-absorbed by structure and forever. That
is the `^_` SHAPES row the research pass killed at 22.0%, whose verdict was "strictly worse than the
integer: a pin absorbs a fixed count and must be visibly raised again; a regex pre-absorbs every
future `_helper` silently". Worse, seven of the 81 are `t_*` self-test functions that `-14` renames,
so the literal reading would legalise the exact drift `-14` exists to remove. The method reading
exempts 4 and the discriminator is the enclosing scope.

**The negative, said plainly.** A structural predicate cannot tell an accessor from a zero-argument
command. Of the 4 members of the method arm, `govkit.py::emit` prints and returns an exit code and
`_find_charter` searches the filesystem; neither is an accessor and both are exempted anyway. The
class is known to over-cover by half its non-property membership, and that is accepted because `ast`
offers no semantic accessor test and the alternative is 81.

### Where the `-19` exemption lands, and why it is here rather than in `-8`

`@property` is visible in a decorator list, which `ast.walk` already sees, so that arm could live
anywhere. The zero-argument accessor arm cannot: it needs the argument list AND the knowledge that
the definition's enclosing scope is a `ClassDef`, and the enclosing scope is precisely what
`ast.walk` destroys and what this unit's visitor restores. The measured gap between the two readings
is 81 versus 4, and the discriminator is scope. `-8`'s subject is the canon and the declaration
grammar; it gains no scope information and would have to re-derive one. So the ruling's machinery is
this unit's, and `-8` should state that it does not carry it.

### P6, and both arms

The predicate reds a binding whose underscore-stripped name is shorter than 3 characters, unless the
name is in the kit-owned allowlist or the enclosing scope is at most 10 lines. It is graded only over
the reach-≥2 population — module-level names, type names, class attributes and parameters.

Both arms are required or P6 is a plain length rule. A 40-line function with a parameter named `d` is
RED; the same parameter in a 4-line function is GREEN. Without the second arm the span condition is
decorative and the predicate would have shown 1,033 offenders instead of the design pass's 51 above
the cut line.

The two figures the design pass reports for this rule — 51 above the cut line, and 55 as this repo's
adopter number — come from slightly different slices and must reconcile to ONE measured number at
build time. AC6 records whichever the build measures rather than asserting either.

### The knobs are kit constants

`3`, `10` and the 14 names live in `lexicon.py` as module constants. They are NOT declaration keys,
and the reason is arithmetic rather than taste: the design pass published its own threshold menu of
87 / 120 / 65 / 51 offenders, and an offender count selected from a menu is a pin wearing a
threshold's clothes. A declaration key would let an adopter dial the span down until the count is
zero — the raisable integer under a new name, arriving in the same build that deletes the raisable
integer. A kit constant can be argued with in a diff to the kit; a conf key can be argued with in a
diff nobody reviews.

### P6's pin, and the edge it creates to `-9`

P6 needs its own accounting at landing. Folding its offenders into the verb pin is the "one fact, two
carriers" defect the research pass names about `P5` and `BANNED_SUFFIXES`, and shipping P6 unarmed is
illegal by this kit's own law — the `lexicon-layers` hole records that "an unarmed predicate that
exits 0 is indistinguishable from a satisfied one". So P6 ships with `SHORTNAME_OFFENDER_PIN`,
measured at landing.

**That is a NEW edge to `-9`, stated here because M2 requires both sides to say it.** `-9`'s exit
criteria name three `*_OFFENDER_PIN` keys to delete; after this unit there are FOUR, and `-9` is
already blocked on `-11`, so it will see them. `-9` should say "deletes four pin keys, the fourth
arriving with `-11`". The 55 or so P6 offenders are grandfatherable under `-9` without special
handling, because assert C derives at `FREEZE_SHA` using today's declaration and today's kit, and P6
is part of the kit by then.

### Files touched (estimate)

`tools/lexicon/lexicon.py` (~250 lines: the record, the visitor, the exemption class, P6, the
exemption total), `tools/drift-audit/drift_report.py` (~5 lines at `:709-718`),
`tools/codebase-map/selftest.py` (~3 lines at `:1129`), `tools/lexicon/scaffold_lexicon.py` (~8 lines
at `:72-79`, and possibly zero if `-8` has already deleted that loop), `.lexicon.conf` (one new pin
key with its measured value and the reason beside it), `tools/lexicon/selftest.py` (the arms), and
the two kit docs.

### Alternatives rejected

- **Keep the 3-tuple and add `extract_records()` beside it.** One fact, two carriers, two shapes to
  keep in step, and the old one stays the path of least resistance forever.
- **Widen only the elements and keep the 3-tuple container.** It still breaks `drift_report.py:715`,
  so it pays the migration cost without buying the single shape.
- **Land the exemption class as its own unit ahead of the visitor.** Its `visit_` arm has zero
  members until the visitor exists, so it would red on its own refusal on landing day.
- **The other three proposed predicates.** Adopter numbers in four figures; the brief's own bar is
  that a predicate redding 2,000 identifiers on a real adopter is deleted rather than adopted.
- **Declaration keys for the thresholds.** The pin with a new name.

## 5. Production-readiness checklist

- **security** — N/A. Parse-only over files the kit already parses; no new input surface, no write
  path, no subprocess. `ast.parse` already runs on every tracked `.py` on every bar.
- **perf / scale** — +0.091 s here and +0.938 s on `incms`, inside a parse that already happens, so
  the check goes from 0.44 s to roughly 0.53 s warm. The three lexicon legs are 13.0 s of a 2,587 s
  leg-sum, 0.503%; cost is not a constraint on this kit and blast radius is.
- **a11y** — N/A. A CLI checker with no rendered surface.
- **i18n** — N/A. Identifier text is ASCII by the splitter's own regex and the predicate counts
  characters after stripping underscores.
- **error / empty / loading states** — the empty state is a first-class refusal in both directions:
  the exemption class REDS if its population goes empty, and the exemption TOTAL is printed on every
  run so a class that silently grows is visible. A file that fails to parse still RAISES rather than
  degrading to an empty result, which `_python_defs` already does deliberately.
- **observability** — P6 reports `graded`, `offenders` and `waived` through the per-predicate
  reporting `-2` builds; this unit consumes that and does not redefine it. New here: the printed
  exemption total, and the record `kind` distribution, which is what makes the cut line auditable
  after the fact.
- **risks** — the shape change reaches THREE other kits, and two of the three external call sites are
  invisible to a default bar run (a guarded map self-test, and a scaffold path `-8` may already have
  removed). The third is caught, but as an unguarded traceback rather than a finding. Second risk: a
  fourth pin key lands two phases before the unit that deletes all pins. Third: the exemption class
  is the first structural exemption this kit has ever shipped, and a structural exemption that grows
  without anyone noticing is the `SHAPES` failure mode — which is what the printed total is for.
- **testing + left-shift gates** — P6's two arms, the exemption class's zero-match refusal, an arm
  asserting the exemption total is printed and non-zero, and a caller-compatibility arm that imports
  each of the three external readers and exercises the path through `extract()`. The class here is
  `memory/gotchas/vacuous-selector-empty-population.md` for the exemption and the unselective-rule
  law for its refusal.
- **migration / rollback** — `extract()`'s signature is a kit-internal contract with three external
  readers, so the migration is "all four in one commit" and the rollback is reverting that commit,
  which takes the new pin key out of `.lexicon.conf` with it. No persisted artifact changes shape.
- **user docs** — S7. The predicate table gains P6, the exemption class is documented as kit-owned
  and closed, and the cut line is written down because it is the reusable result.

Unresolved here, and therefore the owner scope menu: **risks** — whether a fourth pin key is
acceptable two phases before `-9` deletes all of them, or whether `-11` should wait for `-9`; and
**testing** — whether the caller-compatibility arm is enough given that two of the three external
sites are invisible to a default bar.

## 6. Acceptance criteria

- **AC1** — When a `def frobnicate(self)` with a parameter `d` is staged inside a 40-line function
  and `python tools/lexicon/lexicon.py` runs, P6 reds and names `d` with its file and line.
- **AC2** — When the SAME parameter `d` is staged inside a 4-line function, `python
  tools/lexicon/lexicon.py` is green on P6, proving the span arm is load-bearing rather than
  decorative.
- **AC3** — When the kit-owned exemption class is edited so that no shape in it matches any
  definition, `python tools/lexicon/lexicon.py` REDS with the unselective-rule refusal naming the
  class, rather than passing green over an empty exemption.
- **AC4** — When `python tools/lexicon/lexicon.py` succeeds, stdout carries the exemption total as a
  printed number, and `python tools/lexicon/selftest.py` asserts it is greater than zero on this
  corpus rather than reading it by eye.
- **AC5** — When the `ast.NodeVisitor` rewrite is staged in `tools/lexicon/`, the gate that reds
  today at 471 over pin 463 runs GREEN, because all 17 `visit_*` names and `generic_visit` are
  covered by the structural exemption and none is waived.
- **AC6** — When `python tools/lexicon/lexicon.py --measure` runs after P6 arms, it prints a
  `SHORTNAME_OFFENDER_PIN` line whose value is the measured count on this corpus, and that number is
  written into `.lexicon.conf` with its derivation beside it rather than copied from the design
  pass's 51 or 55.
- **AC7** — When `python tools/drift-audit/drift_report.py --check` runs after the shape change, it
  completes and reports `lexicon_verbs_unused` with a live assertion, rather than raising out of
  `drift_report.py:1143`.
- **AC8** — When `python tools/codebase-map/selftest.py` runs after the shape change, its js-probe
  cross-check arm at `:1129` passes and still asserts a non-empty comparison set.
- **AC9** — When `python tools/lexicon/lexicon.py` runs over the reach-≥2 population, no
  comprehension target, except-alias, with-alias, for-target or function local appears as a P6
  offender; a selftest arm stages one of each and asserts silence.
- **AC10** — When `grep -n 'SHORTNAME' .lexicon.conf tools/lexicon/lexicon.py` runs, the two
  thresholds and the 14-name allowlist appear only in `lexicon.py` and never as a declaration key.
- **AC11** — When `python tools/lexicon/lexicon.py` is timed against the pre-change engine on this
  worktree, the added wall clock is under 0.15 s.

## 7. Gates

Keeps green: `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, and — because the
shape change reaches three other kits — `drift-audit records`, `codebase-map kit selftest`,
`codebase-map coverage + freshness`, `memory hygiene` and `kit version markers`.

Adds NO new leg. P6 is a new refusal inside `lexicon naming predicates`, the exemption class's
zero-match refusal is another one in the same leg, and every arm lands in `lexicon selftest`. That is
deliberate: the leg count is not the coverage, and a change whose whole risk is cross-kit is better
served by keeping the existing legs honest than by adding a fourth that only this kit runs.

## 8. Open questions

- **F1 — flat record list, or a widened 3-tuple?** A flat list is one shape and forces all four call
  sites to declare what they want by `kind`; a widened tuple preserves the container shape and breaks
  the same site anyway. RECOMMENDATION: flat record list. The tuple's only advantage is a migration
  it does not actually avoid. RESOLVED (agent, 2026-08-24, delegated): flat record list, all four
  call sites in one commit, with the caller-compatibility arm in the kit's selftest.
- **F2 — does the `-19` noun-led exemption land here or in `-8`?** RECOMMENDATION: here. Two of its
  three arms are decorator-detectable anywhere, but the zero-argument accessor arm needs the
  enclosing scope, and the measured difference between having it and not is 81 exempted definitions
  versus 4. RESOLVED (agent, 2026-08-24, delegated): here, as one class with the `visit_` shapes, and
  read as "zero-argument METHOD" rather than "zero arguments" for the reason in §4.
- **F3 — P6's pin, and the new edge to `-9`.** Options: a fourth `*_OFFENDER_PIN` key deleted by
  `-9`; ship P6 reporting-only until `-9`; or fold P6 into the verb pin. RECOMMENDATION: a fourth
  key. Reporting-only is an unarmed predicate, which this kit's own `lexicon-layers` hole calls a
  refusal rather than a green run, and folding is one fact with two carriers. RESOLVED (agent,
  2026-08-24, delegated): ship `SHORTNAME_OFFENDER_PIN`; the edge is NEW and `-9` must delete four
  keys, not three.
- **F4 — UNRESOLVED, owner. Is a fourth pin acceptable at all, given that `-18` has already ruled
  that gov takes the pressure `-9` ships?** The honest reading is that this unit adds one raisable
  integer to a build whose thesis is that raisable integers are the defect, and it does so two phases
  early. The alternative is re-ordering so that `-9` lands before `-11`, which `-9` cannot do because
  it is blocked on this unit's exemption class. The recommendation above resolves the MECHANISM; the
  sequencing cost is the owner's to accept or refuse, and it is not resolved here.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on the `dScaffoldedMirror` research pass
  (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`, recommendation
  R10 and its Phase 3 exit criteria) and on the read-only probe of `incms/main` taken the same day,
  from which the 481-offender adopter figure is drawn. The call-site inventory, the exemption-class
  populations and the 418/45 offender split were re-measured on this worktree while writing, and the
  call-site table corrects the research pass.
- rev-1 status 2026-08-24 · DEFERRED, with a SPLIT verdict recorded. The visitor rewrite and the `-19` noun-led exemption class are correctness work that stands alone - `extract()` has four resolved readers in three kits and the current `ast.walk` destroys enclosing scope - and they should be re-filed on their own. `SHORTNAME_OFFENDER_PIN` is CUT: it is a FOURTH raisable integer, landing two phases before `-9` deletes three, in a build whose thesis is that the ceiling is the defect. P6 without a pin - a printed count plus the exemption - delivers demand 1 without one.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py ast visitor scope span extractor exemption` returns
`extract` (`tools/lexicon/lexicon.py`, **fan-in 9**, SEAM) at rank one, then three `extract_*`
functions in `tools/memory-recall/extract.py` at fan-in 1 each, the `lexicon.subtokens` affordance
seam, and `t_affordance_exemption_drop` plus `t_extractor_helpers_fail_closed` in
`tools/codebase-map/selftest.py`.

The seam is `extract` itself, and this unit does not wire THROUGH it — it widens it. That is the
finding worth recording: the map grades it a SEAM at fan-in 9, so the shape change is not a local
edit, and §4's verified table is the reconciliation. Fan-in there is NAME-based, counting references
across the whole corpus including this build's own prose and a homonym parameter at
`map_lib.py:284`; the resolved readers are four, three of them in other kits.

No existing seam fits the visitor itself, and the evidence is specific rather than an absence of
search results. `tools/memory-recall/extract.py`'s three functions are chunkers over markdown records
and share no shape with an `ast` descent. `tools/codebase-map/map_extractors.py` is the nearest
neighbour by purpose and is deliberately unavailable: `.lexicon.conf`'s single `LAYERS` row forbids
`tools/lexicon/* -> tools/codebase-map/*`, because the kit must ship self-contained, and
`subtokens.py` was PORTED rather than imported to honour exactly that. The visitor is new code inside
`lexicon.py`, which is the intended answer.

What IS reused, and named so it is not rebuilt: `scan_unselective_rules`'s refusal shape supplies S1's
zero-match red, and `Offender` (`lexicon.py:110-124`) is the finding type P6 emits, unchanged.
