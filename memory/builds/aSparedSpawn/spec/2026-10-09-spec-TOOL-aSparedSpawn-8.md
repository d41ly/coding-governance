# TOOL-aSparedSpawn-8 — fork-free readers, a spawn-idiom lint that stops regrowth, and a fork-count arm

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Under MSYS a `$(f …)` call of a shell function forks a whole subshell, 89 to 315 ms on node `a`, and
when `f`'s body starts no process that fork buys nothing. The round-two spawns census counted 722 such
sites at `6bc6c949c`, 368 in product and 354 in suites, 290 of them in the unattended driver alone
(`memory/builds/aMeteredSweep/build/2026-10-09-build-TOOL-aMeteredSweep-1-research2-spawns.md` §2.2).
This unit converts the product sites in the hottest files to out-variable readers, bans the three
spawn idioms that have no false positive, carries every other spawn idiom in a shrink-only registry,
and pins the forks per invocation of each hot entrypoint under a clock-free ceiling, so a saving shows
as a falling ceiling and regrowth reds instead of costing the next build a day.

## 2. Scope (IN)

- **S1** — `fact`, `runmd_of` and `readme_of` in `tools/unattended/unattended.sh` adopt the global-out
  convention `normpath` already set at `tools/unattended/lib-unattended.sh:635`: each sets a fixed
  global, still prints, and clears the global first so a miss never leaves the previous answer. Every
  `$(fact …)`, `$(runmd_of …)` and `$(readme_of …)` site in the driver becomes `f … >/dev/null; v=$G`,
  keeping the `fact <file> <key>` spelling that check 39 of `tools/unattended/check-unattended.sh`
  reads. Observed by AC1 and AC2.
- **S2** — In `tools/unattended/check-unattended.sh`, `fact_of` takes the same convention, and
  `core_of` and `read_bare_const` read every driver constant through ONE `awk` pass into two
  associative arrays, first match winning and an absent key reading empty, as the loop does today.
  Observed by AC3.
- **S3** — The other product leaf-pure readers the census ranks are converted the same way:
  `declared_scalar` and `declared_list` in `tools/unattended/check-playbook.sh` and the driver,
  `first_of` in `tools/check-wiring.sh`, `ask_home_of` and the residual `$(normpath …)` sites in
  `tools/unattended/lib-unattended.sh`. Each callee's body is read for `cd`, `set`, `trap`, `exit` and
  global writes first; a callee that has one keeps its substitution and carries a registry row whose
  reason names the side effect. Observed by AC4.
- **S4** — `tools/gate-lint/sh_hygiene.py` gains a third mode, `--spawn-idioms`, over the population
  of the location-probe mode (`. :!*.test.sh :!memory/`), reusing `extract_code`, the quoted-heredoc
  skip, `read_registry` and `check_registry`. Three classes are BANNED with no registry escape:
  `epoch-date`, `cat-heredoc` and `redirected-read`. Observed by AC5 and AC6.
- **S5** — The product sites of the two non-empty BAN classes are drained in this unit. Each
  `$(date [-u] +%s)` becomes `$EPOCHSECONDS` and each `$(date +%s%N)` becomes `${EPOCHREALTIME/[.,]/}`
  scaled. Each `"$1" -c "$(cat <<'RKD'` wrapper reads its heredoc with `IFS= read -r -d ''` first,
  and the byte-identical region between the `resolve_kit_dir` markers is untouched. Observed by AC6
  and AC7.
- **S6** — The REGISTRY classes are counted per (path, class), set and count equal in both
  directions, in a new file under `memory/project/` that `.memory-tree.conf` adds to
  `PROJECT_REGISTRY_EXTRA`: `pure-fn-subst`, `printf-subst`, `cat-file`, `path-subst`, `date-fmt` and
  `var-pipe`, with the predicates of the census's §4.1 table. Its rows land at what the scan measures
  after S1 to S5. Observed by AC6 and AC8.
