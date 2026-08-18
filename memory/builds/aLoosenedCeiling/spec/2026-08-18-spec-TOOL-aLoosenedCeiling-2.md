# TOOL-aLoosenedCeiling-2 — check 6's per-class caps become adopter declarations

**Status:** OPEN · rev-3 · 2026-08-18 · node a · Tier-2 · base 6382c564 · streams tooling

## 1. Goal

Check 6 caps a memory-tree index file by class, and all six numbers behind those classes are
literals inside one awk program. Move them to `.memory-tree.conf` at their present values, so an
adopter can set how large a single member of each class may grow without editing a kit script they
re-pull on every update. The per-class cap is a SEPARATE constraint from the aggregate read-path
ceiling: check 16 rule 3 asks only whether a file is IN the capped set, never what the cap is, and
the first draft of this goal said otherwise.

## 2. Scope (IN)

- **S1** — six keys, defaulted to the values check 6 uses today, declared beside the other shell
  defaults so the conf source overrides them the same way it overrides `DISCIPLINES`.
- **S2** — the awk program receives all six through `-v` bindings and holds no cap literal.
- **S3** — a cap that is not a whole number, or a BYTE cap of zero, aborts the whole script: it
  prints a message naming the offending key and its value on STDOUT and exits 2, the same channel
  and status the no-python abort already uses. Both halves are stated because both are load-bearing
  and neither is obvious: the harness captures stdout with stderr discarded and does not read the
  status, so a builder who chose stderr would write an arm that observes nothing and passes. It is
  not a check failure — a gate that cannot read its own thresholds has not found a hygiene
  regression, it has failed to run.
- **S4** — validation happens once, at conf load, ahead of the print modes. The reason is FAIL-FAST
  PROPAGATION, not a differently-derived set: the index set is built from the memory root, the
  tracked file list and the map sub-path alone, so it cannot vary with a cap value. What the early
  abort buys is that the non-zero exit reaches the sibling classifier, which converts it into its
  own named refusal rather than proceeding on a conf this script would not accept. The first draft
  gave the wrong reason for the right placement.
- **S5** — a line cap of zero keeps its present meaning of no independent line cap. That is what
  the build-README class already uses, and generalising it to every class is free.
- **S6** — `check-memory-hygiene.test.sh` gains arms in BOTH directions PER CLASS: one fixture file
  per class, silent at a loose declared cap and named at a tight one. The harness runs the gate
  ONCE per tree into one captured variable, so each declared-cap setting needs its own scratch tree
  or its own re-run, and the malformed-cap arm cannot share a tree with any other assertion because
  the abort ends the run. It also needs its own capture, since the shared idiom discards the status
  and stderr.
- **S6b** — two arms for the build-README tier that do NOT involve the knob, because the knob is
  not what was missing. One file over the 25600 default with no key declared, and one proving a
  zero line cap means NO line cap rather than everything reds. The Inventory gap is about the
  DEFAULTS being unexercised; arms that only vary a declared value would leave it exactly as open.
- **S7** — the shipped `.memory-tree.conf.example`, `tools/memory-tree/HYGIENE.template.md` and
  this repo's installed `memory/HYGIENE.md` describe check 6's caps as declarations with these
  defaults, rather than as fixed numbers.
- **S8** — `KIT_MEMORY_TREE_VERSION` and its markers move, because non-comment lines of the engine
  move. Unit 1 states the mechanics AND the ordering, which is the part that matters: the leg is
  topological, so this unit's engine change lands BEFORE the commit carrying the bump. Delegating
  without saying which commit carries it was how the first draft would have redded that leg.
- **S9** — check 6's failure message is not reworded. Its full literal signature is what arms the
  check in the harness meta-gate, and the arm names that text; the message keeps saying which cap
  was applied, which is what makes a declared-cap arm assertable at all.

## 3. Non-goals (OUT)

- No cap's DEFAULT changes. Every adopter who declares nothing keeps the exact thresholds they have
  today. This unit adds a knob and NO unit in this build turns it — units 3 and 4 move read-path
  CEILINGS, which are a different number, and the first draft implied they were this unit's pin
  movements. Turning a per-class cap is outside the owner's ask.
- No upper BOUND on a declared cap. An aggregate ceiling only measures anything while it binds
  tighter than the sum of the per-class caps over the read-path members, and nothing here enforces
  that relation. It is not crossed in this repo, and unit 4 documents an adopter where the ratio is
  the live question. Recorded as a known limit of the knob rather than left for an adopter to find.
- No new class. The three classes and the file patterns that select them are unchanged.
- Check 7's entry budget, check 6's grandfather list and the map-dossier exemption are untouched.
- Check 16 is untouched. It asks this script which files are capped and does not care what the cap
  is, which is why the two units are separable at all.

## 4. Design

### Data model

