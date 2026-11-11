# TOOL-aSmoothedDispatch-1 — `--writes` takes every path up to the next flag, and splits a whitespace-joined value

**Status:** CLOSED · rev-2 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aSmoothedDispatch-1-1-acceptance-ledger.md](../build/2026-11-10-build-TOOL-aSmoothedDispatch-1-1-acceptance-ledger.md) | journal | TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7 TOOL-aSmoothedDispatch-8 TOOL-aSmoothedDispatch-9 |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-1-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-1-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md) | research | TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-1-token-fix.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-1-token-fix.md) | research | TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 |
| [2026-11-10-review-TOOL-aSmoothedDispatch-1-closing-diff-round1.md](../reviews/2026-11-10-review-TOOL-aSmoothedDispatch-1-closing-diff-round1.md) | diff-review | TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7 |

<!-- /gen:spec-records -->

## 1. Goal

`unattended.sh --dispatch <slug> --pass <id> --writes a b c` declares three paths, and
`--writes "a b"` declares two. Today the first refuses with check 14 on `b`, and the second refuses
with check 49 on whitespace. The driver journal across 38 runs logged 197 "unknown argument"
refusals, most of them bare paths after `--writes` (brief item 1, build README). Every refusal that
guards a real defect keeps refusing.

## 2. Scope (IN)

- **S1** — The `--writes)` arm of the driver's argument loop consumes every following argument up to
  the next one that starts with `--`. It splits each consumed value on space, tab and newline, with
  `IFS` pinned on the `read` itself, and appends every field to `DP_WRITES`. No field is
  glob-expanded. Observed by AC1, AC2 and AC4.
- **S2** — An argument that splits into no field contributes one empty path, and so does a
  `--writes` with no value before the next flag or the end of argv. Either one still reaches the
  existing empty-path refusal in `verb_dispatch`. Observed by AC3.
- **S3** — The whitespace refusal in `verb_dispatch` stays. It now catches the whitespace S1 does not
  split on, such as a carriage return, a vertical tab or a form feed. Its comment is rewritten to say
  so, and its two suite arms move from a space-holding value to a carriage-return value. Observed by
  AC4 and AC6.
- **S4** — The header usage line, and the two sentences of the verb carrier that say "one path per
  occurrence", state the new shape. The verb carrier ships as `tools/unattended/VERBS.template.md`
  and is copied byte for byte to `memory/guides/UNATTENDED-VERBS.md`, and both copies change
  together. Observed by AC5.
- **S5** — Suite arms in `tools/unattended/unattended.test.sh` dispatch with several paths after one
  `--writes` and with one whitespace-joined value, and read the declared row. `FLOOR_ASSERTIONS` and
  `FLOOR_SHARD_4` rise by the net assertions added. Observed by AC6.

## 3. Non-goals (OUT)

- Dropping the run-state file from the declared paths: `TOOL-aSmoothedDispatch-2`.
- `--help`: `TOOL-aSmoothedDispatch-3`, which also edits this argument loop.
- Any change to `verb_dispatch`'s other refusals: the empty, absolute, escaping, repository-root,
  glob, bypass-flag, sibling-overlap and shared-record refusals stay as they are.
- A path that really contains a space. The row grammar keeps its paths in one space-delimited field
  (`tools/unattended/lib-unattended.sh:1123`), so no declaration can carry one, before or after this
  unit.
- A bare `·` field. It is already declarable as `--writes ·`, and S1 produces no field a single
  `--writes <field>` could not already pass, so this unit neither widens nor closes that.
- The worked example in `tools/unattended/SKILL.template.md:114`, which repeats `--writes` once per
  path. That form stays legal, so the example stays true.
- No hand edit to `KIT_UNATTENDED_VERSION` or `tools/unattended/kit.toml`. The lander's `mint` moves
  the version.

### Edges

none

## 4. Design

### What happens today

The arm at `tools/unattended/unattended.sh:15091` appends exactly one value:

```bash
    --writes)       DP_WRITES+=("${2:-}"); shift 2 || shift ;;
```

A second bare path then reaches the catch-all arm, which refuses with check 14 because it is not a
slug verb (`tools/unattended/unattended.sh:15199-15205`). A quoted list arrives in `verb_dispatch`
as one path and meets the whitespace refusal (`tools/unattended/unattended.sh:14515`). The comment
above that loop says a space-joined value "cannot carry" that refusal
(`tools/unattended/unattended.sh:14500-14501`).

Both behaviours were observed at `ae6735c1` with the probe below. `--writes a b c` printed check 14
naming `b` and `rc=1`, and `--writes "a b"` printed `arg[a b]` as one path.

### The arm

The `--writes)` arm becomes a consuming loop:

