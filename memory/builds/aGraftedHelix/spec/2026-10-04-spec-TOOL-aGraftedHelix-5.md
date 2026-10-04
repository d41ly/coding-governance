# TOOL-aGraftedHelix-5 — each leg reading is stamped faithful or contended by a foreign-load census, and only faithful readings argue a ceiling

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 7 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/run-gates/derive-ceilings.py` argues every ceiling from the per-run leg readings under
`<git-dir>/gate-run/<runid>/`, and a reading taken while another session's suite or another clone's
bar loaded the host reads exactly like a slow leg. This unit takes a census of foreign gate work
while each leg runs, writes it into the leg's row as interface I6's `foreign` field, and makes the
evidence tool argue only from readings whose census found none, saying how many it set aside.

## 2. Scope (IN)

- **S1** — `measure_foreign` in `tools/run-gates/run-gates.sh` reads ONE `ps -ef` snapshot and
  prints the number of foreign process trees doing this repository's gate work, then the trees'
  roots. A row is gate work when its line names a script some manifest leg runs, the runner itself
  or its sibling `run-selftests.sh`, or carries a word ending `.test.sh` or `selftest.py`. The
  runner's own ancestors and descendants are never foreign, and a tree counts once, at its topmost
  matching process. It prints `unknown` when `ps` fails, when the header names no PID or PPID
  column, or when the snapshot holds no row for the runner itself. Observed by AC1, AC2 and AC3.
- **S2** — `arm_census` starts, at the first dispatch and beside `arm_wall`, a detached sampler
  shaped like `ts_tick_start`. It truncates the run record's `census` file, appends one sample at
  once, then appends one every `CENSUS_EVERY` seconds until the runner is gone or the run stops it.
  `CENSUS_EVERY` is 60, and `GATE_CENSUS_EVERY` overrides it with a positive integer; any other
  override value prints one `run-gates: NOTE` line and keeps 60. A first sample reading `unknown`
  prints one `run-gates: NOTE` line on stderr. Observed by AC3, AC4 and AC5.
- **S3** — `runleg` writes the eighth field of every `.leg` and `.retry.leg` row from
  `derive_foreign`: over the samples stamped inside `[start − 3 × CENSUS_EVERY, end]`, the largest
  positive count; else `unknown` when any sample there reads `unknown` or none exists; else `0`.
  Observed by AC1, AC3 and AC5.
- **S4** — Every reader of a `.leg` row in the runner keeps its arity: the ledger block's read at
  `tools/run-gates/run-gates.sh:3128` takes field 7 alone, so `gate-ledger.tsv` stays five fields.
  Observed by AC6.
- **S5** — `read_runs` in `tools/run-gates/derive-ceilings.py` sets aside every reading its
  admission rule admits whose eighth field is not `0`, under one reason each, first match: a
  positive integer is `contended`, and anything else, a seven-field row included, is `uncensused`.
  `--report` prints a `# set aside:` line with the count per reason and an `aside` column, names a
  leg whose every reading was set aside on its own line rather than as UNBACKED, and keeps DEAD
  PROBE for a record holding no reading at all. `--write` names the same counts on its summary line
  and, when everything was set aside, holds every evidence row without reporting DEAD PROBE.
  Observed by AC7 and AC8.
- **S6** — The run header gains `census_every`, outside the four-key envelope block. The README's
  run-record and ceiling sections, the `derive-ceilings.py` docstring, the header lines `--write`
  generates into `tools/run-gates/ceiling-evidence.txt` and the run-gates dossier say what the field
  means and what the census cannot see. Observed by AC9.
- **S7** — The run-gates kit version moves once, after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs, and the kickoff manifest's audit stamp is renewed because the
  runner is on its watch list. Observed by AC10.
- **S8** — `tools/run-gates/run-gates.evidence.test.sh` carries this unit's arms, every existing
  derive-ceilings fixture row gains an eighth field of `0` so it stays admitted, and its
  `FLOOR_ASSERTIONS` rises by the arms added. NOT OBSERVED: a suite is the close's to run, and each
  arm's red on a staged break is observed there (§7).

## 3. Non-goals (OUT)

- Contention from the bar's OWN neighbours. `measure_neighbours` and the deferred serial retry own
  it (`TOOL-dDerivedDocket-26`), and the census excludes the bar's own tree by construction.
- Load that is not shaped like this repository's gate work: another repository's build under other
  script names, an on-access scanner, an agent's own CPU, and on Windows any process no MSYS shell
  spawned. The runner's header for the census says so.
