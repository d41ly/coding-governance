# Build brief — TOOL-aBriskPreflight-4: preflight starts its bounded probes together and collects each at its own check

**Serves:** research TOOL-aBriskPreflight-4

Build the unit its spec, `spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md`, describes, in
`tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`, the unattended-stops dossier
and the regenerated `symbols.json`, and nothing else. This run sequences its unit passes one at a
time, inline, because two passes committing at once in one worktree race one git index; no sibling
pass runs while you build.

## The tree you start from

- The run branch merged `origin/main` at `976a85a25`: aFrugalTurnstile and aDistilledCharter grew
  `unattended.sh` by about 200 lines and `unattended.test.sh` by about 195. TOOL-aBriskPreflight-5 then
  landed at `60ac9f5f5` in `check_single_live` and `read_derived_phase`. Every line number in your
  spec (`:234`, `:8451`, `:8588`, `:9964`, `:10173`, `:10603`, `:12096`) is at BASE `b726385f`:
  re-locate each site in the current tree. Where main's changes invalidate a claim the spec makes —
  a new `run_bounded` caller, a moved extraction site, a changed `GB_CMP` block — change the spec
  first (rev bump, revision-log line, its own `Pass: none` commit), then the code.
- `KIT_UNATTENDED_VERSION` reads 1.97 now, main's bump; do not touch it or any `gov:kit unattended@`
  marker.
- Unit 1's pass found that `tools/gate-lint/sh_hygiene.py` refuses a loop fed by a here-document or
  here-string over a variable a command substitution filled, with a shrink-only registry. Run the
  leg's predicate (`sh_hygiene.scan_file`) over the driver before committing, as unit 5's pass did.

## How to work in this tree — each line is a lesson a previous pass paid for

- **Declare before you write**, with `--dispatch` per the harness prompt: the driver, the suite, the
  dossier, `memory/builds/aBriskPreflight/README.md`, `memory/LIVE.md`, `memory/ledger/2026-10.md`,
  `memory/map/generated/symbols.json`, and any record you add.
- **Stage your declared paths AND `memory/builds/aBriskPreflight/RUN.md`** in the pass commit.
- **Name every new function** with `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`
  first, and hoist any new suite helper beside `anchor_restore` (the check-unattended suite refuses a
  helper defined inside a shard region). Run `python tools/codebase-map/gen_map.py --write` after.
- **No suite, no bar.** `unattended.test.sh` is a multi-hour suite. Verify each arm you add through a
  SLICE (prologue plus that block, a temporary script inside `tools/unattended/`, run alone, deleted
  before `gen_map.py --write`). A preflight-level observation goes in a throwaway clone: the build's
  A/B rig prepares one, `bash <scratch>/ab-prep.sh <dir> <code-sha> <tree-sha>` with a fixture slug
  `aTimedFixture` whose remote is the local bare mirror `%TEMP%/bp/R.git` — never the real origin.
- **The order of preflight's printed lines is an acceptance criterion**: compare a preflight's
  stdout before and after on one tree, line for line.
- **Never kill a process you did not start**, and no child of yours may outlive the verb unrecorded.
- Out of scope, per the spec: the driver's readers `fact`, `runmd_of`, `readme_of`
  (aSparedSpawn-8 S1), and the children's own cost.
