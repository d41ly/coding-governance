# TOOL-aRepatriatedFork-28 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-28

Written by the unit pass on node a, 2026-09-30. No merge bar, no self-test runner and no whole suite
ran. Each criterion ran its direct check: a grep, a slice of a suite run inside its own kit dir of a
scratch clone, one arm function of a Python self-test called on its own, or a `--selftest` flag. The
drain itself was checked mechanically before any slice ran. Every edited shell suite, with the
derived prefix read back as gov's, equals its `HEAD` bytes except the lines the spec's rev-3 §4
names. Every edited Python file is AST-identical to `HEAD` at gov's prefix, the prologue aside,
except govkit's fixture respelling and the named edits.

**Evidences:** TOOL-aRepatriatedFork-28
- AC1 — the pattern over `*.test.sh`, `*selftest.py` and this unit's other owned files finds no line outside the three files rev-3 returns: the unattended kit's rendered `playbook.fixture.md` and its two rendered piece records. Before the drain it found 1601 lines in 64 suites alone
- AC2 — `git grep -l 'gov:root-fixture' -- tools skills .githooks` lists `tools/check-install-prefix.sh` and `tools/check-install-prefix.test.sh` only. The 22 other markers are struck, each root-install arm now builds through a prefix variable set empty, and the two `corpus_ids.py` waiver rows are gone
- AC3 — nine kits had the prefix `derive_self_rel` feeds pinned to `wrongpfx/` in a clone of this change, one suite each. In eight the control ran green and the pinned run redded: lib (extract-arms), the loose gates (check-dead-paths), memory-tree (merge-rows), run-gates (the gov canary), codebase-map (adopt-codebase-map, and its JS cross-check arm), workflows (check-review-join), unattended (check-playbook) and govkit (its pytest-ini probe arm). In the ninth, runlog, both host-reading arms print SKIP when pinned, which only the whole suite's floor can red. Two kits were not pinned. Hooks has no host read that depends on the prefix: agent-cap's parity arm finds its subject through git by design, so a pinned prefix stays green. Lexicon's one host read runs at module level, which only a whole-suite run reaches, so its control is owed to the main loop
- AC4 — in a clone with the kits moved to `scripts/`, the arm's own load expression reads 52 rows and 86 pairs. No loaded value names `tools/`, and 132 of the 138 gov-side paths sit under `scripts/`. The other six sit under `skills/`. Red first: `HEAD`'s fixture carried 133 literal `tools/` sources
- AC5 — `git diff 2143b6d6 -G '^(SELFTEST_FLOOR|FLOOR_ASSERTIONS)='` over `tools`, `skills` and `.githooks`, on the staged tree, shows one floor moved since `2143b6d6`, and it rose: `check-memory-hygiene.test.sh` 448 -> 471, by an earlier unit. This change moves none. The executed counts are the main loop's to record, per the criterion's permission clause. `resolve-python.test.sh` is the one suite whose count rises by construction, one parity arm per new inline copy
- AC6 — `bash tools/check-kit-versions.sh` exits 0 with 16 declared carriers. In a clone with the change committed, `govkit.py epoch` is clean for every entry at both `--base f8fdd873` and `--base 2143b6d6`. Seven kits moved in every carrier: check-wiring 1.16, codebase-map 1.17, kickoff-manifest 1.12, memory-tree 2.108, playbook-render 1.15, review-harness and tier2-review 1.19, and unattended 1.45

Other direct checks: nine govkit arm functions ran on their own, 92 arms green, after `check_shipped_verb` and `check_epoch_verb` had been observed red at `HEAD` on seven arms. `render_playbook.py --selftest` passes 22 arms, the same count as before. `check-arms.py --selftest` and `gotchas.py --selftest` pass. `corpus_ids.py --selftest` did not finish inside the pass's 280 s bound, against a declared budget of 1080 s, so it goes to the main loop. The ban list falls from 90 rows and 2391 literals to 56 rows and 625, written by `--write-ratchet`.
