# Build brief — TOOL-aBriskPreflight-6: the pre-push straggler layer sets up only when a pushed ref could carry a delta

**Serves:** research TOOL-aBriskPreflight-6

Build the unit its spec, `spec/2026-10-11-spec-TOOL-aBriskPreflight-6.md`, describes — option (d) of
its F1: every ref the layer audits today stays audited, and the layer's setup is skipped only where
`check_has_delta` could answer nothing but "no delta" — in `.githooks/pre-push` and whatever test the
spec names, and nothing else. The baseline record
(`build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md`, "The pre-push hook on a claim-shaped
push") carries the before figure: 53 s, 45 forks, 31 execs. This run sequences its unit passes one at
a time, inline, because two passes committing at once in one worktree race one git index.

## How to work in this tree — each line is a lesson a previous pass paid for

- **The spec is committed already.** Write the code in a later commit; never spec and code in one.
- **Declare before you write**, with `--dispatch` per the harness prompt. Declare EVERY path your
  commit will carry: the hook, any test file, `memory/builds/aBriskPreflight/README.md`,
  `memory/LIVE.md`, `memory/ledger/2026-10.md`, `memory/map/generated/symbols.json`, and
  `memory/guides/SESSION-KICKOFF.md` if the manifest watches the hook and the pre-commit ratchet asks
  for a `last-audit` re-stamp.
- **Stage your declared paths AND `memory/builds/aBriskPreflight/RUN.md`** in the pass commit.
- **Name a new function** with `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`
  first; after adding or renaming any function, `python tools/codebase-map/gen_map.py --write`.
- **Measure in a throwaway clone, never this tree.** Running the hook directly writes the push
  journal of the git dir it runs in. `%TEMP%/bp/C` is a clone at BASE already; make your own under
  `%TEMP%/<short>` for the after figure. Feed one claim-shaped line on stdin —
  `refs/gov/runs/x <sha> refs/gov/runs/x 0000000000000000000000000000000000000000`, the sha a
  parentless commit over the empty tree (`git mktree </dev/null`, then `git commit-tree`) — and trace
  with the build's `…-run-traced.sh`/`…-trace-spawns.py` instruments. Put the before and after wall,
  forks and execs, with the host's spawn cost, in the commit message.
- **No suite, no bar.** Verify the straggler refusal and the pre-flip notice through SLICED arms of
  the suite that owns them, in a temporary script inside `.githooks/` or `tools/`, run alone, then
  deleted before `gen_map.py --write`.
- **Do not bump the push-main kit's version marker**: the main loop bumps each kit once, at the end.
- **Never kill a process you did not start.** The host is shared.
- Out of scope, per the spec: `REMOTE_BOUND`, the default-branch gates below the exits, and
  `straggler-guard.sh`'s own predicates.

## After the mid-build merge

The run branch merged `origin/main` at `976a85a25`, after this brief and the spec were written.
aFrugalTurnstile and aDistilledCharter landed in between: `tools/unattended/unattended.sh` grew by
about 200 lines and `.githooks/pre-push` by about 614 (a `--decide` mode, a cover pass and a
post-merge red read). Every line number in the spec is at BASE `b726385f`: re-locate each site it
names in the current tree before editing. Where something main changed invalidates a claim the
spec makes, change the spec first (rev bump, its revision-log line), then the code.
