# TOOL-dScriptedRepeat-13 — the bypass-flag guard covers the evidence records too, in the leg that can see them

**Status:** CLOSED · rev-5 · 2026-08-23 · node d · Tier-2 · base abd0f026 · streams tooling

## 1. Goal

Check 11 reds when a RUN-STATE file names the declared bypass flag, on the stated ground that a run
which wrote it is a run that considered using it. `recipe` mode added two more tracked writers — the
per-piece and set-scoped evidence records — and the driver guards both at the moment of writing. No
leg reads them afterwards. A bypass flag in a tracked evidence record is exactly as bad as one in a
run-state file, and today only one of the two is checked after the fact.

Round 2 offered two repairs and this build took the cheaper one: the refusal message stopped citing a
gate that did not cover it. That was honest and it is not the fix.

## 2. Scope (IN)

- **S1 — THE SCAN LANDS IN `check-playbook.sh`, not in check 11.** Rev-1 specced it into
  `check-unattended.sh`, which has no `GITLS`, no `declared_scalar` and enumerates no playbooks —
  measured, all three are zero there and non-zero in `check-playbook.sh`. Building rev-1 would have
  inlined a THIRD copy of the parser, which check 28 compares pairwise and structurally cannot police.
  The evidence-record scan is a NEW check in the leg that already enumerates playbooks, parses their
  `records` root and lists the records under it.
- **S2 — check 11 is untouched.** Two populations, two checks, each where its machinery already is.
  Run-state files stay with check 11 in `check-unattended.sh`; evidence records get the new check.
- **S3 — `check-playbook.sh` learns `BYPASS_BAN`.** It reads `.unattended.conf` for `PLAYBOOK_GLOB`
  only today, so this is a real new read and it is declared here rather than discovered in the diff.
  Absent or empty means the scan does not run, which is the existing convention.
- **S4 — the population is the one the census already built.** The roots come from the same parse the
  census uses and the records from the same `GITLS`. Not a second enumeration.
- **S5 — the widened pass reports its GRADED population**, in the shape `check-playbook.sh` already
  uses for its census note, so a scan that reached zero records says so instead of printing nothing.
- **S6 — the message softened in round 2 goes back to citing a gate**, now naming the new check rather
  than check 11. That sentence is currently true only because it stopped making a claim.

## 3. Non-goals (OUT)

- **Not widening to arbitrary tracked files.** The population is the DECLARED roots. A check that
  greps the tree for a flag string would red on this spec, on the backlog row and on the driver's own
  guard — the containment-tested-one-way shape, inverted.
- **Not checking untracked records.** This is about what LANDED.
- **Not touching the driver's write-time guard**, which is real and armed.
- **Not reading the records at a pinned BASE.** The driver derives its population from the run's BASE;
  this check derives from HEAD, because its question is what is in the tree NOW rather than what that
  run was authorized against. Stated because the two populations differ and a reader will assume they
  do not.

## 4. Design

A new check in `check-playbook.sh`, inside the existing per-playbook loop where `$rr` (the declared
records root) is already in scope. For each tracked record under `$rr`, grep for `BYPASS_BAN`. The
enumeration is the census's own `GITLS "$rr/*.md"`.

`BYPASS_BAN` comes from `.unattended.conf` through the same reader that already resolves
`PLAYBOOK_GLOB`; the new key is optional and its absence disables the scan.

**KNOWN GAP, stated rather than discovered.** `--record-set` takes a caller-supplied records root, so
a record written outside any declared root is unreachable by this check. That is the write-time
guard's job and it holds there; this check covers what a declared root contains. Recorded so the next
reader does not mistake the coverage for total.

## 5. Production-readiness checklist

- **Security** — a security check being widened. The write-time guard prevents; this detects what
  landed. Neither alone is the pair the charter asks for.
- **Observability** — S5's graded-population line, and a refusal naming the file.
- **Perf** — one grep per tracked evidence record over a list the leg already builds. Measured against
  `check-playbook.sh`'s own reading, not the sibling leg's, and reported whatever it is.
- **Migration** — none. No declared roots, no new work.

## 6. Acceptance criteria

- **AC1** — a tracked per-piece record containing the declared bypass flag reds under
  `bash tools/unattended/check-playbook.sh`, and the refusal names that file and calls it an evidence
  record. Armed in `tools/unattended/check-playbook.test.sh`.
- **AC2** — a tracked set-scoped record containing it reds the same way, armed in
  `tools/unattended/check-playbook.test.sh`.
- **AC3** — a run-state file containing it still reds through check 11 in
  `bash tools/unattended/check-unattended.sh` with its ORIGINAL message, and that leg's arms pass
  untouched.
- **AC4** — with `BYPASS_BAN` absent from `.unattended.conf` the scan does not run AND says so, so an
  empty population is distinguishable from a clean one. The `run-unattended-gates.sh --checks` output
  carries the graded count either way.
- **AC5** — the roots this check reads are the ones the census reads: an arm in
  `tools/unattended/check-playbook.test.sh` feeds one fixture playbook to both and reds unless the two
  return an IDENTICAL root list. Sharing is asserted, not liveness.
- **AC6** — the `seed()` fixture in `tools/unattended/check-playbook.test.sh` carries a tracked
  playbook with a declaration block AND a tracked evidence record under its declared root, committed
  into the scratch repo. Without this AC1/AC2/AC5 grade an empty population.
