**Serves:** journal PLAY-dDerivedDocket-1

# PLAY-dDerivedDocket-1 — acceptance ledger

One commit carries the unit: the template edits, the fresh `gov:playbook` render, the authored
`AGENTS.md` lines S4 and S8 name, the `memory/DECISIONS.md` row, the kickoff manifest's re-stamp,
one word of the unattended dossier, this ledger and the CLOSED header. The spec is unchanged at
rev-9; every figure its §4 projected was what the commit measured.

NO MERGE BAR, NO GATE LEG AND NO SUITE FILE RAN IN THIS PASS. The direct checks were the renderer
this unit's fence rides on, `render_playbook.py`, run over scratch fixture targets built under this
run's scratch root, and plain `grep`, `tr` and `wc` reads over the tree. The write-mode render,
`adopt-playbook.sh --target .`, is S4's own step rather than a check.

## What this ledger does NOT evidence, and why

AC1, AC3, AC4, AC8 and AC9 carry `permission:` lines and get no line here; the orchestrator writes
them after the post-build bar, whose `template size <=48KiB`, `playbook render wiring`,
`charter size`, `kickoff-manifest ratchet` and `line length` legs make the observations. The in-pass halves
those permission lines give the pass were read, and are recorded here as prose, not as answers:

- **AC1's two counts.** `tr -d '\r' | wc -c` over the template reads 48,229 at the parent,
  `3215c6cb`, and 48,184 at this commit: 45 bytes lower, the −45 §4 projected, 968 under the
  declared 49,152.
- **AC4's two counts.** The same read over `AGENTS.md` gives 64,333 at the parent and 64,210 at this
  commit: 123 lower, 302 under the declared 64,512. The region alone fell 155 bytes, the figure §4
  projected; the authored lines gave back 32 of it.
- **AC8's stamp.** The `last-audit` line's datetime advanced and its sha stays the merge-base with
  `origin/main`, `869209ed`, as the build brief states; no §B claim the template feeds changed.
- **AC9's lengths.** Counted in characters, the substitute bullet is 392 and the landing bullet 88
  in the template and in the region, both under 450. The longest line in either file is one this
  unit did not touch.

## The DECISIONS row is an undeclared write

`memory/DECISIONS.md` is in `.unattended.conf`'s `SHARED_RECORDS`, and `--dispatch` refuses any
declaration overlapping one (check 49), so S5's row could not be declared. It is written in this
commit anyway, as units 5, 19, 24, 31, 33, 34 and 61 wrote theirs, and the unattended leg's check 23
counts it against `UNDECLARED_WRITE_CEILING`. That leg is the post-build bar's to read. Unit 3 took
the other road and handed its row to the orchestrator (the run-state file's 2026-09-20 decision row).

**Evidences:** PLAY-dDerivedDocket-1
- AC1 — `template size <=48KiB` — at 364278a8 the leg (`bash tools/check-template-size.sh`) printed `template-size OK — coding-governance-agents.template.md: 48184 / 49152 bytes (968 under, 98.0%)`, exit 0. The CR-stripped `wc -c` of the template over `git show` reads 48229 at the parent 3215c6cb and 48184 at the unit commit 504683ef, 45 lower, and 48184 again at 364278a8.
- AC2 — `python tools/playbook/render_playbook.py --target <scratch>` — four scratch targets per template, each a git repository on `main` holding this repo's `.memory-tree.conf` and a copy of `.governance/deploy.toml` whose `kits` omit `unattended`, omit `kickoff-manifest`, omit both and omit neither, with `playbook_path` naming a template copy and stub answers for `ci_file`, `gate_runner` and `lexicon_conf`. At this commit `UNATTENDED-PROTOCOL` counted 0 exactly where `unattended` was omitted and 1 elsewhere; `Kickoff-manifest merge exception` counted 0 exactly where `kickoff-manifest` was omitted; the landing bullet appeared exactly where `unattended` was kept; no render carried two consecutive blank lines before §2; `grep -c 'kit-conditional — drop this block' coding-governance-agents.template.md` printed 0. RED at the parent, `3215c6cb`'s template: both counts read 1 in all four renders, and the heading note survived in each.
- AC3 — `playbook render wiring` — at 364278a8 the leg (`bash tools/playbook/adopt-playbook.sh --target . --check`) printed `render-playbook OK — region matches a fresh render, no placeholder survived`, exit 0.
- AC4 — `charter size` — at 364278a8 the leg (`bash tools/check-template-size.sh AGENTS.md`) printed `template-size OK — AGENTS.md: 64210 / 64512 bytes (302 under, 99.5%)`, exit 0, beside an advisory `TEMPLATE-SIZE WARN` that the file sits 3280 bytes above its recorded high-water of 60930. The CR-stripped `wc -c` of `AGENTS.md` over `git show` reads 64333 at the parent 3215c6cb and 64210 at the unit commit 504683ef, 123 lower.
- AC5 — `grep -n 'status updated in place' coding-governance-agents.template.md AGENTS.md` — printed nothing; §6's record-types bullet now reads "the backlog keeps stable ids (gaps fine), and how an ask's status is kept is the memory tree's rule (§5)" in both files, and `grep -c 'BACKLOG.md' coding-governance-agents.template.md` printed 0.
- AC6 — `grep -n 'backlogs shard per family' AGENTS.md` — printed nothing; the node-registry paragraph names `memory/builds/<slug>/BACKLOG.md` as where asks are filed and `memory/backlog/<FAMILY>.md` as their generated view, and the layout line joins `backlog/<FAMILY>.md` to the GENERATED `LIVE.md` + `ledger/<month>.md` group with a `+`.
- AC7 — `## PLAY — playbook` — `grep -c '^- \*\*PLAY-dDerivedDocket-1\*\*' memory/DECISIONS.md` printed 1; the row is the second under that heading and above `## KICK — kickoff`, names D12-i3, and is 272 characters.
- AC8 — `kickoff-manifest ratchet` — at 364278a8 the leg (`bash skills/session-kickoff/manifest-check.sh`) exited 0 and printed no `MANIFEST check` failure line, so check 5 passed. `git show` reads the `last-audit` line of `memory/guides/SESSION-KICKOFF.md` as `2026-09-28T02:21:57+03:00` at the parent 3215c6cb and `2026-09-28T03:08:00+03:00` at the unit commit 504683ef, both at sha 869209ed.
- AC9 — `line length` — at 364278a8 the leg (`bash tools/check-line-length.sh`) printed `line-length OK` for `AGENTS.md` and for `coding-governance-agents.template.md`, each `0 over 450 characters`, exit 0.
- AC10 — `kit:unattended` — the first fence in `coding-governance-agents.template.md` is four lines, `grep -cE 'in-place|--prepare|--land|LANDER_MODE'` over them printed 0, and its landing bullet reads "An unattended run lands by its protocol's landing rule, not the local-first one above."
- AC11 — `gov:playbook` — `grep -c 'default-branch anchor'` over the first `kit:unattended` fence printed 1; `grep -n 'folder the run did not create' AGENTS.md` hit only line 130, inside the region (79 to 465); `grep -c 'cannot have written' AGENTS.md` printed 0.
