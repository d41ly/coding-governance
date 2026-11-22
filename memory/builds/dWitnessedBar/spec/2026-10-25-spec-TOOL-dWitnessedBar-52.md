# TOOL-dWitnessedBar-52 — the scalar-pin seed reads every root conf the working tree holds, so a fresh install seeds its pin before its first commit

**Status:** CLOSED · rev-6 · 2026-11-19 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 11 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-52-deviation-521.md](../build/2026-10-25-build-TOOL-dWitnessedBar-52-deviation-521.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md) | research | TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-11-19-build-TOOL-dWitnessedBar-52-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-52-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-52-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-52-1-builder-return.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-52-2-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-52-2-builder-return.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-52-deviation-522.md](../build/2026-11-19-build-TOOL-dWitnessedBar-52-deviation-522.md) | deviation | — |
| [2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md](../build/2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md) | research | TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-17-reground-2-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-17-reground-2-brief.md) | journal | TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-53 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-52-2-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-52-2-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-52-3-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-52-3-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-52-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-52-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-52-reground-3-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-52-reground-3-brief.md) | journal | TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-18 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-52-reground-3-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-52-reground-3-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-52-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-52-reground-brief.md) | journal | TOOL-dWitnessedBar-53 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-52-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-52-reground-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-52-rename-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-52-rename-brief.md) | journal | TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-84 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-52-rename-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-52-rename-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 40 to 51
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, in its item **H1**, which it shares with id 13
(`TOOL-dWitnessedBar-53`). `TOOL-dWitnessedBar-46` S2, landed at `e1efccc6b`, has the memory-tree
adopter seed `conf-scalar-pins` at the end of `--scaffold`, measuring "the tree's tracked root confs".
At that moment `.memory-tree.conf` has been copied from the example by the adopter's seed-and-stop
(`tools/memory-tree/adopt-memory-tree.sh@fbbf1499d9a4:98-102`) and is untracked: the scaffold stages
only `git add "$M"` (`:869`, `:871`), and `:875` tells the user to commit the conf later. The seed
writes an armed, empty population. Written only where its home is absent or unarmed
(`tools/lib/legacy_ledger.py#seed_population`), it is rewritten neither by a rerun nor by the
`--seed-pins` row unit 46 S2 runs at each update. Once the conf is committed,
`ratchet (keys, not a scalar)` reds on each scalar pin the conf assigns, the example's
`ROW_DUPLICATE_PIN="0"` among them, the defect unit 46 exists to close. This unit takes the report's
fix: the seed reads the root confs present in the working tree, tracked or not. It repairs
`TOOL-dWitnessedBar-46`.

## 2. Scope (IN)

- **S1** — One conf set. `tools/memory-tree/ratchet.py` reads the root confs through one function,
  `read_root_confs(root)`: the files `git ls-files --cached --others --exclude-standard -- ':(glob).*.conf'`
  lists, run at the repository root. A conf copied but not yet committed is read, and a conf the
  repository ignores is not. `tools/memory-tree/ratchet.py#read_root_conf_lines`, the one conf walk
  `#measure_scalar_pins` and `#measure_cutoffs` share since `TOOL-dWitnessedBar-17` landed it at
  `9a29f1e96` (its §4 "The cutoffs"), takes the paths `read_tracked_paths(root)` lists that
  `ROOT_CONF_RE` matches; it takes `read_root_confs(root)` instead, and `ROOT_CONF_RE`
  (`tools/memory-tree/ratchet.py@586cad8fe8a9:97`), whose one reader is that filter (`:489`), is
  deleted with it. `read_tracked_paths` stays for its other caller, the widen check of
  `#run_never_gains`. `keys-not-scalar --measure`, the seed of unit 46 S2, reaches the new read through
  `measure_scalar_pins`. Observed by AC1, AC2 and AC3.
  **Readers:** by name: `tools/memory-tree/ratchet.py`, which spells `ROOT_CONF_RE` at its definition
  and in `read_root_conf_lines`' filter and nowhere else, as §4 Evidence's grep reads · by value: the
  filter this item replaces is its one reader, so NO VALUE READERS beyond it.
