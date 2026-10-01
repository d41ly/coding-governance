**Serves:** journal TOOL-dMendedRecall-1..3

# Spec brief — dMendedRecall, all 3 units

## The mandate

The owner landed `memory/builds/dMendedRecall/README.md` with `asks: TOOL-dAlignedCarrier-7..9`, and
asked in so many words that the memory-recall red be fixed. The asks are filed in
`memory/builds/dAlignedCarrier/BACKLOG.md`; each ask's `accept` clause IS the acceptance the owner
signed, so a unit's section 6 must imply it and may add to it, never weaken it. Each carrier an
accept clause names is IN SCOPE by the mandate; any carrier none names (AGENTS.md, the charter
template, the protocol) stays OUT under veto 2.

## The units

| Unit | Order | Closes | Mechanism |
|---|---|---|---|
| TOOL-dMendedRecall-1 | 1 | closes TOOL-dAlignedCarrier-8 | the `memory-recall kit selftest` leg, red on main since 78c4bf7d, goes green |
| TOOL-dMendedRecall-2 | 1 | closes TOOL-dAlignedCarrier-9 | an in-place `--close` whose gates-green arm auto-files an inherited-red ask commits its own record, with the generated views re-rendered in that commit |
| TOOL-dMendedRecall-3 | 1 | closes TOOL-dAlignedCarrier-7 | the `--status` entry of `tools/unattended/VERBS.template.md` and its render name the pinned-asks and holder-worktree fields |

All three are Tier-2 shipped-kit edits. They are built SEQUENTIALLY in the order 1, 2, 3, because
every pass writes the run-state file.

## What is known, as a starting point to verify — never as a citation

- **Unit 1.** The red arm is `a spec H1 anchors the id it defines, by the index generator's own
  predicate` (`tools/memory-recall/selftest.py`, the `@check` near line 2939), and it fails only in
  the self-test's ADOPTER-layout re-run (`the whole selftest passes from the ADOPTER layout (kit at
  <root>/memory-recall/)`) with `ModuleNotFoundError: No module named 'backlog'`. The arm imports
  `gen_build_index` from the memory-tree kit dir that `resolve_kit_dir` finds, and
  `tools/memory-tree/gen_build_index.py` imports its sibling `backlog` module (line ~290), split out
  by TOOL-dDerivedDocket-6/-7. The likely cause is that the adopter-layout fixture places a
  memory-tree kit without that sibling, but find the true cause: the fix belongs where the defect
  is, whether that is the fixture's copy list, the arm's import, or the generator's own import
  discipline. It is a merge interaction between main's TOOL-aRepatriatedFork-40 and dDerivedDocket.
  `gate-guard.js` denies running `selftest.py` inside a pass before VERIFYING, so the pass observes
  the fix with a scratch reproduction of that ONE arm in the adopter layout, RED before the fix and
  green after; the close's flagged bar runs the whole leg, which is the accept clause's own
  observation and is named as owed there.
- **Unit 2.** `write_close_commit` in `tools/unattended/unattended.sh` commits what is staged under
  `records(<slug>): close — LANDING`. The gates-green arm's auto-file stages an ask row in the build's
  `BACKLOG.md` and renders nothing, so the pre-commit's hygiene check 9 refuses the commit and the close
  fails check 69 after the whole bar ran. Met for real at dAlignedCarrier's close (2026-09-30) and
  recovered by hand. The accept clause asks for a fixture whose bar leaves one inherited red.
- **Unit 3.** TOOL-dAlignedCarrier-4 added two `--status` fields: `asks as pinned` / `asks moved at
  HEAD, check 73 refuses a resume: ...`, and `worktree holds the run` / `worktree not the run's, check
  58 refuses a resume here: ...` / `worktree unanswerable, ...`. Read their exact spellings and their
  print conditions from `verb_status` itself. The VERBS entry states the fields that print only when
  there is something to report; say when each new one prints.

## Rules every spec follows

- **No suite, no bar, in any criterion.** The unattended kit's own suites are WAIVED for this landing
  (the README's rule). A new driver `fail` branch still gets its arm line written in its suite for the
  arms meta-gate; the arm's run is named as not observed.
- **Kit versions are not a unit's work.** One sweep at VERIFYING by the orchestrator.
- **`tools/unattended/check-unattended.sh` carries raw CR bytes**: any edit there is in bytes.
- **Renders are a unit's work**, in the same pass, with the render command in section 4.
