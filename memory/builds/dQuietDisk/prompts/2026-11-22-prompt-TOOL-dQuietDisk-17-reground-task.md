**Serves:** research TOOL-dQuietDisk-9 TOOL-dQuietDisk-17

# Spec task — dQuietDisk: re-ground orders 5 and 6 on the built order 4

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. Read the spec brief first,
`memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`. Its rules bind this task.

## The base

Orders 1 to 4 are built and CLOSED. TOOL-dQuietDisk-6 is WONTDO and TOOL-dQuietDisk-15 is DEFERRED. Since order 4's
re-ground at `c3c0811b8`, `HEAD` adds:
- TOOL-dQuietDisk-16, one lazy `cat-file --batch` handle for `govkit update`'s receipt-row reads: `BlobBatch` and
  `build_blob_batch` in `tools/govkit/upgrade_steps.py`, threaded through `_cmd_update` in `tools/govkit/govkit.py`
  (`fe51f4d4d`);
- TOOL-dQuietDisk-26, `tools/check-wiring.sh` listing the tree once per invocation (`b31f3bd11`);
- TOOL-dQuietDisk-11, the govkit suite's 70 recurring `build_target` calls on the template cache, and
  `{prefix}/lib/template_cache.py` in the `govkit selftest` guard of `tools/govkit/registry.toml` and
  `tools/gate-legs.json` (`33a4e2325`).

Read the code each spec cites as it stands at `HEAD`. The worktree is checked out there.

## Re-ground each of units 17 and 9

- **Re-check every code fact** at `HEAD`, and re-cite each moved one by symbol or as `<path>@<blob>:<line>`.
  TOOL-dQuietDisk-17 was last grounded at `59e882af`, before any order was built: re-read `cmd_update`, `_cmd_update`
  and the verify pass in `tools/govkit/govkit.py` whole, as units 14, 18 and 16 left them.
  TOOL-dQuietDisk-9 was last grounded at `b3f5a2bc`: re-read every file in its Files touched, among them
  `.githooks/pre-push.test.sh` (unit 12), `tools/gate-legs.json` (unit 11), `tools/run-gates/run-gates.sh` (unit 5)
  and `tools/lib/lib-selftest.sh` and `tools/lib/template-cache.sh` (unit 7), whose scratch paths unit 9 may own.
- **Prove the saving, or say there is none.** State today's cost from the code and probe it where you can. Where
  nothing saves, name it in section 8 as a fork, with "close as WONTDO" among the options.
- **Unit 17 and unit 14's attestation.** Unit 14 built the receipt's `attestations` key and
  `tools/govkit/govkit.py#derive_kit_attestations` (`6749bfa8d`). Unit 15, which consumed it, is deferred: both
  adopters' default bars already hold gov kit self-tests, so fix 3's attestation saves nothing today (ask
  TOOL-dQuietDisk-33). Say whether unit 17's verify-pass reuse depends on either, and correct any edge that names
  unit 15 as built.
- **Unit 17 and unit 18 share `tools/govkit/selftest.py`**, now also changed by unit 11. Build on both units' arms.
- **Unit 9 and the template cache.** The cache's root and its stage directories are scratch paths. Say whether unit 9's
  owned root holds them, and cite `tools/lib/template_cache.py` by symbol.
- **Check every git command, flag and shell idiom against the real tool** before the spec relies on it. This build has
  already ruled on these false facts:
  - `git rev-parse --short` takes a single revision;
  - a local `git clone --shared` spawns two processes;
  - an MSYS shell rewrites a `!/path` argument;
  - `git hash-object --stdin-paths` and an alternates line both refuse an MSYS `/c/...` path;
  - a plain `ls=$(...)` assignment makes the shell-hygiene scanner follow a heredoc loop over that variable, where
    `if ! ls=$(...)` did not (TOOL-dQuietDisk-26's widen 12). A spec that adds such a loop or assignment says so.
- **State the files**, generated outputs included. Name the other unit, 17 or 9, if its Files touched shares a path
  with this one. Shell-line rows grow only through `python tools/memory-tree/ratchet.py widen shell-role`, which the
  main loop runs after the pass.
- **Record the re-ground.** Set the header's base to the `HEAD` you read at, bump the rev and add a revision-log line:
  `re-grounded at <sha> (orders 1 to 4 built), <what moved>`.

Nothing in a unit's goal moves. Where the re-ground changes scope or acceptance, say why in the revision-log line.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk <your unit id>`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Mark every figure you add PINNED, DERIVED or with an id on its own line. A section number before a noun reads as a
  count, so word around it.

Return: your spec's new rev, what moved, the saving it now states, any fork you open, and whether the other unit's
Files touched shares a path with it.
