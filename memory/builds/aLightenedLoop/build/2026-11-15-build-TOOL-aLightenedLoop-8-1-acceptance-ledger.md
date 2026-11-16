# TOOL-aLightenedLoop-8 — acceptance ledger

**Serves:** journal TOOL-aLightenedLoop-8

No merge bar, no self-test suite and no gate ran in this pass. `git fetch` left `origin/main` at
`aebbb4a72`, and `git merge --no-ff --no-commit origin/main` conflicted in exactly the five files
the spec names, so the pass went on. The criteria a probe can reach were observed by the spec's own
probe, `l8.sh`, sourced from the worktree root over a fixture repository under `%TEMP%/l8`, and by
greps, `cmp`, `diff` and parse checks over the resolved tree. One staged break was run: the read
half's cache-off test reading `_stkey` in place of `_stat` turned the probe's first line to `off 1`,
and the driver was restored from a byte copy and compared with `cmp`. The gate-graded halves of
AC2, AC3, AC13 and AC14, the driver suite pooled, the six `New arm:` lines' RED-first observations
and the bar are the close's.

The owner's parity rule. `diff` over the non-comment lines of
`tools/unattended/unattended.sh#verb_dispatch` and
`tools/unattended/unattended.sh#check_spec_token_hits`, cut from `aebbb4a72` and from the resolved
tree, printed nothing; over `tools/unattended/unattended.sh#remove_spec_token_check` it printed the
reset line alone. Over `tools/unattended/unattended.sh#run_spec_token_check` the three refusals,
their texts and order, the skip line and the admit-with-note line read unchanged against
`aebbb4a72`, and unit 6's block from `_stkey=""` to the not-recorded echo reads unchanged against
`d9f84ee14` but for the one comment word the spec names.

**Evidences:** TOOL-aLightenedLoop-8
- AC1 — `bash -n tools/unattended/unattended.sh` — exited 0 over the resolved driver, and
  `git grep -n '^<<<<<<< '` printed nothing. The commit is made with `git merge --no-ff`, so its
  parents are the pre-merge tip `c20db8ff` and `aebbb4a72`; the parents read after the commit are in
  the pass's return.
- AC2 — `grep -cE '^memory/builds/a(ClearedLedger|BriskDeclaration|LightenedLoop)/README[.]md$' memory/project/readme-contract.txt`
  — printed 3, main's two rows first. `python tools/memory-tree/gen_build_index.py --check-format`
  is a gate leg the role refuses, so it is the close's.
- AC3 — `grep -c '^last-audit: ' memory/guides/SESSION-KICKOFF.md` — printed 1, and the line reads
  `2026-11-15T05:28:42+02:00 @ c20db8ffecbfa527060646059e5bff8bab75d569`, the pre-merge tip, later
  than `2026-11-15T00:53:03+02:00`. `bash skills/session-kickoff/manifest-check.sh` is the close's.
- AC4 — `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md | wc -c` — printed 68130 after the re-render, <!-- PINNED 2026-11-15 -->
  and the `awk` row prints that one value. The `grep -c` for the two raises printed 3 and the <!-- PINNED 2026-11-15 -->
  DECISIONS grep printed 1.
- AC5 — `grep -c '^FLOOR_ASSERTIONS=259$' tools/check-spec-tokens.test.sh` — printed 1, and the <!-- PINNED 2026-11-15 -->
  `RECONCILED to 259` grep printed 1. `git show` at `846d51d39`, `aebbb4a72` and `c20db8ff`, piped <!-- PINNED 2026-11-15 -->
  to the floor grep, printed 247, 254 and 252. <!-- PINNED 2026-11-15 -->
- AC6 — `bash "$SCRATCH/l8.sh"` — printed `cache first runs 1 off 0 said 0 key written`,
  `cache unchanged runs 1 skipped 1`, `cache unread runs 1 skipped 1`,
  `cache commit runs 1 skipped 1` and `cache edited runs 2 skipped 0`. With the cache-off test on
  `_stkey` the first line read `off 1`, the named red.
- AC7 — `bash "$SCRATCH/l8.sh"` — printed `cache moved runs 4 said 1 skipped 1` and
  `cache raced runs 5 said 1 key none`.
- AC8 — `bash "$SCRATCH/l8.sh"` — printed `cache popen runs 6 said 1 key none`.
- AC9 — `bash "$SCRATCH/l8.sh"` — printed
  `order state run started 7 after 7 start 0 skipped 0 key written`.
- AC10 — `bash "$SCRATCH/l8.sh"` — printed `cache off runs 9 said 2 key none`.
- AC11 — `seven ST_ globals` — its grep printed 1 and the old-design grep printed 0. The armed
  `init_bounded` and `run_bounded` spellings each counted 1, each of the six line texts counted 1
  under `grep -cF`, and the three function `diff`s read as the parity paragraph above states.
- AC12 — `grep -c '^FLOOR_ASSERTIONS=3335$\|^FLOOR_SHARD_3=451$' tools/unattended/unattended.test.sh`
  — printed 2, the `miss` line's `grep -cxF` printed 1, and the arm-name grep printed 9 over the <!-- PINNED 2026-11-15 -->
  resolved suite and over the suite read from tree `dcafc6b82`. Every arm's executed count is the <!-- PINNED 2026-11-15 -->
  close's, in the pooled driver suite.
- AC13 — `node --check tools/unattended/stop-guard.js` — exited 0. The three `read_open_py` cuts
  were equal under `cmp`, `ast.parse` passed both Python files, the `PHASE_RECORDED_FNS=` line holds
  `print_wake`, the marker grep printed one line, `gov:kit unattended@1.123`, and both template
  `cmp`s printed nothing after `bash tools/unattended/adopt-unattended.sh` re-rendered, which moved
  no rendered byte. Its `--check` is a gate leg the role refuses, so it is the close's.
- AC14 — `python tools/codebase-map/gen_map.py --check` — the three generators ran in their write
  form before the commit; the three checks are gate legs the role refuses, so they are the close's.
