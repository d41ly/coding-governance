**Serves:** journal TOOL-dWitnessedBar-62

# TOOL-dWitnessedBar-62 — builder return 1 (run `wf_ae744491-9ae`), committed f6ce71662e7c5c987559db9e9ec0b49a4b9f7900

## Why

TOOL-dWitnessedBar-62 is built from spec rev-5 and committed. I checked every spec claim against the tree first and found nothing that blocks the build, so there is no DIVERGENCE. The pass commit is f6ce71662: it carries the trailer `Pass: TOOL-dWitnessedBar-62` and the only edit to the spec is its status header, now CLOSED dated 2026-11-20. I then ran the bug-class checklist over that commit. It named the inherited-git-dir class, and that applied: the seed-across compare in the hygiene suite read HEAD with a bare `git rev-parse`, which would follow a GIT_DIR inherited from a hook. Commit 7f2b664e8 (`Pass: none`) makes it read HEAD through `legacy_ledger.read_head_sha`. HEAD is now 7f2b664e8.

## Summary

**Built and committed:** pass commit f6ce71662, then 7f2b664e8 (the checklist fix). Base was b82c0f53.

**What changed, by scope item:**
- **S22, S20 (`exists:` containment):** an `exists:` path that resolves to an absolute path or holds a `..` segment is now refused or skipped by all three readers: `tools/run-gates/regen.py#check_when`, selfcheck's `_check_exists_refused` in `tools/govkit/govkit.py`, and `tools/unattended/lib-unattended.sh#resolve_generated_indexes`. They use the same pattern `read_gate_policy` uses. The unattended README paragraph and the reader's header comment now name both `when` forms, the tokens, the refused shapes and the silent skip of an absent path. The run-gates README `when` table names the refusal.
- **S1–S3 (`tools/govkit/selftest.py#check_when_forms_agree`, rewritten):** the four admissible forms are read together; each of the five refused forms sits alone beside one conf-true row; a row with no write/check/stage is printed `not compared`.
- **S37, S38:** `check_inherited_red_step` now cuts `read_policy_key` with the awk range under bash (the AC24 grep prints 1) and gains the AC25 witness fixture. `inherited_red.py`'s witness now names only a line that opens with the key and an `=`.
- **S23, S32:** `tools/memory-tree/ratchet.py#read_root_confs` keeps only regular files and prints `not in the work tree <path>` on stderr, with a new `deleted-conf` plant. The memory-tree README, `HYGIENE.template.md` and `memory/HYGIENE.md` now describe the conf set as the working tree with ignored files excluded.
- **S4–S7, S36 (hygiene suite):** unit 46's and unit 53's arms are now one scaffold. P is the armed lines of the scaffold plus those of a `seed --all` listing run made before the commit. A new fixture registration, `seed-across-fixture`, is compared, and the SHA columns are checked (null before the commit, HEAD after). Floor raised 796 to 797.
- **S13:** the empty-note `quarantine` row is added to the evidence suite (floor 311 to 312) and to both selection loops in `.githooks/pre-push.test.sh`.
- **S39:** `tools/run-gates/verdict_backends.py#read_signer_principal` now creates and unlinks the signer file in one try/finally, and the `peer-no-ssh-keygen` plant asserts no temp is left.
- **S17, S18:** `verdict_flow.py`'s `read_selection` and its two tuples now sit in a `# >>> selection_row` block. `drift_report.py` carries a byte-identical copy, `read_selection_holds` reads through it, and a `selection_row` row was added to PARITY_ROWS. Both READMEs now spell `--selection` on the gate-health calls.
- **S25–S27, S35:** `tools/lib/refuse-wrong-shell.sh` has one widened call reader: elif, while, until, a group's `{` or `(`, a backtick, `$(` followed by whitespace, and no call after a `#`. `resolve-python.test.sh` gains a fixture file per spelling and the seed-home cases inside a linked worktree.
- **Records:** shell-role widened under widen-5 with the six rows set to their measured counts. The codebase map and build index were regenerated. Deviation record 622 covers the stderr line and the folded unit-54 check. The acceptance ledger is written. Paths added beyond the main loop's declaration (the shell-role ledger, the widen record, the deviation record, the dClosedLoop as-built view) were each declared with `--dispatch` before staging.

**Checks that ran, all probes of this unit's own code; no gate, suite or bar ran:**
- `regen.check_when` and the lib-unattended reader over every `when` form in a scratch tree, and selfcheck's predicate cut and run over each form. Stands in for `govkit selftest` and `govkit selfcheck`.
- AC13: the §4 probe printed `86 10 96`, and `--coverage` printed `derived from 96 files` with 93 members. The fixture of five spellings plus one commented line was named exactly as the arm expects. Stands in for `python resolver (behaviour + inline parity + idiom ban)`.
- AC11: the two `selection_row` cuts diff empty; `read_selection_holds` was probed over a scratch selection. AC12: the `--gate-health --fixture differs --selection <empty>` call exited 0. Stand in for `drift-audit selftest` and the parity leg.
- AC15 and AC20: the `ratchet.py --fixture --plant deleted-conf` and `--plant untracked-conf` plants held. Stand in for `memory-hygiene self-test`.
- AC26 and AC16: the `verdict_backends.py` plants `peer-no-ssh-keygen` (prints `signer temps left: 0`) and `clean` held.
- AC18: seeding inside a scratch linked worktree printed `outside the tree` for `.git` and for a nested repo's `.git`, left the gitlink byte-identical, and armed both a relative and an absolute in-tree home.
- The one-scaffold fixture run by hand (scaffold, listing run, save, commit, clear, re-seed, compare) printed `null-then-head` for all four populations, `seed-across-fixture` included.
- AC24 (grep prints 1) and the awk cut under bash reading the sentinel; AC25 witness probe; AC3, AC9, AC14 and AC22 greps.

**Owed to the close (the main loop):**
- **Legs:** `govkit selftest`, `govkit selfcheck`, `memory-hygiene self-test`, `memory hygiene`, `run-gates evidence`, `run-gates gov canary`, `pre-push self-test`, `pre-push bar self-test`, `python resolver (behaviour + inline parity + idiom ban)`, `drift-audit selftest`, `recall floor`, `kit/dogfood doc parity`, `policy fixtures`.
- **Criteria only a leg or the close can observe:** AC5, AC7, AC10, AC19 and AC21; the ledger-line clauses of AC6 and AC12; AC23.
- **RED-first observation of all seven `New arm:` lines:**
  - selftest: lib-unattended's containment case removed.
  - hygiene: P taken from the scaffold's armed lines alone, and `fx/seed.py` reading tracked files only.
  - evidence: the row cut with a TAB-IFS `read`.
  - hook: `selection.<n>` read with `IFS=$'\t'`.
  - verdict_backends: unlink moved out of the `finally`.
  - ratchet: the regular-file test dropped.
  - resolve-python: the inline copy edited.

**One problem the close should expect:** the verdict_backends staged break as §7 words it may not go red. In `peer-no-ssh-keygen`, `git verify-tag` fails by returning a non-zero code, not by raising, so the unlink still runs even when moved out of the `finally`. The plant itself does assert `signer temps left: 0`.

**Not edited:** `run-gates.gov.test.sh` and `adopt-run-gates.test.sh`. No arm of this unit lands there, so their floors stay at 38 and 23 until the close observes them (S10).

**Skipped commands:** none timed out.

Files: C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-62-1-acceptance-ledger.md, C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-62-deviation-622.md, C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-62-widen-5.md
