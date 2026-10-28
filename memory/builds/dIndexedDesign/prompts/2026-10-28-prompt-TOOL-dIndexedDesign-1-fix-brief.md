**Serves:** research TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20

# Fix brief — dIndexedDesign, the spec set's check findings and unit 8's second part, before the first commit

The SPEC stage of `unattended-build.js` run `wf_00a5e0cc-c48` authored all 16 specs under
`memory/builds/dIndexedDesign/spec/`, and its commit stage was refused on an unrelated README change. The main loop
then ran the memory hygiene gate, `tools/check-spec-tokens.py` and the carries join over the set: 15 of 16 clauses are
carried whole, `cl-dClosedLoop-0390` is carried as part 1/2 only, and six owned nodes are unnamed. The findings below
are the whole remainder. Two jobs, in this order:

1. **Fix each finding** in the file it names, and nothing else. The specs are uncommitted rev-1 drafts: edit them in
   place, with no rev bump and no §9 line, because no revision of them has been committed or reviewed yet.
2. **Author `TOOL-dIndexedDesign-20`**, the unit the main loop added (`--rescope --act add`, recorded in
   `memory/builds/dIndexedDesign/RUN.md`) to carry part 2/2 of `cl-dClosedLoop-0390`.

Do not commit, and do not run the build-index generator. Read
`memory/builds/dIndexedDesign/prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md` "Every spec" and "What
the last spec runs had to fix" first; each finding below breaks one of its rules, and unit 20 follows all of them.

## Hygiene check 12 — TOOL-dIndexedDesign-15

1. `2026-10-28-spec-TOOL-dIndexedDesign-15.md` carries an unfilled skeleton placeholder. Find it (a template
   placeholder left as written, such as an angle-bracketed template instruction or `TBD`), and fill or delete it.

## check-spec-tokens — paths

2. `TOOL-dIndexedDesign-11` cites `tools/unattended/lib-unattended.sh;` with the semicolon inside the backticks; the
   checker reads it as an untracked path. Move the semicolon outside.
3. `TOOL-dIndexedDesign-2` cites the example paths `src/x.sh` and `src/y/z.sh` in backticks (eleven times); the checker
   reads each as an untracked path. Spell the examples so they are not path-shaped tokens (for example `<path-a>` and
   `<dir>/<path-b>`), or use real tracked paths.

## check-spec-tokens — a suite named as an acceptance observation

4. `TOOL-dIndexedDesign-9` names `marker-contract.test.sh` and `bash tools/memory-tree/marker-contract.test.sh` in an
   acceptance criterion, and `TOOL-dIndexedDesign-16` names `marker-contract.test.sh`,
   `bash tools/workflows/tier2-review.test.sh` and `unattended-build.test.sh`. A suite is never an acceptance
   observation: observe the checker on a staged break, a `--selftest` flag or a fixture of the unit's own code, and put
   the suite arm on a `New arm:` line in §7.

## check-spec-tokens — guarded legs absent from the §7 leg line

5. Each path below in the spec's §4 Files touched trips a merge-bar leg's guard, and the spec's §7 leg line does not
   name that leg. Add each leg, spelled exactly as quoted, to that spec's §7 leg line:
   - `TOOL-dIndexedDesign-9`: `routed-commits selftest` (`lib-unattended.sh`), `pre-push run-log line` and
     `run-gates run-log line` (`tools/runlog/model.py`), `verifier fan-out self-test` and `review-join self-test`
     (`review_replay.py`), `codebase-map gate coverage` and `codebase-map adopter e2e` (`replay-phrases.py`),
     `policy fixtures` (`design_lib.py`).
   - `TOOL-dIndexedDesign-12`: `policy fixtures` (`design_lib.py`).
   - `TOOL-dIndexedDesign-16`: `verifier fan-out self-test` and `review-join self-test` (`tier2-review.template.js`).

## check-spec-tokens — hand-off tokens the target never names

6. Each bullet hands a token to a sibling whose spec never names it. Name the token, in backticks, in the target's
   spec where it reads it (its §3 `consumes-from` bullet and the scope item that uses it), or correct the bullet:
   - `TOOL-dIndexedDesign-12` → `TOOL-dIndexedDesign-13`: `derive_tag_bundles`.
   - `TOOL-dIndexedDesign-16` → `TOOL-dIndexedDesign-1`: `coverage-lens` (unit 16's note: `ready-plus-audit` must not
     count a `coverage-lens` record as an audit).
   - `TOOL-dIndexedDesign-16` → `TOOL-dIndexedDesign-3`: `with-spec-audit`.
   - `TOOL-dIndexedDesign-7` → `TOOL-dIndexedDesign-8`: `### Interfaces`.

## The carries join — unit 8's part 2/2

7. Author `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-20.md`, H1
   `# TOOL-dIndexedDesign-20 — <title>`, status header
   `**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 9 ·
   advances TOOL-dIndexedDesign-17`. It carries `cl-dClosedLoop-0390@a096f77c part 2/2` and the six nodes unit 8's
   spec handed on: `node:item.design.input`, `node:item.design.reentry`, `node:item.design.inventory`,
   `node:policy-key.design.reentry`, `node:record-kind.diff`, `node:record-kind.inventory`. Its scope is what unit 8's
   §8 F1 names as part 2: two-level re-entry by `design.reentry` (its set values, never empty, each read through I3
   and each value seen on a planted case), the additive-versus-breaking interface classification as the diff record
   (nearest seam PLAY-dOrderedCharter-36 S5's widening classifier), the `design.input` item routing an input by its
   kind (flow-steps:235), and gap-flow-25's re-design inventory of completed work (`design.inventory`, flow-steps:237:
   each completed unit kept, amended by a new unit, or retired, with its reason). The clause's tokens `design.forks`
   and `design.reentry` both appear in backticks. Read unit 8's spec whole first, and scout C's row 8
   (`memory/builds/dIndexedDesign/build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-c.md`).
8. Make unit 8 and unit 20 agree: unit 8's `external` hand-off bullet for part 2 becomes a `hands-off`
   `TOOL-dIndexedDesign-20` naming `read_feature_designs`, and unit 20 declares the `consumes-from` back. Unit 20 also
   declares `consumes-from TOOL-dIndexedDesign-16` naming `read_design_policy` and `consumes-from
   TOOL-dIndexedDesign-9` naming `read_spec_section` where it reads them; add each matching `hands-off` bullet to unit
   16's and unit 9's §3. Every edge runs from an earlier order to a later one; unit 20's order is 9.
9. Both unit 8 and unit 20 write `tools/loop/loop.toml` rows; unit 13 (also order 9) adds an `upstream` to unit 8's
   `item.design.decompose` row. Name the shared file in each spec's §2 so the build run sequences them.

When done, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` against a private copy of the git
index in your scratch path (untracked specs are never graded in the worktree itself), and return: each finding fixed,
by number, with the file and the change; unit 20's path, its scope items and its forks; and any edge another spec
must still declare.
