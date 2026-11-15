# TOOL-aTrimmedWait-5 — the holder's idle-wake `--resume` stops paying one git process per briefed unit

**Status:** CLOSED · rev-3 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 5 · ratified 2026-11-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aTrimmedWait-5-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aTrimmedWait-5-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-aTrimmedWait-1-arms-observed.md](../build/2026-11-15-build-TOOL-aTrimmedWait-1-arms-observed.md) | journal | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 TOOL-aTrimmedWait-8 TOOL-aTrimmedWait-9 TOOL-aTrimmedWait-10 |
| [2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md) | research | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 |
| [2026-11-14-prompt-TOOL-aTrimmedWait-5-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-5-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-5-3-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-5-3-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-5-fix.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-5-fix.md) | research | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-5-ruling.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-5-ruling.md) | research | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-5-writing-practice.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-5-writing-practice.md) | research | — |
| [2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1.md](../reviews/2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1.md) | diff-review | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 |

<!-- /gen:spec-records -->

## 1. Goal

The idle-wake runs `--resume` every tick, and the brief puts that tick at 51 s in session <!-- PINNED 2026-11-14 -->
`db957487`. Measured for this spec, most of a holder's tick is one loop in `verb_status`: it spawns
one `git hash-object` per parked brief row to grade `STALE briefs`, and dFairHearing's record
briefed 45 units. This unit hashes every brief in one git call, so the tick, `--status` and every <!-- PINNED 2026-11-14 -->
take-over row stop paying per brief, and every line the verb prints stays byte-identical.

The roster names a different mechanism for this item, a replay of the last verdict. Section 8 F1
puts that choice to the owner with the measurements. Sections 2 to 7 are written for F1's
recommendation, and a ruling for the replay rewrites them in a rev-2.

## 2. Scope (IN)

- **S1** — The brief-staleness reader in `verb_status` hashes the briefs it can find in ONE
  `git hash-object --stdin-paths` call, in place of one `GIT hash-object` and one `cut` per row.
  It compares each 12-hex prefix with its row's recorded hash exactly as today, so `STALE briefs`
  and `briefs gone` keep their counts. Observed by AC1 and AC2.
- **S2** — When the batched call exits non-zero, or prints a different number of lines than it was
  given paths, the reader grades every row with today's per-path call. A batch failure therefore
  never moves a count. Observed by AC3.
- **S3** — The acceptance ledger records one holder `--resume` on the §4 fixture, timed with the
  base driver and with the built one on node a. Observed by AC4.

## 3. Non-goals (OUT)

- No replay or cache of `--resume`'s output, no key over HEAD, the run-state file or the task
  registry, and no new sidecar. That is F1's option B and stays out unless the owner rules for it.
- No change to the rows `--resume` decides, its refusals, its claim reads and renewals, its lease
  writes, the orphan reap, or which lines it prints.
- No change to how a brief row is written. The writer at
  `tools/unattended/unattended.sh@95b8f8404cc3:13353-13355` keeps its per-path `GIT hash-object`.
- No change to the brief rows' feed. The `BRIEFROWS` heredoc stays the loop's feed, so its row in
  `memory/project/substitution-fed-loops.txt` (`@6c73310d390c:65`, count 1) stays as written.
