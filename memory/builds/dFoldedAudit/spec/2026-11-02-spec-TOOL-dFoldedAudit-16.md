# TOOL-dFoldedAudit-16 — the flagged bar's own reds cleared: the fork-site registry and the armed-cutoff pin

**Status:** CLOSED · rev-2 · 2026-11-02 · node d · Tier-2 · base 74274869 · streams tooling · order 160

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dFoldedAudit-16-1-first-bar.md](../build/2026-11-02-build-TOOL-dFoldedAudit-16-1-first-bar.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-16-2-spec-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-16-2-spec-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-16-3-builder-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-16-3-builder-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-16-4-builder-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-16-4-builder-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-16-ledger.md](../build/2026-11-02-build-TOOL-dFoldedAudit-16-ledger.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-16-1-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-16-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-16-2-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-16-2-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-16-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-16-build-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-16-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-16-fix-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-16-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-16-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Turn green the two legs `2026-11-02-build-TOOL-dFoldedAudit-16-1-first-bar.md` attributes to this
build. Every fork site the build added moves to its no-fork form, so the registry holds its counts. The
drift pin rises to the two cutoffs the build arms, with its reason written where the ratchet reads it.
No behaviour moves.

| Brief item | Leg | Scope |
|---|---|---|
| 1 | `shell hygiene (a fork spent on builtin work)` | S1, S2, S3, S4 |
| 2 | `drift-audit records` | S5 |
| 3 | both, as criteria | AC1 and AC8, with the direct checks AC2 to AC7 and AC9 |

## 2. Scope (IN)

- **S1** — The driver's two `pure-fn-subst` sites this build added. `review_exit_note` leaves its sentence
  in the fixed global `_exitnote` and still prints it. The two `folds` call sites read the global and
  fork nothing. The row returns to its registered 41. Observed by AC1, AC2 and AC3.
- **S2** — The driver suite's nine sites. Seven `$(cat file)` reads become `$(<file)`, and two
  `$(printf …)` values are built with `printf -v`. `cat-file` returns to 17 and `printf-subst` to 23.
  Observed by AC1 and AC4.
- **S3** — The harness suite's two sites. `run_strict_fa3` builds its runners object with `printf -v`
  into a local. FA12's no-THROW assertion becomes a `hasnt_` over the output with a newline in front.
  `printf-subst` returns to 66 and `var-pipe` to 62. Observed by AC1, AC5 and AC6.
- **S4** — No registry row moves. No site this build added has to keep its substitution, so this unit
  raises no row, and §4 names no raise. Observed by AC7.
- **S5** — The `cutoff_keys_armed` pin in `tools/drift-audit/drift_signals.py` rises from 36 to 38.
  History lines above it name `SPEC_SUPERSEDE_CUTOFF` (`TOOL-dFoldedAudit-4`) and `SPEC_FOLD_CUTOFF`
  (`TOOL-dFoldedAudit-7`, armed at the close), the decision row `TOOL-dFoldedAudit-16`, and the two
  comparisons the ratchet draws. Observed by AC8 and AC9.

## 3. Non-goals (OUT)

- Every other leg the first bar flagged. The record reads them as INHERITED, HOST or pending, and none
  is this build's.
- The two `review_exit_note` substitutions at BASE, at `tools/unattended/unattended.sh:13020-13021`. The
  registry row's reason carries them as `review_exit_note×2`, and that reason stays true. Draining them
  is the follow-up unit that row names.
- Any row of `memory/project/spawn-idiom-sites.txt`, raised or lowered.
- Any behaviour, sentence or exit status of the driver, either suite or the drift report.
- `memory/DECISIONS.md`. The main loop has already landed the row this unit cites.
- The merge of `origin/main` and the pin value it settles. The Edges below say why.
- A kit version move, which the lander mints at landing (`tools/push-main.sh:26-31`).

### Edges

- **consumes-from** external — the decision row `TOOL-dFoldedAudit-16` at `memory/DECISIONS.md:244`,
  which the main loop landed first; without it the pin's history line cites a decision no record holds
- **hands-off** external — the merge of `origin/main`, whose `tools/drift-audit/drift_signals.py:354`
  pins 37 for `SPEC_AC_ORDER_CUTOFF` (`TOOL-dSafePassage-34`). The merged tree arms 38 keys before the
  close and 39 after it, so that merge's resolution sets the pin to 39 under a `37 -> 39` line

## 4. Design

Line numbers are this tree's at `0e3c26cf`, PINNED 2026-11-02. Each site is also named by its
function or arm, so a builder finds it after a line moves.

### The five rows, attributed

The leg could not be run by this pass, and scratch-guard refuses it to a role agent. The attribution
comes from the scanner's own functions, `scan_spawn_file` and `check_spawn_substitution` in
`tools/gate-lint/sh_hygiene.py:790-839`, over the blobs at BASE `74274869` and at `0e3c26cf`, with
`lib-unattended.sh` resolved as `scan_spawn_tree` resolves it (`:877-884`). With these edits applied
to in-memory copies, the same functions measure every row at its registered count. Both readings were
PINNED on 2026-11-02.

| File | Row | Registered | At `0e3c26cf` | The sites this build added |
|---|---|---|---|---|
| `tools/unattended/unattended.sh` | `pure-fn-subst` | 41 | 43 | `:13026`, `:13027` |
| `tools/unattended/unattended.test.sh` | `cat-file` | 17 | 24 | `:2441`, `:2697`, `:2708`, `:2710`, `:2713`, `:2954`, `:2965` |
| `tools/unattended/unattended.test.sh` | `printf-subst` | 23 | 25 | `:2716`, `:2928` |
| `tools/workflows/unattended-build.test.sh` | `printf-subst` | 66 | 67 | `:3061` |
| `tools/workflows/unattended-build.test.sh` | `var-pipe` | 62 | 63 | `:3334` |

The driver's only moved callee is `review_exit_note`, from 2 sites at BASE to 4. Every other callee
this build added runs `git`, `awk` or a nested substitution, so the scanner grades it impure and it is
no site. The driver suite's `var-pipe` row reads its registered 20, because the three sites it gained
stand in for three this build rewrote, in the `--plan --paths` arms near `:3814-3816`.

`origin/main` arms 37 keys and carries neither of this build's two, measured with `parse_conf_text`
over its tracked root confs (PINNED 2026-11-02 at `8a5328a9`). That is the figure §3's hands-off
edge rests on.

### S1 — the driver

The seam is the fixed-global convention at `tools/unattended/unattended.sh:1414-1421`. A reader leaves
its answer in a global and still prints it, so a hot caller writes `f … >/dev/null; v=$_global`.
`runmd_of`, `readme_of` and `fact` follow it.

`review_exit_note` at `:12698` gains that shape. Each of its four arms assigns `_exitnote`, and one
`printf '%s' "$_exitnote"` follows the `esac`. Every arm assigns, the unreachable `*)` arm included, so
no call leaves an earlier answer in the global. The body still runs only builtins, so the scanner keeps
grading it pure, and the two BASE callers at `:13020-13021` keep their substitution and their count. The
comment above the function gains one sentence: it leaves its sentence in `_exitnote` too, the
convention `runmd_of` follows, so the `folds` callers read it with no fork (`TOOL-dFoldedAudit-16`).

The two arms of the `folds` case at `:13026-13027` become:

```bash
      fold)    review_exit_note spec-fold >/dev/null; exitnote=$_exitnote ;;
      promote) review_exit_note spec-promote >/dev/null; exitnote="$_exitnote; this exit owes at least $owe new unit(s), the floor check 2 grades" ;;
```

No checker reads either spelling. `grep -rn review_exit_note tools/` names only the driver and one
comment at `tools/unattended/unattended.test.sh:8146`.

### S2 — the driver suite

- The seven reads at `:2441`, `:2697`, `:2708`, `:2710`, `:2713`, `:2954` and `:2965` spell
  `$(<"$_sw_tmp/err")` and `$(<"$_fc_r/$_fc_f")`. A `$(<…)` with no other redirection inside is a near
  miss of `redirected-read` and no site (`sh_hygiene.py:803-804`).
- `:2928` sets the tab with `printf -v _sd_tab '\t'`.
- `:2716` takes `printf -v _fc_embedded 'FIX-dFix-1\nround 9 · subject z · audited FIX-dFix-1'` on the
  line above it, and passes `--audited "$_fc_embedded"`.

`$(<file)` strips trailing newlines exactly as `$(cat file)` does. No `printf` format here ends in a
newline, so `printf -v` writes the bytes the substitution produced, and every value keeps its bytes.

### S3 — the harness suite

The seam for `:3061` is the line above it. `build_dispose_fa3` at `:3056` already builds `_fa3_d` with
`printf -v`. `run_strict_fa3` becomes:

```bash
run_strict_fa3() { local recexit='' runners; [ -z "${3:-}" ] || recexit="\"record-exit\":$3,"
  printf -v runners '{"spec-write":%s,"workflow":%s,%s"record":%s,"dispose":%s}' "$SPEC_OK" "$_fa3_review" "$recexit" "$2" "$_fa3_d"
  RUN_WF_SCHEMA=strict run_wf "$1" "$runners"; }
```

The seam for `:3334` is the suite's own `hasnt_` at `:154`. The line becomes:

```bash
hasnt_ "FA12 AC1 ...and the run returns" $'\n'"$o" $'\nTHROW '
```

`grep -c '^THROW '` counted lines that open with `THROW `. The leading newline makes the first line one
of those too, and a CR before a newline does not move the match. Both forms count one assertion, so no
assertion floor moves.

### S4 — the registry

No row is raised. The brief's raise applies where a site must keep its substitution, as the driver row's
reason says check 28 requires of `declared_list` and `declared_scalar`. No site above calls either.

### S5 — the drift pin

The ratchet compares the pin with its value at the report's base ref. `resolve_base_ref`
(`tools/drift-audit/drift_report.py:3667`) answers `refs/remotes/origin/main` first, and there the pin
reads 37 (`8a5328a9`, PINNED 2026-11-02). That commit is not on this branch, which reads 36. A raise
needs a comment naming `<old> -> <new>` within `RATCHET_LOOKBACK` lines above the pin
(`drift_report.py:268-275`, `drift_signals.py:435`, 14). So a `36 -> 38` line alone still prints
`RATCHET WEAKENED` against that base, and the history line states both comparisons.

These three lines follow `tools/drift-audit/drift_signals.py:350`, and `:351` reads
`"cutoff_keys_armed": 38,`:

```python
    # 36 -> 38 at dFoldedAudit's close, 2026-11-02, under decision TOOL-dFoldedAudit-16: TOOL-dFoldedAudit-4
    # arms SPEC_SUPERSEDE_CUTOFF in .memory-tree.conf and TOOL-dFoldedAudit-7 SPEC_FOLD_CUTOFF in .unattended.conf,
    # armed at the close; no key stopped being armed. origin/main reads 37 for TOOL-dSafePassage-34, so 37 -> 38 there.
```

The branch measures 37 today, so the pin reads `ok (pin 38, drain it)` until the close arms the second
key, and then it reads 38 against 38.

### The probes the criteria run

The builder writes both probes under the run's scratch. Probe N reads a driver's text on stdin:

```bash
# notes.sh — each disposition's sentence, and a MISMATCH on stderr where `_exitnote` disagrees
eval "$(sed -n '/^review_exit_note() {/,/^}/p')"
for d in promote closing spec-fold spec-promote nonsense; do
  printf '%s\n' "$(review_exit_note "$d")"
  _exitnote=stale; review_exit_note "$d" >/dev/null
  [ "$_exitnote" = "$(review_exit_note "$d")" ] || echo "MISMATCH $d" >&2
done
```

Probe T evaluates the harness suite's own helper:

```bash
# throw.sh — three outputs, as FA12's assertion reads them
eval "$(sed -n '/^hasnt_(){/p' tools/workflows/unattended-build.test.sh)"; n=0; st=0
o=$'agent:x\nTHROW boom';    hasnt_ "second line" $'\n'"$o" $'\nTHROW '
o=$'THROW boom\nRESULT {}';  hasnt_ "first line" $'\n'"$o" $'\nTHROW '
o=$'note: a THROW mid-line'; hasnt_ "mid-line" $'\n'"$o" $'\nTHROW '
```

Probe D reads the pin the way the ratchet does:

```bash
python - <<'EOF'
import sys
sys.path.insert(0, "tools/drift-audit")
import drift_report as d
text = open("tools/drift-audit/drift_signals.py", encoding="utf-8").read()
value, at = d._scalar_at(text, "cutoff_keys_armed")
print(value, d._justified(text, at, 37, 38, 14), d._justified(text, at, 36, 38, 14))
EOF
```

At `0e3c26cf`, probe D prints `36 False False`.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `_exitnote` | none, a global | none: no cell grades a variable |
| `_fc_embedded`, `runners` | none, a suite global and a local | none |

### Files touched (estimate)

`tools/unattended/unattended.sh`
`tools/unattended/unattended.test.sh`
`tools/workflows/unattended-build.test.sh`
`tools/drift-audit/drift_signals.py`

### Alternatives rejected

- **Raising the five rows.** The brief admits a raise only for a site that must keep its substitution.
  None of these has to, and a raise would carry forks the code does not need.
- **Converting the two BASE callers of `review_exit_note` as well.** That lowers the row to 39 and
  rewrites its reason. It is the drain the row names for a follow-up unit, and this unit clears this
  build's sites only.
- **A second, out-variable copy of `review_exit_note`.** Two functions would hold the same four
  sentences. The fixed-global convention keeps one function, read both ways.
- **Writing the pin as 39 now.** That is the merged tree's figure. On this branch it would leave a key
  of headroom no change has armed, and it contradicts the landed row's `36 -> 38`.

## 5. Production-readiness checklist

- **security** — N/A: no write path, input or surface moves.
- **perf / scale** — Each folds exit spends one fork fewer, and each suite site one fewer.
- **error / empty / loading states** — N/A: every value keeps its bytes, and `review_exit_note`'s
  unreachable arm still prints its sentence.
- **observability** — The drift row prints `ok (pin 38, drain it)` until the close arms the second key.
- **risks** — The merge of `origin/main` conflicts on the pin and its history lines, and the hands-off
  edge in §3 gives its resolution. A future arm of `review_exit_note` that skips `_exitnote` would leave
  a stale sentence for the `folds` caller, which probe N's `nonsense` row and its MISMATCH line catch.
- **testing** — Direct probes and greps only, with no gate or suite inside the pass. The two legs and the
  four guarded suites are the main loop's at the close.
- **migration** — N/A: no data or conf key moves.
- **user docs** — N/A: nothing under `help/` names a fork site or a drift pin, and no user-facing
  behaviour moves.

## 6. Acceptance criteria

`<parent>` is the commit the pass starts from. Probes N, T and D are §4's, written under the run's
scratch.

- **AC1** — When `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`
  runs, its output piped to
  `grep -E '^  tools/(unattended/unattended(\.test)?\.sh|workflows/unattended-build\.test\.sh):'`
  prints nothing. A finding line opens with two spaces and its path, while every green
  `sh-hygiene: registered —` line opens with the tool's name.
  permission: scratch-guard refuses this leg's argv to a role agent, so the main loop observes it at the
  close.
  Red when: any of the eleven sites keeps its fork, so its row reads one count above the registry.
- **AC2** — When `git show <parent>:tools/unattended/unattended.sh | bash notes.sh` and
  `bash notes.sh < tools/unattended/unattended.sh` each run, their stdout is byte-identical, five lines,
  and the second prints no `MISMATCH` on stderr.
  Red when: a sentence's bytes move, or an arm leaves `_exitnote` unassigned so it reads `stale`.
- **AC3** — When `grep -c 'exitnote="*$(review_exit_note spec-' tools/unattended/unattended.sh` runs it
  prints 0, and `grep -c '$(review_exit_note ' tools/unattended/unattended.sh` prints 2.
  figure: PINNED, 2 and 4 before the pass, measured at `0e3c26cf`.
  Red when: a `folds` caller keeps its substitution, or a BASE caller is converted beyond this scope.
- **AC4** — When `grep -c '$(cat "$_sw_tmp/err")\|$(cat "$_fc_r/$_fc_f")' tools/unattended/unattended.test.sh`
  runs it prints 0, and `grep -c '$(<"$_sw_tmp/err")\|$(<"$_fc_r/$_fc_f")'` over the same file prints 10:
  the seven reads S2 converts, and the three `_fc_bytes=$(<"$_fc_r/$_fc_f")` reads at `:2877`, `:3276`
  and `:3293` that an earlier unit wrote.
  Then `grep -c '_sd_tab=$(printf' tools/unattended/unattended.test.sh` and
  `grep -c "audited \"\$(printf 'FIX-dFix-1"` over the same file each print 0.
  figure: PINNED, 7, 3, 1 and 1 before the pass, measured at `0e3c26cf`.
  Red when: a read keeps `cat`, or a value is still built in a substitution.
- **AC5** — When `grep -c 'strict run_wf "$1" "$(printf' tools/workflows/unattended-build.test.sh` runs it
  prints 0, and `grep -c "grep -c '^THROW '"` over the same file prints 0.
  figure: PINNED, 1 and 1 before the pass, measured at `0e3c26cf`.
  Red when: either site keeps its fork.
- **AC6** — When `bash throw.sh` runs, it prints `FAIL second line` and `FAIL first line`, and it prints
  `ok   mid-line`. Those are the three answers `grep -c '^THROW '` gave as 1, 1 and 0.
  Red when: the leading newline is left out, so a THROW on the first line passes, or the match is
  unanchored, so a mid-line THROW fails.
- **AC7** — When `git diff --stat 74274869 -- memory/project/spawn-idiom-sites.txt` runs after the pass, it
  prints nothing.
  Red when: a row is raised or lowered to meet the scan, rather than a site converted.
- **AC8** — When `python tools/drift-audit/drift_report.py --check` runs, its stderr holds no line naming
  `cutoff_keys_armed`, neither the over-pin block nor a `RATCHET WEAKENED` line. Its table row for that
  signal reads `ok (pin 38`.
  permission: this is the `drift-audit records` leg's own read, so the main loop observes it at the close.
  fixture: the base ref is `refs/remotes/origin/main`, at `8a5328a9` with the pin at 37 when this was
  written. A fetch that moves it changes the comparison, and the leg reads whatever the ref holds then.
  Red when: the pin stays 36, so 37 reads over it, or the history names only `36 -> 38`, so the ratchet
  reads an unjustified `37 -> 38`.
- **AC9** — When probe D runs with `python -` from the repository root, it prints `38 True True`, and
  `grep -n -B3 '"cutoff_keys_armed": 38,' tools/drift-audit/drift_signals.py` shows lines naming
  `SPEC_SUPERSEDE_CUTOFF`, `SPEC_FOLD_CUTOFF` and `TOOL-dFoldedAudit-16`.
  Red when: the history line sits outside the 14-line lookback, or misspells either comparison.

## 7. Gates

`shell hygiene (a fork spent on builtin work)` · `drift-audit records` · `drift-audit selftest` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `unattended kit gate`

The four `self-test` legs and `drift-audit selftest` are owed by the guard join on
`tools/workflows/` and `tools/drift-audit/`. `unattended kit gate` reads the driver. No arm is added or
moved: the two rewritten assertions keep their count and their red case, so this unit has no
`New arm:` line.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the first bar's attribution, the promotion notes and the
  scanner's own reading of the five rows.
- rev-2 · 2026-11-02 · AC4's `$(<…)` grep reads 10 after the pass and 3 before it, as the builder's
  DIVERGENCE return measured: three `_fc_bytes` reads at `:2877`, `:3276` and `:3293` predate this unit.
  No other criterion and no §4 text moves.

## 10. Reuse audit

The seams are the fixed-global convention at `tools/unattended/unattended.sh:1414-1421`, which
`runmd_of`, `readme_of` and `fact` follow, for S1. For S3 they are `build_dispose_fa3`'s `printf -v` at
`tools/workflows/unattended-build.test.sh:3056` and the suite's `hasnt_` at `:154`. For S5 it is the
`RATCHETS` history above the pin at `tools/drift-audit/drift_signals.py:337-350`.
`TOOL-dTrueNorth-27`'s §4 is the precedent, and it cleared the same two legs the same way.
`reuse_lookup.py` on the out-variable behaviour ranked only name-stem hits (`read`, `read_text`,
`read_conf`), and none of them leaves an answer in a global. So the in-file convention is the seam, and
no existing seam fits better. Recall returned `TOOL-dTrueNorth-28`'s pin raise and the `TOOL-dTrueNorth-27`
brief, the same class of repair.

Reuse probe used: `python tools/codebase-map/reuse_lookup.py "a pure shell function leaves its answer in a global so a caller reads it with no fork"`.
Recall terms used: `python tools/memory-recall/query.py "how is a fork-site registry row lowered or raised and how is an armed cutoff pin raised with its reason" --terms "spawn-idiom-sites pure-fn-subst printf-subst cat-file var-pipe printf -v out-variable cutoff_keys_armed pin ratchet raise"`.