| key | default | class it caps |
|---|---|---|
| `INDEX_CAP_BYTES` | 20480 | every row document in the index set |
| `INDEX_CAP_LINES` | 250 | the same |
| `GUIDE_CAP_BYTES` | 61440 | a file directly under the guides directory |
| `GUIDE_CAP_LINES` | 750 | the same |
| `BUILD_README_CAP_BYTES` | 25600 | a build folder's own README |
| `BUILD_README_CAP_LINES` | 0 | the same; zero means no independent line cap |

The class split itself is a recorded decision — a guide is prose read end to end, an index is rows
a curation sweep prunes — and this unit preserves it exactly. What it changes is who owns the
numbers.

### Why validate, and why aborting rather than failing

The two failure modes are OPPOSITE, and the first draft of this paragraph had them backwards.
Measured on this node's awk: an UNSET or EMPTY binding compares numerically against zero, so every
file in the class exceeds its cap and the gate reds on everything. A NON-NUMERIC binding compares
as a string, so nothing exceeds its cap and the gate reds on NOTHING. The second is the dangerous
one — a typo in the conf produces a silent green, which is this repo's own fixture-passes-by-
finding-nothing class arriving through a config file. Neither prints anything pointing at the conf.
Both are worse than a stop. The script already owns this shape for the case where no python launcher
resolves: it prints why and leaves with a distinct status rather than reporting a clean tree. A
malformed cap is the same category and gets the same treatment, which also keeps the branch out of
the harness meta-gate's population, since that gate counts check failures and this is not one.

A zero BYTE cap is rejected because it reds every file in its class and reads as a
misconfiguration, never an intent. A zero LINE cap is accepted because it already has a meaning.

### Inventory

The awk program at present derives `cb` and `cl` from three literal-bearing branches. After the
change it derives them from six `-v` names and the same three branches, so the control flow keeps
its shape and only the source of the numbers moves.

Two measured facts shape the arms. First, the harness meta-gate scores this engine at nineteen
branches and nineteen armed. Check 6 has TWO failure call sites, not one: the cap branch and a
stale-line guard on the grandfather registry. The cap branch is the one this unit touches, and the
awk parameterization adds no third — which is the whole reason S3 aborts rather than failing a
check. The count matters for S9, because the meta-gate keys a signature per call site. Second, the existing check-6 arms are unaffected: every scratch conf in the
harness declares none of the six keys, so the engine's built-in defaults apply and the fixtures
tuned to 760, 400 and 265 lines keep their present verdicts.

The gap S6 closes is real and already recorded against this repo: there is NO arm anywhere today
for the build-README tier — neither its byte cap nor the absence of a line cap is exercised. A
prior review filed that as a medium finding. Making the tier declarable without arming it would
leave the same hole with a knob on it.

The suite's assertion floor is a minimum rather than an equality, so added arms need no floor
edit; the count itself is derived by the harness, not written.

### Migration

Every adopter conf that declares none of the six keys behaves identically. There is no retrofit
and no re-measure.

One adopter is worth naming because it is the case that motivates the unit. The NicoCares package
repo carries a hand-maintained fork of this awk block — a single flat tier replacing the three
classes — tagged as a carve-out its own source instructs the next adopter to re-apply on every
kit release. These keys are exactly what would let that ruling be a declaration instead of a
fork. Unit 4 does not perform that re-adopt, and says why.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh` — the six defaults, the validation, the awk bindings,
  the kit version constant.
- `tools/memory-tree/check-memory-hygiene.test.sh` — S6's arms and its assertion count.
- `tools/memory-tree/.memory-tree.conf.example` — six declarations and their comment.
- `tools/memory-tree/HYGIENE.template.md` — check 6's description, in the THREE places one file
  states the same row-document cap, plus the build-README class it omits entirely. `memory/HYGIENE.md`
  moves only as the render of that template, never edited directly.
- `tools/memory-tree/check-memory-hygiene.sh`'s own comment block above the awk, which restates
  all three tiers about forty lines from the code that owned them, and the sentence deriving the
  guide cap as three times the row cap — a relation that holds only while both keys keep their
  defaults, and which becomes false the moment an adopter uses the knob.
- Kit version marker carriers.

### Alternatives rejected

- **One declaration parsed into a table**, such as a single key holding class-to-cap pairs. It
  would not have to invent a grammar: `tools/template-size-limits.txt` already ships one in this
  repo, path-keyed rows with each value's history beside it, read by the template size gate.
  Rejected on FIT instead: that file is keyed by measured FILE and check 6's caps are keyed by
  CLASS, so the existing shape does not carry them, and every other threshold in this conf is one
  key holding one number.
- **Reporting a malformed cap as a check 6 failure.** Rejected. It would say a hygiene regression
  was found when none was looked for, and it would put an unarmable branch into the meta-gate's
  count.
- **Validating lazily, inside check 6.** Rejected by S4: the print modes return before check 1, so
  a sibling gate would get an index set computed under a conf this script would have refused.

## 5. Production-readiness checklist

- security — the six values are interpolated into an awk `-v` binding, so the validation that
  rejects a non-numeric value is also what keeps a conf value out of awk's parser. That is the
  reason it runs before use rather than after.
- perf / scale — N/A. Six regex matches at startup; the awk program is unchanged in complexity.
- a11y — N/A. A gate that prints text.
- i18n — N/A.
- error / empty / loading states — the malformed and zero-byte cases are S3, armed by S6.
- observability — the refusal names the offending key and its value, so the operator edits the
  right line without reading the script.
- risks — the failure mode this unit exists to prevent is a silently wrong comparison. Rollback is
  deleting the keys from the conf, which restores the defaults. The risk it CREATES is the unbounded
  cap in section 3: an adopter can raise a per-class cap until the aggregate ceiling can no longer
  fire before check 6 does, at which point check 16 measures nothing. Unit 4 states that condition
  arithmetically for the one adopter where it is close, and this is the sentence that carries it
  back to the unit that creates the possibility.
- testing + left-shift gates — S6's both-directions arms are the left-shift. A one-directional arm
  over a cap knob is the class this repo records as a fixture that passes by finding nothing: a
  fixture under every cap passes whatever the cap says.
- migration / rollback — no migration; see Design.
- user docs — S7's three carriers.

## 6. Acceptance criteria

- **AC1** — When a fixture tree declares a byte cap tighter than a file in that class,
  `bash tools/memory-tree/check-memory-hygiene.sh` reports check 6 against that file; when the same
  fixture declares a cap looser than the file, it is silent. Both directions, per class, are arms
  in `bash tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC2** — When a fixture declares a non-numeric cap, or a byte cap of zero, the script exits 2
  and prints the offending key on stdout, and `bash tools/memory-tree/check-memory-hygiene.test.sh`
  observes BOTH the status and the text through its own capture rather than the shared one.
