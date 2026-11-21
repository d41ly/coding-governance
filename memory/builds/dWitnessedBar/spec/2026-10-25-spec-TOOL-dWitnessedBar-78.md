# TOOL-dWitnessedBar-78 — the round-1 audit of units 68 to 73, its 20 minors batched: one read rule for every green record, derived and wider guards, an honest record open, and records of what each break printed

**Status:** CLOSED · rev-5 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 42 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-78-deviation-781.md](../build/2026-10-25-build-TOOL-dWitnessedBar-78-deviation-781.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-78-deviation-782.md](../build/2026-10-25-build-TOOL-dWitnessedBar-78-deviation-782.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-78-round8-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-78-round8-fix-return.md) | research | — |
| [2026-11-19-build-TOOL-dWitnessedBar-78-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-78-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-78-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-78-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-78-widen-21.md](../build/2026-11-21-build-TOOL-dWitnessedBar-78-widen-21.md) | widen | — |
| [2026-11-21-build-TOOL-dWitnessedBar-78-widen-22.md](../build/2026-11-21-build-TOOL-dWitnessedBar-78-widen-22.md) | widen | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-78-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-78-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-78-round8-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-78-round8-fix-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-88 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-78-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-78-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-78-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-78-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-78-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-78-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 68 to 73
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md`)
exited CONVERGED with 24 confirmed findings: no BLOCKER; four HIGH, ids 10, 24, 9 and 25, which
`TOOL-dWitnessedBar-74`, `-75`, `-76` and `-77` take; and 20 minors. BUILD-METHOD M4 batches every
MEDIUM and LOW into one unit, or two only where they split into disjoint write sets by M6's clauses so
that both build concurrently. §4 "Why one unit" says why these stay one. Each finding is named by
report id and is its own scope item, including where the report merged ids into one item. The minors
land on units 68 to 73, so this unit repairs no single unit and builds above every unit in the build
(order 42).

| Report item | Severity | Report id | Lands on | Scope item |
|---|---|---|---|---|
| M2 | MEDIUM | 1 | unit 70 S2, AC3; unit 72 AC3 | S1 |
| M1 | MEDIUM | 2 | unit 70 §7, AC2; unit 72 §7, AC1 | S2 |
| M3 | MEDIUM | 11 | unit 73 AC7 | S3 |
| M3 | MEDIUM | 20 | unit 73 AC7, S6 | S4 |
| L1 | LOW | 4 | unit 73 AC7 | S5 |
| M4 | MEDIUM | 5 | unit 73 S6; unit 68 §7 | S6 |
| M5 | MEDIUM | 18 | unit 69 §1, S1, §3 | S7 |
| M5 | MEDIUM | 26 | unit 69 §1, §3; unit 73 S9 | S8 |
| M6 | MEDIUM | 19 | unit 73 S6, §4 | S9 |
| M7 | MEDIUM | 27 | unit 69 S2, §5, §7 | S10 |
| L10 | LOW | 22 | unit 69 S2, AC4 | S11 |
| L9 | LOW | 21 | unit 69 §7 | S12 |
| L3 | LOW | 6 | unit 69 S1, §7 | S13 |
| L6 | LOW | 12 | unit 69 §4, §8 F2 | S14 |
| L2 | LOW | 17 | unit 72 S1, §4, §5 | S15 |
| L5 | LOW | 8 | unit 72 S3 | S16 |
| L4 | LOW | 7 | unit 71 S3; unit 73 S1 | S17 |
| L8 | LOW | 14 | unit 71 §10 | S18 |
| L7 | LOW | 13 | unit 73 §4 | S19 |
| L11 | LOW | 23 | unit 68 S1, §7 | S20 |

That is 9 MEDIUM and 11 LOW findings by raw id. Ids 11 and 20 share item M3, which describes at
MEDIUM the defect L1 (id 4) states at LOW. Ids 18 and 26 share item M5. Items M1 and M2 describe the
defect units 74 to 77 close at HIGH; S1, S2 and S15 build what remains of their fixes over those
units' slot and variants. Six items found their code already landed at HEAD (S1, S10, S11, S17, S19,
S20); each says so and keeps its observation.

## 2. Scope (IN)

- **S1** — id 1. Present at HEAD: when the CR-reach canary fails, unit 66 S2's `rec_sha` compare and
  unit 67 S2's `rec_fp` compare still run, each printing its own failure line naming its variable,
  and neither is counted in `a` (`tools/run-gates/run-gates.gov.test.sh@c9500821b:958-963`). S1
  writes no code. Unit 70's acceptance ledger beside AC3, and unit 72's beside AC3, quote both lines
  the strip-less break printed: `TOOL-dWitnessedBar-75`'s `for count 0` line, which
  `TOOL-dWitnessedBar-77` prints once per value of `rgf_whats`, and the compare's own line naming
  `rec_sha` or `rec_fp`. Observed by AC1 and AC2.
- **S2** — id 2. Unit 70's acceptance ledger beside AC2, and unit 72's beside AC1, record for each
  byte-arm break the `diff` count of the break's canary mutant against the break, which reads 1. Each
  names `TOOL-dWitnessedBar-74` AC2 or `TOOL-dWitnessedBar-76` AC2 as the per-run observation that
  answers that unit's §7 New-arm claim to reach the 41-byte comparison. Observed by AC3.
- **S3** — id 11. Unit 73 S7's selection is observed through the manifest. A probe reads the
  `run-gates gov canary` row's `guard` from `tools/gate-legs.json`, resolves each entry with
  `resolve_prefix_token` (`tools/lib/resolve_prefix_token.py`) against the tool root `tools`, and
  passes the result to `git diff --quiet HEAD~1 --` in a scratch clone whose last commit touches
  `.githooks/pre-push` alone. It exits 1. Observed by AC4.
- **S4** — id 20. The probe of S3 is seen red. In the same clone, a scratch manifest whose gov canary
  row lacks `.githooks/pre-push`, and one that spells it `{prefix}/.githooks/pre-push`, each make the
  probe exit 0 on the hook-only commit. Observed by AC5.
- **S5** — id 4. Unit 73's acceptance ledger beside AC7 names this unit's AC4 and AC5 as the
  observation of 73 S7, since AC7's typed pathspec exits 1 on a hook-only commit whatever the guard
  holds. Observed by AC6.
- **S6** — id 5. The `run-gates gov canary` row's `guard` gains `{prefix}/`. The row is declared in
  its `[[exempt_leg]]` row of `tools/govkit/registry.toml` (`@c9500821b:827-840`) and rendered into
  `tools/gate-legs.json` by `python tools/run-gates/leg_factory.py --write`, the route unit 73's
  guard entry took (`daa7d6534`); the manifest is never hand-edited. Unit 68's arm runs
  `read --backend local-hook`, whose `read_backends(tool_root)` reads every `tools/*/kit.toml`
  (`tools/run-gates/verdict_backends.py#read_backends`) and whose `check_backend` refuses before any
  read (unit 6 S1, S2), so an edit to any kit's descriptor selects the leg and moves its reuse key.
  Observed by AC7.
- **S7** — id 18. `read_bar_file` (`.githooks/pre-push#read_bar_file`) reads with the rules unit 69
  S1 gives `read_green_file` (`.githooks/pre-push#read_green_file`): one
  `while IFS= read -r _rb_l || [ -n "$_rb_l" ]` loop over the file, a line with no TAB skipped, the key
  before the first TAB and the value after it, one trailing CR stripped from the value, and the last
  line of a repeated key winning. `_rb_l`, `_rb_k`, `_rb_v` and `_rb_n` are `local`, in place of
  `k v n ln`. A `selection.<n>` value is then the row past its first TAB by the general rule, the value
  its own `case` line gives it at HEAD, and its one CR strip is the one `read_tag_lines`
  (`tools/run-gates/verdict_backends.py#read_tag_lines`) gives every value. The `case` holds one
  `<key>) bg_<name>=$_rb_v ;;` per line, as `read_green_file`'s does. Its callers `check_bar_record`,
  `check_bar_base` and `check_cover_record` read it as they do today. The AC12 arm plants, in a third
  record, each key derived from the cut's `case` labels by unit 73 S9's `sed`, as
  `<key><TAB>old<LF>` then `<key><TAB>new<CR><LF>`, its pairs read from a file and never from a
  here-string of a substitution, and asserts each derived `bg_*` variable reads `new`, as
  `TOOL-dWitnessedBar-73` S9 does for `read_green_file`. The `selection.[1-9]*` label, which fills
  the `bg_sel_rows` array, is outside the derivation. Observed by AC8.
- **S8** — id 26. The inherited-green block reads its record through `read_bar_file`. `read_bar_file`
  also reads `max_age` and `blocks` into `bg_age` and `bg_blocks`; it reads `reused` and
  `reused_cache` at HEAD. `check_bar_base`'s `local` list names both new variables. A function
  `read_inherited_green <path>`, defined beside `read_bar_file` and outside the block, declares every
  `bg_*` variable `local`, as `check_bar_base` does (`.githooks/pre-push#check_bar_base`), calls
  `read_bar_file`, and sets the ten `ig_*` variables from it, in place of the block's ten
  `ig_x=$(awk ...)` reads (`.githooks/pre-push@c9500821b:2118-2127`). S7's derived key list then
  covers `base`, `max_age` and `blocks`. Observed by AC9.
- **S9** — id 19. Unit 73 S6's guard entry `.githooks/pre-push` reaches other builds' carried specs
  only through an ask row. The population is every DEFERRED spec of another build whose Files
  touched names `.githooks/pre-push` and for which `python tools/check-spec-tokens.py --spec <path>`
  prints `run-gates gov canary <- .githooks/pre-push`: `PLAY-dConvergedCharter-41`,
  `TOOL-dPlacedRequest-11`, `TOOL-dWellOiledMachine-10` and `TOOL-dWellOiledMachine-17` (four,
  DERIVED 2026-11-21 at `c9500821b`, §4 Evidence). This unit files one ask row per build (§8 F5) in
  `memory/builds/dConvergedCharter/BACKLOG.md`, `memory/builds/dPlacedRequest/BACKLOG.md` and
  `memory/builds/dWellOiledMachine/BACKLOG.md`. Each names its specs and the token
  `run-gates gov canary <- .githooks/pre-push` each spec's §7 owes once it leaves DEFERRED, with a
  `SEV` disposition line. The builder re-runs the derivation at its pass and files for what it
  prints, recording any difference from the four in this unit's ledger. S6's `{prefix}/` is broad
  and owes no spec a leg. Unit 73's acceptance ledger beside AC6 names the four specs and how they
  were found. Observed by AC10.
- **S10** — id 27. Present at HEAD (§8 F4): `read_local_verdict`
  (`tools/run-gates/verdict_backends.py#read_local_verdict`) opens the record with
  `errors="replace"`, so no decode raises, turns an `OSError` into `DEAD PROBE` naming the error, and
  reads a record path that is no file as `NONE`. So no malformed or unreadable record raises out of
  the read. S10 writes no code. Observed by AC11.
- **S11** — id 22. Present at HEAD: that open is spelled
  `open(slot, encoding="utf-8", errors="replace", newline="")`, unit 69 S2's, so the encoding posture
  scanner finds no unencoded text read in the module. S11 writes no code. Observed by AC12.
- **S12** — id 21. This unit's §7 names `pre-push bar self-test`, `push-main self-test` and
  `pre-push run-log line`, the suites that push through the hook's green-record readers, as unit 65
  S18 named the first for `read_green_file`. Unit 69's acceptance ledger beside AC3 names this unit's
  §7 as the close's declared gate set for the rewritten readers. Observed by AC13.
- **S13** — id 6. Unit 69 S1's three line rules are held by an arm. The AC12 arm writes a fourth
  record holding `manifest<TAB>x<TAB><LF>`, a bare `fingerprint<LF>` and a final `selftests<TAB>on`
  with no LF. Read through the cut `read_green_file`, `rec_man` is `x<TAB>`, `rec_fp` is empty and
  `rec_st` is `on`; read through the cut `read_bar_file`, `bg_man`, `bg_fp` and `bg_st` are the same.
  Observed by AC14.
- **S14** — id 12. Unit 69's acceptance ledger beside AC2 states the BINMODE platform fact: the
  environment form `BINMODE=3 awk` keeps no CR, `awk -v BINMODE=3` keeps it, and `$(...)` loses a CR
  only when an LF follows it. It states that unit 69 §8 F2's option (c) stands discarded on its seven
  forks, the gawk-only variable and `print $2`'s TAB truncation, not on CR loss. Observed by AC15.
- **S15** — id 17. Unit 72's acceptance ledger beside AC1 answers its §4 Inventory's "Minted:
  nothing" and its §5 observability line. It quotes the canary's failure line whole with its slot,
  and names the `rec_fp` value as minted by `TOOL-dWitnessedBar-75` (its rev-3 §8 F3). Observed by
  AC16.
- **S16** — id 8. Unit 72's acceptance ledger beside AC3 states S3's reason as a sentence: since unit
  69 S1 makes one strip serve every key, one strip-less `read_green_file` is the `rec_fp` break.
  Observed by AC17.
- **S17** — id 7. Present at HEAD: section `2o` of `tools/lib/resolve-python.test.sh` holds one
  `refs/heads/master` assertion per fixture builder `TOOL-dWitnessedBar-73` S1 grades, the
  corrupt-HEAD loop's and `child`'s, each failing as `73 AC1:`, and unit 71 wrote none, so each
  fixture already holds one. S17 writes no code. Unit 71's acceptance ledger beside AC3 names unit 73 AC1
  as the observation of 71 S3's `refs/heads/master` clause. Observed by AC18.
- **S18** — id 14. Unit 71's acceptance ledger beside AC1 names
  `tools/memory-tree/check-verdict-epoch.test.sh@c9500821b:31-32` as the two-key bash precedent for
  S1's `GIT_CONFIG_COUNT=2` plant, and states that `git grep -n GIT_CONFIG_COUNT -- tools` printed
  35 lines at `c9500821b` (PINNED 2026-11-21 by that `git grep`). Observed by AC19.
- **S19** — id 13. Present at HEAD: unit 73 rev-5 (`129dee4f6`) cites unit 67's Files touched by
  count and quote, no line of unit 67's spec, so the wrong line numbers are gone. NOT OBSERVED: a
  correction to spec text, which no built artifact carries and no criterion of unit 73 reads. §4
  Evidence of this spec records the measurement.
- **S20** — id 23. Present at HEAD: the suite runs `verdict_backends.py` only through `"$PYBIN"`, the
  plant loop as `"$PYBIN" "$KITDIR/verdict_backends.py" --fixture --plant "$vb_plant"` and the clean
  plant's record through `"$PYBIN" -c` calling `V.run_local_plant("clean", ...)`, and no line of the
  suite opens a command with a bare `python`. S20 writes no code. Observed by AC20.

## 3. Non-goals (OUT)

- Re-wording the spec text of units 68 to 73. Each item is closed by what this pass builds or
  observes, and a claim or criterion it answers is answered in that unit's acceptance ledger by name.
- The left-shift gates the report names: the checklist entries, the spec lints for typed guards,
  hand-named gate lists and sibling-spec citations, and the grep for every reader of a changed file.
  No clause of this build names them. S3's derived probe, S7's derived key list and S13's arm are the
  regressions this batch builds.
- The runner's `read_record_keys` (`tools/run-gates/run-gates.sh#read_record_keys`), which units 65
  and 67 own and which reads by unit 69 S1's rules at HEAD. S7 and S8 bring the hook's readers to one
  rule; the runner's reader stays as those units leave it.
- The `§7` of the four specs S9 names. S9 files the asks; the owning builds edit their specs.
- S10's rev-4 outcome, `NONE` with a stderr line for an unreadable or undecodable record (§8 F4).
- Nothing here waits on `TOOL-dWitnessedBar-28`: S6 declares its guard in the registry row, as at HEAD.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-68` — S1's plant call in the AC12 arm, which S20 observes spelled through the suite's launcher, and the `read --backend local-hook` read whose registry S6's guard covers (ids 5 and 23)
- **consumes-from** `TOOL-dWitnessedBar-69` — S1's loop rules, which S7 and S8 bring to `read_bar_file` and the inherited green and S13 holds by an arm, S2's record open, which S10 and S11 observe, and its ledger lines for AC2 and AC3 (ids 6, 12, 18, 21, 22, 26, 27)
- **consumes-from** `TOOL-dWitnessedBar-70` — the canary's failure path, after which the compares still run, and its ledger lines for AC2 and AC3 (ids 1 and 2)
- **consumes-from** `TOOL-dWitnessedBar-71` — section `2o`'s fixture builders and its ledger lines for AC1 and AC3, which S17 and S18 answer (ids 7 and 14)
- **consumes-from** `TOOL-dWitnessedBar-72` — the `rec_fp` canary and its ledger lines for AC1 and AC3, which S1, S2, S15 and S16 answer (ids 1, 2, 8, 17)
- **consumes-from** `TOOL-dWitnessedBar-73` — S6's guard entry, S7's selection, S9's derived planting and AC7, which S3 to S9 observe, widen or answer (ids 4, 5, 11, 13, 19, 20, 26)
- **consumes-from** `TOOL-dWitnessedBar-74` — its AC2, the per-run observation S2 names for unit 70's New-arm claim (id 2)
- **consumes-from** `TOOL-dWitnessedBar-75` — the slotted failure line, its `for count 0` value and the `rec_fp` value, which S1 quotes beside the compares' own lines and S15 names as minted there (ids 1 and 17)
- **consumes-from** `TOOL-dWitnessedBar-76` — its AC2, the per-run observation S2 names for unit 72's New-arm claim (id 2)
- **consumes-from** `TOOL-dWitnessedBar-77` — one failure line per value of `rgf_whats`, the lines S1 and S15 quote (ids 1 and 17)
- **hands-off** `TOOL-dWitnessedBar-82` — the third and fourth records, the compares and the New-arm claim, which unit 82's restated floor counts and answers in this unit's ledger (id 2 of the round-1 spec audit of units 74 to 78, item H2)
- **hands-off** `TOOL-dWitnessedBar-84` — S6's guard row, S7's derived planting, AC8 and the guard probes of S3, S4 and AC7, which unit 84 widens by the merge-bar guide, derives through one counted helper and observes through `--legs-for` (ids 9, 12, 13, 16, 22 of the round-1 spec audit of units 74 to 78)
- **hands-off** `TOOL-dWitnessedBar-88` — AC5's manifest lacking the hook entry and the ledger line for AC8, which unit 88 observes at this unit's pass commit and grades once its `.githooks/` guard entry lands (ids 4 and 21 of the round-1 spec audit of units 79 to 84)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. The reader half, S6 to S8
and S13, writes `.githooks/pre-push`, `tools/run-gates/run-gates.gov.test.sh`,
`tools/govkit/registry.toml`, `tools/gate-legs.json` and the shell-role rows. The rest writes three
other builds' `BACKLOG.md` and five acceptance ledgers. So the two write sets are disjoint. Dispatch is
strictly sequential, a shared order included (`tools/workflows/unattended-build.js@c9500821b:78-82`),
so a split would buy no concurrency. One unit holds all 20 findings, as `TOOL-dWitnessedBar-73` §4
held its 23.

### Evidence

Read at HEAD `c9500821b` on 2026-11-21 unless dated otherwise.

- `read_bar_file` (`.githooks/pre-push#read_bar_file`) loops `while IFS= read -r ln`, with no
  `|| [ -n ]` guard, skips a line with no TAB, then splits with `IFS=$'\t' read -r k v <<<"$ln"`,
  strips no CR, and takes a `selection.<n>` value as `${ln#*$'\t'}`. Its `case` sets several keys
  per line and reads `reused` and `reused_cache`, but not `max_age` or `blocks`. `check_bar_record`,
  `check_bar_base` (twice) and `check_cover_record` call it; `check_bar_base` declares its `bg_*`
  copies `local` (`.githooks/pre-push#check_bar_base`).
- `read_tag_lines` splits on LF alone and strips one trailing CR from every value, selection rows
  included (`tools/run-gates/verdict_backends.py#read_tag_lines`).
- The inherited-green block reads ten keys with `ig_x=$(awk -F'\t' '$1==k{print $2}' "$_ig")`
  (`.githooks/pre-push@c9500821b:2115-2127`), and the runner writes `gate-inherited-green` with those
  keys plus `legs`, `run_id` and `stamped` (`tools/run-gates/run-gates.sh@c9500821b:6311-6325`).
- The `run-gates gov canary` guard is `["{prefix}/run-gates/", "{prefix}/gate-legs.json", ".githooks/pre-push"]`,
  declared at `tools/govkit/registry.toml@c9500821b:836` and rendered by the leg factory. The runner
  selects a guarded leg by `! git diff --quiet "$BASE" -- "$@"` (`tools/run-gates/run-gates.sh#changed`).
  A guard holding a glob character goes to `input_key`, whose `git ls-files -s` does expand it
  (`tools/run-gates/run-gates.sh#build_input_keys`), but the key's dirt share compares each dirty
  path to each entry LITERALLY (`tools/run-gates/run-gates.sh#build_key_text`), and
  `@c9500821b:3996-3999` says a too-narrow guard is carried forward until its key moves. So a glob
  entry leaves an uncommitted sibling descriptor out of the key.
- `govkit.py`'s guard classifier puts every entry under the tool root in the `kit-relative` class
  (`tools/govkit/govkit.py#selfcheck`), so `{prefix}/` resolves to `tools/` and classifies once.
  `tools/` is carried by 13 legs (DERIVED by the spec-token run's broad list), above
  `BROAD_LEG_FLOOR = 5` (`tools/check-spec-tokens.py@c9500821b:647`), so the join excludes it and S6
  owes no carried spec a leg.
- `python tools/check-spec-tokens.py --legs-for .githooks/pre-push` prints the exact guard for
  `run-gates gov canary` and `measure-legs selftest` alone, below the floor, so the join reads it.
  `LIVE` (`tools/check-spec-tokens.py@c9500821b:616`) grades OPEN, SPECCED, INPROGRESS and BLOCKED
  specs alone. `TOOL-dSafePassage-11` and `PLAY-dOrderedCharter-17`, which rev-4 named, are CLOSED.
  A walk over `memory/builds/*/spec/` found seven DEFERRED specs whose Files touched names the hook
  (DERIVED 2026-11-21); three name the leg, this unit among them, and `--spec` over the other four
  prints the `run-gates gov canary <- .githooks/pre-push` hit for each (S9).
- `read_local_verdict` reads `NONE` where the record is no file, opens it with
  `encoding="utf-8", errors="replace", newline=""`, and maps an `OSError` to `DEAD PROBE`
  (`tools/run-gates/verdict_backends.py#read_local_verdict`); `help/verdict-backends.md` states
  `DEAD PROBE` as "The read itself failed, so nothing is known". The posture probe of AC12 prints `[]`
  over the module (`tools/gate-lint/encoding_posture.py#scan_text_io`).