- **AC7** — the round-2 softening is reverted in `tools/unattended/unattended.sh` and the message
  cites the new check, with an arm in `tools/unattended/unattended.test.sh` that reds if the citation
  returns while the coverage does not.

## 7. Gates

`bash tools/run-gates/run-gates.sh` and `bash tools/unattended/run-unattended-gates.sh --all`.

## 8. Open questions

- **F1 — should this cover a records root declared by an ABORTED run's playbook?** RESOLVED (agent,
  2026-08-23, delegated): yes. The flag is about what landed; an aborted run's records are still
  tracked files, and scoping to live runs would make coverage depend on a phase the flag is unrelated
  to.
- **F2 — a new check number in `check-playbook.sh`, or an arm inside an existing one?** RESOLVED
  (agent, 2026-08-23, delegated): a new number. Its refusal is about a different subject than any
  existing check there, and folding it into one would make a single check's message ambiguous about
  which population failed — the class round 4 filed against the separator guards.

## 9. Revision log

- rev-5 · 2026-08-24 · the round-8 fold. Round 7's repair of blocker 3 traded a parse defect for a
  LIVENESS one: `_conf_key` sourced the file and then could not tell an undeclared key from a conf
  that aborted above the assignment, and `. file || exit 9` does not catch an `exit` inside the
  sourced file. It carries a sentinel the source must survive to print, plus a cross-check against the
  file's own text for the `return 0` shape. The sibling leg sourced the same file in its MAIN shell,
  so one `exit 0` ended it at rc 0 and run-gates read GATE ok — observed, and now it stops on a
  verdict. Round 7's class fix closed word-splitting and left C-QUOTING; `GITLS` pins
  `core.quotePath=false -z` and every consumer reads from a process substitution, because a NUL
  stream cannot ride a heredoc. The zero-teeth refusal moved per-root, its first cut being reachable
  only inside the kit's own fixture. Eleven arms, ten observed RED against the pre-fold code and one
  verified by probe. Full detail: `build/2026-08-24-build-TOOL-dScriptedRepeat-13-round8-fold.md`.
- rev-4 · 2026-08-23 · the round-7 fold. Three of the round's nine defects were this unit's check 10,
  and all three are one class: a guard reporting itself armed while its population, its literal or its
  count is not what the report claims.
  **BLOCKER 2** — the scan sat inside the `grain && records` block, and those are INDEPENDENT declared
  nulls whose only pairing refusal covers the reverse case. Blanking grain alone took the leg RC=1 ->
  RC=0 with the whole evidence corpus unread and a note saying zero. The scan is guarded on `records`
  alone now, one level out, with a PER-ROOT note; and the repo-wide zero reds instead of noting, because
  a declared flag over declared roots that read nothing is a check that cannot move.
  **BLOCKER 3** — this file was the kit's only reader resolving a conf key by `sed | tr -d '"' | head -1`
  while the driver, the sibling leg and the adopter all SOURCE it. `BYPASS_BAN='--no-verify'` kept its
  quotes here and lost them everywhere else; a trailing comment survived here and nowhere else. Either
  makes the scan grep for a literal no record can contain while printing that it read the corpus. It
  sources now, in a subshell, and the resolved value is ARMED — whitespace or a `#` reds.
  **HIGH 1** — `git ls-files` does not quote a path with a space, so an unquoted `for` split one record
  into two names that do not exist and `BYPASS_SEEN` incremented TWICE for the record it never opened.
  Fixed as a CLASS: all five enumerations over `ls-files` output in this leg read without splitting, and
  a record git tracks but the worktree lacks now reds rather than counting as read.
  **Seven arms, every one observed RED against the pre-fold leg and green against this one.**
- rev-3 · 2026-08-23 · BUILT. Check 10 lands in `check-playbook.sh` on the census's own `$rr` and
  `GITLS`; the real tree reads 3 tracked evidence records and finds nothing, and a flag appended to one
  of them reds it. AC5 is asserted by MOVING the declared root and watching both readers follow — its
  own control, a hardcoded root in the scan, reds the arm with the second-copy message. Both write-time
  refusals cite check 10 now, and an arm reds if that citation names a check the leg does not define.
- rev-2 · 2026-08-23 · the round-1 spec audit's BLOCKER 1 and three highs. The scan moves to
  `check-playbook.sh` because rev-1 specced it into a file with none of the machinery it claimed to
  reuse: `GITLS`, `declared_scalar` and the playbook enumeration are all zero in
  `check-unattended.sh` and non-zero in `check-playbook.sh`, so rev-1's §10 "Nothing new is
  introduced" was false and building it would have inlined a third parser copy past a pairwise gate.
  S3 now declares the new conf read. AC5 asserts SHARING rather than liveness, AC6 gives the fixture
  a playbook to find, and AC4 refuses an empty population silently passing. The HEAD-versus-BASE
  population difference and the caller-supplied-root gap are both stated rather than left to be
  discovered.
- rev-1 · 2026-08-23 · drafted, from round 2's better repair which this build deferred as another
  build's check with its own arms.

## 10. Reuse audit

`GITLS`, the declaration parse and `$PLAYBOOKS` all exist in `check-playbook.sh` and are used by the
census; this check reuses them in place. The conf reader there exists and gains one key. The bypass
guard's message grammar exists in the driver. Verified by counting each in both legs rather than
assumed — which is what rev-1 got wrong.
