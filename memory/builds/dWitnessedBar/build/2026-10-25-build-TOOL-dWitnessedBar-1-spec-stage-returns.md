**Serves:** research TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30

# The SPEC stage's returns — unattended-build.js run wf_70b6059f-3a4

Each agent's result, extracted from the run's journal by script, never retyped.

## Agent 1 · dWitnessedBar · TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 · spec-write

run wf_70b6059f-3a4/a1fd3dd4d56f01279, phase Spec

```json
{
 "agentId": "a1fd3dd4d56f01279",
 "result": {
  "authored": [
   "TOOL-dWitnessedBar-26",
   "TOOL-dWitnessedBar-27",
   "TOOL-dWitnessedBar-13",
   "TOOL-dWitnessedBar-15",
   "TOOL-dWitnessedBar-12",
   "TOOL-dWitnessedBar-22"
  ],
  "alreadyPresent": [],
  "refused": [],
  "summary": "I wrote all six specs in my group, in roster order, under memory/builds/dWitnessedBar/spec/. Each is Tier-2 with the status header OPEN · rev-1 · 2026-10-25 · node d · base cdfbd1cf · streams tooling · order 1 to 6 · advances TOOL-dWitnessedBar-31. Each also has its **Carries:** clause line plus one node line per owned node. Nothing is committed and the index was not regenerated. I wrote no deviation records, because none of the six departs from its clause. Every fork is marked RESOLVED (agent, 2026-10-25, delegated) with widens: none · relaxes: none, and every FACT-QUESTION carries the probe I ran.\n\n**Checks run:**\n- Hygiene `--only 2,12,25`, in a throwaway clone under %TEMP%/wbh26 (since removed): no finding on my six files. The reds it still prints are on other writers' specs: 4, 11, 16 and 25 under check 25.\n- My own probes over §6 and §7: every clause token appears verbatim in backticks. No criterion names an untracked path or a bar or suite invocation. Every §7 leg name exists in tools/gate-legs.json. Every `covers` id is a §6 label.\n\n**The units:**\n- **TOOL-dWitnessedBar-26 (bash resolver):**\n  - Canonical blocks `resolve_bash_py` in tools/lib/resolve_bash.py and `resolve_bash_js` in tools/lib/resolve_bash.js, each with a CLI, held by two new PARITY_ROWS rows and a truth-table section in tools/lib/resolve-python.test.sh.\n  - The 14 sites become thin adapters: the 7 PATH loops, profile_bar, regen, drift's `resolve_bash_shell`, process-monitor's `resolve_launcher`, `resolve_shell_argv` (which now raises Refusal instead of falling back to bare bash), stop-guard.js, and check_policy.py.\n  - `test_no_bare_bash_argv` is widened repo-wide through `scan_bare_bash`.\n  - The WSL-first red case uses a copy of System32's bash.exe outside System32; on node d it answers `uname -s` with `Linux`.\n- **TOOL-dWitnessedBar-27 (wrong-shell refusal):**\n  - Block `refuse_wrong_shell` in tools/lib/refuse-wrong-shell.sh, builtins only so it adds no fork. It refuses when the script's own path is under `/mnt/<letter>/` and a WSL marker is present.\n  - It is carried by the 75-file entry-point population, plus Python and JavaScript twins inside unit 26's blocks.\n  - A both-ways coverage arm checks the population.\n- **TOOL-dWitnessedBar-13 (ledger factory, system.retrofit):**\n  - The `legacy_ledger_py` factory. Registrations are `[[ledger]]` tables in each owning kit's kit.toml, and each ledger file has a header line rendered from its registration.\n  - Directions, base and rename carry are covered; `compute_coverage` and `resolve_compare_base` are imported from PLAY-dOrderedCharter-19 S9 (D3: the build run re-grounds, and stops this unit if S9 is still absent).\n  - The `check_ledger` merge class lives in merge-rows.py and is selected by that header. Inline copies go to memory-tree and gate-lint, plus a gate-lint copy of coverage_join.\n  - sh_hygiene and encoding_posture become adapters that keep their four-field grammar until unit 16 converts them.\n- **TOOL-dWitnessedBar-15 (test.seed, item.test.seed, retrofit.unseeded):**\n  - The seed verb is absent-only, with `--widen` appending `widened:<record>` rows only.\n  - An unarmed state is recorded in the home itself.\n  - `retrofit.unseeded` defaults to `unarmed` until policy.py lands.\n  - The two adopter guards (adopt-codebase-map.sh:198, adopt-drift-audit.sh:241) become calls to an unregistered `seed --home` form.\n  - An `item.test.seed` row is added to tools/loop/loop.toml.\n- **TOOL-dWitnessedBar-12 (leg, check, pack namespaces):**\n  - 142 tags of the form `leg.<kit id or gov>.<slugged name>`, cut at 64 bytes. A measured probe at cdfbd1cf gives 142 unique, shape-valid tags.\n  - Three namespace rows and three extractors; `check` stays unarmed until a kit declares `[[check]]` rows.\n  - The two KNOWN literals become one `LEG_KEYS` constant.\n  - New `LEG_KEY_FLOORS` table, plus a 7h tag join and a gov-canary tag arm.\n- **TOOL-dWitnessedBar-22 (tests and enforces):**\n  - `tests` is filled once from the dossiers' `[claims] gate-legs`: 122 legs claimed, 20 not, which carry no value.\n  - `read_leg_edges` becomes the leg-row site of the edge grammar. Edges to `feature.*` are reported unarmed until dTotalRecall registers that namespace.\n  - A both-ways compare against the dossiers goes in the gov canary, and 7h joins both keys.\n  - `enforces` follows PLAY-dOrderedCharter-7 S2 (principle.* and practice.*).\n\n**Edges I added beyond the brief's table, so the other writers' specs reconcile:**\n- 13 hands-off 19 (`legacy_ledger.py`)\n- 15 hands-off 24 (`test.seed`)\n- 26 hands-off 24 (`scan_bare_bash`)\n\nSpecs 19 and 24 already declare these back. Spec 21 already declares consumes-from 22 (`tests`).\n\n**Asks the main loop needs to file:**\n1. dOrderedCharter (PLAY-dOrderedCharter-24): widen the `enforces` edge row's `to` to admit `principle`. Unit 22 §8 F1 widens that one row in tools/playbook/edges.toml itself if the ask has not landed by the build run.\n2. dTotalRecall: register the `feature` namespace, and derive the dossiers' `[claims] gate-legs` from the legs' `tests` edges (unit 22 §8 F2).\n3. dOrderedCharter (PLAY-dOrderedCharter-50 S2): owed_rows.py's \"each KNOWN copy\" read becomes `LEG_KEYS` after unit 12, which updates it in its pass where it has landed.\n4. dSettledRoster: TOOL-dSettledRoster-6 (the three resolve_bash copies) is answered by unit 26 at landing; dispose of it then.\n5. dGroundRules (TOOL-dGroundRules-25 S28): its `resolve_bash_py` block keeps profile_bar's bare-bash fallback, which unit 26 rewrites in place (§8 F1).\n\n**Note for unit 21's writer:** unit 22 §8 F3 reads a `tests` target as the thing the leg tests, not the leg's own test file. So shared interface I15's \"targets of its tests edge\" should not be fenced out of a fix pass's allowance. Spec 21's line 68 already reads it that way.\n\nFiles:\n- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-d0e46e/memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-26.md\n- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-d0e46e/memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-27.md\n- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-d0e46e/memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-13.md\n- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-d0e46e/memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-15.md\n- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-d0e46e/memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-12.md\n- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-d0e46e/memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-22.md"
 }
}
```

