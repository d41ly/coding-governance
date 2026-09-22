# TOOL-cBriefedPilot-13 — leg check 17, a waiver names a declared handle and was there in the first commit

**Status:** CLOSED · rev-3 · 2026-08-16 · node c · Tier-2 · base 37c05e1b · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-15-review-TOOL-cBriefedPilot-1-1.md](../reviews/2026-08-15-review-TOOL-cBriefedPilot-1-1.md) | spec-audit | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |
| [2026-08-16-review-TOOL-cBriefedPilot-1-2.md](../reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md) | diff-review | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |
| [2026-08-16-review-TOOL-cBriefedPilot-5-3.md](../reviews/2026-08-16-review-TOOL-cBriefedPilot-5-3.md) | diff-review | TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-22 TOOL-cBriefedPilot-23 |

<!-- /gen:spec-records -->

## 1. Goal

Grade every parked waiver line on the bar: the handle is one the kit declares, the reason is not
empty, and the line is present in the FIRST committed blob of the run-state file it sits in. The
first two are shape. The third is the owner's answer to P1, and it is the only part that survives
being re-run somewhere the run could not write.

## 2. Scope (IN)

- **S1** — check 17 inside the leg's existing per-run-state-file loop, selecting every line carrying
  the parked waiver grammar ` waiver · item ` followed by ` · reason `.
- **S2** — the handle is a member of the effective directive set, read through the same `core_of`
  parse arm A uses. An undeclared handle is a refusal.
- **S3** — the reason is non-empty. An empty reason is a refusal, because a waiver with no reason is
  indistinguishable from a waiver nobody meant.
- **S4** — the git join: the whole line, byte for byte, is present in the run-state file's first
  committed blob. The first commit is the oldest one that ADDED the path; the blob is read with the
  same pinned `GIT show <sha>:<path>` idiom check 13 already uses.
- **S5** — a run-state file that has never been committed is graded on shape and SILENT on the join.
- **S6** — the honest limit lives in a source comment beside the branch, matching check 13's
  precedent, not in a document read at a different time.
- **S7** — `tools/unattended/check-unattended.test.sh` gains a committing fixture and one arm per
  refusal beside the green control. **At least one arm's waiver line is PRODUCED by invoking
  `unattended.sh --preflight --waive <handle> --reason <text>` inside the fixture and committing it**,
  not hand-authored, and AC4 and the S4 join arm anchor on THAT line. `TOOL-aStandingWrit-8` names
  this exact gap — the kit has driver arms and leg arms and zero arms that run the driver and THEN
  the leg over one tree — and a hand-authored line tests the checker against the checker's own idea
  of the grammar; `ARMS_FLOORS` is raised in the same commit; the leg header's
  check count and the charter's gate-suite count move with it.

## 3. Non-goals (OUT)

- **Writing the waiver.** Unit 3 owns `--waive`, its five refusals and the `park()` call. This unit
  grades what that unit writes.
- **Extending the join to the other parked kinds.** `park()` writes four kinds and only one of them
  has the property this join tests. An `override` is written at `--close`, legitimately after many
  commits, and an `abort` reason likewise; joining either to the first blob would red every honest
  run. The waiver's whole claim is that it was taken at preflight, which is exactly why the join
  means something on it and nothing on the others.
- **Grading the reason's CONTENT.** Unit 3 refuses a reason spelling the bypass flag and a reason
  containing a newline, at the moment of writing. Re-asking either here would be a second answer.
- **A tamper check over the parked region as a whole.** The region is designed to grow. Only the
  waiver lines carry a "written once, at a known moment" property.
- **Claiming this is an authorization verdict.** It is not, and §4 says exactly why.

## 4. Design

### The grammar this reads

