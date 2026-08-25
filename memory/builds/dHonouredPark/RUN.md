# dHonouredPark - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: bd0348f3b69be7af7c8452cf271990b176ddb43f
phase: RUNNING
branch-sha: bd0348f3b69be7af7c8452cf271990b176ddb43f
branch-ref: refs/heads/branch/build-readme-governance-e1c044
mode: slug
anchor-kind: run-branch
keepalive: 03c676d4
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: c97b8b90c0491acee8c227b51d4de9f05d452759
anchor-ref: refs/heads/main
base: bd0348f3b69be7af7c8452cf271990b176ddb43f

## Parked

2026-08-25T08:28:00Z decision · item Does memory/guides/BUILD-METHOD.md's line/byte budget pair ever get a gate? · reason M3 veto 2 puts a change to a governance carrier's own stated constraints outside the delegated mandate, and the budget pair is exactly that, so no resolver this run holds exists. Options seen: (a) add a leg asserting the pair, (b) leave it unobserved and say so in the prose, which is what TOOL-dHonouredPark-2 does, (c) drop the line half entirely and declare bytes only. The owner was asked about the line figure and the byte cap and ruled both; this was never put to them, and the parent build's RUN.md records three options with no recommendation. Refused rather than taken because the file states its own budget and a run that gates its own governing document has changed the terms it is judged by.
