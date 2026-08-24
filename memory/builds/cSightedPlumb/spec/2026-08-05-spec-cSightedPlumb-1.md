# TOOL-cSightedPlumb-1 — the drift-audit kit: port record-vs-reality auditing out of inCMS

**Status:** CLOSED · rev-1 · 2026-08-05 · node c · Tier-2 · base 42c3f4dc · dogfooded, 3 legs wired

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Port the inCMS `ARCH-bCandidLoupe-2/-3` drift-audit tooling into a project-agnostic kit, so any repo
running this governance model can answer "do my own records still describe reality?" in seconds rather
than after a human notices something feels off.

## 2. Scope (IN)

- **S1** `tools/drift-audit/drift_report.py` — the engine. Five signal implementations, `--json`,
  `--check`, stdlib and git only. Every signal carries a `live` assertion.
- **S2** `tools/drift-audit/drift_signals.template.py` — the project layer: `PRODUCT_GLOBS`,
  `SHRINK_ONLY`, `HANDKEPT`, `PINS`, optional `CHARTER`.
- **S3** `tools/drift-audit/adopt-drift-audit.sh` with a `--check` sync arm for the merge bar.
- **S4** `tools/drift-audit/SKILL.template.md`, rendered by the adopt script to
  `.claude/skills/drift-audit/SKILL.md`, carrying the tier routing and the eight harness invariants.
- **S5** `tools/drift-audit/selftest.py` — the kit's own falsifiability test: every gateable signal
  exercised twice, silent on a clean fixture and firing on a minimal violating one.
- **S6** `tools/workflows/drift-audit-code.js` and `drift-audit-state.js` — the Tier-2 waves,
  generic over the adopter (every repo fact arrives via `args`).
- **S7** Dogfood on this repo: a filled `drift_signals.py`, measured pins, and three legs in
  `tools/gate-legs.json`.
- **S8** Wire the version contract: `KIT_DRIFT_AUDIT_VERSION` plus the README marker pair in
  `tools/check-kit-versions.sh`, and both workflow `meta.version` constants.

## 3. Non-goals (OUT)

- **A new conf.** The corpus root comes from `.memory-tree.conf`, which the memory-tree kit owns.
  There is deliberately no `--memory-root` flag: a second way to declare the same value is the
  hand-kept-second-copy defect the kit exists to detect.
- **Auto-remediation.** The kit reports; it never edits a record it is auditing.
- **Cross-node record edits.** The dangling-pointer signal is node-scoped, and the dogfood run left
  node `b`'s stale row alone — `b` owns that file.
- **Porting the inCMS findings.** Those are that repo's; only the mechanism travels.
- **Playbook or template changes.** The size-locked template is untouched; this is kit-only.

## 4. Design

### Data model

Engine owns the five signal implementations, which are generic over any repo following this playbook
(a memory tree, TEMPLATE-SPEC status headers, a per-node in-flight ledger, a node registry in the
charter). The project layer owns only what is genuinely repo-shaped, including the pins — a pin is
measured project state, not kit state.

| Signal | Gateable | Oracle |
|---|---|---|
| `ledger_rows_contradicting_git` | yes | a row claims an open state while naming a landed work sha |
| `non_terminal_specs_cited_by_product_source` | yes | a non-terminal spec's own id appears in product source |
| `shrink_only_lists_not_shrinking` | no | entry count today vs the count at the file's seed commit |
| `handkept_inventories_disagreeing_with_source` | yes | a project-supplied probe returning `(claims, actual)` |
| `dangling_pointers_in_own_ledger` | no | this node's ledger paths that no longer resolve |

### Inventory

Dogfood measurement on this repo at `42c3f4d`, after both oracle corrections:

| Signal | Value | Pin | Note |
|---|---|---|---|
| `ledger_rows_contradicting_git` | 1 of 9 | 1 | real: `in-flight/b.md:5` |
| `non_terminal_specs_cited_by_product_source` | 2 of 5 | 2 | both `INPROGRESS`, arguably accurate |
| `shrink_only_lists_not_shrinking` | 0 of 0 | n/a | DEAD PROBE — this repo ships no such list |
| `handkept_inventories_disagreeing_with_source` | 1 of 1 | 1 | charter names 10 of 22 legs |
| `dangling_pointers_in_own_ledger` | 0 of 0 | n/a | DEAD PROBE — no local paths in `c.md` |

### Migration

N/A — new kit, no existing artifact changes shape. Adopters install by copy, as with every other kit.

### Rollout

The kit is inert until an adopter fills `drift_signals.py`; `PRODUCT_GLOBS` empty means the spec
oracle finds nothing and reports its population honestly. The three legs wired here are green at the
seeded pins, so they can only red on regression.

### Files touched (estimate)

`tools/drift-audit/*` (new, 7 files) · `tools/workflows/drift-audit-{code,state}.js` (new) ·
`tools/gate-legs.json` · `tools/check-kit-versions.sh` · `AGENTS.md` ·
`.claude/skills/drift-audit/SKILL.md` (rendered) · `.gitattributes`.

### Alternatives rejected

**A `.drift-audit.conf`.** Rejected: `.memory-tree.conf` already declares the corpus root, and
memory-recall set the precedent of reading it rather than adding a second declaration.

