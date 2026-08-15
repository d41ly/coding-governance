# TOOL-cBriefedPilot-4 — preflight refuses to start a run with no method to run it under

**Status:** CLOSED · rev-2 · 2026-08-16 · node c · Tier-1 · base 37c05e1b · streams tooling

## 1. Goal

Refuse `--preflight` when the build-method carrier does not exist under the memory root. Every one of
the eleven directives is a POINTER into a section of that file; a run whose tree has nothing to point
at holds a directive set that resolves to nothing, and today it starts anyway and nobody is present
to notice.

## 2. Scope (IN)

- **S1** — one `fail` branch in `verb_preflight`'s precondition block, above the write barrier at
  `tools/unattended/unattended.sh:830`, testing `[ -f "$M/guides/BUILD-METHOD.md" ]` — the same path
  expression `verb_resume` already derives at `:910`.
- **S2** — the branch takes a check number no other branch in the driver uses. `34` is free today:
  the driver spells 1 through 33, 35 and 36, and the literal `check 34` appears nowhere in the tree.
- **S3** — the driver self-test fixture gains a committed `memory/guides/BUILD-METHOD.md` stub,
  created before the fixture's initial commit at `unattended.test.sh:103` so that every `reset_tree`
  — which runs `git clean -qfd` — preserves it.
- **S4** — two arms: a fixture without the carrier prints the refusal and leaves NO run-state file,
  and the green control preflights OK.
- **S5** — `ARMS_FLOORS` for `tools/unattended/unattended.sh` in `.memory-tree.conf` rises by one
  branch and one arm, in the SAME commit as the branch. The absolute value depends on what units 1
  through 3 have already added, so the edit is relative to whatever is there when this lands.

## 3. Non-goals (OUT)

- **The protocol sentence making the build method a run-time dependency of this kit.** Unit 18
  publishes the contract, once what it describes exists.
- **The leg's resolution of the cited M-sections.** Leg check 16 arm B (unit 12) resolves each cited
  `M<n>` against `^## M<n>` and is SILENT when the carrier is absent, because the leg grades the TREE
  and the driver grades the RUN. Two questions, answered in two places on purpose.
- **A conf key naming the carrier.** `verb_resume` derives the path from `MEMORY_ROOT` with no
  declaration and this branch uses the same expression. A key would be a second spelling of a
  derivable value, which `.unattended.conf`'s own header bans.
- **Checking the carrier's CONTENT, size or sections.** Existence is what a run needs before it
  starts.
- **Hardening the Skill's step 0.** Unit 9. The Skill instructing the read and the driver refusing
  without it are two mechanisms, and the design pass kept both deliberately.

## 4. Design

### Why the precondition block and not a new exit path

`fail` sets `status`, and `:830` already prints that the run-state file is unchanged and returns 1.
Joining that block adds a branch and no control flow. It also inherits the property the block exists
for: a refused preflight has written nothing, so the refusal is about a state it did not already
change.

### Why refuse at preflight rather than later

Preflight is the last verb the owner may still be watching — step A's `AskUserQuestion` is the turn
immediately before it, and from the next command onward M10 binds and there is nobody to read
anything. A refusal at `--plan` or at the first `--phase` lands after that boundary, where its only
audiences are a transcript nobody opens and a run that has to decide for itself what to do about it.

### Which check number, and why it is worth a sentence

`check-arms.py` keys a pin on `(gate, number, ordinal)` and assigns ordinals per number in SOURCE
order, so inserting a branch above an existing one that shares its number renumbers it.
`memory/project/unarmed-branches.txt` holds exactly one row, `unattended.sh` check 9 ordinal 1, whose
branch is in `stage_or_fail` at `:551`. This branch's home in `verb_preflight` is below that line, so
even reusing 9 would not disturb the pin. A free number is taken anyway, because the refusal is its
own rule rather than a second way to fail an existing one.

### Files touched (estimate)

`tools/unattended/unattended.sh` (one branch) · `tools/unattended/unattended.test.sh` (the fixture
stub plus two arms) · `.memory-tree.conf` (`ARMS_FLOORS`).

### Rollout

**The fixture change and the branch are ONE commit** (DEC-4). Measured in this worktree: the driver
self-test invokes `--preflight` 61 times and creates no `memory/guides/` anywhere — the string
`guides` does not appear in the file. A refusal writes nothing, so shipping the branch without the
fixture collapses every downstream arm at once, and `unattended driver selftest` is guarded on
`tools/unattended/` in `tools/gate-legs.json`, which is exactly the path this unit writes, so the leg
runs on this unit's own diff.

The stub is a stub. The driver tests existence and nothing else, and the file whose sections have to
resolve lives in the LEG's fixture, not this one.

