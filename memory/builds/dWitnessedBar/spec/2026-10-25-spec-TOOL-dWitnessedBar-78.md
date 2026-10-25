# TOOL-dWitnessedBar-78 — the round-1 audit of units 68 to 73, its 20 minors batched: one read rule for every green record, derived and wider guards, an honest record open, and records of what each break printed

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 42 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 |
| [2026-10-25-build-TOOL-dWitnessedBar-78-round8-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-78-round8-fix-return.md) | research | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-78-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-78-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-78-round8-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-78-round8-fix-brief.md) | research | — |
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
units' slot and variants.

## 2. Scope (IN)

- **S1** — id 1. When the CR-reach canary fails, unit 66 S2's `rec_sha` compare and unit 67 S2's
  `rec_fp` compare still run, and each prints its own failure line naming its variable. Neither is
  counted in `a`. Unit 70's acceptance ledger beside AC3, and unit 72's beside AC3, quote both lines
  the strip-less break printed: `TOOL-dWitnessedBar-75`'s `for count 0` line and the compare's own
  line naming `rec_sha` or `rec_fp`. Observed by AC1 and AC2.
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
- **S6** — id 5. The `run-gates gov canary` row's `guard` in `tools/gate-legs.json` gains `{prefix}/`.
  Unit 68's arm runs `read --backend local-hook`, whose `read_backends(tool_root)` reads every
  `tools/*/kit.toml` and whose `check_backend` refuses before any read (unit 6 S1, S2), so an edit to
  any kit's descriptor selects the leg and moves its reuse key. Observed by AC7.
- **S7** — id 18. `read_bar_file` in `.githooks/pre-push` reads with the rules unit 69 S1 gives
  `read_green_file`: one `while IFS= read -r _rb_l || [ -n "$_rb_l" ]` loop over the file, a line with
  no TAB skipped, the key before the first TAB and the value after it, one trailing CR stripped from
  the value, and the last line of a repeated key winning. `_rb_l`, `_rb_k` and `_rb_v` are `local`.
  Its callers `check_bar_record`, `check_bar_base` and `check_cover_record` read it as they do today.
  The AC12 arm plants, in a third record, each key derived from `read_bar_file`'s `case` labels as
  `<key><TAB>old<LF>` then `<key><TAB>new<CR><LF>`, and asserts each derived `bg_*` variable reads
  `new`, as `TOOL-dWitnessedBar-73` S9 does for `read_green_file`. Observed by AC8.
- **S8** — id 26. The inherited-green block reads its record through `read_bar_file`. `read_bar_file`
  also reads `max_age`, `reused` and `reused_cache` into `bg_age`, `bg_reused` and `bg_reused_cache`,
  and `check_bar_base`'s `local` list names those three. A function `read_inherited_green <path>`
  declares every `bg_*` variable `local`, as `check_bar_base` does (`.githooks/pre-push:1584`), calls
  `read_bar_file`, and sets the nine `ig_*` variables from it, in place of the block's nine
  `ig_x=$(awk ...)` reads. S7's derived key list then covers `base` and `max_age`. Observed by AC9.
- **S9** — id 19. S6's and unit 73 S6's guard entries reach other builds' carried specs only through
  an ask row. This unit files one in `memory/builds/dSafePassage/BACKLOG.md` for
  `TOOL-dSafePassage-11` and one in `memory/builds/dOrderedCharter/BACKLOG.md` for
  `PLAY-dOrderedCharter-17`. Each names the token `run-gates gov canary <- .githooks/pre-push` the
  spec's §7 owes once it leaves DEFERRED, with a `SEV` disposition line. Unit 73's acceptance ledger
  beside AC6 names both specs and how they were found. Observed by AC10.
- **S10** — id 27. `read_local_verdict` in `tools/run-gates/verdict_backends.py` reads `NONE` when
  the record's open or decode raises `OSError` or `UnicodeDecodeError`. It writes one stderr line
  naming the record's path and the exception's class, and no traceback. Observed by AC11.
- **S11** — id 22. That open is spelled `open(path, encoding='utf-8', newline='')`, so the encoding
  posture scanner finds no unencoded text read in the module. Observed by AC12.
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
  and names the `rec_fp` value as minted by `TOOL-dWitnessedBar-77`. Observed by AC16.
