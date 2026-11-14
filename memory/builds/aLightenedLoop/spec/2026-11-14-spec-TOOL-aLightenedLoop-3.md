# TOOL-aLightenedLoop-3 — `--dispatch` runs before the builder spawns, and its spec-token cache keys on what the checker read

**Status:** CLOSED · rev-2 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 3 · ratified 2026-11-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md](../build/2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md) | research | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 |
| [2026-11-14-build-TOOL-aLightenedLoop-3-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aLightenedLoop-3-1-acceptance-ledger.md) | journal | — |
| [2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md) | research | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 |
| [2026-11-14-prompt-TOOL-aLightenedLoop-1-fork-answers.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-fork-answers.md) | research | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-5 |
| [2026-11-14-prompt-TOOL-aLightenedLoop-3-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-3-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aLightenedLoop-3-fork-fold.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-3-fork-fold.md) | research | — |
| [2026-11-14-review-TOOL-aLightenedLoop-1-5-implementation-diff-round1.md](../reviews/2026-11-14-review-TOOL-aLightenedLoop-1-5-implementation-diff-round1.md) | diff-review | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 |

<!-- /gen:spec-records -->

## 1. Goal

A dispatch refusal today costs a spawned builder and its orientation, because the builder runs
`--dispatch` itself. The spec-token cache that `--dispatch` keeps also misses after every commit,
because its key holds HEAD and the whole-tree fingerprint. This unit moves the first `--dispatch`
to the main loop, before the spawn. It also keys the cache on the files and git answers the checker
actually read, so a commit or an edit that moves none of them reuses the last admitted check. No
check's verdict, refusal text or rendered byte moves. Scoping the check to the dispatching build is
out of scope, by the owner's answer to F1, because the cross-build joins are shown below to move.

## 2. Scope (IN)

- **S1** — The build harness's hand-out carries `dispatch.declare` in unattended mode only: one
  sentence telling the main loop to run `--dispatch` for a unit, from that unit spec's Files touched
  estimate, before the unit's Workflow call, and that a refusal means that call is not made.
  Observed by AC1.
- **S2** — The unit harness's unattended driver steps tell the builder that the main loop already
  declared its write set, and that a path outside it is declared before it is written, naming only
  the added paths. The attended text is unchanged. Observed by AC2.
- **S3** — The open-event read filter that `add_source_read` in `tools/policy/check_policy.py`
  carries is extracted into one lib block, `read_open_py`, whose canonical copy sits in the gov lib
  dir. The policy kit and the spec-token checker each carry it inline, byte-identical, under a new
  parity row. Observed by AC3 and AC4.
- **S4** — The spec-token checker records its inputs when `SPEC_TOKENS_INPUTS` names a file: every
  file it opens to read, every directory it lists, and every subprocess it runs. Its stdout and exit
  status are unchanged. Observed by AC5 and AC6.
- **S5** — The checker's `--input-key <record>` prints one digest over the current state of every
  input a record names, or prints nothing and exits 1 when the record cannot be replayed.
  Observed by AC7.
- **S6** — The driver keys the spec-token cache on the slug, the checker, the launcher and the S5
  digest. HEAD and the fingerprint leave the key. A key is recorded only when the checker admitted,
  wrote a record, and neither the tree nor HEAD moved while it ran. The verbs guide states the new
  key in both copies. Observed by AC8, AC9, AC10 and AC11.

## 3. Non-goals (OUT)

- No change to what the checker grades, its refusal lines or its summary. The tracer only records.
- No change to `check_spec_token_hits`, the verdict TOOL-aSmoothedDispatch-4 S1 built, nor to any
  refusal text of `--dispatch`. The skip line and the cache-off line keep their bytes.
- No change to `--dispatch`'s refusals, their order, or its write-set rows. The main loop calls the
  same verb with the same flags the builder called.
- No change to the attended route. Attended mode has no run-state file, so `--dispatch` refuses
  there, and the attended child text stays as it is.
- No new `nextAction` sentence in the build harness. Those sentences are pinned by its suite; the
  new instruction travels as a field, as `resolvePathsWith` already does.
- No edit to the unattended Skill. It sits at its ceiling of 10580 bytes <!-- PINNED 2026-11-14 -->
  (`tools/template-size-limits.txt:188`), and the field is self-describing.
- No scoping of the check to one build. The scoping half of the brief's item 3, rev-1's S7, is out
  of scope by F1's resolution, and the section "Why the check is not scoped" in §4 records why. <!-- PINNED 2026-11-14 -->
- No incremental, per-spec checker. It is filed as a follow-up ask at the build's wrap-up.
- No kit version bump by hand. The lander's mint moves it.
- None of units 1, 2, 4 or 5's mechanisms.

### Edges

none

## 4. Design

### What the code does today, read at `846d51d3`

