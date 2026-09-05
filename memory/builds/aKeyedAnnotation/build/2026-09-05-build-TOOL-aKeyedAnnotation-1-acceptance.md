<!-- **Serves:** journal TOOL-aKeyedAnnotation-1 -->
**Serves:** journal TOOL-aKeyedAnnotation-1

# aKeyedAnnotation unit 1 — acceptance ledger

One line per numbered criterion, in the two forms the ledger grammar allows and no third. Where a
criterion was found wrong at build time it is AMENDED and names the revision that changed it, which
is the form that keeps divergence visible instead of trusted.

**Evidences:** TOOL-aKeyedAnnotation-1

- AC1 — `bash tools/memory-tree/adopt-memory-tree.sh --scaffold` — run against a fresh local clone;
  the target tree holds the rendered annotation guide beside its rendered build-method sibling, and
  `cmp` against the template reports them identical. The first attempt proved the harness rather than
  the unit: a `--local` clone carries only committed content, so the run had to follow the commit.
- AC2 — `memory/guides/ANNOTATION-STYLE.md` — read after rendering. It carries the MUST/MAY/MUST-NOT
  list, the three number dispositions, the delete-the-id test and the voluntary-annotation statement
  with its reason, in four sections and nothing else. The charter's derived-count ban is NAMED where
  the dispositions resolve against it and is not restated.
- AC3 — `python memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py`
  — seven unresolvable product ids before the repairs and the same seven after, same members. No id
  that was not already present at BASE.
- AC4 — `tools/unattended/lib-unattended.sh` — and its sibling in the same kit's test file. Each
  repaired block now names its evidence in prose and carries the id on a trailing line of its own, so
  deleting that line leaves the incident, the controls and the reasoning intact.
- AC5 — amended rev-6 — the criterion, and the scope item behind it, both asserted facts the tree
  refutes. It said TWO bug-class records absorbed comment prose verbatim and that the design pass
  named them. Measured: exactly ONE record at a 60-character threshold and the same one at 90, so the
  count is not a threshold artefact, and that design record names no bug-class file at all. `git log
  -S` over the shared run returns the SAME commit for the record and the call site, so the direction
  the item claimed git established does not exist either. The record was trimmed to its class, its
  incident and its reach, with the mechanism left at the call site that acts on it. Section 9 logs it.
- AC6 — `bash tools/run-gates/run-gates.sh` — the full bar, which binds at the close rather than per unit and is
  recorded there for all four units. The diff-scoped gates this unit touches were green at its
  own commit: memory hygiene, spec tokens, codebase-map coverage, gotchas, drift-audit records,
  kit versions, kit/dogfood parity, method carriers and the staged manifest ratchet.
- AC7 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — four pairs after this unit against
  three at BASE, and a divergence staged into the rendered guide REDS it. Both readings taken.
- AC8 — `bash tools/memory-tree/check-method-carriers.sh` — green, 15 carriers, with no skip case
  added to either of the two files that keep an exclusion list over the build-method filename. The
  template does not spell that literal at all, which is why neither needed one.
- AC8b — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — the pair-list carrier observed both
  ways. With the row present and a divergence staged, exit 1. With the row deleted and the SAME
  divergence still in place, exit 0 over three pairs: the silent miss, seen rather than argued.
  Restored to four pairs green.
- AC8c — amended rev-7 — its earlier form demanded that deleting the descriptor's rendered stanza
  make a deployer run REFUSE. Measured with `python tools/govkit/govkit.py selfcheck`: exit 0 with the
  stanza and exit 0 without it, because the deployer walks rows already declared rendered and an
  absent stanza declares nothing. The two guard rows are observable only through which legs a scoped
  run selects, which costs a full bar on a single-file diff. So three of the four carriers have no
  mechanism behind them, and the criterion now records that gap with its compensating manual check
  rather than asserting a refusal that does not exist. Section 9 logs it.
- AC8d — `python tools/codebase-map/test_codebase_map.py` — exit 0. The three keys this unit minted
  are claimed by dossiers rather than baselined: the rendered guide by a new dossier for this
  feature, and the two new bug-class records by the features that own their subjects. Observed RED
  first, naming all three as unclaimed.
- AC9 — `git grep -o -E` over the memory root for the foreign build's ids, sorted and compared
  against the same command at BASE — byte-identical, 35 ids, with the same three-seq gap. That is the
  clause that catches a head-anchored citation, which the orphan count structurally cannot see.
  `python tools/memory-tree/corpus_ids.py --report` reports 0 orphans, which is the separate clause
  for the body case.