- `tools/run-gates/run-gates.gov.test.sh` sets `PFX` at `@c9500821b:49`, `ROOT` at `:54`, `PYBIN` at
  `:240` and `KITDIR` at `:281`; AC20's ban grep prints nothing.
- BINMODE, probed on this node on 2026-10-25 (GNU Awk 5.4.0, bash 5.3.9 `x86_64-pc-cygwin`) over a
  `sha<TAB>` forty `b` `<CR><LF>` line: `BINMODE=3 awk ... print length($2)` printed 40,
  `awk -v BINMODE=3 ...` printed 41, and `x=$(awk -v BINMODE=3 ... END{printf "%s", v})` held 41
  bytes.
- `grep -cE 'TOOL-dWitnessedBar-67[.]md:[0-9]'` over unit 73's spec prints 0 (PINNED 2026-11-21).
- `git grep -n GIT_CONFIG_COUNT -- tools` prints 35 lines (PINNED 2026-11-21 at `c9500821b`), among
  them `tools/memory-tree/check-verdict-epoch.test.sh@c9500821b:31-32`, which exports
  `GIT_CONFIG_COUNT=2` with `core.autocrlf` and `commit.gpgsign`.
- `tools/lib/resolve_prefix_token.py` holds the canonical `resolve_prefix_token`, the function the
  runner inlines (`tools/run-gates/run-gates.sh@c9500821b:2972-2983`, `:5351-5362`). AC4's probe prints
  `tools/run-gates/ tools/gate-legs.json .githooks/pre-push` at HEAD.