`park()` writes one line per entry: a UTC timestamp, the kind, ` · item `, the item, ` · reason `,
and the free text last. Unit 3's waiver kind therefore produces
`<timestamp> waiver · item <handle> · reason <text>`. The selector is the ` waiver · item ` literal;
the handle is the token between it and ` · reason `; the reason is everything after. Free text last
is not a style choice — a positional in a fail message cannot be armed, and a reason that could
contain the separator would make the parse ambiguous, which is why unit 3 refuses a reason carrying a
newline and why nothing after the reason is ever read.

### The git join

```sh
first=$(GIT log --diff-filter=A --format=%H -- "$f" | tail -1)
[ -n "$first" ] && GIT show "$first:$f" | grep -qF -- "$line"
```

Two properties make the whole line the right unit of comparison rather than the extracted pair.
Unit 3's re-preflight is idempotent — a byte-identical set is a no-op, so `park()` is not called
twice and the timestamped line never moves once written. And `grep -qF` over a blob is the cheapest
form there is, with no second parser to keep in step with the first.

`--diff-filter=A` with `tail -1` takes the OLDEST add, so a file deleted and re-added is still judged
against its original commit. Rename following is deliberately off: the leg's population is selected
at an exact path, so a renamed run-state file is a different file to every other check here too.

### What this buys, and what it does not

Run locally the join proves little, and the reason is the same one protocol §9 gives for everything
else in this kit: the run writes both sides. It can commit a waiver at pass 4 and the blob it is
compared against is a blob it also authored. What changes is that §9's *what actually binds* — the
same leg re-run in a clone the run never touched — finally has something to catch here. Before this
unit, a waiver appended at any moment was accepted on shape alone, and the ordering guarantee lived
entirely inside a driver that is not the only writer of the file, because `park()` is a bare append.
The owner bought that on 2026-08-14 and moved this unit to Tier 2 for it.

### Why an uncommitted run-state file is silent on the join

`stage_or_fail` puts the file in the INDEX, and the leg's whole per-run population is the index.
Between preflight and the run's first commit there is a live, tracked, uncommitted run-state file,
and every diff-scoped bar run in that window would red on a join with nothing to join against. The
cost is stated rather than hidden: a run that never commits the file evades this join entirely, which
is one notch weaker than §9's already-enumerated *a run that simply never creates a run-state file*.
The join is not the control that binds; §9 names the one that does.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/check-unattended.sh` | check 17 in the per-file loop; the header's check count |
| `tools/unattended/check-unattended.test.sh` | a committing fixture; one arm per refusal; the green control |
| `.memory-tree.conf` | `ARMS_FLOORS` for the leg, raised by the branch count |
| `AGENTS.md` | the gate-suite bullet's check count |

### Alternatives rejected

- **Hashing the parked region and pinning the hash.** The region is designed to grow, so the pin
  would have to move on every legitimate park, which makes it a value the run rewrites at will.
- **A `waivers:` run fact compared across the BASE.** Breaks protocol §2's seven-fact contract, and
  the BASE predates the waiver by construction — preflight pins one and writes the other.
- **Refusing when the file has no committed blob.** Reds the honest window described above, on every
  commit in it, with nobody reading.

## 5. Production-readiness checklist

- security — this is the security-shaped branch of the build, and its limit is stated in §4 rather
  than implied by the label. The leg stays READ-ONLY.
- perf / scale — two git invocations per run-state file that carries at least one waiver line, and
  none for a file that carries none. The population is at most one live run.
- a11y · i18n — N/A.
- error / empty / loading states — three refusals, each naming itself; the uncommitted case is
  silent by design and says so in source.
- observability — every refusal quotes the offending handle or line.
- risks — the run writes both sides; the join binds only off-machine. Recorded in the build README as
  a residual and repeated in the source comment, not softened in either.
- testing + left-shift gates — the fixture must COMMIT, which no existing arm in this self-test needs
  to do for its own sake; the committing helper is part of this unit's write set.
- migration / rollback — additive. A tree with no waiver lines is unaffected, which is every tree
  until unit 3's first waived run.
- user docs — protocol §10 is unit 18. The Skill's table (unit 9) is where the owner reads the
  handles.

## 6. Acceptance criteria

- **AC1** — When a parked waiver names a handle that is not in the effective directive set, the leg
  reds naming that handle.
- **AC2** — When a parked waiver carries an empty reason, the leg reds.
- **AC3** — When a well-formed waiver line is APPENDED to a run-state file after its first commit,
  the leg reds on the join naming that line.
- **AC4** — When the same line is present in the first committed blob, the leg is silent.
- **AC5** — When the run-state file has never been committed, the shape checks still run and the
  join prints nothing.
- **AC6** — The fixture's green control still exits 0 and prints nothing with check 17 live.
- **AC7** — `python tools/memory-tree/check-arms.py` is green with the branch armed and the floor
  raised, and RED when the branch is present and its arm is removed — twice over: once naming
  the unarmed branch, once at the armed count against the raised floor. *An UNRAISED floor does
  NOT red on an added branch: `ARMS_FLOORS` is a one-sided minimum, so a higher count passes.
  Measured on unit 4, where the same wording was an acceptance criterion no run could fail.*

## 7. Gates

`unattended gate selftest` · `unattended kit gate` · `harness arms` · the full bar.

**No leg is added** — check 17 rides `unattended kit gate`, so `tools/gate-legs.json`, the dossier's
`gate-legs` claim and the codebase-map re-render are untouched. Of the four gates a new leg would
trip, only the charter's gate-suite bullet moves, for its check count.

## 8. Open questions

### Silent or red when the run-state file has no committed blob? — RESOLVED at authoring: silent

The cost is written down. Red is the stricter reading and it reds the honest preflight-to-first-commit
window on every diff-scoped run, with nobody present to interpret it. The residual it leaves is a
weaker form of a hole §9 already enumerates, so the trade buys nothing it does not already concede.
This is the spec author's decision, not a fork the owner declined.

### The whole line, or the extracted `(handle, reason)` pair? — RESOLVED at authoring: the whole line
 The pair form needs a second parser over the blob, and the two parsers would then have to
agree about whitespace forever. The line is stable because unit 3's re-preflight does not re-park,
and `grep -qF` needs no parser at all.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`, folding FG-2 as the owner resolved it on
  2026-08-14 (P1: buy the git join). The design pass had this unit at Tier 1 with shape checks only;
  the join is what moves it.

