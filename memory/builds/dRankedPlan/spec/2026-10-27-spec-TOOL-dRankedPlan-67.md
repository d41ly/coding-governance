# TOOL-dRankedPlan-67 — the spec audit of units 53 to 62: its 30 medium and low findings, closed in one batch

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 25 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-67-deviation-671.md](../build/2026-10-27-build-TOOL-dRankedPlan-67-deviation-671.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 TOOL-dRankedPlan-48 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-57 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-64 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 TOOL-dRankedPlan-81 |
| [2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md) | spec-audit | TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 53 to 62
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`) confirmed 20
MEDIUM and 10 LOW findings. BUILD-METHOD M4 promotes them all into one unit, and this is that unit.
Each finding is named by its report id and given its own §2 item, and where the report merged ids into
one item, the item it shares is named beside it. Id 12 is the medium face of id 29, whose unit is
`TOOL-dRankedPlan-65`, and id 33 the medium face of id 21, whose unit is `TOOL-dRankedPlan-64`. Each
face item adds the record correction its fix names over the other unit's mechanism, and never repeats
the mechanism.

| Report item | Id | Grade | Face of, or shared with | §2 |
|---|---|---|---|---|
| M1 | 1 | MEDIUM | shared with ids 15 and 24 | S1 |
| M1 | 15 | MEDIUM | shared with ids 1 and 24 | S2 |
| M1 | 24 | MEDIUM | shared with ids 1 and 15 | S3 |
| M2 | 2 | MEDIUM | shared with ids 16 and 25 | S4 |
| M2 | 16 | MEDIUM | shared with ids 2 and 25 | S5 |
| M2 | 25 | MEDIUM | shared with ids 2 and 16 | S6 |
| M3 | 3 | MEDIUM | shared with id 17 | S7 |
| M3 | 17 | MEDIUM | shared with id 3 | S8 |
| M4 | 4 | MEDIUM | none | S9 |
| M5 | 7 | MEDIUM | none | S10 |
| M6 | 8 | MEDIUM | none | S11 |
| M7 | 10 | MEDIUM | none | S12 |
| M8 | 11 | MEDIUM | shared with id 35 | S13 |
| M8 | 35 | MEDIUM | shared with id 11 | S14 |
| M9 | 12 | MEDIUM | face of id 29, `TOOL-dRankedPlan-65` | S15 |
| M10 | 30 | MEDIUM | none | S16 |
| M11 | 33 | MEDIUM | face of id 21, `TOOL-dRankedPlan-64` | S17 |
| M12 | 34 | MEDIUM | none | S18 |
| M13 | 36 | MEDIUM | L2 is its low face | S19 |
| M14 | 37 | MEDIUM | none | S20 |
| L1 | 5 | LOW | none | S21 |
| L2 | 6 | LOW | face of M13 | S22 |
| L3 | 13 | LOW | none | S23 |
| L4 | 14 | LOW | shared with ids 18 and 26 | S24 |
| L4 | 18 | LOW | shared with ids 14 and 26 | S25 |
| L4 | 26 | LOW | shared with ids 14 and 18 | S26 |
| L5 | 19 | LOW | none | S27 |
| L6 | 20 | LOW | none | S28 |
| L7 | 22 | LOW | none | S29 |
| L8 | 23 | LOW | none | S30 |

The minors land on units 50 and 52 to 62, so this unit repairs none in particular and is ordered after
every unit of the build. A correction to a spec whose unit builds earlier reaches that unit's builder
before its pass: each such unit's §3 carries a hands-off edge to this unit, and the item names what
that builder carries. This unit builds the four plants of S13, S14, S16 and S18 in
`tools/loop/ratify.py` and observes every item at its tip.

## 2. Scope (IN)

- **S1** — Id 1, item M1. `TOOL-dRankedPlan-62` AC2 joins each spec's lines before it greps, as `tr
  '\n' ' ' < "$f" | tr -s ' ' | grep -c "<the deferral phrase>"`, so a phrase that wraps after
  `dDeclaredLoop's` still counts. Unit 62 carries the command into its AC2. Observed by AC1.
- **S2** — Id 15, item M1. The joined form prints 1 over each of units 53 to 60, where the
  single-line grep prints 0; the single-line output is unit 62 AC2's pinned red state, and unit 62
  carries it into its AC2. Observed by AC2.
- **S3** — Id 24, item M1. AC2's population holds units 46 to 52 after they carry
  `TOOL-dRankedPlan-62` S6's wrapped form, and units 63 to 67, and each prints 1 joined. Observed by
  AC2.
- **S4** — Id 2, item M2. `TOOL-dRankedPlan-62` AC6's population is units 46 to 62 whose Files
  touched names a `tools/loop/` path, never AC1's list from unit 38. Unit 62 carries this into its AC6.
  Observed by AC4.
- **S5** — Id 16, item M2. `TOOL-dRankedPlan-62` §3 states that units 38 to 45 are outside S6's carry,
  for the reason its S1 gives units 30 to 37: `tools/check-spec-tokens.py`'s guards join owes each of
  their leg lines every non-broad loop leg a Files touched path trips, at their own pass (TEMPLATE-SPEC
  §7). Unit 62 carries the sentence into its §3. Observed by AC5.
- **S6** — Id 25, item M2. The red state of AC6 is pinned at c22908a6: `grep -c 'loop breakpoints
  fixtures'` printed 0 for units 46 to 52 and at least 1 for units 53 to 60 and 62. Over the narrowed
  population, units 46 to 52 are red until they carry S6 and the rest are green. Unit 62 carries the
  pinned state into its AC6. Observed by AC6.
- **S7** — Id 3, item M3. `TOOL-dRankedPlan-62` AC24 greps the bare range `256-263`, which wraps
  nowhere. Unit 62 carries this into its AC24. Observed by AC7.
- **S8** — Id 17, item M3. The bare range printed 1 for each of units 46 and 47 at c22908a6, the pinned
  red state; once units 46 and 47 carry `TOOL-dRankedPlan-62` S22 it prints 0. Unit 62 carries the
  pinned state into its AC24. Observed by AC8.
- **S9** — Id 4, item M4. `TOOL-dRankedPlan-62` AC19 observes the carried text of unit 52's AC10, not
  a sed it types itself: the AC10 bullet of unit 52's spec names the `gen:build-order` region. Unit 62
  carries this into its AC19. Observed by AC9.
- **S10** — Id 7, item M5. `TOOL-dRankedPlan-62`'s `New arm:` line gains three staged breaks: a
  direct-script arm with no duration skip, which reddens its AC10; a wrapper body read from
  `parse_shell_defs` without `spans`, which reddens its AC13; and a `SHELL_BODY_WORDS` test with no
  last-segment or `${name}` normalization, which reddens its AC14. Unit 62 carries this into its §7.
  Observed by AC10.
- **S11** — Id 8, item M6. `TOOL-dRankedPlan-53` gains the plant `caller-heredoc-shell-unquoted-split`,
  which feeds `bash <<EOF` the body line `"$py" "$d/ratify.py" "$slug"; echo --exit`. The line rule
  admits it, because the line holds a mode flag, and the shell reader refuses its first command, so
  it is refused with exit 1. Unit 53's `New arm:` line covers its criterion for it under the staged
  break it names. Unit 53 carries the plant, a criterion and the arm line into its pass. Observed by
  AC11.
- **S12** — Id 10, item M7. `TOOL-dRankedPlan-54` §4's router table replaces its `"$py"` column with
  two: a literal `python`, `python3` or `py`, read by `read_python_callers`, and a `$` variable outside
  `SHELL_BODY_WORDS`, such as `"$tool"`, read by both readers as `TOOL-dRankedPlan-62` S15 states. An
  expanded body fed to such a variable gets `TOOL-dRankedPlan-53` S1's readers and
  `TOOL-dRankedPlan-52` S13's textual rules together. Its `heredoc-kinds-routed` case gains a
  `"$tool"` spelling whose body reaches both readers. Unit 54 carries this into its pass. Observed by
  AC12.
- **S13** — Id 11, item M8. `TOOL-dRankedPlan-58` S1 states that every call site of
  `resolve_ratify_word` passes the enclosing file's bindings of `TOOL-dRankedPlan-49` S1, the line
  rule over an expanded Python-fed body included. Unit 58 carries the sentence into its pass. The
  plant `caller-heredoc-py-bound` plants `r="$d/ratify.py"` and then `python3 - <<EOF` with the body
  line `"$r" "$slug"`, unit 58's §4 row 4, refused with exit 1. Observed by AC13.
- **S14** — Id 35, item M8. `TOOL-dRankedPlan-55` §3's first bullet gains: the line rule over an
  expanded Python-fed body resolves a `$name` against the enclosing file's bindings, through
  `TOOL-dRankedPlan-58`'s test, and only the body's own Python names are not bindings. Unit 55
  carries it into its pass. The carrier half is `TOOL-dRankedPlan-65` S1, which reads an unquoted
  carrier with `TOOL-dRankedPlan-55`'s bindings. The plant `caller-shell-c-dq-bound` plants
  `r="$d/ratify.py"` and then `bash -c "\"$py\" \"$r\" \"$slug\""`, refused with exit 1. Observed by
  AC14.
- **S15** — Id 12, item M9 (face of id 29, `TOOL-dRankedPlan-65`). `TOOL-dRankedPlan-56` §4 "The
  reading after this unit" rows 3 and 4 name their Reader as the shell reader and the line rule, after
  unit 65's unquoting. Unit 56 carries the two rows into its pass. Observed by AC15.
- **S16** — Id 30, item M10. `TOOL-dRankedPlan-56` S1's `-c` carrier follows any option word that
  begins with a single `-` and holds `c` among its letters, as bash reads an option cluster, so `-ec`,
  `-lc` and `-xc` select it too. Unit 56 carries the sentence into its S1. The plant `caller-shell-ec`
  plants `bash -ec '"$py" "$d/ratify.py" "$slug"'`, refused with exit 1. Observed by AC16.
- **S17** — Id 33, item M11 (face of id 21, `TOOL-dRankedPlan-64`). `TOOL-dRankedPlan-60` §3 and its §4
  table name destructuring, `const { s } = …` and `const [s] = …`, as unread, the ceiling, and name
  `TOOL-dRankedPlan-64` for a declaration list. Unit 60 carries this into its pass. Observed by AC17.
- **S18** — Id 34, item M12. `TOOL-dRankedPlan-52` S7's piece rule extends to a word a backtick span
  interrupts: the text before the opening backtick op and after the closing one are `piece` tokens,
  rebuilt with `$()` standing for the span. `TOOL-dRankedPlan-57` S1 says each command substitution,
  a `$(…)` or a backtick span, stands for its nested span's words. Units 52 and 57 carry the two
  sentences. The plant `caller-shell-bound-resolver-backtick` plants ``if g=`resolve_kit_gate loop
  ratify.py`; then "$py" "$g" "$slug"; fi``, refused with exit 1. Observed by AC18.
- **S19** — Id 36, item M13. `TOOL-dRankedPlan-61` AC1's selector matches S1's wording, a Kind cell
  that begins `function` or `functions`: its second awk tests `$3 ~ /^ *functions?([ ,]|$)/`. Unit 61
  carries the regex into its AC1. Observed by AC19.
- **S20** — Id 37, item M14. `TOOL-dRankedPlan-62` S12's `close` index skips a `case` … `esac` span:
  between a `case` word and its `esac` word at the body's depth, parentheses are not counted. A body
  with no closing op makes `parse_shell_defs(src, spans=True)` raise `SyntaxError` naming the
  definition's line, which the caller check turns into its exit 2. `spans=False` is unchanged. Unit 50
  carries the rule with the keyword it builds, and unit 62 carries the sentence into its S12.
  Observed by AC20.
- **S21** — Id 5, item L1. `TOOL-dRankedPlan-62` AC3 carries a positive control in the same command:
  the selector over unit 58's spec prints 58, and over unit 52's prints nothing. Its staged break is a
  selector replaced by `grep -l py.function`, which selects unit 52. Unit 62 carries this into its
  AC3. Observed by AC21.
- **S22** — Id 6, item L2 (face of M13). `TOOL-dRankedPlan-61` AC1 is labelled a derivation, its list
  PINNED, and its Red when names S19's red case, a scratch spec copy whose Kind cell reads `function
  in …`. AC2 carries unit 61's acceptance. Unit 61 carries this into its AC1. Observed by AC22.
- **S23** — Id 13, item L3. The record corrections `TOOL-dRankedPlan-62` S12, S15, S16 and S23 carry
  each get a grep, AC23 below. Unit 62's §5 risks line names AC23 of this unit beside its own greps,
  and unit 62 carries that line. Observed by AC23.
- **S24** — Id 14, item L4. `TOOL-dRankedPlan-62` §4 Evidence re-pins its M1, M3 bullet: at base
  `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` prints `legs-for: REFUSING — no
  path given is tracked at HEAD` and exits 2, because `tools/loop/` is untracked until
  `TOOL-dRankedPlan-9` lands it. Unit 62 carries this into its §4. Observed by AC24.
- **S25** — Id 18, item L4. The §7 deferral of units 53 to 60 and 62 to 67 names a derivation that is
  answerable once `tools/loop/ratify.py` is tracked at HEAD. Each of those units passes at order 22 or
  later, after `TOOL-dRankedPlan-9` at order 3, so no §7 changes; unit 62's §4 states this beside S24.
  Observed by AC25.
- **S26** — Id 26, item L4. `TOOL-dRankedPlan-62` S4's and S18's scratch clones, and its AC4 and AC20
  fixtures, are taken at a revision where `tools/loop/ratify.py` is tracked at HEAD, and no other path
  stands in as a baseline: `--legs-for tools/lexicon/lexicon.py` prints non-broad legs. Unit 62
  carries this into S4, S18, AC4 and AC20. Observed by AC26.
- **S27** — Id 19, item L5. `TOOL-dRankedPlan-62` AC4 and AC20 spell the clone location in bash form,
  `"$TEMP"/drp-legs`, short because a long path makes `git clone` fail on Windows, and never in
  cmd.exe's percent form, which Git Bash does not expand. Unit 62 carries this into AC4 and AC20.
  Observed by AC27.
- **S28** — Id 20, item L6. Units 53, 54, 55, 56, 58 and 59 cite a sibling spec in §4 Evidence by its
  S-item or heading, never by a parenthesized line range, as `TOOL-dRankedPlan-62` S22 prescribes for
  units 46 and 47. Each carries this into its pass. Observed by AC28.
- **S29** — Id 22, item L7. `TOOL-dRankedPlan-61` AC2 checks `codebase-map coverage + freshness` and
  the Files touched line only, and cites the guards join (`derive_tripped_legs`,
  `tools/check-spec-tokens.py:621`) for `recall floor` and `recall floor arms`. It reads §7 through
  `extract_gates` (`tools/check-spec-tokens.py:519`) and Files touched through
  `design_lib.read_spec_writes` (`tools/memory-tree/design_lib.py:528`), and its §10 names both. Unit
  61 carries this into its pass. Observed by AC29.
- **S30** — Id 23, item L8. `TOOL-dRankedPlan-62` AC1's population is derived from
  `design_lib.read_spec_writes(text)`: a spec is selected when a returned word starts with
  `tools/loop/`, through the command below §6, and unit 62's §10 names the reader. Unit 62 carries
  this into its AC1 and §10. Observed by AC30.

## 3. Non-goals (OUT)

- Any HIGH of the same audit: units 63 to 66.
- Rewriting a spec whose unit built earlier. Every correction names the sentence it supersedes, and
  that unit's builder carries it in its own pass.
- Carrying `TOOL-dRankedPlan-62` S6's wording into units 38 to 45 (S5). The guards join owes their leg
  lines at their own pass, so the deferral sentence there is a pointer the join already outranks.
- Two batch units. The carried items write nothing in this unit's pass, so the only write set here is
  `tools/loop/ratify.py`, and there is no second set to run beside it.
- A spec-token check or a checklist entry for any of the audit's left-shift gates: each is a gate over
  the spec corpus or a bug-class record, a separate mechanism the close's left-shift step owns.

### Edges

- **consumes-from** `TOOL-dRankedPlan-46` — §4 Evidence, whose line citation AC8 observes carried
- **consumes-from** `TOOL-dRankedPlan-47` — §4, whose superseded sentence and citation AC8 and AC23 observe carried
- **consumes-from** `TOOL-dRankedPlan-49` — S1, its bindings at every site, and its Alternatives rejected, which S13 relies on and AC23 observes
- **consumes-from** `TOOL-dRankedPlan-50` — the `spans` keyword it builds, which S20 corrects and AC20 probes
- **consumes-from** `TOOL-dRankedPlan-51` — §4 and §10, which AC23 observes carried
- **consumes-from** `TOOL-dRankedPlan-52` — S7's piece rule and AC10, which S18 extends and S9 observes
- **consumes-from** `TOOL-dRankedPlan-53` — S1's arm, its plants and its `New arm:` line, which S11 completes and S28 re-cites
- **consumes-from** `TOOL-dRankedPlan-54` — the router table and `heredoc-kinds-routed`, which S12 corrects and S28 re-cites
- **consumes-from** `TOOL-dRankedPlan-55` — §3 and §4 Evidence, which S14 amends and S28 re-cites
- **consumes-from** `TOOL-dRankedPlan-56` — S1, its §4 table and §4 Evidence, which S15 and S16 correct and S28 re-cites
- **consumes-from** `TOOL-dRankedPlan-57` — S1's substitution value, which S18 extends to a backtick span
- **consumes-from** `TOOL-dRankedPlan-58` — `resolve_ratify_word` and S1, over which S13 plants the Python-fed body and S28 re-cites
- **consumes-from** `TOOL-dRankedPlan-59` — §4 Evidence, which S28 re-cites
- **consumes-from** `TOOL-dRankedPlan-60` — §3 and the §4 table, which S17 amends
- **consumes-from** `TOOL-dRankedPlan-61` — AC1, AC2 and §10, which S19, S22 and S29 correct
- **consumes-from** `TOOL-dRankedPlan-62` — §3, §4, §5, §7, S4, S12, S18 and AC1 to AC4, AC6, AC19, AC20 and AC24, which S1, S4 to S7, S9, S10, S20, S21, S23, S24 to S27 and S30 correct
- **consumes-from** `TOOL-dRankedPlan-65` — S1's unquoted carrier reading, over which S14 plants a bound path and S15 names the reader
- **hands-off** `TOOL-dRankedPlan-77` — S2, S3, S12, AC2, AC6, AC25, §4 and the population command, which that unit's items for findings 5, 14, 20, 27, 6, 26, 7 and 15 correct; carry S1 to S4, S8, S13, S14 and S16 of that unit into this unit's pass (spec audit of units 63 to 67)

## 4. Design

### Evidence

- M1: at c22908a6 the single-line grep of `TOOL-dRankedPlan-62` AC2 printed 0 for each of units 53 to
  60, and the joined form printed 1 for each of units 46 to 60 and 62 to 66. The outputs are PINNED.
- M2: `grep -c 'loop breakpoints fixtures'` printed 0 for units 38 to 41 and 43 to 52 and at least 1
  for units 53 to 60 and 62, at c22908a6. The outputs are PINNED.
- M3: `grep -c '256-263'` printed 1 for each of units 46 and 47, and `grep -c 'lines 256-263'` printed
  0 for unit 46. M4: `grep -c 'gen:build-order'` over unit 52's spec printed 0. The outputs are PINNED.
- M6: `RATIFY_MODE_FLAGS` holds `--exit` (`TOOL-dRankedPlan-32` S4), and `TOOL-dRankedPlan-41` S3 ends
  a command at a `;` op, so a mode flag after `;` belongs to the next command.
- M14: `TOOL-dRankedPlan-62` §4 Evidence's M10 bullet shows `parse_shell_defs` returns `(name, line)`
  pairs at base, so `spans` is new code and its close rule is unbuilt.
- L4: `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`, run by the audit at
  c22908a6, printed the refusal and exited 2, and `git ls-files tools/loop` printed nothing.
- L6: `grep -c '(its lines'` printed 1, 1, 2, 2, 3 and 2 over units 53, 54, 55, 56, 58 and 59. The
  outputs are PINNED.
- L7, L8: `extract_gates` is `tools/check-spec-tokens.py:519`, `derive_tripped_legs` is :621, and
  `read_spec_writes` is `tools/memory-tree/design_lib.py:528`; it returns every backticked word under
  `### Files touched`, or None.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-heredoc-py-bound`, `caller-shell-c-dq-bound`, `caller-shell-ec`, `caller-shell-bound-resolver-backtick` | `ratify.py` fixture plants | none |
| `caller-heredoc-shell-unquoted-split` | `ratify.py` fixture plant, carried by `TOOL-dRankedPlan-53` | none |

No item mints a function.

### Rollout

This unit lands last, at order 25. Its carried items reach their builders through those units'
hands-off edges, so each lands in its own unit's pass and is observed here.

### Files touched (estimate)

- `tools/loop/ratify.py`: the plants of S13, S14, S16 and S18

### Alternatives rejected

- **Widen `TOOL-dRankedPlan-62` S6's carry to units 38 to 45 (S4 to S6).** The audit offers it. It
  writes a second copy of a leg obligation the guards join already derives for those specs at their
  pass, so the deferral sentence would be one fact twice, and it adds seven edges for no new check.
- **Drop AC10, AC13 and AC14 from unit 62's `covers` (S10).** The plants stay unproven then; a staged
  break per criterion is a line each.
- **Apply the line rule alone to an unquoted carrier, unescaping by hand (S14).** `TOOL-dRankedPlan-65`
  reads the unquoted text with the shell reader and the bindings, so the carrier plant here needs no
  second rule.

## 5. Production-readiness checklist

- security — S11, S13, S14, S16, S18 and S20 observe or close reading gaps in a deny-by-default ban.
- perf / scale — four fixture plants; no reader moves in this unit's pass.
- error / empty / loading states — S20 states the exit 2 for a wrapper body that never closes.
- observability — each plant prints its answer.
- risks — every carried item depends on its unit's builder carrying it; the greps of §6 observe it.
- testing — the plants of S11, S13, S14, S16 and S18, the probe of S20, the fixture of S19 and the
  greps of the record corrections.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `grep -cF "tr '\n' ' '"` runs over unit 62's spec at this unit's tip, it prints at
  least 1.
  Red when: unit 62 AC2 still greps one line at a time.
  figure: PINNED 0 at c22908a6.
- **AC2** — When `tr '\n' ' ' < "$f" | tr -s ' ' | grep -c "is owed once dDeclaredLoop's loop legs are
  in the manifest"` runs over each spec the population command below prints, it prints 1.
  Red when: the phrase is matched within one line, so units 53 to 60 print 0.
- **AC4** — When `grep -A3 '^- \*\*AC6\*\*'` over unit 62's spec is piped to `grep -c '46 to 62'`, it
  prints at least 1.
  Red when: unit 62 AC6 still runs over units 38 to 45.
  figure: PINNED 0 at c22908a6.
- **AC5** — When `grep -c 'units 38 to 45'` runs over unit 62's spec at this unit's tip, it prints at
  least 1.
  Red when: unit 62 §3 is silent on the units its S6 does not reach.
- **AC6** — When `grep -c 'loop breakpoints fixtures'` runs over each spec the population command
  below prints, it prints at least 1.
  Red when: a unit of 46 to 52 keeps a deferral naming `loop selftest` alone.
- **AC7** — When `grep -c 'lines 256-263'` runs over unit 62's spec at this unit's tip, it prints 0.
  Red when: unit 62 AC24 still greps a range that wraps in unit 46.
  figure: PINNED 1 at c22908a6.
- **AC8** — When `grep -c '256-263'` runs over the specs of units 46 and 47, each prints 0.
  Red when: a line citation into unit 45 survives in either.
  figure: PINNED 1 for each at c22908a6.
- **AC9** — When `grep -c 'gen:build-order'` runs over unit 52's spec at this unit's tip, it prints at
  least 1.
  Red when: unit 52 AC10 still reads the roster row beside the build-order row.
  figure: PINNED 0 at c22908a6.
- **AC10** — When `grep '^New arm:'` runs over unit 62's spec, the line it prints holds `duration`,
  `spans` and `last-segment`.
  Red when: the arm claims AC10, AC13 or AC14 with no break that reddens it.
- **AC11** — When `python ratify.py --fixture --plant caller-heredoc-shell-unquoted-split` runs, the
  check exits 1 naming `.githooks/pre-commit`.
  Red when: an expanded shell-fed body is read by the textual rules alone, whose line rule sees the
  mode flag and admits it.
- **AC12** — When `grep -cF '"$tool"'` runs over unit 54's spec at this unit's tip, it prints at least
  1.
  Red when: unit 54's router still sends a `$`-variable body to the Python reader alone.
  figure: PINNED 0 at c22908a6.
- **AC13** — When the plant `caller-heredoc-py-bound` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: the line rule over a Python-fed body resolves `$r` against an empty binding set.
- **AC14** — When the plant `caller-shell-c-dq-bound` runs, the check exits 1 naming
  `.githooks/pre-commit`, and `grep -c 'line rule'` over unit 55's spec prints at least 1.
  Red when: an unquoted carrier's `$r` is compared unresolved, or unit 55 §3 still excludes the
  Python-fed body from the bindings.
  figure: the grep PINNED 0 at c22908a6.
- **AC15** — When `grep -F '| double-quoted'` runs over unit 56's spec and is piped to `grep -c 'unit
  65'`, it prints at least 1.
  Red when: unit 56's row 3 still answers "caller" by the raw line rule.
  figure: PINNED 0 at c22908a6.
- **AC16** — When the plant `caller-shell-ec` runs, the check exits 1 naming `.githooks/pre-commit`.
  Red when: only a word equal to `-c` selects the carrier.
- **AC17** — When `grep -ci 'destructuring'` runs over unit 60's spec at this unit's tip, it prints at
  least 1.
  Red when: unit 60 §3 still names no declaration shape beyond one name.
  figure: PINNED 0 at c22908a6.
- **AC18** — When the plant `caller-shell-bound-resolver-backtick` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: the piece rule rebuilds a word around `$(` only, so `g=` names nothing.
- **AC19** — When unit 61's two-awk selector runs over a scratch copy of unit 58's spec whose
  Inventory Kind cell is rewritten to `function in` and the kit's path, with no comma, it prints 58.
  Red when: the selector still requires a comma after `function`.
  fixture: the copy under the session scratch directory; the tree holds no such Kind cell today.
- **AC20** — When a probe imports the loop kit's `extract_code.py` and calls `parse_shell_defs('w() (
  case $1 in a) "$@";; esac )\n', spans=True)`, the hit's `close` index names the last `)`, and
  `parse_shell_defs('w() { echo x; \n', spans=True)` raises `SyntaxError` naming line 1.
  Red when: the close lands on the case pattern's `)`, or an unclosed body returns a span.
