**Serves:** research TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3

# Design pass — the review loop's missing exit, the fold gap, and why `build-complete` cannot be met

Written before the spec revisions it warrants. It supersedes the design `TOOL-aBoundedVerdict-1`
carries at rev-5 (a two-round cap as a driver file constant), on the owner's instruction that the cap
was the wrong move. Every claim below is cited to a file, a line, or a count taken from this tree.

## 1. The measurement that decides the design

The loop's exit condition has never once been reached in this corpus.

`grep -rh '^## Verdict' memory/builds/*/reviews/*.md` over 90 tracked review records:

| verdict | records |
|---|---|
| `BLOCKED` (bare, or with a count suffix) | 38 |
| `CLEAN WITH FIXES` | 6 |
| **`CLEAN`** | **0** |
| a bare `## Verdict` heading carrying no token | 9 |
| outside the method's vocabulary — `CHANGES REQUESTED` ×4, `SHIP WITH FIXES`, `PASS WITH FINDINGS` | 6 |

`memory/guides/BUILD-METHOD.md:104-105` states the only exit: *"once a synthesis pass calls the design
clean, stop reviewing that spec."* The token that satisfies it appears **0 times in 90 records**.
`BLOCKED` is 42% of the corpus and `M8` gives it no disposition at all — `:198` says "Fix every
blocker, then re-review the FIX", which is an instruction to loop, not an exit.

Round counts follow from that: `dClosedLexicon` 10 records (the run reached ABORTED), `aFoldedQuarry`
7, `aSiftedPlaybook` 6, three more at 4.

**So the flat two-round cap was treating the wrong variable.** A cap does not give the loop an exit; it
relocates the stall from round 8 to round 2, which is the failure the owner reported. The cap is
withdrawn as the mechanism, not merely re-tuned.

## 2. Why round two re-reads everything (owner issue 3)

`tools/workflows/tier2-review.js:71` builds one diff command from `args.base`, and `:156` hands that
same string to every finder lens: *"Review ONLY this diff."* The harness carries **no round number, no
prior-findings parameter, and no narrowing of any kind**. The only channel for "do not re-report this"
is `byDesign` (`:69`, `:158`), a free-text caller string, and `M8` never tells the caller to fill it.

A round 2 invoked as `M8:182-187` documents it therefore re-reads the entire cumulative diff —
including every fix round 1 produced. That is the whole of issue 3, and it is also the engine of issue
1: a second pass over already-reviewed code raises fresh findings against fixes, and returns `BLOCKED`
again.

**Both knobs already exist.** The defect is in the caller's instructions, not in the harness's
capability. Separately, `:65` defaults `base` to `origin/main` — a moving ref, which `M8:182` forbids
in the same breath as it requires an immutable sha.

## 3. Why `build-complete` cannot be met (owner issue 2, first half)

The item's first term refuses unless the build README carries a well-formed `roster:units` marker pair
(`tools/unattended/unattended.sh:1494-1497`). That region is **authored**, and
`memory/map/features/build-readme-surface.md:45` states plainly that the index generator never writes
into it.

