# KICK-dKeptSession-56 — the round-1 promotions' audit's 45 minor findings, closed after every unit they land on is built

**Status:** DEFERRED · rev-3 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 31 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-56-deviation-561.md](../build/2026-10-26-build-KICK-dKeptSession-56-deviation-561.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-56-deviation-562.md](../build/2026-10-26-build-KICK-dKeptSession-56-deviation-562.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-56-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-56-promoted-fix-return.md) | research | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-25 KICK-dKeptSession-36 KICK-dKeptSession-44 |
| [2026-10-26-prompt-KICK-dKeptSession-56-1-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-56-1-spec-writer.md) | journal | KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-56-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-56-promoted-fix-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed 34 findings at MEDIUM and 11 at LOW. BUILD-METHOD M4 promotes them into one batch, and this
is it. Each finding is its own §2 item, named by report id beside its report item:

- MEDIUM: ids 1 (M1), 2 (M2), 5 (M3), 6 (M4), 23 and 52 (M5), 7 (M6), 8 (M7), 9 (M8), 10, 20 and
  45 (M9), 11 (M10), 17 (M11), 18 (M12), 19 and 46 (M13), 24 (M14), 25 (M15), 27 (M16), 29 (M17),
  30 (M18), 31 (M19), 32 (M20), 34 and 35 (M21), 36 (M22), 37 (M23), 40 (M24), 44 (M25), 47 (M26),
  50 (M27), 51 (M28), 54 (M29);
- LOW: ids 12 and 55 (L1), 13 (L2), 14 (L3), 15 (L4), 26 (L5), 33 (L6), 41 (L7), 42 (L8), 53 (L9),
  56 (L10).

Six minors are a HIGH's defect found again at a lower grade: ids 18 (H1, `KICK-dKeptSession-45`), 44
(H2, `KICK-dKeptSession-47`), 9 (H3, `KICK-dKeptSession-49`), 8 (H4, `KICK-dKeptSession-51`), and
the pairs 24 with 12 and 55, and 30 with 13, which are each other's. Their items here observe the
fix their sibling builds. The minors land on many units, so this unit is one write set and takes the
order past every unit of the build (order 31): each item amends code its unit has built. Where an
item supersedes a sibling spec's text, it does so by name, and that unit's acceptance ledger answers
the superseded text.

## 2. Scope (IN)

- **S1** — id 1, M1. `render_order` in `tools/memory-tree/gen_build_index.py` prints a group's
  Parallel cell `no — <a> consumes-from <b>` when one member's §3 Edges block names another member,
  read by the TEMPLATE-SPEC §3 bullet grammar. Observed by AC1.
