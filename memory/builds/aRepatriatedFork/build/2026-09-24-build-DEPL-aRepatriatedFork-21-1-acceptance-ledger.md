# DEPL-aRepatriatedFork-21 — acceptance ledger

**Serves:** journal DEPL-aRepatriatedFork-21

One unit pass under the mandate. It ran no merge bar and no self-test suite. Every criterion was
observed on scratch fixtures under `%TEMP%/rf21*`, never at an adopter: this unit's criteria are all
fixture criteria, so no inCMS or NicoCares clone was made.

Two direct checks ran. The first is a scratch probe that builds the `-13` demo gov, swaps a chosen
`govkit.py` into its worktree without committing, and runs `adopt --write` then `apply --resume
--write` over an owning target and a non-owning one. It ran three times: on `7308f088`'s
`govkit.py`, on the pre-change HEAD `5e33d983`, and on the changed bytes. The second is the new
selftest function `check_apply_owned`, run on its own by importing `tools/govkit/selftest.py` and
calling it over a scratch directory. It gave 4 of 4 `ok` on the changed bytes. With `GOVKIT`
pointed at `7308f088`'s bytes it gave 3 `FAIL` lines, both AC1 arms and the AC3 arm. The whole
`selftest.py` suite was not run; the close owes it.

## AC2 — the red-first control

On `7308f088`'s `govkit.py`, and identically on `5e33d983`'s, `apply --resume --write` over the
owning fixture exited 0, printed no skip for `tools/demo/run.py`, overwrote the adopter's program
with gov's `run.py`, and re-recorded the row as `engine`:

```
[7308] own: apply rc=0 run.py unchanged=False role=engine skipped-line=False
[head] own: apply rc=0 run.py unchanged=False role=engine skipped-line=False
```

The same fixture on the changed bytes:

```
[new] own: apply rc=0 run.py unchanged=True role=adopter-owned skipped-line=True
```

## AC4 — the byte comparison, and what it normalises

The non-owning fixture's `apply --resume --write` stdout and `install.json` were compared across all
three runs. Each run builds its own scratch gov under its own directory, so two things differ by
construction: the directory name inside `gov_source` and the target path, and the scratch gov's
commit sha. Both were masked with `sed` before the compare, and nothing else was. After that, `cmp`
reported the changed bytes' output and receipt identical to `7308f088`'s and to `5e33d983`'s.

**Evidences:** DEPL-aRepatriatedFork-21
- AC1 — `adopter-owned` — `check_apply_owned` arm `[aRF-21 AC1]`: the owned `tools/demo/run.py` keeps its bytes, stdout carries `SKIPPED [adopter-owned] tools/demo/run.py <- demo`, and the receipt row equals the one `adopt` wrote
- AC2 — `7308f088` — the control above: that engine's `apply --resume` overwrote the owned file and recorded `role=engine`, and both AC1 arms go FAIL against those bytes
- AC3 — `resolve_owned_rows` — arm `[aRF-21 AC3]`: an `[[own]]` path of `../run.py` exits 1 naming `[[own]] row 1`, with `git status --porcelain` empty and `install.json` byte-equal afterwards. On `7308f088` the same run exited 0
- AC4 — `7308f088` — `cmp` of the normalised stdout and `install.json` of `apply --resume --write` on the non-owning fixture: identical to `7308f088`'s and to `5e33d983`'s. Arm `[aRF-21 AC4]` keeps the structural half: `run.py` lands as `engine` with gov's bytes, and no `adopter-owned` line is printed
