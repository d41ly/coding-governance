# TOOL-dRankedPlan-62 — the spec audit of units 46 to 52: its 23 medium and low findings, closed in one batch

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 24 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-62-deviation-621.md](../build/2026-10-27-build-TOOL-dRankedPlan-62-deviation-621.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-62-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-62-promoted-fix-return.md) | research | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-62-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-62-1-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-62-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-62-promoted-fix-brief.md) | research | — |
| [2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md) | spec-audit | TOOL-dRankedPlan-59 TOOL-dRankedPlan-55 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-60 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-56 TOOL-dRankedPlan-61 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 46 to 52
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`) confirmed 16
MEDIUM and 7 LOW findings. BUILD-METHOD M4 promotes them all into one unit, and this is that unit. Each
finding is named by its report id and given its own §2 item. Where the report merged ids into one item,
each id still takes its own item, and the item it shares is named beside it. Id 2 is the medium face of
id 22, whose unit is `TOOL-dRankedPlan-61`, and id 8 the medium face of id 29, whose unit is
`TOOL-dRankedPlan-58`. Each face item adds the observation its fix names over the other unit's
mechanism, and never repeats the mechanism.

| Report item | Id | Grade | Face of, or shared with | §2 |
|---|---|---|---|---|
| M1 | 1 | MEDIUM | shared with id 13 | S1 |
| M1 | 13 | MEDIUM | shared with id 1 | S2 |
| M2 | 2 | MEDIUM | face of id 22, `TOOL-dRankedPlan-61` | S3 |
| M3 | 4 | MEDIUM | shared with id 14; L2 is its low face | S4 |
| M3 | 14 | MEDIUM | shared with id 4 | S5 |
| M4 | 24 | MEDIUM | none | S6 |
| M5 | 25 | MEDIUM | none | S7 |
| M6 | 8 | MEDIUM | face of id 29, `TOOL-dRankedPlan-58` | S8 |
| M7 | 12 | MEDIUM | none | S9 |
| M8 | 9 | MEDIUM | none | S10 |
| M9 | 17 | MEDIUM | none | S11 |
| M10 | 20 | MEDIUM | none | S12 |
| M11 | 10 | MEDIUM | none | S13 |
| M12 | 15 | MEDIUM | L3 is its low face | S14 |
| M13 | 16 | MEDIUM | none | S15 |
| M14 | 34 | MEDIUM | none | S16 |
| L1 | 5 | LOW | none | S17 |
| L2 | 26 | LOW | face of M3 | S18 |
| L3 | 33 | LOW | face of M12 | S19 |
| L4 | 11 | LOW | none | S20 |
| L5 | 18 | LOW | none | S21 |
| L6 | 19 | LOW | none | S22 |
| L7 | 21 | LOW | none | S23 |

The minors land on units 46 to 52, so this unit repairs none in particular and is ordered after every
unit of the build. A correction to a spec whose unit builds earlier reaches that unit's builder before
its pass: each such unit's §3 carries a hands-off edge to this unit naming the items to carry into its
own pass. This unit builds the rest in `tools/loop/ratify.py` and observes every item at its tip.

## 2. Scope (IN)

- **S1** — Id 1, item M1 (shared with id 13). `TOOL-dRankedPlan-52` S3's and S4's population is the
  specs of units 38 and later whose `### Files touched (estimate)` names a path under `tools/loop/`.
  Units 30 to 37 are outside it: their specs predate `TOOL-dRankedPlan-45` S17's deferral sentence, and
  `tools/check-spec-tokens.py`'s guards join already owes their leg lines every non-broad leg a Files
  touched path trips, at their own pass, once a loop leg is in the manifest (TEMPLATE-SPEC §7). This
  supersedes unit 52 S3's and S4's "units 30 to 52". Unit 52 carries this into its pass. Observed by
  AC1.