`TOOL-cBriefedPilot-18` S12 was the unit that made the roster required rather than opt-in. It is
CLOSED at rev-5. Its **AC9** reads: *"§1's roster bullet in both halves no longer reads `Opt-in by
presence`, grepped and found zero."*

That grep returns two hits today:

- `memory/guides/UNATTENDED-PROTOCOL.md:33`
- `tools/unattended/PROTOCOL.template.md:33`

`git log -S"Opt-in by presence" -- tools/unattended/PROTOCOL.template.md` returns exactly one commit,
the one that ADDED the phrase, dated five days before that spec closed. The phrase was never removed.
**AC9 was never met, and the spec closed claiming it was.**

The consequence is the owner's symptom exactly. `build-complete` (`TOOL-cBriefedPilot-7`) was built
depending on a requirement a sibling unit in the same build was supposed to establish and did not:

- the protocol still declares the roster optional;
- nothing generates one;
- no gate requires one;
- 12+ build READMEs carry a roster table with no marker pair — `memory/builds/aBoundedVerdict/README.md`
  among them, so this build could not close itself today.

The one run that ever satisfied the item hand-authored the pair mid-flight: commit `cfd4011` adds
`<!-- roster:units -->` around an existing table, and its own message claims "build-complete
satisfied". `build-complete` is therefore not unsatisfiable — it is **satisfiable only by an
undocumented hand-edit**, which is the one shape an unattended run cannot be expected to discover.

## 4. The collision the owner's chosen disposition walks into

The owner's rule for a residual blocker is: **spec it as a unit and resolve it in the build.**

`memory/guides/BUILD-METHOD.md:29` instructs *"Rebuild the roster after any fork resolution that adds
a unit."* But `check_authorization` byte-compares the roster slice across the pinned BASE and refuses:
*"the run rewrote the scope it is executing against, and a run that can edit its own scope mid-flight
is not running the build that was authorized."* And `verb_close` refuses any override of that item
(`fail 21`) because the protocol states there is none.

For a build whose README carries the pair at BASE, adding a unit is therefore an **unclosable run with
no repair verb** — the method instructs precisely the act the kit refuses. Two things mask it today:
the comparison is opt-in by presence at BASE, and `:33` records that it does not hold on the
`published` branch anchor at all, which is the anchor this repo declares.

**Ratified resolution** (owner, this session): make `roster:units` **generated and mandatory**, and
move the frozen-scope comparison off the README.

**The trap that resolution must not fall into.** The obvious home for the frozen scope is the
run-state file — but `scaffold_runmd` writes that file, and the run writes the run-state file. A scope
frozen where the subject can write it is `memory/gotchas/inputs-inside-the-subjects-reach.md`, and the
comparison would certify the run's own bytes. So the AUTHORITY stays the BASE blob, re-derived through
`git show <BASE>:<README>` by both the driver and the leg; the run-state copy is a convenience and is
never the side compared against. The roster becomes reproducible from git precisely because it is
generated from spec status headers.

## 5. The recommendation

Three mechanisms. The cap is not among them.

**R1 — the loop gets a reachable exit, and `BLOCKED` gets a disposition.** A closing round ends the
loop when its confirmed-blocker set is empty, and the verdict vocabulary the driver reads is closed and
refused at the verb — because six of 90 records already use spellings outside the method's three, and
nine carry no token at all, so no machine check can read a verdict today. A round whose confirmed
blockers do not shrink against the previous round is **non-convergent**, and non-convergence is what
ends the loop, not a count.

**R2 — a residual blocker becomes a unit, and the roster stops being the obstacle.** At the exit, every
confirmed unfixed blocker is promoted to a spec unit in this build, specced, built and closed —
resolved, never parked and never waived. This is legal under `M6`'s pass vocabulary already ("a spec
authored", "a unit built"). It is made legal in the kit by §4's ratified resolution.

*The cost this incurs, stated rather than assumed away:* a promoted unit is new code, which earns a new
closing diff review, which can raise a new blocker. The bound is not a counter — it is that a promoted
unit is reviewed as a SPEC (`M4`, one unit, cheap) while the closing DIFF review re-runs once, scoped
to the fold per R3. Whether that actually converges is the open question the spec set must answer, and
`§8` of the lead spec is where it goes. If it does not, a runaway ceiling returns as a backstop and the
owner gets the call.

**R3 — round N>1 reviews the fold, not the build.** The caller passes `base` = the tip round N-1
reviewed, and passes round N-1's confirmed findings explicitly. `M8` states it; the harness gains a
named `priorFindings` parameter so the brief is not smuggled through free-text `byDesign`, and the
moving-ref default at `:65` is refused rather than defaulted.

## 6. What this record does not settle

- The close-path defect inventory. A five-lens adversarial audit is running concurrently; its findings
  land in a sibling record and will add units for the silent and unbounded classes. This record covers
  only what was verified directly by the design pass.
- Whether `records-current` and `closing-review-recorded` have the same shape of dependency on an
  authored region. Not examined here.
- The migration order for 12+ build READMEs, and whether the generator can render the region into
  builds whose tables are not currently wrapped.
