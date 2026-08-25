# dPromptedSeam - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: c6268374384dea1a313a129ea070f06fffc3e7e5
phase: REVIEWING
mode: slug
anchor-kind: default-branch
keepalive: 5e8e6047
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: ee6554c3821bad569d7de47d5556f62700ea7dd2
anchor-ref: refs/heads/main
base: ee6554c3821bad569d7de47d5556f62700ea7dd2

## Parked

2026-08-25T09:38:11Z review · item TOOL-dPromptedSeam-1 · reason verdict BLOCKED · blockers 6

2026-08-25T10:16:35Z review · item TOOL-dPromptedSeam-1 · reason verdict BLOCKED · blockers 6 · NON-CONVERGENT

2026-08-25T10:17:14Z rescope · item supersede TOOL-dPromptedSeam-2 -> TOOL-dPromptedSeam-3 · reason Round 2 proved the unit's stated premise FALSE, and a unit built on a false premise fixes the wrong thing. read_object is four lines with no stopword test, no length test and no stemmer: it returns empty for exactly ONE reason, a single-token name. The spec claimed two reasons and claimed both vanish from --brief. Only the single-token case vanishes. The dead-token objects are TRUTHY and reported today, and they manufacture a false drift flag that is the loudest row in the output: --brief on lexicon.py prints 'of: openers x2, cache x1, ext x1, index x1, message x1, owners x1, parent x1, pin x1, token x1  <-- SPELLED MORE THAN ONE WAY', asserting nine unrelated concepts are one concept spelled nine ways because they all end in _of. That is an active wrong answer and it is the defect worth fixing; the one I specced was the half nobody could see. Superseded rather than folded because the goal sentence, the title, S1, S2, S3, D1, D3 and every acceptance criterion all rest on the false premise, so a rev bump would be a rewrite wearing a fold's clothes.

2026-08-25T10:17:28Z decision · item the spec process has now cost three audits on two units whose combined work is a template sentence and a four-line helper · reason Recorded because the owner should see the ratio, not because the run refused a decision it could take. Chronology: rev-1 of -1 refuted by an attended audit on three grounds; round 1 of the M4 audit returned BLOCKED with 6 blockers across both units; round 2 returned BLOCKED with 6 again and the driver called NON-CONVERGENT. Twenty-one distinct findings survive on two units whose actual deliverable is one rung in a rendered Skill and a predicate change in a four-line function. Every round found real defects and I verified the decisive ones by hand each time, so this is not a reviewer calibration problem -- it is that I keep writing spec prose whose premises I have not checked against the source, and the audit is doing the checking I should have done first. Three candidate responses and none is the run's to pick: (a) accept the ratio as the cost of specs that are read by machines and graded by gates, (b) allow a Tier-1 unit this small to skip the M4 audit and be caught by the closing diff review instead, which trades spec cost for rework risk, (c) require a measured before-state pasted into every spec whose premise is a claim about existing behaviour, which is the single change that would have caught rev-1's cost figure, round 1's wrong population and round 2's false premise -- all three were premise errors and none survived contact with a command. I lean (c) and it is a governance-carrier change, which M3 veto 2 puts outside the delegation.

2026-08-25T10:25:47Z rescope · item retire TOOL-dPromptedSeam-1 · reason The instruction this unit would add ALREADY SHIPS, three ways, and one of them is word-for-word what the unit specced. memory/guides/BUILD-METHOD.md:140 renders 'python tools/codebase-map/reuse_lookup.py <behaviour phrase, not a symbol name>' from a template whose {{TOOL_ROOT}} placeholder derives the sibling prefix -- which is the install-prefix problem this spec could not solve and gave up a whole revision to. SPEC-TEMPLATE.template.md:227 names the same script for section 10, and check-memory-hygiene.sh:744 is the forcing function, its own comment reading 'this is the check that makes anyone use it'. A fourth carrier of one instruction is two-answers-to-one-question, the class this repo names and this very spec cites in its own non-goals. What the unit could still claim is narrow: the MOMENT (a refusal, mid-code) and the AUDIENCE (an author who has already picked a name), and only on the will-not-fit branch, because --suggest fetch_conf prints a named replacement and never reaches the ladder the rung sits in. That is a real gap and it is small, and set against a documented anti-pattern it does not carry. Three audits found this spec wrong three times -- rev-1 refuted on cost, query shape and layer ban; round 1 on a renderer mechanism that does not exist; round 2 on a deliverable no section could produce -- which is itself evidence the unit was never clearly conceived. Retired rather than parked: parking implies a decision waiting on the owner, and this one is decided by what is already in the tree. The finding is worth more than the unit: the owner asked whether lexicon should integrate with codebase-map and memory-tree, and the answer is that it already does, through memory-tree, better than the integration I proposed.

2026-08-25T11:22:37Z review · item dPromptedSeam · reason verdict BLOCKED · blockers 1

2026-08-25T11:49:04Z review · item dPromptedSeam · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT
