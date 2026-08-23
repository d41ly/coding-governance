# TOOL-dScriptedRepeat-13 — the bypass-flag guard covers the evidence records too, not just the run-state file

**Status:** SPECCED · rev-1 · 2026-08-23 · node d · Tier-2 · base abd0f026 · streams tooling

## 1. Goal

Check 11 reds when a RUN-STATE file names the declared bypass flag, on the stated ground that a run
which wrote it is a run that considered using it. `recipe` mode added two more tracked writers — the
per-piece and set-scoped evidence records — and the driver guards both at the moment of writing. No
leg reads them afterwards. A bypass flag in a tracked evidence record is exactly as bad as one in a
run-state file, and today only one of the two is checked after the fact.

Round 2 offered two repairs and this build took the cheaper one: the refusal message stopped citing a
gate that did not cover it. That was honest and it is not the fix.

## 2. Scope (IN)

- **S1 — check 11's population widens to the declared `records` roots.** The leg already parses every
  tracked playbook's declaration block, so the roots are derivable where it stands; nothing new is
  declared and no conf key is added.
- **S2 — the refusal names which KIND of file it found the flag in.** A run-state file and an evidence
  record are different states with different remedies, and one message for both sends a reader to the
  wrong file — this kit's own recorded class.
- **S3 — the derivation is LIVE, not a second copy.** The roots come from the same parse the census
  uses. A hand-kept second list of records roots would be the two-answers-to-one-question class in the
  gate written to close a hole.
- **S4 — the message that was softened in round 2 goes back to citing the gate**, because after this
  unit the gate covers what it claims. That sentence is currently true only because it stopped making
  the claim.

## 3. Non-goals (OUT)

- **Not widening to arbitrary tracked files.** The population is the DECLARED roots. A check that
  greps the tree for a flag string would red on this spec, on the backlog row, and on the driver's own
  guard — the containment-tested-one-way shape, inverted.
- **Not checking untracked records.** Check 11 is about what LANDED. An untracked file is not evidence
  and is not covered, and the check's header says so.
- **Not touching the driver's write-time guard.** It is real, it is armed, and it is the reason a
  landed record with the flag in it should be impossible rather than merely detected.

## 4. Design

Check 11 runs per run-state file today. It gains a second pass over `GITLS "$rr/*.md"` for each
declared root `$rr`, which is the same enumeration the census reader already performs — so the cost is
one more grep per record on a population the leg has already listed.

`BYPASS_BAN` is a declared conf value and may be empty; the existing `[ -n "$BYPASS_BAN" ]` guard
covers the new pass unchanged, so a project that declares no flag gets no new work and no new red.

## 5. Production-readiness checklist

- **Security** — this is a security check being widened. The threat is a landed record advertising a
  bypass that discarded the bar; the write-time guard prevents it and this detects it after the fact,
  which is the pair the charter asks for.
- **Observability** — the refusal names the file and the kind. Nothing else changes.
- **Perf** — one grep per tracked evidence record, over a list the leg already builds. Measured before
  landing; if it moves the leg's 13 s reading at all, that is reported rather than absorbed.
- **Migration** — none. A repo with no `recipe` playbooks has no declared roots and sees no change.

## 6. Acceptance criteria

- **AC1** — a tracked per-piece record containing the declared bypass flag reds check 11 under
  `bash tools/unattended/check-unattended.sh`, and the refusal names that file and says it is an
  evidence record. Armed in `tools/unattended/check-unattended.test.sh`.
- **AC2** — a tracked set-scoped record containing it reds the same way, armed in
  `tools/unattended/check-unattended.test.sh`.
- **AC3** — a run-state file containing it still reds with the ORIGINAL message, unchanged; the
  existing arm in `tools/unattended/check-unattended.test.sh` passes untouched.
- **AC4** — a repo declaring no `BYPASS_BAN` in `.unattended.conf` reds nothing new, and a playbook
  declaring no `records` root contributes no population.
- **AC5** — the roots the check reads are the ones the census reads: a fixture whose playbook declares
  a root reachable only through the declaration block is covered by `check-unattended.sh`, proving the
  derivation is live rather than a path convention re-implemented.
- **AC6** — the round-2 softening is reverted in `tools/unattended/unattended.sh` and the message
  cites check 11 again, with an arm that reds if the citation returns while the coverage does not.

## 7. Gates

`bash tools/run-gates/run-gates.sh` and `bash tools/unattended/run-unattended-gates.sh --all`.

## 8. Open questions

- **F1 — should the widened check also cover a records root declared by an ABORTED run's playbook?**
  RESOLVED (agent, 2026-08-23, delegated): yes. The flag is about what landed in the tree, and an
  aborted run's records are still tracked files. Scoping to live runs would make the check's coverage
  depend on a phase the flag has nothing to do with.

## 9. Revision log

- rev-1 · 2026-08-23 · drafted, from round 2's better repair which this build deferred as another
  build's check with its own arms. That reason expires now: the check and the arms are both in this
  kit and this session has been editing them all day.

## 10. Reuse audit

`GITLS` and the declaration parse both exist and are used by the census. The bypass guard's message
grammar exists in the driver. Nothing new is introduced.