- **S2** — The leg reads the same set. `keys-not-scalar` without `--measure`, the check of
  `TOOL-dWitnessedBar-14` S11, measures through the same `measure_scalar_pins` call as its seed
  (`tools/memory-tree/ratchet.py#run_keys_not_scalar`, landed at `25a3d2970`), so S1's one change
  reaches both and this unit adds no second call; the seed and the leg never measure two different
  sets. Observed by AC1 and AC3.
- **S3** — What it does not check, stated. `ratchet.py`'s docstring for `read_root_confs` names the blind
  spot: a root conf the repository ignores is never measured, so a pin assigned only in a machine-local
  ignored conf is neither seeded nor held. Observed by AC2.

## 3. Non-goals (OUT)

- The seed verb, its state table and its absent-only rule: `TOOL-dWitnessedBar-15`'s.
- The adopter's seed call, its `--seed-pins` mode, the population's home and check 3's named list:
  `TOOL-dWitnessedBar-46`'s.
- The suite arm that runs every seeding population in an uncommitted scaffold, the report's
  left-shift: `TOOL-dWitnessedBar-53`, id 13's unit.
- An armed population with zero rows that misses a pin: the minors batch's id 44 item
  (`TOOL-dWitnessedBar-57`).
- Draining the example conf's pins: `TOOL-dWitnessedBar-17` S3's. AC1's fixture plants its own pin
  (§8 F2).
- The policy kit's tracked root-conf read, `tools/policy/policy.py#derive_legacy_homes`, which reads
  the committed set by design (§8 F3).

### Edges

- **consumes-from** `TOOL-dWitnessedBar-46` — `keys-not-scalar --measure` and the adopter's seed of `conf-scalar-pins`, whose conf read this unit widens to the working tree
- **consumes-from** `TOOL-dWitnessedBar-14` — `ratchet.py keys-not-scalar`, the leg whose conf read S2 binds to the seed's
- **hands-off** `TOOL-dWitnessedBar-53` — `read_root_confs`, whose behaviour across a target's first commit unit 53's suite arm observes for every population the scaffold seeds
- **consumes-from** `TOOL-dWitnessedBar-61` — the null SHA on an unborn HEAD, without which AC1's scaffold seed in a commitless `git init` cannot write its row
- **hands-off** `TOOL-dWitnessedBar-62` — `read_root_confs` and AC3's plant, which the minors batch keeps to regular work-tree files and arms with a row for another key (ids 9, 11, 34, 40)

## 4. Design

### Evidence

- `cp "$HERE/.memory-tree.conf.example" "$ROOT/.memory-tree.conf"` with no `git add`, then an exit
  asking for an edit (`tools/memory-tree/adopt-memory-tree.sh@fbbf1499d9a4:98-102`), the
  `seed-and-stop` outcome the descriptor accepts (`tools/memory-tree/kit.toml@aca25b09b5ce:150-153`).
  The scaffold seeds `conf-scalar-pins` through `#seed_scalar_pins` (`adopt-memory-tree.sh@fbbf1499d9a4:868`),
  and its only stagings follow, `git add "$M"` (`:869`, `:871`); its next-step line is
  `git add $M/ .memory-tree.conf && commit` (`:875`).
- The adopter met this class once already: the `method-carriers.txt` seed reads
  `{ git ls-files; find . -type f ... }` because "`git ls-files` is EMPTY here and a tracked-only seed
  writes a header and nothing else" (`adopt-memory-tree.sh@fbbf1499d9a4:824-829`).