- **S2** — id 2, M2. The same cell reads `no — <a> and <b> share <path>` when two members' `### Files
  touched (estimate)` paths intersect by `check_guard_trips`' rule, read by an inline copy of
  `extract_files_touched` (`tools/check-spec-tokens.py:530`) under the kit's inline-parity marker.
  Observed by AC2.
- **S3** — id 5, M3. One launcher, `run_driver(argv)` in `tools/loop/loop_lib.py`, runs
  `[resolve_bash(), <driver>, *argv]`. It finds `<driver>` once per process through `loop_lib.py`'s
  inline `resolve_kit_dir("unattended", "unattended.sh", here)`, joined with `unattended.sh`: a kit
  imports no sibling kit, and the loop kit's one block is that one (TOOL-dDeclaredLoop-12 S4), the
  locator TOOL-dDeclaredLoop-52 S3 reads the same driver through. The block's `LookupError`
  (`tools/lib/resolve_kit_dir.py:23,49`) is the one unarmed signal: `run_driver` spawns nothing and
  re-raises it unchanged, never as a `LoopError`, so each caller turns it into its own unarmed outcome,
  `KICK-dKeptSession-36` S3's absent-driver pass among them, while `resolve_bash`'s `LoopError` keeps
  meaning a present driver with no usable shell. `write_dependency_notices`' posts
  (`KICK-dKeptSession-7` S4, `KICK-dKeptSession-35`), `KICK-dKeptSession-42` S2's
  `check_interface_notice`, its S3 acks and `KICK-dKeptSession-44` S16 and S17's reads call it.
  Observed by AC3.
- **S4** — id 6, M4. `KICK-dKeptSession-36` §3's "This copy keeps govkit's contract so that extraction
  replaces it unchanged" is withdrawn by name. A loop selftest case asserts the copy refuses the
  `System32` and `WindowsApps` candidates, raises `LoopError` on a set but unusable `GOV_BASH`, and
  applies the `uname -s` test; unit 36's ledger records that the python resolver leg does not check
  `resolve_bash`. Observed by AC4.
- **S5** — id 23, M5. `GOV_BASH` passes the candidates' filter: the `System32` and `WindowsApps`
  refusal, then `uname -s` answering `MINGW` or `MSYS` on a Windows host. Observed by AC5.
- **S6** — id 52, M5. `resolve_bash`'s docstring lists each departure from `govkit.py:1170-1183`:
  the filtered override and `LoopError` for `Refusal`. Observed by AC5.
- **S7** — id 7, M6. `check_presets` judges `review.design` against the named member `opt-in` and
  `review.build` against `owed` of `review.<stage>`'s derived default, as `KICK-dKeptSession-33` S3
  judges `maintain.fixes`, and counts the pattern row unassigned. Observed by AC6.
- **S8** — id 8, M7. Observes `KICK-dKeptSession-51`'s ninth position. Observed by AC7.
- **S9** — id 9, M8. Observes `KICK-dKeptSession-49`'s stale read of a pre-unit mirror. Observed by
  AC8.
- **S10** — id 10, M9. Unit 9's per-stage `context` and `runlog.py context` agree on one transcript,
  through `KICK-dKeptSession-46`'s caller-passed root. Observed by AC9.
- **S11** — id 20, M9. `derive_context_window` is memoised per `(model, root, the variable's value)`
  per process, so N rows of one model and root cost one scan. Observed by AC10.
- **S12** — id 45, M9. `KICK-dKeptSession-30` §3's non-goal "A cache of the observation. One scan
  costs under a second" and §5's one-call price are superseded by name: §5's price is one scan per
  distinct pair times its callers, unit 9's rows, unit 14's boundary read and the context verb.
  Observed by AC10.
- **S13** — id 11, M10. `KICK-dKeptSession-5` S12's factory row and `KICK-dKeptSession-39` S1 and S2
  land in one write set, in unit 5's pass, whose gates name `build-index selftest`. Observed by AC11.
- **S14** — id 17, M11. The harness honours `CLAUDE_CODE_MAX_CONTEXT_TOKENS` only where its gate
  `yv(e)` passes, never for a first-party `claude-` model. Rung 1 stays first, as the owner's
  declaration; for a model whose id starts `claude-` the source reads `env, advisory`, and unit 30
  §4 and S5's help line quote the gate. Observed by AC12.
- **S15** — id 18, M12. Observes `KICK-dKeptSession-45`'s resolved default root. Observed by AC13.
- **S16** — id 19, M13. The runlog selftest unsets `CLAUDE_CODE_MAX_CONTEXT_TOKENS` in
  `os.environ` at import, beside the `GIT_*` scrub (`tools/runlog/selftest.py:355-356`); a case that
  wants it sets it in its child's environment. Observed by AC14.
- **S17** — id 46, M13. A canary in `main` reds any case whose child ran with the variable it did
  not set, so a later reader's variable cannot leak. Observed by AC14.
- **S18** — id 24, M14. `derive_cli_line`'s body, from `derive_cli_line() {` to its closing `}`,
  calls `read_claude_version` and spells no `--version`. Observed by AC15.
- **S19** — id 25, M15. `KICK-dKeptSession-44` S7's probe reads the schema that carries the fact,
  `grep -a -c 'hookEventName:A("PreToolUse"),permissionDecision'`, with `additionalContext` checked
  in the same object; unit 21's ledger records both. Observed by AC16.
- **S20** — id 27, M16. `KICK-dKeptSession-44` S20's reader reads an absent `Child builds` line, or
  the region's no-edge sentence, as zero dependents. Observed by AC17.
- **S21** — id 29, M17. The window scan is `extract_session(build_session_tree(path))` per main
  transcript, filtered by kind, `src` and `model`. `derive_main_transcripts(root)` holds the
  `root.glob("*/*.jsonl")` and `SID_RE` population that `measure_tree`, `measure_ready_tree` and the
  scan call. Observed by AC18.
- **S22** — id 30, M18. `read_session_version` is extracted from `derive_cli_line`'s `AI_AGENT` parse
  (`skills/session-kickoff/manifest-check.sh:414`), and `check_version_equal a b` from its
  field-wise integer compare (`:427-433`); `derive_cli_line` and `read_card_fixture_verdict` call
  both. Observed by AC19.
- **S23** — id 31, M19. `tools/unattended/mail-notice.js` carries `readCard` and `extractRouteUnits`
  inline, naming `tools/hooks/scratch-guard.js` as the source as `tools/unattended/gate-guard.js:173-177`
  does, and requires no file of the hooks kit. Observed by AC20.
- **S24** — id 32, M20. `KICK-dKeptSession-44` S33 runs `RB_BOUND=$PROGRESS_BOUND run_bounded <argv>;
  RB_BOUND=""` (`tools/unattended/unattended.sh:262`), reading its exit and `RB_OUT` for the NOTE.
  Observed by AC21.
- **S25** — id 34, M21. `policy fixtures` is owed by units 32, 33, 34 and 40 once dGroundRules' manifest
  lands it: each unit's pass names the legs `check-spec-tokens.py --legs-for` derives over its Files
  touched, and its ledger records them. Observed by AC22.
- **S26** — id 35, M21. The same for units 30, 37, 38, 39, 41, 43 and 44, whose files `policy
  fixtures`' guard holds. Observed by AC22.
- **S27** — id 36, M22. `loop selftest` is owed by units 35, 36, 42 and 44, and `loop definition
  fixtures` by unit 36, once dDeclaredLoop's manifest lands them, by S25's rule. Observed by AC22.
- **S28** — id 37, M23. `render_scaffold`'s five callers in `check_policy.py` (`:1230`, `:1498`,
  `:1499`, `:2212`, `:4439` at `3c8c4718a`) pass an explicit preset, `standard` where a fixture wants
  the full table, and `:1230`'s key count is re-derived; `KICK-dKeptSession-32` S2's "The one caller"
  is superseded. Observed by AC23.