- **S2** — Id 13, item M1 (shared with id 1). While `tools/gate-legs.json` names no `loop selftest`,
  each spec S1 selects holds the deferral sentence once, which supersedes unit 52 AC4's population.
  Observed by AC2.
- **S3** — Id 2, item M2 (face of id 22, `TOOL-dRankedPlan-61`). Unit 61 S2's Inventory selector, run
  over unit 52's spec, selects nothing, though that spec names `py.function` in prose. Observed by AC3.
- **S4** — Id 4, item M3 (shared with id 14). `TOOL-dRankedPlan-52` AC3 cannot be observed against
  today's tree: `tools/gate-legs.json` names no `loop selftest`, and no leg's guard holds
  `{prefix}/loop/`. Its trigger is the manifest gaining such a guard. Until then it is observed on a
  fixture: a scratch clone whose `tools/gate-legs.json` gives `loop selftest` the guard
  `{prefix}/loop/`, over which `tools/check-spec-tokens.py` reports `loop selftest <-
  tools/loop/ratify.py` for a subject spec whose leg line omits the leg, and nothing once the leg line
  names it. Unit 52 carries the sentence into its AC3. Observed by AC4.
- **S5** — Id 14, item M3 (shared with id 4). `TOOL-dRankedPlan-52` AC5 reads: once `tools/gate-legs.json`
  names `loop selftest`, at least one leg's guard holds `{prefix}/loop/`, and that count is at most
  `BROAD_LEG_FLOOR`, 5 (`tools/check-spec-tokens.py:362`). Before then it is not observed, by the same
  trigger as S4. Unit 52 carries this into its AC5. Observed by AC5.
- **S6** — Id 24, item M4. The §7 deferral of units 46 to 52 reads: "`loop selftest`, `loop breakpoints
  fixtures` and every other leg whose guard trips `tools/loop/`, `build-index selftest` among them once
  `TOOL-dRankedPlan-45` S18 lands, is owed once dDeclaredLoop's loop legs are in the manifest, as
  `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them". Units 53 to 62 are
  written in that form. Unit 52 S3 and AC3 compare a selected spec's leg line with the non-broad legs
  `--legs-for` prints for its Files touched paths, never with one hard-coded name. Units 46 to 52 each
  carry this into their pass. Observed by AC6.
- **S7** — Id 25, item M5. Order 12 is sequenced at dispatch whatever the build-order render prints.
  `TOOL-dRankedPlan-52` S10 already has units 44 and 5 name `memory/map/generated/symbols.json` in their
  `--dispatch --writes` lists, and `--dispatch`'s condition-1 check refuses the second declaration while
  the first is open. The render's `yes` is an estimate, as `derive_parallel_step`'s docstring states.
  NOT a carried item: the main loop's dispatch is the act. Observed by AC7.
- **S8** — Id 8, item M6 (face of id 29, `TOOL-dRankedPlan-58`). The plant `caller-shell-bound-timeout`
  plants `r="$d/ratify.py"` and then `timeout 60 "$py" "$r" "$slug"`, refused with exit 1 through unit
  58's `resolve_ratify_word`. Observed by AC8.
- **S9** — Id 12, item M7. `TOOL-dRankedPlan-49` S1's collector reads an assignment word as
  `TOOL-dRankedPlan-52` S7 rebuilds it, which `TOOL-dRankedPlan-57` S1 states, so
  `r="$(cd "$(dirname "$0")" && pwd)/ratify.py"` binds `r` to `"$()/ratify.py"`, whose text ends in
  `ratify.py` once quotes are stripped. The plant `caller-shell-bound-dirname` plants that line and then
  `"$py" "$r" "$slug"`, refused with exit 1. Observed by AC9.
- **S10** — Id 9, item M8. The plant `caller-shell-timeout-direct` plants `timeout -k 5s 60
  "$d/ratify.py" "$slug"`, refused with exit 1, which observes `TOOL-dRankedPlan-50` S1's direct-script
  arm and its duration grammar. Observed by AC10.
