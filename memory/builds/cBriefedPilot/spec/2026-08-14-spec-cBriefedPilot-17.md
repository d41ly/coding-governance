# TOOL-cBriefedPilot-17 — the shipped protocol marker, paired to the constant it claims

**Status:** OPEN · rev-1 · 2026-08-14 · node c · Tier-1 · base 37c05e1b · streams tooling

## 1. Goal

`tools/check-kit-versions.sh` pairs the unattended kit's two SCRIPT constants and nothing it SHIPS,
which is how `PROTOCOL.template.md` sat at `@1.2` against `1.3` unnoticed. Extend the memory-tree
pairing shape to this kit's shipped docs, before unit 19 performs the bump that would otherwise
reproduce the hole. This absorbs the OPEN backlog row `TOOL-cFinalBerth-3`.

## 2. Scope (IN)

- **S1** — a marker/constant block for the unattended kit in `tools/check-kit-versions.sh`, modelled
  on the memory-tree block at lines 62-97: read `KIT_UNATTENDED_VERSION` from
  `tools/unattended/unattended.sh`, then assert every member of a DERIVED population carries
  `gov:kit unattended@` at that value.
- **S2** — the population is `git ls-files 'tools/unattended/*.template.md'`. An empty result is a
  refusal, not a pass, exactly as the memory-tree block treats its own.
- **S3** — two arms per member, as memory-tree has: a member carrying NO `gov:kit unattended@`
  marker at all, and a member whose marker disagrees with the constant. They are different findings
  and the second cannot report the first.
- **S4** — `tools/unattended/SKILL.template.md` gains the marker it does not carry today, because
  S2's glob matches it. It goes on its own line AFTER the YAML front matter's closing `---`, never at
  line 1: line 1 is the front-matter opener and a comment above it breaks the Skill.
- **S5** — the re-rendered `.claude/skills/unattended/SKILL.md`, carrying that marker through
  `adopt-unattended.sh`.
- **S6** — the two INLINE `gov:kit unattended@` markers that share a line with each constant are
  paired to the constant too, the way `agent-cap.js`'s same-line pair is at lines 46-50. Same line is
  not same value, and that is the recorded reason agent-cap's half-bumped pair used to pass.

## 3. Non-goals (OUT)

- **The bump.** Unit 19 moves every literal to `1.5`. This unit lands at `1.4`, so the block is
  proven against the version already in the tree and the bump has something to red against.
- **A self-test sibling for `check-kit-versions.sh`.** It defines no `fail() {` helper — it counts
  with `echo` plus `fails=$((fails+1))` — so `check-arms.py` does not discover it and it has no arm
  obligation and no floor row. Giving it one is backlog row `TOOL-aTimedTurnstile-7`'s class and a
  unit of its own.
- **Content parity between the two protocol halves.** Leg check 10 owns that, and it is precisely
  why this unit exists: both halves stale compare equal.
- **Any new gate leg.** This rides `kit version markers`, which is already on the bar and carries no
  guard in `tools/gate-legs.json`, so it runs on every commit's diff-scoped bar.

## 4. Design

### Why the population is derived and not named

Backlog row `TOOL-aSealedCaravan-3`, now CLOSED, records what naming costs: the memory-tree block
named `HYGIENE.template.md` alone, and the two siblings it did not name drifted — one three bumps
behind and shipping that number into every adopting tree, the other carrying no marker at all.
Naming one file is why the hole reopened at every bump. A derived glob covers the next shipped
template with no further edit.

### The glob matches TWO files, and that is the point

Measured: `git ls-files 'tools/unattended/*.template.md'` returns `PROTOCOL.template.md` and
`SKILL.template.md`. The design pass called this unit "the shipped protocol marker", and the derived
glob is wider than that phrase. Both are docs an adopter renders and keeps, so the wider population
is correct — and it is the whole reason S4 exists. Narrowing the glob back to the protocol would
reproduce the named-one-file defect on the day it was written.

### Where the Skill's marker sits

`tools/unattended/SKILL.template.md` opens at line 1 with `---`, the front matter the harness parses
to discover the skill. `PROTOCOL.template.md` carries its marker at line 1 because it has no front
matter. The assertion is an unanchored `grep -qE`, so placement is free and the front matter is the
only constraint.

### CRLF

