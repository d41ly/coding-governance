# TOOL-dDeclaredLoop-68 — the witness normaliser has one owner, the run-gates program, before unit 67 reads it

**Status:** INPROGRESS · rev-3 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 37 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-68-deviation-681.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-deviation-681.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-68-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-68-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-68-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-68-reground-brief.md) | research | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-68-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-68-build-brief.md) | journal | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**: `TOOL-dDeclaredLoop-56`'s inline Python normaliser
and `TOOL-dDeclaredLoop-67` AC17, which reads the run-gates program and no copy, could not both hold.
Rev-6 of 56 settled its own half by its §8 F7 (b): it builds no copy and leaves the normaliser to this
unit. So this unit builds the normaliser once, on its one owner, the run-gates kit's `write_normaliser`,
which 67 S24 already names.

The need is unchanged at the tip. `tools/loop/loop_witness.py#run_witness_commands` hashes each command's
output raw, so a command that prints its worktree path or a duration never re-runs equal, and a holding
probe reads `refuted`. This unit builds at order 37, after 56 and before 67, whose S24 and AC17 then read
the program route as landed. It repairs `TOOL-dDeclaredLoop-56`.

## 2. Scope (IN)

- **S1** — `run_witness_commands` hashes each command's output after the run-gates program normalises it,
  never a copy of the program's rules. It resolves `resolve_kit_dir("run-gates", "lib-attribute.sh", KIT)`
  before it adds the worktree. Once every command has run, one bash, the one the inline `resolve_bash`
  answers, sources `lib-attribute.sh`, writes the program once with `write_normaliser` into the re-run's
  temporary directory, and applies it with `LC_ALL=C sed -E -f` to each output file, writing a `.norm`
  file beside it. The hash is taken over the `.norm` bytes. The roots handed to `write_normaliser`, in
  order, are the worktree's absolute path, the worktree's `os.path.realpath`, and the repository's
  absolute path, each in forward-slash form from `Path.as_posix()`. No Python argv under `tools/loop/`
  names `sed`. Observed by AC1, AC2, AC3.
- **S3** — A run-gates kit that does not resolve, a bash that does not start, and a source,
  `write_normaliser` or `sed` step that exits non-zero or runs past the re-run's bound each refuse the
  re-run with a `LookupError` whose text is `witness: normaliser unavailable — <reason>`, and no hash is
  returned. A failing `sed` step's reason opens `sed:`. The kit is resolved before the worktree is added,
  so a missing kit adds no worktree. `acceptance` prints the refusal and exits 2 writing no record, as it
  does for every `LookupError` today. `rerun` answers each command `inconclusive`, as it does today, and
  also prints the reason on stderr as `loop-witness: inconclusive · <reason>`. Observed by AC4.
- **S4** — The plants `normalise` and `normaliser-missing` join `PLANTS` and the `--selftest` run.
  `normalise` re-runs one command twice at one commit. The command prints its working directory through
  bash's `pwd`, Python's `os.getcwd()` and `git rev-parse --show-toplevel`, then a duration whose digits
  come from a counter file outside the worktree, so the two runs print different durations.
  `normaliser-missing` rebinds the module's `KIT` to an empty scratch directory for its calls, runs the
  `rerun` verb in process from the fixture repository, and restores both the binding and the working
  directory before returning. Observed by AC1, AC4.
- **S5** — The user page and the carriers say what the hash is taken over. `help/loop.md`'s paragraph on
  the re-run says the output is normalised by the run-gates kit's program before it is hashed, and what
  that program strips; its re-run stand-in bullet lists the two plants. `tools/loop/README.md` and the
  module docstring of `tools/loop/loop_witness.py` say the same. The acceptance-record grammar in
  `tools/memory-tree/HYGIENE.template.md`, rendered into `memory/HYGIENE.md`, says the hash is of the
  output after `write_normaliser`'s program. Observed by AC5, AC6.

## 3. Non-goals (OUT)

- Which bytes the normaliser strips: `tools/run-gates/lib-attribute.sh#write_normaliser`'s own rules,
  unchanged. That file takes no edit, so neither run-gates runner that calls it moves.
