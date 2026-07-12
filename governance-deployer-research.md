# The governance deployer ("one ratchet to wire them all") — research & recommendation

*2026-07-12. Research record for: one mechanism that deploys any subset — or all — of this repo's
kits (including future ones) into one or more target repos, executing every step and installing
every safeguard, unattended. Method: 12-agent research run (4 kit-surface inventories → 3
independently-designed architecture candidates + a prior-art sweep over copier/cruft/chezmoi/
Nix/Ansible/multi-gitter/Renovate → 3-lens judge panel → completeness critic), synthesized here.
Status: RECOMMENDATION — pre-build; owner approves the shape and the Phase-0 start.*

---

## 0 · The problem, precisely

Deployment today is `WIRE-INTO-PROJECT.md` — an agent runbook. It works (nicocares proved it end to
end) but it is the textbook **fire-and-forget scaffolding anti-pattern** (cookiecutter's known
failure, which copier/cruft exist to fix): nothing in a target repo records what was installed,
from which gov commit, with which decisions — so every deployed repo is an upgrade orphan, every
engine-identical copy (`manifest-check.sh`, future ones) is a drift landmine with no verification
channel, and every upgrade is a hand archaeology project. The manifest ratchet solved this for ONE
document; the deployer generalizes the same ratchet philosophy to the whole toolchain.

The empirical base (today's unattended retrofit) fixed the design's center of gravity: seven
judgment moments occurred — owner decisions, watch/gate derivation, a diverged remote mid-run, a
repo-local branch guard, a pre-existing red gate, push-credential scope limits, and living-doc
upgrade fidelity. **The failure class to engineer against is not "agent present" — this repo's
operating mode IS agent-present. It is "agent output unvalidated" and "skip silent."**

## 1 · Recommendation (one paragraph)

Build **govkit** — a mechanical python-stdlib core (`deploy/govkit.py`) driven by per-kit
`kit.toml` descriptors, invoked through a `deploy-governance` skill, with judgment steps executed
by an agent into validator-gated holes and every owner decision captured once in a committed
per-target deploy descriptor — and graft into it the runner-up's safety machinery: a role-tagged
lockfile with project-owned files structurally unwritable, marker-fenced `managed_block` wiring for
every shared host file, a bash-checkable `.governance-lock.sums` sidecar, hard apply-ordering,
an outbox/work-order convention for everything deferred, and a descriptor `spec` version. Two
entrypoints only: **`deploy-governance`** (install = upgrade = converge; same verb, idempotent) and
**`governance-check`** (the aggregate drift/verify gate, riding target CI). Judges: 2–1 for govkit
(operator-realism + failure-mode lenses) over the pure-mechanical converge engine (maintenance
lens); the score gap is small and the graft list below absorbs what made the runner-up win its lens.

## 2 · Architecture (the shape to build)

- **`kit.toml` per kit dir — the executable truth.** Declares: id/version/`spec`/`requires`;
  `[files.engine]` (wholesale-overwritable, LF/track flags), `[files.instantiate]` (template →
  living doc, with its version marker name + retrofit task id), `[files.owned]` (declarative, so
  `check` classifies and NEVER writes); `[decisions]` (owner-only keys); `[derive]` (agent task ids
  with validator commands); `[wiring]` (managed blocks for CI/pre-commit/settings.json/gate
  fences/.gitattributes); `[verify]`, `[probe]`, `[upgrade]` (version-gated recipes tagged
  `mechanical` | `agent-work-order`). A future kit = kit dir + kit.toml + registry line — zero
  deployer changes; gov CI selfcheck enforces descriptor completeness against a fixture repo.
- **Per-target deploy descriptor** (`deploy/targets/<name>.toml` in gov, or `.governance/deploy.toml`
  in the target — owner picks one home; recommendation: **in the target repo**, copier-style, so it
  travels with clones): kit subset, every `[decisions]` value, failure-policy knobs
  (on_diverged_remote / on_preexisting_red / on_hook_block / on_push_scope_fail), standing
  approvals (land/push/edit-workflows). Written once at an interactive `--intake` (the ONLY place
  AskUserQuestion lives); committed = the standing authorization for unattended re-runs.
- **Lockfile** (`.governance-lock.json`, tool-written only, + flat `.governance-lock.sums` in
  `sha256sum -c` format so target CI verifies with bash alone): per file — role
  (`engine|satellite-engine|instantiated|project-owned`), sha256, kit version, gov source commit.
  The apply layer has **no code path that writes a project-owned file** — the split stops being
  Maintenance prose and becomes structure.
- **The core** (`govkit.py`, ~1.6k LOC, stdlib, py≥3.11 on the deployer machine only): `plan`
  (three-way: gov-HEAD vs lock vs live; five-state per kit: `absent|current|stale|patched|broken`),
  `apply` (idempotent compare-then-act; all copies from the gov **git index** at a recorded commit,
  never the working tree; hard ordering: `.gitattributes` blocks → `git add --renormalize` →
  content → CI legs last), `check`, `intake`, `fleet`, `remove`, `selfcheck`.
- **The agent layer** (`skills/deploy-governance/SKILL.md`): runs intake; executes `[derive]` tasks
  (watch pathspecs, gate commands, pointer maps, extractor authoring) whose outputs must pass the
  descriptor's validators before apply proceeds; performs `agent-work-order` upgrades (living-doc
  retrofits) under a no-content-loss lint. Everything else is the script.
