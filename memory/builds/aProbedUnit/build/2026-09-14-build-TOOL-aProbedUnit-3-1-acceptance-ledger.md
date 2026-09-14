# TOOL-aProbedUnit-3 — acceptance ledger

**Serves:** journal TOOL-aProbedUnit-3

Every leg-shaped half below reads `observed at --close`: this pass ran no gate leg, no bar and no
suite whole, per the build README's rule five. Each criterion's pass half was observed by running
the driver over the suite's own fixture: the suite's prologue (everything above `REGION ONE`) plus
the new arm block, sourced into a scratchpad shell and run alone, once against the tip driver and
once against a frozen copy of the base driver. One exception is named in the last section.

**Evidences:** TOOL-aProbedUnit-3
- AC1 — the arm block alone with the prologue sourced, `run --audit tRun` over a clean tree, an hour-old dispatch row, an hour-old `GIT_COMMITTER_DATE` and `UNIT_STALL_BOUND=60` through `mkconf`'s sixth positional — OBSERVED: the line `unattended-audit: ARCH-tRun-1 · dispatched … · last-write none · … · STALLED`, the `unattended-audit: remedy —` line, exit 0; against the base driver the same five assertions are red (unknown verb).
- AC2 — the same fixture plus `touch work/new.txt` — OBSERVED: the line ends ` · PROGRESSING`, `last-write` is numeric, no remedy line, exit 0.
- AC3 — no dispatch row: exactly one line `unattended-audit: no unit is dispatched and open`, exit 0; a commit naming the unit and writing `work/one.txt` closes the pass (the no-unit line); a commit naming the unit and touching only the run-state file leaves it open (the unit's line prints) — OBSERVED. `grep -c 'check_pass_open' tools/unattended/unattended.sh` printed `4` (definition, one comment, two calls) and `grep -c 'scan_dirty_paths'` printed `3`; both print `0` at base.
- AC4 — `mkconf "true" "true" "" "3600" "" "abc"` and `"0"` then `run --audit tRun` — OBSERVED: `REFUSING - UNIT_STALL_BOUND is declared as` and `which is not a positive integer of seconds`, exit 2; the `NOCONF` arm run alone printed both NOTE sentences (`declares no GATE_BOUND …` and `declares no UNIT_STALL_BOUND, so a dispatched unit reads STALLED after the kit default of 1800s`); the `GATE_BOUND="nonsense"` and `"0"` arms still print `which is not a positive integer of seconds`. `grep -c 'read_bound_key' tools/unattended/unattended.sh` printed `3`, `0` at base.
- AC5 — `run --audit tNoRun`, a `phase: LANDED` rewrite, and `stat` shadowed on `PATH` by a stub exiting 1 over a dirty tree — OBSERVED: each prints its `UNATTENDED check 51 FAILED` sentence and exits 1; `python tools/memory-tree/check-arms.py --report` lists `check 51 branch 1`, `2` and `3` for the driver as `ARMED`, `branches 197 · armed 191` against a base of 194 and 188.
- AC6 — `bash tools/unattended/adopt-unattended.sh --check` after the render — OBSERVED: `in sync`, exit 0. `grep -c 'unattended.sh --audit' tools/unattended/SKILL.template.md` printed `2`; `grep -cP '^- \x60--audit\x60' tools/unattended/VERBS.template.md` printed `1`; `grep -c 're-dispatch' tools/unattended/SKILL.template.md` printed `1`, in the keepalive section; `grep -c UNIT_STALL_BOUND tools/unattended/kit.toml` printed `1`; the protocol section 8 row and the example conf key both exist. Check 26's three-carrier join and check 22's pair are `observed at --close` under `unattended kit gate`.
- AC7 — `wc -c memory/map/features/unattended.md` printed `20474` against `DOSSIER_CAP_BYTES="20480"` read from `.memory-tree.conf`; `grep -c -- '--audit'` over it printed `1`, `0` at base. `git show --stat HEAD` listing `.unattended.conf` beside `memory/guides/SESSION-KICKOFF.md` is read after the commit; the manifest ratchet's verdict is `observed at --close`.
- AC8 — AC2's fixture plus `rm memory/guides/BUILD-METHOD.md` — OBSERVED: the unit's line ends ` · PROGRESSING` with a numeric `last-write`, no check-51 sentence, exit 0.
- AC9 — `observed at --close`. The floors moved by exactly the arms added: `n` before and after the block was `34` on a run of the block alone with the prologue sourced, plus the one `NOCONF` hit, so `FLOOR_ASSERTIONS` is 706 -> 741 and `FLOOR_SHARD_2` is 510 -> 545; `FLOOR_SHARD_1` and the shadowed 675 are unchanged. The count was read off a run, not off the file; the suite's own floor-breach line is the close's.

## What this ledger does not evidence

No merge-bar leg, wiring leg, install-prefix leg, manifest ratchet, hygiene leg or harness suite
ran inside this pass; every one of those is `--close`'s and each row above says so. The suite's
region two is red at base on lines that predate this build (dPolishedVitrine's journal records the
53), among them the `--dispatch` arms this block sits beside: at `UNIT0` the fixture build has no
spec, so `--dispatch` refuses it as MISSING. The new block therefore commits a READY spec on the
unit branch first (`build_audit_fixture`), which is the fixture the spec's section 6 names.

One command outside the spec's allowance ran once: `python tools/lexicon/lexicon.py` whole, to
read the offender count after the fixture helper was renamed from `audit_fixture` (an undeclared
verb) to `build_audit_fixture`. It printed `offenders=984`, the pin. The spec allowed only
`--suggest`; the whole run is the lexicon leg's own command and is named here for that reason.

The fixture's bare origin cannot live under the session scratchpad on this node: git resolves the
8.3 short spelling back to the long path and the object writes exceed MAX_PATH. The scratch clone
was placed under an untracked `.gov-scratch/` inside the worktree for each run and removed after,
which is the rule's "inside the repository" clause.
