# TOOL-dDeclaredLoop-40 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-40

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on
node `d` (win32) by the spec's §4 probe: a scratch git repository holding one commit whose message
carries `Pass: TOOL-tFix-2`, the unattended kit's copy of the reader in a `kit` directory beside it,
and, where a criterion has one, an `edges.toml` in a `playbook` directory beside `kit`. Each read was
a `python -c` importing the copy from `kit`, run once with the copy at the pass base `5c7b73c4` and
once with the built copy, under a short scratch directory.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of its one
`New arm:` line in `tools/memory-tree/routed_commits.py#run_selftest`, staged by planting the base
copy of the reader as the kit's own for one run and restoring it. The arm's text alone, executed
outside the suite over a planted base copy, read FAIL on its first two checks with the resolver's
`LookupError` line, and ok on all three over the built copy.

**Evidences:** TOOL-dDeclaredLoop-40
- AC2 — `unregistered-key check skipped: no edges.toml` — no table, two `("Pass",)` reads in one
  process: at base each raised the resolver's `LookupError`; built, each returned the commit with
  `TOOL-tFix-2`, and stderr carried the note once.
- AC3 — `Gov-Nope` — no table: at base the read raised `LookupError` and `tokens HEAD` exited 2 with
  the resolver's line; built, the read raised `ValueError` naming `Gov-Nope`, and `tokens HEAD`
  exited 0 with its `PASSTRAILER TOOL-tFix-2` line on stdout and the note on stderr alone.
- AC4 — `Decided` — a table registering `Pass` alone: at base and built alike a `("Decided",)` read
  raised `ValueError` naming it and the table's path, a `("Pass",)` read returned, and stderr was empty.
- AC5 — `[[trailer]]` — a table holding no row: at base a `("Pass",)` read raised `ValueError`; built,
  it returned the commit and stderr carried the note.
- AC6 — `Red-fix` — no table, `("Pass", "Red-fix")` with `files=True`: at base `LookupError`; built,
  the commit with `TOOL-tFix-2` and an empty `Red-fix` list.
- AC7 — `every read refuses` — `grep -n` over the canonical reader and both copies printed nothing,
  and `grep -n "floor" help/tags.md` printed one line of the trailer paragraph.

Also probed on the built tree: the `commit_trailers_py` block reads byte-identical across the three
copies of the reader.
