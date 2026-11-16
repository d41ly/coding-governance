**Serves:** journal TOOL-dDeclaredLoop-56

# Builder return — TOOL-dDeclaredLoop-56, dispatch 1: dispatch check 49 refused: the spec consumes from unit 70, which builds after it

## Why

DIVERGENCE: the --dispatch refused this pass, and a refusal is binding. The spec needs revising in §3 Edges and §4 Dependency.

1. Binding refusal. `bash tools/unattended/unattended.sh --dispatch dDeclaredLoop --pass TOOL-dDeclaredLoop-56 --writes ...` (39 paths) printed: `UNATTENDED check 49 FAILED — --dispatch declares a build pass for a unit whose spec consumes from a unit of its own build that is neither CLOSED nor WONTDO, so the consumer would build against code its producer has not landed: TOOL-dDeclaredLoop-56 consumes-from TOOL-dDeclaredLoop-70 (DEFERRED)`.
   - The cause is the last bullet of §3 Edges, `consumes-from TOOL-dDeclaredLoop-70 — the shared adopter-phase population, which S18's derive_phase_position call takes by passing no explicit extra`.
   - Unit 70 is DEFERRED at rev-3 and builds after this unit. Its spec mirrors the edge as `hands-off TOOL-dDeclaredLoop-56` and says unit 70 writes `tree=root` onto this unit's call.
   - Since 70 builds on 56's call, the direction is reversed. 56 should carry `hands-off TOOL-dDeclaredLoop-70` (or no edge), and 70 should carry `consumes-from TOOL-dDeclaredLoop-56`.
   - §4 Dependency should also stop reading 70 "for that keyword's default". At HEAD, `derive_phase_position(phase, facts, phase_map=None, extra=())` already has the default S18 needs.

2. Stale figures, which I would otherwise have fixed in deviation 565:
   - §4 "The sweep" counts 18 positional-registry rows for this spec. At HEAD `grep -c 'spec-TOOL-dDeclaredLoop-56.md' memory/project/positional-refs.txt` prints 2 (BUILD-METHOD M4 and M6), both still cited by the spec. So no shrink runs, and `memory/project/positional-refs.txt` leaves Files touched.
   - The sweep's "six other --claims reads" of `tools/unattended/unattended.test.sh` are eight at HEAD. One of them, AC16, reads fields 1, 4 and 5. No field position moves, so nothing turns red.

3. Gaps for the spec writer to settle:
   - Files touched lacks `tools/workflows/README.md`. Its `review_dispose.py classes` sentence says it counts "against every other review record", which S41 changes.
   - S36 does not say whether a scratch with no remote still adds the remote-tip claim. Today that claim reads `re-derived` and prints `interrupt — invalidated · remote tip refs/remotes/?`, which conflicts with "the remote reads absent".
   - The sweep omits two `derive_position` callers over scratch repos with no remote: `tools/loop/adapt.py`'s mid-step plant and `tools/loop/composition.py`'s rename plant. Their answers move off `stale-remote`, but neither checks the answer, so nothing turns red.

Every other sweep claim held at HEAD:
- REFUSAL_CEILINGS driver token 343, VERB_OFFENDER_PIN 1215, SHARED_RECORDS, and manifest-check.sh on the watch line.
- PROBLEM_PIN 17 and the three budget rows (60, 411 and 882 PINNED).
- The code behind each kept item: print_claims, derive_claims_line, read_withdrawn_parents, derive_phase_position, resolve_remote, read_remote_claim and derive_answer, check_terminal_proof and its two inline copies, the canary key-set probe, the roles_lib refusal, the hook factory and guarded write, review_rounds cmd_up, measure_class_occurrences, and build_commit's per-commit fallback.
- Forks F1 to F8 all carry RESOLVED.

## Summary

I did not build TOOL-dDeclaredLoop-56 and committed nothing. The write-set declaration (`--dispatch`) refused the pass with check 49: this unit's spec says it consumes from unit 70, which is DEFERRED and builds after it. The edge in §3 Edges is reversed and needs the spec writer to flip it; the full list is in `why`.

- **Repository state:** HEAD is unchanged at 8b06bb0a4. The refused dispatch wrote nothing to `RUN.md`. No product file was edited, so there is no patch to save. The two untracked unit-79 prompt files in the tree belong to another session.
- **Checks run before the refusal:** I re-ran the spec's sweep against HEAD, reading every file it cites, and printed the docs fingerprints for the scripts this unit touches (`python tools/govkit/docs_leg.py --fingerprints`). `verb:unattended.sh:--claims` reads 4da4f494 with no page anchoring it yet. Every design claim held; the only failures are the edge, two stale counts and three gaps, all in `why`.
- **Blocked:** one attempted read of `check_runbook_parity.py` was refused by the role hook as the gate leg "govkit runbook parity". I relied on the task's figure of 18 problems at HEAD instead.
- **No gate ran,** so nothing stands in for any section 7 leg.

**Plan for the re-dispatch** (all of it falls away until the spec is revised):
- **AC5:** a five-field stand-in driver arm in `skills/session-kickoff/manifest-check.test.sh`, floor 348 to 350.
- **AC13 and AC34:** three plants in `tools/loop/loop_parents.py`: `incomplete-parent`, `aborted-on-run-branch` and `no-run-record`.
- **AC31:** the `no-remote` plant, plus `stale-remote` restaged through an `update-ref` carrying an aged `GIT_COMMITTER_DATE`.
- **AC32:** `factory-restores-create`: the hook factory over a committed hand fragment that turns its gate red.
- **AC19:** a `stage`/`stages` canary pair in `tools/run-gates/run-gates.test.sh`.
- **AC28:** a no-loop-kit arm in `tools/roles/adopt-roles.test.sh` naming `no loop kit places the workflows: `, floor 66 to 67.
- **AC35:** review-rounds rows in `tools/govkit/selftest.py` for a proposal, a conflict and keys already set.
- **AC36:** two rounds of one review in `tools/workflows/unattended-build.test.sh`, floor 1069 to 1071.
- **AC37:** a counter probe over `build_commit` in `tools/unattended/lib-unattended.sh`.
- **AC15:** a `check_terminal_proof` probe with stderr sent to a pipe, to `NUL` and to a regular file.
- **Owed to the close:** each of these new arms observed RED first, then the section 7 legs.

Files: `C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md` and `C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-70.md`.
