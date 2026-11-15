# TOOL-aPiecewiseGrade-4 — the spec-token checker writes its next cache generation into a directory the caller names, so no caller renames a fixed-name temp

**Status:** INPROGRESS · rev-2 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 3 · ratified 2026-11-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-2-forks-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-2-forks-brief.md) | research | TOOL-aPiecewiseGrade-2 |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-4-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-4-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-4-forks-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-4-forks-brief.md) | research | TOOL-aPiecewiseGrade-2 |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-aPiecewiseGrade-1's incremental mode writes its next generation to the fixed name `<dir>.next`,
and a caller that renames it into place renames a fixed-name temp, the class the
`shell hygiene (a fixed-name temp renamed into place)` leg refuses. With this unit the caller names
the next generation's directory in `SPEC_TOKENS_CACHE_NEXT`, made with `mktemp -d` beside the cache.
The checker writes into that directory and never creates, empties or removes it. Nothing the
checker prints moves.

## 2. Scope (IN)

- **S1** — The mode runs only when `SPEC_TOKENS_CACHE` and `SPEC_TOKENS_CACHE_NEXT` are both set and
  not empty, name two different directories, and neither `--spec` nor `--pass-spec` is given. Any
  other run is the plain run. Observed by AC3.
- **S2** — The mode writes the whole next generation into the directory `SPEC_TOKENS_CACHE_NEXT`
  names: `graded.list`, each hit's two files copied, and each fresh entry, exactly as it writes them
  into `<dir>.next` today. It never creates, empties or removes that directory, and it never writes
  or removes `<dir>.next`. Observed by AC1 and AC2.
  **Readers:**
  by name: `tools/check-spec-tokens.py` spells `<dir>.next` in its docstring, in `arm_input_trace`,
  `read_spec_cache`, `write_spec_cache` and `main`; `tools/check-spec-tokens.test.sh` spells it as
  `$pc.next` in the `PG1` arm. No other tracked file outside the build records spells it, by a git
  grep at dd9006677.
  by value: `tools/check-spec-tokens.test.sh`, whose `PG1` arm renames the directory over `$pc` and
  reads its `graded.list`; S6 moves both onto the named directory. No product file reads it.
- **S3** — The input trace skips the named directory, for opens and listings, where it skips
  `<dir>.next` today, so the `SPEC_TOKENS_INPUTS` record stays the plain run's bytes. Observed by
  AC4.
- **S4** — Every other behaviour TOOL-aPiecewiseGrade-1 built keeps its bytes: the plain run,
  `--spec`, `--pass-spec`, `--list`, `--input-key`, the per-spec key, the lookup and the order of
  every output line. Observed by AC1 and AC5.
- **S5** — The checker's header docstring states the new contract, and no `.next` name remains in
  the checker. Observed by AC6.
- **S6** — The suite's `PG1` arm moves onto the new contract with its steps unchanged, and a `PG4`
  arm beside it asserts S1 and S2. NOT OBSERVED by a criterion: the suite is the main loop's, observed
  RED then GREEN at the close under the two `New arm:` lines in §7.

## 3. Non-goals (OUT)

- No edit to TOOL-aPiecewiseGrade-1's CLOSED spec.
- No row raised in `memory/project/temp-name-sites.txt`, and no change to the shell-hygiene lint.
- No promotion by copying, and no promotion inside the checker.
- No change to any verdict, refusal line, report line, summary line or exit status.
- No change to the per-spec key, the context digest, the lookup's four conditions, or which segments
  write an entry.
- No read-only mode for `SPEC_TOKENS_CACHE` alone. No caller needs one (§4, Alternatives rejected).
- No driver change. TOOL-aPiecewiseGrade-2 makes the directory, sets both variables and promotes.
- No kit version bump by hand.

### Edges

- **consumes-from** external — TOOL-aPiecewiseGrade-1's incremental mode, its cache and its `PG1` arm, which this unit changes in where the next generation is written and nothing else. That spec is CLOSED and frozen, and predates this unit, so it declares no hands-off here. The build order is TOOL-aPiecewiseGrade-3 at order 1, TOOL-aPiecewiseGrade-1 at order 2, this unit at order 3 and TOOL-aPiecewiseGrade-2 at order 4
- **hands-off** `TOOL-aPiecewiseGrade-2` — making the next generation's directory with `mktemp -d` beside the per-slug cache, passing it in `SPEC_TOKENS_CACHE_NEXT`, naming it live in a file only where the whole key is recorded, and the lint observation over the driver. That unit builds at order 4, after this one