- **S29** — id 40, M24. `.governance/policy.json` is a write of units 40 and 41, rendered by `policy.py
  mirror --write`; unit 41 §3's "`.governance/policy.json` does not move" is superseded. Observed by
  AC24.
- **S30** — id 44, M25. Observes `KICK-dKeptSession-47`'s model-attributed compactions. Observed by
  AC25.
- **S31** — id 47, M26. The S2 set of `KICK-dKeptSession-33` is data `check_presets` reads,
  `UNASSIGNED_DERIVED` in `tools/policy/presets.py`, derived from the catalogue's derived rows less S3's
  and `review.<stage>`'s, never from what the store assigns. Observed by AC26.
- **S32** — id 50, M27. A `write_consumed_acks` ack refused for no `CLAUDE_CODE_SESSION_ID` or an
  unreachable origin leaves its row open, and the transition is refused naming that cause, `mail ack
  not posted: no session id` or `: origin unreachable`, never `mail open`. Observed by AC27.
- **S33** — id 51, M28. A refused notice is posted again: the parent's next transition and `--landed`
  compare the notices its transitions owe with those its mail ref holds and post the missing ones,
  a duplicate refusing safely by its content-derived id. Observed by AC28.
- **S34** — id 54, M29. S24's call writes to `run_bounded`'s capture files, never a `$( )`; AC21's stub
  backgrounds a grandchild. Observed by AC21.
- **S35** — id 12, L1. `grep -c '^read_claude_version()'` prints `1`, and the `claude --version` line
  sits inside that function's range. Observed by AC15.
- **S36** — id 55, L1. The file spells `claude --version` once. Observed by AC15.
- **S37** — id 13, L2. A recorded `cli 2.1` against a session's `2.1.0` reads equal through
  `check_version_equal`. Observed by AC19.
- **S38** — id 14, L3. `KICK-dKeptSession-34` AC2 is a regression observation only; the deciding
  criterion is `KICK-dKeptSession-54` AC1's rewritten `preset-every-key`. Observed by AC29.