- **S16** — id 8. Unit 72's acceptance ledger beside AC3 states S3's reason as a sentence: since unit
  69 S1 makes one strip serve every key, one strip-less `read_green_file` is the `rec_fp` break.
  Observed by AC17.
- **S17** — id 7. Section `2l` of `tools/lib/resolve-python.test.sh` holds one
  `refs/heads/master` assertion per fixture, `TOOL-dWitnessedBar-73` S1's, whose red is unit 73 AC1's.
  Where units 71 and 73 each wrote one, this unit keeps unit 73's. Unit 71's acceptance ledger beside
  AC3 names unit 73 AC1 as the observation of 71 S3's `refs/heads/master` clause. Observed by AC18.
- **S18** — id 14. Unit 71's acceptance ledger beside AC1 names
  `tools/memory-tree/check-verdict-epoch.test.sh:31-32` as the two-key bash precedent for S1's
  `GIT_CONFIG_COUNT=2` plant, and states that `git grep -n GIT_CONFIG_COUNT -- tools` printed 17
  lines. Observed by AC19.
- **S19** — id 13. Unit 73 §4 Evidence's fifth bullet cites unit 67's Files touched at
  `spec/2026-10-25-spec-TOOL-dWitnessedBar-67.md:224-235` and its "nine" sentence at `:178`, not
  `:220-231` and `:174`. NOT OBSERVED: a correction to spec text, which no built artifact carries and
  no criterion of unit 73 reads. §4 Evidence of this spec records the measurement.
- **S20** — id 23. Unit 68 S1's plant call in `tools/run-gates/run-gates.gov.test.sh` is spelled
  `"$PYBIN" "$ROOT/${PFX}run-gates/verdict_backends.py" --fixture --plant clean`, through the suite's
  resolved launcher, and no line of the suite opens a command with a bare `python`. Observed by AC20.

## 3. Non-goals (OUT)

- Re-wording the spec text of units 68 to 73. Each item is closed by what this pass builds or
  observes, and a claim or criterion it answers is answered in that unit's acceptance ledger by name.
- The left-shift gates the report names: the checklist entries, the spec lints for typed guards,
  hand-named gate lists and sibling-spec citations, and the grep for every reader of a changed file.
  No clause of this build names them. S3's derived probe, S7's derived key list and S13's arm are the
  regressions this batch builds.
- The runner's `read_record_keys` (`tools/run-gates/run-gates.sh:2387-2397`), which units 65 and 67
  own. S7 and S8 bring the hook's readers to one rule; the runner's reader stays as those units leave
  it.