- **AC21** — When `grep -A4 '^- \*\*AC3\*\*'` over unit 62's spec is piped to `grep -c 58`, it prints
  at least 1.
  Red when: unit 62 AC3 still passes on an empty selection with no positive control.
  figure: PINNED 0 at c22908a6.
- **AC22** — When `grep -A4 '^- \*\*AC1\*\*'` over unit 61's spec is piped to `grep -c derivation`, it
  prints at least 1.
  Red when: unit 61 AC1 still reads as a criterion that is green before the unit is built.
  figure: PINNED 0 at c22908a6.
- **AC23** — When `tr '\n' ' ' < "$f" | grep -c 'That fails closed'` runs over unit 47's spec it
  prints 0, `grep -c 'spans'` over §10 of units 50 and 51 each prints at least 1, `grep -cF '((n >
  0))'` over unit 51 prints at least 1, and `grep -c 'sh_hygiene.py:325'` over unit 49 prints at least
  1.
  Red when: a record correction of `TOOL-dRankedPlan-62` S12, S15, S16 or S23 is never carried.
  figure: PINNED 1, 0, 0, 0 and 0 at c22908a6.
- **AC24** — When `grep -c 'printed only legs marked'` runs over unit 62's spec, it prints 0.
  Red when: the false pinned `--legs-for` output stands.
  figure: PINNED 1 at c22908a6.
