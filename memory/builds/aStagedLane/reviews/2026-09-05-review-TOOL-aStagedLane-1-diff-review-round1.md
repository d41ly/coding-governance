**Serves:** diff-review TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3

# aStagedLane — closing diff review, round 1

*Node `a`, 2026-09-05. The cumulative diff from the run's pinned BASE
`c4fcf5add1d0a553097f9eef70935a056896cf16` to `387d51e0`. Four primed lenses — security,
correctness, seams, regressions — a batched skeptic stage prompted to REFUTE, and a synthesis pass.*

## Verdict: BLOCKED

**THIS RECORD WAS WRITTEN BY THE ORCHESTRATOR, NOT BY THE SYNTHESIS AGENT.** That agent died with
`You've hit your session limit · resets 4am (Europe/Kyiv)` before writing anything, so the harness
returned `report: null` and carried the confirmed set out in its run log instead. The findings below
are transcribed from that log verbatim in substance; what is missing relative to a synthesised report
is the cross-finding consolidation and the left-shift ranking, and their absence is stated here
rather than papered over. The harness's own degradation note — `UNVERIFIED: the synthesis agent
died` — is what made this recoverable at all.

Shape: raw 26, confirmed 23, refuted 3, unverified 0, **precision 0.88** — the highest of this
build's five review rounds, and far above the four spec-audit rounds that ran between 0.26 and 0.46.
That is the expected direction: a diff is a narrower and more falsifiable subject than a spec set.

**One blocker, and it is mine.** Unit 1's S6 hardened the `opened:` read to come from the graded
commit rather than the working tree, closing an uncommitted-edit bypass. It left the two sibling
reads on the same code path — `base:` and the CLOSED-units region — still reading the working tree.
So the bypass S6 exists to close is still open one line below where it was closed, and an untracked
`RUN.md` naming HEAD empties the range and turns any violation green. Reproduced by the reviewer on
this suite's own fixture. This is `gate the CLASS, not the instance` — the rule §7 states, applied to
the very unit that cites it.

## Findings

| # | Severity | File | One line |
|---|---|---|---|
| B1 | blocker | check-pass-order.sh:222 | `base:` is read from the WORKING TREE, so an untracked `RUN.md` empties the range and greens any violation — the bypass S6 closed for `opened:` two lines above. The CLOSED-units read at :241 has the same shape. |
| H1 | high | check-pass-order.sh:290 | The pre-anchor probe never examines the anchor `<first>^` itself once the window is full: `--reverse` puts the anchor LAST and the counter declares TRUNCATED on entry `_cap`, which IS the anchor. |
| H2 | high | check-pass-order.sh:288 | `PASS_ORDER_PREANCHOR_CAP` is admitted from the conf unvalidated and flows into `$((_cap+1))` — arithmetic evaluation in the leg's own shell, and a silent green on any non-numeric value. |
| H3 | high | check-pass-order.sh:185 | The waiver registry is read from the working tree, so an uncommitted waiver still waives and its stale-row red cannot fire for anyone else. |
| H4 | high | unattended-build.js:752 | Attended mode logs `SKIPPING <n> terminal unit(s)` and returns them in `skippedTerminal`, then hands the BUILD agent the unfiltered roster. Nothing acts on the skip. |
| M1 | medium | unattended-build.js:710 | The refusal exempts every unit the SPEC stage reported in `alreadyPresent` — precisely the units it did NOT touch, whose entry-time state is therefore not stale. THIN/FORKED is bypassed on an agent's say-so. |
| M2 | medium | unattended-build.js:643 | The CONVERGING early return omits `mode` and `skippedTerminal`, which the final return's own comment says exist so the caller can tell the modes apart. |
| M3 | medium | unattended-build.js:130 | The args contract block still declares `{id, order, specPath, briefPath}` and documents none of `mode`, `runStateExists`, `specBriefPath`, `planState` — one of which is mandatory and throws only after SPEC and AUDIT have run. |
| L1 | low | unattended-build.js:339 | The header's worked example is arithmetically wrong: seven slices at a cap of five give FOUR groups sized 2,2,2,1, not "five groups, two of them carrying two slices". |
| L2 | low | check-pass-order.sh:325 | The pre-anchor violation path duplicates the waiver bookkeeping inline instead of routing through `_report`, whose own comment claims every violation routes through it. |
| L3 | low | run-unattended-gates.sh:91 | The re-declared ceiling's justification says "19 arms to 52"; the suite counts more, and the figure moved again before landing. |

---

### B1 — the hardening that stopped one line short

**BLOCKER** · `tools/unattended/check-pass-order.sh:221-222`, and `:241`

S6 moved the `opened:` read to `GIT show "HEAD:$readme"` precisely so that editing a working copy
could not exempt a build. Two reads on the same path were left on the filesystem:

- `[ -f "$run" ]` and `sed ... "$run"` — the run-state file, which supplies the RANGE.
- the `awk` over `"$readme"` that selects the CLOSED units — which supplies the POPULATION.

Both are strictly worse than the hole S6 closed, because both are load-bearing earlier. An untracked
`RUN.md` carrying `base: <HEAD sha>` makes `base..HEAD` empty, so no build commit is ever found and
every unit lands in `unbuilt-in-range`; the leg exits 0. An uncommitted deletion of a ` CLOSED ` row
drops that unit from grading entirely.

Reproduced by the reviewer against `mkfixture norun build-first`: the leg exits 1 as it should, and
with an untracked `RUN.md` added it exits 0 with a clean liveness line.

**Fix.** Read both from the graded commit, as `opened:` already is. An absent blob at `HEAD:$run`
means no run-state file, which the S2b folder-anchor fallback already handles correctly.

**Left-shift.** The arm is the mirror of the S6 arm that already exists: an UNCOMMITTED edit must not
change the verdict, a COMMITTED one may. The general rule this build should have followed: when a
read is moved from the working tree to a commit because the working tree is attacker-controlled,
every read on that path moves, and the diff is grepped for the ones that did not.

---

### H1 — the anchor the probe cannot see

**HIGH** · `tools/unattended/check-pass-order.sh:290`

`git rev-list --reverse --max-count=N <anchor>` applies the count during traversal and reverses
after, so the ANCHOR is the LAST element of the returned window. The loop guard fires at the top of
the iteration when `_n >= _cap`, which is entry number `cap+1` — the anchor. So whenever the history
behind the anchor is deeper than the cap, the one commit the pre-anchor probe exists to reach is
consumed as the truncation sentinel and never graded.

The arm that covers truncation uses the record-only fixture, where correct and buggy behaviour give
the same verdict, so it could not have caught this. That is the `fixture-passes-by-finding-nothing`
class in the arm written for this very mechanism.

**Fix.** Grade the commit before declaring truncation — increment, run the body, then test the cap —
or take `--max-count=$_cap` and detect truncation by comparing the emitted count.

**Left-shift.** An arm whose violating commit sits AT the anchor with a cap smaller than the window.

---

### H2 — an unvalidated integer reaching `$(( ))`

**HIGH** · `tools/unattended/check-pass-order.sh:288`

`PASS_ORDER_CUTOFF` gets an ISO-date `case` and an `exit 2`. `PASS_ORDER_PREANCHOR_CAP` was added to
the same conf allow-list and gets nothing, then flows into `$((_cap+1))`. Two consequences: arithmetic
evaluation of a tracked value the graded run commits, and a silent green on any non-numeric value —
the pre-anchor violation class disabled with zero truncations reported.

**Fix.** Validate beside the cutoff check, and refuse with exit 2 rather than defaulting.

**Left-shift.** Arms for the non-integer and negative shapes, in the same block as the hostile-conf
arms that already cover `exit 0` and the EXIT trap.

---

### H3 — a waiver that need not be committed

**HIGH** · `tools/unattended/check-pass-order.sh:185`

The registry is read from disk, so an uncommitted waiver waives — and because the file is not in the
pushed tree, the stale-row red cannot fire for anyone else either. Same class as B1, on the file
whose entire purpose is to be a DECLARED population.

**Fix.** Read it from `HEAD:$WAIVER_FILE`; an absent blob is an empty waiver set, which is the
direction the file already declares. The four waiver arms then have to commit the registry, which is
what makes them exercise the tracked path.

---

### H4 — the skip that skips nothing

**HIGH** · `tools/workflows/unattended-build.js:752`

`skippedDone` is computed, logged as `SKIPPING`, and returned as `skippedTerminal`. The BUILD prompt
still interpolates `roster`, which is rendered from all of `ordered`. So an attended run tells its
operator it skipped the terminal units and tells its agent to build them.

**Fix.** Render the BUILD roster from the surviving units, and return without spawning the agent when
none survive. Keep the full roster for the subject resolver, which legitimately wants every spec.

**Left-shift.** An arm asserting the skipped id is ABSENT from the composed build prompt — the same
prompt-level assertion this build already added for the driver verbs.

---

### M1 — an exemption pointed at the wrong list

**MEDIUM** · `tools/workflows/unattended-build.js:710`

The stale-state exemption covers `authored` and `alreadyPresent`. Only `authored` is stale-by-
construction: those are the units this invocation wrote. A unit reported `alreadyPresent` is one the
stage did NOT touch, so its entry-time `planState` is current — and exempting it bypasses the
THIN/FORKED refusal on an agent's say-so.

**Fix.** Build the exemption from `authored` alone.

---

### M2, M3, L1, L2, L3

Each is stated in the table above with its fix; none changes a verdict. M2 and M3 are contract
honesty — a return that cannot be told apart between modes, and an inputs block that stopped
describing its own inputs. L1 and L3 are numbers stated in prose beside code that owns them, which is
this repository's most-broken rule and was broken twice more here. L2 is a comment claiming an
invariant the code next to it does not keep.

## What this review says about the run

The three spec-audit rounds that preceded the code found their defects in prose. This one found them
in behaviour, at three times the precision, and the blocker it found is one that four rounds of spec
audit could not have seen: it is an artifact of how the code was written, not of what the spec said.
The spec for S6 was correct. The implementation applied it to one of three reads.

The cost figure worth recording: five review rounds, ~7.7M subagent tokens, and the round that
mattered most was the cheapest to reason about.
