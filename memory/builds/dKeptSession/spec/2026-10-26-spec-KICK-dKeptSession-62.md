# KICK-dKeptSession-62 — the round-2 promotions' audit's 32 minor findings, closed after every unit they land on is built

**Status:** OPEN · rev-3 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 33 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-63 KICK-dKeptSession-64 |
| [2026-10-26-build-KICK-dKeptSession-57-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-57-promoted-fix-return.md) | research | KICK-dKeptSession-57 |
| [2026-10-26-build-KICK-dKeptSession-62-deviation-621.md](../build/2026-10-26-build-KICK-dKeptSession-62-deviation-621.md) | deviation | — |
| [2026-10-26-prompt-KICK-dKeptSession-57-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-57-promoted-fix-brief.md) | research | KICK-dKeptSession-57 |
| [2026-10-26-review-KICK-dKeptSession-57-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-57-spec-audit.md) | spec-audit | KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-57 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's twelve round-2 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`)
confirmed 27 findings at MEDIUM and 5 at LOW. BUILD-METHOD M4 promotes them into one batch, and this
is it. Each finding is its own §2 item, named by report id beside its report item:

- MEDIUM: ids 2 (M1), 3, 13, 22 and 25 (M2), 4 (M3), 5 (M4), 6 (M5), 7 (M6), 11 (M7), 12 and 35
  (M8), 14 (M9), 15 and 32 (M10), 19 and 29 (M11), 20 and 27 (M12), 21 and 28 (M13), 24 (M14), 26
  (M15), 33 (M16), 34 (M17), 37 (M18), 38 (M19);
- LOW: ids 8 (L1), 16 and 39 (L2), 30 (L3), 36 (L4).

Three minors are a sibling's defect at another grade: id 33 is H3's at MEDIUM
(`KICK-dKeptSession-59`, whose case its item widens), id 36 is id 6's at LOW, and id 8 is id 38's at
LOW. The minors land on eleven units, so this unit is one write set and takes the order past every
unit of the build (order 33): each item amends code its unit has built. Where an item supersedes a
sibling spec's text, it does so by name, and that unit's acceptance ledger answers the superseded
text.

## 2. Scope (IN)

- **S1** — id 2, M1. Units 49, 50 and 54 add `check_policy.py` arms and units 52, 53 and 55 add loop
  selftest arms, and `KICK-dKeptSession-56` S25 and S27's lists omit all six. Those lists gain them by
  name, and at this unit's pass each of the six units' ledgers gains one OBSERVED line by
  `KICK-dKeptSession-57` S3's rule, naming `policy fixtures` (49, 50, 54) or `loop selftest` (52,
  53, 55) as the leg that runs its arm at the close. Observed by AC1.
