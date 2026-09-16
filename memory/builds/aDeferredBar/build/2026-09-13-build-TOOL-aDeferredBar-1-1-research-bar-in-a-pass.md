# Research — where a build pass is told to run the bar, and what refuses it

**Serves:** research TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 TOOL-aDeferredBar-3

Written before the specs, on node `a`, 2026-09-13. Every figure here was read from a tracked file,
a git-dir ledger, or the operator's own transcript store, and each says which. The M12 loop: find
the carriers that instruct the act, measure the act in the corpus, name the candidate mechanisms,
write what would make each lose, choose by M3.

## 1. The chain that puts a bar inside a unit

A unit is built by `tools/workflows/unattended-unit.js`. Its child agent is handed `cfg.ground`,
which says *"Read `memory/guides/BUILD-METHOD.md` WHOLE before acting; it is the procedure you are
bound by"*, then the unit's SPEC and BRIEF, then *"The spec is the design"*. Nothing in that prompt
mentions gates at all. The instruction arrives through three carriers the child reads next.

**Carrier A — the spec's own acceptance criteria and §7.** `memory/TEMPLATE-SPEC.md` §6 requires
each criterion to name *"a test it adds, a gate it moves"*, and §7 *"the named gate legs this unit
must keep green"*. The spec-stage writers in `unattended-build.js` satisfy that with the invocation
they know. Grep of `memory/builds/*/spec/*.md` for `GATE_SELFTESTS=1`, `GATE_FULL=1`,
`bash tools/run-gates/run-gates.sh`, `run-unattended-gates.sh` or `run-selftests.sh`: **20 specs**
carry one, the densest at 28 mentions (`aQuenchedHarness-4`). The live instance that proves the
chain end to end is `TOOL-aLeakedHandle-1`: its spec's AC8 reads *"When `GATE_SELFTESTS=1 bash
tools/run-gates/run-gates.sh` runs with the new rows …"* and its §7 says *"Run them by hand for
this unit; AC8 names the invocation"*. The unit's acceptance ledger
(`memory/builds/aLeakedHandle/build/2026-09-10-build-TOOL-aLeakedHandle-1-2-acceptance-ledger.md`)
records that the child DID: *"AC8 — `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, the one
invocation that lifts the self-test hold. Both new legs appear in the reported set."* That unit ran
from its `--dispatch` row at 09:01Z to its build commit `c0964657` at 10:09Z — 68 minutes for a
diff whose direct checks (`sh_hygiene.py --selftest`, a staged break) take seconds each.

**Carrier B — the build method's M6.** `memory/guides/BUILD-METHOD.md` M6: *"Then the diff-scoped
gates for what the pass touched; the full bar runs ONCE, at the push boundary."* "Diff-scoped gates"
has no spelling narrower than `bash tools/run-gates/run-gates.sh`, because `tools/run-gates/run-gates.sh`
has no leg-selection flag — its only scoping is the manifest `guard`, and 48 of 106 legs carry none
(`tools/gate-legs.json`, counted by `json.load`). A plain bar on this node costs the `records`
chunk 175 s and `declarations` 221 s of wall per `<git-dir>/gate-last-summary.txt`, with
`unattended kit gate` at 399 s and `pass-order history` at 318 s in the ledger. So the cheapest
reading of "diff-scoped gates" is minutes, and the reading a spec's AC8 hands the child is hours.

**Carrier C — the kickoff manifest**, front-loaded at the hand-back: `memory/guides/SESSION-KICKOFF.md`
line 263, *"Adding ONE gate leg trips a SET of meta-gates that GROWS as new ones land — run the full
bar, never a list."* True at the push boundary, read as a per-pass rule by the agent that just added
a leg. Unit 1 corrects this line in place, at the manifest, which is watched and owes a re-stamp.

**Nothing refuses the act.** `tools/hooks/scratch-guard.js` and `tools/hooks/agent-cap.js` are the
two PreToolUse guards; neither reads a command for a bar. `TOOL-cRefutedPremise-1` measured on
2026-09-12 that a `Bash|PowerShell` PreToolUse hook DOES fire inside a `Workflow` sidechain, so a
guard there would bind the child. The driver's `--dispatch` runs BEFORE the pass and reads paths,
not commands.

## 2. What the corpus measures

The operator's transcript store, `~/.claude/projects/C--projects-coding-governance*/**/*.jsonl`,
holds every tool call this node has issued. Probe: every `Bash`/`PowerShell` `tool_use` whose
command carries an INVOCATION-shaped reference — the runner or suite path at command position,
after a separator, optional `VAR=value` prefixes, `timeout N`, and `bash`/`sh` — as distinct from a
mention inside `grep`, `sed`, `git commit -m` or a python heredoc. The transcript's `isSidechain`
flag says whether the call came from an agent inside a `Workflow` or `Agent` sidechain.