- The example conf assigns `ROW_DUPLICATE_PIN="0"`
  (`tools/memory-tree/.memory-tree.conf.example@815710c14c4b:325`), the one scalar count among its
  five `*_PIN=` lines, PINNED 2026-11-19 at `57547e855` by
  `grep -nE '^[A-Z_]+_PIN=' tools/memory-tree/.memory-tree.conf.example`. `TOOL-dWitnessedBar-17` S3,
  which builds before this unit, removes every one of those lines from that file (§8 F2).
- The defect, probed in a scratch target built as AC1's fixture. The scaffold printed
  `armed conf-scalar-pins 0` (PINNED 2026-11-19 at `57547e855`). After `git add -A && git commit`, with
  the home removed, `python tools/memory-tree/legacy_ledger.py seed --population conf-scalar-pins`
  printed `armed conf-scalar-pins 6`, the example's pins and the plant (PINNED 2026-11-19 at `57547e855`).
- `read_registrations` reads tracked descriptors only (`tools/lib/legacy_ledger.py#read_registrations`,
  TOOL-dWitnessedBar-13 §8 F7), and `govkit apply` stages every file it lands before any adopter runs
  (`tools/govkit/govkit.py#_cmd_apply`, its STAGE block). So at a governed install the seed sees the
  kit's registration while the conf the adopter copied stays unstaged; AC1's fixture is that state.
- Unit 15 §4: a live result with zero rows is written armed and empty, and a present armed home is
  left alone on a rerun.
- The read, probed 2026-11-19 at `c3884a6b9`: in gov's tree
  `git ls-files --cached --others --exclude-standard -- ':(glob).*.conf'` lists the confs
  `git ls-files -- '.*.conf'` lists, five each (PINNED 2026-11-19 at `c3884a6b9`, and again at
  `578296c1f` and `57547e855`); in a scratch `git init` it lists an untracked root
  `.x.conf`, and neither a nested `sub/.y.conf` nor a root conf named in `.git/info/exclude`.
- The landed measure, read at `6df29c83d`: unit 14 (`25a3d2970`) has `#run_keys_not_scalar` call
  `tools/memory-tree/ratchet.py#measure_scalar_pins` once for both the seed and the leg; unit 17
  (`9a29f1e96`) moved that function's conf walk into `#read_root_conf_lines`, which `#measure_cutoffs`
  shares and which walks each tracked root conf through `#read_tracked_paths` filtered by
  `ROOT_CONF_RE`. No other line reads `ROOT_CONF_RE` (`git grep -n ROOT_CONF_RE -- tools skills`).
- The policy kit spells the same pathspec over the tracked set only:
  `tools/policy/policy.py#derive_legacy_homes` runs `git ls-files -z -- ':(glob).*.conf'` over the
  committed legacy homes it converts (§8 F3).

### The read

```
read_root_confs(root) := git -C <root> ls-files --cached --others --exclude-standard -- ':(glob).*.conf'
                         (glob magic: `*` never crosses `/`, so only root-level files match)
read_root_conf_lines(root) -> its walk over read_root_confs(root), in place of read_tracked_paths
                              filtered by ROOT_CONF_RE
measure_scalar_pins(root)  -> over read_root_conf_lines(root), unchanged
measure_cutoffs(root)      -> over the same read_root_conf_lines(root), unchanged
keys-not-scalar --measure  -> one row per scalar *_PIN= assignment, from measure_scalar_pins(root)
keys-not-scalar            -> unheld pins, from the same measure_scalar_pins(root), against conf-scalar-pins
```

`measure-cutoffs` reads the widened set too, which unit 17 §4 "The cutoffs" records; in gov's tree
every root conf is tracked (§4 Migration), so its seed is unmoved.

`--exclude-standard` rather than a raw directory listing keeps an ignored local conf out, which a
committed tree never holds either; so the set read before the first commit equals the set read after
it whenever the user commits what the scaffold told them to.

### Inventory