- **S2** — id 3, M2. `KICK-dKeptSession-56` AC15's `grep -c 'claude --version'` is superseded by the
  invocation's count, as `KICK-dKeptSession-37` AC1 pins it: `grep -c 'claude --version </dev/null'
  manifest-check.sh` prints `1`, inside `read_claude_version`. Observed by AC2.
- **S3** — id 13, M2. `KICK-dKeptSession-56` S36's "spells `claude --version` once" reads "runs
  `claude --version` once", and AC15's Red-when loses "as at base": base already runs it once, at
  `skills/session-kickoff/manifest-check.sh:419`. Observed by AC2.
- **S4** — id 22, M2. AC15's range check "no `--version`" reads "`derive_cli_line`'s body runs no
  `claude --version` command", observed as no `timeout ... claude --version` line in that range.
  Observed by AC3.
- **S5** — id 25, M2. The two `cli — skipped:` messages (`manifest-check.sh:422`, `:427`) and the
  three comments keep their text, and `manifest-check.test.sh:1093` and `:1097`, which pin the
  messages byte for byte, stay unchanged. Observed by AC3.
- **S6** — id 4, M3. `KICK-dKeptSession-56` S21's scan reads "filtered by `src` main and by kind
  `usage` and `compact`; the model test applies to usage events only, and a compact event joins by
  `KICK-dKeptSession-47` S1's newest-prior-usage rule over the unfiltered sorted list". Observed by
  AC4.
- **S7** — id 5, M4. `KICK-dKeptSession-56` AC10 counts calls of `derive_main_transcripts` made from
  inside `derive_context_window`, never `build_session_tree`, which unit 9 and the measures also
  call: one across the 22 rows of one model and root, 22 unmemoised. Observed by AC5.
- **S8** — id 6, M5. `KICK-dKeptSession-56` S11's memo keys on the RESOLVED root: a `None` root is
  resolved by `resolve_projects_root()` before the lookup, so two `CLAUDE_CONFIG_DIR` values give two
  entries. Observed by AC6.
- **S9** — id 7, M6. `KICK-dKeptSession-56` S33 re-posts the missing notices oldest first and before
  the transition's own notice in the same run, and skips a re-post whose subject a newer posted notice
  to the same dependent already carries under another content key. Observed by AC7.
- **S10** — id 11, M7. `KICK-dKeptSession-46` S3's root for `runlog.py context <transcript>` is the
  projects dir the file sits in by its shape: the parent's parent for a main transcript, and four
  levels up for `<dir>/<project>/<sid>/subagents/agent-*.jsonl`. Observed by AC8.
- **S11** — id 12, M8. `KICK-dKeptSession-47` S1's compaction joins `model`'s observation only when
  its own `src` is `main` and the newest main usage before it is on `model`; a compaction from a
  merged `subagents/agent-*.jsonl` file joins no model. Observed by AC9.
- **S12** — id 35, M8. The same holds for a main-file record carrying `isSidechain`, which
  `extract_session` relabels `agent` (`tools/runlog/extract.py:881-882`). Observed by AC10.
- **S13** — id 14, M9. `KICK-dKeptSession-56` AC21's unbounded half is staged by a failing stub
  `timeout` first on `PATH`, so the probe at `tools/unattended/unattended.sh:183` sets
  `REMOTE_BOUND_LIVE=0` and lines 186 and 521 carry it into `GATE_BOUND_LIVE`; an exported
  `GATE_BOUND_LIVE=0` is overwritten there. The 12 s bound is timed once on the fixture and written
  as PINNED with its date. Observed by AC11.
- **S14** — id 15, M10. `KICK-dKeptSession-55`'s guard decides from unit 55 S1's one `--mail read
  <slug> --open` row set, less the ids its acks landed, so `write_transition` runs one bounded fetch per
  transition; unit 55 §5's price and `KICK-dKeptSession-5` S9's own read under the writer read as
  this item. A row arriving after that read is read at the next transition. Observed by AC12.
- **S15** — id 32, M10. The acks land all or nothing: `--mail ack <slug> <id> [<id> ...]` builds one
  commit per ack, chained on the session ref's tip, and `write_mail_ref` lands the chain with one
  `write_gov_ref` (`KICK-dKeptSession-5` S2), so a refused record or a lost update leaves every row
  open. `KICK-dKeptSession-55` §4's per-row loop reads as this one call. Observed by AC13.
- **S16** — id 29, M11. `KICK-dKeptSession-56` S1's Python Edges reader names, in its docstring and
  unit 56 §10, the two readers it must agree with: `read_consumes_from`
  (`tools/unattended/lib-unattended.sh:348`) and the hygiene extractor
  (`tools/memory-tree/check-memory-hygiene.sh:2474`), and their rules: a column-0 bullet, the first
  backticked token only, `external` skipped, `none` held across wrapped lines, an id-less payload
  unreadable. Observed by AC14.
- **S17** — id 19, M11. A cross-language case in the build-index selftest runs that reader and
  `read_consumes_from --scan` over one set of fixture Edges blocks (a wrapped `none` bullet holding a
  backticked id, an `external` edge, an unreadable payload) and reds on any difference; AC1 of unit 56
  gains the wrapped-`none` variant. Observed by AC15.
- **S18** — id 20, M12. `KICK-dKeptSession-56` S21's callers of `derive_main_transcripts` include
  `scan_preflights` (`tools/runlog/extract.py:991`), and AC18 counts the construct:
  `glob("*/*.jsonl")` appears once in `extract.py`, inside `derive_main_transcripts`. Observed by AC16.
- **S19** — id 27, M12. `derive_main_transcripts` carries `_check_inside` (`extract.py:176`), the
  stricter rule `scan_preflights` applies today, and its docstring says so, so the window scan refuses
  a transcript linked from outside the root. Observed by AC17.
- **S20** — id 21, M13. The inline-parity arm of `tools/lib/resolve-python.test.sh` reads JS: `blk`
  takes `// >>> <stem>` and `// <<< <stem>` markers, the copy population adds `*.js`, and
  `PARITY_ROWS` gains one row per copied function with `tools/hooks/scratch-guard.js` as canonical.
  Observed by AC18.