- A verdict. The census never turns a leg into a pass, a skip or a red, and it never lowers a
  ceiling: the evidence file stays monotone and `--check` still reads tracked files only.
- The self-test runner's readings. `tools/run-gates/selftest-budgets.txt` and
  `tools/run-gates/selftest-pooled-evidence.txt` are separate evidence artifacts with their own
  writers, and M2 puts a separate artifact in a separate unit.
- Memory pressure as a reason to set a reading aside. That is `TOOL-aGraftedHelix-7`'s pause
  record, which builds on the set-aside path this unit adds.
- No new gate leg, kit, conf key or profile knob.

### Edges

- **hands-off** `TOOL-aGraftedHelix-7` — the set-aside path in `derive-ceilings.py`, its `aside`
  column and its `# set aside:` line, which that unit extends with a `paused` reason read from the
  run record's `pauses` rows.

## 4. Design

### Data model

```
<i>.leg     name  status  rc  seconds  started  ended  key  foreign      (I6: TAB, one row)
foreign     a non-negative integer, or the literal `unknown`
census      <epoch-s> TAB <count|unknown> TAB <pid>:<token> [<pid>:<token> ...]   (one line per sample)
header      census_every TAB <seconds>
```

`census` lives in the run record beside the `.leg` rows, inside the mode-700 run directory. A root is
written as its pid and the token that matched it, never its command line: a command line can carry
a credential, which is why the runner already redacts every durable `.out` copy.

### The census predicate

The tokens are derived once, after the manifest parse, from `argvs[]`: every argv word that carries
a `/` and ends `.sh`, `.py` or `.js`, plus `$KITREL/run-gates.sh` and `$KITREL/run-selftests.sh`.
They go to one file in the run's scratch directory, which the census `awk` reads first. One snapshot
then decides everything, in one `awk`:

1. PID and PPID are located by the header's own column names, so procps and MSYS `ps -ef` both
   parse; a row whose PID or PPID is not a number is the continuation of a multi-line argv and is
   skipped, the guard `scan_descendants` already carries.
2. A row matches when any token is a substring of the WHOLE row, or a word of it ends `.test.sh` or
   `selftest.py`. The whole row, because a start time printed with a space shifts every later
   column.
3. Excluded: the runner's ancestors, walked up by PPID from `$$`, and its descendants, every row
   whose PPID chain reaches `$$`.
4. A root is a matching, non-excluded row whose parent is not one. The count is the root count.
5. `unknown` when the header lacks either column or no row carries `$$`: a snapshot that cannot see
   its observer is not a census of the observer's host.

Run over the real process table on node `a`, 2026-10-04 at 18:53 +03:00 (invariant 7). `ps -ef`
printed ten rows. Hit: another session's `timeout 1200 bash tools/unattended/check-unattended.sh`,
launched in a sibling worktree, as the tree 1927, 1929, 1930, 11035, 11043, which is ONE root at
1927 because that `bash -c` wrapper's own argv names the script. Seven rows matched nothing. Near
miss, by shape: every agent session's `bash -c` wrapper carries its whole command text, so the
wrapper of a session that runs the bar names the runner's path, and only the ancestor walk keeps it
out. A second snapshot at 19:16 showed a live continuation row from another session's multi-line
wrapper, which step 1 skips, and a native `python.exe` that an MSYS shell launched, listed with its
full command line, so a python leg run by another session is visible.

### The sampler

`arm_census` follows `ts_tick_start` property by property: a subshell whose stdio goes to
`/dev/null`, disowned so `live()` never counts it, exiting when `kill -0` on the runner fails or a
disarm marker exists in the scratch directory. The first sample is taken before the loop and
before the first leg dispatches, so every leg has one inside its window. The run stops it beside
`remove_wall_watcher`, and `cleanup` stops it on a signal. A `kill -9` on the runner leaves it to
exit at its next tick, holding no descriptor of the caller's.

Cost, PINNED on node `a` 2026-10-04: `ps -ef` 27 ms per snapshot, 20 in 0.543 s, and an `awk`
spawn 25 ms, so one sample is two spawns and about 52 ms on a quiet host. At 60 s that is 120
spawns an hour, off the dispatch path. The runner's own comment records a loaded `ps -ef` at 0.4 s
to 3.2 s; detached, that cost delays a sample and never a leg.