Minted: the function `read_root_confs`, and the plant functions `run_plant_untracked_conf` and
`run_plant_ignored_conf` behind the `PLANTS` cases `untracked-conf` and `ignored-conf`, spelled as the
table's other cases are (`tools/memory-tree/ratchet.py@586cad8fe8a9:1039-1050`). Removed: the constant
`ROOT_CONF_RE`. Naming cells: `python tools/lexicon/lexicon.py --suggest <name> --as py.function`
answered OK for each minted name, asked 2026-11-19 at `6df29c83d`. `read` is the verb the file's other
readers `read_tracked_paths` and `read_root_conf_lines` lead with, and the lexicon steers
`list_root_confs` to `read_root_confs`; `derive_root_confs` is accepted too but is the name of
govkit's descriptor-class read (`tools/govkit/govkit.py#derive_root_confs`), a different set.

### Migration

None for gov: every root conf of gov's tree is tracked, so the set is the tracked set, the confs of
§4 Evidence (five, PINNED 2026-11-19 at `57547e855`).

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-46`. `TOOL-dWitnessedBar-17` shares this unit's
order, builds before it, and drains the example conf AC1's fixture is made from; the fixture's planted
pin (§8 F2) keeps AC1 observable over the drained example.

### Files touched (estimate)

- `tools/memory-tree/ratchet.py`
- `memory/map/generated/symbols.json`, regenerated for the minted function definitions

### Alternatives rejected

- **Seed after the first commit.** The adopter never commits, by design
  (`tools/memory-tree/adopt-memory-tree.sh@fbbf1499d9a4:875`), so the seed would move
  to a step nobody runs and the population would start unarmed.
- **Seed from the conf the adopter has just written.** It names one file where the leg reads every root
  conf; the two sets would differ on the first adopter carrying a second conf.
- **A raw directory listing.** It reads an ignored machine-local conf that no commit will ever carry.

## 5. Production-readiness checklist

- security — reads files git already lists; writes nothing new.
- perf / scale — one `git ls-files` per run, as before.
- error / empty / loading states — no root conf: no rows, an armed empty population, as unit 15 states.
- observability — the leg prints the confs it read.
- risks — an ignored conf's pin is invisible; S3 states it.
- testing — AC1 to AC3 by fixture and plant; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`; the docstring states the set.

## 6. Acceptance criteria

- **AC1** — When `adopt-memory-tree.sh --scaffold` runs in a scratch target whose `.memory-tree.conf`
  is the example plus the planted line `FOO_PIN="3"`, copied and untracked,
  the kit copy's `python ratchet.py keys-not-scalar`, run at the target's root, exits 0 naming the row
  `.memory-tree.conf` `FOO_PIN`; after `git add -A && git commit` it exits 0 naming the same row.
  Red when: the measure reads tracked confs only, so the seed arms without the planted row and the leg
  reds once the conf is committed.
  fixture: a scratch `git init` target under `%TEMP%/<short-name>` holding the kit copied to
  `tools/memory-tree/` and staged, as `govkit apply` leaves it, and the conf copied and left unstaged
  (§4 Evidence); the tree holds none.
- **AC2** — When `python ratchet.py --fixture --plant untracked-conf` runs in `tools/memory-tree/`, an
  untracked root `.x.conf` assigning `FOO_PIN="3"` appears in `keys-not-scalar --measure`'s output; under
  `--plant ignored-conf`, the same conf named in `.git/info/exclude` does not; and
  `grep -n 'def read_root_confs' ratchet.py` names the function whose docstring states the ignored-conf
  blind spot.
  Red when: an untracked conf is unread, or an ignored conf is measured.
