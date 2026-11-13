# TOOL-aWitnessedCrash-1 — check 23's maps are declared set, and the hygiene engine reds on a bash runtime error it ran past

**Status:** INPROGRESS · rev-2 · 2026-11-13 · node a · Tier-1 · base f9a87e782 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-prompt-TOOL-aWitnessedCrash-1-1-revision.md](../prompts/2026-11-13-prompt-TOOL-aWitnessedCrash-1-1-revision.md) | research | — |
| [2026-11-13-prompt-TOOL-aWitnessedCrash-1-2-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-aWitnessedCrash-1-2-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-aWitnessedCrash-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aWitnessedCrash-1-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

On a commit that stages a memory file outside every build folder, the hygiene engine prints
`check-memory-hygiene.sh: line 3611: ALFORM: unbound variable` and still exits 0. Fix that line, and
make any bash runtime error the engine reports on its own stderr red the run, because bash 5.3 runs
on past some of them under `set -u` and the exit status cannot see them.

## 2. Scope (IN)

- **S1** — Check 23 declares its six associative arrays with an empty value, so every
  `${#…[@]}` read sees an empty set instead of an unset name. Observed by AC1.
- **S2** — A crash witness in `tools/memory-tree/check-memory-hygiene.sh`. The engine keeps its own
  stderr in a temporary file and replays it at exit. A line in bash's runtime-error shape turns an
  exit 0 into exit 1, with a `HYGIENE FAILED` line naming it, and adds a `check crash` key under
  `--offenders`. Exit 2 stays exit 2. Observed by AC2, AC3 and AC4.
- **S3** — A self-test arm in `tools/memory-tree/check-memory-hygiene.test.sh` that injects a
  non-fatal runtime error into a copy of the engine and asserts the red. Observed by AC2 and AC3,
  which the arm re-observes. Its RED-first run belongs to the close and is declared on the
  `New arm:` line in section 6.
- **S4** — The memory-tree kit version moves once, after the last code move, in every file that
  carries its stamp. Observed by AC5.

## 3. Non-goals (OUT)

- No other check's logic moves. That includes the other `declare -A` maps with no value
  (`LEGACY_SET`, `DEBT_SET`, `DEBT_EARNED`, `STAGED_SET`, `_SBUILD`, `TRACKED_SET`). The witness
  covers any of them that ever crashes.
- No new gate leg, and no static lint for unset arrays across the tree.
- No witness over the code before the resolver call at line 613. That covers argument parsing, the
  conf source and the print modes. No check runs in that region.
- No rule added to `memory/HYGIENE.md` and no help page. No flag, verb or conf key is added, and
  `git grep check-memory-hygiene -- help/` finds only `help/shims.md`, which documents a shim
  record and not the engine's verdicts.

## 4. Design

### The defect

All citations below are to `tools/memory-tree/check-memory-hygiene.sh@0a32d7bf2`, the blob at base.

Check 23 declares `declare -A ALFORM ALTOK` with no value (`:3547`). It also declares
`ALLABERA ALTOKERA` (`:3561`) and `ALHASLAB ALSPECLAB` (`:3571`) the same way. A map that never
receives a key stays unset. Under `--staged` with no build folder staged, the ledger stream is empty,
so `ALFORM` stays unset. Then `if [ "${#ALFORM[@]}" -gt 0 ]` (`:3611`) is an expansion error. Bash
prints it, fails the `[`, reads the `if` as false and goes on.

That was reproduced at base on 2026-11-13 (PINNED). In a clone of base, with one blank line appended
to `memory/HYGIENE.md` and staged, `--staged` printed the line above on stderr and exited 0.

The exit status cannot see this class. Probes on node a's `bash 5.3.9`, run against scratch scripts:

| Probe | Result |
|---|---|
| `: "${#X[@]}"` over `declare -A X`, under `set -u` | error printed, script continues, exit 0 |
| the same with `trap … ERR` set | the ERR trap never fires |
| the same under `set -o posix` | error printed, script continues, exit 0 |
| `for k in "${!X[@]}"` over the same unset map | no error |
| `: "${#Y[@]}"` over `declare -A Y=()` | no error |

### S1 — the six maps

Each of the three `declare -A` lines gains `=()` on every name, for example
`declare -A ALFORM=() ALTOK=()`. That is the whole change. The FIRST-WINS reads such as
`${ALFORM[$_alk]+x}` behave the same over an empty map as over an unset one.

### S2 — the witness

**Setup**, directly after the resolver line `_PY=$(resolve_python) || …` (`:613`):

```bash
# TOOL-aWitnessedCrash-1: the crash witness. Bash 5.3 runs on past some runtime errors under
# `set -u` (an unset map's `${#X[@]}` fails its command and the script continues), so the exit
# status cannot see a check that stopped part-way. This engine's stderr is kept and replayed at
# exit, and the tail reds on any line in bash's runtime-error shape.
_CRASH_LOG=$(mktemp) || { echo "HYGIENE — cannot run: mktemp failed, and the crash witness keeps this engine's stderr in a file"; exit 2; }
exec 4>&2 2>"$_CRASH_LOG"
trap 'exec 2>&4; cat "$_CRASH_LOG" >&2; rm -f "$_CRASH_LOG"' EXIT
```

It sits after the resolver because the resolver tests `[ ! -t 2 ]` (`:585`) before offering an
interactive install. Redirecting stderr above that line would withdraw the offer from a user at a
terminal. The resolver block is a byte-identical canonical copy held equal by a parity gate, so it is
not edited.

The engine sets no other trap, and nothing in it uses fd 4. A command substitution or subshell does
not inherit the EXIT trap, so an `exit` inside one never replays or removes the log early. On node
a, bash ran an EXIT trap when the shell was sent SIGTERM, so a run killed at a ceiling still
replays its stderr. A SIGKILL loses it.

**Tail**, a new block between the empty-population report (`:3651` to `:3661`) and the
`# THE KEYS` block (`:3663`):

```bash
_crash=$(grep -E '^.+: line [0-9]+: ' "$_CRASH_LOG" || true)
if [ -n "$_crash" ]; then
  echo "HYGIENE FAILED — bash reported a runtime error on this engine's stderr, so a check may have stopped part-way and its silence is not a pass:"
  printf '%s\n' "$_crash"
  status=1
  [ "$OFFENDERS" = 0 ] || add_offender_keys crash $'\n'"$(printf '%s\n' "$_crash" | sed -E 's#^(.*/)?([^/]*): line [0-9]+: #\2: #')"
fi
```

- **The shape** is bash's own: `<name>: line <N>: <message>`. The name is the script path as
  invoked, which may carry a drive colon. A line from a child bash script, or from an awk that
  reports in that shape, also matches. Either one is a delegate that stopped, which is the class.
  The engine's own notices on stderr all open `memory-hygiene: ` and carry no `line <N>:`, so they
  keep their verdicts.
- **Exit codes.** `status` is 0 or 1 when control reaches the tail, because every refusal exits 2
  where it stands. The `--only` liveness block's exit 2 runs after this block, so it still wins.
  The trap replays stderr on every exit path, exit 2 included.
- **The key** drops the path's directories and the `line <N>`. The bar compares offender sets
  across two trees, and the `--offenders` header at `:59` requires a key with its line locator dropped. A key
  carrying either part would move when an unrelated edit lands above an inherited crash. The block
  does not call `fail`, as the empty-population block does not. So the `fail` branch population that
  `check-arms.py` discovers is unchanged.
- **Ordering.** Stderr now reaches the caller at exit, after stdout. The brief accepted this.
- The header paragraph opening `# Exit 0 = clean` (`:32`) gains one sentence: a line in bash's
  runtime-error shape on this engine's stderr reds an otherwise clean run, and the stderr is replayed
  at exit.

### S3 — the arm

The arm sits in `tools/memory-tree/check-memory-hygiene.test.sh@cc82fd639`, directly after the
young-tree assertions (`:2296` to `:2302`). It reuses `$Y`, the freshly built green tree that
`:2296` asserts exits 0. It copies the kit directory to `$TMP/wcrash`, the shape the `--only` arm
uses at `:1278`, so the trap at `:39` removes it.

The copy runs with `--only 1`, because a full run of a copied kit reds check 9 on `$Y`. Measured at
base on 2026-11-13: the fresh render differs when the generator runs from another directory. Under
`--only 1` only check 1's block runs, but the injected line sits at the tail outside every block,
so it runs either way.

The injection inserts two lines above `# --- empty-population report`, the line at `:3651`, which
precedes the witness block:

```bash
declare -A __wc_probe
: "${#__wc_probe[@]}"
```

This is the shipped defect's own shape, an unset map's count, and not a simpler stand-in. Six
top-level assertions, none skipped:

1. The uninjected copy, `--only 1` over `$Y`, exits 0. This is the precondition that pins the red
   to the injection.
2. The injected copy holds `__wc_probe` exactly twice, so the `sed` landed.
3. The injected copy, `--only 1`, exits 1.
4. Its stdout carries `HYGIENE FAILED — bash reported a runtime error`.
5. Its stderr, captured to a file, carries `__wc_probe: unbound variable`, so the replay ran.
6. The injected copy under `--offenders` prints the exact fd-3 row
   `check crash<TAB>check-memory-hygiene.sh: __wc_probe: unbound variable`.

`FLOOR_ASSERTIONS` (`:4646`, 690 at base) rises by six. Its comment follows the house form of the
`RAISED` lines above it: the build that raised it, the count, and "Counted by reading; OWED: observed at
the close."

At base, assertions 3, 4 and 6 fail. Measured on 2026-11-13: the injected copy exited 0 under
`--only 1` and printed the error only on stderr.

### S4 — the version

`KIT_MEMORY_TREE_VERSION` moves from 2.158 to the next minor above the value at the build's tip.
That is 2.159 unless the tip has moved. It is one commit after the last code move. Every file
`git grep -l "memory-tree@2.158" -- ':!memory/builds'` lists at base moves with it: the engine, the
four `tools/memory-tree/*.template.md` files, and their four dogfood copies under `memory/`. The
pathspec leaves out build records, which quote a stamp as prose and carry none. This spec is one.

### The probe a pass runs for AC2 to AC4

From the pass's worktree root, in Git Bash, with every fixture under a short `%TEMP%` path. Build
`Y` exactly as the suite's young-tree arm does (`check-memory-hygiene.test.sh@cc82fd639:2269` to
`:2287`), then:

```bash
K="$(cygpath -u "$LOCALAPPDATA")/Temp/wck"; rm -rf "$K"; mkdir -p "$K"; cp -r tools/memory-tree/. "$K"/
sed -i 's/^# --- empty-population report/declare -A __wc_probe\n: "${#__wc_probe[@]}"\n&/' "$K/check-memory-hygiene.sh"
( cd "$Y" && bash "$K/check-memory-hygiene.sh" --only 1 2>"$K.err" ); echo "rc=$?"
( cd "$Y" && bash "$K/check-memory-hygiene.sh" --offenders 2>/dev/null 3>&1 ) | grep -F 'check crash'
```

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `tools/memory-tree/ANNOTATION-STYLE.template.md`
- `memory/HYGIENE.md`
- `memory/TEMPLATE-SPEC.md`
- `memory/guides/BUILD-METHOD.md`
- `memory/guides/ANNOTATION-STYLE.md`

### Alternatives rejected

Each one was tested on node a's `bash 5.3.9` on 2026-11-13.

- **An ERR trap.** It never fired on the expansion error, inside an `if` or outside one.
- **`set -o posix`**, to make expansion errors fatal. The script still printed the error, continued
  and exited 0.
- **`exec 2> >(tee "$log" >&4)`**, which would keep stderr streaming in order. Reading the log
  right after the error missed it in 1 of 10 runs, because the tee process had not drained its pipe
  yet. Closing the race needs a `wait` on a process-substitution pid, which is more moving parts
  than the replay for a gain in ordering only.

## 5. Acceptance criteria

- **AC1** — In a clone of the built tip under a short `%TEMP%` path, with one blank line appended to
  `memory/HYGIENE.md` and staged, `bash tools/memory-tree/check-memory-hygiene.sh --staged` prints
  no line containing `unbound variable` on either stream and exits 0.
  Red when: S1 is skipped. Then the line at `:3611` prints, and with S2 built the run exits 1.
- **AC2** — When the probe in section 4 runs the injected copy with `--only 1` over the young tree,
  it exits 1. Its stdout carries `HYGIENE FAILED — bash reported a runtime error`, and its stderr
  file carries `__wc_probe: unbound variable`. The uninjected copy exits 0 over the same tree.
  Red when: the witness block is absent, as at base, where the injected copy exits 0.
- **AC3** — When the injected copy runs with `--offenders` over the young tree, fd 3 carries exactly
  the row `check crash<TAB>check-memory-hygiene.sh: __wc_probe: unbound variable`, with no
  `line <N>` and no directory in it.
  Red when: the key keeps the path or the line number, or `add_offender_keys` is never called.
- **AC4** — When a copy carries both the injection and the shadowed guard the suite stages at
  `check-memory-hygiene.test.sh@cc82fd639:1284` (`check_selected() { return 1; }` above
  `if check_selected 12 25; then`), `--only 12` over the young tree exits 2, not 1.
  Red when: the witness exits on its own, or it runs after the `--only` refusal and overwrites its
  status.
- **AC5** — When `git grep -l "memory-tree@2.158" -- ':!memory/builds'` runs at the built tip, it
  lists nothing, and `git grep -l "memory-tree@2.159" -- ':!memory/builds'`, or the version S4
  chose, lists the same nine files that the first grep listed at base. The pathspec leaves out build
  records, because this spec quotes both strings in its own prose.
  Red when: a stamp is left behind, or the engine moves without its templates.

## 6. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC3 · the engine at base, with no witness block, under the same injection: the injected copy exits 0 and prints no `HYGIENE FAILED` line and no `check crash` key · FLOOR_ASSERTIONS 690 to 696

The close runs these legs and observes the arm. A full engine run at base, measured on 2026-11-13
(PINNED, 11 min 43 s on node a), printed no line in the runtime-error shape on stderr. So the
witness adds no red to the `memory hygiene` leg on today's tree. Other suites run the engine over
their own fixture trees. If one of those trees provokes a runtime error, the witness reds that suite
at the close, and that is a finding for this unit, not noise.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-13 · initial draft.
- rev-2 · 2026-11-13 · S4 · AC5 · the builder's divergence, carried by
  `2026-11-13-prompt-TOOL-aWitnessedCrash-1-1-revision`: AC5's unscoped greps listed this spec,
  which quotes both stamp strings, so the criterion could not be observed. Both greps now take the
  pathspec `':!memory/builds'`. At the tip the 2.158 grep lists nothing and the 2.159 grep lists the
  nine carriers, the same nine the 2.158 grep lists at base f9a87e782. No code move is owed, so the
  built pass commits 8e4f578c3 and ef4855a15 stand.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py` named no seam that reads a script's own stderr for a bash
runtime error. Its candidates were generic readers and runners (`read_text`, `read`, `run`) and the
gates' shared `fail` helper. The witness extends the engine's existing seams instead:
`add_offender_keys` for the key, the empty-population block's `HYGIENE FAILED` and `status=1`
shape for the verdict, and the final `exit "$status"`. Recall named the fatal siblings
`TOOL-aHoistedPass-37` and `TOOL-aTracedSpawn-1`, and `TOOL-dGroundRules-85`, whose spec saw the
same `ALFORM` line in a tree with no spec and masked it. This unit covers the non-fatal form.

Recall terms used: `python tools/memory-recall/query.py "how does the hygiene engine catch a check that crashed under set -u without exiting" --terms "set -u unbound variable crash hygiene engine stderr runtime error exit status offenders silent pass"`
Lookup used: `python tools/codebase-map/reuse_lookup.py "a script reads its own stderr for a bash runtime error and fails the run"`
