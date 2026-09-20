# TOOL-aWokenSentinel-13 — the resume tick sources the root conf before its bound reads, so a declared bound is honoured and the NOTE names the file

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 12b3701d · streams tooling · order 11 · ratified 2026-09-20

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H5 (round 1, raw ids 26 and 33): `read_bound_key` reads `${!_bk_name:-}` from
the CALLING shell and interpolates `$CONF` into its NOTE (`tools/unattended/unattended.sh:358` to
`:368`); the driver makes that work by `. "$CONF"` at `:341` before the calls. `TOOL-aWokenSentinel-5`
hoists the function into `lib-unattended.sh` and calls it from the tick, but sources each worktree's
`.unattended.conf` only in a subshell for `MEMORY_ROOT` and never says which conf is sourced into
the tick's own shell or that `CONF` is set — so as specced every tick takes 6 and 40, prints
`declares no RESUME_ATTEMPTS … Declare one in  to change it` with an empty path even where the
project declares the key, and spec 5 AC5's only NOTE arm is green for the wrong reason. This unit
states the read — the tick's two knobs are ROOT-scoped, sourced once from `$ROOT/.unattended.conf`
into the tick's shell with `CONF` set, before the two `read_bound_key` calls — and proves it with
arms under a declared key and a NOTE that names a non-empty path.

## 2. Scope (IN)

- **S1** — In `tools/unattended/resume-tick.sh`, directly after the root is resolved and before
  any `read_bound_key` call: `CONF="$ROOT/.unattended.conf"`; an absent file is `resume-tick:
  REFUSED — <root> carries no .unattended.conf, so the tick has no bounds to read`, exit 2; then
  `. "$CONF"` into the tick's own shell, so `RESUME_ATTEMPTS` and `RESUME_TURNS` resolve exactly
  as `GATE_BOUND` does in the driver. The knobs are ROOT-scoped: one repo, one pair of bounds,
  whatever worktree a run lives in. Spec 5 §4 is folded at its rev-2 to this read and cites this
  unit; unit 5 builds it at its own pass, and this unit's diff is the proof. Observed by AC1, AC2
  and AC3.
- **S2** — `MEMORY_ROOT` stays per-worktree and stays a subshell read, as spec 5 §4 has it: a
  worktree's memory root is that tree's fact, and sourcing a second conf into the tick's shell
  would let a worktree's declaration overwrite the root's bounds mid-walk. Observed by AC4.
- **S3** — The arms: `RESUME_ATTEMPTS="2"` declared in the fixture's conf with two post-move
  attempt lines seeded → `ATTEMPTS EXHAUSTED` and no NOTE; the conf declaring neither key → the
  NOTE, once per key, whose interpolated path is the fixture's conf and is non-empty; `RESUME_TURNS="7"`
  declared → the launcher carries `--max-turns 7`; each observed RED first against a tick copy
  with the `. "$CONF"` line removed. Observed by AC1, AC2 and AC3.
- **S4** — A NOTE naming no file is the signature of this defect and is greppable: one arm
  asserts every `Declare one in ` line on the tick's stderr is followed by a path that exists.
  Observed by AC2.

## 3. Non-goals (OUT)

- **No change to `read_bound_key`.** Its calling-shell contract is the driver's and the hoist
  keeps its bytes; this unit satisfies the contract from the tick as the driver does.
- **No per-worktree bounds.** A run in a worktree reads the root's `RESUME_ATTEMPTS`; a worktree
  conf that declares a different value is not read for these two keys, and the tick's header says
  so. The driver's own read is per-tree because the driver runs in one tree; the tick walks them
  all from one root and one pair of numbers is the only answer a scheduler can act on.
- **No `RESUME_STALE_BOUND` read.** That is `--liveness`'s number, read by the driver in the
  worktree it runs in, as spec 5 §4 states.
