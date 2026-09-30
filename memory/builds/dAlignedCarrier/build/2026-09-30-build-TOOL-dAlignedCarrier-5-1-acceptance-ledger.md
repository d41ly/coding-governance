# TOOL-dAlignedCarrier-5 — acceptance ledger

**Serves:** journal TOOL-dAlignedCarrier-5

M7 step 1 of `tools/memory-tree/BUILD-METHOD.template.md` now names `--status <slug>` where it named
the no-id `--resume <slug>`, 8 bytes for 8, and `kit-dogfood-parity.test.sh --render` wrote the same
line into `memory/guides/BUILD-METHOD.md`; the manifest's `last-audit` line is re-stamped. The §6
greps, the M7 `diff`, `check-template-size.sh`, one `--status` run over this run's own record and
`manifest-check.sh --staged` stood in for the `kit/dogfood doc parity`, `build-method size` and
`kickoff-manifest ratchet` legs. No suite ran, and no criterion needed one.

**Evidences:** TOOL-dAlignedCarrier-5
- AC1 — `unattended/unattended.sh --status <slug>` — the `--status <slug>` grep over the template
  printed one line, `228:1. `, between `219:## M7` and `239:## M8`; the `--resume` count printed 0,
  where BASE `87c245b3` prints 1.
- AC2 — `rendered memory/guides/BUILD-METHOD.md` — the render rewrote all four live copies and git saw
  only that one move; AC2's M7 `diff` printed nothing and exited 0, and `git status --porcelain` over
  `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` and `memory/guides/ANNOTATION-STYLE.md` printed nothing.
- AC3 — `1` — the awk count of the backticked `playbook-followed` inside M7 of the render printed 1
  after the render, and 1 before the edit.
- AC4 — `27422 / 30720 bytes` — `wc -c` of the render and `git cat-file -s` of BASE both printed
  27422; `check-template-size.sh` exited 0; `git diff --numstat 87c245b3` printed `1 1` for each of
  the two paths. The same run printed an advisory high-water WARN (26941 -> 27422) that BASE already
  carried, since this unit adds 0 bytes; re-recording it is not this unit's write.
- AC5 — `asks as pinned · worktree holds the run` — `--status dAlignedCarrier` in this worktree
  exited 0 with one phase line carrying both verdicts and the lander-mode line, and
  `git status --porcelain` read byte-identical before and after it (`cmp` exited 0).
- AC6 — `no-id spelling` — the grep over `memory/guides/UNATTENDED-STOPS.md` and
  `tools/unattended/STOPS.template.md` printed nothing and exited 1; at BASE it prints line 189 of each.
- AC7 — `MANIFEST check 5 FAILED` — printed, exit 1, with the manifest unstaged and the watched
  `memory/guides/BUILD-METHOD.md` staged; re-staged, `manifest-check.sh --staged` printed nothing and
  exited 0, and `git diff --cached -- memory/guides/SESSION-KICKOFF.md` moved the `last-audit` line
  alone.
