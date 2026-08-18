# aDeclaredBound - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: d0ad6ab1ba29fe2088f462fd0855050642aa807d
phase: BUILDING
branch-sha: 75a664fbeedf0e9b41bbde56194d14ee37bc018d
branch-ref: refs/heads/branch/adeclaredbound-unattended
anchor-kind: run-branch
keepalive: 16f3c9e0
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 098bebd9876c8f2f61a528b5cc9ac0a6b5d7719a
anchor-ref: refs/heads/main
base: 75a664fbeedf0e9b41bbde56194d14ee37bc018d

## Parked

2026-08-18T11:50:05Z decision · item TOOL-aDeclaredBound-4 is unbuilt: the declaration channel, the key-aware ratchet, the Workflow fixture isolation, the deployer rows and the section-B carrier. · reason Options seen: (a) build it now in one pass; (b) build S2c's Workflow fixture isolation first as its own pass, then the hook; (c) park it and hand the owner four of five with the bar green. REFUSED (a) because this is the SECURITY-SHAPED unit and its eleven acceptance criteria cannot be observed until the fixture isolation exists -- every Workflow arm in the hook's harness ships no cwd today, so a hook that reads a declaration would be tested by arms that resolve against the repo root and pass by finding nothing, which is the exact class both audits kept catching. REFUSED (b) as a real option but not one to start at the end of a long run: it is thirteen payload edits before a single line of the feature exists. Taking (c). What remains is enumerated in the spec at rev-4 and none of it is blocked -- this is a size and sequencing call, not a defect. Also carried forward from unit 5: memory/guides/SESSION-KICKOFF.md section B still says the bound is a FILE CONSTANT, true today and false the moment unit 4 lands, and that file is absent from unit 4's Files touched.