### Alternatives rejected

- **A conditional refusal, keyed on the project shipping a method.** Rejected in the design pass: a
  check that excuses its own subject passes by finding nothing, which is this repo's most-recorded
  bug class.
- **A warning instead of a refusal.** An unattended run has no reader for a warning. The kit's
  standing rule is that presence is its own refusal.

## 5. Production-readiness checklist

- security — N/A, an existence test on a path derived from the project's own declared memory root.
- perf / scale — one `[ -f ]` per preflight.
- a11y · i18n — N/A.
- error / empty / loading states — this IS the error state; the refusal names the path it looked for.
- observability — the refusal prints through `fail`, so it carries the same `UNATTENDED check N
  FAILED` shape every other refusal does.
- risks — an adopter who installs this kit without the memory-tree kit's build method can no longer
  preflight. That is the intended reading of "run-time dependency", and it is the reason unit 18 has
  to say so in the contract.
- testing + left-shift gates — S4's two arms; the floor raise in S5 is what makes an unarmed branch
  impossible to land.
- migration / rollback — this repo carries the carrier at `memory/guides/BUILD-METHOD.md`, so no live
  run changes behaviour.
- user docs — the Skill's step 0 (unit 9) and protocol §1 (unit 18).

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs in a fixture with no `memory/guides/BUILD-METHOD.md`, it prints
  the new refusal and no run-state file exists afterwards.
- **AC2** — When the carrier is present, the same invocation prints `preflight OK`.
- **AC3** — The refusal is observed RED with its arm in place and the branch removed.
- **AC4** — Every pre-existing `--preflight` arm is green with the fixture carrying the stub, which
  is the observation that the fixture change is inert apart from the branch it arms.
- **AC5** — `python tools/memory-tree/check-arms.py` is green with the branch armed and the floor
  raised, and RED when the branch is present and its arm is removed — twice over: once for the
  unarmed branch by name, and once for 56 armed against a floor of 57.

  *Corrected at rev-2, measured. The rev-1 wording — red with the floor left unraised — asserts an
  observation that cannot happen. `ARMS_FLOORS` is one-sided upward, so 58 branches against a
  floor of 57 passes; a floor catches a DELETED guard, never an added one. Left as written, AC5
  was an acceptance criterion no run could ever fail, which is the class this build keeps
  finding. What the floor raise actually buys is the SECOND refusal above: at the old floor,
  dropping the arm leaves 56 armed against 56 and only the unarmed-branch check fires.*

## 7. Gates

`unattended driver selftest` (`tools/unattended/unattended.test.sh`) · `harness arms`
(`tools/memory-tree/check-arms.py`) · `unattended kit gate`
(`tools/unattended/check-unattended.sh`).

## 8. Open questions

none — the fork this unit could have carried was FORK-adjacent finding C10, resolved in the design
pass: the refusal is unconditional at the driver and the leg's matching arm stays silent, each for
its own stated reason. The build README records both.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the nine-agent design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds C10 and DEC-4; the free check number
  and the 61 measured `--preflight` invocations were re-measured against source at authoring.

- rev-2 · 2026-08-15 · AC5 corrected against measurement. Its rev-1 form asserted that an
  unraised `ARMS_FLOORS` reds on this unit's added branch; it does not, because the floor is a
  one-sided minimum. Observed: floor unraised exits 0, arm removed exits 1. AC5 now names the
  observation that exists. The `--preflight` count in §4's Rollout was 61 when this spec was
  authored and is 66 today — unit 1's arms moved it; AC4 is the property, not the number.

## 10. Reuse audit

- **`verb_resume` at `tools/unattended/unattended.sh:910`** — the seam. It already derives
  `$M/guides/BUILD-METHOD.md` from `MEMORY_ROOT` and already tests it with `[ -f ]`; this branch is
  the same expression with the opposite disposition, so the two cannot drift onto different paths.
- **`verb_preflight`'s precondition block and its write barrier at `:830`** — extended by one
  branch. No new refusal path, no new message about an unchanged file.
- **`fail()`** — the message channel, unchanged.
- **`unattended.test.sh`'s fixture setup and `reset_tree`** — the stub rides the existing initial
  commit rather than adding a setup step, which is what keeps it alive across the `git clean -qfd`
  every arm begins with.

`python tools/codebase-map/reuse_lookup.py "preflight precondition refusal missing carrier file build
method"` ranked `.unattended.conf` and the `BUILD-METHOD.md` inventory key, and printed its standing
caveat that the bash layer has no symbol extractor. The four seams above were found by hand in the
driver.

Recall terms used: unattended preflight precondition refusal build method carrier memory root
derived path fixture arm floor resume.
