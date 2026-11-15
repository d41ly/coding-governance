# TOOL-aPiecewiseGrade-1 — the spec-token checker's incremental mode: each live spec's findings cached on its own inputs, every join rebuilt whole

**Status:** CLOSED · rev-2 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 2 · ratified 2026-11-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aPiecewiseGrade-1-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aPiecewiseGrade-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-aPiecewiseGrade-1-red-fix-1.md](../build/2026-11-15-build-TOOL-aPiecewiseGrade-1-red-fix-1.md) | red-fix | — |
| [2026-11-15-build-TOOL-aPiecewiseGrade-1-red-fix-2.md](../build/2026-11-15-build-TOOL-aPiecewiseGrade-1-red-fix-2.md) | red-fix | — |
| [2026-11-15-build-TOOL-aPiecewiseGrade-1-red-fix-3.md](../build/2026-11-15-build-TOOL-aPiecewiseGrade-1-red-fix-3.md) | red-fix | — |
| [2026-11-15-build-TOOL-aPiecewiseGrade-1-red-fix-4.md](../build/2026-11-15-build-TOOL-aPiecewiseGrade-1-red-fix-4.md) | red-fix | — |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-1-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-1-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-1-brief.md) | research | TOOL-aPiecewiseGrade-2 |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief.md) | research | TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-2 |

<!-- /gen:spec-records -->

## 1. Goal

When `SPEC_TOKENS_CACHE` names a directory, the whole-tree spec-token checker reuses each live
spec's raw findings while that spec's own inputs hold, re-grades the rest, and runs every
cross-spec join whole over the full finding set. Its stdout, stderr and exit status equal the plain
run's on every tree. It builds on TOOL-aPiecewiseGrade-3, which removes the call overhead the first
finding in §4 names, so it saves about 1 s of about 69 s (DERIVED d9f84ee14). The owner chose to build
both (F1).

## 2. Scope (IN)

- **S1** — The per-spec grading in `main`'s loop moves, unchanged in what it computes, into one
  module-level function, `scan_live_spec`, of the spec's path and the run's context. It returns
  the spec's hits, near-misses and counts. The plain run, `--spec` and `--pass-spec` call it, and
  their stdout and exit status do not move. Observed by AC1.
- **S2** — With `SPEC_TOKENS_CACHE` set and not empty, a whole-tree run looks each live spec up in
  that directory. A hit reuses the entry's findings; a miss grades the spec under a trace segment.
  Every step outside `scan_live_spec` runs exactly as the plain run runs it. Observed by AC2 and
  AC3.
- **S3** — An entry's key digests the run's grading context and the replay of that spec's own
  input lines: each file its grading read, and each tracked-set membership its grading asked. A
  key that cannot be replayed is a re-grade, never a hit, and a segment that ran a subprocess or
  listed a directory writes no entry. Observed by AC4 and AC5.
- **S4** — The mode never writes into the directory it reads. It writes the whole next generation,
  fresh and reused entries alike plus a list of the specs it re-graded, to the sibling directory
  `<dir>.next`, for the caller to promote under its own bracket. Observed by AC4 and AC6.
- **S5** — With `SPEC_TOKENS_INPUTS` also set, the input record the run writes is byte-identical to
  the plain run's, so aLightenedLoop's whole key stays sound. Observed by AC7.
- **S6** — The checker's header docstring states the mode, its key and the promotion contract.
  Observed by AC8.

## 3. Non-goals (OUT)

- No scoping of the check to the dispatching build. Every join runs over the whole tree.
- No change to any verdict, refusal line, report line, summary line or exit status.
- The bar's spec-tokens leg keeps the plain run, and should. The security model below rests on it:
  a forged cache entry can only make a dispatch skip findings that the bar still grades from
  scratch. A bar that read the cache would lose that backstop.
- No caching of any join, the supersede and arm-labels scans included. They run whole on every run,
  for the reasons in §4.
- No change to `--spec`, `--pass-spec`, `--legs-for`, `--input-key` or `--list` behaviour. The mode
  is off under the first four.
- No removal of the `load_kit_module` overhead the first finding names. That is
  TOOL-aPiecewiseGrade-3's, built first.
- No driver change: unit 2 sets the variable and promotes the next generation.
- No kit version bump by hand. The lander's mint moves `KIT_SPEC_TOKENS_VERSION`.

### Edges

- **consumes-from** `TOOL-aPiecewiseGrade-3` — `load_design_lib` answering from one load per process, which `scan_live_spec` keeps calling; without it every miss pays the per-call kit resolution. That unit builds at order 1, this one at order 2
- **hands-off** `TOOL-aPiecewiseGrade-2` — setting `SPEC_TOKENS_CACHE` on the dispatch's checker call, and promoting `<dir>.next` to `<dir>` only where the whole key is recorded. That unit builds at order 3, after this one
- **consumes-from** external — aLightenedLoop landed and reconciled onto main: the tracer, `read_open_py`, `--input-key` and `SPEC_TOKENS_INPUTS` this unit extends

