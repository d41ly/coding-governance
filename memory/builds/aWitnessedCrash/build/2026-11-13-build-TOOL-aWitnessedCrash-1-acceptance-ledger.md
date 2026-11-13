# TOOL-aWitnessedCrash-1 — acceptance ledger

**Serves:** journal TOOL-aWitnessedCrash-1

No merge bar and no self-test suite ran in this pass. The criteria were observed at the built tip,
acb35e0b5, which carries the code commits 8e4f578c3 and ef4855a15. AC1 ran the engine in a clone of
that tip under a short `%TEMP%` path. AC2 to AC4 ran the main loop's probe, which builds the young
tree `Y` as the suite's young-tree arm does and copies the kit to a short `%TEMP%` path. The probe ran
over the worktree's kit. The main loop had run it over the BASE export before this pass, and there the
injected copy exited 0 with no crash row. AC5 ran the two greps at the tip, and the first grep at
base f9a87e782. The suite's new arm and its RED-first run are owed to the close, per the spec's
`New arm:` line.

The fix pass on the close bar's reds replaced the witness's `grep` with a builtin read loop. The
main loop's probe then re-ran over the worktree's kit, and AC2 to AC4 read as below again.

**Evidences:** TOOL-aWitnessedCrash-1
- AC1 — `bash tools/memory-tree/check-memory-hygiene.sh --staged` — in a clone of the tip with one
  blank line appended to `memory/HYGIENE.md` and staged, the run exited 0. `grep -c` found no line
  carrying `unbound variable` across its stdout and stderr together.
- AC2 — `HYGIENE FAILED — bash reported a runtime error` — the uninjected copy exited 0 under
  `--only 1` over `Y`. The injected copy held `__wc_probe` twice and exited 1. Its stdout opened with
  that line and named the error. Its stderr file carried `__wc_probe: unbound variable`, so the replay
  ran.
- AC3 — `check crash<TAB>check-memory-hygiene.sh: __wc_probe: unbound variable` — the injected copy
  under `--offenders`, fd 3 piped through `cat -A`, printed exactly one `check crash` row, and that row
  was this one. It carried no `line <N>` and no directory.
- AC4 — `--only 12` — with the injection and `check_selected() { return 1; }` above
  `if check_selected 12 25; then`, the copy exited 2. It printed the witness's `HYGIENE FAILED` line
  and then the `--only` refusal naming check 12, so the refusal's status won.
- AC5 — `git grep -l "memory-tree@2.158" -- ':!memory/builds'` — at the tip it listed nothing and
  exited 1. The 2.159 grep at the tip listed nine files, and `diff` found them identical to the nine
  the 2.158 grep listed at base f9a87e782: the engine, the four `tools/memory-tree/*.template.md`
  files and their four dogfood copies under `memory/`.
