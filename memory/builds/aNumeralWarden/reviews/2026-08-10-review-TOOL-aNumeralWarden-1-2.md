# Review 2 — scoped Tier-2 pass over S14 of TOOL-aNumeralWarden-1 at rev-3

**Serves:** spec-audit TOOL-aNumeralWarden-1

**Scope: S14 ONLY.** This review reads exactly one scope item — S14, the `Agent`-matcher modality
refusal folded into the spec on 2026-08-10 when the consuming build's owner ratified its F2 as a
FOLD — plus every section of the spec that S14 falsifies, contradicts, or leaves uncovered (§1, §3,
§4, §5, §6, §7, §9). **S1 through S13 were reviewed separately at rev-2** and are not re-opened
here; that pass is recorded in this build's reviews folder as
`2026-08-10-review-TOOL-aNumeralWarden-1-1.md`, and per `memory/guides/REVIEW-PROTOCOL.md:95-96` a spec is
not re-reviewed once the judge calls the design clean. S14 is the exception the protocol
contemplates: it is scope added by a non-owner AFTER that Tier-2 closed, so nothing has ever
reviewed it.

**Target:** `memory/builds/aNumeralWarden/spec/2026-08-10-spec-aNumeralWarden-1.md` at rev-3
(the fold commit is `58dd43d`), before any code.
**Method:** three primed lenses over S14 — is the folded item buildable as written, does the fold's
blast radius reach sections nobody revisited, and does the cross-build dependency close — then a
default-refute verification pass over every raw finding, each verdict required to reproduce against
the file or the running tree.
**Result:** 28 raw findings, **25 confirmed**, 3 refuted, 0 unverified, 0 died. Precision 0.89,
well above the 0.5 floor `memory/guides/REVIEW-PROTOCOL.md:89` sets for adding agents rather than
tightening scope.

---

## Verdict

**Not safe to build as written — six blockers, and two of them make S14 unbuildable rather than
merely under-specified.** S14 keys a per-call refusal on "the consuming build's run-state file
declares a verify phase", and neither half of that key exists: the file is the consuming build's
`RUN.md`, a name `tools/memory-tree/check-memory-hygiene.sh:275` makes illegal in this tree today,
and the token "a verify phase" belongs to a vocabulary that build's spec never enumerates and that
its own F3 makes a PROJECT-OWNED declaration — which a hook `§4:142` deploys verbatim into adopting
repos cannot resolve. Worse, nothing binds a session to a build: none of the six measured
`PreToolUse` payload keys names one, `cwd` resolves ambiguously across the seven live checkouts on
this machine, and the consuming build's authored region is frozen at "exactly five facts and
nothing else", none of them a session id — so the refusal is, in S14's own words, either arbitrary
or a tree-wide false deny, and S14 names that obligation and then does not discharge it. The
dependency also runs backwards: both specs record the edge one-way in opposite directions, so the
`RUN.md` contract the hook reads lands after the code that reads it and neither owner's file shows
the cycle. Against that, the mechanical half is unowned: "the matcher widens" is unspecified
between three spellings and I ran all three — one double-fires the hook, one is silently undone by
the next documented WIRE run, and one reds `python tools/settings-merge.py --selftest`, a leg of
the 40 AC18 requires — while §4's Files-touched table names none of `.claude/settings.json`,
`tools/settings-merge.py`, `tools/check-wiring.sh` or `tools/check-wiring.test.sh`, and the
consuming build's own §4 explicitly disclaims `tools/check-wiring.sh` as "Not touched", so after
the fold no spec's file list claims it. S14 has **no acceptance criterion, no gate leg and no
design paragraph** — AC1 through AC18 map cleanly onto S1 through S13 with nothing left over for
the widened matcher, the refusal, the fail-open, the session binding, the distinguishable deny
string or the `check-wiring.sh` grep fix — which is the same defect this spec's own rev-2 was
reddened for and the class `memory/gotchas/fixture-passes-by-finding-nothing.md` records. The
corrections are not a redesign of the unit: S1-S13 stand untouched, and the cleanest resolution is
to split S14 at its own seam — keep the matcher widening here, and move the run-state-keyed refusal
to an item that cannot start before the consuming build's unit 1 lands.

## Confirmed findings

25 confirmed. Ids are the raw ids from the verification pass; the three gaps (10, 19, 20) are the
three refuted. `spec:N` means the target spec at rev-3.