## 4. Design

### First finding: the joins cost most of the run once one call overhead is gone

Measured on node `a` on 2026-11-15, PINNED, over a frozen shared clone at `d9f84ee14`. The plain
process took 149.7 s of wall (PINNED d9f84ee14). The split below comes from one standalone run of a
probe that loads the checker, wraps each join function with a timer and calls `main([])`. Its
stdout was byte-identical to the plain run's.

| part | ms, PINNED d9f84ee14 |
|---|---|
| `main` | 166 731 PINNED |
| every join together | 66 315 PINNED |
| of it, the carries join | 61 057 PINNED |
| of it, arm-labels, cutoff relations, size ceiling, header sort | 1 982, 1 734, 980, 391 PINNED |
| the sort's 2998 spec reads, re-timed alone | 1 537 PINNED |
| the per-spec loop, by difference | 98 878 PINNED |
| of it, `load_kit_module`, 70 726 calls | 97 865 PINNED |
| per-spec grading net of that overhead | about 1 013 PINNED |

As the code stands at `d9f84ee14`, the joins are 40% of the run and the per-spec loop is 59%. But
99% of the per-spec loop is one overhead, and none of it is grading. The guards join calls
`load_design_lib()` once per guard per declared path, inside generator expressions at
`tools/check-spec-tokens.py@6763260c:2056`, `tools/check-spec-tokens.py@6763260c:2064`,
`tools/check-spec-tokens.py@6763260c:2077` and `tools/check-spec-tokens.py@6763260c:2079`. Each call
resolves two paths through `Path.resolve`, at `tools/check-spec-tokens.py@6763260c:1097` and
`tools/check-spec-tokens.py@6763260c:1099`, about 1.4 ms per call on Windows (PINNED d9f84ee14).

TOOL-aPiecewiseGrade-3 binds that function once per process, at order 1, and so removes about 98 s (PINNED d9f84ee14),
DERIVED from d9f84ee14's table, from every caller: `--dispatch`, the bar's leg and `--spec` alike.
The plain run then takes about 69 s, of which the joins are about 96%, both DERIVED from d9f84ee14's
table. The per-spec grading this unit caches is about 1 s of that (PINNED d9f84ee14). So on the tree
this unit builds against, the joins cost most of the run, and the incremental mode, which must run
every join whole, saves at most that second (PINNED d9f84ee14). The owner chose to build both (F1).
The remaining cost is the carries join's history read,
`read_spec_revisions` (`tools/memory-tree/design_lib.py@82906599:661`), with one `git log` and one
`git cat-file --batch` over 1536 chain specs (PINNED d9f84ee14). Only a cache keyed on that join's
own inputs could cut it, which is a different mechanism.

A second observation at `aebbb4a72` had the same shape: `main` 168 499 ms, joins 63 899 ms,
`load_kit_module` 100 619 ms over 73 134 calls (PINNED aebbb4a72). It ran while another probe shared
the machine, so its absolute figures are high.

The probe, run from the clone's root with the clone's checker:

```python
import importlib.util, io, contextlib, os, time
s = importlib.util.spec_from_file_location("cst", os.path.join(os.getcwd(), "tools", "check-spec-tokens.py"))
cst = importlib.util.module_from_spec(s); s.loader.exec_module(cst)
acc, depth = {}, [0]
def wrap(name, join=True):
    f = getattr(cst, name)
    def w(*a, **k):
        t = time.perf_counter(); depth[0] += join
        try: return f(*a, **k)
        finally:
            depth[0] -= join
            key = name if join else name + (" in-join" if depth[0] else " outside")
            d = acc.setdefault(key, [0.0, 0]); d[0] += time.perf_counter() - t; d[1] += 1
    setattr(cst, name, w)
for n in ("read_tracked derive_legs_path read_size_ceilings read_waivers read_cutoff_key check_cutoff_relation "
          "check_claim_canary read_spec_uids scan_handoffs scan_spec_sizes derive_carries_coverage "
          "scan_live_packets scan_supersede scan_arm_labels check_live_header").split():
    wrap(n)
wrap("load_kit_module", join=False)
t = time.perf_counter()
with contextlib.redirect_stdout(io.StringIO()): cst.main([])
print(round((time.perf_counter() - t) * 1000), {k: (round(v[0] * 1000), v[1]) for k, v in acc.items()})
```

### What the code does today

Read at `d9f84ee14`, aLightenedLoop's head, and at `aebbb4a72`, this build's base. The checker's
blob is `6763260c` at the first and `f1d1d958` at the second. The design is for the tree after
aLightenedLoop reconciles onto main.

