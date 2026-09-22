# Acceptance ledger — DEPL-dCarriedReceipt-15, gov stops shipping its own prefix inside kit bodies

**Serves:** journal DEPL-dCarriedReceipt-15

Built on node `a` under session slug `aResumedRelay`, last of the five units this run carried.

**Evidences:** DEPL-dCarriedReceipt-15
- AC1 — `bash tools/check-install-prefix.sh --list` — RED observed FIRST: the command printed no
  `carried-prefix` section at all and exited 0, so every carried line was unmeasured. GREEN: the
  section now prints, and its rows `diff` byte-identical against `tools/install-prefix-carried.txt`
  as written by `--write-ratchet`, because one function emits both. **The row count and column sum
  ARE this unit's inventory claim and are not restated here or in the spec** — read them out of the
  file. What is worth saying is that they exist: an earlier attempt at this unit published a
  file-and-line pair in prose, six candidate populations were re-measured against it, and none
  reproduced the pair.
- AC2 — `bash tools/check-install-prefix.sh` — staged, observed RED, unstaged, in BOTH directions.
  Appending one `tools/lexicon/lexicon.py` literal to a recorded file reds with `ROSE` naming that
  file and its old and new counts, exit 1. Raising a recorded row above the measured count reds with
  `SLACK` naming the drop and, at zero, telling the operator to delete the row. Both restored to
  green afterwards by re-running `--write-ratchet`.
- AC3 — `bash tools/check-install-prefix.sh` in a scratch repo with no `tools/govkit/registry.toml`
  — the arm prints four lines naming itself SKIPPED and why, and the run exits 0. The fixture also
  carries `scripts/lexicon/lexicon.py` in a usage header, which is NOT a hit: an arm keying on the
  local prefix would red every usage header in every kit an adopter received, and this one does not.
- AC4 — `python tools/lexicon/lexicon.py --nosuchmode` — RED observed first: the usage line read a
  spelled `tools/lexicon/lexicon.py` regardless of where the file sat. GREEN in both directions now:
  it prints `tools/lexicon/lexicon.py` here, and the same file copied into a scratch repo at
  `scripts/lexicon/` prints `scripts/lexicon/lexicon.py`. The docstring's usage block was DELETED
  rather than fixed — it was a second spelling of what the program already prints, and the copy
  nobody re-renders.
- AC5 — amended rev-5 — the criterion demanded NO ratchet row for `lexicon.py`, on a measurement
  taken when all three of its prose citations spelled a bare directory and were therefore invisible
  to the §4 predicate. One of them now spells a real file and IS a hit, while remaining exactly the
  citation §2 forbids S5 to rewrite. **Measured:** the stripped grep the criterion names returns
  **0**, and the file's ratchet row reads **1** — that one prose citation, quoting a kit path as the
  literal subject of a measured glob bug. The executable population S5 owns went from four hits
  (a six-line docstring block and two runtime writers) to zero.
- AC6 — `bash tools/lib/resolve-python.test.sh` — staged drift into ONE inline `render_doc` copy;
  the parity leg reds naming the drifted file against the canonical, exit 1; restored, green. The
  marker-derived population names `tools/memory-tree/adopt-memory-tree.sh` and
  `tools/memory-tree/kit-dogfood-parity.test.sh`, plus the canonical `tools/lib/render-doc.sh`
  itself. `bash tools/memory-tree/kit-dogfood-parity.test.sh` stays green through the change.
- AC7 — `bash tools/run-gates/run-gates.sh` — recorded with the build's closing bar; see the wrap-up
  for the verdict and whether the self-test legs were included.

## Two things the spec did not foresee

- **Python's newline translation made the derived population arrive with a trailing CR.** All 181
  source paths failed `[ -f "$f" ]`, so the first `--write-ratchet` wrote **zero rows** and reported
  it cheerfully — a population that silently became empty, which is precisely the class this unit
  is written against, met while building the unit. Caught by not believing a zero. The existing arm
  one screen up already pipes its own file list through `tr -d '\r'` for the same reason; the new
  one does now too, with the reason written beside it.
- **The repo's own idiom ban redded the launcher fallback this arm was first written with.** The
  carried-prefix population needs python, and the first cut resolved it with a
  `resolve_python`-or-`python` fallback. `tools/lib/resolve-python.test.sh` reds on a bare launcher
  name, correctly: the MS-Store `python3` stub answers `command -v` and exits 9009, so a bare name
  is not an answer. There is no fallback now — a tree without the resolver has no shippable set to
  grade either, so the arm says so and skips, which is AC3's path.

## One declaration this unit owed

`tools/install-prefix-carried.txt` is a new tracked file under the declared surface, so govkit's
surface arm redded until a rule claimed it — correctly, and immediately. It is declared `generated`
rather than copied, for the reason the waiver registry beside it already gives: the rows are
measurements of THIS repo's shippable set, and a target's set is its own.