- **S39** — id 15, L4. `KICK-dKeptSession-32` §4's rejected alternative reads "never keys with no
  comment lines", rejected because the posture is hidden; the claim about unassigned rows is
  withdrawn. NOT OBSERVED: a rationale with no behaviour; unit 32's ledger answers it by this name.
- **S40** — id 26, L5. `KICK-dKeptSession-39` AC1 reads the tuple's membership and cites
  PLAY-dOrderedCharter-42 S2's import refusal, `import build_records` exiting 0, for the equality.
  Observed by AC30.
- **S41** — id 33, L6. `derive_derived_rows` filters with `check_derived` (`policy.py:132` at
  `3c8c4718a`). Observed by AC31.
- **S42** — id 41, L7. `help/orientation-card.md` (unit 43), `help/loop.md` (units 35, 36, 42) and
  `tools/policy/README.md` (unit 40) carry the texts those units' §5 name. Observed by AC32.
- **S43** — id 42, L8. `KICK-dKeptSession-44` §4 cites `ARMS_FLOORS` at `.memory-tree.conf:633` and
  `REFUSAL_CEILINGS` at `:649`; unit 44's ledger cites them so. Observed by AC33.
- **S44** — id 53, L9. Units 35, 36 and 42's ledgers name the leg that runs `tools/loop/selftest.py`
  at the close. Observed by AC22.
