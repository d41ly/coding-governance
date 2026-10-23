# TOOL-dSafePassage-26 — the round-1 spec audit's 54 minors: one base rule, one writer each, honest populations, declared exits, and the texts that name them

**Status:** OPEN · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 6 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-26-deviation-72.md](../build/2026-10-23-build-TOOL-dSafePassage-26-deviation-72.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-26-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-26-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-26-hygiene-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-26-hygiene-fix.md) | research | TOOL-dSafePassage-24 TOOL-dSafePassage-25 |
| [2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-16 TOOL-dSafePassage-20 TOOL-dSafePassage-15 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-17 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-21 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
exited BLOCKED and BOUNDED with 65 confirmed findings. Its 3 blockers and 8 highs are units 15 to 25.
This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW, each by its
report id and each its own scope item, where the report merged ids into one item too. The minors land
on all thirteen units, so this unit repairs none in particular and builds after every unit, order 6.
Where a minor would bite an earlier pass, the hands-off bullet the faulted unit's own §3 carries to
this one names it; the rest are amended and observed at this pass. Where a finding's defect is the
text of a spec built before this one, the item states the superseding reading and this unit's
criterion observes it, because a closed spec is not rewritten.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| D-10 | MEDIUM | 4, 26, 42, 65 | S1, S2, S3, S4 |
| D-11 | MEDIUM | 7 | S5 |
| D-12 | MEDIUM | 8, 37 | S6, S7 |
| D-13 | MEDIUM | 9 | S8 |
| D-14 | MEDIUM | 10 | S9 |
| D-15 | MEDIUM | 11, 62 | S10, S11 |
| D-16 | MEDIUM | 12 | S12 |
| D-17 | MEDIUM | 19 | S13 |
| D-18 | MEDIUM | 27 | S14 |
| D-19 | MEDIUM | 28 | S15 |
| D-20 | MEDIUM | 29, 61 | S16, S17 |
| D-21 | MEDIUM | 30 | S18 |
| D-22 | MEDIUM | 31 | S19 |
| D-23 | MEDIUM | 36 | S20 |
| D-24 | MEDIUM | 38 | S21 |
| D-25 | MEDIUM | 39 | S22 |
| D-26 | MEDIUM | 40 | S23 |
| D-27 | MEDIUM | 43 | S24 |
| D-28 | MEDIUM | 44 | S25 |
| D-29 | MEDIUM | 46 | S26 |
| D-30 | MEDIUM | 47 | S27 |
| D-31 | MEDIUM | 48 | S28 |
| D-32 | MEDIUM | 49 | S29 |
| D-33 | MEDIUM | 55 | S30 |
| D-34 | MEDIUM | 56 | S31 |
| D-35 | MEDIUM | 57 | S32 |
| D-36 | MEDIUM | 58 | S33 |
| D-37 | MEDIUM | 59 | S34 |
| D-38 | MEDIUM | 60 | S35 |
| D-39 | MEDIUM | 63 | S36 |
| D-40 | MEDIUM | 64 | S37 |
| D-41 | MEDIUM | 66 | S38 |
| D-42 | MEDIUM | 67 | S39 |
| D-43 | LOW | 6 | S40 |
| D-44 | LOW | 13 | S41 |
| D-45 | LOW | 14, 20, 41 | S42, S43, S44 |
| D-46 | LOW | 15 | S45 |
| D-47 | LOW | 17 | S46 |
| D-48 | LOW | 21 | S47 |
| D-49 | LOW | 22 | S48 |
| D-50 | LOW | 23 | S49 |
| D-51 | LOW | 24 | S50 |
| D-52 | LOW | 25 | S51 |
| D-53 | LOW | 33 | S52 |
| D-54 | LOW | 34 | S53 |
| D-55 | LOW | 45 | S54 |

That is 39 MEDIUM and 15 LOW findings by raw id. Ids 18 and 32 were refuted by the audit and are not
here. Items whose fix the report records as REJECTED are built from the skeptic's corrected fix.

## 2. Scope (IN)

### The base rule (D-10)

- **S1** — id 4. One base ladder, one owner: `resolve_landing_base(root, base)` in
  `tools/govkit/upgrade_steps.py` returns `(sha, boundary, refusal)` from `--base`, else a non-zero
  `GATE_PUSH_BASE`, else the merge-base with the remote ladder's default branch, the ladder
  `cmd_epoch` holds at `tools/govkit/govkit.py:13446-13474` at the base. `cmd_epoch` prints its own
  lines from the triple. Observed by AC1.
- **S2** — id 26. The second spelling goes. TOOL-dSafePassage-1's `derive_push_base` and
  TOOL-dSafePassage-10's copy in `govkit.py` are replaced by calls of S1's function, and
  TOOL-dSafePassage-10's AC10 is read as S1's grep of both spellings.
  **Readers:** by name: READER NOT IN TREE, because TOOL-dSafePassage-1 mints `derive_push_base` in
  `tools/govkit/govkit.py` and its caller `cmd_frozen` in `tools/govkit/upgrade_steps.py`, a module
  that unit creates, and that unit is unbuilt at the base, so no tracked file spells the function,
  that caller or that module yet; at its landing the callers of `derive_push_base` are `cmd_frozen`
  and `cmd_epoch` in `tools/govkit/govkit.py` · by value: the bases `kit epoch` and
  `step-rows-frozen` grade, which S3 makes one. Observed by AC1.
- **S3** — id 42. The step gate, `cmd_epoch` and `cmd_frozen` call S1's function and nothing else
  resolves a landing's base in `tools/govkit`, so the frozen leg, the epoch leg and the step gate
  grade one range. Observed by AC2.
- **S4** — id 65. The placement. `tools/govkit/upgrade_steps.py` carries the remote ladder inline
  between the `remote_ladder_py` markers, byte-identical with its canonical copy and gated by the
  parity rows that gate govkit's copy (`tools/govkit/govkit.py:555-558`), so the step module imports
  nothing from `govkit.py` and TOOL-dSafePassage-3's §8 F1 holds. Observed by AC3.

### Specs read against what was built (D-11, D-13, D-14)

- **S5** — id 7. TOOL-dSafePassage-3's AC12 second clause is read as: `tools/run-gates/check-receipt.py`
  keeps its schema-3 fixture write (`:198`) and its schema print (`:437`), by grep; TOOL-dSafePassage-8
  S6's edit of that file is expected. Observed by AC4.
- **S6** — id 8. `step-rows-frozen` gets every row a new leg owes: `tools/govkit/subject-pins.tsv`
  through `python tools/govkit/govkit.py selfcheck --write`, `tools/run-gates/ceiling-evidence.txt`
  through `python tools/run-gates/derive-ceilings.py --write` over the measured run, and the leg's name
  in the `gate-legs` list of `memory/map/features/govkit.md`. Observed by AC5.
- **S7** — id 37. `memory/map/generated/` is regenerated by `python tools/codebase-map/gen_map.py
  --write` over every module this build's units mint, and `codebase-map coverage + freshness` is on
  this unit's §7 line, the leg units 1, 5, 10 and 13 omit. Observed by AC6.
- **S8** — id 9. The witness of `govkit/template-size-limits-to-budgets` holds when
  `<prefix>/template-size-limits.txt` is absent and either no before-image exists or every cap reads
  its image's value. Observed by AC7.
- **S9** — id 10. The window plant of `tools/govkit/shims.py` takes `--expect held|allowed`, prints
  the observation `held` or `allowed`, and exits by TOOL-dSafePassage-6 §4's one contract, 0 when the
  observation matches and 1 otherwise; that unit's AC6 and AC7 exit columns are read as `--expect`
  values (§8 F1). Observed by AC8.

### The floor down's population (D-15, D-16)

- **S10** — id 11. The floor step's down grades the files the rollback restores, not the tip's.
  TOOL-dSafePassage-1's grammar gains the placeholder `{to}`, resolved by `resolve_step_argv` only for
  a `down` phase under `update --rollback`, to the rollback's `--to` commit, and refused in every other
  phase (§8 F4). The floor row's down becomes
  `["bash", "{gov}/lib/python-floor.sh", "down", "3.11", "{target}", "{to}"]`, and
  `check_down_floor(target, prior, to_commit)` reads each graded file's bytes at `to_commit`.
  Observed by AC9.
- **S11** — id 62, the skeptic's fix. The graded population: in an adopter, the receipt's `files`
  rows ending `.py` or `.toml`, read from gov at `to_commit`, plus every `.governance/*.toml` in the
  target; never the adopter's own other files. In source mode, gov's tracked set at `to_commit`.
  Observed by AC10.
- **S12** — id 12. A tracked arm never spells a floor statement literally: the plants in
  `tools/lib/resolve-python.test.sh` and TOOL-dSafePassage-12's staged break are assembled at run time,
  as `'Py''thon 3.12 or newer'` is. Observed by AC11.

### The step contract (D-17)

- **S13** — id 19, the skeptic's fix. `build_step_env` carries the parent's effective `core.autocrlf`
  and `core.eol`, each only when set, as further `GIT_CONFIG_KEY_<n>` pairs, `GIT_CONFIG_COUNT`
  counting them; TOOL-dSafePassage-7's AC1 reads `GIT_CONFIG_COUNT` as 2 plus those pairs, and its §4
  table names the two keys (§8 F2). Observed by AC12.

### One reader or writer each (D-18 to D-22)

- **S14** — id 27. `blob_at` (`tools/govkit/govkit.py:6706` at the base) moves into
  `tools/govkit/upgrade_steps.py` beside `Refusal`, govkit imports it back, and TOOL-dSafePassage-1's
  introducing-commit derivation reads blobs through it, so no second revision-blob reader ships. The
  selftest's monkeypatching of `gk.blob_at` keeps working on govkit's callers. Observed by AC13.
- **S15** — id 28, the skeptic's fix. `write_atomic` (`tools/govkit/govkit.py:4198` at the base)
  moves into `tools/govkit/upgrade_steps.py`, govkit imports it back, and the schema-4 step program and
  the walk write the receipt through it. The one-writer arms of `tools/govkit/selftest.py`
  (`:16523`, `:16630`, `:16644` at the base) parse `upgrade_steps.py` and every
  `tools/govkit/steps/*.py` beside `govkit.py`, and their staged break is committed into the file that
  defines `write_atomic`. Observed by AC14.
- **S16** — id 29. `derive_introduced(root, landed_ref, paths, table, id)` takes its declaring files
  and table, and `resolve_shim_landing` calls it over `tools/govkit/shims.toml` and `shim`, so a
  shim's landing is the first first-parent blob holding a row with that exact id; no `git log -S`
  remains in `tools/govkit/shims.py`. Observed by AC15.
- **S17** — id 61. The window plants `window-prefix-id`, two ids one a prefix of the other, and
  `window-comment-id`, the id quoted in the file's header comment at an earlier commit, each resolve
  to their own row's landing. Observed by AC16.
- **S18** — id 30. One writer of an outbox order keyed on a row: `write_row_order` takes the order's
  key, applies `render_order_slug` itself, and the two `update-conflict-` sites
  (`tools/govkit/govkit.py:10667`, `:10805` at the base), the `update-withdrawn-` site (`:10760`) and
  TOOL-dSafePassage-2's `write_attended_order` call it. TOOL-dSafePassage-9's AC7 is read as AC17.
  Observed by AC17.
- **S19** — id 31, the skeptic's fix. One target factory: the fixtures of `tools/govkit/upgrade_steps.py`,
  `tools/govkit/fixtures/retired_edits.py` and `tools/govkit/upgrade_walk.py` build their scratch
  targets through `build_target` and their scratch govs through `build_scratch_gov`, both in
  `tools/govkit/fixture_target.py`, the latter lifted from `build_gov17` (`tools/govkit/selftest.py:1728`).
  Observed by AC18.

### The resolver's text (D-23, D-48, D-49)

- **S20** — id 36. The refusal keeps today's header, `resolve_python: no usable python launcher`, as
  its first line and the `resolve_python: tried:<names>` line as its LAST, verbatim; the per-candidate
  outcomes, the override lines and the install line print between them. The two RA7-4 arms of
  `tools/workflows/unattended-build.test.sh` (`:2413`, `:2417`) and `tools/lib/resolve-python.test.sh:76`
  then hold unedited. Observed by AC19.
- **S47** — see the low items below. Observed by AC45.

### Dead paths, size limits, gov's own tree (D-24 to D-26)

- **S21** — id 38, the skeptic's fix. TOOL-dSafePassage-1's AC15 is read with the step declarations
  excluded: `tools/govkit/steps.toml`, `tools/govkit/steps/`, `help/upgrade-steps.md` and the release-0
  fixture. `tools/check-dead-paths.sh` declares the step declarations and the release-0 fixture outside
  its haystack, three `:(exclude)` pathspecs beside its own two files with a comment saying why, and
  adds no waiver row; the help page names a step's dead path by the step's id, never by its basename.
  Observed by AC20.
- **S22** — id 39. `tools/check-template-size.test.sh`'s limits-file arms (A19 and the pair arms,
  `:112-172` at the base) feed scratch `.governance/policy.toml` fixtures, and the arm for a
  non-numeric declared limit still reds through the policy reader; `template size gate selftest` is on
  §7. Observed by AC21.