- `main` grades each live spec in one loop, `tools/check-spec-tokens.py@6763260c:1959-2129`, whose
  body reads only the spec's path, its bytes, the tracked set, the root-install name sets and values
  `main` computed before the loop. No step in it reads a value another spec's iteration set. At
  `aebbb4a72` the same loop also reads `flag_suites` through `check_bar`
  (`tools/check-spec-tokens.py@f1d1d958:1813`).
- The loop reads files twice: the spec, at `tools/check-spec-tokens.py@6763260c:1960`, and each
  cited tracked file, at `tools/check-spec-tokens.py@6763260c:2089`. It reads the tracked set only
  by membership, through `check_path_shaped` and three `in` tests. The kit helpers it calls,
  `read_spec_writes`, `derive_dir_segments`, `check_dir_shaped` and `check_guard_trips`
  (`tools/memory-tree/design_lib.py@82906599:544-660`), open no file and run no process.
- The leg hit's reason names the module global `LEGS`, which `main` rebinds at
  `tools/check-spec-tokens.py@6763260c:1892`.
- The input tracer: `arm_input_trace` (`tools/check-spec-tokens.py@6763260c:341`) installs the
  audit hook `add_input_event` (`tools/check-spec-tokens.py@6763260c:355`), the `subprocess.run`
  wrapper `run_traced` (`tools/check-spec-tokens.py@6763260c:375`) and the exit writer
  `write_input_record` (`tools/check-spec-tokens.py@6763260c:407`). Every line goes through
  `add_input_line` (`tools/check-spec-tokens.py@6763260c:337`) into one process-wide set. The hook
  skips opens under the interpreter's prefixes, and records listings unfiltered.
- The replay: `derive_input_digest` (`tools/check-spec-tokens.py@6763260c:417`) hashes a record's
  bytes, then each line's replay, and returns None on a parse failure or a kind outside `read`,
  `list` and `run`.
- The arming is module-level, at `tools/check-spec-tokens.py@6763260c:457`, ahead of the kit's
  loads.

### The two classes: every step of the whole-tree run

Every row is `tools/check-spec-tokens.py@6763260c`, at the line given.

| step | site | class | inputs |
|---|---|---|---|
| repo root | `run`, line 1841 | run context | `git rev-parse --show-toplevel` |
| tracked set | `read_tracked`, line 1846 | run context; membership only inside the loop | `git ls-files` |
| live and terminal sort, the unretired set | lines 1870-1880 | cross-spec: the population | every tracked spec's bytes |
| leg manifest | lines 1887-1910 | run context of the loop | the manifest; `derive_flag_suites` at `aebbb4a72` |
| size ceiling | `read_size_ceilings`, line 1912 | size join input | the high-water file; the policy kit's caps |
| waivers | `read_waivers`, line 1918 | waiver join input | the registry |
| cutoffs | `read_cutoff_key`, lines 1924-1929 | four are loop context, handoff and supersede are join inputs | `.memory-tree.conf`, `tree_lib` |
| cutoff relations | `check_cutoff_relation`, lines 1932-1934 | run context, report lines only | `git log -S` over the conf |
| claim canary | `check_claim_canary`, line 1940 | run context | none |
| root-install names | lines 1947-1950 | loop context, membership only | the tracked set |
| leg, legline, paths, bar, guards, cite, claims, covers, source and ac-order | the loop, lines 1959-2129 | per-spec | the spec's bytes, cited files' bytes, tracked-set membership, the loop context |
| hands-off | `read_spec_uids`, `scan_handoffs`, lines 2144-2145 | cross-spec: a hit reads a sibling's text | every live spec's bytes |
| size and stale high-water rows | `scan_spec_sizes`, line 2153 | cross-spec: a row is stale against the live set | live spec bytes, high-water rows, tracked set |
| carries | `derive_carries_coverage`, line 2166 | cross-build | the design record and view, chain specs at every status but WONTDO, their history |
| packet | `scan_live_packets`, line 2188 | cross-build | tracked set; each packet build's `RUN.md` by `is_file`, line 1756, then read; one instrument run per live chain run |
| supersede | `scan_supersede`, line 2198 | per-spec by function | every live spec's bytes |
| arm-labels | `scan_arm_labels`, line 2202 | per-spec by function, over the unretired set | every unretired spec's bytes, each named suite's bytes, tracked set |
| waiver filter and seen set | lines 2205-2208 | cross-spec | every hit, the registry |
| stale rows | lines 2210-2217 | cross-spec | the registry, the seen set, the size join's stale rows |
| report, hit lines, summary, exit | lines 2219-2340 | sums and the lists above | the counters, `live`, `stale` |

