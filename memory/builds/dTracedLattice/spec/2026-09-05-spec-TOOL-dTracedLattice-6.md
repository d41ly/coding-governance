# TOOL-dTracedLattice-6 — the AST import resolver is rescued into codebase-map before P3 deletes it

**Status:** SPECCED · rev-2 · 2026-09-06 · node d · Tier-2 · base c4fcf5ad · streams tooling · order 1 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round3.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round3.md) | spec-audit | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 TOOL-dTracedLattice-7 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aSurfacedLexicon-2` is SPECCED at order 1 to delete predicate P3 from the lexicon kit,
including `resolve_import` and seven sibling engine functions — this tree's only AST import
resolver. `TOOL-dTracedLattice-1` S8 needs exactly that capability as a tracked file, for the variant
harness and its `ast`-verified edge fixtures. Move it into `tools/codebase-map/` before the deletion
rather than deleting it and rebuilding it.

Rev-1 cited that unit's S6, which its rev-5 renumbering turned into the coverage-report item; the
consumer is S8 and has been since rev-4's ratification. **No unit currently IMPROVES the resolver.**
Unit 1 §3 puts the receiver-binding pass out of scope and gives it its own future spec, so the
warrant here is the rescue itself — the capability existing as a tracked file — and not a downstream
improvement.

## 2. Scope (IN)

- **S1** Carry the TRANSITIVE CLOSURE, not the two names rev-1 listed. `resolve_import`
  (`tools/lexicon/lexicon.py:386`) reaches `_resolve_relative` at `:399`/`:408`,
  `_check_path_suffix` at `:417`/`:432`, and `ext_of` at `:396`/`:417`/`:422`/`:432` and
  transitively at `:382`. **Four MOVE and one COPIES** across the TWO builds, and the split is
  not cosmetic — this unit's own diff copies all five and deletes none, per §4's
  copy-then-delete disposition; what makes four of them a MOVE is that
  `TOOL-aSurfacedLexicon-2` S1 deletes those four and not `ext_of`:
  `build_module_index`, `_resolve_relative`, `_check_path_suffix` and `resolve_import` are all on
  `TOOL-aSurfacedLexicon-2` S1's deletion list, so a rescue naming only two ships a resolver whose
  helpers are deleted under it by the unit this rescue exists to beat. `ext_of` is the opposite case:
  it is read at eight further lexicon sites (`:171`, `:521`, `:551`, `:611`, `:727`, `:940`, `:995`,
  `:1077`), is NOT on that deletion list, and cannot leave — so the rescued module carries its own
  copy, which this item authorises explicitly and §3's "no new capability" is not stretched to cover.
  The language-aware branch travels intact: a recorded correction already fixed it once, because a
  dot means different things in Python and JS and the importer's extension is what says which.
- **S2** Preserve the DIRECTIONAL layer rule the lexicon kit built on top of it. A rule of the form
  `tools/lexicon/* -> tools/codebase-map/*` forbids one kit importing another and says nothing about
  a third file importing both, and that asymmetry is the whole value.
- **S3** Carry the resolver's known limits into its new home as a header, not as folklore, and state
  the limits OF THIS FUNCTION. `resolve_import` returns CANDIDATE repo paths and an empty list means
  external or unresolvable, which is never a violation. It is language-branched on the IMPORTER's
  extension: a Python dotted target names its package from the root and the importer's directory gets
  no precedence (`:414-421`), a bare Python name prefers the importer's directory but FALLS BACK to
  every stem hit (`local or hits`), and every other language treats dots as part of a name. A
  consumer that reads it as a call graph will be wrong: it resolves import statements, not call
  sites, and it counts nothing.

  **Rev-1 stated the wrong artifact's limits, and that is this build's own load-bearing lesson
  reproduced inside it.** "Binds same-directory sibling imports" and "554 sites against 9112
  unresolved attribute sites" are properties of the committed research prototype
  `2026-09-05-build-TOOL-dTracedLattice-1-resolver.py`, which carries a
  `Path(c).parent.as_posix() == d` filter at both import branches and counts `ast.Attribute` nodes.
  `lexicon.py`'s `resolve_import` has no `ast.Attribute`, no site counting, and is not
  same-directory-bound. Those two figures may be quoted only in a sentence naming that prototype as
  their source.
- **S4** Sequence against `TOOL-aSurfacedLexicon-2`. That unit's S1 deletes the eight functions and
  its S7 deletes 29 arms; this unit must land first, and that unit's spec gains a pointer saying the
  code moved rather than died.
- **S5** Leave the lexicon kit's own behaviour unchanged, and its FILES unchanged too: per §4
  this unit copies and deletes nothing, so `tools/lexicon/lexicon.py` is not in its write set
  at all. This is an addition plus a pointer, never a rewrite of what P3 decided.

## 3. Non-goals (OUT)

- No new capability. Nothing here improves the resolver, and **no unit in this build does** —
  `TOOL-dTracedLattice-1` §3 puts the receiver-binding pass out of scope and gives it its own future
  spec. Rev-1 named that unit's S6, which its rev-5 renumbering turned into the coverage report.
- No change to `TOOL-aSurfacedLexicon-2`'s decision to delete P3. That unit's reasoning stands and
  this one does not reopen it.
- No type inference and no attribute-site resolution. The limits S3 records are the limits kept.
- Not the variant harness. That is unit 1's S6 and a separate mechanism.

## 4. Design

### Migration

The move is a rescue under a deadline, so the ordering is the design. `TOOL-aSurfacedLexicon-2` is
order 1 in its own build and deletes the source; this unit is order 1 in this build and must precede
it. Both builds are SPECCED and neither has begun, so the constraint is recordable now and expensive
later — once P3 is deleted this unit becomes a rebuild from git history rather than a move.

**The inter-build window, which rev-1 left for somebody to discover.** Three live lexicon callers
reach the resolver — `tools/lexicon/lexicon.py:527` (`build_module_index`), `:536`
(`scan_unselective_rules`) and `:595` (`check_layer_violation`) — and the destination is UNREACHABLE
from them. `lexicon.py:346-352` records why in its own words: no Python import can produce the hyphen
in `tools/codebase-map/`. `AGENTS.md` §12 bans a kit file naming a sibling kit by literal, and S2
preserves the very rule `tools/lexicon/* -> tools/codebase-map/*` that would forbid the import. So
"move" cannot mean "cut" while those callers live.

**The disposition is COPY-THEN-DELETE, and it is chosen rather than left open.** This unit ADDS the
transitive closure to `tools/codebase-map/` and changes `tools/lexicon/` not at all, so the lexicon
legs stay green at this unit's landing commit — AC6. The DELETION is not this unit's: it is
`TOOL-aSurfacedLexicon-2` S1, which already deletes all four moved functions, and S4's pointer is
what tells that unit's reader the code moved rather than died. The duplicate therefore exists only
between the two landings and is retired by a unit already specced to retire it — which is why no
parity gate over the pair is owed, and why the alternative (a declared `sys.path` seam with a §12
waiver) is rejected: it buys a permanent cross-kit import to avoid a temporary duplicate.

### Alternatives rejected

Letting the deletion proceed and rebuilding in `TOOL-dTracedLattice-1` S6. Rejected by the owner on
2026-09-05: it re-spends 164 lines and discards the language-aware dot handling and the directional
layer rule, both of which carry recorded corrections earned by earlier defects.

## 5. Production-readiness checklist

- security — N/A, a code move within the tracked tree.
- perf / scale — the resolver's cost moves with it; `TOOL-dTracedLattice-1` AC8 is the ceiling that
  prices it, at most 0.05 s added. Rev-1 named that unit's S4, which is "Report a miss as a miss";
  its rev-5 moved the re-declaration onto AC8.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an unparseable file is skipped, as today; S3 records that.
- observability — S3's header is the observability item.
- risks — the real risk is ordering. If `TOOL-aSurfacedLexicon-2` lands first this unit's subject is
  gone, so S4 is the mitigation and its pointer is the durable half.
- testing + left-shift gates — the arms that cover `resolve_import` are COPIED alongside it, so
  the lexicon kit keeps its own until `TOOL-aSurfacedLexicon-2` removes both; AC7's assertion
  that the moved module imports nothing from `tools/lexicon/` is the new leg, carried by the
  directional rule S2 preserves, which still refuses what it refused before.
- migration / rollback — revert deletes the copy and nothing else: per §4 the lexicon kit is
  untouched by this unit, so there is nothing to restore there. The functions become
  irrecoverable only after `TOOL-aSurfacedLexicon-2` S1 lands, which is the whole reason for the
  ordering.
- user docs — `tools/codebase-map/README.md` gains the resolver in its contents list.

## 6. Acceptance criteria

- **AC1** — When `resolve_import` is called from `tools/codebase-map/` after the move, it returns the
  same candidate paths for the same target and importer as it did from `tools/lexicon/lexicon.py`,
  asserted by the copied arms over the same fixtures.
- **AC2** — When a JS package specifier carrying a dot is resolved, the importer's extension decides
  the namespace rule, so `lodash.debounce` is not treated as a dotted module path.
- **AC3** — When the directional layer rule is evaluated after the move, `tools/lexicon/lexicon.py`'s
  `LAYERS` direction is still forbidden and a third file importing both sides is still permitted.
- **AC4** — When `tools/lexicon/lexicon.py` is read after `TOOL-aSurfacedLexicon-2` lands, its spec
  carries a pointer naming `tools/codebase-map/` as where the resolver went, so a reader of the
  deletion is not told the capability was removed.
- **AC5** — When the moved `resolve_import` header is read, it states the CANDIDATE-SET semantics
  (an empty return is external or unresolvable, never a violation) and the language branch on the
  importer's extension, including that a bare Python name falls back beyond the importer's directory.
  It does NOT state the same-directory binding limit or the 554/9112 site figures: those are the
  research prototype's, per S3, and shipping them as this function's would make AC5 impossible to
  meet truthfully.
- **AC6** — When `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs at the commit this unit
  lands, `lexicon selftest` and `lexicon naming predicates` are GREEN, proving the three live callers
  at `lexicon.py:527`/`:536`/`:595` still reach a resolver. `lexicon selftest` is `subject: kit` in
  `tools/gate-legs.json` and is HELD on a plain bar, so the plain spelling would not exercise this.
- **AC7** — When the moved module is read, it imports nothing from `tools/lexicon/`, which is the
  directional rule S2 preserves, asserted by that rule itself.

## 7. Gates

`codebase-map kit selftest` · `lexicon selftest` · `lexicon naming predicates` ·
`install-prefix (shipped surface)` · `harness arms (fail branches armed or pinned)`.

Both kit-subject legs are HELD on a plain bar; verifying this unit needs
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. The runner names every held leg, so they are
announced rather than silent.

## 8. Open questions

none — the owner ratified the rescue on 2026-09-05 against the two alternatives, and the ordering
constraint against `TOOL-aSurfacedLexicon-2` follows from it rather than being a second choice.

Recorded so the next reconciliation is cheap: `TOOL-dTracedLattice-1`'s scope numbering MOVED at its
rev-5, and every pointer in this spec was written against the pre-rev-5 numbering. The consumer is
that unit's S8 and its cost ceiling is that unit's AC8; a reader checking a citation here against
unit 1 should expect rev-7 numbering, not rev-1's.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the owner's ruling on the dTracedLattice design pass.
- rev-2 · 2026-09-06 · folded the round-3 spec audit, this spec's FIRST review: B2 (three live lexicon
  callers at `:527`, `:536` and `:595` cannot reach `tools/codebase-map/` — no Python import produces
  the hyphen, §12 bans the literal, and S2 preserves the rule that would forbid it — so §4 states the
  copy-then-delete disposition and AC6 pins the lexicon legs green at this unit's landing commit),
  B3 (S3 stated the research prototype's limits as this function's, which AC5 made a
  Definition-of-Done item and no honest close could meet; both are rewritten from `lexicon.py:386-433`
  and AC7 added), H7 (§1, §3 and §5 cited unit 1's pre-rev-5 numbering — the consumer is its S8 and
  the ceiling its AC8 — and no unit in this build improves the resolver), H12 (S1 named two of five
  things that must travel: four MOVE, `ext_of` COPIES because eight other lexicon sites read it).

## 10. Reuse audit

The seam is `tools/lexicon/lexicon.py`'s `resolve_import` itself, which this unit moves rather than
reimplements — the strongest possible form of reuse, and the reason the owner ruled for the rescue.
Cited from `python tools/codebase-map/reuse_lookup.py "resolve an import target to a repo path"`,
whose ranked output is subject to the 7.2%-precision defect `TOOL-dTracedLattice-1` repairs, which is
why the seam here was established by reading `tools/lexicon/lexicon.py:386` directly rather than by
trusting the ranking. Verified against source at writing time: that function exists, is
language-aware, and is named in `TOOL-aSurfacedLexicon-2` S1's deletion list.

Recall terms used: lexicon P3 import direction resolver layers rule delete rescue codebase-map ast
module index namespace package specifier
