# Acceptance ledger — TOOL-aCarriedStop-9

**Serves:** journal TOOL-aCarriedStop-9

Built against spec rev-1 in one pass commit, on node a. The evidence row was written by the spec's write in a scratch clone detached at `4cb4b39fa`, where `--report` first printed DEAD PROBE, and the write's summary read `wrote 131 row(s)` with `0 raised`, `1 raised by --observed` and `0 held at a previous maximum`. The file was copied back. AC2 to AC4 are the criteria's own commands over the worktree with S1 to S3 staged. No suite, gate leg or bar ran in the pass. Owed to the main loop at the close: AC1 green at the pass commit and its red against the parent's manifest, and the legs of the spec's Gates section, among them the close's bar finishing `routed commits name a specced unit`, which is the Goal's observation.

**Evidences:** TOOL-aCarriedStop-9
- AC1 — `python tools/run-gates/derive-ceilings.py --check` — not run in the pass: the `leg ceilings clear their evidenced maximum` leg runs this argv and the role gate refuses it to the builder. The green reading at the pass commit and the red reading with `GATE_LEGS` at the parent's manifest are owed to the main loop at the close.
- AC2 — `grep -n '^routed commits name a specced unit' tools/run-gates/ceiling-evidence.txt` — it printed line 119 with six tab-separated fields: the leg's name, `1761.4`, `1`, `a`, `2026-11-14`, and a sixth field byte-equal to the `--how` text of the spec's write line.
- AC3 — `git diff --cached --numstat -- tools/gate-legs.json tools/run-gates/ceiling-evidence.txt` — it printed `1 1` for each file; the `-U0` diff of `tools/gate-legs.json` printed one hunk `@@ -1158 +1158 @@` whose added line is `"ceiling": 3540`, and `python -m json.tool tools/gate-legs.json` exited 0.
- AC4 — `bash skills/session-kickoff/manifest-check.sh --staged` — with S1 to S3 staged it exited 0 and printed no `MANIFEST check 5 FAILED` line. Its red was seen first in the pass: with the manifest unstaged it printed `MANIFEST check 5 FAILED — staged changes touch watched files:` naming `tools/gate-legs.json`, and exited 1.
