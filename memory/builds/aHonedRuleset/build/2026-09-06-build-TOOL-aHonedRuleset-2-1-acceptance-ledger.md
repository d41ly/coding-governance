# Acceptance ledger — TOOL-aHonedRuleset-2

**Serves:** journal TOOL-aHonedRuleset-2

Tier-2 · node a · 2026-09-06

Three sentences left the charter's §16 grammar paragraph — the joiner rule, the parentheses rule and
the colon rule — each mapping one-to-one onto a numbered `fail` arm of `tools/check-microformats.sh`.
One connective replaced them. Every surviving sentence's words are byte-identical; only line breaks
moved. The census had estimated 900–1150 bytes for this cut; the measurement returned 126 per
carrier, because only three of the paragraph's eleven sentences map to a predicate.

## Acceptance criteria

**Evidences:** TOOL-aHonedRuleset-2

- AC1 — MET — `grep -c` for `appears exactly ONCE`, `except markdown-link syntax` and
  `glued to a value, as a port` over both `coding-governance-agents.template.md` and `AGENTS.md`
  returns 0 for all six
- AC2 — MET — `git diff --word-diff` over the template shows exactly the three cut sentences removed
  and the one connective added, and no other changed token
- AC3 — MET — squeezed to one line first, `Five glyphs are pinned as STRUCTURE` and
  `R1 — an emitted micro-format is a markdown list item` each occur exactly once in each carrier, all
  four counts 1. The squeeze is load-bearing: a raw grep grades the wrap, and at base the first
  phrase returned 0 in both carriers because it straddled lines 369–370
- AC4 — MET — `bash tools/check-microformats.sh` exits 0 printing
  `microformats OK — 11 definition(s) graded, 11 keyword(s) derived`, unchanged from the pre-edit run
- AC5 — MET — `bash tools/check-template-size.sh` reports the template at 49018 / 49152,
  **134 bytes under**, against the 8 measured before this unit. More than 100, as asked
- AC6 — MET — `AGENTS.md` measures 64355 / 64512, **157 under**, and its delta from base is 126,
  equal to the template's, because the paragraph is byte-identical in both
- AC7 — MET — `bash tools/playbook/adopt-playbook.sh --target . --check` exits 0, proving `AGENTS.md`
  was regenerated rather than hand-edited
- AC8 — MET — `bash tools/check-playbook-parity.sh` exits 0 printing `pairs in agreement`, so none of
  the five S2 extractions was disturbed
- AC9 — MET — the longest re-wrapped line is **100 characters**, measured NOT with `awk`,
  against a documented ceiling of 102. The decode matters: awk counts BYTES here and the
  range carries multi-byte pinned glyphs, so it would over-report
- AC10 — MET — `git diff -- tools/template-size-highwater.txt` is empty on this unit's commit: no
  `--bump` was taken to make a shrinking file look intentional
- AC11 — **NOT MET AS WRITTEN**: `bash tools/run-gates/run-gates.sh` came back RED, and it
  is recorded rather than glossed. Four legs failed. Three reproduce at base
  `6ec402bd` — the `.lexicon.conf` LANGS ratchet, an already-over-pin drift list, and a
  `pass-order` TIMEOUT under contention — and the fourth was hygiene check 23, which this
  ledger and its five siblings exist to answer. No leg failed on this unit's own subject
- AC12 — MET, **in BOTH halves**. With the template staged ALONE, `manifest-check.sh` exits
  1 naming check 5 and the
  template; with the `memory/guides/SESSION-KICKOFF.md` re-stamp bundled it exits 0. The
  failing half is what makes S5's obligation proven rather than assumed

## Later movement on this unit's subject

The closing diff review found that the charter's §1 merge-exception parenthetical still stated the
stamp rule `TOOL-aHonedRuleset-5` retired. That is a different §1 sentence from this unit's §16
paragraph and was fixed in the closing fold, not here; it is recorded because both edits land in the
same two carriers and a later reader diffing them should know which unit moved which byte.
