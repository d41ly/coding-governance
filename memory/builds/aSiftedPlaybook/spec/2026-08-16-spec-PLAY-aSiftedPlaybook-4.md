# PLAY-aSiftedPlaybook-4 — the companions stop contradicting their own contents

**Status:** SPECCED · rev-2 · 2026-08-16 · node a · Tier-1 · base 91ef1b05 · streams playbook

## 1. Goal

Correct three self-description defects in the two companion files, where each file makes a
mechanically false claim about its own structure. All three are measurable against the files
themselves, none changes a rule, and none is byte-gated — neither companion is under a size gate.

## 2. Scope (IN)

- **S1 — the placeholder arithmetic reconciles.** `parallel-coding-governance.customize.md:20-21`
  states "36 in total, and the two groups are **disjoint** — no placeholder appears in both files, so
  each one is filled in exactly one place", under headings claiming 23 in the template and 14 in the
  companion. Measured: 23 + 14 = 37 while the union is 36, because `{{MEMORY_ROOT}}` appears in
  BOTH files. Replace the disjointness guarantee with the true statement — one placeholder is
  shared and must be filled identically in both files — and keep the per-file counts, which are
  each individually correct. **State the intersection explicitly and by name** ("1 shared:
  `{{MEMORY_ROOT}}`"), not merely as prose about sharing: `TOOL-aSiftedPlaybook-3` S3 checks the
  named shared placeholder against the measured intersection, and it can only read a value the file
  actually states.
- **S2 — the shared placeholder is named where it is filled.** The template group at `:33-42` and
  the companion group at `:47-48` both list `{{MEMORY_ROOT}}`. Neither says the other one exists.
  Mark it in both places as the shared key, so an agent filling either group learns of the other.
- **S3 — the companion header's drop-shape claim matches the drop list.**
  `parallel-coding-governance.domain-rules.md:10-12` says "Four are droppable-per-project (§4, §9,
  §11 and §13, per the customize companion) and §1's unattended block is a fifth, line-scoped one",
  which asserts by contrast that the four are whole-section drops. `customize.md:69-71` drops only
  §9's "lines about outbound calls / stored HTML" and only §4's "harness lines". Restate the header
  so it distinguishes whole-section drops (§11, §13) from line-scoped ones (§1, §4, §9).

## 3. Non-goals (OUT)

- **Adding the 37th placeholder.** `{{DEFAULT_BRANCH}}` is `PLAY-aSiftedPlaybook-2`. This unit
  states the arithmetic correctly for the 36 that exist today; that unit re-states it for 37.
  Sequencing is in §4 Rollout.
- **Re-deriving the placeholder catalogue from source.** Making these counts machine-checked rather
  than hand-kept is `TOOL-aSiftedPlaybook-3`. This unit corrects the hand-kept text.
- **Re-numbering companion sections.** Every §-number an adopter's filled copy carries stays stable.

## 4. Design

### Inventory

The measurement, reproducible with the commands in §6:

| Set | Count |
|---|---|
| Unique placeholders in `parallel-coding-governance.template.md` | 23 |
| Unique placeholders in `parallel-coding-governance.domain-rules.md` | 14 |
| Intersection | 1 (`{{MEMORY_ROOT}}`) |
| Union | 36 |

The stated total of 36 is therefore correct and the two group headings are correct. Only the
disjointness sentence is false, and it is false in the direction that causes harm: it tells an
agent that filling a placeholder once is sufficient.

The consequence is bounded but real. `customize.md:14-16` already mandates
`grep -nE '\{\{[A-Z]'` over BOTH written files, so an unfilled `{{MEMORY_ROOT}}` in the companion is
caught downstream. The defect is that the disjointness claim argues against running that grep
carefully, and it is the only sentence in the file that describes the fill procedure's completeness.

### Files touched (estimate)

| File | Change |
|---|---|
| `parallel-coding-governance.customize.md` | S1 at `:20-21`, S2 at `:33-42` and `:47-48` |
| `parallel-coding-governance.domain-rules.md` | S3 at `:10-12` |

Neither file is under a size gate; `tools/check-template-size.sh` gates only the template.

### Rollout

Lands before `PLAY-aSiftedPlaybook-2`, which re-states the same sentence for 37 placeholders. If
that unit lands first, this one's S1 is rewritten against its text rather than against today's.
Either order is correct; this order avoids writing the sentence twice.

### Alternatives rejected