- **S7** — The mode is wired as a leg: a manifest row in `tools/gate-legs.json`, `subject = repo`, no
  guard, a declared ceiling; a `[[gate_leg]]` block in `tools/gate-lint/kit.toml`; and a line in the
  gate-lint dossier `memory/map/features/gate-lint.md`. Observed by AC6.
- **S8** — A fork-count arm, a bash script under `tools/gate-lint/`, counts forks per invocation of
  each declared entrypoint through `env SHELLOPTS=xtrace BASH_XTRACEFD=<fd>` with a `PS4` carrying
  `${BASHPID}` and `${BASH_SOURCE##*/}:${LINENO}`. Forks are the distinct `BASHPID` values less one.
  It calibrates on a specimen first and refuses when the counter disagrees. It reds on growth above a
  declared ceiling and on a ceiling more than max(3, 5 %) above the count. An entrypoint it could not
  run prints the `skipped` shape. No clock is read anywhere. Observed by AC9, AC10 and AC11.
- **S9** — The declared entrypoints, the census's §2.5 ranking: `tools/unattended/unattended.sh` on
  a cheap verb, `tools/unattended/check-unattended.sh` on a minimal fixture,
  `tools/run-gates/run-gates.sh` on a one-leg and a two-leg `GATE_LEGS` manifest,
  `tools/memory-tree/check-memory-hygiene.sh` on a scratch tree, `skills/session-kickoff/manifest-check.sh`
  and `tools/check-wiring.sh --check`. Each ceiling lands at the count measured after S1 to S5, and
  the count at the base is recorded beside it. Observed by AC12.

## 3. Non-goals (OUT)

- Suite sites. Whether they are drained here or carried as registry rows is F2; either way a suite
  file is not converted before the product files are.
- The driver prelude's own spawns: `$(basename "$0")`, `$(dirname "$0")`, the generated-index and
  shared-record resolvers at `tools/unattended/unattended.sh:653-662`, and the lazy preamble.
- The cross-process memo of `resolve_python` (census R7) and of the `timeout -k` capability probe
  (R8). Both trust an inherited variable, which is a contract change of its own.
- The loop classes `spawn-in-loop` and `interp-per-item`, which need a loop parser this mode does not
  have. They are follow-ups once the registry has a steady state.
- `build_commit`'s range memo, which `TOOL-aSparedSpawn-11` owns, and the per-record `## Run facts`
  parse in the checker's record loops.
- `ask_rank_order`'s quadratic sort and the hygiene checker's `PRE_*` count pipelines.

### Edges

- **hands-off** `TOOL-aSparedSpawn-6` — the driver as a library, `load_driver_conf` and `main` with
  suites sourcing it once per shard, and the prelude spawns listed above. This unit declares the
  driver entrypoint's fork ceiling, so that unit's saving lands as a lowered row in the same registry.

## 4. Design

### The out-variable convention

The convention exists: `normpath` leaves its answer in `_np` and a hot caller writes
`normpath x >/dev/null; v=$_np` (`tools/unattended/lib-unattended.sh:635-638`, verified at
22efab65). This unit applies it to readers whose body is pure bash. Four traps from census §3 R1 bind
every conversion:

- **Keep the call spelling.** Check 39 (`tools/unattended/check-unattended.sh:5738-5764`) recognises a
  phase read by the regex `fact[ \t]+[^ \t]+[ \t]+phase`, and asserts its two readers still match it
  (`C39-READERS-SEEN`). A spelling such as `fact -v v f phase` would make that check blind, not red.
- **Fixed global name per function**, never a `-v name` parameter: `printf -v "$1"` writes into the
  callee's own `local` when the caller passes a colliding name.
- **No trailing newline in the global.** `fact` prints `"%s\n"` and `$(…)` stripped it.
- **Clear first.** `fact` returns 1 on a missing file before reading; the global must be empty then,
  or the caller reads the previous key's value.