- **S11** — Id 17, item M9. `TOOL-dRankedPlan-50` §4's row `with_hook_index cp "$s" "$d/ratify.py"`
  answers "caller, fails closed", as unit 50 S1 and `TOOL-dRankedPlan-59` S1 read it. Unit 50 carries
  this into its pass. Observed by AC11.
- **S12** — Id 20, item M10. `parse_shell_defs(src, spans=False)` in the canonical block of
  `tools/lib/extract_code.py` gains the keyword `spans`. With `spans=False` its return is unchanged.
  With `spans=True` each function hit is `(name, line, open, close)`, `open` and `close` being the
  indices, in `scan_shell_tokens(src)`'s default stream, of the `{` or `(` op that opens the body and of
  the op that closes it at the same depth. Every copy of the block carries it byte for byte under
  TOOL-dTotalRecall-13 S3's parity row. `TOOL-dRankedPlan-50` S2 reads a body's words from that stream
  between the two indices, and its §10 and `TOOL-dRankedPlan-51` §10 cite the keyword, not a body the
  function does not return. Unit 50 carries the keyword, the copies and its Files touched and leg line
  for them, as `TOOL-dRankedPlan-48` names them, into its pass, and unit 51 carries its §10 sentence. The
  plant `caller-shell-func-wrapper-nextline` plants `with_hook_index()` with its `{` on the next line,
  `"$@"` in its body, and then `with_hook_index "$py" "$d/ratify.py" "$slug"`, refused. Observed by
  AC12 and AC13.
- **S13** — Id 10, item M11. The plants `caller-heredoc-shell-path`, `/bin/bash <<'EOF'`, and
  `caller-heredoc-shell-brace`, `"${BASH}" -s <<'EOF'`, each feed `TOOL-dRankedPlan-46`'s
  `caller-heredoc-shell` body and are each refused with exit 1, which observes unit 46 S1's last-segment
  and `${name}` normalizations. Observed by AC14.
- **S14** — Id 15, item M12 (L3, id 33, is its low face). One mechanism decides that `"$BASH"` is a
  shell word: `TOOL-dRankedPlan-47` S1's exclusion of `SHELL_BODY_WORDS` from the Python arm. Unit 46
  S2's ordering rule is superseded by it, because a router that tests the classes in either order gives
  the same answer once the classes are disjoint. Unit 46's staged break becomes `SHELL_BODY_WORDS`
  without `$BASH`, which reddens its AC2. Unit 46 carries this into its pass. Observed by AC15.
- **S15** — Id 16, item M13. A heredoc body fed to a `$` variable that is not in `SHELL_BODY_WORDS` is
  read by both `read_python_callers` and `read_shell_callers`, behind `TOOL-dRankedPlan-32` S1's
  prefilter. It is refused when either reads a caller, and exits 2 only when neither can read it,
  because a shell line can parse as Python and pass, and Python source need not tokenize as shell. A
  literal `python`, `python3` or `py` keeps the Python reader alone. This supersedes
  `TOOL-dRankedPlan-47` §4's "That fails closed" sentence and its §5 risks line, and unit 46 AC2's
  Red-when reads "a `"$BASH"`-fed body reaches the Python reader, where its shell line parses as string
  literals and passes". Units 46 and 47 carry the text into their passes. The plant
  `caller-heredoc-var-shell` feeds `"$tool" <<'EOF'` the body `"$py" "$d/ratify.py" "$slug"`, refused.
  Observed by AC16.
