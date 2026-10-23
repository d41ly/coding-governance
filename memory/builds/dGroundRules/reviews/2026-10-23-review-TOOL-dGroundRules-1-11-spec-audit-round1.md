**Serves:** spec-audit TOOL-dGroundRules-1@rev-1 TOOL-dGroundRules-11@rev-1 TOOL-dGroundRules-2@rev-2 TOOL-dGroundRules-3@rev-2 TOOL-dGroundRules-4@rev-2 TOOL-dGroundRules-5@rev-1 TOOL-dGroundRules-6@rev-1 TOOL-dGroundRules-7@rev-1 TOOL-dGroundRules-8@rev-1 TOOL-dGroundRules-10@rev-1 TOOL-dGroundRules-9@rev-1

# Tier-2 spec audit — dGroundRules, the Policy build of the dClosedLoop chain (units 1-11)

Provenance: adversarial review, five finder lenses (gov-spec-reviewer), five skeptic batches (gov-skeptic), synthesis by gov-synthesizer. The build README is the mandate, because no run-mandate prompt exists. The build exists to close gap-spine-06, gap-tool-24 and gap-rt-34 through eleven spec-pinned units.

Reviewed: memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md@ed6bb94a4419b7509e28aaa5722bff0aef6c1f9c, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-11.md@c1e6b01e52a899db91f740ea46c581a3147a1a72, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-2.md@aecf790d35410ee8027781bc044c8f7c44fed35e, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-3.md@8556f7ea439e0d4083bc5deeea5f08c6dc4996b1, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-4.md@465c43ae834b0aa8b428fd9663c94d26ae9691a8, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-5.md@feac3751da1ee52e38774d6a777b27d80f67a12d, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-6.md@8552c78b1cd7ef2f0bc46e86c7047b38a3b59338, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-7.md@e17359dfe9b6ec3b18d9e88943073530869eeb8c, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-8.md@555243ca212cef3cb545b24ccc2e9a185baf00cb, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md@620ba22d8dd8aff691bbed050e62d4e71bff6d17, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-9.md@b96a65580418fc8f764e35a908cb7e48e900356f

ROUND 1

## Verdict: BLOCKED

One blocker item (two raw findings) stops the build: as written, the committed policy mirror can never match the commit that carries it.
The adjudicated tally by item is 1 blocker, 5 high, 28 medium and 8 low, which makes 42 items.
The tally by raw confirmed finding is 2 blocker, 6 high, 33 medium and 8 low, which makes 49 findings.
No confirmed finding was dropped, and none is counted twice.
Unit 11 drew no confirmed finding.

## Review shape

Intensity full, raw 56, confirmed 49, refuted 7, unverified 0 (0 uncertain), precision 0.88.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 11 | 11 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 9 | 8 | 1 | 0 | 0 | 0.89 |
| reuse | yes | 10 | 6 | 4 | 0 | 0 | 0.60 |
| blast-radius | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 13 | 11 | 2 | 0 | 0 | 0.85 |

### Run integrity