## Agent 2 · dWitnessedBar · TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 · spec-write

run wf_70b6059f-3a4/af59dde1869526791, phase Spec

```json
{
 "agentId": "af59dde1869526791",
 "result": {
  "authored": [
   "TOOL-dWitnessedBar-19",
   "TOOL-dWitnessedBar-11",
   "TOOL-dWitnessedBar-14",
   "TOOL-dWitnessedBar-16",
   "TOOL-dWitnessedBar-17",
   "TOOL-dWitnessedBar-18"
  ],
  "alreadyPresent": [],
  "refused": [],
  "summary": "I wrote all six Tier-2 specs in my group, and one deviation record. Nothing is committed and I did not run the index generator. Each spec is OPEN rev-1 with base cdfbd1cf, its roster `order` (7 to 12), `advances TOOL-dWitnessedBar-31`, and its `**Carries:**` line; unit 14 also carries `node:policy-key.retrofit.widen`.\n\nI ran hygiene checks 2, 12 and 25 in a throwaway clone. One red is left on my files: unit 17 declares `consumes-from TOOL-dWitnessedBar-15` (`test.seed`, which seeds its three new populations), but unit 15 has no matching `hands-off TOOL-dWitnessedBar-17`. Unit 15 needs that line added. I did not run check-spec-tokens. Instead I checked by script that every path an acceptance criterion names exists at HEAD or is cited by basename, and that each spec's §7 leg line names every guarded leg its Files touched trips.\n\n**What each spec builds**\n- **19 (`purpose` field):** adds `purpose` to `LEG_KEYS` and `LEG_KEY_FLOORS`, plus three new govkit selfcheck 7h checks: presence, shape (at most 60 characters, unique), and descriptor-vs-manifest agreement. A four-step rule derives each purpose from the name's parenthetical, the descriptor comment, the script header or the dossier title. A review record cites every leg's source. Any leg the rule cannot reach goes on a `leg-purpose-pending` ledger population and into one owner ask; that population is written only if non-empty.\n- **11 (leg factory):** each leg gets one declaration: a kit `[[gate_leg]]` row, or a full `[[exempt_leg]]` row in `tools/govkit/registry.toml`. Gov's own differing values go in a `[gate_leg.gov]` sub-table, so adopter manifests stay byte-identical. `leg_factory.py` generates `tools/gate-legs.json` (verbs `--write`, `--check`, `--conform`, `--list`, `new`) and is registered with regen. It fills the `kind.gate-leg` row and every leg's `enforces`, and retires 7h's leg checks, with a Readers clause. Units 9, 10, 24 and 28 already build on these names.\n- **14 (`ratchet` pack):** `tools/memory-tree/ratchet.py`, nine legs (eight live plus a selftest), the `widen` record and its verb, and `retrofit.widen` read through `policy.py`. It adds a `conf-scalar-pins` population holding today's nine scalar pins.\n- **16 (registries):** converts all 28 registries in place onto the ledger, re-points their readers, and retires drift's `SHRINK_ONLY`, `PINS` and `BASELINES` with a Readers clause. Deviation 161 records the 28-vs-27 difference: `temp-name-sites.txt` landed after the baseline.\n- **17 (pins and cutoffs):** turns the seven pins into keyed populations and registers all 36 cutoffs as one `date-cutoffs` population.\n- **18 (keyed lists):** registers the three dOrderedCharter lists and a `landed-steps` population for dSafePassage's step rows.\n\n**Interface asks on unit 13 (for the main loop to file or fold)**\n- `read_registrations` should also read `[[ledger]]` tables in `tools/govkit/registry.toml`. Three registries read by repo-root tools, and the step rows, have no kit descriptor to register in (16 §8 F3, 18 §8 F2).\n- The factory's line-number refusal needs a declared exception, `verbatim = [<field>]`, so file:line positional references can be stored (18 §8 F1).\n- The ledger row has no reason column, so unit 16 puts every former reason into its conversion record (16 §8 F1). If the audit wants reasons kept in the rows, unit 13's grammar would have to change.\n\n**Edges I added beyond the brief's table, all reciprocal within my group:** 14→17 (`conf-scalar-pins`, `ratchet.py`), 14→18 (`ratchet.py`), 16→17 (`RATCHETS`). 13→19 is already reciprocated by unit 13; 15→17 is the open one above.\n\n**Where the brief or scouts disagree with source**\n- 142 legs, not 140, and 68 descriptor rows, not 70.\n- 36 cutoffs at cdfbd1cf, not 33.\n- IW-1's legacy list is in PLAY-dOrderedCharter-20 S8, not S4.\n\nEach is recorded in its spec's §8 or §10.\n\n**Files** (all under `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-d0e46e/memory/builds/dWitnessedBar/`):\n- `spec/2026-10-25-spec-TOOL-dWitnessedBar-19.md`\n- `spec/2026-10-25-spec-TOOL-dWitnessedBar-11.md`\n- `spec/2026-10-25-spec-TOOL-dWitnessedBar-14.md`\n- `spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md`\n- `spec/2026-10-25-spec-TOOL-dWitnessedBar-17.md`\n- `spec/2026-10-25-spec-TOOL-dWitnessedBar-18.md`\n- `build/2026-10-25-build-TOOL-dWitnessedBar-16-deviation-161.md`\n\nOne temp-path slip: I briefly wrote hygiene output logs directly under %TEMP% instead of the scratchpad. They are deleted, along with the throwaway clone."
 }
}
```

