# TOOL-aRepatriatedFork-15 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-15

One unit pass under the mandate. It ran no merge bar and no self-test suite: govkit's `selftest.py`
was not run whole. The new arm was called in-process over a scratch fixture, and every other
criterion was observed by a direct run of the verb or the checker. No adopter tree was read.

## The fixtures

- **govkit arm**: `check_epoch_verb` called alone over a fixture registry of one versioned and one
  unversioned entry on a five-commit branch. It was then run against a copy of the verb whose
  bump search was cut to an endpoint comparison, which failed the AC3 and decoy arms, then restored.
- **a7c78ad2 clone**: `git clone --shared` of this worktree under `%TEMP%/ep15`, checked out at
  a7c78ad2, with this unit's `govkit.py` copied over the one it carried.
- **Tip clone**: `git clone --shared` under `%TEMP%/ep15c`, at a2584471 plus this unit's diff
  committed as one probe commit, because the verb reads history and the diff was not yet in it.

**Evidences:** TOOL-aRepatriatedFork-15
- AC1 — `python tools/govkit/govkit.py epoch` — in the fixture, the unbumped edit printed `epoch: vk · FAILED · moved in` with `(still 1.0)` and exited 1, and after the bump commit it printed `epoch: vk · clean · 1.1` and exited 0
- AC2 — `python tools/govkit/govkit.py epoch --base fd240496` — in the a7c78ad2 clone it exited 1 naming drift-audit and kickoff-manifest, and the other six the spec pins: lexicon, memory-recall, playbook, playbook-render, process-monitor and review-harness. It also named run-gates and unattended, whose last bump precedes a later move in that range
- AC3 — `check-verdict-epoch.sh` — its endpoint defect was reproduced: the fixture's edit after the bump printed `last bump <sha> precedes last move <sha>` and exited 1, and the endpoint-cut copy of the verb printed `clean` for the same state, failing the arm
- AC4 — `python tools/govkit/govkit.py epoch --base fd240496` — in the tip clone it exited 0 with no FAILED line: kickoff-manifest 1.5, memory-tree 2.89, playbook 3.1, playbook-render 1.3, process-monitor 0.3 and unattended 1.30 bumped here, and drift-audit 1.12, lexicon 1.6, memory-recall 1.10 and review-harness 1.9 were bumped by siblings. The default range from f8fdd873 also exited 0
- AC5 — `bash skills/session-kickoff/manifest-check.sh` — over `memory/guides/SESSION-KICKOFF.md` it printed no `manifest format` line with the vintage at 1.5, and a copy with `MANIFEST_FORMAT` raised to 1.5 printed `WARN: manifest format v1.4 < kit format v1.5`
- AC6 — `skip` — the fixture's unversioned kit printed `epoch: nk · skip · no declared version · moved: tools/nk/nk.sh` on the exit-0 run as well as on the red one