| # | Severity | Where | Claim | Fix |
|---|---|---|---|---|
| 1 | blocker | `spec:64` (S14), with `spec:277` and the consuming spec's `§9:233` | The refusal is keyed on the consuming build's `RUN.md`, a filename `check-memory-hygiene.sh:275` makes illegal today, so this spec now depends on the build both files record as depending on it — a cycle recorded nowhere. | Split S14: keep the matcher widening here, move the refusal to an item gated on the consuming build's unit 1. Flip the header to BLOCKED or state the gating in §4 Rollout; name check 4 as the prereq gate in §7. |
| 2 | blocker | `spec:190` (§6) | S14 has no acceptance criterion: AC1-AC18 map onto S1-S13 with nothing left for the widened matcher, the refusal, the fail-open, the session binding, the deny string or the `check-wiring` fix. | Add ACs phrased as observations, one per S14 claim (Agent payload with no run-state exits 0; with a verify phase exits 2 asserted by `-qF` on a unique string; non-verify exits 0; Workflow handling byte-identical; one-of-two-wired reports UNWIRED). Note that `agent-cap.test.sh:29-34`'s payload builder must gain a `tool_name` parameter. |
| 3 | blocker | `spec:161` (§4 Files-touched) | Every file S14 must edit is missing from the table, and `tools/settings-merge.py` cannot produce the two-matcher-group state S14's last sentence presupposes. | Add rows for `.claude/settings.json`, `tools/settings-merge.py`, `tools/check-wiring.sh`, `tools/check-wiring.test.sh`; state in S14 which spelling the widening takes, because `settings-merge.py:97` and `check-wiring.sh:43` behave differently under each. |
| 12 | blocker | `spec:69` (S14) | The session-to-build binding exists nowhere: 23 build folders, an authored region frozen at five facts none of which is a session id, and no payload key carrying a build slug. | Add a §8 fork naming the binding concretely (an authored `session_id` matched against `data.session_id`, or an env var the unattended driver exports), record the cross-spec obligation, and state the build order explicitly. |
| 13 | blocker | `spec:61` (S14) | "The matcher widens" is unspecified between three spellings; I ran all three — one double-fires the hook, one is undone by the next WIRE run, one reds a bar leg. | State which shape the widening takes; if it is a widened `AGENT_CAP` matcher, scope the four selftest assertions at `settings-merge.py:165/179/188/212` as edits. Add an AC that a re-run leaves the file byte-identical. |
| 21 | blocker | `spec:64` (S14) | "A verify phase" is a token no specified vocabulary contains, and the consuming build's F3 makes that vocabulary project-owned — unresolvable by a verbatim-deployed kit hook. | State that the vocabulary carries a KIT-OWNED reserved token a project declaration may extend but never rename, name it literally, and name the file and resolution path the hook reads it from. Add an AC that a renamed or absent token DENIES. |
| 4 | high | `spec:68` (S14) | S14 declares the fail-open and the session binding load-bearing, states neither, and §4 adds nothing; the measured payload carries no field that can bind a session to a build. | Write both rules as normative text in S14 with a §4 sub-head carrying the resolution order. If the field does not exist, say so and make the binding a §8 fork rather than an implied mechanism. |
| 5 | high | `spec:60` (S14) against `spec:37-39` (S7) | S14 falsifies two published statements of the wiring block that S7 does not cover — `agent-cap.js:22-26` and `WIRE-INTO-PROJECT.md:384` — and AC11's `AGENT_CAP` grep structurally cannot see either. | Extend S7 to name `tools/hooks/agent-cap.js:22-26`, `WIRE-INTO-PROJECT.md:376-386` and the `settings-merge.py:7-13` docstring. Widen AC11 to a second grep asserting no wiring-block site states a narrower matcher. |
| 6 | high | `spec:167` (§4) | §4 contains no design for S14, and its one passage in S14's territory rejects runtime counting for a reason true of a sidechain and false of a direct `Agent` call. | Add a §4 sub-head for S14 carrying the modality inventory row, the refusal-not-count decision, the resolution order, and the branch placement relative to `agent-cap.js:305-325`. Scope the rejected alternative's reason to the sidechain modality. |
| 14 | high | `spec:70` (S14) | The `check-wiring.sh` defect is real as described, but the claimed fix has no material: both fragments emit the identical command and `HOOK_MARKER` is the single substring serving as dedup key and wired-signal at once. | Ship a per-fragment `tools/hooks/agent-cap.fragment.json` with distinct markers and rewrite `check_agentcap` to read matcher and marker from it the way `check_recall_opened` already does. Add the one-of-two-wired arm to `tools/check-wiring.test.sh`. |
| 15 | high | `spec:175` (§5) | §5's "every new branch fails closed, matching `agent-cap.js:242-245`" is falsified by S14's own fail-open, and §5 was not touched at rev-3. | Rewrite the §5 security line to state the split: static rules fail closed as before, the modality refusal fails OPEN by design on an absent run-state file. Add the fail-open to the §5 risks line with its residual named. |
| 16 | high | `spec:64` (S14) | The measurement refutes a read-then-decide counter, not counting; the same sentence names `tool_use_id`, the key that makes the count atomic — and the rule S14 serves is a cardinality a binary cannot express. | Narrow the rationale to what the measurement supports, then either specify an exclusive-create token count keyed on `tool_use_id`, or raise it as a §8 fork with the residual written down: the number stays unenforced for direct spawns. |
| 17 | high | `spec:63` (S14) | The refusal fires only under the unattended driver, so the direct-`Agent` hole stays open for interactive sessions — the modality the protocol calls primary and the one that produced the original incident. | State the residual inside S14 and carry it into S11's rewrite at the protocol's "Enforcement — and where it does NOT reach" section. Add an AC that greps the rewritten protocol for the stated residual, mirroring AC15. |
| 22 | high | `spec:63` (S14) | S14 conflates a run-lifecycle phase with a review's verify STAGE: the phase vocabulary is framed as a sibling of the status enum with a git-checkable witness per claim, and a verify stage produces no commit. | Key the refusal on a short-lived verify-stage assertion the review harness sets and clears, or restate S14 as refusing only calls a run-phase-scoped mandate has not whitelisted. Add an AC proving a 3-6 lens find-stage fan-out is NOT denied while the phase is set. |
| 23 | high | `spec:68` (S14) | The fail-open covers only "no run-state file exists", but the writer the consuming build reuses truncates in place at `gen_build_index.py:75-80`, so a read during a re-render finds no phase and fails open. | Split the state into three: ABSENT fails open silently, PRESENT-and-parseable decides, PRESENT-but-unreadable DENIES with its own string, matching `agent-cap.js:317-322`. Pin an atomic write as a cross-spec obligation and correct `spec:175`. |
| 24 | high | `spec:69` (S14) | The binding is stated as an obligation and not discharged; `cwd` is ambiguous on this machine across seven live checkouts, each with its own build tree at a different commit. | Specify the binding as an explicit input: one path built from a slug an env var supplies, any session without it out of scope and silent. Specify how the hook obtains the project root and memory root. Add a two-worktree AC. |
| 25 | high | `spec:61` (S14) | The "MEASURED NO-OP" widening has no writer and no owner: the only thing that writes the hook entry is absent from both §4's table and §7's gate list, and widening it reds a bar leg. | Add `tools/settings-merge.py` and `.claude/settings.json` to §4, add the settings-merge selftest to §7, state whether the widening is a second fragment or a changed matcher, and add an AC that the selftest's matcher arms move in the same commit. |
| 7 | medium | `spec:9` (§1) and the H1 | §1 and the title bound this unit to resolving the verifier NUMBER; S14 enforces a MODALITY and explicitly disclaims the number. Neither line moved at rev-3. | Rewrite §1 to state both halves and retitle to something the fold does not falsify. Log the §1 and title change in the §9 rev-3 line, which today records only that S14 was added. |
| 8 | medium | `spec:141` (§4 Rollout) | Rollout still reads "One commit, gated by the full bar" while S14 mandates a measured no-op commit first and only then the refusal; "MEASURED" is nowhere defined. | Rewrite Rollout as the ordered sequence, name the no-op observation concretely, and state that S13's byte-parity re-copy does not cover `.claude/settings.json`, so the matcher needs its own wiring check. |
| 9 | medium | `spec:238` (§7) | §7 lists six legs, none covering S14, and both legs S14 necessarily moves already exist and are unnamed — one of which hard-pins the exact matcher string S14 changes. | Add `tools/check-wiring.test.sh` and the settings-merge selftest to §7, note the hardcoded matcher assertions, and amend the closing sentence to name the two items that extend existing legs. |
| 18 | medium | `spec:190` (§6), with `spec:80` (§3) | The one scope item written by a non-owner after the Tier-2 is the only one nothing observes; the "MEASURED NO-OP" names no corpus, and no fixture anywhere feeds an `Agent` payload. | Add the four missing ACs, list the four missing files in §4, and either withdraw the §3 non-goal that calls `check-wiring.sh --check` "cheap and unrelated" or restate its rationale now that S14 edits that script. |
| 26 | medium | `spec:70` (S14) | The claimed `check-wiring.sh` fix is in neither §4's table nor §7's gates, and the "two fragments" model collides with the single documented `HOOK_MARKER`. | Add `tools/check-wiring.sh` and `.claude/settings.json` to §4 and `tools/check-wiring.test.sh` to §7, and state the mechanism: distinct per-fragment markers, or a declared fragment list the script can read. Add the UNWIRED AC. |
| 27 | medium | `spec:141` (§4) and `spec:187` (§5) | The staged rollout falsifies both "One commit" and "revert is one commit", and the single version bump cannot straddle two commits without either an unbumped contract or a premature marker. | Rewrite Rollout and the §5 migration line for the actual sequence, name which commit carries the version bump and why, and state whether reverting the refusal also reverts the matcher. |
| 28 | medium | `spec:236` (§7) | The fold moved an edit that must reference another build's file contract into a spec that never absorbed that build's zero-headroom drift constraint, and §7 omits the leg enforcing it. | Carry the constraint into this spec verbatim, add `python tools/drift-audit/drift_report.py --check` to §7, and state how S14 documents its dependency without a product-source citation of a non-terminal id. |
| 11 | low | `spec:46` (S10) | S10 moves only the agent-cap version pair while S14 changes the wiring contract `tools/settings-merge.py` ships to adopters, whose kit version stays at 1.0 — the exact reasoning S12 applies to the sibling kit. | Extend S10 (or add S15) to move `KIT_SETTINGS_MERGE_VERSION` and its `gov:kit settings-merge@` marker together, with a migration line telling adopters to re-run the merger. Add an AC in AC14's shape. |