- **AC3** — When a fixture file sits between the row-document cap and the guide cap, `bash
  tools/memory-tree/check-memory-hygiene.test.sh` observes check 6 naming it under a declared
  tight cap and silent under a declared loose one, over the same fixture. The first draft asserted
  only that this repo stays green, which any looser cap also produces.
- **AC4** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, it prints an executed
  assertion count at least eight above its previous floor, and that floor rises in the same commit.
  The first draft named `tools/check-testsuite-counts.sh`, which RUNS NOTHING — it greps the suite
  file for the shape of a count — so the criterion was green whether S6 added six arms or zero.
- **AC5** — When `python tools/memory-tree/check-arms.py` runs, no branch of
  `tools/memory-tree/check-memory-hygiene.sh` has become unarmed and check 6's cap-branch signature
  is unchanged. The floors alone do not discriminate: they are one-sided upward, so a failure-based
  design would have met them too.
- **AC6** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs over this unit's diff it is
  green, which requires the kit version constant and its markers to have moved.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `bash
tools/memory-tree/check-memory-hygiene.test.sh` · `python tools/memory-tree/check-arms.py` · `bash
tools/memory-tree/check-verdict-epoch.sh` · `bash tools/check-kit-versions.sh` · `bash
tools/memory-tree/kit-dogfood-parity.test.sh` · `bash tools/memory-tree/hygiene-parity.test.sh` ·
`python tools/memory-tree/corpus_ids.py --selftest` · `bash tools/check-testsuite-counts.sh` ·
`python tools/codebase-map/test_codebase_map.py` · `python tools/drift-audit/drift_report.py
--check` · and `GATE_FULL=1 bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the pre-build survey. The abort-rather-than-fail choice in S3 is
  confirmed by measurement rather than assumed (Inventory); S9 added, because the failure message
  is an armed signature and rewording it silently breaks the arm; the doc carriers were found to
  be more numerous and one of them derivational rather than literal (Files touched); and the
  adopter whose fork this unit dissolves is named in Migration.
- rev-3 · 2026-08-18 · folded spec-audit round 1. The goal claimed check 16 rule 3 cross-references
  the cap value; it reads only set membership. AC4 named a leg that runs nothing, and AC3 and AC5
  were satisfied by an unchanged tree. S3 gained the channel and status the arm needs, S4 the right
  reason for its placement, S6 the invocation count and S6b the default-tier arms the Inventory gap
  actually asks for. The awk failure modes in section 4 were stated backwards: the silent-green one
  is the non-numeric binding. Check 6 has two failure call sites, not one.

## 10. Reuse audit

Satisfied for the set by unit 1's section 10; the same two probes cover both units and the method
requires the audit once per set rather than once per spec. The seam this unit extends is the block
of shell defaults that `check-memory-hygiene.sh` declares immediately before it sources the conf —
the same mechanism that already makes `DISCIPLINES`, `FAMILIES`, `TOMBSTONE_ROOTS` and the three
cutoff dates adopter-owned. No new configuration mechanism is introduced, and the recall probe
surfaced `TOOL-aWidenedGuide-1` as the decision that created the class split these keys preserve.