Only the loop is cached. Supersede and arm-labels are per-spec by function, but they cost, PINNED
d9f84ee14, 29 ms and 1982 ms, arm-labels grades terminal specs the live sort never reaches, and caching
either would add a second key for under 3% of the post-overhead run (DERIVED). They run whole.

### S1 — `scan_live_spec`

`scan_live_spec(root, f, files, bare, ctx)` holds the loop body as written today, with three changes
in how it is spelled and none in what it computes:

1. It reads the spec's bytes itself, so the read falls inside a segment.
2. Every value the body took from `main`'s scope arrives in `ctx`, one dict: `legs`, `guarded`,
   `broad`, the leg manifest's repo-relative path in place of the global `LEGS`, the four loop
   cutoffs, and, after the reconcile, `flag_suites`. Whatever the body reads beyond the spec, the
   tracked set and the root-install sets is a key of `ctx`, because the function is module-level and
   can see nothing else of `main`.
3. Its 24 counters return in one dict, in place of the loop's local accumulators.

It returns `(hits, near, counts)`. `main` extends `hits` and `near` and adds each count, spec by spec
in `specs` order, so every list keeps its order. The plain run and `--spec` both call it.

### S2 and S3 — the incremental mode and its key

The mode runs when `SPEC_TOKENS_CACHE` is set and not empty, `--spec` and `--pass-spec` are absent,
and `main` reaches the loop. A trailing separator in the value is dropped. Before the loop it removes
any `<dir>.next` left by an earlier run, creates it empty, and derives the context digest once.

**The context digest**, `derive_spec_context(ctx)`, is the SHA-1 over three parts. The first is the
launcher, `sys.executable` and `sys.version`. The second is the bytes of the checker and of every
module loaded from the memory-tree kit dir when the loop starts, each named by its realpath. The
third is `ctx` as sorted JSON. Every conf key the loop reads is a value in `ctx`, so a moved cutoff
moves the digest.

**The trace segment.** `INPUT_TRACE` gains a `segment` slot, None outside a segment. `add_input_line`
adds each line to the open segment as well as to the process-wide set, so the hook's reads and the
wrapper's runs inside `scan_live_spec` land in both. The tracked set and the two root-install sets
reach `scan_live_spec` wrapped in `MemberProbe`, whose only method is `__contains__`. It answers
from the real set and adds `{"kind": "member", "of": <files|exts|names>, "key": <token>}` to the open
segment, and to nothing else. Any other use raises `TypeError`.

**One entry** is two files in `<dir>.next`, named by the SHA-1 of the spec's root-relative path:

| file | holds |
|---|---|
| `<id>.inputs` | the segment's lines, sorted and de-duplicated, one compact JSON object per line, as `write_input_record` writes |
| `<id>.json` | `path`, `key`, and the spec's `hits`, `near` and `counts`, exactly as `scan_live_spec` returned them: raw, before any waiver or join |

The key is the SHA-1 over the context digest and `derive_input_digest(<id>.inputs, names)`, where
`names` maps `files`, `exts` and `names` to the run's real sets. It is derived after the `.inputs`
file is written, so it replays the file the lookup will replay.

**`derive_input_digest(record, names=None)`** keeps today's answer exactly when `names` is None. Given
`names`, it admits only `read` and `member` lines. A `member` line replays as `1` or `0` from
`names[of]`. A `list`, `run` or `popen` line, or an `of` that `names` lacks, returns None.

**A lookup** of a live spec reads `<dir>/<id>.json`. It is a hit only when four things hold: the
entry parses, its `path` is the spec's, the digest over `<dir>/<id>.inputs` is not None, and the
SHA-1 of the context digest and that digest equals the entry's `key`. On a hit, the entry's
findings and counts are used, and its two files are copied byte for byte into `<dir>.next`. Any
other answer, an `OSError` or a parse failure included, is a miss.

**A miss** opens a segment, calls `scan_live_spec` and closes it. If the segment holds only `read`
and `member` lines, the entry is written to `<dir>.next` and the path is appended to
`<dir>.next/graded.list`. Otherwise no entry is written and the path is still appended. A write that
fails leaves that entry out and prints nothing.

### S4 — the next generation, and who promotes it

The mode reads `<dir>` and writes only `<dir>.next`. The next generation holds one entry per live
spec that was written, and `graded.list`, one root-relative path per line in grading order, empty
when nothing was re-graded. A spec no longer live has no entry, so the generation sheds it.

The checker cannot tell whether a file it read moved between that read and the key's replay. So an
entry is sound only when the tree held still across the run. The caller knows that, as
TOOL-aLightenedLoop-3 S6 knows it for the whole key, and promotes by removing `<dir>` and renaming
`<dir>.next` to `<dir>`. A caller that does not promote leaves the cache as it was. A crash between
the two steps leaves no `<dir>`, which reads as a miss for every spec.

