# Acceptance ledger — TOOL-aNimbleMend-6

**Serves:** journal TOOL-aNimbleMend-6

Built against spec rev-2 in one pass commit, from the tip `8079fde2d`, which is the `PRE` of AC5. Each line is a probe the builder made in the pass: one PreToolUse payload piped to a hook on stdin with this worktree as its `cwd`, while the run record on this branch read BUILDING. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section, and the RED-first observation of its two new arms, the rows `N-AC1` and `N-AC2` of `tools/hooks/scratch-guard.test.sh` and the rows `N-AC3` and `N-AC4` of `tools/unattended/gate-guard.test.sh`; neither suite was executed here, so both raised floors are static counts the close confirms.

**Evidences:** TOOL-aNimbleMend-6
- AC1 — `G2 runner` — the hook exited 2 and its stderr named the row for the plain command, behind `env`, behind `timeout 600`, and as a PowerShell payload, each with `agent_type` `gov-builder`.
- AC2 — `agent_type` — with the key deleted the same payload exited 0 with empty stdout and stderr, so no line opened `BLOCKED`.
- AC3 — `node tools/unattended/gate-guard.js` — the plain adapter command exited 0 and printed nothing.
- AC4 — `flag:` — with a non-empty full-bar flag in front the hook exited 2, named the record at BUILDING and printed the flag token on its `flag:` line, so the fixture was keyed and AC3 did not pass by failing open.
- AC5 — `PRE` — with `PRE` = `8079fde2d` the criterion's pipeline printed nothing: every moved line of the gate guard is a header comment line.
- AC6 — `grep -c 'pass-legs' tools/hooks/README.md` — printed 1, and the grep of the hook printed three lines: the header comment, the comment on the array, and the array. (PINNED, 2026-11-12)
