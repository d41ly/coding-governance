# TOOL-dWellOiledMachine-94 — the round-2 promotions audit's 37 medium and low findings, batched: verbs, stores, claim layout, coverage lists, renders and citations

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 67 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-94-deviation-941.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-94-deviation-941.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md`)
exited CONVERGED with 37 confirmed findings below HIGH. BUILD-METHOD M4 promotes every one of them,
batched into ONE unit, and this is that unit. It closes, by report id:

- MEDIUM (28): 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 18, 19, 26, 27, 28, 29, 30, 31, 32, 33, 36, 37,
  40, 41, 42, 44.
- LOW (9): 3, 13, 14, 15, 20, 21, 24, 34, 35.

Several findings share a report item (M1: 1, 33; M3: 4, 19, 29; M4: 5, 37; M5: 6, 28, 36; L1: 3, 20;
L4: 15, 24), and each keeps its own scope item here. Finding 16 takes the grade its skeptic re-graded
it to, medium. Each finding takes the fix its skeptic judged SOUND, or the skeptic's corrected fix
where the report marks the finder's UNSOUND (findings 6, 13, 16, 18). The findings land on many units,
so this unit repairs none in particular and sits after every unit of the build. One unit, not two:
the fixes meet in spec 90's file (findings 7 to 14, 26, 27, 30, 32, 34), spec 85's file (2, 3, 20, 32,
42), spec 83's file (4, 19, 29, 30, 44, 21) and `tools/runtime/commit_keys.py` (2, 32, 42), so no split
into two disjoint write sets exists under M6.

## 2. Scope (IN)

Each item names its finding, its report item and the unit or spec it lands on. "Spec N takes a rev
bump" means spec N is amended at this unit's pass, its §9 line naming this unit and the finding. Paths
are those at this unit's order: TOOL-dWellOiledMachine-28 (order 61) has moved `resume-tick.sh`,
`stall-recorder.js` and their suites into `tools/runtime/`.

- **S1** — Finding 1 (M1, with 33), on TOOL-dWellOiledMachine-82 AC2. Spec 82 takes a rev bump whose
  AC2 has the `shared-event-rewire` case in `tools/govkit/selftest.py` call
  `gk.remove_wired_fragments(t, rows, added.get(kit, []), "update")`, as `tools/govkit/selftest.py:2369`
  does, then require B's rows and A's original rows in the table. Observed by AC1.
- **S2** — Finding 33 (M1), on TOOL-dWellOiledMachine-82 AC2. No `rollback` verb is added to
  `govkit.py`: the rollback is reached through `remove_wired_fragments`, which `cmd_update`'s
  rolled-back branch calls (`tools/govkit/govkit.py:11685`), and spec 82 no longer spells
  `govkit.py rollback`. Observed by AC1.
- **S3** — Finding 2 (M2), on TOOL-dWellOiledMachine-85, -90 and -33. One test store, named once here:
  `fixture-store`, a scratch-file backend that `commit_keys.py --fixture` injects in place of
  `read_secret_ref` and `write_secret_ref`, writable, reachable only under `--fixture`, and never a
  value of `runtime.secret-home`. Specs 85 (AC1, §5), 90 (S4, AC55) and 33 (AC7) take rev bumps naming
  `fixture-store` for every salt case that writes; the read-only `env-injected` cases keep that home.
  Observed by AC2.
- **S4** — Finding 3 (L1, with 20), on TOOL-dWellOiledMachine-85 AC3. Spec 85 takes a rev bump whose AC3
  runs `commit_keys.py digest s1`. Observed by AC3.
- **S5** — Finding 20 (L1), on TOOL-dWellOiledMachine-85 AC3 against spec 33's minted verb. No
  `--digest` flag is added; the positional verb `digest <session>` is the one spelling. Observed by
  AC3.
- **S6** — Finding 4 (M3), on TOOL-dWellOiledMachine-83 S3, -80 and -90. The claim's layout stated once,
  in 83 S3 by rev bump: the tick takes `<slug>.starting` through `write_node_lock`, which writes `until`
  and `owner`, and right after it returns 0 writes `pid`, `image` and `stamp` inside the claim, the
  values 78 S3 and 90 S19 record; `check_supervisor_claim_stale` reads those three files and never
  `owner` or `until`. Specs 80 (S1, AC2) and 90 (AC19) take rev bumps planting through
  `write_node_lock` and then writing, or omitting, those files. Observed by AC4, AC5.
- **S7** — Finding 19 (M3), on TOOL-dWellOiledMachine-83 S3. The `owner` token's format is
  `<pid>.<stamp>`, used only by `remove_node_lock`'s release compare; 83 S3's rev bump says so, and a
  claim taken by `write_node_lock` and then filled reads complete. Observed by AC4.
- **S8** — Finding 29 (M3), on TOOL-dWellOiledMachine-83 S1, S3 and -80 S3. The stale function passed
  to `write_node_lock` decides at both of the factory's stale tests, before and under the `.break`
  guard. 80 S3's reap line is printed by the tick: before the take it notes whether a claim was present
  and, if so, whether its `pid` or `stamp` was missing and its age; a take that then returns 0 prints
  `supervisor — <slug> · claim reaped · <incomplete|dead>, <age>s old`. Specs 83 and 80 take rev bumps
  saying so. Observed by AC4.
- **S9** — Finding 5 (M4, with 37), on TOOL-dWellOiledMachine-89 S2. `supervise.py --fixture` gains
  `--plant claim-is-file`: `gov/supervisors/` a writable directory and `<slug>.starting` pre-created as
  a regular file ten seconds old, so the claim's create fails with no claim directory present. Spec 89
  takes a rev bump adding the criterion. Observed by AC6.
- **S10** — Finding 37 (M4), on TOOL-dWellOiledMachine-89 S2. 89 S2's "Observed by" names S9's new
  criterion in place of AC2, whose plant fails at S1's `mkdir -p` first. Observed by AC6.
- **S11** — Finding 6 (M5, the skeptic's corrected fix), on TOOL-dWellOiledMachine-84 S3. The coverage
  case's population is every `refs/gov/` literal under `tools/runtime/`, `tools/unattended/`,
  `tools/memory-tree/`, `tools/lib/`, `tools/run-gates/` and `tools/push-main.sh`. Spec 84 takes a rev
  bump. Observed by AC7.
- **S12** — Finding 28 (M5), on TOOL-dWellOiledMachine-84 S1, S3. The bare `CLAIM_NS` root
  `refs/gov/runs` (`tools/unattended/unattended.sh:2087`) is read as matched by the `refs/gov/runs/`
  entry, the namespace's own root, and `refs/gov/remote/` (`:2088`, a local cache of remote claims never
  written through `write_gov_ref`) joins the exempt list. Observed by AC7.
- **S13** — Finding 36 (M5), on TOOL-dWellOiledMachine-84 S3 against -18, -12 and -55. The exempt list
  gains, each with its reason and source spec: `refs/gov/waits/` (18 §3, kept out of the door),
  `refs/gov/checkpoints/` (12, local and never pushed) and `refs/gov/conform/` (55, scratch), beside
  `refs/gov/bar-red`. Spec 84's AC4 records the expected unmatched set at HEAD, which is empty. Observed
  by AC7.
- **S14** — Finding 7 (M6), on TOOL-dWellOiledMachine-90 AC20. Spec 90 takes a rev bump whose AC20
  runs `git grep -nE "\[\"bash\"|\['bash'" -- 'tools/**/*.py'`. Observed by AC8.
- **S15** — Finding 8 (M7), on TOOL-dWellOiledMachine-90 AC6. Spec 90 takes a rev bump whose AC6 runs
  `python tools/runtime/conformance.py run --replay tools/runtime/fixtures/conformance/claude-code-2.1.292/`.
  Observed by AC9.
- **S16** — Finding 9 (M8), on TOOL-dWellOiledMachine-90 AC48. Spec 90 takes a rev bump whose AC48 runs
  `python tools/settings-merge.py config/settings.json --fragment <f>` from a scratch target root, as
  its callers do, and requires the table at `<root>/.claude/hook-packs.json`. Observed by AC10.
- **S17** — Finding 10 (M9), on TOOL-dWellOiledMachine-90 S48, -82 S1 and -79 S34.
  `run_fragment_merges`' stale probe (`tools/govkit/govkit.py:6158-6167`) passes `--table <scratch copy>`
  to its `--unwire` call, and `map_extractors.py`'s `harness-hooks` extractor reads the table at
  `<target root>/.claude/hook-packs.json`. Spec 90's S48 gains a Readers line naming both, and specs 82
  and 79 take rev bumps dropping "beside the settings file". Observed by AC11.
  **Readers:** by name: `tools/govkit/govkit.py` (`run_fragment_merges`) and
  `tools/codebase-map/map_extractors.py` (the `harness-hooks` extractor), both re-pointed here. by value: `remove_wired_fragments`, which unwires the `added` set the probe decides.
- **S18** — Finding 11 (M10), on TOOL-dWellOiledMachine-90 AC7 and S41. Spec 90 takes a rev bump whose
  AC7 greps the class `stall\.[^ ]*\.log|'stall'.*\.log`, dropping `unattended/stall`, and names as
  allowed rows the sidecar fixture lines of `stall-recorder.test.sh` and of
  `tools/unattended/unattended.test.sh` (`:8570`, `:8573` at this spec's base), suites README rule 8
  waives. Observed by AC12.
- **S19** — Finding 12 (M11), on TOOL-dWellOiledMachine-90 AC31. Spec 90 takes a rev bump whose AC31
  has one observation and one red per reader: card replay, the `Gov-*` trailer filler, the map extra of
  `bash skills/session-kickoff/manifest-check.sh --card --write` (23 S3) and the node
  `read_session_node` returns (35 S2) treat `machine` as `yes`, and the orientation gate still asks for
  a card. Observed by AC13.
- **S20** — Finding 13 (L2, the skeptic's corrected fix), on TOOL-dWellOiledMachine-90 S54. S54 names
  its exempt rows with reasons: `tools/hooks/scratch-guard.js:1206` and `:1318` and
  `tools/unattended/gate-guard.js:501`, which classify argv and spawn nothing. AC54's pattern widens to
  the literal class `['"]python3?['"]` with no call prefix, so a double-quoted, `python3`,
  `execFileSync` or multi-line spawn is caught. Observed by AC14.
- **S21** — Finding 14 (L3), on TOOL-dWellOiledMachine-90 AC14, AC23. Spec 90 takes a rev bump whose
  AC14 runs `grep -c "node writer" tools/memory-tree/gov_record.py help/runtime.md` and whose AC23 cites
  `help/runtime.md`. Observed by AC15.
- **S22** — Finding 15 (L4, with 24), on TOOL-dWellOiledMachine-81 S1. Spec 81 takes a rev bump whose
  S1 reads "rendered by `lease.renderUtc(new Date(resetsAt * 1000))` (`tools/unattended/run-lease.js:206`),
  the formatter `stall-recorder.js` already uses at `:74`", replacing the clause with no verb.
  Observed by AC16.
- **S23** — Finding 24 (L4), on TOOL-dWellOiledMachine-81 §10. 81's §10 names `renderUtc` as a reused
  seam. Observed by AC16.
- **S24** — Finding 16 (M12, the skeptic's corrected fix), on TOOL-dWellOiledMachine-72 S3, -86 §5 and
  -88 §5. 88 S2's head rule stands. Specs 72, 86 and 88 take rev bumps stating that a line made
  unparseable is read as deleted, so it falls under the stated head-deletion limit, and
  `tools/runlog/selftest.py` gains `crlf-hashed-lines`: only the run's hashed lines in `driver.log` are
  rewritten with CRLF while older parseable lines remain at its head. Observed by AC17.
  **Readers:** by name: `tools/runlog/record.py` (`check_commitment`), whose head rule specs 72, 86 and 88 state. by value: NO VALUE READERS — the fixture's CRLF lines are read only by the case that writes them.
- **S25** — Finding 18 (M13, the skeptic's corrected fix), on TOOL-dWellOiledMachine-65 AC2, AC3 and -47
  S10. `supervise.py --fixture --plant limit` and `limits_fixture.py`'s stub plant a limit by copying
  `tools/runtime/fixtures/stall/limit-transcript.jsonl` to scratch, substituting its literal reset
  `1789000000` with now plus 3600 and its record timestamp with now, the record TOOL-dWellOiledMachine-91
  accepts, and running `stall-recorder.js` on a payload naming that copy; no planter spells `resetsAt`,
  so 81 AC4 stands unchanged. Specs 65 and 47 take rev bumps saying so. Observed by AC18.
- **S26** — Finding 26 (M14), on TOOL-dWellOiledMachine-90 S1. Spec 90 takes a rev bump whose S1 and
  Files touched point at TOOL-dWellOiledMachine-93's tree-wide re-render of every README
  `gen_build_index.py --check` reports stale, never this build's README alone. Observed by AC19.
- **S27** — Finding 27 (M15), on TOOL-dWellOiledMachine-90 S10, S22. S10's population is 28 S1's and 28
  S4's moved files together, and S22 re-keys the `tools/unattended/resume-tick.test.sh` rows
  (`memory/project/spawn-idiom-sites.txt:276-280`) and `resume-tick.sh`'s rows (`:273-275`) to
  `tools/runtime/`. Spec 90 takes a rev bump. Observed by AC20.
- **S28** — Finding 30 (M16), on TOOL-dWellOiledMachine-80, -81, -83 and -90. Each takes a rev bump
  naming `memory/map/generated/symbols.json` (re-rendered) under Files touched and
  `codebase-map coverage + freshness` on its §7 leg line, and this unit re-renders the map once with
  `python tools/codebase-map/gen_map.py --write`. Observed by AC21.
- **S29** — Finding 31 (M17), on TOOL-dWellOiledMachine-81 AC3. Spec 81 takes a rev bump whose AC3
  payload carries `cwd` and `hook_event_name`, expects
  `payload-keys=cwd,error,hook_event_name,session_id,transcript_path`, and runs the recorder with
  `CLAUDE_PROJECT_DIR` unset. Observed by AC22.
- **S30** — Finding 32 (M18), on TOOL-dWellOiledMachine-90 S4, AC4 and -85 §6. Every salt fixture child
  runs with `GOV_SECRET_NODE_SALT`, `GOV_NODE_SALT` and every other `GOV_SECRET_*` variable removed
  from its environment; the rule is stated once in 85 §6 and cited by 90 S4, each by rev bump.
  Observed by AC23.
  **Readers:** by name: READER NOT IN TREE — the salt fixtures are TOOL-dWellOiledMachine-33's and -85's, unbuilt at HEAD. by value: NO VALUE READERS — the removed variables are read by no fixture child.
- **S31** — Finding 34 (L6), on TOOL-dWellOiledMachine-90 S23. S23's list gains
  `tools/template-size-highwater.txt:1`, the row keyed on `.claude/skills/unattended/SKILL.md`. Spec 90
  takes a rev bump. Observed by AC24.
- **S32** — Finding 35 (L7), on TOOL-dWellOiledMachine-84 §7. 84's leg line gains
  `python resolver (behaviour + inline parity + idiom ban)`, and S1 notes that TOOL-dPlacedRequest-11
  S8 registers the `gov_ref_sh` parity row. Spec 84 takes a rev bump. Observed by AC25.
- **S33** — Finding 40 (M19), on TOOL-dWellOiledMachine-82 S1, S2. `run_fragment_merges` compares the
  scratch table whenever the target holds one, whatever the settings file's state, and a probe whose
  `--unwire` exits non-zero records the fragment stale, never in `added`. Spec 82 takes a rev bump.
  Observed by AC26.
- **S34** — Finding 41 (M20), on TOOL-dWellOiledMachine-87 S2, S4. For a claim record, a missing
  `keepalive` key, or a missing or empty run-state `keepalive:` fact, refuses, as the `mine` rows do;
  the fleet-tag-and-session clause holds for non-claim records only. The `node-parity` matrix gains
  "record keepalive absent" and "run-state keepalive absent". Spec 87 takes a rev bump. Observed by
  AC27.
- **S35** — Finding 42 (M21), on TOOL-dWellOiledMachine-85 S2. A failed copy is not fatal:
  `read_node_salt` returns the old salt, prints once per process
  `commit keys — node salt read from <old name>; copy to node_salt failed: <cause>`, and retries the copy
  on the next call. `commit_keys.py --fixture` gains `--case unwritable-store`. Spec 85 takes a rev bump.
  Observed by AC28.
- **S36** — Finding 44 (M22), on TOOL-dWellOiledMachine-83 §6. Spec 83 takes a rev bump adding a
  criterion that drives the moved claim-push lock outside the waived suite: AC29 here. Observed by AC29.
- **S37** — Finding 21 (L5), on TOOL-dWellOiledMachine-80, -83, -85, -87 and -89. Citations re-pinned by
  rev bump: 80 §4 to `spec-78.md:35-42`, `:43-46` and `:117`; 85 §4 to `spec-79.md:373`; 89 §4 to
  `spec-78.md:35-38`; 83 S1 and Files touched to "two call sites" (`tools/unattended/unattended.sh:2403`,
  `:2444`). 87 §4's citations of `unattended.sh:2259` and `:2260-2261` are kept, as §4 records.
  Observed by AC30.

## 3. Non-goals (OUT)

- Every HIGH of the report: TOOL-dWellOiledMachine-91, -92 and -93, one unit each.
- The report's left-shift gates that are spec-set lints (verb resolution, pathspec resolution, citation
  ranges, caller lists): each finding here is closed by its own criterion, and a lint over specs is a
  separate mechanism (M2).
- No `rollback` verb, no `--digest` flag and no new `runtime.secret-home` value (S2, S5, S3).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-33` — AC7's stub store, named `fixture-store` (S3)
- **consumes-from** `TOOL-dWellOiledMachine-47` — S10's stub, which plants through a dated transcript (S25)
- **consumes-from** `TOOL-dWellOiledMachine-65` — AC2's and AC3's limit plants (S25)
- **consumes-from** `TOOL-dWellOiledMachine-72` — S3's stated limit, which reads an unparseable line as deleted (S24)
- **consumes-from** `TOOL-dWellOiledMachine-79` — S34's `harness-hooks` extractor and its table location (S17)
- **consumes-from** `TOOL-dWellOiledMachine-80` — the incomplete-claim arm, its plants, its reap line and its citations (S6, S8, S28, S37)
- **consumes-from** `TOOL-dWellOiledMachine-81` — S1's sentence, §10, AC3's payload and the symbol render (S22, S23, S28, S29)
- **consumes-from** `TOOL-dWellOiledMachine-82` — AC2's rollback and the stale probe's guards (S1, S2, S17, S33)
- **consumes-from** `TOOL-dWellOiledMachine-83` — the claim's layout, the factory's stale tests, the claim-push lock's criterion, the symbol render and the call-site count (S6, S7, S8, S28, S36, S37)
- **consumes-from** `TOOL-dWellOiledMachine-84` — the coverage case's population and exempt list, and §7's parity leg (S11, S12, S13, S32)
- **consumes-from** `TOOL-dWellOiledMachine-85` — the salt fixtures' store, AC3's verb, the copy's failure and the environment scrub (S3, S4, S5, S30, S35, S37)
- **consumes-from** `TOOL-dWellOiledMachine-86` — §5's security line (S24)
- **consumes-from** `TOOL-dWellOiledMachine-87` — the keepalive rule for claim records and the parity matrix (S34, S37)
- **consumes-from** `TOOL-dWellOiledMachine-88` — §5's security line (S24)
- **consumes-from** `TOOL-dWellOiledMachine-89` — S2's absent-claim branch and its plant, and §4's citation (S9, S10, S37)
- **consumes-from** `TOOL-dWellOiledMachine-90` — AC4, AC6, AC7, AC14, AC19, AC20, AC23, AC31, AC48, AC54 and AC55, S1, S4, S10, S22, S23, S48 and S54 (S3, S6, S14 to S21, S26 to S28, S30, S31)
- **consumes-from** `TOOL-dWellOiledMachine-91` — the freshness rule the re-pointed limit plants must satisfy (S25)
- **consumes-from** `TOOL-dWellOiledMachine-93` — the tree-wide re-render S26 records against spec 90

## 4. Design

### Evidence

Each finding's evidence is its row of the report's appendix, which its skeptic re-read and confirmed;
the items cite the clause they correct. Probes re-run for this spec at base `0689e7fa`:

- `govkit.py` has no `rollback` verb; `remove_wired_fragments` is called from `cmd_update` at
  `tools/govkit/govkit.py:11685` and from `tools/govkit/selftest.py:2369` (S1, S2).
- `run_fragment_merges` runs its probe only inside `if (target / settings).is_file():` and never reads
  the `--unwire` return code (`tools/govkit/govkit.py:6158-6176`) (S17, S33).
- `settings-merge.py` takes the settings path as a positional argument (`tools/settings-merge.py:1008`)
  and reads no `GOV_SETTINGS_JSON` (S16).
- `CLAIM_NS="refs/gov/runs"` and `CLAIM_CACHE="refs/gov/remote/runs"`
  (`tools/unattended/unattended.sh:2087-2088`); `git grep -ohE "refs/gov/[a-z-]+/?"` over the six
  locations of S11 prints `refs/gov/bar-red`, `refs/gov/remote/`, `refs/gov/runs` and `refs/gov/runs/`
  (S11, S12).
- The claim-push lock's external call sites are `tools/unattended/unattended.sh:2403` and `:2444`, two,
  not three (S37).
- **Where the report and the source disagree.** Finding 21 re-pins 87's `prior-session` read to
  `unattended.sh:2257` and the `mine` rows to `:2258-2259`. At this base and at this spec's HEAD,
  `fact "$rel" prior-session` is at `:2259` and the two `mine` rows at `:2260` and `:2261`, so 87's
  citations stand and S37 does not move them.
- The narrowed sidecar class hits, at this base, `tools/unattended/unattended.test.sh:8570` and `:8573`
  and `tools/unattended/stall-recorder.test.sh:3`, `:179`, `:264` and `:265`, beside the README,
  recorder and driver lines TOOL-dWellOiledMachine-34 S7 re-points (S18).
- `git grep -nE "['\"]python3?['\"]" -- 'tools/*.js'` prints `tools/hooks/scratch-guard.js:1206`,
  `:1318`, `tools/process-monitor/procmon-hook.js:117` and `tools/unattended/gate-guard.js:501` (S20).
- `tools/template-size-highwater.txt:1` keys `.claude/skills/unattended/SKILL.md` (S31).
- `memory/project/spawn-idiom-sites.txt:273-280` holds `resume-tick.sh`'s three rows and
  `resume-tick.test.sh`'s five (S27).
- TOOL-dPlacedRequest-11 S8 adds the `gov_ref_sh` parity row to `tools/lib/resolve-python.test.sh`
  (`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-11.md:81-82`) (S32).
- `codebase-map coverage + freshness` carries no guard in `tools/gate-legs.json`, and
  `memory/map/generated/symbols.json` lists `claim_push_lock` functions three times today (S28).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `fixture-store` | `commit_keys.py --fixture` backend | none |
| `unwritable-store` | `commit_keys.py --fixture` case | none |
| `claim-is-file`, `factory-claim-complete` | `supervise.py --fixture` plants | none |
| `table-no-settings`, `corrupt-table`, `relocated-settings-probe` | `tools/govkit/selftest.py` cases | none |
| `crlf-hashed-lines` | `tools/runlog/selftest.py` case | none |

### Files touched (estimate)

- `tools/govkit/govkit.py`, `tools/govkit/selftest.py`
- `tools/codebase-map/map_extractors.py`
- `tools/runtime/commit_keys.py`, `tools/runtime/supervise.py`, `tools/runtime/resume-tick.sh`,
  `tools/runtime/limits_fixture.py`, `tools/runtime/stall-recorder.test.sh`
- `tools/memory-tree/door_fixture.py`, `tools/memory-tree/gov_record.py`
- `tools/runlog/selftest.py`
- `memory/project/spawn-idiom-sites.txt`, `tools/template-size-highwater.txt`
- `memory/map/generated/symbols.json` (re-rendered)
- the rev bumps of specs 33, 47, 65, 72, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89 and 90 under
  `memory/builds/dWellOiledMachine/spec/`

### Alternatives rejected

- **Two batches split by kit.** The fixes meet in spec 90's, 85's and 83's files and in
  `commit_keys.py` (§1), so the halves would share write paths and M6 forbids running them together.
- **A `file-fixture` value of `runtime.secret-home` (S3).** The finder's first option; it adds a secret
  home a policy could select outside a fixture, a wider surface than an injected stub.
- **`owner` holding the pid, image and stamp (S6).** The skeptic's other option; it makes the release
  token and the liveness record one string, so a reader of one parses the other's grammar.

## 5. Production-readiness checklist

- security — S3 and S30 keep every salt fixture off the real keychain and off an inherited salt; S11 to
  S13 make the door's coverage case a true deny-by-default inventory; S34 restores the `mine` row's
  keepalive bound in the door.
- perf / scale — none beyond one more file compare in the stale probe (S33).
- error / empty / loading states — S9 reaches the absent-claim branch; S33 makes a failed probe and an
  absent settings file safe; S35 makes a failed salt copy non-fatal.
- observability — S8's reap line prints from a named site; S35's notice names the cause.
- risks — the criteria these findings name on units 80 to 90 stand answered by this unit's criterion of
  the same finding, which the builder re-runs after this unit's rev bumps.
- testing — AC1 to AC30 and the arms in §7.
- migration — none: no record or store moves.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

- **AC1** — When the `shared-event-rewire` fixture case, on its §7 `New arm:` line, calls
  `remove_wired_fragments` on the update's `added` set, B's rows and A's original rows stay in the
  table, and `grep -c "govkit.py rollback" 2026-10-27-spec-TOOL-dWellOiledMachine-82.md` prints 0.
  Red when: the rollback unwires A's pre-existing rows, or a `rollback` verb is spelled.
- **AC2** — When `python commit_keys.py --fixture --case seeded-old-salt` runs, the
  `fixture-store` file holds `ab` under `node_salt` afterwards, and `grep -c "fixture-store"` over
  specs 85, 90 and 33 prints 1 or more for each.
  Red when: a writing salt case names `env-injected` or the real keychain.
- **AC3** — When `grep -c "commit_keys.py --digest" 2026-10-27-spec-TOOL-dWellOiledMachine-85.md` runs, it prints 0,
  and `python commit_keys.py digest s1` under the fixture prints the new name's digest.
  Red when: the flag spelling remains.
- **AC4** — When `python supervise.py --fixture --plant factory-claim-complete` takes a
  claim through `write_node_lock`, writes `pid`, `image` and `stamp` for a live tick and ages it three
  minutes, the next tick keeps it and prints `starting elsewhere`; when `--plant torn-claim` takes the
  claim the same way and writes `stamp` as `garbage`, the next tick prints
  `claim reaped · incomplete` and starts one supervisor.
  Red when: a factory-made claim reads incomplete, a live tick's claim is reaped, or no reap line
  prints.
- **AC5** — When `grep -n "write_node_lock"` runs over specs 80 and 90, it prints 80's AC2 plant and
  90's AC19 plant, and `grep -c "never .owner." 2026-10-27-spec-TOOL-dWellOiledMachine-83.md` prints 1
  or more.
  Red when: a plant still writes a layout the production writer does not.
- **AC6** — When `--plant claim-is-file` runs, the tick prints `not started · claim` naming the claim
  and never `starting elsewhere`; with 89 S2's absent-claim arm deleted, it prints `starting elsewhere`.
  Red when: a failure with no claim directory is reported as a rival.
- **AC7** — When `python door_fixture.py --case namespace-coverage` runs, it prints no
  unmatched ref and lists the exempt set `refs/gov/bar-red`, `refs/gov/remote/`, `refs/gov/waits/`,
  `refs/gov/checkpoints/` and `refs/gov/conform/` with their reasons; with `refs/gov/remote/` dropped
  from the exempt list it prints `refs/gov/remote/`.
  Red when: a ref the tools write is neither matched nor exempt.
- **AC8** — When `git grep -nE "\[\"bash\"|\['bash'" -- 'tools/**/*.py'` runs, it prints nothing, and the
  same pattern over a scratch copy of `supervise.py` holding `['bash', 'x']` prints it.
  Red when: the pathspec matches no file and a bare `bash` argv passes.
- **AC9** — When `grep -cE "replay claude-code-2[.]1[.]292([^/]|$)"` runs over specs 90, 67 and 79, each
  prints 0, and `python conformance.py run --replay tools/runtime/fixtures/conformance/claude-code-2.1.292/`
  writes the `prompt-submit` row marked `synthetic`.
  Red when: the bare-name spelling remains.
- **AC10** — When `python settings-merge.py` runs on a settings file under a `config` directory with
  `--fragment <f>` from a scratch target root, the table is written at the root's own `hook-packs.json`
  and none appears beside the settings file.
  Red when: the table follows the settings path.
- **AC11** — When the `relocated-settings-probe` case runs a govkit update with
  `GOV_SETTINGS_JSON` naming a `config` settings file, the live `hook-packs.json` hashes the same before and
  after the probe, `shared-event-rewire` returns an empty `added`, and
  `grep -cE "beside the settings|places beside it"` over specs 82 and 79 prints 0.
  Red when: the probe changes the live table, or a reader still looks beside the settings file.
- **AC12** — When `git grep -nE "stall\.[^ ]*\.log|'stall'.*\.log" -- tools/runtime tools/unattended`
  runs, it prints only the allowed rows S18 names.
  Red when: an unnamed reader of the retired sidecar remains.
- **AC13** — When spec 90's rewritten AC31 runs under a `machine` binding, the card replays, the commit
  carries `Gov-*` trailers, `manifest-check.sh --card --write` prints the map extra,
  `read_session_node` returns the owner-equivalent node, and the orientation gate still asks for a card;
  `grep -c "any of the five readers" 2026-10-27-spec-TOOL-dWellOiledMachine-90.md` prints 0.
  Red when: one reader's arm is dropped, or orientation exempts `machine`.
- **AC14** — When `git grep -nE "['\"]python3?['\"]" -- 'tools/*.js'` runs, it prints only the three
  rows S20 names.
  Red when: `procmon-hook.js` still spawns a bare `python`.
- **AC15** — When `grep -cE "(^|[^/])runtime[.]md" 2026-10-27-spec-TOOL-dWellOiledMachine-90.md` runs, it
  prints 0, and 90's AC14 command prints a count for each of its two files.
  Red when: a bare `runtime.md` remains and the grep errors instead of counting.
- **AC16** — When `grep -c "renderUtc(new Date(resetsAt" 2026-10-27-spec-TOOL-dWellOiledMachine-81.md`
  runs, it prints 1 or more, the §10 line naming `renderUtc` included.
  Red when: S1 still reads the clause with no verb.
- **AC17** — When the `crlf-hashed-lines` fixture case, on its §7 `New arm:` line, runs,
  `runlog.py verify <record>` prints `mismatch` and exits 1, and `grep -c "read as deleted"` over specs
  72, 86 and 88 prints 1 or more for each.
  Red when: a CRLF rewrite of the hashed lines verifies `pruned`.
- **AC18** — When `python supervise.py --fixture --plant limit` runs, the beat journals
  `limit-hold` naming a reset an hour ahead; `python limits_fixture.py --case hold-ceiling`
  reaches `hand-over — fx`; and `git grep -n resetsAt -- tools/runtime tools/unattended` names only
  `stall-recorder.js` and the fixture.
  Red when: a plant yields `reset=none`, or a planter spells `resetsAt`.
- **AC19** — When `python tools/memory-tree/gen_build_index.py --check` runs after this unit's rev
  bumps, it exits 0.
  Red when: a README this build's render changed is left stale.
- **AC20** — When `grep -c "^tools/unattended/resume-tick" memory/project/spawn-idiom-sites.txt` runs, it
  prints 0, and the same for every old path of 28 S1 and S4.
  Red when: a moved suite's rows still key its old path.
- **AC21** — When `python tools/codebase-map/gen_map.py --check` runs, it exits 0, and
  `grep -c "symbols.json"` over specs 80, 81, 83 and 90 prints 1 or more for each.
  Red when: the symbol render is stale or a spec omits it.
- **AC22** — When `stall-recorder.js` runs on a bound fixture payload carrying `cwd` and
  `hook_event_name` with `CLAUDE_PROJECT_DIR` unset, and again with it set to an unrelated directory,
  both runs journal `payload-keys=cwd,error,hook_event_name,session_id,transcript_path`.
  Red when: the binding depends on the ambient project directory.
- **AC23** — When `python commit_keys.py --fixture --case env-salt` runs its unset arm with
  `GOV_NODE_SALT=zz` exported in the parent, it refuses.
  Red when: the fallback reads the inherited old variable and a digest prints.
- **AC24** — When `grep -n "template-size-highwater.txt:1" 2026-10-27-spec-TOOL-dWellOiledMachine-90.md`
  runs, it prints S23's line.
  Red when: the high-water row is left on the old path.
- **AC25** — When `grep -c "python resolver (behaviour + inline parity + idiom ban)" 2026-10-27-spec-TOOL-dWellOiledMachine-84.md`
  runs, it prints 1 or more.
  Red when: 84's leg line omits the leg that observes S1's byte-identity.
- **AC26** — When the `table-no-settings` and `corrupt-table` fixture cases, on their §7 `New arm:` line, run,
  each returns an empty `added`.
  Red when: a target with a table and no settings, or a failed `--unwire`, records the fragment as
  added.
- **AC27** — When `python door_fixture.py --case node-parity` runs, its rows
  "record keepalive absent" and "run-state keepalive absent" both refuse in the door and in
  `check_claim_writable`.
  Red when: the door admits a claim record the `mine` row refuses.
- **AC28** — When `python commit_keys.py --fixture --case unwritable-store` seeds an old
  salt in a store that refuses writes, the digest is the HMAC under the old salt and the notice names
  `copy to node_salt failed`.
  Red when: the failed copy fails the digest.
- **AC29** — When `grep -n "write_node_lock" tools/unattended/unattended.sh` runs, the claim-push call
  site passes `$((EPOCHSECONDS + REMOTE_BOUND + 10))` and the stem `claim-push`; and a `bash -c` probe
  that sources `tools/unattended/lib-unattended.sh`, plants a `claim-push.lock` whose `until` has passed
  in a scratch git common dir and calls `write_node_lock` with those arguments returns 0, writes an
  `until` within one second of now plus `REMOTE_BOUND` plus 10, and leaves a health event
  `claim-push-lock-broken`; with the default stale function unbound it returns 1.
  fixture: a scratch git repository under `%TEMP%/<short-name>`.
  Red when: the moved lock is mis-parameterised and the probe still passes.
- **AC30** — When `grep -c "spec-78.md:35-42"` over spec 80, `grep -c "spec-79.md:373"` over spec 85 and
  `grep -c "spec-78.md:35-38"` over spec 89 each print 1 or more, and `grep -c "three call sites"` over
  spec 83 prints 0.
  Red when: a re-pinned citation still lands on the wrong lines.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `recall floor` · `recall floor arms` · `unattended kit gate` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/govkit/selftest.py · covers AC1 AC11 AC26 · the cases staged against a probe that skips the table without a settings file and ignores the `--unwire` exit · none
New arm: tools/runtime/commit_keys.py · covers AC2 AC23 AC28 · the salt cases staged against a fixture writing `env-injected`, inheriting `GOV_NODE_SALT` and failing on a refused copy · none
New arm: tools/runtime/supervise.py · covers AC4 AC6 AC18 · the plants staged against a claim with no `pid` written after the factory, the absent-claim arm deleted and a payload-planted limit · none
New arm: tools/memory-tree/door_fixture.py · covers AC7 AC27 · the cases staged against an exempt list of `refs/gov/bar-red` alone and a door admitting an absent keepalive · none
New arm: tools/runlog/selftest.py · covers AC17 · the CRLF case staged against a head rule that reads an all-unparseable file as empty · none
New arm: tools/runtime/stall-recorder.test.sh · covers AC22 · the payload case staged with `cwd` dropped and `CLAUDE_PROJECT_DIR` set to the live checkout · none

## 8. Open questions

- **F1 — Which test store do the salt fixtures write?** (a) an injected `fixture-store` stub reachable
  only under `--fixture`; (b) a `file-fixture` value of `runtime.secret-home`; (c) the OS keychain
  under a scratch service name. (b) adds a secret home any policy could select, a wider surface than
  the unit priced; (c) writes the real keychain, which 85 §5 and 90 S4 forbid. (a) makes every write
  criterion runnable and adds no surface. RESOLVED (agent, 2026-10-27, delegated): (a). widens: none ·
  relaxes: none
- **F2 — Which file carries the start claim's liveness record?** (a) `pid`, `image` and `stamp` written
  by the tick after `write_node_lock` returns 0, `owner` a release token only; (b) `owner` holding
  `<pid> <image> <stamp>`, parsed by the stale test. (b) joins the release compare and the liveness
  read into one string and changes the factory's `owner` contract shared with the claim-push lock. (a)
  keeps 78 S3's and 90 S19's record as written and the factory unchanged. RESOLVED (agent, 2026-10-27,
  delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the round-2 promotions audit's 37 medium and low findings
  batched.

## 10. Reuse audit

Each item extends the seam its finding names: `remove_wired_fragments` and `run_fragment_merges`
(S1, S17, S33), `read_secret_ref`'s injected backend (S3, S30, S35), `write_node_lock` and 78 S3's
record (S6 to S8, S36), `door_fixture.py`'s cases (S11 to S13, S34), the runlog selftest (S24), the
stall fixture transcript (S25), `gen_build_index.py` and `gen_map.py` (S26, S28), and
`renderUtc` (S22, S23). The probe `python tools/codebase-map/reuse_lookup.py "batch the round-2
promotions audit minor findings"` ranked `audit` and three `find`-stem builders, none a fix's seam, so
the seams are the per-item ones above; the recall query below ranked TOOL-dWellOiledMachine-90 and -79
first, the two earlier batches whose shape this unit follows. No item mints a module.

Recall terms used: `python tools/memory-recall/query.py "how are the round-2 spec audit's medium and
low findings batched" --terms "minors batch spec audit medium low promoted findings fixture-store claim
layout namespace coverage symbols render"`
