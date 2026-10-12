# Build brief — TOOL-aBriskPreflight-5: the live-run count reads every record's phase in one pass and derives each record once

**Serves:** research TOOL-aBriskPreflight-5

Build the unit its spec, `spec/2026-10-11-spec-TOOL-aBriskPreflight-5.md`, describes, in
`tools/unattended/unattended.sh` and the one arm it adds to `tools/unattended/unattended.test.sh`,
and nothing else. The baseline record (`build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md`)
and this run's own preflight output (18 `EXCLUDED … derived LANDED` lines, two live runs) are the
population this changes. This run sequences its unit passes one at a time, inline, because two
passes committing at once in one worktree race one git index; no sibling pass runs while you build.

## How to work in this tree — each line is a lesson a previous pass paid for

- **The spec is committed already.** Write the code in a later commit; never spec and code in one.
- **Declare before you write**, with `--dispatch` per the harness prompt. Declare EVERY path your
  commit will carry: the product files, `memory/builds/aBriskPreflight/README.md`, `memory/LIVE.md`,
  `memory/ledger/2026-10.md`, `memory/map/generated/symbols.json`, and any record you add.
- **Stage your declared paths AND `memory/builds/aBriskPreflight/RUN.md`** in the pass commit: the
  `--dispatch` and `--brief` rows live there and the `brief-recorded` leg reads them AT the build commit.
- **Name a new function** with `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`
  first, and hoist any new test helper beside `anchor_restore` (the check-unattended suite refuses a
  helper defined inside a shard region). After adding or renaming any function, run
  `python tools/codebase-map/gen_map.py --write` and commit the regenerated `symbols.json` with the code.
- **No suite, no bar.** `unattended.test.sh` is a multi-hour suite: never run it whole. Verify the arm
  you add through a SLICE — its prologue plus that one block, in a temporary script inside
  `tools/unattended/`, run alone, then DELETED before `gen_map.py --write`.
- **The equivalence probe is the acceptance that matters**: every tracked record at BASE, the
  per-record reading against the primed one, field by field, with the population size printed. A
  probe that read nothing must not pass.
- **Do not bump `KIT_UNATTENDED_VERSION`** or any `gov:kit unattended@` marker: the main loop bumps
  each kit once, after its last move.
- **Never kill a process you did not start.** The host is shared. A git spawn costs about 0.75 s
  here, so batch git calls and run anything long in the background.
- Out of scope, per the spec: converting `fact`, `runmd_of` or `readme_of` (aSparedSpawn-8 S1), and
  the gate leg's own copy of this walk.

## After the mid-build merge

The run branch merged `origin/main` at `976a85a25`, after this brief and the spec were written.
aFrugalTurnstile and aDistilledCharter landed in between: `tools/unattended/unattended.sh` grew by
about 200 lines and `.githooks/pre-push` by about 614 (a `--decide` mode, a cover pass and a
post-merge red read). Every line number in the spec is at BASE `b726385f`: re-locate each site it
names in the current tree before editing. Where something main changed invalidates a claim the
spec makes, change the spec first (rev bump, its revision-log line), then the code.