- **No hoist of the driver's conf-sourcing block.** It initialises thirty keys the tick does not
  read; the tick sources the file and reads two.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-5` — the tick, the hoisted `read_bound_key` in
  `lib-unattended.sh`, the fixture with its `mkconf`-shaped conf and the stub `claude`. Without the
  tick there is no read to fix.
- **consumes-from** external — the driver's own idiom at `tools/unattended/unattended.sh:341`,
  `. "$CONF"` before the bound reads, which this read copies.
- **hands-off** `TOOL-aWokenSentinel-6` — the one sentence in the conf comments for the two keys
  saying they are read from the ROOT conf by the tick, where unit 6 finds unit 5's one-liners
  wanting.

## 4. Design

### The read, in the tick

After `ROOT` is resolved (spec 5 §4 'The walk') and before the walk begins:

```
CONF="$ROOT/.unattended.conf"
[ -f "$CONF" ] || { echo "resume-tick: REFUSED — $ROOT carries no .unattended.conf, so the tick has no bounds to read" >&2; exit 2; }
# shellcheck disable=SC1090
. "$CONF"
read_bound_key RESUME_ATTEMPTS "$RESUME_ATTEMPTS_DEFAULT" attempts "…"
read_bound_key RESUME_TURNS "$RESUME_TURNS_DEFAULT" turns "…"
```

`read_bound_key` then reads `${!_bk_name:-}` from a shell that has sourced the file, prints its
NOTE with `$CONF` interpolated to a path that exists, and refuses a malformed value with exit 2
exactly as the driver does — the same function, the same contract, satisfied the same way. The
per-worktree `MEMORY_ROOT` subshell read in the walk is untouched: it reads one key from one
tree's conf and never sources into the tick's shell.

### Why root-scoped

The tick is one process walking every worktree of one repo from one `--repo` root. A per-worktree
bound would mean the same run could be capped at 6 in one tree and 2 in another, decided by which
tree's conf a branch happened to carry; and sourcing each worktree's conf into the tick's shell
would overwrite `RESUME_ATTEMPTS` mid-walk with whatever the previous tree declared. `.unattended.conf`
is a tracked file, so the root's copy is the merged answer, and it is the file an owner registering
the tick edits.

### The NOTE-path arm

The signature of the specced defect was `Declare one in  to change it` — two spaces, no file. One
arm greps the tick's stderr for `Declare one in ` and asserts what follows, up to ` to change it`,
is a path that exists. It is the liveness assertion for the read: a NOTE that names a file proves
`CONF` was set before the call.

### Inventory

No identifier is minted; `CONF` is the driver's own variable name, used by `read_bound_key`'s NOTE
and set here for the same reason.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/resume-tick.sh` | the four lines above, if unit 5's pass did not already build spec 5's rev-2 read; the header sentence on root scope |
| `tools/unattended/resume-tick.test.sh` | three arms: the declared cap, the two NOTEs with a non-empty path, the declared turns |

### Alternatives rejected

- **Source each worktree's conf in a subshell and print the two resolved values for the walk to
  consume.** Correct but per-worktree, which is the wrong scope for a scheduler's bounds, and it
  puts a `printf`-and-`read` protocol between the tick and a function that already sets globals.
- **Read the two keys with a bare `grep` over the conf.** A second reader with its own default,
  the class spec 5 §4 refuses for `RESUME_STALE_BOUND`.

## 5. Production-readiness checklist

- security — the tick sources a tracked conf from the repo it was registered for, the same file
  the driver sources on every verb; no new input.
- perf / scale — one `source` per tick.
- error / empty / loading states — no root conf refuses with exit 2 and the file named; no
  declaration takes the announced default; junk refuses with exit 2 through `read_bound_key`.
- observability — the NOTE names the file; the refusal names the root.
- risks — a worktree conf declaring a different bound is silently not read for these keys; the
  tick's header says so and the conf comment says so.
- testing — §6, three arms and the NOTE-path assertion.
- migration — N/A; both keys are optional and defaulted.
- user docs — the conf comment sentence, unit 6's; the tick's header.