- **S45** — id 56, L10. `KICK-dKeptSession-35` S3's no-ordinal form: `notice — not posted <kind> to
  build:<dependent> · no Design-exit ordinal: <why>`, no post run. Observed by AC34.

## 3. Non-goals (OUT)

- The fixes of ids 3, 4, 16, 21, 22, 28, 38, 39, 43, 48 and 49: units 45 to 55.
- Rewording sibling specs: each superseded text is named here and answered in its unit's ledger.
- The report's left-shift checklist entries: no clause of this build names the bug-class checklist;
  where an item's criterion is the class arm, it says so (S2, S17).
- Renumbering any order: S1 and S2 make the label true instead.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — S12's factory row, which S13 lands with unit 39's tuple member (id 11)
- **consumes-from** `KICK-dKeptSession-30` — the window, its scan, its rung 1 and §3 and §5, S11, S12, S14 and S21 (ids 20, 45, 17, 29), and S26's legs (id 35)
- **consumes-from** `KICK-dKeptSession-31` — the eight-field id, whose act position S8 observes (id 8)
- **consumes-from** `KICK-dKeptSession-32` — `render_scaffold`'s callers and §4's alternative, S28 and S39 (ids 37, 15), and S25's legs (id 34)
- **consumes-from** `KICK-dKeptSession-33` — `check_presets` and `derive_derived_rows`, S7, S31 and S41 (ids 7, 47, 33), and S25's legs (id 34)
- **consumes-from** `KICK-dKeptSession-34` — AC2, S38 (id 14), and S25's legs (id 34)
- **consumes-from** `KICK-dKeptSession-35` — S3's refusal line and the notices' posts, S3, S33 and S45 (ids 5, 51, 56), S27 and S44 (ids 36, 53), and S42's docs (id 41)
- **consumes-from** `KICK-dKeptSession-36` — `resolve_bash`, S3 to S6 (ids 5, 6, 23, 52), S27 and S44 (ids 36, 53), and S42's docs (id 41)
- **consumes-from** `KICK-dKeptSession-37` — `read_claude_version` and `derive_cli_line`, S18, S35 and S36 (ids 24, 12, 55), and S26's legs (id 35)
- **consumes-from** `KICK-dKeptSession-38` — `read_card_fixture_verdict`'s compare, S22 and S37 (ids 30, 13), and S26's legs (id 35)
- **consumes-from** `KICK-dKeptSession-39` — the tuple member and AC1, S13 and S40 (ids 11, 26), and S26's legs (id 35)
- **consumes-from** `KICK-dKeptSession-40` — the mirror's inputs and policy.json, S29 (id 40), S25's legs (id 34) and S42's docs (id 41)
- **consumes-from** `KICK-dKeptSession-41` — the catalogue edit and policy.json, S29 (id 40), and S26's legs (id 35)
- **consumes-from** `KICK-dKeptSession-42` — `write_consumed_acks`, S3 and S32 (ids 5, 50), S27 and S44 (ids 36, 53), and S42's docs (id 41)
- **consumes-from** `KICK-dKeptSession-43` — the pointer arm's docs, S42 (id 41), and S26's legs (id 35)
- **consumes-from** `KICK-dKeptSession-44` — S7, S16, S17, S20 and S33, and its §4 citations, S3, S19, S20, S23, S24, S34 and S43 (ids 5, 25, 27, 31, 32, 54, 42), and S26 and S27's legs (ids 35, 36)
- **consumes-from** `KICK-dKeptSession-45` — the resolved default root, S15 (id 18)
- **consumes-from** `KICK-dKeptSession-46` — the caller-passed root, S10 and S11 (ids 10, 20)
- **consumes-from** `KICK-dKeptSession-47` — the model-attributed compactions, S30 (id 44)
- **consumes-from** `KICK-dKeptSession-49` — `MIRROR_KIT_INPUTS`, S9 (id 9)
- **consumes-from** `KICK-dKeptSession-51` — the act's ninth position, S8 (id 8)
- **consumes-from** `KICK-dKeptSession-54` — the restated cases, S38 (id 14)
- **consumes-from** `KICK-dKeptSession-55` — the all-or-nothing ack post, S32 (id 50)
- **hands-off** `KICK-dKeptSession-57` — S13, S25 to S27, S29 and S44 with AC11, AC22 and AC24, which that unit re-binds to its own pass (id 1)
- **hands-off** `KICK-dKeptSession-62` — S1, S2, S11, S16, S21, S23, S25, S27, S28, S33 and S36 with AC10, AC15, AC18, AC21 and AC23, which the batch's items restate or gate (ids 2 to 7, 13, 14, 19 to 22, 24 to 30, 36, 37)

## 4. Design

### Evidence

Each item's evidence is the audit's appendix row for its id, re-read for this spec on 2026-10-26. The
claims re-verified at this base: `render_order`'s docstring "Units sharing an `order` value are the
parallel group" (`gen_build_index.py:1716`) and `render_edges`' `if vals` (`:1755`); `PARITY_ROWS`
holds no `resolve_bash` row (`resolve-python.test.sh:168-184`); govkit's override accepts any
`GOV_BASH` that runs `-c :` (`govkit.py:1177-1183`); the `cli —` parse and compare
(`manifest-check.sh:414`, `:427-433`); `run_bounded` waits through capture files (`unattended.sh:228-265`);
`gate-guard.js:173-177` copies rather than requires a sibling kit's file; `.memory-tree.conf:633` is
`ARMS_FLOORS` and `:649` `REFUSAL_CEILINGS`. The harness's gate, read 2026-10-26 by `grep -a` over
`claude` 2.1.292 on PATH: `let g=a.CLAUDE_CODE_MAX_CONTEXT_TOKENS;if(g!==void 0&&g>0&&yv(e))return g;`,
and `yv` returns false for a canonical `claude-` id; the `PreToolUse` schema `hookEventName:A("PreToolUse"),
permissionDecision:...,additionalContext:o().optional()` appears twice. dGroundRules' files are read at
`3c8c4718a`.

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `run_driver` | function | `tools/loop/loop_lib.py` |
| `derive_main_transcripts` | function | `tools/runlog/extract.py` |
| `read_session_version`, `check_version_equal` | functions | `skills/session-kickoff/manifest-check.sh` |
| `UNASSIGNED_DERIVED` | derived constant | `tools/policy/presets.py` |
| `order-edge`, `order-shared-path` | fixture builds | `tools/memory-tree/gen_build_index.py`'s selftest |

### Migration

S1 and S2 change one generated cell's text in every build README at the next render; no stored state
changes shape.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`, `tools/lib/resolve-python.test.sh`
- `tools/loop/loop_lib.py`, `tools/loop/loop_transition.py`, `tools/loop/position.py`,
  `tools/loop/selftest.py`
