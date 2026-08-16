# Review 4 — adversarial pass over the U3 corpus-ids sub-spec

**Serves:** spec-audit TOOL-aFoldedQuarry-5  <!-- inferred: U3, the corpus-ids sub-spec, per the build README's unit table -->

**Scope:** `spec/units/2026-08-08-spec-aFoldedQuarry-5-u3-corpus-ids.md` at rev-1, before any code.
**Method:** ask of each rule "what makes this permanently red, or permanently green, on a tree that
is behaving correctly?" Two findings are that shape and one is a cross-kit dependency the spec did
not notice it was creating.

| # | Severity | Where | Finding |
|---|---|---|---|
| H1 | blocker | §2 S6 rule 1 | keying registry rows on a LINE NUMBER makes the gate red on unrelated edits |
| H2 | blocker | §2 S2 | importing the recall kit's grammar makes memory-tree depend on a kit that need not be installed |
| H3 | high | §2 S7 | "the charter" is a filename this kit never names or configures |
| H4 | medium | §2 S5 | the orphan check may be all-waiver on this corpus, i.e. vacuous |
| H5 | medium | §2 S7 | "one-sided ceiling" needs a stated headroom, or the first commit reds it |
| H6 | low | §2 S3 | the printed index set drops a tracked-but-absent file, which check 16 then flags |

## H1 — a line-number key turns every edit into a gate failure (blocker)

S6 rule 1 asserts set equality between the registry and the measured dead set, and §4 models a row as
`(file, line, cited-path)`. Line numbers move. Insert a paragraph anywhere above a dead citation and
its line number changes, the measured set no longer equals the registry, and rule 1 reds — on an edit
that has nothing to do with the citation. On a corpus that is edited constantly, that is a gate whose
steady state is red, and a gate whose steady state is red gets bypassed.

The row key becomes `(citing-file, cited-path)` with an occurrence COUNT. Both parts are stable under
editing: moving a citation within its file changes nothing, and adding a second dead citation of the
same path in the same file changes the count, which is a real signal. The line number is still
REPORTED, because a human repairing the row wants it — it is just not part of the identity.

## H2 — this makes the memory-tree kit depend on the memory-recall kit (blocker)

S2 says the module imports `ID`, `ID_RE` and the anchor shapes from
`tools/memory-recall/extract.py`. That is the right call for avoiding a second grammar, and it is
also an undeclared cross-kit dependency: `tools/memory-tree/` is a separately deployable kit, and
`WIRE-INTO-PROJECT.md` treats memory-recall as an independent opt-in. An adopter with memory-tree and
no memory-recall gets an `ImportError` from a hygiene gate.

Retyping the grammar is worse — that is the catalogue-drift class S2 is avoiding. So the dependency
is DECLARED and its absence is handled explicitly, with the two states kept apart:

- pins blank → checks 13–16 are off, and the module is never imported. A repo without the recall kit
  simply does not run these checks.
- a pin SET but the grammar module absent → a NAMED error: you armed a check whose grammar is not
  installed. Never a traceback, and never a silent pass, which is the shape a bare `try: import`
  would produce.

`WIRE-INTO-PROJECT.md` and the kit README state the dependency where an adopter will read it.

## H3 — "the charter" is not a name this kit knows (high)

S7 derives the read path from "the charter's own text". This repo's charter is `AGENTS.md`; upstream's
was `CLAUDE.md`; an adopter's may be neither. A hardcoded filename makes check 16 either wrong or
silently empty in most adopting repos — and silently empty is the failure mode that looks like a
pass. `CHARTER` becomes a `.memory-tree.conf` key, defaulting to `AGENTS.md`, and check 16 reports a
named error when the configured charter does not exist rather than deriving an empty read set.

## H4 — the orphan check may be all-waiver here, which is worth knowing BEFORE it ships (medium)

This corpus's decision log cites ids like `TOOL-aWardenGraft-1` that have no build folder and no
spec, so they are cited-never-defined by construction. If most ids land that way, check 14 ships as a
waiver file with a pin and no signal. The measurement is therefore a DELIVERABLE of this unit, not a
by-product: measure first, and if the orphan set is dominated by legitimate id-only decisions, say so
in the journal and leave the pin blank rather than shipping a check whose whole population is waived.

## H5 — a one-sided ceiling still needs a number (medium)

S7 says the read-path total must stay under `READ_PATH_CEILING` and that shrinking never reds. It does
not say what the ceiling is set to. Set at exactly the measured total, the very next sentence added
to any read-path file reds the bar. The ceiling is the measured total plus a STATED headroom, and both
numbers go in the journal, so a future raise is an argument against a recorded figure rather than a
guess.

## H6 — the printed index set silently drops a tracked-but-absent file (low)

`index_set()` filters through `[ -f "$f" ]`, so a file that is tracked but missing from the worktree
does not appear. Check 16 would then see it as a read-path member under no byte cap and flag it,
which is a confusing second symptom of a state check 12 already reports directly. Check 16 skips a
member that is tracked-but-absent and says so, leaving that finding to the check that owns it.

## Disposition

All six folded into rev-2 before any code. H1 re-keys the registry; H2 adds the declared-dependency
rule and its two states; H3 adds the `CHARTER` conf key; H4 makes the measurement a deliverable;
H5 pins the headroom to a recorded number; H6 narrows check 16.
