# aDeclaredBound - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 93ce63eb2ada8a754b59bc2bee06a71cbee9e078
phase: REVIEWING
branch-sha: 75a664fbeedf0e9b41bbde56194d14ee37bc018d
branch-ref: refs/heads/branch/adeclaredbound-unattended
anchor-kind: run-branch
keepalive: 16f3c9e0
keepalive-reaped: yes
parked-surfaced: yes
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 098bebd9876c8f2f61a528b5cc9ac0a6b5d7719a
anchor-ref: refs/heads/main
base: 75a664fbeedf0e9b41bbde56194d14ee37bc018d

## Parked

2026-08-18T11:50:05Z decision · item TOOL-aDeclaredBound-4 is unbuilt: the declaration channel, the key-aware ratchet, the Workflow fixture isolation, the deployer rows and the section-B carrier. · reason Options seen: (a) build it now in one pass; (b) build S2c's Workflow fixture isolation first as its own pass, then the hook; (c) park it and hand the owner four of five with the bar green. REFUSED (a) because this is the SECURITY-SHAPED unit and its eleven acceptance criteria cannot be observed until the fixture isolation exists -- every Workflow arm in the hook's harness ships no cwd today, so a hook that reads a declaration would be tested by arms that resolve against the repo root and pass by finding nothing, which is the exact class both audits kept catching. REFUSED (b) as a real option but not one to start at the end of a long run: it is thirteen payload edits before a single line of the feature exists. Taking (c). What remains is enumerated in the spec at rev-4 and none of it is blocked -- this is a size and sequencing call, not a defect. Also carried forward from unit 5: memory/guides/SESSION-KICKOFF.md section B still says the bound is a FILE CONSTANT, true today and false the moment unit 4 lands, and that file is absent from unit 4's Files touched.

2026-08-18T21:57:40Z decision · item Eight left-shift gates named by the two closing-review rounds are NOT built, and M8 requires every confirmed finding to be left-shifted. · reason Options seen: (a) build all eight now; (b) build the two cheapest and park six; (c) park all eight enumerated. Taking (c). The eight: a scan of shipped remedy STRINGS in tools/**/*.js (the population is markdown-only, which is what hid the agent-cap.js remedy defect for a whole round); a shell sibling for tools/gate-lint/ catching an unquoted backslash-n in a command position (the class that put a literal control byte in a gate script during this very build); an eleventh codebase-map inventory joining a claimed gate leg to the files that implement it (the agent-cap dossier claimed two legs whose files were UNMAPPED); a declared pair asserting every key in the engine cap loop is named in HYGIENE.template.md with no bare default beside it; two check-testsuite-counts predicates (no padding n=n+1 outside the counter helper, and no two loops greping one file for the same shape); a repo-wide ban on unnamespaced BLAH:-default reads of a committed registry (the class recurred WITHIN this build - SPEC10_CUTOFF retired in unit 2, reintroduced in unit 5); and the coverage-proving exclusion arm round 2 asked for, which is now moot because the exclusion was deleted. REFUSED (a) because eight new gates is a build's worth of work and each needs its own arms - shipping a gate without running its own stated section 7 is precisely what produced two BLOCKED verdicts here, and doing it eight times at the end of a long run reproduces the cause rather than the fix. REFUSED (b) as arbitrary: no principled line separates two of them from the rest. None is blocked; all are scoped and independent.

2026-08-18T21:57:53Z decision · item TOOL-aDeclaredBound-5 is CLOSED in the spec, but its gate needed two full remediation rounds and the two-round Tier-2 cap (TOOL-aBoundedVerdict-1) is now spent for this subject. · reason Options seen: (a) reopen unit 5 and hand it back unclosed; (b) close it and record the evidence honestly; (c) seek a third review round. REFUSED (c) - the cap is a standing rule and spending it here would set the precedent that a cap yields to whoever is mid-build. REFUSED (a) because the unit's acceptance criteria are met and both rounds' findings are fixed with the bar green at 72/72; an OPEN status would say the work is unfinished, which is not what the record shows. Taking (b), with the caveat stated plainly: this gate has been WRONG twice in ways its own self-test did not catch until the arms were written from a MEASURED population rather than from a pattern. Round 1 found it certifying six live carriers clean; round 2 found the fix had excluded the one file where three of them lived. Both times it was green. A third pair of eyes on tools/check-agent-cap-restatement.sh before an adopter relies on it is a reasonable owner call, and the two review reports under memory/builds/aDeclaredBound/reviews/ are the brief for it.
