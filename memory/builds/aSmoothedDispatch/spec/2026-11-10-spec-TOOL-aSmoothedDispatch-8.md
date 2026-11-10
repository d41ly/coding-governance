# TOOL-aSmoothedDispatch-8 — the closing review's mediums and lows: the writer's row shape, an arm per admit clause and cache key, the no-field `--writes` arms, the context's step-9b read, and the hook leg's driver guard

**Status:** SPECCED · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-8-review-fixes.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-8-review-fixes.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build ended CLEAN WITH FIXES with three medium items, two low items
and one carried medium gap, and the build method's severity rule promotes them all into one batch
unit. This unit closes each one where the review located it. Most of them are suite arms that pin
behaviour units 1, 4 and 6 already ship, so a later edit that breaks that behaviour reds a suite.
It also fixes one wrong writer instruction and one context line the hook should not print.

## 2. Scope (IN)

- **S1** — Item 1, text. The house overlay `tools/roles/house/gov-spec-writer.md` states the row
  shape the checker prints on exit 1. That is one `spec-tokens: <spec path> [<kind>]` row per miss,
  then a `spec-tokens: <N> unwaived hit(s)` summary. It also says that a `spec-tokens: REFUSING`
  line, an exit 2, or an exit 1 with no summary line is the checker refusing, which the writer names
  in its return. `.claude/agents/gov-spec-writer.md` is re-rendered from it. The `--spec` docstring in
  `tools/check-spec-tokens.py` states the same shape where its HIT and NEAR sentence stands today.
  Observed by AC1.
- **S2** — Item 1, arm. The checker suite gains one arm that reads both quoted spans from the overlay
  itself, substitutes a planted red spec's path, kind and count, and finds each in the stdout of a
  red `--spec` run. Observed by AC2.
- **S3** — Item 2. The driver suite's region three gains five verdict arms for unit 4's admit
  predicate. Each arm is staged RED by the break §4 names for it, which the pass probe verifies.
  Observed by AC3.
- **S4** — Item 3. The driver suite's unit 4 cache arm asserts that its second call re-ran the
  checker. It gains arms for an edited tracked file, a moved HEAD, a second slug, a refusal repeated,
  and a missing fingerprint. Observed by AC4.
- **S5** — Item 4. The driver suite's region four gains the three no-field `--writes` arms and the
  second carriage-return arm that unit 1's spec S3 named. Observed by AC5.
- **S6** — Item 5. `renderRouteContext` in `tools/hooks/scratch-guard.js` reads the dispatch rows
  only when no unit on the card is buildable, which is where `checkRouted` reaches step 9b. The hook
  suite gains one context arm for a buildable card unit beside a buildable dispatched unit. Observed
  by AC6.
- **S7** — The carried gap. The `scratch-guard self-test` leg in `tools/gate-legs.json` adds the
  exact driver file its suite reads, `{prefix}/unattended/unattended.sh`, to its guard. Observed by
  AC7.
- **S8** — The one live spec the S7 guard newly owes that leg,
  `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md`, adds
  `scratch-guard self-test` to its §7 leg line, with a rev bump and a revision-log line naming this
  unit and the review record. Observed by AC8.

## 3. Non-goals (OUT)

- No behaviour change to the shipped code of units 1 to 7, apart from S6's read order. The admit
  predicate, the cache key and the `--writes` split stay as they are. The arms pin them.
- No edit to a CLOSED spec of this build. The two wrong texts in the spec of unit 7 are corrected
  in §4 of this spec, under "Corrections to the CLOSED spec of unit 7". Unit 6's spec S3 already
  states the read order S6 builds, so it needs no correction.
- No new bug-class record. All four classes the review names exist under `memory/gotchas/`.
- No arm for the `[ -n "$n" ]` and `[ "$n" -gt 0 ]` clauses of the predicate. §4 says why each
  has no single-clause case.
- No row in `memory/project/spec-token-waivers.txt`. Its header makes it shrink-only.
- No change to the hook suite's other reads of sibling kits, such as its resolution of the run-gates
  kit. The review did not name them.