- **S23** — id 40, the skeptic's fix. Gov's own before-image of the template-size step is removed once
  its witness holds, since gov's down is its git history: no `.governance/steps/` path is tracked or
  left untracked in gov's tree, and `memory/map/generated/CARDS.md` is regenerated so it no longer
  spells the retired file.
  **Readers:** by name: READER NOT IN TREE, because the image's writer `write_before_image` and its
  reader `write_from_before_image`, the step's down, are minted in `tools/govkit/upgrade_steps.py` by
  TOOL-dSafePassage-1, unbuilt at the base, so no tracked file spells them yet; the one tracked reader
  the item touches is `memory/map/generated/CARDS.md`, regenerated by it · by value: NO VALUE READERS,
  since gov's down is its git history, so nothing on gov's tree reads the caps gov's own image holds,
  and an adopter's image is not this item's. Observed by AC22.
- **S24** — id 43, the skeptic's fix. TOOL-dSafePassage-10's AC12 is observed twice: on the branch
  with no receipt, through `TOOL-dSafePassage-21`'s plan source, and on a prepared-merge fixture that
  carries the receipt; its Rollout sentence that the receipt is landed before it is read as: the
  receipt arrives only in the one landing. Observed by AC23.

### The receipt's readers (D-28 to D-30)

- **S25** — id 44. The arms at `tools/govkit/selftest.py:8210` and `:8230`, which force an
  `apply`-written receipt to schema 1 or 2, also take `steps` out, as matrix's `build_role_pair` does.
  Observed by AC24.