```bash
    --writes)       shift; _dw_n=0
                    while [ $# -gt 0 ]; do
                      case "$1" in --*) break ;; esac
                      _dw=(); IFS=$' \t\n' read -r -d '' -a _dw <<<"$1" || :
                      if [ ${#_dw[@]} -eq 0 ]; then DP_WRITES+=(""); else DP_WRITES+=("${_dw[@]}"); fi
                      _dw_n=$((_dw_n+1)); shift
                    done
                    [ "$_dw_n" -gt 0 ] || DP_WRITES+=("") ;;
```

Each line is load-bearing:

- `read -a` splits without pathname expansion, so `tools/*` stays one field and meets the glob
  refusal at `tools/unattended/unattended.sh:14512`. An unquoted `$1` would expand it.
- `IFS` is pinned on the `read` command alone. A tracked `.unattended.conf` is sourced into this
  shell and could otherwise move the split.
- `-d ''` reads past newlines, so a newline-joined value splits as a space-joined one does. `read`
  returns 1 at end of input with the array filled, so `|| :` keeps the status clean.
- A value that yields no field, such as `""` or `"  "`, appends one empty path. A `--writes` that
  consumed nothing appends one empty path too. Both then refuse at
  `tools/unattended/unattended.sh:14504` with the existing empty-path message, which today's
  `--writes ""` arm already asserts (`tools/unattended/unattended.test.sh:9074`).
- The stop test reads a leading `--`, so `--writes a --pass X` still parses `--pass`. A first value
  that starts with `--` is never taken as a path. Today `--writes --pass X` declares the path
  `--pass` and refuses `X` with check 14.
- `set -u` is on (`tools/unattended/unattended.sh:59`). An empty array expanded as `"${_dw[@]}"` is
  legal there on bash 4.4 and later, and the `-eq 0` branch never expands it anyway.

One comment line above the arm states the rule. Check 26 reads `--<name>` tokens from non-comment
lines of the argv region only (`tools/unattended/check-unattended.sh:342-346`, pattern
`--[a-z][a-z0-9-]*`), so `--*)` adds no flag to its join.

The candidate arm was run against a scratch copy of the driver, outside the repository, with the probe
below. It printed `arg[a] arg[b] arg[c]` for `--writes a b c`, for `--writes "a b" --writes c` and for
a tab and newline-joined value. It printed one `arg[two\rwords/x.sh]` for a carriage-return value,
one `arg[]` for each of `""`, `"  "`, a trailing `--writes` and `--writes --pass TOOL-tX-2`, and
`arg[a*]` unexpanded.

### The whitespace refusal

The refusal at `tools/unattended/unattended.sh:14515` matches `[[:space:]]`, which is wider than the
three bytes S1 splits on. It stays live for a carriage return, a vertical tab and a form feed, so it is
not a dead branch left reading as coverage. The comment at `:14500-14501` is rewritten to say that the
argument loop splits space, tab and newline and this refusal catches the rest. The suite arms at
`tools/unattended/unattended.test.sh:9072-9073` pass `'two words/x.sh'` and `'spells · separator.sh'`.
After S1 those values split and no longer reach the refusal, so both arms are replaced by one arm
passing `$'two\rwords/x.sh'`, which asserts the same message.

### The probe

`$SCRATCH` is the run's scratch directory. The probe sources the driver, which defines everything and
returns (`tools/unattended/unattended.sh:15256`), stubs `verb_dispatch` to print what the argument
loop hands it, and calls `main` in a subshell, the form the sourced-driver guard names. Run from the
repository root, it reads the real `.unattended.conf` and writes nothing.

```bash
# $SCRATCH/sd1probe.sh — run as: GOV_RUNLOG=0 bash $SCRATCH/sd1probe.sh <driver argv>
source tools/unattended/unattended.sh
verb_dispatch() { printf 'arg[%s]\n' "$@"; }
( load_driver_conf && main "$@" ); echo "rc=$?"
```

### The suite arms

They sit in region 4, beside the arms they replace, on a fresh `build_specced_tree` and preflight as
the M1 block at `tools/unattended/unattended.test.sh:9047` builds:

```bash
# ---- TOOL-aSmoothedDispatch-1: one --writes takes every path up to the next flag, and splits a
# ---- whitespace-joined value; a carriage return is not split and still meets the refusal.
build_specced_tree; run --preflight tRun --keepalive-id k1 >/dev/null
out=$(run --dispatch tRun --pass ARCH-tRun-1 --writes work/one work/two work/three)
hit  "$out" "ARCH-tRun-1 · work/one work/two work/three"
miss "$out" "unknown argument"
out=$(run --dispatch tRun --pass ARCH-tRun-1 --writes "work/four work/five")
hit  "$out" "ARCH-tRun-1 · work/four work/five"
miss "$out" "containing whitespace"
hit "$(run --dispatch tRun --pass ARCH-tRun-1 --writes $'two\rwords/x.sh')" "--dispatch was given a --writes path containing whitespace, which the declaration's own field separator cannot carry, so the leg would split it into paths nobody declared:"
```