- No hand edit to a kit version. The lander's `mint` moves them.
- No `help/` page. No page documents the overlay text, the suites or the leg manifest.

### Edges

none

## 4. Design

### What the tree holds, read at `dc991a59`

`dc991a59` is this build's branch tip, carrying units 1 to 7 on top of the base `ae6735c1`.

| Fact | Where |
|---|---|
| The overlay and its render say exit 1 prints one `spec-tokens: HIT` row per miss. | `tools/roles/house/gov-spec-writer.md:5`, `.claude/agents/gov-spec-writer.md:56` |
| The `--spec` docstring says "only HIT and NEAR rows naming the file are printed". | `tools/check-spec-tokens.py:260` |
| The `HIT` label prints only under `--list`, and that run returns 0. | `tools/check-spec-tokens.py:1927-1931`, `:2041-2042` |
| Exit 1 prints each unwaived hit as `spec-tokens: {f} [{kind}]`, then the summary. | `tools/check-spec-tokens.py:2043-2049` |
| The checker's refusals print `spec-tokens: REFUSING` and return 1 or 2. | `tools/check-spec-tokens.py:1553-1556`, `:1578-1579`, `:1604-1605` |
| The checker suite already has a `--spec` arm whose spec reds on its leg. | `tools/check-spec-tokens.test.sh:1993` |
| The checker suite resolves sibling kits with `resolve_kit_dir`. | `tools/check-spec-tokens.test.sh:277`, `:328-335` |
| The admit predicate is one line of five clauses. | `tools/unattended/unattended.sh:14315` |
| The cache key hashes the slug, the checker, the launcher, HEAD and the fingerprint. | `tools/unattended/unattended.sh:14338-14344` |
| The record is written only after the verdict admits. | `tools/unattended/unattended.sh:14394-14396` |
| The fingerprint digests `HEAD^{tree}`, the porcelain status and dirty blobs, never the HEAD sha. | `tools/run-gates/gate-fingerprint.sh:50`, `:61`, `:86` |
| The unit 4 arm's second call asserts only the glob refusal. | `tools/unattended/unattended.test.sh:7660-7661` |
| The `--writes` split appends one empty path for a value with no field, and for a flag with no value. | `tools/unattended/unattended.sh:15198`, `:15201` |
| Unit 1 left one carriage-return arm. The base held two space-holding arms. | `tools/unattended/unattended.test.sh:9125`; `git show ae6735c1:tools/unattended/unattended.test.sh`, lines 9072-9073 |
| `renderRouteContext` reads the dispatch rows whatever the card's verdicts are. | `tools/hooks/scratch-guard.js:1595-1604` |
| `checkRouted` returns at step 9a on the first buildable card unit, before step 9b. | `tools/hooks/scratch-guard.js:1249-1267` |
| The hook suite reads the driver at two sites, through `ls-files '*/unattended.sh'`. | `tools/hooks/scratch-guard.test.sh:866`, `:1204` |
| The leg's guard names `{prefix}/hooks/`, `{prefix}/lib/` and `skills/session-kickoff/`. | `tools/gate-legs.json:356-360` |

### Corrections to the CLOSED spec of unit 7

That spec is frozen, so its corrections are recorded here. Its evidence row at line 82 cites
`tools/check-spec-tokens.py:1881` for a `spec-tokens: HIT` row. That line is a carries-join refusal,
and the `HIT` label is printed only by `--list`. The row should cite `tools/check-spec-tokens.py:2044`
and the shape `spec-tokens: <file> [<kind>]`. Its quoted overlay text at line 98 carries the same
wrong sentence. S1's text below replaces it.

### S1 — the overlay text

The overlay becomes this text. Each backticked span sits whole on one line, because S2's arm reads
the spans line by line.