All 5 of 5 lenses returned, and none died.
All 5 of 5 skeptic batches returned, and none died.
No contradictory verdicts, orphaned duplicate refutations, spurious verdicts or duplicates were demoted or discarded.
Of the fixes on confirmed findings, 46 were judged sound, 3 were judged UNSOUND (ids 11, 37, 47, each carrying the skeptic's corrected fix below), none were left without a proposal, and none went unjudged.
No confirmed finding was left ungraded by a skeptic.
Five were re-graded by a skeptic (33, 34, 44, 45 from high to medium; 54 from medium to low), and each binding grade is applied below.
No unverified findings remain.
No lens notes were supplied, so every lens ran on the kit's generic brief.
Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
Intent: one spec document was supplied as `specs`, as sibling context.
Checklist: 76 items, each assigned to exactly one of 5 lenses (coherence 16, grounding 15, reuse 15, blast-radius 15, failure-envelope 15).
By design: none supplied.
Move check: no checked subject moved.

## Blocker

### B1. The mirror embeds the commit sha it was rendered at, so it is stale the moment it is committed (ids 1, 31)

- **Where:** spec-5 §4 "Data model — the mirror", "The render" and "The landing row"; S1-S3; AC1, AC2; §8 F2. The reason strings come from spec-2 §4 and spec-3's reason table.
- **What is wrong:** each mirror key stores its `Resolution.reason`. Units 2-3 spell every reason with the sha8 of the revision read, for example `set in .governance/policy.toml at 3708a705, ...`. F2 keeps the commit id out of the top-level fields because "a commit cannot carry its own id", but the roughly 270 per-key reasons still carry one.
- **Consequence:** a re-render at the commit that carries the mirror never matches its bytes. At a landing, push-main.sh:906-921 runs regen at the merge and then builds a new commit with `commit-tree`, so the landed mirror is stale at birth. `mirror --check`, `arm_mirror_parity` and the bar's `regen.py --check` preflight (run-gates.sh:1449-1458, exit 2) go red on every commit after unit 5 lands. AC2 cannot pass on a correct build.
- **Fix (judged SOUND by both skeptics):** make the mirror's bytes a function of the two blob ids alone. Either leave `reason` out and store only `value` and `source` (the helper rebuilds a reason from `policy_blob`), or render a reason with the sha8 and how-phrase normalised away (a fixed source phrase, with the helper prefixing the landed sha it read at). State this invariant in §4. Reconcile F2 ("renders before the merge commit exists") with §4 ("the render runs ... at the merge commit").
- **Left-shift gate:** a criterion that commits the rendered mirror and then runs `mirror --check` at the new HEAD, expecting exit 0. A build-time probe that runs push-main `--prepare` in a scratch clone and observes the bar's regen preflight green on the prepared merge.

## High

### H1. The `.agent-cap.conf` lowering has three homes, and the mirror misses it (id 2)

- **Where:** spec-10 §2 S1, against spec-5 §4 "The render" and spec-3 §3 / Non-goals.
- **What is wrong:** unit 10 puts the lowering in `resolve(...)`. Unit 5 renders the mirror through `resolve_read`. Unit 3 says a legacy home adds a `RESOLUTION_ORDER` step. The mirror's freshness pins only the policy and catalogue blobs.
- **Consequence:** `get runtime.agents-in-flight` prints the lowered value while the mirror holds the unlowered one. Rule 7 reads the limit through `readPolicy`, so it admits a hand-raised `env` up to 6 when the conf lowered it to 2. A conf edit leaves the mirror "fresh". `arm_mirror_landed` does not catch the conf-only case.
- **Fix (judged SOUND):** have unit 10 add its lowering as a `RESOLUTION_ORDER` post-step, or state that it lives inside `resolve_read`, so `get`, the mirror render, the last-valid branch and the settings render all pass through it. Have unit 5 record the `.agent-cap.conf` blob id, or every legacy input `resolve_read` reads, and have the helper compare it (see also M23, id 49).
- **Left-shift gate:** a unit 10 case: with `FANOUT_CAP=2` committed, `node policy-mirror.js get runtime.agents-in-flight` prints 2.

### H2. Gov-only arms ship in the adopter-facing `policy check` leg (ids 4, 37)

- **Where:** spec-1 §4 "The adopter" and AC9; spec-5 S4 (`arm_mirror_parity`); spec-7 S2, S5 and §4 "The arm" (`legacy-homes`); spec-9 S7 (`arm_cap_census`).
- **What is wrong:** unit 1 ships `policy check` as a repo-subject `[[gate_leg]]`, and `adopt-policy.sh --check` runs every arm in `ARMS`. Three later arms hold only on gov's own tree, and no spec scopes them away from adopters:
  - Unit 5's mirror-parity arm reds an absent mirror, and the scaffold writes none.
  - Unit 7's `tools/policy/legacy-homes.txt` ships gov's 115 rows, while the derivation reads the adopter's confs. Every gov row then reads as stale, every adopter key reads as unlisted, and shrink-only refuses to admit them.
  - Unit 9's census names gov enforcers. Some of them (`check-template-size.sh`, `check-spec-tokens.py`) are registry `[[exempt]]` and never reach an adopter.
- **Consequence:** once units 5, 7 and 9 land, every adopter that installs the policy kit gets a red repo leg and a red `--check`. Unit 1's AC9 stops holding. Every AC observes only gov's tree.
- **Fix (id 4 judged SOUND; id 37's proposal REJECTED, and the skeptic's corrected fix is written here):**
  - Choose and write down a scope for each later arm.
  - For legacy-homes, either move the list to a repo-owned path seeded by `adopt-policy.sh --scaffold`, or keep the arm in a gov-only leg.
  - For `arm_cap_census`, add a field such as `ships = false` to each caps.toml row whose enforcer is a registry `[[exempt]]`. The arm skips such a row, with an announce line, only when its enforcer is absent. It still reds an absent enforcer on any other row. A gov-side check asserts that the `ships = false` rows match the registry exemptions.
  - The mirror-parity arm is scoped by M21 (id 47).
- **Left-shift gate:** a close-time criterion and fixture that installs the policy kit into a bare `git init` target, runs `adopt-policy.sh --scaffold` then `--check` with every unit built, and expects exit 0.

### H3. Rule 2 denies the rendered `unattended-build.js` at the default limit (id 13)

- **Where:** spec-10 §4 "The hook after this unit"; §8 F3.
- **What is wrong:** unit 10 moves `boundedK`'s comparand to `MAX_VERIFIERS` (5), while F3 keeps `SPEC_WRITERS = {{FANOUT_CAP}}`, which renders the limit (default 6). The spec-writer split carries `// gov:fixed-verifiers` (unattended-build.template.js:942, :955), so rule 2 judges K=6 > 5.
- **Consequence:** AC13 (all four renders exit 0 under `--only=scripts`) is red as designed. Live, the hook refuses every `unattended-build` Workflow call, which is the harness that runs builds.
- **Fix (judged SOUND):** pick one of three options:
  - (a) Have rule 2 judge only verifier receivers against `MAX_VERIFIERS`, and give `SPEC_WRITERS` its own marker or bound.
  - (b) Render `Math.min(limit, MAX_VERIFIERS)`. F3 rejects this today.
  - (c) Drop the marker from the spec-writer split and bound it another way.
- **Left-shift gate:** a `limit-` case that renders `unattended-build.template.js` at limit 6 and pipes it through `node tools/hooks/agent-cap.js --only=scripts`, expecting exit 0.

### H4. An agent branch that edits the catalogue or policy file has no path to a green bar (id 32)

- **Where:** spec-6 §4 "The verdict" (the mirror has no exception), read with spec-5 §5 risks.
- **What is wrong:** a catalogue or policy edit stales the mirror on the branch. The bar's regen preflight exits 2 and prescribes `--regen` followed by committing what moved. Unit 6's guard refuses an agent's commit of `.governance/policy.json` "even when it equals the render". With `GATE_REGEN_CHECK=0`, `arm_mirror_parity` still reds.
- **Consequence:** every later build that adds catalogue rows (dKeptSession's presets, each Owner build) is stuck without the owner's terminal. Spec 5 §5 names only "the parity arm reds".
- **Fix (judged SOUND):** state one rule in both specs:
  - (a) The guard admits a staged mirror whose bytes equal `policy.py mirror` rendered at the staged tree.
  - (b) The mirror's `[[generated]]` row is graded only on the landing range, through a regen.py `landing-only` flag.
  - (c) The mirror is not tracked on branches.
- **Left-shift gate:** a fixture case in which an agent commits a catalogue row on a branch, and the bar preflight plus its stated remedy reaches green with no owner terminal.

### H5. The `policy fixtures` leg guard misses the sibling kits its cases run (id 35)

- **Where:** spec-1 §4 "The adopter" (guard `{prefix}/policy/`); spec-8, spec-9 and spec-10 §7 "New arm" lines.
- **What is wrong:** each unit's cases reach outside the guard:
  - Unit 10's `limit-hook-*` cases run `tools/hooks/agent-cap.js`.
  - Unit 9's `budgets-cap-<name>` cases run nine enforcers across memory-tree, roles, playbook, kickoff and memory-recall.
  - Unit 8 imports `tree_lib`.
  - Every policy module inlines tools/lib blocks.

  No unit widens the leg's guard. This is the recorded class held-suite-guard-misses-a-sibling-kit.
- **Consequence:** an edit to any of those sibling files alone skips the leg or reuses its stale green, so the interaction case never runs.
- **Fix (judged SOUND):** units 8, 9 and 10 each add the exact sibling files their cases read to the `policy fixtures` guard in tools/gate-legs.json, and list gate-legs.json in Files touched. Spec 1 adds `{prefix}/lib/`. Prefer exact files to directories, so BROAD_LEG_FLOOR is not tipped.
- **Left-shift gate:** on a scratch branch touching only `tools/hooks/agent-cap.js`, `check-spec-tokens.py --legs-for tools/hooks/agent-cap.js` names `policy fixtures`.

## Medium

### M1. Derived defaults resolve to an inline table (id 3)

- **Where:** spec-3 §2 S2, S4, against spec-1 §4 Data model, spec-2 S7 and spec-5 "Which keys".
- **What is wrong:** unit 1 allows `default = { derived = "..." }`, but unit 3 returns "the row's default" as the value.
- **Consequence:** `get charter.practices` resolves to a table that `get` cannot print, and the mirror publishes `{"derived": ...}` to JS consumers as a value.
- **Fix (SOUND):** unit 3 S2/S4 resolve a derived default to a `Refusal` naming the row ("a derived default no reader computes yet"). Unit 5 states whether such keys are omitted or carried as refusals.
- **Gate:** a `resolution-order` case that plants a derived default and expects exit 2.

### M2. Unit 7's shrink-only baseline names two different bases (ids 5, 15)

- **Where:** spec-7 §2 S4; §4 "The check and the write" item 3; §8 F4; Edges consumes-from TOOL-dGroundRules-2; AC6 Red-when.
- **What is wrong:** S4 compares against "the list at the landed revision", which is unit 2's tip. The same paragraph "calls" unit 1's comparison, `resolve_compare_base`, which is the merge-base when that is a proper ancestor. Unit 2 §10 says the two differ.
- **Consequence:** with the tip as the base, a branch opened before main dropped a key still derives that row. Item 3 reds it as "a new legacy home" and `lists --write` refuses until the branch merges main. This is the misread the merge-base rule exists to avoid. A builder also cannot tell which base to build.
- **Fix (SOUND):** use unit 1's `resolve_compare_base` as the one baseline, spelled once. Amend S4, item 3, F4, the consumes-from edge and AC6's Red-when to match.
- **Gate:** a fixture case where the landed tip drops a row the branch's conf or base still holds, expecting no "new legacy home" finding.

### M3. Unit 8 imports a sibling kit by path join, and unit 7 locates the house file the same way (ids 6, 16)

- **Where:** spec-8 §4 "Landed"; spec-7 :76 (the house-file locator).
- **What is wrong:** unit 8 imports `HDR_RE`, `TERMINAL`, `read_blobs_at` and `parse_conf` from tree_lib "beside the policy kit". It declares no `requires`, uses no `resolve_kit_dir`, and reads an `ImportError` as "no build landed". Units 1, 2 and 5 state that a kit may not import a sibling, and unit 2 rejects `read_blobs_at` for exactly that reason. Unit 7 locates `<tool root>/roles/house/policy.toml` by the same join.
- **Consequence:** two contradictory rules stand. Under an install prefix or receipt layout, the coverage arm grades 0 keys for good: announced, but checking nothing.
- **Fix (SOUND):** either inline the four names (about three lines, plus one `git show`) as the other units do, or follow `tools/memory-recall/extract.py:105-121`: an inlined `resolve_kit_dir`, `memory-tree` in `requires`, and a miss treated as a refusal. Apply the same fix to unit 7's house-file locator. Then make units 2, 5 and 8 state one rule.
- **Gate:** a policy-fixtures case with the kits at a non-default prefix, expecting the arm to grade the landed owners or refuse, never to grade 0.

### M4. AC8's reader scanner cannot match the call shapes units 4 and 9 will write (id 7)

- **Where:** spec-8 §6 AC8, against spec-9 §4 Data model and spec-4 S5.
- **What is wrong:** spec-8's pattern segment excludes quotes and `.`, while unit 9 quotes cap keys (`budgets."AGENTS.md"`) and names no call spelling. Unit 4 reads `policy-file.on-invalid` through `RESOLUTION_ORDER` path tuples, so the literal string need not appear.
- **Consequence:** correct builds of units 4 and 9 leave AC8 red. The builder must either contort the call spelling or accept a red "reader coverage" on the first push.
- **Fix (SOUND):** unit 9 S2 states the literal call (for example `policy.resolve("budgets." + ...)`), and unit 8 widens the pattern segment to admit a quoted segment holding `.`. Alternatively, unit 8 reads the `budgets.*` reader from `caps.toml`'s join. Unit 4 S5 states a string-literal call such as `resolve_read(parse_key("policy-file.on-invalid"), ...)`.
- **Gate:** a unit 8 fixture case `reader-quoted-pattern` using `resolve(f'budgets."{cap}"')`.

### M5. `budgets.<cap> = 0` gets two verdicts (id 8)

- **Where:** spec-9 §2 S4, against §4 Data model and spec-1 §4 allowed grammar.
- **What is wrong:** S4 refuses a value that is "not a positive integer". The Data model says "0 keeps meaning unchecked", and unit 1 types the key `min = 0`.
- **Consequence:** caps whose home holds 0 today (`INDEX_CAP_LINES`, `DOSSIER_CAP_LINES`) cannot be carried. `validate` refuses the file, and on-invalid falls back to the last valid revision.
- **Fix (SOUND):** make S4 "not a non-negative integer". Or, if 0 should be refused, drop the Data-model sentence and set unit 1's row to `min = 1`.
- **Gate:** a `budgets-` case that sets a cap to 0 and asserts the chosen verdict.

### M6. Retiring the `AGENT_CAP` refusal breaks the D7 arm and leaves a stale map card (ids 9, 34)

- **Where:** spec-10 §2 S4 Readers inventory; §4 Files touched.
- **What is wrong:** `tools/workflows/check-review-join.test.sh:207` plants `env AGENT_CAP=7` as its only way to make agent-cap refuse its environment. `memory/map/features/agent-cap.md:84` teaches that refusal as live. Neither file is in the inventory or Files touched.
- **Consequence:** `review-join self-test`, which is on §7's line, goes red with no sanctioned file to fix it. That invites the builder to weaken D7 into checking nothing. The map card teaches a removed rule.
- **Fix (SOUND):** add both files to S4's readers and to Files touched. Re-plant D7 with a refusal the hook still makes: a stub predicate exiting 2 before any rule, reached through the gate's resolver, as the next arm already does.
- **Gate:** a close-time criterion in which the main loop observes `bash tools/workflows/check-review-join.test.sh`, with the D7 arm red against a predicate that does not refuse.

### M7. Unit 2's AC7 `git remote` count cannot pass on a correct build (id 14)

- **Where:** spec-2 §6 AC7.
- **What is wrong:** neither the canonical `remote_ladder_py` block nor the copied `resolve_compare_base` contains the text `git remote`.
- **Consequence:** a correct build prints 0, so AC7 is red. A comment is the only way to reach 1, and then the grep certifies nothing.
- **Fix (SOUND):** drop the `git remote` count and keep `grep -c '^def resolve_remote'` = 1. For the "no other remote read" half, grep for `"remote"`, `remote get-url` and `remote -v` outside the `# >>> remote_ladder_py` … `# <<<` range, or rely on the stub-refusal probe.
- **Gate:** before freezing, run each grep-count criterion against the canonical block it names.

### M8. Bare `bash` in the shim invocation hits the System32 WSL launcher (id 17)

- **Where:** spec-5 §4 "The shim"; "The arms and the cases" (`mirror-landed-parity`).
- **What is wrong:** `check_policy.py` drives `bash <kit>/policy-shim.sh` by its bare name. On Windows, CreateProcess searches System32 before PATH. This is the recorded class subprocess-resolves-a-different-shell. The Node helper inherits PATH order.
- **Consequence:** on any node with WSL, the parity case runs under WSL and fails for reasons unrelated to the code. A non-Git-Bash hook process hits the same launcher, and rule 7 then refuses every spawn.
- **Fix (SOUND):** route every Python shim invocation through a `resolve_bash()` copy that refuses the WSL and WindowsApps launchers, as `tools/run-gates/profile_bar.py` does. State the Node helper's bash resolution (an absolute Git bash or an override variable) and what a non-2 exit means.
- **Gate:** a case that puts a fake WSL-like `bash` first on PATH.

### M9. `arm_limits_readers` already reds on a file outside unit 9's write set (ids 18, 36)

- **Where:** spec-9 §2 S7 (`arm_limits_readers`); §6 AC4; §4 Files touched.
- **What is wrong:** the predicate (any non-comment line naming `template-size-limits.txt`) matches `tools/memory-recall/extract.py:346`, a docstring. `check-spec-tokens.py:159` is a second docstring hit.
- **Consequence:** AC4's "green over this repository at the unit's commit" cannot hold. The builder must edit outside `--writes` or loosen the predicate ad hoc.
- **Fix (SOUND):** make the predicate a reading call (`open(`, `read_text`, `cat`, awk, `<`, or the `SIZE_LIMITS_NAME` constant), or exclude docstrings too, or add extract.py to Files touched and reword it.
- **Gate:** run the predicate over `git ls-files` before freezing AC4. Add a fixture in which a docstring mention stays green.

### M10. New parsed files have no eol pin, so AC8's byte compare is platform-dependent (ids 19, 27)

- **Where:** spec-1 §2 S1, §4 (Files touched lists `.gitattributes` but states no line), §6 AC8; also spec-7's `legacy-homes.txt`.
- **What is wrong:** under `* text=auto` and system `core.autocrlf=true`, `.governance/policy.toml`, `tools/policy/*.toml` and `*.txt` check out CRLF. AC8 byte-compares the working file with scaffold's stdout.
- **Consequence:** AC8 and the adopter's "writes the scaffold's bytes" pass or fail by platform and by stdout text mode. Otherwise the builder strips CR, and the check stops checking bytes.
- **Fix (SOUND):** name the lines in §4: `.governance/policy.toml`, `tools/policy/*.toml` and `tools/policy/*.txt` as `text eol=lf`, following the `tools/template-size-limits.txt` pin. Have `scaffold` write LF through `sys.stdout.buffer`. Phrase AC8 as a compare of the blob (`git show HEAD:...`) or of CR-stripped bytes.
- **Gate:** `git check-attr eol` probes for each new file, expecting `eol: lf`, as unit 5's AC12 does.

### M11. A second writer and a third resolver of `.claude/settings.json` (id 21)

- **Where:** spec-10 §2 S2; §4 Data model; §10.
- **What is wrong:** `policy.py settings --write` and its `[[generated]]` row write a file whose recorded single owner is settings-merge (tools/hooks/kit.toml:52-56). The path is hard-coded, skipping `GOV_SETTINGS_JSON`.
- **Consequence:** in an adopter that sets `GOV_SETTINGS_JSON`, the render and rule 7 grade a file that is not in force. This repeats the two-resolver defect recorded at TOOL-aDeferredBar-7.
- **Fix (SOUND):** extend `tools/settings-merge.py` with an env mode (a fragment kind carrying `env` keys, with `--check`), and have the policy kit's row call it. Otherwise add a §8 fork citing kit.toml:52-56 that settles ownership. Resolve the file as check-wiring.sh:94-117 does (`GOV_SETTINGS_JSON` first), in rule 7 too.
- **Gate:** a case with `GOV_SETTINGS_JSON` pointing elsewhere, asserting that the render writes and grades that file.

### M12. A fourth unchecked copy of the git location-variable leak list (id 24)

- **Where:** spec-2 §4 Behaviour, "Every git call".
- **What is wrong:** `policy.py` spells the list inline ("the list is spelled in this module"). No check compares it with the other copies. This is the open ask TOOL-dRetiredFork-23, which the spec does not cite.
- **Consequence:** a variable added elsewhere and not here lets the reader, started from a hook or a fixture, silently read another repository's policy file.
- **Fix (SOUND):** lift `GIT_ENV_LEAKS` into tools/lib as a canonical `# >>> git_env_leaks_py` block, held by the resolve-python.test.sh parity rows, and inline it. Or cite TOOL-dRetiredFork-23 and add policy.py to its proposed set-equality join.
- **Gate:** the parity row itself.

### M13. The pre-commit guard block swallows a missing delegate (id 25)

- **Where:** spec-6 §4 "The hook block".
- **What is wrong:** `if g=$(resolve_kit_gate policy guard.py); then ... fi` has no `else`, and it bypasses `print_kit_miss`, which every other kit leg calls. This is the recorded class swallowed-delegate-reads-as-clean.
- **Consequence:** with guard.py missing from the working tree, guarded-path changes commit silently. That contradicts F7's refuse-not-skip ruling.
- **Fix (SOUND):** when guarded paths are staged (decided from `git show HEAD:<kit>/guarded-paths.txt`, or from the four paths when the kit is absent), a miss calls `print_kit_miss "policy guard" policy guard.py` and sets `rc=1`.
- **Gate:** a pre-commit.test.sh arm that removes guard.py, stages `.governance/policy.toml`, and expects a refusal.

### M14. Retiring rules 1 and 3 breaks two playbook-parity rows (id 33; finder high, skeptic medium, binding medium)

- **Where:** spec-10 S4, S7; §4 Files touched; §7 Gates.
- **What is wrong:** tools/check-playbook-parity.sh:271-272 extract their numbers from hooks README lines 71 (`boundedParallel(thunks, 5)`) and 114 ("integer ≤5"), which S7 rewrites. Neither the file nor the leg is named.
- **Consequence:** an empty extraction prints PAIRFAIL, and the unguarded `playbook parity` leg reds. Keeping the bullets instead teaches retired rules, which AC14's grep cannot see.
- **Fix (SOUND):** add check-playbook-parity.sh to Files touched, and re-point or retire rows 271-272 to a surviving sentence (for example rule 2's verify bound against `MAX_VERIFIERS`). Add `playbook parity` and `playbook parity selftest` to §7.
- **Gate:** extend AC14 so that no hooks-README bullet still describes the raw-primitive ban or the ≤5 clamp as denied.

### M15. A hand-bumped `KIT_AGENT_CAP_VERSION` leaves two stale marker carriers (id 38)

- **Where:** spec-10 S4; §4 Files touched; §7.
- **What is wrong:** format-guard.js:7 and scratch-guard.js:144 carry `gov:kit agent-cap@1.40`, and check-kit-versions.sh fails every carrier that does not match the constant.
- **Consequence:** the `kit version markers` leg goes red. Editing scratch-guard.js also trips `format-guard self-test`, which §7 omits.
- **Fix (SOUND):** add both files (marker only) to Files touched and `format-guard self-test` to §7. Alternatively, drop the hand bump and let `govkit.py mint` move every carrier at the landing.
- **Gate:** a criterion that `git grep -l "gov:kit agent-cap@1.40" -- '*.js'` prints nothing.

### M16. The new `policy` registry entry carries no version marker (id 39)

- **Where:** spec-1 §4 Inventory (`KIT_POLICY_VERSION`), "The adopter", Files touched.
- **What is wrong:** the spec states no `version_from` and no `gov:kit policy@<v>` marker. Govkit selfcheck 5 and 5c then fail the entry.
- **Consequence:** `govkit selfcheck`, which is in §7, goes red, and the builder has to invent where the marker lives.
- **Fix (SOUND):** set kit.toml `version_from = { file = "policy.py", pattern = "^KIT_POLICY_VERSION = " }` and put `<!-- gov:kit policy@1.0 -->` in tools/policy/README.md, as the roles kit does. Optionally add a `need` row in check-kit-versions.sh.
- **Gate:** a criterion that `python tools/govkit/govkit.py selfcheck` prints no line naming entry 'policy'.

### M17. Seven specs omit the codebase-map freshness leg and the map files (id 40)

- **Where:** §7 and §4 Files touched of specs 2, 3, 4, 7, 8, 9 and 10.
- **What is wrong:** each of these specs adds or retires module-level functions, but none lists the unguarded `codebase-map coverage + freshness` leg or `memory/map/generated/*`. Spec 10 also omits `memory/map/features/agent-cap.md`. This is the recorded class hand-named-gate-list-green-while-the-bar-reds, which has recurred five times.
- **Consequence:** symbols.json goes stale and the bar reds on a leg the list never named. A builder confined to the dispatch write set cannot write the regenerated map.
- **Fix (SOUND):** add the leg to §7 and `memory/map/generated/symbols.json` and `inventories.json` to Files touched in each of the seven specs. Add the feature card for spec 10.
- **Gate:** derive each spec's §7 leg list from `check-spec-tokens.py --legs-for` over its Files touched, rather than typing it by hand.

### M18. Unit 1 omits the arms and install-prefix meta-legs (id 41)

- **Where:** spec-1 §7 Gates; §4 "The adopter" and Files touched.
- **What is wrong:** under `ARMS_REFUSALS="graded"`, the `exit 1` in `adopt-policy.sh --check` must be armed by a sibling `adopt-policy.test.sh` or pinned, and the spec ships neither. §4 places the fixture copy "under `tools/policy/`", a literal that the install-prefix ban flags.
- **Consequence:** `harness arms` and `install-prefix (shipped surface)` go red, but only at the close.
- **Fix (SOUND):** add `tools/policy/adopt-policy.test.sh` arming the refusal, or a pinned row in `memory/project/unarmed-branches.txt`, to Files touched. State that every kit path comes from the kit's own location. Add both legs to §7.
- **Gate:** the two legs themselves, named in §7.

### M19. Rule 7 refuses every spawn in a freshly adopted target (id 42)

- **Where:** spec-10 §2 S5 (rule 7); §4 Migration.
- **What is wrong:** rule 7 exits 2 when the settings env keys are absent. Nothing at install renders them, because the render runs only from a landing's `regen.py`.
- **Consequence:** an adopter that installs both hooks and policy cannot spawn any agent until it runs `policy.py settings --write` by hand. The deny message names the remedy, so this is contained.
- **Fix (SOUND):** have the policy kit's `[adopt]` (`adopt-policy.sh --scaffold`) and its update `[[regenerate]]` run `policy.py settings --write`. List adopt-policy.sh in Files touched and add a Migration line.
- **Gate:** a fixture in which a fresh target receives hooks and policy, and its first Agent payload exits 0.

### M20. Re-pointed size enforcers have no rule for a refusing reader or a missing launcher (id 44; finder high, skeptic medium, binding medium)

- **Where:** spec-9 §4 "The enforcers" (closing paragraph); §8 F4.
- **What is wrong:** only "policy kit absent" is named. `budgets.py` exits 2 in reachable states: two remotes and no `GOV_REMOTE`, an unfetched landed ref, or an invalid file with no valid revision. `check-template-size.sh` also gains a Python dependency it lacks today.
- **Consequence:** each of the ten enforcers either reds unrelated commits or reads the refusal as a pass, chosen per enforcer, so the size gates can disagree.
- **Fix (SOUND):** one rule for every switch enforcer. On exit 2, or when no launcher resolves, the enforcer refuses over its cap as today, prints the reader's refusal once, and never reads the outcome as `warn`.
- **Gate:** a `budgets-reader-refused` case (two remotes, no `GOV_REMOTE`, a subject over its cap) that refuses and names the ladder text, plus a no-launcher case for `check-template-size.sh`.

### M21. The mirror-parity arm reds an absent mirror in an adopter (id 47)

- **Where:** spec-5 §4 "The arms and the cases" (`arm_mirror_parity`); §2 S4; also spec-4's `arm_on_invalid` over HEAD.
- **What is wrong:** the arm reds a mirror that is absent "where the policy kit is present", in the repo-subject leg. Nothing in an adopter writes the mirror. In a fresh `git init` target, HEAD does not resolve either.
- **Consequence:** every adopter reds on `mirror-absent` at its first bar, and unit 1's AC9 stops exiting 0.
- **Fix (finder's proposal REJECTED; the skeptic's corrected fix is written here):** `arm_mirror_parity` grades an absent mirror only when HEAD carries `.governance/policy.toml` or a mirror. Otherwise, including when HEAD does not resolve, it prints one announce line and reports no finding. State the same for unit 4's `arm_on_invalid` when HEAD does not resolve. Rendering the mirror at `--scaffold` is not the fix: `mirror --write` refuses an uncommitted policy file.
- **Gate:** re-run unit 1's AC9 fresh-target `--check` after these arms join, expecting exit 0 (shared with H2).

### M22. The hook helper maps only shim exit 2 and spawns a bare `bash` (id 48)

- **Where:** spec-5 §2 S5; §4 "The reader for hooks", steps 2 and 6.
- **What is wrong:** shim exit 1 or 127, a null `spawnSync` status, a signal, ENOENT and other git failures are all unspecified. The bare `bash` is unresolved (System32 and WindowsApps stubs).
- **Consequence:** in agent-cap.js, which has no top-level catch, a non-`PolicyRefusal` throw or an empty-stdout value fails open as a non-blocking exit 1, or returns an undefined limit.
- **Fix (SOUND):** any outcome other than exit 0 or a documented missing path becomes a `PolicyRefusal` carrying the status and stderr. State how bash is located (the toolchain's Git Bash, never a bare PATH lookup).
- **Gate:** a fixture that points the helper at a shim exiting 1, expecting `PolicyRefusal`.

### M23. Mirror freshness ignores the `.agent-cap.conf` input (id 49)

- **Where:** spec-5 §2 S1/S5; §4 Data model (freshness by two blob ids).
- **What is wrong:** freshness compares only `policy_blob` and `catalogue_blob`, while unit 10's resolution also reads `.agent-cap.conf`.
- **Consequence:** a landing that skips regen.py (the escape §5 names) and changes only the conf leaves the mirror FRESH with the old, higher limit. Rule 7 then admits a raised `env`. The parity arm reds afterwards.
- **Fix (SOUND):** add `legacy_blobs: {".agent-cap.conf": <id or null>}`, compare every entry in step 4, and state the rule that a unit adding a resolution input adds its blob.
- **Gate:** a case `mirror-stale-legacy`: L changes only `.agent-cap.conf` and keeps the old mirror, and the helper must read STALE.

### M24. `arm_mirror_readers` bans every mention of the path, including comments and tests (id 50)

- **Where:** spec-5 §4 arms table (`arm_mirror_readers`); §2 S9.
- **What is wrong:** the arm reds any file "naming `policy.json`", with no comment or test exclusion. This is the recorded class absence-assertion-over-whole-file-text. Unit 10's agent-cap.test.sh and its rule-7 header, and unit 6's pre-commit.test.sh, will name the path.
- **Consequence:** the live arm reds on test data and comments, and the builder then weakens it ad hoc.
- **Fix (SOUND):** skip lines starting `#` or `//` and skip `*.test.sh`, `*.test.js`, `selftest*.py` and `test_*.py`, as unit 8 does. Better still, match a read shape (`readFileSync`, `open(`, `cat` or `git show` followed by `policy.json`). Keep `mirror-direct-reader` red.
- **Gate:** a green case in which a `.js` file has a comment naming `.governance/policy.json`.

### M25. "A population of zero is a finding" contradicts legal empty populations (id 51)

- **Where:** spec-1 §4 "The CLIs" (check_policy.py), against §5 error/empty states and spec-8 AC7.
- **What is wrong:** the blanket rule reds three legal states: `arm_schema` with no policy file, `arm_schema` over an empty policy file, and unit 8's `reader-coverage` before any Owner lands. Unit 8's AC7 requires that last state to pass.
- **Consequence:** either every push reds until a chain build lands, or each builder special-cases its own arm.
- **Fix (SOUND):** make the rule per arm: each `ARMS` entry declares whether an empty population is a finding or an announced pass.
- **Gate:** one case per kind of arm.

### M26. The last-valid walk misreads shallow history (id 52)

- **Where:** spec-4 §2 S4 (`read_last_valid`); §4 "The branch", step 3.
- **What is wrong:** `git rev-list --first-parent` stops at a shallow graft and returns `None`.
- **Consequence:** in a shallow clone (an adopter's CI at depth 1), a malformed file is refused with the false reason "no valid revision precedes", where a full clone falls back. The verdict then depends on clone depth.
- **Fix (SOUND):** when `git rev-parse --is-shallow-repository` is true and the walk hits the boundary, refuse with "history is shallow at <sha8>; fetch more history".
- **Gate:** a case `on-invalid-shallow`: V then C cloned at `--depth 1`, expecting the shallow wording.

### M27. A non-UTF-8 policy file crashes the reader (id 53)

- **Where:** spec-2 §2 S2, S3; spec-4 §2 S1.
- **What is wrong:** `UnicodeDecodeError` is not a `TOMLDecodeError`, so a UTF-16LE file (what a PowerShell 5 `>` writes) escapes all five failure classes.
- **Consequence:** `get`, `check` and unit 4's history walk die with a traceback (exit 1) instead of reading `last-valid` or refusing with a line.
- **Fix (SOUND):** in S2, catch `UnicodeDecodeError` and hand it on as malformed text (a `Problem` with `why="not UTF-8: ..."`) that unit 4's branch treats like a decode error.
- **Gate:** an `on-invalid-classes` case with V valid and C written as UTF-16LE, expecting the V value with source `last-valid`.

### M28. Rule 7 fails open on throws its spec does not name (id 45; finder high, skeptic medium, binding medium)

- **Where:** spec-10 §2 S5 (rule 7); §5 error/empty states.
- **What is wrong:** a malformed `settings.json` or `settings.local.json`, a non-`PolicyRefusal` throw, or a `cwd` outside a checkout all throw. agent-cap.js has no top-level catch (:420-421), and exit 1 from a PreToolUse hook does not block.
- **Consequence:** the spawn is admitted in the very window rule 7 exists to close. The harness still applies the settings env, so the limit itself is not lost.
- **Fix (SOUND):** run rule 7 inside a try/catch that denies with exit 2 on any throw, naming the file or step. A present but unparsable settings file refuses, and a `cwd` with no checkout refuses.
- **Gate:** cases `limit-hook-settings-malformed` and `limit-hook-reader-throws`, each expecting exit 2, with the pre-fix shape observed exiting 1 first.

## Low

### L1. Unit 2 hands unit 9 a blob reader it never defines (id 10)

- **Where:** spec-2 §3 Edges (hands-off to TOOL-dGroundRules-9).
- **What is wrong:** unit 2 defines only `read_policy_text`, so unit 9 consumes an interface that does not exist.
- **Fix (SOUND):** add `read_blob_at(repo, rev, path)` to S2 and the Inventory, with `read_policy_text` calling it. Or reword both Edges lines so unit 9 owns its own reader.
- **Gate:** an edges join that greps the producer's Inventory for each handed-off name.

### L2. AC1 and AC12 spell the policy files by bare names that point at the repository root (id 11)

- **Where:** spec-5 §6 AC1, AC12.
- **What is wrong:** `git rev-parse HEAD:policy.toml` and `git check-attr eol -- policy.json` name root paths, so as written they error or print `unspecified`.
- **Fix (finder's proposal REJECTED; the skeptic's corrected fix is written here):** keep the bare names in the criteria, and extend the criteria preamble to say that `policy.toml` and `policy.json` denote the files under `.governance/` and that their git commands run with that prefix. Have S10 require the `.gitattributes` line to name `.governance/policy.json` exactly, so `git check-attr eol -- .governance/policy.json` prints `eol: lf`. Spelling the full paths inside a criterion would trip the spec-token checker before the build creates the files.
- **Gate:** the preamble's bare-name list, graded by the spec-token checker.

### L3. Unit 1's Evidence bullet is off by one line and miscounts copies (id 20)

- **Where:** spec-1 §4 Evidence, fifth bullet.
- **What is wrong:** `## [presets]` is at v2:1409, not 1408. The bullet names three copies of `read_policy_key` and omits `tools/unattended/unattended.sh:9517`.
- **Fix (SOUND):** cite v2:1409 and say four copies, as unit 2 does.

### L4. Units 5 and 9 each spec their own single-reader scanner (id 26)

- **Where:** spec-9 §2 S7 (`arm_limits_readers`); spec-5 §4 arms table (`arm_mirror_readers`).
- **What is wrong:** the two scanners share one predicate but differ in suffix set and exclusions, so they will drift.
- **Fix (SOUND):** unit 5 specs one `arm_single_reader(repo, path, reader_dir)` with its suffixes and exclusions stated once, and unit 9 registers `template-size-limits.txt` as a second row of it.

### L5. The copied `resolve_compare_base` has no parity check (id 29)

- **Where:** spec-1 §4 Inventory paragraph; §10.
- **What is wrong:** the function is copied "rule for rule" from map_lib.py:1502, outside any gated block.
- **Consequence:** later map-kit fixes do not reach the copy, and nothing goes red.
- **Fix (SOUND):** lift it into tools/lib as a canonical `# >>> compare_base_py` block, inlined in map_lib.py and policy.py. Or record the ungated copy as a deviation with its compensating check.

### L6. The agent-cap.test.sh arm line reads as a permanent historical-sha oracle (id 43)

- **Where:** spec-10 §7, second "New arm" line.
- **What is wrong:** "`git show 3708a705:tools/hooks/agent-cap.js` in the suite's scratch copy" reads as a suite mechanism. This is the recorded class test-oracle-read-from-a-historical-sha.
- **Fix (SOUND):** reword the line so the base-revision run is the main loop's one-off staged observation at the close, and state that the suite carries no `git show <sha>:` read.

### L7. An unprobed restart claim and a non-atomic settings write (id 54; finder medium, skeptic low, binding low)

- **Where:** spec-10 §5 risks; §2 S2/S3.
- **What is wrong:** "A session started before a lowering keeps its harness settings until it restarts" is stated as fact. The recorded gotcha settings-edit-takes-effect-mid-session found a claim like it false. `.claude/settings.json`, which holds the hooks block, is rewritten with a plain dump.
- **Fix (SOUND):** turn the claim into a FACT-QUESTION with the gotcha's two-halves probe, and record the answer in §5 and in the help page. Write the file through a temp file plus `os.replace` in the same directory.

### L8. Guard fixtures use only one-segment cap keys (id 56)

- **Where:** spec-6 §4 "The cases".
- **What is wrong:** the keys `"big.md"`, `"small.md"` and `"docs/*/"` never exercise the shipped shapes, which carry slashes and a leading dot.
- **Consequence:** the leaf-tuple diff, `git cat-file -e HEAD:<segment>` and RAISED matching are proved only on trivial names.
- **Fix (SOUND):** raise a key such as `".claude/skills/x/SKILL.md"` in `guard-admits-raise` and `guard-lowered`, and plant `"memory/builds/*/spec/"` in `guard-class-row`.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=56 confirmed=49 refuted=7 unverified=0 blocker=2 high=6 medium=33 low=8 agents=11 out-tokens=298288

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-5.md:section 4 Data model (the mirror) and The render; section 6 AC1, AC2; section 8 F2 | blocker | blocker | confirmed | I checked this against the spec text and push-main.sh. spec-5:114 shows a mirror key's reason as `set in .governance/policy.toml at 3708a705, ...`. S1 (spec-5:27-29) stores the whole `Resolution` of every key. spec-2:138-140 and spec-3:108-110 define every file and default reason as naming `<sha8>` of the revision read. No part of spec-5 strips or rewrites the reason before the render; a grep for reason/sha8 in spec-5 shows only the helper's fallback prefix. F2 (spec-5:395-401) rejects a commit id for the top-level field because a commit cannot carry its own id, yet the per-key reasons still carry one. In push-main.sh:880-925, run_regen runs after `git merge`, and then `git commit-tree ... -p $R -p $oldb` creates a new commit. So the landed mirror names a sha that is not its own commit, and `mirror --check` at the new HEAD differs. AC2 cannot hold on a correct build. | sound | - |
| 2 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:section 2 S1 (against TOOL-dGroundRules-5 §4 The render and TOOL-dGroundRules-3 §3) | high | high | confirmed | Three specs place the one lowering in three different places. spec-10:36-37 puts it in `resolve("runtime.agents-in-flight")`. spec-5:140-145 splits resolve into a revision read plus `resolve_read`, and the mirror renders through `resolve_read`. spec-3 Non-goals (lines ~53-54) says a legacy home adds a step to `RESOLUTION_ORDER`. spec-10 never mentions resolve_read, RESOLUTION_ORDER or the mirror render; a grep printed only rule 7's readPolicy use. A lowering built in the `resolve` wrapper therefore never reaches the mirror. Rule 7 (spec-10:78-87) reads the limit through readPolicy, so it would admit settings above the lowered value. `arm_mirror_landed` would not catch this: it compares only keys the policy file at L sets (spec-5 arm table), and the limit is unset in the conf-only case. The mirror's freshness pins only the policy and catalogue blobs (spec-5:43). | sound | - |
| 3 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-3.md:section 2 S2, S4 (against TOOL-dGroundRules-1 §4 Data model, TOOL-dGroundRules-2 S7, TOOL-dGroundRules-5 Which keys) | medium | medium | confirmed | spec-1:115 allows `default = { derived = "..." }`, and spec-1:191 has scaffold skip non-literal defaults. Nothing else handles that shape. spec-3 S2 (line 30) returns `the row's default` as the value, and S4 refuses only a row with no default. A grep for `derived` across specs 2, 3 and 5 shows no handling of a derived default. spec-5's Which keys mirrors every non-pattern catalogue name. So such a key would resolve to, and be mirrored as, an inline table. | sound | - |
| 4 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:section 4 The adopter and section 6 AC9 (against TOOL-dGroundRules-5 S4, TOOL-dGroundRules-7 §4 The arm, TOOL-dGroundRules-9 S7) | high | high | confirmed | spec-1:228-234 ships `policy check` as an adopter `[[gate_leg]]` with subject repo, and `--check` runs check_policy.py over the target. Three later arms only hold on gov's own tree: - spec-5's `arm_mirror_parity` reds a mirror that is absent where the policy kit is present. Scaffold writes only policy.toml. - spec-7:150 runs `legacy-homes` on the real tree via unit 1's leg, against `tools/policy/legacy-homes.txt`. That file ships with the kit and holds gov's 115 measured rows (spec-7:118-126). An adopter's derivation would yield typed or stale rows. - spec-9 S7 adds `arm_cap_census` to the same ARMS, joining the census both ways. The census names gov enforcers such as roles/check_roles.py and skills/session-kickoff/manifest-check.sh (spec-9:144-170). None of these specs scopes its arm away from adopters. | sound | - |
| 5 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-7.md:section 2 S4 and section 4 The check and the write, item 3 | medium | medium | confirmed | spec-7 gives two bases for the same comparison. S4 (line 32) and item 3 compare against the list at the landed revision, read through unit 2's landed-revision resolution (spec-7:144-145). The same paragraph then says it calls unit 1's comparison, and spec-1:101-103 defines that as resolve_compare_base: the merge-base when it is a proper ancestor, else the tip. spec-2:296-300 states explicitly that these two differ. AC6's Red-when also only says 'landed revision'. | sound | - |
| 6 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-8.md:section 4 Landed | medium | medium | confirmed | spec-8:67-72 imports HDR_RE, TERMINAL, read_blobs_at and parse_conf from the memory-tree kit's tree_lib, located 'beside the policy kit', and treats an ImportError as no build landed. That contradicts spec-1:98 ('A kit may not import a sibling kit') and spec-2:183-184, which rejects importing read_blobs_at for that reason. `git grep 'from tree_lib import'` outside memory-tree and memory/builds prints only tools/memory-recall/extract.py:119. That file uses resolve_kit_dir and a declared `requires`, and treats a miss as a refusal. spec-8 has no `requires` mention. | sound | two-answers-to-one-question |
| 7 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-8.md:section 6 AC8 (against TOOL-dGroundRules-9 §4 Data model and TOOL-dGroundRules-4 S5) | medium | medium | confirmed | spec-8:105-110 matches a pattern segment as a run of characters that are not a quote, `.`, space or parentheses. spec-9:130-131 says cap keys holding `/` or `.` are quoted, as in `"AGENTS.md"`. spec-9 S2 (lines 44-50) says values are read 'through policy.resolve' but gives no call spelling. A call such as `"budgets." + cap` or `f'budgets."{cap}"'` therefore need not match. For on-invalid, spec-8:101-103 expects a literal `policy-file.on-invalid` read in policy.py. spec-4:47-48 reads it 'by RESOLUTION_ORDER', whose steps take a path tuple (spec-3:101), so the literal string need not appear. | sound | - |
| 8 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-9.md:section 2 S4 against section 4 Data model, and TOOL-dGroundRules-1 §4 allowed grammar | medium | medium | confirmed | The spec gives two verdicts for the value 0. spec-9:64-65 refuses a `budgets.<cap>` that is not a positive integer. spec-9:133-134 says 'A value of 0 keeps meaning unchecked', and spec-1:143 types `budgets.*` as `{ type = "count", min = 0 }`. `grep -nE '^(INDEX_CAP\|DOSSIER_CAP)' .memory-tree.conf` printed INDEX_CAP_LINES="0" and DOSSIER_CAP_LINES="0", matching spec-9's census 'today' values of 0. | sound | - |
| 9 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:section 2 S4 Readers inventory and section 4 Files touched | medium | medium | confirmed | `git grep -l -e '--print-cap' -e AGENT_CAP -e FANOUT_CAP` (excluding memory/builds) lists tools/workflows/check-review-join.test.sh and memory/map/features/agent-cap.md. A grep of spec-10 for either path printed nothing. tools/workflows/check-review-join.test.sh:207 is the D7 arm, `env AGENT_CAP=7 bash "$GATE"`, which depends on the environment refusal that S4 retires. memory/map/features/agent-cap.md:84 reads '**The cap is a FILE CONSTANT and a set `AGENT_CAP` is refused, not ignored.**' `review-join self-test` is on spec-10:336's leg line. | sound | - |
| 10 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-2.md:section 3 Edges, hands-off TOOL-dGroundRules-9 | low | low | confirmed | spec-2:94 hands unit 9 'its blob reader ... for the limits home', and spec-9:105 consumes it. However, spec-2 S2 (lines 32-34) defines only `read_policy_text(repo, rev)`, which reads .governance/policy.toml. The Inventory (spec-2:165-167) lists no general path-at-revision reader. The hand-off names an interface that does not exist. The builder will resolve this at build time, and it does not affect shipped behaviour. | sound | - |
| 11 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-5.md:section 6 AC1 and AC12 | low | low | confirmed | spec-5 AC1 spells `git rev-parse HEAD:policy.toml` and AC12 spells `git check-attr eol -- policy.json`. Read literally, both point at a root path. `git check-attr eol -- policy.json .governance/policy.json` printed 'eol: unspecified' for both. The criteria preamble excuses bare names only for policy.py, policy-mirror.js, policy-shim.sh and check_policy.py. The intent is clear from context, so the effect is on how the commands read as written. The proposed fix is unsound: the preamble says the spec-token checker grades a path-shaped token in a criterion against the tracked set. `git ls-files .governance` shows only deploy.toml. So spelling `.governance/policy.toml` or `.governance/policy.json` inside a criterion, the fix's first two options, would trip that checker before the build creates the files. | unsound | - |
| 12 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-5.md:section 4 Data model — the mirror, and The render | blocker | - | refuted | duplicate of id=1. It makes the same claim: the per-key reason carries the rendered commit's sha8, per spec-5:114 and spec-2:138-140. Once the mirror is committed, or rewritten by commit-tree in push-main.sh:880-925, `mirror --check` goes red. id=1 is confirmed in this answer. | sound | - |
| 13 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:section 4 The hook after this unit, and section 8 F3 | high | high | confirmed | Re-probed. tools/workflows/unattended-build.template.js:942 has `const SPEC_WRITERS = {{FANOUT_CAP}}` and :955 has `chunk(slices, Math.ceil(slices.length / SPEC_WRITERS)) // gov:fixed-verifiers`. In agent-cap.js:551-555, boundedK returns `consts.get(t) <= EFFECTIVE_CAP`. :931 emits the 'bounded split names a cap which this file does not show to be bounded' refusal when a marked chunk branch fails on its K. Unit 10 §4 (:176) moves the boundedK comparand to MAX_VERIFIERS (=5, agent-cap.js:492). S6 and F3 (a) keep SPEC_WRITERS on the token, which renders the limit, and the catalogue default is 6 (unit 3 :170, unit 4 :255). So at the default limit the rendered unattended-build.js carries K=6 > 5. Rule 2 refuses it, AC13 is red as designed, and live the hook denies the build harness. The spec never reconciles SPEC_WRITERS with the MAX_VERIFIERS comparand. | sound | - |
| 14 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-2.md:section 6 AC7 | medium | medium | confirmed | Unit 2 AC7 (:243-246) requires `grep -c 'git remote'` over policy.py to print 1. `grep -c 'git remote' tools/lib/resolve_remote.py` printed 0. The block calls read("remote") through a git argv, and the map_lib resolve_compare_base unit 1 copies holds no `git remote` text either (only `refs/remotes/{remote}`). A correct build prints 0, and only a comment could make it print 1, so the grep certifies nothing. | sound | - |
| 15 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-7.md:section 2 S4, section 4 The check and the write, section 8 F4 | medium | medium | confirmed | Unit 7 S4 (:32-33) uses 'the list at the landed revision'. The consumes-from edge (:59-61) is unit 2's rev=None landed tip, and §4 (:144-146) also says it 'calls that one comparison' of unit 1. Unit 1 (:101-103, :180-183) bases the comparison on resolve_compare_base, a merge-base where it is a proper ancestor. Unit 2 §10 (:290-296) says itself that its landed tip is not compare_base. The map_lib docstring states the merge-base exists so a key main deleted after the branch opened is not misread as one the branch added. With the tip as baseline, a branch still carrying a key main dropped re-derives a row the tip list lacks, and item 3 reds it as a new legacy home. The spec also states two bases. | sound | - |
| 16 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-8.md:section 4 Landed | medium | medium | confirmed | Unit 8 :67-72 imports HDR_RE, TERMINAL, read_blobs_at and parse_conf from tree_lib 'in the memory-tree kit beside the policy kit', and reads an ImportError as no build landed. The tree's seam for a sibling kit is resolve_kit_dir: map_extractors.py:43-44 says 'never by joining that kit's name to the tool root', and extract.py:113-121 shows the pattern. Unit 2 §10 (:296-299) and unit 5 (:449) both reject read_blobs_at because a kit may not import a sibling, which is a contradiction inside one spec set. Unit 7 :76 locates the house file as `<tool root>/roles/house/policy.toml`, the same join. In a relocated install, the arm reads 0 landed owners and certifies nothing. | sound | - |
| 17 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-5.md:section 4 The shim, and The arms and the cases (`mirror-landed-parity`) | medium | medium | confirmed | Unit 5 §4 (:190, :198, :210-218) invokes the shim as bare `bash <kit>/policy-shim.sh`. check_policy.py drives the shim's `landed` for mirror-landed-parity (:239, AC9). The spec names no resolve_bash. `where bash` on this node printed Git's bash, C:\Windows\System32\bash.exe and the WindowsApps alias. A Python subprocess resolving the bare name 'bash' goes through CreateProcess, which searches System32 before PATH, and memory/gotchas/subprocess-resolves-a-different-shell.md records exactly this class and its fix. The tree has many resolve_bash copies (profile_bar.py:282, govkit.py:1144, corpus_ids.py:390) that the spec does not use. The Node half depends on PATH order and is less certain, but the Python half alone establishes the defect. | sound | - |
| 18 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-9.md:section 2 S7 (`arm_limits_readers`) and section 6 AC4 | medium | medium | confirmed | Running the finder's git grep (non-test, non-comment lines) printed tools/memory-recall/extract.py:346 (a docstring), tools/check-spec-tokens.py:159 (a docstring), check-spec-tokens.py:266 and check-template-size.sh:63. S7 (:82-85) only excludes comment lines, and AC4 (:270-274) requires green over this repository at the unit's commit. Files touched (:212-219) lists check-spec-tokens.py but not tools/memory-recall/extract.py, so as written the live arm reds on a file outside the unit's write set. | sound | rule-stated-with-no-check-that-fails |
| 19 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:section 4 (no eol pin stated) and section 6 AC8 | medium | medium | confirmed | Unit 1 lists .gitattributes in Files touched (:257), but `grep gitattributes` finds no §4 statement of what it pins. `git config --show-origin` printed system core.autocrlf=true. `git check-attr eol text` printed eol unspecified and text auto for .governance/policy.toml, tools/policy/catalogue.toml and tools/policy/legacy-homes.txt. .gitattributes pins only .governance/deploy.toml (:100) and tools/*/kit.toml (:210) to LF. AC8 (:327-330) compares the working file's bytes to scaffold's stdout, so its outcome depends on checkout eol and on stdout text mode. | sound | - |
| 20 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:section 4 Evidence, fifth bullet | low | low | confirmed | The v2 file memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md hashes to the pinned 9bf3b4c9. In it, grep printed `1125:## [policies]` and `1409:## [presets]`, while unit 1 :104 cites v2:1408. `git grep 'read_policy_key()'` printed four copies including tools/unattended/unattended.sh:9517, and unit 1 :95-96 names only three. Cosmetic only. | sound | - |
| 21 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:section 2 S2, section 4 Data model, section 10 | medium | medium | confirmed | Unit 10 S2 (:43-44) defaults the file to `.claude/settings.json` under the repo root, and the S3 [[generated]] row invokes it with no path. Its §4 and §10 never mention GOV_SETTINGS_JSON (grep finds no hit). check-wiring.sh:94-117 and govkit.py:6132/6187 resolve GOV_SETTINGS_JSON first, so in an adopter declaring it, the render and --check grade a different file from the wiring readers. tools/hooks/kit.toml:52-56 records settings-merge as the file's owner. §10 (:403-406) acknowledges settings-merge as 'the one writer' and then adds a second writer anyway, without a §8 fork settling ownership. | sound | - |
| 22 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-7.md:section 2 S4, section 4 "The check and the write", section 3 Edges consumes-from TOOL-dGroundRules-2 | medium | - | refuted | duplicate of id=15: the same defect, unit 7's shrink-only baseline at unit 2's landed tip instead of unit 1's resolve_compare_base merge-base, with the same misread of a main-deleted key and the same two-bases contradiction at unit 7 :32, :59-61 and :144-146. | sound | - |
| 23 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-8.md:section 4 "Landed", section 10 | medium | - | refuted | duplicate of id=16: the same defect, unit 8 :67-72 importing tree_lib from a sibling kit 'beside the policy kit' without resolve_kit_dir, an ImportError reading as zero landed builds, and the contradiction with units 2 and 5's rejection of read_blobs_at. | sound | - |
| 24 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-2.md:section 4 Behaviour, "Every git call" | medium | medium | confirmed | Unit 2 §4 :143-146 spells the git location-variable strip list inline in policy.py ('The list is spelled in this module'). grep finds no citation of TOOL-dRetiredFork-23 in the spec. memory/builds/dRetiredFork/BACKLOG.md:9 records that ask, open (no CLOSED marker): the copies (pre-push:100, pre-commit:8, tree_lib GIT_ENV_LEAKS and others) have no check that they agree, and divergence silently reads another repository. The spec adds another unchecked copy into the reader every gate trusts. | sound | - |
| 25 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-6.md:section 4 "The hook block" | medium | medium | confirmed | spec-6 lines 161-173: the block is `if g=$(resolve_kit_gate policy guard.py); then ... fi` with no else, and line 178 says that when the kit resolves nowhere 'the block prints nothing'. In .githooks/pre-commit, the memory-tree, kickoff-manifest, unattended and template-size legs each call `print_kit_miss` in their else branch (lines 42-74 of the 140+ excerpt). resolve_kit_gate reads only the working tree, the receipt and GOV_KITROOT. So if guard.py is missing from the working tree, a staged guarded path commits silently, which contradicts the block's own F7 refuse-not-skip reasoning. | sound | swallowed-delegate-reads-as-clean |
| 26 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-9.md:section 2 S7 (`arm_limits_readers`), and TOOL-dGroundRules-5 section 4 arms table (`arm_mirror_readers`) | low | low | confirmed | spec-5:226 defines `arm_mirror_readers` with an explicit suffix set (js/mjs/cjs/py/sh and .githooks/*) and excludes tools/policy/, the memory root and help/. spec-9:83-85 defines `arm_limits_readers` as 'each tracked script outside tools/policy/ and outside a self-test' on a non-comment line. It states no suffix set, excludes self-tests that spec-5 does not, and does not exclude memory/ or help/. That gives two independently specified scanners of one predicate whose populations already differ, and neither spec's §10 names the other. The drift cost is a maintenance cost with no behavioural fault today, so low. | sound | - |
| 27 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:section 2 S1, section 6 AC8, section 4 Files touched (`.gitattributes`) | medium | medium | confirmed | Re-probed: `git check-attr eol text` gives `eol: unspecified` and `text: auto` for .governance/policy.toml and tools/policy/legacy-homes.txt, and `git config core.autocrlf` prints `true`. .gitattributes pins tools/template-size-limits.txt and similar parsed data files, but has no rule covering .governance/policy.toml or tools/policy/*.txt. spec-1 lists `.gitattributes` only in Files touched (line 257) and never states the line. AC8 byte-compares the checkout against `policy.py scaffold`. spec-5 handles the same exposure for its mirror (S-line 59, AC12); spec-1 and spec-7 do not. | sound | gate-green-by-accident-on-generated-bytes |
| 28 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-8.md:section 4 "Landed", section 10 | low | - | refuted | The premise is false on re-probe. spec-8 §4 'Landed' (lines 66-70) and §10 (lines 246-248) already reuse tree_lib's `TERMINAL` (tools/memory-tree/tree_lib.py:31, ('CLOSED','WONTDO')), `HDR_RE` and `read_blobs_at`, so the status vocabulary is shared rather than re-derived. derive_status (gen_build_index.py:793-812) is a different contract. It needs README front matter and raises Problem when there are no parsed specs and no 'status:' key. Its fall-through also returns CLOSED for any token not in PRECEDENCE, so an unknown token would read as landed. That makes it a looser predicate, not the same rule. Spec-8's 'every spec in TERMINAL' is the stricter and correct reading, and nothing here can drift between two spellings of the token set. | unsound | - |
| 29 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:section 4 Inventory paragraph after the table; section 10 | low | low | confirmed | spec-1:101-103 and :174-175 say policy.py copies `resolve_compare_base` 'rule for rule' from tools/codebase-map/map_lib.py:1502. `git grep -n 'def resolve_compare_base'` finds only map_lib.py:1502, and that function sits outside the `# >>> remote_ladder_py` block, which ends just above it. No criterion or parity row in spec-1 holds the copy to its source, so later refinements to the map kit (its docstring cites TOOL-dLadderedRemote-2 and TOOL-aStandingWrit-5) would not reach the policy copy, and nothing would go red. The effect is a maintenance drift risk with no wrong result at build time, so low. | sound | - |
| 30 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-6.md:section 4 "The verdict" step 4 (RAISED match), section 10 | low | - | refuted | The premise does not reproduce. drift_report.py's `_justified` is applied only to RATCHETS rows. drift_signals.py:447-467 lists .memory-tree.conf, drift_signals.py itself and .codebase-map.conf, and no row names .governance/policy.toml or tools/template-size-limits.txt, nor does any dGroundRules spec add one (grep for RATCHETS/drift_signals across the specs found nothing). The two readers never judge the same raise, so 'one raise justified to one gate and unjustified to the other' cannot happen. spec-6 §10's claim 'No existing seam judges a staged diff's shape' also holds, because `_justified` scans text lines in a lookback window and does not inspect a staged change. The guard's narrower RAISED-adjacent rule is a deliberate tightening, not a defect. | unsound | - |
| 31 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-5.md:section 4 'Data model — the mirror' and 'The landing row'; S1, S2, S3; AC2 | blocker | blocker | confirmed | Verified. spec-2 §4 has every reason name the revision's sha8 ('set in .governance/policy.toml at 3708a705, <remote>/main, the landed revision'), and spec-3's reason table spells `at <sha8>` in every row. spec-5's mirror stores `reason` per key (line 114, example 'at 3708a705'). render_mirror 'resolves rev to a sha' and `mirror --write/--check` render at HEAD (lines 140, 153-161). spec-5:130-131 itself concedes that 'a commit cannot carry its own id', yet it did not apply that to the reason field. A committed mirror therefore re-renders with a different sha8 at the commit that carries it. On the landing, push-main.sh:906-921 runs run_regen and then folds into a new commit via commit-tree. run-gates.sh:1449-1458 runs `regen.py --check` before the first leg and exits 2 on staleness. As specified, mirror --check, arm_mirror_parity and the bar's regen preflight are red after every landing. | sound | - |
| 32 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-6.md:section 4 'The verdict' (the mirror has no exception) read with TOOL-dGroundRules-5 section 5 risks | high | high | confirmed | spec-5 §4 keys the mirror on `catalogue_blob` and `policy_blob`, so a branch commit to tools/policy/catalogue.toml (which units after 5 and later builds make) stales it. run-gates.sh:1449-1458 then exits 2 before any leg and prescribes `--regen` followed by committing what moved. spec-6:144-147 refuses an agent's commit of .governance/policy.json 'even when it equals the render'. With GATE_REGEN_CHECK=0 the bar still reds, because `arm_mirror_parity` in the `policy check` leg fails, which spec-5:310-313 acknowledges ('reds the parity arm'). Neither spec names the preflight refusal, the guard's refusal of the remedy, or any path to a green branch bar for an agent. | sound | - |
| 33 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:S4, S7, section 4 Files touched, section 7 Gates | high | medium | confirmed | Re-probed. tools/hooks/README.md:71 is the rule-1 raw-primitive bullet carrying `boundedParallel(thunks, 5)`, and :114 is 'Any `K` it cannot resolve to an integer ≤5'. tools/check-playbook-parity.sh:271-272 extract their numbers from exactly those phrases and compare them to MAX_VERIFIERS, and an empty extraction yields PAIRFAIL. spec-10 S4 retires rule 1 and the clamp, and S7/AC14 rewrite those README sentences, but `grep check-playbook-parity\\|playbook parity` on spec-10 finds nothing in S4 readers, Files touched or §7. The playbook parity leg would red the bar at build, which contains the damage, so medium rather than high. | sound | - |
| 34 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:S4 Readers list, section 4 Files touched | high | medium | confirmed | tools/workflows/check-review-join.test.sh:207 plants `env AGENT_CAP=7 bash "$GATE"` and expects 'is its own refusal and not a join'. Lines 201-206 say that arm relies on agent-cap exiting 2 on that environment refusal. spec-10 S4 retires 'the refusal of a set AGENT_CAP (:2241-2257)', yet its readers list and Files touched never name check-review-join.test.sh (the grep finds only `review-join self-test` in §7 at line 336). The arm will go red and the spec gives the builder no sanctioned file to fix, which invites weakening D7. Because the leg is in §7, the bar catches it, so medium. | sound | - |
| 35 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:section 4 'The adopter' (policy fixtures leg guard `{prefix}/policy/`); consumers in specs 8, 9 and 10 section 7 New arm lines | high | high | confirmed | spec-1:233 declares `policy fixtures` as subject kit with guard `{prefix}/policy/`, following the `runlog selftest` row (guard ['{prefix}/runlog/'] in gate-legs.json). spec-9 AC5/AC6 have the budgets-cap-<name> cases run the enforcers in the table at :182-193 (check-template-size.sh, memory-tree, roles, playbook, kickoff manifest-check, memory-recall). spec-10:168/338 has the limit-hook-* cases run tools/hooks/agent-cap.js, and spec-8:68-70 imports tree_lib from memory-tree. None of specs 8, 9 or 10 edits the leg's guard. Spec-9's one gate-legs mention, at :37, is not a guard edit. This is the class in memory/gotchas/held-suite-guard-misses-a-sibling-kit.md: an edit to a sibling alone skips the leg or reuses its stale green. | sound | inline-fence-swallows-the-rest-of-the-file |
| 36 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-9.md:S7 (`arm_limits_readers`), AC4, section 4 Files touched | medium | medium | confirmed | Re-ran a git grep over *.py/*.sh/*.js/.githooks, excluding memory/, help/, test suites, selftests and tools/policy/, and dropping `#` lines. It printed tools/check-spec-tokens.py:159 and :266, tools/check-template-size.sh:63, and tools/memory-recall/extract.py:346, a docstring line ("left ``<prefix>/template-size-limits.txt`` ..."). spec-9's Files touched names memory-recall/query.py but not extract.py (grep for extract.py found nothing). Under S7's 'line that is not a comment' predicate, that docstring counts as a reader, so AC4's 'over this repository ... green' fails at the unit's commit. | sound | - |
| 37 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-7.md:S2, S5 (arm in the `policy check` leg) read with TOOL-dGroundRules-1 section 4 'The adopter' and TOOL-dGroundRules-9 S7 (`arm_cap_census`) | high | high | confirmed | Confirmed on re-read. spec-1:232-233 ships `policy check` as a `[[gate_leg]]` with subject `repo`. spec-7 S2 puts the generated list in the kit dir (`tools/policy/legacy-homes.txt`), says the arm runs 'on the real tree by unit 1's leg', and derives the list from the tree under test (root `.*.conf`, `.githooks/gate-env.sh`, roles house file). The only adopter case §4 handles is an absent home. So in an adopter, the gov rows in the shipped list are 'typed rows' and every adopter key is 'stale', and the bar goes red. spec-9 S7 and AC7 have `arm_cap_census` require every census row to have an enforcer naming it. `sed -n 205-215,274-290p tools/govkit/registry.toml` printed `[[exempt]]` rows for `{prefix}/check-template-size.sh`, `check-spec-tokens.py` and `template-size-limits.txt` ('An adopter's instantiated playbook carries no size ceiling'), so those enforcers never reach an adopter. Neither spec states what the arm does there, and every AC observes only gov's tree. Graded high, not blocker: the failure is a loud false red in adopters, not a silent pass. | unsound | - |
| 38 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:S4 (`KIT_AGENT_CAP_VERSION` moves to '2.0'), section 4 Files touched, section 7 | medium | medium | confirmed | `git grep -n "gov:kit agent-cap@" -- '*.js' ':!memory/builds'` printed agent-cap.js:104, format-guard.js:7 and scratch-guard.js:144, all at `@1.40`. tools/check-kit-versions.sh greps every tracked `*.js` carrier with `git grep -lE "gov:kit agent-cap@"` and fails each one whose marker is not `$ac`. spec-10 S4 moves `KIT_AGENT_CAP_VERSION` to '2.0' by hand. Its Files touched omits format-guard.js and scratch-guard.js, and its §7 lists `kit version markers`, so that leg reds. The gate-legs `format-guard self-test` guard includes `{prefix}/hooks/scratch-guard.js`, and spec-10 §7 does not name that leg (it names `scratch-guard self-test` only). | sound | - |
| 39 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:section 4 Inventory (`KIT_POLICY_VERSION`), 'The adopter', Files touched | medium | medium | confirmed | The only mention in spec-1 is line 163, `KIT_POLICY_VERSION \| version constant, 1.0 \| tools/policy/policy.py`. It has no `version_from` and no `gov:kit policy@` marker. Selfcheck 5 (govkit.py:2119-2124) fails an entry that declares no version_from, so the builder must declare it. Then 5c (govkit.py:2250-2291) fails when `seen == 0` ('declares a version constant and carries NO gov:kit marker'). Built as written, `govkit selfcheck`, which is in spec-1's §7, goes red. The roles kit carries its marker at tools/roles/README.md:1 (`<!-- gov:kit roles@1.8 -->`), which matches the proposed fix, and tools/policy/README.md is already in Files touched. | sound | - |
| 40 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:section 7 Gates and section 4 Files touched; likewise specs 2, 3, 4, 7, 8 and 9 section 7 | medium | medium | confirmed | A grep over each spec printed codebase-map-gate/map-files counts of 1:1/5, 2:0/0, 3:0/0, 4:0/0, 5:1/2, 6:1/2, 7:0/0, 8:0/0, 9:0/0, 10:0/0, 11:1/1. Specs 2, 3, 4, 7, 8, 9 and 10 add or retire module-level functions (spec-7 `derive_legacy_homes`, spec-9 the `budgets.py` module, spec-10 the retired agent-cap.js functions and `checkSettingsInForce`). None of them names the `codebase-map coverage + freshness` leg, which has no guard in tools/gate-legs.json, or memory/map/generated/*. `git grep -ln AGENT_CAP -- memory/map` printed memory/map/features/agent-cap.md. The gotcha file records this same recurrence five times. | sound | hand-named-gate-list-green-while-the-bar-reds |
| 41 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:section 7 Gates; section 4 'The adopter' and Files touched | medium | medium | confirmed | `.memory-tree.conf:639` holds `ARMS_REFUSALS="graded"`. check-arms.py documents that every tracked non-test `*.sh` with an `exit 1` site (a delegated `\|\| exit 1` included) is a gate under the sibling-test rule. spec-1 AC9 has `adopt-policy.sh --check` exit 1. Its Files touched names no `adopt-policy.test.sh` and no unarmed-branches pin, while six `tools/*/adopt-*.test.sh` siblings exist. spec-1:199 places the fixture copy 'under `tools/policy/`'. check-install-prefix.sh rules 2 and 3 flag a literal kit segment followed by a file. spec-1 §7 lists neither `harness arms (fail branches armed or pinned)` nor `install-prefix (shipped surface)`. | sound | - |
| 42 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:S5 (rule 7), section 4 Migration | medium | medium | confirmed | spec-10 S5 refuses with exit 2 when either env key is absent, and adds the rule whenever policy-mirror.js sits beside the hooks kit. S3 renders settings only through a `[[generated]]` row run by `regen.py` at a landing. spec-1's adopter `--scaffold` writes only `.governance/policy.toml`. spec-10 Migration covers only hooks-before-policy, and its Rollout admits the refusal lasts 'until `policy.py settings --write` is run there'. So an adopter that installs both kits is refused every Agent and Workflow spawn until a manual step. The finder's claim that the operator cannot diagnose is overstated: the deny message names the remedy command, and it runs without spawning an agent. Effect is contained, so medium. | sound | - |
| 43 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:section 7, second New arm line (tools/hooks/agent-cap.test.sh) | low | low | confirmed | spec-10:339's New arm line for agent-cap.test.sh reads 'staged by running each arm against the base revision's hook, `git show 3708a705:tools/hooks/agent-cap.js` in the suite's scratch copy'. The phrase 'in the suite's scratch copy' reads as a suite mechanism rather than a one-off staged observation. memory/gotchas/test-oracle-read-from-a-historical-sha.md describes exactly this rot. The defect is wording that may mislead the build, so low. | sound | test-oracle-read-from-a-historical-sha |
| 44 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-9.md:section 4 The enforcers (closing paragraph) and section 8 F4 | high | medium | confirmed | spec-9 §4 The enforcers (around line 195) and F4 name only one degraded state, an absent policy kit. S2 has `budgets.py` exit 2 on a refusal through `policy.resolve`, and spec-2 AC5 shows the reader exits 2 with two remotes and no GOV_REMOTE. No sentence says how a switch enforcer treats exit 2, or a missing launcher. `grep -c 'python\\|resolve_python\\|PY' tools/check-template-size.sh` printed 0, so this enforcer gains a Python dependency it lacks today. Graded medium: under the default `warn` mode a fail-open admits nothing that would not already pass. The fail-open matters only under a pin or `refuse` on a narrow path. The other choice, a red on unrelated commits, is loud and contained. | sound | - |
| 45 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:section 2 S5 (rule 7) and section 5 error/empty states | high | medium | confirmed | tools/hooks/agent-cap.js:420-421 states '`main()` has no top-level catch and a PreToolUse hook that exits 1 is NON-BLOCKING'. grep found no `process.on` or uncaught-exception handler, and agent-cap.js:2427 is a bare `main()`. spec-10 S5 covers only an absent value, a non-positive value, an above-limit value and `PolicyRefusal`. It is silent on unparsable settings JSON, a non-PolicyRefusal throw and a cwd outside a checkout, so each of these fails open. Graded medium, not high: the harness itself still applies the settings env, so the limit is not lost. Only rule 7's cross-check is skipped. | sound | - |
| 46 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-7.md:section 2 S2, section 4 The arm | high | - | refuted | duplicate of id=37. That finding, confirmed above, covers the same defect: the gov-derived `tools/policy/legacy-homes.txt` shipped into the repo-subject `policy check` leg, which reds every adopter on install (spec-7:27-28, :150-151, :85-86; spec-1:232-233). The fix proposed here, a repo-owned `.governance/legacy-homes.txt` seeded by `--scaffold`, would itself be sound. | sound | - |
| 47 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-5.md:section 4 The arms and the cases (arm_mirror_parity) and section 2 S4 | medium | medium | confirmed | spec-5:224 has `arm_mirror_parity` red on a mirror 'absent where the policy kit is present', in the repo-subject leg. spec-5 Files touched (lines 273-282) omits adopt-policy.sh, and spec-1's `--scaffold` writes only `.governance/policy.toml`. So an adopter's first bar reds on `mirror-absent`, and spec-1 AC9's fresh `git init` `--check` probe stops exiting 0. In a fresh target with no commit, `render_mirror(repo, "HEAD")` cannot resolve either. The fix's first option is unsound: spec-5:153-156 makes `mirror --write` exit 2 when the working-tree policy file differs from its blob at HEAD. A just-scaffolded, uncommitted policy file is exactly that state, so rendering the mirror at `--scaffold` refuses. | unsound | - |
| 48 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-5.md:section 2 S5 and section 4 The reader for hooks, steps 2 and 6 | medium | medium | confirmed | spec-5:190-191 and the paragraph after step 6 map only shim exit 2 to `PolicyRefusal`. Shim exit 1 or 127, a null spawnSync status, a signal, ENOENT and a git failure other than a missing path are all unspecified. Step 2 spawns a bare `bash`. The existing hooks spawn only `git` (format-guard.js:247, scratch-guard.js:710), so no precedent resolves bash. The finder's `where bash` evidence lists the System32 and WindowsApps stubs. Through spec-10 rule 7 and agent-cap.js's missing top-level catch, a non-PolicyRefusal throw is a non-blocking exit 1. Effect is contained for the reason given under id=45. | sound | - |
| 49 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-5.md:section 2 S1/S5 and section 4 Data model (freshness by two blob ids) | medium | medium | confirmed | spec-5 §4 Data model holds only policy_blob and catalogue_blob, and steps 3-5 compare those two alone to call the mirror FRESH. spec-10 S1 (lines 32-37) has resolve('runtime.agents-in-flight') take the minimum with .agent-cap.conf read at the same revision. Rule 7 reads the limit through readPolicy (spec-10:79, :136). spec-5 §5 (:299-301) itself names a landing that skips regen.py as what escapes. So if a landing changes only .agent-cap.conf and skips regen, the helper reads the mirror as FRESH and returns the old, higher limit. The path is narrow, the effect is contained, and the parity arm reds afterwards. | sound | - |
| 50 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-5.md:section 4 The arms and the cases (arm_mirror_readers row) and section 2 S9 | medium | medium | confirmed | spec-5:226 defines arm_mirror_readers as 'a file naming `policy.json`' over tracked .js/.py/.sh and .githooks/*, excluding only tools/policy/, the memory root and help/. Unlike unit 8's scan (spec-8:96-99), it has no comment or *.test.* exclusion. Unit 10's agent-cap.test.sh exercises rule 7, which reads L:.governance/policy.json (spec-10:298-300, :339), and unit 6's pre-commit.test.sh sits under .githooks/. Both are in scope and likely name the path. The arm would red on test data and comments, and the builder would then have to weaken it ad hoc. | sound | absence-assertion-over-whole-file-text |
| 51 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:section 4 The CLIs (check_policy.py, 'A population of zero is a finding') against section 5 error/empty states | medium | medium | confirmed | spec-1:195 says 'A population of zero is a finding' for every arm check_policy.py runs. The same spec says (:282, :289) that an absent policy file grades nothing in arm_schema and is legal. spec-8 S3 adds reader-coverage as an arm in check_policy.py, and its AC7 (:192-196) requires graded 0 to pass with an announce line and no finding. As written, the two rules contradict each other, both within unit 1 and between unit 1 and unit 8. | sound | - |
| 52 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-4.md:section 2 S4 (read_last_valid) and section 4 The branch, step 3 | medium | medium | confirmed | spec-4 S4 (:40-43) walks `git rev-list --first-parent <sha> -- .governance/policy.toml` and returns None, and the refusal text says 'no valid revision of the file precedes <sha>'. Grepping every spec for shallow or depth finds nothing. Gov's own CI uses fetch-depth: 0, but the kit ships to adopters, and in a shallow clone the walk stops at the graft. A full clone falls back to last-valid where a shallow one refuses with a false reason. The path is narrow and the effect is contained. | sound | - |
| 53 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-2.md:section 2 S2 and S3 (decode as UTF-8, TOMLDecodeError to the caller), with unit 4 section 2 S1 | medium | medium | confirmed | spec-2 S2 (:32-33) decodes the blob as UTF-8, and S3 (:37-38) routes only tomllib.TOMLDecodeError as not TOML. Unit 4 S1 (:29) treats only TOML decode failure as a problem. I probed `b'\xff\xfe[b]'.decode('utf-8')`: it raised UnicodeDecodeError, and issubclass of TOMLDecodeError printed False. No spec mentions a UnicodeDecodeError path, so a UTF-16 policy file crashes the reader with a traceback instead of reaching on-invalid handling. | sound | - |
| 54 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:section 5 risks and section 2 S2/S3 (the render writes .claude/settings.json) | medium | low | confirmed | spec-10:240 states 'A session started before a lowering keeps its harness settings until it restarts' as fact, with no probe and no UNVERIFIED tag. memory/gotchas/settings-edit-takes-effect-mid-session.md records that settings edits are re-read mid-session for hooks, and that a restart-only claim like this one was false before (TOOL-aOrientedCast-22). S2 specifies a plain json.dumps write of .claude/settings.json, which holds the hooks block, with no atomic replace. Enforcement still holds through rule 7, which reads the landed limit at call time, so the effect is mainly a possibly wrong statement in the risk line and help page, plus a narrow torn-read window. Graded low. | sound | settings-edit-takes-effect-mid-session |
| 55 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-8.md:section 4 Landed | medium | - | refuted | The cited section already says it. spec-8 §4 Landed (:66-67) requires that 'at least one spec parses and every one carries a token in TERMINAL'. A file whose header fails HDR_RE carries no token, so it blocks landing. The same section names the rule as the schedule instrument's 'build done', and I read tree_state in memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py: an unparsed spec is counted as 'NONE' and blocks build done. Re-probing found the five headerless spec files, all in a* builds (aDeployScout, aKitHardener, aLeanRework, aPortableWarden, aRatchetForge). None of them is a catalogue owner, so today's tree is not affected. | sound | - |
| 56 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-6.md:section 4 The cases (fixture policy file) | low | low | confirmed | spec-6 §4 The cases (:206-210) builds its fixture with '"big.md" = 100', '"small.md" = 50' and '"docs/*/" = 10'. guard-admits-raise and guard-lowered raise big.md, so no admitted or lowered case uses a key with slashes or a leading dot, the shapes the shipped rows have (for example .claude/skills/unattended/SKILL.md). The leaf-tuple diff, `git cat-file -e HEAD:<segment>` and RAISED matching are therefore proved only on a one-segment name. This is a coverage gap: the spec as written is correct, and the risk is only that a builder's bug goes uncaught. | sound | staged-break-substitutes-a-synthetic-value |
