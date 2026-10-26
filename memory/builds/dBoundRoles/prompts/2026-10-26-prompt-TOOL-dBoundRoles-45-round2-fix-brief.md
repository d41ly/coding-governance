**Serves:** research TOOL-dBoundRoles-45 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51

# Round-2 fix brief — dBoundRoles, the reds on round 2's promotions before their commit

The round-2 spec audit (`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md`)
promoted its findings into TOOL-dBoundRoles-45 to -51 and folded hands-off edges into earlier specs; nothing is
committed. After the main loop staged them and ran `python tools/memory-tree/gen_build_index.py --write`,
`python tools/check-spec-tokens.py` printed the reds below. Fix each in the spec it names and nothing else. A
promoted spec stays `rev-1`; unit 43 already carries its pending rev line from this round's fold. The spec brief
`memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md` still binds.

## Q1 · suites inside acceptance criteria (`[bar]`)

TOOL-dBoundRoles-49 names `tools/govkit/selftest.py`, and TOOL-dBoundRoles-50 names `spawn-guard.test.sh` and
`selftest.py`, inside criteria. Rewrite each criterion to observe the unit's own checker on a staged break, a
`--selftest` flag of its own tool or a fixture (a one-case slice of the module's function is the form units 40 and
43 use), and keep the suite on a `New arm:` line in §7.

## Q2 · paths git does not track (`[path]`)

TOOL-dBoundRoles-50 names `tools/roles/spawn-guard.js` (TOOL-dBoundRoles-25 creates it) and TOOL-dBoundRoles-51
names `.governance/policy.json` inside criteria. Cite a file this build or a parent creates by its basename outside a
path shape in §6, keeping its full path in §2, §4 and Files touched. If `.governance/policy.json` is not a file any
spec creates, say which file was meant (dGroundRules' policy file is `.governance/policy.toml`) and correct it.

## Q3 · TOOL-dBoundRoles-43 is 65 bytes over the ceiling (`[size]`)

Its round-2 hands-off fold took it to 49217 bytes against 49152, with the generated records region filled. Every
later round's fold can add an edge bullet to it, so cut at least 2 KB of authored text this time: restated prose,
duplicated citations, wording. Never drop a finding, a scope item, a criterion's command or a Readers clause, and
do not hand-edit the generated region.

## Return

The files you changed, one line each with the Q-items taken, and 43's byte count after your cut. Commit nothing; run
the build-index generator only in a throwaway clone.