The window reaches `3 × CENSUS_EVERY` before a leg's start because `sleep` on node `a` delivered
1.65 to 1.93 times its nominal seconds under load, the wall watcher's measurement in the same file.
A reach of one period would leave a short leg with no sample at all under that drift.

### Evidence admission

`read_runs` applies the existing window rule first and the census second, so a row the window
refuses was never evidence and is not counted as set aside. The reasons are a module constant,
`("contended", "uncensused")`, in first-match order, and `read_runs` returns the admitted readings
beside a per-leg count of set-aside readings per reason. `cmd_report` and `cmd_write` read both.

A legacy seven-field row is `uncensused`. Measured on node `a`'s primary tree at writing time: five
retained runs, 284 leg rows, every one seven fields. After landing all of them are set aside, and
the tracked evidence holds by monotonicity until a censused bar runs; `--write` prints that rather
than DEAD PROBE.

`--report` keeps its table and appends `aside` as the last column. One header line follows the
existing two: `# set aside: <c> contended, <u> uncensused — readings that argue no ceiling`.

### Inventory

| Identifier | Cell |
|---|---|
| `measure_foreign`, `arm_census`, `derive_foreign`, `remove_census_watcher` | `sh.function` |
| `CENSUS_EVERY`, `GATE_CENSUS_EVERY` | constant and its override, no cell |
| `foreign`, `census`, `census_every` | I6 field, run-record file and header key, no cell |

Each function name was answered `OK` by `python tools/lexicon/lexicon.py --suggest <name> --as
sh.function`. No Python function is added; `read_runs` changes its return value. No gate leg, kit,
hook, guide, workflow script or lexicon verb is added, so the codebase map owes no claim; if
`python tools/codebase-map/gen_map.py --check` reports the generated map stale, it is re-rendered
with `--write` in the same commit.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/derive-ceilings.py`
- `tools/run-gates/ceiling-evidence.txt`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.evidence.test.sh`
- `memory/map/features/run-gates.md`
- `memory/guides/SESSION-KICKOFF.md`

The evidence file moves in its generated header lines only, by one `--write`; its rows hold.

### Alternatives rejected

- **A host load reading** (`/proc/loadavg`) — F1: it costs six times a snapshot and reads the
  bar's own load.
- **A beacon the repo's suites take** — F1: the foreign work live on node `a` takes none.
- **A census at each leg's start and end only** — F2: it leaves the middle of the long legs blind.
- **Admitting an `uncensused` reading as before** — the roster's mechanism is that only faithful
  readings argue, and a reading the census could not grade is not known faithful
  (`memory/gotchas/degradation-known-but-unreported.md`).
- **A profile knob for the period** — no host has asked for a different one; the override serves
  the fixtures and a knob would cost the canary's pinned set.

## 5. Production-readiness checklist

- security — The census writes pids and matched tokens, never command lines. The run record is
  mode 700, and the file is truncated at arm so a reused run id's stale samples are never read.
- perf / scale — Two spawns per sample, detached, at most one sample a minute (§4). The worker
  reads the census with builtins only, and the ledger and dispatch paths gain no spawn.
- error / empty / loading states — `ps` failing, an unparseable header, a snapshot without the
  runner, or no sample in a leg's window reads `unknown`, never `0`, and a first `unknown` sample
  is announced once.
- observability — The `census` file names each foreign root by pid and token, and `--report`
  prints the set-aside counts and the per-leg `aside` column.
- risks — Over-counting: a bar queued on the turnstile, a short command whose text names a gate
  script, and on Windows an orphaned descendant of this bar's own legs whose parent field reads 1
  all count as foreign, which only sets a reading aside. Under-counting: work invisible to `ps -ef`
  (§3). A fixture arm asserting a count of zero would red on a busy host, so the arms assert roots
  by pid.
- testing — AC1 to AC10 by direct observation in the pass; the suite arms in §7 at the close.
- migration — Legacy rows read `uncensused` (§4); no tracked evidence row moves.
- user docs — The README's run-record section names the field, the `census` file and what the
  census cannot see; its ceiling section names the set-aside reasons.

## 6. Acceptance criteria

`$S` below is a scratch repository under `%TEMP%` with a short name, holding a copy of the runner,
`gate-fingerprint.sh` and a one- or two-leg manifest whose legs each run one fixture script,
named below by its basename.

