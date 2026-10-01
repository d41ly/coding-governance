# TOOL-dMendedRecall-3 — acceptance ledger

**Serves:** journal TOOL-dMendedRecall-3

The `--status` entry of `tools/unattended/VERBS.template.md` now describes the line `verb_status`
prints, field by field and in printed order: the `unattended: <slug>` opener, the fields every line
carries, the optional fields with the condition that prints each, and the pinned-asks and
holder-worktree verdicts before the keepalive field, saying that those two print on a pass. The
adopter re-copied the render. The greps of AC1 to AC3, a read of this run's own live `--status`
line for AC4, and `cmp` with `git diff --stat` for AC5 stand in for the `unattended kit gate` leg's
check 10 and check 26, which this pass did not run; AC6 and the rest of section 7 are the close's.

**Evidences:** TOOL-dMendedRecall-3
- AC1 — `asks as pinned` — `grep -c -F` over the template printed 1 for each of
  `asks as pinned`, `asks moved at HEAD`, `worktree holds the run`, `worktree not the run` and
  `worktree unanswerable`, and the same five counts over `git show 1f915870` of the file each
  printed 0.
- AC2 — `check 73` — the awk cut from the `--status` bullet to the `--audit` bullet, 30 lines,
  carried `check 73` twice, `check 58` twice and `lease-utc` once. Split into sentences, the three
  that say when the two verdicts print each carry the word `pass`, among them "the optional fields
  that print on a pass as well as on trouble".
- AC3 — `(no non-terminal unit)` — every fragment the entry now spells, cut at its placeholders and
  its `present|absent` alternation, counted with `grep -c -F` semantics over
  `tools/unattended/unattended.sh`, and every count was at least 1: `unattended: ` 153, ` · ` 253,
  `phase ` 132, `LANDED (derived: ` 2, ` on ` 565, ` at ` 421, `)` 1772,
  `LANDING (not on the remote: ` 1, `witness ` 56, `NONE` 4, `next ` 71,
  `(no non-terminal unit)` 1, `halt-code ` 4, `spec-audit ` 15, `parked ` 57, `noted ` 4,
  `STALE briefs ` 3, `briefs gone ` 1, `resume-tick ` 1, ` attempt(s), last ` 1, `orphans ` 3,
  `asks as pinned` 1, `asks moved at HEAD, check 73 refuses a resume: pinned [` 1,
  `] at HEAD [` 1, `]` 1178, `worktree holds the run` 1,
  `worktree not the run's, check 58 refuses a resume here: ` 1,
  `worktree unanswerable, the record names no run branch` 1, `keepalive ` 47, `present` 13,
  `absent` 91 and ` in the harness listing at ` 1. A first cut of the splitter, which left
  `absent` joined to the fragment after it, printed 0 for that joined string, so the count can red.
- AC4 — `asks as pinned · worktree holds the run` — `--status dMendedRecall` in this worktree
  printed `unattended: dMendedRecall · phase BUILDING`, then the witness, `next TOOL-dMendedRecall-3`
  with its title, `noted 9`, the two verdicts and
  `keepalive 31020819 present in the harness listing at`. Each head's first backticked occurrence
  in AC2's cut was found, at increasing
  offsets in the line's order, the opener at 35 and `keepalive ` last at 2316. The same reading over
  the BASE entry found only `keepalive `, so the probe can red.
- AC5 — `cmp` — `bash tools/unattended/adopt-unattended.sh` printed `installed` for
  `memory/guides/UNATTENDED-VERBS.md` and re-rendered the Skill, `cmp` of the pair exited 0, and
  `git diff --stat` named only the template and that render: no other file under `memory/guides/`
  or `.claude/skills/unattended/` moved.
- AC6 — `unattended_kit_gate.log` — NOT observed here. The criterion's own permission clause puts
  it at the close's bar, where the `unattended kit gate` and `unattended skill wiring` rows and
  their persisted logs are read; check 10's byte compare is what AC5's `cmp` previews.

## What this ledger does not evidence

None of the five section 7 legs ran in this pass. `unattended kit gate`, `unattended skill wiring`,
`dead-path carriers (deleted files still named)`, `recall floor` and `recall floor arms` are all the
close's. `verb_status` prints further LINES beside the one this entry describes: the in-place
`LANDER_MODE` line, the presumed-stopped and landed-observation lines, and the held checkpoint
block. No entry of the verb contract names them. They are outside this unit's scope, which keeps
the entry's one-line promise about the status line itself, and they belong with the hands-off
check that joins the driver's output to this entry.