## Findings in full

### 1. The fold created a cycle, and neither spec records the back-edge — blocker

S14 keys its refusal on "the consuming build's run-state file". The status header names that build,
and its run-state file is `RUN.md` — a name that is illegal in this tree today. I grepped
`tools/memory-tree/check-memory-hygiene.sh:275`: at a build-folder root the whitelist is exactly
`F:README.md`, `F:STATUS.md`, `D:prompts`, `D:spec`, `D:build`, `D:reviews`, and the dated-recording
grammar at `:265` admits only `<date>-(prompt|spec|build|review)-…`. The consuming spec's §1:12-14
independently records a fixture reddening with `HYGIENE check 4 FAILED — build-folder naming/shape`.

The dependency is recorded one-way in both files and in opposite directions: this spec's `§9:277`
says the other build "depends on it landing", and the other spec's `§9:233` says "this build gained
a dependency on it". `git show 58dd43d` proves the fold added no note beyond that one line, so
neither owner's file shows the cycle. The header is SPECCED, while `memory/TEMPLATE-SPEC.md:37-38`
defines BLOCKED as exactly "waiting on an external prereq". A builder taking this at SPECCED either
ships a refusal against a file that reds hygiene — AC18 requires all 40 legs green — or ships it
inert and marks S14 done.

Scoped honestly: a fixture in a `mktemp` dir would not itself red hygiene, so "cannot be built" is
stronger than "cannot be exercised against a real run-state file in this tree". The unrecorded
back-edge is the part that is squarely a fold consequence neither spec absorbed, and it stands.

**Correction:** split S14 at its own seam. The matcher widening is genuinely self-contained and
provably a no-op at `agent-cap.js:305`; keep it here. Move the run-state-keyed refusal to a scope
item that cannot start before the other build's unit 1 lands — either by flipping the header token
to BLOCKED with the prereq id in the tail, or by stating in S14 that the refusal half lands in a
follow-on commit gated on the run-state filename being whitelisted, and saying so in §4 Rollout.
Add a line to §7 naming check 4 of `tools/memory-tree/check-memory-hygiene.sh` as the prereq gate.

### 2 and 18. S14 has no acceptance criterion, no gate leg and no file row — blocker

`git show 58dd43d -- <spec>` shows the rev-3 fold added ZERO lines to §6: the diff is the status
header, the S14 bullet, and the §9 line. Mapping the criteria against scope: AC1-3 to S1, AC4-5 to
S2, AC6-7 to S3, AC8 to S4, AC9 to S4/S5, AC10 to S5/S6, AC11 to S7, AC12 to S8, AC13 to S9, AC14
to S10, AC15 to S11, AC16 to S12, AC17 to S13, AC18 to the bar. Nothing is left for the widened
matcher, the modality refusal, the fail-open, the session binding, the distinguishable deny string,
or the `check-wiring` grep fix. AC18 — "all 40 legs pass", and `tools/gate-legs.json` does hold
exactly 40 — is the unrelated-green-gate form `memory/TEMPLATE-SPEC.md:134-136` bans.

The only apparent coverage is AC13 via S9, and it cannot bind as written: `agent-cap.test.sh:30`'s
payload builder hardcodes `{"tool_name":"Workflow"}`, every arm at `:38-48` and `:190-204` pins
`Workflow`, and the single non-`Workflow` arm at `:40` uses `Bash`. So no fixture anywhere feeds an
`Agent` payload, and the "MEASURED NO-OP" has no corpus — S13's byte-parity arm at `:215-227` diffs
the two hook files, not the matcher. `memory/TEMPLATE-SPEC.md:103` requires every scope item be
verifiable at DoD. This is the same defect this spec's rev-2 was reddened for (the prior review's
finding 10 is titled "S6 has no acceptance criterion") and the class recorded at
`memory/gotchas/fixture-passes-by-finding-nothing.md`.

`spec:80` compounds it: §3 still carries `bash tools/check-wiring.sh --check` as a non-goal on the
rationale "Cheap and unrelated" — a rationale S14 falsifies by editing that very script.

Recorded as non-disqualifying nits: `check()` takes raw JSON, so a builder COULD add an `Agent` arm
and make AC13 bind — but no scope item or AC asks for it, and AC13 would cover at most one of
S14's six claims. §7 has six bullets, not five.

**Correction:** add ACs phrased as observations, one per S14 claim — (a) an `Agent` payload with no
run-state file present exits 0 and writes nothing to stderr; (b) with a run-state file declaring a
verify phase, the same payload exits 2 with a message containing a string unique to this branch,
asserted by `grep -qF`, not by exit code; (c) a non-verify phase exits 0; (d) a `Workflow` payload
is byte-identically handled before and after the widening; (e) with only one of the two matcher
groups carrying the agent-cap command, `bash tools/check-wiring.sh --check` reports UNWIRED naming
the missing one, and reports ok with both. Note in S9 that the payload builder at
`agent-cap.test.sh:29-34` must gain a `tool_name` parameter, or the new arms cannot be written.
List the four missing files in §4. Withdraw or restate the §3 non-goal.