## 6. Acceptance criteria

The fixture is spec 5 §6's scratch repo under a short `%TEMP%` path with its stub `claude`; the
staged break is a tick copy with the `. "$CONF"` line removed.

- **AC1** — When the fixture's conf declares `RESUME_ATTEMPTS="2"` and the sidecar is pre-seeded
  with two attempt lines dated after the fixture commit, `bash resume-tick.sh --repo <fixture>`
  prints `ATTEMPTS EXHAUSTED` and no `declares no RESUME_ATTEMPTS` line; against the staged break
  it launches attempt 3 and prints the NOTE.
  Red when: a declared cap is ignored, which is every tick reading the kit default.
- **AC2** — When the fixture's conf declares neither key, the tick's stderr carries `declares no
  RESUME_ATTEMPTS` and `declares no RESUME_TURNS` once each, and every `Declare one in ` on
  stderr is followed by a path that `test -f` accepts; with no `.unattended.conf` at the root the
  tick prints `REFUSED` naming the root and exits 2.
  Red when: the NOTE's path is empty, which is the specced defect's own signature; or a root with
  no conf walks on defaults silently.
- **AC3** — When the fixture's conf declares `RESUME_TURNS="7"`, the launcher file the tick writes
  carries `--max-turns 7` and `stub.log` shows the stub invoked with it.
  Red when: the launcher carries `40` under a declared `7`.
- **AC4** — When one worktree of the fixture carries a conf declaring `MEMORY_ROOT=mem2` and a
  bound record under `mem2/builds/`, and the root conf declares `RESUME_ATTEMPTS="2"`, the tick
  walks that tree's record under `mem2` and still caps it at 2; `grep -c 'RESUME_ATTEMPTS'` over
  that worktree's conf is 0, which is what makes the root's value the one observed.
  Red when: a worktree conf's absence of the key resets the cap to the default mid-walk, which is
  the second conf sourced into the tick's shell.
  fixture: `git worktree add` inside the scratch repo; the second conf written by the arm.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the tick over the
fixtures of AC1 to AC4.

New arm: `tools/unattended/resume-tick.test.sh` · the declared cap, the two NOTEs with a non-empty path, the declared turns and the two-worktree walk, each observed red against a tick copy with the source line removed · `FLOOR_ASSERTIONS` rises by the arms' executed assertions

## 8. Open questions

- **F1 — root-scoped bounds sourced once, or per-worktree bounds read in a subshell.** (a) Once
  from `$ROOT/.unattended.conf` into the tick's shell. (b) Per worktree, a subshell sourcing that
  tree's conf, setting `CONF`, running the two reads and printing the values for the walk.
  RESOLVED (agent, 2026-09-20, delegated): (a). The scheduler acts on one pair of numbers per
  repo; (b) makes the cap depend on which branch a worktree carries and needs a print-and-read
  protocol around a function that sets globals. Vetoes: no new surface, no governance carrier, no
  widened write; the run-state file names the mandate.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 1 as the
  promotion of H5 (raw ids 26, 33).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "source the project conf before reading a bound key in
a sibling script"` returned no seam and `unscanned layers: .sh`. The seam, read at source, is the
driver's own conf block: the empty initialisation at `tools/unattended/unattended.sh:336` to
`:339`, `. "$CONF"` at `:341`, and the two `read_bound_key` calls at `:369` and `:370` that the
sourcing makes work — the tick copies the sourcing and the calls and nothing else. The recall
probe's hits were `TOOL-aHoistedPass-40` (the kit gate's allow-list as a fourth spelling of the key
set, which does not bind a script that sources the conf directly), this build's audit at the H5
paragraph, and `TOOL-aCollapsedScan-11`; none records a bound read from an unsourced shell before
this one.

Recall terms used: `read_bound_key CONF sourced calling shell NOTE declares no default announced lib-unattended hoist tick`
