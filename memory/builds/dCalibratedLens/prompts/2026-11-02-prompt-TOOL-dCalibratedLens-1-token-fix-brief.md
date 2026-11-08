**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17

# Token-fix brief — the spec set's 68 spec-token hits at 59d3d8e57

`python tools/check-spec-tokens.py` exits 1 over the committed spec set with 68 unwaived hits. Fix every hit in the
specs under `memory/builds/dCalibratedLens/spec/` and nothing else: no design change, no new scope. These edits
happen before the spec set's first audit, so they are the authoring pass's own corrections: keep each spec at
`rev-1` and write no §9 line for them. Do not commit, and do not run the build-index generator.

1. **`[path]` hits (§6 only).** A backticked path with a slash and an extension inside `## 6. Acceptance criteria`
   is joined against `git ls-files`, and a file the build run will create is not tracked yet. Cite it in §6 by
   BASENAME (`loop_review.py`, `measure.py`, `lenses.toml`, `help`-page basenames too), and keep the full path in
   §2 and §4, which the join does not read. A placeholder path in §6 (`tools/x.py`, `tools/y.py`,
   `tools/x/instructions.toml`, `memory/builds/x/README.md`) becomes a basename or a prose description. A
   Python expression that reads a path (`json.load(open('tools/gate-legs.json'))`) is rewritten so no backticked
   token is path-shaped, e.g. name `gate-legs.json` by basename.
2. **`[bar]` hits** (units 1 and 14 cite `tools/unattended/unattended.test.sh` in §6). A suite is not an acceptance
   observation. Observe the checker on a staged break or a fixture instead, and move the suite to a
   `New arm:` line in §7.
3. **`[handoff]` hits.** A hands-off bullet names a token its sibling's spec never names: unit 13's
   `derive_opt_in_tags` handed to unit 14, and unit 5's `PROPOSERS` and `read_keep_records` handed to unit 14. Make
   unit 14's spec name each token where it uses that sibling's work (§4), or correct the bullet if unit 14 does not
   use it.
4. **`[carries]` stale pins.** Units 8, 10 and 11 each wrote a deviation record amending their clause
   (`memory/builds/dCalibratedLens/build/2026-11-02-build-TOOL-dCalibratedLens-<n>-deviation-<k>.md`), and the as-built
   view `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` now holds the amended
   text. Re-pin each `**Carries:**` line to the hash the checker prints: `cl-dClosedLoop-0465@93c242bb` (unit 8),
   `cl-dClosedLoop-0467@0bd9d49f` (unit 10) and `cl-dClosedLoop-0468@ede533ed` (unit 11). Check that each spec's
   text agrees with its record's `After`, and fix the spec where it does not.

The packet's byte-compare red is the main loop's: it re-renders the packet after you return.

Verify with `python tools/check-spec-tokens.py > <scratch>/tokens.txt 2>&1; echo $?`, where `<scratch>` is your
session scratchpad. Return 0, or list every hit left with the reason it stands. The run takes several minutes on
this host, so run it once after all the edits, not after each.