## 4. Design

### What the code does today

Read at `dd9006677`. The checker's blob is `e535b5ee`, the lint's `448d62cb`, the driver's
`a9ff4a9c` and the checker's suite `eeb7f115`.

- The header docstring's `SPEC_TOKENS_CACHE` paragraph says the run writes its next generation to
  `<dir>.next` and the caller promotes it by removing `<dir>` and renaming `<dir>.next` to it
  (`tools/check-spec-tokens.py@e535b5ee:300`).
- `main` arms the mode at `tools/check-spec-tokens.py@e535b5ee:2416`. It removes any `<dir>.next`
  with `shutil.rmtree`, re-creates it with `os.makedirs` and creates `graded.list` in it
  (`tools/check-spec-tokens.py@e535b5ee:2418`).
- `read_spec_cache` (`tools/check-spec-tokens.py#read_spec_cache`) copies a hit's two files into
  `cache + ".next"`. `write_spec_cache` (`tools/check-spec-tokens.py#write_spec_cache`) writes there,
  then reads back the `.inputs` it wrote to derive the key.
- `arm_input_trace` (`tools/check-spec-tokens.py#arm_input_trace`) skips `<cache>` and
  `<cache>.next` for opens and listings. The module-level call passes it the cache directory
  (`tools/check-spec-tokens.py@e535b5ee:500`).
- `scan_temp_file` (`tools/gate-lint/sh_hygiene.py#scan_temp_file`) follows an `mv` source that is
  one expansion one hop, to its latest binding in the innermost function holding the line. The
  source is admitted when that binding holds `$(mktemp`, and is `fixed`, the gated class, when no
  unpredictable part names it. A binding in another function is unfollowed, which the lint's own
  boundary row "a temp bound in another scope" records as a miss
  (`tools/gate-lint/sh_hygiene.py@448d62cb:1014`).
- The driver's spec-token check has two halves. `init_spec_token_check` starts the checker through
  `init_bounded` (`tools/unattended/unattended.sh@a9ff4a9c:14609`), and `run_spec_token_check` reads
  it and writes the whole key at `tools/unattended/unattended.sh@a9ff4a9c:14667`. The start half
  hands the read half its state through seven `ST_` globals
  (`tools/unattended/unattended.sh@a9ff4a9c:14588`).

### Mechanisms weighed (M12)

What would make each lose was written before any probe ran.

| | A: the caller names the next generation | B: the checker promotes its own generation | C: the caller names it and records it live, with no rename |
|---|---|---|---|
| how | `SPEC_TOKENS_CACHE_NEXT` names a directory the caller made with `mktemp -d`; after its bracket the caller removes `<dir>` and renames the named directory to it | the checker keeps `<dir>.next`, and a later checker call told to keep it runs `shutil.rmtree` and `os.replace` | A's contract; the driver writes the generation's name beside the whole key and reads it back as `SPEC_TOKENS_CACHE`, renaming nothing |
| loses if | the lint gates the rename, or the `mktemp` fork costs near the mode's saving | a fixed-name temp remains, or keeping costs a process | it adds state a reader must validate before it removes anything |
| the lint | the rename is unfollowed, never gated, because the two halves bind and rename in different functions. In one function it is admitted | no shell `mv` to read. `<dir>.next` and its window between `rmtree` and `makedirs` stay, in Python, which no shell predicate reads | no `mv`. The name file is a direct write at a fixed destination, as the whole key's record already is |
| the bracket | renamed only at the whole key's write. A moved tree leaves the generation unpromoted in its own directory, which the next start sweeps | the bracket closes after the key's replay, after the checker exits, so keeping needs a third checker process at the write site | named live only at the whole key's write, as A |
| a run killed mid-write | the checker writes its input record at exit, so a killed checker leaves none and nothing is promoted. A driver killed between `rm -rf` and `mv` leaves no live cache, and every spec misses once | as A, and the orphan is `<dir>.next`, which the next run's `rmtree` reclaims | the name file is written once, so a kill leaves the old name or a truncated one, a miss either way |
| result | survives. The lint gives no coverage for the rename, which F1 puts to the owner | loses on both counts | survives, at the cost of a name file, a shape check and a sweep that spares the live generation |

The tests behind the table:

- **The lint, A.** `scan_temp_file` over four shapes, run on 2026-11-15 at `dd9006677`. A start
  function binding `ST_NEXT=$(mktemp -d "$d/s.$1.specs.XXXXXXXX")` and a read function renaming
  `"$_stnext"` after `_stnext=$ST_NEXT` gave `unfollowed`. The same read function renaming `"$ST_NEXT"`
  directly gave `unfollowed`. One function binding `n=$(mktemp -d "$s.XXXXXXXX")` and renaming `"$n"`
  gave `admitted`. TOOL-aPiecewiseGrade-2's rev-2 line, `mv "$_stspecs.next" "$_stspecs"`, gave `fixed`.
- **The cost, A.** `mktemp -d` took 0.022 s to 0.028 s over three runs (PINNED dd9006677, this node).
- **The cost, B.** The driver derives the key over the record before its second tree read
  (`tools/unattended/unattended.sh@a9ff4a9c:14657`), so no existing checker call sits after the
  bracket closes. A checker process doing `--input-key` over a one-line record took 0.23 s to 0.26 s
  over three runs (PINNED dd9006677, this node). TOOL-aPiecewiseGrade-1's mode saves about 1 s
  (DERIVED d9f84ee14, that spec's table).
- **The rename, B.** On this node, `os.replace` onto a directory holding a file raised
  `PermissionError`, and `mv a b` with `b` present moved `a` into `b`. So every mechanism that
  renames still removes `<dir>` first, and B gains no atomic swap over A.

A rename across the driver's two halves cannot be admitted by a lint that follows one hop inside
one function. That is a fact about the lint, not about A: a rename B or C does not make is not
gated either. F1 asks the owner which of A and C TOOL-aPiecewiseGrade-2 builds. This unit's contract
serves both, so its build does not wait on F1.

### S1 — when the mode runs

`main` reads `SPEC_TOKENS_CACHE_NEXT` as it reads `SPEC_TOKENS_CACHE`, with a trailing separator
dropped. The mode runs when both are set and not empty, `named_specs` is None, and the two do not
name one directory, compared by `os.path.normcase` over `os.path.realpath`. Otherwise `cache` is the
empty string and the loop runs exactly the plain run, as it does today with the variable unset. Two
names for one directory would make the run write the directory it reads, so that pair is refused
silently, by default.

The module-level call keeps its condition and passes the named directory as a third argument.

### S2 — where the generation goes

Where `main` removed and re-created `<dir>.next`, it now only creates `graded.list` in the named
directory, empty, inside the same `try` that swallows `OSError`. `read_spec_cache` takes the named
directory in place of `cache + ".next"`, and `write_spec_cache` takes it in place of `cache`, which
it used for nothing else. Every write keeps its form, its order and its failure rule: a write that
fails leaves that entry out and prints nothing.

The named directory is the caller's. A missing one makes every write fail, so the run writes nothing
and still prints the plain run's bytes. The checker never calls `os.makedirs`, `shutil.rmtree` or
`unlink` on it, and `unlink` stays only on the entry files a failed write left half-written.

### S3 — the trace

`arm_input_trace(path, cache="", nxt="")` puts `<cache>` and `<nxt>` in `INPUT_TRACE["cache"]`, in
place of `<cache>` and `<cache>.next`. The hook reads that tuple for opens and listings as today.
The skip matters: `write_spec_cache` reads back each `.inputs` it wrote in the named directory,
outside any segment, and without the skip that read would enter the whole record and move the whole
key on every run.

### S4 — what keeps its bytes

The plain run, `--spec`, `--pass-spec`, `--legs-for`, `--input-key` and `--list` never reach the
mode, as today. With the mode on, the per-spec key, the context digest, the lookup, the segment rule
and the loop's order are unchanged, so the output, the record and each entry's bytes are the ones
the `<dir>.next` contract produced. Only the directory the entries land in moves.

### S5 — the docstring

The usage line becomes `SPEC_TOKENS_CACHE=<dir> SPEC_TOKENS_CACHE_NEXT=<new> python <prefix>/check-spec-tokens.py`.
The paragraph's last three sentences say the run writes the whole next generation into the
directory `SPEC_TOKENS_CACHE_NEXT` names, which the caller made empty with an unpredictable name and
which the run never creates or removes. They say the caller promotes SPEC_TOKENS_CACHE_NEXT only under
its own bracket, by passing it as a later run's `SPEC_TOKENS_CACHE`, and that with either
variable empty, or the two naming one directory, the run is the plain run.

### The two arms

The `PG1` arm (`tools/check-spec-tokens.test.sh@eeb7f115:2360`) moves onto the contract. Every
incremental call names a fresh `mktemp -d "$pc.XXXXXXXX"`, the in-process call that captures the
context digest included, and each promotion renames that directory over `$pc`. Its eleven
`check_grade_step` lines and its plants keep their bytes. The generation check reads `$pc.next` as
absent right after the incremental run, before the promotion, which is the contract's own claim.

The `PG4` arm follows it and adds three assertions:

1. The generation lands in the named directory, and `$pc.next` never appears.
2. A named directory that does not exist is not created, and a file already in a named directory
   survives the run.
3. `SPEC_TOKENS_CACHE` alone, and the two variables naming one directory, each leave the cache's
   parent and the cache's files as they were.

The suite runs bash, so its own `mv` lines are not in the lint's population. Each arm's promotion
binds the `mktemp` and renames in one function, the shape `scan_temp_file` admits.

### What the design does not check

Carried from TOOL-aPiecewiseGrade-1: a path probed only for existence, the environment beyond the
launcher, and a forged entry, which the bar's plain run backstops.

New with this design:

- **The named directory's provenance.** The checker does not check that the directory is empty, that
  its name was unpredictable, or that it sits beside the cache. The contract says the caller made it
  with `mktemp -d`; TOOL-aPiecewiseGrade-2's criteria observe that its caller does.
- **The caller's promotion** is out of the lint's sight: the lint reads `mv` alone, and F1's pick
  renames nothing.
- **One directory nested in the other.** Only the equal pair is refused. A named directory inside
  `<dir>` would put the generation inside the cache it read.
- **An older checker.** A caller passing both variables to a checker built before this unit gets a
  `<dir>.next` written and an empty named directory. Promoting it costs a miss per spec at the next
  run, never a wrong verdict. The checker and the driver ship from this repository and land
  together.

### The pass probe, `$SCRATCH/pg4.sh`

`$SCRATCH` is the run's scratch directory. The probe builds the `PG1` arm's fixture at `$TEMP/pg4`,
lifted from the suite (`tools/check-spec-tokens.test.sh@eeb7f115:2368`), with the built checker and
the memory-tree kit copied into the fixture's tool root. `C` is the cache, and each incremental run
names a fresh `mktemp -d "$C.XXXXXXXX"`. `same` is 1 when stdout, stderr and the status equal the
plain run's over the same tree.

| line | what happens | what it prints |
|---|---|---|
| `cold` | no cache; one run naming `N1`, then `N1` renamed to `C` | `cold graded <lines of N1/graded.list> entries <.json files in N1> dotnext <0|1> same <0|1>` |
| `warm` | one run naming `N2`, `C` snapshotted with `find "$C" -type f -exec sha1sum {} +` before and after | `warm graded <n> entries <n> untouched <0|1> dotnext <0|1> same <0|1>` |
| `missing` | one run naming `$C.gone`, which does not exist | `missing made <0|1> same <0|1>` |
| `planted` | `N3` holds `keep.me` before one run naming it | `planted kept <0|1>` |
| `alone` | `SPEC_TOKENS_CACHE` alone; `ls -a` of the cache's parent and `C`'s snapshot before and after | `alone wrote <0|1> same <0|1>` |
| `selfnamed` | both variables naming `C` | `selfnamed wrote <0|1> same <0|1>` |
| `record` | `SPEC_TOKENS_INPUTS` beside both variables, cold and then warm, against the plain run's record | `record cold <0|1> warm <0|1>` |
| `step` | the `PG1` arm's eleven steps, each promoting from a fresh named directory | the arm's `step` lines, then `regraded <n> <path>` |

`dotnext` is 1 when `$C.next` exists right after the run. The rows run in table order over one
fixture. The `record` row removes `C` first, and the `step` rows run over a fresh fixture with no
cache, as the arm does.

### Inventory

| identifier | kind | lexicon |
|---|---|---|
| `SPEC_TOKENS_CACHE_NEXT` | environment variable the checker reads | no declared cell; spelled as `SPEC_TOKENS_INPUTS` is |
| `nxt` | parameter of `arm_input_trace`, `read_spec_cache` and `write_spec_cache`, and a local of `main` | no declared cell for a parameter |
| `PG4` | the suite's assertion label | no declared cell |

No function, conf key, check number or refusal line is minted. Three functions change their
parameters in place.

### Docs, and what the change owes beyond the code

- The checker's header docstring, per S5.
- No `help/` page names `SPEC_TOKENS_CACHE`, grepped at `dd9006677`.
- The codebase map's symbol index records each function's name, kind and file, none of which
  moves, so it is not regenerated.
- The kit epoch leg sees shipped bytes move, and the lander's mint moves the version.

### Rollout

This unit builds at order 3, after TOOL-aPiecewiseGrade-1 is CLOSED, against the checker at
`e535b5ee`. No product caller sets the variable before TOOL-aPiecewiseGrade-2, so the mode stays
dark until it lands. `FLOOR_ASSERTIONS` in the spec-tokens self-test rises from 275 to 278 by the
three `PG4` assertions, which the close confirms from a real run.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **B, the checker promotes its own generation.** Rejected by the tests above: it keeps the fixed
  name and its window between `rmtree` and `makedirs`, moved into Python where no shell predicate
  reads it, and keeping costs a third checker process, 0.23 s to 0.26 s (PINNED dd9006677), against a
  mode that saves about 1 s (DERIVED d9f84ee14).
- **Keep `<dir>.next` when `SPEC_TOKENS_CACHE_NEXT` is unset.** Two contracts, one with no caller.
  The charter's `[yagni]` says delete rather than disable.
- **A read-only mode for `SPEC_TOKENS_CACHE` alone.** TOOL-aPiecewiseGrade-2 sets both whenever the
  sidecar root resolves, so no caller passes one alone.
- **The checker makes the directory with `tempfile.mkdtemp`.** The caller then cannot learn its
  name without a new output, and stdout and stderr must stay the plain run's.
- **The checker empties the named directory first.** A directory `mktemp -d` made is empty, and a
  checker that removes what a caller names re-opens the window this unit closes.

## 5. Production-readiness checklist

- security — the checker writes only into a directory the caller made with an unpredictable name,
  and never creates or removes it, so no fixed name sits between a removal and a write. Two names for
  one directory turn the mode off.
- perf / scale — none in the checker. The caller's `mktemp -d` costs 0.022 s to 0.028 s per run
  (PINNED dd9006677, this node).
- error / empty / loading states — a missing or unwritable named directory leaves every entry out
  and prints nothing, and the output is the plain run's.
- observability — `graded.list` in the named directory names every re-graded spec.
- risks — an older checker beside a newer driver writes `<dir>.next`, which costs misses only. The
  two land together.
- testing — the pass probe above, and both arms observed RED then GREEN at the close.
- migration — none in the checker. A `<dir>.next` left by an earlier run is never read again;
  TOOL-aPiecewiseGrade-2's sweep removes it.
- user docs — the checker's header docstring. No `help/` page names this surface.

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/pg4.sh"`, described in §4, removed after the
pass.

- **AC1** — When `bash "$SCRATCH/pg4.sh"` runs, it prints `cold graded 3 entries 3 dotnext 0 same 1`
  and `warm graded 0 entries 3 untouched 1 dotnext 0 same 1`.
  Red when: the checker still writes `<dir>.next`, writes into the cache it reads, or leaves a hit
  or a fresh entry out of the named directory.
- **AC2** — When `bash "$SCRATCH/pg4.sh"` runs, it prints `missing made 0 same 1` and
  `planted kept 1`.
  Red when: the checker creates the named directory with `os.makedirs`, or empties it with
  `shutil.rmtree`.
- **AC3** — When `bash "$SCRATCH/pg4.sh"` runs, it prints `alone wrote 0 same 1` and
  `selfnamed wrote 0 same 1`.
  Red when: the mode runs on `SPEC_TOKENS_CACHE` alone, or runs when the two variables name one
  directory.
- **AC4** — When `bash "$SCRATCH/pg4.sh"` runs, it prints `record cold 1 warm 1`.
  Red when: the trace keeps `<cache>.next` in its skip prefixes in place of the named directory, so
  the read-back of each written `.inputs` enters the record.
- **AC5** — When `bash "$SCRATCH/pg4.sh"` runs, its eleven `step` lines each begin with the string
  the `PG1` arm's `check_grade_step` call expects (`tools/check-spec-tokens.test.sh@eeb7f115:2421`
  through `tools/check-spec-tokens.test.sh@eeb7f115:2432`), and it prints `regraded 1` followed by
  the edited spec's path.
  Red when: the named generation drops a reused entry or keeps a spec that left the live set, so a
  later step re-grades more than its change moved or reuses a stale entry.
