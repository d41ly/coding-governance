# DEPL-aRepatriatedFork-17 — acceptance ledger

**Serves:** journal DEPL-aRepatriatedFork-17

One unit pass under the mandate. It ran no merge bar and no self-test suite. The new arms were run
on their own. `check_update_safety` ran by importing `tools/govkit/selftest.py` and calling that one
function over a scratch root under `%TEMP%`. The `-13` gate-leg block ran as a slice of the suite's
`main`, executed alone over its own scratch root. All held: 36 arms in the first, 34 in the slice.
The whole `selftest.py` suite and the acceptance matrix were not run, and the close owes both.

Every new arm was observed RED first. The same two runs with a7c78ad2's `govkit.py` copied into the
fixtures redded 20 arms of the first and both AC13 arms of the slice; what held there was the
liveness arms, AC4's control and AC10's no-byte-moved arm, which a refused flag satisfies too. The
S2 tamper arm, which a7c78ad2 also passes, was observed red against this unit's own `govkit.py` with
the `blob_oid(raw) != oid` half removed.

The adopters were read-only. AC12 was observed at NicoCares in a `git clone --shared` of its git
directory, `C:/projects/incms/main/.git/modules/vendor/nicocares-package`, checked out at
`14b9fb7a`, under `%TEMP%/a17n`. Nothing was written in either real tree, and inCMS was not needed.

**Evidences:** DEPL-aRepatriatedFork-17
- AC1 — `govkit selftest` — `[aRF-17 AC1]`: after `update --write` rolls the `demo` kit back, `docs/out.md` is `v1` again and the rollback order carries `restored  docs/out.md`. Red at a7c78ad2, which left `v2`
- AC2 — `writes` — `[aRF-17 AC2]`: `docs/stray.txt`, written by the `[[regenerate]]` argv and named by no `writes` list, prints `still differs after the rollback`, and the order says `still differs`. The declared `docs/declared.txt` is reverted and printed `reverted`
- AC3 — `eol-only` — `[aRF-17 AC3]`: in a `core.autocrlf=true` clone whose `plain.txt` is CRLF, `check` prints a non-zero `eol-only` count and no `does not match the receipt`. Red at a7c78ad2
- AC4 — `check` — `[aRF-17 AC4]`: the same clone with one real byte changed still prints the mismatch. `[aRF-17 S2]` also reds a tampered `sha256` over untouched LF bytes
- AC5 — `git merge-file -p --diff3` — `[aRF-17 AC5]`: the conflicting `conf.sh` is byte-identical after the run, the four files sit under `.governance/outbox/update-conflict-<slug>/`, and `git merge-file -p --diff3 -L ours -L base -L theirs` over them reproduces `candidate` exactly. The order prints that line. Red at a7c78ad2, which wrote no directory
- AC6 — `candidate` — `[aRF-17 AC6]`: the lone CR inside the awk program on line 1 sits at the same offset in `candidate` as in the target file, and the CR counts are equal
- AC7 — `lone-CR` — `[aRF-17 AC7]`: a read-only `update` prints `lone-CR tools/demo/lone.sh` with `gov 4 · target 0`. `[aRF-17 S4]` shows the `--write` run failing with that finding and withholding the re-stamp
- AC8 — `oid` — `[aRF-17 AC8]`: the same staged tree is refused without the flag (`differ from HEAD`), then `adopt --re-adopt --staged --write` exits 0 and the row's `oid` equals `git rev-parse :tools/demo/plain.txt`, with `.governance/install.json` staged
- AC9 — `--staged` — `[aRF-17 AC9]`: an unstaged edit at `tools/demo/plain.txt` makes the `--staged` run exit 2 with `--staged:` and the path on stderr
- AC10 — `role-recorded` — `[aRF-17 AC10]`: both rows print `role-moved` first, then `update --write --accept-role-moves` prints `role-recorded` for both, their bytes and index entries do not move, and the next read-only run prints no `role-moved`
- AC11 — `KEEP` — `[aRF-17 AC11]`: `plan` prints `KEEP` for the existing seed `tools/demo/s.txt`. Red at a7c78ad2, which printed `write`
- AC12 — `unattended` — at `%TEMP%/a17n`, a read-only `update` prints `unattended  DIFFERS — target has 1.28, gov has 1.31 · read from the target's own copy`, whose `scripts/unattended/unattended.sh` holds 1.28. The receipt's rows hold 1.17 and 1.28, which a7c78ad2's branch prints as `MIXED`, and `[aRF-17 S7]` observed that red over a fixture. codebase-map and lexicon also stopped reading `MIXED`
- AC13 — `agent-instructions wiring` — `[aRF-17 AC13]`: the runner holds that leg with gov's resolved argv and the receipt has no emitted legs, and `update --write` prints `claimed` and records it as emitted. The older `-13` arm's runner now carries a different argv, and the refusal names both argvs. Both red at a7c78ad2
- AC14 — `adopter-owned` — `[aRF-17 AC14]`: `adopt --suggest-pins` prints `--pin tools/demo/prog.py=<A>` for the row one line off vintage A. It prints `no-pin tools/demo/other.py` naming `adopter-owned` for the unrelated program. Red at a7c78ad2, which refused the flag
- AC15 — `project-owned` — `[aRF-17 AC15]`: the `project-owned` row moved to `engine` is recorded `evidence: "vintage-match"` at gov's vintage A with no byte written. The next `update --write` lands `p v2` with the row's verdict `stale`
