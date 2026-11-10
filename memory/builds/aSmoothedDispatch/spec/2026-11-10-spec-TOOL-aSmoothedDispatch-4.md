# TOOL-aSmoothedDispatch-4 — `--dispatch`'s spec-token check grades the dispatching build's specs, and skips when its inputs match the last admitted check

**Status:** CLOSED · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md) | research | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 |
| [2026-11-10-review-TOOL-aSmoothedDispatch-1-closing-diff-round1.md](../reviews/2026-11-10-review-TOOL-aSmoothedDispatch-1-closing-diff-round1.md) | diff-review | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7 |

<!-- /gen:spec-records -->

## 1. Goal

`verb_dispatch` runs the declared spec-token checker over the whole live tree and refuses on any
non-zero exit, so a red in another build's spec blocks this build, and every re-dispatch pays a
full checker run even when nothing it reads has moved. This unit refuses only on reds the
dispatching build owns, and skips the run when its inputs match the last check it admitted. The
bar's whole-tree `spec tokens (a spec's own names resolve)` leg still grades every build.

## 2. Scope (IN)

- **S1** — A verdict function, `check_spec_token_hits`, reads the checker's exit status and stdout
  and admits only when the checker exited 0, or when the checker's own counted reds are all hits
  in another build's folder. Any red it cannot prove foreign refuses as today. Observed by AC1, AC2
  and AC3.
- **S2** — A cache: `derive_spec_token_key` derives a key over every input the checker reads, and
  `run_spec_token_check` skips the checker when the key matches the one recorded for this slug.
  A key is recorded only when the check admits. Observed by AC4, AC5 and AC6.
- **S3** — With no working-tree fingerprint, the cache is off for that call: the check announces it
  and runs the checker, and nothing is recorded. Observed by AC7.
- **S4** — `verb_dispatch` calls `run_spec_token_check` in place of the inline block, which moves
  into it with its existing refusal texts and announced skip unchanged. Observed by AC8.
- **S5** — The verbs guide and the protocol's `SPEC_TOKENS_CLI` row state the new rule, in both the
  kit template and its dogfood copy, and the protocol does not grow past its size ceiling. Observed
  by AC9.

## 3. Non-goals (OUT)

- No change to `tools/check-spec-tokens.py`. No `--build` flag and no output change: the driver
  filters the output the checker already prints.
- No change to the bar's `spec tokens (a spec's own names resolve)` leg, which stays whole-tree, and
  none to the token check in the build harness's commit stage (`tools/workflows/unattended-build.js`).
- No cached RED. A refusal re-runs the checker every time, because a refusal is what the operator is
  about to fix.
- No key that leaves out the run-state file. The checker's packet join reads run-state phases, so a
  parallel group's second dispatch, which follows the first one's row, re-runs the checker. That is
  a correct miss, not a defect.
- No reordering of `verb_dispatch`'s refusals, and no change to any refusal other than the
  spec-token one.
- No kit version bump by hand. The lander's `mint` moves it.
- None of units 1, 2, 3, 5 or 6's mechanisms.

### Edges

none

## 4. Design

### What the code does today, read at `ae6735c1`

- `verb_dispatch` opens at `tools/unattended/unattended.sh:14276`. The spec-token block is
  `tools/unattended/unattended.sh:14325-14341`: it runs `run_bounded "$_stpy" "$SPEC_TOKENS_CLI"`
  and calls `fail 49` on any non-zero exit, quoting up to three `spec-tokens:` lines with the report
  lines filtered out.
- The `--writes` refusals run after that block: whitespace at `tools/unattended/unattended.sh:14515`,
  the run-state file at `tools/unattended/unattended.sh:14535` and sibling overlap at
  `tools/unattended/unattended.sh:14632`. A refusal writes no row, so a re-dispatch after any of them
  re-runs the whole checker over an unchanged tree. That is the case the cache pays for.
- The checker prints each unwaived hit as `spec-tokens: <file> [<kind>] ` + backticked token
  (`tools/check-spec-tokens.py:1987`), each stale row as `spec-tokens: STALE ...`
  (`tools/check-spec-tokens.py:1989`), and on any red the summary
  `spec-tokens: <N> unwaived hit(s), <M> stale row(s)` (`tools/check-spec-tokens.py:1991`). N counts
  exactly the hit lines printed, because both read the one `live` list
  (`tools/check-spec-tokens.py:1865`).
- A hit's file field is a spec path for most joins, a packet path under the build's `prompts/` for
  the packet join, and for some carries findings a bare build name. A bare build name is not under
  any build folder, so S1 refuses on it as today.

### S1 — the verdict, `check_spec_token_hits <slug> <rc> <output>`

Status 0 admits and status 1 refuses. Stdout holds the lines the caller quotes, at most three.

1. `rc` 0 admits, quoting nothing.
2. Otherwise, take the summary line's N and M. With no summary line, refuse and quote today's tail.
   That is the checker that did not grade.
3. Read every hit line with `^spec-tokens: ([^ ]+) \[[a-z-]+\] `. A hit is OWN when its file starts
   with `$MEMORY_ROOT/builds/<slug>/`. It is FOREIGN when its file starts with
   `$MEMORY_ROOT/builds/` and is not own. The trailing slash keeps `tA` from matching `tAB`.
4. Admit only when OWN is 0, M is 0, N is above 0 and N equals the FOREIGN count, and quote the
   foreign lines. Otherwise refuse and quote the own lines first, falling back to today's tail.

Step 4 is a COUNTED proof, not the absence of an own line. A stale row, an unattributed hit, or a
hit line whose shape drifts away from the pattern leaves N above the foreign count, so it refuses.
That is deny-by-default: the only red that is waved through is one the checker itself counted and
the driver attributed to a named other build.

The admit note, printed by the caller:
`unattended: dispatch — the spec-token checker reds only in other builds' specs, which the bar's
whole-tree leg still grades, so this dispatch is admitted: <N> hit(s), first: <line>`.

### S2 — the key and the cache

`derive_spec_token_key <slug> <launcher>` prints a 40-hex key, or prints nothing and returns 1.
The key is `GIT hash-object --stdin` over five lines:

| line | what | why it is an input |
|---|---|---|
| 1 | the slug | S1's verdict depends on it |
| 2 | `$SPEC_TOKENS_CLI` | the program that runs |
| 3 | the resolved launcher | the interpreter that runs it |
| 4 | `GIT rev-parse HEAD` | the checker reads history through `git log` pickaxe on the conf |
| 5 | the working-tree fingerprint | every tracked byte and file name the checker reads |

Line 5 is `tools/run-gates/gate-fingerprint.sh`, run with no argument: its working-tree form
digests the HEAD tree, the sorted porcelain status and the blob of every dirty or untracked file.
It is resolved the way `print_drift_delta` resolves a sibling kit
(`tools/unattended/unattended.sh:1410-1424`): `resolve_kit_dir "$py" run-gates gate-fingerprint.sh
"$KIT_DIR"` (`tools/unattended/lib-unattended.sh:133`), then `bash "$ROOT/$d/gate-fingerprint.sh"`.
The script's own contract is that it prints nothing on any failure, and a caller must then take the
expensive path (`tools/run-gates/gate-fingerprint.sh:24-26`). An empty line 5 is S3.

The record is one file per slug in the kit's sidecar root,
`$(resolve_sidecar_dir)/spec-tokens.<slug>.key` (`tools/unattended/lib-unattended.sh:122`). That
root is the per-worktree git dir, so it is never in the working tree and never moves the
fingerprint. The slug passed `check_slug` at the top of
`verb_dispatch`, so it is safe in a file name.

`run_spec_token_check <slug>` holds the moved block and adds:

1. Resolve the launcher as today. Derive the key.
2. If a key exists and the slug's record holds it, print
   `unattended: dispatch — spec-token check skipped: its inputs match the check last admitted for
   <slug> (key <first 12 hex>)` and return 0.
3. If no key exists, print `unattended: dispatch — spec-token cache off: no run-gates
   gate-fingerprint.sh resolves in this install, or it printed no digest, so the checker runs`.
4. Run the checker. Call `check_spec_token_hits`. On refuse, call `fail 49` with today's message and
   the returned lines, and return 1. On admit with a red, print the admit note.
5. On admit with a key, `mkdir -p` the sidecar root and write the key with one `printf`. Read the
   record with `read -r` from the file, never with a command substitution. A failed write or read
   only costs a later miss, so neither refuses.

The key is derived BEFORE the checker runs and recorded after it admits, so a tree edited while the
checker ran is recorded under the key of the tree it read.

### What the cache does not check

- Whether the checker is deterministic over these inputs. The checker, `design_lib.py` and
  `tree_lib.py` read no clock, grepped at `ae6735c1`. Their one environment read is
  `tools/memory-tree/tree_lib.py:241`, which hands the environment through to git, so a git
  setting carried in the environment is not seen. The launcher path stands in for the interpreter,
  so a Python package upgraded in place under the same path is not seen either.
- Whether a skipped run would have printed the same foreign note. A skip prints the skip line only.
- Anything outside this worktree's git dir. A second worktree keeps its own record.

The fingerprint is over-sensitive by design: an untracked scratch file moves it. That costs a run
and never admits a tree nobody checked.

### Inventory

| identifier | kind | lexicon verb |
|---|---|---|
| `check_spec_token_hits` | sh function | check |
| `derive_spec_token_key` | sh function | derive |
| `run_spec_token_check` | sh function | run |
| `spec-tokens.<slug>.key` | sidecar file under the kit's sidecar root | — |

No conf key, no flag and no check number is minted. The refusal stays check 49.

### Docs

- `tools/unattended/VERBS.template.md:234-238`: the sentence that says the verb refuses when the
  checker exits non-zero becomes this. The verb refuses on any red but a hit in another build's
  spec, which it notes and admits because the bar's whole-tree leg still grades that build. It
  skips the run when its inputs match the last check it admitted for this build, keyed as S2 states.
  With no fingerprint it announces that the cache is off. The phrase
  `skips the run when its inputs match` is spelled as written. `memory/guides/UNATTENDED-VERBS.md`
  takes the identical edit, because the two files are byte-identical at `ae6735c1`.
- `tools/unattended/PROTOCOL.template.md:516`: `refusing the dispatch on a non-zero exit` becomes
  `refusing on any red but another build's`, one byte shorter. The file sits at its ceiling,
  67183 bytes (`tools/template-size-limits.txt:150`), so the row must not grow.
  `memory/guides/UNATTENDED-PROTOCOL.md` takes the identical edit.
- No `help/` page names `--dispatch`, grepped at `ae6735c1`.

### The pass probe, `$SCRATCH/sd4.sh`

`$SCRATCH` is the run's scratch directory, where the probe script is written. Run it from the root
of the worktree under build. It builds a fixture repository at `$TEMP/sd4`, a short path because a
clone under the scratch directory's long path fails on Windows. The fixture holds this repo's two
conf files. The probe sources the driver there and loads its conf as the suite does
(`tools/unattended/unattended.test.sh:664`, then `load_driver_conf`), overrides `SPEC_TOKENS_CLI`
with a stub, and calls the three functions directly. Sourcing and loading in such a fixture was
tried at `ae6735c1` while this spec was written: the conf loads, the fingerprint kit resolves to
`tools/run-gates`, and the sidecar root reads `.git/unattended`. The stub checker logs one line per
run under the fixture's git dir, so the log never moves the fingerprint.

```bash
set -u
G=$(pwd); R="$TEMP/sd4"; rm -rf "$R"; mkdir -p "$R/tools/run-gates"; cd "$R" || exit 2
git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
cp "$G/.unattended.conf" "$G/.memory-tree.conf" . && cp "$G/tools/run-gates/gate-fingerprint.sh" tools/run-gates/
printf 'import os,sys\nopen(os.environ["SD4_LOG"],"a").write("r\\n")\nsys.stdout.write(open(os.environ["SD4_OUT"]).read())\nsys.exit(int(os.environ["SD4_RC"]))\n' > stub.py
printf 'seed\n' > a.txt; git add -A; git commit -qm seed
. "$G/tools/unattended/unattended.sh" || exit 2
load_driver_conf || exit 2
export SD4_LOG="$R/.git/sd4.log" SD4_OUT="$R/.git/sd4.out" SD4_RC=0
: > "$SD4_LOG"; : > "$SD4_OUT"; SPEC_TOKENS_CLI=stub.py
runs() { local n; n=$(wc -l < "$SD4_LOG"); echo "${n// /}"; }
S='spec-tokens: %s unwaived hit(s), %s stale row(s)'
own='spec-tokens: memory/builds/tA/spec/2026-11-10-spec-T-tA-1.md [bar] `t` — w'
far='spec-tokens: memory/builds/tB/spec/2026-11-10-spec-T-tB-1.md [bar] `t` — w'
odd='spec-tokens: tools/x.md [packet] `tA` — w'
v() { check_spec_token_hits tA "$2" "$3" >/dev/null; echo "verdict $1 $?"; }
v clean 0 ''
v foreign 1 "$far"$'\n'"$(printf "$S" 1 0)"
v own 1 "$own"$'\n'"$(printf "$S" 1 0)"
v both 1 "$own"$'\n'"$far"$'\n'"$(printf "$S" 2 0)"
v stale 1 "$far"$'\n''spec-tokens: STALE WAIVER `x` — w'$'\n'"$(printf "$S" 1 1)"
v uncounted 1 "$far"$'\n'"$(printf "$S" 2 0)"
v unattributed 1 "$odd"$'\n'"$(printf "$S" 1 0)"
v nosummary 1 'spec-tokens: REFUSING — x'
run_spec_token_check tA >/dev/null; o=$(run_spec_token_check tA)
echo "cache unchanged runs $(runs) skipped $(grep -c 'spec-token check skipped' <<<"$o")"
printf 'e\n' >> a.txt; run_spec_token_check tA >/dev/null; echo "cache edited runs $(runs)"
: > b.txt; run_spec_token_check tA >/dev/null; echo "cache untracked runs $(runs)"
run_spec_token_check tB >/dev/null; echo "cache slug runs $(runs)"
git add -A; git commit -qm two; run_spec_token_check tA >/dev/null; echo "cache commit runs $(runs)"
printf 'r\n' >> a.txt; printf '%s\n' "$own" "$(printf "$S" 1 0)" > "$SD4_OUT"; SD4_RC=1
run_spec_token_check tA >/dev/null; run_spec_token_check tA >/dev/null; echo "cache refused runs $(runs)"
printf '%s\n' "$far" "$(printf "$S" 1 0)" > "$SD4_OUT"
o=$(run_spec_token_check tA); run_spec_token_check tA >/dev/null
echo "cache foreign runs $(runs) noted $(grep -c "other builds' specs" <<<"$o")"
rm tools/run-gates/gate-fingerprint.sh; SD4_RC=0; : > "$SD4_OUT"
o=$(run_spec_token_check tA; run_spec_token_check tA)
echo "cache off runs $(runs) said $(grep -c 'spec-token cache off' <<<"$o")"
```

The edits to `a.txt` before the refused step are there because the stub's output is not an input
to the key. A real checker's output is a function of the tree, so the probe moves the tree whenever
it moves the stub's verdict.

### Rollout

One pass, at order 4, after units 1 to 3 have built, because units 1, 2, 3, 4 and 6 all edit
`tools/unattended/unattended.sh`. The cited line numbers are at `ae6735c1` and move with those
units, so the builder finds each site by its text. The suite's `FLOOR_ASSERTIONS` moves by the
count of new assertions, and the close confirms it from a real run.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`

### Alternatives rejected

- **A `--build <slug>` flag on the checker.** Grading one build's specs makes every waiver row for
  another build's hit read STALE, and it starves the joins that read across builds, such as the
  carries join's crossbuild arm. `SPEC_TOKENS_CLI` is also declared, so an adopter's checker need not
  know the flag.
- **Admit whenever no own-build hit line is printed.** A stale row, an unattributed hit and a drifted
  line shape would all pass. S1's counted proof refuses all three.
- **Cache only an exit-0 run, as the brief's word "green" reads literally.** A tree carrying a
  standing foreign red would then never cache, and that is exactly the tree S1 admits. The build
  README's expected improvement is that `--dispatch` "re-checks only when its inputs move"
  (`memory/builds/aSmoothedDispatch/README.md:23`), with no exception for such a tree. So the cached
  fact is "this check admitted this build over these inputs", which is green for the dispatch.
- **Key on HEAD alone.** The cache would admit a dispatch over a spec edited since the last check.
- **A second working-tree digest written inline in the driver.** That is two answers to one
  question, which the fingerprint script's header names as the failure it exists to prevent.
- **Add run-gates to the kit's `requires`.** The cache is an optimisation, and S3 degrades to
  today's behaviour, so a hard dependency buys nothing.
- **Move the check below the cheaper refusals instead of caching.** It reorders every refusal the
  check now precedes, which no item asks for, and the brief asks for a cache.

## 5. Production-readiness checklist

- security — the record is a file under the per-worktree git dir that only the driver writes. A
  forged record can only skip a check the bar still runs. S1 is deny-by-default: only a counted red
  attributed to a named other build is admitted.
- perf / scale — a hit costs one Python start to resolve the kit, one porcelain status and one
  `git hash-object` per dirty file. A miss adds that to today's full checker run. The README's
  journal figures, 947 minutes over 287 refusals, put an average run near 3.3 minutes (DERIVED from
  `memory/builds/aSmoothedDispatch/README.md`).
- error / empty / loading states — no fingerprint turns the cache off with an announcement. A failed
  record write or read costs a miss. A checker that did not grade refuses as today.
- observability — the skip line names the key prefix, the admit note names the count and the first
  foreign hit, and a refusal quotes own hits first.
- risks — a skipped check prints no foreign note, so a reader sees that build's red only on the
  first dispatch and at the bar. A Python package upgraded in place under one launcher path is
  invisible to the key.
- testing — the probe above for each pass, and the driver suite's new arms, observed RED then GREEN
  at the close.
- migration — none. No record exists before the first admitted check, and the first dispatch after
  install misses.
- user docs — the verbs guide and the protocol row, both copies, per the Docs sub-head.

## 6. Acceptance criteria

Each probe line below comes from one run of `bash "$SCRATCH/sd4.sh"`, the Design section's fenced
block, removed after the pass. At the close the driver suite observes the dispatch-level behaviour
with the real checker.

- **AC1** — When `bash "$SCRATCH/sd4.sh"` runs, it prints `verdict clean 0` and
  `verdict foreign 0`. At the close the driver suite reads a fixture whose only red is a live spec of a second build `tOther`
  backticking the flagged bar: `--dispatch tRun` prints the admit note and `dispatch declared`.
  Red when: the verdict refuses on any non-zero exit whatever build the hit sits in, as at
  `ae6735c1`, where that dispatch is refused with check 49.
- **AC2** — When `bash "$SCRATCH/sd4.sh"` runs, it prints `verdict own 1` and `verdict both 1`.
  At the close the suite's existing refusal arm, whose live spec is `tRun`'s own, still reads
  `--dispatch refuses: the declared spec-token checker reds over the live tree`.
  Red when: an own-build hit is admitted because a foreign hit sits beside it.
- **AC3** — When `bash "$SCRATCH/sd4.sh"` runs, it prints `verdict stale 1`, `verdict uncounted 1`,
  `verdict unattributed 1` and `verdict nosummary 1`.
  Red when: the verdict admits on the absence of an own line rather than on N equalling the foreign
  count with no stale row.
- **AC4** — When `bash "$SCRATCH/sd4.sh"` runs, it prints `cache unchanged runs 1 skipped 1`.
  At the close the driver suite dispatches `tRun` twice over an unchanged tree, each time refused by a later
  `--writes` check, and the second call prints `spec-token check skipped` and no checker report line.
  Red when: the key is never recorded or never compared, and the run count reads 2.
- **AC5** — When `bash "$SCRATCH/sd4.sh"` runs, it prints `cache edited runs 2`,
  `cache untracked runs 3`, `cache slug runs 4` and `cache commit runs 5`.
  Red when: the key leaves out the working tree, the slug or HEAD, so that step skips and its line
  reads fewer runs than stated.
- **AC6** — When `bash "$SCRATCH/sd4.sh"` runs, it prints `cache refused runs 7` and
  `cache foreign runs 8 noted 1`.
  Red when: a refusal records its key, so the second refused call skips and the count reads 6, or a
  foreign admission records nothing and the count reads 9.
- **AC7** — When `bash "$SCRATCH/sd4.sh"` runs, it prints `cache off runs 10 said 2`.
  Red when: a missing fingerprint makes the check refuse, or skip on a stale record.
- **AC8** — When `grep -c 'run_spec_token_check "$slug" || return 1' tools/unattended/unattended.sh`
  runs it prints 1, and
  `grep -c 'run_bounded "$_stpy" "$SPEC_TOKENS_CLI"' tools/unattended/unattended.sh` prints 1. At the
  close the suite's arm at `tools/unattended/unattended.test.sh:4309` and its spec-token message arms at `tools/unattended/unattended.test.sh:7613-7632` read green unchanged.
  Red when: `verb_dispatch` keeps an inline copy beside the function, and the second grep prints 2.
- **AC9** — When `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` and
  `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` run, each prints
  nothing. `wc -c < memory/guides/UNATTENDED-PROTOCOL.md` prints at most 67183,
  `grep -c "any red but another build's" memory/guides/UNATTENDED-PROTOCOL.md` prints 1, and
  `grep -c 'skips the run when its inputs match' memory/guides/UNATTENDED-VERBS.md` prints 1.
  Red when: one copy is edited without its twin, or the protocol row grows past its ceiling.
  figure: 67183 is PINNED at `ae6735c1` from `tools/template-size-limits.txt`.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `tier2-review self-test` · `unattended protocol size` · `recall floor` · `recall floor arms` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `spec tokens (a spec's own names resolve)` · `memory hygiene` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC4 · a second build `tOther` whose live spec backticks the flagged bar, with `tRun` clean, and a repeated dispatch refused by a glob `--writes` path; staged by restoring the inline block, which refuses the first and runs the checker twice · `FLOOR_ASSERTIONS`, raised by the count of new assertions, which the close confirms

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
`memory hygiene` and the lexicon over this file.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft from brief `2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief`,
  item 4, grounded at `ae6735c1`. The brief left the scoping route to the writer: a filter on the
  checker's output, for the reasons under Alternatives rejected. "Green" is read as "admitted by the
  scoped verdict", for the same section's reason.

## 10. Reuse audit

The seams this unit extends: the spec-token block in `verb_dispatch`
(`tools/unattended/unattended.sh:14325-14341`), moved into `run_spec_token_check`; the working-tree
form of `tools/run-gates/gate-fingerprint.sh`, which `reuse_lookup.py` ranked as the `digest` SEAM
(fan-in 9) for "a digest of the working tree that says whether a recorded green still describes it";
the sibling-kit resolution of `print_drift_delta` (`tools/unattended/unattended.sh:1410-1424`); and
the sidecar root `resolve_sidecar_dir` (`tools/unattended/lib-unattended.sh:122`), which check 32 of
the kit gate requires every sidecar reader to use. The probe for "cache a check result keyed on a
hash of its inputs and skip the rerun" ranked generic name stems only, so no existing cache seam fits
beyond the fingerprint. Recall's top hits were `TOOL-aDeferredBar-2`, which put the checker in
`--dispatch`, and `TOOL-aOrientedCast-28`, whose harness-side token check is out of scope here. The
recall records cite the block at older line numbers (13493 and 13667), which the source at
`ae6735c1` places at 14325.

Recall terms used: `python tools/memory-recall/query.py "how does --dispatch run the spec-token checker and can its result be cached or scoped to one build" --terms "dispatch spec-token checker SPEC_TOKENS_CLI live tree refuse cache sidecar scoped build hits foreign"`
