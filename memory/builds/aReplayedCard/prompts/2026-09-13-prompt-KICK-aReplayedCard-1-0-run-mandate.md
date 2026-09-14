# Run mandate — aReplayedCard

**Serves:** journal KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5

node a · 2026-09-13 · order 0 · streams kickoff+tooling · authorized-by prompt

## The prompt, verbatim

The owner invoked `/unattended` with `--prompt` and this value, taken as the prompt itself because
it carries whitespace and names no readable file:

```
Stage 1 of the session-orientation redesign, Tier-2, tooling stream. Design source: the synthesized
design document at C:/Users/daily-agent/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-session-orientation-tooling-2faa9f/80e02246-4e09-4235-b09d-8a39175ab2c8/scratchpad/orientation-design.md
(44 KB; copy it into the build folder as the design record, it is outside the repo and
session-local). Owner decisions, 2026-09-13, applied over that document: (1) stage 1 ONLY, no orient
subagent; stage 2 is deferred behind a counterfactual the build must leave a runnable harness for: a
matrix of agent type {custom orient, Explore-typed} x probe set {memory-recall in/out, reuse-lookup
in/out}, each arm measured as tokens and wall to READY on two matched kickoffs, to identify the
better-oriented combination. (2) doc-only sessions PAY A KICKOFF: there is no --waive verb; the
commit deny has no waiver line. (3) the prompt-path unattended run's build-folder commit precedes
kickoff, so the deny EXEMPTS a commit whose cwd holds a build folder with authorized-by: prompt; hook
logic, with its own RED arm. (4) the manifest traps eviction is FOLDED INTO THIS UNIT: the 22
path-bearing bullets of memory/guides/SESSION-KICKOFF.md section Environment traps move to
memory/gotchas/ records that gotchas.py --for-paths keys, with the manifest re-stamped. Scope per the
design doc section 2 and section 3: the --card verb family on skills/session-kickoff/manifest-check.sh
(--card, --replay, --append, --check, --path; 8192 B cap; batched citation check via one git ls-files
and one git grep -F -f; UNVERIFIED annotation; DEAD PROBE on zero tokens); the commit-shaped deny
folded into tools/hooks/scratch-guard.js keyed on agent_id absence, READY line, tree cell match,
fail-open on missing session_id; SessionStart matchers startup|resume|clear on the two existing
entries plus startup|clear -> --card and resume|compact -> --card --replay, shipped as a fragment for
settings-merge.py; the card arm in tools/check-wiring.sh; engine Step 1 consumes the card and Step
5/5b appends (must fit SKILL.md headroom, else split); tools/unattended/SKILL.template.md resume
section gains /session-kickoff after --resume with no /session-kickoff mention above template line
175; dossier refresh for session-kickoff; WIRE-INTO-PROJECT.md step; close backlog rows
TOOL-aWeighedCompass-14 and -15 whose fix the manifest already carries. Acceptance: every new gate
arm observed RED before landing; one compaction observed replaying the card verbatim; a commit
without READY denied with the remedy in the reason; the prompt-path exemption observed passing; the
22 evicted bullets selected by gotchas.py --for-paths over their paths. Non-goals: the subagent, any
charter or template body change, gating Edit/Write, a second LLM refuter, a signed artifact.
```

## The owner turn that preceded it

The design record was produced by a 13-agent study in the attended session that started this run.
The owner was then asked the design's open decisions in two `AskUserQuestion` calls and answered,
verbatim:

- Build the orientation subagent now, or after a counterfactual? — **Stage 1 only, measure first.**
- If stage 2 is built, which subagent type? — **Test custom 'orient' vs 'explore-typed', test with
  memory-recall and reuse-lookup in and out of scope, identify a better-oriented combination.**
- Doc-only sessions hit the commit-deny without a kickoff. How should they pass? — **Pay a kickoff.**
- Prompt-path unattended runs commit the build folder before kickoff. Which resolution? — **Deny
  exempts prompt-authorized commits.**
- Evict the 22 path-bearing trap bullets into `memory/gotchas/` as a separate unit? — **Yes, fold
  into stage 1.**
- What next? — **`/unattended --prompt` Kick off stage 1 as a Tier-2 unit.**

The second answer turns the deferred stage 2 into a measurement the harness unit must make possible:
two agent types by four probe-set arms. The design record's section 7 held these as forks; every one
is resolved by the lines above, and the specs cite this record rather than restating them.

## The design record

The prompt names a scratchpad path outside the repository. Its bytes travel here as
`build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md`, unchanged apart from the
binding header, because the build folder is the authorization and may not point at a file that can
be edited after the run starts.