- No change to driver startup. A refused `--release-task` took 4.7 s at kickoff (brief, "Drawn
  from the session"), and every verb pays that, this one included.
- No `--release-task` change. The brief's Non-goals rule it out below the 4.7 s startup.
- No kit version bump. The build README moves kit versions once, after the last code move.
- No help page or verbs guide edit. The verb's output does not change, and no page under `help/`
  names `--resume` (grep over `help/` at `a25c84fc0`).

### Edges

none

## 4. Design

### What a holder's tick spends, measured for this spec

All readings were taken on node a on 2026-11-14, against code byte-identical to the base
`846d51d3`. The host was contended by other sessions, so they bound the cost rather than pin it.

| Reading | Result |
|---|---|
| Holder `--resume`, a clone of this repo, a record with no brief rows, untraced | 33.5 s |
| The same under `bash -x` with timestamps | startup 13.0 s, `verb_status` 7.9 s, the rest under 1 s | <!-- PINNED 2026-11-14 -->
| The same record with 72 brief rows, traced | 24.3 s in all: startup 2.1 s, `verb_status` 21.4 s, of which the brief loop is 16.2 s |
| `hash-object` calls in that trace | 72, every one at `verb_status`'s brief loop, none elsewhere |
| 72 spec files hashed one `git hash-object` each, then in one `--stdin-paths` call | 15.9 s, then 1.07 s |
| Holder `--resume` on the §4 fixture, 72 rows, base driver | 34.5 s, exit 0 | <!-- PINNED 2026-11-14 -->
| Brief rows in landed run records | dFairHearing 52 rows over 45 units, dTrueNorth 30 over 30 | <!-- PINNED 2026-11-14 -->

The batched call printed the same hashes as the per-path calls, in input order. That held for a
file with CRLF line endings under `core.autocrlf=true`, the value a clone on node a reads.

### The code today

`verb_status` (`tools/unattended/unattended.sh@95b8f8404cc3:8361`) builds one status line. Its
brief reader is lines 8435-8455. An `awk` pass over the run-state file keeps the latest
`brief · item · reason` row per unit, and feeds `<12-hex> <path>` lines through the `BRIEFROWS`
heredoc. For each line the loop counts the path gone when `[ ! -f ]` holds. Otherwise it runs
`_bnow=$(GIT hash-object "$_bp" 2>/dev/null | cut -c1-12)` (line 8440) and counts a stale brief when
the prefixes differ. A failed call leaves `_bnow` empty, which counts as stale. Lines 8454-8455
append the two fields to the status line. `GIT` is
`git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV" "$@"` (`tools/unattended/lib-unattended.sh@a3e03db6b9f0:62`).

`verb_resume`'s holder row (`tools/unattended/unattended.sh@95b8f8404cc3:9507-9566`) calls
`verb_status` once per tick at line 9563. The take-over rows reach it too, through `run_takeover`
and the `verb_status "$slug" || true` lines ahead of their refusals.

### S1 — one call

1. The `BRIEFROWS` loop keeps its feed and its `[ ! -f ]` test. A present brief no longer hashes
   inside the loop. Its recorded prefix and its path are appended to two arrays, in feed order.
2. After the loop, if the path array is non-empty, one call hashes them all:
   `printf '%s\n' "${paths[@]}" | GIT hash-object --stdin-paths 2>/dev/null`, taken into a variable
   with its exit status kept. A path read from the record cannot hold a newline, because the
   `awk` feed is line-split.
3. The output is split into an array with a builtin, such as `mapfile -t` over a here-string. No new
   loop is fed by a command substitution.
4. Row `i` is stale when `${now[i]:0:12}` differs from the recorded prefix `i`, as today.

`--stdin-paths` hashes each path as a file with that path's filters, as the path-argument form the
writer uses does. So a row the writer recorded fresh reads fresh.

### S2 — the fallback

Step 2's output is trusted only when the call exits 0 and its line count equals the path count.
Otherwise the reader takes today's per-path call for every row in the arrays, with today's rule
that an empty answer is stale. The counts are then those of the code today, row for row. The
fallback runs only on a failed batch, so the common tick pays one process.

### The pass probe, `$SCRATCH/r5.sh`

`$SCRATCH` is the run's scratch directory. The probe builds a fixture repository at `$TEMP/tw5f`,
a short path as the build's clone rule requires, and runs the driver in it from the worktree, as
this spec's author did at `a25c84fc0`. That run graded the fixture: the worktree's driver and a
base copy run from a scratch directory printed identical stdout. The base copy also prints one
`resolve_generated_indexes found no .git` line on stderr, so the probe compares stdout only.

```bash
set -u
G=$(pwd); R="$TEMP/tw5f"; B="$SCRATCH/base5"; rm -rf "$R" "$B"; mkdir -p "$R/memory/builds/tB" "$B"
git show 846d51d3:tools/unattended/unattended.sh > "$B/unattended.sh"
git show 846d51d3:tools/unattended/lib-unattended.sh > "$B/lib-unattended.sh"
cd "$R" || exit 2
git init -q . && git checkout -q -b tw && git config user.email t@t.test && git config user.name t
git config core.autocrlf false
cp "$G/.unattended.conf" "$G/.memory-tree.conf" . && sed -i 's/^RUN_CLAIMS="on"/RUN_CLAIMS="off"/' .unattended.conf
printf '# tB\n' > memory/builds/tB/README.md
for i in $(seq 1 72); do printf 'brief %s\n' "$i" > "memory/builds/tB/b$i.md"; done
git add -A && git commit -qm seed && H=$(git rev-parse HEAD)
{ printf '# tB - run state\n\n## Run facts\nwitness: %s\nphase: BUILDING\nmode: slug\nrun-branch: refs/heads/tw\n' "$H"
  printf 'lease-utc: %s\npid: 4242\nsession: tw-sess\nkeepalive: kTB\nbase: %s\n\n## Parked\n\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$H"
  for i in $(seq 1 72); do
    printf '2026-11-14T10:00:00Z brief · item TOOL-tB-%s · reason %s memory/builds/tB/b%s.md\n' \
      "$i" "$(git hash-object "memory/builds/tB/b$i.md" | cut -c1-12)" "$i"
  done; } > memory/builds/tB/RUN.md
git add -A && git commit -qm run
printf 'edited\n' >> memory/builds/tB/b2.md && rm memory/builds/tB/b3.md
export CLAUDE_CODE_SESSION_ID=tw-sess CLAUDE_PID=4242
REAL=$(command -v git); mkdir -p "$SCRATCH/shim5"; SH=$(cygpath -u "$SCRATCH/shim5")
printf '#!/bin/bash\ncase " $* " in *" hash-object "*) printf "%%s\\n" "$*" >> "$SHIM_LOG";; esac\n[ -n "${SHIM_FAIL:-}" ] && case " $* " in *" --stdin-paths "*) exit 1;; esac\nexec "%s" "$@"\n' "$REAL" > "$SCRATCH/shim5/git"
chmod +x "$SCRATCH/shim5/git"
for d in base new; do
  drv="$G/tools/unattended/unattended.sh"; [ "$d" = base ] && drv="$B/unattended.sh"
  bash "$drv" --status tB 2>/dev/null > "$SCRATCH/r5-$d.status"
  bash "$drv" --resume tB --keepalive-id kTB 2>/dev/null > "$SCRATCH/r5-$d.resume"
  SHIM_LOG="$SCRATCH/r5-$d.calls"; : > "$SHIM_LOG"; export SHIM_LOG
  PATH="$SH:$PATH" bash "$drv" --status tB >/dev/null 2>&1
done
SHIM_LOG="$SCRATCH/r5-fail.calls"; : > "$SHIM_LOG"
SHIM_FAIL=1 PATH="$SH:$PATH" bash "$G/tools/unattended/unattended.sh" --status tB 2>/dev/null > "$SCRATCH/r5-fail.status"
cmp "$SCRATCH/r5-base.status" "$SCRATCH/r5-new.status" && echo "status identical"
cmp "$SCRATCH/r5-base.resume" "$SCRATCH/r5-new.resume" && echo "resume identical"
grep -o 'STALE briefs 1 · briefs gone 1' "$SCRATCH/r5-new.status"
echo "calls base $(grep -c '' "$SCRATCH/r5-base.calls") new $(grep -c '' "$SCRATCH/r5-new.calls") stdin $(grep -c -- '--stdin-paths' "$SCRATCH/r5-new.calls")"
cmp "$SCRATCH/r5-base.status" "$SCRATCH/r5-fail.status" && echo "fallback identical"
echo "fallback calls $(grep -c '' "$SCRATCH/r5-fail.calls")"
```

The shim logs every `hash-object` call the driver makes, then runs the real git. With `SHIM_FAIL`
set it fails the batched call, which stages S2. The shim directory goes on PATH in its POSIX
spelling, because a `C:/` entry splits at its colon. This writer ran the block at `a25c84fc0`,
before any build, and it printed `status identical`, `resume identical`, the `STALE briefs` field,
`calls base 71 new 71 stdin 0`, `fallback identical` and `fallback calls 71`. The probe removes nothing the build reads; the main
loop removes `$TEMP/tw5f` after AC4.

### What this does not check

- Whether `--stdin-paths` and the path-argument form agree under every filter. They agreed on a
  CRLF file under `core.autocrlf=true` and on 72 spec files. A smudge or clean filter that reads
  the command line is not exercised, and this repo declares none.
- The other per-tick costs. Startup, the claim read under `RUN_CLAIMS=on`, the lease clock and the
  unit derivation keep their price. The traced fixture put `verb_status` outside the brief loop at
  5.2 s.

### Rollout

One pass at order 5. Units of this build that edit `tools/unattended/unattended.sh` may land
first, so the cited lines move: the builder finds the site by the `BRIEFROWS` tag and the
`_bnow=$(GIT hash-object` text. The driver suite's `FLOOR_ASSERTIONS`
(`tools/unattended/unattended.test.sh@0d9cd1632c89:19547`) rises by the count of new assertions,
and the close confirms the count from a real run.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Replay the last `--resume` output when HEAD, the run-state file and the task registry match.**
  It is the roster's wording, and F1 carries it to the owner. As worded, it moves a verdict: the
  stop-guard appends a line to `stop.<slug>.log` at every stop of a bound session
  (`tools/unattended/stop-guard.js@241f63c7925b:64-67`, `:224-233`). Each idle tick ends a turn,
  and `verb_status` prints that line's time on the status line
  (`tools/unattended/unattended.sh@95b8f8404cc3:8511`). So a faithful replay must re-read that field
  every tick, and the key must cover far more than three inputs (F1 lists them).
- **Hash the briefs once per run and store the result.** A brief edited between ticks is the case
  the reader exists for (`tools/unattended/unattended.sh@95b8f8404cc3:8424-8426`), so a stored
  answer must be keyed on the files, which is a hash again.
- **Grade only a unit's latest brief, or skip landed units.** The reader already keeps the latest
  row per unit, and skipping rows would move the count.

## 5. Production-readiness checklist

- security — N/A. No new input, path or write. The paths come from the record, as today, and reach
  git on stdin instead of argv.
- perf / scale — a tick pays one git process for its briefs instead of one per briefed unit, about
  15 s at 72 rows on node a (§4, PINNED 2026-11-14 on a contended host).
- error / empty / loading states — no brief row runs no call. A gone brief is counted before any
  hash. A failed or short batch falls back to today's per-path grading.
- observability — unchanged. The fields are the same bytes, and AC4's ledger lines carry the timing.
- risks — a batch whose lines align with the wrong rows would move `STALE briefs`. AC1 and AC2 pin
  the order on a fixture with a stale, a gone and 70 fresh rows.
- testing — the §4 probe for the pass, and the driver suite's new arm, observed RED then GREEN at
  the close.
- migration — none. No record shape changes.
- user docs — none. The output is unchanged, and no help page names the verb.

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/r5.sh"`, the §4 block, run from the worktree
root.

- **AC1** — When `bash "$SCRATCH/r5.sh"` runs, it prints `status identical`, `resume identical` and
  `STALE briefs 1 · briefs gone 1`.
  Red when: a batched hash is matched to the wrong row, so the stale count reads other than 1 and
  the base and new reports differ.
- **AC2** — When `bash "$SCRATCH/r5.sh"` runs, it prints `calls base 71 new 1 stdin 1`.
  Red when: the reader still hashes per row, so the new count reads 71.
  figure: DERIVED from the fixture. It holds 72 rows, one of them gone, so the base driver hashes 71
  paths.
- **AC3** — When `bash "$SCRATCH/r5.sh"` runs, it prints `fallback identical` and `fallback calls 72`:
  the failed batch, then 71 per-path calls.
  Red when: a failed batch counts every brief stale, or none, so the fallback report differs from
  the base.
- **AC4** — When the main loop times `bash "$SCRATCH/base5/unattended.sh" --resume tB --keepalive-id kTB`
  and then the built driver's same call in `$TEMP/tw5f`, with the probe's two exports set, one at a
  time on node a with no suite beside them, the acceptance ledger records both readings, and the
  second is the lower.
  Red when: the built driver still spawns per brief, and the two readings fall within the host's
  noise of each other.
  figure: PINNED for the base at 34.5 s, measured by this spec's author on 2026-11-14 on a contended
  host. The ledger's readings are DERIVED at observation.
  cost: about a minute for both readings.

## 7. Gates

`scratch-guard self-test` · `tier2-review self-test` · `unattended kit gate` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fixed-name temp renamed into place)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

