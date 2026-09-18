# TOOL-cMendedVintage-12 — the brief reader stops waiting on a grandchild's write end

**Status:** SPECCED · rev-1 · 2026-09-18 · node c · Tier-2 · base 859daa67 · streams tooling · order 39

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-18-prompt-TOOL-cMendedVintage-12-2-build-brief.md](../prompts/2026-09-18-prompt-TOOL-cMendedVintage-12-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`read_brief_paths` assigns from a command substitution whose body is the `GIT` shell function, then
feeds a `while read` loop from a heredoc holding that variable. The substitution reads until EOF, EOF
arrives when the last inherited write end closes, and because `GIT` is a function the substitution
forks a subshell which forks `git` — so the reader waits on a grandchild's write end. `pass_commit`
one function below was repaired for exactly this on 2026-09-10 after the `unattended kit gate` leg
sat at zero CPU for 63 minutes. The reader it calls was not. Give it the same treatment.

## 2. Scope (IN)

- **S1** `read_brief_paths` reads the run-state file at a commit through a SCRATCH FILE and a
  redirect, never a command substitution and never a heredoc over its result, matching the shape
  `pass_commit` already uses and for the reason its header already records. Observed by AC1.
- **S2** A scratch file that cannot be created is a NAMED REFUSAL on stderr, never a silent empty
  answer. An empty brief set means "this pass declared no brief paths", which is a legitimate state,
  so a broken `TMPDIR` returning it would read as a correct answer. Observed by AC3.
- **S3** The shell-hygiene leg's predicate is widened to follow ONE assignment: a loop fed by a
  variable that was assigned from a command substitution is the same defect as a loop fed by the
  substitution directly. The leg refuses the direct form repo-wide today and this instance sat inside
  its blind spot for the whole of this build. Observed by AC2.
- **S4** The widened predicate is run over the tracked tree and every further instance is REPORTED
  with its file and line, so the population is known rather than assumed. Fixing only this one
  certifies coverage the repo does not have. Observed by AC2.

## 3. Non-goals (OUT)

- No change to what the openness scan COMPUTES. Which rows are open, and the supersession rule
  `TOOL-cMendedVintage-10` added, are untouched; this is about how one reader reads.
- No caching of the run-state file across commits, and no narrowing of the commit walk. Both would
  change the answer's inputs, and this unit must not move a disjointness verdict while repairing the
  mechanism that computes it. The COST of that walk is a separate, parked question.
- No change to `pass_commit`. It was repaired for this class already and its header is the
  specification this unit follows.
- No retirement of the heredoc form elsewhere. A heredoc over a LITERAL is not this defect; only a
  heredoc over a value that arrived from a forked substitution is.

### Edges

- **hands-off** external — every later unit of this build regains a usable `--dispatch`; nothing in
  this build reads the function.

## 4. Design

The recorded class is `memory/gotchas/bounded-through-a-pipe-is-unbounded.md`. `pass_commit`'s header
states the repair in full and the two properties that have to hold together: the walk runs in the
CURRENT shell so a `return` still returns from the function, and its output goes to a scratch file so
no pipe exists and no EOF has to arrive. `read_brief_paths` needs only the second, because it prints
rather than returning, but the same shape gives both.

WHY THIS WENT UNSEEN, which is the more useful half. The merge bar carries a leg that refuses a loop
fed by a command substitution, repo-wide. This loop is fed by a HEREDOC whose body is a VARIABLE, and
the variable was assigned from the substitution on the line above. The predicate does not follow the
assignment, so the instance was invisible to the gate written to catch it — a check that cannot fail
for the one shape it most needed to reach. S3 is therefore not a tidy-up; it is the left-shift, and
S4 measures what else was hiding in the same blind spot.

## 5. Production-readiness checklist

- security — none. The function reads a tracked file at a commit and writes only a scratch file under
  the caller's own temporary root.
- perf / scale — one `mktemp` and one redirect per call, replacing one fork of a subshell per call.
  It is a wash on cost and the point is termination, not speed.
- error / empty / loading states — an absent run-state file at that commit already yields an empty
  set through `|| true`, unchanged; an unreadable scratch root takes S2's named refusal.
- observability — the refusal names the function and what it could not do, which is the only thing
  that makes a broken temporary root visible; a stall names nothing, which is how this cost hours.
- risks — the real risk is a repair that changes which paths the function returns, because the
  disjointness verdict rests on them. `AC1` compares the returned set before and after on the same
  inputs, so a changed answer reds.
- testing — `AC1` to `AC3` run the function and the verb directly; `AC2` runs the widened predicate
  over the tracked tree. The permanent arms are declared in section 7.
- migration — none. No recorded data changes and no adopter receives a new field.
- user docs — none owed. The function is internal to the kit's library and no runbook names it.

## 6. Acceptance criteria

- **AC1** — For a commit and unit whose brief rows are known, `read_brief_paths` returns the same
  path set before and after the change, and a bounded `--dispatch` for a unit of this build COMPLETES
  and writes its row. Red when: the repair changes the returned set, in which case a disjointness
  verdict moved while the mechanism was being fixed.
- **AC2** — The widened shell-hygiene predicate REPORTS this instance in `lib-unattended.sh` before
  the repair and reports zero there after it, with every other instance in the tracked tree
  named. Red when: the predicate still only matches a loop fed directly by a substitution, which is
  the blind spot that hid this one.
- **AC3** — With the scratch root made unwritable, `read_brief_paths` prints a refusal naming itself
  on stderr and does not return an empty set silently. Red when: a broken temporary root is
  indistinguishable from a pass that declared no brief paths.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `shell hygiene (a loop fed by a command substitution)`

New arm: `tools/unattended/unattended.test.sh` · the function over a fixture run-state file, asserted
to return the same set and to refuse on an unwritable scratch root · the shell-hygiene registry gains
no row, because the repaired form is not a declared exception but an absence.

## 8. Open questions

- **Q1 — should this unit also bound the openness scan's cost?** RESOLVED (agent, 2026-09-18,
  delegated): no. The cost is rows times commits times run-state size and all three grow with the
  run; bounding it is a design question about what a run-state file is, which this run has already
  parked twice. This unit makes the scan TERMINATE. Making it cheap is somebody's next unit.

## 9. Revision log

- rev-1 · 2026-09-18 · initial draft, authored mid-build by the main loop after `--dispatch` exited
  on a one-hour bound at 11350 seconds having written nothing, three attempts having died the same
  way. Adopted under the protocol's discovery rule as a blocker between this run and its own landing.
  THIS UNIT IS BUILT WITHOUT A DISPATCH DECLARATION OF ITS OWN, because the verb that records one is
  the thing it repairs; the exception is recorded here and in the run's parked decisions rather than
  taken silently.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read a file at a commit into a loop without waiting on a forked write end"`
returns the seam and it is in the same file: `pass_commit`, twenty lines below, was repaired for this
exact class on 2026-09-10 and its header carries the reasoning, the measurement and the gotcha id. AN
EXISTING SEAM FITS, and the evidence is that the repaired function and the unrepaired one are
neighbours reading the same file for the same scan.

This unit therefore copies a shape rather than inventing one, and the only judgement in it is S3's:
that the gate which was supposed to prevent this needs to follow one assignment to see it.

Recall terms used: unattended dispatch openness scan brief paths command substitution heredoc write
end EOF grandchild scratch file zero CPU stall shell hygiene.