- `tools/runlog/extract.py`, `tools/runlog/selftest.py`, `tools/runlog/fixtures/transcripts.json`
- `skills/session-kickoff/manifest-check.sh`, `skills/session-kickoff/card-store.fixture.sh`,
  `skills/session-kickoff/manifest-check.test.sh`
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`,
  `tools/unattended/mail-notice.js`
- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/build_records.py`: S13, in unit 5's pass
- `tools/policy/presets.py`, `tools/policy/check_policy.py`, `tools/policy/README.md`,
  `.governance/policy.json`
- `help/orientation-card.md`, `help/loop.md`

### Alternatives rejected

- **Two batches.** S3 and S42 cross the loop kit and its help page, S25 to S27 and S44 write the
  ledgers of units in both the policy and the loop sets, and S13 lands inside an earlier unit's pass,
  so no two write sets are disjoint by M6's clauses.
- **Renumbering the orders for ids 1 and 2.** It moves units the harness placed one step after their
  repairs; §8 F1 records it.

## 5. Production-readiness checklist

- security — S5 closes a WSL launcher let in through the override; S23 removes a cross-kit require;
  S32 refuses with its cause rather than releasing.
- perf / scale — S11 bounds the window scans to one per model and root.
- error / empty / loading states — S20's zero dependents, S32's causes and S45's no-ordinal line.
- observability — S1 and S2 name why a group is not parallel; S14's `env, advisory`.
- risks — S1 and S2 re-render every build README's order cell once.
- testing — the criteria of §6 and the arms of §7.
- migration — §4.
- user docs — `help/orientation-card.md` (S14, S42) and `help/loop.md` (S42).

## 6. Acceptance criteria

Fixtures are each repaired unit's own, named by that unit's spec, under `%TEMP%`.

- **AC1** — When `python gen_build_index.py --write` renders the `order-edge` fixture build, two units at
  one order where one consumes from the other, its build-order cell reads `no — ` naming the edge.
  Red when: it reads `yes`.
- **AC2** — When it renders `order-shared-path`, two units at one order listing one path, the cell names
  the path, and the inline copy's parity row passes. Red when: a shared write set reads `yes`.
- **AC3** — When `grep -rnE "subprocess\.(run|Popen)\(\[\"bash\"" tools/loop` runs, it prints nothing,
  and a probe stubbing `subprocess.run` records `resolve_bash()`'s path as every driver call's
  `argv[0]` and, as its `argv[1]`, the directory `resolve_kit_dir("unattended", "unattended.sh", here)`
  resolved joined with `unattended.sh`; with the unattended kit absent from every place the block
  searches, `run_driver` raises `LookupError` and the stub records no call. Red when: a loop-kit call
  launches bare `bash`, or a driver path the block did not resolve.
- **AC4** — When the loop case runs `resolve_bash` against stub `System32` and `WindowsApps` candidates
  and an unusable `GOV_BASH`, each is refused, the last with `LoopError`, and `grep -c "replaces it
  unchanged"` over unit 36's ledger prints `0`. Red when: a refused launcher is accepted.
- **AC5** — When `GOV_BASH` names a stub whose `uname -s` prints `Linux` on a Windows host, `resolve_bash`
  raises `LoopError`, and its docstring names both departures from govkit. Red when: the override admits
  the WSL launcher.
- **AC6** — When the `presets-derived` case plants standard's `review.build = "off"`, `python presets.py
  check` reds the standard-equals-default rule naming `review.build`. Red when: the key has no rule.
- **AC7** — `KICK-dKeptSession-51` AC2 and AC3 hold. Red when: the guide or the ask states seventh.
- **AC8** — `KICK-dKeptSession-49` AC1 holds. Red when: a pre-unit mirror reads FRESH.
- **AC9** — When unit 9's `--orient` row and `runlog.py context` read `context-window-sibling` under one
  `<dir>`, both print `90%`. Red when: they differ.
- **AC10** — When a probe counts `build_session_tree` calls over unit 9's AC3 fixture of 22 rows on one
  model and root, it records one scan, and unit 30's ledger states the count. Red when: N rows cost N
  scans.
- **AC11** — When `git show <unit 5's pass commit>` lists its files, both `tree_lib.py` and
  `build_records.py` are among them, and `python -c "import build_records"` exits 0 at that commit.
  Red when: the factory row lands without the tuple member.
