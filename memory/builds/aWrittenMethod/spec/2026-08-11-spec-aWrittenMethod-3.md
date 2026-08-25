# TOOL-aWrittenMethod-3 — the method's displacement, at 247 of 250 lines

**Status:** CLOSED · rev-3 · 2026-08-11 · node a · Tier-1 · base 7f614a17 · streams tooling · review wf_eb978bb2-f98

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-11-review-TOOL-aWrittenMethod-1-1.md](../reviews/2026-08-11-review-TOOL-aWrittenMethod-1-1.md) | diff-review | TOOL-aWrittenMethod-1 TOOL-aWrittenMethod-2 TOOL-aWrittenMethod-4 TOOL-aWrittenMethod-5 TOOL-aWrittenMethod-6 |
| [2026-08-11-review-TOOL-aWrittenMethod-1-2.md](../reviews/2026-08-11-review-TOOL-aWrittenMethod-1-2.md) | diff-review | TOOL-aWrittenMethod-1 TOOL-aWrittenMethod-2 TOOL-aWrittenMethod-4 TOOL-aWrittenMethod-5 TOOL-aWrittenMethod-6 |
| [2026-08-11-review-TOOL-aWrittenMethod-1-3.md](../reviews/2026-08-11-review-TOOL-aWrittenMethod-1-3.md) | diff-review | TOOL-aWrittenMethod-1 TOOL-aWrittenMethod-2 TOOL-aWrittenMethod-4 TOOL-aWrittenMethod-5 TOOL-aWrittenMethod-6 |

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/BUILD-METHOD.md` renders at 247 lines against hygiene check 6's 250-line cap. Three
lines of headroom on a document designed to grow is a red gate waiting for its first fold-in. Exercise
the displacement rule the method's own M1 states, so the rule is load-bearing rather than decorative.

## 2. Scope (IN)


**Landing order.** This unit is step three of five. The set lands `2 → 6 → 3 → 4 → 5`, fixed by the
audit `wf_eb978bb2-f98`: unit 6 rewrites the renderer unit 3 measures against, unit 3 creates a new
method carrier unit 4 must then enumerate, and unit 5 puts the method under a manifest ratchet that
would otherwise tax every earlier unit's commit. These are NOT parallel-safe under M6.

- **S1** — move BOTH displacements the backlog row named, not one. (a) M5's probe-failure taxonomy —
  measured at SEVEN lines (the guide's M5 spans 109-130 and the taxonomy is 123-129); and (b) M11's
  pointer list, ~14 lines. Target `tools/memory-tree/README.md`, APPENDED after existing content so
  the line-keyed waiver in `tools/install-prefix-waivers.txt` is not unpinned. M5 keeps a pointer plus
  the two rules a reader cannot afford to look up (probes exit 0 on a miss; a hit can be stale); M11
  keeps a pointer. **In the TEMPLATE the pointer is spelled `{{KIT_DIR}}/README.md`**, never a literal
  `tools/` path, which would red the install-prefix gate on a shipped file.
- **S2** — re-render and land the guide at **≤236 lines**, giving 14 lines of headroom. See §9: the
  225 estimate did not survive measurement, and the gap was closed by revising the number rather than
  by deleting instruction.
  Arithmetic, stated so the builder does not improvise deletions: 247 today, minus 7 for the taxonomy,
  minus ~14 for M11's list, plus ~4 for the two pointers ≈ 230; a further ~5 comes from tightening
  the paragraphs the moves leave stranded. Rev-1 scoped only the 7-line move and kept the 225 target,
  which was arithmetically unreachable — 247 − 7 + 3 ≈ 243.
- **S3** — record the achieved figure in the spec's §9 and in the build README, so the next author
  sees a number rather than a cap.

## 3. Non-goals (OUT)

No content is deleted. Displacement means it moves and stays reachable; a rule that vanishes is a
regression dressed as a budget. `tools/memory-tree/README.md` is outside the hygiene index set, which
is why it is the spill target — verified: check 6's index set covers `memory/**`, not `tools/**`.

No change to the cap. Raising a limit to fit the content is the move this repo's ethos forbids.

No restructure of M1 through M11. The section set and their numbering stay.

## 4. Design

M5 is the only section carrying a taxonomy rather than a procedure, which makes it the one place where
detail can leave without taking an instruction with it. The two rules that stay are the two whose
absence changes what an agent DOES: a probe exiting 0 on a miss makes "no output" an answer rather
than a failure, and a stale hit makes source the tiebreak. Everything else in that paragraph explains
WHY, and why can live one hop away.

The pointer in M5 must name the file and the section, because M7 re-reads the method whole and a
reader who cannot find the spilled text will re-derive it worse.

## 5. Acceptance criteria

- **AC1** — When `wc -l memory/guides/BUILD-METHOD.md` runs, it reports at most **236** lines.
- **AC1b** — When `bash tools/check-install-prefix.sh` runs, it exits 0, with the
  `tools/install-prefix-waivers.txt` row for `tools/memory-tree/README.md` re-keyed in the SAME commit
  if the append moved the line it is keyed on.
- **AC2** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` runs, it reports three
  pairs and exits 0.
- **AC3** — When the TEMPLATE's M5 and M11 are read, each carries a pointer spelled
  `{{KIT_DIR}}/README.md`; when the RENDERED guide is read, each reads `tools/memory-tree/README.md`.
  Two assertions, because the shipped side and the installed side are different files.
- **AC4** — When the spilled text is searched for in `tools/memory-tree/README.md`, every sentence
  moved is present; nothing was dropped in transit.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, it exits 0.

## 6. Gates

`tools/memory-tree/kit-dogfood-parity.test.sh` · `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/check-install-prefix.sh` (the README is a shipped file and may spell no root-install path).

## 7. Open questions

### F1 — RESOLVED (agent, 2026-08-11, delegated): spill BOTH, M5's taxonomy and M11's pointer list

**RESOLVED (agent, 2026-08-11, delegated): BOTH**, which is what the backlog row this unit came from
specified and what the 225-line target requires arithmetically. Rev-1 recommended M5's taxonomy alone
and kept a target that move cannot reach. M11 keeps a pointer in the guide, so a compacted agent still
finds the index in one hop — the objection rev-1 raised is answered by leaving the pointer, not by
leaving the list.

## 8. Revision log

- rev-3 · 2026-08-11 · BUILT on branch, unmerged. Landed at 236 lines and 16,459 B, against the
  hygiene caps of 250 and 20,480 — headroom 14 lines, up from the 3 this unit was raised for.
  **The 225 target did not survive measurement and the NUMBER moved, not the content.** Displaced,
  in two passes: M5's probe-failure taxonomy, M11's pointer list, the three self-labelled
  "*Judgment, not procedure*" asides, and M4's lens catalogue — every one of them explanation, with
  the rules that change what an agent DOES left in the method. Reaching 225 would have required
  cutting instruction, which §3 forbids and which unit 1 had already measured as load-bearing. The
  method's own M2 says to change the spec before diverging from it; this is that.
- rev-2 · 2026-08-11 · folded audit `wf_eb978bb2-f98`. BLOCKER: AC1's 225-line target was
  arithmetically unreachable from S1's scope — the taxonomy is seven lines, so the move lands at ~243
  — and reaching 225 by trimming would have deleted content §3 forbids and unit 1 measured as
  load-bearing. F1 re-resolved to BOTH displacements. Added the template-vs-rendered pointer
  distinction and the install-prefix waiver re-key.
- rev-1 · 2026-08-11 · initial draft. Raised by unit 1 as `TOOL-aWrittenMethod-3` when the guide
  landed at 247 lines with the line axis binding and the byte axis comfortable.
