# TOOL-dDeclaredLoop-68 — the witness normaliser has one owner, the run-gates program, before unit 67 reads it

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 37 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-68-deviation-681.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-deviation-681.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item. `TOOL-dDeclaredLoop-56` S27
(order 36) carries `run_witness_commands`' normaliser as a Python copy inline in the loop kit under a
`normalise_output` parity row of `tools/lib/resolve-python.test.sh`, and its §7 New arm asserts that row.
`TOOL-dDeclaredLoop-67` S24 (order 38) runs the existing program instead and its AC17 requires
`git grep -c normalise_output -- tools/lib/resolve-python.test.sh` to print nothing, while nothing between
the two removes what 56 builds. Built in order, 56's arm and 67's AC17 cannot both hold.

This unit chooses one owner: the run-gates kit's `write_normaliser`
(`tools/run-gates/lib-attribute.sh:39-53`), which 67 S24 already names. It builds immediately after 56,
so 56's pass is untouched and 67's pass finds the program route in place. It repairs
`TOOL-dDeclaredLoop-56`.

## 2. Scope (IN)

- **S1** — `run_witness_commands` normalises each command's output by running the program, never a copy:
  the run-gates kit resolved by `resolve_kit_dir("run-gates", "lib-attribute.sh", here)`,
  `lib-attribute.sh` sourced in a bash the loop kit's own `resolve_bash` answers
  (`TOOL-dDeclaredLoop-42` S1), `write_normaliser <file> <worktree root> <repo root>` written once per
  re-run into the run's scratch directory and applied with `sed -E -f <file>`. The roots are the ones
  56 S27 names, the worktree root among them. Observed by AC1, AC2.
- **S2** — The Python copy 56 S27 adds to the loop kit, and its `normalise_output` row and block markers
  in `tools/lib/resolve-python.test.sh`, are deleted in this pass; the `resolve_bash_py` row 56 S28 adds
  is untouched. The `normalise_output` half of 56's `New arm:` line is retired with them, its
  `resolve_bash_py` half standing. Observed by AC3.
  **Readers:**
  by name: `tools/lib/resolve-python.test.sh`, whose `PARITY_ROWS` table and marker scan are the only
  readers of the row name.
  by value: NO VALUE READERS — the row's value is a byte comparison of two blocks, read by the parity
  arm that this pass deletes with it.
- **S3** — A run-gates kit that does not resolve, or a `write_normaliser` that exits non-zero, refuses
  the re-run by name, `witness: normaliser unavailable — <reason>`, and records no hash: an
  un-normalised hash would read `refuted` on a holding probe. Observed by AC4.

## 3. Non-goals (OUT)

- Which bytes the normaliser strips: `write_normaliser`'s own rules, unchanged.
- `TOOL-dDeclaredLoop-67` S24's other text: that pass now reads S1 as landed and observes AC17 green over
  it, as its consumes-from bullet to this unit records.
