# TOOL-aTwinnedPass-3 — `--dispatch` condition 1 leaves an effective generated output out of the sibling comparison

**Status:** INPROGRESS · rev-1 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md) | research | TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2 |
| [2026-11-15-prompt-TOOL-aTwinnedPass-3-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-3-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-3-pass-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-3-pass-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Two open passes that both declare a generated output every pass rewrites are refused by
`--dispatch` condition 1 today, though `--check-commit` admits that same output undeclared, so the
refusal binds only the pass that declared honestly. This unit leaves a declared path that an effective
generated output covers out of condition 1's sibling comparison, on both sides, and names the paths
it left out in one stderr note. Every other refusal is unchanged, so two disjoint passes of one
build can be declared together, which units 1 and 2 need.

## 2. Scope (IN)

- **S1** — A library predicate `check_generated_output` in `tools/unattended/lib-unattended.sh`,
  placed after `overlaps`, takes a path and the `index:generator` pairs and returns 0 when the index
  half of one pair covers the path, through `covers`. Observed by AC1.
- **S2** — `verb_dispatch` sorts its declared paths once, on the line after the run-state removal
  block: each path the predicate admits over `${GENERATED_INDEXES:-}` joins `_c1_gen`, and every other
  path joins `_c1_own`. Condition 1's outer loop reads `$_c1_own` in place of `"$@"`. Observed by
  AC2, AC4, AC7.
- **S3** — Condition 1's inner loop skips each sibling path that the predicate admits, before its
  `overlaps` call. Observed by AC5, AC7.
- **S4** — One stderr note per call, printed when `_c1_gen` is not empty, directly after the
  run-state file's note, naming the unit and each path left out. Observed by AC2, AC5.
- **S5** — Condition 1's refusal text, its `fail 49` site, condition 3's two halves, the parked row
  and every other refusal are unchanged. The row still records every declared path. Observed by AC2,
  AC3, AC4, AC6.
- **S6** — The block comment above condition 1 states the narrowing, why it is sound, and what it
  does not check (§4, "The comment"). Observed by AC7.
- **S7** — The `--dispatch` paragraph and the "Before dispatching a pass" bullet of the verbs guide
  state the narrowing, in `tools/unattended/VERBS.template.md` and its copy
  `memory/guides/UNATTENDED-VERBS.md`, byte-equal past line 1. Each new phrase AC8 greps sits on one
  line. Observed by AC8.
- **S8** — The suite arms of §4, "The arms", in region 4 of `tools/unattended/unattended.test.sh`,
  with `FLOOR_ASSERTIONS` and `FLOOR_SHARD_4` raised by the block's counted assertions. Observed by
  AC2, AC3, AC4, AC5.
- **S9** — No `fail 49` site is added or moved, so `tools/unattended/unarmed-branches.txt` is not
  re-keyed. Observed by AC6.
- **S10** — `memory/map/generated/symbols.json` regenerated, carrying the new function. Observed by
  AC9.

## 3. Non-goals (OUT)

- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`. The live
  dDeclaredLoop branch rewrote them, so a change there conflicts when that run merges main.
- `memory/builds/dDeclaredLoop/`, its run's worktree, its branch and its run-state file.
- Moving the three existing inline copies of the same question to the new predicate:
  `check_commit_message` (`tools/unattended/unattended.sh@eb567029:14352`), `check_branch_carried`
  (`:4088`) and check 23's `check_generated_render` (`tools/unattended/check-unattended.sh@434b64be:4390`).
  This is F2. The live branch's `check_commit_message` hunk sits just above the first copy, and
  moving the other two owes suites the build README does not allow while that run is live.
- Condition 3's generator pairing and its shared-record half. The pairing still reads every declared
  path and every sibling path, generated outputs included.
- A path that CONTAINS a generated output, such as a declared `memory/map`. It is still compared, on
  either side (§4, "Which paths are left out").
- The empty-set note `no sibling pass is open`. It keeps measuring the sibling rows, not the paths
  left to compare.
- M6's own wording in the build method. This is F3.
- The kit version. The lander's `mint` moves it (`tools/push-main.sh`, its "KIT VERSIONS ARE MINTED
  HERE" comment).
- A `help/` page. None covers `--dispatch` or condition 1: `grep -rlF -e --dispatch help/` and
  `grep -rlF 'condition 1' help/` match nothing at `aebbb4a72`. No flag or declared usage row moves,
  so the docs leg has nothing to re-anchor.
- The worktree tool and the merge-back are `TOOL-aTwinnedPass-2`'s, and the harness's `tree` key is
  `TOOL-aTwinnedPass-1`'s.

### Edges

- **hands-off** `TOOL-aTwinnedPass-2` — its merge verb's `check_resolvable_path` calls
  `check_generated_output` for the generated half of its test.
- **hands-off** external — moving the three inline copies named above onto `check_generated_output`,
  after the dDeclaredLoop run merges main, owed as an ask the main loop files.
- **hands-off** external — M6 condition (1)'s wording, if F3 picks (b), owed as an ask on the
  memory-tree kit's build-method template.

## 4. Design

### Evidence

Read at base `aebbb4a72`.

| Line | What sits there |
|---|---|
| `tools/unattended/unattended.sh@eb567029:61` | `set -u` |
| `tools/unattended/unattended.sh@eb567029:890` | `GENERATED_INDEXES=$(resolve_generated_indexes ...)` at conf load, so `verb_dispatch` reads the effective pairs |
| `tools/unattended/unattended.sh@eb567029:14544` | `verb_dispatch` |
| `tools/unattended/unattended.sh@eb567029:14746` | the `--writes` refusals: empty, absolute, `..`, the root, a glob character, whitespace, the bypass flag |
| `tools/unattended/unattended.sh@eb567029:14770` | `remove_run_state_writes "$rel" "$@"`; its note is at `:14772`, and `set -- "${_rw_keep[@]}"` follows |
| `tools/unattended/unattended.sh@eb567029:14776` | condition 3's flat half: the run-state file and `SHARED_RECORDS`, through `overlaps` |
| `tools/unattended/unattended.sh@eb567029:14829` | `sibrows=$(read_open_passes "$rel")`; `sibpaths` at `:14830` |
| `tools/unattended/unattended.sh@eb567029:14861` | the generator pairing, `for pair in ${GENERATED_INDEXES:-}`, over `"$@" $sibpaths` on both halves |
| `tools/unattended/unattended.sh@eb567029:14883` | condition 1: `for p in "$@"` at `:14888`, `for q in ${sib#* · reason }` at `:14889` |
| `tools/unattended/unattended.sh@eb567029:14894` | condition 1's `fail 49`, then `remove_spec_token_check; return 1` |
| `tools/unattended/unattended.sh@eb567029:14352` | `check_commit_message`: `covers "${q%%:*}" "$p"` over `${GENERATED_INDEXES:-}` admits a staged path undeclared |
| `tools/unattended/lib-unattended.sh@a3e03db6:746` | `covers`, directional, both sides through `normpath`; `overlaps` at `:751` |
| `tools/unattended/lib-unattended.sh@a3e03db6:839` | `resolve_generated_indexes`: the kits' `[[generated]]` rows, then the conf's pairs |
| `tools/unattended/lib-unattended.sh@a3e03db6:912` | `scan_shared_index_overlaps`, which takes the pairs as an argument |

The `--writes` refusals at `:14746` reject whitespace and glob characters in every declared path, and
`park` records the normalised spelling. So a space-joined list of declared or sibling paths splits
back into those paths unquoted, as `$sibpaths` and `${sib#* · reason }` already do. Under the repo's
declaration, the effective pairs resolve to ten, from `memory/map/generated` to `.claude/roles.json`.
That set is DERIVED by `resolve_generated_indexes "$PWD" "" memory` at any time.

### Why the narrowing is sound

`check_commit_message` admits a staged path that an effective generated output covers, whether or
not the pass declared it (`:14352`), and check 23's `check_generated_render` reads it the same way at
the close. So two passes that both rewrite `memory/map/generated/symbols.json` without declaring it
are admitted by `--dispatch` and by the commit hook today, while the same two that declare it are
refused by condition 1. The refusal tests how a pass spelled its declaration, not what it writes,
and leaving these paths out of condition 1 makes the two readers agree. Condition 3 already admits a
generated index alone, which M6 retracted as the vacuous reading. The collision M6 names, the index
TOGETHER WITH its generator, stays refused by the pairing, which this unit leaves alone.

### Which paths are left out

A declared path is left out when `covers <index> <path>` holds for some pair. That is the path is
the index, or sits under it, as `check_commit_message` reads it. A path that contains an index is not
left out. `--writes memory/map` therefore still collides with a sibling's `memory/map/README.md`. The
direction is the one the commit hook already forgives, and widening it to `overlaps` would admit
`--writes memory` against every sibling. This is the one-way containment the gotcha
`containment-tested-one-way` warns of, chosen here because the exemption must stay narrower than the
writes it forgives.

A sibling path is left out by the same test. So `--writes work` from one pass and `--writes
work/idx` from a sibling, where `work/idx` is an index, are admitted together: their only
shared file is the index. The pass declaring `work` is still compared on every other sibling path.

### The predicate

```
# `check_generated_output path pairs` — the index half of one `index:generator` pair covers the path,
# through `covers`, so the path is a generated output's and not a pass's own write.
check_generated_output() { # path · generated-indexes (`index:generator` pairs, space-separated) -> 0 when one index half covers the path
  local _cgo_q
  for _cgo_q in $2; do covers "${_cgo_q%%:*}" "$1" && return 0; done
  return 1
}
```

It takes the pairs as an argument, as `scan_shared_index_overlaps` and `build_commit` do, so it reads
no caller global. It forks nothing: `covers` and `normpath` are pattern substitution. A token
carrying no colon is read whole as an index, as `check_commit_message` reads it.

### The driver change

Directly after the run-state removal block ends (`:14775`), and before condition 3's flat half:

```
  # CONDITION 1 LEAVES AN EFFECTIVE GENERATED OUTPUT OUT (TOOL-aTwinnedPass-3): see the comment above condition 1.
  _c1_own=""; _c1_gen=""
  for p in "$@"; do
    if check_generated_output "$p" "${GENERATED_INDEXES:-}"; then _c1_gen="$_c1_gen $p"; else _c1_own="$_c1_own $p"; fi
  done
  [ -z "$_c1_gen" ] || echo "unattended: dispatch — an effective generated output covers these declared paths, which every pass may rewrite and --check-commit admits undeclared, so condition 1 leaves them out of the sibling comparison while the row records them and the generator pairing reads them, for $unit:$_c1_gen" >&2
```

`_c1_own` and `_c1_gen` join `verb_dispatch`'s `local` line. Condition 1 becomes:

```
    for p in $_c1_own; do
      for q in ${sib#* · reason }; do
        check_generated_output "$q" "${GENERATED_INDEXES:-}" && continue
        overlaps "$p" "$q" || continue
        ...unchanged
```

The loop order is kept, `p` outer and `q` inner, so a refusal over several overlaps names the same
first pair it names today. The note sits beside the run-state note and before every refusal below
it, so it prints on a call that is then refused, as that note does. It names this call's own paths
only, because the sibling rows are not read until `:14829`. A sibling's paths left out were named by
that sibling's own call. The note goes to stderr, where the run-state note goes. The driver's run log
records refusals by check number and the START and END pair, not stderr lines, so the note is read
in the caller's captured output, not in `driver.log`.

`"$@"` is not narrowed. Condition 3's flat half, the generator pairing, `want` and the parked row
all read it as today.

### The comment

The block comment above condition 1 gains one paragraph, tagged `TOOL-aTwinnedPass-3`. It says that a path an effective generated
output covers is left out of the comparison on both sides, through `check_generated_output`. It says
why that is sound: `--check-commit` admits such a path undeclared, so the refusal bound only the pass
that declared it. It says that a path containing an index is still compared, and that the generator
pairing above still reads every path. It also names what this does not check, the first bullet of
"What the design does not check" below.

### The verbs guide

In the `--dispatch` paragraph, after "a unit's own rows are never siblings of each other.", one
sentence, with the phrase `is left out of that comparison` on one line: "A declared path that an
effective generated output covers, a kit's `[[generated]]` row or a `GENERATED_INDEXES` pair, is left
out of that comparison on either side, because every pass may rewrite one and `--check-commit` admits
it undeclared; the call names its own such paths in one stderr note, and its row still records them
and the generator pairing still reads them."

In the "Before dispatching a pass, DECLARE its write set" bullet, "It refuses two passes claiming one
file" becomes "It refuses two passes claiming one file other than a generated output", with the phrase
`other than a generated output` on one line. Both copies change identically.

### The arms

One block in region 4 of `tools/unattended/unattended.test.sh`, directly after the M1 pairing block
ends at `mv .unattended.conf.bak .unattended.conf` (`tools/unattended/unattended.test.sh@ba1ce4cb:9528`),
and before the L2 missing-library block. It saves and restores the conf the way the M1 block does.

```
build_specced_tree; run --preflight tRun --keepalive-id k1 >/dev/null
cp .unattended.conf .unattended.conf.bak
printf '\nGENERATED_INDEXES="work/idx:gen/mk"\n' >> .unattended.conf
```

| # | Call | Assertions |
|---|---|---|
| B1 | `--pass ARCH-tRun-1 --writes work/idx --writes lane/one` | `hit` `dispatch declared`; `hit` `for ARCH-tRun-1: work/idx` |
| B2 | `--pass ARCH-tRun-2 --writes work/idx --writes lane/two` | `hit` `dispatch declared`; `miss` `two passes claiming one file are not disjoint`; `hit` `for ARCH-tRun-2: work/idx` |
| B3 | the run-state file after B2 | one counted `grep -q` for the row ` dispatch · item .* ARCH-tRun-2 · reason work/idx lane/two$` |
| B4 | `--pass ARCH-tRun-3 --writes gen/mk` | `hit` `--dispatch declares a generated index together with its generator` |
| B5 | `--pass ARCH-tRun-3 --writes lane/one` | `hit` `--dispatch declares a path a sibling pass in the same group already declared, and two passes claiming one file are not disjoint: lane/one also in` |
| B6 | `--pass ARCH-tRun-3 --writes work` | `hit` `dispatch declared`; `miss` `so condition 1 leaves them out of the sibling comparison` |

Then `mv .unattended.conf.bak .unattended.conf`. That makes ten assertions, every one unconditional,
counted off the block's own lines. `FLOOR_ASSERTIONS` rises 3329 to 3339 and `FLOOR_SHARD_4` rises 410
to 420, each with a `RAISED` comment in the house shape. B4 runs before B6 because B6 parks a row
that B4 does not need.

At base, B1's note, all three of B2's, B3 and B6's `dispatch declared` are red: B2 and B6 are refused
by condition 1, and no note exists. B4 and B5 are the controls, green at base and after. B5 is the
answer to `fixture-passes-by-finding-nothing`: an exemption that skipped the whole sibling row, or
every path of a row carrying an index, admits B5 and reds it. B4 is red if the narrowing removes
covered paths from `"$@"` or `$sibpaths` instead of from condition 1's loops.

No `GENERATED_INDEXES` line set earlier in region 4 survives into this block, because
`build_specced_tree` resets the tree. The fixture's own kits' `[[generated]]` rows join the effective
set, and none covers `work/`, `lane/` or `gen/`.

Ceiling, a declared bound rather than a measurement: the block adds one tree build, one preflight and
six driver calls to shard 4, at most 90 s on node a (PINNED 2026-11-15). The close's shard-4 run
measures it.

### Inventory

| Identifier | Kind | Lexicon |
|---|---|---|
| `check_generated_output` | function, `tools/unattended/lib-unattended.sh` | `python tools/lexicon/lexicon.py --suggest check_generated_output --as sh.function`: OK, leads with `check`. `is_generated_output` was refused, "use `check_`"; `covered_by_generated` has no declared verb |
| `_cgo_q` | the predicate's local | no shell-variable cell: `.lexicon.conf` declares `sh.function` alone |
| `_c1_own`, `_c1_gen` | `verb_dispatch` locals | no cell, as above |

None of these names occurs in `tools/` at base (`grep -rn check_generated_output tools/` matches
nothing).

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/map/generated/symbols.json`

### Rollout

Live, with no switch, unless F1 picks (b). The pass commit carries
`memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-3-1-acceptance-ledger.md`, one
`**Evidences:** TOOL-aTwinnedPass-3` block, and names the arms' red then green as owed to the main
loop. The status flip to CLOSED is the pass's last change. The build README requires the owner's
explicit ask before landing.

The live dDeclaredLoop branch's hunks in `tools/unattended/unattended.sh` stop at
`check_commit_message`'s trailer read, above `:14352`. Its two hunks in the library sit at
`pass_commit` and `check_gen_region_only`, past `:1062`. None overlaps `:751`, `:14770` to `:14900`
or the predicate's new lines. This was read with `git diff 0578adb73 branch/unattended-declared-loop-d56bf0`
on 2026-11-15, and it is PINNED to that branch tip.

### Alternatives rejected

- **`overlaps` in the predicate.** It would leave out `--writes memory` and `--writes memory/map`,
  which contain an index, and admit every sibling under them.
- **Removing covered paths from `"$@"` at the note.** The generator pairing and the parked row read
  `"$@"`, so the pairing would stop seeing an index, which B4 catches, and the row would lose paths
  that `--check-commit` grades against.
- **Skipping a whole sibling row that declares any covered path.** It drops that row's product paths
  from the comparison, which B5 catches.
- **An inline loop at both new sites.** That makes four and five copies of one question, against the
  charter's `[reuse]`. F2 covers moving the existing three.
- **A note naming sibling paths too.** The note would move below `read_open_passes`, away from the
  run-state note, and would repeat what each sibling's own call already printed.

### What the design does not check

- That a path an effective generated output covers is ever re-rendered. Two passes that hand-edit
  one index are both admitted, as `--check-commit` already admits each, and whichever render runs
  last wins. `TOOL-aTwinnedPass-2`'s merge re-renders after each merge, but this unit does not rely
  on that.
- That a `[[generated]]` row's generator really writes its path. `resolve_generated_indexes`' header
  says no reader here runs a generator, and this unit adds none.
- A declaration whose every path is covered reaches condition 1 with nothing to compare. The
  empty-set note does not fire for it, because that note measures sibling rows. The new note names
  the paths, which is the reader's signal.
- A sibling row parked before this change reads the same as one parked after: rows record paths, not
  verdicts, so the narrowing applies to every open row at once.
- The note on a call that a later refusal rejects. It prints anyway, as the run-state note does.
- A colonless `GENERATED_INDEXES` token is read whole as an index, as `check_commit_message` reads
  it. The generator pairing skips such a token, so the two readers differ on a malformed conf, as they
  do at base.

## 5. Production-readiness checklist

- security — no new input, flag, write path or surface. The narrowing admits only paths that
  `--check-commit` already admits undeclared, and the deny cases, product paths and the index with
  its generator, keep their refusals.
- perf / scale — one predicate call per declared path, and one per sibling path per uncovered
  declared path, each pure bash with no fork, against today's `overlaps` calls in the same loops.
- error / empty / loading states — an empty `GENERATED_INDEXES` leaves every path compared and
  prints no note, which is today's behaviour exactly.
- observability — one stderr note per call that leaves a path out, naming the unit and the paths.
- risks — two passes hand-editing one generated output are admitted (§4, "What the design does not
  check"); the merge with the live run's branch, which §4 "Rollout" read as hunk-disjoint.
- testing — AC1 to AC9, and the arms on the `New arm:` line in §7.
- migration — N/A: no record shape moves; rows already parked read as before.
- user docs — the verbs guide (S7); no page under `help/` describes `--dispatch`.

## 6. Acceptance criteria

- **AC1** — When the probe below sources `tools/unattended/lib-unattended.sh` and calls
  `check_generated_output` over seven paths and an empty pair list, it prints `work/idx 0`,
  `./work//idx 0`, `work/idx/x 0`, `lane/dir/y 0`, `work 1`, `work/idxa 1`, `gen/mk 1` and
  `empty 1`.
  ```
  ( . tools/unattended/lib-unattended.sh
    for p in work/idx ./work//idx work/idx/x lane/dir/y work work/idxa gen/mk; do
      check_generated_output "$p" "work/idx:gen/mk lane/dir:gen/mk"; printf '%s %s\n' "$p" "$?"; done
    check_generated_output work/idx ""; echo "empty $?" )
  ```
  Red when: the predicate is missing and every row prints 127, it tests `overlaps` and `work` prints
  0, or it reads the generator half and `gen/mk` prints 0.
- **AC2** — When `--dispatch tRun --pass ARCH-tRun-1 --writes work/idx --writes lane/one` and then
  `--pass ARCH-tRun-2 --writes work/idx --writes lane/two` run with the conf declaring
  `GENERATED_INDEXES="work/idx:gen/mk"`, stdout and stderr captured apart, each call's stdout
  carries `dispatch declared`. Each call's stderr carries
  `so condition 1 leaves them out of the sibling comparison` and `for ARCH-tRun-<n>: work/idx`,
  and its stdout carries neither. The second call's output carries no
  `two passes claiming one file are not disjoint`.
  Red when: condition 1 still compares a covered path, which refuses the second call, or the note is
  missing or printed on stdout.
  fixture: the driver suite's tRun build as `build_specced_tree` and a preflight leave it. Outside
  the suite the tree holds none, and a pass builds it in a `%TEMP%` repository the way the suite's
  `mkconf` and `build_specced_tree` do.
  permission: the suite arm that re-observes this is the main loop's to run at the close.
- **AC3** — When, after AC2, the tRun build's run-state file is read, one row matches
  ` dispatch · item .* ARCH-tRun-2 · reason work/idx lane/two$`.
  Red when: the covered path is dropped from the parked row.
  fixture: as AC2.
  permission: as AC2.
- **AC4** — When, after AC2, `--dispatch tRun --pass ARCH-tRun-3 --writes gen/mk` runs, it exits 1
  and its output carries `--dispatch declares a generated index together with its generator`.
  Red when: the narrowing removes covered paths from `"$@"` or `$sibpaths`, so the pairing no longer
  sees the index.
  fixture: as AC2.
  permission: as AC2.
- **AC5** — When, after AC4, `--dispatch tRun --pass ARCH-tRun-3 --writes lane/one` runs, it exits 1
  and its output carries today's message,
  `--dispatch declares a path a sibling pass in the same group already declared, and two passes claiming one file are not disjoint: lane/one also in`.
  Then `--pass ARCH-tRun-3 --writes work` prints `dispatch declared` and no
  `so condition 1 leaves them out of the sibling comparison`.
  Red when: the exemption skips a whole sibling row, which admits `lane/one`, or only this call's
  side is left out, which refuses `work` against the sibling's `work/idx`.
  fixture: as AC2.
  permission: as AC2.
- **AC6** — When the probe below prints each check-49 branch's ordinal and signature at base and
  after the change, the two listings are equal, and `git diff --exit-code` over
  `tools/unattended/unarmed-branches.txt` prints nothing.
  ```
  python -c "import importlib.util as u;s=u.spec_from_file_location('a','tools/memory-tree/check-arms.py');m=u.module_from_spec(s);s.loader.exec_module(m);[print(b['ord'],b['sig'][:60]) for b in m.branches('.','tools/unattended/unattended.sh') if b['num']==49]"
  ```
  Red when: a `fail 49` site is added, removed or reordered, or condition 1's text changes.
  figure: the ordinals are DERIVED by the probe from the source at observation time; at base it
  lists 40 branches.
- **AC7** — When the awk below runs over `tools/unattended/unattended.sh`, it prints `2 1`: two
  `check_generated_output` calls inside `verb_dispatch`, and one condition-1 loop reading
  `for p in $_c1_own`. `grep -c 'TOOL-aTwinnedPass-3'` over the same file prints at least 2, for the
  sort and the comment above condition 1.
  ```
  awk '/^verb_dispatch\(\)/{v=1} v && /^}$/{v=0} v && !/^[[:space:]]*#/ && /check_generated_output /{c++} v && /for p in \$_c1_own; do/{o++} END{print c+0, o+0}' tools/unattended/unattended.sh
  ```
  Red when: either side's skip is missing, or condition 1 still loops over `"$@"`.
- **AC8** — When `grep -c 'is left out of that comparison'` and
  `grep -c 'other than a generated output'` run over `tools/unattended/VERBS.template.md` and
  `memory/guides/UNATTENDED-VERBS.md`, each prints 1, and the comparison below prints nothing.
  ```
  diff <(tail -n +2 tools/unattended/VERBS.template.md) <(tail -n +2 memory/guides/UNATTENDED-VERBS.md)
  ```
  Red when: either copy lacks a sentence, or the copies differ.
- **AC9** — When `python tools/lexicon/lexicon.py --suggest check_generated_output --as sh.function`
  runs, it prints a line opening `OK`, and `memory/map/generated/symbols.json` carries the string
  `"check_generated_output"`.
  Red when: a name the lexicon refuses lands, or the index is not regenerated.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `routed-commits selftest` · `scratch-guard self-test` · `tier2-review self-test` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `unattended skill wiring` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `pass-order history` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 AC4 AC5 · the driver at base aebbb4a72, whose condition 1 compares work/idx and so refuses B2 and B6, prints no note for B1 and B2, and parks no B2 row; B4 and B5 are controls green at base · FLOOR_ASSERTIONS 3329 to 3339 and FLOOR_SHARD_4 410 to 420

The close's driver-suite run re-observes, unchanged, every existing `--dispatch` arm: in region 4
the condition-3 arms at `memory/LIVE.md`, the dGroundRules-66 terminal-unit arm, the aSwiftRefusal-3
deferred-unit arm and the M1 pairing block, none of which declares one generated output from two
siblings; and in region 3 the aBriskDeclaration-1 A6 arm, whose stderr trace now carries the note's
`echo` line, which none of its four patterns matches, and whose A4 window holds no new `return 1`.

## 8. Open questions

- **F1 — Does this land live, or dark behind a default-off switch?** The charter lands risky
  behaviour dark. (a) Live, no switch: the change narrows a refusal to what `--check-commit` already
  admits, the deny cases keep their refusals, and a switch would keep a second path that no run
  exercises. (b) A conf key, default off: the run stays on today's path until an owner turns it on,
  at the cost of a key-table row, a second path the arms must cover, and units 1 and 2 reaching a
  parallel group only with the key set. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).
- **F2 — Where does the "covered by a generated output" question live, and who calls it?** (a) A
  library predicate, `check_generated_output`, called at this unit's two sites only, with the three
  existing inline copies left and named as a follow-up ask. (b) The same predicate, with all three
  existing copies moved onto it in this unit. That honours `[reuse]` in full, but it changes
  `check_commit_message` beside the live branch's hunk and `check-unattended.sh`, whose suites the
  build README does not allow while that run is live. (c) Inline loops at the two new sites. That
  makes five copies. Recommendation: (a). `TOOL-aTwinnedPass-2`'s merge verb asks the same question
  and sources the same library, so the predicate is there for it.
  RESOLVED (agent, 2026-11-15, delegated): (a); `TOOL-aTwinnedPass-2` calls the predicate.
- **F3 — Does M6 condition (1)'s wording change?** It reads "their WRITE sets ... do not intersect",
  and after this unit `--dispatch` admits two sets that intersect on a generated output. (a) Leave
  the method as it is: condition (3) already treats a generated index alone as harmless, and the verbs
  guide states the narrowing. (b) An ask for the memory-tree kit's build-method template to say
  "less the generated outputs" in (1), as a unit of its own under M2. Recommendation: (b), filed by
  the main loop at this build's close, with this unit unchanged either way.
  RESOLVED (agent, 2026-11-15, delegated): (b), the ask filed at the close.

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

The seam this unit extends is `covers` in `tools/unattended/lib-unattended.sh`, the question
`check_commit_message` already asks of `${GENERATED_INDEXES:-}` at
`tools/unattended/unattended.sh@eb567029:14352`, now asked through one library predicate placed
beside it. The probe `python tools/codebase-map/reuse_lookup.py "is a path covered by a generated
output index, exempt a generated index from the write-set overlap"` ranked `overlaps`,
`resolve_generated_indexes` and `scan_shared_index_overlaps` in `tools/unattended/lib-unattended.sh`
among its seams, and no candidate answers "does an index half cover this path". The source read
found three inline copies of that question, in `check_commit_message`, `check_branch_carried` and
check 23's `check_generated_render`, and none extracted. So the predicate is the extraction, and F2
decides who else calls it. `gotchas.py --for-paths` over the driver and the library selected
`containment-tested-one-way`, answered in §4 "Which paths are left out" by choosing `covers` over
`overlaps` on purpose; `fixture-passes-by-finding-nothing`, answered by the B5 control; and
`inherited-git-dir-pins-the-work-tree-to-the-cwd`, which does not bind, because `--dispatch` does not
run under a hook.

Recall terms used: `python tools/memory-recall/query.py "why does dispatch condition 1 refuse two
passes declaring one generated index" --terms "dispatch condition GENERATED_INDEXES covers overlaps
sibling generated index check-commit exemption disjoint"`