### S5 — the whole record stays the plain run's

`arm_input_trace` runs at module level when either variable is set, and registers the exit writer
only when `SPEC_TOKENS_INPUTS` is set. Its skip prefixes gain `<dir>` and `<dir>.next`, and the hook
applies them to listing events as well as to opens. Otherwise the cache's own reads and the removal
of an old `<dir>.next` would enter the record and move the whole key on every run.

A hit's replay reads the spec and each cited file through `derive_input_digest`, outside any
segment. So the process-wide set gains the same `read` lines the plain run's grading adds. Member
lines never enter it: its `git ls-files` run line already answers for the tracked set. The two
records are therefore the same bytes.

### Why every join's answer equals the whole-tree run's

Every join runs the plain run's code over the plain run's inputs. Only one join reads anything the
mode supplies: the waiver filter and its stale rows read `hits`. And `hits` is the concatenation, in
`specs` order, of per-spec findings that each equal the plain run's. A spec's findings are a
function of its bytes, the files its grading read, its membership answers, `ctx`, the code and the
launcher. A hit requires every one of those to replay equal to what it was when the entry was
graded. Named one by one:

- **The live and terminal sort and the unretired set** run whole, reading every spec's bytes. A spec
  flipped CLOSED leaves `specs`. Its entry is never looked up, and its findings leave `hits`.
- **A stale waiver row** is computed from the full `hits` and the registry, both whole. When a
  status flip or a retired token removes a waived row's only hit, that row's token leaves the
  seen set as it does in the plain run. A cached entry cannot keep the hit alive, because the
  flipped spec is not looked up and the edited spec's own bytes are a `read` line of its key.
- **The carries finding that names a chain build bare** comes from `derive_carries_coverage`, run
  whole over chain specs at every status. Its `where` is the build, and no entry holds it.
- **The packet runs** come from `scan_live_packets`, run whole. Its `is_file` probe of each `RUN.md`
  and its instrument runs happen on every run, so a run appearing, going live or landing is seen as
  the plain run sees it.
- **Hands-off, size, supersede and arm-labels** run whole over their populations.
- **The report lines** sum the per-spec counts, and each summand equals the plain run's.

### Output order

The loop's lists are extended spec by spec in `specs` order, and each entry keeps its own internal
order. Every join appends after the loop, as today. The mode prints nothing, on stdout or stderr.
So the hit lines, stale rows, report lines and summary come out in the plain run's order and
spelling, with its exit status.

### What the design does not check

Carried from TOOL-aLightenedLoop-3's "What the key does not check":

- **A path probed only by `is_file` or `exists`.** No such probe is in `scan_live_spec` at
  `d9f84ee14`. The packet join's `RUN.md` probe sits in a join that runs whole. A stat probe added
  to `scan_live_spec` later raises no event the hook records, so a spec's key would not see it.
- **The environment beyond the launcher, and a package upgraded in place** under one launcher path.
- **A subprocess whose answer is not a function of the tree.** A segment that runs any subprocess
  writes no entry, so per-spec keys hold none. The joins run whole.

New with this design:

- **A module global that `main` rebinds and `scan_live_spec` reads** escapes the context. `LEGS` is
  the one today, and it is passed in `ctx`. Nothing grades the function's free names.
- **A use of the tracked set other than `in`** inside `scan_live_spec` raises `TypeError`. The mode
  then fails where the plain run does not. The differential arm sees it only where a fixture reaches
  that use.
- **The window between a read and its key's replay.** The checker does not guard it. Soundness rests
  on the caller promoting only under a bracket. A caller that promotes over a moving tree can
  promote a stale entry.
- **A forged entry** in the cache directory can make a lookup reuse the forged findings. The bar's
  leg runs the plain check and never reads the cache.
- **Over-sensitivity.** A cited file's edit that keeps its line count still re-grades the citing
  spec, though only the count is read. A spec whose grading ran a subprocess re-grades every run.

### The pass probe, `$SCRATCH/pg1.sh`

`$SCRATCH` is the run's scratch directory. The probe builds a fixture repository at `$TEMP/pg1`,
a short path, as TOOL-aLightenedLoop-3's probe does. It copies the built checker and the
memory-tree kit into the fixture's tool root, so a kit edit stays inside the fixture. The
fixtures follow the suite's own recipes, `scratch`, `seed_carries_repo` and the packet join's stub
instrument (`tools/check-spec-tokens.test.sh@b78125e1:363`, `tools/check-spec-tokens.test.sh@b78125e1:1589`,
`tools/check-spec-tokens.test.sh@b78125e1:1994`).

