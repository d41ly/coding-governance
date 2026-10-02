**Serves:** journal TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-46

# aRepatriatedFork: the round-1 closing diff review, folded

*Node `a`, 2026-09-30. The fold of `reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md`
(verdict BLOCKED), over round 1's recorded tip `7de665e5`. Each finding was reproduced RED on
`7de665e5`'s bytes before any code moved for it. None was refuted. Each fix went in as a spec
rev bump on its owning unit, committed as records before the code commit that names the unit.
Owners were found with `git log -S` on the regressed line, not assumed.*

The round is BLOCKED, not an exit, so BUILD-METHOD M4's disposition by severity does not apply
yet. M8 does: every finding is fixed in place and round 2 reviews the fix diff from `7de665e5`.
No suite ran whole. Each arm ran as a slice (the suite's prologue plus the blocks changed) in a
temporary file beside the suite, removed after. The old-bytes observation staged the pre-fold file
from `HEAD` into the tree, or spliced the fix out of a copy, and restored it after.

## Per finding

| Item | Red first | Fix | Owner | Regression arm |
|---|---|---|---|---|
| B1 | The real hook, end to end: an ignored receipt naming `.git/x/run-gates/run-gates.sh` beside a planted manifest printed `PLANTED BAR RAN` and landed over a tracked RED runner; the same receipt tracked landed too | `check_reviewed_file` in `.githooks/pre-push`, one predicate for `gate-env.sh`, the receipt and the default bar's runner | TOOL-aRepatriatedFork-24 (`baa7289a`, S2c) | Three refusal arms in `.githooks/pre-push.test.sh`, each red on the old hook, plus a control |
| H1 | `check-verifier-fanout.sh --print-cap` and `check-review-join.sh` from a scratch checkout threw MODULE_NOT_FOUND | Join the kit dir to `git -C "$HERE" rev-parse --show-toplevel` | TOOL-aRepatriatedFork-46 (`a25c87e7`, S7a) | The verifier suite's two held arms, red in a slice at `7de665e5`; a new review-join arm run from a checkout with no hooks kit |
| H2 | A canary slice over arm 1b reported 114 guards matching no tracked path | Arm 1b resolves each guard through the inlined `resolve_prefix_token` block | TOOL-aRepatriatedFork-29 (`f6f41cc3`, S8a) | Arm 1b itself; a planted untracked `{prefix}` guard reds it by name |
| M1 | `derive_gate_runner` rendered `''` for a `prefix = "scripts"` target holding a flat `scripts/gate.sh` | Read the top-level `prefix` from the target's `deploy.toml` | TOOL-aRepatriatedFork-29 (`f6f41cc3`, S8c) | A render selftest arm over three flat runners; fails with the read spliced out |
| M2 | 113 of arm 2's 124 needles carried the raw token, so a runner inlining a leg could not red it | Arm 2 resolves each needle first | TOOL-aRepatriatedFork-29 (`f6f41cc3`, S8b) | A liveness assertion that every needle names a tracked path, red on the old reader; a runner copy carrying a resolved leg path reds arm 2 |
| M3 | Selfcheck printed 28 `reported, not repaired` notes | 5b resolves `resolve_carrier_kit` variables through the canonical resolver inlined into `govkit.py`, then the gate's aliases | TOOL-aRepatriatedFork-46 (`d2df966d`, S7b) | An unresolved carrier FAILs; with the resolution spliced out, 13 FAIL by name. Notes fall to 10 |
| M4 | A lone `scripts/settings-merge.py --selftest` raised AttributeError on `.name` | One miss-name constant, read by arm 12 when no hooks kit resolves | TOOL-aRepatriatedFork-46 (`d2df966d`, S7c) | Arm 18 re-runs the selftest from a copy alone; spliced onto the old arm 12 it fails |
| M5 | `govkit apply` into a `scripts` intake with a hand-copied `tools/check-wiring.sh` exited 0 and installed | The probe takes the union of the target's ctx, `canonical_ctx` and the root | TOOL-aRepatriatedFork-24 (S7a's rev-3 code, S7b) | A govkit selftest arm; the same apply now exits 2 before any write |
| M6 | With every python launcher stubbed, check-wiring printed `skip agent-cap — not adopted` over a present hook | `resolve_kit_file` probes the resolver's two places in bash | TOOL-aRepatriatedFork-46 (`d2df966d`, S7d) | A check-wiring suite arm, red with the old checker staged in |
| L1 | `git grep` found each named carrier; the dead-path gate run over `memory/map/features/` found six more dossier lines | The carriers rewritten, and the gate reads the map dossiers | TOOL-aRepatriatedFork-30 (`289a9cae`, S9) | A dead-path suite arm with a dossier naming a deleted file, red against the old gate |
| L2 | `resolve_kit_homes('HEAD')` returned 0 homes against 27 at the base | Resolve each tokened descriptor, join kit-relative homes unless `home_root_relative`, refuse an empty read | TOOL-aRepatriatedFork-29 (`f6f41cc3`, S8d) | A govkit selftest arm, 0 homes on the old reader; it caught the kickoff home the first cut mis-joined |