- **AC25** — When `python tools/check-spec-tokens.py --legs-for` runs over the loop kit's `ratify.py`
  at this unit's tip, it exits 0.
  Red when: the loop kit's `ratify.py` is untracked at the unit passes that read the deferral.
- **AC26** — When `grep -c 'tracked at HEAD'` runs over unit 62's spec at this unit's tip, it prints
  at least 2.
  Red when: a clone or fixture of unit 62 is taken where the loop kit is untracked.
  figure: PINNED 0 at c22908a6.
- **AC27** — When `grep -c '%TEMP%'` runs over unit 62's spec, it prints 0.
  Red when: a fixture line still spells the cmd.exe form.
  figure: PINNED 2 at c22908a6.
- **AC28** — When `grep -c '(its lines'` runs over each spec of units 53, 54, 55, 56, 58 and 59, each
  prints 0.
  Red when: a sibling citation by line range survives.
  figure: PINNED 1, 1, 2, 2, 3 and 2 at c22908a6.
- **AC29** — When `grep -c 'extract_gates'` and `grep -c 'read_spec_writes'` run over unit 61's spec,
  each prints at least 1.
  Red when: unit 61 AC2 still reads §7 by its ordinal and re-checks the two guarded legs.
  figure: PINNED 0 for each at c22908a6.
