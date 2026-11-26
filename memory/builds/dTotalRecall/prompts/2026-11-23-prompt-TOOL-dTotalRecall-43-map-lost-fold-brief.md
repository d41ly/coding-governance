**Serves:** journal TOOL-dTotalRecall-43
**Caused-by:** TOOL-dTotalRecall-17

# Brief — dTotalRecall: fold TOOL-dTotalRecall-43 over the map's lost replay

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. TOOL-dTotalRecall-17 closed at `cb97caf03` with the verdict `lose · recall`
(`memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-17-map-replay-verdict.md`), so under its §8 F5 the
run holds units 14, 15 and 26 unbuilt, deferred against owner ask TOOL-dTotalRecall-111.

## The brief

### Goal

Revise unit 43's spec in place as one rev bump, with one revision-log line naming this brief by its file stem, so it no
longer consumes from a held unit and a builder can build the rest of it over HEAD.

### Items

1. Remove the `consumes-from` edges to `TOOL-dTotalRecall-14` and `TOOL-dTotalRecall-26`. Every item, scope line and
   criterion of this spec that writes, reads or observes `gov_map.py`, `gen_atlas.py`, the map's cache or the atlas
   (among them S10, S12, S48, AC10, AC12, AC48 and the cache criterion; re-derive the set by grepping the spec for
   `gov_map`, `gen_atlas`, `atlas` and `TOOL-dTotalRecall-14`/`-26`) moves out of Scope into a non-goal that states it
   rides with the held units under ask TOOL-dTotalRecall-111, its report id named. Keep every other item byte-for-byte
   unless the removal forces a renumbering note; never drop a criterion that does not depend on the held units.
2. The decision is a fork the verdict forces: record it in §8 as `RESOLVED (agent, 2026-11-23, delegated)`, option (a)
   the held-unit items ride with units 14 and 26, against (b) holding all of unit 43 and its 39 dependants, citing this
   brief after the mark. (b) holds 43 units (DERIVED 2026-11-23 over the roster's consumes-from edges) for a
   dependency confined to those items.
3. Units 14 and 26 are DEFERRED: remove from each its `hands-off` bullet to `TOOL-dTotalRecall-43`, as a rev bump with
   one revision-log line naming this brief; those two bullets are your only grant in those specs.
4. A §8 resolution mark has nothing else inside the parentheses (check 12 strips code spans and refuses the rest). Cite
   code as `path#symbol` or blob-pinned, never a bare `path:line`; every number carries an id, a path:line, PINNED or
   DERIVED on its line.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-43 TOOL-dTotalRecall-14 TOOL-dTotalRecall-26`
and `python tools/check-spec-tokens.py --spec <path>` over each spec you edit, and fix every finding they name. Every
status header keeps `DEFERRED`; do not commit.

### Acceptance

Both commands exit 0 for the three specs; unit 43 names no `consumes-from` edge to unit 14 or 26, and each edited spec
carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec outside units 43, 14 and 26, and in 14 and 26 only the one hands-off bullet each.