- rev-2 · 2026-08-15 · §8's audit fold. S7 now requires at least one arm whose waiver line is PRODUCED by the driver and
  committed, not hand-authored, and §10 cites `TOOL-aStandingWrit-8` — the row naming this kit's
  driver-arms-and-leg-arms-but-never-both gap, which is exactly what the join needs closed.
- rev-3 · 2026-08-15 · the acceptance criterion asserting that an UNRAISED `ARMS_FLOORS`
  reds is corrected against measurement. It cannot: the floor is a one-sided minimum and a
  higher branch count passes. Found on unit 4 and swept across the set; three specs carried it.

## 10. Reuse audit

- **Check 13's blob read** — the seam. It already derives a path from the run-state file's own
  location and reads it at a recorded sha through the `GIT()` dereference pin, for the same reason:
  a sha is a name, and `git replace` or a graft file rewrites what it means. This check reads a
  different sha and the same way.
- **The per-run-state-file loop** — iterated with `read` and not word-split, after a tracked path
  containing a space silently removed a file from every check inside it. Check 17 joins the loop
  rather than opening a second pass over the same population.
- **`park()`'s kind discriminator** — already the thing that separates an abort reason from an
  override. The selector reads it rather than inventing a marker.
- **Check 13's honest-limit comment** — the precedent for where the limit goes: beside the branch,
  because a document stating it is read at a different time from the code relying on it.

The cross-component gap this unit's S7 closes for one line is `TOOL-aStandingWrit-8`, cited here
because §10 is where a reused seam is named and that row is the reason the arm has its shape.

Recall terms used: unattended waiver parked region park kind grammar run-state first commit blob git
show join tamper evidence shape check directive handle reason index population.
