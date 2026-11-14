# TOOL-aBriskDeclaration-1 — `--dispatch` reads the order verb with no process, and starts the spec-token checker before the open-pass reader

**Status:** CLOSED · rev-2 · 2026-11-14 · node a · Tier-2 · base 846d51d39 · streams tooling · order 1 · ratified 2026-11-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aBriskDeclaration-1-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aBriskDeclaration-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-14-build-TOOL-aBriskDeclaration-1-analysis.md](../build/2026-11-14-build-TOOL-aBriskDeclaration-1-analysis.md) | research | — |
| [2026-11-14-prompt-TOOL-aBriskDeclaration-1-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aBriskDeclaration-1-2-builder.md](../prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-2-builder.md) | journal | — |
| [2026-11-14-prompt-TOOL-aBriskDeclaration-1-3-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-3-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aBriskDeclaration-1-4-builder.md](../prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-4-builder.md) | journal | — |
| [2026-11-14-prompt-TOOL-aBriskDeclaration-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-brief.md) | research | — |
| [2026-11-14-prompt-TOOL-aBriskDeclaration-1-forks-brief.md](../prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-forks-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

One `--dispatch` of an order-7 unit in a 99-unit build took 625.6 s on node a: its order gate
starts about seven processes per unit to read one header line, and the spec-token checker starts
only after the open-pass reader returns, though neither reads the other. This unit reads the order
verb with shell builtins and starts the checker before the reader, reading its answer where it is
read today, so a declaration costs the longer of the two, and every refusal, note and parked row
reads as it did.

## 2. Scope (IN)

- **S1** — `order_verb_of` reads the spec's first line that begins with `**Status:**` with the
  `read` builtin, one trailing CR stripped, matches `ORDER_OK_RE` and `ORDER_LOOSE_RE` with
  `[[ =~ ]]`, and leaves its answer in `_order_verb` as well as printing it. Its answers are the
  old reader's, `MALFORMED <loose>` included. Observed by AC1.
- **S2** — The order gate's two call sites in `verb_dispatch` call it with stdout sent to
  `/dev/null` and read `_order_verb`, so neither forks. Observed by AC2.
- **S3** — A start half, `init_spec_token_check`, decides what the checker block decides today
  and records it in five `ST_` globals; under `run` it starts the checker through `init_bounded`.
  It prints nothing and refuses nothing. Observed by AC3, AC6.
- **S4** — `run_spec_token_check` becomes the read half: it calls the start half itself when no
  start ran, takes and empties the record, and prints every line and makes every refusal it makes
  today, in the same order. Observed by AC3, AC6, AC7.
- **S5** — `verb_dispatch` calls `init_spec_token_check "$slug"` on the line before
  `sibrows=$(read_open_passes "$rel")`, below the HEAD refusal; `run_spec_token_check` stays where
  it is. Observed by AC3.
- **S6** — `remove_spec_token_check` waits for a started checker and discards its answer, never
  killing it, and the generator-pairing and condition-1 refusals call it between their `fail 49`
  and their `return 1`. Observed by AC4, AC5, AC12.
- **S7** — The comments that state the old order are made true (§4, "Comments made true").
  Observed by AC9.
- **S8** — The verbs guide's `--dispatch` paragraph says the checker is started before the
  open-pass reader and read after condition 1, in `tools/unattended/VERBS.template.md` and its copy
  `memory/guides/UNATTENDED-VERBS.md`, byte-equal past line 1. Observed by AC8.
- **S9** — The suite arms of §4, "The arms", in `tools/unattended/unattended.test.sh`. Observed by
  AC1, AC3, AC4, AC5, AC6, AC12.
- **S10** — No `fail 49` site moves, so `tools/unattended/unarmed-branches.txt` is not re-keyed.
  Observed by AC7.
- **S11** — `memory/map/generated/symbols.json` regenerated, carrying the two new functions.
  Observed by AC10.
- **S12** — A measured before and after of one whole `--dispatch` on the frozen clone, with process
  counts, recorded by the main loop under this build's `build/` folder. Observed by AC11.

## 3. Non-goals (OUT)

- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`. The live
  dDeclaredLoop branch rewrote the first three, so a change here conflicts when that run merges main.
- The spec-token checker's own cost, its joins and its key's inputs; `gate-fingerprint.sh`.
- `memory/builds/dDeclaredLoop/`, its run's worktree and its branch.
- Check 49's index-with-its-generator refusal text and condition, which stay as they are; only a
  call is added before its `return 1`.
- Any refusal's or note's text, check number or relative order.
- Starting the checker any earlier than the open-pass reader. Each refusal between the start and
  the read would wait for the checker, and the order gate this unit speeds up no longer needs it.
- A shared discard helper with `read_preflight_probes` (§4, "Alternatives rejected").
- The kit version: the lander's `mint` moves it (`tools/push-main.sh`, its "KIT VERSIONS ARE
  MINTED HERE" comment).
- A `help/` page: none covers `--dispatch` (`grep -rlF -e --dispatch help/` matches nothing at base).

### Edges

- **hands-off** external — the open-pass reader's own cost, about half of it the per-key Python
  reader and `resolve_python` probe on the dDeclaredLoop branch, is that run's branch to fix.

## 4. Design

### Evidence

Read at base `846d51d39`. Line numbers are `tools/unattended/unattended.sh` unless named.

| Line | What sits there |
|---|---|
| `tools/unattended/unattended.sh@95b8f840:1021` | `ORDER_OK_RE` and, on the next line, `ORDER_LOOSE_RE`, both POSIX ERE |
| `tools/unattended/unattended.sh@95b8f840:4833` | `order_verb_of`: `grep -m1`, then `printf` piped through `grep -oE`, `head`, `grep -oE`, `head` |
| `tools/unattended/unattended.sh@95b8f840:270` | `init_bounded`: starts a child, records it, leaves `RB_HANDLE`; prints nothing |
| `tools/unattended/unattended.sh@95b8f840:314` | `read_bounded`: `wait`s the handle, sets `RB_OUT`, `RB_STDOUT`, `RB_ERR` and `RB_TOOK` from the child's own end stamp |
| `tools/unattended/unattended.sh@95b8f840:3364` | `read_preflight_probes`: reads each unread handle and discards it, never a kill |
| `tools/unattended/unattended.sh@95b8f840:397` | `resolve_python`: on failure prints a diagnosis on stderr (`} >&2` at `:543`), and under `platforms.provision` uv with stderr a terminal it prompts on `/dev/tty` (`:522`) |
| `tools/unattended/unattended.sh@95b8f840:14430` | `derive_spec_token_key`: every child's stderr to `/dev/null` |
| `tools/unattended/unattended.sh@95b8f840:14458` | `run_spec_token_check`: blank, missing, resolver, key, skip, cache-off, `run_bounded`, verdict, record |
| `tools/unattended/unattended.sh@95b8f840:14542` | the dispatched unit's `_d_ord=$(order_verb_of "$_d_spec")`; the sibling one is at `:14551` |
| `tools/unattended/unattended.sh@95b8f840:14746` | the HEAD refusal, the last refusal above the reader |
| `tools/unattended/unattended.sh@95b8f840:14765` | `sibrows=$(read_open_passes "$rel")` |
| `tools/unattended/unattended.sh@95b8f840:14813` | the generator-pairing refusal; condition 1's is at `:14830` |
| `tools/unattended/unattended.sh@95b8f840:14841` | `run_spec_token_check "$slug" \|\| return 1` |
| `tools/unattended/unattended.sh@95b8f840:15459` | `main` calls `verb_dispatch` directly, in the top-level shell |

The order loop runs only when the dispatched unit's own spec carries an order verb (`:14547`); it
then calls `order_verb_of` once per other unit of the build. Nothing after `verb_dispatch` returns
reads an `RB_` value: the only exit trap is `write_runlog_end` (`:15279`).

### The order verb reader

```
order_verb_of() { # spec file -> prints the order integer, or nothing, and leaves it in `_order_verb`; refuses a malformed verb
  local hdr="" n="" loose="" line
  _order_verb=""
  [ -f "$1" ] || return 0
  while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in '**Status:**'*) hdr=${line%$'\r'}; break ;; esac
  done 2>/dev/null <"$1"
  [ -n "$hdr" ] || return 0
  [[ $hdr =~ $ORDER_OK_RE ]] && [[ ${BASH_REMATCH[0]} =~ [0-9]+ ]] && n=${BASH_REMATCH[0]}
  if [ -z "$n" ]; then
    [[ $hdr =~ $ORDER_LOOSE_RE ]] && loose=${BASH_REMATCH[0]}
    if [ -n "$loose" ]; then _order_verb="MALFORMED $loose"; printf '%s' "$_order_verb"; return 0; fi
  fi
  _order_verb=$n; printf '%s' "$n"; return 0
}
```

The `[ -f ]` guard and the loop's `2>/dev/null`, placed before the input redirect, keep a missing
path, a directory or an unreadable file silent with an empty answer, as the old `grep -m1` with
its stderr silenced was. The prototype guarded with `[ -r ]`, which lets a directory reach the redirect, and
bash then prints `read: read error: 0: Is a directory` on stderr (observed on node a, 2026-11-14).
The call sites become `order_verb_of "$_d_spec" >/dev/null; _d_ord=$_order_verb` and the same with
`_o_spec` and `_o_ord`. A redirect on a function call forks nothing.

The ten planted headers below are what AC1 and the new arm grade. Each answer is the base reader's,
PINNED from a run on node a on 2026-11-14 under `LC_ALL=C` and `LC_ALL=C.UTF-8`, GNU grep 3.0 and
bash 5.3.9; the candidate above gave the same ten. Each header is the line
`**Status:** SPECCED · rev-1 · 2026-11-14 · node a · Tier-2 · base 0123abcd` followed by the tail.

| # | Tail, or the file's shape | Answer |
|---|---|---|
| 1 | ` · order 7` | `7` |
| 2 | ` ·  order 7`, two spaces | `7` |
| 3 | ` ·order 7`, no space | `7` |
| 4 | ` · order 7 · streams tooling` | `7` |
| 5 | ` · order 7`, then CR LF | `7` |
| 6 | ` · order 7x`, then CR LF | `MALFORMED · order 7x` |
| 7 | ` · order 2x` | `MALFORMED · order 2x` |
| 8 | no tail | empty |
| 9 | two header lines, ` · order 3` then ` · order 9` | `3` |
| 10 | ` · order 7`, the header indented two spaces | empty |

### The checker's two halves

The start half records, the read half prints. The record is five globals declared beside the
functions, in the `RB_` and `PF_PROBE_` register:

| Global | Holds |
|---|---|
| `ST_STATE` | empty when no start ran; else `blank`, `missing`, `nopython`, `skip` or `run` |
| `ST_PY` | the launcher `resolve_python` printed |
| `ST_KEY` | the key `derive_spec_token_key` printed, or empty, which is the cache off |
| `ST_REC` | the record path, `<sidecar>/spec-tokens.<slug>.key`, or empty |
| `ST_HANDLE` | the `init_bounded` handle under `run`, or empty when the capture could not be made |

`init_spec_token_check "$slug"` empties all five, then decides in today's order: a blank
`SPEC_TOKENS_CLI` is `blank`; a declared file that is not there is `missing`;
`ST_PY=$(resolve_python 2>/dev/null)` failing is `nopython`; it derives `ST_KEY`, resolves
`ST_REC` and reads the record with `read -r`, and a match is `skip`; otherwise it is `run`, and
`init_bounded "$ST_PY" "$SPEC_TOKENS_CLI" && ST_HANDLE=$RB_HANDLE`. The resolver's stderr is
silenced here because the start cannot hold it for the read without a file, and printing it here
would move it ahead of the reader's notes and onto a condition-1 refusal that never printed it.
With stderr not a terminal, the silenced call never reaches the uv prompt.

`run_spec_token_check "$slug"` keeps its name, its header line and its contract:

1. `[ -n "$ST_STATE" ] || init_spec_token_check "$slug"`. The verb always starts first, so this
   serves direct callers, the suite's in-process cache arms among them. As `run_bounded` is
   `init_bounded` then `read_bounded`, it is then the two halves back to back.
2. It copies the five globals into its locals `_stst`, `_stpy`, `_stkey`, `_strec` and `_sth`, and
   empties the globals, so a later call in the same shell never reads this call's record. The
   prototype never emptied `ST_STATE`, and a second in-process call reused the first one's verdict.
3. `blank` echoes the announced skip and returns 0. `missing` makes the not-there refusal and
   returns 1. `nopython` runs `resolve_python >/dev/null || :`, so its diagnosis, or its prompt,
   prints on stderr where it always printed, then makes the resolver refusal and returns 1 on the
   start's verdict, not the second call's. `skip` echoes the skip line with `${_stkey:0:12}`.
4. Under `run`, an empty `_stkey` echoes the cache-off line. A non-empty `_sth` is read with
   `read_bounded "$_sth"`, and an empty one, a start that could not make its capture, runs
   `run_bounded "$_stpy" "$SPEC_TOKENS_CLI"`, which prints that sentence as it always did, the shape
   `init_preflight_probes` states for its probes. `_strc` takes the status.
5. The verdict through `check_spec_token_hits`, the refusal and the foreign-only note are the
   current lines unchanged. The record write becomes `mkdir -p "${_strec%/*}"` then the `printf`,
   since a slug carries no slash. The prototype's separate directory global was redundant.

`remove_spec_token_check` runs `[ -z "$ST_HANDLE" ] || read_bounded "$ST_HANDLE" || :`, then
empties the five globals, and prints nothing. It never kills: `read_preflight_probes` gives the
reason, a kill being the least reversible act the driver takes. It does not put `RB_` values back,
because nothing reads them after the verb returns.

Every `fail 49` stays inside `run_spec_token_check` in today's order: missing, resolver, red. The
start and remove halves hold no `fail`. So check 49's ordinals are as at base, the three pinned
rows of `tools/unattended/unarmed-branches.txt` at 8, 15 and 21 keep their keys, and the suite's
launcher arm's literal `run_bounded "$_stpy" "$SPEC_TOKENS_CLI"` is still in the source.

### The window between the start and the read

The start sits on the line above `sibrows=$(read_open_passes "$rel")`, below the HEAD refusal, so
every refusal above it returns with no checker started. Two refusals sit between the start and the
read, and each becomes `fail 49 "<unchanged text>"; remove_spec_token_check; return 1`:

| Refusal | Base line |
|---|---|
| the index declared with its generator | `tools/unattended/unattended.sh@95b8f840:14813` |
| condition 1, a path a sibling pass already declared | `tools/unattended/unattended.sh@95b8f840:14830` |

Those two now take the longer of the reader and the checker, where they took the reader's time.
The read half reads the handle on every one of its paths that has one: only `run` has a handle, and
`run` always reaches the read.

**Nothing between the start and the read writes the tree.** Between them run `read_open_passes`,
whose `check_pass_open` and `pass_commit` run `git rev-parse`, `git log` into a `mktemp` scratch
file under `TMPDIR`, and `git diff-tree`; the `_sibothers` count and the empty-set note; the nested
`resolve_generator`, which runs `git ls-files`; `overlaps` and `normpath`, which read strings; and
`fail`, which echoes and sets `status` and `RUNLOG_CHECKS`. None writes the work tree, the index or
a ref. So the key the start derived describes the tree the checker reads, and an admitted verdict
recorded at the read is recorded under the key of the tree it graded.

What would break it: a write moved above the read (the claim write, `park`, `stage_or_fail`), a
`git status` added between, which may rewrite the index, or a writer added to `read_open_passes`.
Any of those lets the checker grade a tree the key does not describe. AC5's predicate does not see
it; the block comment above the start says so in one sentence.

### Output parity

The start prints nothing on either stream. Every line the checker block printed is printed by the
read half, at the old call's position, after condition 1, so the reader's stderr notes and the
empty-set note keep their place before it. The two waiting refusals print what they printed. The
checker's own stdout and stderr go to the capture files as before. `RB_TOOK` in the red refusal is
the child's own wall from `init_bounded` to its end stamp, as `read_bounded` defines it.

### Comments made true

- `run_spec_token_check`'s header: "derived BEFORE the checker runs" stays true; a sentence says
  the start half derives the key and starts the checker before the open-pass reader, the read half
  prints and refuses where the call always sat, and a direct call runs the two back to back.
- The block comment above the call in `verb_dispatch`, "IT RUNS LAST AMONG THE LOCAL REFUSALS",
  says it is READ last: started before the reader, read after condition 1. A new comment above
  the start names the window, the two refusals that call `remove_spec_token_check`, and the
  no-write invariant with what breaks it.
- `order_verb_of`'s "Both call sites read this through `$( )`" says both call sites read
  `_order_verb` with no fork. The sentinel stays the caller's to refuse, because one place holds both
  refusal texts and a `$( )` reader would hit the old trap.
- The verbs guide's "It runs last because it costs a tree-wide scan" becomes this sentence: "It is
  started just before the open-pass reader and read after condition 1, because it costs a tree-wide
  scan: it runs beside the reader, a refusal between the two waits for it and discards its answer,
  and its own refusal still prints after every refusal above it — the order gate, the edge and hold
  gates, the path and shared-record refusals, condition 1 — each decided from the run-state file,
  the spec headers or `git`."

### The arms

One group in region 3 of `tools/unattended/unattended.test.sh`, after the aSwiftRefusal-4 positive
control (`tools/unattended/unattended.test.sh@0d9cd163:7961`) and before the aSwiftRefusal-2 group, which
resets `RUN.md`. At that point ARCH-tRun-4 is dispatched on `${PFX}swift.sh` and the stub exiting 1
is declared. Each traced run is a process, `bash -x "$SCRIPT"` through `run_main_at_head`, counted as
`run_proc` counts one, its stderr to a file under `$TMP`. The group restores what it changes.

- **A1, the order verb.** With `PATH` emptied in a subshell of the suite, which sourced the driver
  at its prologue, the ten §4 plants each leave the table's answer in `_order_verb`, read as
  `${_order_verb-UNSET}`. The slice of `order_verb_of`, comment lines removed, carries no `$(` and no
  backtick. The trace of the ARCH-tRun-5 dispatch on `${PFX}swift5.sh` carries at least one line
  matching `^\+ order_verb_of ` and none matching `^\+\+ order_verb_of `.
- **A2, start before the reader.** In that same trace, the first line matching
  `^\++ init_bounded .*swift-stub\.py` precedes the first matching `^\++ read_open_passes `, and a
  line matching `^\++ read_bounded ` follows that; the output carries the spec-token refusal.
- **A3, a condition-1 refusal waits.** The trace of the ARCH-tRun-5 dispatch on `${PFX}swift.sh`
  carries the stub's `init_bounded` line, a line matching `^\++ fail 49 .--dispatch declares a path`,
  a `read_bounded` line after it, and no line matching `^\++ kill ` after it. The output
  carries condition 1's text and not the spec-token refusal.
- **A4, the window's class.** Over `verb_dispatch`'s source, the non-comment lines after the
  `init_spec_token_check "$slug"` call and before the `run_spec_token_check "$slug"` call that
  match `return 1` number at least two, and each carries `remove_spec_token_check`.
- **A5, the start prints nothing.** In a subshell after `load_driver_conf`, with a `resolve_python`
  double that prints `RESOLVER-DIAG` on stderr and returns 1, `init_spec_token_check tRun` prints
  nothing on either stream and leaves `ST_STATE` at `nopython`. A following
  `run_spec_token_check tRun` prints `RESOLVER-DIAG` and then the resolver refusal.
- **A6, a generator-pairing refusal waits** (the owner's F2 pick). Placed after A3 and before A4:
  the group appends `GENERATED_INDEXES="${PFX}bd-idx.md:${PFX}bd-gen"` to `.unattended.conf`, and
  the trace of the ARCH-tRun-5 dispatch with `--writes ${PFX}bd-idx.md --writes ${PFX}bd-gen`
  carries the stub's `init_bounded` line, a line matching
  `^\++ fail 49 .--dispatch declares a generated index together with its generator` after it, a
  `read_bounded` line after that, and no line matching `^\++ kill ` after the refusal. The output
  carries the pairing refusal's text and not the spec-token refusal. One declaration names both
  halves, so the refusal needs no sibling row, and the order gate and condition 1 pass as they do
  for A2: ARCH-tRun-4 is dispatched, and neither path is one it declared. Neither file exists, so
  `resolve_generator` keys the declared spelling alone. The group then deletes the
  `GENERATED_INDEXES` line, which no arm in region 3 sets before it. The refused dispatch writes no row.

Ceiling, a declared bound rather than a measurement: the group adds three driver processes and
twelve in-process calls to shard 3, at most 120 s on node a (PINNED 2026-11-14). The close's shard-3 run measures it.

### Inventory

| Identifier | Kind | Lexicon |
|---|---|---|
| `init_spec_token_check` | function | `--suggest ... --as sh.function`: OK, leads with `init` |
| `remove_spec_token_check` | function | OK, leads with `remove`. The prototype's `drop_` answered "use `remove_`" from the shipped canon |
| `ST_STATE`, `ST_PY`, `ST_KEY`, `ST_REC`, `ST_HANDLE` | globals | no shell-variable cell: `.lexicon.conf` declares `sh.function` alone |
| `_order_verb` | global left by `order_verb_of` | no cell; named as `readme_of` leaves `_readme` and `runmd_of` leaves `_runmd` |

None of these names occurs in the driver, its library or the suite at base.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/map/generated/symbols.json`

### Rollout

Live, with no switch, the owner's F1 pick. The build README requires the owner's explicit
ask before landing. The live dDeclaredLoop run merges these lines with main when it next does; the
analysis record's `dm` clone took the same hunks onto that merge with no conflict in the driver.

### Alternatives rejected

- **The prototype's start half as written.** It let `resolve_python`'s diagnosis, and its uv
  prompt on a terminal, out ahead of the reader's notes and onto refusals that never printed it. It
  also kept `ST_STATE` across calls and carried a redundant directory global.
- **A start that records nothing on a resolver failure, leaving the read half to decide as before.**
  The skip path would then derive the key twice, about 8 s of `git status` (PINNED 2026-11-14), on every re-dispatch.
- **A shared discard helper extracted from `read_preflight_probes`.** What the two share is one
  `read_bounded` call on a handle, which both already reuse. The rest, putting `RB_` values back,
  has no reader after `--dispatch` returns, and extracting it moves `--preflight`'s code and owes
  that verb's arms in a build whose README allows only the dispatch arms while the run is live.
- **A `RETURN` trap in place of the two calls.** It is a global trap in bash unless function
  tracing is set, so it fires on returns this unit does not mean.
- **A recorded verdict of closed keys, or a narrower checker.** Rejected by the analysis record,
  section 3: the first loosens condition 1 on a wrong answer, the second drops a refusal.

### What the design does not check

- A spec holding a NUL byte. On node a, GNU grep 3.0 prints its binary-file notice on stdout, so
  the old reader read that notice and found no order; the new reader reads the header. GNU grep 3.5
  and later print the notice on stderr, with the same empty answer. No tracked spec holds one.
- A header line holding an invalid UTF-8 byte under a UTF-8 locale. GNU grep calls the line binary
  and the old reader read nothing; the new reader reads it. Planted on node a under `C.UTF-8`, the
  tail ` · order 7 \xff` read empty before and `MALFORMED · order 7` after. The analysis record's
  section 6 does not list this. In both cases the new reader reads more, so the gate refuses or
  orders where it skipped, never the other way.
- A refusal from the generator pairing or condition 1 waits for the checker and discards its
  answer: those refusals take the longer of the reader and the checker.
- A launcher that becomes runnable between the start and the read is refused as absent, on the
  start's verdict, and its diagnosis does not print.
- An abort between the start and the read that is not a `return`, such as a `set -u` failure or a
  signal, leaves the checker running. `init_bounded` recorded it in the process ledger, where the
  reap finds it.
- A caller that starts for one slug and reads for another. The verb passes one `$slug` to both.
- A write between the start and the read, as stated above. A4 grades the returns in the window and
  nothing else.

## 5. Production-readiness checklist

- security — no new input, write path or surface; the checker's argv and launcher are unchanged;
  the started child is never killed, and its record goes to the existing process ledger.
- perf / scale — the order gate's per-unit process pipeline goes, and the checker overlaps the
  reader. The analysis record measured the prototype at 625.6 s before and 203.2 s after, 728 and
  233 other processes, PINNED 2026-11-14; AC11 measures this build's code.
- error / empty / loading states — every announced skip, cache-off line and refusal prints from
  the read half at its old position; a capture that cannot be made runs synchronously as before.
- observability — no line changes. The trace shows the start before the reader.
- risks — the window's no-write invariant (§4); concurrent load from the two children on a loaded
  node; the merge with the live run's branch.
- testing — AC1 to AC12 and the arms on the `New arm:` lines in §7.
- migration — N/A: no data or record shape moves; the sidecar key file is read and written as now.
- user docs — the verbs guide (S8); no page under `help/` describes `--dispatch`.

## 6. Acceptance criteria

- **AC1** — When the probe below evals `ORDER_OK_RE`, `ORDER_LOOSE_RE` and `order_verb_of` out of
  `tools/unattended/unattended.sh` and calls the function with `PATH` emptied over files holding the
  ten §4 plants, each row prints the table's answer, and the function's slice with comment lines
  removed carries no `$(` and no backtick.
  ```
  ( eval "$(sed -n '/^ORDER_OK_RE=/p;/^ORDER_LOOSE_RE=/p;/^order_verb_of() {/,/^}$/p' tools/unattended/unattended.sh)"
    PATH=/nonexistent
    for f in "$@"; do order_verb_of "$f" >/dev/null; printf '%s\t[%s]\n' "$f" "${_order_verb-UNSET}"; done )
  ```
  Red when: the reader still runs `grep`, so every row reads empty, or it leaves no `_order_verb`.
  figure: the ten answers are PINNED, measured on node a on 2026-11-14 from the base reader.
- **AC2** — When `grep -c 'order_verb_of "$_[do]_spec" >/dev/null'` runs over
  `tools/unattended/unattended.sh` it prints 2, and the same file holds no line where a command
  substitution opens on `order_verb_of`.
  Red when: either call site still reads the function through a substitution.
- **AC3** — When `bash -x tools/unattended/unattended.sh --dispatch tRun --pass ARCH-tRun-5` runs
  with `--writes` naming its own path, the stub checker that exits 1 declared, and its stderr to a
  file, the first `init_bounded` trace line naming the stub precedes the first `read_open_passes`
  line, a `read_bounded` line follows that, and stdout carries the red refusal
  `the declared spec-token checker reds over the live tree`.
  Red when: the start sits below the reader, or the read half runs the checker synchronously.
  fixture: the driver suite's tRun build as the aSwiftRefusal-1 arms leave it, ARCH-tRun-4
  dispatched; outside the suite the tree holds none, and a pass builds it in a `%TEMP%` repository
  the way the suite's `mkconf` and `readme` do.
  permission: the suite arm that re-observes this is the main loop's to run at the close.
- **AC4** — When the same traced dispatch names ARCH-tRun-4's path instead, stdout carries
  `two passes claiming one file are not disjoint` and not the spec-token refusal, and the trace
  holds the stub's `init_bounded` line, the condition-1 `fail 49` line, a `read_bounded` line after
  that, and no `kill` line after it.
  Red when: the `remove_spec_token_check` call is missing at condition 1, or the checker is killed.
  fixture: as AC3.
  permission: as AC3.
- **AC5** — When the awk below runs over `tools/unattended/unattended.sh`, it prints a count of at
  least 2 and no `MISSING` line.
  ```
  awk '/^verb_dispatch\(\)/{v=1} v && /init_spec_token_check "\$slug"/{w=1; next} v && /run_spec_token_check "\$slug"/{w=0}
       w && !/^[[:space:]]*#/ && /return 1/{n++; if ($0 !~ /remove_spec_token_check/) print "MISSING " NR}
       END{print n+0}' tools/unattended/unattended.sh
  ```
  Red when: a refusal in the window returns without the remove, or no start call bounds the window,
  which prints 0.
- **AC6** — When a subshell that sourced the driver and ran `load_driver_conf` defines
  `resolve_python` to print `RESOLVER-DIAG` on stderr and return 1, `init_spec_token_check tRun`
  prints nothing on either stream and leaves `ST_STATE` at `nopython`, and a following
  `run_spec_token_check tRun` prints `RESOLVER-DIAG` before `the inline resolver found no usable python`.
  Red when: the start lets the resolver's stderr through, as the prototype did, or the read half
  refuses without re-running the resolver for its diagnosis.
  fixture: as AC3, the stub declared.
- **AC7** — When the probe below prints each check-49 branch's ordinal and signature before and
  after the change, the two listings are equal, and `git diff --exit-code` over
  `tools/unattended/unarmed-branches.txt` prints nothing.
  ```
  python -c "import importlib.util as u;s=u.spec_from_file_location('a','tools/memory-tree/check-arms.py');m=u.module_from_spec(s);s.loader.exec_module(m);[print(b['ord'],b['sig'][:60]) for b in m.branches('.','tools/unattended/unattended.sh') if b['num']==49]"
  ```
  Red when: a `fail 49` site is added to, or reordered in, the halves.
  figure: the ordinals are DERIVED by the probe from the source at observation time.
- **AC8** — When `grep -c "It runs last because it costs a tree-wide scan"` runs over
  `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`, each prints 0,
  `grep -c "started just before the open-pass reader"` prints 1 for each, and the comparison below
  prints nothing.
  ```
  diff <(tail -n +2 tools/unattended/VERBS.template.md) <(tail -n +2 memory/guides/UNATTENDED-VERBS.md)
  ```
  Red when: either copy keeps the old sentence, or the copies differ.
- **AC9** — When `grep -c` runs over `tools/unattended/unattended.sh` for
  `Both call sites read this through` and for `IT RUNS LAST AMONG THE LOCAL REFUSALS`, each prints 0, and for
  `remove_spec_token_check` it prints at least 4: the definition, two calls and the window comment.
  Red when: a comment still states the old order.
- **AC10** — When `python tools/lexicon/lexicon.py --suggest init_spec_token_check --as sh.function`
  and the same for `remove_spec_token_check` run, each prints a line opening `OK`, and
  `memory/map/generated/symbols.json` carries one entry whose id is each of the two names.
  Red when: a name the lexicon refuses lands, or the index is not regenerated.
- **AC11** — When the command below runs under `bash -x` with `GIT_TRACE` on the frozen clone,
  before and after the change, stdout, the stderr lines that are not trace lines, and
  the parked row with its UTC stamp cut compare equal by `diff`. The after-trace holds no line
  matching `^\+\+ order_verb_of ` and its checker `init_bounded` line precedes `read_open_passes`.
  The record gives both wall times and both git and other process counts.
  ```
  bash tools/unattended/unattended.sh --dispatch dDeclaredLoop --pass TOOL-dDeclaredLoop-9 --writes tools/loop/loop_lib.py
  ```
  Red when: any line or the row differs, or the after-trace still reads the order verb through a
  substitution.
  cost: about 10 minutes per run on node a under the live run's load; the before-run measured
  625.6 s on 2026-11-14.
  fixture: the analysis record's `dm` clone, the live run's tip `bc42f13ca` merged with `846d51d39`,
  with an unreachable push URL; rebuilt as that record's section 1 says if it is gone.
  permission: the main loop's, at the close; it fetches the real remote's claim and pushes nothing.
  figure: the before figures are PINNED in the analysis record; the after figures are DERIVED here.
- **AC12** — When the same traced dispatch runs with the conf declaring
  `GENERATED_INDEXES="${PFX}bd-idx.md:${PFX}bd-gen"` and `--writes ${PFX}bd-idx.md --writes ${PFX}bd-gen`
  in place of its own path, stdout carries
  `--dispatch declares a generated index together with its generator` and not the spec-token
  refusal, and the trace holds the stub's `init_bounded` line, the generator-pairing `fail 49` line,
  a `read_bounded` line after that, and no `kill` line after it.
  Red when: the `remove_spec_token_check` call is missing at the generator-pairing refusal, or the
  checker is killed, or the start sits below that refusal.
  fixture: as AC3, plus the `GENERATED_INDEXES` pair, where `PFX` is the suite's install prefix.
  permission: as AC3.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `scratch-guard self-test` · `tier2-review self-test` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `unattended skill wiring` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `pass-order history` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · the driver at base 846d51d39, whose reader forks grep under a substitution, so the emptied-PATH table reads UNSET and the trace carries the doubled-plus order_verb_of line · none
New arm: tools/unattended/unattended.test.sh · covers AC3 · base, where run_bounded starts the checker after the open-pass reader returns · none
New arm: tools/unattended/unattended.test.sh · covers AC4 AC5 · base, which starts no checker on a condition-1 refusal and has no start call to bound the window · none
New arm: tools/unattended/unattended.test.sh · covers AC6 · base, which has no start half, and the prototype's start, which prints the resolver's diagnosis · none
New arm: tools/unattended/unattended.test.sh · covers AC12 · the driver at base 846d51d39, which starts no checker before the generator-pairing refusal, so the trace holds no stub init_bounded line and no read_bounded after the refusal; and 4fed38fe1 with that refusal's remove_spec_token_check call deleted, which leaves no read_bounded after it · none

The close's driver-suite run re-observes, unchanged, every existing arm over `--dispatch`: in region
3 the dBriefedPass-2 and -3 refusal arms with the malformed `order 2x` case, the aDeferredBar F3
and aSmoothedDispatch-4 and -8 spec-token group with its in-process cache steps, which now reach the
start half through the read half's own call, and the aSwiftRefusal-1, -2 and -4 arms; in region 4
the dUnstalledConvoy-9 write-set arms; and the dispatch arms of regions 1, 2, 7 and 8. The launcher
arm in region 2 still finds `run_bounded "$_stpy" "$SPEC_TOKENS_CLI"`. Shard 3 holds the new group.
The suite's floor is a minimum, and these arms only add to it.

## 8. Open questions

- **F1 — Does this land live, or dark behind a default-off switch?** The charter lands risky
  behaviour dark. The change runs a second child beside the reader for every admitted dispatch.
  (a) Live, no switch: every line is unchanged, AC11 diffs a whole dispatch, and a switch would
  keep two paths where the dark one is exercised by no run. (b) A conf key, default off: the run
  stays on today's path until an owner turns it on, at the cost of a key-table row and a second
  path the arms must cover. Recommendation: (a). RESOLVED (owner, 2026-11-14): (a) Live, no switch.
- **F2 — Does the generator-pairing refusal owe a behavioural arm of its own?** (a) No: AC5's class
  predicate grades every `return 1` in the window, that refusal's included, and the brief names
  condition 1's arm alone. (b) Yes: a traced arm with a `GENERATED_INDEXES` pair in the fixture,
  one more driver process in shard 3. Recommendation: (a). RESOLVED (owner, 2026-11-14): (b) Add its
  own arm, which is A6 and AC12.

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.
- rev-2 · 2026-11-14 · F1 and F2 RESOLVED by the owner (2026-11-14-prompt-TOOL-aBriskDeclaration-1-forks-brief): F1 (a) live, which the code at 4fed38fe1 and fc4c62bfa already follows; F2 (b), so arm A6, AC12 and its `New arm:` line are added. No other code moves.

## 10. Reuse audit

The seam this unit extends is `init_bounded` and `read_bounded` in `tools/unattended/unattended.sh`,
the two halves TOOL-aBriskPreflight-4 S1 split out of `run_bounded` for exactly this use, which
`init_preflight_probes` and `read_preflight_probes` already make. The checker block stays in
`run_spec_token_check`, which the read half keeps, and the order reader stays in `order_verb_of`.
The probe `tools/codebase-map/reuse_lookup.py`, given the query "start a bounded child early and
read its answer later, overlap two slow readers, discard an unread probe", ranked `read_text`, `read`,
`probe` and `read_bytes` by name stem, and the same probe over the names `init_bounded`,
`read_bounded`, `read_preflight_probes` and `order_verb_of` ranked `read_text`, `read`, `run` and
`check`; none splits a bounded child's start from its read, so the source read is the evidence for
the seam. `gotchas.py --for-paths` over the driver and its suite selected
`guard-above-a-fold-makes-its-fallback-dead`, which the read half's own start call answers, since the
suite's in-process cache steps exercise it; `decision-re-derived-by-a-second-process`, answered by
refusing on the start's verdict and re-running the resolver only for its print;
`test-oracle-read-from-a-historical-sha`, answered by literal plants in A1; and
`fixture-passes-by-finding-nothing`, answered by a positive line beside every absence in A1 to A4.

Recall terms used: `python tools/memory-recall/query.py "why does dispatch run the spec-token
checker after the open-pass reader, and how does preflight overlap its probes" --terms "dispatch
spec-token SPEC_TOKENS_CLI init_bounded read_bounded read_preflight_probes read_open_passes
order_verb_of order gate aBriskPreflight overlap"`