## Agent 3 · dWitnessedBar · TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 · spec-write

run wf_70b6059f-3a4/a7d9faeec7c6c3dcf, phase Spec

```json
{
 "agentId": "a7d9faeec7c6c3dcf",
 "result": {
  "authored": [
   "TOOL-dWitnessedBar-20",
   "TOOL-dWitnessedBar-24",
   "TOOL-dWitnessedBar-10",
   "TOOL-dWitnessedBar-9",
   "TOOL-dWitnessedBar-4",
   "TOOL-dWitnessedBar-25"
  ],
  "alreadyPresent": [],
  "refused": [],
  "summary": "I wrote all six specs in my group, each as an OPEN Tier-2 rev-1 spec at base cdfbd1cf with the `order` the roster gives (13 to 18) and `advances TOOL-dWitnessedBar-31`. Nothing is committed and the index was not regenerated. Under memory/builds/dWitnessedBar/spec/:\n- 2026-10-25-spec-TOOL-dWitnessedBar-20.md\n- 2026-10-25-spec-TOOL-dWitnessedBar-24.md\n- 2026-10-25-spec-TOOL-dWitnessedBar-10.md\n- 2026-10-25-spec-TOOL-dWitnessedBar-9.md\n- 2026-10-25-spec-TOOL-dWitnessedBar-4.md\n- 2026-10-25-spec-TOOL-dWitnessedBar-25.md\n\n**Checks run.** I ran `check-memory-hygiene.sh --only 2,12,25` in a throwaway clone under %TEMP%, with all specs present at the time committed there. It reports nothing on my six files. The clone is deleted. I did not run `check-spec-tokens.py`; the main loop runs it. No §6 criterion names a path that does not exist at HEAD, the runner, a `*.test.sh` suite or a `GATE_*=` assignment. I wrote no deviation records, because no unit departs from its clause.\n\n**What each spec covers:**\n- **Each spec:** carries its clause whole, every owned node and every clause token. Every §8 fork is resolved by the plan's rungs, and every §10 records the seam and the recall terms.\n- **Unit 20:** the legacy-homes list becomes a ledger population in unit 13's row format. The mark column is no longer stored; it is derived from `GATE_ENV_MARKS`. The registration is a `[[ledger]]` table in `tools/policy/kit.toml`.\n- **Unit 24:** the portability pack, with one leg per rule and five new populations. The bare-shell leg runs unit 26's `scan_bare_bash`, and `ps-hygiene.py` gets a self-test leg.\n- **Unit 10:** a `precommit` row key and a `run-gates.sh --precommit` mode replace the five gates hand-named in the pre-commit hook. Ceiling evidence is keyed by leg and node, and `bar-wall-evidence.txt` holds each node's whole-bar wall time.\n- **Unit 9:** a `level` row key, a `[[test_runner]]` pytest adapter and `product_tests.py`. Each `tests.product` value has its own planted-repository case.\n- **Unit 4:** the runner writes `<common-dir>/gate-verdict/<tree hash>`, plus a `.scoped` file, for GREEN and RED runs. All three `write_bar_green` writers are deleted (hook, driver, post-merge). `verdict.tree` drives `--prepare`, and `item.test.exit` records the verified tree.\n- **Unit 25:** the verdict gains `run_id`, `cause` (set through `GATE_CAUSE`) and `tail.<n>`. Tails are kept in the common dir, and under `tail-by-hash` they are committed as `leg-tail` records after a pass through runlog's `scan_secrets`.\n\n**Things you should know:**\n- **Units 4 and 25 grow shell files.** Unit 24's shell-role population refuses that growth unless a widen record admits it, so both specs say they write a widen row.\n- **Unit 10 makes commits slower.** The trigger is the leg's own `guard`, and all five pre-commit legs are unguarded, so each now runs on every commit. Staged-only memory hygiene measured 1.3 s with nothing staged; the other costs are unmeasured (§8 F1). The open ask TOOL-aTrimmedHook-8 is about this hook's cost.\n- **Sibling edges are consistent.** Unit 24's edges to units 15 (`test.seed`) and 26 (`scan_bare_bash`) are not in the brief's table, but both siblings already declare the matching hands-off. Every other edge matches. I aligned names with what siblings wrote: unit 13's `[[ledger]]`, `read` CLI and header line; unit 15's seed output format; unit 11's `[gate_leg.gov]` sub-table; unit 12's `LEG_KEYS`.\n\n**Asks for the main loop to file:**\n1. dSafePassage: TOOL-dSafePassage-11 §3 says the TOML 1.0 arm is this build's job. The owner's AP-31 answer says it is not built (`away-pass.md:479`).\n2. dOrderedCharter: PLAY-dOrderedCharter-30 §3 says the floor arm is dSafePassage's. TOOL-dSafePassage-11 §3 and this clause give it to dWitnessedBar (unit 24).\n3. This build's BACKLOG: gap-test-09 has two parts no unit covers (unit 24 §8 F7). One is the stale held-leg figure at `tools/run-gates/README.md:98`; the other is eight held legs with no guard.\n4. dGroundRules, for information: after unit 20 lands, TOOL-dGroundRules-7 S2/S3 no longer hold, because the list stores no mark. S4's \"grows by no command\" also changes: under `retrofit.widen: record-reason` a widen record can admit growth.\n5. Stale comment: `tools/run-gates/run-selftests.sh:280` names a Python `_resolve_node_tag` that no longer exists in the tree."
 }
}
```

