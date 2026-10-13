# Brief — aSweptBar: the full bar with self-tests goes green over local main

**Serves:** research TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6

## The prompt

> Run a full bar over the repo, including self-tests, and fix all discovered reds gracefully.

## The brief

### Goal
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` over local main `53b25884` reported
30 of 138 legs red, every one inherited from six landings that merged without a bar. Each red this
build owns is fixed at its root cause, one mechanism per unit, so the same bar reads green apart from
the roles reds aOrientedCast owns. Evidence for every item is the leg log under
`.git/worktrees/bar-53b2/gate-logs/` and the standalone re-runs named below.

### Items
1. **TOOL-aSweptBar-1 — stale suite fixtures, re-armed.** Test-only edits, each restoring an arm a
   landing disarmed:
   - `tools/memory-tree/transition-audit.test.sh:503` spells `sed -n's/…'`, the flag fused to the
     script, so sed prints usage and AC11's `after` is empty (TOOL-aSparedSpawn-8). A space.
   - `tools/workflows/unattended-build.test.sh:1036-1039` derives the no-run-state verbs from
     `fail 4N "no run-state file`, a spelling TOOL-aSparedSpawn-14 folded into `check_run_state`; F2
     derives 0. Derive from `check_run_state` calls inside each `verb_*` body (13 verbs today), and
     confirm the absence arms below still hold over that set.
   - `tools/hooks/agent-cap.test.sh` no-regress `property` mode (nr.js `buildPayload`): rule 6
     (TOOL-aOrientedCast-7) refuses every inline Workflow script once the payload cwd resolves a
     `.claude/roles.json`, so the marked fixture is denied by rule 6 and nothing is ratified. Give the
     payload a `cwd` in the scratch fixture dir, which no checkout holds, so the property compares
     rules 0 to 5 with BASE `d65da7ab`, which predates rule 6.
   - `skills/session-kickoff/manifest-check.test.sh:921` expects `node — a · daily-agent`; the v4.0
     registry's Machine/user cell is `daily-agent @ COMPEETO-AGENT`, which the card prints.
   - `tools/unattended/unattended.test.sh:550-556` roots the harness tallies and the namespace
     snapshot in `$TMP`, which IS the fixture repository's work tree, so the first `run` of an arm
     dirties the tree and `--preflight` refuses check 2 (`harness-proc.tally`); shard 8's first arm
     then reads "no run-state file". Root them under `$TMP/.git/`.
   - `tools/run-gates/run-gates.runlog.test.sh` AC4: the writer's one `cat` is deliberate
     (TOOL-aPairedSlots-7, measured torn lines without it, `run-gates.sh` `write_runlog_verdict`); the
     arm must sanction exactly that one exec rather than none. AC8 EXITS: three exits inside the
     `REUSE_DIGEST=$( … )` substitution (`git version … || exit 1`, the `mapfile … || exit 1`,
     `[ -n "$vp" ] || exit 1`) exit a subshell that runs no trap of the runner's; give each an exempt
     row in the table, as the wall watcher's rows are.
   - `tools/runlog/selftest.py:331` — the newest floor move, 1578 -> 1580 by TOOL-aHeardState-8,
     states no arithmetic, so record AC2 reads None. Two checks were added (`prose AC4: a UTF-16
     charter exits 0…` and `…its pair line reads unknown`): `1 + 1 = 2`.
   - `tools/memory-tree/check-memory-hygiene.test.sh` `_pyexempt` lacks `GIT_INDEX_FILE`, an
     environment read `gen_build_index.py:903` added (TOOL-aTrimmedHook-4); add it and its comment line.
   - `tools/govkit/selftest.py:6383` pins `ORDER|project-owned` at 32; a default plan now measures
     34. Measure which two withheld rows arrived and from which landing, and write the move into the
     comment ledger above the pin as its predecessors are written.
2. **TOOL-aSweptBar-2 — the foreign-prefix probe contract.** `tools/run-gates/foreign-prefix.gov.test.sh`
   reds four suites that print no probe marker: `held-halves selftest`, `roles render selftest` and
   `routed-commits selftest` are `--selftest` modes of shipped engines and join `WHOLE_RUN` with the
   reason those rows carry; `tools/hooks/format-guard.test.sh` takes the two-line one-arm stop
   `scratch-guard.test.sh:179-180` carries, after the last AC1 check and before `# AC2` (its owner,
   aHeardState, asked for that placement).