- **S21** — id 28, M13. `KICK-dKeptSession-56` S23's copied closure is `readCard`,
  `buildComparablePath` and `extractRouteUnits` (`scratch-guard.js:667`, `:166`, `:839`), each
  inside a marker pair in both files. Observed by AC19.
- **S22** — id 24, M14. `tools/check-spec-tokens.py` carries `extract_files_touched` and its closure,
  `FILES_HEAD`, `TICK`, `NOT_A_TOKEN`, `derive_dir_segments`, `check_dir_shaped`, `check_path_shaped`
  and `check_guard_trips`, inside one `# >>> files_touched_py` block, moved together; `PARITY_ROWS`
  gains `files_touched_py`, canonical `tools/check-spec-tokens.py`, excluding `tools/check-spec-tokens`,
  for `KICK-dKeptSession-56` S2's copy. Observed by AC20.
- **S23** — id 26, M15. `KICK-dKeptSession-56` AC23's grep covers both one-argument spellings, and
  the four fixtures holding `render_scaffold`'s callers run. Observed by AC21.
- **S24** — id 33, M16. `policy-mirror.js` gains `MIRROR_LEGACY_INPUTS`, a copy of `LEGACY_INPUTS`,
  and `readMirrorAt` expects the policy file, the catalogue, `MIRROR_KIT_INPUTS` and
  `MIRROR_LEGACY_INPUTS`, never the stored mirror's own keys. `KICK-dKeptSession-59`'s
  `mirror-input-parity` compares the whole JS list with `derive_mirror_inputs()`. Observed by AC22.
- **S25** — id 34, M17. `KICK-dKeptSession-47` S1's fold skips a compaction whose `pre_tokens` is
  `None` (`_derive_int`, `extract.py:157-158`); the scenario `context-window-compact-malformed` holds
  one. Observed by AC23.
- **S26** — id 37, M18. The runlog selftest gains a class arm: every variable name `extract.py` reads
  through `env.get`, `env[...]` or `os.environ` is in `DECOY_VARS`, set by `build_arm_env`, or unset
  at import beside the `GIT_*` scrub (`KICK-dKeptSession-56` S16). At this unit's pass the window
  criteria of units 46 and 47 are re-observed with `CLAUDE_CODE_MAX_CONTEXT_TOKENS` unset, each
  recorded in this unit's ledger. Observed by AC24.
- **S27** — id 38, M19. `KICK-dKeptSession-45` AC2's no-second-spelling check is scoped to code: the
  `derive_context_window` range, from its `def` to the next top-level `def`, read with its
  docstring's lines left out of the grepped text, matches neither `expanduser` nor `\.claude`. Observed by AC25.
- **S28** — id 8, L1. That range check reads `.claude` in either quote style, and the whole-file
  `grep -c '".claude"'` keeps its base figure beside it, `1` at line 198. Observed by AC25.
- **S29** — id 16, L2. `KICK-dKeptSession-45` §4 Evidence's second bullet reads: the literal ignores
  `CLAUDE_CONFIG_DIR`, the decoy it misses, while `build_arm_env` also decoys `HOME` and `USERPROFILE`.
  NOT OBSERVED: an evidence sentence with no behaviour; unit 45's ledger answers it by this name.
- **S30** — id 39, L2. `KICK-dKeptSession-45` AC1's probe aims every `DECOY_VARS` member but
  `CLAUDE_CONFIG_DIR` at the empty directory, `HOME` and `USERPROFILE` among them. Observed by AC26.
- **S31** — id 30, L3. `render_order`'s docstring in `tools/memory-tree/gen_build_index.py` reads:
  units sharing an `order` value are candidates for one parallel group, and the Parallel cell names
  why a group is not one. §8 F1 records the two template texts. Observed by AC27.