| shape | invocations | of which sidechain |
|---|---|---|
| a `*.test.sh` suite | 1365 | 554 |
| the plain bar, no flag | 408 | 204 |
| `GATE_FULL=` prefix | 263 | 63 |
| `run-selftests.sh` | 142 | 94 |
| `GATE_SELFTESTS=` prefix | 60 | 2 |
| `run-unattended-gates.sh` | 30 | 9 |

Over 3044 transcript files and 101 419 shell calls, 76 613 of them sidechain. The probe still
admits a heredoc'd python line that spells a suite path in a string, so the counts are an upper
bound on invocations and the ORDER is the finding, not the last digit: agents inside sidechains run
suites and bars routinely, and the self-test forms — the ones costing 850–3400 s each in
`<git-dir>/gate-ledger.tsv` — are among them. The predicate unit 3 ships is measured against this
same corpus with a string-blanked view, the way `scratch-guard.js` measured its own, and reports
hits AND near-misses in its spec.

## 3. The candidates, and what would make each lose

Three mechanisms differ in WHERE they refuse. Each is tested by the smallest thing that could
refute it, written down before the pick.

**C1 — refuse the INSTRUCTION at the spec.** `tools/check-spec-tokens.py` already parses §6 and §7
of every non-terminal spec and joins them against the tree; a fourth join reds a backticked token
that spells a bar or suite invocation. *Loses if* a bar run inside a unit was NOT named by the spec.
Test: section 2's 204 sidechain plain-bar runs against the 20 bar-naming specs — the majority of
sidechain bar runs come from M6 and the manifest, not from an AC. **C1 is necessary and not
sufficient**: it stops the writer at the cheapest point but cannot see the act.

**C2 — refuse the ACT at the tool call.** A PreToolUse `Bash|PowerShell` hook in the unattended
kit reads `.unattended.conf`'s `MEMORY_ROOT`, finds the run-state file whose `branch-ref:` is the
current branch, and while its `phase:` precedes `VERIFYING` denies a command that sets `GATE_FULL=`
or `GATE_SELFTESTS=`, or invokes `run-selftests.sh`, `run-unattended-gates.sh`, or any `*.test.sh`.
The plain bar passes: it is the scoped form the owner allows. *Loses if* the hook cannot see the
child's command — refuted by `TOOL-cRefutedPremise-1`'s measurement — or if the predicate reds the
main loop's legitimate bar at `VERIFYING` — which the phase key excludes — or if it denies prose
about a suite; the string-blanked view is the sibling hook's answer to that. **C2 is the only
candidate that reaches a sidechain.** It is textual and fails open, exactly as `scratch-guard.js`
states of itself; an agent that constructs the path at runtime walks past it, and no agent in the
corpus does.

**C3 — refuse in the RUNNER.** `run-gates.sh` and the suites refuse when a run on the current
branch is before `VERIFYING`. *Loses if* it needs a kit to read another kit's record: `run-gates.sh`
is the run-gates kit and the run-state file is the unattended kit's, and the hooks README's
literal ban ("a kit file names nothing outside itself by literal") is a merge-bar leg. The
unattended kit's own six suites could self-refuse through `lib-unattended.sh`, but that covers 6
of the 55 `subject = kit` legs and none of the three that cost most (`govkit selftest` 3445 s,
`manifest-check self-test` 2162 s, `memory-hygiene self-test` 906 s). **C3 is rejected**: partial by
construction, and the part it can cover is a subset of C2.

**C0 — instruction only**, the sentence at every carrier. *Loses by* the scratch-guard precedent:
the rule it enforces was loaded in every session that broke it. Kept as unit 1 because the owner
named the instruction as the defect and a refusal with no stated rule is a puzzle; not relied on
alone.

## 4. The choice, by M3

Most feature-rich survivor: **unit 1 (C0) + unit 2 (C1) + unit 3 (C2)**, sequential. Vetoes: no
new dependency; no new install location (the hook ships inside the unattended kit's existing `**`
rule and wires through the existing `settings-merge.py --fragment` seam, as `procmon-hook.js` does);
the governance carriers touched are the ones the mandate names, and M1's byte budget is not raised.
C3 rejected on veto 2's literal ban and on coverage. Tie-break unused. Recall terms used for M5,
recorded here so M7 can re-run the query: *unattended unit pass full bar run-gates GATE_SELFTESTS
GATE_FULL self-test diff-scoped push boundary stall wall-clock turnstile brief*. The map probe
(`reuse_lookup.py`) found no seam for "refuse a bar inside a pass" and printed `unscanned layers:
.sh`, so the shell surface was read by hand: `run-gates.sh`'s knob set (`GATE_FULL GATE_SELFTESTS
GATE_JOBS GATE_WALL …`, no leg filter) and `lib-unattended.sh`'s phase reads at line 405.
