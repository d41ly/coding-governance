# Acceptance ledger — TOOL-dFairHearing-30

**Serves:** journal TOOL-dFairHearing-30

Built against spec rev-6 in two passes: pass (a) at `0d11473c8`, and pass (b) at `db0f99c71`, whose
first parent is the orchestrating commit `3cf918a65`. The main loop drafted this ledger at the close
from the builder returns of `0d11473c8`, of pass (b)'s first dispatch and of `db0f99c71`, and from the
verdict record `2026-11-04-build-TOOL-dFairHearing-30-replay-verdict.md`. No suite, gate or bar ran in
either pass. The spec's Gates section declares no new arm, and its legs are owed to the close.

Unit 35's S6 entry stands in that verdict record, under "Superseded here" in its `## Scoring` section:
the unit's S4, the figure and decision half of its S5 and AC3, and AC4's `ungated` half.

**Evidences:** TOOL-dFairHearing-30
- AC1 — `f<r><a><n>` — the record's attempts table lists nine attempts under nine distinct clones, f1s1, f1u1, f2s1, f2s2, f2u1, f3s1, f3u1, f4s1 and f4u1, all `completed`, so no `refused` attempt owes a reason and no `failed` attempt exists. Its "Each clone" section gives each clone an empty status before its call and one `??` path after, its own report. Pass (b)'s probe `f30-b2-attempts.py` found each `HEAD` equal to its record's range head, `6f5f4ddec`, `033b15f24`, `0a6eff73e` and `f8ad789e1`, and each post-run status listing exactly one path
- AC2 — `dirty:` — pass (a)'s `f30-probe.sh`, its block composed from the README's two fences, exited 2 printing `dirty: …/fdirty` over a clone under `%TEMP%/fdirty` holding one planted file, and a second run into `fpa` exited 2 printing `replay: …/fpa exists` before any fetch. Over the record, f2s1's void row is followed by attempt 2's row and the attempt numbers rise. No void cell cites an outside read, so that half has an empty population and is not counted as coverage
- AC3 — `replay_scorer.py --experiment` — over the committed manifest it printed `arm ungated: varies checklist from selected`, `parsed selected: 4 of 4` and `parsed ungated: 4 of 4`, and a red copy naming f2s1 printed `3 of 4`. The recall, pairing, pooled figures, decision and class set are superseded here by unit 35, whose AC3 observes them in the record's `## Scoring` section
- AC4 — `git diff HEAD~1 HEAD` — over `tools/memory-tree/gotchas.py`, `tools/workflows/tier2-review.template.js` and `tools/workflows/tier2-review.js` it printed nothing at `db0f99c71`. Pass (a)'s `0d11473c8` writes only `tools/workflows/README.md` and `memory/LIVE.md`. The behavioural check of a `selected` decision is unit 32's
- AC5 — `cygpath -m` — on pass (a)'s staged blob the greps printed `cygpath -m` at lines 1111 and 1124, `status failed` at 1114 and `orchestrating head unreadable` at 1116, all inside the replay section, lines 1033 to 1132, whose fenced bash lines hold the trap opener once. `f30-probe.sh` passed all 10 checks: an empty `SCRATCH`, an empty `ORCH`, and `TEMP` and `TMPDIR` both empty each exited 2 with the variable's message and left no clone directory; an `ORCH` that is no repository exited 2 printing `orchestrating head unreadable` with no log line; a 7-byte `.git/index` made `git status` exit 128 and the block exit 2 printing `status failed:`; and a clean clone wrote exactly 1 `orchestrating` line whose sha equals `ORCH`'s `HEAD`. A README whose two reads drop their `||` checks failed 2 of the checks
- AC6 — `orchestrating` — the record quotes `run.log`'s nine lines, all naming `3cf918a65`, and names that sha on a line of its own. The record's adding commit has first parent `3cf918a65`, `7ff570cfa` is its ancestor, the three named blobs equal `HEAD:<path>`, and the nine `HEAD` lines each stand on a line of their own
- AC7 — `test -e` — pass (b)'s probe `f30-b2-ac7.py` found all 60 paths the record names: clones, reports, result files, run folders and 24 cited transcripts. A red copy reported 1 missing. No clone was removed
