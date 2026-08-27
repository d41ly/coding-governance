**Status:** OPEN · rev-1 · 2026-08-27 · node a · Tier-1 · base b4e1d5be · streams tooling · order 2

# TOOL-aGroundedOrientation-1 — the prompt path runs its orientation probes before it writes the roster

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-prompt-TOOL-aGroundedOrientation-1.md](../prompts/2026-08-27-prompt-TOOL-aGroundedOrientation-1.md) | research | TOOL-aGroundedOrientation-2 |

<!-- /gen:spec-records -->

## 1. Goal
Make the unattended prompt path RUN the kickoff engine's Step 4 probes at its own step 1, before
step 3 writes the build folder and step 4 pushes it, so the roster is decided with the probe output
rather than two steps ahead of it.

## 2. Scope (IN)
- **S1.** `tools/unattended/SKILL.template.md`, the `## Start a run from a PROMPT` section, step 1:
  add a paragraph instructing that the orientation probes RUN at that step, carrying the literal
  `RUN the orientation probes`, and stating why the step-6 hand-back does not substitute.
- **S2.** Re-render the three installed artifacts with `bash tools/unattended/adopt-unattended.sh`,
  so `.claude/skills/unattended/SKILL.md` matches the template its `--check` leg byte-compares.

## 3. Non-goals (OUT)
- **N1.** Restating WHICH probes exist. `skills/session-kickoff/SKILL.md` Step 4 owns that list. A
  second spelling here is the `two-answers-to-one-question` class, which `gotchas.py --for-paths`
  selected for these exact files.
- **N2.** Editing `skills/session-kickoff/SKILL.md`. It is an M11 carrier and it sits 207 bytes under
  its 18432-byte gate in `tools/template-size-limits.txt`. The delta this unit owns is timing, and
  timing belongs to the caller.
- **N3.** Adding the lexicon kit to orientation. Refused with a measurement, recorded in §10.
- **N4.** Any change to `memory/guides/UNATTENDED-PROTOCOL.md`. This is a Skill-path instruction, not
  a contract clause, and that file is an M11 carrier.

## 4. Design
Step 1 currently reads, in full:

> 1. **Orient from the prose**, in the `/session-kickoff` manner — steps 0 to 4 of that engine.
>    Derive every field you can from the prose, the memory tree and the code. Do not ask yet.

"In the `/session-kickoff` manner" describes a posture. A reader can satisfy it without running a
single command, and the engine that would have run them is not invoked until step 6 — after step 3
has written the roster and step 4 has pushed it. Under `ANCHOR_SCOPE="published"` that roster is the
authorization, so correcting it costs a fresh commit and a fresh push.

This run is its own evidence in both directions. It DID run the probes at orientation, and recall
returned `TOOL-aPromptedMandate-5` and the note that leg check 18 orders the first `--preflight`
against the first `/session-kickoff` — which is why N2 and AC3 exist. It also amended its roster
after the fact, which cost exactly the commit-and-push this unit exists to avoid.

The added paragraph names the timing and points at Step 4 for the content. It does not enumerate.

### Files touched (estimate)
- `tools/unattended/SKILL.template.md` — one paragraph inside step 1.
- `.claude/skills/unattended/SKILL.md` — regenerated, never hand-edited.

## 6. Acceptance criteria
- **AC1.** `tools/unattended/SKILL.template.md`'s prompt section carries the literal
  `RUN the orientation probes`, and its line number within that section is strictly less than the
  line of `Write the build folder`.
- **AC2.** `bash tools/unattended/adopt-unattended.sh --check` exits 0, so the rendered Skill matches
  the edited template.
- **AC3.** `bash tools/unattended/check-unattended.sh` exits 0 — in particular check 18's ordering of
  the first `--preflight` against the first `/session-kickoff` is unchanged, and check 20's three
  ordered prompt-path steps still resolve.
- **AC4.** The added paragraph names no individual probe command, satisfying N1. Observed by reading
  the diff: it adds no occurrence of `reuse_lookup`, `query.py` or `gotchas.py`.

## 7. Gates
`bash tools/unattended/adopt-unattended.sh --check` · `bash tools/unattended/check-unattended.sh` ·
`bash tools/run-gates/run-gates.sh` at the push boundary.

## 8. Open questions
None. The one fork this unit had — enumerate the probes here or point at Step 4 — is resolved by the
`two-answers-to-one-question` class the checklist selected over these files, which is evidence rather
than preference.

## 9. Revision log
- rev-1 · 2026-08-27 · authored during the run, unreviewed by definition (M4). Grounded against
  b4e1d5be, the merged tree, not the run's original f5dff6ae.

## 10. Reuse audit
**Map probe.** `python tools/codebase-map/reuse_lookup.py "orientation probes an unattended run runs
before it writes its build folder"` returned the `unattended` affordance seam (`.unattended.conf`),
`memory/guides/UNATTENDED-PROTOCOL.md` and `BUILD-METHOD.md`; no symbol-level seam, which is correct
for a documentation-shaped unit.

**Recall probe.** Terms, which M7 re-runs: `unattended prompt path orientation kickoff step4
memory-recall reuse_lookup gotchas lexicon probe build-method M5 spec section10 hand-back`. It
surfaced `TOOL-aPromptedMandate-5`, the spec that designed this path — whose S3 first step is
literally "orient in the `/session-kickoff` manner" — and the review note recording check 18's
ordering constraint.

**The seam extended.** `skills/session-kickoff/SKILL.md` Step 4, which already names the map dossier
probe, `gotchas.py --for-paths` and the memory-recall query. This unit adds no probe; it extends that
seam by reference only.

**The lexicon candidate, tested and rejected.** M12 requires the loss recorded, not just the win.
`python3 tools/lexicon/lexicon.py --brief` over both `tools/unattended/SKILL.template.md` and
`tools/unattended/unattended.sh` returned `COVERAGE: dark` — `.lexicon.conf` declares `md::dark` and
`sh::dark`, so every file this build touches is outside its armed population. It also has no input at
orientation: `--suggest` takes an identifier nobody has written yet. Wiring it in would install a
probe that cannot move, which the charter bans by name. Rejected on the measurement, not on taste.

**Staleness.** Step 4's contents were verified against source at writing time, not taken from the
recall hit.