- **S32** — id 36, L4. `KICK-dKeptSession-56` S11's memo lives within one process, as
  `functools.lru_cache`, and the runlog selftest calls its `cache_clear` between in-process cases; a
  transcript added between two calls on one root is not seen by the second, as its docstring states.
  Observed by AC6.

## 3. Non-goals (OUT)

- The fixes of ids 1, 9, 10, 23 and 31: units 57 to 61.
- Rewording sibling specs: each superseded text is named here and answered in its unit's ledger.
- The report's left-shift checklist entries and hygiene arms: no clause of this build names the
  bug-class checklist, and each arm is a separate gate, so a separate unit by M2. Where an item's
  criterion is the class arm, it says so (S20, S26).
- Renumbering any order.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `--mail ack`, `write_mail_ref` and S9's guard read, S14 and S15 (ids 15, 32)
- **consumes-from** `KICK-dKeptSession-45` — AC1, AC2 and §4's evidence, S27 to S30 (ids 38, 8, 16, 39)
- **consumes-from** `KICK-dKeptSession-46` — the context verb's root and AC1, S10 and S26 (ids 11, 37)
- **consumes-from** `KICK-dKeptSession-47` — the fold's compaction rule and its criteria, S6, S11, S12, S25 and S26 (ids 4, 12, 35, 34, 37)
- **consumes-from** `KICK-dKeptSession-48` — the owner's variable advice, whose ambient value S26's arm guards (id 37)
- **consumes-from** `KICK-dKeptSession-49` — `readMirrorAt`'s expected list and its arm's leg, S24 and S1 (ids 33, 2)
- **consumes-from** `KICK-dKeptSession-50` — the `mirror-upgrade` arm's leg, S1 (id 2)
- **consumes-from** `KICK-dKeptSession-52` — the `notices-repeat-key` arm's leg, S1 (id 2)
- **consumes-from** `KICK-dKeptSession-53` — the chain's arm's leg, and the order S9's re-posts take, S1 and S9 (ids 2, 7)
- **consumes-from** `KICK-dKeptSession-54` — the restated cases' arm's leg, S1 (id 2)
- **consumes-from** `KICK-dKeptSession-55` — the listed rows, the guard's read and the ack loop, S1, S14 and S15 (ids 2, 15, 32)
- **consumes-from** `KICK-dKeptSession-56` — S1, S2, S11, S16, S21, S23, S25, S27, S28, S33 and S36 with AC10, AC15, AC18, AC21 and AC23, S1 to S9, S13, S16 to S24, S26, S31 and S32 (ids 2, 3, 13, 22, 25, 4, 5, 6, 7, 14, 29, 19, 20, 27, 21, 28, 24, 26, 37, 30, 36)
- **consumes-from** `KICK-dKeptSession-57` — S3's ledger rule, which S1 runs for the six units it adds (id 2)
- **consumes-from** `KICK-dKeptSession-59` — the `mirror-input-parity` case, which S24 widens to the whole list (id 33)
- **hands-off** external — the two template texts of S31, `memory/TEMPLATE-SPEC.md:84` and `tools/memory-tree/SPEC-TEMPLATE.template.md:84`, governance carriers BUILD-METHOD M3's veto 2 reserves to the owner (§8 F1)
- **hands-off** `KICK-dKeptSession-63` — S1, S15, S19, S20, S22, S24, S26, S31, AC20, AC25 and §7's leg line, which the batch's S1 to S5, S8, S9, S12 to S18, S21 and S23 to S26 amend (ids 4, 10, 24, 2, 20, 11, 13, 15, 18, 21, 25, 26, 27, 5, 9, 22, 23, 30, 31)
- **hands-off** `KICK-dKeptSession-64` — S19, S31, §5's "seven definitions" and S15 and §4's ack-chain sketch, whose ledger answers the batch's S4 reads (id 1)

## 4. Design

### Evidence