- The `§7` of `TOOL-dSafePassage-11` and `PLAY-dOrderedCharter-17`. S9 files the asks; the owning
  builds edit their specs.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-68` — S1's plant call in the AC12 arm, which S20 spells through the suite's launcher, and the `read --backend local-hook` read whose registry S6's guard covers (ids 5 and 23)
- **consumes-from** `TOOL-dWitnessedBar-69` — S1's loop rules, which S7 and S8 bring to `read_bar_file` and the inherited green and S13 holds by an arm, S2's record open, which S10 and S11 amend, and its ledger lines for AC2 and AC3 (ids 6, 12, 18, 21, 22, 26, 27)
- **consumes-from** `TOOL-dWitnessedBar-70` — the canary's failure path, after which S1 keeps the compares running, and its ledger lines for AC2 and AC3 (ids 1 and 2)
- **consumes-from** `TOOL-dWitnessedBar-71` — section `2l`'s fixtures and its ledger lines for AC1 and AC3, which S17 and S18 answer (ids 7 and 14)
- **consumes-from** `TOOL-dWitnessedBar-72` — the `rec_fp` canary and its ledger lines for AC1 and AC3, which S1, S2, S15 and S16 answer (ids 1, 2, 8, 17)
- **consumes-from** `TOOL-dWitnessedBar-73` — S6's guard entry, S7's selection, S9's derived planting and AC7, which S3 to S9 observe, widen or answer (ids 4, 5, 11, 13, 19, 20, 26)
- **consumes-from** `TOOL-dWitnessedBar-74` — its AC2, the per-run observation S2 names for unit 70's New-arm claim (id 2)
- **consumes-from** `TOOL-dWitnessedBar-75` — the slotted failure line and its `for count 0` value, which S1 quotes beside the compares' own lines (id 1)
- **consumes-from** `TOOL-dWitnessedBar-76` — its AC2, the per-run observation S2 names for unit 72's New-arm claim (id 2)
- **consumes-from** `TOOL-dWitnessedBar-77` — the slot's `rec_fp` value, which S15 names as minted there (id 17)
- **hands-off** `TOOL-dWitnessedBar-82` — the third and fourth records, the compares and the New-arm claim, which unit 82's restated floor counts and answers in this unit's ledger (id 2 of the round-1 spec audit of units 74 to 78, item H2)
- **hands-off** `TOOL-dWitnessedBar-84` — S6's guard row, S7's derived planting, AC8 and the guard probes of S3, S4 and AC7, which unit 84 widens by the merge-bar guide, derives through one counted helper and observes through `--legs-for` (ids 9, 12, 13, 16, 22 of the round-1 spec audit of units 74 to 78)
- **hands-off** `TOOL-dWitnessedBar-88` — AC5's manifest lacking the hook entry and the ledger line for AC8, which unit 88 observes at this unit's pass commit and grades once its `.githooks/` guard entry lands (ids 4 and 21 of the round-1 spec audit of units 79 to 84)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. The reader half, S1, S6 to
S8, S10, S11, S13 and S20, writes `.githooks/pre-push`, `tools/run-gates/run-gates.gov.test.sh`,
`tools/run-gates/verdict_backends.py` and `tools/gate-legs.json`. The rest writes
`tools/lib/resolve-python.test.sh`, two other builds' `BACKLOG.md` and acceptance ledgers. So the two
write sets are disjoint. Dispatch is strictly sequential, a shared order included
(`tools/workflows/unattended-build.js:76-80`), so a split would buy no concurrency. One unit holds all
20 findings, as `TOOL-dWitnessedBar-73` §4 held its 23.

### Evidence

- `read_bar_file` (`.githooks/pre-push:1420-1432`) reads with `while IFS=$'\t' read -r k v`, with no
  CR strip and no `|| [ -n ]` guard. `check_bar_record` (`:1567`), `check_bar_base` (`:1588`, `:1596`)
  and `check_cover_record` (`:1992`) call it. `check_bar_base` declares its `bg_*` copies `local` at
  `:1584`.
- The inherited-green block (`.githooks/pre-push:1696-1704`) reads nine keys with
  `ig_x=$(awk -F'\t' '$1==k{print $2}' "$_ig")`, and `tools/run-gates/run-gates.sh:5668-5683` writes
  `gate-inherited-green` with those keys plus `legs`, `run_id` and `stamped`.
- The `run-gates gov canary` guard is `["{prefix}/run-gates/", "{prefix}/gate-legs.json"]`
  (`tools/gate-legs.json:1189-1192`). The runner selects a guarded leg by
  `! git diff --quiet "$BASE" -- "$@"` (`tools/run-gates/run-gates.sh:419`), and builds its reuse key
  from guard slices that compare each path to each entry LITERALLY, a path equal to a slash-less entry
  or starting with the entry and `/` (`:3280-3290`). `:3650-3653` says a too-narrow guard is carried
  forward until its key moves. So a glob entry selects through `git diff` and matches nothing in the
  slice.
- `govkit.py`'s guard classifier puts every entry under the tool root in the `kit-relative` class
  (`tools/govkit/govkit.py:2560-2584`), so `{prefix}/` resolves to `tools/` and classifies once.
  `tools/` is already carried by 12 legs, above `BROAD_LEG_FLOOR = 5`
  (`tools/check-spec-tokens.py:331`), so the spec-tokens join excludes it and S6 owes no carried spec
  a leg.
- `python` walking `tools/gate-legs.json` on 2026-10-25 found `.githooks/pre-push` as an exact guard
  of `measure-legs selftest` alone. After unit 73 S6 it is carried by two legs, below the floor, so
  the join reads it. `TOOL-dSafePassage-11` (Files touched, line 338) and `PLAY-dOrderedCharter-17`
  (line 125) name it, are DEFERRED and dated 2026-10-23, after `SPEC_GUARD_LEGS_CUTOFF="2026-09-22"`
  (`.memory-tree.conf:356`). `LIVE` (`tools/check-spec-tokens.py:299`) excludes DEFERRED.
- `tools/gate-lint/encoding_posture.py` flags a text-mode `open` with no `encoding=` through
  `scan_text_io(tree)` (`:94`), and the `encoding posture (text IO names its encoding)` row has no
  guard.
- `tools/run-gates/run-gates.gov.test.sh` sets `PFX` at `:49`, `ROOT` at `:54` and `PYBIN` at `:88`.
- BINMODE, probed on this node on 2026-10-25 (GNU Awk 5.4.0, bash 5.3.9 `x86_64-pc-cygwin`) over a
  `sha<TAB>` forty `b` `<CR><LF>` line: `BINMODE=3 awk ... print length($2)` printed 40,
  `awk -v BINMODE=3 ...` printed 41, and `x=$(awk -v BINMODE=3 ... END{printf "%s", v})` held 41
  bytes.
- `spec/2026-10-25-spec-TOOL-dWitnessedBar-67.md` lists Files touched at lines 224-235; line 174 is
  the heading `### Why one unit`, and "The rest writes nine other files" is line 178.
