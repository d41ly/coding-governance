# codebase-map — a self-verifying feature/inventory map for any repo

An opt-in kit: per-feature **dossiers** whose machine-readable claims are **CI-verified against
live code inventories** (a ratchet — new moving parts fail the gate until claimed; claims naming
dead keys fail too), a **shrink-only baseline** so adoption never blocks work, deterministic
**generated map artifacts** with a byte-compare freshness gate, and a **git-range digest**
(`map_diff`) that answers "what did that merge touch, feature-wise". Operationalizes the
playbook's §5/§6 documentation-currency goals with machine enforcement.

Reference implementation extracted from adopter ic (ARCH-dWovenAtlas-1) after a ground-truth mapping
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

  Its `test_dossier_prose_carries_no_typed_count` arm refuses a present-tense typed count of an
  inventory population in dossier prose: a digit run before an inventory noun, `key` or `dossier`,
  found by `measure_typed_counts`, unless its sentence reads as a past measurement, which is a hit
  of any pattern in `FROZEN_MARKERS` and is listed there, not here. It prints its
  candidate and frozen counts on every run. The gap it states: it reads digits only, so a count
  spelled as a word ("two legs") passes, and so does a count inside a fence, the toml `title`
  included, or a code span. The template reaches a project only when absent, so an existing
  adopter gets the arm by copying it in.
- `map_imports.py` — an import target to the repo paths it may DENOTE, by AST: `resolve_import`
  plus the module index it resolves against, language-branched on the IMPORTER's extension because a
  dot means different things in Python and JS. Returns CANDIDATE paths; an empty list means external
  or unresolvable, which is not an error. It resolves import STATEMENTS only — not call sites, not
  attribute receivers — and counts nothing, so a consumer that reads it as a call graph will be
  wrong. Rescued from the lexicon kit's P3 predicate ahead of that predicate's deletion.
- `check_gate_coverage.py` — does the INSTALLED gate compare every artifact the engine writes?
  `--list` prints both sets. The adopter's gate is copied once and never again; the engine upgrades
  every time. This reports the SET difference, not a byte diff, because a project is entitled to
  customise its gate — and it states that it cannot tell a deliberate omission from a stale one.
- `gen_map.py` — CLI: `--scaffold · --write · --check · --seed-baseline · --seed-affordance-baseline
  · --seed-affordances --top N`.

  It writes `generated/inventories.json`, `generated/MAP.md`, `generated/CARDS.md` and, where the
  SYMBOL tier is declared, `generated/symbols.json`. `CARDS.md` holds one card of at most
  `FEATURE_CARD_CAP_BYTES` bytes per feature dossier, rendered by `render_cards_md` from the toml
  fence alone: title, status, streams, path, then decisions, claims and globs, each with its full
  count, and a `cut <n> item(s)` line naming what did not fit. A prose edit never stales it.
  An adopter upgrading past this kit's first `CARDS.md` adds one line to its gate's `fresh`
  mapping, `gen_dir / "CARDS.md": m.render_cards_md(tree, INVENTORY_IDS),`, which is the line
  `check_gate_coverage.py` reds naming until it is there.
- `map_diff.py` — the range digest (`<base>..<head>`), plus `--drop-affordance-exempt` (S4a
  touch-drop).

  Beneath its mixed header figure it prints a `# code:` line and a `# records:` line, split by the
  conf's `RECORD_ROOTS` (directories whose files are records, `memory` here). The CODE line is the
  map's convergence figure; the header also counts record writing, which the map does not claim to
  describe. `RECORD_ROOTS` blank prints an `undeclared` line, and an entry naming no tracked path a
  `DEAD PROBE` line, never a split. `--tree` attributes every tracked file instead of a range and
  prints the header and those lines only; it refuses a range, `--stale-dossiers` and
  `--drop-affordance-exempt`.

  `--stale-dossiers [--json]` lists the feature dossiers OLDER THAN THEIR PATHS: a commit touching
  a path a dossier claims is not an ancestor of the dossier's own last commit. Derived from git
  ancestry, never a stamp or a date. With no range it reads the whole history at HEAD; with
  `<base>..<head>` it lists the dossiers that range touched and did not refresh. Paths under
  `MAP_ROOT` are never a claim, a merge commit carries no paths (a conflict-resolution-only change
  is not seen), `FOUNDATION.md` is not measured, and a shallow clone prints `live` false rather
  than a count. Report only; drift-audit reads it as `dossiers_older_than_their_paths`.

  A `<git-common-dir>/codebase-map/reinvention-backlog.md` left in any clone is obsolete: the
  closing-loop mode that appended to it ran on no gate or hook and was deleted, so no tool writes
  or reads that untracked local file again; remove it by hand.
- `reuse_lookup.py` + `reuse-lookup.agent.md` — the behaviour→seam lookup (S3): a portable CLI that
  ranks a reuse shortlist from the map's four recall sources (symbols · inventory keys · affordance
  seams · shared-seams prose), plus the agent-instruction that turns it into a decision. Run it
  BEFORE building new behaviour to wire through an existing seam instead of reinventing it.
  Output is bounded by `--budget <bytes>` (default `DEFAULT_BUDGET` in the script, measured over
  the replay corpus): the header, candidates and sources stop before the first candidate that
  would pass it, the first candidate always shows, and a `cut <n> of <m> candidate(s)` line names
  what was dropped. `--budget 0` shows them all; the partial-recall notice, the install-site
  totals and the `Decision:` line print at every budget. Each candidate line carries its fan-in
  (files naming it, definers subtracted) and, where any exist, `installs <n>`: the install sites,
  tracked files carrying a `# >>> <name>` canonical-copy marker, the source the marker names left
  out. A symbol is a SEAM when fan-in plus installs reaches `SEAM_FANIN_THRESHOLD`, here and in
  `gen_map.py --seed-affordances` alike; installs never move the ranking order.
- `adopt-codebase-map.sh --scaffold` — the one-shot adopter.
- `.codebase-map.conf.example` — per-repo conf (MAP_ROOT · GATE_FILE · MAP_DIFF_CMD).
- `selftest.py` — the kit's own contract check (`python <kit>/selftest.py`).

## Adopt (per project)

1. Copy this directory into the target repo as a directory NAMED `codebase-map` (the fixed name
   the gate resolves — don't rename). Its PREFIX is free: `<root>/codebase-map/` and
   `<root>/<prefix>/codebase-map/` both work, so a repo that keeps its kits under one directory
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
rather than reporting `corpus: 0 symbols` / every file UNMAPPED at exit 0 — a confident answer
over a population that was never read is the failure this kit exists to prevent.

## The contract in one paragraph

Claims are exact keys, gated BOTH directions; path globs are digest-only and never gated;
baseline additions are reserved for the initial backfill (shrink-only: the gate refuses a key the
baseline at the branch's merge-base with the remote default branch did not carry, and says
`UNGRADED` when no such base resolves);
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
