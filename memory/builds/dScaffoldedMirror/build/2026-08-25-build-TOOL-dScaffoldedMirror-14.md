# TOOL-dScaffoldedMirror-14 — build record

**Serves:** journal TOOL-dScaffoldedMirror-14

Node `d`, 2026-08-25, base `500a5db6`, unattended run `dScaffoldedMirror`. Spec:
`../spec/2026-08-24-spec-dScaffoldedMirror-14.md`, built at rev-2.

## Result

**`VERB_OFFENDER_PIN` 463 → 384, and it is the first downward move this key has ever made.** The four
entries above it in `.lexicon.conf` are raises. Seventy-nine offenders left the set by being RENAMED
rather than absorbed:

| move | count | why it cost nothing |
|---|---|---|
| `t_*` → `test_*` | 52 | `test` was already a declared row meaning exactly that |
| `do_*` → `cmd_*` | 22 | converged on the spelling govkit already used |
| govkit's existing `cmd_*` | 5 | already the target spelling; one new reserved row admitted them |

The pin lands at **384**, not rev-1's predicted 380. rev-1 measured from a 459 baseline and the live
one was 463, so exactly 79 keys left the set as stated and the four-point gap is the baseline rather
than the work.

## The defect this unit found is the defect this unit is about

The `cmd` row was first written across TWO indented lines, for readability. **The block grammar reads
every indented line as a row, so a phantom verb `down` entered the declared table** — and the pin
still read 384, because `down` leads no identifier anywhere in the corpus. A vocabulary that grew by
accident, in the unit whose whole subject is that the vocabulary must not grow by exception.

**What would have caught it, and what that is worth.** `lexicon_verbs_declared_but_unused` DID see it
— 1 of 24 — and its pin is 3, so it would have REPORTED the phantom and refused nothing. The guard
exists, it was awake, and it was under its pin. That is the honest reading: this was found by
diffing the declared verb set against `HEAD` before committing, not by a gate.

Recorded because the same shape is available to anyone editing `VERBS`: a gloss that wraps is a
second row.

## What is NOT renamed, and why (S7)

- **govkit's five `cmd_*`** are already the target spelling. They were offenders only because `cmd`
  was undeclared; declaring it admitted them without an edit.
- **`.lexicon.conf`'s pin archaeology** — roughly seventy lines of dated notes about past raises,
  three of which name identifiers this unit deleted. They record what was true when written, and
  `TOOL-dScaffoldedMirror-9` removes the block entirely. Churning a file scheduled for deletion is
  work nobody banks.
- **Frozen records under `memory/`** that cite `do_*`. A record is not rewritten to match a later
  rename; that is the supersession rule applied to prose.
- **The remaining 384 keys.** They are `-9`'s grandfather set and `-8`'s canon work. A unit that
  starts renaming on judgment does not stop at a defensible line.

## A stale comment the rename turned into nonsense

`tools/memory-recall/selftest.py` carried four lines explaining that three arms were deliberately
`t_*`-inconsistent with their siblings and that "renaming the siblings is that kit's shrink work, not
this unit's". The rename turned it into a claim that these are `test_*` where every sibling is
`test_*`. Deleted with the state it described, which is what S2 asked for.

**Evidences:** TOOL-dScaffoldedMirror-14
- AC-S1 — `grep -cE "^def t_"` over both selftests returns 0, and `test_` definitions number 58 (52 renamed plus 6 pre-existing); `python tools/memory-recall/selftest.py` and `python tools/codebase-map/selftest.py` both exit 0
- AC-S2 — the four-line deliberate-inconsistency comment is absent from `tools/memory-recall/selftest.py`, and the state it described is gone
- AC-S3 — `bash tools/lexicon/adopt-lexicon.sh --check` reports `23 verb(s) declared`, and a diff of the declared set against `HEAD` shows exactly one addition, `cmd`
- AC-S4 — `grep -cE "^def do_"` over `tools/memory-tree/*.py` returns 0 and `cmd_` definitions number 22; `python tools/memory-tree/gen_build_index.py --selftest` exits 0
- AC-S5 — `python tools/lexicon/lexicon.py --measure` prints `VERB_OFFENDER_PIN="384"`, and the conf carries its `463 -> 384` marker within the ratchet's window; `python tools/drift-audit/drift_report.py --check` exits 0
- AC-S6 — `grep -c '"do_' memory/map/generated/symbols.json` returns 0, down from 22, after `python tools/codebase-map/gen_map.py --write`
- AC-S7 — this record's "What is NOT renamed" section, four items with their reasons
