# govkit Phase 0 — kit hardening (spec)

*2026-07-14 · DEPL-aKitHardener · node `a`. Pre-build design for the first govkit build unit. The
parent research ([../../2026-07-12-DEPL-aDeployScout/](../../2026-07-12-DEPL-aDeployScout/), §4 + §8)
is the approved shape; this is the Phase-0 slice made concrete.*

## Goal

Make every kit **machine-version-detectable** and every adopt script **idempotent + fail-fast**, so the
future deployer (`plan`/`apply`/`check`/`upgrade`) has a version to read and a converge entrypoint that
never wedges. No deployer code here — this is the substrate it stands on.

## IN scope (spec §4, all 7 surfaces)

- Version constant + doc marker for **memory-tree**, **codebase-map**, **agent-cap.js**, **tier2-review.js**.
- Idempotency + `set -e` fixes for the adopt scripts (**memory-tree** needs all three; **codebase-map** the idempotency one).
- New **`tools/settings-merge.py`** — idempotent `.claude/settings.json` merge of the agent-cap Workflow hook.
- **`python <GATE_FILE>` non-Python CI-leg fallback** — documented in `WIRE-INTO-PROJECT.md` (no code; the engine already ships the runner).
- New gate **`tools/check-kit-versions.sh`** — the contract made executable (rides `run-gates.sh`).

## OUT (Phases 1–3 — separate sessions)

Deployer core (`govkit.py`), `kit.toml` descriptors, the lockfile + `.sums` sidecar, the
`deploy-governance`/`governance-check` skills, `[wiring]` managed-block machinery, per-file
`# gov: <kit>@<v> <sha>` fingerprint headers (lock-writer output), marker-fencing the playbook.

## The version-marker convention (the durable contract Phase 1 consumes)

- **Value:** `1.0`, two-part `X.Y` for every kit — matches the existing `KIT_MANIFEST_VERSION="1.1"`;
  only monotone comparability matters to the deployer. (Rejected `1.0.0`: needless third part, inconsistent.)
- **Engine constant** — a greppable literal in the kit's single source-of-truth file:
  bash `KIT_<NAME>_VERSION=1.0`, python `KIT_<NAME>_VERSION = "1.0"`, JS meta `version: '1.0'`. One home per
  kit (no per-file duplication — that reintroduces the drift the deployer exists to detect).
- **Doc marker** — how the deployer reads the *installed* version in a target repo:
  - instantiated docs (memory-tree HYGIENE.md): HTML comment `<!-- gov:kit <name>@1.0 -->` (invisible, greppable, CRLF-safe because the token is mid-line).
  - generated artifacts (codebase-map MAP.md / inventories.json): a `<name>@1.0` token interpolated from the constant (no drift possible).
  - verbatim-copied engine files (agent-cap.js, tier2-review.js, settings-merge.py): the constant **is** the marker; JSON settings.json carries none, so the deployer greps the `agent-cap.js` command substring instead.
- **Drift guard:** memory-tree is the only kit with the version in *two* hand-kept literals (constant + shipped-doc marker); `check-kit-versions.sh` asserts they agree. All other kits are single-source.

## Two contested calls (readers split; resolved here)

1. **memory-tree, absent `.memory-tree.conf` → HALT (copy example, exit 1)**, not warn-and-proceed.
   A deploy tool must never silently scaffold the built-in *demo* disciplines into a real repo; halting
   mirrors codebase-map's existing loud behavior; gov + nicocares both ship a conf, so nothing relies on the fallback.
2. **codebase-map adopt → SKIP `set -e`** (memory-tree gets `set -eu`). Every fallible line in the
   codebase-map script already ends in `|| exit N` (already fail-fast); its half-scaffold safety lives inside
   `gen_map.py` (extractors run before the first write). Adding a reader-contested `set -e` that grants no
   required capability is exactly the over-build ponytail forbids. The load-bearing fix is the idempotency guard.

## Acceptance

Each kit is version-greppable; each adopt script re-runs clean (converge, no wedge); `settings-merge.py`
merges idempotently (apply-twice-changed=0); `check-kit-versions.sh` green; `bash tools/run-gates.sh` green
on a Python host. Risk tier: **2** (new kit contract) — closing adversarial review recorded in `build/`.
