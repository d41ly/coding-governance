# Acceptance ledger — TOOL-aGraftedHelix-3

**Serves:** journal TOOL-aGraftedHelix-3

Node `a`, 2026-10-05. The build commit is `56321bcf`, over the spec's rev-3 commit `ebfed9a2`, which
moved the unattended seed's claim to the unattended-mandate dossier before any code. The catalogue's
`INDEX.md` re-render and this ledger ride the records commit after the build commit: `--dispatch`
refused the index beside its generator, and `--check-commit` could not subtract it under the hook's
`GIT_DIR`. No merge bar and no self-test suite ran in this pass. The gotchas self-test ran whole,
because it is a `--selftest` flag. The three suites' new arms ran as slices under their kit dirs,
behind each suite's prologue, and every arm was observed RED against a staged copy of the code it
reads, each copy deleted after its run.

**Evidences:** TOOL-aGraftedHelix-3
- AC1 — `python tools/memory-tree/gotchas.py --for-paths tools/run-gates/run-gates.test.sh` — at the
  build commit its stdout ended with `# by design — 1 invariant(s) this selection touches` and one
  `- canary-waits-on-a-rendezvous-not-a-clock — …` line ending `(TOOL-cSteadyMetronome-1)`.
- AC2 — `python tools/memory-tree/gotchas.py --selftest` — printed `PASS — gotchas: all arms held`
  with 15 new arm lines: the clean invariant, the block on a hit, the `0` header on a miss, the item exclusion, the
  blank-key and absent-grammar announcements at exit 0, a fixture `LEG_MANIFEST` leg name resolving,
  the seven reds (decision, section, guard path, leg name, unanchored, `universal`, anchored only on
  the decision log) and the missing-manifest process printing one `HYGIENE` line and no traceback.
  Twelve staged copies each disabled one predicate, `inert_only()` included, and each target arm
  printed `arm FAIL`.
- AC3 — `python tools/memory-tree/gotchas.py --check` — with the sweep seed's `decision:` set to its
  ruling's id at sequence 99, an id no record defines (spelled here only in prose, so this ledger
  does not define it), it exited 1 printing one `HYGIENE check 18` line naming
  `memory/gotchas/sweep-issues-no-cost-verdict.md`, that id and `which no record in this corpus defines`;
  restored, it exited 0. With `LEG_MANIFEST` blanked in `.memory-tree.conf` it exited 0 and printed
  one `NOT resolved — LEG_MANIFEST is blank` line for each leg-name guard, `run-gates canary` and
  `run-selftests self-test`. The engine arm at `tools/memory-tree/check-memory-hygiene.sh:2461` ran as
  a slice of the memory-hygiene self-test: green, then red against an engine copy with the green-run
  print deleted; the whole suite is the main loop's at VERIFYING.
- AC4 — `PYTHONUTF8=0 PYTHONIOENCODING=cp1252 python tools/memory-tree/gotchas.py --for-paths tools/run-gates/run-gates.test.sh`
  — exited 0 and its stdout decoded as UTF-8 carried `→`; a copy with the stdout reconfigure removed
  exited 1 with `UnicodeEncodeError` on stderr.
- AC5 — `python tools/memory-tree/gotchas.py --report` — printed `invariants       : 3`, and
  `memory/gotchas/INDEX.md`'s summary line reads `97 record(s): 94 class, 0 note, 3 invariant, 0 superseded`;
  `python tools/memory-tree/gotchas.py --check` exited 0 over the rendered index.
- AC6 — `node` — a scratch probe over the rendered `tools/workflows/tier2-review.js`, with AC1's
  stdout as `checklist`, logged `by-design: 1 invariant(s) from the checklist's by-design block`, put
  the seed in no parsed item, and its synthesis prompt's RUN INTEGRITY slice carried the matching
  `By design:` clause. With `byDesign: 'x'` it logged both sources, every lens prompt carried `x`
  and the seed's entry under their two labels, and the clause read
  `By design: the caller's byDesign; 1 invariant(s) from the checklist's by-design block.` A head
  claiming 2 refused before any agent naming 2 and 1, and a header-only remainder parsed zero items.
- AC7 — `git status --porcelain tools/workflows/` — printed nothing after the renderer's `--render`
  mode ran at the build commit; the six harness arms ran as a slice, green, and red against staged
  render copies: extraction disabled, the clause deleted, the caller's value replacing the block, the
  count check disabled and the header-only refusal restored.
- AC8 — `node` — the build-harness slice over the rendered `tools/workflows/unattended-build.js`, with
  a stub resolver returning a `checklist`, recorded spec-audit args carrying it; with the field
  absent it logged the `WARNING:` line and passed no `checklist` key; beside a caller `checklist` the
  audit received the caller's. The resolver prompt names `gotchas.py --for-paths` through the
  rendered memory-tree path and `### Files touched`. Each of the four was red against a staged copy.
- AC9 — `python tools/memory-tree/gotchas.py --report` — listed 3 `invariant` rows; each seed's
  `git grep` from §4 re-run at the build commit printed: `tools/run-gates/run-gates.test.sh:480`,
  `tools/run-gates/run-selftests.sh:603` and `:854`, and `tools/unattended/unattended.sh:2523`.
- AC10 — `python tools/codebase-map/test_codebase_map.py` — every line read `ok`, six tests, after
  `gen_map.py --write` re-rendered `generated/`.
- AC11 — `grep -c "kind: invariant" memory/HYGIENE.md tools/memory-tree/README.md` — counted 2 and 1;
  the `by design —` grep over the workflows README counted 1; the `supplied by no caller anywhere in the tree`
  grep over the harness render counted 0; and `grep -n '^LEG_MANIFEST=""' tools/memory-tree/.memory-tree.conf.example`
  printed line 258.
- AC12 — `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` — with `ebfed9a21` it
  printed `epoch: memory-tree · clean · 2.119` and `epoch: review-harness · clean · 1.29`;
  `git diff <the pass's parent sha> -- memory/guides/BUILD-METHOD.md` changed line 1 only, `2.118` to
  `2.119`. `bash skills/session-kickoff/manifest-check.sh` reds check 9 at the build commit, a body
  unchanged across ten watched commits; the records commit carrying this ledger revises the body,
  advances `last-body-change` to the build commit, and the check exits 0 over its staged tree.

The suite-only observations, left to the main loop's run at VERIFYING: the memory-hygiene self-test
with its new green-run arm, the harness self-test at its floor of 186 and the build-harness self-test
at its floor of 301.
