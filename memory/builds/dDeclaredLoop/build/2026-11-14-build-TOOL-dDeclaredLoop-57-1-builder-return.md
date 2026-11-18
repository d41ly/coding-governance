**Serves:** journal TOOL-dDeclaredLoop-57

# Builder return — TOOL-dDeclaredLoop-57, dispatch 1: a divergence, nothing built

## Why

DIVERGENCE: spec section 5 (Production-readiness checklist, "risks") assumes no existing fixture receipt claims a kit without its dependency, and it marks that claim UNVERIFIED. I checked it by reading the fixtures, and it is false. In tools/govkit/selftest.py, the TOOL-dRedressedBar-11 "fixture B" block builds stale_target("rq11b"), which applies --kits check-wiring and pins gov_commit at OLD (24f39915). It then appends "agent-cap" to the receipt's kits and runs `update --write`. The live agent-cap descriptor requires settings-merge and kickoff-manifest. The registry at OLD already holds kickoff-manifest in [selection] default (checked with git show 24f39915:tools/govkit/registry.toml), so kickoff-manifest is never default-gained. The comment beside the [dRB-9] arm says the same: "agent-cap is left out for its unmet kickoff-manifest". settings-merge is gained, kickoff-manifest is neither claimed nor gained, so S1's demand_claimed_requires would now refuse this update with exit 2, naming ('agent-cap','kickoff-manifest'), before the settings-merge adopter runs. The arm "[dRB-11] update over fixture B: exactly one problem line names settings-merge, and it carries the adopter's `cannot read`" expects a `govkit: kit 'settings-merge'` problem line from that adopter. It would go red. The "exits non-zero", "gov_commit where it was" and "no declared-stop means" arms would stay green, but only by accident. The spec's write set and section 7 never mention this fixture, so building as written would break an existing arm. Section 5's risk bullet and section 4's Files touched would have to name the dRB-11 fixture B receipt in tools/govkit/selftest.py and settle it, either by claiming kickoff-manifest in that fixture (stale_target kits="check-wiring,kickoff-manifest", as the rq9p fixture beside it already does) or by recording that its settings-merge arm now observes the new refusal. Sections 6 and 7 would then name that fixture edit and what the arm still proves. Nothing was written, no --dispatch or --brief was declared, and the tree is clean at base, so there is no patch to save.

## Summary

Nothing was built or committed: the spec's one unverified claim turned out to be false.

The task asked me to check, before building, the claim in spec section 5 that no fixture receipt claims a kit without its dependency. I checked it by reading the code and the fixtures:
- **Kit dependencies:** I listed every kit's `requires` from the live descriptors with a `python -c` call into govkit.
- **Default set at the fixture's base:** `git show` of the registry at 24f39915 shows kickoff-manifest is already in the default set there, so an update from that point never gains it.
- **Hand-written receipts:** I read every one in tools/govkit/selftest.py and tools/govkit/matrix.py, and every update call in the matrix.

**What breaks:** one fixture, "fixture B" of the dRB-11 block in tools/govkit/selftest.py (`stale_target("rq11b")`). Its receipt claims check-wiring plus a hand-appended agent-cap, but not kickoff-manifest, which agent-cap requires. With the new check its `update --write` would be refused (exit 2) before the settings-merge adopter runs. Its arm expecting exactly one problem line about settings-merge would then fail.

**What is safe:**
- The other hand-written receipts claim memory-tree, pytest-parallel-guardrails, demo, ghost or a single kit, and are either fine or only ever run through `check`.
- Receipts that `apply` writes always have their dependencies met.

The full reason, and the two ways the spec could settle this fixture, are in `why`.

Before any write I read the base commit (7812191de1d672e1cbbcc9bbc40de48f2a8db547). I never ran `--dispatch` or `--brief`, edited no file, and the tree is clean at that commit, so there is no patch file and no gotchas check. I ran no gate or suite. Every command returned within its time limit, so nothing was skipped.

When the spec is revised, the close still owes the RED-first observation of the arm section 7 declares in `check_roles_default` (covering AC1 to AC4). That observation is not run here.