- **S16** — Id 34, item M14. Under `TOOL-dRankedPlan-51` S1, the words of an array value `name=(…)` are
  read as a command of their own, so an array that invokes `ratify.py` is refused unless its own words
  hold a mode flag. A mode flag added only at the `"${name[@]}"` call site is not read, the ceiling. The
  words inside `((…))` are arithmetic, and read as a command they never hold an interpreter word, so no
  rule is needed. Unit 51 carries the two rows into its §4 table. The plant `caller-shell-array-exit`,
  `cmd=("$py" "$d/ratify.py" "$slug"); "${cmd[@]}" --exit`, is refused as that ceiling, and
  `caller-shell-arith`, `if ((n > 0)); then :; fi`, is admitted. Observed by AC17 and AC18.
- **S17** — Id 5, item L1. `TOOL-dRankedPlan-52` AC10 reads its row from the build-order region only:
  `sed -n '/<!-- gen:build-order -->/,/<!-- \/gen:build-order -->/p'` over the build README, then
  `grep '^| 12 |'`. Unit 52 carries this into its AC10. Observed by AC19.
- **S18** — Id 26, item L2 (face of M3). An observation of `TOOL-dRankedPlan-52` S5 that can fail: on
  S4's scratch clone, `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` prints `loop
  selftest <- tools/loop/` with no `broad` mark, and on a second clone whose manifest gives that guard
  to six legs it prints them marked `broad`. Observed by AC20.
- **S19** — Id 33, item L3 (face of M12). `TOOL-dRankedPlan-46`'s `New arm:` line lists each staged
  break and the criteria it reddens: a router with no `SHELL_BODY_WORDS` test reddens AC1 and AC2, and
  `SHELL_BODY_WORDS` without `$BASH` reddens AC2. AC3 is green-only. Unit 46 carries this into its pass.
  Observed by AC21.
- **S20** — Id 11, item L4. `TOOL-dRankedPlan-48` §4 pins the probe's whole default stream:
  `[('word','const',1), ('word','a',1), ('op','=',1), ('op','[',1), ('op',',',1), ('op',',',2),
  ('word','slug',2), ('op',']',2), ('op',';',2)]`. Unit 48 carries this into its pass. Observed by AC22.
- **S21** — Id 18, item L5. `TOOL-dRankedPlan-47` §4 Evidence states its bare-form command, `git grep
  -nE '(^|[^A-Za-z0-9_$])(python|python3|py) -( |$).*<<' -- '*.sh' '.githooks/*'`, and records that its
  3 hits, `tools/unattended/gate-guard.test.sh` :417, :427 and :430, are quoted test-input strings
  passed to `run`, not heredocs. Its Alternatives rejected reads "thirty `$`-fed heredocs, against no
  literal-interpreter heredoc". Unit 47 carries this into its pass. Observed by AC23.
- **S22** — Id 19, item L6. `TOOL-dRankedPlan-46` and `TOOL-dRankedPlan-47` §4 Evidence cite unit 45's
  table by its heading, "File kinds and readers", and its two heredoc rows, not by line. Units 46 and
  47 carry this into their passes. Observed by AC24.
- **S23** — Id 21, item L7. `TOOL-dRankedPlan-49` S1 counts `NAME+=value` as an assignment to `NAME`,
  its value compared as written. Its §10 cites `tools/gate-lint/sh_hygiene.py:160-163` and
  `tools/process-monitor/scope.py:38-39` as sibling assignment readers, cited and not imported, and its
  Alternatives rejected records why S2 keeps every assignment where `sh_hygiene.py:325` clears a name on
  re-assignment: a cleared name fails open on a branch the reader cannot order. Unit 49 carries the
  text into its pass. The plant `caller-shell-bound-append`, `r="$d"; r+="/ratify.py"; "$py" "$r"
  "$slug"`, is refused. Observed by AC25 and AC26.

## 3. Non-goals (OUT)

- Any HIGH of the same audit: units 53 to 61.
- Rewriting a spec whose unit built earlier. Every correction here names the sentence it supersedes,
  and that unit's builder carries it out in its own pass.
- Two batch units. The carried items write nothing in this unit's pass, so the only write set here is
  `tools/loop/ratify.py`, and there is no second set to run beside it.
- A spec-token check for any of the audit's left-shift gates: each is a gate over the spec corpus, a
  separate mechanism, and the close's left-shift step owns it.

### Edges

- **consumes-from** `TOOL-dRankedPlan-46` — S1's normalizations, S2, AC2 and its `New arm:` line, which S13 plants, S14 and S19 restate and S15 respells
- **consumes-from** `TOOL-dRankedPlan-47` — S1's exclusion, §4 and §5, which S14 relies on, S15 corrects and S21 and S22 cite
- **consumes-from** `TOOL-dRankedPlan-48` — §4's probe, which S20 pins
- **consumes-from** `TOOL-dRankedPlan-49` — S1, §10 and its Alternatives rejected, which S9 and S23 extend and correct
- **consumes-from** `TOOL-dRankedPlan-50` — S1's direct arm, S2, §4 and §10, which S10 plants, S11 corrects and S12 re-seams
- **consumes-from** `TOOL-dRankedPlan-51` — S1's command model and §4 and §10, over which S16 reads arrays and S12 corrects the citation
- **consumes-from** `TOOL-dRankedPlan-52` — S3 to S5, S7, S10, AC3 to AC5 and AC10, which S1, S2, S4 to S7, S9 and S17 narrow, restate or observe
- **consumes-from** `TOOL-dRankedPlan-58` — `resolve_ratify_word`, over which S8 plants the bound path behind `timeout`
- **consumes-from** `TOOL-dRankedPlan-59` — the restated wrapper arm, which S11's table row reads
- **consumes-from** `TOOL-dRankedPlan-61` — the Inventory selector, which S3 observes over unit 52's spec
- **hands-off** `TOOL-dRankedPlan-67` — §3, §4, §5, §7, S4, S12, S18 and AC1 to AC4, AC6, AC19, AC20 and AC24, which that unit's items for findings 1 to 5, 7, 13 to 19, 23 to 26 and 37 correct; carry S1, S2, S4 to S10, S20, S21, S23 to S27 and S30 of that unit into this unit's pass (spec audit of units 53 to 62)

## 4. Design

### Evidence

- M1, M3: `grep -c '"loop selftest"' tools/gate-legs.json`, run 2026-10-27, printed 0, and no leg's
  guard holds `{prefix}/loop/`. `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`
  printed only legs marked `broad`. The outputs are PINNED.
- M1: the units of this build whose Files touched names a `tools/loop/` path, read 2026-10-27, are 30
  to 41 and 43 to 60, with this unit added at its pass. The list is DERIVED by AC1's command.
- M5: `tools/memory-tree/gen_build_index.py:1730` reads "`yes` says only that the estimates are
  disjoint; `--dispatch` still decides", and `verb_dispatch` in `tools/unattended/unattended.sh` reads
  the open sibling passes' paths for its condition-1 check.
- M10: `parse_shell_defs` (`tools/lexicon/lexicon.py:747-803`) appends `(name, line)` and returns `out,
  [], []`. `parse_shell_defs('w()\n{ "$@"; }\n')`, run 2026-10-27 at base 0689e7fa, printed `([('w',
  1)], [], [])`, and `scan_shell_tokens` over the same text printed the `{` op at line 2.
- M13: `ast.parse('"$py" "$d/ratify.py" "$slug"')`, run 2026-10-27, printed one `Expr` holding the
  `Constant` `'$py$d/ratify.py$slug'`: the shell line is valid Python with no argv list.
- M14: `scan_shell_tokens('cmd=("$py" "$d/ratify.py" "$slug"); "${cmd[@]}" --exit\n')` printed `cmd=`,
  a `(` op, the three words, a `)` op, `"${cmd[@]}"` and `--exit`; `if ((n > 0))` printed two `(` ops,
  `n`, `0` and two `)` ops. The outputs are PINNED.
- L4: `scan_ts_tokens('const a = ["python3",\n  "ratify.py", slug];\n')` printed S20's nine tokens.
- L7: `tools/gate-lint/sh_hygiene.py:160-163` holds `ASSIGNMENT` with `\+?=`, :325 clears a name on
  re-assignment, and `tools/process-monitor/scope.py:38-39` holds `ASSIGNMENT` and
  `ASSIGNMENT_LEADERS`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `spans` | keyword parameter of `parse_shell_defs`, carried by `TOOL-dRankedPlan-50` | none |
| `caller-shell-bound-timeout`, `caller-shell-bound-dirname`, `caller-shell-timeout-direct`, `caller-shell-func-wrapper-nextline`, `caller-heredoc-shell-path`, `caller-heredoc-shell-brace`, `caller-heredoc-var-shell`, `caller-shell-array-exit`, `caller-shell-arith`, `caller-shell-bound-append` | `ratify.py` fixture plants | none |

No item mints a function.

### Rollout

This unit lands last, at order 24. Its carried items reach their builders through those units'
hands-off edges, so each lands in its own unit's pass and is observed here.

### Files touched (estimate)

- `tools/loop/ratify.py`: S8 to S10, S12's plant, S13, S15, S16 and S23's plant

### Alternatives rejected

- **State the `$`-variable body's fail-open as the ceiling (S15).** The audit offers it, but the ban is
  deny-by-default, the charter's security rule, and reading the body twice behind the prefilter costs
  nothing on a tree where no body names `ratify.py`.
- **Drop `TOOL-dRankedPlan-47` S1's exclusion and keep unit 46 S2's order (S14).** The order then
  carries the decision, and a router refactor that reorders the tests fails open with no criterion able
  to say why. The exclusion makes each arm's test total on its own.
- **Restate the four definition forms over the separators stream in `ratify.py` (S12).** It is a second
  recognizer beside the shared one, and the two drift; the keyword mirrors `TOOL-dRankedPlan-48`'s
  `strs` and `TOOL-dRankedPlan-41`'s `seps`.
- **Write the `symbols.json` line into units 5 and 44 now (S7).** That folds a finding, which M4
  refuses; the dispatch check already sequences the two writers.

## 5. Production-readiness checklist

- security — S9, S10, S12, S13, S15, S16 and S23 close or observe reading gaps in a deny-by-default ban.
- perf / scale — S15 reads a prefiltered `$`-fed body twice; none names `ratify.py` at base.
- error / empty / loading states — S15 states the exit 2 for a body neither reader can read.
- observability — each plant prints its answer.
- risks — S1 to S7 and S11 to S23 depend on units 46 to 52 carrying their items; the greps of §6
  observe it.
- testing — the plants of S8 to S10, S12, S13, S15, S16 and S23, the fixtures of S4 and S18, the probe
  of S12 and the greps of the record corrections.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `grep -c "units 38 and later"` runs over unit 52's spec at this unit's tip, it prints
  at least 1, and the population command below prints `38 39 40 41 43 44 45 46 47 48 49 50 51 52 53 54
  55 56 57 58 59 60 62`.
  Red when: unit 52 S3's population still reaches units 30 to 37, which carry no deferral sentence.
  figure: PINNED at 2026-10-27 from the specs as written; a unit added later joins the list.
- **AC2** — When `grep -c '"loop selftest"' tools/gate-legs.json` prints 0, `grep -c "is owed once
  dDeclaredLoop's loop legs are in the manifest"` prints 1 over each spec AC1 lists.
  Red when: a spec under `tools/loop/` carries neither the leg nor the deferral.
- **AC3** — When `TOOL-dRankedPlan-61`'s Inventory selector runs over unit 52's spec alone, it prints
  nothing, and `grep -c 'py.function'` over the same spec prints at least 1.
  Red when: the selector reads prose, so a spec naming the cell in a sentence is selected.
- **AC4** — When `python tools/check-spec-tokens.py` runs in S4's scratch clone, it reports the
  `loop selftest` leg owed for the loop kit's `ratify.py` on unit 46's spec, and nothing for it once
  that leg line names `loop selftest`.
  Red when: the guards join stops owing a non-broad loop leg.
  fixture: a scratch clone under `%TEMP%` whose `tools/gate-legs.json` gives `loop selftest` the guard
  `{prefix}/loop/`. The tree holds none today, so unit 52 AC3 is not observed against it.
- **AC5** — When `tools/gate-legs.json` names `loop selftest`, a probe counting the legs whose `guard`
  holds `{prefix}/loop/` prints a number from 1 to 5.
  Red when: no leg guards the loop kit, or the guard turns broad.
  fixture: the manifest at the trigger S4 names; today the count is 0 and the criterion is not observed.
- **AC6** — When `grep -c "loop breakpoints fixtures"` runs over each spec AC1 lists, it prints at
  least 1.
  Red when: a deferral still names `loop selftest` alone.
- **AC7** — When `grep -E 'dispatch · item [0-9a-f]+ TOOL-dRankedPlan-(44|5) · reason'` runs over
  `memory/builds/dRankedPlan/RUN.md` at this unit's tip, it prints a row for each of the two units, and
  each row names `memory/map/generated/symbols.json`.
  Red when: a step-12 writer of the symbol render was dispatched without declaring it.
- **AC8** — When `python ratify.py --fixture --plant caller-shell-bound-timeout` runs, the check exits
  1 naming the `timeout` line.
  Red when: a bound path behind `timeout` passes.
- **AC9** — When the plant `caller-shell-bound-dirname` runs, the check exits 1 naming the `"$py"
  "$r"` line.
  Red when: a `$(dirname "$0")/ratify.py` binding reads as an empty value.
- **AC10** — When the plant `caller-shell-timeout-direct` runs, the check exits 1 naming the `timeout`
  line.
  Red when: the direct-script arm or the duration grammar is missing.
- **AC11** — When `grep -F 'with_hook_index cp'` runs over unit 50's spec at this unit's tip, the
  table row it prints answers `caller, fails closed`.
  Red when: the table still calls a caller "not a caller".
- **AC12** — When a probe imports the loop kit's `extract_code.py` and calls `parse_shell_defs('w()\n{
  "$@"; }\n', spans=True)`, it returns one hit whose `open` index names the `{` op on line 2, and
  without the keyword it returns `([('w', 1)], [], [])`; `cmp` finds every copy's block equal to the
  canonical one.
  Red when: the keyword changes the default return, or a copy lacks it.
- **AC13** — When the plant `caller-shell-func-wrapper-nextline` runs, the check exits 1 naming the
  `with_hook_index "$py"` line.
  Red when: a wrapper whose body opens on a later line is not found.
- **AC14** — When the plants `caller-heredoc-shell-path` and `caller-heredoc-shell-brace` run, each
  check exits 1 naming `.githooks/pre-commit`.
  Red when: a `/bin/bash` or `${BASH}` command word is not normalized to the shell set.
- **AC15** — When `grep -c "interpreter class before the shell words"` runs over unit 46's spec at this
  unit's tip, it prints 0, and its `New arm:` line names `SHELL_BODY_WORDS` without `$BASH`.
  Red when: the staged break still cannot redden AC2.
- **AC16** — When the plant `caller-heredoc-var-shell` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: a shell body fed to a non-Python `$` tool parses as Python and passes.
- **AC17** — When the plant `caller-shell-array-exit` runs, the check exits 1 naming the `cmd=(` line.
  Red when: an array value's words are not read as a command.
- **AC18** — When the plant `caller-shell-arith` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: arithmetic words are read as an invocation.
- **AC19** — When unit 52 AC10's `sed -n '/<!-- gen:build-order -->/,/<!-- \/gen:build-order -->/p'`
  over the build README is piped to `grep '^| 12 |'`, it prints exactly one row.
  Red when: the roster row for unit 12 is printed beside the build-order row.
- **AC20** — When `python tools/check-spec-tokens.py --legs-for` runs over the loop kit's `ratify.py`
  in S4's clone, it prints `loop selftest <- tools/loop/` unmarked, and in S18's six-leg clone it
  prints the guard's legs marked `broad`.
  Red when: the observation cannot tell a narrow loop guard from a broad one.
  fixture: the two scratch clones under `%TEMP%`; the tree holds neither manifest today.
- **AC21** — When `grep "^New arm:"` runs over unit 46's spec at this unit's tip, the line names both
  staged breaks and the criteria each reddens.
  Red when: the arm line claims a criterion its break leaves green.
- **AC22** — When `grep -cF "('word','const',1), ('word','a',1)"` runs over unit 48's spec, it prints
  at least 1.
  Red when: AC1's equality still points at a stream §4 does not pin.
- **AC23** — When `grep -c "test-input strings"` runs over unit 47's spec, it prints at least 1.
  Red when: the bare-form count is stated without its command and its reading.
- **AC24** — When `grep -c "lines 256-263"` runs over units 46 and 47's specs, each prints 0.
  Red when: a citation still points before the table's heading.
- **AC25** — When the plant `caller-shell-bound-append` runs, the check exits 1 naming the `"$py" "$r"`
  line.
  Red when: a `+=` assignment is not read as a binding.
- **AC26** — When `grep -c "sh_hygiene.py:160-163"` runs over unit 49's spec, it prints at least 1.
  Red when: the reuse audit still misses the sibling assignment readers.

The population command of AC1, run from the repository root:

```bash
for n in $(seq 38 62); do for f in memory/builds/dRankedPlan/spec/*-spec-TOOL-dRankedPlan-$n.md; do
  awk '/^### Files touched/{f=1;next} /^#/{f=0} f' "$f" | grep -q 'tools/loop/' && printf '%s ' "$n"
done; done
```

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands, is owed once dDeclaredLoop's
loop legs are in the manifest, as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`
derives them, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC8 AC9 AC10 AC13 AC14 AC16 AC17 AC18 AC25 · the plants of S8 to S10, S12, S13, S15, S16 and S23, staged by a reader that compares bound words unresolved, keeps a `$`-fed body to one reader and drops an array value's words · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 46 to 52: its 16 MEDIUM and
  7 LOW findings, ids 1 2 4 5 8 9 10 11 12 13 14 15 16 17 18 19 20 21 24 25 26 33 34, batched under
  BUILD-METHOD M4.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-67`, each the reciprocal of that promoted unit's own edge (spec audit of units 53 to 62, `reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`); no other section moves.

## 10. Reuse audit

Each item extends the seam its finding names rather than minting one. S8 and S9 extend
`TOOL-dRankedPlan-58`'s and `TOOL-dRankedPlan-57`'s readings, S12 extends `parse_shell_defs` in the
shared block as `TOOL-dRankedPlan-48` extends `scan_ts_tokens`, S15 reuses the two readers of
`TOOL-dRankedPlan-32`, and S4, S6 and S18 reuse `tools/check-spec-tokens.py`'s guards join and its
`--legs-for` query. `python tools/codebase-map/reuse_lookup.py "resolve a shell variable bound to a
script path where a command invokes it"`, run 2026-10-27, ranked name stems only (`resolve`,
`resolve_kit_dir`, `resolve_caps`), so no existing seam fits beyond the readers these units already
build. The recall query returned units 47 to 52 and dWitnessedBar's resolver scouts, and they agree
with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve bound variables wrappers and inline sources to a script invocation" --terms "assignment binding resolver substitution wrapper timeout here-string bash -c interpreter option caller ratify"`