### The `--spawn-idioms` mode

Same architecture as `--location-probes` (TOOL-aGraftedHelix-45): the tracked `*.sh` plus shebang
shell files, narrowed by pathspecs; the comment cut and the quoted-heredoc skip, so embedded Python
and written specimens are data; a registry keyed on (path, class) and never on a line, because a
line-keyed registry reds on an unrelated edit above the site. Populations and near-miss counts print
on every run, green included. The header states what it does not check: execution frequency, `eval`
and code built in variables, substitutions split across a continuation, transitive purity, repeated
identical `git` queries, cross-process probes, and the cost of fork-free work such as a bash `read`
loop over a 13k-line file. Those last three are why S8 exists.

| class | predicate, on the code half | gating |
|---|---|---|
| `epoch-date` | `$(date` `[-u]` `+%s)` or `+%s%N)` | BAN |
| `cat-heredoc` | `$(cat <<` | BAN |
| `redirected-read` | `$(<` followed by another redirection inside the same substitution | BAN |
| `pure-fn-subst` | `$(f …)`, f defined in the file or a library it sources by literal path, body spawning nothing | registry |
| `printf-subst` | `$(printf FMT ARGS)` with no pipe or redirect, FMT not ending `\n` | registry |
| `cat-file` | `$(cat "<one word>" [2>/dev/null])` | registry |
| `path-subst` | `$(basename`, `$(dirname` | registry |
| `date-fmt` | `$(date [-u] +FMT)` with no `-d`/`-r`, FMT free of `%N`, `%:z`, `%-`, `%_` | registry |
| `var-pipe` | `printf`/`echo` of one expansion piped into `grep -q/-c`, `wc -l`, `tr`, `sed s///`, `head -1`, `cut` | registry |

`redirected-read` has no site in the tree today (`git grep` at 22efab65), and it is banned because
`$(<f 2>/dev/null)` reads EMPTY and still forks: any extra redirection defeats bash's special case
(census §3 R3, verified on bash 5.3.9). `pure-fn-subst` grades a callee that calls another function as
impure, which is a MISS and never a false red.

### The `cat-heredoc` drain

The `"$1" -c "$(cat <<'RKD'` line sits OUTSIDE the `# >>> resolve_kit_dir` marker region in every copy
checked (`tools/unattended/lib-unattended.sh:132-134`), so the gated byte-identical region is not
re-rendered; each wrapper is edited in place. `read -r -d ''` returns 1 at EOF, so it carries `|| :`
under `set -e`, and it keeps the trailing newline `$(…)` stripped. The two non-resolver sites in
`tools/unattended/check-unattended.sh` (`:4726`, `:4900`) convert the same way.

### The fork counter

Prototyped in round two as `forkcount.sh` and verified on one specimen (census §4.2). `SHELLOPTS` is
readonly in bash, so it is set through `env`; exported, it makes every child `bash` script trace too.
The count is a deterministic LOWER bound: a subshell that traces no command of its own is unseen, and
on the specimen it read 7 pids against 8 forks. A red prints the delta and the top ten `file:line`
contributors, never a bare total. The calibration specimen is written at run time from a quoted
heredoc inside the script, so the S4 scan reads it as data and never as a site. Python and node
children count once each and their own subprocesses are invisible; the header says so.

### Inventory

| identifier | kind | cell that grades it |
|---|---|---|
| `_fact`, `_runmd`, `_readme`, `_fact_of` | shell globals | none: globals are not graded |
| `_CORE`, `_BARE` | shell associative arrays | none |
| `--spawn-idioms` | CLI flag of `sh_hygiene.py` | none |
| `scan_spawn_file`, `scan_spawn_tree`, `run_spawn_scan`, `print_spawn_populations` | Python functions | `lexicon naming predicates`, python cell |
| `measure_forks`, `read_budgets`, `check_budgets`, `print_contributors` | shell functions | `lexicon naming predicates`, shell cell |
| `shell hygiene (a fork spent on builtin work)` | leg name | none |
| `spawn budget (forks per hot entrypoint)` | leg name | none |

