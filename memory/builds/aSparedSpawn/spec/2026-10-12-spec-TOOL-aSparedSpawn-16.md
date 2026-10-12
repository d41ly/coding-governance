# TOOL-aSparedSpawn-16 — the closing review's mediums and lows, and the bar reds this build's diff carries

**Status:** INPROGRESS · rev-3 · 2026-10-12 · node a · Tier-2 · base f479ba42 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-prompt-TOOL-aSparedSpawn-16-build-brief.md](../prompts/2026-10-12-prompt-TOOL-aSparedSpawn-16-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Make the build's own HEAD bar green, and fix every MEDIUM and LOW finding of the round-1 closing
review (`memory/builds/aSparedSpawn/reviews/2026-10-12-review-TOOL-aSparedSpawn-1-15-closing-diff-round1.md`)
that no HIGH unit owns. The review converged with three HIGHs, and the owner rulings of 2026-10-04
promote one unit per HIGH and batch the rest here: ids 1, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18,
19, 21, 22 and 23. Ids 4 and 15 duplicate HIGH id 20 and go with it to `TOOL-aSparedSpawn-19`. The
bar reds this build's diff carries ride along: two drifted registries, two stale fork ceilings and
six unarmed exit sites.

## 2. Scope (IN)

Every site was re-read at f479ba42; line numbers are that tree's. Each item names the review finding
id it closes and, where the report gives one, follows the skeptic's corrected fix. Labels S5, S7 and
S8 are unused since rev-2; §9 says where their work went.

- **S1** — Finding 9. `tools/govkit/subject-pins.tsv` carries no row for the `held-halves selftest`
  leg that unit 5 added to `tools/gate-legs.json`, so `govkit selfcheck` reds. The row comes from
  `python tools/govkit/govkit.py selfcheck --write`, committed as written; the file is generated and
  is never hand-edited. Observed by AC1.
- **S2** — Finding 10. `memory/project/spawn-idiom-sites.txt` has drifted from its population: the
  leg's argv reports seven findings at f479ba42. They are `cat-file` in `run-gates.sh` (15 declared,
  16 measured), `run-gates.test.sh` (23, 24), `run-gates.evidence.test.sh` (11, 14) and
  `.githooks/pre-push.test.sh` (8, 12); `printf-subst` (2, 3) and `var-pipe` (136, 141) in
  `run-gates.test.sh`; and `var-pipe` in `tools/unattended/check-unattended.sh` (26 declared, 25
  measured). Each forking site this build added in its own files is rewritten first: a `$(cat f)`
  becomes `$(<f)` or a `read`, and a `printf … | grep -c` becomes a builtin test where one reads the
  same answer. Every row is then re-measured and set to exactly what the scan reports, the
  `check-unattended.sh` row lowered to its measured 25. This item lands LAST in the pass, after every
  other item adds its arms, so the registry is measured over the final bytes. Rev-3: the
  `printf … | grep -c` and `grep -q` sites this build added in `run-gates.test.sh` read a count or a
  match over multi-line output, which no one builtin test reads, so that file's `var-pipe` row is set
  to its measured count, above its old one, while every `cat-file` and `printf-subst` site the build
  added is rewritten. Observed by AC2.
