# TOOL-aPromptedMandate-3 — the build method's research→test→choose section

**Status:** CLOSED · rev-3 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md](../reviews/2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md) | spec-audit | TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2 TOOL-aPromptedMandate-4 TOOL-aPromptedMandate-5 TOOL-aPromptedMandate-6 |
| [2026-08-18-review-TOOL-aPromptedMandate-1-tier2-diff.md](../reviews/2026-08-18-review-TOOL-aPromptedMandate-1-tier2-diff.md) | diff-review | TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2 TOOL-aPromptedMandate-4 TOOL-aPromptedMandate-5 TOOL-aPromptedMandate-6 |

<!-- /gen:spec-records -->

## 1. Goal

State the research→test→choose loop once, in the build method, so unit 4's directives can POINT at it
instead of restating it — which the method's own M1 forbids and the gate leg enforces by asserting
that every directive's cited section exists.

## 2. Scope (IN)

- **S1** — a new section `M12` in `BUILD-METHOD.template.md` and its render
  `memory/guides/BUILD-METHOD.md`: how a prose-started build finds candidate solutions, what it must
  TEST before choosing, and what the record of the choice is.
- **S2** — M1's stated budget rises, with the new figures and the reason written in place.
- **S3** — M5 gains a one-line pointer at M12 at its "no existing seam fits" branch, which is exactly
  where research begins.
- **S4** — *(struck at rev-2)* no kit version bump. `check-verdict-epoch.sh` fixes its subject as
  `check-memory-hygiene.sh` plus six named delegate modules; `BUILD-METHOD.template.md` is in neither
  set, so this unit moves nothing that gate scans and a bump would date no verdict. Bumping anyway
  would be worse than idle: `git grep 'gov:kit memory-tree@'` returns SEVEN live carriers, so a bump
  reds `check-kit-versions.sh` on `HYGIENE.template.md` and `SPEC-TEMPLATE.template.md` and then
  `kit-dogfood-parity.test.sh` on `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md` — four files this
  unit has no business touching.

## 3. Non-goals (OUT)

- **No renumbering.** M12 is appended rather than inserted next to M5, even though M5 is its logical
  neighbour. Inserting would renumber M6–M11 and break every `M<n>` pointer in the directive
  registry, the Skill table and the protocol — the leg joins those in both directions, so the blast
  radius is real and the gain is aesthetic.
- **No kit version bump, and no marker moves.** See S4. The marker stays where it is; the epoch rule
  is about gate ENGINES and this is a rendered guide.
- **No new rule about ordinary attended builds.** M12 governs the research a prose-started build owes;
  an attended build with a specced solution passes through it unchanged.
- Not a research METHODOLOGY. M12 states the obligation and the record; it does not prescribe tools.

## 4. Design

### Why a new section rather than widening M5

The owner ratified this at kickoff over the cheaper option. M5 is "Recall and reuse" and ends at "no
existing seam fits". Research-and-test is what happens after that answer, and it carries obligations
M5 does not — a candidate SET rather than a lookup, a test that discriminates between candidates, and
a recorded reason for the pick. Folding three obligations into a section about two probes makes M5
the thing M1 warns against.

### The budget

M1 currently states **≤20 KB, ≤250 lines** and the file measures 245 lines / 17460 B. **Re-measured
at `098bebd9` during the M7 reground: unchanged.** Main's only edit to this file since BASE was the
kit marker line, byte-for-byte; the budget figures, M1's stated constraint and M6's pass set are all
identical, so nothing below rests on a stale reading. The line budget
has five lines of headroom and M12 does not fit in five lines. M1 also states WHY the budget exists —
M7 re-reads the file whole at every pass boundary — so the raise is priced against that, not waived:

- new stated budget **≤22 KB, ≤290 lines**, with the reason recorded in M1 beside the figures
- the read-path ceiling is the second constraint and has room: `corpus_ids.py --report` measures the
  six read-path files at 90809 B against `READ_PATH_CEILING="112987"`, so 22178 B of margin against a
  growth of roughly 2 KB

### Migration

`BUILD-METHOD.md` is RENDERED from `BUILD-METHOD.template.md` and the pair is byte-compared by
`kit-dogfood-parity.test.sh`, so both move together or the bar reds. `check-method-carriers.sh`
grades files outside `memory/` that point at the method — a new section is a new `## M12` heading and
that gate's structural scan is what catches a copy of it landing elsewhere.

### Files touched (estimate)

`tools/memory-tree/BUILD-METHOD.template.md` · `memory/guides/BUILD-METHOD.md` · possibly
`.memory-tree.conf` if the read-path measurement moves against its ceiling. **Not**
`check-memory-hygiene.sh` — S4 is struck, so `KIT_MEMORY_TREE_VERSION` does not move and neither do
the seven `gov:kit memory-tree@` markers.