```
Before you return, check each spec you wrote or revised with the spec-token checker's one-spec mode,
where this repository holds `<prefix>/check-spec-tokens.py`, `<prefix>` being its tool root:
`python <prefix>/check-spec-tokens.py --spec <the spec's path>`. That run grades your one spec and is
not a gate leg. The checker run with no `--spec` is the gate leg, and it stays refused to you.
Exit 1 with hits prints one `spec-tokens: <spec path> [<kind>]` row per miss, naming its token,
then a `spec-tokens: <N> unwaived hit(s)` summary. Fix each miss your spec's own text can fix, then
run the check again. A hit your spec's text cannot fix goes in your return, with its row.
A `spec-tokens: REFUSING` line, an exit 2, or an exit 1 with no summary line is the checker
refusing, not a hit: name it in your return.
```

Spec 7's AC2 grep must still print nothing over the file. The text holds no `tools/` literal, no
heading line, no double brace and no protocol file name. `python tools/roles/render_agents.py --write`
re-renders `.claude/agents/gov-spec-writer.md`, and no other agent type moves.

The docstring sentence at `tools/check-spec-tokens.py:258-260` becomes: "Stale waiver rows and stale
size high-water rows are NOT reported, because one file cannot show a row is stale. A hit prints as
`spec-tokens: <path> [<kind>]` followed by its token, then the `<N> unwaived hit(s)` summary, and the
run exits 1. The `HIT` and `NEAR` labels are `--list`'s, and that run exits 0."

### S2 — the overlay-parity arm

The arm sits after the unit 5 arms in `tools/check-spec-tokens.test.sh`, in the `scope` scratch repo,
where `$sc_spec` reds on its leg. It resolves the roles kit with
`resolve_kit_dir "$PY" roles render_agents.py "$HERE"` and reads `house/gov-spec-writer.md` under it.

1. Extract the first backticked span opening `spec-tokens: <spec path> [` and the first opening
   `spec-tokens: <N> unwaived`.
2. If the overlay is missing or either span is empty, print `arm FAIL` and count a failure. An empty
   needle matches every output, so this check is what keeps the arm from passing on nothing.
3. Replace `<spec path>` with `$sc_spec` and `<kind>` with `leg` in the row span, and `<N>` with `1`
   in the summary span.
4. Call `arm` twice with `ARM_ARGS=(--spec "$sc_spec")`, expecting exit 1 and each substituted span.

Staged RED: the overlay put back to the `spec-tokens: HIT` sentence, so step 2 fails. The arm adds
2 to `FLOOR_ASSERTIONS`, or 3 if step 2's check counts as its own assertion. The builder counts by
reading and writes a `RAISED` line.

### S3 — the verdict arms, and the break that reds each

The arms sit in the `if [ -f "$STC" ]` block of region three, after the unit 4 arm and before its
cleanup. Each arm deletes `.git/unattended/spec-tokens.tRun.key` first, so a cache skip cannot stand
in for a verdict. Each dispatch uses `--writes "${PFX}*.sh"`, which the glob check refuses after the
spec-token check, so no row is written. The stub arms reuse the `${PFX}stub-tokens.py` pattern
already in that block, with the stub's stdout written to fit the arm.

The review asked that each arm be staged RED "by deleting its clause". The pass probe below shows
that holds for the stale arm only. The clauses overlap, so the `both` and `nosummary` cases still
refuse when any one clause is deleted. This table states the break that reds each arm, as the probe
measured it.

| arm | checker | output | asserts | staged RED by |
|---|---|---|---|---|
| both | real | `tRun`'s and `tOther`'s specs each backtick the flagged bar | the check-49 refusal, a `memory/builds/tRun/` line quoted, no admit note | deleting `[ "${#ownq[@]}" = 0 ]` and `[ "$n" = "$nfar" ]` together |
| undercount | stub | an own line, a foreign line, `spec-tokens: 1 unwaived hit(s), 0 stale row(s)` | the check-49 refusal | deleting `[ "${#ownq[@]}" = 0 ]` |
| stale | real | `tRun` clean, `tOther` red, and a waiver row no spec produces | the check-49 refusal | deleting `[ "$m" = 0 ]` |
| unattributed | stub | `spec-tokens: tools/x.md [packet]` and its token, then a summary of 1 hit and 0 stale | the check-49 refusal | deleting `[ "$n" = "$nfar" ]` |
| nosummary | stub | one foreign hit line and no summary, exit 1 | the check-49 refusal | the predicate cut to `[ "${#ownq[@]}" = 0 ] && [ "$nfar" -gt 0 ]` |

Two clauses get no arm. `[ -n "$n" ]` is dominated, because `[ "$n" -gt 0 ]` is false on an empty
`n` (bash reports an integer error). `[ "$n" -gt 0 ]` matters only for a zero-hit summary on exit 1,
which the checker never prints: it prints the summary only when a hit or a stale row exists.

The stubs are the fixture and never the break. The real checker cannot print the `undercount`,
`unattributed` or `nosummary` output today, and those outputs are what the predicate must refuse if
the checker's print ever drifts.

### S4 — the cache arms, and the key part each one isolates

These extend the unit 4 arm in order, on its fixture.

| step | action | asserts | staged RED by |
|---|---|---|---|
| a | call 2 as today, after call 1 moved the run-state file | the admit note, and no `spec-token check skipped` | `$fp` dropped from the hash input |
| b | edit a tracked file, then dispatch | the admit note, and no skip line | `$fp` dropped |
| c | `git commit -q --allow-empty`, then dispatch, then `git reset -q --soft HEAD~1` | the admit note, and no skip line | `$hd` dropped |
| d | `( load_driver_conf && run_spec_token_check tOther )`, in process | the check-49 refusal naming `memory/builds/tOther/`, and no skip line | `$1` dropped from the hash input and the slug dropped from the record's file name |
| e | `tRun`'s spec made own-red, then dispatched twice | both calls refused under check 49, and neither prints a skip line | the record write moved above the verdict |
| f | delete the record and `./${PFX}run-gates/gate-fingerprint.sh`, then dispatch twice | `spec-token cache off` on both calls, and no `spec-tokens.tRun.key` file | the two early returns of `derive_spec_token_key`, on an unresolved kit and on an empty digest, made no-ops, so a key is hashed over an empty fingerprint |

Step c isolates HEAD because an empty commit leaves `HEAD^{tree}`, the porcelain and the blobs as
they were, so the fingerprint does not move. Step d needs two breaks because the slug guards the
cache twice, in the key and in the record's file name. Step d calls the function in process, as the
suite's top-level source of the driver allows (`tools/unattended/unattended.test.sh:664`). A full
`--dispatch tOther` would first need a run-state file, a chain and a spec for `tOther`. The real
checker grades the tree, so `tOther`'s own red refuses it.

### S5 — the `--writes` arms

They sit beside the `--writes ''` arm in region four, at `tools/unattended/unattended.test.sh:9115`.

| argv after `--pass ARCH-tRun-1` | asserts | staged RED by |
|---|---|---|
| `--writes --writes ${PFX}a.sh` | `given an empty --writes path` | deleting the trailing empty-path append at `:15201` |
| `--writes ${PFX}a.sh --writes` | `given an empty --writes path` | the same |
| `--writes '  ' --writes ${PFX}a.sh` | `given an empty --writes path` | the `DP_WRITES+=("")` of the empty-array branch at `:15198` replaced by `:` |
| `--writes $'spells\r·\rseparator.sh'` | `containing whitespace` | the split's IFS widened to `$' \t\n\r'`, the break of the first carriage-return arm |

The `:` replacement keeps the `if` branch legal bash. The fourth row is the base's separator arm
rewritten to a carriage return, as unit 1's spec S3 stated.

### S6 — the context's read order

In `renderRouteContext`, the step-6 block runs only when
`route.units.some((u) => !checkBuildable(u, route.build, top, memRoot.trim(), confBytes))` is false.
That is the same set and test `checkRouted` walks at step 9a. The comment above the block says so.
No new function or constant is minted.

The hook suite gains one arm beside the D-AC5 rows. It runs `write_run_state TOOL-x-13`, then
`run_sub` over `session_id=sgtest-r1`, whose card routes the INPROGRESS `TOOL-x-1`. It asserts with
`check_ctx` that the context names `TOOL-x-1 is buildable`, and asserts that it carries no
`dispatch row` line. Then it removes the run-state file. `TOOL-x-13` is an INPROGRESS Tier-1 spec of
build `bx`, written at `tools/hooks/scratch-guard.test.sh:1030`. Staged RED: the new condition
removed, so the context names `TOOL-x-13` through its dispatch row. The pin `FLOOR_ASSERTIONS=325`
rises by the rows added, counted by reading, in that file's `<new> = <old> + ...` comment form.

### S7, S8 — the guard, and the spec it newly binds

The suite reads only the driver script from the unattended kit, so the guard gains that one file.
The record `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md` gives this fix: name the exact
files the suite reads, not the sibling's directory.

The guards join of `tools/check-spec-tokens.py` reads guards, and a declared directory trips a guard
under it (`tools/memory-tree/design_lib.py:636-645`). Every live spec dated on or after
`SPEC_GUARD_LEGS_CUTOFF` was swept for a path under `tools/unattended/` in its files-touched
estimate. Three were found. `DEPL-aScoutedSeam-1` and `KICK-aScoutedSeam-1` already name the leg, and
their paths do not trip an exact-file guard. `TOOL-aOrientedCast-28` declares the directory
`tools/unattended/` and does not name the leg. With either guard spelling, the bar's
`spec tokens (a spec's own names resolve)` leg would then red on
`scratch-guard self-test <- tools/unattended/`. S8 adds the leg to that spec's §7 line instead:
the leg would run on that unit's driver edits, which is the point of the guard. Its §9 line is
`- rev-3 · <date> · §7 · adds scratch-guard self-test, which TOOL-aSmoothedDispatch-8's guard on the
driver now trips through this spec's tools/unattended/ estimate
(2026-11-10-review-TOOL-aSmoothedDispatch-1-closing-diff-round1).`

### The pass probe for S3, `$SCRATCH/sd8.sh`

`$SCRATCH` is the run's scratch directory. Run the probe from the worktree root. It copies the
predicate's function into the scratch directory, applies each staged break with `sed`, and prints
each fixture output's verdict. This spec's author ran it at `dc991a59`.

```bash
set -u; S="$SCRATCH/sd8"; mkdir -p "$S"
sed -n '/^check_spec_token_hits() {/,/^}/p' tools/unattended/unattended.sh > "$S/f.sh"
P='\[ -n "\$n" \] && \[ "\${#ownq\[@\]}" = 0 \] && \[ "\$m" = 0 \] && \[ "\$n" -gt 0 \] && \[ "\$n" = "\$nfar" \]'
echo "predicate lines $(grep -c "$P" "$S/f.sh")"
mk() { sed "s/$P/$2/" "$S/f.sh" > "$S/$1.sh"; }
mk shipped '[ -n "$n" ] \&\& [ "${#ownq[@]}" = 0 ] \&\& [ "$m" = 0 ] \&\& [ "$n" -gt 0 ] \&\& [ "$n" = "$nfar" ]'
mk noown '[ -n "$n" ] \&\& [ "$m" = 0 ] \&\& [ "$n" -gt 0 ] \&\& [ "$n" = "$nfar" ]'
mk noeq '[ -n "$n" ] \&\& [ "${#ownq[@]}" = 0 ] \&\& [ "$m" = 0 ] \&\& [ "$n" -gt 0 ]'
mk noowneq '[ -n "$n" ] \&\& [ "$m" = 0 ] \&\& [ "$n" -gt 0 ]'
mk nom '[ -n "$n" ] \&\& [ "${#ownq[@]}" = 0 ] \&\& [ "$n" -gt 0 ] \&\& [ "$n" = "$nfar" ]'
mk absent '[ "${#ownq[@]}" = 0 ] \&\& [ "$nfar" -gt 0 ]'
own='spec-tokens: memory/builds/tRun/spec/a.md [bar] `t` — w'
far='spec-tokens: memory/builds/tOther/spec/b.md [bar] `t` — w'
odd='spec-tokens: tools/x.md [packet] `tRun` — w'
F='spec-tokens: %s unwaived hit(s), %s stale row(s)'
declare -A C=([both]="$own"$'\n'"$far"$'\n'"$(printf "$F" 2 0)"
  [undercount]="$own"$'\n'"$far"$'\n'"$(printf "$F" 1 0)"
  [stale]="$far"$'\n''spec-tokens: STALE WAIVER `x` — w'$'\n'"$(printf "$F" 1 1)"
  [unattributed]="$odd"$'\n'"$(printf "$F" 1 0)" [nosummary]="$far"
  [foreign]="$far"$'\n'"$(printf "$F" 1 0)")
for v in shipped noown noeq noowneq nom absent; do l=$v
  for c in both undercount stale unattributed nosummary foreign; do
    r=$(MEMORY_ROOT=memory bash -c '. "$1"; check_spec_token_hits tRun 1 "$2" >/dev/null 2>&1; echo $?' _ "$S/$v.sh" "${C[$c]}")
    l="$l $c=$r"; done; echo "$l"; done
```

At `dc991a59` it printed `predicate lines 1`, then these rows. A `0` is an admission, which is the
arm's RED.

```
shipped both=1 undercount=1 stale=1 unattributed=1 nosummary=1 foreign=0
noown both=1 undercount=0 stale=1 unattributed=1 nosummary=1 foreign=0
noeq both=1 undercount=1 stale=1 unattributed=0 nosummary=1 foreign=0
noowneq both=0 undercount=0 stale=1 unattributed=0 nosummary=1 foreign=0
nom both=1 undercount=1 stale=0 unattributed=1 nosummary=1 foreign=0
absent both=1 undercount=1 stale=0 unattributed=1 nosummary=0 foreign=0
```

### The builder's own checks

The builder runs no suite. After editing, it runs `bash -n` over each edited shell suite and
`node --check tools/hooks/scratch-guard.js`, and it runs the probe above. Each new arm's RED and
GREEN observation belongs to the main loop at the close.

### Files touched (estimate)

- `tools/roles/house/gov-spec-writer.md`
- `.claude/agents/gov-spec-writer.md`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/unattended/unattended.test.sh`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/gate-legs.json`
- `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md`

### Rollout

One pass, after units 1 to 7, all CLOSED. The overlay is a seed of the roles kit, and the hook and
the driver suite are shipped bytes of their kits, so `kit epoch` wants those versions moved. The
lander's `mint` moves them. The checker, its suite and the leg manifest are gov-only
(`tools/govkit/registry.toml:218-233`). A session started before the render spawns the old writer
type, so S1 reaches writers from the next session on.

### Alternatives rejected

- **Guard the directory `{prefix}/unattended/`, as the brief's acceptance spells it.** The suite
  reads one file of that kit. The gotcha record's fix names the exact file. The directory would
  also run a held suite with a 490-second ceiling on every edit to the kit's other files. The brief
  wrote the directory, so this choice is called out in the return to the dispatcher.
- **A waiver row for the hit S8 fixes.** The waiver registry is shrink-only by its own header.
- **Take the `anyBuildable` flag from `renderVerdict`, the review's other option.** That function
  runs only for route lines inside the context's character cap. A buildable card unit past the cap
  would then leave the flag false while `checkRouted` admits at step 9a.
- **Have the writer run `--spec <path> --list`.** It exits 0 on hits, so every exit-code sentence
  of the overlay would change, and the review named that fix instance-only.
- **Stage each verdict arm by deleting one clause, as the brief and review state.** The probe shows
  that leaves the `both` and `nosummary` arms green, so they would be arms never seen red.

## 5. Production-readiness checklist

- security — S3 and S4 pin the dispatch boundary's deny-by-default verdict and its cache. A
  regression in either now reds a suite. S6 changes only a context line. The gate's verdict is
  unchanged. S7 widens when a held suite runs and narrows nothing.
- perf / scale — S6 skips one run-state file read and one spec-folder walk per subagent start when a
  card unit is buildable. S7 adds the hook suite's run to driver-script edits only.
- error / empty / loading states — S2's arm fails on a missing overlay or an empty span, never
  passing on an empty needle.
- observability — the overlay names the three refusal shapes a writer reports.
- risks — the new arms raise three floors by hand counts, which the close confirms from a real run.
  S8 edits another build's live spec. It adds one leg name and changes nothing that spec builds.
- testing — the pass probe for S3, and five new suite arms observed RED and GREEN at the close.
- migration — none.
- user docs — N/A: no `help/` page covers the overlay, the suites or the leg manifest.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'spec-tokens: HIT' tools/roles/house/gov-spec-writer.md .claude/agents/gov-spec-writer.md`
  runs, each file counts 0. `grep -cF 'spec-tokens: <spec path> [<kind>]'` and
  `grep -cF 'spec-tokens: REFUSING'` each count 1 in both files.
  `grep -c 'only HIT and NEAR rows' tools/check-spec-tokens.py` prints 0, and
  `python tools/roles/render_agents.py --check` exits 0.
  Red when: the overlay still quotes the `--list` label, or it is edited without `--write`, so
  `--check` names the agent type as drift.
- **AC2** — When `grep -nF 'print(f"spec-tokens: {f} [{kind}] ' tools/check-spec-tokens.py` runs, it
  prints the one exit-1 hit print that the overlay's row span quotes, and
  `grep -cF 'unwaived hit(s), {len(stale)} stale row(s)' tools/check-spec-tokens.py` prints 1. At the
  close, the checker suite's S2 arm finds both substituted spans in a red `--spec` run's stdout.
  Red when: the overlay's row span is reverted to the `HIT` sentence, so the arm extracts no span
  and fails.
- **AC3** — When `bash "$SCRATCH/sd8.sh"` runs, it prints the six rows in §4 exactly. In the driver
  suite, `grep -c 'TOOL-aSmoothedDispatch-8 AC3' tools/unattended/unattended.test.sh` counts one
  marker per verdict arm, 5 in all. At the close each arm reads RED on its §4 break and GREEN once
  restored.
  Red when: a staged break leaves its arm's case refused. The `noown` row would then read
  `undercount=1`, so that arm is never seen red.
- **AC4** — When `grep -c 'TOOL-aSmoothedDispatch-8 AC4' tools/unattended/unattended.test.sh` runs, it
  counts one marker per cache step a to f, 6 in all. At the close step a reads RED with `$fp` dropped
  from the hash input in `derive_spec_token_key`, step c with `$hd` dropped, and steps d, e and f on
  their §4 breaks. Each reads GREEN once restored.
  Red when: the key leaves out a part, and the arm for that part still reads green because it
  asserts the refusal text only and never that the checker ran.
- **AC5** — When `grep -c 'TOOL-aSmoothedDispatch-8 AC5' tools/unattended/unattended.test.sh` runs, it
  counts 4. `grep -cF "spells\r·\rseparator.sh" tools/unattended/unattended.test.sh` prints 1. At the
  close the first two arms read RED with `|| DP_WRITES+=("")` deleted, the third with the
  empty-array append replaced by `:`, and the fourth with the IFS widened. Each reads GREEN once
  restored.
  Red when: a no-field `--writes` shape declares only `${PFX}a.sh` and skips the empty-path refusal.
- **AC6** — When `grep -n 'route.units.some' tools/hooks/scratch-guard.js` runs, it prints one line
  inside `renderRouteContext`, and `node --check tools/hooks/scratch-guard.js` exits 0. At the close the
  hook suite's new arm reads GREEN, then RED with the condition removed, when the context names
  `TOOL-x-13` through its dispatch row. The D-AC5 rows stay green.
  Red when: the step-6 block runs while a card unit is buildable.
- **AC7** — When `python tools/check-spec-tokens.py --legs-for tools/unattended/unattended.sh` runs, the
  path's block names `scratch-guard self-test`. The same query for
  `tools/unattended/lib-unattended.sh` does not name it.
  Red when: the guard is unchanged and the driver path trips no hook leg, or the guard names the
  whole kit directory.
- **AC8** — When `grep -c 'scratch-guard self-test' memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md`
  runs, it prints at least 1, on its §7 leg line. Its header reads `rev-3`, and its §9 holds a
  `rev-3` line naming `TOOL-aSmoothedDispatch-8`. `python tools/check-spec-tokens.py --spec` over
  that file prints no `scratch-guard self-test <-` row.
  Red when: S7 lands alone, so that spec's `tools/unattended/` estimate trips the leg its §7 omits.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `memory-hygiene self-test` · `build-index selftest` · `policy fixtures` · `check-wiring self-test` · `spec-tokens self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `roles catalogue` · `roles render wiring` · `unattended kit gate` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC2 · the overlay put back to the `spec-tokens: HIT` sentence, so no span is extracted · `FLOOR_ASSERTIONS`, raised by the arm's count
New arm: tools/unattended/unattended.test.sh · covers AC3 · the five verdict arms of region three, each on its break in §4 S3 · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_3`, raised by the same count
New arm: tools/unattended/unattended.test.sh · covers AC4 · cache steps a to f of region three, each on its break in §4 S4 · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_3`, raised by the same count
New arm: tools/unattended/unattended.test.sh · covers AC5 · the four `--writes` arms of region four, each on its break in §4 S5 · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_4`, raised by the same count
New arm: tools/hooks/scratch-guard.test.sh · covers AC6 · the step-6 condition removed, so the context names the dispatched unit · `FLOOR_ASSERTIONS`, raised by the rows added

The driver suite is no leg of the manifest. It runs as the eight shard rows of
`tools/run-gates/selftest-budgets.txt`, so its arms are declared above and not on the leg line. The
brief's "unattended kit self-test" names that suite, not a leg. The leg line names every leg a path
under Files touched trips, apart from the broad guards, as the checker reads them. A builder runs only
the lexicon. The main loop observes each new arm RED, then GREEN, and runs the bar once, at the close.
This spec's author ran no gate but the spec-token checker's one-spec mode over this file.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft from the brief
  `2026-11-10-prompt-TOOL-aSmoothedDispatch-8-review-fixes`, grounded at `dc991a59`. The probe
  replaced the review's per-clause staging for the `both` and `nosummary` arms and added the
  `undercount` and `unattributed` arms. The guard names the driver file, following the gotcha
  record's fix. A sweep of live specs found the one spec S8 repairs.

## 10. Reuse audit

Every item extends a seam already in the tree, so no new mechanism is added. The arms reuse the
`arm` helper of `tools/check-spec-tokens.test.sh`, which `reuse_lookup.py` ranked as the `arm` SEAM
(fan-in 37) for "a suite arm that reads a documented output prefix from a doc and greps the tool's
real output for it". They also reuse the `hit` and `miss` helpers and the region-three
`stub-tokens.py` fixture of the driver suite, and the `run_sub` and `check_ctx` helpers of the hook
suite. The roles kit is resolved with the suite's own `resolve_kit_dir`. Recall ranked the earlier
minors batches `TOOL-dFairHearing-43` and `TOOL-dTrueNorth-26` first. This spec follows their
per-item shape. The checklist from `gotchas.py --for-paths` selected
`held-suite-guard-misses-a-sibling-kit`, whose fix shaped S7, and
`hand-named-gate-list-green-while-the-bar-reds`, which led to S8's sweep. One record disagreed with
the code: the review cites the unit 7 spec's lines 81 and 97, and the file puts them at 82 and 98.

Recall terms used: `python tools/memory-recall/query.py "how were closing-review minors batched into one repair unit adding suite arms per key component and per clause" --terms "closing review minors batch suite arm staged RED clause cache key component guard sibling kit"`