**Scalars in the conf instead of a Python project layer.** Rejected: `HANDKEPT` probes are code, not
scalars, and `codebase-map`'s `map_extractors.py` is the established shape for project-owned code.

**Tolerance-zero gating.** Rejected: the spec oracle has a residual ambiguity (a forward reference, or
a legitimately-`INPROGRESS` built-but-unmerged unit) that would red the bar on correct work and train
`--no-verify`. A shrink-only pin drains the population without needing a perfect oracle.

**Comparing charter bullet COUNT to leg count** for the dogfood `HANDKEPT` probe. Rejected after
measuring: bullets legitimately group legs, so 12 vs 19 could never be equal and the probe was
permanently red — a decoration, not a signal. Comparing leg NAMES can legitimately reach zero.

## 5. Production-readiness checklist

- **security** — N/A — read-only analysis. Runs git and reads tracked files; takes no untrusted input.
- **perf / scale** — seconds on this repo; on a 419-spec adopter it measured ~30 s, dominated by
  per-sha `merge-base` calls. Full-mode leg, not a fast path.
- **a11y** — N/A — command-line output.
- **i18n** — N/A — internal tooling.
- **error / empty / loading states** — the whole point: an empty population reports `live: false` and
  prints DEAD PROBE rather than a clean 0. A missing project layer or conf is a refusal (rc 2).
- **observability** — `--json` for trending; the pins are the trend line, printed beside each value.
- **risks** — the real risk is a false all-clear, which the `live` field and the two-armed selftest
  exist to prevent. A secondary risk is a false positive redding an adopter's bar, which is why both
  field-observed false positives were fixed in the oracle rather than absorbed by a pin.
- **testing + left-shift gates** — `selftest.py` (19 checks) plus three wired legs. Both oracle
  corrections came from a real misjudged row and are recorded at the code, not just in this spec.
- **migration / rollback** — additive; delete the kit dir and the three legs to revert.
- **help/ docs** — `tools/drift-audit/README.md` plus the rendered Skill.

## 6. Acceptance criteria

- **AC1** When `python tools/drift-audit/selftest.py` runs, all checks pass, and each gateable signal
  is shown both silent on a clean fixture and firing on a violating one.
- **AC2** When a signal's population is empty, the report prints DEAD PROBE and not `ok`.
- **AC3** When `drift_signals.py` is absent, the report exits 2 with a refusal naming the template.
- **AC4** When `.memory-tree.conf` is absent, the adopt script refuses and names the memory-tree kit.
- **AC5** When the rendered Skill is hand-edited, `adopt-drift-audit.sh --check` exits 1 and diffs.
- **AC6** When a pin is lowered below its measured value, `drift_report.py --check` exits 1 and names
  the signal on stderr.
- **AC7** When `bash tools/check-kit-versions.sh` runs, the drift-audit constant and its README marker
  agree, and both workflow `meta.version` constants are present.
- **AC8** When `bash tools/run-gates.sh` runs, the three new legs are green.

## 7. Gates

New legs, all wired in `tools/gate-legs.json`: `drift-audit selftest` · `drift-audit wiring` ·
`drift-audit records`. Existing legs that must stay green: memory hygiene, kit versions, template
size, run-gates canary.

## 8. Open questions

none — the port shape followed the established kit conventions (`codebase-map` for the project layer,
`memory-recall` for the rendered-Skill/`--check` pair and the conf-reuse refusal), and every fork the
build met was resolved by measurement rather than preference. Two are recorded as decided rather than
open: the `HANDKEPT` probe compares leg NAMES because the bullet-count form was measured
permanently-red, and node `b`'s stale ledger row is pinned rather than edited because `b` owns that
file.

## 9. Revision log

- rev-1 · 2026-08-05 · initial spec, written after the build. Kit 1.0 built, dogfooded, selftested
  19/19, three legs wired. Two oracle corrections folded during the dogfood run, both from field
  false positives: a parity-comparison sha read as a work sha, and a bullets-vs-legs probe that could
  never agree.

## 10. Reuse audit

No reuse-lookup tool runs in this repo, so the pass was by reading the sibling kits — which is what
the tool would have been standing in for.

- **The conf parser** is a deliberate COPY of `codebase-map/map_lib.load_conf`, not an import: kits
  are copied into adopters independently, and importing across kit dirs would make drift-audit
  un-adoptable without codebase-map. `memory-recall/recall_conf.py` documents and follows the same
  reasoning, and the drift is gated by asserting the parser against a SHELL sourcing the same file —
  never against a second Python parser, since two operands from one generator assert nothing.
- **The project-layer split** copies `codebase-map/map_extractors.template.py` exactly: kit-owned
  engine, project-owned declarations, seeded once and never overwritten.
- **The rendered-Skill plus `--check` pair** copies `memory-recall/adopt-memory-recall.sh`.
- **The version constant plus README marker pair** copies the memory-tree and memory-recall assertions
  already in `tools/check-kit-versions.sh`.
- **The workflows** reuse `tools/workflows/tier2-review.js`'s harness shape — the bounded fan-out
  helper, the integer-keyed verdict join, the batched skeptic, the file-plus-summary return schema.
  Only the lens briefs and the scoping differ: that one reviews a diff, these audit a repo at a sha.

No new shared contract is introduced, so no new parity gate is owed beyond the three legs above.
