# TOOL-aRoutedQuill-1 — acceptance ledger

**Serves:** journal TOOL-aRoutedQuill-1

No merge bar and no self-test suite ran in this pass. The criteria were observed directly on node a,
in a `git clone --local` of the run branch under a short `%TEMP%\rq1` root carrying the built engine
and `SPEC_TIER1_CUTOFF="2026-10-10"`, with fixture specs staged there. The suite's ten new arms ran
as a scratch slice: their block alone, against the built engine, printed `n=10 st=0`. The generator's
`--selftest` ran whole and printed `PASS`. The close still owes `memory-hygiene self-test` and
`build-index selftest` run whole, `kit/dogfood doc parity`, and the other legs §7 names.

**Evidences:** TOOL-aRoutedQuill-1
- AC1 — `check-memory-hygiene.sh` — a SPECCED Tier-1 spec dated 2026-10-10 holding only its header and a `## 1. Revision log` logging rev-1 printed `(Tier-1 micro-spec sections, required at/after SPEC_TIER1_CUTOFF 2026-10-10; found by heading text, numbering free): missing: Goal, Scope (IN), Non-goals (OUT), Design, Acceptance criteria, Gates, Open questions`. Break, the base engine restored in the clone: no finding for it.
- AC2 — `Tier-2` — the eight sections numbered 1 to 8 printed nothing for the spec, and so did the same eight renumbered 1 to 4 and 6 to 9. The same body under a `Tier-2` header printed `## sections differ from the canonical ten` from `check-memory-hygiene.sh`.
- AC3 — `## 3. Non-goals (OUT)` — `check-memory-hygiene.sh` printed `empty: Design` for an emptied Design, `out of order: Non-goals (OUT)` when `## 3. Non-goals (OUT)` and `## 4. Design` swapped, and `not canonical: ## 9. Notes` for an added heading.
- AC4 — `check-memory-hygiene.sh --staged` — every observation above ran under `check-memory-hygiene.sh --staged` with only the fixture specs staged, which is the commit-time grade `TOOL-aRoutedQuill-2` relies on.
- AC5 — `SPEC_TIER1_CUTOFF` — with `SPEC_TIER1_CUTOFF` blank the AC1 spec printed nothing, and so did the same spec dated 2026-10-09 under the armed key. A full run over this tree, where every tracked spec predates the declared key, printed `the Tier-1 micro-spec arm graded NO spec — SPEC_TIER1_CUTOFF is 2026-10-10`.
- AC6 — `--tier 1` — `render_spec_skeleton` with `--tier 1` over the rendered `memory/TEMPLATE-SPEC.md` wrote the eight headings numbered 1 to 8, with `**AC1**` under `## 5. Acceptance criteria` and no readiness row. With each `FILL_MARKER` slot replaced, that file staged in the clone drew no check 12 finding. `--tier 2` output was byte-identical to the base generator over the base template. Break, the base generator over the new template: 24 headings, both fences merged.
- AC7 — `grep -n "SPEC_TIER1_CUTOFF" memory/TEMPLATE-SPEC.md memory/HYGIENE.md` — it hit the opening paragraph and the Tier-1 bullet naming the eight titles in `memory/TEMPLATE-SPEC.md`, whose Tier-1 fence holds exactly those eight headings, and the check 12 entry in `memory/HYGIENE.md`.
- AC8 — `check-memory-hygiene.sh` — a full run over this worktree with gov's declared `SPEC_TIER1_CUTOFF` printed no micro-spec finding on any tracked spec. 2026-10-10 is past the newest spec filename date on every local and remote ref, 2026-10-09.