Every name is confirmed through `python3 tools/lexicon/lexicon.py --suggest` at build time.

### Files touched (estimate)

- `tools/unattended/unattended.sh`, `tools/unattended/lib-unattended.sh`,
  `tools/unattended/check-unattended.sh`, `tools/unattended/check-playbook.sh`, `tools/check-wiring.sh`
- `tools/gate-lint/sh_hygiene.py`, `tools/gate-lint/README.md`, `tools/gate-lint/kit.toml`
- `tools/gate-legs.json`, `.memory-tree.conf`, `memory/map/features/gate-lint.md`
- S5's drain: `tools/run-gates/run-gates.sh`, `tools/run-gates/run-selftests.sh`, `tools/push-main.sh`,
  `skills/session-kickoff/manifest-check.sh`, `tools/unattended/resume-tick.sh`,
  `tools/unattended/run-unattended-gates.sh`, `tools/check-install-prefix.sh`,
  `tools/check-kit-versions.sh`, `tools/check-playbook-parity.sh`, `tools/lexicon/adopt-lexicon.sh`,
  `tools/lib/render-doc.sh`, `tools/memory-tree/adopt-memory-tree.sh`,
  `tools/memory-tree/check-verdict-epoch.sh`, `tools/unattended/adopt-unattended.sh`,
  `tools/workflows/check-review-join.sh`, `tools/workflows/check-verifier-fanout.sh`
- New, not yet tracked: the fork-count script under tools/gate-lint/, and two registries under
  memory/project/, one for spawn-idiom counts and one for fork ceilings.

### Rollout

The lint and the counter land first and red nothing: the registry's rows and the ceilings are the
measured tree. S1 to S3 and S5 then each lower a row or a ceiling in the same commit as the edit, so
every saving is a visible diff on a shrink-only file rather than a claim.

### Alternatives rejected

- **A `-v name` parameter on each reader.** Collides with the callee's own locals, and changes the
  spelling check 39 reads.
- **`${ cmd; }` funsub.** A parse error on CI's bash 5.2.
- **A `read` loop in place of the `awk` behind `core_of`.** A bash `read` over the 13,310-line driver
  took 2,026 ms measured; above about 1-2k lines one `awk` is cheaper (census §1).
- **Counting forks with a clock.** The clock arms are what aMeteredSweep had to recalibrate on a
  loaded host; a trace count cannot flake.
- **A line-keyed registry.** Reds on an unrelated edit above a waived site (`install-prefix waivers
  are line-keyed`).

## 5. Production-readiness checklist

- security — No new write path; the lint and the counter read tracked files and a scratch fixture.
- perf / scale — The lint is one python pass, about 1 s; the counter about 1-3 min quiet (census §4.2).
- error / empty / loading states — An empty population and a counter that fails calibration refuse
  with exit 2; an entrypoint that cannot run prints the `skipped` shape and is never a pass.
- observability — Both legs print populations, near misses and every registry reason on green runs;
  a growth red prints the top ten `file:line` contributors.
- risks — A converted reader whose callee had a side effect changes behaviour; S3's read is the guard.
- testing — `sh_hygiene.py --selftest` specimens per class in both directions, and the counter's own
  `--selftest` with the calibration break staged.
- migration — Kit versions bump once after the last move in each touched kit; `gen_map.py --write`
  runs after the new shell functions land.
- user docs — `tools/gate-lint/README.md` documents the mode, the registry grammar and the counter.

## 6. Acceptance criteria

- **AC1** — When `grep -o '\$(fact '` runs over `tools/unattended/unattended.sh` after the pass, it
  prints nothing, and `fact` sets `_fact` byte-equal to the old printed value for a fixture `RUN.md`
  holding a valueless key, a CRLF line, and a key-shaped line above `## Run facts`.
  Red when: `_fact` keeps a trailing newline or CR, or a missing file leaves the previous value in it.
  fixture: a scratch `RUN.md` the build writes; the tree holds none to borrow.