`python tools/check-spec-tokens.py --legs-for` over the two files touched names
`scratch-guard self-test` and `tier2-review self-test` as guarded by
`tools/unattended/unattended.sh`, beside the broad `tools/` guards it prints and excludes. The
unguarded legs beside them read what this unit changes. The kit-version legs are graded once the
build's single version move lands.

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 · a git shim on PATH logging every `hash-object` call while `--status` grades a record of three briefs, one fresh, one edited and one gone, then the same with the shim failing `--stdin-paths`; staged by restoring the per-row `GIT hash-object` loop, which logs two calls where the arm wants one · `FLOOR_ASSERTIONS`, raised by the count of new assertions

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
`memory hygiene`, the lexicon and `check-spec-tokens.py --spec` over this file.

## 8. Open questions

- **F1 — Which mechanism answers R4: batch the brief hashing (A), or replay the last `--resume`
  output when its inputs have not moved (B)?** The roster's row 5 and the brief's item 5 name B,
  keyed on HEAD, the run-state file and the task registry. The measurements in §4 were taken after
  the roster was written.
  - **A, batch (this spec as written).** One `git hash-object --stdin-paths` call grades every
    brief. Every line stays byte-identical by construction. It also speeds `--status` and the
    take-over rows. On the 72-row fixture it removes about 15 s of a 24-34 s tick. It leaves startup <!-- DERIVED from §4's two hash rows -->
    and the rest of `verb_status`, about 5 s traced. <!-- PINNED 2026-11-14 -->
  - **B, replay.** As worded, B moves a verdict. The stop-guard appends a timed line at every turn
    end, and the status line prints its time. To keep every line, B must re-read that field live
    every tick and splice it into the replay. Its key must also cover far more than three inputs:
    - the working tree, for the build README, the brief files and the conf;
    - `AI_AGENT`, for the CLI-version line;
    - the resume-tick sidecar;
    - the lease clock's verdict, recomputed every tick;
    - a process ledger whose every line classifies `gone`, or orphans are possible.
    The key costs about 3 s to derive. After A, B would save at most the 5 s left in `verb_status`. <!-- PINNED 2026-11-14 -->
    B adds a sidecar record, a key and a splice.
  - **C, both.** C is B's cost on top of A's.

  Recommendation: A. It meets the README's speed outcome and its "No verdict moves" rule with the
  smallest diff, and B on top would save about 2 s per tick for a cache with the ceilings above. <!-- DERIVED from B's 5 s less its 3 s key, above -->
  Ruling for B or C rewrites §2 to §7 in a rev-2, and amends the README's roster row 5 and its
  expected-improvement line, which are the owner's.
  RESOLVED (owner, 2026-11-14): A, batch the brief hashing ("Batch hashing (Recommended)").

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft from the brief `2026-11-14-prompt-TOOL-aTrimmedWait-1-brief`,
  item 5, grounded at `846d51d3` and measured at `a25c84fc0` on node a. The trace showed the
  per-brief hash loop dominating a holder's tick, and the stop-guard's per-turn line made the
  roster's replay unable to keep the output as worded. The spec is written for the batch, and F1
  asks the owner to choose.
