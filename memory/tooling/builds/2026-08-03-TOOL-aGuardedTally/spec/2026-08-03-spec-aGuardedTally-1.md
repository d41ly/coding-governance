# TOOL-aGuardedTally-1 — a dead reviewer must never read as a clean one

**Status:** INPROGRESS · rev-4 · 2026-08-03 · node a · Tier-2 · base 57d9b5460

## 1. Goal

`tools/workflows/tier2-review.js:128` returns `clean: 0 findings` when every finder agent has
*died*, because `finderResults.filter(Boolean)` drops a dead agent silently and an all-dead run is
indistinguishable from an all-clean one. Observed live on 2026-08-03: a review returned
`{"confirmed":[],"note":"clean: 0 findings"}` with `agents_done: 0` and four `ENOTFOUND` errors, and
the journal held four `started` lines and zero `result` lines. Close that, and port the small set of
project-agnostic gate lessons the same session produced.

## 2. Scope (IN)

- **S1** — Distinguish *no findings* from *no finders*. Count the lenses that actually returned; if
  any returned `null`, the run is partial and says so; if all did, it is `UNVERIFIED` and never
  `clean`. The return shape gains `lensesRun` and `lensesDead`.
- **S2** — Same treatment at `:164` (`all findings refuted`): a refutation verdict reached with dead
  skeptics is not a refutation. A finding with no verdict is UNVERIFIED, never refuted.
- **S3** — Port four project-agnostic rules into `parallel-coding-governance.template.md`: a guard
  sharing a variable with the thing it guards is not a guard; mutation-verify every gate; run a
  candidate gate predicate over the real tree before wiring it; a skip must announce itself.
- **S4** — Add `tools/gate-lint/` carrying two drop-in scans for any repo with `.ps1` files: a
  case-only identifier collision scan and a BOM check for non-ASCII scripts. Both mutation-verified
  upstream.

- **S5** — The harness must resolve, state and verify its review ROOT. Today it derives the diff
  from the process cwd and never reports which tree it read, so a run given one target can audit a
  different one and return confident, well-evidenced findings about code nobody asked about.
  Observed live 2026-08-03: a run briefed on `C:/projects/coding-governance` at `c47b5d2` reviewed
  the inCMS worktree it happened to be launched from and wrote its report there. The run was only
  salvageable because the wrong target happened to contain a real blocker. The resolved root goes in
  the returned object and in the report header, and when an explicit target is supplied and
  disagrees with the resolved root, the run refuses rather than silently preferring its default.

## 3. Non-goals (OUT)

- The inCMS gate runners, `gate-legs.json`, the slot pool and the pg autowire. Project-specific.
- Any change to `agent-cap.js` or the concurrency cap.
- Re-running the reviews whose verdicts this defect may have distorted. Their ids are recorded in
  §4 so the next reader can judge; re-running them is a separate call.

## 4. Design

### Data model

`tier2-review.js` returns one object. Today a caller cannot tell these three apart, and all three
render identically to an orchestrator that trusts `note`:

| Situation | Today | After |
|---|---|---|
| Every lens ran, found nothing | `clean: 0 findings` | `clean: 0 findings`, `lensesDead: 0` |
| Some lenses died, rest found nothing | `clean: 0 findings` | `partial: N/M lenses died` |
| Every lens died | `clean: 0 findings` | `UNVERIFIED: no lens completed` |

The third case is the dangerous one and is what fired. A caller reading `note` alone was told the
diff was clean by a run that reviewed nothing.

### Inventory

Known instances of this class, both in this harness family: the mis-keyed verdict join (a finder ref
a skeptic could not echo byte-identically joined to nothing, so every finding fell through to
not-confirmed and the run reported `precision 0.00`), and this one, transport death. Both share a
shape: **an absent result counted as a negative result.**

### Rollout

Pure additive change to a return shape plus template prose. No migration. Rollback is `git revert`.

### Reuse

`tools/workflows/tier2-review.js` is the existing seam and S1/S2 modify it in place rather than
adding a wrapper. S4's scans are net-new because `tools/` carries no lint kit today; they are
deliberately standalone scripts with no dependency on the workflow layer, so a repo can adopt one
without the other.

### Alternatives rejected

Throwing on any dead agent. Rejected because a single flaky lens should degrade a review, not abort
it; the caller needs the partial result and an honest label.

Leaving it to the caller to read `agents_done` from diagnostics. Rejected: the defect is that the
harness's own summary field asserts a conclusion it has not earned. Fixing the label is the fix.

## 5. Production-readiness checklist