- **AC2** — When a converted `fact <file> phase` read is moved into a function outside the two readers
  in a scratch copy of the driver, check 39 of `tools/unattended/check-unattended.sh` reds naming that
  line, and on the unbroken tree it is green with `C39-READERS-SEEN` reached.
  Red when: the staged break passes, which means the conversion changed the spelling check 39 reads.
- **AC3** — When `core_of` and `read_bare_const` are called for every `^[A-Z_]+=` key of
  `tools/unattended/unattended.sh` at base and after the pass, the two answer sets are identical, an
  absent key answering empty in both.
  Red when: any key differs, or a key declared twice answers its second value.
- **AC4** — When `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms` runs after the pass, no
  `pure-fn-subst` row names a converted file unless its reason names the callee's `cd`, `set`,
  `trap`, `exit` or global write.
  Red when: a row for a converted file carries a reason naming no side effect.
- **AC5** — When `python3 tools/gate-lint/sh_hygiene.py --selftest` runs, each class in the §4 table
  fires on its specimen and stays silent on its near miss, and a registry row naming a BAN class is
  refused rather than honoured.
  Red when: a specimen inside a quoted heredoc or a comment fires, `$(<f)` with no further redirect
  fires, or a BAN row greens its site.
- **AC6** — When `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms` runs over the tree with the
  new registry after the pass, it exits 0, prints each class's scanned, gated and near-miss counts,
  and reports zero sites for each BAN class; with one `x=$(date +%s)` added to a product file in a
  scratch clone it exits 1 naming the file, line, class and `$EPOCHSECONDS`.
  Red when: the scratch break exits 0, or an empty population exits anything but 2.
  figure: every count is DERIVED by the run, none is typed into the registry header.
- **AC7** — When `resolve_kit_dir` is called through the converted wrapper in
  `tools/unattended/lib-unattended.sh` and through the base wrapper, for a receipt hit, a probe hit and
  a refusal, stdout, stderr and exit code are identical.
  Red when: any differs, or the `read -r -d ''` exit 1 at EOF aborts a `set -e` caller.
- **AC8** — When a converted site is reverted to `$(fact …)` in a scratch clone, `--spawn-idioms`
  exits 1 naming the (path, class) count mismatch; when a registered site is converted and its row is
  left unchanged, it exits 1 naming the stale row.
  Red when: either staged break exits 0.
- **AC9** — When the fork-count script's `--selftest` runs, its calibration on the specimen equals the
  specimen's declared count on two consecutive runs; with the declared count edited by one in a
  scratch copy it refuses with exit 2 and the line "the counter cannot move".
  Red when: the two counts differ, or the edited declaration does not refuse.
- **AC10** — When one `$(:)` is added to the prelude of `tools/unattended/unattended.sh` in a scratch
  clone, the arm reds for the driver entrypoint, printing measured, ceiling, delta and the top ten
  `file:line` contributors with the added line among them.
  Red when: the arm stays green, or prints a bare total.
- **AC11** — When one ceiling row is raised to max(3, 5 %) plus one above its measured count, the arm
  reds naming the stale row; when an entrypoint's fixture cannot be built, it prints
  `skipped — <id> · <why>` and the run's summary does not count that row as passed.
  Red when: the raised row passes, or the unrunnable row is silent or counted.
- **AC12** — When the arm runs at base 22efab65 and at the pass's tip, the per-entrypoint fork counts
  are recorded side by side in the build folder, and the count for `tools/unattended/unattended.sh` is lower at the tip.
  Red when: the driver entrypoint's tip count is not lower than its base count.
  cost: two runs of the arm, about 1-3 min each quiet by the census's estimate.
  figure: both counts DERIVED at observation; the census's ~17 avoidable prelude forks are a hint.