- The builder runs the first `--dispatch`. The unattended branch of `DRIVER_STEPS`
  (`tools/workflows/unattended-unit.js@71852dc0:258`) opens with "Declare the write set with" the driver's
  `--dispatch` at `tools/workflows/unattended-unit.js@71852dc0:264`. A Workflow script has no shell, so the
  child cannot run it for the builder.
- The build harness's hand-out object `dispatch` (`tools/workflows/unattended-build.js@996b9ed7:3018`) holds
  `scriptPath`, `args`, `perUnit` and `resolvePathsWith` (`tools/workflows/unattended-build.js@996b9ed7:3039`).
  The last is already a command the main loop runs before a unit's call, so a field that instructs
  the main loop is an existing shape.
- The key is `derive_spec_token_key` (`tools/unattended/unattended.sh@95b8f840:14430`): the slug, the
  checker, the launcher, `GIT rev-parse HEAD` and the run-gates working-tree fingerprint. The
  fingerprint digests the HEAD tree, the porcelain status and every dirty or untracked blob
  (`tools/run-gates/gate-fingerprint.sh@862c00cc:1`). So any commit, any tracked edit and any untracked file
  moves the key, whether or not the checker reads it.
- `run_spec_token_check` (`tools/unattended/unattended.sh@95b8f840:14458`) derives the key before the
  checker runs and records it after an admit. Its skip line and its cache-off line are the two
  announcements the suite pins (`tools/unattended/unattended.test.sh@0d9cd163:7839`,
  `tools/unattended/unattended.test.sh@0d9cd163:7876`).
- The suite's arm asserts the old over-sensitivity. Step b edits the build's README and expects a
  re-run (`tools/unattended/unattended.test.sh@0d9cd163:7842`), and step c makes an empty commit and expects
  a re-run (`tools/unattended/unattended.test.sh@0d9cd163:7850`). This unit inverts both on purpose.
- The checker's git calls go through `subprocess.run`: `run` (`tools/check-spec-tokens.py@42905ba5:577`) for
  `git ls-files`, the cutoff pickaxe (`tools/check-spec-tokens.py@42905ba5:762`), the packet instrument per
  live chain run (`tools/check-spec-tokens.py@42905ba5:1559`), the spec revision log
  (`tools/memory-tree/design_lib.py@82906599:687`), the one `git cat-file --batch` that takes stdin
  (`tools/memory-tree/tree_lib.py@54a65cd4:377`, through `tools/memory-tree/tree_lib.py@54a65cd4:327`), and the policy
  read (`tools/memory-tree/tree_lib.py@54a65cd4:74`).
- `add_source_read` (`tools/policy/check_policy.py@4b35ad98:4182`) is an audit hook that keeps an `open`
  event only when it reads, maps a bytecode-cache read to its source, and flags a cache name it
  cannot map. It is installed by `sys.addaudithook` at `tools/policy/check_policy.py@4b35ad98:5020`. The
  recorder below needs that same filter, so this unit is its second instance.

### S1 — `dispatch.declare`

In unattended mode the hand-out's `dispatch` object gains one key, `declare`, a sentence built from
`DRIVER` and the slug. In attended mode the object carries no such key. The sentence, with
`<driver>` and `<slug>` substituted:

```
Before each unit's Workflow call, run `<driver> --dispatch <slug> --pass <unitId> --writes <path>`
with one --writes per backticked path under that unit spec's `### Files touched (estimate)`, in the
foreground with the tool's timeout at 600000 ms. A refusal is binding: make no Workflow call for
that unit, and act on what the refusal names.
```

The edit is made in `tools/workflows/unattended-build.js` and its template twin alike. The two files
differ today only in the install-prefix placeholders, 26 `diff` lines, and they still do after.

### S2 — the child's driver steps

The unattended branch of `DRIVER_STEPS` replaces its first sentence and keeps the rest. Its new
opening, with the driver, slug and unit substituted as today:

```
The main loop declared this unit's write set with `<driver> --dispatch <slug> --pass <unitId>
--writes <path>` before it spawned you, from the spec's Files touched estimate. Before you write a
path outside that set, declare it with the same command, naming only the paths you add.
```

The sentences "A REFUSAL FROM IT IS BINDING", "ITS SILENCE IS NOT A CLEARANCE" and the `--brief`
order follow unchanged. The verbs guide already states that a re-declaration naming only added paths
widens the pass (`tools/unattended/VERBS.template.md:784`), so no rule is new.

### S3 — the shared read filter, `read_open_py`

One function, `derive_read_path(path, mode, flags)`, moves out of `add_source_read`. It returns
`(path, refused)` for a read and None otherwise:

1. A descriptor (an int path) is None.
2. With mode None, any of `O_WRONLY`, `O_RDWR` or `O_CREAT` in the flags is None. With a mode that
   is not a string, or holds any of `w`, `a`, `x` or `+`, it is None.