The seed holds three live specs across two builds. One cites a tracked file at its last line. One
carries a waived hit, and a second waiver row's only hit sits in another live spec. A carries design
binds a chain build whose chain spec is CLOSED, and a packet instrument stub that exits 1 is tracked
with a packet prompt for a chain build that has no `RUN.md` yet.

Each step applies one change, then runs the plain checker and the incremental one with
`SPEC_TOKENS_CACHE="$C"`. It then promotes as a caller would, with `rm -rf "$C"` and
`mv "$C.next" "$C"`, and prints one line:
`step <name> moved <0|1> same <0|1> rc <plain>/<incremental> graded <n>`. Here `moved` says the plain
output differs from the previous step's, `same` says `cmp` found stdout and stderr equal and the two
statuses match, and `graded` counts `$C/graded.list`'s lines.

| step | the change | how the plain output moves |
|---|---|---|
| `seed` | none | first run |
| `rerun` | none | does not move |
| `closed` | the spec carrying the waived hit set CLOSED and committed | a STALE WAIVER row |
| `retired` | the other waiver's only hit token removed from its live spec | a second STALE WAIVER row |
| `carries` | the CLOSED chain spec stops naming a clause token | a `[carries]` hit whose file is the bare build |
| `packet` | a `RUN.md` with phase BUILDING committed for the packet's chain build | a `[packet]` hit |
| `isfile` | a second packet prompt and a tracked `RUN.md` for another chain build | the packet join's live-run count |
| `cited` | the cited file loses its last line | a `[cite]` hit |
| `kit` | the copied kit's `read_spec_writes` made to return None | the guards line's no-sub-head count |
| `cutoff` | `SPEC_DIRECT_CUTOFF` moved past a live spec carrying a bar token | that spec's `[bar]` hit leaves |
| `onespec` | one live spec's prose edited and committed | does not move |

After the `onespec` step the probe also prints `regraded <n> <path>`, from `graded.list`.

Then the probe forges two entries in `$C`. One gets a `.inputs` file holding a `run` line, with a key
derived as if it were valid. The other gets a `.json` that does not parse. It prints
`forged run <hit|miss> corrupt <hit|miss>`, read from `graded.list` after one incremental run. Next,
it runs the plain and the incremental checker with `SPEC_TOKENS_INPUTS` naming two record files, on a
cold cache and then on a warm one, and prints `record cold <same> warm <same>` from `cmp`. Last, it
snapshots `$C` with `find "$C" -type f -exec sha1sum {} +` before and after one incremental run, and
prints `untouched <0|1> generation <ok|bad>`, the second word folding the per-step check that
`$C.next` is gone after each promotion and `$C` holds one entry pair per live spec.

### Inventory

| identifier | kind | lexicon |
|---|---|---|
| `scan_live_spec` | Python function | `scan`, OK by `--suggest` |
| `derive_spec_context` | Python function | `derive`, OK |
| `read_spec_cache` | Python function: the lookup | `read`, OK |
| `write_spec_cache` | Python function: one entry into the next generation | `write`, OK |
| `MemberProbe` | Python type | pascal for `py.type`, OK |
| `SPEC_TOKENS_CACHE` | environment variable the checker reads | no declared cell; spelled as `SPEC_TOKENS_INPUTS` is |
| `<dir>.next`, `<id>.json`, `<id>.inputs`, `graded.list` | cache files, never tracked | no declared cell |

`derive_input_digest`, `arm_input_trace`, `add_input_line` and `add_input_event` are extended in
place, not minted. No conf key, no check number and no refusal line is minted.

### Docs, and what the change owes beyond the code

- The checker's header docstring gains a `SPEC_TOKENS_CACHE` paragraph beside the
  `SPEC_TOKENS_INPUTS` one, carrying the phrase `promotes <dir>.next only under its own bracket`.
- The codebase map's symbol index is regenerated by `tools/codebase-map/gen_map.py --write`, for the
  five new names. The spec-tokens dossier names its paths and legs, and neither moves.
- No `help/` page names the spec-token checker's cache or `SPEC_TOKENS_INPUTS`, grepped at
  `aebbb4a72`, so none is owed. The verbs guide is unit 2's.
- The kit epoch leg sees shipped bytes move, and the lander's mint moves the version.

### Rollout

This unit builds after aLightenedLoop lands and this build reconciles onto it, against the
reconciled checker, and after TOOL-aPiecewiseGrade-3. Every line cited above moves, so the builder finds each site by its text.
`FLOOR_ASSERTIONS` in the spec-tokens self-test rises by the new assertions, which the close
confirms from a real run. The mode is dark until unit 2 sets the variable.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Hoisting the overhead instead.** It is the better buy by the first finding, and a different
  mechanism. The owner chose both (F1), so TOOL-aPiecewiseGrade-3 hoists it first.
