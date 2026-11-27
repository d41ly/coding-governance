**Serves:** journal TOOL-dTotalRecall-24
**Caused-by:** TOOL-dTotalRecall-24

# TOOL-dTotalRecall-24 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `55f322f29` from [2026-11-22-prompt-TOOL-dTotalRecall-24-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-24-build-brief.md), recorded whole; the pass commits are `5d632d67d` and `be084a5f5`.

## Why

TOOL-dTotalRecall-24 is built from its spec at rev-2 and committed. The pass commit is 5d632d67d, with the `Pass: TOOL-dTotalRecall-24` trailer, and it sets the spec header to CLOSED · 2026-11-23. A follow-up commit, be084a5f5 (`Pass: none`), adds suite arms for two refusal branches that the bug-class checklist flagged. The spec could be built as written. Where the code goes past it, a deviation record covers the gap rather than a divergence: memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-24-deviation-1008.md.

## Summary

**Built (commit 5d632d67d)**
- `tools/lib/gov-feed.sh`, the canonical block:
  - The lock / count / append subshell moved out of `add_feed_event` into `write_feed_lines`. The trap and take lines are byte-identical, and so are the `exit 0 ) || rc=$?` line and the counter line.
  - The append-once read became the builder `derive_feed_row`. Its awk text is unchanged, so the existing staged copies still apply.
  - New functions: `add_record_events`, `derive_record_events` (one `git log --reverse --topo-order --no-merges --no-renames --raw --no-abbrev` over `<from>..<tip>` under MEMORY_ROOT, one event per distinct key), `derive_record_rows` (walks from the feed's newest `record` commit) and `read_record_root` (default `memory`; refuses a byte outside `A-Za-z0-9_./-`, a leading `/`, or a `..` segment).
  - `check_feed` gained a record arm that compares as sets and prints `missing`, `extra` and `unread`.
  - The census gained a landing arm over `FEED_LANDING_PUSH_FNS="write_effect_push"`. Its output lines end ` landing`, it grades the list in both directions, and it reports when it finds no landing line at all.
  - The `NODE_LOCK_BOUND` comment now records the first walk's hold, re-measured on this node: 4.01 s for 69,097 events (PINNED).
- The block is copied byte-identical into `tools/push-main.sh`, `tools/unattended/unattended.sh`, `tools/run-gates/post-merge.sh` and `tools/memory-tree/gov-claim.sh`; a diff reads each identical to the canonical.
- Both lander success branches now call `add_record_events "refs/heads/$def" "$pushed"` first.
- `--feed rebuild` now appends the tracking ref's record events, or exits 2 with `feed: no record events were rebuilt: <why>`.
- Three suites gained arms:
  - `tools/lib/resolve-python.test.sh`: the carrier-alone record call, the MEMORY_ROOT plant, and four census landing arms.
  - `tools/unattended/unattended.test.sh`: a record block covering AC1–5, AC8–10 and two staged reds. I also changed the keyless mutation to `s/^    return 0$/    :/`.
  - `tools/push-main.test.sh`: RE AC7, one row per landing path; `FLOOR_ASSERTIONS` goes from 103 to 105.
- Docs: `help/loop.md` (the `--feed` usage anchor is unchanged), plus the VERBS and STOPS templates and their two guide copies.
- Also in the commit: `symbols.json` re-rendered, the README staged with only this unit's rows, the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-24-1-acceptance-ledger.md`, and deviation 1008.

**Outside the spec (all in deviation 1008)**
- The two builders are named; the spec's inventory lists neither.
- `write_feed_lines` was added to `FEED_WRITER_HELPER_FNS`. Without it the census flags `add_feed_event`, whose body no longer writes to the log itself.
- `check_feed` prints `unread <ref> walk <tip>` when git refuses the walk.
- The walk also passes `--root`, `--no-color` and `-c core.quotePath=false`.
- No kit version moves on the branch: `govkit.py#cmd_epoch` says the lander mints the bump at the push boundary.
- `lexicon.py --measure` leaves `VERB_OFFENDER_PIN` at 1435.

**Checks that ran (each a probe, not a gate)**
- Every probe sourced the code in fixtures under `%TEMP%`.
- AC1, AC3, AC4, AC8 and AC10: fixture probe of `add_record_events` and `check_feed`.
- AC2: a two-clone fetch landing, with the feed reading C1 C2 C3 in order.
- AC5: 2,000 fast-import commits; the wrappers saw one lock take and no `add_feed_event` call, and seq ran unbroken to 2000.
- AC6: the census over the real population and planted files. These stand in for the `python resolver` leg.
- AC9: the real `unattended.sh --feed rebuild` and `--feed check` in a clone, standing in for the `unattended kit gate`.
- AC11: all five block copies run under `env -i` and `set -u`, plus the MEMORY_ROOT plant.
- A sed probe confirmed every existing staged mutation of the unattended suite still changes the new cut.
- The record door (`gov_record.py new research`) writes into the seeded fixture.

**Owed at the close**
- The three `New arm:` lines, each seen RED on its staged break:
  - resolve-python (AC6, AC11): a planted default-branch push with no `add_record_events` call, and a record path reading an unset name.
  - unattended (AC1–5, AC8–10): a landed hand commit whose event is absent.
  - push-main (AC7): one success branch's call deleted. AC7 was not observed in this pass at all.
- All eleven legs in the spec's section 7.
- My suite edits were never run, only checked with `bash -n` and probes.

**Known dependency, not fixed:** the census limb-2 hit at `tools/push-main.sh#check_landing_verdict` (TOOL-dWitnessedBar-6) still prints, as the spec states.

**Bug-class checklist**
- Run over both commits.
- `refusal-branch-with-no-arm` produced be084a5f5: suite arms for the walk-refused and tip-refused NOTEs.
- `check_feed`'s unread-walk branch still has no arm. It cannot be staged without corrupting the object store; this is recorded as a `Decided:` trailer.
- `a-helper-extraction-blinds-a-per-function-rule` is covered by the helper-list entry and the kept trap, take and close lines.

**For the main loop**
- Closing this unit makes TOOL-dTotalRecall-30 (deferred until -24) read OPEN in the derived backlog. The spec names no `closes`, so its disposal is left to you.
- The spec writer's working-tree edits to specs 52 and 62, and their README rows, are left unstaged.
- No probe or command was skipped for timeout.
