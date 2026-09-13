# Acceptance ledger — cSpliceWarden, all five units

**Serves:** journal TOOL-cSpliceWarden-1 TOOL-cSpliceWarden-2 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-4 TOOL-cSpliceWarden-5

Every criterion below is answered by something that was RUN on node `c` on 2026-09-13, against the
real tree unless the line says fixture. Two things are labelled weaker than the rest and are not
smoothed over: the cross-reader arm SKIPS where no candidate shell runs, and nothing in this build
grades the declared rotation mode at all.

**Evidences:** TOOL-cSpliceWarden-1

- AC1 — `grep -n '^ROTATION_MODE=' .memory-tree.conf tools/memory-tree/.memory-tree.conf.example` —
  two lines, `cut` in the repo conf and `snapshot` in the shipped example. The two differ on purpose;
  the example keeps the discipline this kit's prose has always described.
- AC2 — `bash tools/memory-tree/check-memory-hygiene.sh` exited 2 naming `ROTATION_MODE` and the
  offending value, staged into the real conf, observed, then reverted. The blank arm was observed separately at exit 0, because an adopter conf predating the
  key must not red on upgrade. Both are now fixture arms in `check-memory-hygiene.test.sh`, covering
  `cut`, `snapshot`, blank, `Cut` and `rotate`.
- AC3 — `kit-parity: shipped and installed docs agree (4 pairs, rendered for 'tools/memory-tree')` at
  exit 0, and `grep -c 'carries forward every non-CLOSED/non-WONTDO row'` returns 0 in BOTH
  `memory/HYGIENE.md` and its template. The live copy was rendered, never hand-edited.
- AC4 — `bash tools/check-template-size.sh` reports 48908 of 49152 bytes, 244 under, at exit 0.
  The edit is net **−124** bytes against the 49032 measured at base `09a22d2b`, paid for by
  deleting §5's restatement of §7's liveness rule — a duplication the charter itself forbids. The
  high-water WARN is still lit and `--bump` was NOT run.
- AC5 — `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh` both
  exit 0. The first RED on this build named three templates whose marker had not moved with the
  engine; the kit version is shared, so all four `*.template.md` markers went to `2.71` together.

**Evidences:** TOOL-cSpliceWarden-2

- AC1 — `bash tools/memory-tree/check-memory-hygiene.sh --print-rotated-archive-ere` enumerates
  exactly the four real archives. The eight `parallel-coding-governance.template-v-2-*.md` snapshots
  and the four `memory/archive/ledger/*.md` shards are excluded, which was verified by running the
  candidate over the tree before wiring it.
- AC2 — covered by the `n10 -ne 1` branch in `check-memory-hygiene.sh`, which names the archive,
  the stem and the count. WEAKER THAN THE REST: this branch has no fixture in the tree, because no stem in this repo
  resolves to zero or several. It is an arm nobody has watched fail and is labelled so rather than
  counted as verified.
- AC3 — observed both ways on the real tree. With the `TOOL.2026-08-17b.md` reference removed from
  `memory/backlog/TOOL.md`: `HYGIENE check 10 FAILED — rotated archives not referenced from their
  live index preamble: memory/archive/TOOL.2026-08-17b.md`. Restored: green. The control matters —
  without it the green is only evidence the predicate can be silenced.
- AC4 — the stranded arm was re-keyed. The message text changed from `(lines 1-3)` to `preamble`, so
  the old literal would have matched nothing and passed by finding nothing; two new arms in the
  `rotarchive` fixture assert a rotated BACKLOG archive is both reached and correctly left alone when
  its shard does announce it.

**Evidences:** TOOL-cSpliceWarden-3

- AC1 — `python tools/memory-tree/row_grammar.py --report` reads 816 rows across nine documents,
  including all three rotated TOOL archives and excluding every frozen snapshot and ledger shard.
  Before the widening it read 698 across six.
- AC2 — `arm ok    a duplicate inside a rotated BACKLOG archive is found, not skipped` and
  `arm ok    the rotated backlog archive is named with its lines`. The fixture is written before
  `_tree`'s `git add -A`, because `row_docs` enumerates through `git ls-files` and an untracked
  fixture would pass by finding nothing.