- **AC1** — When the runner runs in `$S` over a leg running the script `a.sh`, which sleeps 5 s,
  while a second run of `a.sh` that the arm started outside the bar is alive, that leg's `.leg`
  row ends in a `foreign` field of 1 or more, and a line of the run's `census` file names the
  outside process's pid with that leg's script as its token.
  Red when: the outside process is not a root, or the field reads `0`.
  fixture: built per run; the tree holds none today.
- **AC2** — When the same fixture runs with no outside process, started through a `bash -c`
  wrapper whose argv names the runner's path, with a leg that starts a nested run of `b.sh` and
  writes its own and the nested pid to files, no root in the `census` file is the wrapper's, the
  runner's, the leg's or the nested pid.
  Red when: an ancestor or a descendant of the runner is counted as foreign.
- **AC3** — When `$S` runs with a `ps` stub that exits 1 first on `PATH`, every `.leg` row's
  `foreign` field reads `unknown`, every `census` line reads `unknown`, stderr carries one
  `run-gates: NOTE` line naming the census, and the verdict equals the same fixture's without the
  stub.
  Red when: a census that could not read the process table stamps any row `0`, or the stub moves
  the verdict.
- **AC4** — When `$S` runs with `GATE_JOBS=1` and two legs, both legs report, and a `$(...)`
  capture of the runner returns within 30 s of the runner's own exit while `CENSUS_EVERY` is 60.
  Red when: the sampler is a live job, so the serial pool never dispatches its second leg, or it
  holds the caller's stdout until its `sleep` ends.
- **AC5** — When `$S` runs with `GATE_CENSUS_EVERY=2` over one leg that sleeps 15 s, and the arm
  starts an outside run of `a.sh` 4 s after the runner that lives 8 s, the `census` file holds at
  least four sample lines and the leg's `foreign` field is 1 or more.
  Red when: the loop never samples after its first line, so load arriving mid-leg is missed.
  cost: about 20 s, most of it the leg's own sleep.
- **AC6** — When a two-leg bar has run in `$S`, `awk -F'\t' 'NF != 5' "$GD/gate-ledger.tsv"`
  prints nothing, and the passing leg's key field carries no TAB.
  Red when: the ledger block's read of field 7 absorbs the eighth field, its shape at base.
- **AC7** — When `python tools/run-gates/derive-ceilings.py --report` runs in a fixture git dir
  whose one run holds four `ok` readings of leg L — 10 s with `foreign` 0, 50 s with 2, 60 s with
  `unknown`, 70 s with no eighth field — and one `ok` reading of leg M with `foreign` 1, L's row
  reads a max of `10.0` from 1 reading with an `aside` of 3, the `# set aside:` line names
  `2 contended` and `2 uncensused`, and M is named on the every-reading-set-aside line and not on
  the UNBACKED line. The two counts are asserted apart, so a reason a later unit inserts between
  them leaves this criterion standing.
  Red when: the seven-field row is admitted, the 50 s reading raises the max, or M reads UNBACKED.
  figure: every count is PINNED by the fixture.
- **AC8** — When `python tools/run-gates/derive-ceilings.py --write` runs over AC7's fixture with
  an evidence row of 40.0 for L, that row stays 40.0 and the summary line names `2 contended` and
  `2 uncensused`; over a fixture holding only M's reading it exits 0, prints no `DEAD PROBE` and
  leaves every evidence row byte-identical; over a fixture holding no reading it still prints
  `DEAD PROBE`.
  Red when: DEAD PROBE fires over readings the tool set aside itself, or a set-aside reading moves
  a row.
- **AC9** — When `grep -n 'foreign' tools/run-gates/README.md` runs it names the run-record
  section's field list, and the header lines `--write` renders in AC8's fixture equal the header
  lines of the tracked `tools/run-gates/ceiling-evidence.txt`.
  Red when: the README still lists seven fields, or the tracked header differs from the rendered
  one.
- **AC10** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0,
  `python tools/govkit/govkit.py epoch --base <the pass's base>` names no run-gates entry, and
  `bash skills/session-kickoff/manifest-check.sh` prints no `MANIFEST check 5 FAILED` line.
  Red when: the runner's bytes moved and its version or the manifest's audit stamp did not.

## 7. Gates

