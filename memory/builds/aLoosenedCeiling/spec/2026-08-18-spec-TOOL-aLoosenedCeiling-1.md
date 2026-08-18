# TOOL-aLoosenedCeiling-1 — the read-path headroom becomes a declaration, and its default rises

**Status:** OPEN · rev-2 · 2026-08-18 · node a · Tier-2 · base 6382c564 · streams tooling

## 1. Goal

`corpus_ids.py --measure` tells every adopter what to write into `READ_PATH_CEILING`, and the
headroom half of that arithmetic is a constant in this repo's copy of the kit. Make it a
`.memory-tree.conf` declaration, and raise the shipped default from 20480 to 25600 bytes.

## 2. Scope (IN)

- **S1** — `load_conf` gains `READ_PATH_HEADROOM` with the shipped default `25600`. The key must
  be present in that defaults dict whatever else happens: every consumer indexes `conf` directly,
  so a key the dict does not carry is a `KeyError` rather than a missing setting.
- **S2** — `do_measure` reads the declaration instead of its own literal, and the comment it prints
  beside the number continues to name both halves of the sum, so the written pin still carries its
  own derivation.
- **S3** — a value that is neither blank nor a whole number of bytes raises the module's named
  `Problem`, never a `ValueError` traceback. Blank means "use the shipped default", because the key
  is a formatting input to one report and there is no coherent "off" state for it.
- **S4** — `--selftest` gains arms in BOTH directions over ONE fixture: the printed ceiling equals
  the measured total plus 25600 when the key is absent, equals the measured total plus the declared
  value when it is set to something else, and a malformed value is refused by name.
- **S5** — the shipped `tools/memory-tree/.memory-tree.conf.example` declares the key, commented in
  the register that file already uses, and `tools/memory-tree/HYGIENE.template.md` plus this repo's
  installed `memory/HYGIENE.md` describe check 16's budget as measured-plus-declared-headroom.
- **S6** — `KIT_MEMORY_TREE_VERSION` moves, and so does every marker spelling it. The verdict-epoch
  leg counts an added or removed line whose first non-space character is not a comment marker, in
  the engine OR in its declared delegates, and `corpus_ids.py` is one of those delegates. The
  spellings are the constant and its inline marker, the three shipped template headers, and the
  three live copies rendered from them — and the live copies move only through the parity
  harness's render mode, never by hand.

## 3. Non-goals (OUT)

- The ceiling ENFORCEMENT path is untouched. Check 16 keeps comparing the summed read path against
  `READ_PATH_CEILING` and knows nothing about headroom. Headroom is advice `--measure` gives an
  author. Letting the gate compute a ceiling from a headroom would let a growing corpus raise its
  own budget, which is the ratchet inverted.
- No change to `read_set`, so which files count as read-path members is exactly as before.
- No change to `READ_PATH_WAIVER` semantics.
- This unit does not move any repo's `READ_PATH_CEILING`. That is unit 3 for this repo and unit 4
  for the adopter. Keeping them separate is what lets a reviewer see the knob and the turning of
  the knob as two decisions.

## 4. Design

### Data model

One key, one integer, one consumer.

| key | shipped default | read by | blank |
|---|---|---|---|
| `READ_PATH_HEADROOM` | `25600` | `do_measure` only | falls back to the shipped default |

The default is a module constant rather than a bare literal inside the defaults dict, because the
selftest asserts against it, and an arm that re-types the number it is checking proves nothing
about the number the code uses.

### Why the default moves 20480 to 25600

20480 was the figure the first read-path pin was written with, and it has been re-typed into every
`--measure` run since. It is 20 KiB against a corpus whose largest single member is now a 25036 B
guide. One binding document landing consumes more than the whole allowance, which is exactly what
happened here twice: this repo has 82 bytes of headroom left, and the adopter surveyed by unit 4
has 2. A headroom smaller than the corpus's largest member cannot absorb the arrival of one more
member of that class, and absorbing that is the only thing headroom is for. 25600 is 25 KiB, one
tier up on the same binary scale the neighbouring caps use, and it exceeds the largest present
member. It is the owner's number. This paragraph records the measurement that supports it.

### Inventory

`do_measure` has no selftest coverage at all today: no arm in `--selftest` reaches it, and the
constant this unit replaces has therefore never been exercised. S4 is the first coverage of that
function rather than an extension of existing coverage, which is why it is written as three arms
over one fixture rather than as an assertion bolted to an existing one.

The unit adds no PUBLIC module-level name. The codebase map indexes public top-level definitions
under the tool root and byte-compares its generated inventory, so a new public function here
would red the map's freshness leg until the map is re-rendered and the key claimed by a dossier.
The default belongs in a module constant and the parsing belongs inside `do_measure`, which
keeps the public surface unchanged.

### Migration

An absent key means the shipped default, so every adopter tree keeps working with no edit. An
adopter who wants the old figure writes it into their conf. Nothing recomputes an existing
`READ_PATH_CEILING`: a pin already written is a recorded decision, and this unit does not rewrite
recorded decisions.

### Files touched (estimate)