- **AC3** — When `grep -n 'read_root_confs(\|read_tracked_paths(\|ROOT_CONF_RE' ratchet.py` runs in
  `tools/memory-tree/`, `read_root_confs(` appears at its definition and in `read_root_conf_lines`, the
  one conf walk the measures share, `read_tracked_paths(` appears only at its definition and in the
  widen check, and `ROOT_CONF_RE` appears nowhere; and `--plant
  untracked-conf` with no population row for `FOO_PIN` makes `keys-not-scalar` exit 1 naming it.
  Red when: the leg or a measure keeps its own conf list, so the seed and the leg read two sets.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `ratchet selftest` · `ratchet (keys, not a scalar)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

`ratchet selftest`, landed by `TOOL-dWitnessedBar-14` at `25a3d2970`, runs the plants of AC2 and AC3;
`ratchet (keys, not a scalar)` is the leg S2 binds to the seed's read. `lexicon naming predicates`
grades the minted names against `VERB_OFFENDER_PIN`, which this unit leaves where it is; the map and
recall legs read the regenerated `memory/map/generated/symbols.json`.

New arm: tools/memory-tree/ratchet.py · covers AC2 AC3 · the plants `untracked-conf` and `ignored-conf`, staged red by dropping `--others` from `read_root_confs` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-46`'s clause. Unit 46 carries
  none, being itself derived, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Where does AC1's fixture get its scalar pin, once unit 17 drains the example's?** The
  re-ground at `c3884a6b9` read `TOOL-dWitnessedBar-17` S3, which removes every `*_PIN=` line from the
  example conf at this unit's order (§4 Evidence). Options: (a) the fixture's conf is the example plus
  one planted line `FOO_PIN="3"`, and AC1 names the planted row; (b) the fixture relies on the
  example's `ROW_DUPLICATE_PIN`, and the main loop lands this unit before unit 17; (c) the fixture
  plants nothing and asserts whatever pins the example carries. (b) leaves AC1 unobservable whenever
  unit 17 lands first, and rests on an order neither spec declares and this unit's grant cannot write
  into unit 17's; (c) asserts over nothing once unit 17 lands, the empty-population class this unit
  closes. RESOLVED (agent, 2026-11-19, delegated): (a), rung 3, the one option whose AC1 holds in
  either order; `FOO_PIN="3"` is the plant AC2 and unit 14's AC7 already spell.
  widens: none · relaxes: none
- **F3 — Does `read_root_confs` extract a factory shared with the policy kit's root-conf read?** Since
  `cdfbd1cf`, `tools/policy/policy.py#derive_legacy_homes` lists the tracked root confs with the same
  pathspec (§4 Evidence). Options: (a) `read_root_confs` lives in `ratchet.py` and the policy reader is
  left alone; (b) one `read_root_confs(root, untracked)` in `tools/lib/`, inlined into memory-tree and policy
  under a parity row; (c) `ratchet.py` imports the policy kit's reader. The two read different sets by
  design: the policy reader converts committed legacy homes, and this read must see a conf before its
  first commit. So (b) is a flag with one caller per value, which [yagni] refuses, and it widens the
  write set into a kit §3 leaves alone; (c) imports a function returning policy rows rather than a conf
  list, over the tracked set this unit exists to widen. RESOLVED (agent, 2026-11-19, delegated): (a),
  rung 3, the only option meeting S1 to S3 inside this unit's write set. What it does not check: a
  third root-conf reader drifting from both. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 40 to 51, id 1
  (HIGH, item H1, shared with id 13).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the consumes-from bullet mirroring
  TOOL-dWitnessedBar-61's hands-off edge and the hands-off bullet mirroring TOOL-dWitnessedBar-62's
  consumes-from edge, promoted by the round-1 spec audit of units 52 to 57; nothing else moved.
- rev-3 · 2026-11-19 · §1 · §3 · §4 Evidence, Migration, Rollout, Alternatives rejected · AC1 · §8 F2 F3
  · §10 · re-grounded at `c3884a6b9` per brief 2026-11-19-prompt-TOOL-dWitnessedBar-52-reground-brief:
  the adopter and example-conf citations become blob-pinned at their moved lines, and the pin and conf
  counts are re-pinned; unit 46's seed now runs at the end of `--scaffold` and from its `--seed-pins`
  row; AC1's fixture stages the kit, since `read_registrations` reads tracked descriptors only, and
  plants `FOO_PIN` because unit 17 S3 drains the example's pins at this order (F2); the policy kit's
  root-conf read, landed since the base, is left alone (F3).
