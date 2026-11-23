**Serves:** research TOOL-dQuietDisk-11 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-26

# Spec task — dQuietDisk: re-ground order 4 on the built order 3

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. Read the spec brief first,
`memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`. Its rules bind this task.

## The base

Orders 1 to 3 are built and CLOSED, and TOOL-dQuietDisk-6 is WONTDO. Since order 3's re-ground at `7b8c737b0`,
`HEAD` adds:
- TOOL-dQuietDisk-28, the store resolved once per calling shell;
- TOOL-dQuietDisk-18, `govkit apply`'s reads through the target's reuse cache, in `tools/govkit/govkit.py` and
  `tools/govkit/selftest.py` (`87bd02fec`);
- TOOL-dQuietDisk-10, `tools/check-wiring.test.sh` wiring each copy from one captured config, with no template cache
  and no switch (`c687e8c83`), by its forks F2 (b) and F3 (a);
- TOOL-dQuietDisk-13, `read_template_mode` in `template_cache_sh` and the turnstile suite on the cache (`5ea60aaa9`);
- TOOL-dQuietDisk-12, pre-push's pushed fixtures copied without objects (`f0d3eac32`).

Read the code each spec cites as it stands at `HEAD`. The worktree is checked out there.

## Re-ground each of units 11, 15, 16 and 26

- **Re-check every code fact** at `HEAD`, and re-cite each moved one by symbol or as `<path>@<blob>:<line>`.
- **Prove the saving, or say there is none.** A suite moves onto the template cache only where it then spends fewer
  git processes and fewer temp entries than today. Count today's per-case cost from the code, and probe it with
  `GIT_TRACE2_EVENT` where you can. A cached clone costs three git processes [PINNED, TOOL-dQuietDisk-7 rev-6 AC7],
  and a template build about nine. A suite that copies with `cp -a` and spawns no git gains nothing from a clone.
  Unit 13 measured that only one of its three suites gained. Unit 12 built a copy without objects instead of a clone.
  Where nothing can save, name it in section 8 as a fork, with "close as WONTDO" among the options.
- **The template switch has one reader.** A suite that reads `tests.fixture-templates` calls `read_template_mode`
  from `template_cache_sh`, never a copy of the read.
- **Unit 26 builds on unit 10 as built.** Its consumes-from edge on unit 10 says "as moved onto the template cache".
  Unit 10's ruling kept that suite off the cache, so correct the edge to name unit 10's captured config.
- **Unit 15 consumes unit 14's attestation as built** (`6749bfa8d`): the receipt's `attestations` key and
  `tools/govkit/govkit.py#derive_kit_attestations`. Read them whole.
- **Unit 11 and unit 18 share `tools/govkit/selftest.py`.** Build on unit 18's arms there.
- **Check every git command, flag and shell idiom against the real tool** before the spec relies on it. This build has
  already ruled on these false facts:
  - `git rev-parse --short` takes a single revision;
  - a local `git clone --shared` spawns two processes;
  - an MSYS shell rewrites a `!/path` argument;
  - `git hash-object --stdin-paths` and an alternates line both refuse an MSYS `/c/...` path.
- **State the files**, generated outputs included, and name any other order-4 unit, 11, 15, 16 or 26, whose Files
  touched shares a path with this one. Shell-line rows grow only through
  `python tools/memory-tree/ratchet.py widen shell-role`.
- **Record the re-ground.** Set the header's base to the `HEAD` you read at, bump the rev and add a revision-log line:
  `re-grounded at <sha> (orders 1 to 3 built), <what moved>`.

Nothing in a unit's goal moves. Where the re-ground changes scope or acceptance, say why in the revision-log line.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk <your unit id>`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Mark every figure you add PINNED, DERIVED or with an id on its own line. A section number before a noun reads as a
  count, so word around it.

Return: your spec's new rev, what moved, the saving it now states, any fork you open, and the order-4 units whose
Files touched share a path with it.
