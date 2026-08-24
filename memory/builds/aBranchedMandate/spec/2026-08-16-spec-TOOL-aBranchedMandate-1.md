# TOOL-aBranchedMandate-1 — the memory-recall adopter stops reding the bar on a checkout artifact

**Status:** CLOSED · rev-4 · 2026-08-17 · node a · Tier-1 · base 96141aed · streams tooling · ratified 2026-08-16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-16-review-TOOL-aBranchedMandate-1-1.md](../reviews/2026-08-16-review-TOOL-aBranchedMandate-1-1.md) | spec-audit | TOOL-aBranchedMandate-2 TOOL-aBranchedMandate-3 |
| [2026-08-17-review-TOOL-aBranchedMandate-1.md](../reviews/2026-08-17-review-TOOL-aBranchedMandate-1.md) | diff-review | TOOL-aBranchedMandate-2 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-recall/adopt-memory-recall.sh --check` byte-compares the rendered Skill against a fresh
render without normalising CR, so a worktree whose pinned `.claude/` renders carry CRLF reds a
merge-bar leg on a file nobody edited — the state all five live worktrees are in today. Give it the
normalising half its two sibling adopters already have.

## 2. Scope (IN)

- **S1** — CR-normalise the Skill side of the `--check` comparison in
  `tools/memory-recall/adopt-memory-recall.sh`, matching the seam
  `tools/unattended/adopt-unattended.sh:122` already uses.
- **S2** — CR-normalise the same side of the truncated diff this script prints on failure, so the
  reported hunks are the real drift rather than every line of the file.
- **S3** — one runnable arm that fails if S1 regresses. The fixture is **CONSTRUCTED, never
  inherited**: copy the tree into scratch, write CRLF into the rendered Skill deliberately, then
  assert `--check` exits 0. It lives in `tools/memory-recall/selftest.py`, which is already a gate
  leg, so this unit adds no leg. A fixture that merely creates a worktree and hopes for CRLF passes
  today with S1 reverted — measured — which is the `fixture-passes-by-finding-nothing` class.
- **S5** — the `[ -s ]` empty-render refusal the sibling at `tools/unattended/adopt-unattended.sh:121`
  carries and this adopter does not. S1 tells a builder to port the seam from that file; porting the
  normalising diff without the line above it turns a pipe that at least reds on a non-empty Skill into
  a two-empty-file comparison that greens. The guard comes with the seam or the seam is not ported.
- **S4** — the header comment gains the rule the other two adopters state in their own headers, so
  the next reader of this file learns why the normalisation is there rather than deleting it as
  redundant.

## 3. Non-goals (OUT)

- Changing `.gitattributes`. The `eol=lf` pin is the other half and it is correct; the gotcha record
  says both halves are needed and this unit adds the missing one.
- Changing what `tools/check-wiring.sh` reports about CRLF. That is `TOOL-aBranchedMandate-2`, and it
  depends on this unit landing first.
- Auditing every other byte-comparing gate in the tree for the same class. Three adopters carry the
  `eol=lf` pin on a `.claude/skills/**` render and this unit measures all three; a tree-wide sweep is
  a separate unit nobody has scoped.
- Rendering or re-scaffolding the Skill's content. Nothing about the render is wrong.

## 4. Design

The rule is already written down. `memory/gotchas/gate-green-by-accident-on-generated-bytes.md`
states that a generated file needs **both** an `eol=lf` pin and a normalising comparison, and that
either alone leaves the failure mode. `tools/unattended/adopt-unattended.sh` states the same rule in
its header and implements it. This adopter has the pin and not the comparison.

### Inventory

Measured in this worktree at BASE, by running each adopter's `--check` and by reading each source.
The fourth column is here because the audit found §5 asserting a guard this adopter does not have:

| Adopter | Pin | CR-normalising comparison | Empty-render refusal | `--check` here |
|---|---|---|---|---|
| `tools/unattended/adopt-unattended.sh` | yes | yes | yes | exit 0 |
| `tools/drift-audit/adopt-drift-audit.sh` | yes | yes | **no** | exit 0 |
| `tools/memory-recall/adopt-memory-recall.sh` | yes | **no** | **no** | **exit 1** |

The drift-audit cell said `yes` until it was re-measured at build time: `adopt-drift-audit.sh:129-138`
renders to a temp file and diffs it with no `[ -s ]` test anywhere in the script, so only
`adopt-unattended.sh:170` carries the refusal. That does not move S5 — this unit adds the guard here
either way, and the sibling it is ported from is the one that has it. What it does move is the
argument's SHAPE: the guard is one adopter's practice, not two adopters' convention, and the third
adopter's gap is a real one nobody has scoped. The row for it is in `memory/backlog/TOOL.md`.

The failure was confirmed to be line endings alone and nothing else. The Skill holds CRLF on 89 of
89 lines. With CR stripped from the working copy, `--check` prints
`ok       memory-recall skill — SKILL.md matches the conf` and exits 0; the original bytes were then
restored. That test matters because this script truncates its printed diff at **forty** lines
(`tools/memory-recall/adopt-memory-recall.sh:154`, `render | diff -u "$SKILL" - | head -40`), so
reading the log cannot distinguish a pure line-ending diff from a content drift whose first forty
lines happen to be line-ending noise. Twenty is the SIBLINGS' window
(`adopt-unattended.sh:125`, `adopt-drift-audit.sh:136`) and an earlier revision of this section
carried it here by mistake — which matters for S3, because a fixture that discriminates has to place
its content mutation past line 40.

This adopter's `--check` path is `[ -f "$SKILL" ]` at `:148` then `render | diff -q - "$SKILL"` at
`:149`. There is no temp file, no `[ -s ]` test, and therefore no empty-render refusal — S5 adds one.

### Migration

None. The committed bytes do not move, so every node's repository state is already correct; only the
comparison changes. What makes a working copy hold CRLF is NOT the index-normalises-on-commit
argument an earlier revision gave — see the reproduction record under this build's `build/` for the
measurement that refuted it and for the writer's actual scope.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/memory-recall/adopt-memory-recall.sh` | S1, S2, S4, S5 |
| `tools/memory-recall/selftest.py` | S3 |

### Alternatives rejected

- **Normalise both sides.** The render side is produced by this script and is LF by construction; a
  `tr` on it would be a no-op that reads as though the render were untrusted. The sibling at
  `adopt-unattended.sh:122` normalises only the on-disk side, and matching it keeps one shape.
- **Have the gate runner normalise.** It would fix this leg and hide the class everywhere else,
  including in adopters shipped to other repos where no gate runner of ours exists.
- **Drop the `eol=lf` pin instead.** The pin is what makes the committed bytes right, and
  `tools/check-wiring.sh:198` derives its whole eol population from it. Dropping it trades a red leg
  for a silent one.

## 5. Production-readiness checklist

- security — N/A. The comparison's strictness about content is unchanged; only line endings stop
  counting as content.
- perf / scale — N/A. One `tr` over an 89-line file.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No message content changes.
- error / empty / loading states — **this adopter has NO empty-render guard**; its two siblings do.
  An earlier revision of this line said the guard existed and must not be weakened, which was false
  and actively dangerous: it would have sent a builder to port the sibling's normalising diff while
  skipping the `[ -s "$TMP" ]` line directly above it, converting a pipe that at least reds on a
  non-empty Skill into a two-empty-file comparison that greens. S5 adds the guard with the seam.
- observability — the truncated failure diff becomes readable, which is S2. Today a CR-only drift and
  a real content drift print the same wall of removed lines.
- risks — the one real risk is that normalisation hides a genuine drift that consists only of line
  endings *in the render*. That cannot happen here: the render is generated LF in-process.
- testing + left-shift gates — S3. The regression is invisible without a fixture, because the tracked
  worktree on a node that has run the repair is LF and the comparison passes for the wrong reason.
- migration / rollback — revert the commit; nothing persists.
- user docs — S4 only. No adopter-facing instruction changes.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-recall/adopt-memory-recall.sh --check` runs in a worktree whose
  `.claude/skills/memory-recall/SKILL.md` holds CRLF, it exits 0 and prints its `ok` line.
- **AC2** — When the rendered Skill differs from the conf in CONTENT, `--check` still exits 1 and
  still names the drift. Proven by mutating one line of `SKILL.md` in a scratch copy, not by
  reasoning about the code.
- **AC3** — When `bash tools/run-gates.sh` runs in a tree whose pinned `.claude/` renders have been
  given CRLF **deliberately**, the leg named `memory-recall skill wiring` is green. The earlier
  wording keyed this to "a fresh worktree created by `git worktree add`", which is already green at
  BASE with S1 reverted — measured — and therefore observed nothing.
- **AC4** — When the arm in S3 runs against a build with S1 reverted, it fails, and its message names
  `.claude/skills/memory-recall/SKILL.md`.
- **AC5** — When `bash tools/check-wiring.sh --check` runs against that same constructed-CRLF tree,
  its eol arm still reports the CRLF paths. This unit does not silence that report; it removes the red
  leg the report warns about. Also re-keyed off `git worktree add`, where the arm prints `ok` and the
  criterion was unsatisfiable.
- **AC6** — When `--check` is run against a tree whose rendered Skill is EMPTY, it exits 1 rather than
  reporting a match. This is S5's observation, and without it a builder who ports the sibling's seam
  without the sibling's guard turns an empty-vs-empty comparison into a pass.

## 7. Gates

- `bash tools/run-gates.sh` — the whole bar, and specifically the leg `memory-recall skill wiring`
  which is the one this unit turns green.
- `python tools/memory-recall/selftest.py` — the leg that hosts S3.
- `python tools/codebase-map/test_codebase_map.py` and `python tools/drift-audit/drift_report.py --check`
  — both must stay green, and both are the reason S3 went where it did: each reds on an ADDED gate
  leg, the second at a pin with zero slack. Named here so a later reader does not move S3 into a new
  sibling test file without paying for it.

## 8. Open questions

none — the fork below is RESOLVED.

- **F1 — where does S3's arm live?** Two options. **(a) Fold it into
  `tools/memory-recall/selftest.py`**, which is already a leg, so no new leg is created and none of
  the four leg-addition gates in §7 move. It costs a `subprocess` call to bash from a python selftest
  that today exercises only the retrieval engine. **(b) A new
  `tools/memory-recall/adopt-memory-recall.test.sh`**, matching how `tools/unattended/` tests its own
  adopter, at the cost of a new gate leg plus the dossier claim, the map re-render, the manifest
  re-stamp and the drift-signal pin it drags with it. **RESOLVED (owner, 2026-08-16): (a).** The arm
  is four lines and the shape it proves is not adopter-specific; option (b) spends four gate
  movements on file placement. Revisit if a second adopter-level arm appears, at which point a
  sibling test file is earning its keep.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the reproduction recorded under this build's `build/`.
- rev-2 · 2026-08-16 · F1 resolved by the owner; S3, §4's file table and §7's gate list now name
  `tools/memory-recall/selftest.py` instead of deferring to the fork.
- rev-4 · 2026-08-17 · BUILT and CLOSED. §4's Inventory claimed `adopt-drift-audit.sh` carries an
  empty-render refusal; re-measured at build time it does not, and the cell plus the paragraph under
  it are corrected — the same class the audit's C11 caught one cell to the left. No scope moved: S5
  is unchanged and the seam it ports from is `adopt-unattended.sh:170`, which does have the guard.
  All six acceptance criteria observed, AC4 by reverting S1/S2 in a scratch copy rather than by
  reading the code.
- rev-3 · 2026-08-16 · folded the spec audit recorded under this build's `reviews/`. Its C1 refuted
  this spec's causal premise: `git worktree add` does NOT land CRLF, so AC3 was already green with S1
  reverted and AC5 was unsatisfiable — both re-keyed to a CONSTRUCTED fixture, and S3 says so. C11:
  §5 asserted an empty-render guard this adopter does not have; the line is corrected, S5 and AC6 add
  the guard, and §4's Inventory gains the column that would have caught it. C17: §4's truncation
  window was the siblings' twenty, not this file's forty. §1 and §4 Migration re-stated against the
  measurement.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` returned no seam for this behaviour, which is correct:
the thing being reused is not a symbol but a two-line idiom. The seam is
`tools/unattended/adopt-unattended.sh:122`, `diff -q <(tr -d '\r' < "$SKILL_OUT") "$TMP"`, with its
rule stated at that file's lines 9 to 12. `tools/drift-audit/adopt-drift-audit.sh` carries the same
shape. This unit makes the third copy of a three-copy idiom agree with the other two rather than
introducing anything. No new abstraction is warranted at three call sites in three separately
copy-installed kits — a shared helper cannot be shared across kits that ship independently, which is
the same constraint that makes `resolve_python` an inline byte-identical block rather than an import.
