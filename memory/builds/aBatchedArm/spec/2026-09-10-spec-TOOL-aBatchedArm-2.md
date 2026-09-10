# TOOL-aBatchedArm-2 — the structural group linter over the batched self-test

**Status:** OPEN · rev-1 · 2026-09-10 · node a · Tier-2 · base e9ed269b · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aBatchedArm-1` states a partition rule its conversion cannot enforce per group: once a batch is
written, nothing downstream re-asks whether its control arms still witness anything. Add one
structural linter over `tools/unattended/check-unattended.test.sh` that grades the LINKAGE between a
group's `emitted` set and the arms inside it, so a mis-grouped control REDS instead of passing green
over a branch that was never evaluated.

## 2. Scope (IN)

- **S1** — a linter that parses each `reset_tree`-delimited group in the suite and reds on rule A:
  a group carrying a `miss` or `same` assertion against a check number the group's `emitted` set does
  not name. Observed by **AC1**.
- **S2** — rule B: a group carrying more than one arm whose assertion TEXT is identical, so one break
  cannot satisfy two assertions. Observed by **AC2**.
- **S3** — rule C: a group carrying a `run` capture assigned to anything other than that group's own
  `out`, which is a poisoned baseline. Observed by **AC3**.
- **S4** — a header stating what the linter does NOT grade, and a LIVENESS line naming the group count
  it parsed, so a run that parsed nothing cannot report clean. Observed by **AC4** and **AC5**.
- **S5** — one gate-manifest row in `tools/gate-legs.json`, `subject = kit`, beside the suite it
  grades. Observed by **AC6**.

## 3. Non-goals (OUT)

- **Grading whether a group's assertions are ADEQUATE.** The linter reads linkage: that a control's
  check is named, that no two arms share a text, that no capture is foreign. Whether the arm proves
  anything is a reader's question and the header must say so, or a structural check reads as a
  semantic one to everybody who did not write it.
- **Parsing the checker.** The linter reads the TEST file only. Which branches exist is
  `check-arms.py`'s question and is already answered.
- **Repairing existing violations.** It reports them; `TOOL-aBatchedArm-1`'s conversion fixes them as
  it goes. A pre-existing violation count is recorded as the starting figure, never waived.

### Edges

- **consumes-from** `TOOL-aBatchedArm-1` — the `emitted` helper and its argument grammar, which rule
  A parses. Without it there is no set to link against and every group reds.
- **hands-off** `none`

## 4. Design

### Data model

A group is the text between one `reset_tree` call and the next, which is the same delimiter
`TOOL-aBatchedArm-1` batches on, so the two cannot disagree about where a group starts. Within a
group the linter extracts: the `emitted` argument if present, each `hit`/`miss`/`same` call with its
helper name and its literal text, and each `$(run` capture with its assignment target.

### The three rules

| Rule | Reds when | Round-1 finding it left-shifts |
|---|---|---|
| A | a `miss` or `same` names a check outside the group's `emitted` set | 18, 25, 10 |
| B | two arms in one group carry an identical assertion text | 26 |
| C | a capture in a group is assigned to a name other than that group's `out` | 21 |

Rule A is the load-bearing one and it encodes the admissibility rule
`TOOL-aBatchedArm-1` §4 states: a control is admissible only when the check it is silent about is one
the group makes fire, so the firing witnesses that the branch was reached.

**Rule A needs the check number of a `miss`, and the arm does not carry one.** The text does. The
linter resolves text to check number by the same join `check-arms.py` uses — the interpolation-stripped
`fail N "…"` signatures from `check-unattended.sh` — and a text it cannot resolve is REPORTED as
unresolved rather than skipped, because a silently unresolved control is the exact class this unit
exists to close.

**That join carries a known truncation and this unit inherits it rather than discovering it.**
`memory/map/features/testsuite-counts.md` records that a signature runs to the FIRST interpolation,
"so lengthening a message always strands it while shortening never does, and the sibling test still
quotes enough of the old sentence to look correct" — the `arm-literal-strands-on-message-edit` class,
caught three times in one file in one session. For rule A the consequence is bounded and is the safe
direction: a stranded literal resolves to NOTHING, which this unit reports as unresolved rather than
passing. It never mis-attributes a control to the wrong check; it declines to attribute it at all.

**And `check-arms.py` cannot see this class itself**, which is why the join is borrowed rather than
the whole gate. `TOOL-aTimedTurnstile-7`, OPEN: "check-arms.py forbids absence-only arms yet cannot
see this class — its population needs a `fail() {` helper and excludes `*.test.sh`". A test file is
outside its population by construction, so nothing today grades what rule A grades.

### What it does not grade, and why that goes in the header

Adequacy, reachability of a branch the suite never names, and whether a `hit` proves what its author
meant. A gate's own header owes its gaps (`AGENTS.md` §7), and this one's gap is wide: it can say a
control is LINKED to a firing check and never that the control is worth having.

### Liveness

The linter prints the number of groups it parsed and the number of arms inside them, and REFUSES when
either is zero. A predicate that matches nothing reports clean, and this repo has paid for that shape
often enough that a new one arrives with the assertion attached.

### Files touched (estimate)

`tools/unattended/check-arms-groups.sh` (new), its `.test.sh` sibling, `tools/gate-legs.json`,
`tools/run-gates/selftest-budgets.txt`, and this build's records.

## 5. Production-readiness checklist

- security — N/A. It reads two tracked files and writes nothing.
- perf / scale — seconds. It is a single pass over one file with no subprocess per group.
- error / empty / loading states — a zero group count REFUSES; an unresolvable assertion text is
  reported, never skipped.
- observability — every red names the group's first line number, the offending arm and the rule.
- risks — rule A's text-to-check join is the only inference in the unit. A wrong join is a false red,
  which is loud; a missing join is reported rather than silent, which is the direction that matters.
- testing — the sibling `.test.sh`, with a staged failing case per rule per AC.
- migration — none.
- user docs — N/A. Developer-facing; the header carries the contract.

## 6. Acceptance criteria

- **AC1** — When a `miss` arm is moved into a neighbouring group whose `emitted` set does not name its
  check, `check-arms-groups.sh` REDS naming that arm, that group and rule A. Staged and observed RED
  before the linter is wired, per `AGENTS.md` §7.
  Red when: the move runs green, which is round 1's blocker surviving its own gate.
- **AC2** — When two arms carrying an identical assertion text are placed in one group,
  `check-arms-groups.sh` REDS naming both line numbers and rule B.
  Red when: only one is named, or the pair passes.
- **AC3** — When a group asserts against a capture belonging to another group, it REDS naming rule C.
  `fixture:` the `_f1_clean` shape at `check-unattended.test.sh:360` is the live instance to model.
  Red when: a foreign capture passes, which is how a poisoned baseline survives.
- **AC4** — When `check-arms-groups.sh` runs over a file it cannot parse into groups, it exits
  non-zero saying it graded nothing, and never prints a clean verdict.
  Red when: a zero-group run reports clean, which is indistinguishable from coverage.
- **AC5** — When `check-arms-groups.sh` runs over the tracked suite, its header output names what it
  does NOT grade.
  Red when: the header is absent, leaving a structural check to read as a semantic one.
- **AC6** — When `bash tools/run-gates/run-gates.sh` runs with the kit self-tests enabled, the new leg
  appears in the manifest-derived leg list and reports a verdict.
  `figure:` DERIVED from `tools/gate-legs.json` at emission time, never a count typed here.
  Red when: the leg is absent, which is the green-by-absence class the manifest exists to refuse.

## 7. Gates

`memory hygiene` · `unattended kit gate` · `testsuite counts self-test` · `run-gates canary`

New arm: `tools/unattended/check-arms-groups.test.sh` · one staged violation per rule, each observed
RED then unstaged · floor to move: none, the suite is new and declares its own.

## 8. Open questions

- **F1 · Does rule A's text-to-check join belong here or in `check-arms.py`?** That module already
  owns the `fail N "…"` signature extraction and its interpolation stripping, so a second
  implementation is two answers to one question. RESOLVED (agent, 2026-09-10, delegated): import the
  join from `check-arms.py` by invoking it rather than re-implementing the regex, and record in the
  build log what that invocation costs; if it cannot be invoked for a single file, the fallback is a
  shared constant and NOT a copied regex.
- **F2 · Should rule B red on duplicate texts that exist in the file today but in separate groups?**
  No. The unit's subject is the partition, and 20 to 36 texts are already duplicated across the file
  at BASE. RESOLVED (agent, 2026-09-10, delegated): rule B is scoped WITHIN a group; the file-wide
  duplication is recorded as a starting figure in the build log and is not this unit's to drain.

## 9. Revision log

- rev-1 · 2026-09-10 · initial draft, from spec-audit round 1 of `TOOL-aBatchedArm-1`, which named
  this linter as the left-shift for five of its six findings and specified its three rules and its
  failing case. Added to the build by `--rescope --act add` rather than folded into that unit,
  because M2 requires one mechanism per spec and a gate is not the thing it gates.

## 10. Reuse audit

- **The seam is `tools/memory-tree/check-arms.py`**, which already parses `fail N "…"` sites out of a
  gate, strips shell interpolation to a stable signature, and joins them against a sibling
  `*.test.sh`. This unit's rule A needs exactly that join in the opposite direction — text to check
  number — so F1 resolves to invoking it rather than re-deriving its regex. The group-splitting half
  has no seam: nothing in this tree parses a shell test file into `reset_tree`-delimited regions, and
  the reuse probe cannot see shell at all (`unscanned layers: .sh`), so that half is written new and
  the probe's silence about it is not evidence either way. The recall probe returned two live
  constraints the symbol probe could not: `TOOL-aTimedTurnstile-7` (OPEN), which says `check-arms.py`
  excludes `*.test.sh` from its population so nothing today grades rule A's subject; and the
  first-interpolation truncation recorded in `memory/map/features/testsuite-counts.md`, which §4 now
  states as an inherited limitation with its failure direction named.
- **The retrieval arguments, verbatim:**
  `python tools/codebase-map/reuse_lookup.py "parse a shell test file into arm groups and grade each group's assertions against a declared set"`
  and
  `python tools/memory-recall/query.py "what already parses a gate's fail branches and joins them to its sibling test file, and what decided that arms asserting absence cannot be scoped" --terms "check-arms armed branch signature interpolation fail sibling test join miss absence scoping vacuous floor linter"`.