### 3, 13 and 25. "The matcher widens" is unspecified, unowned, and not gate-neutral — blocker

The §4 Files-touched table at `:148-161` is 12 rows and names none of `.claude/settings.json`,
`tools/settings-merge.py`, `tools/check-wiring.sh` or `tools/check-wiring.test.sh`; the fold added
no row. Meanwhile the consuming build's `§4:133` explicitly disclaims `tools/check-wiring.sh` as
"Not touched" — so after the fold no spec's file list claims it, which is the mirror of the failure
its own `§3:50-51` names: "Two specs claiming one edit is how a half-applied change passes every
gate."

I measured the consequence directly. `.claude/settings.json:5` is `"matcher": "Workflow"`, and
piping `{"tool_name":"Agent","tool_input":{"prompt":"const r = await parallel(x.map(y))"}}` into
`node tools/hooks/agent-cap.js` exits 0 at the `:305` tool gate. A builder following the table edits
only the kit hook, the modality stays unhooked, and the bar stays green.

Then I reproduced all three candidate spellings in a scratch tree against copies of this repo's real
`.claude/settings.json` and `tools/settings-merge.py`:

- **A second fragment via `--fragment`.** Exited 0 and APPENDED a second `PreToolUse` group, leaving
  the existing `"matcher": "Workflow"` group intact. Both groups dispatch the identical
  `node "${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js"`, so the hook fires twice on every
  `Workflow` call. `merge()` at `:97` keys the group lookup on exact matcher equality and the
  docstring at `:34-38` confirms it never rewrites a stale entry.
- **A hand-widened single group.** The built-in fragment printed
  `settings-merge: DRIFT — .claude/settings.json is missing the agent-cap Workflow hook`, exit 1,
  and a plain re-run silently re-added the narrow group; matchers afterwards were
  `['Workflow|Agent', 'Workflow']`. Adopters re-running the documented WIRE step at
  `WIRE-INTO-PROJECT.md:384` land in this state silently.
- **Widening `AGENT_CAP["matcher"]` at `:56`.** `--selftest` fails at the `"Workflow"` literal pin
  on `:165/:166` (control: the unmodified kit copy prints `settings-merge selftest: PASS`); the
  matcher is pinned literally again at `:179`, `:188` and decisively at `:212`
  (`assert [g["matcher"] for g in both["PreToolUse"]] == ["Workflow"]`). That selftest is gate leg
  `tools/gate-legs.json:246`, so the bar reds.

So the "provably safe no-op" commit is not gate-neutral on the natural implementation path, and the
spec assigns the edit to no file and no gate — against §7's closing claim that "Every other
assertion lands in a leg that already runs".

There is also no fragment to pass: a tree-wide search for `*.fragment.json` returns only
`tools/memory-recall/recall-opened.fragment.json`. `check-wiring.sh:102` prints
`Fix: $PY tools/settings-merge.py` as the remedy and `:11-12` forbids auto-applying it, so S14's
improved detector would report UNWIRED with a printed remedy that provably cannot reach the state it
detects.

**Correction:** state in S14 which shape the widening takes — a second group plus a shipped
agent-cap fragment file the merger can write, or one group with a regex matcher — and say which,
because `settings-merge.py:97` and `check-wiring.sh:43` behave differently under each. If it is the
widened built-in matcher, scope the four selftest assertions as edits. Add rows to §4 for
`.claude/settings.json`, `tools/settings-merge.py` and its selftest, `tools/check-wiring.sh`,
`tools/check-wiring.test.sh`, the `agent-cap.js:24` wiring block and `WIRE-INTO-PROJECT.md:384`. Add
the settings-merge selftest and the check-wiring self-test to §7. Add an AC that a merger re-run
after the widening leaves the file byte-identical.

### 4, 12 and 24. The session-to-build binding is named as an obligation, never discharged — blocker

`spec:67-69` states the obligation verbatim — "Two things this unit must state rather than imply:
the fail-open when no run-state file exists, and the session-to-build binding, without which the
refusal is either arbitrary or a tree-wide false deny" — and then supplies no mechanism. I grepped
§4 (spec lines 86-172) for run-state, fail-open, session, phase, modality, matcher, `Agent` and
settings.json: the only hit is the S13 sentence naming `.claude/settings.json:9`. §8 carries no
fork. The fold added nothing to either section.

The binding half is not merely unwritten, it is unsupported by the cited evidence. The measured
`PreToolUse` payload keys are `session_id`, `prompt_id`, `transcript_path`, `cwd`,
`permission_mode` and `tool_use_id` — none names a build, and `cwd` resolves to a repo root, not to
a build folder. The consuming build's authored region is frozen at "exactly five facts and nothing
else" (mandate, phase, keepalive id, parked decisions, BASE sha) — none of them a session id. There
are 23 build folders in this tree.

`cwd` is worse than merely coarse on this machine. `git worktree list` shows the primary tree plus
six worktrees under `.claude/worktrees/`, each a full checkout with its own build tree at a
different commit (`b8e33b1`, `f9675d0`, `d55474d`, `e7ec336`, `63687a1`, `4ce97c0`). A cwd-derived
root therefore resolves to a different run-state file per session at a different branch state, and
the only uniqueness guarantee — the consuming build's unit-4 assertion that at most one run-state
file is in a non-terminal phase — is a merge-bar assertion inside one tree that does not run during
a session.

Closing the gap by adding a sixth authored fact reopens a contract that build has already ratified
at five, and the landing order is backwards: `spec:277` puts the run-state contract downstream of
the code that reads it. This is precisely the fold consequence neither spec absorbed — and the
other build's own Tier-2 told it to "Name the binding here, before the dependency spec goes to
rev-3 … State the fail-open for both the absent and the ambiguous case." Rev-3 restates the
obligation and states the absent case only.

