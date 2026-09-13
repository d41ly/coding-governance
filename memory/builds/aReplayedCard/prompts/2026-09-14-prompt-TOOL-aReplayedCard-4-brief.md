# Brief — TOOL-aReplayedCard-4, the manifest traps eviction

**Serves:** journal TOOL-aReplayedCard-4

What this pass is handed: the unit's spec at rev-1, which the round-1 audit called CLEAN with no
finding; the build README; and the manifest at `memory/guides/SESSION-KICKOFF.md`, whose
`### Environment traps` section is the population.

What it builds: one `memory/gotchas/` record per trap bullet whose body carries a token
`tools/memory-tree/gotchas.py`'s `ANCHOR_RE` recognises, the bullets deleted from the manifest, the
manifest re-stamped, `INDEX.md` re-rendered, every new record claimed under a dossier's
`gotcha-classes` key, and backlog rows `TOOL-aWeighedCompass-14` and `-15` flipped to CLOSED.

What is not obvious, each already measured:

- **The population is DERIVED, not the prompt's 22.** This run's probe with `ANCHOR_RE` over the
  section at base counted 22 bullets with an anchor token and 14 whose tokens name a tracked path.
  Re-derive at the pass, write the two numbers into the acceptance ledger, and for each of the
  eight that resolve to nothing decide per spec S2: rewrite the body to name the tracked file the
  trap is about, or leave the bullet in the manifest and say which in the ledger.
- **A record that names no gate fails check 18.** Every record carries one of the literal phrases
  `gated by`, `gated in`, `gated at`, `documented check` or `no machine gate`, as
  `gotchas.py`'s `DECLARES_RE` at its line 58 reads them.
- **A record whose anchors reach only append-only paths fails check 19**, and `UNIVERSAL_BUDGET` is
  5 and already spent, so no new record is `universal: true`.
- **Stage before you measure.** `gotchas.py --check`, the hygiene leg and the codebase-map
  coverage inventory read TRACKED files: `git add memory/gotchas/` first, then
  `python tools/memory-tree/gotchas.py --write`, then `--check`, then the dossier claims, then the
  coverage leg. Which dossier: the one whose feature the trap is about; `memory-tree-hygiene.md`,
  `agent-cap.md`, `session-kickoff.md`, `unattended.md` and `run-gates.md` already carry
  `gotcha-classes` lists to extend.
- **The manifest owes three stamps, not one.** `last-audit` and `last-body-change` both move
  because the body changed; the delta line goes in the commit message
  (`manifest-audit: delta <summary incl. deletions> · watch-commits-since-stamp: <n>`). Run
  `bash skills/session-kickoff/manifest-check.sh` before committing; check 11 caps a bullet at
  400 bytes, and the "evicted to the catalogue" sentence gains the new names.
- **Do not touch the dated-corrections section**, and do not lower the manifest below what
  `KICK-aReplayedCard-1` needs: it adds a `registry:` key to the audit block at order 2 and has
  3 B of headroom at base. Leave the freed bytes free.
- **The backlog is a shared mutable record**, which is why this unit runs alone at order 1. Flip
  the two rows' status in place with a closing note naming this unit; do not renumber or move them.
- **The acceptance ledger** is a `build/` record, `**Serves:** journal TOOL-aReplayedCard-4`, one
  `**Evidences:** TOOL-aReplayedCard-4` block, one line per AC in the OBSERVED form with a
  backticked token, per `memory/HYGIENE.md` "Acceptance ledger". Name the file
  `2026-09-14-build-TOOL-aReplayedCard-4-1-acceptance-ledger.md`.
- **Author files with the Write tool, never a heredoc**: a heredoc into python or sed corrupts
  backslashes silently, and this tree's data files are LF. Verify staged bytes with
  `git diff --cached --check`.
- **Finish with the records**: set the spec's status header to CLOSED with today's date, run
  `python tools/memory-tree/gen_build_index.py --write`, `git add -A memory/`, run
  `bash tools/memory-tree/check-memory-hygiene.sh` (minutes; never through `tail`) and
  `python tools/check-spec-tokens.py`, and commit with the unit id in the subject. No push, no
  merge.