A second dispatch of one unit at one anchor is legal and parks its own row, as the arm at
`tools/unattended/unattended.test.sh:9000-9005` shows. The `dispatch declared` line prints
`<anchor> <unit> · <paths>` (`tools/unattended/unattended.sh:14676`).

The block holds 5 assertions and removes 2, so the net is +3. The builder counts off the block's own
lines as written, and adds that net to the values it finds at `FLOOR_ASSERTIONS`
(`tools/unattended/unattended.test.sh:19086`) and `FLOOR_SHARD_4` (`:19295`), with a dated `RAISED`
comment beside each. Units 2, 3 and 4 of this build move the same pins, so no value is written blind.

### The documents

- Header line `tools/unattended/unattended.sh:20` becomes
  `#   unattended.sh --dispatch <slug> --pass <id> --writes <path> [<path> ...] [--writes <path> ...]`.
- `tools/unattended/VERBS.template.md:220` says a REPEATABLE `--writes <path>`, "one path per
  occurrence". It becomes: `--writes` takes every path up to the next flag, a whitespace-joined value
  splits into its paths, and the flag may repeat.
- `tools/unattended/VERBS.template.md:765` shows `--writes <path> --writes <path>`, "one path per
  `--writes`". It becomes `--writes <path> <path>`, with the same sentence.
- `memory/guides/UNATTENDED-VERBS.md` is the byte copy the kit's adopter writes
  (`tools/unattended/adopt-unattended.sh:772-774`). The builder writes the same bytes there.

### Inventory

Two shell variables, `_dw` and `_dw_n`, both in the argument loop. `.lexicon.conf` declares no cell
for shell variables, only `sh.function`, and this unit mints no function.

### Files touched (estimate)

