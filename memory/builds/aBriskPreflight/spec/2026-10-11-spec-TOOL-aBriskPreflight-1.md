# TOOL-aBriskPreflight-1 — check-wiring's per-item loops become one batched call per site

**Status:** SPECCED · rev-1 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md](../build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md) | research | TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 |
| [2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md) | research | TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 |
| [2026-10-11-prompt-TOOL-aBriskPreflight-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-build-brief.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-1-rebuild-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-rebuild-brief.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`check_merge_rows` and `check_eol` in `tools/check-wiring.sh` start one process per item at four
sites, and the baseline charges about 190 s of a 568 s `--check` on node `a` to them. Each site
becomes one call over all of its items, and every line either arm prints stays byte for byte what it
prints today.

## 2. Scope (IN)

Line numbers are at BASE `b726385f`. Every verdict, every printed line and the exit status stay as
they are; only the number of processes behind them moves.

- **S1** — The family harvest at `tools/check-wiring.sh:1248` keeps its builtin `[ -f ]` test per
  declared index and hands the existing paths to the SAME `sed -n` expression in as few invocations
  as a fixed argument bound allows: a new invocation starts when the next path would carry the
  current one past 8000 characters. This tree's 120 indexes are 4704 bytes of paths, measured
  2026-10-11, so they take one invocation. Observed by AC1, AC2, AC3 and AC4.
- **S2** — The smoke assertion at `tools/check-wiring.sh:1204` becomes one `awk` over `$smoke/a`. It
  counts, for each family of `$fams` in order and each id of `001 002 003` in order, the lines that
  begin with the literal text `- <family>-<id> |`, and prints the ids whose count is not exactly 1.
  That is the `miss` list, in the order the nested loop builds it today. Observed by AC3 and AC5.
- **S3** — The two audit-line reads at `tools/check-wiring.sh:1225` become one `sed` that carries
  both existing expressions verbatim. The line is held before the first and restored before the
  second, and each printed value is tagged; builtins take the last value of each tag, as `tail -1`
  took it. Observed by AC3 and AC6.
- **S4** — The eol population at `tools/check-wiring.sh:1022` feeds the filtered `git ls-files` list
  to one `git check-attr --stdin eol`, which reads one path per line, so a path holding a space
  reaches it whole. The comment above the site says why `--stdin` is safe where `xargs` was not.
  Observed by AC1, AC3 and AC7.
- **S5** — The AC10 block of `tools/check-wiring.test.sh` gains one state: `merge-rows.py` stubbed by
  a script that exits 0 having copied %O to %A. The arm must print `cannot merge` naming every `-002`
  and `-003` id. No state of the suite reaches the miss list with a driver that exits 0 today, so
  this is the arm that holds S2. Observed by AC5.

## 3. Non-goals (OUT)

- The `$(first_of …)` and `$(resolve_receipt_path …)` substitutions. aSparedSpawn-8 S3 plans
  `first_of` as a fork-free reader, and this unit leaves both as they are.
- The settings and fragment readers (`json_str`, `matchers_of`, `settings_json`) and the python
  resolution, which are `TOOL-aBriskPreflight-2`.
- The straggler inventory's own cost, which `TOOL-aBriskPreflight-3` decides.
- Raising any timeout or bound.
- `KIT_CHECK_WIRING_VERSION`. The build moves it once, after the kit's last move in this build.
- aOrientedCast's late arm in this file. Whoever lands second reconciles the file additively.

## 4. Design

### The harvest (S1)

Today, at `tools/check-wiring.sh:1249-1251`, a `while read` loop runs `[ -f "$p" ] && sed -n '…' "$p"`
once per declared path, then `LC_ALL=C sort -u`. The new form keeps the loop and the `[ -f ]` test,
collects existing paths into the positional list, and calls `sed -n "$expr" -- "$@"` whenever the
next path would carry the list past the bound, and once more for the remainder. `$expr` is the
current expression, held in one variable so both call sites spell it once. The `sort -u` is
unchanged. The loop reads `$declared` through a here-document of the variable, which is the feed the
shell-hygiene leg admits.

**Why 8000 characters.** A native `sed.exe` on PATH is started through `CreateProcess`, whose command
line caps at 32767 characters. Bash's `${#p}` counts characters, and a UTF-8 character is at most 4
bytes, so 8000 characters stays under 32000 bytes for any path. Under Git-Bash the MSYS `sed` is
started without that cap; the bound costs one comparison there.

**Why splitting loses nothing.** Each existing path is appended to exactly one invocation's list.
The expression is a per-line substitution with no address and no hold space, so the output of
several invocations, concatenated, is the output of the per-file loop. One input differs. When an
index's last line is a row and has no trailing newline, the per-file form printed that prefix with
no newline, and the next file's first prefix joined it into one token. GNU `sed` reading several
files ends that line before starting the next file. A python census of this tree's 120 indexes on
2026-10-11 found none without a trailing newline, so AC1 and AC2 are expected to be equal; if a later
tree holds one, the new reading is the correct one.

### The smoke count (S2)

At `tools/check-wiring.sh:1204-1208` twelve `grep -c -- "^- $f-$n |"` calls each count one id. The
`awk` takes `$fams` with `-v`, reads `$smoke/a` once, counts every line by the leading
`- <family>-<id> |` it carries, and in its `END` walks the families and the three ids in the same
nested order, printing ` <family>-<id>` for each count other than 1. The output is the `miss` string
byte for byte, leading space included.

The grep pattern is a BRE and the awk compare is literal. They agree for every token the harvest
regex admits as a family, `[A-Z][A-Z0-9]+`, because such a token holds no BRE metacharacter. A
`FAMILIES` token holding one, `.` say, matched more lines under the grep than it names. The literal
compare is the reading the arm's comment states: every row of the three inputs is in %A exactly once.

### The audit line (S3)

`kd` and `hs` are each a `sed -n … | tail -1` today, four processes. The new read is one
`sed -n 'h; s/<kd expression>/K \1/p; g; s/<hs expression>/H \1/p'` over `$smoke/err`, with the two
expressions copied verbatim from `tools/check-wiring.sh:1225-1226`. `h` and `g` hand the second
substitution the original line, since the first one rewrites the pattern space. Its output is
captured into a variable, and a `while read` over that variable keeps the last `K` and the last `H`
value. The tags are capital letters so neither reads as sed's own `h` command.

### The eol population (S4)

The current loop runs `git check-attr eol -- "$_p" | sed …` once per path. The new pipeline is
`git ls-files … | grep -E … | git check-attr --stdin eol 2>/dev/null | sed -n 's/^\(.*\): eol: lf$/\1/p'`.
`--stdin` reads one path per line and does not word-split, which is the defect TOOL-aBatchedTribunal-1h
recorded against `xargs`. Git's `--stdin` also unquotes a C-quoted input line, which the argv form
did not. That never applies here: `git ls-files` quotes a path with unusual bytes, and the
`^\.claude/` anchor of the `grep -E` before it rejects a line that opens with `"`. So only unquoted
paths reach either form, and each form names the same path. The output is in input order, one line
per path.

### Spawn arithmetic, DERIVED from the tree at observation time

| Site | Before | After |
|---|---|---|
| S1 harvest | one `sed` per existing index (120 at writing) | one `sed` per 8000-character chunk (1 at writing) |
| S2 smoke | one `grep` per family per id (4 × 3 at writing) | one `awk` |
| S3 audit line | two `sed` and two `tail` | one `sed` |
| S4 eol | one `git` and one `sed` per pinned path (10 at writing) | one `git` and one `sed` |

### Inventory

No new function, variable visible outside its site, flag or conf key. `expr` is local to the
harvest's substitution.

### Hazards this path carries

- `gotchas.py --for-paths tools/check-wiring.sh` selected, among others,
  `staged-break-substitutes-a-synthetic-value`: every staged break in §5 mutates the changed site
  itself, never a constant beside it.
- The sliced test script lives inside the kit dir while it runs and is cleaned up before any
  `gen_map.py --write`, which reads untracked files.
- The working copy holds CRLF on node `a`, so a multi-line scripted replace can match nothing and
  still report success. Edits are made with the editor tool and verified by reading the bytes.

### Files touched (estimate)

`tools/check-wiring.sh` · `tools/check-wiring.test.sh` ·
`memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-spawns-ab.md`

### Alternatives rejected

- **`xargs -0 -r sed`**, the idiom `tools/memory-tree/check-method-carriers.sh` uses. Measured on node
  `a` on 2026-10-11, `xargs --show-limits` reports a POSIX upper limit of 23569, which is 32000 less
  the 6383-byte environment less 2048. Once the environment passes about 30 KB, `xargs` refuses
  before running anything, `seen` comes back empty, the harvest reads no index, and the arm prints
  `ok`. The shell chunk loop has no environment term in its bound.
- **One `awk` reading the path list on stdin through `getline`.** It has no argument limit at all,
  but it re-expresses the BRE and its capture group in awk, which POSIX awk can only do with
  `match` and `substr` arithmetic. That would be two expressions of one predicate.
- **One `awk` over `$smoke/a` and `$smoke/err` together.** It saves one more process and couples two
  assertions that fail for different reasons.

## 5. Acceptance criteria

- **AC1** — When `tools/check-wiring.sh --check` runs in a throwaway clone at the pass commit under
  `%TEMP%/bp1`, after one `--fix` there, once with the built script and once with BASE's copy written
  over it (`git show` of `b726385f` at that path), the lines whose second column is `merge` or `eol`
  are byte-identical between the two runs, and both runs print `ok       merge` and `ok       eol`.
  Red when: a line differs, or either run prints `skip     eol` or no `merge` line, which would mean
  the comparison never reached a changed site.
  fixture: a clone, never the shared git dir, because `--fix` writes git config there.
- **AC2** — When the same clone's `.memory-tree.conf` has every `FAMILIES` token renamed to one no
  row leads with, streams kept (`tooling:TOOL` to `tooling:ZZZC`, and so on), and `--check` runs
  with each script, both print one identical `UNWIRED  merge` line carrying `does not declare`, and
  that line names every family the indexes lead with. This is state 5d of the suite widened from one
  family to all of them, so the printed line exposes the whole harvested set.
  Red when: the line is absent from either run, the two lines differ, or the line omits `TOOL`, which
  is the harvest returning less than the tree holds while the arm still reports.
  figure: DERIVED. The families named are whatever the indexes lead with at observation time;
  `DEPL KICK PLAY TOOL` at writing.
  fixture: if the driver refuses the renamed conf, both runs print `cannot merge` instead and this
  observation is not made; the builder then renames one family per run, four runs.
- **AC3** — When `2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh` traces `--check` in that
  clone with BASE's script and then the built one, and
  `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py` reads
  each trace, its `execs by program` table shows `sed` lower by at least the index count plus the
  pinned-path count less 1, `grep` lower by at least three per family, `git` lower by at least the
  pinned-path count less 1, and `tail` lower by 2. Both rows and a host-state line beside each are
  written to the result record under `build/`.
  Red when: any site still starts a process per item, which leaves its program's count where it was.
  figure: DERIVED. The index, family and pinned-path counts are read from the clone at observation
  time: 120, 4 and 10 at writing.
- **AC4** — When state 5d of the AC10 block of the check-wiring suite runs as a sliced arm against
  the built script, its `does not declare TOOL` assertion passes. With the post-loop `sed` call of
  the harvest commented out as a staged break, it fails. Restored, it passes.
  Red when: the staged break leaves the assertion passing, so the arm never read the harvest.
- **AC5** — When the new stub state of S5 runs as a sliced arm, `check-wiring.sh --check` prints one
  `UNWIRED  merge` line whose `missing or duplicated:` list names every `-002` and `-003` id of every
  declared family, and that list is byte-identical to the one BASE's script prints in the same state.
  With the `awk` changed to print nothing as a staged break, the assertion fails. Restored, it passes.
  Red when: the list differs from BASE's, or reads ` none`.
- **AC6** — When state 5e of the AC10 block runs as a sliced arm against the built script, its
  `HASHED` assertion passes. With the `K` and `H` tags of S3 swapped as a staged break, it fails.
  Restored, it passes.
  Red when: the staged break leaves the assertion passing.
- **AC7** — When the AC9 block of the check-wiring suite runs as a sliced arm against the built
  script, the `a Skill path with a space is still seen` and `--fix repairs a spaced path` assertions
  pass, and the `note     eol` line names that path. With a `tr ' ' '\n'` stage inserted before
  `git check-attr --stdin` as a staged break, the first assertion fails. Restored, both pass.
  Red when: the staged break leaves the assertions passing.
- **AC8** — When `python tools/codebase-map/gen_map.py --check` runs at the pass commit, it exits 0.
  Red when: the pass left an untracked slice script under `tools/` or minted a function the map does
  not hold.

## 6. Gates

`check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/check-wiring.test.sh · covers AC5 · a merge-rows.py stub that exits 0 after copying %O to %A · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py "run one sed over many files split by command-line length without
word-splitting paths"` returned name-stem neighbours only, such as `run`, `run_arms` and
`extract_run_facts`, and none of them batches a per-file command. No existing seam fits as a helper.
The seams this unit extends are in place: `check_merge_rows` already reads attributes through one
`git check-attr --stdin` at `tools/check-wiring.sh:1136`, and S4 copies that call shape. `xargs -0 -r`
in `tools/memory-tree/check-method-carriers.sh` was found by grep and rejected in §4 on measurement.
The recall probe returned `TOOL-aBatchedTribunal-1h`, the record of why the eol population went
per-path, which S4 answers, and aMendedLedger U5's reason for `--stdin` in the same arm.

Recall terms used: `python tools/memory-recall/query.py "why does check-wiring run one process per
item in the merge-rows harvest and the eol population" --terms "check-wiring merge=rows family
harvest check_eol git check-attr stdin xargs word-split spawn per-path SessionStart"`
