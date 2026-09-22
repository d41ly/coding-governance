**Serves:** spec-audit TOOL-aGroundedOrientation-1 TOOL-aGroundedOrientation-2 TOOL-aGroundedOrientation-3

# Spec audit — aGroundedOrientation, round 1

Tier-2 spec audit over the build's three-unit spec set, node `a`, 2026-08-27. ROUND 1. Shape: raw 25, confirmed 6, refuted 19, unverified 0, precision 0.24.

Subjects, each pinned at the blob it was reviewed at: memory/builds/aGroundedOrientation/spec/2026-08-27-spec-TOOL-aGroundedOrientation-3.md@efcb23a6573ef4cfc6f706a7dccb9fba927e8c2f, memory/builds/aGroundedOrientation/spec/2026-08-27-spec-TOOL-aGroundedOrientation-1.md@c02532eb94f4c836cadfe169a2a236b13da5667a, memory/builds/aGroundedOrientation/spec/2026-08-27-spec-TOOL-aGroundedOrientation-2.md@35eff9e1e00ceee023a45e74747fdbcf78b9bc5f.

## Verdict: CLEAN WITH FIXES

Zero blockers, three highs, one medium. Every confirmed finding closes with a fold — a rev bump plus a §9 line on the spec that owns it — and none of them needs a new unit, a design change, or a promotion. The designs themselves hold; what fails is the OBSERVABILITY of two of them: unit 2's acceptance set cannot tell the mandated implementation apart from the alternative §4 explicitly rejects, and unit 3's AC1 is falsified by the very edit its own §1 scope mandates. Unit 1 drew no confirmed finding at all.

Three of the twenty-five raw findings (ids 8, 9 and 18, at three different severities) were the same defect in unit 3 §7. They are merged below as F4 and adjudicated ONCE, so the table's counts and the integers this review reports agree.

## Findings

