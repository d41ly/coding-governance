# TOOL-aRepatriatedFork-11 — unattended: build-root pathspecs stop at the build root, and a pull lands its hooks wired and its pins measurable

**Status:** SPECCED · rev-1 · 2026-09-23 · node a · Tier-2 · base a7c78ad2 · streams tooling+deployer · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Four things made the unattended 1.28 pull cost both adopters hand work. Check 21 grades 41 nested
READMEs at inCMS as though they were build READMEs, so inCMS forks the check. The kit shipped two new
hooks as fragments, its own `--check` reds until they are wired, and `govkit update` then rolled the
whole kit back rather than wiring them. Check 23 requires a measured `UNDECLARED_WRITE_CEILING` and
ships no verb that measures it, so both adopters measured it by running the check at 0 and reading
the failure. The rendered protocol grew past a guide cap an adopter had declared, and nothing said so
before the hygiene gate did. This unit fixes the pathspec class, wires shipped hook fragments during
the install that lands them, adds the measuring verb, and makes protocol growth a declared decision.

## 2. Scope (IN)

- **S1** — Every `git ls-files` pathspec in the unattended kit naming a file at a BUILD ROOT carries
  the `:(glob)` magic, so `*` stops at `/`. The sites: `tools/unattended/check-unattended.sh:235`,
  `:445`, `:626` and `:2535`, `tools/unattended/unattended.sh:1398`, and
  `tools/unattended/resume-tick.sh:370`. inCMS's `awk -F/ 'NF==4'` spelling
  (`scripts/unattended/check-unattended.sh:2588`) is not taken, because it assumes `MEMORY_ROOT` is
  one segment. Observed by AC1.
- **S2** — The class gate: `check-unattended.sh` refuses any script in its own kit directory that
  spells a `builds/*/<file>` pathspec whose tail carries no `/` and no `:(glob)` magic. Pathspecs
  whose tail descends, such as `builds/*/spec/*.md`, are NOT graded, because sub-spec depth is
  intended there. Observed by AC2.
- **S3** — `govkit update` and `govkit apply` wire every landed `*.fragment.json` row of every
  touched kit before the verify pass, through the target's installed `settings-merge.py --fragment`,
  resolving the settings file as `check-wiring.sh` does: a declared `GOV_SETTINGS_JSON` first, else
  `.claude/settings.json`. One line per fragment reports `wired`, `already wired` or the refusal.
  Observed by AC3.
- **S4** — A verify rollback of a kit unwires exactly the fragments this run newly wired for that
  kit, through a new `settings-merge.py --unwire --fragment` mode, so a rolled-back kit never leaves
  an entry pointing at a hook file the rollback removed. Observed by AC4.
- **S5** — `check-unattended.sh --emit-ceiling` runs checks 1 to 27 silently and prints one line,
  `UNDECLARED_WRITE_CEILING="<n>"`, measured over this tree, with the graded population on stderr.
  `PROTOCOL.template.md:485` stops saying an adopter's value is 0 and names the verb. Observed by AC5.
- **S6** — `memory/guides/UNATTENDED-PROTOCOL.md` gains a declared ceiling row in
  `tools/template-size-limits.txt` and a gate leg, so its growth is a decision gov makes in a diff.
  Observed by AC6.
- **S7** — `adopt-unattended.sh`, in both modes, compares the rendered protocol's bytes and lines
  against the target's declared `GUIDE_CAP_BYTES` and `GUIDE_CAP_LINES` and prints one line naming
  the overflow and the conf keys. It announces and never refuses; the hygiene gate is the grader.
  Observed by AC7.
- **S8** — `KIT_UNATTENDED_VERSION` and `KIT_SETTINGS_MERGE_VERSION` move and their paired markers
  move with them. Observed by AC8.

## 3. Non-goals (OUT)

- The `tools/memory-tree/gen_build_index.py` literal in check 21's repair message
  (`tools/unattended/check-unattended.sh:2560`). It is a derived kit path and unit 2 of this build
  owns that class; inCMS's R3 repath of it is therefore unit 2's to make unnecessary.