3. A `.pyc` under a `__pycache__` directory maps to its source through
   `importlib.util.source_from_cache`. A name that function refuses is kept as spelled, with
   `refused` true.
4. The path is returned through `os.path.realpath`.

The canonical copy is a new file in the gov lib dir, `read_open.py`, holding the block between
`# >>> read_open_py -- canonical copy: read_open.py in the gov lib dir (byte-identical; gated)` and
`# <<< read_open_py`. `tools/policy/check_policy.py` and `tools/check-spec-tokens.py` each carry the
block inline, and `add_source_read` keeps only its root, temp and git-dir filtering around the call.
The parity table (`tools/lib/resolve-python.test.sh@4b2fb1fb:351`) gains the row
`read_open_py|$ROOT/$KIT_REL/read_open.py|$KIT_REL/read_open`.

Before writing the block, the builder greps the tree for `addaudithook` outside the policy kit. If
unit 1 has landed a tracer of its own by then, this unit extracts that tracer into the lib block too,
and both callers consume it. If not, the tracer below stays in the checker alone, because it has one
caller.

### S4 — the input record

When `SPEC_TOKENS_INPUTS` is set and not empty, the checker calls `arm_input_trace` at module level,
right after its standard-library imports (`tools/check-spec-tokens.py@42905ba5:272`) and before the kit
resolves. Arming inside `main` would be too late: the kit's modules load at import, and a change to
one of them would then move no key. An environment variable, not a flag, carries the request,
because a declared `SPEC_TOKENS_CLI` that does not know it simply ignores it and writes no record. A
flag could make such a checker exit non-zero and move the dispatch verdict.

`arm_input_trace(path)` first records the checker's own file as a read, since the interpreter opened
it before any hook could exist. It then installs three things:

- An audit hook, `add_input_event`. An `open` event that `derive_read_path` keeps is recorded as a
  read, unless it sits under `sys.prefix`, `sys.base_prefix` or `sys.exec_prefix`, which the launcher
  in the key stands for. An `os.listdir` or `os.scandir` event is recorded as a listing. A
  `subprocess.Popen` event fired outside the wrapper below is recorded as unreplayable.
- A wrapper, `run_traced`, set as `subprocess.run` for the life of the process. It records the argv,
  the working directory, the call's input bytes, and the environment delta from `os.environ`: the
  names the call drops, and the names it adds or changes with their values. The parent's own values
  are never written. It then calls the real `subprocess.run` and returns its result untouched.
- An exit handler, `write_input_record`, which writes the record, one compact JSON object per line,
  sorted and de-duplicated.

| `kind` | other keys | replayed by S5 as |
|---|---|---|
| `read` | `path` | the SHA-1 of the file's bytes, or `absent` |
| `list` | `path` | the sorted names, or `absent` |
| `run` | `argv`, `cwd`, `drop`, `set`, `input` (base64) | the exit status and the SHA-1 of stdout, run with the recorded input and env delta |
| `popen` | `argv` | nothing: the record is unreplayable |

The record goes to the path the variable names, which the driver places in the sidecar root, so it
is never in the working tree and never moves the fingerprint. The checker's own stdout and exit
status are byte-identical with and without the variable.

### S5 — `--input-key <record>`

`--input-key` is branched at the top of `main`, ahead of the spec walk, as `--legs-for` is. It calls
`derive_input_digest(record)`. That hashes the record's own bytes, then each line's replay from the
table above, in record order, into one SHA-1. It prints the 40-hex digest and exits 0. It prints
nothing and exits 1 when the record does not parse or holds a `popen` line. The replay of a `run`
line rebuilds the env from the current `os.environ` with the recorded delta, and feeds the recorded
input. A recorded `git cat-file --batch` therefore replays exactly, with no special case.

Because the digest folds the record's bytes, a key is self-certifying. A key recorded for one
record can only match a later digest over the same record lines and the same replayed state.

### S6 — the driver

`derive_spec_token_key <slug> <launcher> <record>` keeps its name and its contract, a 40-hex key or
nothing with status 1. Its body becomes `GIT hash-object --stdin` over four lines: the slug,
`$SPEC_TOKENS_CLI`, the launcher, and the output of `"$launcher" "$SPEC_TOKENS_CLI" --input-key
"$record"`. A new helper, `read_tree_state`, prints the fingerprint line and `GIT rev-parse HEAD`,
or nothing when either is missing. The fingerprint is resolved exactly as today.

The sidecar root holds two files per slug: `spec-tokens.<slug>.key`, as today, and
`spec-tokens.<slug>.inputs`, the record. `run_spec_token_check` becomes:

1. Resolve the launcher as today.
2. If both files exist, derive the key over the record. If it equals the stored key, print the
   unchanged skip line and return 0.