- **AC12** — When `runlog.py context` reads a `claude-` model's transcript with the variable at 200000,
  stderr names `env, advisory`, and `grep -n "first-party" orientation-card.md` in `help/` prints the
  `context —` paragraph's sentence. Red when: the source claims the harness's own window.
- **AC13** — `KICK-dKeptSession-45` AC1 holds. Red when: the literal profile path is scanned.
- **AC14** — When a probe imports the runlog selftest with the variable exported at 500000,
  `os.environ` lacks it after import, and a planted case whose child carries it reds the canary.
  Red when: an ambient value reaches a fill case.
- **AC15** — When an `awk '/^derive_cli_line\(\) \{/,/^\}/'` range is grepped, it holds
  `read_claude_version` and no `--version`; `grep -c '^read_claude_version()' manifest-check.sh` prints
  `1`, and `grep -c 'claude --version' manifest-check.sh` prints `1`. Red when: the read is spelled twice,
  as at base.
- **AC16** — When unit 21's ledger is read, it records the schema probe's count per version beside the
  `additionalContext` check. Red when: the deny-builder count stands for the fact.
- **AC17** — When `python loop_transition.py record` moves a parent out of Design whose rendered edges
  carry the no-edge sentence, or no `Child builds` line, it posts nothing and exits 0. Red when: it
  throws or misparses.
- **AC18** — When `grep -c 'SID_RE.fullmatch(p.name' extract.py` runs in the runlog kit, it prints `1`,
  inside `derive_main_transcripts`. Red when: the population is spelled per caller.
- **AC19** — When `grep -c 'claude-code_\*' manifest-check.sh` runs, it prints `1`, and a plant recording
  `cli 2.1` under `AI_AGENT` `claude-code_2.1.0` reads `pass`. Red when: a string compare reds it.
- **AC20** — When `node mail-notice.js` runs from a scratch install holding only the unattended kit's
  files, it exits 0, and `grep -c "scratch-guard" mail-notice.js` counts only the source comment.
  Red when: the hook throws at require time.
- **AC21** — When the progress verb is stubbed to run `sleep 30 &` and exit 0, `bash unattended.sh
  --landed <slug>` returns within 12 s, and with `GATE_BOUND_LIVE=0` it still emits. Red when: the
  lander waits on the grandchild.
- **AC22** — When each named unit's ledger is read, it records the legs `check-spec-tokens.py
  --legs-for` printed over its Files touched at its pass, `policy fixtures` or `loop selftest` among
  them once their parent landed, and units 35, 36 and 42 name `loop selftest` as the leg that runs the
  loop kit's self-test at the close.
  Red when: a guarded leg is missing from a pass's record.
- **AC23** — When `grep -c "render_scaffold(rows)" check_policy.py` runs in the policy kit, it prints
  `0`, and `python check_policy.py --fixture scaffold-preset` passes. Red when: a caller raises
  `TypeError`.
- **AC24** — When `python policy.py mirror --check` runs at each of unit 40's and unit 41's pass commits,
  it exits 0. Red when: the committed mirror is stale.
- **AC25** — `KICK-dKeptSession-47` AC1 holds. Red when: another model's compaction lifts the rung.
- **AC26** — When the `presets-derived` case plants `5` on one `budgets.*` cap in `strict`, `arm_presets`
  reds naming `strict` and the key. Red when: a valid literal on an unassigned row loads green.
- **AC27** — When unit 42's AC1 runs with `CLAUDE_CODE_SESSION_ID` unset, the transition is refused
  naming `no session id`. Red when: it reads `mail open`.
- **AC28** — When the parent's first post is planted to exit 2 and a second
  `python loop_transition.py record` runs, both dependents' mail refs hold the first exit's notice. Red when: the refused notice is lost.
- **AC29** — When unit 34's ledger is read, AC2 is answered as a regression observation and AC1 by
  `KICK-dKeptSession-54` AC1. Red when: AC2 is recorded as deciding.
- **AC30** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import tree_lib,
  build_records; print('mailbox-message' in tree_lib.TYPED_RECORD_KINDS)"` runs, it prints `True`.
  Red when: the import refuses.
