# Acceptance ledger — TOOL-dLoggedFlight-7

**Serves:** journal TOOL-dLoggedFlight-7

Tier-2 · node d · 2026-09-14 · the build pass of the `Decided:` commit trailer, against spec rev-2,
which needed no change before its code. AC1 and AC3 are OBSERVED. AC2 and AC4 are observed by gate
legs, so each is written as owed to the post-build gate run, beside what this pass saw without
running a leg. No gate leg was run, per the owner's instruction of 2026-09-13, and no suite that
existed under `tools/unattended/` before this build ran.

## The criteria

**Evidences:** TOOL-dLoggedFlight-7

- AC1 — `grep -n 'Decided:' memory/guides/BUILD-METHOD.md` — printed three lines. Line 274 is the
  M9 "decisions taken" row, whose sources now end with the commits' `Decided:` trailers. Line 292 is
  the M10 home, a `Decided: <the choice> — <why>` line per choice in the commit's final trailer block
  beside `Co-Authored-By:`. Line 294 is M10's example. The same grep over the method at the pass's
  parent commit printed nothing.
- AC2 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` and `bash tools/check-template-size.sh`
  — OWED to the post-build gate run, which records the `kit/dogfood doc parity` and
  `build-method size` verdicts. What this pass observed: `--render` rewrote the four live copies from
  their templates, and the resulting diff touched line 1 of `memory/HYGIENE.md`,
  `memory/TEMPLATE-SPEC.md` and `memory/guides/ANNOTATION-STYLE.md` and, in the method, exactly the
  lines the template's own diff touched, so no drift that predated the pass was overwritten. `wc -c`
  read the rendered method at 26733 bytes: under its 27648 row by 915, under its recorded high-water
  of 26941, and 339 lines against the 350 the method states. The addition is 294 bytes against the
  300 the spec's risks line allows; the first draft read 308, and the M9 row's clause was shortened.
- AC3 — `git log --format='%(trailers:key=Decided,valueonly)'` — a scratch arm, a script kept
  outside the tree, read M10's section out of the rendered method and took its one backticked
  `Decided: ` span with no placeholder as the example. In a throwaway repository, the example in the
  final trailer block beside `Co-Authored-By:` printed exactly the example's value. The same line
  mid-body, above a paragraph break, printed nothing, while `%(trailers:key=Co-Authored-By,valueonly)`
  on that commit printed its value and `%B` held the line, so the empty answer is the placement and
  not a probe that cannot print. Two `Decided:` lines in one final block came back as two values, in
  order. The unrendered template gave the same seven passes. RED seen six ways: the method at the
  parent commit, which has no example; the example wrapped across two lines; the example replaced by
  a placeholder form; the example carrying trailing blanks, which git trims (three arms); the
  positive commit with a paragraph break between the example and `Co-Authored-By:`; and the negative
  commit with the example in its final block. The arm encodes M10's placement as written and does
  not parse the placement sentence, so a rewording of that sentence which kept the example would not
  be seen by it.
- AC4 — `bash tools/check-kit-versions.sh` — OWED to the post-build gate run, which records the
  `kit version markers` verdict. What this pass observed: outside the build records,
  `git grep 'memory-tree@2\.69\|MEMORY_TREE_VERSION=2\.69'` printed nothing after the move, and the
  2.70 marker stood once in each of nine carriers: the engine constant's line in
  `tools/memory-tree/check-memory-hygiene.sh`, line 1 of the four `tools/memory-tree/*.template.md`,
  and line 1 of their four renders.

## What else the pass carried

- The kickoff manifest's `last-audit` moved to this pass's local time at the same merge-base, because
  the commit touches two watched paths, `tools/memory-tree/check-memory-hygiene.sh` and
  `memory/guides/BUILD-METHOD.md`. No §B line changed: §B points at the method and restates nothing
  M9 or M10 now say.
- The build-method dossier gains a Gaps bullet: the trailer home is ungated by design, and a later
  edit to M10's example is graded by nothing.
- The verdict-epoch rule: `git log 9fac2b53..HEAD` over the engine and its six delegates printed no
  commit before this one, so this commit is both the newest bump of `KIT_MEMORY_TREE_VERSION` and the
  newest engine line moved in the range.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `kit/dogfood doc parity`, `build-method size` and `kit version markers`;
- `method carriers (every pointer declared)`, `unattended kit gate` and `memory hygiene`;
- `verdict epoch (kit version dates the engine)`, which section 7 does not name and which grades the
  bump this commit makes.
