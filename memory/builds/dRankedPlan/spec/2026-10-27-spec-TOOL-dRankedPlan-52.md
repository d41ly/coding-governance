# TOOL-dRankedPlan-52 — the spec audit of units 38 to 45: its 25 medium and low findings, closed in one batch

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 22 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-52-deviation-521.md](../build/2026-10-27-build-TOOL-dRankedPlan-52-deviation-521.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md) | spec-audit | TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 38 to 45
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`) confirmed 14
MEDIUM and 11 LOW findings. BUILD-METHOD M4 promotes them all into one unit, and this is that unit.
Each finding is named by its report id and given its own §2 item. Where the report merged ids into one
item, each id still takes its own item, and the item it shares is named beside it. Id 2 is the medium
face of a high that has its own unit, and id 11 the low face of id 24. Each face item adds the
observation its fix names, over the other item's mechanism, and never repeats the mechanism.

| Item | Ids | Grade | Face of | §2 |
|---|---|---|---|---|
| M1 | 2 | MEDIUM | `TOOL-dRankedPlan-51` (H5, id 35) | S1 |
| M2 | 3 | MEDIUM | none | S2 |
| M3 | 4, 14, 27 | MEDIUM | none | S3, S4, S5 |
| M4 | 5 | MEDIUM | none | S6 |
| M5 | 9 | MEDIUM | none | S7 |
| M6 | 12 | MEDIUM | none | S8 |
| M7 | 24 | MEDIUM | none | S9 |
| M8 | 25 | MEDIUM | none | S10 |
| M9 | 26 | MEDIUM | none | S11 |
| M10 | 29 | MEDIUM | none | S12 |
| M11 | 31 | MEDIUM | none | S13 |
| M12 | 32 | MEDIUM | none | S14 |
| L1 | 6 | LOW | none | S15 |
| L2 | 11 | LOW | M7 (id 24) | S16 |
| L3 | 15 | LOW | none | S17 |
| L4 | 16 | LOW | none | S18 |
| L5 | 18 | LOW | none | S19 |
| L6 | 19 | LOW | none | S20 |
| L7 | 20 | LOW | none | S21 |
| L8 | 21 | LOW | none | S22 |
| L9 | 23 | LOW | none | S23 |
| L10 | 28 | LOW | none | S24 |
| L11 | 36 | LOW | none | S25 |

The minors land on units 5, 38 to 41 and 43 to 45, so this unit repairs none in particular and is
ordered after every unit of the build. A correction to a spec whose unit builds earlier must reach that
unit's builder before its pass, so each such unit's §3 carries a hands-off edge to this unit naming the
items to carry into its own pass. This unit builds the rest and observes every item at its tip.

## 2. Scope (IN)

- **S1** — Id 2, item M1 (face of id 35, `TOOL-dRankedPlan-51`). The fixture case `sets-reachable`
  joins `ratify.py --fixture --plant <case>`. It tokenizes `<member> x` and its newline with
  `scan_shell_tokens(seps=True)` for each member of `SHELL_RESERVED_WORDS`, `SHELL_PREFIX_COMMANDS`,
  `SHELL_WRAPPER_COMMANDS` (`TOOL-dRankedPlan-50`) and `SHELL_BODY_WORDS` (`TOOL-dRankedPlan-46`), and
  passes only when each first token is a `word` whose text is the member. Observed by AC1.
- **S2** — Id 3, item M2. The seed of `TOOL-dRankedPlan-45` S31 prints `seed — kit copies: <n>` once per
  fixture run, `<n>` being the memory-tree kit copies that run made. This supersedes unit 45 AC23's
  clause "the seed copies the kit once per fixture run", which had no command. Observed by AC2.
- **S3** — Id 4, item M3 (with ids 14 and 27). Unit 45 AC12 is superseded by this unit's AC3: for each
  spec of units 30 to 52 whose `### Files touched (estimate)` names a path under `tools/loop/`, the §7
  leg line, the line under `## 7. Gates` holding only backticked names and separators, holds
  `` `loop selftest` `` once `tools/gate-legs.json` names that leg. A prose mention does not count.
  Observed by AC3.