- **Landing policy:** each target deploy runs in a dedicated worktree/branch; **branch + PR is the
  default fleet landing mode**, direct-to-main only under an explicit standing approval in the
  deploy descriptor. This one default absorbs four of the seven empirical failure moments
  (diverged remote, branch guard, pre-existing red, push scope) — they become PR-review states, not
  mid-run wedges. A crash leaves an abandoned branch, never a half-mutated primary tree.

## 3 · The judgment boundary (what stays agent work, and how it's caged)

Mechanical (script): preflight (clean/fetch/ff/divergence-stop, python probe, push-scope probe,
gate baseline), all copies/hashes/EOL, managed-block wiring, JSON merge for settings.json (backup +
idempotent + duplicate-matcher detection), version stamps, probes (incl. the manifest red/green
probe generalized), verification battery, lock/sums, report. Agent (validator-gated): intake
conversation; placeholder/inventory/watch derivation (validators prove *shape and liveness* — the
residual "wrong-but-alive" hole is accepted and named, mitigated by PR review + the kits' own
runtime ratchets); living-doc upgrades via **copier-style three-way**: re-render the OLD template
with the saved answers, diff against the live doc to isolate local accretions, replay onto the new
render — never a raw template-vs-instance diff (34 filled placeholders make every naive merge
conflict). Deferred work (scope-limited CI edits, held-back retrofits) goes to
`.governance/outbox/` as work orders with `held_back` lock states — visible in every
`governance-check`, never silently dropped.

## 4 · Phasing (each phase independently valuable; DoD-gated)

- **Phase 0 — kit hardening (~10 items, ~150 LOC, before any deployer code):** version constants +
  doc markers for memory-tree (`KIT_MEMORY_TREE_VERSION` + HYGIENE marker), codebase-map (none
  exist today — upgrade-blocking), agent-cap.js, tier2-review.js; idempotency/`set -e` fixes for
  the two adopt scripts (today: refuse-if-present, half-scaffold wedges, silent demo-conf
  fallback); `settings-merge.py`; a `python <GATE_FILE>` explicit CI-leg fallback for non-Python
  repos. Worth landing even if the deployer never ships.
- **Phase 1 — descriptors + lock + `governance-check` (read-only).** Drift visibility across the
  fleet first: kit.tomls, lock writer, sums sidecar, the aggregate checker riding target CI.
  Cheapest slice, immediate value, zero write-risk.
- **Phase 2 — converge core.** `plan`/`apply` for engine files + managed blocks + verify battery;
  the acceptance matrix in gov CI: six fixtures (fresh empty repo · non-Python repo · hostile
  branch-guard repo · pre-existing v1.0-manifest repo · diverged-remote sim · push-scope-denied
  sim), each required to pass **apply-twice-changed=0** (the Ansible idempotency test) on POSIX +
  Git-Bash.