## Agent 4 · dWitnessedBar · TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 · spec-write

run wf_70b6059f-3a4/a8e722911dd4936ab, phase Spec

```json
{
 "agentId": "a8e722911dd4936ab",
 "result": {
  "authored": [
   "TOOL-dWitnessedBar-23",
   "TOOL-dWitnessedBar-3",
   "TOOL-dWitnessedBar-5",
   "TOOL-dWitnessedBar-8",
   "TOOL-dWitnessedBar-1",
   "TOOL-dWitnessedBar-30"
  ],
  "alreadyPresent": [],
  "refused": [],
  "summary": "All six units in my group are written as Tier-2 specs. Each is OPEN · rev-1 · base cdfbd1cf · streams tooling, carries the `order` from the roster and `advances TOOL-dWitnessedBar-31`. Nothing was committed and the index was not regenerated. I also wrote one deviation record. All files are under memory/builds/dWitnessedBar/:\n- spec/2026-10-25-spec-TOOL-dWitnessedBar-23.md (order 19)\n- spec/2026-10-25-spec-TOOL-dWitnessedBar-3.md (order 20)\n- spec/2026-10-25-spec-TOOL-dWitnessedBar-5.md (order 21)\n- spec/2026-10-25-spec-TOOL-dWitnessedBar-8.md (order 22)\n- spec/2026-10-25-spec-TOOL-dWitnessedBar-1.md (order 23)\n- spec/2026-10-25-spec-TOOL-dWitnessedBar-30.md (order 24)\n- build/2026-10-25-build-TOOL-dWitnessedBar-3-deviation-31.md\n\n**Checks:** I ran memory hygiene checks 2, 12 and 25 in a throwaway clone. They report nothing on my six specs or the deviation record; the remaining reds are on other writers' specs. I confirmed check 12 does grade my files by planting a defect in a copy and watching it fail, then removed the clone. Every edge in the brief's table that touches my units is answered on both sides, every scope item names a criterion, and every criterion has a `Red when:` clause. No criterion names a suite, the merge bar or a path missing at HEAD. Each §7 leg line names every leg that its Files touched paths trip.\n\n**Owed by the main loop:**\n1. **Unit 6 must change one name.** The leg-ask function is now spelled `write_leg_ask`, not the brief's `file_leg_ask` (unit 8 §8 F4). `file` is not a declared lexicon verb, and the lexicon's verb-offender count already equals its pin (1211, `.lexicon.conf:312`), so one new offender would turn `lexicon naming predicates` red. Unit 6 still spells `file_leg_ask` at its lines 63, 76 and 111. Until it is changed, the spec-token check will report unit 8's hands-off to unit 6 as missing that name. For the same reason, unit 30's ask-closing function is `write_ask_closing`.\n2. **An ask for dUnstuckLanding.** Unit 3 retires `INHERITED_RED`, replacing it with `verdict.blocks`; an upgrade step maps `land` to `own-mixed-contended` and `park` to `every-red`. The open ask TOOL-dUnstuckLanding-11 still accepts on adopters declaring `INHERITED_RED=land`. Its acceptance needs restating as `verdict.blocks = \"own-mixed-contended\"` in each adopter's `.governance/policy.toml`.\n\n**Choices that differ from the brief or the design, each recorded as a resolved fork in the spec's §8:**\n- **A `DEAD PROBE` red blocks under every value** (unit 3 F1). The design let it pass under some values, but every red reads `DEAD PROBE` when `lib-attribute.sh` is missing, so that would let any red land. This is the one departure from a clause, recorded as deviation 31 (risk: stricter).\n- **Interface I11 gains a third hold-source word, `level`,** for legs whose test level is not a landing level (unit 5 F1). Unit 5 owns I11; the brief's `kit` and `quarantine` are unchanged.\n- **The flake and gate-health records are registered only in the record factory, with no `kinds.toml` row** (unit 8 F2). The brief's I12 asked for both. The design gives \"record kind\" one register row, owned by dConvergedCharter, and dDeclaredLoop already registered its `disposition` record the same way.\n- **One flake record per Test-step run, with a row for every leg that ran** (unit 8 F1). A record per flaky leg would have no count of verdicts, so neither the window nor the clause's \"30 verdicts per leg\" could be read from it.\n- **\"Every leg of the bar\" means the legs the kit hold does not hold** (unit 1 F1). Counting all 142 legs would never arm on gov, because the held self-test class runs only on request.\n- **Quiet host uses the existing `check_quiet` probe in `profile_bar.py`, given a Linux branch,** not the turnstile's census the brief's unit row named (unit 30 F3). The turnstile only sees one clone's bars and misses others on the same host."
 }
}
```

## Agent 5 · dWitnessedBar · TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 · spec-write

run wf_70b6059f-3a4/ab82540d141bc1c11, phase Spec

```json
{
 "agentId": "ab82540d141bc1c11",
 "result": {
  "authored": [
   "TOOL-dWitnessedBar-29",
   "TOOL-dWitnessedBar-7",
   "TOOL-dWitnessedBar-21",
   "TOOL-dWitnessedBar-6",
   "TOOL-dWitnessedBar-2",
   "TOOL-dWitnessedBar-28"
  ],
  "alreadyPresent": [],
  "refused": [],
  "summary": "I wrote all six Tier-2 specs in my group. Nothing is committed and I did not regenerate the index. One edge is still one-sided: unit 28 depends on unit 15, and the main loop needs to add the reverse line to unit 15's spec before the commit stage, or the hygiene gate goes red.\n\nI ran hygiene checks 2, 12 and 25 in a throwaway clone with the current sibling specs. That edge is the only finding on my specs; check 25 also flagged specs 4, 11, 14, 16, 17 and 25, which belong to other writers. I did not run `check-spec-tokens.py`: the main loop runs it. I computed the guarded legs each spec owes from `tools/gate-legs.json` with my own read-only script and added them to each §7 leg line.\n\nEach spec has the header the brief asks for (OPEN, rev-1, order 25 to 30, `advances TOOL-dWitnessedBar-31`), all ten sections, the Carries lines for its clause and its owned nodes, and §8 forks resolved in place.\n\n**Fixes the main loop owes:**\n- **One-sided edge.** `TOOL-dWitnessedBar-28` declares `consumes-from TOOL-dWitnessedBar-15` for `test.seed`, because unit 15 seeds the population of adopters' hand-added leg rows. Unit 15's spec needs the line `hands-off TOOL-dWitnessedBar-28 — test.seed`. This edge is not in the brief's table; I added it because 28 really depends on it.\n- **Ask for dOrderedCharter's backlog.** PLAY-dOrderedCharter-36's schema grammar can't express \"a ceiling widens as it rises\" or \"any `argv` change widens\". Unit 28 adds two scalar directions, `rises` and `changes`, to `read_kind_schema` and the classifier in `tools/playbook/row_checks.py` (its §8 F2). The ask is for that parent spec to admit them.\n\n**Interface notes:**\n- **I15 (unit 21).** I left out the `tests` edge targets as kept files. Unit 22's S1 defines them as \"a thing the leg tests\", which is the code a fix pass has to change. Unit 21 still reads `tests`, but only to name those targets in its refusal, so the 22→21 edge holds.\n- **Units 7, 2 and 6.** Unit 7 names the seen-red reader `read_seen_red_records`, which unit 28 calls. Unit 2's `refused` value relies on unit 6's `off_node` registry field. Unit 6 files the remote pin's owner item through unit 8's `file_leg_ask`, from the driver's gates-green term.\n\n**Deviation records, all risk loosening, approver the spec writer under `author-recorded`:**\n- `2026-10-25-build-TOOL-dWitnessedBar-7-deviation-71.md`: a gate counts as changed when its `argv` moved or a spec declares a new arm for it, not on any script edit.\n- `2026-10-25-build-TOOL-dWitnessedBar-21-deviation-211.md`: \"the acceptance commands' own files\" means the test and fixture files they name, not the module they probe.\n- `2026-10-25-build-TOOL-dWitnessedBar-28-deviation-281.md`: gov legs an adopter hand-edited before conversion go on the legacy list instead of being overwritten.\n\nSpecs, under `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-d0e46e/memory/builds/dWitnessedBar/spec/`:\n- `2026-10-25-spec-TOOL-dWitnessedBar-29.md`\n- `2026-10-25-spec-TOOL-dWitnessedBar-7.md`\n- `2026-10-25-spec-TOOL-dWitnessedBar-21.md`\n- `2026-10-25-spec-TOOL-dWitnessedBar-6.md`\n- `2026-10-25-spec-TOOL-dWitnessedBar-2.md`\n- `2026-10-25-spec-TOOL-dWitnessedBar-28.md`\n\nThe three deviation records are under `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-d0e46e/memory/builds/dWitnessedBar/build/`."
 }
}
```

## Agent 6 · dWitnessedBar · specs · commit

run wf_70b6059f-3a4/a86241281d6b74a6d, phase Spec

```json
{
 "agentId": "a86241281d6b74a6d",
 "result": {
  "committed": false,
  "sha": "19d6aae644d9a8e676c239eb0228e524eb7a685f",
  "why": "The build-index generator (`python -B tools/memory-tree/gen_build_index.py --write`) exited 1 and stopped the block with this refusal: \"Build-index: memory/builds/dWitnessedBar/README.md: front matter declares 'status: OPEN' but 30 spec(s) carry a status header — the build status is DERIVED from them, and two answers to one question is exactly the drift this index removes. Delete the 'status:' key.\"\n\nNothing was committed and HEAD is still 19d6aae64. The refusal came before any write, so `git diff` shows no rendered view.\n\nAll 30 specs are still staged as additions (A), from the block's first `git add`. They need `git reset -q -- <spec paths>` before a re-run, or they can stay staged for one.\n\nThe fix is outside this stage: delete the `status:` key from the front matter of memory/builds/dWitnessedBar/README.md, then run the block again.\n\nProcedural note: the first inline Bash call failed to parse (\"unexpected EOF while looking for matching `''\") and staged nothing, which I checked. I then ran the identical block, with only the mandated substitutions, as one `bash <script>` invocation from C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dwitnessedbar-d0e46e/871858cc-6dd1-48fc-bfcd-88d1d87e87dc/scratchpad/spec-commit.sh.\n\nThere is no commit, so the gotchas checklist (step 6) was not run.",
  "specs": [
   {
    "id": "TOOL-dWitnessedBar-26",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-26.md"
   },
   {
    "id": "TOOL-dWitnessedBar-27",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-27.md"
   },
   {
    "id": "TOOL-dWitnessedBar-13",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-13.md"
   },
   {
    "id": "TOOL-dWitnessedBar-15",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-15.md"
   },
   {
    "id": "TOOL-dWitnessedBar-12",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-12.md"
   },
   {
    "id": "TOOL-dWitnessedBar-22",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-22.md"
   },
   {
    "id": "TOOL-dWitnessedBar-19",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-19.md"
   },
   {
    "id": "TOOL-dWitnessedBar-11",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-11.md"
   },
   {
    "id": "TOOL-dWitnessedBar-14",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-14.md"
   },
   {
    "id": "TOOL-dWitnessedBar-16",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md"
   },
   {
    "id": "TOOL-dWitnessedBar-17",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-17.md"
   },
   {
    "id": "TOOL-dWitnessedBar-18",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-18.md"
   },
   {
    "id": "TOOL-dWitnessedBar-20",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-20.md"
   },
   {
    "id": "TOOL-dWitnessedBar-24",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-24.md"
   },
   {
    "id": "TOOL-dWitnessedBar-10",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-10.md"
   },
   {
    "id": "TOOL-dWitnessedBar-9",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-9.md"
   },
   {
    "id": "TOOL-dWitnessedBar-4",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-4.md"
   },
   {
    "id": "TOOL-dWitnessedBar-25",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-25.md"
   },
   {
    "id": "TOOL-dWitnessedBar-23",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-23.md"
   },
   {
    "id": "TOOL-dWitnessedBar-3",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-3.md"
   },
   {
    "id": "TOOL-dWitnessedBar-5",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-5.md"
   },
   {
    "id": "TOOL-dWitnessedBar-8",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-8.md"
   },
   {
    "id": "TOOL-dWitnessedBar-1",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-1.md"
   },
   {
    "id": "TOOL-dWitnessedBar-30",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-30.md"
   },
   {
    "id": "TOOL-dWitnessedBar-29",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-29.md"
   },
   {
    "id": "TOOL-dWitnessedBar-7",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-7.md"
   },
   {
    "id": "TOOL-dWitnessedBar-21",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-21.md"
   },
   {
    "id": "TOOL-dWitnessedBar-6",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-6.md"
   },
   {
    "id": "TOOL-dWitnessedBar-2",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-2.md"
   },
   {
    "id": "TOOL-dWitnessedBar-28",
    "path": "memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-28.md"
   }
  ],
  "summary": "Not committed: gen_build_index.py refused because memory/builds/dWitnessedBar/README.md still has a 'status: OPEN' key, which clashes with the status the 30 specs' headers derive. HEAD is still 19d6aae64, nothing was rendered, and all 30 specs are left staged. The fix is to delete that key, then unstage the specs or leave them staged, and run the block again.",
  "checklist": ""
 }
}
```