`run-gates canary` · `run-gates evidence` · `run-gates turnstile` · `run-gates gov canary` · `run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `foreign-prefix parity (every self-test at three prefixes)` · `leg ceilings clear their evidenced maximum` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `install-prefix (shipped surface)` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

The close runs these once; no pass runs a suite. `run-gates evidence`, `run-gates turnstile`,
`run-gates run-log line`, `run-gates adopter e2e` and `profile-bar selftest` are held kit
self-tests, so the close owes each a run of its own, bounded, rather than inside the bar.

New arm: tools/run-gates/run-gates.evidence.test.sh · AC1 to AC6 as fixture bars; stage the ancestor walk deleted, the window reach set to zero, the sampler left undisowned, and the ledger read's trailing field deleted · FLOOR_ASSERTIONS rises by the arms added
New arm: tools/run-gates/run-gates.evidence.test.sh · AC7 and AC8 over fixture rows; stage the census filter deleted and the DEAD PROBE test moved after it · FLOOR_ASSERTIONS rises by the arms added

## 8. Open questions

- **FACT-QUESTION · F1 — Which census mechanism tells foreign load apart on node `a`?** The
  candidates differ in mechanism: (a) a process-table scan for gate work outside this bar's tree;
  (b) a host load reading, `/proc/loadavg`; (c) a beacon that each suite takes, the way bars take
  the turnstile. The probe is a read of each source on node `a` while foreign gate work was known to
  be running, plus the cost of one read of each. What would make each lose, written first: (a)
  loses if the foreign work is absent from `ps -ef` or costs more than a sample period; (b) loses if
  its reading moves with the reader's own load; (c) loses if the foreign work takes no beacon. The
  observation, 2026-10-04 18:53 +03:00: `ps -ef` listed the foreign `check-unattended.sh` tree in 27
  ms; `/proc/loadavg` read `2.47 2.47 2.47` and then `5.04 3.11 2.69` with nothing changed but the
  probe's own loops running, at 177 ms per read; and the foreign work was a checker launched by hand
  through `timeout`, which no runner wraps and so takes no beacon. Liveness: the predicate (a) can
  read negative, since seven of the same snapshot's ten rows matched nothing. The runner's own
  turnstile comment adds that three concurrent bars ran at 39 % CPU, so the contended resource here
  is process creation, which (b) does not read. RESOLVED (agent, 2026-10-04, delegated): (a), the
  process-table scan; (b) loses on discrimination and cost, (c) on the live instance.
- **FACT-QUESTION · F2 — Is the census taken at each leg's start and end, or by a periodic
  sampler?** Start-and-end loses if most of the measured work sits in legs long enough for foreign
  work to come and go inside them. The probe is node `a`'s primary `gate-ledger.tsv`, last written
  2026-09-29: 116 legs carrying 26655 s, of which the 46 legs of 60 s or more carry 25409 s, 95 %.
  Liveness: the probe can read low, since 70 of the 116 legs ran under 60 s and a ledger of short
  legs would put the share near zero. RESOLVED (agent, 2026-10-04, delegated): the periodic sampler,
  since start-and-end leaves the middle of 95 % of the work unobserved and the sampler costs the
  same spawns or fewer on any bar longer than one period per leg.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 5 section, `run-gates.sh` and
  `derive-ceilings.py` at base `5266d22e`, and the probes recorded in §4 and §8.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "stamp a timing reading as contended when foreign load
ran beside it"` ranked only name-stem neighbours (`read_text`, `load_conf`) and printed `unscanned
layers: .sh`, so the shell seams were read from source, per
`memory/gotchas/reuse-lookup-cannot-see-shell-seams.md`. Extended: `runleg`'s row write and the
ledger block's read in `tools/run-gates/run-gates.sh`; `ts_tick_start`, whose detached-ticker
properties the sampler copies; `scan_descendants`'s continuation-row guard; and `read_runs`,
`cmd_report` and `cmd_write` in `tools/run-gates/derive-ceilings.py`. `measure_neighbours` is the
in-bar sibling this unit deliberately does not touch. The recall probe surfaced
`TOOL-aPooledSweep-2`, whose withheld reading with a stated count is the pattern the `# set aside:`
line follows, and `TOOL-aSurfacedLexicon-22`, whose leg was written up twice from contended
readings. Where probe and source disagreed: nothing the map ranked touches a leg reading.
Rejected candidates and the tests that rejected them are §8 F1 and F2.

Recall terms used: ceiling evidence derive-ceilings contended reading neighbours serial retry timeout monotone headroom spawn floor HOST

The question passed with them: "why are leg ceilings raised from readings taken while the host was
loaded, and what separates a slow leg from a contended one".