- The rollback of RENDERED outputs and the CRLF restore class. Unit 17 of this build owns govkit's
  rollback consistency; S4 covers only the settings entries this unit's own step writes.
- Raising any adopter's guide cap. S7 reports the overflow; the cap stays the adopter's value.
- Wiring a fragment the target holds under an inert kit. The inert posture is the target's choice
  and the step declines it, as the regenerate step already does.
- The two other root-file pathspecs the S2 predicate also matches outside this kit,
  `tools/drift-audit/drift_report.py:1474` and `tools/hooks/scratch-guard.js:653`. Filed for their kits.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-2` — the derived check 21 repair path, without which inCMS's check-unattended fork keeps its R3 delta
- **consumes-from** `DEPL-aRepatriatedFork-17` — item (h) of that unit's brief, fragment wiring during `update`, which it hands here and S3 builds
- **consumes-from** `TOOL-aRepatriatedFork-19` — the card fragments check-wiring reports unwired, which S3 wires on the install that lands them
- **hands-off** external — the drift-audit and hooks kits apply the S2 predicate to their own two root-file pathspecs

## 4. Design

### Data model

The pathspec fix is one prefix: `GIT ls-files ":(glob)$M/builds/*/README.md"`. PINNED, measured
2026-09-23 on node a with and without the magic:

| Tree | `builds/*/README.md` | `builds/*/RUN*.md` | `builds/*/spec/*.md` |
|---|---|---|---|
| inCMS | 365 plain, 324 glob | 12 and 12 | 1154 and 805 |
| nc | 93 and 93 | 16 and 16 | 400 and 376 |
| gov | 127 and 127 | 66 and 66 | 735 and 714 |

The README column is the live defect; the inCMS 41 is the backlog row's figure. The RUN column is
latent everywhere today and is fixed as the same class. The spec column shows why S2 exempts a
descending tail: switching it would drop every sub-spec the kit means to read.

The wiring step, in `tools/govkit/govkit.py`, sits in `_cmd_update` after the regenerate loop that
starts at `:8560` and before the verify loop at `:8742`, and in `_cmd_apply` after `[adopt]`. It is
derived, not declared: the population is every receipt row this run landed whose path ends
`.fragment.json`, grouped by kit. For each one it records the baseline with
`settings-merge.py --check --fragment <row>`, then merges. It is gated by `GOVKIT_RERENDER`, the one
switch this verb already has for running target-side code with gov's argv, and it skips a kit
`read_inert_kits` names.

`--unwire`: removes, from the group under the fragment's event and matcher, the one command entry
whose text carries both the fragment's marker and the hook's basename, the same `check_ours` test the
merge dedups on; drops the group if that empties it; exits 0 whether or not anything was there. It
never touches a foreign command.

`--emit-ceiling`: parsed beside `--only 28` and `--skip 28` at
`tools/unattended/check-unattended.sh:85-90`; it sets the skip-28 scope, suppresses `fail` output,
and after check 23's count at `:2317-2453` prints the line. It exits 0 when a count was taken and 1
when check 23's population could not be graded at all, so a dead probe does not hand out a 0.

### Inventory

New names: the flag `--unwire` in `tools/settings-merge.py`, the flag `--emit-ceiling` in
`tools/unattended/check-unattended.sh`, the gate leg `unattended protocol size`, and one Python
function in govkit for the step. Its name is asked of the lexicon leg at build time; the working name
is `wire_landed_fragments`, under the Python function cell.

### Migration

At both adopters every hook the 1.28 pull shipped is wired already, by hand, so S3 reports
`already wired` for each and changes nothing. A later pull shipping a new fragment lands it wired.

What each adopter then does:

- **inCMS** takes gov's `scripts/unattended/check-unattended.sh` verbatim once unit 2 lands the
  derived repair path, and deletes the `scripts/unattended/check-unattended.sh` row, marker
  `KIT_UNATTENDED_CHECK_DELTA`, from `.governance/kits.json`. Its C21 is S1, its C21B and C30 are
  already upstream or retired per the row's own text, and R1 and R2 are comment repaths gov derives.
  The four lone CR bytes the file lost in `6ca2d0b38` return with gov's bytes. Its
  `.unattended.conf:51` comment may cite `--emit-ceiling` instead of a failed run.
- **NicoCares** carries no unattended carve-out this unit touches; its `check-unattended.sh` is
  already gov's bytes less the four lost CRs, which gov's bytes restore. Its `.memory-tree.conf:218-221`
  guide-cap move stays; S7 would have named it on the pull instead of the hygiene gate.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/resume-tick.sh`
- `tools/unattended/adopt-unattended.sh`
- `tools/unattended/PROTOCOL.template.md` and its render `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/settings-merge.py`
- `tools/govkit/govkit.py`
- `tools/template-size-limits.txt`
- `tools/gate-legs.json`
- `WIRE-INTO-PROJECT.md`
- `memory/map/features/unattended.md`

### Alternatives rejected

- **Per-kit `[[regenerate]]` lines calling `settings-merge.py`.** Six kits ship fragments today
  (`git ls-files '*.fragment.json'` under `tools/` and `skills/`); a declaration per kit is six places
  to forget, and `TOOL-aReplayedCard-15` records the same gap for two of them. A derived step closes
  the class once.
- **Let `adopt-unattended.sh` write settings.json.** `tools/hooks/kit.toml:52-54` rules the file is
  settings-merge's, and `adopt-process-monitor.sh:13-18` refuses to write it for the same reason.
- **Refuse in S7.** The render is correct; the cap is the adopter's decision, and a refusal would
  block an install over a number only the adopter can change.

## 5. Production-readiness checklist

- security — S3 runs target-side code: the target's own installed `settings-merge.py`, with an argv
  built by govkit from receipt rows and never from the target's `deploy.toml`. The hooks it wires are
  the kit's shipped hooks; `stop-guard.js` and `stall-recorder.js` both exit 0 with no effect for a
  session no run-state record binds.
- perf / scale — one `settings-merge` spawn per landed fragment, two with the baseline probe; ten
  fragments ship today.
- error / empty / loading states — no landed fragment prints nothing and runs nothing; a missing
  settings-merge prints that the fragments landed unwired and why; `--emit-ceiling` refuses an
  ungraded population.
- observability — one line per fragment, and S7's overflow line on every adopter run.
- risks — wiring changes every future session's hook set on the adopter's machine without a
  separate prompt. Bounded by the report line and by `GOVKIT_RERENDER=0`; F1 asks whether it should
  ride that switch.
- testing — arms in `tools/unattended/check-unattended.test.sh`, `tools/settings-merge.py --selftest`
  and govkit's own selftest; see §7.
- migration — no adopter state changes on the next pull, measured above.
- user docs — `WIRE-INTO-PROJECT.md`'s hook-wiring step says the install now does it;
  `PROTOCOL.template.md` names `--emit-ceiling`.

## 6. Acceptance criteria

- **AC1** — When a fixture tree holds a build README for `tOne` and a second README one directory
  deeper under the same build, neither carrying markers, `bash tools/unattended/check-unattended.sh`
  names only the build-root file in check 21.
  Red when: the pathspec lacks `:(glob)` and the nested file is graded.
- **AC2** — When a staged copy of `unattended.sh` spells `"$M/builds/*/RUN.md"` without the magic,
  `bash tools/unattended/check-unattended.sh` refuses naming the file and line; with a descending
  `builds/*/spec/*.md` tail it stays silent.
  Red when: the predicate grades descending tails or misses a root-file tail.