- **S4** — Id 14, item M3 (with ids 4 and 27). While `tools/gate-legs.json` does not name `loop
  selftest`, each spec S3 selects carries the deferral sentence "`loop selftest` is owed once
  dDeclaredLoop's loop legs are in the manifest" in its §7, observed by its own grep, apart from S3's.
  Observed by AC4.
- **S5** — Id 27, item M3 (with ids 4 and 14). The gate that holds S3 between audits is
  `tools/check-spec-tokens.py`'s guards join, which owes on the leg line every leg whose guard a Files
  touched path trips, unless the guard is broad (TEMPLATE-SPEC §7). S5 pins that `{prefix}/loop/` is
  carried by at most `BROAD_LEG_FLOOR` legs, 5 (`tools/check-spec-tokens.py:362`), so the join reds a
  `tools/loop/` spec whose leg line omits the leg. Observed by AC5.
- **S6** — Id 5, item M4. `TOOL-dRankedPlan-41` §4 states the effect of its new copy
  `tools/loop/extract_code.py` on the verb-offender count: the corpus counts each copy of a name, and
  the block holds `ext_of`, whose `ext` is not a declared verb. Unit 41's pass measures the count before
  and after the copy and moves `VERB_OFFENDER_PIN` in `.lexicon.conf` by the measured difference in the
  same commit, with a comment naming the copy and TOOL-dTotalRecall-13, re-derived from the walk as
  the conf's own history records each move. Its Files touched gains `.lexicon.conf`, and its §7 leg
  line gains `govkit acceptance matrix` and `straggler-guard arms`, the legs that file's guard trips.
  Unit 41 carries this into its pass. Observed by AC6.
- **S7** — Id 9, item M5. In separators mode, a word that a `$(…)` interrupts with no break on that side
  is emitted as `piece` tokens instead of `word` tokens: the text before the `$(`, and each text after
  a `$)` up to the next break. `read_shell_callers` rebuilds one outer word from the consecutive pieces
  of one nesting level, with `$()` standing for each nested span, and reads it at its first piece's
  position before stripping quotes. A substitution standing alone between breaks adds no outer word,
  as `TOOL-dRankedPlan-41` S3 reads it. The plant `caller-shell-subst-path` plants `"$py" "$(dirname
  "$0")/ratify.py" "$slug"`, refused with exit 1. Observed by AC7.
- **S8** — Id 12, item M6. `SHELL_PREFIX_OPTIONS = {"exec": ("-a",), "env": ("-u", "-C", "-S",
  "--unset", "--chdir", "--split-string"), "time": ("-f", "-o", "--format", "--output")}` in
  `tools/loop/ratify.py`. After a `TOOL-dRankedPlan-40` S1 prefix command, an option word in its row
  skips the next word too, and an `--opt=value` word is one word. `timeout`'s options need no row,
  because `TOOL-dRankedPlan-50` S1 reads a wrapper call by adjacency. The plants `caller-shell-env-u`,
  `env -u PYTHONPATH "$py" "$d/ratify.py" "$slug"`, and `caller-shell-exec-a`, `exec -a ratify "$py"
  "$d/ratify.py" "$slug"`, are each refused. Observed by AC8.
- **S9** — Id 24, item M7. `TOOL-dRankedPlan-41` §4 Files touched under S2 and `TOOL-dRankedPlan-45` §4
  Files touched under S10 name `tools/memory-tree/extract_code.py`, the kit copy TOOL-dTotalRecall-8
  creates. Unit 41 S2's copy set is whatever `git grep -l "^# >>> extract_code" -- '*.py'` lists at the
  pass, not a typed list. Units 41 and 45 carry this into their passes. Observed by AC9.