3. **TOOL-aSweptBar-3 — the run-gates evidence and pre-push suites' standalone reds.** Both suites
   were re-run alone on node a at `53b25884` and stay red (logs in the session's temp `barlogs/`):
   - `tools/run-gates/run-gates.evidence.test.sh` S2's broken copy matches 4 of 6 variants: the
     newline strip is now `while [[ $out == *$'\n' ]]; do out=${out%$'\n'}; done` on one line, and the
     redaction guard is `*://*@*|*$'\r\n'*)`, whose CRLF alternative still redacts, so AC2 to AC4 cannot
     go red; re-anchor each sed and break both alternatives. Also red alone: AC5 "a repeat under the
     edited runner reused nothing", AC6 "the opt-in run did not reuse pa", AC4 and AC5 controls
     "GATE_REUSE=1 did not reuse pa": root-cause them. Line 2248's location probe is asked bare: apply
     the remedy the shell-hygiene leg prints.
   - `.githooks/pre-push.test.sh`: 25b "<no decision line>", RP AC12 "expected no knob", VR AC15 (two
     arms), VR F8 and PM AC3 red alone; root-cause each. The other ten pre-push reds the bar showed
     passed alone, so they are contention and out of scope.
4. **TOOL-aSweptBar-4 — shipped-surface bans.** Each a gate's own remedy:
   - install-prefix: kit-path literals in `tools/hooks/scratch-guard.test.sh` (44, TOOL-aOrientedCast-11's
     G rules) and `tools/hooks/agent-cap.test.sh` (7, ~2355-2502) assemble the kit segment from a
     variable, the form the gate's header names for a fixture; `tools/run-gates/README.md:699,703`
     take the drained `<prefix>/` token.
   - remote literals: `tools/run-gates/run-held-wsl.sh:166` reads `git remote get-url origin`;
     resolve the remote through the inlined, marked `resolve_remote_sh` copy.
   - encoding posture: `tools/run-gates/held_halves.py:326` `subprocess.run` takes `encoding="utf-8"`.
   - python resolver: `tools/govkit/selftest.py:2779` resolves `{prefix}` by hand; route it through
     `resolve_prefix_token`. `tools/hooks/format-guard.test.sh:62` captures its resolver heredoc with
     `cat`; read it the no-fork way the gate names.
   - memory-hygiene `--render`: `tools/memory-tree/SPEC-TEMPLATE.template.md:384` names
     `REVIEW-PROTOCOL.md`, a gov path in an adopter's docs (TOOL-aDistilledCharter-9); spell it
     `{{REVIEW_PROTOCOL}}`, which `adopt-memory-tree.sh:303,310` already renders, and re-render gov's
     `memory/TEMPLATE-SPEC.md`.
   - playbook parity check 16: `tools/memory-tree/README.md:526` cites "charter §9"; cite the
     `[security]` handle.
   - check-wiring BP2 AC12: `KIT_FILE_PAIRS` in `tools/check-wiring.sh:574` lacks the
     `roles workflows.toml` pair its own call site passes.
   - shell hygiene, loop fed by a substitution: `tools/run-gates/run-gates.sh:3060`
     (`done <<<"$_sel_out"`, TOOL-aSparedSpawn-12) and one new `EOF` loop in
     `tools/workflows/check-protocol-parity.test.sh`; convert each so the registry counts hold.
5. **TOOL-aSweptBar-5 — fork idioms re-grown past the registry.** The `shell hygiene (a fork spent
   on builtin work)` leg lists 24 findings; outside `tools/roles/` they are in `.githooks/pre-push.test.sh`,
   `skills/session-kickoff/manifest-check.sh` and its test, `tools/check-wiring.test.sh`,
   `tools/hooks/format-guard.test.sh`, `tools/hooks/scratch-guard.test.sh`,
   `tools/memory-tree/check-memory-hygiene.sh` (a count that fell: lower its row),
   `tools/run-gates/run-gates.sh` (`cat-file` 23 -> 38), `run-gates.runlog.test.sh`,
   `run-gates.test.sh`, `run-gates.turnstile.test.sh` and `tools/workflows/unattended-build.test.sh`.
   Convert product-source sites to the no-fork forms; a suite site is converted, or declared in
   `memory/project/spawn-idiom-sites.txt` with its reason where the registry's grammar admits it.
6. **TOOL-aSweptBar-6 — records, pins and ceilings re-measured last.**
   - memory hygiene check 21: seven `memory/builds/aSparedSpawn/build/` records carry no `**Serves:**`
     line (`-6-fork-probe.sh`, `-13-direct-checks.out`, `-13-direct-checks.sh`, `-3-direct-checks.sh`,
     `-32-fixtures.sh`, `-33-fixtures.sh`, `-4-direct-checks.sh`); add `# **Serves:** journal <its unit>`.
   - python resolver: bare `python` in seven build records (aBriskPreflight-7, aPairedSlots-1,
     aSparedSpawn-2, -10, -11, -12, -15) and a hand `{prefix}` in `-12-select-sim.py:40,50`.
   - spawn budget: `memory/project/fork-ceilings.txt` rows memory-hygiene, manifest-check and
     check-wiring are stale above their measured counts; lower each to what the counter measures over
     the tree units 1 to 5 leave.
   - lexicon: verb offenders 1087 over pin 1063, the 24 new ones in aSparedSpawn's build-folder
     instruments, and an undeclared `out` extension from its `*.out` records. Declare `out` dark and
     re-measure the pin with a dated row (aScoutedSeam reconciles onto it).
   - harness arms: `tools/unattended/unattended.sh` holds 319 refusal sites against a ceiling of 318;
     aBriskPreflight-11 added the two wiring-timeout refusals, which grade different bounds and are
     armed apart. Raise `REFUSAL_CEILINGS` to 319 with a dated decision id, by the README's rule.
   - method carriers check 3: eight rendered `.claude/agents/gov-*.md` mention `BUILD-METHOD.md` and
     no row in `memory/project/method-carriers.txt` declares them.

### Acceptance
Each unit's own red leg reads green when its argv runs alone at the unit's tip; a re-armed arm is
observed red on its staged break before it is called armed. At the close, the full bar with
`GATE_FULL=1 GATE_SELFTESTS=1` reds only on legs whose cause is under `tools/roles/`.

### Gates
`transition-audit arms` · `unattended-build self-test` · `agent-cap self-test` · `manifest-check self-test` · `runlog selftest` · `run-gates run-log line` · `memory-hygiene self-test` · `govkit selftest` · `foreign-prefix parity (every self-test at three prefixes)` · `run-gates evidence` · `pre-push self-test` · `install-prefix (shipped surface)` · `remote literals (kit code names no remote)` · `encoding posture (text IO names its encoding)` · `python resolver (behaviour + inline parity + idiom ban)` · `playbook parity` · `check-wiring self-test` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `memory hygiene` · `spawn budget (forks per hot entrypoint)` · `lexicon naming predicates` · `lexicon wiring` · `harness arms (fail branches armed or pinned)` · `method carriers (every pointer declared)`

### Non-goals
- Nothing under `tools/roles/`, `.claude/agents/`, `.claude/skills/build/` or `tools/playbook/`:
  aOrientedCast owns the roles reds and lands them at its close.
- No pin, ceiling or registry row raised to absorb a red that a code change can fix; a raise is taken
  only where the leg's own rule names a raise as the remedy and the growth is a decided one.
- No merge to local main and no push without the owner's ask.

### Limitations
- Children run no bar and no whole suite; each verifies with the one check that exercises its change,
  and returns a suite verdict it needs to the main loop.
- `tools/unattended/check-unattended.sh` carries raw CR bytes; edit it in binary mode.
- Under MSYS, `/tmp` and `C:/…/Temp` name one directory; compare through git.

### Reuse
The remedies each leg prints; the marked canonical copies under `tools/lib/` (`resolve_remote_sh`,
`resolve_prefix_token`); `WHOLE_RUN`'s existing reason; scratch-guard.test.sh's probe stop; the
comment ledgers above each pin. No new mechanism is needed.

## Drawn from the session

> The fix is already being built by another session branch/deterministic-attended-workflows-943570 and will land it when it finishes. Coordinate.
— owner, the bootstrap question

## Owner confirmation

Asked: The bar is still running, and three root causes are confirmed so far: the foreign-prefix declarations, the driver fixture's harness files, and the roles kit citing v3 charter §n sections that v4 no longer has. Shall I go and build aSweptBar, adding later reds to the roster as they land?
Answer: Go (Recommended)