- **AC3** — When `python tools/govkit/govkit.py update --write` lands a kit whose new fragment is
  unwired in a fixture target, the run prints `wired` for it, the fixture's settings file carries the
  entry, and the kit's `[check]` verifies green with no rollback.
  Red when: the step runs after verify, or not at all.
  fixture: a scratch target at unattended 1.27 with only `gate-guard` wired; none exists today.
- **AC4** — When the same fixture's verify rolls the kit back for another reason,
  `python tools/settings-merge.py --check --fragment` for the newly wired fragment reports it absent,
  and a fragment wired before the run is still present.
  Red when: rollback leaves the entry, or unwires a baseline fragment.
- **AC5** — `bash tools/unattended/check-unattended.sh --emit-ceiling` in a fixture with two
  over-declared passes prints `UNDECLARED_WRITE_CEILING="2"` and nothing else on stdout.
  Red when: the verb prints check output, or prints 0 over an ungraded population.
- **AC6** — `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` exits 1 on a
  render one byte over its declared row and 0 on the committed render.
  Red when: the row is absent and the file is ungraded.
- **AC7** — When a fixture declares `GUIDE_CAP_BYTES="61440"`, `bash tools/unattended/adopt-unattended.sh`
  prints the overflow line naming `GUIDE_CAP_BYTES` and still exits 0.
  Red when: the adopter is silent, or refuses the install.