3. Read the tree state. If it is empty, print the unchanged cache-off line.
4. Remove the record file. Run the checker with `SPEC_TOKENS_INPUTS` set to the record path for that
   one call.
5. Take the verdict from `check_spec_token_hits` exactly as today, refusal and admit note included.
6. On an admit, record only when three things hold: the state from step 3 was not empty, the state
   read now equals it, and the record file exists. Then derive the key over the new record and write
   it with one `printf`. Otherwise print one line,
   `unattended: dispatch — spec-token cache not recorded: <reason>, so the next dispatch runs the checker`,
   whose reason is `the tree or HEAD moved while the checker ran`, `the checker wrote no input
   record`, or `the input record cannot be replayed`. The fingerprint-missing case already printed
   the cache-off line and prints nothing more.

HEAD still guards the window in which the checker runs. It is no longer part of the key, so it no
longer invalidates a record between runs.

### When the cache hits, derived from what the checker reads

- A re-dispatch after any refusal, when nothing the checker read has moved. This holds today too.
- A records-only commit, or an edit to a file no live spec cites and the checker never opens. Today
  both miss.
- A second unit of the same build in a parallel group. The run-state file is read only by the packet
  join, for a chain run that has a packet (`tools/check-spec-tokens.py@42905ba5:1551`). So a non-chain run's
  own dispatch row no longer moves the key. That reverses TOOL-aSmoothedDispatch-4's non-goal, which
  had to include the run-state file because the fingerprint could not tell who read it.
- Not the next unit of a sequential run. Each pass commit sets its unit's spec CLOSED, and the
  checker reads every spec to sort live from terminal. That flip can change the verdict, because a
  waiver row whose hit came only from that spec turns stale. So a sound key must miss there. The
  incremental per-spec checker, the wrap-up's follow-up ask, is where that cost would be cut.

### What the key does not check

- A path probed only by `is_file` or `exists` and never opened, such as `run_md.is_file()` at
  `tools/check-spec-tokens.py@42905ba5:1551`. A tracked file appearing there moves the replayed
  `git ls-files` answer. An untracked one does not.
- The environment beyond the recorded delta, and a Python package upgraded in place under one
  launcher path. Both were outside TOOL-aSmoothedDispatch-4's key as well.
- A subprocess whose answer is not a function of the tree and history. None is in the population
  read at `846d51d3`; the packet instrument and the policy read are both read-only checks.

### Why the check is not scoped

The cheap scoped form is the checker's `--spec` mode over the dispatching build's live specs. That
mode differs from the whole-tree run in three places, read at `846d51d3`:

- It skips the carries join and the packet join (`tools/check-spec-tokens.py@42905ba5:1954`,
  `tools/check-spec-tokens.py@42905ba5:1976`).
- It reports no stale waiver row (`tools/check-spec-tokens.py@42905ba5:2000`).
- It grades every named spec whatever its status, where the whole tree grades live specs only.

The dispatch verdict refuses on any stale row and on any hit whose file is not under a build folder,
which includes a carries finding that names a chain build bare. Both come only from the joins the
scoped run skips. So a scoped run admits trees the whole-tree run refuses, and the verdict moves.
The brief allowed the scope only where the cross-build joins are shown not to move, and they do.
The owner resolved F1 to option (a), so this unit builds no scoping.

### The pass probe, `$SCRATCH/l3.sh`

`$SCRATCH` is the run's scratch directory. The probe runs from the root of the worktree under build.
It builds a fixture repository at `$TEMP/l3`, a short path because a clone under the scratch
directory's long path fails on Windows. The stub checker loads the real checker module for its
tracer and its `--input-key`, and fakes only the verdict.