- **S3** — `memory/project/fork-ceilings.txt` rows `run-gates-1leg` and `run-gates-2leg` declare
  ceilings 72 and 74 against measured counts of 51 and 53, which the `spawn budget (forks per hot
  entrypoint)` leg reds as STALE (the file's tolerance is max(3, 5 %) above the count). The one-leg
  row falls to its measured count. The two-leg row falls to its measured count plus two, because its
  reason already records a polled reading that varied, and the reason gains that margin and the date
  measured. Both are re-measured after every runner change in this unit. Observed by AC3.
- **S4** — `python tools/memory-tree/check-arms.py --check` reds on six unarmed exit sites in
  `tools/run-gates/run-gates.sh` that units 1, 2 and 4 added. Each is armed or pinned:
  - `:1270` (no spawn command resolves) and `:1273` (a rate could not be measured) are reasoned
    sites. Each gains an arm in `tools/run-gates/run-gates.test.sh` beside arm 12a, asserting its
    whole failure text from the calibrate verb run without the rates seam: a blank
    `GATE_SPAWN_CMD` for the first, and `false` as the spawn command for the second.
  - `:1236`, the `|| exit 1` inside `measure_spawn_rate`'s timed subshell, is delegated: its only
    effect is the `:1273` refusal. It gains a `# arm-signature:` marker naming that refusal's text,
    which the `:1273` arm then arms.
  - `:2896` (`git version … || exit 1`) and `:2909` (`[ "${#evs[@]}" -gt 0 ] || exit 1`) exit the
    `REUSE_DIGEST` capture. S18's line gives that failure a text, so each is marked with
    `# arm-signature:` naming it, and canary arm 9d3 (S18) asserts it whole (rev-3): check-arms reads
    this gate's arms from `run-gates.test.sh` alone, so the arm is the canary's, and nothing is pinned.
  - `:5088`, the bare `exit 1` closing a red run, gains a `# arm-signature:` marker naming the
    `gates RED` summary text an existing canary arm already asserts.

  The canary's `FLOOR_ASSERTIONS` rises by every assertion this unit adds to the canary, with a
  `RAISED` line. Observed by AC4.
- **S6** — Finding 1. `.githooks/pre-push` clears `GATE_REUSE_SAMPLE` and `GATE_REUSE_DAY` beside
  `GATE_REUSE_PUSH` (`:1456`-`:1457`), for every bar a STUB included, and appends each to
  `ENV_CLEARED` when it was set, so the `not honoured from the environment by this bar:` line names
  it. The runner keeps reading both, since they are its own suite's seams. An arm in
  `.githooks/pre-push.test.sh` beside the AC15 arm exports `GATE_REUSE_SAMPLE=0` and
  `GATE_REUSE_DAY=1` into a push and asserts the line names each. Observed by AC6.
- **S9** — Finding 18. `FLOOR_ASSERTIONS` in `tools/run-gates/run-gates.evidence.test.sh` (151 at
  `:156`, 163 since `TOOL-aSparedSpawn-17` counted its own twelve) rises by the executed assertions
  unit 13 and this unit's evidence arms add, counted one per `ok … || nope` pair as units 1, 3 and 4
  counted theirs: unit 13's forty-one beyond the six it rewrote in place, and this unit's four, to 208, with a
  `RAISED <old> -> <new> by TOOL-aSparedSpawn-13 and -16` line. The acceptance ledger marks the
  executed count OWED until the suite runs at VERIFYING. Observed by AC10.
- **S10** — MOVED TO THE BUILD'S EXIT AS A NAMED ASK (rev-3); the text below is the ask's design and
  nothing of it is built here. A pre-push hook's environment, observed 2026-10-12 on node a, differs
  from a plain shell by more than `GIT_EXEC_PATH` and the PATH prefix: git also exports `GIT_PREFIX`,
  and Git for Windows exports `LC_CTYPE=C.UTF-8` where the caller set none, while a `git -c alias`
  child, AC11's instrument, adds `GIT_DIR` and `GIT_CONFIG_PARAMETERS` too. `LC_CTYPE` is a locale a
  leg can read, so leaving it out of the digest trades a miss for a possible false hit, which is the
  owner's call this spec did not make, and without it no direct bar's entry is reused through the
  hook on this node. `REUSE_SCHEMA` stays 3, since S11's entry reads compatibly.
  Findings 11 and 21 (M3), reconciled as the report says: id 21's fix, with id 11's rule
  for the `tool` lines. `REUSE_DIGEST` in `tools/run-gates/run-gates.sh` (`:2891`-`:2913`) leaves
  out of its env loop `GIT_EXEC_PATH` and the hook-only knobs `GATE_ATTRIBUTE`,
  `GATE_INHERITED_RED`, `GATE_INHERITED_RED_MAX_AGE` and `GATE_DOCS_BASE`, which `.githooks/pre-push`
  exports (`:1507`, `:1517`, `:1547`-`:1549`) and which decide red attribution or leg selection, not
  a leg's own `ok`. PATH is hashed with a leading component stripped when it names git's exec path,
  in its native or MSYS spelling, and each `tool` line resolves with `type -P` under that stripped
  PATH. `REUSE_SCHEMA` moves from 3 to 4. An arm in `.githooks/pre-push.test.sh` earns an entry with
  a direct bar, pushes through the real `.githooks/pre-push` with a scoped decision, and asserts
  `GATE reuse` on a remote leg. Observed by AC11.
- **S11** — Finding 12 (M5). The consecutive-reuse count is kept per cache KEY, as a sixth field of
  the entry itself, and no longer per leg name in the shared `$REUSE_CACHE/age.<name key>` file. A
  reuse rewrites its entry with the count plus one, in place by `printf`; a torn read is malformed
  and executes, which costs a saving and never a verdict. An entry with five fields reads as count 0.
  Only an execution under that key resets it, by writing a fresh entry; an execution under another
  key touches nothing of it. The evidence suite's AC7 arm sets the entry's count field to 10 rather
  than an `age.*` file, and `tools/run-gates/README.md`'s age rule says per key. Spec 13 is a landed
  record, so its S7 text is superseded by this item rather than rewritten. Observed by AC12.
  - **Readers:** by name: READER NOT IN TREE once this item is built, since it rewrites every reader
    that spelled the file kind (rev-3); at f479ba42 `tools/run-gates/run-gates.sh` read,
    incremented and reset the
    `age.<name key>` file (`:3097`, `:3115`, `:4819`); `tools/run-gates/run-gates.evidence.test.sh`
    globs `age.*` in its AC7 arm (`:1244`-`:1249`); `tools/run-gates/README.md` names
    `age.<name key>` (`:214`); `TOOL-aSparedSpawn-17`'s AC1 arm, landed after this spec, globs
    `age.*` too, and reads its key after a reuse run, whose record holds no row for a reused leg, so
    it reads the key from the earning run instead (rev-3). by value: `tools/run-gates/run-gates.sh`'s
    reuse block compares the count to 10 at `:3099`, the evidence AC7 arm compares it to 0 after an
    execution, and the evidence AC5 arm asserts a reused leg's entry is byte-identical, which now
    holds for every field but the count, 0 to 1 (rev-3).
- **S12** — Finding 16 (M6). Arms 9k and 9m in `tools/run-gates/run-gates.test.sh` stop placing
  their signal with a fixed sleep. 9k's sleeper (`:3074`, `sleep 12`) polls every 0.1 s, up to a
  120 s hang bound, until `$TMPDIR/../1.retry.pid` exists, then lists the directory into `HV_PEEK`
  and exits 0. 9m's sleeper (`:3101`, `sleep 15`) polls the same way until `$TMPDIR/../1.retry.rc`
  exists, which means the tail attempt started and timed out beside it; 9m's sleeper becomes a
  committed fixture file, as 9k's is. Observed by AC13.
- **S13** — Finding 17 (M7). Arm 9f in `tools/run-gates/run-gates.test.sh` (`:2954`), before
  `unset HV_FLAG` at `:2979`, takes the newest `$H1/.git/gate-run/*/` record, reads the contended
  leg's key from field 7 of its `1.leg`, and asserts `$H1/.git/gate-cache/${k:0:2}/$k` does not
  exist. As the control, the spinner's key from field 7 of `0.leg` has its entry. The fixture is not
  rerun after `HV_FLAG` is unset. Observed by AC14.
- **S14** — Finding 7 (L1). `load_half` in `tools/run-gates/held_halves.py` (`:150`) opens the
  stdout file with `newline=""`, so `parse_verdicts` receives the runner's exact bytes and a bare CR
  in a failing leg's echoed output cannot split off a `GATE <verb> <name>` row. A `--selftest` arm,
  in Python, seeds a failing leg's output carrying `\rGATE ok    <other leg>` and asserts the per-leg
  view is unchanged. Observed by AC15.
- **S15** — Finding 8 (L2). One rule: the runner requires bash 5's `EPOCHSECONDS`, which every site
  but one already reads bare. The ticker's `${EPOCHSECONDS:-$(ts_now)}` (`:1433`) becomes
  `$EPOCHSECONDS`, as does `measure_foreign`'s `${EPOCHSECONDS:-0}` (`:3632`, the site AC16's count
  also finds, rev-3), the comment at `:1418`-`:1423` states the rule, and `ts_now` (`:1381`), whose last
  caller that was, is deleted. The turnstile suite's R6 extraction (`run-gates.turnstile.test.sh:377`)
  stops naming it, and `memory/map/generated/symbols.json` is re-rendered by `gen_map.py --write`.
  Observed by AC16.
  - **Readers:** by name: `tools/run-gates/run-gates.sh` defines and calls `ts_now`;
    `tools/run-gates/run-gates.turnstile.test.sh` extracts it by its definition line at `:377`;
    `.lexicon.conf` names it in a historical comment at `:117`, which is left as written;
    `memory/map/generated/symbols.json` lists it. by value: `ts_tick_start` in
    `tools/run-gates/run-gates.sh` writes its output into the heartbeat file on a shell without
    `EPOCHSECONDS`, a path no supported bash takes.