- **Phase 3 — agent integration + fleet.** Intake, `[derive]` validators, headless runtime contract
  (agent steps via headless `claude -p` with the skill, cwd = target deploy worktree, sequential
  per target, ≤4 fleet-wide, validator-red retries once then outboxes), three-way doc upgrades,
  `fleet` fan-out, `remove` (the descriptor already enumerates everything a kit put in — removal is
  its mechanical inverse; today de-adoption is an un-inventoried surface that strands gate files,
  playbook lines, and settings hooks).
- **Standing item — gov is fleet target #0.** This repo carries none of its own medicine (no
  manifest, no memory tree, no playbook instance). Converge it from its own HEAD first; it dogfoods
  every kit and every deployer path with the cheapest blast radius.

## 5 · Contested axes — resolved (ADR)

1. **Source of truth:** `kit.toml` is executable truth; WIRE-INTO-PROJECT.md is demoted to
   narrative with a gov-CI **parity gate** (every descriptor step ↔ a WIRE section; red on
   mismatch). Rationale: the v2.0 template rework already proved prose-as-machine-contract breaks;
   a parity gate keeps prose honest without making it load-bearing.
2. **Marker-fencing migration of instantiated docs** (playbook conditional deletions are
   prose-addressed today): do it ONCE, NOW, while exactly one live instantiation exists
   (nicocares) — every §-block the deployer must add/delete/upgrade gets `<!-- gov:block -->`
   fences in the template, mirrored by the retrofit.
3. **Junction distribution** (session-kickoff engine): keep for this one kit (single-owner
   machines; prior art correctly flags symlink farms as non-portable, but a per-MACHINE dev-tool
   skill is the legitimate case) — with a `governance-check --machine` leg asserting junction
   health, closing today's "restart and look" interactive-only verify.

## 6 · Alternatives considered (judge panel, 3 lenses)

| Candidate | Operator realism | Maintenance econ | Failure adversary | Note |
|---|---|---|---|---|
| **govkit (winner)** | **48** | 45 | **47** | mechanical core + descriptor + agent holes; worktree-branch landing survives crashes |
| Lockstep converge engine | 44 | **48** | 44 | purest state model; its safety machinery is grafted wholesale; loses on in-place apply wedges + cost (~5k LOC) |
| Bash adopt-registry | 41 | 42 | 41 | cheapest, most house-native; loses because every future kit = a new PROGRAM (per-kit adopt script) rather than data, and the existing adopters need a risky idempotency retrofit anyway |

Key prior-art imports: copier's committed answers file + old-render three-way merge; cruft's
lock + CI drift check; chezmoi/Ansible's converge-with-dry-run-diff + second-run-clean test;
multi-gitter's branch+PR fleet mode; Renovate's thin-reference-over-copy lesson (minimize copied
surface; checksum every copy that must exist). Anti-patterns explicitly avoided: naive
template-merge sync, hand-edited state files, undeclared snowflake tweaks, imperative steps with no
state model.

## 7 · Top risks (named, with mitigations)

1. **Validator false confidence** — shape ≠ truth for derived values. Mitigation: PR-default
   landing, the kits' own runtime ratchets (manifest C5/C6, map ratchet), decision-rot WARN in
   `governance-check` (descriptor older than N months, or pinned gate commands that no longer run).
2. **Lock integrity** — a merge-mangled or hand-edited lock corrupts converge classification.
   Mitigation: tool-written only, integrity-checked against the sums sidecar + per-file
   `# gov: <kit>@<version> <sha>` fingerprint headers in engine files (self-healing re-derivation).
3. **Descriptor/prose bifurcation** — parity gate covers ids, not semantics; accept + review.
4. **Outbox silt** — deferred work orders becoming wallpaper. Mitigation: `governance-check`
   escalates outbox age (WARN → FAILED past a threshold).
5. **Windows/POSIX duality** — the acceptance matrix runs both; every fixture on both shells.

Cost estimate (build): ~16 files / ~3.4k LOC / 4–6 focused sessions across the phases, plus
Phase 0's ~150 LOC of kit hardening. Each phase lands independently and is useful standalone.

## 8 · What to approve

(1) The govkit-with-grafts shape (§1–§3); (2) the ADR resolutions (§5); (3) Phase 0 as the next
build unit; (4) two policy defaults to confirm at first intake: branch+PR fleet landing (vs
direct-to-main standing approval) and deploy-descriptor home (target repo recommended).