- security — N/A, no credential or egress surface.
- perf / scale — N/A, a counter.
- a11y — N/A, no user interface.
- i18n — N/A, no user-facing copy.
- error / empty / loading states — this unit *is* the empty-versus-absent distinction.
- observability — the return shape gains the counts a caller needs to judge trust.
- risks — a caller keying on the literal string `clean: 0 findings` would see a new value. Grep
  shows the only consumers are orchestrator prose, so the blast radius is a human reading a summary.
- testing + left-shift gates — §7.
- migration / rollback — none; `git revert`.
- help/ docs — N/A, agent-facing tooling.

## 6. Acceptance criteria

- **AC1** — When every finder returns `null`, the harness returns a note containing `UNVERIFIED`
  and never the substring `clean`.
- **AC2** — When some finders die and the survivors report nothing, the note names the dead count
  and does not claim `clean`.
- **AC3** — When every finder runs and reports nothing, the note is `clean: 0 findings` with
  `lensesDead: 0`, so the fix does not manufacture false alarms.
- **AC4** — When a finding reaches the verify stage and no verdict comes back, it is recorded
  UNVERIFIED, not refuted.
- **AC5** — When the harness is given an explicit review root that differs from its resolved cwd
  root, it refuses and names both. When they agree, the report header states the resolved root and
  the sha it read.
- **AC6** — The case-collision scan reds against a file with two identifiers differing only by case
  and passes on a clean one; the BOM scan reds on a BOM-less non-ASCII `.ps1`. Both proven by
  injecting the defect, not by asserting on already-clean input.

## 7. Gates

`tools/gate-lint/` ships with its own self-test exercising AC5 in both directions. AC1 through AC4
are covered by a fixture harness that stubs the agent layer, since the real one needs network. Every
gate is mutation-verified: the test must be observed failing against an injected defect before it
counts.

## 8. Open questions

none — one fork, resolved.

- RESOLVED (unattended build, 2026-08-04) Fork 1: FOLD. Two copies of a review harness is how the
  mis-keyed verdict join survived in one and not the other, and this unit's own two misdirected runs
  used the inCMS-local copy while the fix landed here. The fold itself is NOT done in this unit and
  is owed as follow-up work; the decision is recorded so the next session does not re-litigate it.

### Owed, not blocking

The template §-stub pointing at domain-rules §14 could not land: `parallel-coding-governance.template.md`
is already within 366 bytes of its 32768-byte ceiling, and any stub overflows it. The gate is right
to refuse and explicitly says not to raise the limit, so §14 lives in `domain-rules.md` without its
pointer until someone trims the template. That the canonical template is full is a finding in its
own right — the same drift as its nine-vs-ten section canon lagging the downstream consumer.

## 9. Revision log

- rev-4 · 2026-08-04 · REOPENED from CLOSED. The closing review (12 agents, precision 0.79, root
  named as C:/projects/coding-governance at 02b1af4 — S5's root-logging working) found the status
  false. S2/AC4 is verbatim UNBUILT: tier2-review.js:197 drops dead skeptic batches uncounted and
  :201 derives `refuted` by subtraction, so a finding with no verdict is scored refuted and an
  all-skeptics-dead run returns `all findings refuted` with lensesDead 0 — the same false-all-clear
  this unit fixed at the FINDER stage, still live one stage downstream. S5's verify-the-root half
  and AC5's refuse-on-disagreement half are also unbuilt, and S4 ships inert: ps-hygiene.py is on no
  gate leg, in no CI, no adopt script, no doc, and scans zero .ps1 files here. Also: the reuse-audit
  adoption missed the DEPLOYED tools/memory-tree/SPEC-TEMPLATE.template.md that adopt-memory-tree.sh
  copies, TEMPLATE-SPEC.md now contradicts itself (ten at line 6, nine at 48/53/54), and check 12's
  excerpt post-pass diffs the nine-canon even when awk chose ten, so the primary new failure prints a
  blank diagnostic. Report: reviews/2026-08-04-review-aGuardedTally-1-closing.md.
- rev-3 · 2026-08-04 · partially BUILT. S1/S2/S5 in tier2-review.js, S3 in the template, S4 as
  tools/gate-lint/ps-hygiene.py with a --selftest that observes both scans failing AND passing.
  Root cause of the two misdirected reviews confirmed exactly: `const repo = a.repo || '.'` with a
  PROSE args string, so a.repo was undefined and the harness reviewed its own cwd. It now refuses
  a non-object args and logs the resolved root before any lens runs.
- rev-2 · 2026-08-03 · added S5 and AC5 after the rev-1 review audited the WRONG REPOSITORY: same
  family as the false-all-clear, a tool doing something other than what it was told and reporting
  success. Prior AC5 renumbered to AC6.
- rev-1 · 2026-08-03 · initial draft, from the live false-all-clear observed during
  `PERF-aCurbedStampede-1` on the inCMS repo.
