# TOOL-aEvidencedLens-11 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-11

The carriers now state what units 1 to 9 built. The method was rendered with
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, run as the renderer, and the Skill and
the verbs entry with `bash tools/unattended/adopt-unattended.sh`. Each criterion's RED side was read
at BASE `028b5cac` with `git show 028b5cac:<path>`, since this unit adds no gate clause to stage a
break against.

**Evidences:** TOOL-aEvidencedLens-11
- AC1 — `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` printed `template-size OK` (28151 / 30720, with the advisory high-water warning BASE also printed), and `wc -c < memory/guides/BUILD-METHOD.md` printed 28151, at most the pinned 28169. The first render measured 28229 and was trimmed before landing.
- AC2 — `grep -c 'FOLDED into its spec'` printed 0 over both the template and the render (1 at BASE), `grep -c 'SPEC_LENSES'` printed 1 over both (0 at BASE), and `grep -cE 'underspecification|unstated assumption'` printed 0 over both (1 at BASE). Over the render, M4 line 133 carries `read-only` and `scratch` in one sentence, `grep -c 'a round that is not an exit'` printed 1, `grep -c "a review's minors batch"` printed 1 and `grep -c "the closing review's minors batch"` printed 0.
- AC3 — `grep -nE 'underspecification|unstated assumption|prior art' tools/memory-tree/README.md` printed nothing (3 lines at BASE) and `grep -c 'SPEC_LENSES' tools/memory-tree/README.md` printed 1.
- AC4 — `bash tools/unattended/adopt-unattended.sh --check` printed `in sync`. The AC4 alternation grep over the four carriers printed nothing, against 3 lines in each at BASE, and the Skill's `CONVERGING` bullet opens its second line with "On a SPEC subject the fold fixes what that round confirmed".
- AC5 — `git diff 028b5cac -- memory/DECISIONS.md` shows one added line and no removed line (numstat `1 0`). The line is the main loop's `TOOL-aEvidencedLens-17` row from commit `6da1829a1`, 288 bytes, naming `TOOL-aProbedUnit-9` and carrying `2026-10-05`.
- AC6 — `git grep -nIiE 'MEDIUM or LOW is FOLDED|FOLDED into the spec|four lenses|ACCEPTED there, never|is ACCEPTED, never required'` with §4's exclusions plus `':!memory/gotchas'` (rev-3) printed no line in a file this unit owns. It printed three lines in files other units own, returned to the main loop below.

## Returned to the main loop

Neither of these states the spec-audit lens count as a rule. Both are history or fixture prose, so
no fix is recommended. They are listed because AC6 names them.

- `tools/workflows/tier2-review.template.js:216` and its render `tools/workflows/tier2-review.js:216`,
  owned by `TOOL-aEvidencedLens-1`. The comment says "Four lenses were then handed nothing to read",
  describing an earlier closing-review incident.
- `tools/workflows/unattended-build.test.sh:760`, owned by `TOOL-aEvidencedLens-8`. It says "four
  lenses of twelve findings each" about a fixture, and the next line says the fifth spec lens returns
  none.