### What M12 must NOT do to M6

M6 closes the pass set at five and says "Nothing else is a pass". M12 states the research→test→choose
loop as work performed WITHIN the existing passes; it does not add a sixth pass kind. Unit 2's S4
resolves the same collision from the phase side, and the two must agree — this sentence is the
agreement, and M2's ordering axis is why it is written here rather than assumed.

## 5. Production-readiness checklist

- security — N/A
- perf / scale — the re-read cost M1 names; priced in §4 and stated in M1 itself
- a11y / i18n — N/A
- error / empty / loading states — N/A
- observability — the choice record M12 requires is what makes a research pass auditable at wrap-up
- risks — the template/render pair drifting (gated); the read-path ceiling (measured, 22 KB of
  margin); a directive pointing at a section that does not exist (gated, and observed firing during
  this build's own reproduction against a stub method)
- testing + left-shift gates — the parity test, the carriers gate, the verdict epoch, and unit 4's
  pointer join
- migration / rollback — none; M12 is additive and no existing pointer moves
- user docs — the method itself is the doc

## 6. Acceptance criteria

- **AC1** — When `memory/guides/BUILD-METHOD.md` is read, a `## M12` section states the
  research→test→choose loop and no other section restates it.
- **AC2** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, the template and the
  render agree.
- **AC3** — When `wc -l memory/guides/BUILD-METHOD.md` and `wc -c` on the same file are compared
  against the budget M1 states, the measurements match the stated figures and both are within them.
- **AC4** — When `bash tools/check-kit-versions.sh` runs, it is clean, and THIS BUILD's cumulative
  diff does not modify the `KIT_MEMORY_TREE_VERSION` line — S4 is struck, and the criterion observes
  that the strike held rather than that a gate nobody moved stayed quiet. **Keyed on the build's own
  diff, not on a literal value**: main moved the constant 2.21 -> 2.22 independently at `098bebd9`,
  so a criterion naming the value at `base 6517579f` would fail at landing for a reason that has
  nothing to do with this build.
- **AC5** — When `python tools/memory-tree/corpus_ids.py --report` runs, the read-path total is under
  `READ_PATH_CEILING`.
- **AC6** — When `bash tools/memory-tree/check-method-carriers.sh` runs, it exits 0.
- **AC7** — When M12 is read, it adds no sixth member to M6's pass enumeration, and M6's
  "Nothing else is a pass" sentence is unchanged from `base 6517579f`.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `bash tools/memory-tree/kit-dogfood-parity.test.sh` ·
`bash tools/memory-tree/check-method-carriers.sh` · `bash tools/check-kit-versions.sh` ·
`bash tools/unattended/check-unattended.sh` (check 16 resolves every directive's `M<n>`) ·
`bash tools/run-gates.sh`

## 8. Open questions

none — the forks below are RESOLVED.

- **Fold into M5, or a new section with a budget raise** — RESOLVED (owner, 2026-08-18): a new
  section, budget raised. Put to the owner at kickoff because M3's veto 2 makes a change to a
  governance carrier's stated constraint an owner turn rather than an agent one.
- **Append as M12, or insert beside M5 and renumber** — RESOLVED (agent, 2026-08-18): append, per
  §3's blast-radius argument.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the M4 spec audit. S4 struck and AC4 re-pointed: the verdict-epoch
  gate does not scan this unit's subject, so AC4 could not fail, and a bump at the stated two-carrier
  scope would have redded four other files (ids 10, 23). Added the M6 agreement sentence and AC7,
  which unit 2's S4 depends on.
- rev-3 · 2026-08-18 · M7 reground against `098bebd9`, which main advanced to after this build's
  BASE. AC4 was keyed to a literal `KIT_MEMORY_TREE_VERSION` value that main has since moved
  (2.21 -> 2.22); re-keyed onto this build's own diff. Budget figures re-measured and unchanged —
  main's only edit to the build method was the kit marker.

## 10. Reuse audit

Satisfied for the SET in unit 1's §10. The seam here is documentary rather than code: M5's existing
"no existing seam fits" branch is the entry point M12 continues, and M11's pointer table is the
existing mechanism for naming a carrier without copying it. Verified at rev-2 that
`check-verdict-epoch.sh`'s subject set does not contain this unit's files — the rev-1 claim that it
did was a stale reading of the gate, exactly the failure M5's staleness rule names. Verified against source rather than
against prose, per M5's staleness rule: the M1 budget figures and the 245/17460 measurement in §4
were taken with `wc` on the file at BASE, not read out of any document that describes it — and the
read-path figures from `corpus_ids.py --report`, not from the ceiling alone, which is the trap the
manifest front-loads.