- The loop kit's `requires` edge to run-gates, and the probe that every kit the loop kit resolves is one
  its descriptor names: `TOOL-dDeclaredLoop-79` S4 and S5 (the round-4 audit's ids 4 and 23). Until that
  pass, an install without the run-gates kit refuses each re-run by S3's name.
- `TOOL-dDeclaredLoop-67` S24's text: that pass reads S1 as landed and observes its AC17 over this unit's
  `normalise` plant.
- A spec-set check that reds a later spec's absence assertion over a token an earlier sibling mints, the
  finding's left-shift: the class is recorded at the close.

### What the built code and the committed specs already settle

- Rev-2's S2, the deletion of 56's Python copy and its `normalise_output` parity row, leaves the scope:
  56 rev-6 §8 F7 (b) builds neither, and `git grep -c normalise_output -- tools/` prints nothing at the
  tip. Rev-2's AC3, which observed that absence, leaves with it; 67 AC17 observes it at its own pass. The
  `resolve_bash_py` row stands, as 56 rev-6 §3 records against its S28.
- Rev-2's §5 claim that the loop kit's descriptor requires every kit it resolves was false at the time
  (round-4 id 4); it is `TOOL-dDeclaredLoop-79` S5's to make true, and this spec no longer states it.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-56` — §8 F7 (b), which builds no inline normaliser and no `normalise_output` row and leaves the normaliser of `run_witness_commands` to this unit
- **hands-off** `TOOL-dDeclaredLoop-67` — the program-route normaliser and the absent `normalise_output` row, which S24 and AC17 read as landed, AC17 over the `normalise` plant
- **hands-off** `TOOL-dDeclaredLoop-79` — the normaliser route and its named refusal in `tools/loop/loop_witness.py`, built here inside the resolved bash with forward-slash roots and a `sed:` reason (§8 F3), which S6, S7 and S12 re-ground onto; the descriptor's `requires` edge to run-gates and its probe (S4, S5; ids 4, 23); and the sibling-minted `loop computed witness` leg this pass keeps green (id 3)

## 4. Design

### Evidence

Every code claim below was read with `git show` on branch `unattended-declared-loop-d56bf0` at
`dca74c239`, the tip after `TOOL-dDeclaredLoop-53` landed.

- `tools/loop/loop_witness.py#run_witness_commands` writes each command's output to `cmd-<n>.out` beside
  the worktree and keeps `hashlib.sha256` of its raw bytes; the module docstring says the output is
  "reported, never normalised". Its callers are all in that file: `run_acceptance`, `run_rerun`,
  `check_rerun_plant`, `check_bash_syntax_plant` and `check_grandchild_plant`.
- `tools/loop/loop_witness.py#run_rerun` reads any `LookupError` from the re-run as `inconclusive` and
  prints no reason; `tools/loop/loop_witness.py#run_acceptance` prints it as `refused` and exits 2 before
  the writer runs.
- `tools/run-gates/lib-attribute.sh#write_normaliser` truncates its file, writes one `s|...||g` line per
  spelling of each non-empty root, then the `tmp.` name, duration, CR and trailing-space rules; its
  header says to apply the file with `sed -E -f`. `tools/run-gates/lib-attribute.sh#render_path_spellings`
  derives the backslash and `/c/` spellings from a root of the shape `X:/...`, so a backslash root yields
  no forward-slash rule (the round-4 audit's id 10). `run-gates.sh` and `run-selftests.sh` in that kit
  each call it once, on their attribution paths.
- `tools/loop/loop_lib.py#resolve_kit_dir` finds a kit by the install receipt, then beside `here`, then
  one level up, else raises `LookupError` naming the three places. From the module's `KIT` it finds the
  run-gates kit beside the loop kit in gov's tree.
- `help/loop.md` says the output "is hashed exactly as printed", and the acceptance grammar in
  `tools/memory-tree/HYGIENE.template.md` says the hash is of "the command's combined output".
- No acceptance record exists at the tip, and main carries no loop kit, so no hash recorded under the raw
  rule survives this pass: `git ls-tree -r --name-only dca74c239 memory/ | grep -c -E 'build/[0-9-]+-build-.*-acceptance-[0-9]+\.md$'`
  prints 0, PINNED 2026-11-16.

### The route (S1, S3)

```
lib   = resolve_kit_dir("run-gates", "lib-attribute.sh", KIT) / "lib-attribute.sh"
        LookupError -> LookupError("witness: normaliser unavailable — " + its text)   # before mkdtemp
...     the worktree added and every command run as today, each into <tmp>/cmd-<n>.out
roots = [Path(tree).absolute().as_posix(), Path(os.path.realpath(tree)).as_posix(),
         Path(repo).absolute().as_posix()]
run_normaliser(bash, lib, <tmp>/normalise.sed, roots, outs, env, timeout):
    [bash, "-c", '. "$1" || exit 3; p=$2; write_normaliser "$p" "$3" "$4" "$5" || exit 4; shift 5;
                  for f in "$@"; do LC_ALL=C sed -E -f "$p" < "$f" > "$f.norm" || exit 5; done',
     "_", lib.as_posix(), prog, *roots, *outs]
    exit 3, 4 or 5, any other non-zero, an OSError, past `timeout`
        -> LookupError("witness: normaliser unavailable — <source|write_normaliser|sed>: <exit or why>")
hash  = sha256(<tmp>/cmd-<n>.out.norm bytes)[:12]
```

The worktree's two spellings come first, because a command run in the worktree prints that path; the
realpath form covers a temporary directory reached through a short or linked name, which
`git rev-parse --show-toplevel` may print expanded. A root equal to another only writes duplicate rules.
`LC_ALL=C` makes `\b` and `[[:space:]]` byte rules, so two nodes with different locales hash one output
alike. The bash runs with `read_clean_env()`, as the commands do. Every path reaches it as a positional
argument, never inside the script text. Its stderr is read as UTF-8 with `errors="replace"` for the
reason, and the `.norm` files are read as bytes.

### Inventory

| Minted | Kind | Cell or table |
|---|---|---|
| `run_normaliser` | function in `tools/loop/loop_witness.py` | `py.function`, which `tools/lexicon/lexicon.py --suggest` answers OK |
| `check_normalise_plant` | function, the `normalise` plant | `py.function`, answered OK |
| `check_normaliser_missing_plant` | function, the `normaliser-missing` plant | `py.function`, answered OK |
| `normalise`, `normaliser-missing` | `PLANTS` keys | the `--plant` choices, which `tools/govkit/usage.toml` declares as any value |

No flag, verb, constant, leg, record kind or parity row is minted.

### Files touched (estimate)

- `tools/loop/loop_witness.py`
- `tools/loop/README.md`
- `help/loop.md`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`, rendered from the template by the parity suite's `--render`, never typed twice
- `memory/map/generated/symbols.json`, and any generated sibling the map's writer rewrites, regenerated in the unit's commit (§5)
- `tools/run-gates/selftest-budgets.txt`, its `loop computed witness` row, only where §5's measurement moves it

### Alternatives rejected

- **A Python port of the rules under a parity row.** It is rev-5 S27 of unit 56, the copy round 3 found
  incompatible with 67 AC17, and two implementations of one normaliser held equal by a byte arm is the
  copy the reuse rule forbids where the program runs in place.
- **A bare `sed` spawned from Python.** A re-run started outside Git Bash's PATH raises an unnamed
  `FileNotFoundError`, and a failing `sed` would hash empty output (the round-4 audit's ids 11 and 30).
- **One bash per command**, the literal argv of 79 S6. It spawns once per command where once per re-run
  serves, and the property 79 S6 asks, the apply step inside the resolved bash with no bare `sed`, holds
  either way.
- **Normalising inside `rerun` alone.** An `acceptance` record and a probe's expectation would then be
  hashed by two rules.

## 5. Production-readiness checklist

- security — no new surface. A sibling kit's library is sourced from the install's own tree, found by
  `resolve_kit_dir`, which skips a receipt row whose path leaves the tree, and applied to the re-run's own
  output files under the host temp directory. Every path reaches bash as a positional argument.
- perf / scale — one more bash per re-run, never per command: it writes the program once and runs `sed`
  once per output. The `loop computed witness` leg's budget row reads 75 s PINNED 2026-11-16, from a 50 s
  reading PINNED at `202e287fb`. The pass reads the leg's time once on its node and raises the row by the
  file header's rule, the worst reading times 1.5 floored at 60 s PINNED, only where the reading exceeds it, as
  unit 53's pass did for its own leg.
- error / empty / loading states — S3 refuses by name. Empty output normalises to empty and hashes as
  the empty string does. A timed-out command's partial output is normalised and hashed beside the exit
  `timeout`, as it is hashed raw today.
- observability — S3's text names the step and its exit, and `rerun` now prints it.
- risks — a path printed in a spelling none of the three roots produces, such as a relative path, stays
  in the output and reads as a difference: the direction `lib-attribute.sh`'s header chooses, failing
  toward noise. The `timeout-grandchild` plant's ten-second window now holds the normaliser's bash too;
  the pass reads the plant's printed time, and a reading over the window is a red of this pass, never a
  wider window. An install without the run-gates kit refuses every re-run until 79 S4 lands the edge.
- testing — AC1 to AC6 as plants and greps; the arm under §7, observed RED then GREEN at the close.
- migration — none: §4 Evidence shows no recorded hash under the raw rule, so no recorded `--expect`
  turns `refuted`.
- user docs — `help/loop.md`, by S5.

### Dependency

`TOOL-dDeclaredLoop-56` (order 36, committed rev-6) leaves `tools/loop/loop_witness.py` alone, by its §4
Dependency. `TOOL-dDeclaredLoop-70` (order 36, committed rev-3) imports `resolve_bash` from this module
inside `read_driver_conf`, a name this unit leaves alone. `TOOL-dDeclaredLoop-33` (rev-7), 54, 56, 63, 64,
70 and 72 edit `help/loop.md` or `tools/loop/README.md` at other sections, and none edits the re-run
paragraph or the stand-in bullet. At order 37, `TOOL-dDeclaredLoop-65` edits `tools/loop/position.py` and
`TOOL-dDeclaredLoop-76` edits `tools/loop/loop_lib.py`, `budget.py` and `breakpoints.py`, sharing only
`memory/map/generated/symbols.json`, which whichever lands second regenerates over the merged tree.
`TOOL-dDeclaredLoop-34` is deferred against ask TOOL-dDeclaredLoop-113 and edits another sentence of the
HYGIENE template; `TOOL-dDeclaredLoop-33`'s numeric direction is deferred against ask
TOOL-dDeclaredLoop-114. Neither shares a line with this unit.

### The sweep

Read at `dca74c239`. Each figure is PINNED 2026-11-16 and re-derived by the command beside it.

| What moves | Its readers, pins and populations | What keeps each green |
|---|---|---|
| the hash `run_witness_commands` returns | `git grep -n "run_witness_commands(" -- tools/` prints 8 lines PINNED: the definition, the five callers §4 names, the docstring and the README | `check_rerun_plant` derives its expectation through the same call, so its three verdicts hold; `check_bash_syntax_plant`'s `0` line carries nothing the program strips, so its owed hash holds (AC3); `check_acceptance_plant` compares exits; `check_grandchild_plant` reads the exit and the time |
| what the hash is taken over | `tools/memory-tree/build_records.py#read_acceptance` and `#write_acceptance` grade the `<hash12>` shape; `tools/loop/position.py` reads an acceptance record's `Sha` and `malformed`, never a hash | the shape is unchanged; S5 states the meaning in the grammar |
| the module's helpers | `git grep -l "from loop_witness import" -- tools/` lists 13 files PINNED, importing `read_git`, `read_clean_env`, `remove_tree`, `resolve_bash`, `resolve_commit`, `run_fixture_git` and `write_fixture_files` | none of them moves, and the run-gates kit is resolved inside the call, never at import |
| the module's `KIT` | `check_hold_plant` and `run_selftest` read it | `normaliser-missing` restores it before it returns, and plants run one at a time |
| the parity blocks | `tools/lib/resolve-python.test.sh`'s `resolve_bash_py`, `run_tree_kill_py` and `resolve_kit_dir` rows | no byte between their markers moves, and no row is added |
| `write_normaliser` | `run-gates.sh` and `run-selftests.sh`, and their suites | `lib-attribute.sh` takes no edit |
| usage rows and help anchors | `tools/govkit/usage.toml`'s three `loop_witness.py` rows, anchored on `help/loop.md` as `6de87be4`, `55bc486e` and `016ed8f7` | no flag or verb is added and `--plant=` takes any value, so no fingerprint moves; `python tools/govkit/docs_leg.py --fingerprints` re-derives them |
| the lexicon offender pin | `.lexicon.conf`'s `py.function` cell | §4's three names each answered OK to `python tools/lexicon/lexicon.py --suggest <name> --as py.function`, run on the worktree at `179486e8f`, so the pin gains no offender |
| shared records | `.unattended.conf`'s `SHARED_RECORDS`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | this pass writes neither, and no decision row is owed ahead of it |
| refusal ceilings and families | `tools/memory-tree/check-arms.py` discovers tracked `*.sh` files only, by its docstring | this pass edits no `*.sh`; its bash runs a string inside a Python file, so `tools/unattended/unattended.families.txt` and the driver's refusal census are untouched |
| encoding posture | `memory/project/encoding-posture-sites.txt` holds no loop row: `grep -c loop memory/project/encoding-posture-sites.txt` prints 0 PINNED | every new text read names `encoding="utf-8"`, and the `.norm` files are read as bytes |
| the install-prefix ban | `tools/loop/` and `tools/memory-tree/HYGIENE.template.md` are in its population | run-gates is reached by `resolve_kit_dir`, and prose names the run-gates kit's `lib-attribute.sh`, never the two joined by a slash; `git grep -n "run-gates/" -- tools/loop/loop_witness.py tools/loop/README.md tools/memory-tree/HYGIENE.template.md` prints nothing after the pass |
| kit epochs | the loop kit's and the memory-tree kit's shipped bytes move | the lander mints both versions, `tools/govkit/govkit.py#cmd_epoch` reading a move off the push boundary as owed at the lander; `KIT_LOOP_VERSION` and the README marker stay paired |
| the verdict epoch | `tools/memory-tree/check-verdict-epoch.sh`'s `DELEGATES` | the HYGIENE template is no delegate, and its body moves no verdict |
| the HYGIENE render | the `kit/dogfood doc parity` leg | the render is made from the template by the parity suite's `--render` |
| the recall corpus | the `recall floor` and `recall floor arms` legs guard `memory/HYGIENE.md` | the edit is one clause of one grammar sentence; both legs run at the close, and a moved score is a red of this pass, never a lowered floor |
| size caps | `tools/template-size-limits.txt` | `grep -c -E "loop|HYGIENE\.template" tools/template-size-limits.txt` prints 0 PINNED: no doc this pass edits carries a cap |
| the generated map | `memory/map/generated/symbols.json` lists every function | `python tools/codebase-map/gen_map.py --write` regenerates it in the unit's commit |
| the leg and its companions | `tools/gate-legs.json`, the `tools/govkit/subject-pins.tsv` row, the `[[exempt_leg]]` row of `tools/govkit/registry.toml` and the claim in `memory/map/features/loop.md` | no leg is added, renamed or re-argued; the exempt row's reason, gov's tree holding every kit the plants reach, holds for run-gates too |
| the kickoff manifest | `memory/guides/SESSION-KICKOFF.md`'s `watch:` line | it names none of the touched paths, so no re-stamp |
| upgrade steps | `tools/govkit/upgrade_steps.py` | no receipt, conf or adopter file changes shape, so no step row |
| a sibling's count | 72's `git grep -c "unattended\.conf" -- 'tools/loop/*.py'`, 1 PINNED for this module | the two plants spell no conf name |

## 6. Acceptance criteria

- **AC1** — When `python loop_witness.py --fixture --plant normalise` runs in `tools/loop/`, it exits 0:
  the two re-runs' hashes are equal, and neither is `e3b0c44298fc`, the hash of empty output.
  Red when: the raw output is hashed, a root reaches `write_normaliser` in a spelling the command does not
  print, or the apply step leaves the `.norm` file empty.
- **AC2** — When `grep -c write_normaliser loop_witness.py` runs in `tools/loop/`, it prints at least 1,
  and `git grep -n '"sed"' -- tools/loop/` prints nothing.
  Red when: the re-run carries a Python copy of the rules, or spawns `sed` from Python.
- **AC3** — When `python loop_witness.py --fixture --plant bash-syntax` and
  `python loop_witness.py --fixture --plant probe-rerun` run in `tools/loop/`, each exits 0: the `0` line
  still hashes as `9a271f2a916b`, the hash of `0` and a newline, and the re-run at a later commit still
  reads `refuted`.
  Red when: the program alters a line carrying no root and no duration, or strips a real difference.
- **AC4** — When `python loop_witness.py --fixture --plant normaliser-missing` runs in `tools/loop/`, it
  exits 0: with the run-gates kit looked for from an empty scratch directory, `run_witness_commands` raises
  a `LookupError` whose text opens `witness: normaliser unavailable`, the fixture repository lists one
  worktree, and the `rerun` verb run in process prints a `rerun · inconclusive · ` line and a stderr line
  carrying `witness: normaliser unavailable`, returning 1.
  Red when: the re-run falls back to the raw hash, adds its worktree first, or `rerun` reads inconclusive
  with no reason.
- **AC5** — When `grep -c "hashed exactly as" help/loop.md` runs it prints 0, `grep -c "never normalised"`
  in `tools/loop/` over `loop_witness.py` prints 0, and `grep -c normaliser-missing` over `help/loop.md`
  and `tools/loop/README.md` prints at least 1 for each.
  Red when: the page or the docstring still says the output is hashed as printed, or a carrier omits the
  plants.
- **AC6** — When `grep -n write_normaliser` runs over `tools/memory-tree/HYGIENE.template.md` and
  `memory/HYGIENE.md`, each prints one line in the acceptance-record grammar, and the two lines read alike.
  Red when: the grammar still says the hash is of the raw output, or the render diverges from its template.

## 7. Gates

`loop computed witness` · `encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `docs` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass keeps the sibling-minted `loop computed witness` leg green, the leg that runs the file it edits.

New arm: tools/loop/loop_witness.py · covers AC1 AC3 AC4 · the normalise and normaliser-missing plants, staged against the tip's raw hash, where the two re-runs differ and a missing kit raises nothing · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which spec owns the normaliser, 56 S27's copy or 67 S24's program?** Options: (a) the copy, 67
  AC17 dropped; (b) the program, 56's row deleted. (a) fails 67 AC17, a criterion already written, and
  veto 1 discards it. RESOLVED (agent, 2026-10-24, delegated): (b), at order 37 so neither pass is
  folded. widens: none · relaxes: none
- **F3 — Does this pass build the apply step 79 S6, S7 and S12 describe, or rev-2's route?** Options: (a)
  rev-2's route, `sed` spawned from Python, roots as given and a refusal on the write step alone, which 79
  rewrites at order 40; (b) the apply step inside the resolved bash, the roots in forward-slash form and
  the refusal covering the apply step, built once here, so 79's S6, S7 and S12 find them built and
  re-ground. (a) builds a route the round-4 audit judged defective (ids 10, 11 and 30) for a later unit to
  rewrite, the reason 56 §8 F7 gave for its own (b). Recommendation: (b). RESOLVED (agent, 2026-11-16,
  delegated): (b), by rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-3 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-79, written by the round-4 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-16 · §1 to §10 · S1, S2, S3, S4, S5 · AC1 to AC6 · §8 F3 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `dca74c239` and on the committed specs of TOOL-dDeclaredLoop-56
  rev-6, -67 rev-3 and -79 rev-5, per the brief `2026-11-16-prompt-TOOL-dDeclaredLoop-68-1-spec-writer`:
  56 builds no copy, so S2 and rev-2's AC3 leave the scope and S1 builds the normaliser on the program;
  by F3 the apply step runs inside the resolved bash over forward-slash roots, the realpath among them;
  S3 covers the apply step and `rerun` prints the reason; S4 names the plants; S5 brings the help page,
  the carriers and the record grammar; §7 names the leg and its keep-green sentence; §5 the sweep; line
  citations made symbol citations.

## 10. Reuse audit

The seam is the run-gates kit's `write_normaliser` (`tools/run-gates/lib-attribute.sh#write_normaliser`),
run in place, reached through `resolve_kit_dir` and the loop kit's inline `resolve_bash`; no copy is
minted. `python tools/codebase-map/reuse_lookup.py "normalise a re-run command's output, stripping worktree roots and durations, before hashing it"`,
on the worktree at `179486e8f`, ranked name-stem neighbours by fan-in, `run`, `repo_root`, `run_git` and
`read_git_output` among them, and the same file's `add_scratch_worktree` and `remove_scratch_worktree`;
none normalises output. `python tools/codebase-map/reuse_lookup.py "write the sed normaliser program that strips absolute roots from output"`
ranked `write_normaliser` itself, from `lib-attribute.sh`, low on fan-in, which is the seam, and reading
67 S24 and that file agrees with source.

Recall terms used: write_normaliser lib-attribute normaliser sed program roots as_posix witness rerun hash resolve_kit_dir resolve_bash run-gates