- `memory/map/generated/symbols.json` holds no symbol of `.githooks/pre-push` (DERIVED 2026-11-21),
  so `read_inherited_green` joins no map, and the arms mint no suite function.

### Inventory

Minted: the hook function `read_inherited_green`; the `read_bar_file` locals `_rb_l`, `_rb_k`, `_rb_v`
and `_rb_n`; the variables `bg_age` and `bg_blocks`; S7's third and S13's fourth record in the AC12
arm; and S9's three ask rows, each under the next free id of its build's family. No constant, plant
or flag. Naming cells: `read_inherited_green` leads with `read`, which `python tools/lexicon/lexicon.py
--suggest read_inherited_green --as sh.function` reports `OK`; it nests no helper.

### Migration

None: no stored data changes. Every record the runner writes holds one TAB-separated key per line,
each once, ending in LF, so S7 and S8 read each to the values the base reads give. S6 widens when one
leg runs and narrows nothing.

### Rollout

Live at landing, at order 42 beside `TOOL-dWitnessedBar-87`, after every order-41 unit, the last of
them `TOOL-dWitnessedBar-81`. Dispatch sorts a tie by id string, so this unit builds before unit 87,
whose Files touched names `memory/builds/dWitnessedBar/build/`; unit 81 names only the ledgers of
units 74 and 76, which this unit does not touch. S1, S2, S5, S9, S12 and S14 to S18 are answered in
other units' ledgers at the close.

