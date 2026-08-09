# codebase-map — a self-verifying feature/inventory map for any repo

An opt-in kit: per-feature **dossiers** whose machine-readable claims are **CI-verified against
live code inventories** (a ratchet — new moving parts fail the gate until claimed; claims naming
dead keys fail too), a **shrink-only baseline** so adoption never blocks work, deterministic
**generated map artifacts** with a byte-compare freshness gate, and a **git-range digest**
(`map_diff`) that answers "what did that merge touch, feature-wise". Operationalizes the
playbook's §5/§6 documentation-currency goals with machine enforcement.

Reference implementation extracted from inCMS (ARCH-dWovenAtlas-1) after a ground-truth mapping
pass and two adversarial reviews; the portable engine (`map_lib.py`) is identical across repos —
project specifics live in exactly two files the adopting repo owns.

## Contents

- `map_lib.py` — the engine: dossier/baseline contract (first ```` ```toml ```` fence), pure
  both-direction coverage, deterministic renderers, digest attribution, fail-closed extractor
  helpers, and the one root resolver (`resolve_root`/`repo_root`). Stdlib-only, Python ≥ 3.11.
- `map_extractors.template.py` — the PROJECT layer: the `EXTRACTORS` dict declaring what is
  enumerable in this repo. Filling it well is the whole adoption job — see
  `INVENTORY-DERIVATION.md`.
- `test_codebase_map.template.py` — the gate; copied into the project's existing test dir
  (zero CI changes: a test file is its own deployment). Also runs standalone (`python <file>`).
- `gen_map.py` — CLI: `--scaffold · --write · --check · --seed-baseline · --seed-affordance-baseline
  · --seed-affordances --top N`.
- `map_diff.py` — the range digest (`<base>..<head>`), plus `--drop-affordance-exempt` (S4a
  touch-drop) and `--converge` (S5 closing loop): WARNs on each NEW export that resembles an existing
  high-fan-in seam of the same kind it did not wire through — shipped reinvention, over ALL new code —
  and routes each to `<MAP_ROOT>/reinvention-backlog.md` (deduped by `{new, resembles}`), alongside
  `new_clones` and the demoted hygiene hints. A report + WARN at review, never a merge gate.
- `reuse_lookup.py` + `reuse-lookup.agent.md` — the behaviour→seam lookup (S3): a portable CLI that
  ranks a reuse shortlist from the map's four recall sources (symbols · inventory keys · affordance
  seams · shared-seams prose), plus the agent-instruction that turns it into a decision. Run it
  BEFORE building new behaviour to wire through an existing seam instead of reinventing it.
- `adopt-codebase-map.sh --scaffold` — the one-shot adopter.
- `.codebase-map.conf.example` — per-repo conf (MAP_ROOT · GATE_FILE · MAP_DIFF_CMD).
- `selftest.py` — the kit's own contract check (`python <kit>/selftest.py`).

## Adopt (per project)

1. Copy this directory into the target repo as a directory NAMED `codebase-map` (the fixed name
   the gate resolves — don't rename). Its PREFIX is free: `<root>/codebase-map/` and
   `<root>/tools/codebase-map/` both work, so a repo that keeps its kits under one directory
   needs no exception. Below, `<kit>` is wherever you put it.
2. `cp <kit>/.codebase-map.conf.example .codebase-map.conf` and edit (map root, gate path). It
   goes at the repo ROOT whatever the kit's prefix — it is the marker the kit walks up to find.
3. `cp <kit>/map_extractors.template.py <kit>/map_extractors.py` and declare the
   project's inventories per `INVENTORY-DERIVATION.md` (the adopter scaffolds both files for you
   and stops until they're filled).
4. `<kit>/adopt-codebase-map.sh --scaffold` — scaffolds the map tree, seeds the baseline
   from live inventories, installs + runs the gate (green on a fresh seed, by construction).
5. Commit; add the map section to the kickoff manifest and the DoD line to the governance doc
   (WIRE-INTO-PROJECT §3b).

`reuse_lookup.py` and `map_diff.py` read only committed artifacts, so no project layer fails
closed for them. Both REFUSE (exit 2) when the resolved root carries no `.codebase-map.conf`,
rather than reporting `corpus: 0 symbols` / `collision_flags: 0` at exit 0 — a confident answer
over a population that was never read is the failure this kit exists to prevent.

## The contract in one paragraph

Claims are exact keys, gated BOTH directions; path globs are digest-only and never gated;
baseline additions are reserved for the initial backfill (shrink-only, socially enforced);
dossiers carry three pinned prose sections (`## Constraints & why`, `## Shared seams`,
`## Gaps`) plus a GRACED `## Reuse affordance` section (list the seams this feature is reused
through — `seam: <id> — reuse for <need>; extend via <point>` — or `none — <why>`; presence
gated, content not); generated artifacts are byte-deterministic (POSIX keys, LF compares, no
timestamps) so the freshness gate cannot flap across platforms; convergence rides the
design pass — substantial work touching an undossiered feature creates its dossier then.

The affordance check is graced by a shrink-only `affordance-exempt.toml` (feature names),
seeded from existing dossiers at adoption (`gen_map.py --seed-affordance-baseline`, wired into
the adopter) so it never retro-reds the fleet; a NEW dossier is never exempt, so new work is
always forced to record its reuse decision.