- **AC30** — When `grep -c 'read_spec_writes'` runs over unit 62's spec, it prints at least 1.
  Red when: unit 62 AC1 still reads Files touched with a raw awk.
  figure: PINNED 0 at c22908a6.

The population command of AC2 and AC6, run from the repository root, prints the units of 46 to 67
whose Files touched names a path under the loop kit; at this unit's authoring it printed `46 47 48 49 50
51 52 53 54 55 56 57 58 59 60 62 63 64 65 66`, and this unit joins it:

```bash
for n in $(seq 46 67); do for f in memory/builds/dRankedPlan/spec/*-spec-TOOL-dRankedPlan-$n.md; do
  [ -f "$f" ] || continue
  python -B -c 'import sys; sys.path.insert(0, "tools/memory-tree"); import design_lib as d; w = d.read_spec_writes(open(sys.argv[1], encoding="utf-8").read()) or []; sys.exit(0 if any(x.startswith("tools/loop/") for x in w) else 1)' "$f" && printf '%s ' "$n"
done; done
```

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC13 AC14 AC16 AC18 · the four plants of S13, S14, S16 and S18: a line rule and carrier reader resolving against an empty binding set reddens AC13 and AC14, a carrier selected only after a word equal to `-c` reddens AC16, and a piece rule around `$(` only reddens AC18 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 53 to 62: its 20 MEDIUM and
  10 LOW findings, ids 1 2 3 4 5 6 7 8 10 11 12 13 14 15 16 17 18 19 20 22 23 24 25 26 30 33 34 35 36
  37, batched under BUILD-METHOD M4.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-77`, each the reciprocal of that promoted unit's own edge (spec audit of units 63 to 67, `reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`); no other section moves.

## 10. Reuse audit

Each item extends the seam its finding names rather than minting one. S13 and S14 reuse
`TOOL-dRankedPlan-58`'s `resolve_ratify_word` and `TOOL-dRankedPlan-65`'s unquoted reading, S18
extends `TOOL-dRankedPlan-52` S7's piece rule, S20 extends the `spans` keyword `TOOL-dRankedPlan-62`
S12 adds to `parse_shell_defs`, and S29 and S30 point unit 61's and unit 62's criteria at
`extract_gates` and `design_lib.read_spec_writes`, the declared readers of the two sections, instead
of an awk. `python tools/codebase-map/reuse_lookup.py "find command substitutions inside an unquoted
heredoc body"`, run 2026-10-27, ranked name stems only (`build_baseline_findings`, `find_block`), so no
existing seam fits beyond the readers these units already build. The recall query returned units 46,
47 and 52 to 56 and this audit's records, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does the caller check read a bash -c word or a heredoc whose body the outer shell expands" --terms "bash -c carrier double-quoted unquote shlex heredoc expanded command substitution backtick span line rule caller ratify"`
