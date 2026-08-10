# TOOL-aUnmannedHelm-8 — the kickoff hand-back, and the five exits it does NOT buy

**Status:** CLOSED · rev-3 · 2026-08-10 · node a · Tier-2 · base 4c338893 · streams kickoff · ratified 2026-08-10 · review wf_077104e6

## 1. Goal

Let a mandated run get past `/session-kickoff` Step 5 without an owner turn, and make every OTHER
interactive exit in the engine resolve without one too. This is unit 6 of seven; the master scope and
the ratified decision menu live in this build's `README.md`.

The review found this unit was the only one of the seven with no acceptance criterion and no gate
leg, on an engine that every session on all three nodes runs through. Both holes are closed here.

## 2. Scope (IN)

- **S1 · Step 5b in `skills/session-kickoff/SKILL.md`** — the hand-back, fenced to the case where a
  committed standing mandate is reachable from the pinned BASE.
- **S2 · all SIX interactive exits enumerated by their step**, each with a stated no-owner-turn
  resolution. Five resolve by ABORTING or PARKING; exactly one is replaced by the hand-back.
- **S3 · the gate leg that reads the engine's TEXT** — check 12 of `tools/unattended/check-unattended.sh`,
  keyed on a `KICKOFF_ENGINE` declaration so a non-adopting repo is unaffected.
- **S4 · a shrink-only floor on the exit count** (`KICKOFF_EXITS`), so dropping one from the
  enumeration reds.
- **S5 · the engine on the manifest's `watch` list**, so a change to it forces a re-audit.

## 3. Non-goals (OUT)

- **Removing the Step 5 stop.** It is the DEFAULT and the leg asserts it in both directions. The
  hand-back is the exception, not the replacement.
- **Making the other five exits interactive-but-faster.** They resolve by aborting or parking. An
  unattended run that guesses at an ambiguous repo is worse than one that stops.
- **Editing `manifest-check.sh`.** Shipped to adopters; editing it diverges their copies.
- **Any agent-cap edit.** `TOOL-aNumeralWarden-1`'s.

## 4. Design

### Why the enumeration is the deliverable, not the hand-back

The hand-back is three sentences. The work is the other five exits, because "the run is unattended"
is false the moment any of them fires — and each one had a different right answer:

| Exit | Resolution | Why not the other one |
|---|---|---|
| Step 0 · ambiguous worktree parent | resolve to the default-branch checkout, else ABORT | guessing a repo is worse than stopping |
| Step 0 · no git anywhere | ABORT | a mandate authorizes landing; there is nothing to land into |
| Step 1 · the STOP conditions | ABORT, recording the condition verbatim | these are the states where continuing destroys work |
| Step 2 · no manifest, offer to scaffold | do NOT scaffold; park the offer | scaffolding a governance layer unasked is a bigger decision than the one being skipped |
| Step 3 · an underivable field | park with question + options + reason; ABORT if it is acceptance or gates | a unit with no acceptance check is not Ready, and a run cannot split it |
| Step 5 · the READY stop | replaced by the hand-back | the only one the mandate buys |

An ABORT writes its reason to the run-state file and stops. It does not merge and it does not push,
which is what keeps "abort" from being a quieter way to fail open.

### Why the check lives in the unattended leg

Nothing read the engine's text. The manifest ratchet watches the project layer, not the engine; the
coverage gate enumerates the skill's PATH key, not its contents. So the check goes where the rule
comes from — the unattended kit — and is keyed on a `KICKOFF_ENGINE` declaration that a repo without
the kickoff skill leaves blank. A blank declaration turning a check off is this fleet's standing
pattern, and the arm for it is explicit.

Three assertions, in both directions:

1. the engine declares the hand-back;
2. the engine still carries the READY prompt string VERBATIM — the more dangerous direction, because
   deleting the stop makes every ATTENDED kickoff run on unasked. The literal string is asserted
   rather than the heading, since a heading survives a gutted body;
3. the enumeration holds at least `KICKOFF_EXITS` entries. A dropped exit is a place an unattended
   run silently regains to stop, and the count is the only thing that notices.

Plus a fourth: a `KICKOFF_ENGINE` naming a file that does not exist is a refusal, because otherwise
a typo skips the whole check.

### Files touched

