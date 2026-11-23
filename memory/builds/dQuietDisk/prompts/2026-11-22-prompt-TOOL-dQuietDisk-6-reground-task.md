**Serves:** research TOOL-dQuietDisk-6 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-18

# Spec task — dQuietDisk: re-ground order 3 on the built order 2

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. Read these first:

- the spec brief, `memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`. Its rules bind
  this task;
- the build's sibling-divergence lesson below, which cost three build passes.

## The base

Orders 1 and 2 are built and CLOSED. `HEAD` carries, beside the merge `40def53f7` of dWitnessedBar's landing:
- TOOL-dQuietDisk-2, -3 and -4, the history legs over the store;
- TOOL-dQuietDisk-5, one `git diff --name-only BASE` per bar (`c81e16bbd`);
- TOOL-dQuietDisk-7, the suite template cache (`360d706f6`, and `3ffbc03fe`): `tools/lib/template_cache.py`,
  `tools/lib/template-cache.sh`, `build_fixture --template` and `arm_reading` in `tools/lib/lib-selftest.sh`, and
  `build_target(..., template=None)` in `tools/govkit/fixture_target.py`;
- TOOL-dQuietDisk-8, the `--shared` and sparse readers (`7b8c737b0`).

Read the code each spec cites as it stands at `HEAD`. The worktree is checked out there, so read files directly.

## Re-ground each of units 6, 10, 12, 13 and 18

- **Re-check every code fact.** Re-check each cited path, line, symbol, argv and behaviour at `HEAD`. Where a fact
  moved, re-cite it by symbol or as `<path>@<blob>:<line>`, and change the design to match.
- **Units 10, 12 and 13 consume the template cache as built, not as unit 7's earlier revisions described it.** Read
  `tools/lib/template_cache.py`, `tools/lib/template-cache.sh` and the `--template` path of `tools/lib/lib-selftest.sh`
  whole. Name the functions, options and keys each unit calls, exactly as spelled there. Unit 7's rev-6 changed three
  things a consumer sees:
  - every clone the cache hands out has no remote;
  - a cached clone costs three git processes [PINNED, TOOL-dQuietDisk-7 rev-6 AC7];
  - a copy-installed suite that carries `template_cache_sh` inline must also carry the `resolve_python` block inline,
    and a file that calls `resolve_python` sources `refuse-wrong-shell.sh` and calls `refuse_wrong_shell`.
- **Prove the saving, or say there is none.** A suite moves onto the cache only where it then spends fewer git
  processes and fewer temp entries than it does today. Unit 7 found that a suite copying its fixture with `cp -a`
  spends no git and gains nothing from a clone. For each suite your unit moves, count today's per-case git cost from
  the code, and state the saving in section 1.
- **Check every git command, flag and shell idiom against the real tool** before the spec relies on it. Sibling specs
  carried three false facts this build had to rule on:
  - `git rev-parse --short` takes a single revision;
  - a local `git clone --shared` spawns two processes, `git` and `git-upload-pack`;
  - an MSYS shell rewrites a `!/path` argument such as a sparse pattern into a Windows path.
  Probe a claim of that kind in a scratch repository under the session scratch root.
- **State the files.** Each spec's Files touched names every path its pass writes, generated outputs included where
  the pass regenerates them. Name any other order-3 unit, 6, 10, 12, 13, 18 or 28, whose Files touched shares a path
  with this one.
- **Record the re-ground.** Change the header's base to `7b8c737b`, bump the rev and add a revision-log line:
  `re-grounded at 7b8c737b0 (orders 1 and 2 built), <what moved>`. Write `nothing moved` where nothing did.

Nothing in a unit's goal moves. Where the re-ground changes scope or acceptance, say why in the revision-log line.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk <your unit id>`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Mark every figure you add PINNED, DERIVED or with an id on its own line. A section number before a noun reads as a
  count, so word around it.

Return: your spec's new rev, what moved, the saving it now states, and the order-3 units whose Files touched share a
path with it.