```bash
set -u
G=$(pwd); R="$TEMP/l3"; rm -rf "$R"; mkdir -p "$R/tools/run-gates"; cd "$R" || exit 2
git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
cp "$G/.unattended.conf" "$G/.memory-tree.conf" . && cp "$G/tools/run-gates/gate-fingerprint.sh" tools/run-gates/
cat > stub.py <<EOF
import importlib.util, os, subprocess, sys
if os.environ.get("L3_NOTRACE"):
    os.environ.pop("SPEC_TOKENS_INPUTS", None)
s = importlib.util.spec_from_file_location("cst", r"$G/tools/check-spec-tokens.py")
cst = importlib.util.module_from_spec(s); s.loader.exec_module(cst)
if "--input-key" in sys.argv:
    sys.exit(cst.main(sys.argv[1:]))
open("a.txt").read(); subprocess.run(["git", "ls-files"], capture_output=True)
if os.environ.get("L3_TOUCH"):
    open("a.txt", "a").write("t\n")
open(os.environ["L3_LOG"], "a").write("r\n")
sys.stdout.write(open(os.environ["L3_OUT"]).read()); sys.exit(int(os.environ["L3_RC"]))
EOF
printf 'seed\n' > a.txt; printf 'seed\n' > b.txt; git add -A; git commit -qm seed
. "$G/tools/unattended/unattended.sh" || exit 2
load_driver_conf || exit 2
PY=$(resolve_python) || exit 2
export L3_LOG="$R/.git/l3.log" L3_OUT="$R/.git/l3.out" L3_RC=0
: > "$L3_LOG"; : > "$L3_OUT"; SPEC_TOKENS_CLI=stub.py
runs() { local n; n=$(wc -l < "$L3_LOG"); echo "${n// /}"; }
sk() { grep -c 'spec-token check skipped' <<<"$1"; }
S='spec-tokens: %s unwaived hit(s), %s stale row(s)'
own='spec-tokens: memory/builds/tA/spec/2026-11-10-spec-T-tA-1.md [bar] `t` — w'
far='spec-tokens: memory/builds/tB/spec/2026-11-10-spec-T-tB-1.md [bar] `t` — w'
M="$(resolve_sidecar_dir)/spec-tokens.tA.inputs"
run_spec_token_check tA >/dev/null; o=$(run_spec_token_check tA)
echo "cache unchanged runs $(runs) skipped $(sk "$o")"
"$PY" -c 'import json,os,sys; L=[json.loads(x) for x in open(sys.argv[1])]; n=lambda b: sum(1 for x in L if x["kind"]=="read" and os.path.basename(x["path"])==b); print("manifest read a.txt", n("a.txt"), "run ls-files", sum(1 for x in L if x.get("argv")==["git","ls-files"]), "log", n("l3.log"))' "$M"
printf 'e\n' >> b.txt; o=$(run_spec_token_check tA); echo "cache unread runs $(runs) skipped $(sk "$o")"
git commit -qam two; o=$(run_spec_token_check tA); echo "cache commit runs $(runs) skipped $(sk "$o")"
printf 'e\n' >> a.txt; run_spec_token_check tA >/dev/null; echo "cache edited runs $(runs)"
: > c.txt; o=$(run_spec_token_check tA); echo "cache untracked runs $(runs) skipped $(sk "$o")"
run_spec_token_check tB >/dev/null; echo "cache slug runs $(runs)"
printf '%s\n' "$own" "$(printf "$S" 1 0)" > "$L3_OUT"; L3_RC=1
run_spec_token_check tA >/dev/null; run_spec_token_check tA >/dev/null; echo "cache refused runs $(runs)"
printf '%s\n' "$far" "$(printf "$S" 1 0)" > "$L3_OUT"
o=$(run_spec_token_check tA); p=$(run_spec_token_check tA)
echo "cache foreign runs $(runs) noted $(grep -c "other builds' specs" <<<"$o") skipped $(sk "$p")"
printf 'm\n' >> a.txt
o=$(L3_TOUCH=1 run_spec_token_check tA); run_spec_token_check tA >/dev/null; p=$(run_spec_token_check tA)
echo "cache moved runs $(runs) said $(grep -c 'the tree or HEAD moved' <<<"$o") skipped $(sk "$p")"
printf 'n\n' >> a.txt; o=$(L3_NOTRACE=1 run_spec_token_check tA; L3_NOTRACE=1 run_spec_token_check tA)
echo "cache untraced runs $(runs) said $(grep -c 'wrote no input record' <<<"$o")"
rm tools/run-gates/gate-fingerprint.sh
o=$(run_spec_token_check tA; run_spec_token_check tA)
echo "cache off runs $(runs) said $(grep -c 'spec-token cache off' <<<"$o")"
printf '{"kind":"popen","argv":["x"]}\n' > "$R/.git/l3.bad"
k=$("$PY" stub.py --input-key "$R/.git/l3.bad"); echo "key popen $? ${#k}"
```

The stub imports the real checker, so the module-level arming records its reads exactly as it would
for the checker itself; `L3_NOTRACE` removes the variable before that import. The edit to `a.txt`
before the moved step makes the step-8 record miss, so the stub runs. `L3_TOUCH` then appends to
`a.txt` after the stub has read it, so the fingerprint moves inside the run.
The log is opened to append, so the filter must leave it out of the record. `L3_OUT` sits under
the fixture's git dir and is read, so a changed stub verdict moves the key as a real one would.

### Inventory

| identifier | kind | lexicon verb |
|---|---|---|
| `declare` | key of the hand-out's `dispatch` object | — |
| `derive_read_path` | Python function, block `read_open_py` | derive |
| `read_open.py` | new canonical file in the gov lib dir | — |
| `arm_input_trace` | Python function in the checker | arm |
| `add_input_event` | Python audit hook in the checker | add |
| `run_traced` | Python wrapper in the checker | run |
| `write_input_record` | Python exit handler in the checker | write |
| `derive_input_digest` | Python function in the checker | derive |
| `--input-key` | checker flag | — |
| `SPEC_TOKENS_INPUTS` | environment variable the checker reads | — |
| `read_tree_state` | sh function in the driver | read |
| `spec-tokens.<slug>.inputs` | sidecar file | — |