- `git grep -n GIT_CONFIG_COUNT -- tools` printed 17 lines at `d7671e04`, among them
  `tools/memory-tree/check-verdict-epoch.test.sh:31-32`, which exports `GIT_CONFIG_COUNT=2` with
  `core.autocrlf` and `commit.gpgsign`.
- `tools/lib/resolve_prefix_token.py` holds the canonical `resolve_prefix_token`, the function the
  runner inlines (`tools/run-gates/run-gates.sh:2740-2751`).

### Inventory

Minted: the hook function `read_inherited_green`; the `read_bar_file` locals `_rb_l`, `_rb_k` and
`_rb_v`; the variables `bg_age`, `bg_reused` and `bg_reused_cache`; S7's third and S13's fourth
record in the AC12 arm; S10's stderr line; and S9's two ask rows, each under the next free id of its
build's family. No constant, plant or flag. Naming cells: none apply.

### Migration

None: no stored data changes. Every record the runner writes holds one TAB-separated key per line,
each once, ending in LF, so S7 and S8 read each to the values the base reads give. S6 widens when one
leg runs and narrows nothing.

### Rollout

Live at landing, at order 42, after every other unit of the build, the last of them
`TOOL-dWitnessedBar-73`, `TOOL-dWitnessedBar-76` and `TOOL-dWitnessedBar-77` at order 41. S1, S2, S5,
S9, S12 and S14 to S18 are answered in other units' ledgers at the close.

### Files touched (estimate)