- **S26** — id 46. TOOL-dSafePassage-4's AC6 is read with exit 2, govkit's `Refusal` code, which
  `tools/govkit/selftest.py:7528-7530` already asserts for the downgrade refusal; the usage line of
  `skills/deploy-governance/SKILL.md:89` gains `[--rollback]`. Observed by AC25.
- **S27** — id 47. The four receipt readers TOOL-dSafePassage-8's table omits are graded with gov's
  source receipt present and absent: `rendered_at` in `tools/unattended/adopt-unattended.sh:423-436`
  and `tools/memory-tree/adopt-memory-tree.sh:284-297`, `tools/settings-merge.py:360-372` and
  `tools/memory-tree/row_grammar.py:2576-2578`; a reader whose output differs is fixed in this pass,
  its path added to the dispatch writes. `unattended skill wiring` and `row-grammar selftest` are on
  §7. Observed by AC26.

### The update verdicts (D-31, D-42)

- **S28** — id 48. The seed override in `_cmd_update` (`tools/govkit/govkit.py:9987-9999` at the base)
  exempts `retired-edited` beside `missing` and `renamed`, and the fixture plant `edited-gone-seed`
  expects `retired-edited` with an order.
  **Readers:** the item withdraws no name; the verdict it keeps is spelled with the trigger's verb.
  by name: `_cmd_update` in `tools/govkit/govkit.py`, the one reader of the exemption set the item
  widens · by value: NO VALUE READERS, since no verdict value is withdrawn and the seed row's
  verdict is graded by AC27. Observed by AC27.
- **S39** — id 67. A `retired-edited` row whose path gov ships again, as a descriptor role or a
  `[[retired]]` successor's, returns to that role and is graded as a three-way conflict candidate
  with an order; the plant `edited-reshipped` observes it. Observed by AC38.

### Records and step programs (D-32 to D-35)

- **S29** — id 49. `.memory-tree.conf`'s `PROJECT_REGISTRY_EXTRA` (`:917`) gains
  `docs-undocumented.txt`, with a comment block in that key's established form. Observed by AC28.
- **S30** — id 55, the skeptic's fix. The `agent-cap/fanout-cap-to-agents-in-flight` up keeps the
  shared parser's grammar (`tools/hooks/agent-cap.js:1631-1632`): other keys, blanks and comments are
  legal and the last `FANOUT_CAP` wins. It removes only the `FANOUT_CAP` lines, deletes the file only
  when nothing but blanks and comments remains, and keeps the whole file in its before-image. Its
  witness: no `FANOUT_CAP` assignment in `.agent-cap.conf`, or the file absent. TOOL-dSafePassage-1's
  AC12 is read with `FANOUT_CAP=abc` alone.
  **Readers:** by name: `loadDeclaredCap` in `tools/hooks/agent-cap.js`, which spells `FANOUT_CAP`
  and `.agent-cap.conf`, and the other files S43's grep prints, which that item derives and disposes
  · by value: `loadDeclaredCap`, whose declared cap the
  fan-out guard holds the agents in flight under, the value the step's up carries to
  `runtime.agents-in-flight`. Observed by AC29.
- **S31** — id 56. `write_before_image` writes through `write_atomic` (S15); an image that does not
  parse is treated as absent only when no path it would list has changed since, and otherwise the up
  exits 1 naming the image. Observed by AC30.
- **S32** — id 57, the skeptic's option (a). In source mode `run_step_isolated` runs the `witness` of a
  `needs-target = true` row, while its `up` and `down` stay `attended`: on gov's tree the target's code
  is gov's own (TOOL-dSafePassage-7 §4), so an up the owner ran on the run branch is seen to hold at
  `--prepare` and the row is listed `applied` (§8 F3). Observed by AC31.

### Liveness, forwarders, page commands, history, readers (D-36 to D-41)

- **S33** — id 58. The write lock records `platform`, `sys.platform`, and under Linux the kernel's
  `boot_id`; `check_holder_dead` reads a holder `unknown` whenever either differs from this process's,
  so a WSL run and a Windows run on one tree never reclaim each other's live lock. Observed by AC32.
- **S34** — id 59. The `js` forwarder exits 127 printing the error when `spawnSync` sets `error`,
  128 plus the signal's number when it sets `signal`, and `status` otherwise. Observed by AC33.
- **S35** — id 60. Both `py` forwarders put the target's own directory first on `sys.path` before
  running or loading it, as `python <target>` would; the forwarding plant's target imports a sibling.
  Observed by AC34.
- **S36** — id 63, the skeptic's fix. `read_page_commands`: in a `console` fence only lines opening
  `$ ` or `> ` are commands, the prompt stripped; a trailing backslash joins the next line; inside
  `bash` and `sh` fences a comment line is skipped and a trailing comment stripped, through
  `shlex.split(line, comments=True)`; a line that still cannot be split is a finding naming the page
  and the line. Observed by AC35.
- **S37** — id 64. `read_steps` exits 2 when `git rev-parse --is-shallow-repository` prints `true`,
  naming `git fetch --unshallow`, and the declaring-file set is read at each commit of the walk, from
  that commit's registry and descriptor paths, never from the head's. Observed by AC36.
- **S38** — id 66. The step gate's reader contract: a reader returns an empty set when its source is
  absent at that revision, and a reader that raises makes the gate exit 2 naming the class, the side,
  `base` or `tip`, and the error. Plants `reader-raises` and `base-without-source`. Observed by AC37.