- rev-4 · 2026-11-19 · S1 · S2 · §4 Evidence, The read, Migration · AC3 · §7 · §10 · re-grounded at
  `578296c1f` by brief 2026-11-19-prompt-TOOL-dWitnessedBar-17-reground-2-brief over unit 14 as landed
  at `25a3d2970`: `root_confs` replaces the conf walk of `measure_scalar_pins`, which the leg and its
  seed already share, so AC3 counts one call where it counted two, and `read_tracked_paths` keeps its
  widen-check caller; `root_confs` sits behind the walk unit 17 shares with `measure-cutoffs`;
  `ratchet selftest` and `ratchet (keys, not a scalar)`, now in the manifest, join the leg line; the
  conf count is re-pinned, unchanged.
- rev-5 · 2026-11-19 · §1 · S1 · §4 Evidence, Migration, Rollout, Alternatives rejected · §10 ·
  re-grounded at `57547e855` by brief 2026-11-19-prompt-TOOL-dWitnessedBar-52-reground-3-brief over
  units 16 and 46 as landed: the adopter, descriptor and example-conf citations re-pinned at their
  moved lines, unit 46's seed cited at `#seed_scalar_pins`, and the defect recorded as probed in AC1's
  fixture; unit 17 builds before this unit, so S1 and the rollout drop "whichever lands first"; the
  pin and conf counts re-pinned, unchanged. No Scope intent or criterion moved.
- rev-6 · 2026-11-19 · S1 · S3 · §3 · §4 Evidence, The read, Inventory, Files touched · AC2 · AC3 · §7 ·
  §8 F3 · §10 · per brief 2026-11-19-prompt-TOOL-dWitnessedBar-52-rename-brief, after the first
  builder's return: the conf read is renamed `read_root_confs`, a name the naming lexicon accepts, and
  restated behind `read_root_conf_lines`, the walk unit 17 landed at `9a29f1e96`; `ROOT_CONF_RE`, whose
  one reader that walk's filter was, is deleted with it and AC3 observes its absence; the plant
  functions join the inventory and `memory/map/generated/symbols.json` joins Files touched, with the
  naming, map and recall legs its guards and the rename name joining the §7 leg line.

## 10. Reuse audit

The seam is the adopter's own working-tree fallback for the `method-carriers.txt` seed
(`tools/memory-tree/adopt-memory-tree.sh@fbbf1499d9a4:824-829`), the one place this repo already met
the tracked-only-seed class, expressed as one `git ls-files` call with `--others --exclude-standard` so
the leg and the seed share it; the call it replaces is the conf filter of
`tools/memory-tree/ratchet.py#read_root_conf_lines`, the walk unit 17 moved out of `#measure_scalar_pins`
at `9a29f1e96`, which the new read sits behind.
`python tools/codebase-map/reuse_lookup.py "seed measure untracked root
conf before first commit"`, re-run at `57547e855`, ranked `before`, `seed` (test helpers), `repo_root`,
`load_conf`, `parse_conf` and `write_commit`; none lists a working tree's root confs. A `git grep` for the pathspec
found `tools/policy/policy.py#derive_legacy_homes`, which lists the tracked root confs for the policy
kit's legacy-home conversion; §8 F3 records why this unit does not share it. No existing seam fits
beyond the adopter's fallback.

Recall terms used: `python tools/memory-recall/query.py "why does an adopter seed read the working tree at scaffold time" --terms "method-carriers seed git ls-files empty scaffold untracked conf vacuous-selector-empty-population adopter first commit"`