`derive_spec_token_key` is re-bodied, not minted. No conf key and no check number is minted, and
the refusal stays check 49.

### Docs

`tools/unattended/VERBS.template.md:245-247` says the cache is keyed on "the slug, the checker, the
launcher, HEAD and the run-gates working-tree fingerprint". It becomes: keyed on the slug, the
checker, the launcher and a digest of every file and git answer its last admitted run read, recorded
under the sidecar root only when the tree and HEAD held still while it ran, and with no fingerprint
it announces that the cache is off and runs the checker. The phrase
`a digest of every file and git answer its last admitted run read` is spelled as written, on one line.
`memory/guides/UNATTENDED-VERBS.md` takes the identical edit, because the two files are
byte-identical at `846d51d3`. No `help/` page names the dispatch cache, grepped at `846d51d3`.

### Rollout

One pass at order 3. Unit 2 edits `tools/unattended/unattended.sh` at order 2 and unit 4 edits
`tools/workflows/unattended-unit.js` at order 4, so every cited line number moves and the builder
finds each site by its text. The driver suite's `FLOOR_ASSERTIONS` moves by the count of new
assertions, which the close confirms from a real run.

### Files touched (estimate)

- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/lib/read_open.py`
- `tools/lib/resolve-python.test.sh`
- `tools/policy/check_policy.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **The child harness runs `--dispatch`.** A Workflow script has no shell. Only an agent, or the
  main loop, can run a command.
- **A new `nextAction` sentence, or a Skill line.** The sentences are pinned whole by the build
  harness's suite, and the Skill is at its ceiling. A field beside `resolvePathsWith` reaches the
  main loop without either.
- **A declared input list written in the checker or the driver.** The cited files of every live
  spec, the chain population and the packet runs are data-dependent. A second list of them is two
  answers to what the checker reads, and the next join added to the checker would leave it short.
  The observed record derives the list from the run itself.
- **Replay recorded output instead of re-running.** A recorded answer says what the state was, not
  whether it still is. Only a replay against today's tree answers the cache's question.
- **Keep HEAD in the key.** The brief asks for it out. HEAD stays only as a guard on the window the
  checker runs in.
- **Pass the request as a `--inputs` flag.** A declared checker that does not know the flag may exit
  non-zero, which `--dispatch` reads as a red. The environment variable is ignored instead.
- **A second copy of the policy kit's read filter.** The charter's reuse rule extracts at the second
  instance.

## 5. Production-readiness checklist

- security — the record and the key live in the per-worktree git dir that only the driver writes. A
  forged record can only skip a check the bar still runs. The record holds argv, paths, the call's
  input and the env names the checker's own code sets or drops, never a parent environment value.
- perf / scale — a lookup costs one Python start, one hash per recorded file, and a replay of each
  recorded call, the spec revision log among them (about 1.1 s on node `a` at `846d51d3`, PINNED).
  A miss adds that and two tree-state reads to today's full checker run.
- error / empty / loading states — no fingerprint prints the cache-off line and records nothing. A
  checker that writes no record, a moved tree and an unreplayable record each print the
  not-recorded line. An unreadable record or key costs a miss, never a refusal.
- observability — the skip line names the key prefix, and every reason not to record is printed.
- risks — the tracer wraps `subprocess.run` process-wide while armed. A call that bypasses it is
  recorded as `popen` and makes the record unreplayable, so the failure is a miss.
- testing — the probe above for the pass, and the four suites' new arms observed RED then GREEN at
  the close.
- migration — none. A key without a record file is never looked up, so the first dispatch after
  install misses once and records.
- user docs — the verbs guide in both copies, per the Docs sub-head.

## 6. Acceptance criteria

Each probe line below comes from one run of `bash "$SCRATCH/l3.sh"`, the Design section's fenced
block, removed after the pass. At the close the suites observe the same behaviour with the real
checker.

- **AC1** — When `grep -c "Before each unit's Workflow call, run" tools/workflows/unattended-build.js`
  runs it prints 1, the same grep over `tools/workflows/unattended-build.template.js` prints 1, and
  `diff tools/workflows/unattended-build.js tools/workflows/unattended-build.template.js` prints 26
  lines. At the close the build harness's suite reads `"declare":` in an unattended return and no
  `"declare"` key in an attended one.
  Red when: the field is written in attended mode too, or only one of the twins carries it.
  figure: 26 is PINNED at `846d51d3`.