### The low items

- **S40** — id 6, the skeptic's fix. The build-order table's `Parallel` column is M6's candidate set
  and not a dispatch order. Within order 1 TOOL-dSafePassage-1 builds before TOOL-dSafePassage-3; within
  order 3 TOOL-dSafePassage-11 before TOOL-dSafePassage-8 before TOOL-dSafePassage-12, and
  `TOOL-dSafePassage-15` before TOOL-dSafePassage-11, `TOOL-dSafePassage-18` before
  `TOOL-dSafePassage-19`. Each pair is declared as a consumes-from edge, which `--dispatch` waits on.
  Observed by AC39.
- **S41** — id 13. TOOL-dSafePassage-11's AC11 is read as: govkit runs under a real interpreter given
  by absolute path, and the fakes sit first on the `PATH` the step's isolated environment inherits.
  Observed by AC40.
- **S42** — id 14. The comment at `tools/workflows/kit.toml:68` names `runtime.agents-in-flight` in
  place of a tracked `.agent-cap.conf`. Observed by AC41.
- **S43** — id 20. The by-name readers of `.agent-cap.conf` are derived, not typed: the pass prints
  `git grep -l -F '.agent-cap.conf' -- tools skills` and disposes each file it prints, re-pointed,
  re-worded or kept as a legacy-home reader under `cl-dClosedLoop-0016`, one ledger line per file.
  Observed by AC42.
- **S44** — id 41. `tools/workflows/README.md:28` is re-worded to name `runtime.agents-in-flight`.
  Observed by AC41.
- **S45** — id 15. `tools/check-spec-tokens.py` gains an `ac-order` join: a live spec whose §6
  criterion labels, read with its `AC_LABEL`, do not ascend is a finding naming the spec and the first
  label out of order. TOOL-dSafePassage-8's AC8 and AC9 are cited by label, which their order does
  not change. Observed by AC43.
- **S46** — id 17. The schema-4 step program writes through `write_atomic` (S15), UTF-8 with
  `newline="\n"`, so its down's bytes equal its up's input on Windows. Observed by AC44.
- **S47** — id 21. The resolver block's comment and `help/python-floor.md` state that its `[ -f ]`
  test holds on an App Execution Alias, so a Store Python whose `sys.executable` is itself an alias is
  echoed as printed, the gap `check_app_alias` (`tools/run-gates/measure_legs.py:890`) closes there and
  the block does not; the perf figure names the candidate node d picks, `python3`, a plain shim
  measured by the audit at 25 ms against `py`'s 92 ms (PINNED, 2026-10-23). Observed by AC45.
- **S48** — id 22. `help/python-floor.md` says `-I` is new to the probe, and a resolver arm plants a
  fake launcher that exits non-zero under `-I` and zero without it, which is passed over as
  `did not run`. Observed by AC46.
- **S49** — id 23. `tools/lexicon/selftest.py:107-109` points at `python-floor.txt`, and
  `FLOOR_STATEMENT_RX` gains the case `no declared Python floor`, so the query at `3708a705` prints
  seven statements, TOOL-dSafePassage-11's AC8 figure read as seven. Observed by AC47.
- **S50** — id 24. TOOL-dSafePassage-10 §4's figure reads 5382 of 5832 tracked paths at `3708a705`
  (PINNED, `git ls-tree -r --name-only`, 2026-10-23). Observed by AC48.
- **S51** — id 25. TOOL-dSafePassage-5 S12's figure reads 79 call sites of `make_target`, the grep's
  80 less the definition at `tools/govkit/selftest.py:679`. Observed by AC49.
- **S52** — id 33. `resolve_lander_kit <kit> <file>` in `tools/push-main.sh` echoes the resolved
  interpreter and kit directory or prints the skip reason, and every lander stage that resolves a kit
  calls it (`:440`, `:735`, `:763`, `:809`, `:831` at the base, and `run_gov_first`), the last turning
  a missing interpreter into a refusal. Observed by AC50.
- **S53** — id 34. `tools/lib/python-floor.sh floor` is the one shell reader of `python-floor.txt`,
  applying `read_floor`'s rule, exactly `<major>.<minor>` and one optional LF, with no Python; the
  `floor` step of `.github/workflows/remote-ci.yml` runs `floor=$(bash tools/lib/python-floor.sh floor)`.
  Observed by AC51.
- **S54** — id 45. `skills/deploy-governance/SKILL.md:63` and `:73-75` say the receipt is at schema 4
  with `steps`, reached by the step `govkit/receipt-schema-4`, and point at `help/upgrade-steps.md`'s
  receipt section. Observed by AC52.

## 3. Non-goals (OUT)

- Every blocker and high: units 15 to 25.
- Rewriting a closed spec. An item that corrects a built spec's text states the reading here.
- A lint that reads a step witness's meaning, a linter for every "exits N" claim, and the other
  spec-set lints the report proposes as left-shifts, beyond S45's.
- `merge.<driver>.driver` in the step contract, which `TOOL-dSafePassage-24` names as uncovered.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — the row grammar, `derive_introduced`, `derive_push_base`, the two legacy-home steps and the leg `step-rows-frozen`, which S1, S2, S6, S8, S10, S14, S16, S21, S23, S30, S31 and S37 amend
- **consumes-from** `TOOL-dSafePassage-2` — the lock, `write_attended_order` and the walk's fixtures, which S18, S19 and S33 amend
- **consumes-from** `TOOL-dSafePassage-3` — the schema step program and the receipt's readers, which S5, S15, S25, S46 and S54 amend
- **consumes-from** `TOOL-dSafePassage-4` — the rollback's refusals and `{to}`'s one phase, which S10 and S26 amend
- **consumes-from** `TOOL-dSafePassage-5` — `fixture_target.py` and `build_target`, which S19 and S51 extend
- **consumes-from** `TOOL-dSafePassage-6` — the forwarders and the window plant, which S9, S16, S17, S34 and S35 amend
- **consumes-from** `TOOL-dSafePassage-7` — `build_step_env`, `resolve_step_argv` and `run_step_isolated`, which S10, S13 and S32 amend
- **consumes-from** `TOOL-dSafePassage-8` — the source-mode walk and its readers' table, which S24, S27 and S32 amend
- **consumes-from** `TOOL-dSafePassage-9` — `write_row_order` and `retired-edited`, which S18, S28 and S39 amend
- **consumes-from** `TOOL-dSafePassage-10` — the step gate and its base, which S1, S3, S24, S38 and S50 amend
- **consumes-from** `TOOL-dSafePassage-11` — the floor module, its down and the resolver block, which S10, S11, S12, S20, S41, S47, S48, S49 and S53 amend
- **consumes-from** `TOOL-dSafePassage-12` — the CI workflow's `floor` step, which S12 and S53 amend
- **consumes-from** `TOOL-dSafePassage-13` — `read_page_commands` and `docs-undocumented.txt`, which S29 and S36 amend
- **consumes-from** `TOOL-dSafePassage-21` — the `file` class's plan source, beside which S24 observes the receipt source
- **consumes-from** `TOOL-dSafePassage-22` — the reclaim's clock rule, beside which S33 adds the namespace
- **consumes-from** `TOOL-dSafePassage-23` — the resolver's echo rule, beside which S20 and S47 set the refusal's lines and the alias gap
- **consumes-from** `TOOL-dSafePassage-24` — the contract's repository-scope refusal, beside which S13 carries the line-ending keys
- **consumes-from** `TOOL-dSafePassage-25` — `run_gov_first`'s refusal shape, which S52's extraction keeps
- **hands-off** `TOOL-dSafePassage-31` — the lock's pid namespace recorded and judged, the repair of finding 13 of the round-1 audit of units 15 to 26
- **hands-off** `TOOL-dSafePassage-34` — the ac-order join armed by a dated key over a measured population, the repair of finding 29 of the round-1 audit of units 15 to 26
- **hands-off** `TOOL-dSafePassage-35` — the minors batch of the round-1 audit of units 15 to 26, which reads this unit's criteria and items against their sources and adds the boot rows of the namespace verdict
- **hands-off** `TOOL-dSafePassage-41` — S45's `ac-order` join, AC43 and the `tools/check-spec-tokens.test.sh` arm covering it, which that unit builds in one pass with its key: this unit's pass adds no join, the repair of finding 22 of the spec audit of units 27 to 35

