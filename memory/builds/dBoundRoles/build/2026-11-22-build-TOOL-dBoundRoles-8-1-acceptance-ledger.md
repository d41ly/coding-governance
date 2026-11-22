**Serves:** journal TOOL-dBoundRoles-8

# TOOL-dBoundRoles-8 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `6151b39f5`: `node -e` calls of the exported `checkRoleGate` and
`resolveRoleRoot` with `CLAUDE_PROJECT_DIR` unset, the outside `cwd` a directory under the session scratchpad in no
checkout, a scratch adopter beside it holding a `.git` folder and a `.claude/roles.json` reading `{`, and the hook
itself piped JSON payloads. The same AC1 and AC2 payloads returned null from the hook at base. No gate, suite or bar
ran in the pass: the `New arm:` arm section 7 declares, its RED-first observation, and the legs section 7 lists are
owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-8
- AC1 — `G2 runner` — `checkRoleGate('bash <outside>/tools/run-gates.sh', { agent_type: 'gov-builder', cwd: <outside> }, {})` returned a deny naming `row G2 runner` and `No checkout root was found`; the same call at base returned null. Piped to `tools/hooks/scratch-guard.js`, the payload exited 2. The step is `tools/hooks/scratch-guard.js#checkRoleGate`'s step 3. OWED: the `tools/hooks/scratch-guard.test.sh` rows `BR8-AC1`, RED first against step 3 returning null with no root, and the `scratch-guard self-test` leg at the close.
- AC2 — `G3 suite` — the AC1 call over `bash <outside>/tools/x.test.sh` returned a deny naming `row G3 suite`; with `--help` appended it returned no deny, the witness `role-gate rows G1 leg and P1 to P3 unarmed`, and the hook exited 0 printing that line alone. OWED: the `BR8-AC2` rows, RED first at the close.
- AC3 — `.claude/roles.json` — the AC1 call over `bash <adopter>/tools/run-gates.sh`, the adopter's index reading `{`, returned a deny naming `<adopter>/.claude/roles.json is not JSON`, so the script's checkout was read through `tools/hooks/scratch-guard.js#resolveRoleRoot`'s third start; a call over this worktree's own runner by absolute path from the outside `cwd` was refused naming this worktree's index and its allowlist, and its allowlisted lexicon leg was admitted with no line. Agent-cap's rule 6: an `Agent` payload with the outside `cwd`, piped to a copy of `tools/hooks/agent-cap.js` and a copy of the base file, each beside its own `scratch-guard.js` in the scratchpad, exited 0 with byte-identical stderr, and with `CLAUDE_PROJECT_DIR` set to the outside directory both exited 0 printing the same `rule 6 unarmed` line. OWED: the `BR8-AC3` rows, RED first against no third start, and the `agent-cap self-test` leg at the close.
- AC4 — `grep -E` — `checkRoleGate` with `gov-builder` and a `cwd` inside this worktree returned null for `f=tools/roles/adopt-roles.test.sh && sed -n 1,5p "$f"`, for `grep -E 'serve.sh|run-gates.sh|await.sh' tools/x.md` and for `sed -n 5p tools/hooks/agent-cap.test.sh`. OWED: the `BR8-AC4` rows at the close, whose red is an arm refusing a read that only names a gate script.
- AC5 — `checkRoleGate` — `grep -n 'checkRoleGate' README.md` in `tools/hooks/` printed the section's lines stating the three root starts and the line naming the replay through the exported `checkRoleGate` and `scanCommandHeads` as the census instrument; `grep -c 'neither resolving adds no arm'` over `README.md` and `scratch-guard.js` there found the phrase in neither (DERIVED, at this pass). OWED: nothing beyond the legs section 7 lists at the close.
