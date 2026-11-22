**Serves:** journal TOOL-dWitnessedBar-24

# TOOL-dWitnessedBar-24 — builder return 1 (run `wf_d0af23e9-e5d`), a divergence, nothing committed

## Why

DIVERGENCE: `unattended.sh --dispatch` refused the pass, and its refusal is binding. When I declared two more write paths it ran tools/check-spec-tokens.py over the live tree, and the spec failed: "[guards] `powershell hygiene selftest <- tools/gate-lint/eol_class.py` — §4 files-touched names tools/gate-lint/eol_class.py, which trips the guard of leg 'powershell hygiene selftest', absent from the §7 leg line". Once S12's new leg is in tools/gate-legs.json, its guard `{kit}/` covers every gate-lint path in §4 Files touched. So the §7 Gates leg line must name `powershell hygiene selftest`. At the moment §7 names the new legs only in prose. The spec-writer needs to fold these points in one revision: (DERIVED from the builder's probe)
(1) §7 — add `powershell hygiene selftest` to the leg line. Every other new leg has no guard, so it is not required there.
(2) S14 / §4 — the pending-list edits are wider than S14 says. The leg factory's enforces arm (leg_factory.py#check_enforces) and core.py meta-check both fail a leg that has no `enforces` and no `leg` row in core-pending.txt. AC12 rules out `enforces` on a self-test leg, so the new `powershell hygiene selftest` needs a new `leg` row. That adds a row to a list whose header says it only shrinks; there is a precedent in PLAY-dOrderedCharter-86. Also, once the loop-fed and fork-spent legs carry `practice.portable.launch`, their two `leg` rows are stale and must leave. S14 names only the three practice rows.
(3) Files touched — add tools/govkit/subject-pins.tsv. govkit selfcheck fails a pin file that no longer matches the manifest, and its generator is `govkit.py selfcheck --write`, a gate the builder role cannot run. Say whether tools/run-gates/ceiling-evidence.txt and tools/run-gates/pass-leg-evidence.txt owe rows for the nine new legs.
(4) §4 / AC11 contradict each other. §4 makes every population `direction = "shrink-only"`, and the ledger factory's compare_counts reports a count that fell as a finding under shrink-only. The existing scanner adapters fail on that. But AC11 requires exit 0 when a.sh drops from 10 to 9. The spec should say that the shell-role scan compares with ceiling semantics (a fall is no finding) while its ledger stays shrink-only.
(5) AC9 — the green case's fixture also has to track a `.js` file. scan_bare_bash reports "no tracked *.js file was read" as a hit, so a repository with only guarded `.py` launches exits 1.
(6) §5 says both scanners exit 1 on an empty population "as both scanners already do". sh_hygiene.py actually refuses with exit 2.
(7) §8 F10 does not say whether the moved encoding leg keeps `leg.gov.encoding-posture-text-io-names-its-encoding` or is re-tagged `leg.gate-lint.…` now that it is a gate-lint row.
(8) State which population gov's argv grades for each new mode. I built `. {prefix} skills` for --stdout and --js, as the existing encoding leg does, and `. :!memory/` for --path-literals, --quoting and --shell-role. The ledger seeds measure the same population.

## Summary

Nothing was committed and the worktree is clean at base 85a1c4507. The brief was already recorded, unchanged, at 335861ab2526.

**What happened.** I built the whole unit, then tried to declare two more write paths (tools/govkit/subject-pins.tsv and a deviation record). `--dispatch` refused, because the spec-token checker fails the spec once the new guarded `powershell hygiene selftest` leg is in the manifest. I stopped there and restored every path I had changed or created.

**The built work is saved** in C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/TOOL-dWitnessedBar-24-wip:
- `tracked.patch` holds the diff to 12 files: .gitattributes (four class lines and five merge=rows lines), .memory-tree.conf, the rendered tools/gate-legs.json, tools/gate-lint README.md, encoding_posture.py (--stdout, --js, --measure, 15 new selftest assertions, floor 41), kit.toml (8 new gate_leg rows, pack/enforces on the 5 joined rows, 5 [[ledger]] tables), sh_hygiene.py (--path-literals, --quoting, --shell-role, --measure, 11 new assertions, floor 136), tools/govkit/registry.toml (encoding exempt row removed; floor and bare-bash exempt rows added), tools/lib/python_floor.py (census verb and FLOOR_FEATURES table), tools/lib/resolve-python.test.sh (census arm 1d2), tools/playbook/core-pending.txt, and tools/run-gates/measure_legs.py (--bare-bash). (DERIVED from the builder's probe)
- `untracked.tar` holds tools/gate-lint/eol_class.py and the five seeded homes under memory/project/.

**Probes run on the built code** (stand-ins for the AC observations, none of them a gate):
- AC1: eol_class over a scratch repo exits 1 naming a.py with only `* text=auto`, and 0 once `*.py text eol=lf` is added.
- AC2: on the tree it exits 0 grading 581 files (577 by extension plus 4 shebang hooks), and exits 1 with 224 findings before the class lines. (DERIVED from the builder's probe)
- AC4 and AC5: --stdout and --js are red then green on their planted cases.
- AC6 and AC8: the planted sites are red; the forward-slash path, the comment and the quoted heredoc writing notes.txt are green.
- AC9: red on a bare launch and green on a guarded one, with a .js tracked. The tree reads 0.
- AC10: the 3.99 floor, the syntax error in b.py and `removal 3.15` are each red; the clean case is green. The census over the tree is green, 250 files at 3.15. (DERIVED from the builder's probe)
- AC11: red at 11 lines and for a new file, green at 10 and at 9. (DERIVED from the builder's probe)
- AC12: the AC's own print lists 15 portability legs, and core-pending's `practice.portable.` count is 0. A join probe found no leg missing both enforces and a pending row, and no stale pending row.
- AC13: each of the five `legacy_ledger read` calls exits 0 (56, 5, 4, 52 and 147 rows), and the conf count is 1. (DERIVED from the builder's probe)
- Each in-process arm function returned PASS: eol_class 8, encoding_posture 41, sh_hygiene 136.
- The naming lexicon was asked about every new function name.

The hook refused one probe of mine, `encoding_posture.py --stdout <home> . tools skills`, as the leg itself. Separately, my runs of `sh_hygiene.py --path-literals`, `--quoting` and `--shell-role` against their seeded homes were the new legs' own argv, and those legs belong to the main loop. M6's gotchas checklist did not run because there is no commit.

**Owed at the close, after the spec is revised and this unit is dispatched again:**
- the four `New arm:` RED-first observations: sh_hygiene --selftest, encoding_posture --selftest, eol_class --selftest, and resolve-python.test.sh;
- the §7 legs, plus the nine new legs and `ps-hygiene.py --selftest`, which no probe ran; (DERIVED from the builder's probe)
- the subject-pins regeneration;
- the kickoff manifest re-stamp (gate-legs.json and .memory-tree.conf are both on its watch list), the codebase map, `gen_build_index --write`, and the acceptance ledger.