Edited: `skills/session-kickoff/SKILL.md` (Step 5b), `tools/unattended/check-unattended.sh` (check
12), `tools/unattended/check-unattended.test.sh` (six arms), `.unattended.conf` and its shipped
example (two declarations), `.memory-tree.conf` (the arms floor 22 -> 26),
`.claude/SESSION-KICKOFF.md` (the `watch` list gains the engine and the unattended conf).

### Alternatives rejected

- **A leg inside `skills/session-kickoff/`.** The rule is the unattended kit's; a second gate in the
  kickoff kit would make the kickoff kit depend on a kit an adopter may not have.
- **Extending `manifest-check.sh`.** Shipped verbatim to adopters, who re-pull it.
- **Asserting the Step 5b heading only.** A heading survives a gutted body; the prompt string does
  not.
- **Letting the other five exits stay interactive.** Then "zero owner turns" holds only on the happy
  path, which is the claim the review refused.

## 5. Production-readiness checklist

- **security** — no write path; the leg greps a file.
- **perf / scale** — four greps over one 220-line document.
- **a11y · i18n** — N/A.
- **error / empty / loading states** — a blank declaration is off, a dangling one is a refusal.
- **observability** — each of the four assertions names itself.
- **risks** — the dominant one is a hand-back that quietly becomes the default. The prompt-string
  assertion is the guard, and it is armed in the deleting direction.
- **testing + left-shift gates** — six arms, including the blank-declaration green control.
- **migration / rollback** — the engine change is additive; deleting Step 5b restores prior
  behaviour and the leg reds until the declaration is blanked, which is the correct coupling.
- **user docs** — the engine IS the doc.

## 6. Acceptance criteria

- **AC1** — With no committed mandate, the engine still halts at Step 5 carrying the literal prompt
  string; the leg reds if that string is gone. Observed by deleting the string and watching check 12
  fire.
- **AC2** — With Step 5b removed, check 12 reds naming the missing hand-back. Observed.
- **AC3** — With one exit deleted from the enumeration, check 12 reds naming the count and the floor.
  Observed at 5 against 6.
- **AC4** — With `KICKOFF_ENGINE` naming a nonexistent file, check 12 reds rather than skipping.
  With it blank, the leg is silent and green. Both observed.
- **AC5** — A conforming engine leaves the leg silent. Observed as the green control.
- **AC6** — The engine is on the manifest's `watch` list, so editing it forces a re-audit. Observed
  by `manifest-check.sh` exiting 0 only after the re-stamp.

## 7. Gates

The standing bar. Newly relevant: the kickoff-manifest ratchet, whose `watch` list now includes the
engine, and `check-arms.py`, whose floor for the unattended leg rises 22 -> 26.

**Build-wide constraint this unit inherits:** `non_terminal_specs_cited_by_product_source` measures
2 against a pin of 2, zero headroom.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, as unit 6 of seven, carrying the review's finding that this was
  the only unit with neither an acceptance criterion nor a gate leg, on an engine every session runs
  through.
- rev-2 · 2026-08-10 · BUILT on the unit branch, unmerged, in the same pass. The six exits were
  enumerated by reading the engine rather than by trusting the count: the review said six against the
  master spec's five, and six is what the file holds. The enumeration turned out to be the unit's
  real content — the hand-back is three sentences, and each of the other five exits needed a
  different answer, two of which are ABORT rather than "proceed conservatively". The gate leg went
  into the unattended kit rather than the kickoff kit, so an adopter without the kickoff skill is
  unaffected by a blank declaration.

- rev-3 · 2026-08-10 · LANDED on `main` in the merge commit that closes this build. CLOSED in this tree's vocabulary means built AND landed, which is true from the moment that commit exists; the push publishes it.

## 10. Reuse audit

The seams this unit wires through rather than reinvents:

- `tools/unattended/check-unattended.sh` — the existing leg gains one check rather than a sixth
  script; the kit already had a home for a rule this kit owns.
- The blank-declaration-turns-it-off pattern — `.memory-tree.conf`'s `TOMBSTONE_ROOTS`,
  `SPEC_FORMAT_CUTOFF` and `STREAMS_CUTOFF` all work this way, and each has an explicit green arm.
- The shrink-only count floor — the same shape `ARMS_FLOORS`, `baseline.toml` and this kit's own
  `CORE_FLOOR` use, for the same reason: it catches a deletion without duplicating a list.
- `skills/session-kickoff/SKILL.md`'s existing Step 5 — the hand-back is a NEW step beside it, not an
  edit to it, so the default and the exception are separately assertable.
- The manifest's `watch` list — the existing ratchet, extended rather than paralleled.
