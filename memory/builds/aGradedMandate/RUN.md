# aGradedMandate - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 54309e9c565d30b695ba353adfb8503a3a98dfee
phase: FOLDING
branch-sha: 54309e9c565d30b695ba353adfb8503a3a98dfee
branch-ref: refs/heads/branch/unattended-kit-adversarial-review-6810dc
mode: prompt
anchor-kind: run-branch
keepalive: 61c79592
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 396cd9db154f1621db5cb4cde72b93470b2f690c
anchor-ref: refs/heads/main
base: 54309e9c565d30b695ba353adfb8503a3a98dfee

## Parked

2026-08-30T23:41:31Z review · item aGradedMandate-specs · reason verdict BLOCKED · blockers 2

2026-08-30T23:46:23Z rescope · item retire TOOL-aGradedMandate-3 · reason The spec audit's round-1 BLOCKER F1: every implementation that buys anything in this repository reverses the owner ruling of 2026-08-27 recorded in .githooks/gate-env.sh, and the in-driver form is refused independently by govkit selfcheck check 7h3 because kit.toml ships that file to every adopter. F3 also measured the proposed intersection firing on 100% of closes, since the recall floor arms leg guards memory/ and every unattended run commits under it. Retired at rev-2 before any code; the fork and its five options are the spec's section 8 and are parked

2026-08-30T23:46:34Z decision · item Should a --close whose diff touches a held self-test leg's guard path run that leg? Today 46 of 86 legs are held, no carrier an unattended run reads even names GATE_SELFTESTS, and a run that edits a checker lands with none of that checker's arms exercised. · reason OPTIONS SEEN. (a) export GATE_SELFTESTS=1 inside tools/unattended/unattended.sh, refused by govkit selfcheck check 7h3 because kit.toml ships that file verbatim to every adopter and a repo-local policy may not ride out in a kit payload. (b) Set it in .githooks/gate-env.sh, which IS the sanctioned repo-local channel, and which is a straight reversal of the owner ruling of 2026-08-27 whose recorded reason is that the cost lands on every push including the majority that touch no kit source. (c) A .unattended.conf key defaulting OFF so the mechanism travels and the choice does not, lawful but inert here unless gov declares it ON, which is (b) wearing a longer name. (d) A new Definition-of-Done item reading a RECORDED self-test verdict joined to the kit tree state, a new public record surface and M3 veto 2. (e) Retire the unit and park the fork. WHY I REFUSED. Every option that buys anything in this repository is an owner turn: (b) reverses a dated ruling, (c) and (d) trip M3 veto 2, and M3 is explicit that a veto is not a licence to take the vetoed option. TWO MEASUREMENTS THE OWNER NEEDS. The gap is real, 46 of 86 legs held and zero mentions of the flag in any kit carrier; and the naive fix is worse than it looks, because the recall floor arms leg guards memory/ so the intersection fires on every unattended close, at a bar this repo sizes near 26 minutes of wall at width 8 and roughly twice that on a width-2 profile row, which breaches GATE_BOUND
