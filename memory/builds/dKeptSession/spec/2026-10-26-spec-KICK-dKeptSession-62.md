# KICK-dKeptSession-62 — the round-2 promotions' audit's 32 minor findings, closed after every unit they land on is built

**Status:** CLOSED · rev-5 · 2026-11-23 · node a · Tier-2 · base 71b22e42 · streams kickoff · order 33 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-57-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-57-promoted-fix-return.md) | research | KICK-dKeptSession-57 |
| [2026-10-26-build-KICK-dKeptSession-62-deviation-621.md](../build/2026-10-26-build-KICK-dKeptSession-62-deviation-621.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-62-deviation-622.md](../build/2026-10-26-build-KICK-dKeptSession-62-deviation-622.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-62-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-62-1-acceptance-ledger.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-57-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-57-promoted-fix-brief.md) | research | KICK-dKeptSession-57 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief.md) | research | KICK-dKeptSession-30 KICK-dKeptSession-32 KICK-dKeptSession-35 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-57-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-57-precheck-brief.md) | research | KICK-dKeptSession-57 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-62-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-62-build-brief.md) | research | — |
| [2026-11-22-prompt-KICK-dKeptSession-62-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-62-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-62-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-62-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-57-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-57-spec-audit.md) | spec-audit | KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-57 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's twelve round-2 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`)
confirmed 27 findings at MEDIUM and 5 at LOW (PINNED, the report's verdict, read 2026-10-26).
BUILD-METHOD M4 promotes them into one batch, and this is it. Each finding is its own §2 item,
named by report id beside its report item:

- MEDIUM: ids 2 (M1), 3, 13, 22 and 25 (M2), 4 (M3), 5 (M4), 6 (M5), 7 (M6), 11 (M7), 12 and 35
  (M8), 14 (M9), 15 and 32 (M10), 19 and 29 (M11), 20 and 27 (M12), 21 and 28 (M13), 24 (M14), 26
  (M15), 33 (M16), 34 (M17), 37 (M18), 38 (M19);
- LOW: ids 8 (L1), 16 and 39 (L2), 30 (L3), 36 (L4).

Three minors are a sibling's defect at another grade: id 33 is H3's at MEDIUM
(`KICK-dKeptSession-59`, whose case its item widens), id 36 is id 6's at LOW, and id 8 is id 38's at
LOW. The minors land on eleven units, so this unit is one write set and takes the order past every
unit of the build (order 33). An item the landed tree, or a unit before it, already meets is reduced
to its observation, naming that unit; the rest amend code their units built. Where an item
supersedes a sibling spec's text, it does so by name, and this unit's own acceptance ledger,
`memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-62-1-acceptance-ledger.md`,
quotes that text as it stands at that unit's rev and answers it (F3). Every unit whose text or
record an item answers builds before order 33 and is CLOSED when this unit builds, so neither its
spec nor its ledger is written.

## 2. Scope (IN)

- **S1** — id 2, M1. Units 49, 50 and 54 add `check_policy.py` arms and units 52, 53 and 55 add
  `tools/loop/loop_transition.py` plants, and `KICK-dKeptSession-56` S25 and S27's lists omit all
  six. At this unit's pass its own ledger gains one OBSERVED line per unit by
  `KICK-dKeptSession-57` S3's rule, naming the leg the unit's own §7 names to run its arm at the
  close: `policy fixtures` (49, 50, 54) or `loop transition record` (52, 53, 55). No `loop selftest`
  leg exists. `loop transition record` carries no `guard` in `tools/gate-legs.json`, so `--legs-for`
  never prints it, and the line names it beside what the query prints, as 57 rev-4 S3 does for
  units 35, 36 and 42. Observed by AC1.
- **S2** — id 3, M2. Met by `KICK-dKeptSession-56` rev-6 AC15 and unit 37's extraction: the count is
  the invocation's, `claude --version </dev/null`, once, inside
  `skills/session-kickoff/manifest-check.sh#read_claude_version`. Observed by AC2.
- **S3** — id 13, M2. Met by 56 rev-6: S36 reads "runs `claude --version` once" and AC15's Red-when
  no longer says "as at base". Observed by AC2.
- **S4** — id 22, M2. Met: `manifest-check.sh#derive_cli_line` calls `read_claude_version` and its
  body spells no `--version`, its skip lines printing `read_claude_version`'s reason. Observed by AC3.
- **S5** — id 25, M2. Met: the two skip messages print `read_claude_version`'s `unknown:` reasons,
  and `manifest-check.test.sh` pins them byte for byte, unchanged here. Observed by AC3.
- **S6** — id 4, M3. Met by unit 47 and 56 rev-6 S21: `tools/runlog/extract.py#derive_context_window`
  walks every event of each transcript, a main usage setting the model and a compaction joining it
  by the newest-prior-usage rule; no scan filters by model first. Observed by AC4.
- **S7** — id 5, M4. Met by 56 rev-6 AC10, which counts calls of `derive_context_window` from
  `extract.py#measure_orient_tree`, one for 22 rows of one model. Observed by AC5.
- **S8** — id 6, M5. Met by 56 rev-6 S11, which withdraws the memo: `derive_context_window` keeps no
  cache and resolves a `None` root by `resolve_projects_root()` at each call, and
  `measure_orient_tree`'s `windows` lives for one call, keyed by model under the root it was passed.
  Observed by AC6.
- **S9** — id 7, M6. Met by 56 rev-6 §4 "The re-post": a re-post runs only on a move that is not a
  Design exit, carries the interface listing at that move's commit, so its content key is the
  current one, and is posted only where `check_interface_notice` answers `unconfirmed`. No re-post
  sits beside a newer notice of its own pass. Observed by AC7.
- **S10** — id 11, M7. Met by the landed relabel: an agent transcript's records carry `isSidechain`,
  which `extract.py#extract_session` reads as `agent`, so `extract.py#measure_context_fill` finds no
  main usage and `runlog.py context` prints `none` before any root is read; the runlog README states
  that `context` is always the main file's. Observed by AC8.
- **S11** — id 12, M8. Met: `derive_context_window` parses each scanned transcript as
  `SessionTree(sid=p.stem, main=p)`, its main file alone, so no `subagents/agent-*.jsonl` compaction
  reaches the fold. Observed by AC9.
- **S12** — id 35, M8. Owed: a compaction joins `model`'s observation only where its own `src` is
  `main`, so a main-file record carrying `isSidechain`, which `extract_session` relabels `agent`,
  joins no model. `KICK-dKeptSession-47` S1's rule reads as this item, answered in this unit's
  ledger. Observed by AC10.
- **S13** — id 14, M9. `KICK-dKeptSession-56` AC21's unbounded half is staged by a failing stub
  `timeout` first on `PATH`: the driver's probe then sets `REMOTE_BOUND_LIVE=0`, and two top-level
  assignments carry it into `GATE_BOUND_LIVE`, overwriting an exported value
  (`tools/unattended/unattended.sh@ef6ec3841c98:216`, `:219`, `:702`). AC21's "with
  `GATE_BOUND_LIVE=0`" reads as this item, answered in this unit's ledger. Observed by AC11.
- **S14** — id 15, M10. Met by `KICK-dKeptSession-55` rev-6 S1: `write_consumed_acks` takes the
  rows of the guard's one `read_mail_rows` read and makes no read of its own. Observed by AC12.
- **S15** — id 32, M10. The acks land all or nothing. `--mail ack <slug> <id> [<id> ...]` reads the
  mailbox once and refuses before any write where an id names no row addressed to `<slug>`. It makes
  one bounded fetch and derives each ack's message by `write_mail_post`'s steps, every id's duplicate
  check before any write. Message k's tip read is the chain's commit k-1, so its `seq` is that tip's
  first-parent count plus one, and the chain lands with one `write_gov_ref` against the tip it read
  (`KICK-dKeptSession-5` S2). A refused record or a lost update leaves every row open; one id keeps
  today's lines and exits. `write_consumed_acks` posts its ids in that one call, and
  `KICK-dKeptSession-55` §4 "The step"'s per-row loop reads as it, answered in this unit's ledger.
  Observed by AC13.
- **S16** — id 29, M11. `tools/memory-tree/design_lib.py#read_spec_edges`, the one Python Edges
  reader the build-order render and the spec-token checker's hands-off join read
  (TOOL-dGroundRules-32 S17), names in its docstring the dispatcher's reader it must agree with,
  `tools/unattended/lib-unattended.sh#read_consumes_from`, beside check 12's extractor, and their
  one departure: a bare id run, which `read_consumes_from` reports unreadable and `--dispatch`
  refuses. Observed by AC14.
- **S17** — id 19, M11. An `edges-agreement` case in the driver suite, which already copies
  `design_lib.py` beside its fixtures, runs `read_spec_edges(text, "consumes-from")` and
  `read_consumes_from --scan` over one set of fixture Edges blocks (a backticked id, a wrapped `none`
  bullet holding a backticked id, an `external` edge, an id-less payload) and reds on any difference
  between their id-shaped targets. Observed by AC15.
- **S18** — id 20, M12. `extract.py#scan_preflights` reads its population through
  `derive_main_transcripts` (`KICK-dKeptSession-56` S21), so `glob("*/*.jsonl")` is spelled once in
  `extract.py`. 56 S21's "`scan_preflights` keeps its `_check_inside` walk" reads as this item,
  answered in this unit's ledger. Observed by AC16.
- **S19** — id 27, M12. `derive_main_transcripts` applies `extract.py#_check_inside` against the
  resolved root, the rule `scan_preflights` applies today, and its docstring says so, so the window
  scan omits a transcript linked from outside the root. Observed by AC17.
- **S20** — id 21, M13. The inline-parity arm of `tools/lib/resolve-python.test.sh` already reads
  `// >>> ` markers and `*.js` (TOOL-dWitnessedBar-26 S4). Owed: `PARITY_ROWS` gains
  `extract_route_units_js` and `card_file_rel_js`, canonical `tools/hooks/scratch-guard.js`, its
  kit dir resolved by `resolve_kit_dir` ahead of the rows. Observed by AC18.
- **S21** — id 28, M13. The copied closure is `KICK-dKeptSession-44` S9's: `extractRouteUnits` and
  `CARD_FILE_REL`, never `readCard`, so `buildComparablePath` is not carried. Each sits inside a
  marker pair in `scratch-guard.js` and in `tools/unattended/mail-notice.js`. Observed by AC19.
- **S22** — id 24, M14. Met: 56 rev-6 S2 copies no Files touched reader, the index reading
  `tools/memory-tree/design_lib.py#read_spec_writes`, so no `files_touched_py` row or block is owed.
  Observed by AC20.
- **S23** — id 26, M15. Met by unit 32: every `render_scaffold` call in `check_policy.py` passes
  `(rows, preset)`. Observed by AC21.
- **S24** — id 33, M16. `tools/policy/policy-mirror.js` gains `MIRROR_LEGACY_INPUTS`, a copy of
  `tools/policy/policy.py#LEGACY_INPUTS`, and `readMirrorAt` expects the policy file, the catalogue,
  `MIRROR_KIT_INPUTS` and `MIRROR_LEGACY_INPUTS`, never the stored mirror's own keys. The
  `mirror-input-parity` case compares the JS list with `policy.LEGACY_INPUTS` beside its kit-input
  compare. Observed by AC22.
- **S25** — id 34, M17. Met by unit 47: the fold admits a compaction only where
  `type(ev.get("pre_tokens")) is int`, so a `None` never reaches `max()`. Observed by AC23.
- **S26** — id 37, M18. The runlog selftest gains a class arm: every variable name `extract.py` reads
  through `env.get`, `env[...]` or `os.environ` is in `DECOY_VARS`, set by `build_arm_env`, or popped
  in `tools/runlog/selftest.py#main` before any arm runs. The instance is met by unit 30, whose pop
  of `CLAUDE_CODE_MAX_CONTEXT_TOKENS` landed at order 13, before units 46 and 47 (order 14) built, so
  no re-observation is owed. Observed by AC24.
- **S27** — id 38, M19. Met by `KICK-dKeptSession-45` rev-5 AC2: every line `grep -n '\.claude'`
  prints lies inside `resolve_projects_root`, which sees an unquoted literal. Observed by AC25.
- **S28** — id 8, L1. Met by the same criterion, which reads `.claude` in any quote style.
  Observed by AC25.
- **S29** — id 16, L2. Met by unit 45 rev-5's §4 Evidence, whose second bullet names
  `CLAUDE_CONFIG_DIR` as the decoy the literal misses. NOT OBSERVED: an evidence sentence with no
  behaviour, already true in its own spec, so no answer is owed.
- **S30** — id 39, L2. Met by unit 45 rev-5 AC1 and its arm, which aim `HOME` and `USERPROFILE` at
  the empty directory inside `build_arm_env`'s decoys. Observed by AC26.
- **S31** — id 30, L3. Met for the code: `gen_build_index.py#render_order`'s docstring reads that
  units sharing an `order` value are a step whose Parallel cell `derive_parallel_step` derives. The
  two template texts stay the owner's (§8 F1). Observed by AC27.
- **S32** — id 36, L4. Met by S8's withdrawal: no memo exists to key or invalidate. Observed by AC6.

## 3. Non-goals (OUT)

- The fixes of ids 1, 9, 10, 23 and 31: units 57 to 61.
- Rewording sibling specs: each superseded text is named here and answered in this unit's own
  ledger (F3).
- The report's left-shift checklist entries and hygiene arms: no clause of this build names the
  bug-class checklist, and each arm is a separate gate, so a separate unit by M2. Where an item's
  criterion is the class arm, it says so (S17, S26).
- The build-order verb comment above `gen_build_index.py#ORDER_RE`, which still says a shared value
  is the parallel group: `KICK-dKeptSession-63` S24's.
- Renumbering any order, and a memo, fixture or ledger line the landed tree makes needless.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `--mail ack`, `write_mail_ref` and `write_mail_post`'s steps, S14 and S15 (ids 15, 32)
- **consumes-from** `KICK-dKeptSession-45` — AC1, AC2 and §4's evidence at rev-5, which meet S27 to S30 (ids 38, 8, 16, 39)
- **consumes-from** `KICK-dKeptSession-46` — the context verb and its README sentence, S10 (id 11), and S26's window arms (id 37)
- **consumes-from** `KICK-dKeptSession-47` — the fold's compaction rule, S6, S11, S12, S25 and S26 (ids 4, 12, 35, 34, 37)
- **consumes-from** `KICK-dKeptSession-48` — the owner's variable advice, whose ambient value S26's arm guards (id 37)
- **consumes-from** `KICK-dKeptSession-49` — `readMirrorAt`'s expected list and its arm's leg, S24 and S1 (ids 33, 2)
- **consumes-from** `KICK-dKeptSession-50` — the `mirror-upgrade` arm's leg, S1 (id 2)
- **consumes-from** `KICK-dKeptSession-52` — the `notices-repeat-key` plant's leg, S1 (id 2)
- **consumes-from** `KICK-dKeptSession-53` — the chain's plants' leg and the order S9's re-posts take, S1 and S9 (ids 2, 7)
- **consumes-from** `KICK-dKeptSession-54` — the restated cases' arm's leg, S1 (id 2)
- **consumes-from** `KICK-dKeptSession-55` — the listed rows, the guard's read and the ack loop, S1, S14 and S15 (ids 2, 15, 32)
- **consumes-from** `KICK-dKeptSession-56` — at rev-6, S1, S2, S11, S21, S23, S27, S33 and S36 with AC10, AC15, AC21 and §4 "The re-post", which S2 to S9, S13, S16 to S22 and S32 observe or amend (ids 2, 3, 13, 22, 25, 4, 5, 6, 7, 14, 29, 19, 20, 27, 21, 28, 24, 36)
- **consumes-from** `KICK-dKeptSession-57` — S3's ledger rule, which S1 runs for the six units it adds (id 2)
- **consumes-from** `KICK-dKeptSession-59` — the `mirror-input-parity` case, which S24 widens to the legacy list (id 33)
- **hands-off** external — the two template texts of S31, `memory/TEMPLATE-SPEC.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md` under "The status header", governance carriers BUILD-METHOD M3's veto 2 reserves to the owner (§8 F1)
- **hands-off** `KICK-dKeptSession-63` — S1, S15, S19, S20, S22, S24, S26, S31, AC20, AC25 and §7's leg line, which the batch's S1 to S5, S8, S9, S12 to S18, S21 and S23 to S26 amend (ids 4, 10, 24, 2, 20, 11, 13, 15, 18, 21, 25, 26, 27, 5, 9, 22, 23, 30, 31)
- **hands-off** `KICK-dKeptSession-64` — S19, S31, §5's "seven definitions" and S15 and §4's ack-chain sketch, which the batch's S4 answers in its own ledger (id 1)

## 4. Design

### Evidence

Each item's evidence is the audit's appendix row for its id, re-checked against the tree at
`71b22e42` on 2026-11-23, with units 21, 6, 7, 35, 42, 8, 11, 43, 52, 53, 55, 17, 61, 18, 41, 44
and 56 at their current revs, and 57 at rev-4, read as landed before this unit.

- `skills/session-kickoff/manifest-check.sh` spells `claude --version </dev/null` once, inside
  `#read_claude_version`; `#derive_cli_line`'s range holds no `--version`; the test pins
  `cli — skipped: claude --version printed no version` and `… did not answer within 1s`
  (`skills/session-kickoff/manifest-check.test.sh@91456cd95e76:1533`, `:1537`).
- `tools/runlog/extract.py#derive_context_window` keeps no cache (`grep -c 'lru_cache\|functools'`
  prints 0, DERIVED), parses `SessionTree(sid=p.stem, main=p)`, admits a compaction where `on_model`
  and an integer `pre_tokens` hold, with no `src` test, and spells its own glob; `#scan_preflights`
  spells a second, with `SID_RE` and `_check_inside`; `#measure_tree` and `#measure_ready_tree` two
  more (`glob("*/*.jsonl")` four times at `extract.py@1bb03a70d1b9`, DERIVED).
- The runlog fixtures write agent files with `isSidechain: true`
  (`tools/runlog/selftest.py#build_orient_transcript`, the `context-fill` scenario's `fxcf1`).
- `tools/unattended/unattended.sh#write_mail_ack` takes one id and calls `write_mail_post`, which
  fetches, derives the id, checks for a duplicate, reads the tip, derives `seq` from it and calls
  `write_mail_ref` once; the `--mail` arm refuses any `ack` that is not two positionals.
- `tools/lib/resolve-python.test.sh#blk` and the copy grep read `# >>> ` and `// >>> ` markers over
  `*.sh`, `*.py`, `*.js`, `.githooks/*` and `WIRE-INTO-PROJECT.md`, and `PARITY_ROWS` is built
  before the hooks kit's dir is resolved.
- `tools/policy/policy-mirror.js#readMirrorAt` expects `MIRROR_KIT_INPUTS`, then every other key the
  stored `legacy_blobs` records; `tools/policy/check_policy.py#run_mirror_input_parity` compares the
  kit list alone and names the repository-relative inputs this unit's widening.

### The ack chain

```
--mail ack <slug> a b           read tip T, one fetch, both ids checked and dedup-checked first
  m_a := message(a, tip T)        seq = count(T) + 1
  c_a := build_gov_commit T   m_a
  m_b := message(b, tip c_a)      seq = count(c_a) + 1
  c_b := build_gov_commit c_a m_b
  write_gov_ref <ref> T c_b   -> one update: both land (two `mail — posted` lines, exit 0),
                                 or neither (`mail — lost`, exit 1; `mail — not written`, exit 2)
```

### Texts

| Shipped text | Disposition |
|---|---|
| `extract.py#derive_context_window`'s docstring and the runlog README's window sentence, "a compaction whose newest earlier main usage" | false: S12, each reads "a main compaction whose …" |
| `unattended.sh`'s `--mail ack` usage row, `#write_mail_ack`'s comment and the `--mail` arm's form line | false: S15 names `<id> [<id> ...]` and the one update |
| `tools/unattended/VERBS.template.md` and its byte-equal copy `memory/guides/UNATTENDED-VERBS.md`, the `--mail ack` sentence | false: S15 |
| `help/loop.md`'s `--mail` paragraph, its `--mail ack` sentence | false: S15; the anchor's input is the usage row's `--` flags (`tools/govkit/docs_leg.py#read_verb_usage`), which S15 does not move, re-read by `docs_leg.py --fingerprints` at the build |
| `loop_transition.py#write_consumed_acks`' docstring and `tools/loop/README.md`'s mail guard, as units 42, 55 and 56 land them | false where they say one post per id: S15; found by `git grep -n -E "per id\|once per\|mail ack" tools/loop` at the unit's base |
| `design_lib.py#read_spec_edges`' docstring | false by omission: S16 |
| `extract.py#scan_preflights`' docstring; `derive_main_transcripts`' docstring as 56 lands it | false: S18 and S19 |
| the comment above `PARITY_ROWS` naming each JS copy | false by omission: S20 |
| `policy-mirror.js`'s header steps 3 and 5 and the comment on `MIRROR_KIT_INPUTS`; `check_policy.py#run_mirror_input_parity`' docstring and the module's `mirror-input-parity` sentence; the policy README's "Every input the resolution reads is pinned" paragraph and THE RULE | false: S24 |
| `help/loop.md`'s refusal remedy naming `--mail ack <slug> <id>`; `help/policy.md`'s `legacy_blobs` list; `policy.py#LEGACY_INPUTS`' comment | true: one id stays legal, the list is unchanged, the comment points at THE RULE |
| the runlog README's "A path resolving outside its root is refused or counted, never read" | true: S19 keeps it |

No catalogue row moves, so `.governance/policy.json` stands.

### The driver's ceiling

`tools/unattended/unattended.sh` is edited by S15 and sits at its ceiling, 347 sites (PINNED,
`.memory-tree.conf@d4f8d497b8c3:661`, 2026-11-23). The census counts a `fail <n> "` call, an `exit 1`
word and a `status=1` assignment (`tools/memory-tree/check-arms.py#FAIL_RE`, `#EXIT_RE`,
`#STATUS_RE`). S15 adds none: its refusals are `echo …; return 2` and `return 1` lines, as
`write_mail_ack` and `write_mail_post` write theirs, and the arm's form check moves in place, so the
ceiling is met unraised. The arms of §7 raise the driver suite's effective `FLOOR_ASSERTIONS` and the
floor of each shard they fall in by their counted assertions, each with a `RAISED` line; they read
4137 and `FLOOR_SHARD_8` 1354 at `71b22e42`
(`tools/unattended/unattended.test.sh@82201773d73f:24700`, `:24992`, DERIVED, the last assignment of
each), and units before this one raise them first. No budget row is re-priced: the shard rows are
ESTIMATE rows with no `plants=` token (`tools/run-gates/selftest-budgets.txt@d851d800fad1:161`), and
no loop plant is added.

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `MIRROR_LEGACY_INPUTS` | constant | `tools/policy/policy-mirror.js` |
| `extract_route_units_js`, `card_file_rel_js` | parity marker stems | `tools/hooks/scratch-guard.js`, `tools/unattended/mail-notice.js` |
| `context-window-compact-sidechain` | fixture scenario | `tools/runlog/fixtures/transcripts.json` |
| `edges-agreement` | driver suite case | `tools/unattended/unattended.test.sh` |

### Migration

None: no stored state changes shape. S15's acks are the records unit 5 already writes, landed by one
ref update.

### Files touched (estimate)

- `tools/runlog/extract.py`, `tools/runlog/selftest.py`, `tools/runlog/fixtures/transcripts.json`,
  `tools/runlog/README.md`: S12, S18, S19, S26
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`,
  `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`, `help/loop.md`: S13,
  S15, S17, and the floors of §4 "The driver's ceiling"
- `tools/unattended/mail-notice.js`, `tools/hooks/scratch-guard.js`: S21, marker comments only
- `tools/lib/resolve-python.test.sh`: S20
- `tools/memory-tree/design_lib.py`: S16, its docstring only
- `tools/loop/loop_transition.py`, `tools/loop/README.md`: S15
- `tools/policy/policy-mirror.js`, `tools/policy/check_policy.py`, `tools/policy/README.md`: S24
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-62-1-acceptance-ledger.md`:
  S1's lines and every answer the items name, beside the criteria observed

### Alternatives rejected

- **Two batches.** S1 records lines for units of both the policy and the loop kits, and S15 crosses
  the driver and the loop kit, so no two write sets are disjoint by M6's clauses.
- **One ack message whose `answers` lists every id, for S15.** It changes unit 5's record grammar,
  which S7's state derivation and the id derivation read; §8 F2 records it.
- **Hosting `edges-agreement` in the build-index selftest.** The memory-tree kit imports no
  unattended file, while the driver suite already copies `design_lib.py`.

## 5. Production-readiness checklist

- security — S19 omits a transcript linked from outside the root; S20 gates two JS copies that had
  no parity check; S15 writes the records unit 5 already validates.
- perf / scale — S15 makes one fetch for n acks where unit 55's loop makes n.
- error / empty / loading states — S12's sidechain compaction joins no model; S15's refusal leaves
  every row open; an absent JS literal reds S24's case.
- observability — S16 names the reader S17 holds the Python reader to; S26's arm names the variable
  it found.
- risks — S15 edits the driver at its refusal ceiling and adds no site (§4).
- testing — the criteria of §6 and the arms of §7.
- migration — §4.
- user docs — `help/loop.md` and the verbs guide's `--mail ack` sentence, S15.

## 6. Acceptance criteria

Fixtures are each repaired unit's own, named by that unit's spec, under `%TEMP%`.

- **AC1** — When this unit's ledger is read at its pass, its lines for units 49, 50 and 54 each name
  `policy fixtures`, and those for units 52, 53 and 55 each name `loop transition record`;
  `tr -s ' \r\n' ' '` over it piped into `grep -c` prints `1` for each of "`scan_preflights` keeps
  its `_check_inside` walk" (S18), "with `GATE_BOUND_LIVE=0` a stub exiting 0 still emits its line"
  (S13) and "for r in eat: --mail ack <slug> r.id" (S15); and `git diff --name-only <pass base> HEAD
  -- memory/builds/dKeptSession/build/` lists no acceptance ledger but this unit's own.
  Red when: an arm's unit has no line naming the leg that runs it, an answer lands in a record of
  the unit it names, or a quoted passage is left out.
- **AC2** — When `grep -c 'claude --version </dev/null' manifest-check.sh` runs in
  `skills/session-kickoff/`, it prints `1`, on a line inside `read_claude_version`'s range.
  Red when: a second invocation is written.
  figure: PINNED, `1` at `71b22e42`, read 2026-11-23.
- **AC3** — When `awk '/^derive_cli_line\(\) \{/,/^\}/' manifest-check.sh | grep -c -- '--version'`
  runs, it prints `0`, and `grep -c 'cli — skipped: claude --version' manifest-check.test.sh` prints
  `2`. Red when: the body runs the binary, or a pinned message was reworded to green a count.
  figure: PINNED, both at `71b22e42`, read 2026-11-23.
- **AC4** — When `runlog.py context` reads `context-window` from a root holding
  `context-window-compact-own`, it prints `15%`, and from one holding `context-window-compact-other`,
  `75%`. Red when: a scan pre-filtered by model drops every compaction or keeps another model's.
- **AC5** — `KICK-dKeptSession-56` AC10 holds: `extract.derive_context_window`, wrapped to count its
  calls over unit 9's 22-row fixture of one model, records one call in `measure_orient_tree`.
  Red when: N rows cost N scans.
- **AC6** — When `grep -c 'lru_cache\|functools' extract.py` runs in the runlog kit, it prints `0`,
  and a probe calling `derive_context_window("fixture-model")` in one process under two
  `CLAUDE_CONFIG_DIR` values, one root holding `context-window-sibling`, returns two windows.
  Red when: a cache keyed on the unresolved root returns the first window twice.
- **AC7** — `KICK-dKeptSession-56` AC28 holds: under `--plant notices-reposted`, both dependents'
  mail refs hold a `confirmed` of pass 1 and the second run posts nothing to the other.
  Red when: a re-post carries an older pass's content key.
- **AC8** — When `runlog.py context` reads the `context-fill` scenario's agent file under
  `<dir>/<project>/<sid>/subagents/`, it prints `none`, writes nothing on stderr and exits 0.
  Red when: the agent file's usage is read as main and a window is derived under `<sid>`.
- **AC9** — When `grep -n 'SessionTree(sid=p.stem, main=p)' extract.py` runs in the runlog kit, it
  prints one line, inside `derive_context_window`. Red when: the scan builds `build_session_tree(p)`,
  listing agent files.
- **AC10** — When `runlog.py context` reads `context-window` from a root holding
  `context-window-compact-sidechain`, a 900000-token compaction on an `isSidechain` record in the
  main file after a main usage on `fixture-model`, it prints `75%`.
  Red when: the relabelled record lifts the main model to `15%`.
- **AC11** — When `bash unattended.sh --landed <slug>` runs with a failing stub `timeout` first on
  `PATH` and a progress stub exiting 0, it still emits the stub's line, and with a stub running
  `sleep 30 &` it returns within unit 44 AC30's bound.
  Red when: the run takes the live `timeout` path, so the unbounded half is never reached.
- **AC12** — When an `ast` walk of `tools/loop/loop_transition.py` lists the calls of
  `read_mail_rows`, it finds one, inside `write_transition`, and none inside `write_consumed_acks`.
  Red when: the writer makes a read of its own.
- **AC13** — When `--mail ack <slug> <a> <b>` runs over a planted mailbox where an ack of `<a>` is
  already posted, it prints `mail — duplicate` and exits 1, and `--mail read <slug>` shows `<b>`
  `open`; with neither acked it prints two `mail — posted` lines, exits 0, and the session ref's tip
  is the second ack, whose parent is the first and whose `seq` is one past it.
  Red when: a per-row loop leaves `<b>` acked, or two acks share one `seq`.
- **AC14** — When `grep -n "read_consumes_from" design_lib.py` runs in `tools/memory-tree/`, it prints
  `read_spec_edges`' docstring line naming it. Red when: the reader names no rule it must match.
- **AC15** — When the driver suite's `edges-agreement` case runs, `read_spec_edges` and
  `read_consumes_from --scan` print one set of id-shaped targets over the four fixture blocks.
  Red when: a copy of the Python reader taking a wrapped `none` bullet's id as an edge passes.
- **AC16** — When `grep -c 'glob("\*/\*.jsonl")' extract.py` runs in the runlog kit, it prints `1`,
  inside `derive_main_transcripts`. Red when: `scan_preflights` keeps its own spelling.
  figure: DERIVED, the grep; `4` at `71b22e42`, before unit 56 folds three.
- **AC17** — When a fixture root holds a transcript linked from outside it, `derive_main_transcripts`
  omits it. Red when: the window scan reads a file `scan_preflights` refuses.
- **AC18** — When the inline-parity arm runs over a scratch tree whose `mail-notice.js` copy of
  `extractRouteUnits` is staged to differ by one byte, it reds naming `extract_route_units_js`.
  Red when: the JS copy drifts with no red.
- **AC19** — When `grep -cE '^// >>> (extract_route_units_js|card_file_rel_js)'` runs over
  `scratch-guard.js` and over `mail-notice.js`, each prints `2`, and `grep -c "readCard"
  mail-notice.js` prints `0`. Red when: a carried definition sits outside its markers.
- **AC20** — When `grep -c 'def extract_files_touched' gen_build_index.py` runs in
  `tools/memory-tree/`, it prints `0`, and `grep -c 'read_spec_writes' gen_build_index.py` at least
  `1`. Red when: a second Files touched reader is copied into the index.
- **AC21** — When `grep -cE 'render_scaffold\((rows|policy\.load_catalogue\(KIT\))\)'
  check_policy.py` runs in the policy kit, it prints `0`, and `python check_policy.py --fixture`
  runs `adopter-fresh-target`, `arms-empty-target`, `mirror-absent-adopter` and
  `mirror-hand-edited`, each exiting 0. Red when: a caller passes one argument and raises `TypeError`.
- **AC22** — When a planted mirror whose `legacy_blobs` lacks the `.agent-cap.conf` key is read by
  `node policy-mirror.js get hooks.bypass`, it reports the mirror stale, and `--fixture
  mirror-input-parity` reds on a copy adding a path to `LEGACY_INPUTS` alone.
  Red when: the missing key reads FRESH, or the one-sided addition passes.
- **AC23** — When `grep -n 'type(ev.get("pre_tokens")) is int' extract.py` runs in the runlog kit, it
  prints one line, inside `derive_context_window`. Red when: a `None` reaches `max()`.
- **AC24** — When the runlog selftest's environment arm runs over a copy of `extract.py` adding
  `env.get("RUNLOG_PLANTED")`, it reds naming that variable.
  Red when: a variable the code reads reaches a case from the machine.
- **AC25** — When `grep -n '\.claude' extract.py` runs in the runlog kit, every line it prints lies
  inside `resolve_projects_root`, and the `derive_context_window` range, its docstring removed,
  grepped with `grep -cE 'expanduser|\.claude'`, prints `0`.
  Red when: a copy keeping `os.path.expanduser("~/.claude/projects")` as a fallback passes.
  figure: PINNED, two lines at `71b22e42`, the docstring and the return, read 2026-11-23.
- **AC26** — When `grep -n 'HOME=str(empty), USERPROFILE=str(empty)' selftest.py` runs in the
  runlog kit, it prints one line, inside `test_extract_context_window_root`.
  Red when: the probe aims `HOME` alone and reads the owner's real profile.
- **AC27** — When `grep -n "are a step, and" gen_build_index.py` runs in `tools/memory-tree/`, it
  prints `render_order`'s docstring. Red when: the docstring says a shared order is the parallel
  group.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `format-guard self-test` · `scratch-guard self-test` · `agent-cap self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended kit gate` · `loop transition record` · `policy fixtures` · `routed-commits selftest` · `build-index selftest` · `memory-recall kit selftest` · `playbook render selftest` · `docs` · `help reference pages` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The guarded legs are those `python tools/check-spec-tokens.py --legs-for` printed over §4's Files
touched at `71b22e42`, less the broad ones; `unattended kit gate`, `loop transition record`, `docs`
and `help reference pages` carry no guard and run S15's, S17's and the page's changes.

New arm: tools/runlog/selftest.py · covers AC10 AC17 AC24 · the `context-window-compact-sidechain` scenario, a linked transcript and a planted variable · none
New arm: tools/unattended/unattended.test.sh · covers AC11 AC13 AC15 · a failing stub `timeout`, a planted duplicate ack and the four fixture Edges blocks · the effective `FLOOR_ASSERTIONS` and its shard's floor rise by the arms' count, counted off the diff
New arm: tools/lib/resolve-python.test.sh · covers AC18 · a one-byte edit to the JS copy · none
New arm: tools/policy/check_policy.py · covers AC22 · a mirror missing its legacy key · none

## 8. Open questions

- **F1 — How do the texts that say a shared order is the parallel group follow S31, id 30?**
  Options: (a) reword `render_order`'s docstring and leave the two template texts under "The status
  header" of `memory/TEMPLATE-SPEC.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md` to the
  owner; (b) reword all three. (b) changes a governance carrier no clause of this build names, which
  BUILD-METHOD M3's veto 2 makes an owner turn that `PLAY-dClosedLoop-3` does not lift. (a) meets
  AC27 and names the two template texts for the owner as §3's external hand-off. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3. At rev-5 the docstring is already reworded.
  widens: none · relaxes: none
- **F2 — How do S15's acks land all or nothing, id 32?** Options: (a) one commit per ack, chained,
  landed by one ref update; (b) one ack message whose `answers` lists every id; (c) the per-row
  loop with a compensating message. (c) cannot retract from an append-only ref. (b) changes unit 5's
  record grammar that its state rule and id derivation read. (a) meets AC13 and keeps every record
  as unit 5 writes it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes:
  none
- **F3 — Where are S1's lines and the answers to the sibling texts recorded?** Every unit whose text
  or record an item answers builds before order 33, so each is CLOSED when this unit builds, and
  their ledgers are in neither this unit's Files touched nor its write set. (a) Each named unit's
  acceptance ledger, a record of a closed unit written by a later one; (b) this unit's own
  acceptance ledger, one line per unit S1 names and each sibling text quoted. Recommendation (b).
  RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a CLOSED unit's records are never written by
  a later unit, as KICK-dKeptSession-49 rev-6 ruled. Rejected: (a), writing the other unit's ledger.
  The main loop's ruling, in `2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the round-2 promotions' audit's minors batch.
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared
- rev-3 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-64` mirrored, the other ends of
  the edges the round-4 minors batch's audit's disposal declared
- rev-4 · 2026-11-21 · §1 · S1 · S29 · §3 · §4 · AC1 · §7 · §8 · S1's six lines and S29's answer
  move from units 49, 50, 52 to 55 and 45's ledgers to this unit's own acceptance ledger, which joins
  Files touched, F3 resolved (b) and AC1 observing the lines and two quoted passages, under the brief
  `2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief`; the class KICK-dKeptSession-49 rev-6
  first resolved. The Edges bullet to `KICK-dKeptSession-64` says its S4 answers in its own ledger.
  §7's line gains `policy fixtures` and `routed-commits selftest`, which the spec-token checker's
  guards join named at rev-3; the ledger's path trips the two `recall floor` legs, already on it.
- rev-5 · 2026-11-23 · §1 to §10 · S1 to S32 · AC1 to AC27 · re-grounded on `71b22e42` by
  `2026-11-22-prompt-KICK-dKeptSession-62-reground-brief`, units 21 to 57 read as landed: S2 to S11,
  S14, S22, S23, S25 and S27 to S32 reduced to their observations, met by units 37, 45, 47, 55, 56
  rev-6 and the landed relabel; S1 names `loop transition record`, no `loop selftest` leg existing,
  as 57 rev-4 S3; S12 adds the `src` test; S15 states each ack's `seq` and the driver's ceiling; S16
  and S17 move to `design_lib.py#read_spec_edges` and the driver suite; S20 and S21 carry unit 44
  S9's copies under the landed JS markers; §4 gains the texts table and the ceiling, and every line
  citation is a symbol or a blob-pinned line.

## 10. Reuse audit

Every item extends the seam its repaired unit names: `tools/unattended/unattended.sh#write_mail_ref`
and `#write_mail_post`'s steps for S15, landed by `#write_gov_ref`; `PARITY_ROWS` of
`tools/lib/resolve-python.test.sh`, whose `#blk` already reads `// >>> ` markers, for S20 and S21;
`tools/unattended/lib-unattended.sh#read_consumes_from` as the rule S16 and S17 hold
`tools/memory-tree/design_lib.py#read_spec_edges` to; `tools/runlog/extract.py#_check_inside` for
S19; and the failing `timeout` shim the driver suite already stages
(`tools/unattended/unattended.test.sh@82201773d73f:11589`) for S13. `python
tools/codebase-map/reuse_lookup.py "land several mail records on one ref with one update"`, run
2026-11-23, ranked `records`, `build_records`, `write_record` and `read_records` by the name stem
`record` alone, none a ref writer; the source read found `write_mail_ref` and `build_gov_commit`.
No item mints a mechanism where one of these fits.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted unit placed when it
repairs an earlier unit's pass" --terms "promoted order pass commit ledger superseded batch minors
hands-off consumes-from parity mirror"`