- **AC6** — When `grep -c '\.next' tools/check-spec-tokens.py` runs it prints 0, and
  `grep -c 'promotes SPEC_TOKENS_CACHE_NEXT only under its own bracket' tools/check-spec-tokens.py`
  prints 1.
  Red when: a fixed `.next` name survives in the checker, or the docstring leaves the new contract
  unstated.

## 7. Gates

`spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `spec tokens (the pass's own spec)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 AC3 · the PG4 arm's three assertions after the PG1 arm; staged RED by restoring the old rmtree and makedirs of the fixed next name, which reds the first two, then by running the mode on SPEC_TOKENS_CACHE alone, which reds the third · FLOOR_ASSERTIONS 275 to 278, which the close confirms
New arm: tools/check-spec-tokens.test.sh · covers AC4 AC5 · the PG1 arm moved onto the named directory, its steps unchanged; staged RED by keeping the fixed next name in the trace's skip prefixes, which reds its record assertion · none

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
the spec-token checker's `--spec` over this file.

## 8. Open questions

- **F1 — The lint cannot admit a rename across the driver's two halves. Which promotion does TOOL-aPiecewiseGrade-2 build on this contract?**
  The brief asked for a promotion the lint admits. `scan_temp_file` follows a binding one hop inside
  one function, and the driver makes the directory in its start half and renames it in its read
  half, so any rename there reads as unfollowed (§4, the tests). Options:
  - (a) A: the start half makes the directory with `mktemp -d` and carries it in an eighth `ST_`
    global, and the read half renames it over the cache where the whole key is recorded. The leg
    passes with no registry row and prints the site as unfollowed, which is not coverage.
    TOOL-aPiecewiseGrade-2's own criteria observe that the name came from `mktemp -d` and that no
    `.next` name exists.
  - (b) C: the read half writes the generation's name into a file beside the whole key and removes
    the old generation, renaming nothing. No `mv` exists for the lint to read. It costs a name file,
    a shape check on every name read back before `rm -rf` sees it, and a sweep that spares the live
    generation.
  - (c) A, plus a lint unit outside this build that follows a global bound in another function of
    the same file. Its wider predicate would re-measure every product shell source.
  Recommendation: (a). It is the smallest change to TOOL-aPiecewiseGrade-2's ratified design, its
  name is unpredictable whether or not the lint can see that, and (b) adds a file that goes to `rm -rf`
  to avoid a rename the lint does not gate.
  RESOLVED (owner, 2026-11-15): (b) Name file, no rename

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft from brief `2026-11-15-prompt-TOOL-aPiecewiseGrade-4-forks-brief`,
  the owner's answer (c) to TOOL-aPiecewiseGrade-2's divergence in
  `2026-11-15-prompt-TOOL-aPiecewiseGrade-2-revision`, grounded at `dd9006677`.
- rev-2 · 2026-11-15 · §8 · §3 · S5 · §4 · from brief
  `2026-11-15-prompt-TOOL-aPiecewiseGrade-2-1-spec-writer`: F1 RESOLVED as the owner's (b), a name
  file and no rename, with the ratified pointer. Three sentences the pick made false are rewritten:
  the hands-off edge's "renaming it into place only where the whole key is recorded", S5's
  docstring clause "by removing `<dir>` and renaming the named directory to it", and the
  not-checked bullet "A rename across the driver's two halves". The contract does not move.

## 10. Reuse audit

The seams this unit extends are TOOL-aPiecewiseGrade-1's own: the mode's block in `main`
(`tools/check-spec-tokens.py@e535b5ee:2416`), `read_spec_cache`, `write_spec_cache` and
`arm_input_trace`, each changed in place to take the named directory. The caller's shape is the
driver's own `mktemp` beside a destination (`tools/unattended/unattended.sh@a9ff4a9c:2066`) and the
lint's remedy text, `t=$(mktemp -u "$dest.XXXXXXXX")`, with `-d`. `tools/codebase-map/reuse_lookup.py`
for "write the next cache generation into a directory the caller made with mktemp and rename it into
place" ranked `write` stems and the suite's `mktemp`, generic names only, so no generation or
promotion seam fits beyond these. Recall's top hits were this build's revision record and
TOOL-dRedressedBar-24, the unit that wrote the lint and its one-hop rule.

Recall terms used: `python tools/memory-recall/query.py "how does a shell caller promote a directory generation without a fixed-name temp renamed into place" --terms "mktemp fixed-temp rename promote generation sidecar cache next directory temp-names binder unfollowed"`
