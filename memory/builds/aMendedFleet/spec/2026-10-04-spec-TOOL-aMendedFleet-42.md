# TOOL-aMendedFleet-42 — the reuse probe counts canonical-copy install sites beside fan-in

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 42

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The most-installed helper in this tree is `resolve_kit_dir`: 66 tracked files carry its
canonical-copy marker, and the reuse probe prints it at "fan-in 3". `fan_in` subtracts every file
that DEFINES a symbol, and an inlined copy defines it, so the more widely a helper is installed the
less used it looks. This unit counts each file carrying a `# >>> <name>` canonical-copy marker as an
install site, prints that count beside fan-in, and lets it make a symbol a seam, in the lookup and
in the affordance worklist alike, so a seam means one thing in both.

## 2. Scope (IN)

- **S1** — `tools/codebase-map/map_lib.py` gains `scan_install_sites(root)`, which runs one `git grep`
  over the tracked tree for lines opening a canonical-copy block, `#` or `//` then `>>>` then a name,
  and returns each name mapped to the set of files carrying it. The file whose basename the marker
  itself names after `canonical copy:` is the source, not an install, and is left out. The call names
  `encoding="utf-8"`. With no git, or git failing, it returns no mapping and the reason. Observed by
  AC1 and AC3.
- **S2** — `load_corpus` in `tools/codebase-map/reuse_lookup.py` reads the install sites once into the
  `Corpus`; `Ranked` gains `installs`; `_rank` sets it from the corpus and marks a candidate a seam
  when fan-in plus installs reaches the threshold; `_line` prints `installs <n>` after `fan-in <n>`
  when n is above zero. `_derive_shortlist_key` is NOT changed, so the shortlist order is
  unchanged. Observed by AC1 and AC2.
- **S3** — `seed_affordances` scores a candidate by fan-in plus installs with the same threshold, and
  `tools/codebase-map/gen_map.py --seed-affordances` prints the installs beside the fan-in it already
  prints. Observed by AC4.
- **S4** — The lookup header gains one line: `# install sites: <files> canonical-copy marker file(s)
  over <names> name(s)`, or `# install sites: none found` with the reason when the scan returned no
  mapping, so an empty count is never silent. The header's disclaimer adds that an install count is a
  count of inlined copies. Observed by AC1 and AC3.
- **S5** — The `reuse_lookup.py` row of `tools/codebase-map/README.md` and the `codebase-map`
  dossier's text on fan-in name install sites. Observed by AC5.

## 3. Non-goals (OUT)

- Changing the shortlist ORDER. It is what `replay-phrases.py` grades, and unit 41's floor is the
  check; §8 F2 records why ordering stays on fan-in.
- Changing `fan_in` itself, whose callers and selftest pin its meaning as a reference count.
- What `map_imports.py` becomes, and a join from gate legs to the paths they exercise. §8 F1 moves
  them to `TOOL-aMendedFleet-88` and `TOOL-aMendedFleet-87`.
- The fan-in noise `TOOL-aScouredKit-16` measures. Install sites are counted from a fixed marker
  grammar, not from name tokens, and add no noise of that kind; the ask stays open.
- The codebase-map kit version bump, owed once at the build's close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-41` — AC2 runs that unit's `--floor`; without it there is no
  recorded reading to show the order unchanged against.
- **consumes-from** `TOOL-aMendedFleet-36` — AC1 and AC3 pass that unit's `--budget 0`, so the byte
  budget cuts no candidate line they read.
- **hands-off** `TOOL-aMendedFleet-87` — the legs-to-paths join F1 moves there.
- **hands-off** `TOOL-aMendedFleet-88` — `map_imports.py`'s disposition F1 moves there, deletion.
- **hands-off** external — the kit version bump at the close.

## 4. Design

### Evidence

Read at base `7af5f564` and re-run at `fee9f62ba`, byte-equal for every file below.

- `python tools/codebase-map/reuse_lookup.py "find a sibling kit directory through the install
  receipt"` prints `resolve_kit_dir` with sixteen definer files and `fan-in 3`.
- `git grep -l` for a column-0 `# >>> resolve_kit_dir` line lists 66 files: 17 Python, 48 shell and
  one hook. One of them, `tools/lib/resolve_kit_dir.py`, is the source its own marker names. Across
  every marker name the tree carries eight: `resolve_kit_dir`, `resolve_python`, `derive_self_rel`,
  `resolve_prefix_token`, `resolve_prefix_sh`, `render_doc`, `derive_kit_paths` and
  `kickoff_region`. Figures PINNED as read on node a; AC1 re-derives the one it states.
- `fan_in` subtracts every definer from the referencing set, so each Python copy of the helper is
  removed from its own count.
- The shell copies sit inside heredocs and are not symbol definitions in any layer, so only a marker
  scan sees them; the reference index reads covered-layer extensions only and cannot.

### Inventory

| Name | Kind | Cell |
|---|---|---|
| `scan_install_sites` | function in `map_lib.py` | `py.function`; `--suggest` answered OK |
| `installs` | field of `Ranked` and of `Corpus` | none |

### Files touched (estimate)

- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/reuse_lookup.py`
- `tools/codebase-map/gen_map.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/README.md`
- `memory/map/features/codebase-map.md`

### Alternatives rejected

- **Adding installs inside `fan_in`.** One number would then mean two things, and the probe's header
  says fan-in counts name tokens; a reader could no longer tell a used helper from a copied one.
- **Counting only Python definers that carry a marker.** It misses the 48 shell carriers, which are
  most of the installs.
- **Scanning the reference index's files instead of the tracked tree.** The index reads covered-layer
  extensions only, so it cannot see the shell carriers either.

## 5. Production-readiness checklist

- security — N/A — a read-only scan of tracked text.
- perf / scale — one `git grep` per lookup, measured at 0.14 seconds over this tree.
- error / empty / loading states — no git or a failing scan prints `install sites: none found` and
  the reason, and every candidate shows fan-in alone, as today.
- observability — the header line states the scan's own totals on every run.
- risks — a record that quotes a marker at column 0 counts as an install; none does today, and the
  header's totals make a jump visible. Candidate lines grow by a few bytes, which unit 36's budget
  charges, so AC2 reruns the floor.
- testing — a fixture arm in the kit selftest at the close, declared in §7; AC1 to AC5 run directly.
- migration — N/A — the lookup log's fields are unchanged.
- user docs — S5.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/reuse_lookup.py "find a sibling kit directory through the
  install receipt" --budget 0` runs after the unit's commit, the `resolve_kit_dir` line carries `fan-in 3`,
  `installs <n>` and `SEAM`, where n is one less than the count of files
  `git grep -l -E "^[[:space:]]*# >>> resolve_kit_dir"` prints; and the header carries an
  `install sites:` line with non-zero totals.
  Red when: the canonical source is counted, a shell carrier is missed, or the header line is absent.
  figure: DERIVED from the grep at observation; 65 at writing.
- **AC2** — When `python tools/codebase-map/replay-phrases.py --floor` runs after the unit's commit,
  it exits 0.
  Red when: the install bit moved the order, or pushed a hit past the byte budget.
- **AC3** — When a scratch clone under the TEMP root rewrites every canonical-copy opening marker
  line to drop one `>`, the AC1 lookup in it prints `install sites: none found` and no candidate line carries
  an `installs` bit.
  Red when: an empty scan is silent, or a stale count survives it.
- **AC4** — When `python tools/codebase-map/gen_map.py --seed-affordances --top 50` runs after the
  unit's commit, a `resolve_kit_dir` line appears carrying its installs, or `git grep -n "seam:
  resolve_kit_dir" -- memory/map` shows a dossier already declares it.
  Red when: the worklist and the lookup disagree about whether the helper is a seam.
- **AC5** — When `git grep -n -i "install site" -- tools/codebase-map/README.md
  memory/map/features/codebase-map.md` runs after the unit's commit, it hits both files.
  Red when: either document still describes fan-in as the only count.

## 7. Gates

`codebase-map coverage + freshness` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `kit epoch (shipped bytes move, the version moves)` · `encoding posture (text IO names its encoding)` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/codebase-map/selftest.py · a fixture tree with two carriers of one marker and its named source, asserting two installs and the source left out, staged red by counting the source · none

## 8. Open questions

- **F1 — The brief puts three things in this point: install sites in fan-in, a join from gate legs
  to paths, and a consumer for `map_imports.py` or its deletion. Is that one mechanism?**
  It is three. The join is a new query, and the module's fate is a deletion or a new caller, each
  with its own readers. Measured for the third at writing: no tracked file imports the module except
  the kit selftest; its rescue named a variant harness as consumer, and `rank_harness.py`, which that
  build shipped, does not import it; and the selftest's parity arm now skips because the lexicon kit
  no longer carries the original. Deletion is the recommendation the new unit inherits.
  RESOLVED (agent, 2026-10-04, delegated): split — the legs-to-paths join and the `map_imports.py`
  disposition move to new units the run adds, `TOOL-aMendedFleet-87` and `TOOL-aMendedFleet-88`;
  this unit keeps the install count.
- **F2 — Does the install count enter the shortlist order?**
  Options: display and seam status only; the ordering key too. The ordering is what unit 41's floor
  grades, and raising eight heavily installed names in every query whose stems they share is a
  ranking change this spec cannot price without building it.
  RESOLVED (agent, 2026-10-04, delegated): display and seam status only. Moving the order is a
  ranking change for a later unit, measured by the floor before it lands.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#46], `fan_in`, `seed_affordances`
  and a census of canonical-copy markers at base.
- rev-2 · 2026-10-04 · §3 §8 AC1 AC3 · the M2 cross-read: the two split halves named `external` and
  "units the run adds" while `TOOL-aMendedFleet-87` and `TOOL-aMendedFleet-88` exist in this build,
  so the Non-goal, Edges and F1 name them; and AC1 read one candidate line at the default byte budget
  `TOOL-aMendedFleet-36` lands first, which can cut it, so AC1, and AC3 through it, pass `--budget 0`.

## 10. Reuse audit

The seams extended are `load_corpus`, `_rank`, `_line` and `seed_affordances` in
`tools/codebase-map/reuse_lookup.py`; the marker grammar read is the one
`tools/lib/resolve-python.test.sh` extracts blocks by, `# >>> <name>` opening and `# <<< <name>`
closing, and S1 reads only the opening line. `python tools/codebase-map/reuse_lookup.py "count the
files carrying an inlined canonical copy of a helper"` returned name-stem neighbours,
`corpus_files`, `tracked_files` and `canonical_ctx` among them, none of which reads a marker; the
probe printed `unscanned layers: .sh`, and the shell seam it cannot see is that parity suite's `git grep -l`, which this unit cannot call from a kit and
reproduces as one subprocess. `derive_present_layers` in `map_lib.py` is the existing precedent for a
`git` subprocess inside the kit's library. The recall probe returned the marker grammar's own record
and the synthesis point, and no prior unit counting installs. Where the report and the tree disagree:
nowhere; "fan-in 3" reproduces at base.

Recall terms used: `python tools/memory-recall/query.py "does fan-in count the canonical copies of an
inlined helper as uses, and who consumes map_imports" --terms "fan_in canonical copy marker install
site resolve_kit_dir byte-identical inlined helper map_imports resolve_import consumer seam
threshold"`