- **Delete the counts entirely rather than correct them.** Rejected: the counts are the file's only
  completeness check for a human reader, and the verification grep is a separate mechanism that
  catches unfilled placeholders, not missing catalogue entries. A catalogue with no count cannot be
  audited against the files at all.
- **Fold S3 into `PLAY-aSiftedPlaybook-3`** (the unwired-kits unit, which also edits companion
  prose). Rejected: that unit adds conditional-section rows and would make this correction's diff
  unattributable, which is M2's stated reason for one mechanism per spec.

## 5. Production-readiness checklist

- security — N/A. No write path, no surface, documentation prose only.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — N/A.
- risks — the only risk is the sequencing collision with `PLAY-aSiftedPlaybook-2` on the same
  sentence, handled in §4 Rollout.
- testing + left-shift gates — the arithmetic becomes machine-checked only in
  `TOOL-aSiftedPlaybook-3`. Until then this is a documented check, and §6 states its recipe. That is
  the honest disposition per domain-rules §10's documented-check rule, not a gap left unstated.
- migration / rollback — N/A. Prose edits, revertable by `git revert`.
- user docs — N/A. These files ARE the docs.

## 6. Acceptance criteria

- **AC1** — When the placeholder sets are recomputed, the file's stated arithmetic holds. The recipe:

  ```bash
  grep -oE '\{\{[A-Z_]+\}\}' parallel-coding-governance.template.md | sort -u > /tmp/t.txt
  grep -oE '\{\{[A-Z_]+\}\}' parallel-coding-governance.domain-rules.md | sort -u > /tmp/d.txt
  comm -12 /tmp/t.txt /tmp/d.txt        # must print exactly {{MEMORY_ROOT}}
  cat /tmp/t.txt /tmp/d.txt | sort -u | wc -l   # must print the total the file states
  ```

- **AC2** — When `parallel-coding-governance.customize.md` is read, no sentence claims the two
  placeholder groups are disjoint, and `{{MEMORY_ROOT}}` is marked as shared in both group listings.
- **AC3** — When `parallel-coding-governance.domain-rules.md:10-12` is read against
  `customize.md:69-71`, every section the header calls droppable carries the same drop shape
  (whole-section or line-scoped) in both files.
- **AC4** — When `bash tools/run-gates.sh` runs, it is green, and the template-size leg reports the
  template unchanged in size — this unit does not touch the template.

## 7. Gates

- `bash tools/memory-tree/check-memory-hygiene.sh` — this unit adds a spec and touches a build README.
- `python tools/memory-tree/gotchas.py --for-diff <base>..<head>` — run after the commit, per M6.
- `bash tools/check-template-size.sh` — must report an unchanged byte count.
- `bash skills/session-kickoff/manifest-check.sh` — no `watch:` path is touched, so no re-stamp is
  expected; run it to confirm that rather than assume it.
- No new gate. The left-shift for this defect class is `TOOL-aSiftedPlaybook-3`.

## 8. Open questions

none

## 9. Revision log

- rev-2 · 2026-08-16 · folded the spec audit `wf_4ed62ebb-cef`. S1 now requires the intersection to
  be stated by name, because `TOOL-aSiftedPlaybook-3` S3 was written to compare against a value the
  file never stated — a compare-against-nothing that would have passed vacuously.
- rev-1 · 2026-08-16 · initial draft. Placeholder arithmetic measured directly at BASE 91ef1b05
  (23 / 14 / 1 shared / 36 union) rather than taken from the audit narrative.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "governance playbook template companions"` returns no
seam for companion prose: the ranked candidates are `agent-cap.topLevelArgs`,
`kit-dogfood-parity.PAIRS` and the `template size <=32KiB` gate-legs key, none of which is a
mechanism this unit could extend. **No existing seam fits** — the unit edits two Markdown files and
wires through nothing.

Recall terms used, recorded per M5 so a reground can re-run the query:
`playbook template companion customize domain-rules agnostic adopter stale externalize byte gate
section stub kit wiring`. The query returned `PLAY-aCandidStub-1` (the same three files audited at
v2.5, CLOSED) as the binding prior record; its §2 S4 fixed an earlier instance of exactly the S3
defect — "Reconcile the companion header's 'All are droppable-per-project' against `customize.md`'s
four-section drop list" — which establishes that this header has now drifted from its drop list
twice. That recurrence is the evidence for `TOOL-aSiftedPlaybook-3` and is cited there.