- **AC8** — `bash tools/check-kit-versions.sh` exits 0 after both bumps.
  Red when: a paired marker stays on 1.28 or 1.5.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `settings-merge selftest` · `govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · `govkit refusal join` · `run-gates canary` · `run-gates gov canary` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `kit version markers` · `codebase-map coverage + freshness` · `lexicon naming predicates`

New arm: `tools/unattended/check-unattended.test.sh` · a nested README under a build, and a staged root-file pathspec without the magic · the kit gate's `ARMS_FLOORS` token moves by the S2 branch
New arm: `tools/settings-merge.py --selftest` · an entry wired by merge, then `--unwire`, with a foreign command in the same group · none
New arm: `tools/govkit/govkit.py` selftest · a fixture update landing an unwired fragment, then a forced rollback · none

The new leg `unattended protocol size` is not an arm; AC6 observes its failing case directly.

## 8. Open questions

- **F1 — does the wiring step ride `GOVKIT_RERENDER`?** Options: (a) yes, one switch for "this verb
  runs target-side code"; (b) its own switch. Recommendation: (a). A second switch is a second
  channel with no diff, the thing `.memory-tree.conf`'s cutoff history records removing.
- **F2 — what if the target did not select settings-merge?** The step then cannot wire, and a kit
  whose `[check]` grades wiring, as unattended's does, rolls back. Options: (a) add
  `settings-merge` to the unattended kit's `requires`; (b) run gov's own copy of `settings-merge.py`
  against the target. Recommendation: (a), because the target's receipt then names the program that
  wrote its settings file.
- **F3 — the protocol's ceiling value.** Options: (a) the committed render's size at build, PINNED;
  (b) the 96 KB guide default. Recommendation: (a), so the next growth is a line in this repo's diff,
  as `TOOL-dFoldedVerdict-7` asked for the three carriers it found at their caps.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, from audit-C's inCMS check-unattended section, both adopters'
  `.unattended.conf` and `.memory-tree.conf`, and the pathspec census measured on node a.

## 10. Reuse audit

Two existing seams carry this unit. `settings-merge.py --fragment` is already the one writer of a
target's settings file and is extended with `--unwire` rather than duplicated; govkit's regenerate
step at `tools/govkit/govkit.py:8535-8600` is the existing place target-side code runs before
verify, and the new step sits beside it under its switch. `reuse_lookup.py` returns the `.unattended.conf`
affordance seam for the wiring query and scans no `.sh`, so the pathspec sites were found by grep.
`TOOL-aGradedDoorway-4` and `TOOL-aReplayedCard-15` are the open rows this unit answers.

Recall terms used: `unattended`, `check 21`, `pathspec`, `glob`, `nested README`, `fragment`,
`settings-merge`, `stop-guard`, `stall-recorder`, `rollback`, `UNDECLARED_WRITE_CEILING`,
`GUIDE_CAP_BYTES`, `PROTOCOL`, `adopter`.
