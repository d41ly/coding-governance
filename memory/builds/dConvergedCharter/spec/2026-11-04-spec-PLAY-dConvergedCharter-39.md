# PLAY-dConvergedCharter-39 — the five renamed `gov-` Skills claimed in the codebase-map dossiers, the drift-audit kit given the dossier it lacks, and the baseline shrunk to match

**Status:** OPEN · rev-2 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 19 · advances PLAY-dConvergedCharter-24

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-40 |
| [2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's 23 specs
(`memory/builds/dConvergedCharter/reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md`)
confirmed finding **id 44 at MEDIUM**, report item **M25**. PLAY-dConvergedCharter-9 renders
`.claude/skills/gov-<name>/SKILL.md` for five Skills, and the codebase-map extractor keys every
directory under `.claude/skills/` holding a `SKILL.md` as a `rendered-skills` item
(`tools/codebase-map/map_extractors.py:216-217`). Four dossiers claim only the old names, the drift-audit
kit has no dossier at all, and the shrink-only baseline cannot gain `gov-drift`, so `codebase-map
coverage + freshness` reds with five UNCLAIMED keys. Closing it needs a document no unit's scope names,
a dossier for the drift-audit kit, which is why this finding is its own unit. It is one unit for one
MEDIUM finding because its write set, the map tree, is disjoint from PLAY-dConvergedCharter-38's gate
and inventory (BUILD-METHOD M6), and it lands right after the unit it repairs, the Skills it claims
existing only from that unit's commit.

## 2. Scope (IN)

Build-run precondition: PLAY-dConvergedCharter-9 has rendered the five `gov-` entries and the five
forwarders at the old paths.

- **S1** — id 44, the four existing dossiers. Each claims its new key beside the old one, which the
  forwarder keeps inventoried for `install.deprecation-window` releases:
  `memory/map/features/memory-recall.md` `rendered-skills = ["gov-recall", "memory-recall"]`,
  `memory/map/features/runlog.md` `["gov-runlog", "runlog"]`, `memory/map/features/lexicon.md`
  `["gov-lexicon", "lexicon"]` and `memory/map/features/branch-reconcile.md` `["cleanup", "gov-cleanup"]`.
  Each old key's claim leaves in the commit that closes its shim row, the kit's release-bound act
  (PLAY-dConvergedCharter-20 S4), and not in this build. Observed by AC1.
- **S2** — id 44, the new dossier. `memory/map/features/drift-audit.md`, in the dossier shape
  `memory/map/README.md` states, claims the drift-audit kit's items the baseline carries unclaimed at
  base: `kits = ["drift-audit"]`, `gate-legs` and `rendered-skills = ["drift-audit", "gov-drift"]`, with
  its title, status, streams and paths read from `tools/drift-audit/kit.toml` and its README at the
  pass. The `gate-legs` claims are DERIVED at the pass from the manifest `tools/gate-legs.json` and the
  baseline the parents leave, never typed from the base: each `drift-audit …` leg the manifest still
  holds and the baseline carries unclaimed. At base those are `drift-audit records`, `drift-audit
  selftest` and `drift-audit wiring`, but DEPL-dShippedRelease-10 S10, a parent built before this build,
  folds `drift-audit wiring` into `kit wiring (every descriptor's check)`, so it is not claimed here;
  and `kit wiring (every descriptor's check)` is claimed only by the dossier that owns the run-gates kit,
  never by this one. Observed by AC2 and AC3.
- **S3** — id 44, the baseline shrinks. Each key S2 claims moves from `memory/map/baseline.toml`
  (`:21-23`, `:36`, `:49` at base) into the new dossier's claims and stays in the inventory: its
  baseline line is taken out by hand, as the file's own grammar asks of a claimed item (`:1-5`), and no
  key is added to the baseline. `python tools/codebase-map/gen_map.py --write` regenerates
  `memory/map/generated/`. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- The renames, their entries, forwarders and shim rows: PLAY-dConvergedCharter-9.
- Removing an old name's claim when its shim row closes: the release-bound act of the kit the row
  names, outside this build.
- Claiming any other unclaimed baseline key: the baseline keeps every key this unit does not move.
- The live-carrier inventory: PLAY-dConvergedCharter-38.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-9` — `.claude/skills/gov-<name>/SKILL.md`, the five entries whose `rendered-skills` keys S1 and S2 claim; without them each claim is STALE

## 4. Design

### Evidence

Read at `e6909dcaa`; no product file differs from base `0d1c1dda`.

- `rendered-skills` is `walk_dir_keys(ROOT / ".claude" / "skills", {"SKILL.md"})`
  (`tools/codebase-map/map_extractors.py:216-217`): one key per directory holding a `SKILL.md`, so a
  forwarder at an old path keeps its old key.
- The claims at base: `memory/map/features/branch-reconcile.md:18` `["cleanup"]`, `lexicon.md:23`
  `["lexicon"]`, `memory-recall.md:22` `["memory-recall"]`, `runlog.md:21` `["runlog"]`; no file under
  `memory/map/features/` names the drift-audit kit as its feature.
- `memory/map/baseline.toml` carries the drift-audit kit's `gate-legs` (`:21-23`), its `kits` entry
  (`:36`) and its `rendered-skills` entry (`:49`), and only shrinks (`:1-5`). Of the three legs,
  `drift-audit wiring` leaves the manifest with DEPL-dShippedRelease-10 S10
  (`memory/builds/dShippedRelease/spec/2026-10-30-spec-DEPL-dShippedRelease-10.md:116-119`) before this
  unit's pass, so a claim of it would read STALE.

### Inventory

Minted: the dossier `memory/map/features/drift-audit.md`, feature id `drift-audit`. No function, flag or
verb.

### Rollout

Gov's tree, one pass at order 19, the commit after PLAY-dConvergedCharter-9's. The bar between the two
commits is not run; the close runs it once.

### Files touched (estimate)

- `memory/map/features/memory-recall.md`, `memory/map/features/runlog.md`,
  `memory/map/features/lexicon.md`, `memory/map/features/branch-reconcile.md`: S1
- `memory/map/features/drift-audit.md` (new): S2
- `memory/map/baseline.toml`, `memory/map/generated/`: S3

### Alternatives rejected

- **`gov-drift` claimed in an unrelated dossier.** A claim in the wrong dossier is one of the six things
  the spec-token join cannot see (`memory/TEMPLATE-SPEC.md`, writing rules), so it would pass and mislead.
- **`gov-drift` added to the baseline.** The baseline refuses a key its merge-base did not carry (`:3-5`).
- **The new keys claimed and the old ones dropped.** The forwarders keep the old directories through the
  window, so the old keys stay inventoried and would read UNCLAIMED.

## 5. Production-readiness checklist

- security — no code, no write surface: map records only.
- perf / scale — one regeneration of `memory/map/generated/`.
- error / empty / loading states — N/A: no runtime path; a claim of a key absent from the inventory is
  the coverage leg's STALE line at the close.
- observability — the coverage leg's verdict at the close.
- risks — a forwarder closed before its claim leaves reads STALE; S1 ties the two to one commit.
- testing — the probes of §6; the coverage leg at the close.
- migration — none.
- user docs — N/A: the dossiers are the map's own records, read by sessions, not by adopters.

## 6. Acceptance criteria

- **AC1** — When `git grep -n "gov-recall\|gov-runlog\|gov-lexicon\|gov-cleanup" -- memory/map/features`
  runs at the unit's tip, it prints one `rendered-skills` line in each of the four dossiers, each line
  also holding its old name.
  Red when: a renamed Skill's new key is unclaimed, or its forwarder's old key loses its claim.
- **AC2** — When `grep -n "gov-drift" drift-audit.md` runs in `memory/map/features/`, and each key the
  new dossier claims is grepped in `memory/map/baseline.toml` at the tip, the first prints the claim and
  no claimed key is found in the baseline; `grep -c 'drift-audit wiring' drift-audit.md` prints 0.
  Red when: `gov-drift` has no dossier, a key S2 claims still sits in the baseline, or a leg the parents
  retired is claimed.
- **AC3** — When `python tools/codebase-map/gen_map.py --write` runs at the tip, `git diff --exit-code --
  memory/map/generated/` exits 0, `memory/map/generated/inventories.json` lists the five `gov-` keys
  under `rendered-skills`, and it lists under `gate-legs` every key the new dossier claims there.
  Red when: the generated map is stale against the dossiers, an entry is missing from the inventory, or
  the new dossier claims a `gate-legs` key the inventory does not hold, which the coverage leg reads
  STALE.

## 7. Gates

`codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-04 · initial draft, promoted by the disposal of
  `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1` for finding 44 (MEDIUM, item M25), repairing
  PLAY-dConvergedCharter-9; that unit's §3 rewritten as this unit's sibling edit (its rev-3).
- rev-2 · 2026-11-04 · S2 §4 AC2 AC3 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1` findings 7 and 34: the new dossier's
  `gate-legs` claims are derived at the pass from the manifest and baseline the parents leave, `drift-audit
  wiring` dropped as retired by DEPL-dShippedRelease-10 S10, `kit wiring (every descriptor's check)` left
  to the run-gates dossier, and AC2 and AC3 checking every claimed leg against the baseline and the
  inventory.

## 10. Reuse audit

The seams extended are the dossier claim tables under `memory/map/features/` and the shrink-only
baseline `memory/map/baseline.toml`, read by the extractor `walk_dir_keys`
(`tools/codebase-map/map_extractors.py:216-217`) and the coverage leg; no code is written.
`python tools/codebase-map/reuse_lookup.py "claim a renamed rendered Skill in a codebase-map dossier"`
ranked `claims` (`tools/codebase-map/selftest.py`, fan-in 15), `map_root`, `load_map_tree` and
`render_map_md`, all readers of the map this unit edits as records; no existing seam fits beyond the
dossiers themselves, and the drift-audit kit has none, so S2 adds one. The recall probe's hits were the
audit item itself and TOOL-dLoggedFlight-32's spec-token join on dossier-claim sentences, which this spec
keeps to: every claimed object above is an exact key, never a path, glob or symbol.

Recall terms used: `python tools/memory-recall/query.py "how does a dossier claim a rendered skill key
when a skill is renamed" --terms "codebase-map dossier claims rendered-skills baseline shrink-only
unclaimed stale claim rename forwarder"`
