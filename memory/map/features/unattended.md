# unattended — the run that merges and pushes with no owner turn

```toml
feature = "unattended"
title = "Unattended runs — a mandate on disk, not a block of chat"
status = "shipped"
streams = ["tooling", "playbook", "kickoff", "deployer"]
decisions = []

[claims]
gate-legs = ["unattended kit gate", "unattended gate selftest", "unattended driver selftest", "unattended skill wiring", "unattended adopter e2e"]
kits = ["unattended"]
git-hooks = []
workflow-scripts = []
skill-engines = ["session-kickoff"]
rendered-skills = ["unattended"]
gotcha-classes = ["assertion-between-two-derived-values.md", "second-implementation-is-not-a-second-opinion.md",
  "inputs-inside-the-subjects-reach.md",
]
guides = ["UNATTENDED-PROTOCOL.md"]
backlog-shards = []
[paths]
globs = [
  "tools/unattended/*",
  "memory/guides/UNATTENDED-PROTOCOL.md",
  ".unattended.conf",
]
```

## Constraints & why

**The checkpoint is replaced, not removed.** Every other kit here makes a rule enforceable. This one
removes a rule — the explicit ask before a merge and a push — and its whole burden is to put
something machine-checkable in the vacated slot. That is why the mandate is ASSERTED rather than
written by the run, and why reachability from the pinned BASE is part of the contract: a run that can
author its own authorization has none, and every gate downstream would certify it.

**The anchor is an OBSERVATION of the remote, and the kit no longer claims more than that.** Kit 1.0
pinned BASE against `refs/remotes/origin/<default>` and justified it in a source comment claiming the
ref could not move without a push. That was false — `git update-ref` moves it offline — and it was
reproduced end to end: preflight printed OK over a base the run had authored, the leg agreed silently,
and the push landed. The ref name and tip now come from what the remote advertises for its own HEAD,
and `GOV_DEFAULT_BRANCH` is a cross-check that can only refuse. Both routes are inert rather than
detected: neither value is read at all.

**A sha is a NAME, and the dereference is pinned separately.** `git replace` substitutes the object a
sha resolves to and a graft file rewrites the commit graph, both at a perfectly honest anchor, so
neither is closed by any amount of anchor hardening. Every read that turns a sha into bytes or into
ancestry goes through a wrapper pinning `core.useReplaceRefs=false` with `GIT_GRAFT_FILE` pointed
away from the repo. The two suppressions are not interchangeable and only the second stops a graft —
measured, not assumed.

**The boundary is stated rather than implied.** A design panel broke four independent anchor
mechanisms and converged on the reduction that a check running under the run's own uid cannot
constitute authorization. The protocol's §9 enumerates what remains reachable — editing the kit,
shimming its tools, skipping the hook layer, relaying through a seeded endpoint, or never creating a
run-state file at all — and names the only control that binds: re-running the same leg in a clone the
run never touched.

**Nothing in a script can reach the scheduler.** The keepalive store is in-memory and session-scoped,
so a driver verb claiming to schedule or reap it claims an effect it cannot produce. The obligation
therefore splits by actor — the agent schedules and reaps, the driver records an id and asserts a
recorded reap — and the reaped item is labelled agent-attested wherever it is reported, so it never
spends the `--close` override budget.

**Declarations, not constants.** The phase vocabulary, the Definition-of-Done set, the lander, the
bypass flag and the scheduler tool names all live in the repo-root `.unattended.conf`. The driver and
the leg READ them; a phase token or a DoD item spelled into a script is a defect. The kit owns the
CORE of both sets and the project may only EXTEND them, asserted against a shrink-only floor —
without that floor, deleting an item is a silent, reason-free override of everything keyed on it,
and the fleet already has a recorded case of a pin RAISE being indistinguishable from a drain.

**The run-state file is split mechanically, not by discipline.** The generated region is
byte-compared against a fresh render; the authored region holds only the five facts nothing in the
tree derives. The precedent is in this repo: one build's hand-kept status file still reads
IN-PROGRESS while the generated region of the same build's README correctly reads CLOSED. The
authored half rotted and the derived half did not.

**The template is byte-gated and this feature is kit-conditional.** The playbook has ~190 bytes of
headroom, so the unattended rules live in the domain-rules companion (§1) with two amended clauses in
the template proper, both written to stay true for a non-adopting re-puller. A new universal-core
section for an opt-in kit was rejected on both counts.

## Shared seams

- `memory/guides/REVIEW-PROTOCOL.md` — the structural precedent for a BINDING guide: charter-cited,
  in the hygiene index set, entry-budget exempt, enforced by a leg rather than by its own prose.
- `tools/push-main.sh` + `.githooks/pre-push` — the mandated lander and the marker that makes it
  mandatory. The kit names it through `LANDER`, never by hardcoded path.
- `tools/check-wiring.sh --check` — the non-repairing wiring probe preflight delegates to. The
  repairing mode is deliberately out of reach.
- `tools/memory-tree/check-memory-hygiene.sh` — supplies the run-state file's legality (check 4's
  whitelist), its size cap (check 6 via `index_set`), its prose exemption (check 7's `ex7`) and,
  by deliberate omission, leaves phase-vocabulary validation to this kit's own leg.
- `tools/memory-tree/gen_build_index.py` `apply_region()` — the generated-region splice contract,
  reused verbatim rather than re-implemented.
- `tools/drift-audit/drift_report.py` — the judgeability discipline, reused for witness RESOLUTION
  and deliberately NOT for witness PRESENCE, which is its own refusal here.

## Reuse affordance

seam: `.unattended.conf` — the project declaration surface. Anything that needs to know this repo's
lander, merge bar, wiring check, bypass ban or scheduler tool names reads it from here rather than
re-deriving or hardcoding. `PHASES_EXTRA` and `DOD_EXTRA` are the sanctioned extension points; the
core sets are not editable from the project layer.

## Gaps

All seven units are built on the unit branch and UNMERGED. What remains is not design work:

- **No end-to-end run has been driven through this kit.** Every property above is designed,
  gated and documented; none is yet observed on a live unattended run. The five legs prove the
  pieces refuse and agree in fixtures — they do not prove a real run reaches `LANDED`.
- **The junction arm of the adopter e2e is SKIPPED on node `a`**, which lacks the privilege to
  create a symlink. It reports the skip loudly rather than passing, but the shape this fleet
  actually installs with is therefore unexercised here and needs a run on a node that can link.
- **No adopter has installed this kit.** The path exists and is gated; nothing has travelled it.
- **A bug class this build DISCOVERED is now catalogued but only gated in one place.**
  `assertion-between-two-derived-values` was found here, in this kit's own leg, and the arm that
  proves it is this kit's. The class is general — any checker that composes both sides of a
  comparison has it — and nothing sweeps for it repo-wide.
- **The gate leg still recomputes BASE against a live local ref.** The driver's anchor is observed;
  the leg's is not. It reads `GOV_DEFAULT_BRANCH` and `refs/remotes/origin/<d>`, so handed a tree
  with a forged tracking ref it recomputes the same wrong value and agrees. The driver refuses such a
  run before a run-state file exists, so the reachable damage is bounded, but the leg's own
  independence is not what it claims. Scoped as the next unit.
- **Nothing binds the executing kit to kit code an owner approved.** A run may edit these scripts and
  commit them; the parity legs compare two files the same run can change together. This bounds every
  property above and is the reason the protocol names an off-machine verifier as the real control.
- **The keepalive half is unenforceable by construction.** Two DoD items are agent-attested because
  no script can reach the scheduling store. They are labelled everywhere they appear, and they are
  still the softest part of the contract.
