**Serves:** journal TOOL-dAlignedCarrier-1..6

# Spec brief — dAlignedCarrier, all 6 units

ONE file for the whole roster. The build method (M2) requires sub-specs to AGREE on scope, interface,
ordering and acceptance, and four of the six units edit the same two files, so an author who has read
only their own row cannot check that. Read your unit's row, the shared-file table, and the rules.

## The mandate

The owner landed `memory/builds/dAlignedCarrier/README.md` with `asks: TOOL-dDerivedDocket-70..74`.
The asks are filed in `memory/builds/dDerivedDocket/BACKLOG.md` (rows 25-29, SCOPE locators at
446-450). Each ask's `accept` clause IS the acceptance the owner signed: a unit's §6 must imply it, and
may add to it, never weaken it. The owner's rulings behind four of them are rows in
`memory/DECISIONS.md` under the same ids (TOOL-dDerivedDocket-70 to -73), dated 2026-09-30; cite them in
§8 as `RESOLVED (owner, 2026-09-30)` and never re-decide them.

**The governance carriers these units edit are IN SCOPE by the mandate**, not a veto-2 fork: each is
named by the accept clause of an ask the owner landed. Veto 2 still applies to any carrier an accept
clause does NOT name (AGENTS.md and the charter template are OUT for every unit).

## The units

| Unit | Order | Closes | Mechanism |
|---|---|---|---|
| TOOL-dAlignedCarrier-1 | 1 | closes TOOL-dDerivedDocket-74 | the driver comment above `read_leg_argv` in `tools/unattended/unattended.sh` stops saying no driver verb commits, and `tools/unattended/check-unattended.sh` gains a case-insensitive scan of the kit's shipped files for the retired premise, seen RED on a staged instance |
| TOOL-dAlignedCarrier-2 | 1 | closes TOOL-dDerivedDocket-73 | the protocol's `gates-green` row and its non-overridable-items text (`tools/unattended/PROTOCOL.template.md`, rendered to `memory/guides/UNATTENDED-PROTOCOL.md`) point at `UNATTENDED-STOPS.md` section 13 and check 83 instead of restating the old boundary |
| TOOL-dAlignedCarrier-3 | 1 | closes TOOL-dDerivedDocket-71 | `researched` and `solution-tested` carry scope `all`: `DIRECTIVES_CORE` in the driver, the Skill's directive table and its scope prose (`tools/unattended/SKILL.template.md`), protocol section 10's prompt-only rationale, and whatever `check_waiver_scope` and the kit gate's scope join then read |
| TOOL-dAlignedCarrier-4 | 1 | advances TOOL-dDerivedDocket-72 | `--status <slug>` also reports, READ-ONLY, the holder-worktree verdict (check 58's question) and the pinned-asks verdict (check 73's question) that a no-id `--resume` runs before refusing; `UNATTENDED-STOPS.md` section 8's regrounding sentence follows |
| TOOL-dAlignedCarrier-5 | 2 | closes TOOL-dDerivedDocket-72 | BUILD-METHOD M7 step 1 names `--status <slug>` under a mandate (`tools/memory-tree/BUILD-METHOD.template.md`, rendered to `memory/guides/BUILD-METHOD.md`), keeping `playbook-followed` named in M7; ordered after unit 4 because it points at what unit 4 adds |
| TOOL-dAlignedCarrier-6 | 1 | closes TOOL-dDerivedDocket-70 | the owed-flagged-bar notice (`print_selftests_owed`, today called inside `--close`) prints at VERIFYING entry instead, and the Skill's close sequence tells the MAIN LOOP to export `GATE_SELFTESTS=1` into its one `--close` when the range owes it; the driver still sets the flag nowhere |

Every unit is Tier-2: each is a shipped-kit edit.

## Files more than one unit writes — the build is SEQUENTIAL because of them

| File | Units |
|---|---|
| `tools/unattended/unattended.sh` | 1, 3, 4, 6 |
| `tools/unattended/SKILL.template.md` and its render `.claude/skills/unattended/SKILL.md` | 3, 6 |
| `tools/unattended/PROTOCOL.template.md` and its render `memory/guides/UNATTENDED-PROTOCOL.md` | 2, 3, 6 (only if 6 names the protocol) |
| `tools/unattended/STOPS.template.md` and its render | 4 |
| `tools/unattended/check-unattended.sh` | 1, and 3 if the scope join lives there |

Name in §3 Edges every file your unit shares with a sibling, and in §2 exactly which region of it you
touch, so the build order cannot make two units disagree about the same lines. Where two units edit
one paragraph, the LATER order owns the paragraph and the earlier spec says so.

## Rules every spec follows

- **No suite, no bar, in any criterion.** The owner WAIVED the unattended kit's own self-test suites
  for this landing (the README's build-level rule). A criterion is observed by a direct check: the
  kit gate `bash tools/unattended/check-unattended.sh` on a staged break, a driver fixture run in a
  scratch repository, a grep over a rendered file, `python tools/memory-tree/check-memory-hygiene.sh`.
  Where a new `fail` branch in the driver needs an arm line in `tools/unattended/unattended.test.sh`
  for the arms meta-gate, the arm is WRITTEN and its RUN is named as not observed under that waiver.
- **`tools/unattended/check-unattended.sh` carries raw CR bytes on purpose.** Say in §4 that it is
  edited in bytes (a binary-safe read and write), never through a text-mode rewrite.
- **Kit versions are NOT a unit's work.** The orchestrator makes ONE version sweep at VERIFYING over
  every kit this build moved (unattended, memory-tree); no unit bumps a version or names one in §6.
- **Renders are a unit's work.** A unit that edits a `.template.md` re-renders its copy in the same
  pass and names the render command in §4; the parity leg is the observation.
- **Two units that change a sentence both carry** — say, the Skill's "kit work owes the
  `GATE_SELFTESTS=1` form too, run by you at VERIFYING" bullet (unit 6) — are the LATER unit's; a
  sibling that meets it leaves it alone.

## Evidence already gathered

A research pass on 2026-09-30 read each of these asks against the tree at `9888065c` and had a
skeptic refute it. Its notes are outside the repository and are REFERENCE, not a source to cite in a
spec: `research-1-2.md` (M7, M12), `research-3-6.md` (the inherited-red carriers), `research-9-10.md`
(the self-test flag, the no-verb-commits premise) and their `verify-*.md` siblings, under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-build-readme-governance-18d6ea/2588f719-5358-4984-93bc-1f908a71e0ab/scratchpad/parked/`.
Re-verify any line number there against the tree before building on it: the tree has moved.

Points the skeptics established that a spec must not get wrong:

- Unit 3: `check_waiver_scope` runs at preflight BEFORE the asks fact is pinned; the scope token set is
  joined against `AUTH_SCOPES` in `check-unattended.sh`. With scope `all` no new token is needed.
- Unit 4: a no-id `--resume` runs `check_holder_worktree` (check 58) and `check_asks_pinned` (check 73)
  before its refusal; `--status` runs neither today. Reporting them read-only must write nothing.
- Unit 6: `print_selftests_owed` computes its range as `HEAD^1..HEAD` of the PREPARED landing merge,
  which does not exist at VERIFYING entry. Deciding what range the earlier notice reads is this
  unit's fork (M3), and the pass-through arm that pins the driver never setting the flag must hold.