Recorded as loose supporting links I discount: S14 does not itself enumerate the payload keys (the
other spec's `§9:230-231` does); and the other spec's `§3:49-51` reserves agent-cap EDITS to this
build without forbidding a sixth run-state fact. An env var or a conventional single-run path would
also bind without one.

**Correction:** specify the binding as an explicit INPUT rather than an inference. Name the
mechanism and the field it reads — the run-state file records the session id the preflight pinned
and the refusal fires only when the payload's `session_id` equals it, or a slug arrives from an env
var the unattended driver exports and any session without it is out of scope, fails open, silent.
Specify how the hook obtains the project root and the memory root, since the hook reads no conf
today and gets `${CLAUDE_PROJECT_DIR}` only inside its command string. Add a §4 sub-head carrying
the resolution order and a §8 fork if the field does not exist, and record the cross-spec
obligation against the other build's five-fact list and its AC set. Add an AC with two worktrees
proving one is bound and the other untouched.

### 21 and 22. "A verify phase" names an undefined token, at a granularity that cannot compose — blocker

The consuming spec never enumerates the phase set. The only definition is "from a closed vocabulary
that unit 4's leg validates", plus "Validating the phase vocabulary. Unit 4's leg owns it" and a
reference to "the declaration that F3 makes project-owned". A grep for `phase` across that spec and
its README returns no token list anywhere, and unit 4 is unwritten. F3 reads "the full protocol
travels to adopters, with the phase vocabulary and the DoD assertion set as project-owned
declarations" — and the kit-owned floor that build's review added is scoped to the DoD set, not to
the phase vocabulary.

Against that, `agent-cap.js:3` declares itself "project-agnostic" and this spec's `§4:142` says the
hook is "deployed verbatim into adopting repos". The hook reads only stdin plus an optional script
path at `:298-325` and has no route to any project declaration. So the builder must hardcode a
token; whichever one, an adopter that renames its phase under F3 silently loses the refusal with no
signal (it fails open), and unit 4's leg validates a declaration the hook never read — two answers
to one question, and `memory/gotchas/two-answers-to-one-question.md` is marked universal, so it is
the class the machine asks every reviewer of this diff about.

The granularity is a second, independent defect. The phase vocabulary is framed explicitly against
the seven-token status enum — "CLOSED in the spec vocabulary already means 'built AND landed' and
there is no token for 'built and reviewed, not yet merged'" — a run-lifecycle set, and every phase
claim must carry a git-checkable witness. A review's verify STAGE produces no commit and spans no
git-visible state. Both horns fail: run-grained, the modality refusal denies every direct spawn
across the whole review-shaped stretch of the run, including the find stage that
`memory/guides/REVIEW-PROTOCOL.md:94` prescribes scaling by adding LENSES (up to 6 at
`agent-cap.js:97`) — a false deny of the protocol's own recommended path; stage-grained, the driver
must rewrite the phase per review stage, a write cadence no unit specifies and one that cannot
carry the required witness.

**Correction:** mirror F3's own floor — state in S14 that the phase vocabulary carries a KIT-OWNED
reserved token the project declaration may extend but never rename or delete, name that token
literally, and name the file the hook reads it from plus how the hook resolves that path. Add an AC
asserting a renamed or absent token DENIES rather than allows. Then stop keying on the run phase:
key the refusal on a distinct, short-lived verify-stage assertion the review harness itself sets
and clears, with its own token and no witness obligation, or restate S14 as refusing only direct
spawns that a run-phase-scoped mandate has not whitelisted. Add an AC proving a 3-6 lens find-stage
fan-out is NOT denied while the phase is set. If the declaration format must be owned by the other
build's unit 4, the refusal half cannot be specified until unit 4 is.

### 5. Two published statements of the wiring block fall outside S7's range — high

`agent-cap.js:22-26` is the Wiring block and `:24` reads `"matcher": "Workflow"`. S7 at `spec:37-39`
enumerates `README.md:50`, `WIRE-INTO-PROJECT.md:388` and `tools/hooks/agent-cap.js:14-21` — the
range stops one line above the wiring block, and `:388` is the AGENT_CAP prose sentence, not the
matcher JSON at `:384` (confirmed by reading both lines). `grep -n 'AGENT_CAP' README.md
WIRE-INTO-PROJECT.md tools/hooks/agent-cap.js` returns `README.md:50`,
`WIRE-INTO-PROJECT.md:388`, `agent-cap.js:19`, `:37`, `:38` — so AC11 structurally cannot see a
stale matcher at either site.

Since `§4:142` records that the hook is deployed verbatim into adopting repos, its header IS the
adopter-facing wiring contract: after S14, every adopter reads a docstring telling them to wire a
matcher that no longer catches the modality the bumped version advertises. That re-opens, one
paragraph below S7's own range, precisely the false-record class the prior review's finding 7
closed — whose correction was literally "extend S7 to name `tools/hooks/agent-cap.js:14-21`".
Neither S7 nor AC11 moved at rev-3. (Citation slip that does not affect the substance: the
"deployed verbatim" sentence is at `§4:142`, not `:143`.)

**Correction:** extend S7 to name `tools/hooks/agent-cap.js:22-26` and `WIRE-INTO-PROJECT.md:376-386`,
and the `tools/settings-merge.py:7-13` module docstring which publishes the same block. Widen AC11
with a second grep asserting that no wiring-block site states a matcher narrower than what S14
requires.

### 6. §4 has no design for S14, and its one adjacent passage dismisses S14's territory wrongly — high

My grep over spec lines 86-172 found no mention of the `Agent` modality, run-state, refusal, matcher
or phase. The Inventory table's six rows at `:94-99` have no row for the unhooked modality; "The
predicate change" at `:108-130` covers S1-S4 only; Migration at `:133-138` covers AGENT_CAP and the
args knobs only; Alternatives-rejected has no entry for the refusal-versus-count choice S14 makes.

Instead `:167-168` rejects runtime counting citing `memory/guides/REVIEW-PROTOCOL.md:42`, which
reads: "Nothing counts agents at runtime — a workflow script runs in a sidechain with no hooks and
no filesystem." That reason is scoped to a workflow SIDECHAIN and is false of a direct `Agent` tool
call, which is a main-loop call that fires `PreToolUse` — that is S14's entire premise, and the
four-call burst producing overlapping hook processes is itself proof the hook fires on those calls.
Meanwhile S14's actual reason for refusing rather than counting sits in a §2 bullet, where
`memory/TEMPLATE-SPEC.md:109-113` assigns mechanism to §4. A reviewer or builder reading §4 alone
concludes counting was considered and closed.

**Correction:** add a §4 sub-head for S14 (the canonical names allow a new `###` under §4) carrying
the modality inventory row (a direct `Agent` call fires `PreToolUse` and reaches no rule today), the
refusal-not-count decision with the counter-race measurement, the resolution order from payload to
run-state to phase, and the placement of the refusal branch relative to `agent-cap.js:305-325` — it
must land before the script extraction at `:311`, since an `Agent` payload has neither script nor
path and `:325` exits 0. Amend the rejected alternative at `:167-168` to scope its reason to the
sidechain modality, and add a rejected alternative for counting spawns across hook processes citing
the burst measurement.

### 14 and 26. The `check-wiring.sh` fix is real, and has no material to work with — high

I confirmed the defect by running the script's own predicate — `wired() { … grep -qF "$1"
.claude/settings.json; }` at `:43`, called at `:99` with the literal `agent-cap.js` — against three
settings files: narrow group only, widened group only, and both. It printed the `ok  agent-cap`
verdict in all three. It cannot distinguish them because `_command()` at `settings-merge.py:82-84`
builds the identical string from the same hook path, and `HOOK_MARKER = "agent-cap.js"` at `:49` is
a single constant serving as both dedup key and the deployer's is-it-wired grep target — the file
documents it as exactly that at `:20-21`.

`check-wiring.sh:92-94` already records the limitation in a comment ("agent-cap's hook path is not
declared anywhere this script can read") and names the recall arm at `:118-150` as the shape that
CAN do it, because that fragment declares its hook path. So making the grep per-fragment requires
first deciding where the fragment set is declared — a design decision S14 does not make. S14 asserts
the fix in one clause and specifies neither the new predicate nor the fragment file that would carry
it, so the half-wired state — the state the widening commit passes through — keeps reporting `ok`.
S9 budgets new arms for `agent-cap.test.sh` only; `tools/check-wiring.test.sh` is a bar leg whose
only nearby arm is the adopted-but-unwired case at `:100-106`.

**Correction:** ship a `tools/hooks/agent-cap.fragment.json` per fragment (name, event, matcher,
marker, hook path) with DISTINCT markers so the file-wide grep stays a valid key, and rewrite
`check_agentcap` at `check-wiring.sh:90-105` to read matcher and marker from it the way
`check_recall_opened` at `:118-150` already does — which also retires the "skip agent-cap — hook
path not declared anywhere this script can read" limitation. Add an arm to
`tools/check-wiring.test.sh` for the one-of-two-wired state, plus the matching AC: one fragment
wired and the other absent must print UNWIRED, not `ok`.

### 15 and 23. §5's fail-closed claim is falsified twice over — high

`spec:175` reads "security — the hook is a guard; every new branch fails closed, matching
`agent-cap.js:242-245`". That citation says exactly what §5 claims: `:242-245` is the FAIL CLOSED
block ("An iteration construct this rule cannot PROVE bounded is denied; the burden is on the
fan-out, not on the gate") and `:262-268` denies any receiver the file cannot prove bounded. S14's
`:68` requires a fail-open. `git show 58dd43d` proves §5 was not revisited at rev-3.

Per `memory/TEMPLATE-SPEC.md:130` the §5 sweep is what becomes the owner's scope menu, so the
contradiction is load-bearing. A builder reading §5 as binding implements the `Agent` branch
fail-closed and denies every direct spawn in any repo with no run-state file — the tree-wide false
deny S14 itself warns about one line later. A builder reading S14 instead ships a guard whose §5
security line is a false claim of the same species as the AGENT_CAP override claim S7 exists to
delete.

There is a second, sharper hole in the same clause. S14 scopes the fail-open to exactly one case —
"no run-state file EXISTS" — leaving present-but-unparseable undefined. The writer the consuming
build reuses is not atomic: `gen_build_index.py:75-80` is `def write_text` doing
`with open(path, "wb")`, truncate-in-place, and it is the writer behind the render path the other
spec reuses verbatim. A hook reading during a region re-render sees a truncated file, finds no
phase, and fails open — the guard silently disarmed exactly while the driver writes, allowed
nondeterministically and unreproducibly. The measured overlapping hook processes are evidence the
window is real. (Recorded caveat: that build's driver is unwritten, so the truncation window is a
consequence of the writer the spec names rather than of code that exists today. The unspecified
branch and the falsified claim are on the page regardless.)

**Correction:** rewrite the §5 security line to state the split explicitly — the static rules fail
closed as before, and the modality refusal fails OPEN by design when no run-state file is present —
and add the fail-open to the §5 risks line with its residual named. Then split the state into
three, not two: ABSENT fails open and silent; PRESENT-and-parseable decides;
PRESENT-but-unreadable/unparseable DENIES with its own string, matching the existing script-path
precedent at `agent-cap.js:317-322` ("a script this hook cannot read is not a script this hook may
approve"). Pin an atomic write (temp plus `os.replace`) as a cross-spec obligation on the other
build's driver unit.

### 16. The measurement refutes a read-then-decide counter, not counting — high

`spec:64-66` concludes "It does NOT count" from an overlap in which "two of four read the same
counter value". That is a lost-update race, whose textbook fix is an atomic primitive, not
abandonment — and the same sentence's own measurement set includes `tool_use_id`, exactly the key
that makes the count atomic. I verified in node on this NTFS host that
`fs.writeFileSync(p,'',{flag:'wx'})` throws `EEXIST` on a second create, with `readdirSync(dir).length`
giving the count, so an exclusive-create-per-`tool_use_id` counter cannot lose an entry under
precisely the observed overlap, and is idempotent under a retried id.

The substitution also mismatches the rule it serves. `memory/guides/REVIEW-PROTOCOL.md:7-13` caps
verify-stage agents at 5 TOTAL — a cardinality — while a modality refusal is binary and inherits
both of the binary's failure modes: 0 during a declared verify phase, which forbids the 3-6 lens and
batched-skeptic configuration `:83-85` prescribes and which a legitimate review running 3 direct
verifiers is permitted, and unbounded outside one via S14's own fail-open. Ratifying "cannot count"
in the record also forecloses the fix for whoever picks this up next.

**Correction:** narrow the rationale to the claim the measurement supports — a read-then-decide
counter loses updates under overlapping hook processes — then either specify the exclusive-create
token-file count keyed on `tool_use_id`, or raise the choice as a §8 fork (modality refusal versus
atomic count) with the residual written down: the ≤5 NUMBER stays unenforced for direct spawns.

### 17. The refusal never reaches the modality the rule exists for — high

The refusal is gated on the consuming build's run-state file with an explicit fail-open when none
exists, and that file exists only for unattended runs — the other spec's `§1:7` says "so an
unattended run has one durable place to record what only it knows", written by its unit 3's
preflight. An interactive review session therefore has no run-state file, takes the fail-open, and
its direct `Agent` fan-out stays exactly as unenforced as today.

That modality is the primary one, not an edge case. `agent-cap.js:76-79` records that the failure
this rule exists for "was written as an INLINE `script` on a `Workflow` tool call" in a live
session, and `memory/guides/REVIEW-PROTOCOL.md:32-36` calls the session path "**This is the primary
point**". Since S11 rewrites that BINDING document in the same unit, the protocol will read as
though the `Agent`-modality hole is closed when it is closed only for unattended runs — the same
overstated-reach defect as the AGENT_CAP claim this spec's §8 F1 cites as surviving two releases.
Neither spec absorbs the residual: the protocol's "What neither reaches" section at `:40-42` is not
in S11's stated edit set, and the fold added no non-goal, no §5 line and no fork for it. (The
finding's §1 citation is loose — §1 is about resolving the number — but the coverage gap stands on
S14's own text.)

**Correction:** state the residual inside S14, and carry it into S11's rewrite at the protocol's
"Enforcement — and where it does NOT reach" section at `:28-42`, which exists to enumerate exactly
this. Add an AC that greps the rewritten protocol for the stated modality residual, mirroring
AC15's shape.

### 7. §1 and the title no longer bound §2 — medium

`spec:9-10` reads "This unit makes the hook resolve the number wherever a bound is written", and the
H1 reads "agent-cap enforces the verifier number, not just the helper shape". `git show 58dd43d`
shows the rev-3 diff touched neither — the only edits were the header line, the S14 bullet and the
§9 line. S14 explicitly disclaims the number ("It does NOT count") and enforces a modality instead.

§2 is supposed to be bounded by §1, so the spec's own statement of what it is for now excludes its
newest scope item. Three incompatible statements of the unit's surface coexist: the number
(`§1:9`), "every agent-cap edit" (`§9:277`), and a modality gate keyed on another build's file. A
downstream reader deciding whether a future edit belongs here has no correct answer. This is the
class the prior review escalated to a blocker at rev-1 — its finding 1 was explicitly a merge of
three angles including the goal statement, so §1 was rewritten at rev-2 for exactly this and was not
rewritten at rev-3. Medium, not higher: it is a record defect, not a build blocker.

**Correction:** rewrite §1 to state both halves — the hook reads no bound (S1-S4) and reaches only
one of the two spawn modalities (S14) — and retitle to something the fold does not falsify. Log the
§1 and title change in the §9 rev-3 line, which currently records only that S14 was added.

### 8 and 27. Rollout and rollback both contradict S14's own commit sequence — medium

§4 Rollout reads "One commit, gated by the full bar" (the sentence sits at `:142`, under the head at
`:140`) and `§5:187` reads "migration / rollback — revert is one commit". S14 at `:61-63` mandates
two: the matcher widens "as a MEASURED NO-OP commit first … and only then gains a per-call refusal".
Both lines were written at rev-2 and neither moved; the §9 rev-3 entry records only that S14 was
folded in and unreviewed.

The contradiction is load-bearing, not cosmetic: the no-op commit is the whole safety argument for
touching the executed `.claude/settings.json` ahead of any behaviour change, and folding it into one
commit destroys the property S14 relies on. Nothing states what "MEASURED" means — no procedure, no
AC, no artifact — so the safety step can be skipped with the bar green. The version contract goes
with it: S10 moves the agent-cap constant and its `gov:kit agent-cap@` marker 1.1 to 1.2 exactly
once, and the hook's own header documents the matcher as part of the wiring contract it ships, so a
first commit that widens the matcher either ships a contract change under an unbumped marker — the
precise failure S10 and S12 exist to prevent — or moves the marker ahead of the contract. An
operator following `§5:187` reverts one commit and leaves the widened matcher wired with no refusal
behind it. Rollout also still attributes the contract signal to S10's bump and the take-effect to
S13's re-copy, and S13 is scoped at `:57-59` to `.claude/hooks/agent-cap.js`, not to
`.claude/settings.json`, whose matcher is what actually decides whether the hook fires.

**Correction:** rewrite §4 Rollout and the §5 migration line as the ordered sequence S14 requires —
commit 1 widens the matcher in `.claude/settings.json` plus its merger fragment and its docs, with
the no-op observation named concretely (feed the current `Workflow` arms of `agent-cap.test.sh`
before and after and require identical output); commit 2 adds the refusal branch. Name which commit
carries the version bump and why. State that reverting the refusal also reverts the matcher, or that
the widened matcher is a safe standalone state because `agent-cap.js:305` exits 0 on any
non-`Workflow` tool name. State that S13's byte-parity re-copy does not cover
`.claude/settings.json`, so the matcher needs its own wiring check.

### 9. §7 names neither leg S14 necessarily moves — medium

§7 lists six legs at `:231-236` — `agent-cap.test.sh`, `check-verifier-fanout.sh`,
`check-protocol-parity.test.sh`, `check-kit-versions.sh`, `check-memory-hygiene.sh`, `run-gates.sh` —
and gained nothing at rev-3. Both affected legs already exist and are named in
`tools/gate-legs.json`: "check-wiring self-test" (`bash tools/check-wiring.test.sh`) and
"settings-merge selftest" (`python3 tools/settings-merge.py --selftest`). Neither appears in §7,
while S14's last sentence explicitly commits to moving `check-wiring.sh`'s marker grep at `:43`,
consumed at `:99`.

The settings-merge leg is the sharper hazard, and I verified it live: the selftest PASSes today and
pins the matcher literally at `:165`, `:179` and decisively at `:212`, so any second matcher group
or changed matcher in the built-in fragment reds a leg the spec does not mention — and a builder who
instead leaves the fragment alone ships a detector whose remedy cannot reach the state it detects.
Scoped honestly: §7's closing sentence "Every other assertion lands in a leg that already runs" is
under-informative rather than strictly false, since both unnamed legs do already run. The operative
defect — an unrevisited §7 naming neither leg, one of which hard-pins the exact string S14 changes —
is confirmed. It is the same self-referential shape the prior review's finding 8 recorded against
S10.

**Correction:** add `tools/check-wiring.test.sh` and `python tools/settings-merge.py --selftest` to
§7, note that `settings-merge.py:165/:179/:212` hardcode the matcher and must move with the
fragment, and amend the closing sentence to name S10 and S14 as the two items that extend existing
legs.

### 28. The zero-headroom drift constraint did not travel with the folded item — medium

I ran `python tools/drift-audit/drift_report.py --check`:
`non_terminal_specs_cited_by_product_source 2 20 ok (pin 2, drain it)`, exit 0.
`drift_report.py:262-271` sets tolerance 0 and gateable true; `:496` flags OVER PIN over the pin;
`drift_signals.py:129-137` pins 2 and names the two current claimants; the product globs at `:20-28`
include `tools`. The oracle at `:254` is a plain `git grep -l -F <own id>` over those globs.

The consuming build is SPECCED with six of seven units unwritten, so a single citation of its id
from `tools/hooks/agent-cap.js` or `tools/check-wiring.sh` makes it a third claimant and reds
`drift-audit records`, one of the 40 legs AC18 requires — while NOT citing it leaves the hook's
dependency on another build's file contract undocumented in the only file that implements it. That
build's `§7:201-204` states the constraint verbatim ("measures 2 against a pin of 2, with zero
headroom. No file under `tools/`, `skills/`, `.claude/` … may cite this build's own ids while the
owning sub-spec is non-terminal"), and it did not travel with the folded scope item: this spec's §7
lists six gates and not the drift check, and the constraint appears nowhere in it — its only
drift-audit mention at `:79` is the unrelated pin-raise non-goal.

**Correction:** carry that constraint into this spec verbatim, add
`python tools/drift-audit/drift_report.py --check` to §7's gates, and state how S14's implementation
documents its dependency without naming a non-terminal id — e.g. by referencing the run-state file's
path and phase contract only, with the build id cited from `memory/`, deliberately outside the
product globs, instead of from `tools/`.

### 11. The merger's own kit version does not move with the contract it ships — low

`tools/settings-merge.py:48` carries `KIT_SETTINGS_MERGE_VERSION = "1.0"` and
`tools/check-kit-versions.sh:25` presence-gates it as a deployer signal — that file's header says
"Every kit carries a well-formed version constant a deployer can grep in a target repo".
`settings-merge.py:53-59` is the built-in fragment shipped to adopters, hardcoding
`"matcher": "Workflow"` at `:56`, so "the matcher widens" can only reach an adopter by changing that
fragment.

The spec states the governing principle verbatim for the sibling case at `§4:136-138` — "the
contract change must be visible to version detection" — and acts on it in S12, while S10 moves only
the agent-cap pair. The rev-3 diff added no version handling for the merger, and the merger is
absent from §4's table entirely. Whichever branch the builder takes — edit the fragment and the
contract moves silently at 1.0, or leave it alone and adopters never get the widened matcher — no
version signal moves. Applying the principle to one kit and not the other in the same commit leaves
an adopter at an unchanged version with a hook wired to catch only half the modalities the bumped
agent-cap advertises. Low only because the wiring is idempotent and re-runnable. (Wording quibble
that does not affect the defect: the contract widens, it does not narrow.)

**Correction:** extend S10 (or add S15) to move `KIT_SETTINGS_MERGE_VERSION` and its
`gov:kit settings-merge@` marker together, with the same constant-versus-marker reconciliation S10
adds for agent-cap, and add a migration line telling adopters to re-run the merger after the kit
update. Add an AC in the shape of AC14: bumping only one of the two literals reds
`tools/check-kit-versions.sh`.

## Unverified

**None.** Every raw finding reached a verdict. 25 confirmed, 3 refuted, 0 unverified, 0 died in
verification. Nothing in this review is reported on the strength of a claim that could not be
reproduced against the file or the running tree.

## Refuted

**3 refuted** of 28 raw (raw ids 10, 19 and 20). Precision 0.89.

## What must change before S14 is built

Ordered by what unblocks what, not by severity. Items 1 and 2 are structural and make items 3
onward tractable; nothing below item 2 is worth drafting until the seam is chosen.

1. **Split S14 at its own seam.** The matcher widening is self-contained and provably a no-op at
   `agent-cap.js:305`; keep it in this unit. Move the run-state-keyed refusal to a separate item
   that cannot start before the consuming build's unit 1 lands, and correct the recorded dependency
   direction in both specs' §9 so the cycle is visible to both owners. Either flip the header token
   to BLOCKED with the prereq id in the tail, or state the gating in §4 Rollout.
2. **Decide the three undecided mechanisms, or fork them in §8.** (a) The session-to-build binding —
   as an explicit input (an authored session id matched against `data.session_id`, or a slug from an
   env var the driver exports), with the resolution order from payload to root to memory root to
   run-state file, and every session lacking it out of scope. (b) The phase token — a KIT-OWNED
   reserved token named literally, that a project declaration may extend but never rename, plus the
   file and path the hook reads it from; and whether the refusal keys on the run phase or on a
   short-lived verify-stage assertion. (c) Refusal versus atomic count — either narrow the "does not
   count" rationale to the read-then-decide race and specify the exclusive-create count keyed on
   `tool_use_id`, or fork it with the residual written down.
3. **Name the matcher spelling.** Second matcher group with a shipped agent-cap fragment file and
   distinct markers, or one group with a regex matcher. Say which: all three candidate spellings
   were run, and each fails differently — double-dispatch, silent undo on the next WIRE run, or a
   red `settings-merge` selftest.
4. **Add the four missing file rows to §4** — `.claude/settings.json`, `tools/settings-merge.py` and
   its selftest, `tools/check-wiring.sh`, `tools/check-wiring.test.sh` — plus the `agent-cap.js:24`
   wiring block and `WIRE-INTO-PROJECT.md:384`, and confirm with the consuming build's owner that
   its §4 "Not touched" line for `tools/check-wiring.sh` is now this spec's row.
5. **Add a §4 design sub-head for S14** carrying the modality inventory row, the refusal-not-count
   decision with its measurement, the resolution order, and the branch placement before the script
   extraction at `agent-cap.js:311`. Amend the rejected alternative at `:167-168` to scope its
   sidechain reason, and add a rejected alternative for counting across hook processes.
6. **Write the ACs.** One observation per S14 claim: fail-open exit 0 with no run-state file;
   refusal exit 2 asserted by `grep -qF` on a branch-unique string; non-verify phase exit 0;
   present-but-unparseable DENIES; `Workflow` handling byte-identical across the widening; a 3-6
   lens find-stage fan-out NOT denied; one-of-two-wired reports UNWIRED; a merger re-run leaves
   `.claude/settings.json` byte-identical; a two-worktree case proving one session is bound and the
   other untouched. Note in S9 that `agent-cap.test.sh:29-34`'s payload builder must gain a
   `tool_name` parameter first.
7. **Add the three missing gate legs to §7** — `bash tools/check-wiring.test.sh`,
   `python tools/settings-merge.py --selftest`, `python tools/drift-audit/drift_report.py --check` —
   note the hardcoded matcher assertions at `settings-merge.py:165/:179/:212`, and carry the
   consuming build's zero-headroom citation constraint into this spec verbatim.
8. **Reconcile the sections the fold falsified.** §1 and the H1 (both halves: the number and the
   modality); §4 Rollout and the `§5:187` rollback line (the two-commit sequence, and which commit
   carries the version bump); the `§5:175` security line (static rules fail closed, the modality
   refusal fails open by design, with the residual named); the `§3:80` non-goal that calls
   `check-wiring.sh --check` "cheap and unrelated"; and the §9 rev-3 entry, which should record the
   §1, title, Rollout and §5 changes rather than only that S14 was added.
9. **Extend the version work.** S7 to name the two uncovered wiring-block sites and the merger
   docstring, with AC11 widened to a matcher grep; and S10 (or a new S15) to move
   `KIT_SETTINGS_MERGE_VERSION` with its `gov:kit settings-merge@` marker, plus the adopter
   migration line and an AC14-shaped pair assertion.
10. **State the residual reach.** S14 refuses only under the unattended driver, so the interactive
    direct-spawn hole stays open — the modality the protocol calls primary. Write that into S14, and
    carry it into S11's rewrite at the protocol's "Enforcement — and where it does NOT reach"
    section, with an AC that greps the rewritten document for it.
