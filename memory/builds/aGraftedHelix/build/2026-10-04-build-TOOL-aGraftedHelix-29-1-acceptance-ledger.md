# Acceptance ledger — TOOL-aGraftedHelix-29

**Serves:** journal TOOL-aGraftedHelix-29

Node `a`, 2026-10-05. The build commit is `d52f0ede`, over the spec's rev-2 commit `f5ee0928`, which
was made before any code after reading the tree at `489f1ec7`. The catalogue's `INDEX.md` re-render
rides the records commit that carries this ledger, because `--dispatch` refused the index declared
beside its generator. No merge bar and no self-test suite ran in this pass. The checker's
`--selftest` ran whole, because it is a flag. The two workflow suites' new arms ran as slices: the
prologue plus the arms' blocks, copied under names that are not `.test.sh`, and every staged break was
a scratch copy, deleted after its run. The whole suites are the main loop's, at VERIFYING.

**Evidences:** TOOL-aGraftedHelix-29
- AC1 — `python tools/memory-tree/gotchas.py --selftest` — at `d52f0ede` printed 52 `arm ok` lines and `PASS — gotchas: all arms held`; the add arm's block is `inv-one`'s line alone with `- [ ] NEW/CHANGED invariant inv-new` before it, and the edit and take-out arms print a head of 0 with `inv-one`'s item.
- AC1 — `arm FAIL` — the parent's `gotchas.py` from `f5ee0928`, with the twelve new arms grafted in before its summary, ran inside the kit dir under a non-test name: its 40 old arms read `arm ok` and all 12 new arms read `arm FAIL`, the three AC1 arms among them.
- AC2 — `inv-side` — the same two runs: the uncommitted `## Actually` edit, the three-dot side branch, the base with no `memory/gotchas/` directory and the unparseable base record each read `arm ok` at `d52f0ede` and `arm FAIL` on the grafted parent.
- AC2 — `arm FAIL` — a scratch copy of the built checker with the three-dot branch made to read the left side read `arm FAIL` on the three-dot arm alone, with the other 51 arms `arm ok`.
- AC3 — `INVARIANTS_UNPINNED` — the pinned `cmd_for_paths` arm over an uncommitted `inv-new`, the unpinned header arm, and the `--for-paths --base` usage arm each read `arm ok` at `d52f0ede` and `arm FAIL` on the grafted parent.
- AC4 — `python tools/memory-tree/gotchas.py --for-diff nosuchrev..HEAD` — at `d52f0ede` exited 1 with stdout opening `HYGIENE gotchas: git diff cannot read the range`, and neither stream carried `Traceback`; at `f5ee0928` it printed a traceback.
- AC4 — `python tools/memory-tree/gotchas.py --for-diff --stat` — exited 1 with `HYGIENE gotchas: '--stat' opens with '-', which git would read as an option` and no diffstat; the two `--selftest` arms, the second aiming `--output=` at a fixture file that does not exist afterwards, read `arm FAIL` on the grafted parent.
- AC5 — `INVARIANTS_AT_BASE` — the command over `c3ef67429fef..a49d53d5` at `d52f0ede` printed `# invariants are read at c3ef67429fef; 3 that ...`, three `NEW/CHANGED invariant` items naming `canary-waits-on-a-rendezvous-not-a-clock`, `concurrent-runs-are-announced-not-refused` and `sweep-issues-no-cost-verdict`, and `# by design — 0 invariant(s) this selection touches`, where `f5ee0928` printed a head of 3.
- AC6 — `--base 018b5675` — the pinned command printed a block of 1 naming `concurrent-runs-are-announced-not-refused` and 0 `NEW/CHANGED invariant` lines; without `--base` it printed the `INVARIANTS_UNPINNED` line and the same block.
- AC7 — `FLOOR_ASSERTIONS` — the build-harness suite's prologue, the `NOSUBJ` fixture and the GH3 block with the 7 new GH29 sites ran as a slice inside the kit dir: 17 arms, exit 0; the floor rose 495 to 502, counted as 619 static sites at the parent and 626 after.
- AC7 — `--base` — on scratch copies of `tools/workflows/unattended-build.js`, the forward cut redded the pinned prompt arm, the cut `at base` suffix redded the log arm, a deleted `WARNING:` redded both warning arms, an unconditional one redded the no-warning arm, a dropped shape test redded the `origin/main` arms, and an unconditional forward redded the unpinned-command arm.
- AC8 — `by-design: 1 invariant(s) from the checklist's by-design block` — the review suite's prologue, its runner's helpers and the new block ran as a slice: the real checker ran over the fixture range, and the four new assertions read `ok`, `bd-base` under the intended-behaviour label in every lens prompt, no prompt carrying `bd-new`'s ruling, and one lens sweeping `NEW/CHANGED invariant bd-new`.
- AC8 — `MEMORY_TREE_DIR` — pointed at a scratch directory holding the parent's `gotchas.py` and `tree_lib.py`, the slice's three harness assertions read `FAIL`; pointed at a directory that does not exist, the producer assertion read `FAIL` naming why and the harness run refused. The floor rose 246 to 250.
- AC9 — `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` — with `--base f5ee0928` it printed `memory-tree · clean · 2.129` and `review-harness · clean · 1.37`; `bash tools/check-kit-versions.sh` printed `kit-versions: clean`, and line 3 of `tools/workflows/unattended-build.js` reads `unattended-build@1.8`, one minor step above 1.7.
- AC9 — `bash skills/session-kickoff/manifest-check.sh` — exited 0 at `d52f0ede`, and the diff of `memory/guides/BUILD-METHOD.md` from `f5ee0928` changes line 1 only, the version marker.
- AC10 — `python tools/memory-tree/gotchas.py --check` — exited 0 with the re-rendered index; `python tools/memory-tree/gotchas.py --for-paths tools/memory-tree/gotchas.py` printed `- [ ] inputs-inside-the-subjects-reach`, which the record at `018b5675` could not select, its only anchors being `tools/unattended/check-unattended.sh` and `second-implementation-is-not-a-second-opinion.md`.
- AC10 — `It is never a checklist item` — counted 0 in `memory/HYGIENE.md`; `NEW/CHANGED invariant` counted 2, 1 and 2 in the memory-tree README, `memory/HYGIENE.md` and the workflows README, and every line of `python tools/codebase-map/test_codebase_map.py` read `ok` after `gen_map.py --write`.
