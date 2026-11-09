# PLAY-dOrderedCharter-14 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-14

Each line is a probe this pass ran at rev-4 of the spec, with the pass applied. No leg, suite or bar ran in
the pass: the parity block was compared with the parity table's own extractor run by hand, the drift report
was run before and after the move, the card engine was run by hand over scratch repositories under the short
temp path, and the new `memory_index.py` verbs were called directly over fixture memory directories and stub
commands. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-14
- AC1 — `auto_memory` — the parity table's block extractor read the `auto_memory` block of `auto_memory.py`, `memory_index.py` and `tools/drift-audit/drift_report.py` as equal, CRs dropped; a scratch copy of the drift-audit file with one character of the block changed read as different; the copy grep the table runs listed exactly those three files, the canonical excluded by its row; `python tools/drift-audit/drift_report.py` printed the `dangling_pointers_in_own_ledger` row as `4 78 report only, no pin` before the move and after it.
- AC2 — `memory.load-budget` — over a fixture target committed on main and a scratch home whose index is 9000 bytes linking three entries, two of them `type: feedback` and the second carrying `promoted-to:`, the measure line read `9000 B over its 8000 B budget` with `1 standing directives unpromoted`, within the 200-byte line cap; cut to 4000 bytes it read `4000 B within its 8000 B budget`; with the fixture's committed policy file setting `memory.load-budget = "9k"` it printed one `memory — skipped:` line naming `memory.load-budget` and compared nothing. Over this node's real index it printed 20366 B over the 8000 B default, 134 lines and 79 directives unpromoted.
- AC3 — `outside.md` — the directives verb over AC2's fixture printed only `fx-rule — MUST keep the fixture rule` above its count line; with a link planted to `../outside.md`, a feedback file one directory above the memory directory, the same one line printed and the count line named `1 links outside the memory directory skipped: ../outside.md`.
- AC4 — `live —` — `manifest-check.sh --card --write` in a scratch repository tracking a copy of `memory_index.py` and `policy_value.py`, run with `HOME` set to a scratch home holding an index where `derive_index_dir`, which calls `resolve_auto_memory_dir`, puts it, exited 0 and its stored card held one `memory —` line, after `live —` and before `claims —`, reading the index and naming `memory.load-budget` as unread because the fixture holds no policy kit.
- AC5 — `CARD_MEMORY_BOUND=1` — the same write exited 0 each time and its card held one `memory — skipped:` line: in a repository tracking no module, naming that no playbook `memory_index.py` resolves; with `HOME` naming an empty directory, naming the auto-memory index it did not find; with the tracked module replaced by a five-second sleeper under `CARD_MEMORY_BOUND=1`, naming the one-second bound.
- AC6 — `promoted-to:` — the promote verb at `--level 3 --tag repo.fixture-rule` against a stub that exits 1 printed the composed row, its tag and its type, and the stub's refusal line, exited 1, passed `--promoted-from auto-memory fx-rule`, and left the entry's bytes equal; against a stub that exits 0 the entry gained one `promoted-to: repo.fixture-rule` line and a second scan counted no directive. Against the real guarded command the verb printed the composed row, then that command's refusal for the absent guard and its proposal, verbatim, and wrote nothing.
- AC7 — `--tag practice.repo.x` — with `--level 1`, with `--level 9`, with a name no directive carries, and with `--tag practice.repo.x`, refused by the tag shape check's first-segment rule, each exited 2 naming the refused value, and the stub's call log was never written.

**Owed to the close.** The bar, and the RED-first observation of each `New arm:` line: the `auto_memory` parity row
of `tools/lib/resolve-python.test.sh`, staged by a one-character change to the drift-audit copy; the seven arms of
the `memory —` cell in `skills/session-kickoff/manifest-check.test.sh`, its floor raised by seven, staged by moving
the cell after `claims —`; and the eleven `check_memory_arms` arms of `render_playbook.py --selftest`, staged by
counting a promoted entry. `python tools/playbook/gov_tag.py check` over the tree is owed too.
