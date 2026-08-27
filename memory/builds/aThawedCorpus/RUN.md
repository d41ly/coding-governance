# aThawedCorpus - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 4f406bf73d203fe80f99d6b71576d63fa44dbc81
phase: RUNNING
branch-sha: 4f406bf73d203fe80f99d6b71576d63fa44dbc81
branch-ref: refs/heads/branch/memory-toolkit-closed-records-cache-8eee95
mode: prompt
anchor-kind: run-branch
keepalive: 01b60017
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: f5dff6aee0b0a0177fac8ec842532b461eeca71f
anchor-ref: refs/heads/main
base: 4f406bf73d203fe80f99d6b71576d63fa44dbc81

## Parked

2026-08-27T09:55:20Z rescope · item add TOOL-aThawedCorpus-4 · reason the per-check measurement found check 23 carries the same per-item spawn defect as check 21 — one awk per record for the acceptance ledger, plus two basename spawns and a cut per spec. Speccing it inside unit 1 would put two mechanisms in one spec and make the closing diff unable to say which half a finding lands on.

2026-08-27T11:21:18Z decision · item Should check-memory-hygiene.sh become ONE scanner process rather than a shell script that spawns per check? The owner asked this directly mid-run, 2026-08-27. · reason OPTIONS SEEN. (a) Collapse the two per-item loops to awk passes — what units -4 and -1 build: 1398 s to roughly 80 s, ~4300 spawns to 3, low risk, no gate property lost. (b) Rewrite the whole checker in Python — 1398 s to roughly 5 s, but check-arms.py discovers the 20 armed fail branches by scanning TRACKED SHELL and .memory-tree.conf pins check-memory-hygiene.sh:20:20, so the harness meta-gate goes blind on its own subject. (c) THE ONE I WOULD RECOMMEND, and it is the file's own established pattern rather than a new idea: one Python SCANNER reads the corpus once and emits a findings stream; the shell keeps all 20 fail branches and only prints what the scanner found. That is exactly what check 21 already does with gen_build_index.py --print-bindings, and the checker's own header records why the split is drawn there. It gets one process AND keeps the arms gate. WHY I REFUSED IT HERE. It ports the scanning half of checks 1-12, 21, 22 and 23 into Python in one diff, on the script that IS the merge bar, inside a run whose mandate is a performance fix. The measured remainder after (a) is roughly 80 s, so (c) buys a further ~75 s and costs a full Tier-2 build with a byte-identity proof over every check. That is a separate authorization, not a widening of this one. Units -2 and -3 as specced are worth less than (c) and should probably be reconsidered against it.
