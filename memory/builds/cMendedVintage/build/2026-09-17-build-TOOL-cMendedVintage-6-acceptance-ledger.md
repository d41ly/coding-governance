# cMendedVintage — the acceptance ledger for unit 6

**Serves:** journal TOOL-cMendedVintage-6

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh` suite
ran in this pass. Every line below was taken by running the new checker, or the named gate script,
at the shell in the worktree, and every red was STAGED and then removed rather than described.*

## Read this before you read the green leg

**On gov's own bar this leg's receipt half never runs, and that is the design.** There is a
`.governance/` directory here but it holds `deploy.toml` and nothing else — no receipt — so every bar
in this repository takes the announced `SKIP` path. Verified, not assumed: the directory was listed
and `git ls-files` reports one tracked file in it.

The consequence is the thing a reader will otherwise get wrong. **The only part of this checker that
any gov bar ever grades is the four built-in fixture arms.** A green row for this leg here is
evidence that the hash loop, the role scoping, the missing-file branch and the liveness counter all
behave — it is NOT evidence that anything in this repository was verified against a receipt, because
there is no receipt to verify against. The integrity half gets its first real exercise at an adopter.
That is exactly why the arms run on every invocation rather than under the selftest flag alone:
without them the leg's whole live behaviour here would be "nothing to do", which is the could-not-fail
shape, and it would sit green forever having looked at nothing.

**The ceiling was measured, not chosen.** Five consecutive runs on this node — four cores, heavily
loaded, which biases the reading conservatively — came in at 0.26, 0.26, 0.25, 0.25 and 0.25 seconds
against the empty-receipt path, which is the path a gov bar takes and therefore the one the ceiling
must cover. The margin declaration demands headroom of
`max(120s, 1.0 x max)`
above a leg's evidenced maximum, so the smallest legal ceiling for a 0.26 s leg is about 121 s. The
declared 300 clears that with room and is also the standing value across this chunk, so the number is
defensible from the measurement AND consistent with its neighbours. Note the trap it avoids: three
legs in this chunk carry a 60 s ceiling, which is BELOW the floor the margin rule imposes and will
red the moment a run puts evidence beside them.

**The brief promised four declarations. Six fired.** The named bug class
`a-new-leg-trips-a-growing-set-of-meta-gates.md`
says the set is discovered by RUNNING it and is never enumerable from memory, and this unit is one
more reading of exactly that. Logged as rev-4. Beyond the four the brief named:

- **A fifth — staging the file.** With the descriptor row, the manifest row and the file all present
  in the worktree but the file UNSTAGED, `selfcheck` reds with the leg's argv naming a path that "NO
  rule in any descriptor writes, seeds, orders or produces", because the `**` engine rule's pool is
  the TRACKED surface. So the `git add` is not bookkeeping ahead of the commit, it is a declaration,
  and its refusal text mentions neither the manifest nor the pins.
- **A sixth — the leg NAME is a codebase-map inventory key.** The map gate redded `UNCLAIMED` on it.
  Claimed in `memory/map/features/run-gates.md`, with a prose paragraph added on the same touch, and
  the three generated map artifacts regenerated in the same commit.
- **And the kickoff-manifest ratchet**, a meta-gate on the same edit by a different route:
  `tools/gate-legs.json` is a watched file, so `last-audit` owed a re-stamp. Re-verified rather than
  assumed — the manifest front-loads no leg count, says outright that the leg list is single-sourced
  from that file, and its ceiling and `GATE_FULL` claims all hold for the new row. Datetime advanced,
  sha unchanged, because the merge-base is still the one already stamped.

Each was caught by a machine and none by reading the spec: the fifth by `selfcheck`, the sixth by the
post-commit bug-class checklist, the ratchet by the pre-commit hook.

**Evidences:** TOOL-cMendedVintage-6

- AC1 — OBSERVED. Bare invocation in this worktree, which holds no
  `install.json`
  under `.governance/`, prints a line whose head is the literal word `SKIP` naming the full path it
  looked for, and exits 0. The line says in its own words that it is a skip and not a pass.
- AC2 — OBSERVED. Run with
  `--selftest`
  it prints one `ARM ok` line per arm followed by
  `fixtures: 4/4 arm(s) ok`
  and exits 0. The arm count is printed from the length of the results list, so the figure is
  DERIVED by the run and asserted nowhere in this document or in the code.
- AC3 — OBSERVED RED. A fixture git repo was built under this run's scratchpad with one engine row
  and one `seed` row, its
  `sha256`
  filled in from the bytes actually written. Altering the first character of that hash and passing
  the tree as the positional argument gives
  `DRIFTED   shipped.py — receipt 195d3aaffff1, disk 895d3aaffff1`
  and exit 1, naming the row's `path`. The engine row deliberately carries NO `role` key in the
  second fixture arm, which is what proves the absent-key default is read as engine rather than
  skipped.
- AC4 — OBSERVED RED. The same tree with that engine file deleted gives
  `MISSING   shipped.py — in the receipt and not on disk`
  and exit 1. The row's `path` is reported as missing and not as a hash mismatch, so the remedy the
  line names is the right one.
- AC5 — OBSERVED RED. A fixture whose receipt carries only a `seed` row and a `merged` row prints the
  summary line
  `receipt: schema 3 · 2 row(s) read · 0 engine row(s) graded`
  and then
  `DEAD PROBE`
  with a refusal to call the tree verified, exiting 1. Two rows were read and none was graded, which
  is precisely the state a clean report would have misrepresented.
- AC6 — OBSERVED, both reds and the green. With the manifest row present and no descriptor claiming
  it, `selfcheck` reds: the leg "is claimed by no descriptor and carried by no `[[exempt_leg]]`".
  With both declarations present and the pin file stale it reds: the leg "has no row in
  `tools/govkit/subject-pins.tsv`". After
  `python tools/govkit/govkit.py selfcheck --write`
  regenerated the pins — one added row,
  `receipt sync (installed files match the receipt)	repo	declarations`
  — the same command exits 0 over 26 entries and 68 tracked paths with 0 unclaimed.
- AC7 — OBSERVED, and the figure is DERIVED as the criterion demands. The AC3 fixture was cloned under
  the scratchpad with
  `core.autocrlf=true`
  and graded through the positional argument. The finding count is **1 of 1 graded engine rows**, so
  the residue on that clone is the entire engine population, and the run's own summary line names
  `schema 3` immediately above the finding. The stronger reading is the one the setup did not intend:
  the SOURCE fixture had `core.autocrlf=false` set locally and its working copy still held CR bytes,
  because `* text=auto` with a native `core.eol` normalizes on checkout regardless of that setting.
  So the false-red population is not "clones that opted into autocrlf" — §5's existing wording, every
  clone that is not the install machine, is correct and if anything understated.

Nothing is OWED among the seven criteria: all seven were observed against the real checker. Two gate
legs named in §7 could not be observed in this pass and are OWED to the main loop's bar; they are
listed below with what each would add.

## What did not run, and why

`bash tools/run-gates/run-gates.sh` in every form, and every `*.test.sh` suite, were withheld by this
pass's own mandate. The four gate scripts that DO grade this unit's new bytes were run individually,
which is the direct-check substitution the mandate asks for, and all four are green:

| gate script run directly | what it says about this unit | result |
|---|---|---|
| `python tools/govkit/govkit.py selfcheck` | the four declarations agree | exit 0 |
| `python tools/run-gates/derive-ceilings.py --check` | the declared ceiling is legal | exit 0, this leg among the 70 reported unbacked |
| `bash tools/check-install-prefix.sh` | the new shipped file spells no kit path | exit 0, 269 shipped files |
| `python tools/lexicon/lexicon.py` | every new function name leads with a declared verb | exit 0, `.py` graded in parser mode |

Also green and touching this unit's surface: `bash tools/check-dead-paths.sh`,
`bash tools/check-line-length.sh` and `python tools/check-kit-placeholders.py`.

**OWED to the bar, two legs.** `run-gates gov canary` is a `*.test.sh` suite and is banned here; it is
the leg that would confirm the new manifest row parses and dispatches the way the runner expects,
which no direct check in this pass covers. `every held leg is budgeted, every budget row resolves`
runs through `run-selftests.sh`, named in the ban list by file; the risk it covers is low for this
unit specifically, because the new leg declares `subject = "repo"` and is therefore not held and owes
no budget row, but that reasoning is an argument and not an observation.

**The staged break and the real drift are different mutations, and both were observed.** AC3 altered
the RECEIPT's recorded hash; AC7's clone altered the FILE's bytes. That pairing matters because a
break staged only on the receipt side proves the comparison for a synthetic input — the class
`staged-break-substitutes-a-synthetic-value.md`
— and the CRLF clone is the same red reached from the direction drift actually arrives from.

**Arm 4 is the liveness arm and would pass under a broken no-op loop.** It asserts zero graded rows,
which is also what a loop that stopped looking would report. Arms 1 to 3 are its control: each
demands a non-zero graded count, so the four cannot all be green while the loop grades nothing. Said
here rather than left implicit, because an arm that passes by finding nothing is its own bug class.

**One thing measured and not acted on.** The spec's files-touched estimate put the new file at
"roughly 60 lines"; it landed at 207, almost all of it the header stating what the checker does NOT
check and the four fixture arms. No revision was logged for it — an estimate in a table headed
"estimate" is not a claim the build can falsify.