- **S16** — Finding 13 (L3). `runleg` in `tools/run-gates/run-gates.sh` (`:3326`-`:3331`) skips the
  durable `gate-logs/<leg>.log` write when its suffix is `.sample`, so the `log:` pointer
  `FAILED_LEGS` carries keeps naming the attempt that redded the run. An evidence arm on the
  nondeterministic path asserts the `log:` file holds the failing attempt's exit code. Observed by
  AC17.
- **S17** — Findings 14 and 22 (L4). `report_one` in `tools/run-gates/run-gates.sh` (`:3420` on)
  reads the two reuse markers and tails the leg's own line under the two-space tail contract: a leg
  with `$WORK/$i.sampled` prints `(sampled against a cached ok)`, and a leg with `$WORK/$i.aged`
  prints `(executed: reused on 10 runs in a row)`, on its `GATE ok` or `GATE FAIL` line. The `.aged`
  marker gains its first reader here; `TOOL-aSparedSpawn-17` keeps the marker for it. Canary arms
  assert both tails. Observed by AC18.
- **S18** — Finding 19 (L5). When `build_input_keys` (`:2813`) returns early on a failed step, or
  `REUSE_DIGEST` comes out empty, and the reuse mode is not off or a cache write was due, the runner
  prints one stderr line, `run-gates: reuse — the input keys could not be measured (<which step>), so
  nothing is reused or cached this run`. A canary arm (rev-3: the canary, not the evidence suite,
  because it also arms S4's two digest sites) breaks the digest step with a `git` shadowing
  `hash-object` and asserts the line. Observed by AC19.
- **S19** — Finding 23 (L6). `2026-10-09-spec-TOOL-aSparedSpawn-14.md`'s AC11 (`:295`) and its §7
  arm line (`:332`) name five checks (27, 29, 56, 69 and 88), the nine sites and the helper
  `print_env_failure` that shipped, so they agree with its S10. The spec takes rev-5 with a §9 line
  citing finding 23. Observed by AC20.

## 3. Non-goals (OUT)

- The three HIGH findings: id 3 is `TOOL-aSparedSpawn-17`, id 6 is `TOOL-aSparedSpawn-18`, and id 20
  with its duplicates 4 and 15 is `TOOL-aSparedSpawn-19`.
- The review's left-shift gates beyond the arms named in §2: the unit builder's per-pass
  `govkit selfcheck` and shell-hygiene check, check-arms comparing a floor against a diff's added
  arms, the fixed-sleep lint over the suites, the dead-plumbing grep over `$WORK` suffixes, and the
  `GATE_REUSE*` enumeration arm. Each is carried to the build's exit as an ask.
- S10 and its AC11, the reuse digest's view of a hook's environment, carried to the build's exit as
  a named ask (rev-3): the hook's `GIT_PREFIX` and Git for Windows' `LC_CTYPE` differ from a plain
  shell as well, and whether a locale may leave the key is the owner's ruling.
- Running any suite or the bar inside the build pass. The suites and the bar run once, at VERIFYING.
- A kit version bump. The main loop bumps every kit this unit touches once, after it.

### Edges

- **consumes-from** `TOOL-aSparedSpawn-17` — the `$WORK/$i.aged` marker stays written, so S17's
  `report_one` tail has something to read.

## 4. Design

Fixes at the sites the review located. Three registry repairs are measured from the tree (S1, S2,
S3), and S2 and S3 are measured last because every other item moves the bytes they count. S4 and S9
are arms and marks for the floors and the arms meta-gate. S6, S10, S11, S15, S16, S17 and S18 change
the runner or the hook and each carries an arm. S12, S13 and S14 change only suites. S19 is a record
correction.

### Reuse key and age (S10, S11)

S10's half is the exit ask's design since rev-3 and is not built here. The digest's env loop gains the five names to its `continue` arm. PATH is read once into a local,
its first `:`-separated component dropped when it equals `$GIT_EXEC_PATH`, its MSYS spelling
(`/c/...`), or ends in `/libexec/git-core`, and the `tool` lines resolve under that local through
`PATH=$stripped type -P`, which spawns nothing. With the schema at 4 every key changes, so no entry
earned under 3 is trusted.

The age count moves into the entry: `ok<TAB>secs<TAB>run id<TAB>HEAD<TAB>ended epoch<TAB>reuses`.
The reuse block reads it with the `read` it already makes and writes the entry back with the count
plus one. The cache block's reset at `:4819` goes, since an executed green writes a fresh entry with
count 0 and an executed red writes nothing.

### Inventory

No new function or variable family is minted. S15 deletes `ts_now`; S11 retires the
`age.<name key>` file kind. New arms reuse the helpers their suites already define
(`run_sp_verb` and `check_sp_value` in the canary, `ru_repo` and `ru_run` in the evidence suite,
`run_rp_push` in the pre-push suite, `arm_case` in `held_halves.py`'s selftest), so the lexicon leg
sees no new definition.

### Files touched (estimate)

- `tools/govkit/subject-pins.tsv`
- `memory/project/spawn-idiom-sites.txt`
- `memory/project/fork-ceilings.txt`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/run-gates/held_halves.py`
- `tools/run-gates/README.md`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `memory/map/generated/symbols.json`
- `memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-14.md`

### Alternatives rejected

- **Raise the spawn-idiom rows to their measured counts without rewriting any site.** The registry
  is shrink-only by design, and the sites this build added are its own to drain.
- **Keep the age count in a per-key `age.<key>` file.** Per-key files grow with every key ever
  reused and nothing prunes them; the entry already sits under the 30-day prune.
- **Restore the `EPOCHSECONDS` fallback at every converted site (L2's other option).** A
  `$(date +%s)` fallback is the BANNED `epoch-date` class, and no supported host lacks the variable.
- **Write sample runs to `<leg>.sample.log` (L3's other option).** It adds a file kind for a run
  whose output the run directory already keeps.
- **Have pre-push restore the pre-git PATH for the digest (M3's other option).** The runner would
  then trust a hook to shape its own key; stripping inside the digest serves every caller.

## 5. Production-readiness checklist

- security: S6 and S10 bound what the environment and the hook decide about a push bar's reuse; S11 makes a wrong entry's life follow its own key; no new input or write path.
- perf / scale: S10 and S11 add builtin work only; S2 removes forks; S3 records savings already made; S12 and S13 shorten no wait on the pass path and bound the red path at 120 s.
- error / empty / loading states: S18 prints the one line a silent key failure lacked; a malformed or five-field entry executes or reads as count 0.
- observability: S17 puts the sampled and aged facts on the leg's own line; S16 keeps the `log:` pointer on the failing attempt.
- risks: S10's schema bump makes the first reuse bar on each node cold; S11's in-place rewrite can be read torn, which executes; S15 drops a fallback no supported bash needs.
- testing: an arm per behavioural item, each observed red on a staged break first; the canary and evidence floors rise by what is added.
- migration: entries under schema 3 are no longer matched and age out under the 30-day prune; the old `age.*` files are left to no reader and the prune does not walk them.
- user docs: `tools/run-gates/README.md`'s reuse section states the per-key age, the digest's exclusions and the two tails.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs after S1, it exits 0 and prints no
  line naming `held-halves selftest`. Red when: the pin file still lacks the row, which is f479ba42's
  state.
- **AC2** — When the shell-hygiene leg's argv,
  `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`,
  runs after every other scope item has landed, it exits 0 with no finding. Red when: any registry
  row differs from the scan, in either direction.
  figure: DERIVED, the scan's own count at observation time.
- **AC3** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only run-gates-1leg`
  runs, and again with `--only run-gates-2leg`, each prints `fork-count: ok` for its row. Red when:
  either prints `STALE` or `RED`.
  figure: the counts 51 and 53 are PINNED, measured 2026-10-12 at f479ba42 on node a under bash
  5.3.9; the verdict is DERIVED at observation.
- **AC4** — When `python tools/memory-tree/check-arms.py --check` runs, it exits 0 and prints no
  `HYGIENE check-arms: tools/run-gates/run-gates.sh` line. Red when: one of the six sites stays
  unarmed and unpinned, or an arm asserts a shorter text than the site's signature.
  permission: the canary arms themselves execute at VERIFYING; this criterion reads their text.
- **AC6** — When a scratch clone with `.githooks/pre-push` installed pushes to a local bare remote
  with `GATE_REUSE_SAMPLE=0` and `GATE_REUSE_DAY=1` exported and `GOV_GATE_CMD` naming a stub, the
  hook's `not honoured from the environment by this bar:` line names both. Red when: either name is
  absent from the line, or the stub sees either knob set.
- **AC10** — When `grep -n 'by TOOL-aSparedSpawn-13 and -16' tools/run-gates/run-gates.evidence.test.sh`
  runs, it prints one `RAISED` line, and `FLOOR_ASSERTIONS` is that line's new value. Red when: no
  such line exists, which is f479ba42's state.
  permission: whether the floor sits at or below the executed count is observed when the suite runs
  at VERIFYING, and the ledger marks it OWED until then.
- **AC11** — MOVED TO THE BUILD'S EXIT WITH S10 (rev-3); not observed in this unit. When a scratch
  repository's bar earns an `ok` from a plain shell, and the runner then
  runs as a git alias child (`git -c alias.rg='!bash …' rg`), which receives the environment a hook
  does, with `GATE_REUSE=1`, it prints `GATE reuse` for the leg. Red when: the child executes the
  leg, which f479ba42 does because its digest hashes `GIT_EXEC_PATH` and the prefixed PATH.
- **AC12** — When a scratch repository reuses one leg's entry under key K1 nine times, then runs
  that leg under another key K2 on a dirty tree, then reuses K1 again, the runner's next K1 run after
  that executes it with the age line. Red when: the K2 execution resets K1's count, which the
  per-name `age.*` file does at f479ba42.
- **AC13** — When arm 9k's and 9m's blocks are sliced with the canary's prologue into a scratch
  script and run under twelve `true` fork loops, both pass, and `grep -n 'sleep 1[25]' tools/run-gates/run-gates.test.sh`
  finds neither sleeper. Red when: either sleeper still sleeps a fixed time.
  cost: the slice runs two tail-retry fixtures, about a minute on node a.
- **AC14** — When the runner's cache writer is staged to read `$WORK/$i.retry.rc` in place of
  `$WORK/$i.rc`, arm 9f's new assertion reds on a cache entry for the contended leg; unstaged, it
  passes and the spinner's entry exists. Red when: the staged break passes.
- **AC15** — When `python tools/run-gates/held_halves.py --selftest` runs, the new CR arm passes;
  with `load_half`'s `newline=""` removed it reds. Red when: the text-mode read passes the arm.
- **AC16** — When `git grep -n 'ts_now' -- tools/` runs, it prints nothing, and
  `grep -c 'EPOCHSECONDS:-' tools/run-gates/run-gates.sh` prints 0. Red when: either finds a site.
- **AC17** — When a scratch repository's leg reds then greens under `GATE_REUSE=1` and
  `GATE_REUSE_SAMPLE=1`, the `log:` file the run names opens with `exit 1`. Red when: it opens with
  `exit 0`, the sample run's, which is f479ba42's behaviour.
- **AC18** — When a scratch repository's leg is drawn by `GATE_REUSE_SAMPLE=1`, its line reads
  `GATE ok    <leg>  (sampled against a cached ok)`; with its age count at 10 the line carries the
  `(executed: reused on 10 runs in a row)` tail. Red when: either line is the plain one.
- **AC19** — When a scratch repository's bar runs with `GATE_REUSE=1` and a `git` wrapper first on
  its PATH that fails `hash-object`, stderr carries `the input keys could not be measured`. Red when:
  the run is silent, which f479ba42 is.
- **AC20** — When `grep -n 'print_env_failure' memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-14.md`
  runs, it prints AC11's bullet and the §7 arm line, and AC11 names five checks. Red when: AC11
  still says six checks or names `die_env` as the shipped helper.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` ·
`shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` ·
`harness arms (fail branches armed or pinned)` · `run-gates evidence` · `run-gates canary` ·
`run-gates gov canary` · `run-gates turnstile` · `run-gates run-log line` · `run-gates adopter e2e` ·
`profile-bar selftest` · `held-halves selftest` · `pre-push self-test` · `pre-push bar self-test` ·
`pre-push run-log line` · `push-main self-test` · `branch-guard self-test` ·
`python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` ·
`transition-audit arms` · `straggler-guard arms` · `recall floor arms` · `recall floor` ·
`memory hygiene` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/run-gates/run-gates.test.sh · covers AC4 AC13 AC14 AC18 AC19 · the calibrate verb with a blank spawn command and a failing spawn, fixed sleepers under load, the cache writer reading the retry, the plain leg line, a failing hash-object · FLOOR_ASSERTIONS, by S4
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC12 AC17 · a second key resetting the first's count, a sample run overwriting the log · FLOOR_ASSERTIONS, by S9
New arm: .githooks/pre-push.test.sh · covers AC6 · the two reuse knobs exported into a push · none
New arm: tools/run-gates/held_halves.py · covers AC15 · a text-mode read of a CR-bearing stdout · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft.
- rev-2 · 2026-10-12 · §1 §2 §3 §4 §5 §6 §7 S5 S7 S8 S10 S11 S12 S13 S14 S15 S16 S17 S18 S19 AC5 AC7
  AC8 AC9 AC11 to AC20 · the review converged and the owner rulings of 2026-10-04 promote one unit per
  HIGH and batch the MEDIUMs and LOWs into this one. S5 (id 3) with AC5 and AC9 went to
  TOOL-aSparedSpawn-17, S8 (id 6) with AC8 to TOOL-aSparedSpawn-18, and S7 (id 4) with AC7 to
  TOOL-aSparedSpawn-19, which takes id 20's duplicates. S10 to S19 add ids 11 and 21, 12, 16, 17, 7,
  8, 13, 14 and 22, 19 and 23, each with its own criterion. S4's two digest exits may be armed by
  S18's line instead of pinned.
- rev-3 · 2026-10-12 · §2 §3 §4 §6 §7 S2 S4 S9 S10 S11 S12 S15 S18 AC11 · the build pass forced these.
  S10 with AC11 moves to the build's exit as a named ask: a hook's environment on node a also differs
  by `GIT_PREFIX` and Git for Windows' `LC_CTYPE`, and dropping a locale from the key is the owner's
  call. S4's digest exits are marked and armed by S18's canary arm, which is the canary's because
  check-arms reads this gate's arms there alone, so `unarmed-branches.txt` leaves the files touched.
  S11's Readers gain the evidence AC5 arm and unit 17's AC1 arm, whose key is read from the earning
  run because a reused leg writes no record row. S15 makes `measure_foreign`'s fallback bare too,
  which AC16's count finds. S9 counts unit 13's forty-one and this unit's four, 163 to 208. S2 sets
  the canary's `var-pipe` row to its measured count. S12's 9m sleeper is a committed fixture file.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "quarantine a leg whose cached ok disagrees with an executed red"`
ranks generic `ok` and `leg` helpers and no reuse seam; no new seam is built. Each fix extends the
code that already owns its case: S6 the hook's `ENV_CLEARED` scrub that clears `GATE_REUSE_PUSH`
and `GATE_DOCS_BASE`; S10 the `REUSE_DIGEST` env loop's own exclusion arm; S11 the cache entry
`TOOL-aSparedSpawn-13` writes and the 30-day prune that already walks it; S17 `report_one`'s
two-space tail contract; S1 govkit's own `selfcheck --write` generator; S4 check-arms' marker and
pin grammar.

Recall terms used: cache disagreement quarantine sampled age bound GATE_REUSE_PUSH ENV_CLEARED
REUSE_DIGEST GIT_EXEC_PATH subject pins spawn idiom registry fork ceilings FLOOR_ASSERTIONS