- **Keying each spec on the whole `git ls-files` answer.** Every pass commit adds a record, so every
  spec would re-grade every time. Membership lines key a spec only on the paths its grading asked
  about.
- **Keying on the run's whole input record, per spec.** The sort reads every spec, so one status flip
  would move every key.
- **A declared list of the loop's context, kept beside the loop.** It would be two answers to one
  question. `ctx` is the function's own argument, so whatever the function reads, the digest covers.
- **Caching the supersede, arm-labels or size scans.** Each would need its own key for under 3% of
  the post-overhead run (DERIVED from the table).
- **Writing entries straight into `<dir>`.** An entry graded while a cited file was being written
  would be kept with a key over the new bytes. Only the caller's bracket can see that.
- **Recording iteration of the tracked set as a whole-set line.** Nothing in the loop iterates it,
  and a loud `TypeError` is caught by the differential arm when it first happens.
- **A flag in place of the variable.** A declared checker that does not know a flag may exit
  non-zero and move the dispatch verdict, which is TOOL-aLightenedLoop-3's reason for its own
  variable.
- **Replaying `run` and `list` lines per spec.** No per-spec grading runs a process or lists a
  directory today, and replaying a cached `argv` executes what a cache file says. Deny by default:
  such a segment is never cached.

## 5. Production-readiness checklist

- security — the cache lives in the per-worktree git dir that only the driver writes. A per-spec
  replay reads and hashes files and answers membership, and runs no process. A forged entry can
  only hide findings from a dispatch, and the bar's plain run still grades them.
- perf / scale — a hit costs one hash per recorded file and a dictionary lookup per member line. A
  miss costs the per-spec grading on the tree after TOOL-aPiecewiseGrade-3: about 34 ms per spec on
  node `a`, DERIVED from d9f84ee14's table. The joins' about 66 s is unchanged (PINNED d9f84ee14), so
  a whole-tree run stays near 69 s (DERIVED d9f84ee14).
- error / empty / loading states — an absent, unreadable or corrupt entry is a miss. A write failure
  costs that entry. The mode prints nothing in any case.
- observability — `graded.list` names every re-graded spec of the run.
- risks — the refactor of the loop touches every per-spec join. AC1 holds the plain output to the
  base's at every probe step and over the real tree.
- testing — the pass probe above, and the suite's new differential arm observed RED then GREEN at
  the close.
- migration — none. With no cache directory, every spec misses once and the caller promotes.
- user docs — the checker's header docstring. No `help/` page names this surface.

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/pg1.sh"`, described in §4, removed after the
pass.

- **AC1** — When the probe also runs the base checker, the reconciled one before this unit, plainly at
  every step, `cmp` against the built checker's plain output prints nothing at each step, and the
  statuses match. At the close the main loop makes the same comparison over this worktree with
  `python tools/check-spec-tokens.py`.
  Red when: the extraction drops, reorders or re-spells a hit, a near-miss or a counter.
  permission: the whole-tree run over the real tree is the main loop's.
  cost: two whole-tree runs, about 69 s each on node `a` after TOOL-aPiecewiseGrade-3. <!-- DERIVED from d9f84ee14's table -->
- **AC2** — When `bash "$SCRATCH/pg1.sh"` runs, every `step` line it prints reads `same 1`, and the
  `closed`, `retired`, `carries`, `packet`, `isfile`, `cited`, `kit` and `cutoff` lines also read
  `moved 1`.
  Red when: the key leaves out a cited file's read, the kit's code or a `ctx` value, so `cited`,
  `kit` or `cutoff` reuses a stale entry; or the mode iterates cached entries rather than the live
  sort, so `closed` keeps a CLOSED spec's waived hit.
- **AC3** — When `bash "$SCRATCH/pg1.sh"` runs, the `carries`, `packet` and `isfile` lines read
  `same 1` while their plain output moved, and the `rerun` line reads `moved 0 same 1 rc 0/0 graded 0`.
  Red when: any join's answer is taken from the previous run or from cached entries, or the
  re-run re-grades a spec whose inputs did not move.
- **AC4** — When `bash "$SCRATCH/pg1.sh"` runs, the `seed` line reads `graded 3` and the probe prints
  `regraded 1` followed by the edited spec's path.
  Red when: a key digests the whole tracked set or every spec's bytes, so one edit re-grades all.
- **AC5** — When `bash "$SCRATCH/pg1.sh"` runs, it prints `forged run miss corrupt miss`.
  Red when: `derive_input_digest` with `names` replays a `run` line, or a parse failure is read as a
  hit.
- **AC6** — When `bash "$SCRATCH/pg1.sh"` runs, it prints `untouched 1 generation ok`.
  `generation ok` says that after every step's promotion `$C.next` was gone and `$C` held one
  `.json` and one `.inputs` per live spec.
  Red when: the mode writes into the directory it reads, or the next generation keeps a spec that
  left the live set.
