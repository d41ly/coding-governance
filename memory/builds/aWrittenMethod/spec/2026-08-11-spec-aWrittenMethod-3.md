# TOOL-aWrittenMethod-3 — the method's displacement, at 247 of 250 lines

**Status:** SPECCED · rev-1 · 2026-08-11 · node a · Tier-1 · base 7f614a17 · streams tooling

## 1. Goal

`memory/guides/BUILD-METHOD.md` renders at 247 lines against hygiene check 6's 250-line cap. Three
lines of headroom on a document designed to grow is a red gate waiting for its first fold-in. Exercise
the displacement rule the method's own M1 states, so the rule is load-bearing rather than decorative.

## 2. Scope (IN)

- **S1** — move M5's probe-failure taxonomy (the exit-status, blind-layer, stale-hit and absent-tool
  paragraph) out of `tools/memory-tree/BUILD-METHOD.template.md` into `tools/memory-tree/README.md`,
  leaving in M5 a one-line pointer plus the two rules a reader cannot afford to look up: probes exit 0
  on a miss, and a hit can be stale.
- **S2** — re-render and land the guide at **≤225 lines**, giving at least 25 lines of headroom.
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

- **AC1** — When `wc -l memory/guides/BUILD-METHOD.md` runs, it reports at most 225 lines.
- **AC2** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` runs, it reports three
  pairs and exits 0.
- **AC3** — When M5 is read, it carries the two retained rules and a pointer naming
  `tools/memory-tree/README.md` and the section holding the moved text.
- **AC4** — When the spilled text is searched for in `tools/memory-tree/README.md`, every sentence
  moved is present; nothing was dropped in transit.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, it exits 0.

## 6. Gates

`tools/memory-tree/kit-dogfood-parity.test.sh` · `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/check-install-prefix.sh` (the README is a shipped file and may spell no root-install path).

## 7. Open questions

### F1 — spill M5's taxonomy, or M11's pointer list

M11 is longer, but it is the method's index and moving it makes the method point at a file that points
at files. **Recommendation: M5's taxonomy.** It is explanation rather than instruction, which is the
only safe thing to move, and M11 is what a compacted agent uses to find everything else.

## 8. Revision log

- rev-1 · 2026-08-11 · initial draft. Raised by unit 1 as `TOOL-aWrittenMethod-3` when the guide
  landed at 247 lines with the line axis binding and the byte axis comfortable.
