# TOOL-cBriefedPilot-19 — the kit identifies as the version it now is

**Status:** CLOSED · rev-3 · 2026-08-16 · node c · Tier-1 · base 37c05e1b · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-15-review-TOOL-cBriefedPilot-1-1.md](../reviews/2026-08-15-review-TOOL-cBriefedPilot-1-1.md) | spec-audit | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |
| [2026-08-16-review-TOOL-cBriefedPilot-1-2.md](../reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md) | diff-review | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |

<!-- /gen:spec-records -->

## 1. Goal

Move the unattended kit from `1.4` to `1.5` in every place it spells its own version, after unit 17
makes a partial bump red the bar. A kit that ships a new contract under the old number tells the
deployer, and the adopter reading their own installed copy, something false.

## 2. Scope (IN)

- **S1** — the two script constants: `tools/unattended/unattended.sh:32` and
  `tools/unattended/check-unattended.sh:17`.
- **S2** — the two INLINE `gov:kit unattended@` markers that share those same two lines. Measured:
  each constant line carries both spellings, so the four literals the design pass counted are
  actually four LINES holding six spellings.
- **S3** — the two doc markers at line 1 of `tools/unattended/PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md`.
- **S4** — the marker unit 17 adds to `tools/unattended/SKILL.template.md`, and its re-render at
  `.claude/skills/unattended/SKILL.md`. Six files, eight spellings.

## 3. Non-goals (OUT)

- **Any behaviour change.** This unit moves digits. Every branch, every check and every document
  section is unit 17's, unit 18's or unit 22's.
- **A CHANGELOG or migration note.** The kit ships none today and adding one is a new artifact with
  its own parity obligation.
- **`tools/unattended/kit.toml`.** Measured: it declares `version_from = { file = "unattended.sh",
  pattern = "^KIT_UNATTENDED_VERSION=" }` and holds no literal, which is why it takes no edit.

## 4. Design

### Why the bump is its own unit, and lands last

Two reasons, and both are ordering. Unit 17 must land first so that a partial bump reds rather than
passing silently — the row it absorbs, `TOOL-cFinalBerth-3`, exists because a partial bump did pass.
Units 18 and 22 must land first because the version is the claim that the contract at that number is
the contract this kit ships; bumping before the contract changes publishes a number against the old
text.

### The eight spellings

| File | Spellings | Shape |
|---|---|---|
| `tools/unattended/unattended.sh` | 2 | the constant and an inline marker on line 32 |
| `tools/unattended/check-unattended.sh` | 2 | the constant and an inline marker on line 17 |
| `tools/unattended/PROTOCOL.template.md` | 1 | the line-1 HTML comment marker |
| `memory/guides/UNATTENDED-PROTOCOL.md` | 1 | the same marker in the live twin |
| `tools/unattended/SKILL.template.md` | 1 | the marker unit 17 adds |
| `.claude/skills/unattended/SKILL.md` | 1 | that marker, rendered |

### What each gate sees, and the one gap

