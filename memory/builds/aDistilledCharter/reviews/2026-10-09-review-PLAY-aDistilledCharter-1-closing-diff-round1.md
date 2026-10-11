**Serves:** diff-review TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1

# Tier-2 closing diff review — aDistilledCharter, ROUND 1

Three read-only finder lenses run as direct agents on 2026-10-09 (renderer and fleet; gates and
canary; charter content and claims), primed with the bug-class checklist `gotchas.py --for-diff`
selected over the range. The main loop then verified each finding against the code as the skeptic,
reproducing where a run was cheap. Not run through `tier2-review.js`: this session had no owner
opt-in to a `Workflow` fan-out, so three direct agents stood in, inside the cap.

**Reviewed range:** `6473ae38a517a3559f2b7daed67a9820c505bd4d...1f6e9209c` (25 commits). **ROUND: 1.**

## Verdict: BLOCKED

One BLOCKER: an adopter's next `govkit update` rolls the playbook-render kit back, because the
seeded template stays v3.5 while the new engine and descriptor refuse its retired fences and
placeholders. It is fixed in place, as a fold of `TOOL-aDistilledCharter-2`. Three HIGH findings are
each promoted to a unit, and the twenty-two MEDIUM and LOW findings are batched into one unit.

## Review shape

- Raw 26, confirmed 26, refuted 0. The lenses carried a repro for most; the main loop re-read the
  cited code for every finding and re-observed three itself (R1 through govkit's seed policy,
  `UPDATE_ROLE` reporting `reseed-available` and never writing; G1; G7). Precision 1.0, which is a
  reason to suspect the skeptic was gentle, not that the lenses were perfect.

## Findings and their disposition

| # | Sev | Where | Finding | Disposition |
|---|---|---|---|---|
| R1 | BLOCKER | `tools/playbook/render_playbook.py` | a seeded v3.5 template no longer renders under the v4.0 engine, so `update` rolls back | fixed: `TOOL-aDistilledCharter-2` rev-2 |
| R2 | HIGH | `render_playbook.py` `derive_node_table` | the node table's paths come from the rendering checkout's directory name, so two nodes render two charters | promoted: `TOOL-aDistilledCharter-5` |
| G1 | HIGH | `tools/check-playbook-parity.sh` | three bound phrases left the charter for `tools/hooks/README.md`, where no gate compares them | promoted: `TOOL-aDistilledCharter-6` |
| C1 | HIGH | `coding-governance-agents.template.md` | the security checklist and tiers ship only with `review-harness`, which no default adoption selects | promoted: `DEPL-aDistilledCharter-2` |
| R3 | MEDIUM | `render_playbook.py` | the claim keys identity on user and host, while every reader matches the user alone | batched: `TOOL-aDistilledCharter-7` |
| R4 | MEDIUM | `render_playbook.py` | a `[charter]` key naming a retired placeholder is refused | batched (R1's fix keeps the names declared) |
| G2 | MEDIUM | `check-playbook-parity.sh` | at a root install S4's surface holds no kit directory | batched |
| G3 | MEDIUM | `check-playbook-parity.test.sh` | the self-test header cites a section, hidden by the whole-file exclusion and the `.md` gap | batched |
| G4 | MEDIUM | `tools/run-gates/run-gates.gov.test.sh` | the two negative arms stopped reading `AGENTS.md` | batched |
| C2 | MEDIUM | `.governance/deploy.toml` | gov's `kits` omits `runlog` and `process-monitor`, so the evicted `/runlog` bullet has no successor | batched |
| C3 | MEDIUM | `WIRE-INTO-PROJECT.md` | "the bug classes it fixes stay in the charter either way" is false | batched |
| C4 | MEDIUM | `skills/session-kickoff/manifest-check.sh` | the retrofit recipe still pulls manifest lines into the playbook; `README.md` likewise | batched |
| C5 | MEDIUM | the template | `[gate]` and `[contract]` lost green-by-absence, the exemption rule and coupled releases; the pytest line lost structural classes | batched |
| C6 | MEDIUM | the template and runbook | a claim reaches an adopter by `govkit update`, not by re-rendering | batched |
| C7 | MEDIUM | `tools/playbook-kit-waivers.txt` | the `runlog` waiver's premise is false, and a `kit:` fence does not count as naming | batched |
| R5 | LOW | `render_playbook.py` | DEL passes the claim's control check, and the write precedes the validation | batched |
| R6 | LOW | `render_playbook.py` `read_git` | an exported `GIT_DIR` points the probes at the ambient repository | batched |
| R7 | LOW | `render_playbook.py` | a `[charter]` value may carry one-line markers and escape the grade | batched |
| R8 | LOW | `render_playbook.py` | the trailing-newline strip applies to the render and not to `--answers` | batched |
| G5 | LOW | `check-playbook-parity.sh` | S4's predicate misses curly apostrophes, non-breaking spaces and trailing forms, and hits the protocol template | batched |
| G6 | LOW | `check-playbook-parity.sh` | `GIT_LITERAL_PATHSPECS` disables the `:!` exclusions | batched |
| G7 | LOW | `.memory-tree.conf` | `ARMS_FLOORS` still pins the parity gate at `11:9` where it measures `13:11` | batched |
| G8 | LOW | `check-playbook-parity.sh` | S4's surface omits `memory/*.md` and `CLAUDE.md` | batched |
| C8 | LOW | the template | `[pair]` lost the BUILD and SPEC field rules | batched |
| C9 | LOW | `.governance/deploy.toml` | two section-2 rules overstate what `product.md` and `memory/project/` hold | batched |
| C10 | LOW | the template | `reap.py --sweep` names a flag the script does not read | batched |

## Round 2

Owed over the fold and the promoted units, from this round's recorded tip, per BUILD-METHOD M8.
