# TOOL-aWokenSentinel-11 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-11

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite, per the build README's rule three. The pass verified with the direct checks the spec's
section 7 names for it — the checker run WHOLE over a frozen `--local` clone of this worktree at
`85c7761f` under `%TEMP%/ws11`, with the working tree's edited checker copied beside the clone's
driver and lib, once per driver copy: the inline second spelling (AC1 red), the same line as a
comment (the near-miss, green), the unmodified driver (AC1 green) and the driver with its one
`$(resolve_sidecar_dir)` call site deleted (AC2). The four runs cost 165, 193, 218 and 201 s on node `a`,
against the 199 s the spec pinned from the gate ledger. The suite's new arm was run ALONE with the suite's
preamble sourced (lines 1 to 278 of `check-unattended.test.sh`, `HERE` re-pointed at this
worktree's kit dir, `TMPDIR` at `%TEMP%/ws11t`): it executed six assertions and failed none.
`bash -n` over both edited files. `python3 tools/memory-tree/check-arms.py` in assert mode exited
0 and its `--report` row reads `check 32 branch 1 line 3560 ARMED`. Those stand in for the
`unattended kit gate` and `harness arms (fail branches armed or pinned)` legs.

**Evidences:** TOOL-aWokenSentinel-11
- AC1 — clone's driver with `_x=$(GIT rev-parse --git-dir)/unattended` appended at line 2922 inside `verb_status`; `bash tools/unattended/check-unattended.sh` in the clone printed exactly one `FAILED` line, `UNATTENDED check 32 FAILED — the kit must hold ONE derivation of the sidecar root … code-line count: 2 (lib: 1), driver callers: 1`, exit 1, 165 s; the other 33 lines were check 7 EXCLUDED announcements and check 23 report lines, identical across every run below. The same line appended as a COMMENT printed 0 `FAILED` lines and 0 lines naming `check 32`, exit 0, 193 s — the near-miss beside the hit. The driver restored (`git checkout -- tools/unattended/unattended.sh`, `git status` clean on that path) printed 0 `FAILED` lines and 0 lines naming `check 32`, exit 0, 218 s. OBSERVED.
- AC2 — clone's driver with the line `sidecar=$(resolve_sidecar_dir) || …` deleted (one line, `git diff --stat` 1 deletion); the checker printed one `FAILED` line, `UNATTENDED check 32 FAILED — … code-line count: 1 (lib: 1), driver callers: 0`, exit 1, 201 s. OBSERVED.
- AC3 — `grep -c 'does NOT check' tools/unattended/check-unattended.sh` printed `0` over `git show 85c7761f:` (the base of this pass; the spec's `12b3701d` predates unit 20 and the count there is also `0`) and `1` at the tip; the one header line opens `What this check does NOT check` and the paragraph names `rev-parse --git-common-dir`, a `$GIT_DIR` read, a path composed from `.git`, the two hooks `stop-guard.js` and `stall-recorder.js` with `deriveSidecarPath`, and a COMMENT-line spelling. OBSERVED.
- AC4 — `python3 tools/memory-tree/check-arms.py --report` at the tip lists `check 32 branch 1 line 3560 ARMED` under the `tools/unattended/check-unattended.sh -> tools/unattended/check-unattended.test.sh` pair, and assert mode exits 0; `grep -c 'code-line count: 2' tools/unattended/check-unattended.test.sh` printed `1` at the tip and `0` over `git show HEAD:` at base. The `harness arms (fail branches armed or pinned)` leg itself: observed at --close.

## What this ledger does not evidence

No kit gate leg, harness-arms leg, hygiene leg, spec-token leg or install-prefix leg ran inside
this pass; every one is `--close`'s and each row above says so. Section 7's floors moved by
exactly the arm: `FLOOR_ASSERTIONS` 410 to 416 and `FLOOR_SHARD_2` 319 to 325, by the six
assertions the arm-alone run executed (three `mutate`, two `hit`, one `miss`), all in region two,
with `FLOOR_SHARD_1` untouched; the suite whole, sharded or not, is observed at --close and is
what grades those floors. The `fail 32` number is derived
from the tree (`grep -oE 'fail [0-9]+'` high-water 31 at base), not copied from the spec, and the
spec's `<n>` placeholder is that number. The check's variable names differ from the spec's sketch
(`_sd_in_lib` and `_sd_calls` for the spec's `_sd_lib` and `calls`, so a shared global named
`calls` cannot be clobbered); the refusal sentence and the interpolated fields are the spec's
verbatim. `resume-tick.sh` does not exist at this order, so the third member of the population
contributed zero in every run above and the tick's own spelling is first graded by the unit that
lands it. No identifier was minted, so no lexicon query was owed. The build README's authored
roster row for this unit moved `PLANNED` to `CLOSED` beside the spec header.