The token is mid-line in all six spellings, so a working tree checked out CRLF still matches. This
is the same reasoning the memory-tree block states, and it is why no `tr -d '\r'` is needed here.

### Files touched (estimate)

`tools/check-kit-versions.sh` (the block, plus the file header comment that enumerates which pairs
are asserted) · `tools/unattended/SKILL.template.md` · `.claude/skills/unattended/SKILL.md`.

### Alternatives rejected

A shared per-kit marker helper over all of them. Rejected: each kit spells its marker differently —
an HTML comment, a shell comment, a Python docstring — so the helper's parameter list would be
longer than the six lines each block costs, and the blocks already read as one shape.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — two greps per member on one of the cheapest legs on the bar.
- a11y · i18n — N/A.
- error / empty / loading states — an empty derived population is a refusal (S2), the repo's
  `vacuous-selector-empty-population` class.
- observability — each arm prints the offending file and both values.
- risks — the glob widens silently when a third `*.template.md` lands in the kit. That is intended,
  and the failure mode is a loud refusal naming the new file rather than silence.
- testing + left-shift gates — no arm registry covers this file (§3), so acceptance is an OBSERVED
  red on a reverted edit rather than a persisted arm.
- migration / rollback — the `SKILL.template.md` marker is additive; deleting the block restores
  today's behaviour exactly.
- user docs — the file's own header comment enumerates the pairs it asserts and must name this one.

## 6. Acceptance criteria

- **AC1** — When `tools/unattended/PROTOCOL.template.md`'s marker alone is edited to `@1.3`,
  `bash tools/check-kit-versions.sh` exits 1 and names that file; reverting returns exit 0.
- **AC2** — When `tools/unattended/SKILL.template.md`'s marker alone is edited, the leg reds and
  names that file.
- **AC3** — When `SKILL.template.md`'s marker LINE is deleted, the leg reds through the no-marker
  arm, not the mismatch arm.
- **AC4** — When the inline `gov:kit unattended@` marker on `tools/unattended/unattended.sh`'s
  constant line is edited alone, the leg reds (S6).
- **AC5** — On the clean tree the leg exits 0, and the population it reads is the two template files
  named in §4.
- **AC6** — `bash tools/unattended/adopt-unattended.sh --check` is green after the re-render, with no
  surviving brace-shaped placeholder.

## 7. Gates

`kit version markers` (`tools/check-kit-versions.sh`) · `unattended skill wiring` ·
`unattended adopter e2e` · `method carriers` (`SKILL.template.md` is a declared carrier and the edit
must not turn it into a copy) · the full bar.

## 8. Open questions

**RESOLVED at authoring: keep the derived glob, and give `SKILL.template.md` the marker it implies.**
The alternative was to narrow the population to `PROTOCOL.template.md`, which is what the design pass
described and what the backlog row asks for literally. It is rejected on `TOOL-aSealedCaravan-3`'s
recorded evidence: a named population is the defect, and a shipped doc that self-identifies as
nothing cannot be caught by any comparison. This is a decision by the spec's author, not a fork the
owner declined, and it is recorded because it grows unit 19's bump set.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds D6 and absorbs the OPEN backlog row
  `TOOL-cFinalBerth-3`. Records two measurements the design pass did not make: the derived glob
  matches two files rather than one, and the kit's version is spelled six times across four lines,
  two of those spellings being inline markers no gate reads.

## 10. Reuse audit

- **The memory-tree pairing block, `tools/check-kit-versions.sh:62-97`** — the seam this extends.
  Same derivation, same two arms, same empty-population refusal, a different constant and marker
  token. Nothing is factored out; see §4's rejected alternative.
- **The agent-cap same-line block, `tools/check-kit-versions.sh:46-50`** — the precedent for S6, and
  the recorded case of a half-bumped one-line pair passing a presence-only check.
- **`tools/unattended/kit.toml`'s `version_from`** — already derives the kit's version from
  `unattended.sh`'s constant for the govkit registry, so no second version home is introduced here.

Recall terms used: kit version marker shipped doc pair constant drift unattended protocol template
adopter deployer. `python tools/codebase-map/reuse_lookup.py "pair a shipped document version marker
against a kit version constant"` returned the `kit version markers` leg and `kit-dogfood-parity.PAIRS`
as the nearest seams; the parity seam is the wrong one here, because it compares two documents to each
other and this unit compares a document to a constant.