- AC3 — `arm ok    a frozen non-row file under archive/ is NOT scanned`, over a fixture holding three
  shapes the naive widening would have swept in: an undated snapshot name, a dated file whose stem is
  no declared family, and a file nested below `archive/`.
- AC4 — `arm ok    check 10's shell enumeration and row_docs() select the same archives`. This arm
  EARNED ITS KEEP BEFORE LANDING: on its first run it reported
  `DISAGREE shell=['memory/archive/NOTAFAMILY.2026-01-01.md'] python=[]`, because the shell carried
  only the date half of the contract. The shell's ERE now derives its family alternation from
  `FAMILIES`. WEAKER THAN THE REST: the arm SKIPS, loudly and by name, where no candidate shell runs
  `--print-rotated-archive-ere`; on node `c` plain `bash` resolves to the WSL launcher, which tries to
  boot a VM and returns UTF-16 at rc=1, so the arm probes candidates rather than trusting PATH.
- AC5 — `bash tools/memory-tree/check-verdict-epoch.sh` exits 0 and
  `python tools/codebase-map/test_codebase_map.py` exits 0 with
  `ok   test_generated_artifacts_are_fresh`.

**Evidences:** TOOL-cSpliceWarden-4

- AC1 — the supersession note names all three false header claims and quotes both dropped rows
  verbatim, and `row_grammar` keys 24 rows from the file with 0 unkeyed — the note is a blockquote,
  so it contributes neither a row nor an unkeyed line.
- AC2 — `python tools/memory-tree/row_grammar.py --report` over the repaired archive: 24 rows, all
  CLOSED, zero duplicate ids. The partition was verified as exact before it was applied —
  49 + 15 + 2 + 24 = 90, with no row in two sets and none in none.
- AC3 — amended rev-3 — the criterion asserted a global `grep -c '· CLOSED ·'` delta of 15 and was
  never observable: this build also closed two consolidated rows and added one, so the real delta is
  18. Re-stated per id and logged in that spec's §9. What WAS observed against the amended criterion:
  `grep` over `memory/backlog/TOOL.md` shows each of the 15 re-homed ids reading CLOSED, zero ids sit
  in both the archive and the shard, and 4 of the 15 carry a body differing from the archive's
  because their closing commit rewrote the sentence as well as the token.
- AC4 — `bash tools/memory-tree/check-memory-hygiene.sh` reports no check-10 finding, and all four
  archives resolve and are announced.

**Evidences:** TOOL-cSpliceWarden-5

- AC1 — both rows read a terminal status. `TOOL-cTracedPromise-6` survives, rewritten to name all
  four defects and closed against `TOOL-cSpliceWarden-2`; `TOOL-aBoundedVerdict-9` closes as
  superseded and points at it.
- AC2 — the `aCollapsedScan` retirement is unchanged byte-for-byte; `git diff` over
  `memory/backlog/TOOL.md` touches neither that line nor any other ratified WONTDO row. A new row
  records that its premise was false for backlog archives.
- AC3 — the over-broad claim is gone from both surviving carriers. `row_docs`'s docstring now states
  which archives it admits and why, and `HYGIENE.md`'s check-20 entry says the same. That entry also
  carried a SECOND stale claim nobody had filed — it said an undeclared `ROW_DUPLICATE_PIN` is a
  refusal, where `pin_of` has meant ZERO since the refusal was removed for breaking every adopter.
- AC4 — `python tools/memory-tree/gen_build_index.py --write` renders the new rows, and
  `check-memory-hygiene.sh` exits 0 with check 9 green, so the generated index matches a fresh render.

## What this ledger does NOT evidence

Nothing here observes that a tree HONOURS its declared `ROTATION_MODE`. The key is validated against
its closed set and then read by no check, so no gate asserts that a rotated shard archive holds
terminal rows only, nor that no id sits in both a shard and its archive. That is the left-shift owed
on the very finding this build repaired, it is filed as a backlog row under this slug, and a green
bar after this build is not evidence against it.
