# TOOL-dWellOiledMachine-79 — the spec audit's 49 medium and low findings, batched: capability rows, pack shapes, launch environment, registries, renders and the records that miscount

**Status:** DEFERRED · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 63 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-79-deviation-791.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-79-deviation-791.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
exited BOUNDED with 49 confirmed findings below HIGH. BUILD-METHOD M4 promotes every one of them,
batched into ONE unit, and this is that unit. It closes, by report id:

- MEDIUM (37): 4, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 30, 31, 32, 33, 39, 41, 42,
  45, 48, 51, 52, 53, 54, 55, 56, 57, 61, 65, 66, 67, 69, 70.
- LOW (12): 22, 23, 24, 25, 26, 27, 36, 37, 40, 43, 44, 58. Findings 27 and 43 are one report item,
  L6, and each keeps its own scope item here.

Each finding takes the fix its skeptic judged SOUND, or the skeptic's corrected fix where the report
marks the finder's UNSOUND (findings 12, 37, 39, 67). The findings land on many units, so this unit
repairs none in particular and sits after every unit of the build. One unit, not two: the write sets
of the 49 fixes meet in `tools/gate-legs.json`, `tools/runtime/kit.toml`, `tools/runtime/harness.py`
and the claude-code capability table, so no split into two disjoint halves exists under M6.

## 2. Scope (IN)

Each item names its finding and the unit or spec it lands on. "Spec N takes a rev bump" means spec N
is amended at this unit's pass, its §9 line naming this unit and the finding.

- **S1** — Finding 4 (M1), on TOOL-dWellOiledMachine-36. `derive_conformance_rows`
  (`tools/runtime/conformance.py`) measures `prompt-submit`: the live arm's scratch repository gains a
  `UserPromptSubmit` probe hook logging its payload, and the row reads `yes` when the probe fired with
  the prompt field, else `no`, through the one derivation the replay arm shares. Observed by AC1.
- **S2** — Finding 7 (M2), on TOOL-dWellOiledMachine-12 S10 and -23 S6. `reattach-cap-bytes` and
  `session-start-output-cap` join `CAPABILITY_NAMES` (`tools/runtime/harness.py`); the
  `reattach-cap-bytes` row is written `unmeasured`, its documented figure kept as a pinned comment
  beside `CARD_CAP_BYTES` in `tools/runtime/session_binding.py`, where 12 S10 already reads a missing
  row as `CARD_CAP_BYTES` alone. Observed by AC2.
- **S3** — Finding 8 (M3), on TOOL-dWellOiledMachine-10 S5. check-wiring's session arm reads the
  `on-failure` row through `python <runtime>/harness.py --read claude-code on-failure <version>`, a
  verb `harness.py` gains over `read_capability`, and prints
  `hook-failure — closed · onFailure ignored by <version>` when it reads `no` or `unmeasured`.
  Observed by AC3.
- **S4** — Finding 9 (M4), on TOOL-dWellOiledMachine-11 S6. `enqueue_commit`
  (`tools/runtime/commit_queue.py`) calls `check_act_ready <act>` first for a commit bound to an act and
  refuses `commit — refused · <act> · session pending`. The binding writer is not gated: the binding
  never holds a session id (TOOL-dWellOiledMachine-39), so its readiness is not the act's. Observed by
  AC4.
- **S5** — Finding 10 (M5), on TOOL-dWellOiledMachine-33 S1, S2. `derive_gov_trailers`
  (`tools/runtime/commit_keys.py`) takes `Gov-Item` and `Gov-Session` from the act record
  (TOOL-dWellOiledMachine-32 S2, its `item` and `session`) and `Gov-Unit` from the act's named call
  (TOOL-dWellOiledMachine-7 S1), never from the binding, which carries neither. Observed by AC5.
- **S6** — Finding 11 (M6), on TOOL-dWellOiledMachine-35 S1, S2. `tools/runtime/session_node.py` joins
  an act record on its `session` field (committed `Session`), never `harness-session`, and names the
  minter `derive_act_id`. Observed by AC6.
- **S7** — Finding 12 (M7), on TOOL-dWellOiledMachine-33 S6, the skeptic's corrected fix.
  `read_node_salt` reads the salt through `read_secret_ref("node_salt")`
  (`tools/runtime/secret_scan.py`, TOOL-dWellOiledMachine-17 S4), so it resolves env
  `GOV_SECRET_NODE_SALT`, target `gov:node_salt` and libsecret `name node_salt`; first use creates it
  through a new `write_secret_ref(name, value)` in `secret_scan.py` under the same grammar; 33 S6's
  `CredReadW`, `CredWriteW` and `secret-tool` calls are deleted. Observed by AC7.
  **Readers:** by name: READER NOT IN TREE — `commit_keys.py`, `read_node_salt` and `GOV_NODE_SALT` are
  TOOL-dWellOiledMachine-33's, unbuilt at HEAD, re-pointed here. by value: `write_binding`'s caller, which passes the
  salt-derived digest (TOOL-dWellOiledMachine-39 S1), unchanged in form.
