**Serves:** research TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21

# The spec fix pass — dPlacedRequest, its return

The return of the gov-spec-writer dispatched from `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-5-spec-writer.md`, run direct/aa076f91b905dbf5c, extracted from its transcript by script.

All the hits are dispositioned: 33 fixed by editing the specs and none judged false. I could not run `check-spec-tokens.py`, though: the scratch-guard hook blocks this role from running gates, so its final count is unobserved and needs the main session to run it. The hygiene gate (`check-memory-hygiene.sh --only 2,12,25`) is clean.

The 15 edited specs are all under `C:\projects\coding-governance\.claude\worktrees\unattended-dplacedrequest-f41432\memory\builds\dPlacedRequest\spec\`. Each is bumped to rev-2 with a §9 line naming what changed. Nothing is staged, committed or re-rendered, and no `**Carries:**` line was touched, so coverage is unaffected.

**[guards]** — every hit fixed by adding the named leg to §7's leg line. I checked each leg name against `tools/gate-legs.json`.
- TOOL-dPlacedRequest-12, -15, -18, -19, -20: added `recall floor` and `recall floor arms`.
- TOOL-dPlacedRequest-21: added `tier2-review self-test`, `run-gates canary`, `run-gates gov canary` and `measure-legs selftest`.
- TOOL-dPlacedRequest-4: added `run-gates canary`, `run-gates gov canary` and `measure-legs selftest`.

**[path]** — all fixed.
- TOOL-dPlacedRequest-1 AC6: the two illustrative scripts are now described in prose as the fixture's own scratch kit directory, not as tracked paths.
- TOOL-dPlacedRequest-2 AC1: the fixture is cited by its basename, `bash card-store.fixture.sh --plant render`.
- TOOL-dPlacedRequest-7 AC10: now `git grep -n "probe.raise" -- probe.py`, run in the loop kit's directory.
- TOOL-dPlacedRequest-8 AC4: the plant's three paths are described in prose as its own temp paths.

Basenames are safe because this repo's tool root is `tools`, so the checker's bare-name arm (`tools/check-spec-tokens.py:1455`) is off.

**[handoff]** — all fixed.
- TOOL-dPlacedRequest-19 to -7, -4 and -21: these units take the key as a `--request <content key>` argument and never call `derive_request_content_key`. So I corrected 19's bullets to name that argument, which each of them already spells.
- TOOL-dPlacedRequest-19 to -14: unit 14 really does compute the key from text (`--request-text`). So 14's S1 and its consumes-from bullet now name `derive_request_content_key`. The key's spelling stays `request_content_key` across units 4, 7, 14, 19 and 21.
- TOOL-dPlacedRequest-2 to -3: unit 3 does not call `--card --lookup`; it resolves the card through `manifest-check.sh --card --path` (its line 126). I corrected 2's bullet to name that reader.

**Check 12, one-sided edges** — all fixed by adding the missing reverse bullet in the producer's §3. Every edge runs from an earlier order to a later one.
- TOOL-dPlacedRequest-11 (order 1) now hands off to -14 (order 18): `write_gov_ref`, `build_gov_commit`.
- TOOL-dPlacedRequest-13 (order 2) now hands off to -15 (order 9): `gov-feed.log`, `gov_feed_sh`, `add_feed_event`.
- TOOL-dPlacedRequest-13 (order 2) now hands off to -2 (order 12): `gov-feed.log`, `gov_feed_sh`, `gov_ref_sh`.
- TOOL-dPlacedRequest-1 (order 3) now hands off to -4 (order 16): `refs/gov/leases/<slug>/build`, read by `placement.check` for `continue` and `amend`.

**Check 12, conformance** — both fixed.
- TOOL-dPlacedRequest-13 S1: the "placeholder" was the `YYYY-MM-DD` time-format note, not a skeleton gap. It now reads as an example, `2026-10-25T14:03:07Z`.
- TOOL-dPlacedRequest-15 AC3: now names its witnesses, `check_fence_beat` refusing with exit 1 and `git ls-remote` showing both refs unchanged.

**Check 25** — only one item actually retires something; the rest were reworded.
- TOOL-dPlacedRequest-11 S7 does retire the two lock events, so it gained a `**Readers:**` clause. By name: `tools/unattended/README.md`, `unattended.sh` and `unattended.test.sh`, found by `git grep`. By value: `NO VALUE READERS`, with its reason.
- These items retire nothing named, so I reworded them instead of adding a `**Readers:**` clause, as the spec brief allows:
  - TOOL-dPlacedRequest-11 S1: the ref delete is now worded as "pushes the ref's deletion".
  - TOOL-dPlacedRequest-11 S5: now "leaves `pre-push-refusal` in place".
  - TOOL-dPlacedRequest-13 S1 and S3: now say "deletion" for the delete case.
  - TOOL-dPlacedRequest-16 S7: says "prunes" for runtime refs instead of "deletes".

**Final counts**
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`: 0 failures. The only output is `HYGIENE --only 2,12,25 ran checks 2 12 25` plus the existing "did not grade" notes on other builds.
- `python tools/check-spec-tokens.py`: not run, because the hook refused it for this role. I reread the checker's path, guard and handoff logic and expect 0 of the 30 listed hits to remain. The main loop needs to run it, along with `carries.py --report dPlacedRequest`.