- **AC2** — When `grep -c "The main loop declared this unit's write set" tools/workflows/unattended-unit.js`
  runs it prints 1, `grep -c "Declare the write set with" tools/workflows/unattended-unit.js` prints
  0, `grep -c "A REFUSAL FROM IT IS BINDING" tools/workflows/unattended-unit.js` prints 1, and
  `grep -c "This run has NO run-state file" tools/workflows/unattended-unit.js` prints 1.
  Red when: the child still orders the first `--dispatch`, or the attended text moved.
- **AC3** — When `python -I -c` loads the lib block from the gov lib dir and calls `derive_read_path`
  on six events, it reads a source path for a plain read, None for a `w` mode, None for an int
  path, None for `os.O_WRONLY` with mode None, the source file for a `.pyc` under `__pycache__`, and
  `refused` true for a cache name `source_from_cache` refuses.
  Red when: a write or a descriptor is kept, or a cache read is kept as the `.pyc`.
- **AC4** — When the probe extracts the `read_open_py` block from the canonical file,
  `tools/check-spec-tokens.py` and `tools/policy/check_policy.py`, and `cmp` compares the three, it
  prints nothing, and `grep -c "derive_read_path(" tools/policy/check_policy.py` prints at least 1.
  At the close the parity table's new row and the policy fixtures read green.
  Red when: one inline copy drifts by a byte, or `add_source_read` keeps its own filter.
- **AC5** — When `bash "$SCRATCH/l3.sh"` runs, it prints `manifest read a.txt 1 run ls-files 1 log 0`.
  Red when: the filter records the append-mode log, or the wrapper misses the git call.
- **AC6** — When `python tools/check-spec-tokens.py --spec` runs over this spec once with
  `SPEC_TOKENS_INPUTS` naming a scratch file and once without it, `cmp` over the two captured
  stdouts prints nothing and both exit statuses match. At the close the same comparison runs on the
  whole-tree checker over the real tree.
  Red when: the tracer prints, raises or changes the exit status.
  permission: if the builder's role hook refuses the checker, the main loop observes it at the close.
- **AC7** — When `bash "$SCRATCH/l3.sh"` runs, it prints `key popen 1 0`.
  Red when: `--input-key` digests a record holding a call it cannot replay.
- **AC8** — When `bash "$SCRATCH/l3.sh"` runs, it prints `cache unchanged runs 1 skipped 1`,
  `cache unread runs 1 skipped 1`, `cache commit runs 1 skipped 1`, `cache edited runs 2`,
  `cache untracked runs 2 skipped 1` and `cache slug runs 3`.
  Red when: HEAD or the fingerprint is still in the key, so the unread, commit or untracked step
  re-runs, or the key leaves out a read file or the slug.
- **AC9** — When `bash "$SCRATCH/l3.sh"` runs, it prints `cache refused runs 5`,
  `cache foreign runs 6 noted 1 skipped 1`, `cache moved runs 8 said 1 skipped 1`,
  `cache untraced runs 10 said 2` and `cache off runs 12 said 2`.
  Red when: a refusal records, a key is stored over a tree that moved during the run, a missing
  record is not announced, or a missing fingerprint does not turn the cache off.
- **AC10** — When the main loop runs `bash "$SCRATCH/l3-time.sh"` at the close, the base driver and
  this unit's driver each run `run_spec_token_check aLightenedLoop` over this worktree. Their exit
  statuses match, and `cmp` over their outputs, with the skip, cache-off and not-recorded lines
  removed, prints nothing. The script then times each driver cold, repeated, after a one-line edit
  to a tracked file the record does not name, and after a one-line edit to this spec, restoring each
  edit. It records the eight times beside itself in the build's records.
  Red when: the verdict lines differ between the two drivers, or this unit's driver re-runs on the
  unread edit.
  permission: it runs the whole-tree checker, which only the main loop may run.
  cost: about eight cold checker runs, near 62 s each on node `a`. <!-- PINNED 2026-11-14 -->
  fixture: the base driver is a worktree at `846d51d3` under `%TEMP%/l3b`, sourced from this
  worktree's root as the pass probe sources the driver.
  figure: every time is DERIVED at observation.
- **AC11** — When `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` runs it
  prints nothing, `grep -c 'a digest of every file and git answer its last admitted run read' memory/guides/UNATTENDED-VERBS.md`
  prints 1, and `grep -c 'launcher, HEAD and the run-gates working-tree fingerprint' memory/guides/UNATTENDED-VERBS.md`
  prints 0.
  Red when: one copy is edited without its twin, or the old key sentence survives.

## 7. Gates