### Files touched (estimate)

- `.githooks/pre-push`: S7's loop and S8's function and block.
- `tools/run-gates/run-gates.gov.test.sh`: S7's third and S13's fourth record in the AC12 arm.
- `tools/govkit/registry.toml`: S6's guard entry in the gov canary's `[[exempt_leg]]` row.
- `tools/gate-legs.json`: re-rendered by `python tools/run-gates/leg_factory.py --write`.
- `memory/project/shell-role.txt`: the rows of the hook and the gov suite, each read from the file.
  When an edit grows a file past its row, the pass widens it with
  `python tools/memory-tree/ratchet.py widen shell-role --key <path> --reason "TOOL-dWitnessedBar-78 <item>" --unit TOOL-dWitnessedBar-78`,
  as unit 69's ledger records doing.
- `memory/builds/dWitnessedBar/build/`: each widen record that command writes, and this unit's own
  acceptance ledger.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-69-1-acceptance-ledger.md`:
  S12's and S14's lines.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-70-1-acceptance-ledger.md`:
  S1's and S2's lines.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-71-1-acceptance-ledger.md`:
  S17's and S18's lines.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-72-1-acceptance-ledger.md`:
  S1's, S2's, S15's and S16's lines.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-73-1-acceptance-ledger.md`:
  S5's and S9's lines.
- `memory/builds/dConvergedCharter/BACKLOG.md`
- `memory/builds/dPlacedRequest/BACKLOG.md`
- `memory/builds/dWellOiledMachine/BACKLOG.md`

### Alternatives rejected

- **Two batches, reader half and the rest.** §4 "Why one unit".
- **Narrow unit 69's title and goal to `read_green_file`, naming `read_bar_file` and the inherited
  green out of scope (ids 18 and 26, option (b)).** It leaves three readers of one runner format on
  two rules, with no owning unit, and §8 F2 says why it loses.
- **Give the guard `{prefix}/*/kit.toml` (id 5's first option).** It selects through `git diff`, but
  the key's dirt share compares literally (§4 Evidence), so an uncommitted sibling descriptor would not
  move the leg's reuse key and a stale green could be carried forward.
- **List each kit's `kit.toml` in the guard.** A kit added later is unguarded, the C16 class again.
- **Run the arm's read over a fixture tool root holding only the run-gates descriptor.** Unit 6's
  CLI takes no tool-root argument, so this needs a new flag, a public surface this batch may not add.
- **Hand-edit `tools/gate-legs.json`.** The leg factory renders it and `gate-leg conformance` reds a
  row that differs from its declaration.

## 5. Production-readiness checklist

- security — S7 and S8 put the hook's push decision on one read rule for every green record; each
  still fails closed to a full bar on a record it refuses. S9 writes only ask rows outside this
  build, as the build README allows.
- perf / scale — S8 replaces ten awk processes with one builtin loop on the inherited-green path.
  S6 runs the gov canary on any `tools/` change once GATE_SELFTESTS is set, which
  `SELFTESTS_OWED_PATHS="tools/"` already sets for every such change.
- error / empty / loading states — S13 states the no-TAB, trailing-TAB and unterminated cases; AC11
  holds the landed stray-byte and directory cases.
- observability — none added; the read's state line names an unreadable record as at HEAD.
- risks — a record line with no TAB is skipped by `read_bar_file` at HEAD and stays skipped; an
  unterminated last line, dropped at HEAD, is now read.
- testing — AC1, AC4, AC5, AC7 to AC9, AC11, AC12, AC14, AC18 and AC20 by probe, fixture or scratch
  clone; the rest by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch clone whose `.githooks/pre-push` has a `read_green_file` holding no
  `%$'\r'`, the arm prints the canary's `for count 0` line, a failure line naming `rec_sha` and one
  naming `rec_fp`.
  Red when: the compares are skipped when the canary fails, so the strip-less break prints no line
  naming a variable.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — When `grep -n 'AC3' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-70*acceptance-ledger*`
  and the same grep over unit 72's ledger run at the close, each line quotes `for count 0` and the
  compare's line naming `rec_sha` or `rec_fp`, and names `TOOL-dWitnessedBar-78`.
  Red when: the strip-less break is recorded with the canary's line alone.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When `grep -n 'diff count' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-70*acceptance-ledger*`
  and the same grep over unit 72's ledger run at the close, each byte-arm break's line reads 1 and
  names `TOOL-dWitnessedBar-74` AC2 or `TOOL-dWitnessedBar-76` AC2.
  Red when: a byte-arm red is recorded from a break whose mutant changed two lines.
  permission: the arm's run is the main loop's, at the close.
- **AC4** — When the S3 probe runs in a scratch clone whose last commit touches `.githooks/pre-push`
  alone, with its pathspecs printed by
  `python -c "import json, sys; sys.path.insert(0, 'tools/lib'); from resolve_prefix_token import resolve_prefix_token as r; print(' '.join(r(g, 'tools') for l in json.load(open(sys.argv[1], encoding='utf-8')) if l['name'] == 'run-gates gov canary' for g in l['guard']))" tools/gate-legs.json`,
  `git diff --quiet HEAD~1 --` over them exits 1.
  Red when: the probe types the pathspecs, so it passes whatever the guard holds.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
- **AC5** — When the same probe reads a scratch `tools/gate-legs.json` whose gov canary row lacks
  `.githooks/pre-push`, and then one spelling it `{prefix}/.githooks/pre-push`, it exits 0 both times
  on the hook-only commit.
  Red when: a misspelt or missing hook entry leaves the probe at exit 1.
  fixture: the scratch clone of AC4.
- **AC6** — When `grep -n 'AC7' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-73*acceptance-ledger*`
  runs at the close, the line names `TOOL-dWitnessedBar-78` AC4 and AC5.
  Red when: unit 73 AC7 is recorded green on its typed pathspec alone.
  permission: the ledger is written at the close.
- **AC7** — When the AC4 probe runs on the built tree, its printed pathspecs hold `tools/`. In a
  scratch clone whose last commit touches `tools/hooks/kit.toml` alone, `git diff --quiet HEAD~1 --`
  over them exits 1, and no printed entry holds `*`, `?` or `[`.
  Red when: a change to a sibling kit's descriptor leaves the gov canary unselected, or a glob entry
  that the key's dirt share cannot match stands in the guard.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
- **AC8** — When a probe sources the function cut by `awk '/^read_bar_file\(\)/,/^}/' .githooks/pre-push`
  and calls it on S7's third record, each `bg_*` variable derived from the cut's `case` labels reads
  `new`, three bytes, and the derived list holds `base`, `max_age` and `blocks`. Against a scratch
  hook whose `read_bar_file` keeps `while IFS=$'\t' read -r k v`, the arm fails naming a `bg_*`
  variable.
  Red when: `read_bar_file` keeps a CR or a key's first value, or the derived list is empty and the
  arm passes.
  fixture: a record the probe writes under `%TEMP%/<short-name>`.
- **AC9** — When `awk '/^inh_sha=""; inh_why=""/,/^fi$/' .githooks/pre-push` is piped to
  `grep -c 'awk'`, it prints 0, and piped to `grep -c 'read_inherited_green'`, it prints 1. A probe
  sourcing `read_bar_file` and `read_inherited_green` over a record holding `sha<TAB>` forty `b`
  `<CR><LF>` and `max_age<TAB>7<CR><LF>` gives `ig_sha` 40 bytes and `ig_age` as `7`, and leaves a
  `bg_sha` set before the call unchanged.
  Red when: the inherited green keeps its own awk reads, or its read overwrites the caller's `bg_*`.
- **AC10** — When `grep -n 'run-gates gov canary <- .githooks/pre-push' memory/builds/dConvergedCharter/BACKLOG.md memory/builds/dPlacedRequest/BACKLOG.md memory/builds/dWellOiledMachine/BACKLOG.md`
  runs on the built tree, it prints one ask row in each, naming `PLAY-dConvergedCharter-41`,
  `TOOL-dPlacedRequest-11`, and `TOOL-dWellOiledMachine-10` with `TOOL-dWellOiledMachine-17`
  respectively. Unit 73's ledger line for AC6 names the four specs and the `--spec` runs that found
  them.
  Red when: the wider guard is landed with no ask row for a carried spec it reaches.
- **AC11** — When `python verdict_backends.py read --backend local-hook --sha <sha>` runs in
  `tools/run-gates/` over a fixture whose per-tree record holds a `0xff` byte in a value, it prints
  its `verdict: local-hook · ` line and stderr holds no `Traceback`; over one whose record path is a
  directory, it prints a line carrying `· NONE ·` and no `Traceback`.
  Red when: the open drops `errors="replace"`, so a stray byte raises `UnicodeDecodeError` out of the
  read.
  fixture: the `clean` plant fixture of `TOOL-dWitnessedBar-56` AC6, under `%TEMP%/<short-name>`.
- **AC12** — When `python -c "import ast, sys; sys.path.insert(0, '../gate-lint'); import encoding_posture as e; print(e.scan_text_io(ast.parse(open(sys.argv[1], encoding='utf-8').read())))" verdict_backends.py`
  runs in `tools/run-gates/` on the built tree, it prints `[]`, and
  `grep -n 'encoding="utf-8", errors="replace", newline=""' verdict_backends.py` in the same
  directory names the record's open.
  Red when: the open names `newline=""` and no encoding, which the unguarded encoding leg reds.
- **AC13** — When `grep -n 'AC3' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-69*acceptance-ledger*`
  runs at the close, the line names `TOOL-dWitnessedBar-78` §7 and `pre-push bar self-test`.
  Red when: the close's gate set for the rewritten reader omits the suites that push through it.
  permission: the ledger is written at the close.
- **AC14** — When a probe sources the cut `read_green_file` and the cut `read_bar_file` over S13's
  fourth record, `printf %s "$rec_man" | od -c` and `printf %s "$bg_man" | od -c` each show `x \t`,
  `rec_fp` and `bg_fp` are empty, and `rec_st` and `bg_st` are `on`. Against a scratch hook whose
  `read_green_file` splits with `IFS=$'\t'`, the arm fails naming `rec_man`; against one whose loop
  lacks `|| [ -n "$_rg_l" ]`, it fails naming `rec_st`.
  Red when: a read trims a value's trailing TAB, sets a variable from a line with no TAB, or loses an
  unterminated last line, with the arm green.
  fixture: a record the probe writes under `%TEMP%/<short-name>`.
- **AC15** — When `grep -n 'BINMODE' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-69*acceptance-ledger*`
  runs at the close, the line states that `-v BINMODE=3` keeps the CR and the environment form does
  not, and names `TOOL-dWitnessedBar-78`.
  Red when: unit 69's record still rests option (c)'s discard on a CR that `$(...)` loses.
  permission: the ledger is written at the close.
- **AC16** — When `grep -n 'Minted' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-72*acceptance-ledger*`
  runs at the close, the line quotes the canary's failure line whole with `for <what>`, and names
  `TOOL-dWitnessedBar-75` as where the `rec_fp` value is minted.
  Red when: unit 72's "Minted: nothing" stands unanswered beside a criterion that needs the slot.
  permission: the ledger is written at the close.
- **AC17** — When `grep -n 'one strip serve every key' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-72*acceptance-ledger*`
  runs at the close, it names the AC3 line.
  Red when: unit 72 S3's reason is recorded as the verbless clause the spec carries.
  permission: the ledger is written at the close.
- **AC18** — When `grep -n -A1 '= refs/heads/master \]' tools/lib/resolve-python.test.sh` runs on
  the built tree, it prints one assertion per fixture builder unit 73 S1 grades, each followed by a
  `73 AC1:` failure line, and `grep -c '71 S3\|71 AC3' tools/lib/resolve-python.test.sh` prints 0.
  Unit 71's ledger line for AC3 names `TOOL-dWitnessedBar-73` AC1.
  Red when: two assertions grade one fixture's branch, so either builder's red is ambiguous.
  figure: the builder count is DERIVED at observation time; it read 2 at `c9500821b` (PINNED 2026-11-21).
- **AC19** — When `grep -n 'check-verdict-epoch.test.sh@' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-71*acceptance-ledger*`
  runs at the close, the AC1 line names it and states 35 lines (PINNED 2026-11-21 by `git grep -n GIT_CONFIG_COUNT -- tools`).
  Red when: unit 71's reuse audit stands with the two-key precedent unnamed.
  figure: 35 is PINNED, measured at `c9500821b` on 2026-11-21.
  permission: the ledger is written at the close.
- **AC20** — When `grep -nE '(^|[;&|(]|then|do)[[:space:]]*python[0-9.]*[[:space:]]' tools/run-gates/run-gates.gov.test.sh`
  runs on the built tree, it prints nothing, and
  `grep -c '"$PYBIN" "$KITDIR/verdict_backends.py" --fixture --plant' tools/run-gates/run-gates.gov.test.sh`
  and `grep -c 'V.run_local_plant("clean"' tools/run-gates/run-gates.gov.test.sh` each print 1.
  Red when: the plant runs through a bare `python`, which the resolver leg's idiom ban reds and the
  MS-Store stub cannot run.

## 7. Gates

`run-gates gov canary` · `run-gates canary` · `measure-legs selftest` · `pre-push self-test` · `pre-push bar self-test` · `push-main self-test` · `pre-push run-log line` · `encoding posture (text IO names its encoding)` · `python resolver (behaviour + inline parity + idiom ban)` · `gate-leg conformance` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `portability (shell lines only shrink)` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `policy fixtures` · `memory hygiene`

`measure-legs selftest` is owed for `.githooks/pre-push`, and it, `run-gates canary`,
`run-gates gov canary` and `policy fixtures` for `tools/gate-legs.json`. `govkit selftest`,
`govkit refusal join`, `govkit acceptance matrix`, `recall floor arms` and `policy fixtures` are owed
for `tools/govkit/registry.toml`; `gate-leg conformance` checks the manifest renders from it, and
`govkit selfcheck` grades S6's entry's class. `recall floor` and `recall floor arms` are owed for the
paths under `memory/`. `pre-push bar self-test`, `push-main self-test` and `pre-push run-log line` are
S12's. `portability (shell lines only shrink)` reads the shell-role rows, `lexicon naming predicates`
grades `read_inherited_green`, and `encoding posture (text IO names its encoding)` and
`python resolver (behaviour + inline parity + idiom ban)` hold AC12's and AC20's landed shapes. Every
leg here whose subject is `kit` or whose chunk is `selftests` is held unless the main loop sets
GATE_SELFTESTS at the close (`tools/run-gates/run-gates.sh#derive_hold_source`), which
`SELFTESTS_OWED_PATHS="tools/"` does (`.unattended.conf@c9500821b:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC8 AC14 · `read_bar_file`'s every-key record and the line-rule record over both readers, staged red by a `read_bar_file` that keeps `IFS=$'\t' read -r k v` (reaches a `bg_*` variable), by an `IFS=$'\t'` split (reaches `rec_man`) and by a loop with no `|| [ -n "$_rg_l" ]` (reaches `rec_st`) · none, `FLOOR_ASSERTIONS` is a minimum (`tools/run-gates/run-gates.gov.test.sh@c9500821b:246`) and `TOOL-dWitnessedBar-82` restates it

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. Units 68 to 73 are
  themselves derived and carry no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — What closes the three-reader gap of ids 18 and 26?** Options: (a) `read_bar_file` takes unit
  69 S1's rules and the inherited green reads through it, `read_green_file` left whole so the
  canaries still cut and mutate a function holding the strip; (b) unit 69's scope narrowed to
  `read_green_file`, the other two readers named out of scope with an owning unit; (c) one shared
  record reader the three call. (c) moves the strip out of `read_green_file`, so the canary of units
  70, 74 and 76 cuts a function with nothing to mutate and fails on every run; veto 1 discards it.
  (b) leaves the readers on two rules and names an owner no unit of this build is. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the most feature-rich survivor, since it closes both ids with no
  follow-up.
  widens: none · relaxes: none
- **F3 — Which guard entry covers the registry the gov canary's read globs (id 5)?** Options: (a)
  `{prefix}/*/kit.toml`; (b) each kit's `kit.toml` listed; (c) a fixture tool root for the arm's read;
  (d) `{prefix}/`. (a) leaves the reuse key unmoved by an uncommitted sibling descriptor (§4
  Evidence), which fails AC7; veto 1 discards it. (b) leaves a kit added later unguarded, which fails
  AC7's Red-when on that kit; veto 1 discards it. (c) needs a CLI flag unit 6 does not define, a new
  public surface; veto 2 discards it. RESOLVED (agent, 2026-10-25, delegated): (d), rung 3, the one
  survivor.
  widens: none · relaxes: none
- **F4 — What does S10 build, now that unit 6 and unit 69 S2 landed the record's open?** At HEAD the
  open replaces an undecodable byte, an `OSError` reads `DEAD PROBE` and a non-file reads `NONE`
  (§4 Evidence), so nothing raises out of the read. Options: (a) S10 and S11 write no code, and AC11
  and AC12 observe the landed open; (b) S10 as rev-4 wrote it: drop `errors="replace"` and read an
  `OSError` or `UnicodeDecodeError` as `NONE` with a stderr line. (b) relabels a read that failed,
  which the state table of `help/verdict-backends.md` documents as `DEAD PROBE`, a change to a
  public surface; veto 2 discards it. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, the one
  survivor, closing ids 27 and 22 with no follow-up.
  widens: none · relaxes: none
- **F5 — How many ask rows does S9 file for four specs in three builds?** Options: (a) one row per
  build, naming each of its specs; (b) one row per spec. Both satisfy AC10's token and S9's
  disposition line. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, by the tie-break: one
  open ask per build leaves fewer open questions, and it keeps rev-4's one row in each `BACKLOG.md`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 68 to 73: 9
  MEDIUM and 11 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-82 and TOOL-dWitnessedBar-84, promoted by the round-1 spec audit of
  units 74 to 78; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-88, promoted by the round-1 spec audit of units 79 to 84; nothing else
  moved.
- rev-4 · 2026-11-19 · §7 · the leg line gains `policy fixtures`, whose manifest guard holds the §4 path
  `tools/gate-legs.json`, per brief 2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief; nothing else
  moved.
- rev-5 · 2026-11-21 · §1 to §10 · S1 · S6 to S11 · S15 · S17 to S20 · AC8 to AC12 · AC16 · AC18 to
  AC20 · re-grounded at `c9500821b` over units 68 to 80 as landed, per
  2026-11-19-prompt-TOOL-dWitnessedBar-78-reground-brief. S1, S10, S11, S17, S19 and S20 find their
  code landed and keep their observations (§8 F4). S6 declares its guard in `registry.toml` and
  renders the manifest. S7 and S8 meet `read_bar_file` and a ten-key inherited green as built, minting
  `bg_age` and `bg_blocks`. S9's population is re-derived to four DEFERRED specs in three builds
  (§8 F5). S15 names unit 75. Files touched drops `verdict_backends.py` and the resolver suite and
  gains the registry, the shell-role rows and the five ledgers; §7 gains their legs; the New arm
  covers AC8 and AC14.

## 10. Reuse audit

Each item extends the seam its finding names. S7 and S8 bring `read_bar_file` to unit 69 S1's loop
(`.githooks/pre-push#read_green_file`) and route the inherited green through it under
`check_bar_base`'s `local` idiom (`.githooks/pre-push#check_bar_base`), and S7's arm reuses
`TOOL-dWitnessedBar-73` S9's derived planting and its `sed` over the cut's `case` labels. S3's probe
calls the canonical `resolve_prefix_token` (`tools/lib/resolve_prefix_token.py`) rather than a second
resolver. S6 adds an entry to the existing guard through the registry row unit 73's `daa7d6534`
edited. S20 reuses the suite's `PYBIN` and `KITDIR`.
`python tools/codebase-map/reuse_lookup.py "read a tab separated key value record file line by line keeping carriage return"`,
re-run at `c9500821b` on 2026-11-21, ranked `read_text`, `key`, `read` and `read_bytes` first, none
reachable from the hook, so no existing seam fits beyond those named above.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of units 68 to 73 find" --terms "read_bar_file inherited green gov canary guard kit.toml encoding newline BINMODE GIT_CONFIG_COUNT PYBIN ask row"`
