# TOOL-dUnstalledConvoy-24 — a LANDING evaluated in one tree has to travel, and the refusal has to say where it went

**Status:** CLOSED · rev-4 · 2026-08-21 · node d · Tier-2 · base d9728f89 · streams tooling

## 1. Goal

`--close` writes `LANDING` into the run-state file and STAGES it. Nothing commits it. A run that then
merges from another tree carries the older phase into the merge, and `--landed` refuses with check 31.

**rev-1 of this spec was wrong about why.** It claimed check 31 reports the COMMITTED phase while a
staged `LANDING` sits unseen in the index. `fact()` reads the file on disk, so check 31 reports the
WORKING-TREE phase and reported it truthfully. Verified against this build's own merge `c5da884`, whose
run-state file carries `phase: BUILDING` with nothing staged; `LANDING` first appears as a commit at
`8e1a81b`, in the other tree.

The real defect is that the LANDING evaluation is confined to the tree that performed it, and the
refusal — while accurate — names nothing that helps a run find it.

## 2. Scope (IN)

- **S1 — `--close`'s success message names committing the run-state file** as a step before the lander.
  It ends at "Land with: …" today, which reads as though nothing is outstanding. This is the only item
  that reaches the flow the incident actually took, and it is the primary fix.
- **S2 — check 31's refusal enumerates the other worktrees** and names any whose run-state file for
  this slug reads `LANDING`, so "your run is at BUILDING" becomes "this tree is at BUILDING; the LANDING
  is uncommitted in `<path>`". When no other tree has one, the message is today's, unchanged.
- **S3 — an arm per state, including the one that must NOT fire:** a genuinely un-closed run at
  `BUILDING` with no other tree holding `LANDING` gets today's message verbatim.

## 3. Non-goals (OUT)

- **Reading the staged blob.** rev-1's S1. `git show :<path>` returns the same value as the working
  tree for a clean tracked file, so the discriminator is empty in both trees of the recorded incident,
  and the state it was written for is producible by no verb in the kit. An arm pinning a state the kit
  cannot enter goes green while the trap stays — the shape this build has now shipped twice.
- **`--abort` parity.** rev-1's S3 assumed `--abort` reaches check 31. It does not: `refuse_if_terminal`
  fires check 26 first for an already-terminal record, and `--abort` is not a path to `LANDED` at all.
  The claim was inherited from a mental model, not from the source.
- **`--close` committing the phase itself.** The driver stages and the run commits; committing here
  would take an action the protocol reserves, at the moment the run is about to hand a clean index to a
  lander it controls.
- Changing what check 31 REQUIRES. A run still reaches `LANDED` only from a `LANDING` phase in the tree
  it is landing from. This unit changes what the refusal SAYS, never the bar.

## 4. Design

S1 is small and reaches the real flow. `--close` already prints the lander; adding the commit to that
same line costs nothing and removes the step whose omission caused the incident.

S2 is the half that helps a run already in the hole. `git worktree list --porcelain` is cheap, the
run-state path is derived from the slug the verb already holds, and reading each tree's copy is a file
read. The refusal keeps its verdict and gains the one fact a run cannot otherwise get: which tree
evaluated the Definition of Done. Without it the only recovery is to re-run `--close` on the merged
tree, which is what this build did at the cost of a full bar.

S3's negative arm is what stops S2 from swallowing the ordinary case. A run that never closed and a
run whose close is stranded elsewhere are different states, and the message must distinguish them or it
has replaced one misleading answer with another.

What this deliberately does not do is make the stranded state acceptable. A phase attests that `--close`
evaluated the Definition of Done in a specific tree; it does not transfer by being described. The
refusal stays a refusal.

## 5. Production-readiness checklist

- **security** — none. The refusal reads worktree paths already listed by git and its verdict is
  unchanged.
- **perf/scale** — one `git worktree list` plus one file read per other tree, on a refusal path.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — no other worktrees, a tree with no run-state file for this slug, or
  an unreadable one all fall back to today's message; S3's negative arm pins the first.
- **observability** — the refusal text IS the deliverable.
- **testing/gates** — the driver self-test plus the full bar. The cross-tree arm needs a second
  worktree in the fixture. The precedent is `tools/memory-recall/recall-opened.test.sh`, which does
  `git worktree add`; `adopt-unattended.test.sh` does NOT, and rev-2 named it from memory.
- **migration/rollback** — message-only, no state, no conf key. Rollback is a revert.
- **help/ docs** — `PROTOCOL.template.md`'s close-then-land sequence gains the commit step S1 names.

## 6. Acceptance criteria

- **AC1** — `--close`'s success message names committing the run-state file before the lander, observed
  in `tools/unattended/unattended.test.sh`.
- **AC2** — with a second worktree whose run-state file reads `LANDING` and this tree at `BUILDING`,
  check 31's refusal names that tree's path, observed in `tools/unattended/unattended.test.sh`.
- **AC3** — with this tree at `BUILDING` and no other tree holding `LANDING`, the refusal is today's
  message verbatim, observed in `tools/unattended/unattended.test.sh`. This arm is GREEN at base by
  construction, so it is a negative control and never evidence on its own; AC2 is the arm that
  carries the unit, and the two are asserted against the SAME fixture differing only in whether the
  second tree holds `LANDING`.
- **AC4** — the refusal still REFUSES in every case above; no arm asserts a stranded `LANDING` is
  accepted, observed in `tools/unattended/unattended.test.sh`.
- **AC5** — both new arms were observed RED against the pre-fix code, observed in
  `2026-08-21-build-TOOL-dUnstalledConvoy-24-1-red-first.md`.
- **AC6** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`bash tools/run-gates/run-gates.sh`. The unattended driver self-test is the leg that exercises this.

## 8. Open questions

- **F1 — should `--close` refuse to report success while its write is uncommitted?** RESOLVED (agent, 2026-08-21, delegated): no. It
stages, and that is its contract; a verb policing the caller's commit discipline would still be
defeated by a caller that does not commit. `--landed` is where the missing commit actually matters.

- **F2 — is the cross-tree read worth its cost when most runs use one tree?** RESOLVED: yes, and the
cost is bounded to the refusal path. A single-tree run enumerates one worktree and falls straight to
today's message, which AC3 pins.

## 9. Revision log

- rev-4 · 2026-08-21 · BUILT and closed. Both arms observed RED against a staged break before
  their fix; the record names which break per arm.
- rev-3 · 2026-08-21 · a second spec review found two AC defects. The worktree-fixture precedent
  named in section 5 was wrong — `adopt-unattended.test.sh` contains no `git worktree` call at all,
  and the real precedent is in the memory-recall kit. AC3 was stated as though it were evidence when
  it is green at base by construction; it is now labelled a negative control and tied to AC2's
  fixture so the pair discriminates instead of both passing for unrelated reasons.
- rev-2 · 2026-08-21 · re-grounded after a spec review returned BLOCKED. rev-1's premise that check 31
  reports the committed phase is false — `fact()` reads the file on disk — so its S1 discriminator was
  empty in both trees of the incident and its AC1 pinned a state no verb can produce. `--abort` parity
  was also wrong: check 26 fires first. S2 replaces the index read with a cross-tree one, which is
  where the missing LANDING actually is.
- rev-1 · 2026-08-21 · initial draft, written from the trap hit during `dUnstalledConvoy`'s own landing
  without verifying how check 31 reads the phase.

## 10. Reuse audit

`runmd_of` already derives the run-state path from a slug and `fact` already reads a phase out of one,
so S2 composes two existing helpers over a path list git supplies. No new helper unless S1 and S2 want
the same lines, which they do not — one is an echo and the other a refusal.