Each item's evidence is the audit's appendix row for its id, re-read for this spec on 2026-10-26.
The claims re-verified at this base: `manifest-check.sh` spells `claude --version` on lines 222,
405, 419, 422, 427 and 491, and only 419 runs it; `manifest-check.test.sh:1093` and `:1097` pin
the two skip messages; `unattended.sh:183` probes `timeout`, and lines 186 and 521 assign
`GATE_BOUND_LIVE=$REMOTE_BOUND_LIVE` at top level; `extract.py` builds the compact item with `src`
first (`:743-744`), copies it into an event with no `model` (`:819-821`), relabels a sidechain
record (`:881-882`), and spells `glob("*/*.jsonl")` at `:1002`, `:1135` and `:1209`, the first inside
`scan_preflights` with `_check_inside`; `build_arm_env` copies `os.environ` and decoys `DECOY_VARS`
(`selftest.py:348-349`, `:1515-1520`); `scratch-guard.js` defines `buildComparablePath` at `:166`,
`readCard` at `:667` and `extractRouteUnits` at `:839`; `resolve-python.test.sh`'s `blk` (`:213`)
and copy grep (`:218`) read only `# >>>` markers in `*.sh`, `*.py`, `.githooks/*` and
`WIRE-INTO-PROJECT.md`; `check-spec-tokens.py` holds `TICK` (`:286`), `NOT_A_TOKEN` (`:290`),
`FILES_HEAD` (`:325`), `extract_files_touched` (`:530`), `derive_dir_segments` (`:560`),
`check_dir_shaped` (`:571`), `check_guard_trips` (`:581`) and `check_path_shaped` (`:1122`), with
markers only for `resolve_prefix_token` and `resolve_kit_dir`; `render_order`'s docstring
(`gen_build_index.py:1716`). dGroundRules' files are read at `3c8c4718a`: `render_scaffold`'s
callers at `check_policy.py:1230` (`adopter-fresh-target`), `:1498-1499` (`arms-empty-target`),
`:2212` (`mirror-absent-adopter`) and `:4439` (`build_repo`, every plant case), and
`policy-mirror.js:111`'s `Object.keys(doc.legacy_blobs)`.

### The memo

```
@functools.lru_cache(maxsize=None)
def _derive_window(model, root_resolved, variable): ...
def derive_context_window(model, root=None):
    root = resolve_projects_root() if root is None else root   # S8: resolved before the lookup
    return _derive_window(model, str(root), os.environ.get("CLAUDE_CODE_MAX_CONTEXT_TOKENS"))
```

### The ack chain

```
--mail ack <slug> a b      tip T
  c_a := build_gov_commit T   <ack a>
  c_b := build_gov_commit c_a <ack b>
  write_gov_ref <ref> T c_b    -> one update: both land, or neither (rc 1 lost, rc 2 not completed)
```

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `MIRROR_LEGACY_INPUTS` | constant | `tools/policy/policy-mirror.js` |
| `files_touched_py` | parity marker stem | `tools/check-spec-tokens.py`, `tools/memory-tree/gen_build_index.py` |
| `read_card_js`, `build_comparable_path_js`, `extract_route_units_js` | parity marker stems | `tools/hooks/scratch-guard.js`, `tools/unattended/mail-notice.js` |
| `context-window-compact-sidechain`, `context-window-compact-agent`, `context-window-compact-malformed` | fixture scenarios | `tools/runlog/fixtures/transcripts.json` |
| `edges-agreement` | selftest case | `tools/memory-tree/gen_build_index.py`'s selftest |

### Migration

None: no stored state changes shape. S15's acks are the records unit 5 already writes, landed by one
ref update.

### Files touched (estimate)