- `.githooks/pre-push`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/verdict_backends.py`
- `tools/gate-legs.json`
- `tools/lib/resolve-python.test.sh`
- `memory/builds/dSafePassage/BACKLOG.md`
- `memory/builds/dOrderedCharter/BACKLOG.md`

### Alternatives rejected

- **Two batches, reader half and the rest.** §4 "Why one unit".
- **Narrow unit 69's title and goal to `read_green_file`, naming `read_bar_file` and the inherited
  green out of scope (ids 18 and 26, option (b)).** It leaves three readers of one runner format on
  two rules, with no owning unit, and §8 F2 says why it loses.
- **Give the guard `{prefix}/*/kit.toml` (id 5's first option).** It selects through `git diff`, but
  the reuse slice compares literally (§4 Evidence), so the leg's reuse key would not move on a
  sibling descriptor and a stale green could be carried forward.
- **List each kit's `kit.toml` in the guard.** A kit added later is unguarded, the C16 class again.
- **Run the arm's read over a fixture tool root holding only the run-gates descriptor.** Unit 6's
  CLI takes no tool-root argument, so this needs a new flag, a public surface this batch may not add.

## 5. Production-readiness checklist

- security — S7 and S8 put the hook's push decision on one read rule for every green record; each
  still fails closed to a full bar on a record it refuses. S10 turns a malformed record into `NONE`
  rather than a traceback. S9 writes only ask rows outside this build, as the build README allows.
- perf / scale — S8 replaces nine awk processes with one builtin loop on the inherited-green path.
  S6 runs the gov canary on any `tools/` change once GATE_SELFTESTS is set, which
  `SELFTESTS_OWED_PATHS="tools/"` already sets for every such change.
- error / empty / loading states — S10 names the unreadable and undecodable record; S13 states the
  no-TAB, trailing-TAB and unterminated cases.
- observability — S10's stderr line names the path and the exception's class.
- risks — a record line with no TAB was read by `read_bar_file` as a key with an empty value; S7
  skips it, which leaves the same empty value.
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
  that the reuse slice cannot match stands in the guard.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
- **AC8** — When a probe sources the function cut by `awk '/^read_bar_file\(\)/,/^}/' .githooks/pre-push`
  and calls it on S7's third record, each `bg_*` variable derived from the cut's `case` labels reads
  `new`, three bytes, and the derived list holds `base` and `max_age`. Against a scratch hook whose
  `read_bar_file` keeps `while IFS=$'\t' read -r k v`, the arm fails naming a `bg_*` variable.
  Red when: `read_bar_file` keeps a CR or a key's first value, or the derived list is empty and the
  arm passes.
  fixture: a record the probe writes under `%TEMP%/<short-name>`.
- **AC9** — When `awk '/^inh_sha=""; inh_why=""/,/^fi$/' .githooks/pre-push` is piped to
  `grep -c 'awk'`, it prints 0, and piped to `grep -c 'read_inherited_green'`, it prints 1. A probe
  sourcing `read_bar_file` and `read_inherited_green` over a record holding `sha<TAB>` forty `b`
  `<CR><LF>` and `max_age<TAB>7<CR><LF>` gives `ig_sha` 40 bytes and `ig_age` as `7`, and leaves a
  `bg_sha` set before the call unchanged.
  Red when: the inherited green keeps its own awk reads, or its read overwrites the caller's `bg_*`.
- **AC10** — When `grep -n 'run-gates gov canary <- .githooks/pre-push' memory/builds/dSafePassage/BACKLOG.md memory/builds/dOrderedCharter/BACKLOG.md`
  runs on the built tree, it prints one ask row in each, naming `TOOL-dSafePassage-11` and
  `PLAY-dOrderedCharter-17` respectively. Unit 73's ledger line for AC6 names both specs.
  Red when: the wider guard is landed with no ask row for a carried spec it reaches.
- **AC11** — When `python verdict_backends.py read --backend local-hook --sha <sha>` runs in
  `tools/run-gates/` over a fixture whose per-tree record holds a `0xff` byte, and over one whose record path is a
  directory, each prints a line carrying `· NONE ·`, and stderr names the record's path and the
  exception's class and holds no `Traceback`.
  Red when: a malformed or unreadable record raises out of the read.
  fixture: the `clean` plant fixture of `TOOL-dWitnessedBar-56` AC6, under `%TEMP%/<short-name>`.
- **AC12** — When `python -c "import ast, sys; sys.path.insert(0, '../gate-lint'); import encoding_posture as e; print(e.scan_text_io(ast.parse(open(sys.argv[1], encoding='utf-8').read())))" verdict_backends.py`
  runs in `tools/run-gates/` on the built tree, it prints `[]`, and
  `grep -n "encoding='utf-8', newline=''" verdict_backends.py` in the same directory names the
  record's open.
  Red when: the open names `newline=''` and no encoding, which the unguarded encoding leg reds.
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
  `TOOL-dWitnessedBar-77` as where the `rec_fp` value is minted.
  Red when: unit 72's "Minted: nothing" stands unanswered beside a criterion that needs the slot.
  permission: the ledger is written at the close.
- **AC17** — When `grep -n 'one strip serve every key' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-72*acceptance-ledger*`
  runs at the close, it names the AC3 line.
  Red when: unit 72 S3's reason is recorded as the verbless clause the spec carries.
  permission: the ledger is written at the close.
- **AC18** — When `awk '/^# ---- 2l\./{f=1;print;next} /^# ---- /{f=0} f' tools/lib/resolve-python.test.sh`
  is piped to `grep -c 'refs/heads/master'`, the count equals the number of fixtures section `2l`
  builds. Unit 71's ledger line for AC3 names `TOOL-dWitnessedBar-73` AC1.
  Red when: two assertions grade one fixture's branch, so either builder's red is ambiguous.
  figure: the fixture count is DERIVED from section `2l` at observation time.
- **AC19** — When `grep -n 'check-verdict-epoch.test.sh:31' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-71*acceptance-ledger*`
  runs at the close, the AC1 line names it and states 17 lines.
  Red when: unit 71's reuse audit stands with the two-key precedent unnamed.
  figure: 17 is PINNED, measured at `d7671e04` on 2026-10-25.
  permission: the ledger is written at the close.
- **AC20** — When `grep -nE '(^|[;&|(]|then|do)[[:space:]]*python[0-9.]*[[:space:]]' tools/run-gates/run-gates.gov.test.sh`
  runs on the built tree, it prints nothing, and
  `grep -n 'run-gates/verdict_backends.py" --fixture --plant clean' tools/run-gates/run-gates.gov.test.sh`
  names one line that opens with `"$PYBIN"`.
  Red when: the plant runs through a bare `python`, which the resolver leg's idiom ban reds and the
  MS-Store stub cannot run.

## 7. Gates

`run-gates gov canary` · `run-gates canary` · `measure-legs selftest` · `pre-push self-test` · `pre-push bar self-test` · `push-main self-test` · `pre-push run-log line` · `encoding posture (text IO names its encoding)` · `python resolver (behaviour + inline parity + idiom ban)` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `memory hygiene`

`measure-legs selftest` is owed for `.githooks/pre-push`, and it, `run-gates canary` and
`run-gates gov canary` for `tools/gate-legs.json`. `recall floor` and `recall floor arms` are owed for
the two `BACKLOG.md` files under `memory/`. `pre-push bar self-test`, `push-main self-test` and
`pre-push run-log line` are S12's. `encoding posture (text IO names its encoding)` is S11's and has no
guard. `govkit selfcheck` grades S6's guard entry's class. Every leg here whose subject is `kit` or
whose chunk is `selftests` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC8 AC14 · the compares after a failed canary, `read_bar_file`'s every-key record and the line-rule record over both readers, staged red by a strip-less `read_green_file` (reaches the compares' lines), by a `read_bar_file` that keeps `IFS=$'\t' read -r k v` (reaches a `bg_*` variable), by an `IFS=$'\t'` split (reaches `rec_man`) and by a loop with no `|| [ -n "$_rg_l" ]` (reaches `rec_st`) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

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
  (d) `{prefix}/`. (a) leaves the reuse key unmoved by a sibling descriptor (§4 Evidence), which fails
  AC7; veto 1 discards it. (b) leaves a kit added later unguarded, which fails AC7's Red-when on that
  kit; veto 1 discards it. (c) needs a CLI flag unit 6 does not define, a new public surface; veto 2
  discards it. RESOLVED (agent, 2026-10-25, delegated): (d), rung 3, the one survivor.
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

## 10. Reuse audit

Each item extends the seam its finding names. S7 and S8 bring `read_bar_file` to unit 69 S1's loop
and route the inherited green through it under `check_bar_base`'s `local` idiom
(`.githooks/pre-push:1584`), and S7's arm reuses `TOOL-dWitnessedBar-73` S9's derived planting. S3's
probe calls the canonical `resolve_prefix_token` (`tools/lib/resolve_prefix_token.py`) rather than a
second resolver. S6 adds an entry to the existing guard. S11 follows the open
`tools/gate-lint/encoding_posture.py` grades. S20 reuses the suite's `PYBIN`, `ROOT` and `PFX`.
`python tools/codebase-map/reuse_lookup.py "read a tab separated key value record file line by line keeping carriage return"`
ranked `read`, `read_text`, `key`, `keys` and `records`, none reachable from the hook, so no existing
seam fits beyond those named above.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of units 68 to 73 find" --terms "read_bar_file inherited green gov canary guard kit.toml encoding newline BINMODE GIT_CONFIG_COUNT PYBIN ask row"`
