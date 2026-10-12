# Spec brief — TOOL-aBriskPreflight-2: check-wiring reads the settings file and each fragment once, and resolves python once

**Serves:** research TOOL-aBriskPreflight-2

Read first: the build README, the prompt record and the baseline record
(`build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md`), and unit 1's spec, which is built
before this one in the same file.

## The mechanism, one

In `tools/check-wiring.sh`, the same input is re-read and the same interpreter re-started once per
QUESTION; each becomes one read per RUN, answered from memory after that. Three readers:

1. `json_str` (one `sed | head` per key per fragment, 16 s at BASE) and its callers in
   `resolve_fragment_hook`, `check_scratch_guard`, `check_recall_opened` and `check_card`: each
   fragment is read once, its four keys (`marker`, `matcher`, `event`, `hook_path`) taken in that one
   read. The owner's words are "each fragment's JSON parsed once, by one interpreter call"; a read
   with no process at all (bash's own `read` and `[[ =~ ]]`) satisfies that and costs less, and the
   spec may pick either, with the pick and its reason in §8. The value must be the one the current
   `sed` yields: the LAST `"key": "value"` on the FIRST line that carries one (`.*` is greedy).
2. `matchers_of` (a seven-stage `tr | sed | grep | sed | sed | grep | grep | sed` pipeline over the
   whole settings file on every `wired` call, 37 s at BASE): the file is flattened and split into
   event chunks once per run, and each call filters what was kept. The filters stay what they are —
   the event chunk test is a SUBSTRING test for `@<event>@` (or `@` with no event), the group is cut
   at its first `]`, the marker and basename are fixed-string tests, the matcher is the value of a
   group line that opens `{"matcher":"`. `settings_json`'s cache never survives today because every
   caller reads it through `$(…)`; the spec says how the resolved path and its refusal reach the arms
   once.
3. `resolve_python`, re-RUN on every call (`python3 -c 'import sys'`, 17 python starts at BASE), and
   `resolve_kit_file`, which calls it and then starts python again through `resolve_kit_dir` with a
   `$(cat <<'RKD' …)` heredoc: python is resolved once per run (`PY` is already resolved at the top
   and the straggler arm tests `command -v resolve_python`), and the kit files the arms locate are
   resolved through one interpreter start, not one per file. The no-python rung (the bash probe of
   the same two places, with its `note resolver` line) must still run when no launcher resolves.

## What may not move

- Every printed line byte for byte on the same tree, every verdict and the exit status.
- `resolve_python` and `resolve_kit_dir` are INLINE COPIES gated byte-identical against canonical
  copies (`>>> resolve_python — canonical copy …` markers; the resolve-python self-test's parity
  table). Their bodies between the markers do not change. Memoize AROUND them.
- `--resolve-fragment` prints the same bytes as `settings-merge.py` (the hook-destinations gate).
- The SessionStart contract: this script runs as a hook on a host that may have NO python, so no
  reader may come to need one.

## Out of scope

- `$(first_of …)` and `$(resolve_receipt_path …)`: aSparedSpawn-8 S3. Do not convert them.
- Unit 1's three loops.

## Acceptance shape

- Equivalence: every arm's printed lines before and after on one tree, byte for byte, and
  `--resolve-fragment` on every shipped fragment.
- Spawn count with the build's `trace-spawns` instrument, before and after.
- RED on a staged break, GREEN restored, through SLICED arms of `tools/check-wiring.test.sh`: a
  fragment missing `matcher` still prints its `declares no marker/matcher` UNWIRED; a group wired
  under the wrong matcher still names the matcher found; a card replay wired under `resume` alone
  still reds; a `GOV_PYTHON` that does not run still takes the no-python rung.
- Witnesses in §6 by basename.

## Conventions this repo grades

- Lexicon verbs for any new function (`--suggest … --as sh.function`); `gen_map.py --write` after a
  new or renamed function; the kit version bumped once, after the kit's last move in this build.
- Tier-1 unless the spec finds a contract it changes.
- Order: 2, after unit 1 (same file).