- **S10** — Id 25, item M8. `TOOL-dRankedPlan-44`, `TOOL-dRankedPlan-41` and `TOOL-dRankedPlan-5` each
  mint a function or a module copy whose symbols the map renders. Each names
  `memory/map/generated/symbols.json`, re-rendered by `gen_map.py --write`, in its Files touched, and
  `codebase-map coverage + freshness`, `recall floor` and `recall floor arms` on its §7 leg line. Each
  carries this into its own pass, and its `--dispatch --writes` list names the file, so units 44 and 5
  at order 12 are sequenced by BUILD-METHOD M6 clause 3. Observed by AC10.
- **S11** — Id 26, item M9. Beside unit 45 AC22, which observes only the tip, AC11 observes S30's
  per-unit rule: over the specs of units 30 to 52 whose §4 Inventory mints a `py.function`, the §7 leg
  line names `codebase-map coverage + freshness` and Files touched names
  `memory/map/generated/symbols.json`. Observed by AC11.
- **S12** — Id 29, item M10. `TOOL-dRankedPlan-45` §4 Files touched gains `help/plan.md`, and its §5
  user docs line names it. The section "Plan's exit without the intake hook" (`TOOL-dRankedPlan-10` S8)
  gains one sentence: a fresh disposition record added in the commit that takes the stale one out of
  the tree is held, and the remedy is to add the fresh record in a commit that keeps the stale one.
  Unit 45 carries this into its pass. Observed by AC12.
- **S13** — Id 31, item M11. In separators mode the heredoc token of `TOOL-dRankedPlan-45` S10 has two
  kinds: `heredoc` for a quoted delimiter, whose body the shell does not expand, and
  `heredoc-expanded` for an unquoted one. A body `TOOL-dRankedPlan-47` S1 routes to Python is read, when
  it is `heredoc-expanded`, by the textual rules only: `TOOL-dRankedPlan-38`'s name rule, and a line
  rule that a line holding a word ending in `ratify.py`, quotes stripped, is a caller unless the line
  holds a mode flag. A `heredoc` body that fails `ast.parse` exits 2 printing `ratify — <path>:<line>
  cannot be parsed: heredoc body`, the line being the body's first file line. The plants
  `caller-heredoc-unquoted`, refused with exit 1, and `caller-heredoc-quoted-broken`, exit 2, join
  `ratify.py --fixture`. Observed by AC13.
- **S14** — Id 32, item M12. Python source handed to an interpreter inline is read in all three
  carriers: a heredoc body, the word after `-c`, and a here-string, which separators mode emits as a
  `herestring` token keeping its quotes. For a command whose command word is in `TOOL-dRankedPlan-47`
  S1's Python class, a single-quoted `-c` word or here-string is read by `read_python_callers` behind
  unit 32 S1's prefilter, and any other quoting by S13's textual rules. The plants `caller-hook-c-argv`,
  `"$py" -c 'import subprocess, sys; subprocess.run([sys.executable, "ratify.py", sys.argv[1]])'
  "$slug"`, and `caller-herestring-argv`, the same source after `<<<`, are each refused. Observed by
  AC14.
- **S15** — Id 6, item L1. `TOOL-dRankedPlan-38` S2 and its Inventory gain the plant
  `caller-hook-comment`, a `.githooks/pre-commit` holding `# read_plan_ratification is asked only at
  the act`, named in unit 38 AC3 and on its `New arm:` line. Unit 38 carries this into its pass.
  Observed by AC15.
