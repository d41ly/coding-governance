# TOOL-aLoosenedCeiling-2 — check 6's per-class caps become adopter declarations

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 6382c564 · streams tooling

## 1. Goal

Check 6 caps a memory-tree index file by class, and all six numbers behind those classes are
literals inside one awk program. Move them to `.memory-tree.conf` at their present values, so an
adopter can set the per-member ceiling that check 16 rule 3 cross-references without editing a
kit script they re-pull on every update.

## 2. Scope (IN)

- **S1** — six keys, defaulted to the values check 6 uses today, declared beside the other shell
  defaults so the conf source overrides them the same way it overrides `DISCIPLINES`.
- **S2** — the awk program receives all six through `-v` bindings and holds no cap literal.
- **S3** — a cap that is not a whole number, or a BYTE cap of zero, aborts the whole script with a
  named message naming the offending key or keys. It is not a check failure: a gate that cannot
  read its own thresholds has not found a hygiene regression, it has failed to run.
- **S4** — validation happens once, at conf load, ahead of the print modes, so the sibling that
  asks this script for the index set fails identically rather than receiving a set derived under a
  conf the gate itself would refuse.
- **S5** — a line cap of zero keeps its present meaning of no independent line cap. That is what
  the build-README class already uses, and generalising it to every class is free.
- **S6** — `check-memory-hygiene.test.sh` gains arms in BOTH directions over ONE fixture file: it
  passes at a loose declared cap and reds at a tight one, for each of the three classes, plus an
  arm for the malformed-cap refusal.
- **S7** — the shipped `.memory-tree.conf.example`, `tools/memory-tree/HYGIENE.template.md` and
  this repo's installed `memory/HYGIENE.md` describe check 6's caps as declarations with these
  defaults, rather than as fixed numbers.
- **S8** — `KIT_MEMORY_TREE_VERSION` and its markers move, because non-comment lines of the engine
  move.

## 3. Non-goals (OUT)

- No cap's DEFAULT changes. Every adopter who declares nothing keeps the exact thresholds they have
  today. This unit adds a knob and does not turn it; the pin movements are units 3 and 4.
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

awk compares an unset or non-numeric `-v` binding as a string. A conf carrying a typo would not
red: it would silently compare every file against zero, or against a string, and the gate would
either red on everything or red on nothing with no message pointing at the conf. Both readings are
worse than a stop. The script already owns this shape for the case where no python launcher
resolves: it prints why and leaves with a distinct status rather than reporting a clean tree. A
malformed cap is the same category and gets the same treatment, which also keeps the branch out of
the harness meta-gate's population, since that gate counts check failures and this is not one.

A zero BYTE cap is rejected because it reds every file in its class and reads as a
misconfiguration, never an intent. A zero LINE cap is accepted because it already has a meaning.

### Inventory

The awk program at present derives `cb` and `cl` from three literals-bearing branches. After the
change it derives them from six `-v` names and the same three branches, so the control flow is
byte-for-byte the same shape and only the source of the numbers moves.

### Migration

Every adopter conf that declares none of the six keys behaves identically. There is no retrofit and
no re-measure.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh` — the six defaults, the validation, the awk bindings,
  the kit version constant.
- `tools/memory-tree/check-memory-hygiene.test.sh` — S6's arms and its assertion count.
- `tools/memory-tree/.memory-tree.conf.example` — six declarations and their comment.
- `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md` — check 6's description.
- Kit version marker carriers.

### Alternatives rejected

- **One declaration parsed into a table**, such as a single key holding class-to-cap pairs.
  Rejected: it invents a parser and a grammar for six integers, and every other threshold in this
  conf is one key holding one number.
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
  deleting the keys from the conf, which restores the defaults.
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
- **AC2** — When a fixture declares a non-numeric cap, or a byte cap of zero, the script leaves
  with its distinct cannot-run status and prints the offending key name, and
  `bash tools/memory-tree/check-memory-hygiene.test.sh` observes that text.
- **AC3** — When no key is declared, this repo's `bash tools/memory-tree/check-memory-hygiene.sh`
  is green and its check 6 verdict is identical to the verdict at this unit's base commit.
- **AC4** — When `bash tools/check-testsuite-counts.sh` runs, the hygiene suite's printed assertion
  count has risen by the arms S6 added and still meets its floor.
- **AC5** — When `python tools/memory-tree/check-arms.py` runs, the branch and armed counts for
  `tools/memory-tree/check-memory-hygiene.sh` still meet their declared floors, which the abort
  design of S3 is what preserves.
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

## 10. Reuse audit

Satisfied for the set by unit 1's section 10; the same two probes cover both units and the method
requires the audit once per set rather than once per spec. The seam this unit extends is the block
of shell defaults that `check-memory-hygiene.sh` declares immediately before it sources the conf —
the same mechanism that already makes `DISCIPLINES`, `FAMILIES`, `TOMBSTONE_ROOTS` and the three
cutoff dates adopter-owned. No new configuration mechanism is introduced, and the recall probe
surfaced `TOOL-aWidenedGuide-1` as the decision that created the class split these keys preserve.