- rev-2 · 2026-11-14 · §8 F1 · F1 RESOLVED (owner) to A, batch hashing, by the ruling
  `2026-11-14-prompt-TOOL-aTrimmedWait-5-ruling`. Sections 2 to 7 stand as written.
- rev-3 · 2026-11-14 · §1 §4 §8 · each fact the writing-practice leg's pinned-facts arm named is pinned
  on its line, with no change of meaning, by `2026-11-14-prompt-TOOL-aTrimmedWait-5-writing-practice`.

## 10. Reuse audit

The seam this unit extends is the brief-staleness reader inside `verb_status`
(`tools/unattended/unattended.sh@95b8f8404cc3:8435-8455`), with git's own `--stdin-paths` batching in
place of a per-row process. The brief names `derive_spec_token_key`'s key-then-record pattern
(`tools/unattended/unattended.sh@95b8f8404cc3:14430-14436`) as R4's reuse. It is the seam option B
would extend, together with `tools/run-gates/gate-fingerprint.sh` and `resolve_sidecar_dir`, and
option A needs none of them. `python tools/codebase-map/reuse_lookup.py "hash many files in one git
call instead of one process per file"` ranked name stems only (`git`, `run_git`, `GIT`,
`read_git_output`), none of which batches a hash, so no existing seam fits beyond git's flag. Recall
returned `TOOL-dWellOiledMachine-54`, then the aGraftedHelix-1 spec's line that the holder's
`--resume` renews the claim every tick, which is why both options leave the claim block alone. It
also returned `TOOL-aWokenSentinel-5`'s resume-tick field and `TOOL-dMendedRecall-3`'s field table
naming `STALE briefs`. No record batches the reader.

Recall terms used: `python tools/memory-recall/query.py "why does the resume tick take so long and how does status hash each parked brief" --terms "resume tick holder status brief stale hash-object parked rows lease idle-wake cache verdict"`