## Beside the findings

- **Two hygiene reds already standing at `7de665e5`**, cleared first in `7e4e67c6`. Check 21 read the
  review record's own binding line naming the pass-order backlog row this build filed, which no
  spec defines.
  Check 15 read two backlog rows citing the deleted install-prefix files, the L1 class.
- **The structural gate the cross-cutting note asked for was not built**, because no sound
  predicate exists. The survey and the reasoning are in `memory/gotchas/a-spelling-change-strands-its-readers.md`,
  committed as a class record with a documented check, and `TOOL-aRepatriatedFork-47` takes no rev.
- **A version decision was wrong and corrected.** `0a79f19b` recorded that no bump was owed, reading
  `govkit epoch` before the commit existed. After it, three kits read `last bump precedes last move`,
  and `1daf68d8` bumps them. The fold moved check-wiring 1.19, settings-merge 1.15, review-harness
  1.22, run-gates 1.18, playbook-render 1.18 and memory-tree 2.111.
- **Not done here:** the review's push-main hardening (withhold the lander marker on an empty bar
  blob) and its `.git/` path filter in the awk rung. The hook now refuses both shapes before it
  writes the bar record push-main reads, so neither is reachable; both are left to round 2's
  judgement. The planted `gate-fingerprint.sh` beside a tracked runner is main's behaviour too.

**Evidences:** TOOL-aRepatriatedFork-24
- AC11 — `.githooks/pre-push.test.sh` (sliced: prologue plus the B1 block) — the ignored `.governance/install.json`, the tracked receipt naming a runner under `.git/`, and the modified receipt each refused as `bar-refused` with no `PLANTED BAR RAN`; the clean tracked receipt reached `TRACKED BAR RAN - RED` and was refused as `gate-red`. On the `7de665e5` hook the first two landed at rc 0 and the third was refused only as `dirty-tree`
- AC12 — `foreign_kit_present` through `govkit apply` — a `prefix = "scripts"` target with a foreign kit at gov's canonical prefix exits 2 naming `check-wiring (at tools/check-wiring.sh)` and writes no receipt; the `7de665e5` probe exited 0 and installed. The `tools/govkit/selftest.py` arm pins it

**Evidences:** TOOL-aRepatriatedFork-29
- AC9 — `tools/run-gates/run-gates.test.sh` (sliced: prologue plus arms 1b and 2) — green on the real manifest; with `GATE_LEGS` naming a copy carrying a `{prefix}/no-such-kit/` guard it fails naming that guard. At `7de665e5` the same slice reported 114 bad guards
- AC10 — `run-gates.sh` copy with `tools/check-microformats.sh` planted — arm 2 fails naming it; with the resolution spliced out its new assertion fails naming the raw `{prefix}/…` needles
- AC11 — `render_playbook.py --selftest` — 23 arms OK, the new one rendering `bash scripts/gate.sh`, `bash scripts/run-gates.sh` and `bash tools/run-gates.sh`; with the deploy read spliced out all three rendered `''` and the arm failed
- AC12 — `tools/govkit/selftest.py` arm, replayed standalone over both readers — `resolve_kit_homes` yields 27 homes for 27 entries, each tracked; the `7de665e5` reader yields 0

**Evidences:** TOOL-aRepatriatedFork-30
- AC10 — `bash tools/check-dead-paths.sh` — `clean — 34 derived needle(s), 14 declared waiver(s)` with the map dossiers in the haystack, after naming six dossier lines on its first run; `tools/check-dead-paths.test.sh` (sliced: arms 1 to 3c) passes 8, and with the `7de665e5` gate staged in the `memory/map/features/` arm fails reading `clean`

**Evidences:** TOOL-aRepatriatedFork-46
- AC10 — `tools/workflows/check-verifier-fanout.sh --print-cap` from a fresh `git init` checkout prints 5; `tools/workflows/check-review-join.test.sh` (sliced) passes its new arm reading `review-join: clean`, which fails with the `7de665e5` gate staged in
- AC11 — `python tools/govkit/govkit.py selfcheck` — exits 0 with 10 `reported, not repaired` notes, none naming a `${MT_DIR}`-style carrier; with the carrier resolution spliced out, 13 carriers FAIL by name
- AC12 — `python tools/settings-merge.py --selftest` — PASS in gov and as a lone copy under `scripts/`; arm 18 spliced onto the `7de665e5` arm 12 fails on `.name`
- AC13 — `tools/check-wiring.test.sh` (sliced: prologue plus the M6 arm) — reads `UNWIRED  agent-cap` with every launcher stubbed; with the `7de665e5` checker staged in it printed `not adopted` and failed