- `tools/memory-tree/corpus_ids.py` — the default constant, `load_conf`, `do_measure`, `--selftest`.
- `tools/memory-tree/.memory-tree.conf.example` — the declaration and its comment.
- `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md` — check 16's description.
- `.memory-tree.conf` — the key, declared at this repo's chosen value.
- `tools/memory-tree/check-memory-hygiene.sh`, the three `*.template.md` headers in the kit, and
  the three live copies re-rendered from them.

### Alternatives rejected

- **Blank means print no headroom.** Rejected. `--measure` exists to print a pin an author can
  paste, and a ceiling equal to the measured total reds on the next byte added. The review record
  cited in section 10 already established that as the wrong answer.
- **Derive headroom as a percentage of the measured total.** Rejected. It grows the allowance
  exactly as the corpus grows, so the budget stops being a budget. This is veto 1 of the fork rule:
  the option fails the one property the ceiling exists to have.
- **Silently default a malformed value.** Rejected. An adopter who typed a headroom and got the
  shipped one believes they chose. The module docstring already commits to named errors over
  tracebacks and over silent fall-through.

## 5. Production-readiness checklist

- security — N/A. No new input reaches a shell, a path or a subprocess; the value is parsed as a
  decimal integer and used in arithmetic.
- perf / scale — N/A. One integer parse per `--measure` run.
- a11y — N/A. A command-line report.
- i18n — N/A. A command-line report in one language.
- error / empty / loading states — the blank and malformed cases are S3, and both are armed by S4.
- observability — the printed comment continues to name the measured total and the headroom
  separately, so a written pin still shows its own derivation to the next reader.
- risks — the one reachable failure is a malformed declaration, refused by name. No concurrency, no
  data loss, no write path. Rollback is deleting the key.
- testing + left-shift gates — S4's both-directions arms. The malformed-value arm is the left-shift
  for the class this repo records as a fixture that passes by finding nothing.
- migration / rollback — covered under Design. An absent key is the pre-change behaviour except for
  the default's new value, which is the point of the unit.
- user docs — S5's three carriers.

## 6. Acceptance criteria

- **AC1** — When this repo's conf declares no headroom, `python tools/memory-tree/corpus_ids.py
  --measure` prints a `READ_PATH_CEILING` equal to the measured read path plus 25600, and its
  trailing comment names both halves.
- **AC2** — When a fixture tree declares a headroom other than the default, `--measure` over that
  tree prints the measured total plus that value, and the same fixture with the key removed prints
  the measured total plus 25600. Both are arms in `python tools/memory-tree/corpus_ids.py
  --selftest`.
- **AC3** — When a fixture declares a non-numeric headroom, `python tools/memory-tree/corpus_ids.py
  --selftest` observes the named refusal text and no traceback.
- **AC4** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, the edited
  `HYGIENE.template.md` and the installed `memory/HYGIENE.md` still agree.
- **AC5** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs over this unit's diff it is
  green, which requires `KIT_MEMORY_TREE_VERSION` and its markers to have moved with the code.

## 7. Gates

`python tools/memory-tree/corpus_ids.py --selftest` · `bash
tools/memory-tree/check-memory-hygiene.sh` · `bash tools/memory-tree/check-verdict-epoch.sh` ·
`bash tools/check-kit-versions.sh` · `bash tools/memory-tree/kit-dogfood-parity.test.sh` · `bash
tools/memory-tree/hygiene-parity.test.sh` · `python tools/codebase-map/test_codebase_map.py` ·
`python tools/drift-audit/drift_report.py --check` · `bash tools/check-testsuite-counts.sh` · and
`GATE_FULL=1 bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none — the default's value was chosen by the owner at kickoff, and the measurement supporting it is
recorded in section 4.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the pre-build survey. Three corrections, none to the design: the
  defaults dict entry is load-bearing rather than tidy (S1); the verdict-epoch leg watches the
  delegates too and the live doc copies move only through the render mode (S6); and `do_measure`
  has no existing coverage, so S4 is first coverage (Inventory). The ceiling-value carriers the
  survey found — a backlog row and a docstring example — moved to unit 3, which owns that number.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declare a numeric gate threshold in the project conf
instead of a script constant"` returns `load_conf` in `tools/memory-tree/row_grammar.py` at fan-in
15 as the top seam, with `corpus_ids.py`'s own `load_conf` the sibling this unit extends. The seam
this unit wires through is therefore that defaults dict: one more key in an existing loader, not a
new configuration mechanism.

`python tools/memory-recall/query.py "why is READ_PATH_CEILING measured rather than defaulted, and
what governs raising it per adopter" --terms "READ_PATH_CEILING read path ceiling headroom measured
pin adopter corpus_ids check 16 raise ratchet rotation"` returned the governing prior art. The
`aFoldedQuarry` unit-5 review record establishes that the ceiling is the measured total plus a
STATED headroom with both numbers journalled; this unit turns "stated" into "declared", which is
the same rule with a carrier a gate can read. `TOOL-aWidenedGuide-1` establishes that check 16's
byte budget is the real one and is not relaxed when a line cap is, and that constraint is
preserved, since this unit touches neither check 16's comparison nor any line cap.
`TOOL-aDeclaredCeiling-1` records that declaring a threshold in the conf, rather than holding it as
a shell constant, is this repo's established answer for exactly this shape.