- **S16** — Id 11, item L2 (face of id 24). `TOOL-dRankedPlan-41`'s §7 leg line names `build-index
  selftest`, the memory-tree kit's suite, beside the other kits' legs, because the block it changes now
  ships in the memory-tree kit. Unit 41 carries this into its pass. Observed by AC16.
- **S17** — Id 15, item L3. `TOOL-dRankedPlan-39` §4 Evidence reads: `if` 2, at
  `tools/lexicon/adopt-lexicon.sh:423` and `tools/memory-tree/merge-rows.test.sh:423`, and `!` 1, at
  `tools/lexicon/adopt-lexicon.sh:423`. Unit 39 carries this into its pass. Observed by AC17.
- **S18** — Id 16, item L4. `TOOL-dRankedPlan-45` §4 Evidence, M6 bullet, cites
  `tools/memory-tree/.memory-tree.conf.example:20` and `tools/memory-tree/tree_lib.py:416-418`. Unit 45
  carries this into its pass. Observed by AC18.
- **S19** — Id 18, item L5. `TOOL-dRankedPlan-45` AC10 also requires that `until order 14` occur 0
  times in unit 31's spec, and both of its greps run over the spec with its lines joined, `order` and
  `17` matched as `order[[:space:]]+17`. Unit 45 carries this into its pass. Observed by AC19.
- **S20** — Id 19, item L6. `TOOL-dRankedPlan-40` §10 cites `tools/runlog/extract.py:89-90` `WRAPPERS`
  and `INTERPRETERS` and `_derive_program` (:479). Its Alternatives rejected records why `ratify.py`
  keeps its own narrower prefix set: a copy-installed kit imports nothing from a sibling kit, `sudo`
  and `nice` stay out by its §3 non-goal, and `timeout` is read by `TOOL-dRankedPlan-50`'s wrapper
  rule, so the two edits agree. Unit 40 carries this into its pass. Observed by AC20.
- **S21** — Id 20, item L7. `TOOL-dRankedPlan-39` §10 cites `tools/gate-lint/sh_hygiene.py:735` and
  `TEMP_KEYWORDS` at :969. Its Alternatives rejected records why the loop kit keeps its own list:
  `sh_hygiene.py` imports no `extract_code` block, so moving the set into the block would leave the
  gate-lint list standing beside it, and `time` is `TOOL-dRankedPlan-40`'s prefix command. Unit 39
  carries this into its pass. Observed by AC21.
- **S22** — Id 21, item L8. `TOOL-dRankedPlan-45` S21's containment test calls `_is_under(path, top)`
  from the loop kit's `budget.py` (TOOL-dDeclaredLoop-100 S9), which passes both paths through
  `realpath` and `normcase`, in place of its own realpath-only test. Observed by AC22.
- **S23** — Id 23, item L9. The docstring of `scan_shell_tokens` in the canonical block respells its
  kind sentence: `word` or `op` by default, and in separators mode also `piece` (S7), `heredoc` and
  `heredoc-expanded` (S13) and `herestring` (S14), beside the separator ops `TOOL-dRankedPlan-41` S1
  names. This supersedes unit 41 S1's list of emitted tokens. Observed by AC23.
- **S24** — Id 28, item L10. `TOOL-dRankedPlan-43` S3 is not carried out: the correction to the date
  stands only in unit 43 §4 "The date after this unit", and unit 34's spec, which builds at order 5, is
  not edited. Unit 43 carries this into its pass. NOT OBSERVED by a criterion: it removes a record
  edit and changes no behaviour.
- **S25** — Id 36, item L11. A body's reader reports a body line `k` at file line `t + k - 1`, where `t`
  is the heredoc token's line, the body's first file line. A `-c` word or a here-string reports its
  word's line. Unit 45 AC8's "the body's line" is that exact file line. Observed by AC24.

## 3. Non-goals (OUT)

- Any HIGH of the same audit: units 46 to 51.
- Rewriting a landed spec. Every correction here names the sentence it supersedes, and the earlier
  unit's builder carries it out in its own pass.
- Two batch units. The carried items write nothing in this unit's pass, so the only write set here is
  `tools/loop/ratify.py` and the block's copies, and there is no second set to run beside it.
- A template literal in a JavaScript argv array: unread, as `TOOL-dRankedPlan-48` §3 states.

### Edges

- **consumes-from** `TOOL-dRankedPlan-5` — `derive_mapping`'s Files touched and §7, which S10 completes
- **consumes-from** `TOOL-dRankedPlan-38` — S2's plants, AC3 and its arm line, which S15 completes with the comment plant
- **consumes-from** `TOOL-dRankedPlan-39` — `SHELL_RESERVED_WORDS`, §4 Evidence and §10, which S1 probes and S17 and S21 correct
- **consumes-from** `TOOL-dRankedPlan-40` — `SHELL_PREFIX_COMMANDS`, S1's skip and §10, which S1 probes, S8 gives an option table and S20 corrects
- **consumes-from** `TOOL-dRankedPlan-41` — the separators mode, its copies, Files touched and §7, which S6, S7, S9, S10, S16 and S23 extend or correct
- **consumes-from** `TOOL-dRankedPlan-43` — S3's edit to unit 34, which S24 withdraws
- **consumes-from** `TOOL-dRankedPlan-44` — `read_kept_dispositions`' Files touched and §7, which S10 completes
- **consumes-from** `TOOL-dRankedPlan-45` — S10's heredoc token, S21's seed check, S31's seed, AC8, AC10, AC12, AC22, AC23, §4 and §5, which S2, S3, S9, S11 to S13, S18, S19, S22 and S25 correct or extend
- **consumes-from** `TOOL-dRankedPlan-46` — `SHELL_BODY_WORDS`, which S1 probes
- **consumes-from** `TOOL-dRankedPlan-47` — the Python arm of the heredoc routing, over which S13, S14 and S25 add the unparsable-body rule, the inline carriers and the file line
- **consumes-from** `TOOL-dRankedPlan-50` — `SHELL_WRAPPER_COMMANDS` and the wrapper call, which S1 probes and beside which S8 and S20 stand
- **consumes-from** `TOOL-dRankedPlan-51` — the command model over the four ops and the `{`-free reserved set, which S1 observes for the class
- **consumes-from** `TOOL-dRankedPlan-58` — `resolve_ratify_word`, which S13's line rule calls for its `ratify.py` comparison; without it a bound name on a body line is compared unresolved (spec audit of units 46 to 52, id 29)
- **hands-off** `TOOL-dRankedPlan-53` — S13's `heredoc-expanded` kind and its line rule, which that unit applies to a shell-fed body (spec audit of units 46 to 52, id 3)
- **hands-off** `TOOL-dRankedPlan-54` — S13's two heredoc kinds, which that unit names as one set for the router (spec audit of units 46 to 52, id 23)
- **hands-off** `TOOL-dRankedPlan-56` — S14's `herestring` token and `-c` reading and S13's line rule, which that unit extends to the shell class (spec audit of units 46 to 52, id 27)
- **hands-off** `TOOL-dRankedPlan-57` — S7's `piece` tokens and rebuilt word, through which that unit reads a substitution's words in an assignment (spec audit of units 46 to 52, id 28)
- **hands-off** `TOOL-dRankedPlan-61` — S11 and AC11, whose selector that unit replaces with an Inventory-row reading (spec audit of units 46 to 52, id 22)
- **hands-off** `TOOL-dRankedPlan-62` — S3 to S5, S7, S10, AC3 to AC5, AC10 and §7, which that unit's items for findings 1, 4, 5, 13, 14, 24, 25 and 26 narrow, restate or observe; carry S1, S2, S4, S5, S6 and S17 of that unit into this unit's pass (spec audit of units 46 to 52)

## 4. Design

### Evidence

- M2: unit 45 AC23 greps `tools/run-gates/selftest-budgets.txt` for `loop selftest`, a row the parent
  build's leg creates whether or not S31's one-copy seed is built.
- M3: units 38 to 45 each carry the deferral sentence, which `grep -l "loop selftest"` matches, and
  TEMPLATE-SPEC §7 says a line with a prose prefix is not read by `tools/check-spec-tokens.py`.
- M4: `python tools/lexicon/lexicon.py --suggest ext_of --as py.function`, run 2026-10-27, printed
  that `ext` is not in the declared table, and `.lexicon.conf:327` pins `VERB_OFFENDER_PIN="1212"`.
- M5: a probe run 2026-10-27 at base 0689e7fa, `scan_shell_tokens('"$py" "$(dirname "$0")/ratify.py"
  "$slug"\n')`, printed `('word','"$py"',1) ('word','"',1) ('word','dirname',1) ('word','"$0"',1)
  ('word','/ratify.py"',1) ('word','"$slug"',1)`. The idiom is in the tree at `.githooks/pre-commit:111`.
- M8: `tools/codebase-map/test_codebase_map.py:292` lists `symbols.json` among the compared renders,
  and the build README's build-order row 12 reads `TOOL-dRankedPlan-44`, `TOOL-dRankedPlan-5`, `yes`.
- M11: `tools/unattended/gate-guard.test.sh:430` writes `python - <<EOF`, an unquoted delimiter.
- L3, L4, L6, L7: `tools/memory-tree/merge-rows.test.sh:423` holds the second `if`;
  `tools/memory-tree/.memory-tree.conf.example:20` holds the `FAMILIES` line and `_id_alternation` is
  defined at `tools/memory-tree/tree_lib.py:416`; `tools/runlog/extract.py:89` holds `WRAPPERS`;
  `tools/gate-lint/sh_hygiene.py:735` pops a reserved-word tuple.
- L8: TOOL-dDeclaredLoop-100 S9 defines `_is_under` in `tools/loop/budget.py` with `normcase` and
  `realpath`.

### Token kinds in separators mode, after this unit

| Kind | Text | Item |
|---|---|---|
| `word` | a whole word | `TOOL-dRankedPlan-41` S1 |
| `op` | a separator, `$(`, `$)`, a backtick, or `(`, `)`, `{`, `}` | `TOOL-dRankedPlan-41` S1 |
| `piece` | part of a word a `$(…)` interrupts | S7 |
| `heredoc`, `heredoc-expanded` | a body, by its delimiter's quoting | S13 |
| `herestring` | the word after `<<<`, quotes kept | S14 |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `SHELL_PREFIX_OPTIONS` | constant, `tools/loop/ratify.py` | none declared |
| `piece`, `heredoc-expanded`, `herestring` | token kinds of `scan_shell_tokens` in separators mode | none |
| `sets-reachable`, `caller-shell-subst-path`, `caller-shell-env-u`, `caller-shell-exec-a`, `caller-heredoc-unquoted`, `caller-heredoc-quoted-broken`, `caller-hook-c-argv`, `caller-herestring-argv` | `ratify.py` fixture plants | none |

The carried items mint `caller-hook-comment` in unit 38's pass. No item mints a function.

### Rollout

This unit lands last, at order 22. Its carried items reach their builders through those units'
hands-off edges, so each lands in its own unit's pass and is observed here.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2, S7, S8, S13, S14, S22, S25
- `tools/lib/extract_code.py`: S7, S13, S14, S23
- `tools/lexicon/extract_code.py`, `tools/codebase-map/extract_code.py`,
  `tools/memory-tree/extract_code.py`, `tools/loop/extract_code.py`: the re-synced copies

### Alternatives rejected

- **Name `-c`, here-strings and `$(…)`-built paths as unread (S7, S14).** The audit offers it, but each
  is a shape a hook writes, and BUILD-METHOD M3 takes the option that satisfies more.
- **Put the reserved-word set in the shared block (S21).** `sh_hygiene.py` reads no block, so the
  move would change four parity copies and remove no list.

## 5. Production-readiness checklist

- security — S7, S8, S13 and S14 close reading gaps in a deny-by-default ban, and S22 makes the seed's
  one write-path check agree with the kit's own containment test.
- perf / scale — unchanged: every new reading runs over tokens the check already makes.
- error / empty / loading states — S13 names the exit 2 for an unparsable quoted body.
- observability — each plant prints its answer, and S2's line counts the seed's copies.
- risks — S10 and S11 depend on units 5, 41 and 44 carrying their items; AC10 and AC11 observe it.
- testing — the plants of S1, S7, S8, S13 and S14, the probes of S2, S5, S22 and S23, and the greps of
  the record corrections.
- migration — none.
- user docs — `help/plan.md`, S12's sentence, carried by unit 45.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant sets-reachable` runs, it exits 0.
  Red when: a matching set holds a member the tokenizer yields as an `op`, as `{` was.
- **AC2** — When `python ratify.py --fixture` runs every plant, it prints `seed — kit copies: 1` once.
  Red when: the per-plant kit copy is back and the count equals the plant count.
- **AC3** — When `grep -A2 "^## 7. Gates"` runs over each spec S3 selects at this unit's tip, and
  `tools/gate-legs.json` names `loop selftest`, the third line it prints, the leg line, holds the
  backticked leg name.
  Red when: a spec under `tools/loop/` names the leg only in prose.
- **AC4** — When `grep -c '"loop selftest"' tools/gate-legs.json` prints 0, `grep -c "is owed once
  dDeclaredLoop's loop legs are in the manifest"` prints 1 over each spec S3 selects.
  Red when: a spec under `tools/loop/` carries neither the leg nor the deferral.
- **AC5** — When a probe reads `tools/gate-legs.json` and counts the legs whose `guard` holds
  `{prefix}/loop/`, the count is at most 5.
  Red when: the guard turns broad and the guards join drops it with no other check left.
- **AC6** — When `grep -n "tools/loop/extract_code.py" .lexicon.conf` runs at this unit's tip, it
  prints the pin-move comment, and `python lexicon.py --suggest ext_of --as py.function` names `ext` as
  undeclared.
  Red when: the copy raises the offender count with no recorded move.
- **AC7** — When the plant `caller-shell-subst-path` runs, the check exits 1 naming the line.
  Red when: a script path built around `$(dirname "$0")` passes.
- **AC8** — When the plants `caller-shell-env-u` and `caller-shell-exec-a` run, each check exits 1.
  Red when: an option's argument is read as the command word.
- **AC9** — When `git grep -l "^# >>> extract_code" -- '*.py'` runs at this unit's tip, it lists the
  memory-tree kit's `extract_code.py`, whose block `cmp` finds equal to the canonical block.
  Red when: the memory-tree copy is left stale.
- **AC10** — When `grep -n '^| 12 |' memory/builds/dRankedPlan/README.md` runs at this unit's tip, the
  row ends `| no |`, and the Files touched of units 5, 41 and 44 each name `symbols.json`.
  Red when: two units that write the symbol render are rendered parallel.
- **AC11** — When `grep -l 'py.function'` selects the specs of units 30 to 52 at this unit's tip, each
  selected spec's §7 leg line holds `` `codebase-map coverage + freshness` `` and its Files touched
  names `symbols.json`.
  Red when: a function-minting unit omits the render or the leg.
- **AC12** — When `grep -c "keeps the stale one"` runs over the help page `plan.md` at this unit's tip,
  it prints at least 1.
  Red when: the owner meets the replace-in-one-commit hold with no page explaining it.
- **AC13** — When the plant `caller-heredoc-unquoted` runs, the check exits 1, and when
  `caller-heredoc-quoted-broken` runs, it exits 2 printing `cannot be parsed: heredoc body`.
  Red when: an expanded body exits 2, or a broken literal body is skipped.
- **AC14** — When the plants `caller-hook-c-argv` and `caller-herestring-argv` run, each check exits 1.
  Red when: an argv call in a `-c` string or a here-string passes.
- **AC15** — When the plant `caller-hook-comment` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: a comment line naming the predicate is read as a caller.
- **AC16** — When AC3's `grep -A2` runs over unit 41's spec at this unit's tip, the leg line holds
  `` `build-index selftest` ``.
  Red when: the memory-tree kit's suite is unnamed after its copy moves.
- **AC17** — When `grep -c "merge-rows.test.sh:423"` runs over unit 39's spec, it prints at least 1.
  Red when: the probe still cites one location for two hits.
- **AC18** — When `grep -c "tree_lib.py:416-418"` and `grep -c "memory-tree/.memory-tree.conf.example:20"`
  run over unit 45's spec, each prints at least 1.
  Red when: a citation names a line or a file that does not hold its token.
- **AC19** — When `tr '\n' ' '` joins unit 31's spec, `grep -c 'until order 14'` over the result prints
  0 and `grep -cE 'order[[:space:]]+17'` prints at least 1.
  Red when: a stale window survives beside the new figure.
- **AC20** — When `grep -c "tools/runlog/extract.py:89"` runs over unit 40's spec, it prints at least 1.
  Red when: the reuse audit still misses the sibling wrapper set.
- **AC21** — When `grep -c "sh_hygiene.py:735"` runs over unit 39's spec, it prints at least 1.
  Red when: the reuse audit still misses the sibling reserved-word list.
- **AC22** — When `python ratify.py --fixture --seed <dir> --build tFix` runs on Windows with `<dir>`
  under the temp directory spelled in another case, it exits 0, and `grep -c "_is_under"` over the loop
  kit's `ratify.py` prints at least 1.
  Red when: a case-only spelling difference refuses the seed.
- **AC23** — When `grep -c "heredoc-expanded"` runs over the canonical block's `extract_code.py` in the
  lib folder at this unit's tip, it prints at least 1, inside the `scan_shell_tokens` docstring.
  Red when: the documented shape omits a kind the stream emits.
- **AC24** — When the plant `caller-heredoc-argv` runs at this unit's tip, the refusal names
  `.githooks/pre-commit` at the file line of the planted `subprocess.run` line.
  Red when: the refusal names a body-relative line.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `python resolver (behaviour + inline parity + idiom ban)` · `build-index selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by S3's rule.

New arm: tools/loop/ratify.py · covers AC1 AC7 AC8 AC13 AC14 AC15 AC24 · `sets-reachable` and the plants of S7, S8, S13 and S14, staged by a reader that keeps `{` in the reserved set, reads `$(…)` pieces as separate words and reads no inline Python source · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 38 to 45: its 14 MEDIUM and
  11 LOW findings, ids 2 3 4 5 6 9 11 12 14 15 16 18 19 20 21 23 24 25 26 27 28 29 31 32 36, batched
  under BUILD-METHOD M4.
- rev-2 · 2026-10-27 · §3 · gains the consumes-from edge to `TOOL-dRankedPlan-58`, the hands-off edge to `TOOL-dRankedPlan-53`, the hands-off edge to `TOOL-dRankedPlan-54`, the hands-off edge to `TOOL-dRankedPlan-56`, the hands-off edge to `TOOL-dRankedPlan-57`, the hands-off edge to `TOOL-dRankedPlan-61`, the hands-off edge to `TOOL-dRankedPlan-62`, each the reciprocal of that promoted unit's own edge (spec audit of units 46 to 52, `reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`); no other section moves.

## 10. Reuse audit

Each item extends the seam its finding names rather than minting one. S7, S13, S14 and S23 extend
`TOOL-dRankedPlan-41`'s separators mode of `scan_shell_tokens`. S8 extends `TOOL-dRankedPlan-40`'s skip,
S13 and S14 `TOOL-dRankedPlan-47`'s Python arm, and S22 reuses TOOL-dDeclaredLoop-100's `_is_under`.
`python tools/codebase-map/reuse_lookup.py "find which command a shell heredoc or wrapper function runs
and read its script argument"` ranked name stems only (`read`, `run`, `run_git`), so no seam fits beyond
the readers these units already build. The recall query returned units 38, 40 and 41 and this audit's
items, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve heredoc bodies wrappers and bound variables to a script invocation" --terms "heredoc interpreter wrapper timeout function variable assignment tokenizer brace subshell string literal caller"`