## 4. Design

### Data model

The placeholder `{to}` (S10), beside TOOL-dSafePassage-1's three:

| Placeholder | Resolves to | Phases |
|---|---|---|
| `{to}` | the 40-hex `--to` commit of `update --rollback` | `down` only; any other phase, or a down outside `--rollback`, is a refusal naming the step and the token |

The lock record (S33): `{"pid", "verb", "started", "started_utc", "host", "platform", "boot_id"}`,
`boot_id` the content of `/proc/sys/kernel/random/boot_id` or `""` where it does not exist.

The step environment's carried keys (S13): `GIT_CONFIG_KEY_<n>` = `core.autocrlf` or `core.eol`,
`GIT_CONFIG_VALUE_<n>` the parent's effective value, read once by `git config --get` in the parent,
each pair present only when the parent sets the key.

### Inventory

Minted: `resolve_landing_base` in `tools/govkit/upgrade_steps.py`; `build_scratch_gov` in
`tools/govkit/fixture_target.py`; `resolve_lander_kit` in `tools/push-main.sh`; the verb `floor` on
`tools/lib/python-floor.sh`; the placeholder `{to}`; the lock keys `platform` and `boot_id`; the join
name `ac-order` in `tools/check-spec-tokens.py`; the plants `window-prefix-id`, `window-comment-id`,
`edited-gone-seed`, `edited-reshipped`, `reader-raises`, `base-without-source`, `console-prompt`,
`continued-flag`, `unbalanced-quote`, `comment-apostrophe`, `truncated-image`, `autocrlf`,
`lock-foreign-namespace`, `needs-target-source` and `missing-target`. Each Python function passes
`py.function` and `resolve_lander_kit` passes `sh.function`, by `python tools/lexicon/lexicon.py
--suggest <name> --as <cell>`, run at the pass. Moved, not minted: `blob_at`, `write_atomic`. No conf
key, no gate leg, no policy key.

### Migration

Additive for adopters: the lock's new keys are read only when present, an old lock reading `unknown`
only where its namespace cannot be shown equal (TOOL-dSafePassage-2 §4 "Migration" keeps reading an
old lock on this host). No landed step row exists at the base, so `{to}` and S30's witness change no
frozen row.

### Rollout