- `tools/runlog/extract.py`, `tools/runlog/runlog.py`, `tools/runlog/selftest.py`,
  `tools/runlog/fixtures/transcripts.json`
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`,
  `tools/unattended/mail-notice.js`, `tools/unattended/VERBS.template.md`
- `tools/hooks/scratch-guard.js`: S20 and S21, marker comments only
- `tools/lib/resolve-python.test.sh`, `tools/check-spec-tokens.py`,
  `tools/memory-tree/gen_build_index.py`
- `tools/loop/loop_transition.py`, `tools/loop/selftest.py`
- `tools/policy/policy-mirror.js`, `tools/policy/check_policy.py`
- `memory/builds/dKeptSession/build/`: the ledger lines of S1 and S26

### Alternatives rejected

- **Two batches.** S1 and S26 write ledgers of units in both the policy and the runlog sets, and S20
  and S22 share `resolve-python.test.sh`'s `PARITY_ROWS` with S16 and S17's `gen_build_index.py`, so
  no two write sets are disjoint by M6's clauses.
- **One ack message whose `answers` lists every id, for S15.** It changes unit 5's record grammar,
  which S7's state derivation and the id derivation read; §8 F2 records it.

## 5. Production-readiness checklist

- security — S19 refuses a transcript linked from outside the root; S20 and S22 gate two copies that
  had no parity check; S15 writes the records unit 5 already validates.
- perf / scale — S14 removes one bounded fetch per transition; S8 and S32 keep one scan per model
  and root.
- error / empty / loading states — S11, S12 and S25's compactions join no model; S15's refusal
  leaves every row open; an absent JS literal reds S24's case.
- observability — S16 names the readers S1 must match; S26's arm names the variable it found.
- risks — S22 moves seven definitions inside `check-spec-tokens.py` into one block, a reorder with
  no behaviour change, observed by its own self-test.
- testing — the criteria of §6 and the arms of §7.
- migration — §4.
- user docs — `tools/unattended/VERBS.template.md`'s `--mail ack` line names several ids, S15.

## 6. Acceptance criteria

Fixtures are each repaired unit's own, named by that unit's spec, under `%TEMP%`.

- **AC1** — When the ledgers of units 49, 50 and 54 are read at this unit's pass, each names `policy
  fixtures`, and those of units 52, 53 and 55 each name `loop selftest`.
  Red when: an arm's unit records no leg that runs it.
- **AC2** — When `grep -c 'claude --version </dev/null' manifest-check.sh` runs in
  `skills/session-kickoff/`, it prints `1`, on a line inside `read_claude_version`'s range.
  Red when: a second invocation is written.
  figure: PINNED, `1` at base too, line 419, read 2026-10-26.
- **AC3** — When `awk '/^derive_cli_line\(\) \{/,/^\}/' manifest-check.sh | grep -c 'timeout .*
  claude --version'` runs, it prints `0`, and `grep -c 'cli — skipped: claude --version'
  manifest-check.sh` prints `2`.
  Red when: the body still runs the binary, or a skip message was reworded to green a count.
- **AC4** — When `runlog.py context` reads `context-window` from a root holding
  `context-window-compact-own`, it prints `15%`, and from one holding `context-window-compact-other`,
  `75%`.
  Red when: a scan pre-filtered by model drops every compaction or keeps another model's.
- **AC5** — When a probe counts calls of `derive_main_transcripts` from `derive_context_window` over
  unit 9's 22-row fixture of one model and root, it records `1`.
  Red when: an unmemoised copy records `22`.
- **AC6** — When a probe calls `derive_context_window("fixture-model")` in one process under two
  `CLAUDE_CONFIG_DIR` values, it returns two windows, and after `cache_clear` a transcript added
  between two calls on one root is seen.
  Red when: a memo keyed on `None` returns the first window twice.
- **AC7** — When unit 56's AC28 plant runs and the parent's next transition re-posts the refused
  notice, `--mail read <dependent>` shows the re-post with a lower `seq` than that transition's own
  notice, and the dependent's next `python loop_transition.py record` succeeds with both rows acked.
  Red when: the re-post lands after the current notice and stays open.
- **AC8** — When `runlog.py context` reads an agent transcript under `<dir>/<project>/<sid>/subagents/`,
  it prints the share unit 9's `--orient <dir>` row prints for that file.
  Red when: the root resolves to `<sid>` and the share reads the bottom rung.
- **AC9** — When `runlog.py context` reads `context-window` from a root holding
  `context-window-compact-agent`, a 900000-token compaction in a `subagents/agent-*.jsonl` file after a
  main usage on `fixture-model`, it prints `75%`.
  Red when: the agent's compaction lifts the main model to `15%`.
- **AC10** — When the same read runs from a root holding `context-window-compact-sidechain`, the
  compaction an `isSidechain` record in the main file, it prints `75%`.
  Red when: the relabelled record joins the main model.
- **AC11** — When `bash unattended.sh --landed <slug>` runs with a failing stub `timeout` first on
  `PATH` and a progress stub that runs `sleep 30 &`, it returns within the PINNED bound and still
  emits.
  Red when: the run takes the live `timeout` path, so the unbounded half is never reached.
  figure: PINNED, the bound timed once on the fixture at the build and written with its date.
- **AC12** — When a probe records the `--mail read` subprocesses of one `python loop_transition.py
  record`, it records one.
  Red when: the guard runs a second fetch.
- **AC13** — When the second of two acks is planted to fail its record check, `--mail ack <slug> <a>
  <b>` exits non-zero and `--mail read <slug>` shows both rows `open`.
  Red when: a per-row loop leaves the first ack landed.
- **AC14** — When `grep -n "read_consumes_from" gen_build_index.py` runs in `tools/memory-tree/`, it
  prints the Edges reader's docstring line naming it and `check-memory-hygiene.sh`.
  Red when: the reader names no rule it must match.
- **AC15** — When the build-index selftest's `edges-agreement` case runs, the Python reader and
  `read_consumes_from --scan` print one edge set over the three fixture blocks.
  Red when: a copy of the Python reader that reads a wrapped `none` bullet's id as an edge reds it.
- **AC16** — When `grep -c 'glob("\*/\*.jsonl")' extract.py` runs in the runlog kit, it prints `1`,
  inside `derive_main_transcripts`.
  Red when: `scan_preflights` keeps its own spelling of the population.
- **AC17** — When a fixture root holds a transcript linked from outside it, `derive_main_transcripts`
  omits it.
  Red when: the window scan reads a file `scan_preflights` refuses.
- **AC18** — When the inline-parity arm runs over a scratch tree whose `mail-notice.js` copy of
  `readCard` is staged to differ by one byte, it reds naming `read_card_js`.
  Red when: the JS copy drifts with no red.
- **AC19** — When `node mail-notice.js` runs from a scratch install holding only the unattended kit's
  files and a card, it exits 0.
  Red when: a copy lacking `buildComparablePath` throws `ReferenceError`.
- **AC20** — When the parity arm runs over a scratch tree whose `gen_build_index.py` copy of the
  `files_touched_py` block differs by one byte, it reds naming `files_touched_py`.
  Red when: the canonical block is missing, or the copy drifts with no red.
- **AC21** — When `grep -cE 'render_scaffold\((rows|policy\.load_catalogue\(KIT\))\)'
  check_policy.py` runs in the policy kit, it prints `0`, and `python check_policy.py --fixture` runs
  `adopter-fresh-target`, `arms-empty-target`, `mirror-absent-adopter` and `mirror-hand-edited`, each
  exiting 0.
  Red when: a caller still passes one argument and raises `TypeError`.
- **AC22** — When a planted mirror whose `legacy_blobs` lacks the `.agent-cap.conf` key is read by
  `node policy-mirror.js get hooks.bypass`, it reports the mirror stale, and `--fixture
  mirror-input-parity` reds on a copy adding a path to `LEGACY_INPUTS` alone.
  Red when: the missing key reads FRESH, or the one-sided addition passes.
- **AC23** — When `runlog.py context` reads `context-window` from a root holding
  `context-window-compact-malformed`, it prints `75%` and exits 0.
  Red when: `max()` over `None` raises `TypeError`.
- **AC24** — When the runlog selftest's environment arm runs over a copy of `extract.py` adding
  `env.get("RUNLOG_PLANTED")`, it reds naming that variable, and this unit's ledger records units 46
  and 47's window criteria re-observed with `CLAUDE_CODE_MAX_CONTEXT_TOKENS` unset.
  Red when: a variable the code reads reaches a case from the machine.
- **AC25** — When the `derive_context_window` range of `extract.py`, its docstring removed, is
  grepped with `grep -cE 'expanduser|\.claude'`, it prints `0`, and `grep -c '".claude"' extract.py`
  prints `1`.
  Red when: a copy keeping `os.path.expanduser("~/.claude/projects")`, or a single-quoted
  `'.claude'`, as a fallback passes.
  figure: PINNED, the whole-file `1` at base is line 198, read 2026-10-26.
- **AC26** — When `KICK-dKeptSession-45` AC1's probe runs with `HOME`, `USERPROFILE`, `LOCALAPPDATA`
  and `XDG_STATE_HOME` aimed at the empty directory, it prints `(1000000, 'observed 900000 on
  fixture-model')`.
  Red when: a copy defaulting to the profile's `.claude/projects` reads the owner's real profile.
- **AC27** — When `grep -n "candidates for one parallel group" gen_build_index.py` runs in
  `tools/memory-tree/`, it prints `render_order`'s docstring.
  Red when: the docstring still says a shared order is the parallel group.

## 7. Gates

`build-index selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `memory-hygiene self-test` · `spec-tokens self-test` · `tier2-review self-test` · `unattended kit gate` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The policy kit's `policy fixtures` leg runs its cases once dGroundRules has landed it, and the loop
kit's `loop selftest` leg its cases once dDeclaredLoop has landed it; the arm lines below declare
them.

New arm: tools/runlog/selftest.py · covers AC4 AC5 AC6 AC8 AC9 AC10 AC16 AC17 AC23 AC24 · the scenarios of S11, S12 and S25, an agent transcript, two config roots, a linked transcript and a planted variable · none
New arm: tools/loop/selftest.py · covers AC7 AC12 · a re-post beside the current notice and a recorded fetch count · none
New arm: tools/unattended/unattended.test.sh · covers AC11 AC13 · a failing stub `timeout` and a planted second ack · `FLOOR_ASSERTIONS` and its shard floor rise by the arm's count, counted off the diff
New arm: tools/memory-tree/gen_build_index.py · covers AC15 · the three fixture Edges blocks, staged red by a reader taking a wrapped `none` bullet's id · none
New arm: tools/lib/resolve-python.test.sh · covers AC18 AC20 · one-byte edits to the JS and Python copies · none
New arm: tools/policy/check_policy.py · covers AC21 AC22 · the four scaffold callers' fixtures and a mirror missing its legacy key · none

## 8. Open questions

- **F1 — How do the texts that say a shared order is the parallel group follow S31, id 30?**
  Options: (a) reword `render_order`'s docstring and leave `memory/TEMPLATE-SPEC.md:84` and
  `tools/memory-tree/SPEC-TEMPLATE.template.md:84` to the owner; (b) reword all three. (b) changes a
  governance carrier no clause of this build names, which BUILD-METHOD M3's veto 2 makes an owner
  turn that `PLAY-dClosedLoop-3` does not lift. (a) meets AC27 and names the two template lines for
  the owner as §3's external hand-off. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3.
  widens: none · relaxes: none
- **F2 — How do S15's acks land all or nothing, id 32?** Options: (a) one commit per ack, chained,
  landed by one ref update; (b) one ack message whose `answers` lists every id; (c) the per-row
  loop with a compensating message. (c) cannot retract from an append-only ref. (b) changes unit 5's
  record grammar that its state rule and id derivation read. (a) meets AC13 and keeps every record
  as unit 5 writes it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the round-2 promotions' audit's minors batch.
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared
- rev-3 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-64` mirrored, the other ends of
  the edges the round-4 minors batch's audit's disposal declared

## 10. Reuse audit

Every item extends the seam its repaired unit names, and the cross-cutting ones extend existing
mechanisms: the `PARITY_ROWS` arm of `tools/lib/resolve-python.test.sh` (`:168-184`, `:213-218`)
for S20 and S22, `read_consumes_from` (`tools/unattended/lib-unattended.sh:348`) as the rule S16 and
S17 hold the Python reader to, `resolve_projects_root` and `_check_inside`
(`tools/runlog/extract.py:185`, `:176`) for S8 and S19, unit 5's `write_mail_ref` for S15, and the
failing `timeout` shim on `PATH` that `unattended.test.sh:8964` already stages for S13. `python
tools/codebase-map/reuse_lookup.py "inline copy of a function held byte identical to its canonical
source"` ranked `canonical_ctx` and name stems only, missing the `PARITY_ROWS` arm the source read
found; no item mints a mechanism where one of these fits.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted unit placed when it
repairs an earlier unit's pass" --terms "promoted order pass commit ledger superseded batch minors
hands-off consumes-from parity mirror"`
