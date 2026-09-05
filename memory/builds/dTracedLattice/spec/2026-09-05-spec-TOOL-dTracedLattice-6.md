# TOOL-dTracedLattice-6 — the AST import resolver is rescued into codebase-map before P3 deletes it

**Status:** SPECCED · rev-1 · 2026-09-05 · node d · Tier-2 · base c4fcf5ad · streams tooling · order 1 · ratified 2026-09-05

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aSurfacedLexicon-2` is SPECCED at order 1 to delete predicate P3 from the lexicon kit,
including `resolve_import` and seven sibling engine functions — this tree's only AST import
resolver. `TOOL-dTracedLattice-1` S6 needs exactly that capability as a tracked file. Move it into
`tools/codebase-map/` before the deletion rather than deleting it and rebuilding it.

## 2. Scope (IN)

- **S1** Move `resolve_import` and the module index it resolves against out of
  `tools/lexicon/lexicon.py` into `tools/codebase-map/`, preserving the language-aware branch that a
  recorded correction already fixed once — a dot means different things in Python and JS, and the
  importer's extension is what says which.
- **S2** Preserve the DIRECTIONAL layer rule the lexicon kit built on top of it. A rule of the form
  `tools/lexicon/* -> tools/codebase-map/*` forbids one kit importing another and says nothing about
  a third file importing both, and that asymmetry is the whole value.
- **S3** Carry the resolver's known limits into its new home as a header, not as folklore: it binds
  same-directory sibling imports, and on this tree it resolves 554 sites against 9112 unresolved
  attribute sites. A consumer that reads it as a call graph will be wrong.
- **S4** Sequence against `TOOL-aSurfacedLexicon-2`. That unit's S1 deletes the eight functions and
  its S7 deletes 29 arms; this unit must land first, and that unit's spec gains a pointer saying the
  code moved rather than died.
- **S5** Leave the lexicon kit's own behaviour unchanged. This is a move plus a pointer, never a
  rewrite of what P3 decided.

## 3. Non-goals (OUT)

- No new capability. Nothing here improves the resolver; `TOOL-dTracedLattice-1` S6 does that.
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

### Alternatives rejected

Letting the deletion proceed and rebuilding in `TOOL-dTracedLattice-1` S6. Rejected by the owner on
2026-09-05: it re-spends 164 lines and discards the language-aware dot handling and the directional
layer rule, both of which carry recorded corrections earned by earlier defects.

## 5. Production-readiness checklist

- security — N/A, a code move within the tracked tree.
- perf / scale — the resolver's cost moves with it; unit 1 S4 re-declares the ceiling once it has a
  consumer.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an unparseable file is skipped, as today; S3 records that.
- observability — S3's header is the observability item.
- risks — the real risk is ordering. If `TOOL-aSurfacedLexicon-2` lands first this unit's subject is
  gone, so S4 is the mitigation and its pointer is the durable half.
- testing + left-shift gates — the arms that cover `resolve_import` move with it, and an arm asserts
  the directional rule still refuses what it refused before.
- migration / rollback — revert restores the functions to the lexicon kit; nothing is deleted here.
- user docs — `tools/codebase-map/README.md` gains the resolver in its contents list.

## 6. Acceptance criteria

- **AC1** — When `resolve_import` is called from `tools/codebase-map/` after the move, it returns the
  same candidate paths for the same target and importer as it did from `tools/lexicon/lexicon.py`,
  asserted by the moved arms over the same fixtures.
- **AC2** — When a JS package specifier carrying a dot is resolved, the importer's extension decides
  the namespace rule, so `lodash.debounce` is not treated as a dotted module path.
- **AC3** — When the directional layer rule is evaluated after the move, `tools/lexicon/lexicon.py`'s
  `LAYERS` direction is still forbidden and a third file importing both sides is still permitted.
- **AC4** — When `tools/lexicon/lexicon.py` is read after `TOOL-aSurfacedLexicon-2` lands, its spec
  carries a pointer naming `tools/codebase-map/` as where the resolver went, so a reader of the
  deletion is not told the capability was removed.
- **AC5** — When the moved `resolve_import` header is read, it states the same-directory binding
  limit and the site-resolution figures, so a consumer cannot mistake it for a call graph.

## 7. Gates

`codebase-map kit selftest` · `lexicon selftest` · `lexicon naming predicates` ·
`install-prefix (shipped surface)` · `harness arms (fail branches armed or pinned)`.

Both kit-subject legs are HELD on a plain bar; verifying this unit needs
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. The runner names every held leg, so they are
announced rather than silent.

## 8. Open questions

none — the owner ratified the rescue on 2026-09-05 against the two alternatives, and the ordering
constraint against `TOOL-aSurfacedLexicon-2` follows from it rather than being a second choice.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the owner's ruling on the dTracedLattice design pass.

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