Live at landing. It builds at order 6, after every unit of the build, units 15 to 25 included. Its
items share `tools/govkit/govkit.py`, `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py`
with each other, so the pass is one unit: the minors do not split into two disjoint write sets by M6.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/govkit/step_gate.py`
- `tools/govkit/shims.py`
- `tools/govkit/docs_leg.py`
- `tools/govkit/steps.toml`
- `tools/govkit/steps/fanout_cap.py`
- `tools/govkit/steps/template_size_limits.py`
- `tools/govkit/steps/receipt_schema_4.py`
- `tools/govkit/fixture_target.py`
- `tools/govkit/fixtures/retired_edits.py`
- `tools/govkit/upgrade_walk.py`
- `tools/govkit/subject-pins.tsv`
- `tools/govkit/refusal_join.py`
- `tools/run-gates/ceiling-evidence.txt`
- `memory/map/features/govkit.md`
- `memory/map/generated/inventories.json`
- `memory/map/generated/MAP.md`
- `memory/map/generated/CARDS.md`
- `memory/map/generated/symbols.json`
- `tools/lib/resolve-python.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/lib/python-floor.sh`
- `tools/lib/python_floor.py`
- `tools/lexicon/selftest.py`
- `.github/workflows/remote-ci.yml`
- `tools/check-dead-paths.sh`
- `tools/check-template-size.test.sh`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `.memory-tree.conf`
- `skills/deploy-governance/SKILL.md`
- `tools/workflows/kit.toml`
- `tools/workflows/README.md`
- `help/upgrade-steps.md`
- `help/python-floor.md`

The resolver block's inline copies, derived as `TOOL-dSafePassage-23` S4 derives them, are re-synced
in the same commit and added to this unit's `--dispatch --writes`, as is any S27 reader this pass fixes.

### Alternatives rejected

- **Two batch units.** The items share three govkit files and the map renders; no split leaves two
  disjoint write sets (M6 clause 1).
- **Folding each minor into its unit's spec.** The disposal promotes, never folds (BUILD-METHOD M4).
- **`git log -G` anchored on the id line** (S16), the report's lesser option: a second reader of one
  landing fact beside `derive_introduced`.
- **Moving `resolve_remote` out of govkit** (S4). Govkit's copy is already an inline copy of a
  canonical file; a further inline copy under the same parity gate adds no import edge.

## 5. Production-readiness checklist

- security: S13 carries two non-credential keys into the step environment; S32 runs a needs-target
  witness only on gov's own tree; S10's `{to}` is refused outside a rollback's down; S33 refuses
  more reclaims, never fewer.
- perf / scale: one extra `git config` read per step for S13 and one `rev-parse` per `read_steps` for
  S37; nothing else measurable. The perf figure S47 pins is the audit's measurement.
- error / empty / loading states: S31's corrupt image, S36's unsplittable line, S37's shallow clone and
  S38's raising reader each refuse or report by name, never silently.
- observability: every new refusal names its file, key or class.
- risks: S15 and S14 move two functions other suites monkeypatch; govkit re-imports both names, and
  the selftest's own arms run at the close.
- testing: the probes and fixtures of §6 and the arms of §7.
- migration: §4 "Migration".
- user docs: `help/upgrade-steps.md` (S8, S21, S30) and `help/python-floor.md` (S47, S48), and the
  deploy skill page (S26, S54).

## 6. Acceptance criteria

- **AC1** — When `git grep -n -e "def resolve_landing_base" -e "def derive_push_base" -- tools/govkit`
  runs, it prints one line, the definition in `tools/govkit/upgrade_steps.py`.
  Red when: a second base function survives in either module.
- **AC2** — When `git grep -n "resolve_landing_base(" -- tools/govkit` runs, it prints the calls in
  `cmd_epoch`, `cmd_frozen` and `tools/govkit/step_gate.py`, and `python tools/govkit/step_gate.py --print-base`
  prints the sha `git merge-base origin/main HEAD` prints.
  Red when: one of the three legs resolves its base by its own code.
- **AC3** — When a `python -c` probe parses `tools/govkit/upgrade_steps.py` with `ast`, it finds no
  import of `govkit`, and `git grep -c "^# >>> remote_ladder_py" -- tools/govkit/upgrade_steps.py` prints 1.
  Red when: the step module imports govkit back.
- **AC4** — When `git grep -n -F '{"schema": 3, "files": rows}' -- tools/run-gates/check-receipt.py`
  and `git grep -n -F "receipt: schema {receipt.get('schema')}" -- tools/run-gates/check-receipt.py`
  run, each prints one line.
  Red when: either line moved with TOOL-dSafePassage-8's edit.
- **AC5** — When `git grep -n -F "step-rows-frozen" -- tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/ceiling-evidence.txt memory/map/features/govkit.md`
  runs, each of the five files names the leg.
  Red when: the leg lacks a row a new leg owes its meta-gates.
- **AC6** — When `python tools/codebase-map/gen_map.py --check` runs after the pass, it exits 0.
  Red when: a module this build minted is absent from the generated map.
- **AC7** — When `python tools/govkit/steps/template_size_limits.py witness <t> tools` runs on a
  scratch target that never held the file, and on gov's tree after the pass, each exits 0.
  Red when: the witness requires a before-image that was never written.
- **AC8** — When `python "tools/govkit/shims.py" --fixture --plant window --window 2 --releases 1 --expect held`
  runs, it prints `held` and exits 0; with `--expect allowed` it exits 1.
  Red when: the window plant exits by the held verdict rather than by its match.
- **AC9** — When `bash tools/lib/python-floor.sh down 3.11 <t> <to>` runs on a scratch target whose
  gov-shipped file at the tip holds `v = f"{"X" if c else "y"}"` and whose `<to>` predates it, it
  exits 0; and a `{to}` in an `up` argv is refused by `python tools/govkit/upgrade_steps.py list`
  naming the token.
  Red when: the down grades the tip's bytes, or `{to}` resolves outside a down.
- **AC10** — When the same down runs on a target holding an adopter-owned PEP 701 `.py` no receipt row
  names, it exits 0; with a TOML 1.1 multi-line inline table in `.governance/policy.toml`, it exits 1
  naming that file.
  Red when: the adopter's own files are graded, or the policy file is not.
- **AC11** — When `python tools/lib/python_floor.py check` runs after the pass, it prints nothing and
  exits 0, and `git grep -n -F "Python 3.12 or newer" -- tools/lib/resolve-python.test.sh` prints nothing.
  Red when: an arm's literal plant is a floor statement the scan finds.
- **AC12** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant autocrlf` runs,
  with the parent at `core.autocrlf=true` and a target without `text=auto` holding a CRLF file, the
  step's `git hash-object --path` oid equals the parent's, and the run exits 0.
  Red when: the step hashes with the contract's dropped scopes.
- **AC13** — When `git grep -n "def blob_at" -- tools/govkit` runs, it prints one definition, in
  `tools/govkit/upgrade_steps.py`.
  Red when: a second revision-blob reader is defined.
- **AC14** — When `git grep -n "def write_atomic" -- tools/govkit` runs, it prints one definition, in
  `tools/govkit/upgrade_steps.py`, and `git grep -n "write_atomic(" -- tools/govkit/steps/receipt_schema_4.py`
  prints its call.
  Red when: the step program keeps its own temp-and-rename.
- **AC15** — When `git grep -n -e "derive_introduced(" -e "log.*-S" -- tools/govkit/shims.py` runs, it
  prints the call inside `resolve_shim_landing` and no `-S` pickaxe.
  Red when: the shim landing is found by a substring search.
- **AC16** — When `python "tools/govkit/shims.py" --fixture --plant window-prefix-id` and
  `--plant window-comment-id` run, each exits 0, the landing printed for each id being its own row's
  commit.
  Red when: an id resolves to the commit of a longer id or a comment.
- **AC17** — When `git grep -n 'outbox / f"update-' -- tools/govkit/govkit.py tools/govkit/upgrade_steps.py`
  runs, every hit keyed on a row's path or a step's slug sits inside `write_row_order`.
  Red when: a row-keyed order is written inline.
- **AC18** — When `git grep -n -F '"init", "-q", "-b", "main"' -- tools/govkit/upgrade_steps.py tools/govkit/fixtures/retired_edits.py tools/govkit/upgrade_walk.py tools/govkit/fixture_target.py`
  runs, it prints lines in `tools/govkit/fixture_target.py` only.
  Red when: a new fixture module builds its own scratch repository.
- **AC19** — When `PATH="<stubs>:$PATH" bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`
  runs with every launcher a stub exiting 9009 and `GOV_PYTHON` unset, the first stderr line opens
  `resolve_python: no usable python launcher` and the last is `resolve_python: tried: python3 python py`.
  Red when: an outcome or install line prints after the `tried:` line.
- **AC20** — When `bash tools/check-dead-paths.sh` runs after the pass, it names no hit in
  `tools/govkit/steps.toml`, `tools/govkit/steps/` or the release-0 fixture, and with a planted line
  spelling the retired file's basename in a tracked `.md` outside `memory/` it exits 1 naming it.
  Red when: the exemption is a waiver row, or it hides a prose carrier.
- **AC21** — When `bash tools/check-template-size.sh` runs with a scratch `.governance/policy.toml`
  declaring a non-numeric `budgets` limit, it exits non-zero naming the key, and
  `git grep -n "limits-bad" -- tools/check-template-size.test.sh` prints nothing.
  Red when: an arm still feeds the retired limits file.
- **AC22** — When `git ls-files -- .governance/steps` and `git status --porcelain -- .governance/steps`
  run on gov's tree after the pass, both print nothing, and
  `git grep -n -F "template-size-limits.txt" -- memory/map/generated/CARDS.md` prints nothing.
  Red when: gov's image is committed or left untracked.