- A spec-set check that reds a later spec's absence assertion over a token an earlier sibling mints,
  the finding's left-shift: the class is recorded at the close; AC3 is this pair's observation.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-56` — S27's normaliser in `run_witness_commands` and its `normalise_output` parity row, which this unit replaces with the run-gates program
- **hands-off** `TOOL-dDeclaredLoop-67` — the program-route normaliser and the absent `normalise_output` row, which S24 and AC17 read as already landed
- **hands-off** `TOOL-dDeclaredLoop-79` — the normaliser route, its named refusal and the loop kit's descriptor, which that unit applies inside the resolved bash, refuses on a failed `sed`, feeds forward-slash roots and gives a `requires` edge to run-gates (ids 4, 10, 11, 23, 30); this pass keeps the sibling-minted `loop computed witness` leg green (id 3)

## 4. Design

### Evidence

- `write_normaliser <sed-file> <root>...` truncates the file, writes one `s|...||g` line per spelling of
  each root, then the scratch-name, duration, CR and trailing-space rules
  (`tools/run-gates/lib-attribute.sh:39-53`), and its header says to apply it with `sed -E -f`: read at
  base `ed497191`.
- `PARITY_ROWS` lists `<marker-stem>|<canonical file>|<excluded prefix>` rows
  (`tools/lib/resolve-python.test.sh:166-182`); no `normalise_output` row exists at base, so the row is
  56's to add and this unit's to delete.
- `tools/loop/` does not exist at base: every loop path below is a sibling unit's output.

### The route

```
kit   = resolve_kit_dir("run-gates", "lib-attribute.sh", here)       # refuse by name when absent
prog  = <run scratch>/normalise.sed
bash  = resolve_bash()                                                # the loop kit's own resolver
run   [bash, "-c", '. "$1"; write_normaliser "$2" "$3" "$4"', _, kit/lib-attribute.sh, prog, wt, repo]
norm  = run ["sed", "-E", "-f", prog] over the command's raw output file
hash  = sha256(norm)
```

### Files touched (estimate)

- `tools/loop/loop_witness.py`
- `tools/lib/resolve-python.test.sh`

### Alternatives rejected

- **Keeping 56's Python copy and dropping 67's AC17 clause.** Two implementations of one normaliser held
  equal by a byte arm is the copy the reuse rule forbids where the program can run in place; and the
  clause belongs to a spec this pass may not fold.
- **Building after 67 (order 39).** 67's pass would read AC17 red over 56's row and park.

## 5. Production-readiness checklist

- security — no new surface: a sourced library of a sibling kit, run on the re-run's own output file.
- perf / scale — one bash and one `sed` per re-run, not per command line.
- error / empty / loading states — S3 refuses by name; empty output normalises to empty and hashes.
- observability — S3's refusal names the reason.
- risks — an adopter install without the run-gates kit refuses the re-run; the loop kit's descriptor
  already requires the kits it resolves, and S3 names the missing one.
- testing — AC1 to AC4 as plants and greps; the arm under §7, observed at the close.
- migration — none: no hash recorded under 56's copy survives a spec run, `tools/loop/` being unbuilt.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python loop_witness.py --fixture --plant normalise` hashes two re-runs of one command that
  prints its worktree path and a duration, the two hashes are equal.
  Red when: the raw output is hashed, so two worktree paths give two hashes.
- **AC2** — When `grep -c write_normaliser loop_witness.py` runs in `tools/loop/`, it prints at least 1.
  Red when: the re-run still calls a Python copy of the rules, so the program is never run.
- **AC3** — When `git grep -c normalise_output -- tools/lib/resolve-python.test.sh tools/loop/` runs after
  this pass, it prints nothing, and `git grep -c resolve_bash_py -- tools/lib/resolve-python.test.sh`
  prints a count.
  Red when: the row or its markers survive, or the `resolve_bash_py` row is deleted with them.
- **AC4** — When `--plant normaliser-missing` points `resolve_kit_dir` at a directory without
  `lib-attribute.sh`, the re-run exits non-zero printing `witness: normaliser unavailable` and writes no
  hash.
  Red when: the re-run falls back to hashing the raw output.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_witness.py · covers AC1 AC4 · the normalise and normaliser-missing plants, staged against TOOL-dDeclaredLoop-56 S27's inline copy · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which spec owns the normaliser, 56 S27's copy or 67 S24's program?** Options: (a) the copy, 67
  AC17 dropped; (b) the program, 56's row deleted. (a) fails 67 AC17, a criterion already written, and
  veto 1 discards it. RESOLVED (agent, 2026-10-24, delegated): (b), at order 37 so neither pass is
  folded. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-3 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-79, written by the round-4 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is the run-gates kit's `write_normaliser` (`tools/run-gates/lib-attribute.sh:39-53`), run in
place, reached by `resolve_kit_dir` and the loop kit's own `resolve_bash`; no copy is minted and the one
56 adds is deleted. `python tools/codebase-map/reuse_lookup.py "normalise command output before hashing"`
ranked `read_git_output` (`tools/memory-tree/tree_lib.py`), `derive_clause_hash` and `hash_file`, none of
which normalises output; the dossier does not index shell functions of `lib-attribute.sh`, so the seam
was found by reading 67 S24 and that file, where it agrees with source.

Recall terms used: write_normaliser lib-attribute normalise_output parity row resolve-python witness rerun hash inline copy