## 7. Gates

`codebase-map kit selftest` · `kit/dogfood doc parity` · `lexicon naming predicates` · `lexicon selftest` ·
`manifest-check self-test` · `playbook parity selftest` · `recall floor` · `recall floor arms` ·
`review-join self-test` · `run-gates gov canary` · `run-selftests self-test` · `scratch-guard self-test` ·
`shell-hygiene selftest` · `straggler-guard arms` · `tier2-review self-test` · `transition-audit arms` ·
`unattended-build self-test` · `verifier fan-out self-test` · `run-gates canary` ·
`shell hygiene (a loop fed by a command substitution)` ·
`shell hygiene (a location probe asked from a moved directory)` · `unattended kit gate` · `memory hygiene` ·
`kit version markers` · `kit epoch (shipped bytes move, the version moves)` ·
`verdict epoch (kit version dates the engine)` · `govkit selfcheck` · `codebase-map coverage + freshness` ·
`harness arms (fail branches armed or pinned)` · `leg ceilings clear their evidenced maximum` ·
`spec tokens (a spec's own names resolve)`

New arm: tools/gate-lint/sh_hygiene.py --selftest · covers AC5 AC8 · a specimen per class both ways, and a row naming a BAN class · the selftest's assertion floor rises by the arms added
New arm: tools/gate-lint/sh_hygiene.py --spawn-idioms, as a new manifest row · covers AC4 AC6 · one `$(date +%s)` added to a product file in a scratch clone · none
New arm: the fork-count script under tools/gate-lint/, as a new manifest row · covers AC9 AC10 AC11 · a `$(:)` in the driver prelude, and a ceiling raised past the stale margin · none

The two new legs are not on the line above because they do not exist until the pass adds them. The
held unattended driver and gate suites cover S1 and S2 at the owner's manual run of the merged tree.

## 8. Open questions

- **F1 — Which bash a ceiling is declared for.** Fork counts differ by bash version: `$(<f)` does not
  fork on 5.3 and still forks on CI's 5.2, and resolver candidates differ between Windows and Linux.
  - (a) One row per (entrypoint, bash major.minor); an undeclared version prints the `skipped` shape.
  - (b) One row per entrypoint holding the maximum across the platforms that run it.
  - (c) Run the arm only on node `a`'s bash and announce the skip everywhere else.
  - Recommendation: (a). It keeps the stale-ceiling red meaningful on each platform, which (b) loses.
- **F2 — Suite sites in this unit or after it.** The census counted 354 leaf-pure suite sites, led by
  `tools/workflows/unattended-build.test.sh`, `stop-guard.test.sh` and `transition-audit.test.sh`.
  - (a) Carry them as registry rows now, drained by a follow-up unit; this unit converts product only.
  - (b) Convert the top suite files in this unit, after the product files.
  - Recommendation: (a). The registry already stops regrowth, and a suite edit costs its own arm
    inventory compare.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The probe `tools/codebase-map/reuse_lookup.py "fact reader out variable normpath global"` ranks
`normpath` (`tools/unattended/lib-unattended.sh`, fan-in 6, SEAM): S1 to S3 extend its global-out
convention rather than inventing one. The lint extends `tools/gate-lint/sh_hygiene.py`'s
`extract_code`, `read_registry` and `check_registry`, the reuse TOOL-aGraftedHelix-45 made for its
second mode; the probe "shell source lint with a count registry keyed on file and class, shrink-only"
ranked only name-stem hits (`key`, `counts`) and did not surface them, so the seam is named from the
file. For the fork counter no existing seam fits: `tools/lib/lib-selftest.sh` records that its own
spawn counter was taken out and that a `PS4` trace gave the attributable figure, which is prose and
not a function to call.

Recall terms used: normpath _np fork command substitution sh_hygiene registry location-probe waivers
shrink-only spawn ceiling xtrace