- **S8** — Finding 13 (M8), on TOOL-dWellOiledMachine-8 S3, S4. The returns pack becomes class `refuse`
  with one refusal row `return-unusable` (actor `self`, `remedy-call` `none`, remedy "end with one
  StructuredOutput within the return cap"); a hold prints `{"decision":"block","reason":…}` ending
  `rule — return-unusable` on stdout, which holds a `SubagentStop`, where exit 2 of a `record` pack
  never could. The count of holds and the refusal at `roles.retries` stand. Observed by AC8.
- **S9** — Finding 14 (M9), on TOOL-dWellOiledMachine-8 AC4. Spec 8 takes a rev bump re-pointing AC4
  at S29's parity row, whose population is derived by the row, never a pinned `5 file(s)`. Observed by
  AC9.
- **S10** — Finding 16 (M10), on TOOL-dWellOiledMachine-60 S7. `run_build_push` fences on the lease the
  pushing session holds: `--lease fence unit <slug> <unit>` for a `gov/<slug>/<unit>` branch, the build
  lease otherwise, so a unit holder's push is fenced on its own unit lease. Observed by AC10.
- **S11** — Finding 17 (M11), on TOOL-dWellOiledMachine-42 AC1. Spec 42 takes a rev bump whose AC1
  grep excludes `tools/roles/kit.toml`'s `[[upgrade]]` row and its step program, the two places 42 S5
  writes `gov-session`. Observed by AC11.
- **S12** — Finding 18 (M12), on TOOL-dWellOiledMachine-16 S3. `JOURNAL_CLASSES`
  (`tools/runtime/journal.py`) drops `secret-hit`, `deadline-passed`, `cycle` and `budget-spent`, which
  no unit writes; spec 16 takes a rev bump dropping them from S3 and §3. Observed by AC12.
  **Readers:** by name: READER NOT IN TREE — `journal.py` and its `JOURNAL_CLASSES` are TOOL-dWellOiledMachine-16's,
  unbuilt at HEAD; spec 47's §3 edge naming the class is re-worded at this pass. by value: NO VALUE READERS — no line of the four classes
  is ever written, so no reader counts one.
- **S13** — Finding 19 (M13), on TOOL-dWellOiledMachine-1's `runtime selftest` leg.
  `tools/runtime/selftest.py --modules` runs `python <m> --fixture` for every tracked
  `tools/runtime/*.py` whose source defines a `--fixture` flag, prints one line per module and refuses
  an empty population, and `--modules --list` prints that population without running it; the `runtime selftest` leg runs it, and `tools/run-gates/selftest-budgets.txt`
  gains its row. Observed by AC13.
- **S14** — Finding 20 (M14), on TOOL-dWellOiledMachine-37 S4. `launch_act` adds, after
  `derive_launch_env`'s filter, `GOV_ACT` (the act it minted), `GOV_SESSION_KIND`, `GOV_RETURN_KEY`
  where the work order carries one, and `GIT_COMMITTER_NAME` and `GIT_COMMITTER_EMAIL` from
  `derive_act_identity` (TOOL-dWellOiledMachine-39 S3). Observed by AC14.
- **S15** — Finding 21 (M15), on TOOL-dWellOiledMachine-14 AC4. The govkit fixture plants its capability
  table in the scratch target's copy of the runtime kit, and spec 14 takes a rev bump dropping
  `GOV_HARNESS_TABLES` from AC4, so no undefined override is named. Observed by AC15.
- **S16** — Finding 22 (L1), on TOOL-dWellOiledMachine-40 AC3. The commit queue's fixture pushes from
  clone `na` while `na` holds `push-main-active` and a 60-second stub bar runs, and requires the push to
  finish within 10 s printing `decision skip-nondefault`; spec 40 takes a rev bump so stated. Observed
  by AC16.
- **S17** — Finding 23 (L2), on TOOL-dWellOiledMachine-23 S5. The session-start fallback in
  `manifest-check.sh` prints `next — none · unanswered · next verb did not answer in 10s`, unit 2's
  fence shape; spec 23 takes a rev bump so stated. Observed by AC17.
- **S18** — Finding 24 (L3), on TOOL-dWellOiledMachine-32 S7. The `act` row of
  `tools/memory-tree/record-kinds.toml` carries `tag = "record.act"`. Observed by AC18.
- **S19** — Finding 25 (L4), on TOOL-dWellOiledMachine-1 AC6. Spec 1 takes a rev bump making AC6 expect
  S3's unquoted `launch — refused · runtime.spawn-backend remote ·`. Observed by AC19.
- **S20** — Finding 26 (L5), on TOOL-dWellOiledMachine-13 AC4. `cadence.py` gains the verb
  `period <kind> --at <utc>`, printing `derive_period`'s key. Observed by AC20.
- **S21** — Finding 27 (L6, with 43), on TOOL-dWellOiledMachine-17 §4. Spec 17 takes a rev bump naming
  TOOL-dWellOiledMachine-55 S7, not unit 20, as the builder of `check_value`'s registry arm. Observed
  by AC21.
- **S22** — Finding 30 (M16), on TOOL-dWellOiledMachine-10 S14. The lander compares `core.hooksPath`
  with the trusted copy after normalising both through one function, `derive_abs_dir` in
  `tools/push-main.sh`: `cd` and `pwd -W` where the shell has it, else `pwd`, so `C:\…`, `C:/…` and
  `/c/…` spellings of one directory compare equal. Observed by AC22.
- **S23** — Finding 31 (M17), on TOOL-dWellOiledMachine-4 S1 to S3. `write_intake` writes bytes,
  `text.encode("utf-8")`, and `read_intake` reads bytes and decodes, so a prompt's newlines are stored
  as typed on every node. Observed by AC23.
- **S24** — Finding 32 (M18), on TOOL-dWellOiledMachine-1 S4. The spike's live arm
  (`tools/runtime/spike.py`) launches each case under an environment carrying none of
  `policy.SETTINGS_VARS`, `CLAUDE_PROJECT_DIR`, the `CLAUDE_CODE_*` keys or the `MESSAGING_*` keys,
  the filter `run_live_session` applies, and records the child's environment keys in each case's
  `case.toml`. Observed by AC24.
- **S25** — Finding 33 (M19), on TOOL-dWellOiledMachine-37 S4. Every `LAUNCH_ENV_ALLOW` entry is spelled
  upper case and the filter compares names upper-cased, so `SYSTEMDRIVE` survives on Windows. Observed
  by AC25.
- **S26** — Finding 36 (L7), on TOOL-dWellOiledMachine-10 §4. Spec 10 takes a rev bump reading
  "13 commands across 6 events". Observed by AC26.
- **S27** — Finding 37 (L8), on TOOL-dWellOiledMachine-15 §4, the skeptic's corrected fix. Spec 15 takes
  a rev bump stating that no clock-offset correction code exists, and that
  `git grep -i -n "skew\|clock offset\|remote time" -- tools .githooks` hits only comments about other
  skews: kit-version skew in check-wiring, runner and table skew in run-gates, blame-time skew in
  drift-audit, and commit-time windows in runlog. Observed by AC27.
- **S28** — Finding 39 (M20), on TOOL-dWellOiledMachine-11 S6, -45 S2 and -9 §8 F1, the skeptic's
  corrected fix. One arrival-order ticket queue, `tools/runtime/tickets.py` with `add_ticket`,
  `read_queue` and `remove_ticket`, extracted from `commit_queue.py`; `commit_queue.py` and
  `slots.py` both use it and keep no ticket code of their own. The bash turnstile in `run-gates.sh`
  stays separate. Specs 9 and 11 take rev bumps correcting F1 and F3 to name what each unit does.
  Observed by AC28.
  **Readers:** by name: READER NOT IN TREE — `commit_queue.py` and `slots.py` are TOOL-dWellOiledMachine-11's and -9's,
  unbuilt at HEAD, their own ticket functions deleted and re-pointed here. by value: NO VALUE READERS —
  the queue order is held by one process and read by no other.
- **S29** — Finding 40 (L9), on TOOL-dWellOiledMachine-8 S9. `PARITY_ROWS`
  (`tools/lib/resolve-python.test.sh:167-186`) gains the row
  `gov_returns_js|$ROOT/<runtime>/returns-block.js|<runtime>/returns-block`, and `blk()` and the copy
  glob widen to a `// >>>` marker and `*.js`. `returns.py --check-block` and the leg
  `runtime returns block parity` are deleted. Observed by AC29.
  **Readers:** by name: `tools/gate-legs.json` (the leg's row) and READER NOT IN TREE for `returns.py`
  (`--check-block`), TOOL-dWellOiledMachine-8's, unbuilt at HEAD, each removed here. by value: NO VALUE READERS — the leg's verdict is read only by
  the runner.
- **S30** — Finding 41 (M21), on TOOL-dWellOiledMachine-23 S6. `derive_conformance_rows` gains a
  `session-start-output-cap` case (live: a scratch repository whose SessionStart hook prints a
  32768-byte map; replay: a recorded transcript under `tools/runtime/fixtures/conformance/`), written
  through 36 S4's `--write`; `tools/runtime/measure_hook_cap.py` is deleted. Observed by AC30.
  **Readers:** by name: `tools/gate-legs.json`, and READER NOT IN TREE for the runtime kit's descriptor,
  its hook-cap fixtures leg and the conformance module, TOOL-dWellOiledMachine-1's, -23's and -36's,
  unbuilt at HEAD, each removed or re-pointed to the conformance module. by value: NO VALUE READERS —
  the session-start cap is read through `read_capability`, unchanged in form.
- **S31** — Finding 42 (M22), on TOOL-dWellOiledMachine-10 S6, -12 S3, -16 S4 and -24 S1. Every Python
  run from a pack or a JavaScript producer goes through `bash <prefix>/runtime/pyrun.sh <script>`
  (TOOL-dWellOiledMachine-8 S3): `dispatch.js`'s `hook-failure` write, the session-binding fragment's
  command, the JavaScript journal producers and `map-reads.js`. Observed by AC31.
- **S32** — Finding 43 (L6, with 27), on the `§3` edges of specs 57, 4, 13, 29 and 17. Each of specs
  57, 4, 13 and 29 takes a rev bump re-pointing its `scan_secrets` consumes-from edge to
  TOOL-dWellOiledMachine-16 (`redaction.py`), spec 16 takes a rev bump adding the four hands-off
  mirrors, and spec 17 takes a rev bump dropping its four `scan_secrets` hands-off rows, keeping
  `scan_values` and `read_secret_ref`. Observed by AC32.
- **S33** — Finding 44 (L10), on TOOL-dWellOiledMachine-14 §10. Spec 14 takes a rev bump reading
  `resolve_tokens` (`:1233`) and `target_context` (`:1436`). Observed by AC33.
- **S34** — Finding 45 (M23), on TOOL-dWellOiledMachine-10 S3. `map_extractors.py`'s `harness-hooks`
  extractor reads `.claude/hook-packs.json` beside the settings file, keying each pack as
  `<event> <its hook script>` as it keys a settings hook today, so the five dossiers' claims stay
  live; the generated map is re-rendered. Observed by AC34.
- **S35** — Finding 48 (M24), on TOOL-dWellOiledMachine-34 S8. The four suites reading the health log
  at its old home by TAB position, `tools/run-gates/run-gates.test.sh`,
  `tools/run-gates/run-gates.turnstile.test.sh`, `tools/runtime/resume-tick.test.sh` and
  `tools/process-monitor/selftest.py`, read through `journal.py read --producer health`. Observed by
  AC35.
- **S36** — Finding 51 (M25), on TOOL-dWellOiledMachine-28 S4. `check-unattended.sh` drops its check-36
  exemption row for `resume-tick.sh` (`:4862`) and its check-32 scan of `$HERE/resume-tick.sh`
  (`:5779`), the moved files having left both populations, and says so in each check's comment.
  Observed by AC36.
  **Readers:** by name: `tools/unattended/check-unattended.sh`, the one file spelling both rows,
  edited here. by value: NO VALUE READERS — the rows feed only those two checks.
- **S37** — Finding 52 (M26), on TOOL-dWellOiledMachine-28 §4. `memory/project/spawn-idiom-sites.txt`
  and `memory/project/substitution-fed-loops.txt` re-key every row naming a moved file to
  `tools/runtime/`, re-counting `resume-tick.sh`'s rows for the forwarder. Observed by AC37.
- **S38** — Finding 53 (M27), on TOOL-dWellOiledMachine-28 §7. Spec 28 takes a rev bump adding
  `routed-commits selftest` to its leg line. Observed by AC38.
- **S39** — Finding 54 (M28), on TOOL-dWellOiledMachine-1 S1. `WIRE-INTO-PROJECT.md` gains a runtime-kit
  adoption section naming `<prefix>/runtime/`, its adopter and the packs it wires. Observed by AC39.
- **S40** — Finding 55 (M29), on the legs specs 1, 2, 8, 11, 12, 20, 23 and 39 add.
  `tools/runtime/kit.toml` carries a `[[gate_leg]]` row per runtime leg in `tools/gate-legs.json`,
  `tools/govkit/subject-pins.tsv` is re-written by `govkit.py selfcheck --write`, and
  `memory/map/features/runtime.md` claims each leg under `gate-legs`. Observed by AC40.
- **S41** — Finding 56 (M30), on the catalogue edits of specs 1, 37, 44, 55 and 56.
  `.governance/policy.json` is re-rendered by `python tools/policy/policy.py mirror --write` after the
  last of them. Observed by AC41.
- **S42** — Finding 57 (M31), on TOOL-dWellOiledMachine-12 §5 and -23 §5. The two paragraphs those
  units add to `skills/session-kickoff/SKILL.md` move to `help/runtime.md`, each leaving one pointer
  line, so the file is at or under its 18432-byte cap. Observed by AC42.
- **S43** — Finding 58 (L11), on TOOL-dWellOiledMachine-2 S9. `tools/unattended/SKILL.template.md`
  folds the `--status` sentence into the `next.py` read, and its render
  `.claude/skills/unattended/SKILL.md` is at or under 10240 bytes. Observed by AC43.
- **S44** — Finding 61 (M32), on TOOL-dWellOiledMachine-4 S5. `intake.py hook` exits 1, a failed pack,
  when stdin does not parse or carries no `prompt` or no `session_id` key; only a present empty prompt
  writes nothing and exits 0. Observed by AC44.
- **S45** — Finding 65 (M33), on TOOL-dWellOiledMachine-45 S8. settings-merge renders each dispatcher
  entry's `timeout` as the sum of its packs' `budget-ms`, in seconds, plus 10, since the dispatcher
  runs them in sequence. Observed by AC45.
- **S46** — Finding 66 (M34), on TOOL-dWellOiledMachine-10 §4. The decision table and `dispatch.js`
  gain rows: `UserPromptSubmit`, refused by exit 2 or `{"decision":"block"}`, emitted unchanged, its
  `additionalContext` joined; `PostToolUse`, record and context only; `StopFailure` and `SessionEnd`,
  record only. Spec 10 takes a rev bump adding them. Observed by AC46.
- **S47** — Finding 67 (M35), on TOOL-dWellOiledMachine-58 S2 and -57 S2, the skeptic's corrected fix.
  57's token-shape scan runs on every `write_gov_ref` under `refs/gov/`, with an exempt list naming
  `refs/gov/bar-red` and its reason; 58's session rule extends to `refs/gov/life/` and
  `refs/gov/attendance/`; `refs/gov/bindings/` and `refs/gov/decisions/` take the fleet-tag rule (the
  writer's node equals the record's `node`), which admits the sessionless supervisor as
  TOOL-dWellOiledMachine-63's node writer does. Observed by AC47.
- **S48** — Finding 69 (M36), on TOOL-dWellOiledMachine-6 S4. On a non-zero `write_binding` the
  supervisor launches nothing, journals `act-launch` with `binding=failed <GOVREF_WHY>`, releases the
  act's slot reservation, and retries at a later beat. Observed by AC48.
- **S49** — Finding 70 (M37), on TOOL-dWellOiledMachine-43 S2, S3. An unmeasured or absent
  `hook-hold-seconds` row reads as a hold of 0: the call is denied at once with the
  `admission — waiting` notice and the case is journaled, so the limit is never passed by a crash.
  Observed by AC49.

## 3. Non-goals (OUT)

- Every BLOCKER and HIGH of the report: TOOL-dWellOiledMachine-63 to -78, one unit each.
- The report's left-shift gates that are spec-set lints (a capability-coverage lint, a field-source
  lint, a pinned-count lint and their kin): each finding here is closed by its own criterion, and a
  lint over specs is a separate mechanism (M2).
- Re-measuring the spike's rows after S24: the code path is fixed and observed with a stub; a paid
  live run is the next measurement's.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-1` — `launch.py`, `spike.py`, `selftest.py` and the `runtime selftest` leg (S13, S14, S24, S39, S40)
- **consumes-from** `TOOL-dWellOiledMachine-2` — the unattended Skill template's `next.py` read (S43) and its leg (S40)
- **consumes-from** `TOOL-dWellOiledMachine-4` — `intake.py`'s writer, reader and hook (S23, S44)
- **consumes-from** `TOOL-dWellOiledMachine-6` — `supervise.py`'s launch and binding write (S48)
- **consumes-from** `TOOL-dWellOiledMachine-8` — the returns pack, `pyrun.sh` and the `gov_returns_js` block (S8, S29, S31)
- **consumes-from** `TOOL-dWellOiledMachine-10` — `dispatch.js`, the session arm and the decision table (S3, S31, S46)
- **consumes-from** `TOOL-dWellOiledMachine-11` — `commit_queue.py`'s `enqueue_commit` and its tickets (S4, S28)
- **consumes-from** `TOOL-dWellOiledMachine-12` — `session_binding.py` and its pack (S2, S31, S42)
- **consumes-from** `TOOL-dWellOiledMachine-13` — `cadence.py`'s `derive_period` (S20)
- **consumes-from** `TOOL-dWellOiledMachine-14` — `harness.py`, `CAPABILITY_NAMES` and the govkit fixture (S2, S3, S15)
- **consumes-from** `TOOL-dWellOiledMachine-16` — `journal.py`'s `JOURNAL_CLASSES` and its writer (S12, S31, S35)
- **consumes-from** `TOOL-dWellOiledMachine-17` — `secret_scan.py`'s `read_secret_ref` (S7)
- **consumes-from** `TOOL-dWellOiledMachine-20` — the leg it adds to `tools/gate-legs.json` (S40)
- **consumes-from** `TOOL-dWellOiledMachine-23` — the session-start fallback and `measure_hook_cap.py` (S17, S30, S42)
- **consumes-from** `TOOL-dWellOiledMachine-24` — `map-reads.js` (S31)
- **consumes-from** `TOOL-dWellOiledMachine-28` — the moved hooks, tick and suites (S35, S36, S37)
- **consumes-from** `TOOL-dWellOiledMachine-32` — the act record and its record-kind row (S5, S18)
- **consumes-from** `TOOL-dWellOiledMachine-33` — `commit_keys.py`'s trailers and node salt (S5, S7)
- **consumes-from** `TOOL-dWellOiledMachine-34` — `journal.py read` (S35)
- **consumes-from** `TOOL-dWellOiledMachine-35` — `session_node.py` (S6)
- **consumes-from** `TOOL-dWellOiledMachine-36` — `derive_conformance_rows` (S1, S30)
- **consumes-from** `TOOL-dWellOiledMachine-37` — `derive_launch_env` and `LAUNCH_ENV_ALLOW` (S14, S25, S41)
- **consumes-from** `TOOL-dWellOiledMachine-39` — `derive_act_identity` and its leg (S14, S40)
- **consumes-from** `TOOL-dWellOiledMachine-40` — the commit queue's push fixture (S16)
- **consumes-from** `TOOL-dWellOiledMachine-41` — the unit holder's push (S10)
- **consumes-from** `TOOL-dWellOiledMachine-43` — `inflight.py admit` and its hold (S49)
- **consumes-from** `TOOL-dWellOiledMachine-44` — its catalogue edit (S41)
- **consumes-from** `TOOL-dWellOiledMachine-45` — `slots.py`'s tickets and the entry timeout (S28, S45)
- **consumes-from** `TOOL-dWellOiledMachine-55` — its catalogue edit (S41)
- **consumes-from** `TOOL-dWellOiledMachine-56` — its catalogue edit (S41)
- **consumes-from** `TOOL-dWellOiledMachine-57` — the token-shape scan at the door (S47)
- **consumes-from** `TOOL-dWellOiledMachine-58` — the door's namespaces and rules (S47)
- **consumes-from** `TOOL-dWellOiledMachine-60` — `run_build_push`'s fence (S10)
- **hands-off** `TOOL-dWellOiledMachine-84` — S47's attendance entry, re-spelled as the exact ref `refs/gov/attendance` (finding 39)
- **hands-off** `TOOL-dWellOiledMachine-85` — S7's `read_node_salt`, which reads the old store names as a fallback and copies them across (finding 40)
- **hands-off** `TOOL-dWellOiledMachine-90` — S1's replay, S3's verb, S7's salt, S13's leg, S22's normaliser, S28's tickets, S31's population, S35's re-point, S36's rows, S47's scan and §7's legs (findings 4, 5, 6, 7, 11, 25, 26, 29, 31, 35, 37, 44, 47, 48, 65, 66, 67, 68, 69)
- **hands-off** `TOOL-dWellOiledMachine-94` — S34's `harness-hooks` extractor, which the batch re-points to the root table (finding 10)

## 4. Design

### Evidence

Each finding's evidence is its row of the report's appendix, which its skeptic re-read and confirmed;
the items cite the clause they correct. Probes re-run for this spec at base `0689e7fa`:

- `.claude/settings.json` holds 6 events and 13 commands (S26).
- `tools/lib/resolve-python.test.sh:167-186` holds `PARITY_ROWS`, and `blk()` matches `^# >>> ` only
  (`:221`) (S29).
- `tools/settings-merge.py:247` admits `node` and `bash` as interpreters only (S31);
  `tools/process-monitor/procmon-hook.js:117` spawns a bare `python` (S31's class).
- `tools/govkit/govkit.py:1233` defines `resolve_tokens` and `:1436` `target_context` (S33).
- `tools/unattended/check-unattended.sh:4862` exempts `resume-tick.sh\tpid: `, and `:5779` scans
  `$HERE/resume-tick.sh` (S36).
- `memory/project/spawn-idiom-sites.txt` and `memory/project/substitution-fed-loops.txt` are tracked
  path-keyed registries (S37).
- `tools/check-playbook-parity.sh:226-233` fails a registry kit no carrier names (S39).
- `.governance/policy.json` carries `catalogue_blob` (S41).
- `wc -c` prints 18310 for `skills/session-kickoff/SKILL.md` against 18432
  (`tools/template-size-limits.txt:63`), and 10237 for `.claude/skills/unattended/SKILL.md` against
  10240 (`:154`), PINNED 2026-10-27 (S42, S43).
- `tools/policy/check_policy.py:4291` strips `policy.SETTINGS_VARS` and `CLAUDE_PROJECT_DIR` for its
  own live sessions (S24's model).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `write_secret_ref` | Python function, `secret_scan.py` | `write`, OK |
| `tickets.py`: `add_ticket`, `read_queue`, `remove_ticket` | runtime module | `add`, `read`, `remove`, OK |
| `derive_abs_dir` | shell function, `push-main.sh` | `derive`, OK |
| `harness.py --read` | verb | none |
| `cadence.py period` | verb | none |
| `selftest.py --modules` | flag | none |
| `return-unusable` | refusal rule | none |

### Files touched (estimate)

- `tools/runtime/conformance.py`, `tools/runtime/fixtures/conformance/`, `tools/runtime/harness.py`,
  `tools/runtime/harnesses/claude-code.toml`, `tools/runtime/harnesses/codex.toml`
- `tools/runtime/session_binding.py`, `tools/runtime/session-binding.fragment.json`
- `tools/check-wiring.sh`, `tools/push-main.sh`, `tools/settings-merge.py`
- `tools/runtime/commit_queue.py`, `tools/runtime/commit_keys.py`, `tools/runtime/tickets.py`,
  `tools/runtime/slots.py`, `tools/runtime/session_node.py`, `tools/runtime/secret_scan.py`
- `tools/runtime/returns.py`, `tools/runtime/returns.fragment.json`, `tools/runtime/journal.py`,
  `tools/runtime/selftest.py`, `tools/runtime/launch.py`, `tools/runtime/spike.py`,
  `tools/runtime/cadence.py`, `tools/runtime/intake.py`, `tools/runtime/dispatch.js`,
  `tools/runtime/map-reads.js`, `tools/runtime/supervise.py`, `tools/runtime/inflight.py`,
  `tools/runtime/measure_hook_cap.py` (deleted), `tools/runtime/kit.toml`,
  `tools/runtime/resume-tick.test.sh`
- `tools/memory-tree/record-kinds.toml`, `tools/memory-tree/gov_record.py`,
  `tools/memory-tree/door_fixture.py`
- `tools/lib/resolve-python.test.sh`, `tools/gate-legs.json`, `tools/run-gates/selftest-budgets.txt`
- `tools/govkit/selftest.py`, `tools/govkit/subject-pins.tsv`
- `tools/codebase-map/map_extractors.py`, `memory/map/features/runtime.md`,
  `memory/map/features/agent-cap.md`, `memory/map/generated/inventories.json`
- `tools/run-gates/run-gates.test.sh`, `tools/run-gates/run-gates.turnstile.test.sh`,
  `tools/process-monitor/selftest.py`
- `tools/unattended/check-unattended.sh`, `tools/unattended/SKILL.template.md`,
  `.claude/skills/unattended/SKILL.md`
- `memory/project/spawn-idiom-sites.txt`, `memory/project/substitution-fed-loops.txt`
- `WIRE-INTO-PROJECT.md`, `.governance/policy.json`, `skills/session-kickoff/SKILL.md`,
  `skills/session-kickoff/manifest-check.sh`, `help/runtime.md`
- the rev bumps of specs 1, 8, 9, 10, 11, 14, 15, 16, 17, 23, 28, 29, 4, 13, 40, 42, 47 and 57 under
  `memory/builds/dWellOiledMachine/spec/`

### Alternatives rejected

- **Two batches split by kit.** The fixes meet in `tools/gate-legs.json`, `tools/runtime/kit.toml`,
  `tools/runtime/harness.py` and the claude-code table (S2, S13, S29, S40), so the halves would share
  write paths and M6 forbids running them together.
- **Dropping the returns pack's hold (S8).** The skeptic's other option; it loses the retries
  `roles.retries` exists to give, where a block keeps them.

## 5. Production-readiness checklist

- security — S7 removes a second secret reader; S14 and S25 stop the launch filter stripping an act's
  identity; S44 and S49 close two fail-open paths; S47 puts every `refs/gov/` write behind the scan.
- perf / scale — S13 runs every runtime module fixture in one leg; its budget row bounds it.
- error / empty / loading states — S13 and S29 refuse an empty population.
- observability — S3's session line and S48's journal line name their cause.
- risks — until this unit builds, the criteria these findings name cannot pass as written: unit 8
  AC4, unit 13 AC4, unit 14 AC1 and AC4, unit 40 AC3, unit 41 AC3 and unit 42 AC1. Their builders
  record each as answered by this unit's criterion of the same finding.
- testing — AC1 to AC49 and the arms in §7.
- migration — S7's salt moves its environment name to `GOV_SECRET_NODE_SALT`; a node that injected
  `GOV_NODE_SALT` sets the new name. S28 changes no ticket file's shape.
- user docs — S39's runbook section; S42's `help/runtime.md` paragraphs.

## 6. Acceptance criteria

- **AC1** — When `python conformance.py run --replay claude-code-2.1.292`
  runs, its rows include `prompt-submit`. Red when: the row stays `unmeasured` after a replay.
- **AC2** — When `python harness.py --check` runs over both tables, it exits 0 with
  `reattach-cap-bytes` and `session-start-output-cap` present. Red when: either name is refused.
- **AC3** — When the planted claude-code table reads `on-failure = "no"`, `check-wiring.sh --session`
  prints `onFailure ignored by`. Red when: the session line reads the row nowhere.
- **AC4** — When `python commit_queue.py --fixture --plant pending-act` enqueues a commit for an act
  whose record reads `session: pending`, it prints `session pending` and commits nothing.
  Red when: a commit with a pending session is enqueued.
- **AC5** — When an act commit is enqueued in `commit_keys.py`'s fixture, its trailers carry
  `Gov-Act`, `Gov-Item`, `Gov-Unit` and `Gov-Session: <sid>`. Red when: only `Gov-Act` is written.
- **AC6** — When `git grep -n "harness-session\|mint_act" -- tools/runtime` runs, it prints nothing,
  and `session_node.py`'s fixture prints a non-empty `runs-in` edge. Red when: the join is empty.
- **AC7** — When `git grep -n "CredReadW\|secret-tool" -- tools/runtime` runs, it names only
  `secret_scan.py`, and `GOV_SECRET_NODE_SALT=ab python commit_keys.py salt` prints a salt-derived
  digest. Red when: a second reader remains.
- **AC8** — When `node dispatch.js SubagentStop` runs the returns pack on an oversized return, stdout
  carries `{"decision":"block"` and `rule — return-unusable`. Red when: the stop is not held.
- **AC9** — When `grep -n "PARITY_ROWS\|gov_returns_js" 2026-10-26-spec-TOOL-dWellOiledMachine-8.md`
  runs over spec 8, AC4 names the parity row and no pinned count. Red when: AC4 still pins 5.
- **AC10** — When unit 41's fixture runs its holder push from `nb` holding only the unit lease, the
  branch reaches the remote. Red when: it prints `lease refused`.
- **AC11** — When spec 42's corrected AC1, `git grep -n gov-session` with the two exclusions, runs
  over the tree after unit 42, it prints nothing.
  Red when: the upgrade row's `gov-session` text is still matched.
- **AC12** — When `python -c "import journal; print(journal.JOURNAL_CLASSES)"` runs in
  `tools/runtime`, none of the four dropped classes is printed. Red when: one remains.
- **AC13** — When each runtime module runs its own `--fixture` flag, each exits 0 with a non-zero
  count, and `grep -c "runtime selftest"` over the run-gates budget file `selftest-budgets.txt`
  prints 1. Red when: a module fixture runs under no leg, or the population is empty.
- **AC14** — When `launch_act` builds an act launch, its environment carries `GOV_ACT`,
  `GOV_SESSION_KIND` and `GIT_COMMITTER_EMAIL=<act>@gov-act.invalid`. Red when: the filter strips
  them.
- **AC15** — When `grep -c GOV_HARNESS_TABLES 2026-10-26-spec-TOOL-dWellOiledMachine-14.md tools/govkit/selftest.py`
  runs, both print 0, and the govkit fixture's AC4 case passes. Red when: the override is named.
- **AC16** — When the commit queue's fixture pushes from `na` holding `push-main-active` with a 60 s
  stub bar, the push finishes within 10 s printing `decision skip-nondefault`. Red when: it waits
  for the bar.
- **AC17** — When the session-start hook's `next` verb is stubbed to hang, the last line reads
  `next — none · unanswered · next verb did not answer in 10s`. Red when: the `<answer>` segment is
  missing.
- **AC18** — When `grep -n 'tag = "record.act"' record-kinds.toml` runs, it prints
  the row. Red when: the row reads `record-kind.act`.
- **AC19** — When `grep -n 'spawn-backend "remote"' 2026-10-26-spec-TOOL-dWellOiledMachine-1.md`
  runs, it prints nothing. Red when: AC6 still quotes the value.
- **AC20** — When `python cadence.py period weekly --at 2026-10-27T00:00:00Z` runs, it prints the
  period key. Red when: the verb is unknown.
- **AC21** — When `grep -n "TOOL-dWellOiledMachine-55 S7" 2026-10-26-spec-TOOL-dWellOiledMachine-17.md`
  runs, §4 names it. Red when: §4 still names unit 20.
- **AC22** — When `tools/push-main.sh`'s fixture stores the trusted path as `C:\…`, the landing is
  not refused; with a drifted path it is. Red when: one directory's two spellings compare unequal.
- **AC23** — When `intake.py fixture --case multiline` submits `a\nb\n`, the stored `.md` holds no
  `\r\n` and equals the typed bytes. Red when: a CR is added.
- **AC24** — When `python spike.py --fixture --case env` launches a stub that dumps its environment,
  no `CLAUDE_CODE_` or `MESSAGING_` key reaches it, and `case.toml` lists the child's keys.
  Red when: a parent session key leaks.
- **AC25** — When `launch_act` runs under an environment holding `SYSTEMROOT` and `SYSTEMDRIVE`,
  both survive the filter. Red when: `SYSTEMDRIVE` is dropped.
- **AC26** — When `grep -n "13 commands across 6 events" 2026-10-26-spec-TOOL-dWellOiledMachine-10.md`
  runs, it prints the line. Red when: the spec still says 7.
- **AC27** — When `grep -n "no clock-offset correction code" 2026-10-26-spec-TOOL-dWellOiledMachine-15.md`
  runs, it prints the corrected evidence. Red when: §4 still says the probe finds nothing.
- **AC28** — When `git grep -n "def add_ticket" -- tools/runtime` runs, it prints only `tickets.py`,
  and the commit queue's and the slots' fixtures pass their ordering cases. Red when: a second FIFO
  remains.
- **AC29** — When one byte of `unattended-unit.js`'s `gov_returns_js` block changes in a scratch
  copy, the parity row `gov_returns_js` names that file; `grep -c "check-block"
  tools/runtime/returns.py` prints 0. Red when: a drifted copy passes.
- **AC30** — When `conformance.py run --replay` runs over the recorded transcript, it writes
  `session-start-output-cap`, and `git ls-files measure_hook_cap.py` prints nothing.
  Red when: a second measurer remains.
- **AC31** — When a stub `python` exiting 9009 is first on `PATH`, `node dispatch.js` writing a
  `hook-failure` line still writes it, and `git grep -n "'python'" -- tools/runtime` prints nothing.
  Red when: a pack spawns a bare `python`.
- **AC32** — When `grep -n "scan_secrets" 2026-10-26-spec-TOOL-dWellOiledMachine-57.md` and the same
  over specs 4, 13 and 29 run, each edge names TOOL-dWellOiledMachine-16, and spec 17 hands off no
  `scan_secrets`. Red when: an edge still names unit 17.
- **AC33** — When `grep -n ":1233" 2026-10-26-spec-TOOL-dWellOiledMachine-14.md` runs over spec 14,
  the §10 line it prints names `resolve_tokens`. Red when: the numbers stay swapped.
- **AC34** — When the codebase map is re-rendered, `grep -c "PreToolUse tools/hooks/agent-cap.js"
  memory/map/generated/inventories.json` prints 1 or more. Red when: only dispatcher keys remain.
- **AC35** — When `git grep -n "\.git/health\.log" -- tools/run-gates tools/runtime tools/process-monitor`
  runs, it prints nothing. Red when: a suite still reads the retired path.
- **AC36** — When `grep -n "resume-tick.sh" tools/unattended/check-unattended.sh` runs, neither
  `:4862`'s exemption nor `:5779`'s scan remains. Red when: check 36 still carries a STALE row.
- **AC37** — When `grep -c "tools/unattended/resume-tick.test.sh\|tools/unattended/gate-guard" memory/project/spawn-idiom-sites.txt`
  runs, it prints 0. Red when: an old-path row remains.
- **AC38** — When `grep -n "routed-commits selftest" 2026-10-26-spec-TOOL-dWellOiledMachine-28.md`
  runs, §7 names it. Red when: the leg is absent.
- **AC39** — When `bash tools/check-playbook-parity.sh` runs, it does not fail 4 for `runtime`.
  Red when: the runbook never names the kit.
- **AC40** — When `python tools/govkit/govkit.py selfcheck` runs, every runtime leg is claimed.
  Red when: a leg is claimed by no descriptor.
- **AC41** — When `python tools/policy/policy.py mirror --write` runs, `git diff --stat
  .governance/policy.json` prints nothing afterwards. Red when: the mirror differs from its render.
- **AC42** — When `wc -c skills/session-kickoff/SKILL.md` runs, it prints 18432 or less. Red when:
  the paragraphs push it over.
- **AC43** — When `wc -c .claude/skills/unattended/SKILL.md` runs, it prints 10240 or less.
  Red when: the `next.py` read pushes it over.
- **AC44** — When `intake.py fixture --case no-prompt-field` and `--case bad-json` run, each hook exits
  1. Red when: either exits 0.
- **AC45** — When two packs of 300000 and 400000 `budget-ms` share an entry, the rendered `timeout`
  is 710. Red when: it is 410, the largest alone.
- **AC46** — When the dispatcher fixture sends a `UserPromptSubmit` refusal and a `PostToolUse`
  context, the first is emitted unchanged and the second's context joined. Red when: either
  event has no row.
- **AC47** — When `python door_fixture.py --case life-token` writes a `refs/gov/life` request
  carrying a token, the write is refused by the scan. Red when: it is pushed unscanned.
- **AC48** — When `python supervise.py --fixture --plant binding-unreachable` makes the remote
  unreachable, nothing launches and the journal names `binding=failed`. Red when: the act launches.
- **AC49** — When `python inflight.py --fixture --plant unmeasured-hold` runs, the call is denied at
  once with `admission — waiting`. Red when: the pack crashes and admits the call.

## 7. Gates

`check-wiring self-test` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map coverage + freshness` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selftest` · `govkit selfcheck` · `lexicon naming predicates` · `manifest-check self-test` · `measure-legs selftest` · `policy fixtures` · `process-monitor census selftest` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `run-gates turnstile` · `scratch-guard self-test` · `straggler-guard arms` · `transition-audit arms` · `playbook parity` · `kickoff engine size <=18KiB` · `unattended skill size` · `unattended kit gate` · `python resolver (behaviour + inline parity + idiom ban)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/runtime/selftest.py · covers AC2 AC13 AC24 · the module population staged empty, a planted unknown capability name, and a stub child receiving the parent's keys · none
New arm: tools/lib/resolve-python.test.sh · covers AC29 · one byte changed in a scratch copy of a `gov_returns_js` block · none
New arm: tools/runtime/dispatch.test.sh · covers AC8 AC46 · the returns pack exiting 2 and the two new events, staged against a dispatcher with no row for them · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the spec audit round 1's 49 medium and low findings batched.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-1
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-84, TOOL-dWellOiledMachine-85, TOOL-dWellOiledMachine-90.
- rev-3 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-94.

## 10. Reuse audit

Each item extends the seam its finding names: `derive_conformance_rows` (S1, S30), `read_secret_ref`
(S7), `PARITY_ROWS` (S29), `pyrun.sh` (S31), `journal.py read` (S35), `resolve_kit_dir` and the
playbook's carriers (S39), and the door (S47). The probe
`python tools/codebase-map/reuse_lookup.py "batch the spec audit minor findings"` ranked `audit`,
`read_spec_revisions` and `parse_spec_h1`, spec readers rather than any fix's seam, so the seams are
the per-item ones above; S28's ticket queue is the one new module, extracted at its second instance.

Recall terms used: `python tools/memory-recall/query.py "how are a spec audit's medium and low
findings batched" --terms "minors batch spec audit medium low promoted findings write set capability
rows pyrun"`