- **AC31** — When `grep -n "check_derived(" presets.py` runs in the policy kit, it prints
  `derive_derived_rows`' filter. Red when: a second spelling of the predicate exists.
- **AC32** — When `grep -n "GOV_BASH" loop.md` and `grep -n "skipped" orientation-card.md` run in
  `help/`, and `grep -n "presets.toml" README.md` in the policy kit, each prints its unit's sentence.
  Red when: a page a §5 names stays stale.
- **AC33** — When unit 44's ledger is read, it cites `ARMS_FLOORS` at `:633` and `REFUSAL_CEILINGS` at
  `:649`. Red when: the swapped addresses stand.
- **AC34** — When the transition log is planted unreadable, `loop_transition.py record` prints `no
  Design-exit ordinal` and runs no post. Red when: a post runs with a guessed pass or a fake rc.

## 7. Gates

`build-index selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `manifest-check self-test` · `scratch-guard self-test` · `tier2-review self-test` · `unattended kit gate` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 · the two fixture builds, staged red by the base's `render_order` · none
New arm: tools/loop/selftest.py · covers AC3 AC4 AC5 AC27 AC28 AC34 · recorded argv, refused launchers, a missing session, a refused post and an unreadable log · none
New arm: tools/runlog/selftest.py · covers AC9 AC10 AC12 AC14 · one transcript under two readers, a scan count, a first-party model and an exported variable · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC15 AC19 · the extracted reads and the integer compare · none
New arm: tools/unattended/unattended.test.sh · covers AC21 · a backgrounding progress stub · `FLOOR_ASSERTIONS` and its shard floor rise by the arm's count, counted off the diff
New arm: tools/policy/check_policy.py · covers AC6 AC23 AC26 · the two plants and the scaffold callers · none

## 8. Open questions

- **F1 — How do ids 1 and 2 stop the order region claiming parallel safety it does not check?**
  Options: (a) S1 and S2, the cell derived from edges and Files touched; (b) a `--check` that reds such
  a group; (c) renumbering the orders. (c) moves the units this disposal places one step after their
  repairs; (b) reds the ties the harness places on purpose, which `--dispatch` already serialises
  (`unattended.sh:13690-13760`). (a) meets AC1 and AC2 and leaves the dispatcher's refusals as they
  are. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Where does `CLAUDE_CODE_MAX_CONTEXT_TOKENS` rank for a first-party model, S14?** Options:
  (a) first, its source marked advisory; (b) ranked only where the harness honours it. (b) removes
  `KICK-dKeptSession-48`'s override for a 200k session of a first-party model. (a) meets AC12 and
  keeps unit 48's AC1. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the skeptic's second
  option. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the round-1 promotions' audit's minors batch.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-57`, `KICK-dKeptSession-62`
  mirrored, the other ends of the edges the round-2 promotions' audit's disposal declared
- rev-3 · 2026-10-26 · S3 · AC3 · re-grounded on the cross-check record
  `2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck`, row 108: `run_driver` finds `<driver>`
  through `loop_lib.py`'s inline `resolve_kit_dir` and passes its `LookupError` to each caller as the
  unarmed signal; AC3's stub records `argv[1]` as the resolved path.

## 10. Reuse audit

Every item extends the seam its repaired unit names, and the cross-cutting ones extend existing
mechanisms: `resolve_bash` (unit 36) under one launcher for S3, `extract_files_touched` and
`check_guard_trips` (`tools/check-spec-tokens.py:530`, `:581`) inline under the parity marker for S2,
`run_bounded` (`tools/unattended/unattended.sh:262`) for S24, `check_derived` for S41, and
`extract_session` with `build_session_tree` for S21. `python tools/codebase-map/reuse_lookup.py
"resolve the transcripts projects root honouring CLAUDE_CONFIG_DIR"` ranked name stems only and missed
`resolve_projects_root`, which the source read found; no item mints a mechanism where one of these
fits.

Recall terms used: `python tools/memory-recall/query.py "how are a spec audit's confirmed minor
findings batched into one repair unit placed after every unit" --terms "spec-audit minors batch
MEDIUM LOW promoted order hands-off consumes-from superseded ledger"`
