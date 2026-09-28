# TOOL-dHashedPrelude-3 — the kit's published facts stop being a typed count, and its version moves

**Status:** SPECCED · rev-1 · 2026-09-28 · node d · Tier-1 · base 3cf05f29 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-recall/README.md` line 26 tells a reader the selftest is "18 checks". It has not been
18 since 2026-08-03, and units 1 and 2 move the number again. Replace the typed figure with a
pointer to the run's own summary line, and move the kit version markers, which must not land in an
earlier commit than the last change to the kit's shipped bytes.

## 2. Scope (IN)

- **S1** — `tools/memory-recall/README.md` line 26 describes `selftest.py` by its role and by where
  a reader finds the number of checks, which is the summary line the run itself prints. No figure is
  typed into that table. Observed by AC1.
- **S2** — `KIT_MEMORY_RECALL_VERSION` in `tools/memory-recall/recall_conf.py` moves from 1.12 to
  1.13, and so do the two `gov:kit memory-recall@1.12` markers, one in that file's docstring and one
  in the README's HTML comment. All three carry the same value. Observed by AC2.
- **S3** — The backlog row `TOOL-aProbedToolkit-14` records that its memory-recall half is answered
  here and that its `tools/lexicon/README.md` half is still open. Observed by AC3.

## 3. Non-goals (OUT)

The lexicon half of `TOOL-aProbedToolkit-14` is not touched: it is a different kit, a different
sample paste, and this build edits neither. No other figure in this README is audited — the row is
specific about which claims it measured, and the ones it checked and found correct stay as they are.
No change to how the version enters `Conf.digest()`.

## 4. Design

Three markers carry the version and `bash tools/check-kit-versions.sh` asserts they agree, so they
move in one edit. The bump lands in this unit's commit and not in unit 1's or unit 2's, because
`govkit epoch` reds when a kit's last bump precedes the last commit that moved its shipped bytes:
this unit is the one that edits `README.md`, whose role in `kit.toml` is `engine` and which is
therefore inside the measured set. `selftest.py` is `project-owned` and is not, so units 1 and 2
move no bytes that `epoch` grades.

That is also why the bump is recorded as contested rather than routine. The kit's own rule asks for
no bump on account of units 1 and 2, and the value enters the conf digest, so every node rebuilds a
warm cache for a file no adopter holds. The owner ruled on 2026-09-28 that an edit inside the kit
directory is a kit edit. The ruling stands and this unit implements it; the build README's parked
section carries the reasoning so the next reader does not re-derive it.

### Files touched (estimate)

`tools/memory-recall/README.md` · `tools/memory-recall/recall_conf.py` · `memory/backlog/TOOL.md`

## 6. Acceptance criteria

- **AC1** — When line 26 of `tools/memory-recall/README.md` is read, it names no check count, and
  `grep -n "18 checks" tools/memory-recall/README.md` prints nothing.
  Red when: a fresh figure is typed in place of the stale one, which restores the class rather than
  answering it.
- **AC2** — When `bash tools/check-kit-versions.sh` runs it exits 0, and
  `grep -rn "memory-recall@1\.13\|KIT_MEMORY_RECALL_VERSION" tools/memory-recall/` prints three
  lines all carrying 1.13. `python tools/govkit/govkit.py epoch --base 3cf05f29` prints a `clean`
  row for `memory-recall` and no `FAILED` line for it.
  figure: the three markers are DERIVED by the grep at observation time; 1.13 is PINNED.
  Red when: one of the three markers is left at 1.12, or the bump rides unit 1's or unit 2's commit
  and so precedes the README edit that moves engine bytes.
- **AC3** — When `TOOL-aProbedToolkit-14` is read in `memory/backlog/TOOL.md`, it names which half
  this build answered and which half is still open, and its status token still reflects that one
  half remains.
  Red when: the row is closed outright, which would claim the lexicon README was fixed here.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `row-keyed merge driver replay` · `hook destinations self-test` · `memory-recall skill wiring`

New arm: none. This unit adds no arm; AC1 and AC2 are direct greps and a checker run.

## 8. Open questions

none — the one fork this unit carried was the version bump, resolved before the spec was written.
RESOLVED (owner, 2026-09-28): bump 1.12 to 1.13, against the recommendation recorded in §4 and in
the build README's parked section.

## 9. Revision log

- rev-1 · 2026-09-28 · initial draft.