After unit 17 the `kit version markers` leg pairs the SIX spellings that live in the four kit files
against the constant, so any single omission there reds it. It does not reach the other two, and the
measurement says why: `tools/check-kit-versions.sh` names no path under `memory/` or `.claude/`
anywhere, and unit 17's population is derived from `git ls-files 'tools/unattended/*.template.md'`.
Those two have their own signals rather than none. The live protocol twin is covered by leg check 10,
which byte-compares the pair whole, so a one-sided bump is a diff; the rendered Skill is covered by
`unattended skill wiring`, which diffs the render against a fresh render of the template. Three
gates, eight spellings, no spelling unwatched — but not one gate, which is what this section said
before it was checked.

### Files touched (estimate)

The six files in the table above, in one commit. Splitting them is what the gate exists to refuse.

### Alternatives rejected

Deriving the doc markers from the constant at render time. Rejected: the marker's whole purpose is
that a deployer can grep the version out of a file in an adopting tree without running anything, and
a rendered value is still a literal in the file that ships. It would also convert a second-opinion
comparison into a generator and its output, which checks nothing.

## 5. Production-readiness checklist

- security · perf / scale · a11y · i18n · observability — N/A, six literals.
- error / empty / loading states — N/A.
- risks — a partial bump, which is exactly what unit 17 makes visible.
- testing + left-shift gates — `kit version markers`, plus the two second opinions named in §4.
- migration / rollback — an adopter re-renders and gets the new number; the previous state is one
  revert.
- user docs — the protocol pair's marker IS the user-visible version.

## 6. Acceptance criteria

- **AC1** — All eight spellings read `1.5`, verified by
  `grep -rn "unattended@1\.5\|KIT_UNATTENDED_VERSION=1\.5"` returning the six files in §4's table, and
  `git grep -n "unattended@1\.4\|KIT_UNATTENDED_VERSION=1\.4"` returning nothing. The bare-`1.4` form
  was measured FALSE against this tree — five legitimate hits survive outside `memory/` (`agent-cap.js`
  twice, `WIRE-INTO-PROJECT.md`, and two timing comments), none of them this kit's version token.
- **AC2** — `bash tools/check-kit-versions.sh` exits 0.
- **AC3** — Reverting any ONE of the SIX spellings in the four kit files to `1.4` reds
  `bash tools/check-kit-versions.sh`, observed for each of the six rather than argued.
- **AC4** — `bash tools/unattended/check-unattended.sh` check 10 is green, and reds when only the
  live protocol twin's marker is reverted. That twin is NOT in `check-kit-versions.sh`'s population,
  so this is its only signal and is observed, not argued.
- **AC5** — `bash tools/unattended/adopt-unattended.sh --check` is green after the re-render, and
  reds when only the rendered Skill's marker is reverted. Same reason as AC4: the render is outside
  the version leg's population.

## 7. Gates

`kit version markers` · `unattended kit gate` · `unattended skill wiring` ·
`unattended adopter e2e` · `verdict epoch` (unaffected — it dates the memory-tree engine, not this
kit, and the distinction is worth stating because the two look alike) · the full bar.

## 8. Open questions

none — the version format is the house two-part `X.Y` that `check-kit-versions.sh` enforces with one
regex, and the increment is a minor one because the contract grows and nothing it declared is
withdrawn.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Corrects that pass's file list: it named
  four literals in four files, and the measured set is eight spellings in six files — two inline
  markers share the constant lines, and unit 17's derived glob adds the Skill template and its
  render.
- rev-2 · 2026-08-14 · §4's coverage claim and AC3 corrected. Both said `check-kit-versions.sh`
  pairs all eight spellings after unit 17; measured, that script names no path under `memory/` or
  `.claude/` at all, and unit 17's population comes from `git ls-files 'tools/unattended/*.template.md'`
  — so the live protocol twin and the rendered Skill are outside it and two of AC3's eight
  observations could not have been made. The version leg now claims six, and the other two are
  observed against check 10 and `unattended skill wiring`, which are the gates that do see them.

- rev-3 · 2026-08-15 · §8's audit fold. AC1's bare-`1.4` clause was measured FALSE against this tree — five legitimate
  hits survive outside `memory/` — so it is scoped to the kit's own version tokens.

## 10. Reuse audit

- **`tools/check-kit-versions.sh`** — the seam this unit is graded by rather than one it extends.
  Unit 17 builds the coverage; this unit is the first bump that runs under it.
- **`tools/unattended/kit.toml`'s `version_from`** — the govkit registry's single derivation, which
  is why the deployer descriptor needs no edit here.
- **`tools/unattended/adopt-unattended.sh`'s `render()`** — carries the Skill marker from template to
  render with no substitution key, so S4's second spelling costs no renderer change.

No new seam. A version bump is the smallest possible extension of machinery that already exists, and
the only reason it is a unit at all is that unit 17 changes what a partial one costs.

Recall terms used: unattended kit version bump constant marker shipped doc render adopter deployer
pair partial half-bumped grep.
