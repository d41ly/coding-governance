# TOOL-dWitnessedBar-7 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-7

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon's `--suggest`
and the command factory's own `loop command conformance` run excepted. The criteria were observed on
node d, 2026-11-20, at base `8614bf41c`, by `seen_red.py --fixture` over its five scratch
repositories, by the ratchet plant `populated-seen-red` called in process over a scratch repository,
by the new memory-hygiene self-test block extracted into a scratch script with `hit` and the counters
stubbed, by check 23's ledger awk extracted from the engine and run over a scratch ledger, and by
`grep` and `wc -c` over the edited files. The suites themselves were not run: the `New arm:` lines of
spec section 7, in `check-memory-hygiene.test.sh` and `ratchet.py --fixture`, their RED-first
observations and the legs of §7 are owed to the main loop at the close.

**Evidences:** TOOL-dWitnessedBar-7
- AC1 — `python seen_red.py --fixture --plant seen` in `tools/memory-tree/` exited 0 printing
  `seen-red: fix added leg · 062c715e · memory/builds/dFix/build/2026-01-01-build-TOOL-dFix-1-1-acceptance-ledger.md`.
- AC2 — `python seen_red.py --fixture --plant unseen-gate` exited 1 printing
  `seen-red: fix added leg · NO RECORD`, the leg the plant added past its base.
- AC3 — `python seen_red.py --fixture --plant unseen-arm` exited 1 printing
  `seen-red: fix base leg · NO RECORD`, the leg whose `argv` holds the spec's `New arm:` suite path.
- AC4 — `python seen_red.py --fixture --plant empty` exited 0 printing
  `seen-red: dFix adds or changes no gate · nothing joined`, its `adds or changes no gate` line.
- AC5 — `python deviation_join.py --fixture --plant amended` in `tools/memory-tree/` printed the same
  bytes before and after S2 (`cmp` silent, its ledger arm's `amended rev-3` line among them); check 23's
  awk over a scratch ledger whose `AC1` answer `zulu.py` is followed by a seen-red line naming
  `alpha.sh` emitted the answer's tokens as `zulu.py` alone, and the same line read as a continuation
  joined `alpha.sh` to it.
- AC6 — `python seen_red.py --fixture --plant bad-line` exited 2 naming
  `memory/builds/dFix/build/2026-01-01-build-TOOL-dFix-1-1-acceptance-ledger.md:7` and the line.
- AC7 — `grep -n 'seen-red' memory/guides/BUILD-METHOD.md memory/HYGIENE.md` showed M8's sentence and
  the "Acceptance ledger" section's grammar; `grep -n 'seen-red' tools/memory-tree/kit.toml` the
  `seen-red` command row the factory wrote; `grep -n 'command:memory-tree.seen-red' tools/loop/loop.toml`
  the item's actor, `command:test.seen-red` gone; `wc -c memory/guides/BUILD-METHOD.md` printed 30717
  against the 30720 row.
- AC8 — `python ratchet.py --fixture --plant populated-seen-red`'s plant, run in process from
  `tools/memory-tree/`, held all three: `admitted` with exit 0 while the line names the leg, `empty`
  with exit 1 once removed, and exit 2 naming the record once its red SHA is dropped; the
  `populated-empty-armed` plant kept its exit 1.