| # | Sev | Unit · address | One line |
|---|---|---|---|
| F1 | high | 2 · §2 S1 vs §6 AC1-AC3 | The acceptance set greens on the whole-file grep §4 rejects. |
| F2 | high | 3 · §6 AC1 (and §1 S1's address) | An absolute line pin falsified by the edit S1 mandates. |
| F3 | high | 3 · §7 vs §4 | No declared gate can reach `check-memory-hygiene.test.sh`. |
| F4 | medium | 3 · §7 line 66 | `bash` on a python3 script — a gate line that cannot exit 0. |

---

### F1 — high — unit 2, §2 S1 (the `$psec` slice) against §6 AC1-AC3

**The defect.** S1 requires the new arm to live inside check 20's existing prompt-section slice, and §4's rejected-alternatives block names a whole-file grep for the two literals and refuses it: "The section slice is the point." Yet every criterion in §6 is satisfied by that rejected implementation. A whole-file grep REDs on AC1's staged ordering break, REDs on AC2's removal, greens on AC3's unmodified tree, and adds the same two `fail` call sites AC4's arm floor counts. AC1 says only that the leg REDs "naming both line numbers", which does not distinguish section-relative from file-absolute.

**Verified against.** `tools/unattended/check-unattended.sh:1747-1760` — check 20 slices `$psec` heading-to-heading and its arms compare section-relative line numbers.

**Why it matters here.** The one break the mandated implementation catches and the rejected one does not is the literal sitting OUTSIDE the prompt section, or a second start path carrying it instead — which is exactly the blindness N3 records check 18 already has and which check 20 exists to fix. For a unit whose entire product is a gate, that is a missing failing-case observation for the class it certifies. The charter's rule is that a new gate is not landed until its failing case has been observed; this observes two failing cases and not the one that separates the design from its alternative.

**Fix.** Add a criterion: with `RUN the orientation probes` present in the file but OUTSIDE the prompt section (moved into the mandate-path section in a scratch copy), the leg REDs with the vacuity message. That case separates the slice from the grep, and nothing currently in §6 does.

**Left-shift gate.** A spec-level check, cheapest as a new bug-class entry under `memory/gotchas/` selected for `memory/builds/*/spec/*.md`: *an acceptance set that cannot distinguish the mandated implementation from the alternative §4 rejects*. `gotchas.py --for-paths` already routes by path, so the class lands in every future spec audit over a spec file without new machinery. The machine-checkable form, if it earns its keep later: a spec carrying an "Alternatives rejected" bullet must carry a §6 criterion whose text names the discriminating observation.

---

### F2 — high — unit 3, §6 AC1 (and the address in §1 S1)

**The defect.** AC1's observation is `sed -n '1114p'` showing the guard. The implementation S1 mandates — "with a comment naming the measurement and the four sibling line numbers" — inserts that comment ABOVE the guard and shifts it down. AC1 is therefore falsified by a correct landing.

**Verified in the tree as it now stands.** `tools/memory-tree/check-memory-hygiene.sh:1113` is `alcut="${ACCEPTANCE_LEDGER_CUTOFF:-}"`, `:1114` is the first line of the new `TOOL-aGroundedOrientation-3` comment block, and the guard `if [ "$STAGED" = 0 ] && [ -n "$alcut" ]; then` sits at `:1121`. The spec is already INPROGRESS with that change present, so this is not hypothetical.

**Why it matters.** Check 23 grades the acceptance ledger for SHAPE and COVERAGE only — its own header says it never asserts the token names anything real. So a wrong AC1 gets answered by a claim line and nothing notices. The criterion will either be checked off against text that is false, or silently reinterpreted, and a criterion nobody can honestly run is not a criterion. The same brittle pin sits in S1's address.

**Fix.** Replace the absolute line number with a content observation: `grep -n 'STAGED" = 0 ] && [ -n "$alcut'` returns exactly one hit, and it is the `if` opening the acceptance-ledger block. Update S1's address the same way, or state it as `:1114 (pre-edit)`. The AMENDED ledger form exists for exactly this and is the legal route.

**Left-shift gate.** A cheap, exact predicate for the memory-tree spec check: refuse an absolute line-pin observation token — `sed -n '<N>p'`, `head -<N>`, a bare `:<N>` with no surrounding text — inside a §6 acceptance criterion, when that spec's own §2 edits the file being pinned. A criterion that names a line number in a file the spec is about to edit is falsified by its own scope, always, and the class is worth a named refusal rather than a review round.

---

### F3 — high — unit 3, §7 Gates, against §4 Design

**The defect.** §4 changes WHICH checks execute under `--staged`, but §7 names no run of `tools/memory-tree/check-memory-hygiene.test.sh`, and the one gate it does declare for the push boundary cannot reach that suite.

**Verified.** The suite exists and carries dedicated `--staged` arms whose own comment records that `in_scope` is the only thing deciding selection there, so no full-mode arm covers them. Its leg at `tools/gate-legs.json:224-233` is `"chunk": "selftests"` and `"subject": "kit"`. `tools/run-gates/run-gates.sh:756-758` holds every leg that is either, unless `GATE_SELFTESTS` is set, and the comment above it states outright that `GATE_FULL` deliberately does NOT ask for self-tests. `.githooks/pre-push:224` exports `GATE_FULL=1` and never `GATE_SELFTESTS`.

**Why it matters.** `bash tools/run-gates/run-gates.sh` at the push boundary therefore never runs the regression suite for the exact file this unit edits. A staged arm flipping red-to-green under the new guard lands unseen — and "coverage silently stops running" is the risk AC3 itself names as the one that matters here. Sibling unit 2's §7 names `check-unattended.test.sh` explicitly for precisely this reason; unit 3 omits its equivalent.

**Fix.** Add `bash tools/memory-tree/check-memory-hygiene.test.sh` (or `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`) to §7, and add a criterion asserting the suite's pre-existing `--staged` arms still pass with the guard in place.

**Left-shift gate.** Machine-checkable and narrow: for every path a spec's §2 scope names, if a tracked sibling `<path>.test.sh` or `<stem>.test.py` exists, §7 must name it. That is a set membership test over two sections of one file, it needs no judgement, and it catches the whole class — a spec editing a checker without declaring the checker's own suite.

---

### F4 — medium — unit 3, §7 Gates, line 66 (merges raw findings 8, 9 and 18)

**The defect.** §7 spells the gate `bash tools/memory-tree/check-arms.py --check`. That file is Python: line 1 is `#!/usr/bin/env python3` and line 2 opens a `"""` docstring. Run under bash it exits 2 with `line 35: fail: command not found` and an unterminated-quote parse error, having graded nothing. Sibling unit 2's §7 spells the identical gate `python3 tools/memory-tree/check-arms.py --check`, and `tools/gate-legs.json:350-359` declares its argv as `["python3", "tools/memory-tree/check-arms.py", "--check"]`. So unit 3 disagrees with both its own sibling spec and the manifest that owns the invocation.

**Why it matters.** A Gates line that cannot exit 0 whatever the tree's state is a DoD item that is either unmeetable or quietly ignored, and an ignored gate line in a landed spec is a gate a later reader believes ran. Two spellings of one command inside one spec set is also the second-spelling class this build is otherwise careful about — unit 1's N1 refuses a second spelling of the probe list for the same reason.

**Compounding, and worth one line in the fold.** The spec never says why check-arms is relevant to this change at all. `check-arms.py` grades `fail` BRANCHES; S1 adds a condition to an existing `if` and no new `fail` call site, so `ARMS_FLOORS`'s `tools/memory-tree/check-memory-hygiene.sh:20:20` is untouched. The line is both mis-spelled and unmotivated.

**Fix.** Spell it `python3 tools/memory-tree/check-arms.py --check`, matching unit 2 §7 and the manifest; or drop the line and state in §4 that the branch count is unchanged because no `fail` call site is added.

**Left-shift gate.** The tightest version costs a dozen lines in the memory-tree spec check: for each backticked command in a spec's §7 whose second token is a tracked script, assert the first token agrees with that script's shebang interpreter. It is a byte comparison against the file the command names, it cannot rot, and it would have caught this the moment the spec was written. The looser alternative — assert every §7 command matching a `tools/gate-legs.json` argv is spelled the way the manifest spells it — is also correct and covers the "two spellings of one gate" half directly.

## On the shape

Precision 0.24 over a 25-finding raw fan is low, and the reason is legible: the spec set is small, three files, one of them a single-scope-item unit, and a large lens fan over a small hardened surface manufactures refuted noise. Nineteen findings were refuted by the skeptic pass, three of the six survivors were one defect seen three times, and nothing came back unverified. A round 2 over the same three files should scale DOWN, not up — fewer lenses, and only after the four folds above are in.

Every finding above was re-verified against the tree at review time, not carried on the finder's word: line numbers were read from source, and F4's failure was reproduced at the shell.