`unattended kit gate` · `unattended-build self-test` · `spec-tokens self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `review-join self-test` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `verifier fan-out self-test` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `spec tokens (a spec's own names resolve)` · `memory hygiene` · `lexicon naming predicates` · `install-prefix self-test` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: tools/unattended/unattended.test.sh · covers AC8 AC9 · steps b and c of the existing cache arm inverted to skip, plus an input edited during the run and an untraced checker; staged by putting HEAD and the fingerprint back into the key · `FLOOR_ASSERTIONS`, raised by the count of new assertions, which the close confirms
New arm: tools/check-spec-tokens.test.sh · covers AC5 AC6 AC7 · a traced fixture run whose stdout must equal the untraced one, its record naming the fixture's spec and legs reads, and a `popen` record refused; staged by a tracer that prints one line · its assertion floor, where it carries one
New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC2 · `dispatch.declare` in an unattended return and absent from an attended one, and the child's new opening sentence; staged by dropping the mode test on the field · its assertion floor, where it carries one
New arm: tools/lib/resolve-python.test.sh · covers AC4 · the `read_open_py` parity row; staged by one changed byte in the checker's inline copy · none

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
`memory hygiene`, the lexicon and the spec-token checker's `--spec` over this file.

## 8. Open questions

- **F1 — Is the `--dispatch` check scoped to the dispatching build, and on what terms?**
  RESOLVED (owner, 2026-11-14): (a). No scoping in this unit. Rev-1's S7 left §2 for §3, and the
  incremental per-spec checker is a follow-up ask at the wrap-up. The main loop corrects the build
  README's roster row for this unit.
  The brief allowed the scope only where the cross-build joins are shown not to move, and §4 shows
  they do. Options:
  - (a) Build no scoping here. S7 stays NOT OBSERVED, and an incremental checker, keyed per spec,
    is filed as a follow-up at the wrap-up. The build README's roster row for this unit names the
    scope and is corrected by its owner.
  - (b) Scope only when the record shows that nothing but this build's own specs moved since the
    last admitted whole-tree run, and that no waiver row, chain spec or packet run depends on them.
    That needs per-input hashes in the record and a checker mode that attributes waived hits, which
    is a second mechanism and, by M2, its own unit. It rarely applies, because a pass commit also
    moves product files that live specs cite.
  - (c) Scope always, and leave stale rows and bare-build carries findings to the bar. This moves
    the dispatch verdict, which the brief's non-goals forbid unless the owner lifts that.
  Recommendation: (a). It is the only option that keeps every verdict and needs no new mechanism.
  (b) is the feature-rich survivor if the owner wants it, as an added unit after this one.

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft from brief `2026-11-14-prompt-TOOL-aLightenedLoop-1-brief`,
  item 3, grounded at `846d51d3`. The child cannot run a shell, so "the harness or main loop" is
  read as the main loop, and the instruction travels as a hand-out field. "The files the checker
  reads" is read as the files and git answers one run observed, because the cited files make a
  declared list data-dependent. The scoping half is held at F1 on the measurement in §4.
- rev-2 · 2026-11-14 · §1 §2 §3 §4 §8 S7 · folded the owner's F1 answer from
  `2026-11-14-prompt-TOOL-aLightenedLoop-3-fork-fold`: option (a), no scoping. S7 is removed from
  §2 and the scoping half stands in §3 as out of scope, the incremental per-spec checker is a
  wrap-up follow-up ask, and F1 is marked RESOLVED. §6 named no scoping criterion, so no AC moved.

## 10. Reuse audit

The seams this unit extends: the hand-out's `dispatch` object and its command field
`resolvePathsWith` (`tools/workflows/unattended-build.js@996b9ed7:3039`); the unattended `DRIVER_STEPS`
branch (`tools/workflows/unattended-unit.js@71852dc0:258`); `derive_spec_token_key` and
`run_spec_token_check` (`tools/unattended/unattended.sh@95b8f840:14430`,
`tools/unattended/unattended.sh@95b8f840:14458`), re-keyed in place; the run-gates fingerprint, kept as the
run-window guard; and the policy kit's audit-hook read filter `add_source_read`
(`tools/policy/check_policy.py@4b35ad98:4182`), extracted to the lib dir under the parity table at its second
instance. `reuse_lookup.py` for "record which files a check read and skip the rerun when none of
them changed" ranked generic name stems only (`read_text`, `read`, `check`, `records`, `skip`), so
no caching seam fits beyond the fingerprint; `addaudithook` was then found by grep at
`tools/policy/check_policy.py@4b35ad98:5020`. Recall's top hit was TOOL-aSmoothedDispatch-4, whose key this
unit replaces. A scout note it surfaced named `derive_cache_key` (`tools/memory-tree/transition_audit.py@419c2700:636`
at `846d51d3`, cited there as line 693) as a key over declared inputs; that is the rejected
declared-list shape. TOOL-aHoistedPass-21, an ask about hoisting a dispatch to the main loop,
concerns Workflow calls rather than this verb.

Recall terms used: `python tools/memory-recall/query.py "how does the dispatch spec-token cache key on its inputs and who runs --dispatch before the builder" --terms "dispatch spec-token cache key fingerprint HEAD inputs builder spawn main loop write set scoped"`
