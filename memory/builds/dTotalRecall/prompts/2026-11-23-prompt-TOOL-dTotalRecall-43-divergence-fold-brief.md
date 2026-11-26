**Serves:** journal TOOL-dTotalRecall-43
**Caused-by:** TOOL-dTotalRecall-43

# Brief — dTotalRecall: fold TOOL-dTotalRecall-43 rev-7 over its builder's divergence

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 43's builder, dispatched at `f41d86c42`, returned a divergence and
built nothing: `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-43-1-builder-return.md` holds it
whole. Each of its five points is a claim of this spec that HEAD does not bear out.

## The brief

### Goal

Revise unit 43's spec in place as one rev bump, with one revision-log line naming this brief by its file stem, so a
builder can build it as written over HEAD. Read the builder return first and re-derive each of its five points at HEAD
before acting on it.

### Items

1. S19 and AC19: the two ledger homes share the key (`2026-10-20-build-PLAY-dClosedLoop-1-execution.md`, `research`), so
   a merge keyed by (`path`, `section`) marks it duplicate. Decide the fork by M3 and record it in §8: (a) this pass keys
   the merged registration by (`path`, `section`, `check`), taking the triple key from unit 52, or (b) the merge itself
   moves to unit 52, and S19 here keeps only what needs no merge. Whichever survives, make Scope, AC19, Files touched
   (`memory/project/legacy-records.txt`, `.memory-tree.conf`'s PROJECT_REGISTRY_EXTRA, and
   `tools/memory-tree/record_causes.py#POPULATION` if this pass moves it) and §3's hand-off to unit 52 agree. Where the
   pick moves work to unit 52 (DEFERRED), amend that unit's spec only as far as its edge with unit 43 and the clause it
   now inherits, as a rev bump naming this brief.
2. S22 and AC22: `blob_parsed` is keyed (blob, extractor, version) with no path, while `query.py#write_recall_rows`
   extracts per path and recall serves untracked files `query.py#derive_served_pairs` hashes, which the sweep in
   `tag_index.py` deletes. State how path-keyed and untracked pairs are tracked once `fts_blob` goes, or narrow S22 to
   what the ledger can carry and say what stays on `fts_blob`. Add `tools/memory-recall/check-recall.py` to Files
   touched if it still joins `fts_blob` at this pass.
3. S21 and AC21: state the leg reader's registration, its row shape (it is a JSON payload per blob, and `blob_row` has
   no payload column), how its rows stay out of tag queries, and where an optional params digest enters
   `tag_index.py#derive_extractor_versions`; add `tools/playbook/namespaces.toml` to Files touched if the registration
   lands there. Or, if that design cannot be derived from the tree, decide the smaller fork by M3 and record it.
4. S21's Readers line is stale: `tree_lib.py#LEG_READERS`, `#LEG_TABLE`, `#read_rows_at` and `#build_leg_rows` exist
   at HEAD with readers in `gen_build_index.py`, `corpus_ids.py` and `tag_index.py`, and `LEG_READERS` holds a third
   reader, `spec-head` (`design_lib.py#extract_spec_head`). Re-ground the line and name `design_lib.py` in Files touched
   if this pass touches it.
5. Files touched gains every path the revised scope writes; the gates section's leg line names each leg those paths'
   guards trip.
6. A §8 resolution mark is exactly `RESOLVED (agent, 2026-11-23, delegated)`, the brief cited after the mark. Cite code
   as `path#symbol` or blob-pinned; every number carries an id, a path:line, PINNED or DERIVED on its line. Keep the
   spec under 49152 B (PINNED 2026-11-20), tightening prose you touch, never dropping a criterion.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-43 TOOL-dTotalRecall-52`
and `python tools/check-spec-tokens.py --spec <path>` over each spec you edit, and fix every finding they name. Unit 43's
status header keeps `INPROGRESS`; unit 52's keeps `DEFERRED`; do not commit.

### Acceptance

Both commands exit 0; each edited spec carries the next rev and one revision-log line naming this brief; the return
names each of the five points with what the spec now says.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec outside units 43 and 52, and in 52 only what item 1's pick moves.
