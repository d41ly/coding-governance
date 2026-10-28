# TOOL-dSafePassage-26 — the round-1 spec audit's 54 minors: one base rule, one writer each, honest populations, declared exits, and the texts that name them

**Status:** CLOSED · rev-11 · 2026-10-27 · node d · Tier-2 · base 3708a705 · streams tooling · order 6 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-26-deviation-120.md](../build/2026-10-23-build-TOOL-dSafePassage-26-deviation-120.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-26-deviation-72.md](../build/2026-10-23-build-TOOL-dSafePassage-26-deviation-72.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-25-build-TOOL-dSafePassage-1-parent-fixes-return.md](../build/2026-10-25-build-TOOL-dSafePassage-1-parent-fixes-return.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-13 |
| [2026-10-25-build-TOOL-dSafePassage-26-deviation-164.md](../build/2026-10-25-build-TOOL-dSafePassage-26-deviation-164.md) | deviation | — |
| [2026-10-26-build-TOOL-dSafePassage-26-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-26-ledger.md) | journal | — |
| [2026-10-27-build-TOOL-dSafePassage-26-deviation-178.md](../build/2026-10-27-build-TOOL-dSafePassage-26-deviation-178.md) | deviation | — |
| [2026-10-27-build-TOOL-dSafePassage-26-deviation-179.md](../build/2026-10-27-build-TOOL-dSafePassage-26-deviation-179.md) | deviation | — |
| [2026-10-27-build-TOOL-dSafePassage-26-deviation-180.md](../build/2026-10-27-build-TOOL-dSafePassage-26-deviation-180.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-26-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-26-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-26-hygiene-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-26-hygiene-fix.md) | research | TOOL-dSafePassage-24 TOOL-dSafePassage-25 |
| [2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md](../prompts/2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-13 |
| [2026-10-26-prompt-TOOL-dSafePassage-26-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-26-build-brief.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-5-tokens-a-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-5-tokens-a-1-spec-writer.md) | research | TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-17 TOOL-dSafePassage-21 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-61 |
| [2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 |
| [2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-brief.md) | research | TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-8 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-13 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-46 TOOL-dSafePassage-50 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-69 |
| [2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-16 TOOL-dSafePassage-20 TOOL-dSafePassage-15 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-17 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-21 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
exited BLOCKED and BOUNDED with 65 confirmed findings, its 3 blockers and 8 highs units 15 to 25.
This unit is M4's batch of the rest by raw id, 39 MEDIUM and 15 LOW, one scope item per id; ids 18
and 32 were refuted. The minors land on all thirteen units, so it builds after every unit, order 6.
A minor that would bite an earlier pass is named by the hands-off bullet the faulted unit's §3
carries here; where the defect is a built spec's text, the item states the superseding reading and
a criterion here observes it. An item the report marks REJECTED is built from the skeptic's fix.

Report items D-10 to D-42 are MEDIUM and D-43 to D-55 LOW, mapping onto S1 to S54 in order, one id
and one item each, except D-10 (ids 4, 26, 42, 65: S1 to S4), D-12 (8, 37: S6, S7), D-15 (11, 62:
S10, S11), D-20 (29, 61: S16, S17) and D-45 (14, 20, 41: S42 to S44). "Unit N" is
TOOL-dSafePassage-N, each item naming the unit it amends; cites are at base `3708a705` unless stated.

## 2. Scope (IN)

### The base rule (D-10)

- S1. id 4. One base ladder: `resolve_landing_base(root, base)` in
  `tools/govkit/upgrade_steps.py` returns `(sha, boundary, refusal)` from `--base`, else a non-zero
  `GATE_PUSH_BASE`, else the remote ladder's merge-base, `cmd_epoch`'s ladder
  (`tools/govkit/govkit.py:13446-13474`), which prints its lines from the triple. Observed by AC1.
- S2. id 26. The second spelling goes: unit 1's `derive_push_base` and unit 10's copy in
  `govkit.py` become calls of S1's function, and unit 10's AC10 is read as S1's grep of both.
  **Readers:** by name: READER NOT IN TREE — unbuilt unit 1 mints `derive_push_base`, called at its
  landing by `cmd_frozen` and `cmd_epoch` · by value: the bases `kit epoch` and `step-rows-frozen`
  grade, which S3 makes one. Observed by AC1.
- S3. id 42. The step gate, `cmd_epoch` and `cmd_frozen` call S1's function, and nothing else in
  `tools/govkit` resolves a landing's base, so the three grade one range. Observed by AC2.
- S4. id 65. `tools/govkit/upgrade_steps.py` carries the remote ladder inline between `remote_ladder_py`
  markers, byte-identical with its canonical copy under govkit's parity rows
  (`tools/govkit/govkit.py:555-558`), so it imports nothing from `govkit.py` and unit 3's §8 F1 holds. Observed by AC3.

### Built specs re-read (D-11 to D-14)

- S5. id 7. Unit 3's AC12 second clause is read as: `tools/run-gates/check-receipt.py` keeps its
  schema-3 fixture write (`:198`) and schema print (`:437`), unit 8 S6's edit expected. Observed by AC4.
- S6. id 8. `step-rows-frozen` gets every row a new leg owes: `tools/govkit/subject-pins.tsv` by
  `python tools/govkit/govkit.py selfcheck --write`, `tools/run-gates/ceiling-evidence.txt` by
  `python tools/run-gates/derive-ceilings.py --write` over the measured run, and its name in the
  `gate-legs` list of `memory/map/features/govkit.md`. Observed by AC5.
- S7. id 37. `python tools/codebase-map/gen_map.py --write` regenerates `memory/map/generated/`
  over every module this build mints, and `codebase-map coverage + freshness`, which units 1, 5, 10
  and 13 omit, is on §7. Observed by AC6.
- S8. id 9. Moved to TOOL-dSafePassage-61, its S2, on 2026-10-26: it observes only the size-limits step, which
  left TOOL-dSafePassage-1 at that unit's §8 F8 stop. NOT OBSERVED here — TOOL-dSafePassage-61's AC6
  observes it.
- S9. id 10. The window plant of `tools/govkit/shims.py` takes `--expect held|allowed`, prints
  the observation and exits by unit 6 §4's one contract, 0 on a match, else 1; that unit's AC6 and
  AC7 exit columns read as `--expect` values (§8 F1). Observed by AC8.

### The floor down's population (D-15, D-16)

- S10. id 11. The floor step's down grades the files the rollback restores, not the tip's: unit
  1's grammar gains `{to}`, which `resolve_step_argv` resolves (§4 Data model, §8 F4). The floor row's
  down becomes
  `["bash", "{gov}/lib/python-floor.sh", "down", "3.11", "{target}", "{to}"]`, and
  `check_down_floor(target, prior, to_commit)` reads each graded file at `to_commit`. Observed by AC9.
- S11. id 62, the skeptic's fix. The graded population: in an adopter, the receipt's `files`
  rows ending `.py` or `.toml`, read from gov at `to_commit`, plus every `.governance/*.toml` in the
  target, never the adopter's other files; in source mode, gov's tracked set at `to_commit`.
  Observed by AC10.
- S12. id 12. No tracked arm spells a floor statement literally: the plants in
  `tools/lib/resolve-python.test.sh` and unit 12's staged break are assembled at run time, as
  `'Py''thon 3.12 or newer'` is. Observed by AC11.

### The step contract (D-17)

- S13. id 19, the skeptic's fix. `build_step_env` carries the parent's `core.autocrlf` and
  `core.eol` (§4 Data model); unit 7's AC1 reads `GIT_CONFIG_COUNT` as 2 plus those pairs, and its §4
  table names the two keys (§8 F2). Observed by AC12.

### One reader or writer each (D-18 to D-22)

- S14. id 27. `blob_at` (`tools/govkit/govkit.py:6706`) moves into
  `tools/govkit/upgrade_steps.py` beside `Refusal`, govkit imports it back, and unit 1's
  introducing-commit derivation reads through it; the selftest's patching of `gk.blob_at` still
  reaches govkit's callers. Observed by AC13.
- S15. id 28, the skeptic's fix. `write_atomic` (`tools/govkit/govkit.py:4198`) moves into
  `tools/govkit/upgrade_steps.py`, govkit imports it back, and the schema-4 step program and the walk
  write the receipt through it. The one-writer arms of `tools/govkit/selftest.py` (`:16523`,
  `:16630`, `:16644`) parse `upgrade_steps.py` and every `tools/govkit/steps/*.py` beside
  `govkit.py`, their break staged in the file defining `write_atomic`. Observed by AC14.
- S16. id 29. `derive_introduced(root, landed_ref, paths, table, id)` takes its declaring files
  and table, and `resolve_shim_landing` calls it over `tools/govkit/shims.toml` and `shim`, so a
  shim's landing is the first first-parent blob holding a row with that exact id; no `git log -S`
  remains in `tools/govkit/shims.py`. Observed by AC15.
- S17. id 61. The window plants `window-prefix-id` (one id a prefix of another) and
  `window-comment-id` (the id in the header comment at an earlier commit) each resolve to their own
  row's landing. Observed by AC16.
- S18. id 30. One writer of a row-keyed outbox order: `write_row_order` takes the order's key
  and applies `render_order_slug` itself, and the two `update-conflict-` sites
  (`tools/govkit/govkit.py:10667`, `:10805`), the `update-withdrawn-` site (`:10760`) and
  unit 2's `write_attended_order` call it. Unit 9's AC7 is read as AC17. Observed by AC17.
- S19. id 31, the skeptic's fix. The fixtures of `upgrade_steps.py`, `fixtures/retired_edits.py`
  and `upgrade_walk.py` in `tools/govkit/` build targets through `build_target` and synthetic govs
  through `build_scratch_gov` in `tools/govkit/fixture_target.py`, lifted from `build_gov17`
  (`tools/govkit/selftest.py:1728`). `upgrade_walk.py` builds no synthetic gov: its one gov is
  TOOL-dSafePassage-5 S2's `git clone --no-tags` of gov at the pin, whose own `apply` writes
  release-0, so it stays a clone. A local helper that comes to call the factory takes a name of its
  own, `retired_edits.py`'s `build_target` (`:152`) and `upgrade_steps.py`'s (`:2419`) among them: a
  local `build_target` calling it calls itself, as TOOL-dSafePassage-5's fourth pass measured.
  Observed by AC18.

### The resolver's text (D-23)

- S20. id 36. The refusal's first line stays `resolve_python: no usable python launcher` and its
  LAST `resolve_python: tried:<names>`, verbatim, the outcomes, override and install lines between,
  so the two RA7-4 arms of `tools/workflows/unattended-build.test.sh` (`:2413`, `:2417`) and
  `tools/lib/resolve-python.test.sh:76` hold unedited. Observed by AC19.

### Dead paths, size limits, gov's own tree (D-24 to D-27)

- S21. id 38. Moved to TOOL-dSafePassage-61, its S6, on 2026-10-26: it observes only the size-limits step, which
  left TOOL-dSafePassage-1 at that unit's §8 F8 stop. NOT OBSERVED here — TOOL-dSafePassage-61's AC8
  observes it.
- S22. id 39. Moved to TOOL-dSafePassage-61, its S7, on 2026-10-26: it observes only the size-limits step, which
  left TOOL-dSafePassage-1 at that unit's §8 F8 stop. NOT OBSERVED here — TOOL-dSafePassage-61's AC9
  observes it.
- S23. id 40. Moved to TOOL-dSafePassage-61, its S8, on 2026-10-26: it observes only the size-limits step, which
  left TOOL-dSafePassage-1 at that unit's §8 F8 stop. NOT OBSERVED here — TOOL-dSafePassage-61's AC10
  observes it.
- S24. id 43, the skeptic's fix. Unit 10's AC12 is observed on the branch with no receipt,
  through unit 21's plan source, and on a prepared-merge fixture carrying it; its Rollout sentence
  that the receipt lands first is read as: it arrives only in the one landing. Observed by AC23.

### The receipt's readers (D-28 to D-30)

- S25. id 44. The arms at `tools/govkit/selftest.py:8210` and `:8230`, forcing an
  `apply`-written receipt to schema 1 or 2, also take `steps` out, as matrix's `build_role_pair` does.
  Observed by AC24.
- S26. id 46. Unit 4's AC6 is read with exit 2, govkit's `Refusal` code, as
  `tools/govkit/selftest.py:7528-7530` asserts for the downgrade; the usage line of
  `skills/deploy-governance/SKILL.md:89` gains `[--rollback]`. Observed by AC25.
- S27. id 47. Unit 8's table's four omitted receipt readers are graded with gov's source receipt
  present and absent: `rendered_at` in `tools/unattended/adopt-unattended.sh:423-436`
  and `tools/memory-tree/adopt-memory-tree.sh:284-297`, `tools/settings-merge.py:360-372` and
  `tools/memory-tree/row_grammar.py:2576-2578`; a reader whose output differs is fixed here and
  joins the dispatch writes. `unattended skill wiring` and `row-grammar selftest` are on
  §7. Observed by AC26.

### The update verdicts (D-31, D-42)

- S28. id 48, read as unit 9's change: its `SEED_KEPT_VERDICTS` passes `retired-edited` and
  `withdrawn` through the seed override (`tools/govkit/govkit.py:9988-10000`); this pass makes no edit
  and observes unit 9's plant.
  **Readers:** by name: `_cmd_update` in `tools/govkit/govkit.py`, the tuple's one reader · by value:
  NO VALUE READERS — no verdict is withdrawn. Observed by AC27.
- S39. id 67. Moved to TOOL-dSafePassage-64, its S1, on 2026-10-27: unit 5's build-run walk needs
  it before order 6. NOT OBSERVED here — TOOL-dSafePassage-64's AC1 observes it.

### Records and step programs (D-32 to D-35)

- S29. id 49. `.memory-tree.conf`'s `PROJECT_REGISTRY_EXTRA` (`:917`) gains
  `docs-undocumented.txt` with a comment block in the key's form. Observed by AC28.
- S30. id 55, the skeptic's fix. The `agent-cap/fanout-cap-to-agents-in-flight` up keeps the
  shared parser's grammar (`tools/hooks/agent-cap.js:1631-1632`): other keys, blanks and comments
  legal, the last `FANOUT_CAP` winning. It removes only `FANOUT_CAP` lines, deletes the file only when
  just blanks and comments remain, and images the whole file. Witness: no `FANOUT_CAP` assignment in
  `.agent-cap.conf`, or no file. Unit 1's AC12 is read with
  `FANOUT_CAP=abc` alone.
  **Readers:** by name: `read_legacy_fanout` in `tools/policy/policy.py`, whose `FANOUT_LINE` and
  `LEGACY_FANOUT` spell `FANOUT_CAP` and `.agent-cap.conf`, and the files S43's grep prints and
  disposes · by value: `derive_lowered_limit`, which lowers `runtime.agents-in-flight` to that
  line's value where smaller, the value the up carries there. Observed by AC29.
- S31. id 56. `write_before_image` writes through `write_atomic` (S15); an image that does not
  parse is absent only when no path it lists has changed since; otherwise the up exits 1 naming it.
  Observed by AC30.
- S32. id 57, the skeptic's option (a). In source mode `run_step_isolated` runs the `witness` of
  a `needs-target = true` row while its `up` and `down` stay `attended`: on gov's tree the target's
  code is gov's own (unit 7 §4), so an up the owner ran holds at `--prepare`, the row `applied` (§8 F3). Observed by AC31.

### Liveness, forwarders, commands, history, readers (D-36 to D-41)

- S33. id 58. The write lock records `platform` (`sys.platform`) and, under Linux, the kernel's
  `boot_id`; `check_holder_dead` reads a holder `unknown` when either differs from this process's, so
  WSL and Windows runs on one tree never reclaim each other's live lock. Observed by AC32.
- S34. id 59. The `js` forwarder exits 127 printing the error when `spawnSync` sets `error`,
  128 plus the signal's number when it sets `signal`, and `status` otherwise. Observed by AC33.
- S35. id 60. Both `py` forwarders put the target's directory first on `sys.path`, as
  `python <target>` would; the plant's target imports a sibling. Observed by AC34.
- S36. id 63, the skeptic's fix. `read_page_commands`: in a `console` fence only `$ ` or `> `
  lines are commands, the prompt stripped; a trailing backslash joins the next line; in `bash` and
  `sh` fences comments go through `shlex.split(line, comments=True)`; an unsplittable line is a
  finding naming the page and line. Observed by AC35.
- S37. id 64. `read_steps` exits 2 when `git rev-parse --is-shallow-repository` prints `true`,
  naming `git fetch --unshallow`, and reads each walked commit's declaring files from that commit's
  registry and descriptors, never the head's. Observed by AC36.
- S38. id 66. The step gate's reader contract: a reader returns an empty set when its source is
  absent at that revision; one that raises makes the gate exit 2 naming the class, the side (`base`
  or `tip`) and the error. Plants `reader-raises` and `base-without-source`. Observed by AC37.

### The low items

- S40. id 6, the skeptic's fix. The build-order table's `Parallel` column is M6's candidate set.
  Within order 1 unit 1 builds before unit 3; within order 3 unit 11 before unit 8 before unit 12,
  unit 15 before unit 11, and unit 18 before unit 19, each pair a consumes-from edge `--dispatch`
  waits on. Observed by AC39.
- S41. id 13. Unit 11's AC11 is read as: govkit runs under a real interpreter by absolute path,
  the fakes first on the `PATH` the step's isolated environment inherits. Observed by AC40.
- S42. id 14. The comment at `tools/workflows/kit.toml:68` names `runtime.agents-in-flight` in
  place of a tracked `.agent-cap.conf`. Observed by AC41.
- S43. id 20. `.agent-cap.conf`'s by-name readers are derived: the pass disposes each file
  `git grep -l -F '.agent-cap.conf' -- tools skills` prints, re-pointed, re-worded or kept as a
  legacy-home reader under `cl-dClosedLoop-0016`, one ledger line per file. Observed by AC42.
- S44. id 41. `tools/workflows/README.md:28` is re-worded to name `runtime.agents-in-flight`.
  Observed by AC41.
- S45. id 15. `tools/check-spec-tokens.py` gains an `ac-order` join: a live spec whose §6
  labels, read with its `AC_LABEL`, do not ascend is a finding naming the spec and the first label out
  of order; unit 8's AC8 and AC9 are cited by label, which their order does not change.
  Observed by AC43.
- S46. id 17. The schema-4 step program writes through `write_atomic` (S15), UTF-8 with
  `newline="\n"`, so its down's bytes equal its up's input on Windows. Observed by AC44.
- S47. id 21. The resolver block's comment and `help/python-floor.md` say its `[ -f ]` holds on
  an App Execution Alias, so a Store Python whose `sys.executable` is an alias is echoed as printed,
  a gap `check_app_alias` (`tools/run-gates/measure_legs.py:890`) closes and the block does not; the
  perf figure names node d's `python3`, a shim measured at 25 ms to `py`'s 92 ms (PINNED, 2026-10-23). Observed by AC45.
- S48. id 22. `help/python-floor.md` says `-I` is new to the probe; a resolver arm plants a fake
  launcher exiting non-zero under `-I` and zero without, passed over as `did not run`. Observed by AC46.
- S49. id 23. `tools/lexicon/selftest.py:107-109` points at `python-floor.txt`, and
  `FLOOR_STATEMENT_RX` gains the case `no declared Python floor`, so the query at `3708a705` prints
  seven statements, unit 11's AC8 figure read as seven. Observed by AC47.
- S50. id 24. Unit 10 §4's figure reads 5382 of 5832 tracked paths at `3708a705` (PINNED,
  `git ls-tree -r --name-only`, 2026-10-23). Observed by AC48.
- S51. id 25. Unit 5 S12's figure reads 79 `make_target` call sites, the grep's 80 less the
  definition at `tools/govkit/selftest.py:679`. Observed by AC49.
- S52. id 33. `resolve_lander_kit <kit> <file>` in `tools/push-main.sh` echoes the resolved
  interpreter and kit directory or prints the skip reason, and every lander stage resolving a kit calls
  it (`:440`, `:735`, `:763`, `:809`, `:831` and `run_gov_first`), the last turning a missing
  interpreter into a refusal. Observed by AC50.
- S53. id 34. `tools/lib/python-floor.sh floor` is the one shell reader of `python-floor.txt`,
  applying `read_floor`'s rule, exactly `<major>.<minor>` and one optional LF, with no Python; the
  `floor` step of `.github/workflows/remote-ci.yml` runs `floor=$(bash tools/lib/python-floor.sh floor)`.
  Observed by AC51.
- S54. id 45. `skills/deploy-governance/SKILL.md:63` and `:73-75` say the receipt is at schema 4
  with `steps`, reached by `govkit/receipt-schema-4`, pointing at `help/upgrade-steps.md`'s receipt
  section. Observed by AC52.

## 3. Non-goals (OUT)

- Every blocker and high: units 15 to 25.
- Rewriting a closed spec (§1).
- A lint of a step witness's meaning or of every "exits N" claim, and the report's other spec-set
  left-shift lints beyond S45's.
- `merge.<driver>.driver` in the step contract, which unit 24 names uncovered.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — the row grammar, `derive_introduced`, `derive_push_base`, the fan-out step and `step-rows-frozen`
- **consumes-from** `TOOL-dSafePassage-2` — the lock, `write_attended_order` and the walk's fixtures
- **consumes-from** `TOOL-dSafePassage-3` — the schema step program and the receipt's readers
- **consumes-from** `TOOL-dSafePassage-4` — the rollback's refusals and `{to}`'s one phase
- **consumes-from** `TOOL-dSafePassage-5` — `fixture_target.py` and `build_target`
- **consumes-from** `TOOL-dSafePassage-6` — the forwarders and the window plant
- **consumes-from** `TOOL-dSafePassage-7` — `build_step_env`, `resolve_step_argv` and `run_step_isolated`
- **consumes-from** `TOOL-dSafePassage-8` — the source-mode walk and its readers' table
- **consumes-from** `TOOL-dSafePassage-9` — `write_row_order`, `retired-edited` and `SEED_KEPT_VERDICTS`
- **consumes-from** `TOOL-dSafePassage-10` — the step gate and its base
- **consumes-from** `TOOL-dSafePassage-11` — the floor module, its down and the resolver block
- **consumes-from** `TOOL-dSafePassage-12` — the CI workflow's `floor` step
- **consumes-from** `TOOL-dSafePassage-13` — `read_page_commands` and `docs-undocumented.txt`
- **consumes-from** `TOOL-dSafePassage-21` — the `file` class's plan source, beside S24's receipt source
- **consumes-from** `TOOL-dSafePassage-22` — the reclaim's clock rule, to which S33 adds the namespace
- **consumes-from** `TOOL-dSafePassage-23` — the resolver's echo rule, beside S20's refusal lines and S47's alias gap
- **consumes-from** `TOOL-dSafePassage-24` — the contract's repository-scope refusal, beside S13's line-ending keys
- **consumes-from** `TOOL-dSafePassage-25` — `run_gov_first`'s refusal shape, which S52's extraction keeps
- **hands-off** `TOOL-dSafePassage-31` — the lock's pid namespace recorded and judged (finding 13, audit of units 15 to 26)
- **hands-off** `TOOL-dSafePassage-34` — the ac-order join armed by a dated key over a measured population (finding 29, same audit)
- **hands-off** `TOOL-dSafePassage-35` — that audit's minors batch, re-reading this unit's items and adding the namespace verdict's boot rows
- **hands-off** `TOOL-dSafePassage-41` — S45's `ac-order` join, AC43 and its arm, built there with its key, so this pass adds no join (finding 22, audit of units 27 to 35)
- **hands-off** `TOOL-dSafePassage-61` — S8, S21, S22 and S23 (ids 9, 38, 39, 40) and their criteria, which observe only the size-limits step, built there with that step beside `write_atomic`
- **hands-off** `TOOL-dSafePassage-45` — S13 read as "3 plus those pairs" and S33's lock record with `started_boot` and `pid_ns` as unit 42 S10 spells it, keeping unit 32's key (findings 14 and 3, audit of units 36 to 42)

## 4. Design

### Data model

The placeholder `{to}` (S10), beside unit 1's three:

| Placeholder | Resolves to | Phases |
|---|---|---|
| `{to}` | the 40-hex `--to` commit of `update --rollback` | `down` only; any other phase, or a down outside `--rollback`, is a refusal naming the step and the token |

The lock record (S33): `{"pid", "verb", "started", "started_utc", "host", "platform", "boot_id"}`,
`boot_id` read from `/proc/sys/kernel/random/boot_id`, else `""`.

The step environment's carried keys (S13): `GIT_CONFIG_KEY_<n>` = `core.autocrlf` or `core.eol`,
`GIT_CONFIG_VALUE_<n>` the parent's effective value by one `git config --get`, each pair present only
when the parent sets the key.

### Inventory

Minted: `resolve_landing_base` in `tools/govkit/upgrade_steps.py`; `build_scratch_gov` in
`tools/govkit/fixture_target.py`; `resolve_lander_kit` in `tools/push-main.sh`; the verb `floor` on
`tools/lib/python-floor.sh`; the placeholder `{to}`; the lock keys `platform` and `boot_id`; the join
`ac-order`; the plants `window-prefix-id`, `window-comment-id`,
`reader-raises`, `base-without-source`, `console-prompt`,
`continued-flag`, `unbalanced-quote`, `comment-apostrophe`, `truncated-image`, `autocrlf`,
`lock-foreign-namespace`, `needs-target-source` and `missing-target`. Each Python function passes
`py.function` and `resolve_lander_kit` `sh.function`, by `python tools/lexicon/lexicon.py --suggest
<name> --as <cell>` at the pass. Moved, not minted: `blob_at`, `write_atomic`. No conf
key, gate leg or policy key.

### Migration

Additive: the lock's new keys are read only when present, an old lock reading `unknown` only where
its namespace cannot be shown equal (unit 2 §4 "Migration"). No step row has landed at the base, so `{to}` and S30's witness change no frozen row.

### Rollout

Live at landing, at §1's order 6. The items share `govkit.py`,
`upgrade_steps.py` and `selftest.py`, so they do not split into two disjoint write sets by M6.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/govkit/step_gate.py`
- `tools/govkit/shims.py`
- `tools/govkit/docs_leg.py`
- `tools/govkit/steps.toml`
- `tools/govkit/steps/fanout_cap.py`
- `tools/govkit/steps/receipt_schema_4.py`
- `tools/govkit/fixture_target.py`
- `tools/govkit/fixtures/retired_edits.py`
- `tools/govkit/upgrade_walk.py`
- `tools/govkit/subject-pins.tsv`
- `tools/govkit/refusal_join.py`
- `tools/run-gates/ceiling-evidence.txt`
- `memory/map/features/govkit.md`
- `memory/map/generated/` (inventories, MAP, CARDS and symbols)
- `tools/lib/resolve-python.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/lib/python-floor.sh`
- `tools/lib/python_floor.py`
- `tools/lexicon/selftest.py`
- `.github/workflows/remote-ci.yml`
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

The resolver block's inline copies (unit 23 S4) are re-synced in the same commit and join
`--dispatch --writes`, as does any S27 reader fixed.

### Alternatives rejected

- **Two batch units**: no split leaves disjoint write sets (M6 clause 1; §4 Rollout).
- **Folding each minor into its unit's spec**: M4's disposal promotes, never folds.
- **`git log -G` on the id line** (S16): a second reader of one landing fact.
- **Moving `resolve_remote` out of govkit** (S4): another inline copy under one parity gate adds no
  import edge.

## 5. Production-readiness checklist

- security: S13's two keys carry no credential; S32 runs a needs-target witness only on gov's tree;
  `{to}` is refused outside a rollback's down; S33 refuses more reclaims, never fewer.
- perf / scale: one `git config` read per step (S13), one `rev-parse` per `read_steps` (S37).
- error / empty / loading states: S31, S36, S37 and S38 refuse or report by name.
- observability: each new refusal names its file, key or class.
- risks: S14 and S15 move two monkeypatched functions; govkit re-imports both.
- testing: §6 and §7.
- migration: §4 "Migration".
- user docs: `help/upgrade-steps.md` (S30), `help/python-floor.md` (S47, S48), the deploy
  skill page (S26, S54).

## 6. Acceptance criteria

The criteria AC7, AC20, AC21 and AC22 moved to TOOL-dSafePassage-61 on 2026-10-26, as its AC6,
then AC8 to AC10, with S8, S21, S22 and S23, and AC38 moved to TOOL-dSafePassage-64 on 2026-10-27,
as its first criterion, with S39; the labels are not reused here.

- AC1. When `git grep -n -e "def resolve_landing_base" -e "def derive_push_base" -- tools/govkit`
  runs, it prints one line, the definition in `tools/govkit/upgrade_steps.py`.
  Red when: a second base function survives.
- AC2. When `git grep -n "resolve_landing_base(" -- tools/govkit` runs, it prints calls in
  `cmd_epoch`, `cmd_frozen` and the step gate TOOL-dSafePassage-10 creates, and
  `python "tools/govkit/step_gate.py" --print-base` prints the sha of `git merge-base origin/main HEAD`.
  Red when: a leg resolves its base by its own code.
- AC3. When an `ast` probe parses `tools/govkit/upgrade_steps.py`, it finds no `govkit` import,
  and `git grep -c "^# >>> remote_ladder_py" -- tools/govkit/upgrade_steps.py` prints 1.
  Red when: the step module imports govkit.
- AC4. When `git grep -n -F '{"schema": 3, "files": rows}' -- tools/run-gates/check-receipt.py`
  and `git grep -n -F "receipt: schema {receipt.get('schema')}" -- tools/run-gates/check-receipt.py`
  run, each prints one line.
  Red when: unit 8's edit moved either line.
- AC5. When `git grep -n -F "step-rows-frozen" -- tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/ceiling-evidence.txt memory/map/features/govkit.md`
  runs, each of the five files names the leg.
  Red when: a meta-gate row the leg owes is missing.
- AC6. When `python tools/codebase-map/gen_map.py --check` runs, it exits 0.
  Red when: a module this build minted is absent from the map.
- AC8. When `python "tools/govkit/shims.py" --fixture --plant window --window 2 --releases 1 --expect held`
  runs, it prints `held` and exits 0; `--expect allowed` exits 1.
  Red when: the plant exits by its verdict, not its match.
- AC9. When `bash tools/lib/python-floor.sh down 3.11 <t> <to>` runs where a gov-shipped file
  holds `v = f"{"X" if c else "y"}"` at the tip but not at `<to>`, it exits 0; and
  `python tools/govkit/upgrade_steps.py list` refuses a `{to}` in an `up` argv, naming the token.
  Red when: the down grades the tip's bytes, or `{to}` resolves outside a down.
- AC10. When that down runs over an adopter-owned PEP 701 `.py` no receipt row names, it exits 0;
  over a TOML 1.1 multi-line inline table in `.governance/policy.toml`, it exits 1 naming the file.
  Red when: the adopter's own files are graded, or the policy file is not.
- AC11. When `python tools/lib/python_floor.py check` runs, it prints nothing and exits 0, and
  `git grep -n -F "Python 3.12 or newer" -- tools/lib/resolve-python.test.sh` prints nothing.
  Red when: an arm plants a literal floor statement.
- AC12. When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant autocrlf` runs,
  parent at `core.autocrlf=true`, target holding a CRLF file without `text=auto`, it exits 0 with the
  step's `git hash-object --path` oid equal to the parent's.
  Red when: the step hashes with the contract's dropped scopes.
- AC13. When `git grep -n "def blob_at" -- tools/govkit` runs, it prints one definition, in
  `tools/govkit/upgrade_steps.py`.
  Red when: a second revision-blob reader is defined.
- AC14. When `git grep -n "def write_atomic" -- tools/govkit` runs, it prints one definition, in
  `tools/govkit/upgrade_steps.py`, and `git grep -n "write_atomic(" -- tools/govkit/steps/receipt_schema_4.py`
  prints its call.
  Red when: the step program keeps its own temp-and-rename.
- AC15. When `git grep -n -e "derive_introduced(" -e "log.*-S" -- "tools/govkit/shims.py"` runs, it
  prints the call inside `resolve_shim_landing` and no `-S` pickaxe.
  Red when: the shim landing is found by a substring search.
- AC16. When `python "tools/govkit/shims.py" --fixture --plant window-prefix-id` and
  `--plant window-comment-id` run, each exits 0, each id's landing its own row's commit.
  Red when: an id resolves to a longer id's commit or a comment's.
- AC17. When `git grep -n 'outbox / f"update-' -- tools/govkit/govkit.py tools/govkit/upgrade_steps.py`
  runs, every hit keyed on a row's path or a step's slug sits inside `write_row_order`.
  Red when: a row-keyed order is written inline.
- AC18. When `git grep -n -F '"init", "-q", "-b", "main"' -- tools/govkit/upgrade_steps.py "tools/govkit/fixtures/retired_edits.py" "tools/govkit/upgrade_walk.py" "tools/govkit/fixture_target.py"`
  runs, it prints lines in the last path it names, the factory module, only.
  Red when: a fixture module builds its own scratch repository.
- AC19. When `PATH="<stubs>:$PATH" bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`
  runs, every launcher a stub exiting 9009 and `GOV_PYTHON` unset, stderr's first line opens
  `resolve_python: no usable python launcher` and its last is `resolve_python: tried: python3 python py`.
  Red when: any line prints after the `tried:` line.
- AC23. When `python "tools/govkit/step_gate.py" --base HEAD` runs in the prepared merge of unit
  8's AC5 fixture after a clean `--prepare`, it exits 0 with a non-zero `file` count.
  Red when: the receipt and plan sources disagree on a landing.
- AC24. When `git grep -n -A4 -F '["schema"] = _sch' -- tools/govkit/selftest.py` runs, the block
  shows `pop("steps"`, as does the block forcing schema 1 for `s1`.
  Red when: a receipt forced below schema 4 keeps `steps`.
- AC25. When `python3 "tools/govkit/upgrade_steps.py" fixture rollback-update --plant refused`
  runs, and `descendant`, `scoped` and `no-base`, `update` exits 2 under each naming its reason, and
  `git grep -n -F "[--rollback]" -- skills/deploy-governance/SKILL.md` prints the usage.
  Red when: a rollback refusal exits 1, or the skill's usage omits the flag.
- AC26. When `bash tools/unattended/adopt-unattended.sh --check` and
  `bash tools/memory-tree/adopt-memory-tree.sh --check` run in a scratch clone of gov with and without
  the receipt `update --target . --write` writes, each prints the same lines and exit.
  Red when: a source receipt sends `rendered_at` to another path.
- AC27. When `python "tools/govkit/fixtures/retired_edits.py" --plant seed-retired-edited` runs,
  it exits 0, the seed row reading `retired-edited` with an outbox order.
  Red when: the seed override rewrites the verdict to `patched`.
- AC28. When `git grep -n "docs-undocumented.txt" -- .memory-tree.conf` runs, it prints the
  `PROJECT_REGISTRY_EXTRA` member.
  Red when: the registry key leaves the file unnamed.
- AC29. When `python tools/govkit/steps/fanout_cap.py up <t>` runs over an `.agent-cap.conf`
  holding `OTHER=1` and `FANOUT_CAP=2`, it exits 0 leaving `OTHER=1`; over `FANOUT_CAP=abc` alone it
  exits 1 writing nothing.
  Red when: a key the hook ignores makes the step refuse.
- AC30. When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant truncated-image` runs,
  a half-written image with no listed path changed is rewritten and the step applies; with one changed
  the up exits 1 naming the image.
  Red when: a corrupt image is read, or discarded over a changed path.
- AC31. When `python tools/govkit/govkit.py update --target . --write` runs in a scratch clone of
  gov planting a `needs-target = true` row, it exits 0, the row `applied`, when its witness holds, and
  1 naming the row `attended` when not.
  Red when: a needs-target row whose witness holds blocks the landing.
  fixture: a scratch clone under `%TEMP%`, the plant `needs-target-source`.
- AC32. When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-foreign-namespace`
  runs over a lock from another `platform`, the take refuses, holder `unknown`, and exits 1.
  Red when: a lock from another pid namespace is reclaimed.
- AC33. When `python "tools/govkit/shims.py" --fixture --plant missing-target --lang js` runs, the
  forwarder exits 127 and the plant 0.
  Red when: the forwarder exits 0 over a target never started.
- AC34. When `python "tools/govkit/shims.py" --fixture --plant py` and `--plant module` run over
  a target importing a sibling module, each exits 0.
  Red when: the target raises `ModuleNotFoundError`.
- AC35. When `python "tools/govkit/docs_leg.py" --fixture --plant <case>` runs, `console-prompt`,
  `continued-flag` and `unbalanced-quote` each exit 1 naming the page and line, and
  `comment-apostrophe` exits 0.
  Red when: a prompt, continuation or split error is skipped or tracebacks.
- AC36. When `python tools/govkit/upgrade_steps.py list` runs in a scratch shallow clone, it exits
  2 naming `git fetch --unshallow`; where a descriptor moved, a row's introducing commit is the first
  holding it at its old path.
  Red when: a shallow or moved history prints a commit.
- AC37. When `python "tools/govkit/step_gate.py" --fixture --plant reader-raises` runs, it exits 2
  naming the class, the side and the error; `--plant base-without-source` exits 0, that class counted
  as joining.
  Red when: a raising reader tracebacks with exit 1, or an absent source errors.
- AC39. When `bash -c '. "$1"; read_consumes_from "$2"' _ tools/unattended/lib-unattended.sh <spec>`
  runs over the specs of units 3, 8, 12, 11 and 19, each prints its same-order producer named in S40.
  Red when: a same-order pair has no edge `--dispatch` waits on.
- AC40. When `PATH="<fakes>:$PATH" "<real interpreter>" tools/govkit/govkit.py update --target <scratch adopter> --to HEAD --write`
  runs, the fakes printing `3.14`, the walk stops at the step lib/python-floor-3.15 on the
  preflight's refusal.
  Red when: a fake launches govkit itself.
- AC41. When `git grep -n -F "runtime.agents-in-flight" -- tools/workflows/kit.toml tools/workflows/README.md`
  runs, each file prints its re-worded line.
  Red when: either still points an adopter at the retired file.
- AC42. When the acceptance ledger is read beside what `git grep -l -F '.agent-cap.conf' -- tools skills`
  prints at the pass, it holds one disposition line per printed file.
  Red when: a printed file has no disposition.
- AC43. When the `ac-order` join of `tools/check-spec-tokens.py` runs over a scratch live spec
  listing `AC2` before `AC1`, it names the spec and `AC2`; over this build's live specs, none.
  Red when: an out-of-order criterion passes the join.
- AC44. When `python tools/govkit/steps/receipt_schema_4.py up <t>` then `down <t>` run on Windows
  over a receipt `update` wrote, the bytes after equal those before, with no `\r`.
  Red when: the program writes in the locale encoding or with CRLF.
- AC45. When `git grep -n -e "App Execution Alias" -e "25 ms" -- help/python-floor.md` runs, it
  prints the stated gap and the pinned figure naming `python3`.
  Red when: the page claims the block refuses an alias.
- AC46. When `bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh` runs with a fake
  `python3` first on `PATH`, exiting 1 under `-I` and 0 without, the fake is passed over as `did not run`.
  Red when: the probe runs without `-I`.
- AC47. When `python tools/lib/python_floor.py check --rev 3708a705` runs, it prints seven
  statements, `tools/lexicon/selftest.py:108` among them.
  Red when: the lexicon comment is missed, the count six.
  figure: PINNED at `3708a705`.
- AC48. When `git ls-tree -r --name-only 3708a705 | wc -l` and
  `git ls-tree -r --name-only 3708a705 -- memory | wc -l` run, they print 5832 and 5382.
  Red when: a figure differs from S50's.
  figure: PINNED at `3708a705`.
- AC49. When `git show "3708a705:tools/govkit/selftest.py" | grep -c "make_target("` runs, it prints
  80, one being the definition at line 679.
  Red when: the count differs, so S51's 79 is wrong.
  figure: PINNED at `3708a705`.
- AC50. When `git grep -n 'resolve_kit_dir "$py"' -- tools/push-main.sh` runs, it prints one call,
  inside `resolve_lander_kit`, and `git grep -n "resolve_lander_kit" -- tools/push-main.sh` prints a
  call in every stage S52 names; each stage's lines before and after the extraction are the
  push-main arm's comparison, declared on §7's `New arm:` line.
  Red when: a stage keeps its own copy of the pair.
- AC51. When `bash tools/lib/python-floor.sh floor` runs over a `python-floor.txt` of `3.15`,
  `3.15\nx=1` and `3.\n15`, it prints `3.15` for the first and exits non-zero for the others, and
  `grep -n "python-floor.sh floor" .github/workflows/remote-ci.yml` prints the `floor` step.
  Red when: the workflow reads the file by its own rule.
- AC52. When `git grep -n -e "schema 4" -e "upgrade-steps.md" -- skills/deploy-governance/SKILL.md`
  runs, it prints the re-worded receipt paragraph.
  Red when: the skill still says the receipt is at schema 3.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `python resolver (behaviour + inline parity + idiom ban)` · `template size gate selftest` · `dead-path carriers (deleted files still named)` · `dead-path carriers self-test` · `unattended skill wiring` · `row-grammar selftest` · `push-main self-test` · `spec-tokens self-test` · `unattended-build self-test` · `lexicon selftest` · `codebase-map kit selftest` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `verifier fan-out self-test` · `review-join self-test` · `tier2-review self-test` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC9 AC12 AC14 AC30 AC31 AC32 AC37 · its new plants and the widened one-writer arms, each failing case staged by its plant or a direct write · `tools/govkit/refusal_join.py` `BRANCH_PIN`, by the measured count
New arm: tools/lib/resolve-python.test.sh · covers AC19 AC46 · stubs exiting 9009 and a fake that fails only under `-I` · none
New arm: tools/check-spec-tokens.test.sh · covers AC43 · a scratch live spec whose criteria run out of order · none
New arm: tools/push-main.test.sh · covers AC50 · each lander stage's base-run lines compared before and after the extraction · none

## 8. Open questions

- **F1 — The window plant's exit contract (S9).** Options: exit as `check_shim_windows` would, an
  exception to unit 6 §4's contract; or one contract for every plant, the window plant taking the
  expected case and printing its observation, which the selftest asserts uniformly.
  RESOLVED (agent, 2026-10-23, delegated): the second, on rung 3. widens: none · relaxes: none
- **F2 — The line-ending scopes the contract drops (S13).** Options: carry the parent's effective
  `core.autocrlf` and `core.eol` into the step environment; or forbid a step to stage, which unit 7's
  own fixture step does and which leaves `git hash-object --path` unequal. RESOLVED (agent,
  2026-10-23, delegated): carry them, on rung 3; neither key carries a credential. widens: none ·
  relaxes: none
- **F3 — A `needs-target = true` step under gov first (S32).** Options: (a) in source mode its witness
  runs, its up and down staying attended; (b) it never passes gov first, the lander refusing with the
  remedy, so no later build shipping one lands. RESOLVED (agent, 2026-10-23, delegated): (a), on rung
  3; on gov's tree the target code is gov's own. widens: none · relaxes: none
- **F4 — How the floor down learns the rollback's `--to` (S10).** Options: a declared placeholder
  `{to}`; or an environment name the runner sets, outside unit 7's allowlist and invisible in the
  graded row. RESOLVED (agent, 2026-10-23, delegated): `{to}`, on rung 3, refused outside a rollback's
  down. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the Edges gain units 31, 34 and 35 (audit of units 15 to 26).
- rev-3 · 2026-10-23 · §3 · the Edges gain unit 41 (audit of units 27 to 35).
- rev-4 · 2026-10-23 · §3 · the Edges gain unit 45 (audit of units 36 to 42).
- rev-5 · 2026-10-25 · §1 to §10 · trimmed under the class cap (audit P12), from
  `2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md`: §1's table becomes its mapping rule;
  S28 and AC27 read unit 9's `SEED_KEPT_VERDICTS`; trimmed again for the records rows.
- rev-6 · 2026-10-25 · §2 · S30 · the Readers clause re-applied over the trimmed rev-5, which kept
  the hook function `TOOL-dGroundRules-10` removed when it moved the agent limit to
  `tools/policy/policy.py` (hygiene check 25); written by `TOOL-dGroundRules-86`.
- rev-7 · 2026-10-26 · S8 · S21 · S22 · S23 · §3 Edges · §4 Files touched · §5 · AC7 · AC20 · AC21 ·
  AC22 · §7 · the four items and their criteria moved to TOOL-dSafePassage-61, since the size-limits
  step they observe left TOOL-dSafePassage-1 at its §8 F8 stop, by
  `2026-10-26-prompt-TOOL-dSafePassage-61-1-spec-writer.md`.
- rev-8 · 2026-10-26 · AC2 · AC15 · AC18 · AC39 · AC40 · AC49 · AC50 · §7 · the leg line names
  `policy fixtures`, whose guard `tools/govkit/govkit.py` from §4 Files touched trips; the
  criteria quote the files earlier units create, as sibling criteria do, and the git revision
  path; AC39 passes the library as an argument, as AC19 does, so no `;` joins its path; the
  floor step's id leaves backticks; and AC50 observes the calls by grep, the stages' unchanged
  lines staying the push-main arm's, by
  `2026-10-26-prompt-TOOL-dSafePassage-5-tokens-a-1-spec-writer.md`; no other section moved.
- rev-9 · 2026-10-27 · S19 · S19 sent every gov `upgrade_walk.py` builds through
  `build_scratch_gov`, which disagreed with TOOL-dSafePassage-5 S2 and its §8 F1, whose release-0
  is written by the pinned clone's own `apply`; S19 now binds synthetic govs alone and names that
  clone, by `2026-10-27-prompt-TOOL-dSafePassage-5-2-spec-writer.md`; no other section moved.
- rev-10 · 2026-10-27 · S39 · AC38 · §4 Inventory · §7 · S39 and AC38 moved to the new
  TOOL-dSafePassage-64 at order 5, since TOOL-dSafePassage-5's walk measured the sticky
  `retired-edited` role after a rollback and unit 5 builds before this unit, by
  `2026-10-27-prompt-TOOL-dSafePassage-5-6-spec-writer.md`; no other section moved.
- rev-11 · 2026-10-27 · S19 · the local helpers named `build_target` take names of their own when
  they call the factory, since TOOL-dSafePassage-5 rev-10 leaves them to S19 and its fourth pass
  measured a local binding of that name recursing, by
  `2026-10-27-prompt-TOOL-dSafePassage-5-8-spec-writer.md`; no other section moved.

## 10. Reuse audit

Seams extended, each at the line its item cites: `cmd_epoch`'s ladder and the inline
`remote_ladder_py` copy, `blob_at`, `write_atomic`, `planned_writes` through unit 21, the seed
override, the outbox order sites, `build_gov17`, the lander's kit-resolution pairs
(`tools/push-main.sh:445`, `:735`, `:763`, `:809`, `:831`), the dead-path haystack's exclusions
(`tools/check-dead-paths.sh:192-195`), `AC_LABEL` (`tools/check-spec-tokens.py:338`),
`read_consumes_from` and `check_app_alias`.
`python tools/codebase-map/reuse_lookup.py "list the planned destinations of an accepted deploy plan"`
and `"keep a python override launcher name instead of its resolved executable"` ranked `plan`,
`resolve_python` and `resolve_kit_dir`, missing `planned_writes`, found by reading `cmd_plan`. The
report's cites match source but `blob_at`'s, at `:6706` and not `:6704`.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