- **AC7** — When `bash "$SCRATCH/pg1.sh"` runs, it prints `record cold 1 warm 1`.
  Red when: the hook records a read or a listing under the cache directories, or a hit's replay
  records fewer reads than the plain run's grading.
- **AC8** — When `grep -c 'promotes <dir>.next only under its own bracket' tools/check-spec-tokens.py`
  runs it prints 1.
  Red when: the docstring leaves the promotion contract unstated.

## 7. Gates

`spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `spec tokens (the pass's own spec)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC2 AC3 AC4 AC5 AC6 AC7 · the probe's steps as a differential arm comparing plain and incremental stdout, stderr and status at every step, each plant asserting the plain output moved; staged RED by a key that leaves out the `read` lines, then by a mode that reuses the previous run's packet answer · `FLOOR_ASSERTIONS`, raised by the count of new assertions, which the close confirms

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
the spec-token checker's `--spec` over this file and the positional check.

## 8. Open questions

- **F1 — Build the incremental mode as briefed, or retarget the build at the overhead the first finding names?**
  The joins cost about 96% of the run once the `load_kit_module` overhead in the guards join is
  removed, and the incremental mode must run every join whole (DERIVED from §4's table). Options:
  - (a) Build both units as specified. DERIVED from d9f84ee14's table, a pass commit's `--dispatch`
    on node `a` drops from about 167 s to about 71 s while the overhead stands (d9f84ee14). If the
    overhead is ever removed, the mode saves about 1 s (d9f84ee14) and keeps its cache, key and arm.
  - (b) Retarget: replace this unit with one that binds `load_design_lib()` once per run in the
    guards join, a Tier-1 change that moves no verdict, and retire unit 2 as WONTDO. Every caller,
    the bar's leg included, drops to about 69 s with no cache (DERIVED d9f84ee14). File the carries join's
    history read, about 61 s (PINNED d9f84ee14), as a follow-up ask for a cache keyed on that join's
    own inputs.
  - (c) Both: the overhead removal as an added unit at order 1, then these two units. The mode then
    saves about 1 s of about 69 s (DERIVED d9f84ee14) for the diff this spec describes.
  Recommendation: (b). It cuts the same seconds from every caller with a few lines and no new
  surface, and the incremental mode cannot reach the cost that is left. (a) is the feature-rich
  survivor only if the owner wants `--dispatch` faster without touching the guards join.
  RESOLVED (owner, 2026-11-15): (c) Both

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft from brief `2026-11-15-prompt-TOOL-aPiecewiseGrade-1-brief`,
  grounded at `aebbb4a72` and at aLightenedLoop's head `d9f84ee14`, and measured there on node `a`.
  The measurement is §4's first finding and F1.
- rev-2 · 2026-11-15 · §1 · §3 · §4 · §5 · AC1 · §8 · from brief
  `2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief`, item 3: F1 RESOLVED as the owner's (c),
  order 1 to 2 with the ratified pointer, a consumes-from edge on TOOL-aPiecewiseGrade-3, and the gain, cost and non-goal
  statements read against the tree after that unit.

## 10. Reuse audit

The seams this unit extends: aLightenedLoop's tracer, `arm_input_trace` with `add_input_line` and
the audit hook (`tools/check-spec-tokens.py@6763260c:341`), opened per spec as a segment rather than
once per run; and its replay, `derive_input_digest` (`tools/check-spec-tokens.py@6763260c:417`),
given a membership kind and called per spec. Its `--spec` walk is not the seam: it grades named
specs whatever their status and skips three joins, as section 4 of TOOL-aLightenedLoop-3 records. The per-spec
loop of `main` is the seam, extracted. `tools/codebase-map/reuse_lookup.py` for "cache each spec's
grading on the inputs it read and re-grade only the specs whose inputs moved" ranked generic name
stems only (`read_text`, `read`, `read_bytes`, `read_spec_revisions`), and no caching seam fits
beyond aLightenedLoop's, which the lookup cannot see because it indexes `aebbb4a72`. Recall's top
hits were TOOL-aSmoothedDispatch-4, the first key, TOOL-aSmoothedDispatch-5, the `--spec` mode, and
TOOL-aBriskDeclaration-1, the two-half driver. `gotchas.py --for-paths` selected
`fixture-passes-by-finding-nothing`, which every probe step's `moved` field answers.

Recall terms used: `python tools/memory-recall/query.py "how can the spec-token checker re-grade only specs whose inputs moved while cross-build joins stay whole" --terms "spec-token checker incremental per-spec cache input record replay waiver stale carries packet dispatch key"`