- **AC23** — When `python "tools/govkit/step_gate.py" --base HEAD` runs in the prepared merge of
  TOOL-dSafePassage-8's AC5 fixture after a clean `--prepare`, it exits 0 with a non-zero `file` count.
  Red when: the receipt source and the plan source disagree on a landing.
- **AC24** — When `git grep -n -A4 -F '["schema"] = _sch' -- tools/govkit/selftest.py` runs, the block
  shows `pop("steps"`, and so does the block at the forcing to schema 1 for `s1`.
  Red when: a receipt forced below schema 4 keeps `steps`.
- **AC25** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback-update --plant refused`
  runs with `descendant`, `scoped` and `no-base` beside it, the scratch gov's `update` exits 2 under
  each, naming its reason, and `git grep -n -F "[--rollback]" -- skills/deploy-governance/SKILL.md`
  prints the usage line.
  Red when: a rollback refusal exits 1, or the skill's usage omits the flag.
- **AC26** — When `bash tools/unattended/adopt-unattended.sh --check` and
  `bash tools/memory-tree/adopt-memory-tree.sh --check` run in a scratch clone of gov with the receipt
  `update --target . --write` writes and again with it removed, each prints the same lines and exits
  the same way.
  Red when: a source receipt sends `rendered_at` to another path.
- **AC27** — When `python "tools/govkit/fixtures/retired_edits.py" --plant edited-gone-seed` runs, the
  seed row reads `retired-edited` with an outbox order, and the run exits 0.
  Red when: the seed override rewrites the verdict to `patched`.
- **AC28** — When `git grep -n "docs-undocumented.txt" -- .memory-tree.conf` runs, it prints the
  `PROJECT_REGISTRY_EXTRA` member.
  Red when: the file sits in the whitelisted directory unnamed.
- **AC29** — When `python tools/govkit/steps/fanout_cap.py up <t>` runs on a target whose
  `.agent-cap.conf` holds `OTHER=1` and `FANOUT_CAP=2`, it exits 0 leaving `OTHER=1` in the file, and
  on `FANOUT_CAP=abc` alone it exits 1 writing nothing.
  Red when: a key the hook ignores makes the step refuse.
- **AC30** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant truncated-image` runs,
  an image truncated mid-write with no listed path changed is rewritten and the step applies; with a
  listed path changed the up exits 1 naming the image.
  Red when: a corrupt image is kept and read, or discarded over a changed path.
- **AC31** — When `python tools/govkit/govkit.py update --target . --write` runs in a scratch clone of
  gov whose steps file plants a `needs-target = true` row whose witness holds, it exits 0 with the
  row `applied`, and with the witness failing it exits 1 naming the row `attended`.
  Red when: a needs-target row whose witness holds blocks the landing.
  fixture: a scratch clone under `%TEMP%`, the plant `needs-target-source`.
