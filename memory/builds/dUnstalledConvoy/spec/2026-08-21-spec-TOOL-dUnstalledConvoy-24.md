# TOOL-dUnstalledConvoy-24 — a staged LANDING is a state the refusal can see, so it stops reading as a run that never closed

**Status:** SPECCED · rev-1 · 2026-08-21 · node d · Tier-2 · base d9728f89 · streams tooling

## 1. Goal

`--close` STAGES the LANDING phase and nothing commits it. A run that then merges from another tree
carries `BUILDING` into the merge, and `--landed` refuses with check 31 — reporting the COMMITTED
phase and saying nothing about the staged one sitting in the index. The refusal is correct and its
diagnosis is misleading, which is the worst combination a refusal can have.

## 2. Scope (IN)

- **S1 — check 31 reads the index as well as the tree.** When the committed phase is not `LANDING` but
  the STAGED run-state file says `LANDING`, the refusal names that state and says the phase is staged
  and uncommitted, rather than reporting the committed value alone.
- **S2 — `--close`'s success message names the commit as the next step**, in the same line that already
  names the lander. It currently ends at "Land with: …", which reads as though nothing is outstanding.
- **S3 — the same reading for `--abort`**, which stages a terminal phase by the identical path and has
  the identical trap. A fix that lands on one verb and not its sibling is the "more than one carrier"
  defect this repo has now hit twice.
- **S4 — an arm per state**, including the one that must NOT fire: a genuinely un-closed run at
  `BUILDING` with nothing staged still gets today's message, unchanged.

## 3. Non-goals (OUT)

- **`--close` committing the phase itself.** The kit deliberately never commits for the run: the run
  owns its commits and the driver stages. Committing here would take an action the protocol reserves,
  and it would do it at the one moment the run is about to hand off to a lander that expects a clean
  index it controls.
- Changing what check 31 REQUIRES. A run still reaches `LANDED` only from a committed `LANDING`, and
  the phase still attests that `--close` evaluated the Definition of Done. This unit changes the
  DIAGNOSIS, never the bar.
- Any change to the DoD set, the attestation verbs, or the landing anchors.

## 4. Design

The refusal today reads one source — the phase in the working tree — and reports it. The staged blob is
a second source that already exists, is already what the run needs to act on, and is already reachable
with `git show :<path>`. Reading it costs one command and turns "your run is at BUILDING" into "your
run has LANDING staged and uncommitted; commit it, then run `--landed`".

S3 is the load-bearing half of the scope rather than a courtesy. `--abort` reaches its terminal phase
through `set_fact` + `stage_or_fail`, exactly as `--close` does, so the trap is identical; and an abort
is the path a WEDGED run takes, which is precisely when a misleading refusal costs the most.

What this deliberately does not do is make the staged state acceptable. The phase is a machine-checked
attestation that the DoD was evaluated, and a staged-but-uncommitted attestation is not one — it can be
discarded by any `git restore` and leaves no record. So the refusal stays a refusal. It just explains
itself.

The negative arm in S4 is what keeps this honest: a run at `BUILDING` with nothing staged must still
get the ordinary message, or the new branch has swallowed the case it was written beside.

## 5. Production-readiness checklist

- **security** — none. The refusal reads one more source and its verdict is unchanged; nothing becomes
  reachable that was not.
- **perf/scale** — one `git show :<path>` per refusal, on a path already known. The refusal path is not
  hot.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — the staged blob may be absent (nothing staged) or unreadable (no
  index entry); both fall back to today's message rather than erroring, and S4's negative arm pins it.
- **observability** — the refusal text IS the observability here; that is the whole unit.
- **testing/gates** — the driver self-test, plus the full bar.
- **migration/rollback** — message-only, no state, no conf key. Rollback is a revert.
- **help/ docs** — `PROTOCOL.template.md` describes the close-then-land sequence; S2's message change is
  a step it should name, so the protocol's sequence line is checked and updated if it implies the phase
  is committed.

## 6. Acceptance criteria

- **AC1** — with `LANDING` staged and `BUILDING` committed, `--landed` refuses AND its message names the
  staged phase and the missing commit, observed in `tools/unattended/unattended.test.sh`.
- **AC2** — with `BUILDING` committed and NOTHING staged, `--landed` gives today's message unchanged,
  observed in `tools/unattended/unattended.test.sh`.
- **AC3** — `--close`'s success message names committing the run-state file as a step before the lander,
  observed in `tools/unattended/unattended.test.sh`.
- **AC4** — `--abort` carries the same staged-phase reading as `--close`, with its own arm, observed in
  `tools/unattended/unattended.test.sh`.
- **AC5** — the refusal still REFUSES in every staged case; no arm asserts a staged phase is accepted,
  observed in `tools/unattended/unattended.test.sh`.
- **AC6** — both new arms were observed RED against the pre-fix code, observed in
  `2026-08-21-build-TOOL-dUnstalledConvoy-24-1-red-first.md`.
- **AC7** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`bash tools/run-gates/run-gates.sh`. The unattended driver self-test is the leg that exercises this.

## 8. Open questions

**F1 — should `--close` refuse to report success while its own write is unstaged or uncommittable?**
RESOLVED: no. `--close` stages and that is its contract; a verb that policed the caller's commit
discipline would be doing the caller's job and would still be defeated by a caller that simply does not
commit. The refusal at `--landed` is the correct place to catch it, because that is where the missing
commit actually matters.

## 9. Revision log

- rev-1 · 2026-08-21 · initial draft, written from the trap hit during `dUnstalledConvoy`'s own landing
  on 2026-08-21, where the workaround was re-running `--close` on the merged tree at the cost of a full
  bar.

## 10. Reuse audit

`fact`/`set_fact` already read and write the run-state file, and the refusal already knows the path, so
this reads the staged blob of a path it holds rather than introducing a locator. No new helper is
needed unless S3 shows the two verbs want the same three lines, in which case one function in
`lib-unattended.sh` serves both — which is the existing seam, not a new one.