`tools/unattended/unattended.sh`
`tools/unattended/unattended.test.sh`
`tools/unattended/VERBS.template.md`
`memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- Splitting in `verb_dispatch` instead of the argument loop. Rejected because a bare second path
  never reaches `verb_dispatch`: the loop refuses it with check 14 first.
- Splitting on the whole `[[:space:]]` class and deleting the whitespace refusal. Rejected because
  `IFS` cannot name every locale's space class, so the refusal would still be the only guard for the
  rest, and a deleted guard would let those bytes reach the row.
- Unquoted word splitting, `DP_WRITES+=($1)`. Rejected because it glob-expands, so `tools/*` would
  become every entry under `tools/` and bypass the glob refusal.

## 5. Production-readiness checklist

- security — the write boundary stays `verb_dispatch`'s per-path refusals
  (`tools/unattended/unattended.sh:14502-14523`), unchanged. Every field S1 produces is a token free
  of space, tab and newline, which one `--writes <field>` could already pass, so no new input reaches
  the row.
- perf / scale — one `read` builtin per consumed value. No fork, no subshell.
- error / empty / loading states — an empty or all-whitespace value, and a `--writes` with no value,
  each meet the existing empty-path refusal.
- observability — the `dispatch declared` line already prints every declared path, so a split the
  agent did not intend is visible in the verb's own output.
- risks — a path that really holds a space is now declared as two paths instead of refused. The pass's
  commit then stages a path its declaration does not cover, and `--check-commit` refuses it at
  `tools/unattended/unattended.sh:14269`. That is one step later than today, and no such path is
  declarable either way.
- testing — the suite arms §7 declares, observed RED and GREEN by the main loop at the close, and the
  probes of §6, which a pass can run.
- migration — none: every argv that dispatched before dispatches the same row after.
- user docs — the verb carrier's two sentences and the header usage line, which `usage` renders. No
  `help/` page names `--dispatch`, grepped at `ae6735c1`.

## 6. Acceptance criteria

Each probe is §4's `$SCRATCH/sd1probe.sh`, run from the repository root with `GOV_RUNLOG=0`. A pass
runs no suite, and no probe here runs a gate.

- **AC1** — When `GOV_RUNLOG=0 bash $SCRATCH/sd1probe.sh --dispatch tX --pass TOOL-tX-1 --writes a b c`
  runs, it prints `arg[tX]`, `arg[TOOL-tX-1]`, `arg[a]`, `arg[b]`, `arg[c]` and `rc=0`. At the close
  the driver suite reads the arm asserting `ARCH-tRun-1 · work/one work/two work/three` green.
  Red when: the arm takes one value, as at `ae6735c1`, where the probe prints
  `UNATTENDED check 14 FAILED` naming `b`, then `rc=1`.
- **AC2** — When the probe runs with `--writes "a b" --writes c`, and again with one value holding
  `a`, a tab, `b`, a newline and `c`, each run prints `arg[a]`, `arg[b]` and `arg[c]` after the slug and
  the unit. At the close the driver suite reads the arm asserting
  `ARCH-tRun-1 · work/four work/five` green.
  Red when: a whitespace-joined value stays one path, as at `ae6735c1`, where the first run prints
  `arg[a b]`.
- **AC3** — When the probe runs with `--writes ""`, with `--writes "  "`, with `--writes` last in argv,
  and with `--writes --pass TOOL-tX-2`, each run prints exactly one `arg[]` after the unit, and the
  last prints `arg[TOOL-tX-2]` as the unit. The existing `--writes ''` suite arm stays green.
  Red when: a value with no field contributes no path, so the run prints no `arg[]` and the
  empty-path refusal is skipped, or a leading `--` is taken as a path, as at `ae6735c1`, where the last
  run refuses with check 14 naming `TOOL-tX-2`.
- **AC4** — When the probe runs with `--writes $'two\rwords/x.sh'`, it prints exactly three `arg[`
  lines, the third holding the carriage return. When it runs with `--writes 'tools/*'`, it prints
  `arg[tools/*]` and no other path. At the close the driver suite reads the carriage-return arm
  asserting `containing whitespace` green.
  Red when: the split covers every `[[:space:]]` byte, so the carriage-return value splits and the
  refusal is unreachable, or the split expands globs, so `tools/*` prints one `arg[` per entry.
- **AC5** — When `grep -c 'one path per' tools/unattended/VERBS.template.md` runs it prints 0, when
  `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` runs it exits 0, and when
  `grep -cF -- '--writes <path> [<path> ...] [--writes <path> ...]' tools/unattended/unattended.sh`
  runs it prints 1.
  Red when: the carrier still states one path per flag, as at `ae6735c1`, where the first grep prints
  2, or only one copy of the carrier moved.
- **AC6** — When `grep -c 'TOOL-aSmoothedDispatch-1' tools/unattended/unattended.test.sh` runs it
  prints at least 1, and the command below prints 0.

  ```bash
  grep -cF -- "--writes 'two words/x.sh'" tools/unattended/unattended.test.sh
  ```

  Red when: the old space-holding arms stay, as at `ae6735c1`, where the second grep prints 1. After
  S1 that arm splits its value and no longer meets the refusal, so it reds the suite.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `memory hygiene` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC4 · the five region-4 assertions, staged by restoring the one-value `--writes)` arm, where the first dispatch refuses with check 14 · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_4` raised by the net 3

`tier2-review self-test` is owed because its guard names `tools/unattended/unattended.sh`, and the two
`recall floor` legs because their `memory/` guard covers the verb carrier's copy. The
`unattended skill wiring` leg holds the two carrier copies equal, and `harness arms` reads the
whitespace refusal's new arm. This spec's author may run only `memory hygiene` and the lexicon, so
every other verdict is the main loop's at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft from the brief
  `2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief`, item 1, grounded at `ae6735c1`.
- rev-2 · 2026-11-10 · AC6 · its second grep moves out of inline backticks into an indented fenced
  block inside the bullet, so the spec-token paths join no longer grades `words/x.sh'"` as an
  untracked path. The command, its expected 0 and the criterion's meaning are unchanged. Per the
  revision brief `2026-11-10-prompt-TOOL-aSmoothedDispatch-1-token-fix`.

## 10. Reuse audit

The seam is the `--writes)` arm of the driver's argument loop (`tools/unattended/unattended.sh:15091`)
and the `DP_WRITES` array it fills, extended in place. `verb_dispatch` and its per-path refusals are
reused unchanged. `python tools/codebase-map/reuse_lookup.py "a repeatable flag takes several values up
to the next flag"` ranked generic name stems only, `check_verb_flag` among them, and none splits or
consumes values, so no existing seam fits beyond the arm itself. The `--plan` arm's sub-loop
(`tools/unattended/unattended.sh:15157-15166`) is the precedent for consuming arguments up to the next
`--` token, and S1 takes that shape. Recall returned the dUnstalledConvoy round-1 review and
`TOOL-dUnstalledConvoy-9`, which added the whitespace refusal because the row field is space-delimited.
That is why S3 keeps the refusal. It also returned a dFairHearing builder return that hit check 14 by
passing several paths to one `--writes`, which is the refusal this unit removes. No hit disagreed with
source.

Recall terms used: `python tools/memory-recall/query.py "how does dispatch parse writes paths, and why is whitespace in a writes path refused" --terms "dispatch writes declaration whitespace refusal argument loop DP_WRITES check 49 field separator path"`