- **AC32** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-foreign-namespace`
  runs over a lock whose `platform` differs from the running one, the take refuses with the holder
  `unknown`, and exits 1.
  Red when: a lock from another pid namespace is reclaimed.
- **AC33** — When `python "tools/govkit/shims.py" --fixture --plant missing-target --lang js` runs, the
  forwarder's exit is 127 and the plant exits 0.
  Red when: the forwarder exits 0 over a target that never started.
- **AC34** — When `python "tools/govkit/shims.py" --fixture --plant py` and `--plant module` run with a
  target importing a sibling module from its own directory, each exits 0.
  Red when: the forwarded target raises `ModuleNotFoundError`.
- **AC35** — When `python "tools/govkit/docs_leg.py" --fixture --plant <case>` runs for
  `console-prompt`, `continued-flag` and `unbalanced-quote`, each exits 1 naming its page and line,
  and for `comment-apostrophe` it exits 0.
  Red when: a prompt, a continuation or a split error is skipped or raises a traceback.
- **AC36** — When `python tools/govkit/upgrade_steps.py list` runs in a scratch shallow clone, it exits
  2 naming `git fetch --unshallow`; in a clone whose descriptor moved, a row's introducing commit is
  the commit that first held it under its old path.
  Red when: a shallow or moved history prints a commit.
- **AC37** — When `python "tools/govkit/step_gate.py" --fixture --plant reader-raises` runs, it exits 2
  naming the class, the side and the error; `--plant base-without-source` exits 0 with that class
  counted as joining.
  Red when: a raising reader exits 1 with a traceback, or an absent source is an error.
- **AC38** — When `python "tools/govkit/fixtures/retired_edits.py" --plant edited-reshipped` runs, the
  row re-shipped by gov reads as a conflict candidate with an order, and the run exits 0.
  Red when: the row stays `retired-edited` while gov ships the path.
- **AC39** — When `bash -c '. tools/unattended/lib-unattended.sh; read_consumes_from "$1"' _ <spec>`
  runs over the specs of TOOL-dSafePassage-3, -8, -12, -11 and `TOOL-dSafePassage-19`, each prints its
  same-order producer named in S40.
  Red when: a same-order dependent pair carries no edge `--dispatch` can wait on.
- **AC40** — When `PATH="<fakes>:$PATH" "<real interpreter>" tools/govkit/govkit.py update --target <scratch adopter> --to HEAD --write`
  runs with the fakes printing `3.14`, the walk stops at `lib/python-floor-3.15` with the preflight's
  refusal as its failure.
  Red when: govkit itself is launched by a fake, so nothing is observed.
- **AC41** — When `git grep -n -F "runtime.agents-in-flight" -- tools/workflows/kit.toml tools/workflows/README.md`
  runs, each file prints its re-worded line.
  Red when: either still tells an adopter to lower the cap in the retired file.
- **AC42** — When the unit's acceptance ledger is read beside the output of
  `git grep -l -F '.agent-cap.conf' -- tools skills` at the pass, it holds one disposition line per
  file the grep prints.
  Red when: a printed file has no disposition.
- **AC43** — When the `ac-order` join of `tools/check-spec-tokens.py` runs over a scratch live spec
  whose §6 lists `AC2` before `AC1`, it names the spec and `AC2`; over this build's live specs it names
  none.
  Red when: an out-of-order criterion passes the join.
- **AC44** — When `python tools/govkit/steps/receipt_schema_4.py up <t>` and then `down <t>` run on
  Windows over a receipt `update` wrote, the bytes after the down equal the bytes before the up, and a
  probe finds no `\r` in them.
  Red when: the program writes in the locale encoding or with CRLF.
- **AC45** — When `git grep -n -e "App Execution Alias" -e "25 ms" -- help/python-floor.md` runs, it
  prints the stated gap and the pinned figure naming `python3`.
  Red when: the page claims the block refuses an alias.
- **AC46** — When `bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh` runs with a fake
  `python3` first on `PATH` that exits 1 under `-I` and 0 without it, the fake is passed over and named
  `did not run`.
  Red when: the probe runs without `-I`.
- **AC47** — When `python tools/lib/python_floor.py check --rev 3708a705` runs, it prints seven
  statements, `tools/lexicon/selftest.py:108` among them.
  Red when: the lexicon comment is missed and the count stays six.
  figure: seven is PINNED at `3708a705`, re-derived by this command.
- **AC48** — When `git ls-tree -r --name-only 3708a705 | wc -l` and
  `git ls-tree -r --name-only 3708a705 -- memory | wc -l` run, they print 5832 and 5382.
  Red when: either figure differs from S50's.
  figure: PINNED at `3708a705`.
- **AC49** — When `git show 3708a705:tools/govkit/selftest.py | grep -c "make_target("` runs, it prints
  80, one of which is the definition at line 679.
  Red when: the count differs, so S51's 79 is wrong.
  figure: PINNED at `3708a705`.
- **AC50** — When `git grep -n 'resolve_kit_dir "$py"' -- tools/push-main.sh` runs, it prints one call,
  inside `resolve_lander_kit`, and the lander stages print their base-run lines unchanged in
  `tools/push-main.test.sh`'s arm.
  Red when: a stage keeps its own copy of the pair.
- **AC51** — When `bash tools/lib/python-floor.sh floor` runs in scratch trees whose `python-floor.txt`
  holds `3.15`, `3.15\nx=1` and `3.\n15`, it prints `3.15` for the first and exits non-zero for the
  others, and `grep -n "python-floor.sh floor" .github/workflows/remote-ci.yml` prints the `floor` step.
  Red when: the workflow reads the file by its own rule.
- **AC52** — When `git grep -n -e "schema 4" -e "upgrade-steps.md" -- skills/deploy-governance/SKILL.md`
  runs, it prints the re-worded receipt paragraph.
  Red when: the skill still says the receipt is at schema 3.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `python resolver (behaviour + inline parity + idiom ban)` · `template size gate selftest` · `dead-path carriers (deleted files still named)` · `dead-path carriers self-test` · `unattended skill wiring` · `row-grammar selftest` · `push-main self-test` · `spec-tokens self-test` · `unattended-build self-test` · `lexicon selftest` · `codebase-map kit selftest` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `verifier fan-out self-test` · `review-join self-test` · `tier2-review self-test` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC9 AC12 AC14 AC27 AC30 AC31 AC32 AC37 AC38 · the self-test runs each fixture plant this unit adds, and its one-writer arms over the widened population, each failing case staged by its plant or a committed direct write · `tools/govkit/refusal_join.py` `BRANCH_PIN`, by the measured count
New arm: tools/lib/resolve-python.test.sh · covers AC19 AC46 · stubs exiting 9009 and a fake that fails only under `-I` · none
New arm: tools/check-template-size.test.sh · covers AC21 · a scratch policy file declaring a non-numeric limit · none
New arm: tools/check-dead-paths.test.sh · covers AC20 · a retiring step's declaration beside a planted prose carrier · none
New arm: tools/check-spec-tokens.test.sh · covers AC43 · a scratch live spec whose criteria run out of order · none
New arm: tools/push-main.test.sh · covers AC50 · each lander stage's base-run lines compared before and after the extraction · none

## 8. Open questions

- **F1 — The window plant's exit contract (S9).** Options: the plant exits as `check_shim_windows`
  would, an exception to TOOL-dSafePassage-6 §4's contract; or one contract for every plant, the
  window plant taking the expected case and printing the observation. The second keeps one contract
  the selftest arm asserts uniformly and satisfies both of that unit's criteria by their observation.
  RESOLVED (agent, 2026-10-23, delegated): the second, on rung 3. widens: none · relaxes: none
- **F2 — The line-ending scopes the contract drops (S13).** Options: carry the parent's effective
  `core.autocrlf` and `core.eol` into the step environment; or forbid a step to stage and leave
  staging to the walk. The second contradicts TOOL-dSafePassage-7's own fixture step, which stages, and
  leaves `git hash-object --path` unequal too. RESOLVED (agent, 2026-10-23, delegated): carry them, on
  rung 3; neither key carries a credential. widens: none · relaxes: none
- **F3 — A `needs-target = true` step under gov first (S32).** Options: (a) in source mode the row's
  witness runs, its up and down staying attended; (b) such a step can never pass gov first and the
  lander refuses with the remedy named. (b) leaves every later build that ships an attended step
  unable to land. RESOLVED (agent, 2026-10-23, delegated): (a), on rung 3; on gov's tree the target
  code is gov's own. widens: none · relaxes: none
- **F4 — How the floor down learns the rollback's `--to` (S10).** Options: a declared placeholder
  `{to}` in the row grammar; an environment name the runner sets. An environment name is outside the
  allowlist TOOL-dSafePassage-7 builds and invisible in the row, which the reader grades. RESOLVED
  (agent, 2026-10-23, delegated): `{to}`, on rung 3, refused outside a rollback's down. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the round-1 spec audit's 39 MEDIUM and 15 LOW
  findings, one scope item per raw id.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 audit of units 15 to 26, written by the disposal stage: `TOOL-dSafePassage-31`, `TOOL-dSafePassage-34`, `TOOL-dSafePassage-35`; no other section moved.
- rev-3 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-41`; no other section moved.

## 10. Reuse audit

The seams extended are named per item: `cmd_epoch`'s ladder and the inline `remote_ladder_py` copy
(`tools/govkit/govkit.py:555-558`, `:13446-13474`), `blob_at` (`:6706`), `write_atomic` (`:4198`),
`planned_writes` through `TOOL-dSafePassage-21`, the seed override (`:9987-9999`), the outbox order
sites (`:10667`, `:10760`, `:10805`), `build_gov17` (`tools/govkit/selftest.py:1728`), the lander's
kit-resolution pairs (`tools/push-main.sh:445`, `:735`, `:763`, `:809`, `:831`), the dead-path
haystack's exclusions (`tools/check-dead-paths.sh:192-195`), `AC_LABEL`
(`tools/check-spec-tokens.py:338`), `read_consumes_from` (`tools/unattended/lib-unattended.sh`) and
`check_app_alias` (`tools/run-gates/measure_legs.py:890`). `python tools/codebase-map/reuse_lookup.py
"list the planned destinations of an accepted deploy plan"` and `"keep a python override launcher name
instead of its resolved executable"` ranked `plan`, `resolve_python` and `resolve_kit_dir`; the
second agrees with source and the first does not rank `planned_writes`, which the batch found by
reading `cmd_plan`. Every other seam was found by reading the line the report cites; where the report
and the source disagreed, `blob_at` sits at `:6706` where the report says `:6704`.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
