# TOOL-aWokenSentinel-3 — `stop-guard`, the `Stop` hook that refuses a bound session's turn end

**Status:** SPECCED · rev-2 · 2026-09-20 · node a · Tier-2 · base 5f9648d6 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md](../build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md) | research | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 |
| [2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md) | journal | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 |
| [2026-09-20-review-TOOL-aWokenSentinel-1-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-1-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 |

<!-- /gen:spec-records -->

## 1. Goal

Refuse the act where it is committed: `stop-guard.js`, a `Stop` hook in the unattended kit, sees
the decision to end the turn and, when the stopping session holds a non-terminal unattended run,
continues the conversation with the absent-owner instruction instead. Four of six recorded stalls
are class E — the run parked and ended its turn to wait for an owner who had left — and nothing
today sees that act. The hook is bounded per session, writes every decision on a bound session to
a sidecar under the git dir, and records the harness's own cron listing verbatim, which is what
unit 7 checks `keepalive-reaped` against.

## 2. Scope (IN)

- **S1** — the hook, `stop-guard.js`, in the unattended kit: read stdin, bind the `session_id` to
  a run-state record whose `session:` fact equals it, and exit 0 silently with zero writes when no
  record does. Every other session on the node pays one scan of the build folders and nothing
  else. Observed by AC1, AC9.
- **S2** — the decision on a bound session, in this order: liveness verdict `TERMINAL` allows;
  a non-empty `background_tasks` allows; a block count for this session at or above
  `STOP_GUARD_BLOCKS` allows; everything else blocks with the §4 reason. An unreadable liveness
  allows and says so. The `FINISHED-UNSTAMPED` row is PROVISIONAL at this order — it allows here
  and is replaced one order later by `TOOL-aWokenSentinel-8`'s `landing-unstamped` BLOCK, which
  owns that row and its arm; this unit does not observe it. Observed by AC2, AC3, AC4, AC5, AC6,
  AC7.
- **S3** — the sidecar: every stop on a bound session, allowed or blocked, appends ONE compact
  JSON line to `stop.<slug>.log` under `<git-dir>/unattended/`, carrying `session_crons` verbatim
  as the harness handed them. The block count is derived from that file and from nothing else.
  Observed by AC2, AC5, AC8, AC10.
- **S4** — the sibling module `run-lease.js`: the repo walk that returns the per-worktree git dir,
  the conf-line reader, the lease scan, the sidecar path derivation and the append. Required by
  `__dirname` from this hook and from unit 4's. Observed by AC10, AC11.
- **S5** — the knob `STOP_GUARD_BLOCKS`, read by the hook from `.unattended.conf` with the kit
  default 6 — below the harness's own cap of 8 consecutive blocks, pinned in the hook as
  `HARNESS_CONSECUTIVE_CAP` with the record that measured it — announced on stderr when the
  project declares none. Its DECLARATIONS — the shipped example, `optional_keys`, the protocol's
  section 8 row and the root conf — are `TOOL-aWokenSentinel-10`'s, two orders later. Observed by
  AC6, AC7 and AC18.
- **S6** — the fragment `stop-guard.fragment.json` on event `Stop` with matcher `*`, wired into
  `.claude/settings.json` by `tools/settings-merge.py --fragment` in the same commit, and
  `tools/unattended/kit.toml` carrying the suite in its `project-owned` list. Observed by AC12,
  AC13 and AC18.
- **S7** — the adopter's `--check` wiring arm generalised from one named fragment to every
  `*.fragment.json` the kit dir ships, refusing on zero fragments and on a fragment whose marker
  names a hook the kit dir does not carry, and printing the count it checked; its suite's seed
  copies every fragment and hook and writes an entry per fragment. Observed by AC14, AC15.
- **S8** — the suite, the budget row, the carried-prefix registry raise, and the symbols
  artifact regenerated. Observed by AC11, AC16, AC17.

## 3. Non-goals (OUT)

- **No sub-agent coverage.** `Stop` fires for the main agent only; a sub-agent's end fires
  `SubagentStop` under the parent's `session_id`. This hook does not register for that event and
  exits silently on a payload carrying `agent_id`, so a Workflow or Agent child is never trapped
  here. Measured in the research record, section 6.
- **No liveness of its own.** The hook asks `unattended.sh --liveness <slug>` beside itself and
  reads `verdict:` and `phase:` from its output. It does not read mtimes, transcripts or `git`.
- **No prose carriers.** The kit README, the Skill template and its render, the protocol's
  section 5 and the map dossier are unit 6's, which restates every earlier unit's vocabulary in
  one commit. The knob's four declarations, the protocol's section 8 row among them, are unit
  10's. This unit's documentation is the hook's own header, which states what it does and does not
  check — including what the HARNESS bounds versus what the hook bounds: the harness ends a turn
  after 8 consecutive stop-hook blocks (`memory/builds/aReplayedCard/build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md:299`,
  verdicts 8 and 22 against the hooks documentation), so inside one turn no knob above 8 is
  reachable; the hook's count persists in the sidecar across resumes, so its cap bounds the
  session's lifetime blocks, and the default sits below 8 so the hook's ANNOUNCED exhaustion
  precedes the harness's silent one.
- **No version bump.** The kit steps from 1.24 to 1.25 once, at the close, across every carrier
  `bash tools/check-kit-versions.sh` names. The hook's header carries the courtesy marker at the
  value read from the driver at dispatch.
- **No `tools/check-wiring.sh` arm.** The adopter's `--check` and the hook-destinations gate cover
  the wiring; a check-wiring arm for this kit's fragments is `TOOL-aDeferredBar-7`, OPEN.
- **No rewiring of `gate-guard.js`** onto the new module; §8 F2.
- **No `--resume` and no scheduling.** The hook refuses a stop; unit 5 resumes a dead one.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-1` — the `session:` fact in the run-state file's
  `## Run facts` region, written by `--preflight` and by `--resume --keepalive-id`. Without it no
  record binds and the hook allows every stop silently, which is today's behaviour.
- **consumes-from** `TOOL-aWokenSentinel-2` — `--liveness <slug>`, its `verdict:` and `phase:`
  lines and the verdict vocabulary `TERMINAL`, `FINISHED-UNSTAMPED`, `UNBOUND`, `STALE`, `LIVE`.
  Without it every bound stop reads `liveness-unreadable` and allows.
- **consumes-from** `TOOL-aWokenSentinel-14` — `seed()` in `adopt-unattended.test.sh` committing
  once, so the real-driver fixture of AC11 has a born HEAD and the driver's `git log` clock probe
  is live; without it `--liveness` refuses with check 52 and AC11 can never block.
- **hands-off** `TOOL-aWokenSentinel-8` — the `FINISHED-UNSTAMPED` row of the decision table,
  provisional here, and its arm.
- **hands-off** `TOOL-aWokenSentinel-10` — the knob's declarations: the example line, the
  `optional_keys` entry, the protocol's section 8 row with its render, and the root conf line
  with its rationale and the manifest re-stamp.
- **hands-off** `TOOL-aWokenSentinel-4` — `run-lease.js` as the shared binder, the adopter's
  generalised fragment loop, and the seed that copies every fragment; unit 4 adds its own
  fragment and hook and asserts the loop found them.
- **hands-off** `TOOL-aWokenSentinel-6` — every prose carrier named under §3 and the version
  step; the root conf's `STOP_GUARD_BLOCKS` line is unit 10's, not unit 6's.
- **hands-off** `TOOL-aWokenSentinel-7` — the `session_crons` field of the last stop line, which
  `--landed` reads against the recorded keepalive id.
- **hands-off** external — a `check-wiring.sh` arm for this kit's fragments
  (`TOOL-aDeferredBar-7`); moving `gate-guard.js` onto `run-lease.js` (§8 F2), a backlog row at
  landing.

## 4. Design

### The order of work inside the hook

```
stdin JSON -> hook_event_name is "Stop" and no agent_id  -> else exit 0, nothing written
  -> resolveRepo(cwd)             {root, gitDir} from the .git walk; a worktree's .git FILE
                                  points at the per-worktree git dir; no .git: exit 0
  -> readMemoryRoot(root)         .unattended.conf beside .git, key MEMORY_ROOT, default memory
  -> resolveLease(root, memoryRoot, session_id)
                                  the record under builds/*/RUN.md whose session: fact equals
                                  session_id; absent or no match: exit 0, nothing written
  -> runLiveness(kitDir, root, slug)
                                  bash <kitDir>/unattended.sh --liveness <slug>, cwd root,
                                  bounded at 60 s; verdict: and phase: parsed, else unreadable
  -> readBoundKey(root, STOP_GUARD_BLOCKS, 6)
  -> measureBlocks(sidecar, session_id)
                                  lines of stop.<slug>.log with this session and decision block
  -> checkStop(...)               the §4 table: {decision, reason}
  -> writeSidecarLine(sidecar, line)
  -> block: {"decision":"block","reason":<text>} on stdout, exit 0; allow: nothing, exit 0
```

`cwd` is the payload's own field, `CLAUDE_PROJECT_DIR` the fallback, `process.cwd()` the last.
The walk follows `gate-guard.js`'s `resolveRepoRoot` except that it RETURNS the git dir and does
not require `HEAD` to name a branch: the key here is the session, never the branch, and the git
dir is where the sidecar lives. In a linked worktree `.git` is a file holding `gitdir: <path>` and
that path is the per-worktree git dir, where `gate-logs/` already sits; the common dir is never
used, because a run lives in one worktree.

The driver path is `path.join(__dirname, 'unattended.sh')` with backslashes folded to `/`,
spawned as `bash <driver> --liveness <slug>` with `cwd` at the root, because the driver sources
the conf of the tree it runs in and MSYS mangles a backslash path handed to a shell (charter §11).
No path outside the kit dir is spelled: the conf basename, the conf keys, the record basename and
the sidecar names are the only literals, and the kit dir is `__dirname`.

### The key

The record is the one under `<root>/<MEMORY_ROOT>/builds/<slug>/RUN.md` whose `## Run facts`
region carries `session: <uuid>` equal to the payload's `session_id`. The literal `absent` never
matches. A record with no `session:` fact keys nothing, so every run preflighted before unit 1
landed — every record in this tree today, this build's own included — is invisible to the hook
until a `--resume --keepalive-id` re-records its lease. The hook therefore lands DARK for the run
that builds it, which is the §1 landing rule's shape rather than an accident.

Two records claiming one session cannot happen from the driver, which writes the fact from one
`CLAUDE_CODE_SESSION_ID`; if a hand-edited tree produces two, the hook reads them all and blocks if
any is open, naming the first, the way `gate-guard.js` handles two records on one branch.

### The decision

| verdict from `--liveness` | `background_tasks` | blocks so far | decision | reason class |
|---|---|---|---|---|
| `TERMINAL` | any | any | allow | `terminal` |
| `FINISHED-UNSTAMPED` | any | any | allow — PROVISIONAL at this order; `TOOL-aWokenSentinel-8` replaces it with a bounded BLOCK, `landing-unstamped`, and owns its arm | `finished-unstamped` |
| `LIVE`, `STALE` or `UNBOUND` | non-empty | any | allow | `background-tasks` |
| `LIVE`, `STALE` or `UNBOUND` | empty or absent | at or above `STOP_GUARD_BLOCKS` | allow | `blocks-exhausted` |
| `LIVE`, `STALE` or `UNBOUND` | empty or absent | below | BLOCK | `run-open` |
| no `verdict:` line, non-zero exit, or the 60 s bound | any | any | allow | `liveness-unreadable` |

`UNBOUND` is listed for completeness: `--liveness` prints it when the record's `session:` is
`absent`, and a record this hook matched by session is not absent, so the row is reachable only
when two readers disagree, and then the hook's own read governs because it is the one that bound.
`background_tasks` allows because the harness re-invokes the session when a task completes and a
blocked stop there is a wasted turn. `stop_hook_active` is honoured the way the docs ask: it is
true on every continuation and changes nothing but the reason text, which says so.

A malformed `STOP_GUARD_BLOCKS` — declared and not a positive integer — ALLOWS with reason class
`knob-malformed` and one stderr line, never a refusal. The driver's `read_bound_key`
(`unattended.sh:358`) exits 2 on the same input, and for a verb that is the right answer; for a
`Stop` hook exit 2 is a BLOCK, so the driver's refusal shape would turn a typo in a conf into a
session that cannot end its turn. §8 F4.

### The block reason

Printed as the `reason` string of `{"decision":"block","reason":…}` on stdout with exit 0, the
shape measured in the research record's section 6, which reaches the model headed
`Stop hook feedback:`.

```
stop-guard: this session holds unattended run <slug>, phase <phase>, liveness <verdict>;
block <n>/<N>. The owner is absent. Run `bash <kit-rel>/unattended.sh --plan <slug>` and build
the next READY unit, or `bash <kit-rel>/unattended.sh --abort <slug> --reason <text>
--code <halt-code>` if the run cannot proceed. Never end the turn by asking: there is nobody
to answer, and a question is a stall.
```

One trailing sentence when `stop_hook_active` is true: `This is a continuation the hook already
blocked once.` `<kit-rel>` is the kit dir relative to the root, derived from `__dirname` and the
walk, never spelled; `<n>` counts this block; `<N>` is the resolved knob.

### The sidecar line

`<git-dir>/unattended/stop.<slug>.log`, created with its directory on first write, append-only,
never tracked, one compact JSON object per line, keys in this order:

| key | value |
|---|---|
| `utc` | an ISO-8601 UTC stamp at second precision, `2026-09-16T12:00:05Z`, the spelling the driver's `--park` writes into the Parked region |
| `session` | the payload's `session_id` |
| `decision` | `allow` or `block` |
| `reason` | one of the six reason classes above, or `knob-malformed` |
| `phase` | the `phase:` line from `--liveness`, or `unknown` when unreadable |
| `verdict` | the `verdict:` line, or `unreadable` |
| `blocks` | blocks for this session INCLUDING this line when it is a block |
| `background_tasks` | the array's length, 0 when absent |
| `stop_hook_active` | the payload's boolean, false when absent |
| `session_crons` | the payload's value VERBATIM — any JSON value, `null` when absent |

The last key is unit 7's evidence and is copied without inspection: the harness's own listing of
the cron store no script can reach. The block count is `measureBlocks`: the lines of this file
whose `session` equals the payload's and whose `decision` is `block`. There is no second counter.
An unwritable sidecar allows with `sidecar-unwritable` on stderr and writes nothing, because a
bound the hook cannot derive is a bound it cannot enforce, and a hook that blocks without one
loops.

### The knob

`STOP_GUARD_BLOCKS`, read from `.unattended.conf` beside `.git` by `readBoundKey`, which reads the
line the way `gate-guard.js` reads `MEMORY_ROOT` — a trailing comment stripped, quotes stripped,
an `export` prefix admitted — and applies the driver's rule: absent takes the kit default 6 and
prints `unattended: NOTE - this project declares no STOP_GUARD_BLOCKS, so a bound session is
blocked at most 6 times per run and session. Declare one in .unattended.conf to change it.` on
stderr; a declared value that is not a positive integer takes the `knob-malformed` row. Six is
PINNED as `BLOCKS_DEFAULT`, and the reason is the harness: it ends a turn after 8 consecutive
stop-hook blocks, recorded at
`memory/builds/aReplayedCard/build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md:299`
and pinned in the hook as `HARNESS_CONSECUTIVE_CAP = 8` with that record cited beside it, so a
default above 8 promises blocks a single turn can never deliver and the `blocks-exhausted` row is
unreachable until a resume. Six leaves two blocks of headroom under the harness's cap, so the
hook's announced exhaustion — a sidecar line and a reason naming `--abort` — precedes the
harness's silent turn end; because the count persists in the sidecar, the cap still bounds a
session that is resumed and blocked again. The hook's header states the two bounds side by side,
and one arm asserts `BLOCKS_DEFAULT <= HARNESS_CONSECUTIVE_CAP`. The key's DECLARATIONS —
`optional_keys` in `tools/unattended/kit.toml`, the shipped `.unattended.conf.example` line, the
protocol's section 8 row and this repo's root `.unattended.conf` line with its rationale and the
manifest re-stamp that edit owes — are `TOOL-aWokenSentinel-10`'s, one commit two orders later
(§8 F3 as amended at rev-2). Until then the hook's announced default is what this repo runs on.

### The fragment and the wiring

```json
{ "name": "stop-guard", "event": "Stop", "matcher": "*",
  "marker": "stop-guard.js", "hook_path": "{kit}/unattended/stop-guard.js" }
```

The brief said "no matcher" and to extend the readers if they refused one. They refuse:
`tools/settings-merge.py`'s `load_fragment` requires every key in `_FRAGMENT_KEYS` to be a
non-empty string,
`adopt-unattended.sh:393` refuses an empty matcher by name, and `tools/check-hook-destinations.sh`
resolves a fragment through `settings-merge.py --resolve-fragment`, which calls the same loader.
Three readers to extend for one hook. The harness documentation, fetched 2026-09-16, states in its
matcher table that `"*"`, `""` or omitted are each `Match all`, and that `Stop` has no matcher
support and always fires. So the fragment declares `*`, every reader accepts it unchanged, and the
rendered group is `{"matcher":"*","hooks":[…]}` under a new `Stop` key. §8 F1.

`python tools/settings-merge.py --fragment tools/unattended/stop-guard.fragment.json` writes the
entry; `.claude/settings.json` is part of the commit and is the LAST write of the pass, because a
wired `Stop` hook is live for every later session in this tree. `{kit}` resolves against the
fragment's own location two directories up, as `check-hook-destinations.sh` and `settings-merge.py`
both read it, and the `**` engine rule ships the hook, the module and the fragment.

### The adopter's fragment loop

`adopt-unattended.sh`'s `--check` asserts ONE fragment by name at its sixth artifact (`GG_FRAG`,
lines 379 to 428 at base). Generalised: enumerate `"$KIT_DIR"/*.fragment.json`; ZERO is a refusal
naming the kit dir, because a copy that lost every fragment is a broken copy and a loop over
nothing is the green-by-absence shape; for each, read `name`, `marker`, `event` and `matcher`,
refuse when any is empty, refuse when `$KIT_DIR/<marker>` is not a file (a fragment naming a hook
the kit does not carry), then run the existing awk group reader once per fragment over the
settings file resolved once. UNWIRED names the fragment's `name` and the remedy names its file,
the way the current message does, so the adopter suite's existing `gate-guard hook is UNWIRED`
assertions keep their text. The final line prints `hooks: <n> fragment(s) wired`, the count the
loop derived. A fragment deleted from a copy that still holds another is not detected by this loop
and is stated in the arm's comment: the old per-name check saw one file, the new one sees the
population, and the population floor is the zero guard (§8 F5).

The suite's `seed()` copies `"$HERE"/*.fragment.json` and `"$HERE"/*.js` beside the driver and
writes a settings entry per fragment under its event and matcher. Measured 2026-09-16 on a fixture
built by that function extracted verbatim: `--check` exits 1 with `gate-guard.fragment.json is
missing from the kit`, because the seed reads the fragment's marker out of `$HERE` and never copies
the file, so arm 1 of `adopt-unattended.test.sh` is RED at base 5f9648d6 and the fixture-gone arm
of 1a moves a file that is not there. The seed change closes both. Arm 1a's absent-fragment arm
becomes "every fragment gone", and a new arm writes a fixture fragment `fx.fragment.json` naming
`fx.js` beside it, asserts UNWIRED naming `fx`, wires it, asserts green, then deletes `fx.js` and
asserts the hook-missing refusal.

### The fixture and the direct observation

Every §6 hook observation feeds one payload on stdin to a COPY of the hook: `KIT` is a scratch
directory under the run's scratchpad holding `stop-guard.js`, `run-lease.js` and a stub
`unattended.sh` that prints the file `$STOP_GUARD_TEST_LIVENESS` names on `--liveness`, exits
with `$STOP_GUARD_TEST_LIVENESS_RC`, and sleeps `$STOP_GUARD_TEST_LIVENESS_SLEEP` seconds first
when that is set; `FIX` is a scratch tree holding `.git/HEAD`, a `.unattended.conf` and one
`memory/builds/fx/RUN.md` with a `## Run facts` region; `P` is the payload built by python, never
hand-spliced, with `cwd` resolved through `cygpath -m`. The stub is what makes the predicate
observable in milliseconds without the driver's startup, and it is what the suite runs. ONE
integration arm uses a real `git init` fixture seeded the way `adopt-unattended.test.sh`'s
`seed()` builds one — which, from `TOOL-aWokenSentinel-14` at order 4, commits once, so HEAD is
born and the driver's `git log -1 --format=%ct` probe is live rather than the check-52 dead-probe
refusal an unborn HEAD triggers — and the REAL driver copied beside the hook, so the spawn, the
`cwd` and the `verdict:` parse are exercised once against unit 2's verb. The liveness bound
`LIVENESS_BOUND_MS` is overridable by the environment variable `STOP_GUARD_LIVENESS_BOUND_MS`,
which is the fixture's seam: a stub that sleeps longer than a bound of a few hundred
milliseconds observes `liveness-unreadable` in seconds instead of sixty. The suite prints
`PASS (<n> assertions)` against a derived `FLOOR_ASSERTIONS`, the shape of `gate-guard.test.sh`,
and every arm is observed RED first on the break it names.

### Inventory

Cell `js.function camel` from `.lexicon.conf`, verbs from its table. In `run-lease.js`:
`readStdin`, `resolveRepo`, `readConfValue`, `readMemoryRoot`, `readBoundKey`, `scanLeases`,
`resolveLease`, `deriveSidecarPath`, `writeSidecarLine`, `readSidecarLines`, `renderUtc`. In
`stop-guard.js`: `runLiveness`, `parseLiveness`, `measureBlocks`, `checkStop`, `renderBlock`,
`main`. Constants `KIT_STOP_GUARD_VERSION`, `BLOCKS_DEFAULT`, `HARNESS_CONSECUTIVE_CAP`,
`LIVENESS_BOUND_MS`, `REASONS`. All
exported, `main` guarded by `require.main === module`, so a `require` from the suite or from unit
4 reads no stdin. Cell `sh.function snake`: none minted; the adopter's loop is inline in the
`--check` branch, which deliberately defines no `fail()` (its line 14).

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/stop-guard.js` | new, the hook; header states what it checks and does not; requires `./run-lease.js` |
| `tools/unattended/run-lease.js` | new, the shared binder and sidecar writer; no `tools/` literal, basenames and conf keys only |
| `tools/unattended/stop-guard.fragment.json` | new, the §4 shape, event `Stop`, matcher `*` |
| `tools/unattended/stop-guard.test.sh` | new, the withheld suite; stub driver arms plus one real-driver arm; `FLOOR_ASSERTIONS` derived at first green |
| `.claude/settings.json` | one `Stop` group appended by the merger, never by hand; the last write of the pass |
| `tools/unattended/adopt-unattended.sh` | the sixth artifact becomes the fragment loop of §4, same awk reader, same message shapes |
| `tools/unattended/adopt-unattended.test.sh` | `seed()` copies every fragment and hook and writes an entry per fragment; arm 1a's fragment-gone arm reads every fragment gone; the `fx` arm; observed RED first on the adopter at base |
| `tools/unattended/kit.toml` | `stop-guard.test.sh` joins the `project-owned` include list; the `optional_keys` entry is unit 10's |
| `tools/run-gates/selftest-budgets.txt` | one row, budget from the measured first green times 1.5 floored at 60 s, so `run-selftests.sh --kit tools/unattended` enumerates it |
| `tools/install-prefix-carried.txt` | the `selftest-budgets.txt` row raised by ONE by hand with its reason, from whatever value it holds at dispatch (15 at base); a hand-written row for the suite if `bash tools/check-install-prefix.sh` reports its literals, with the reason the gate-guard row carries |
| `memory/map/generated/symbols.json` | re-rendered by `python tools/codebase-map/gen_map.py --write` in the same commit: the `kit-js` layer indexes every kit `.js`, so two new files move it |

### Alternatives rejected

- **An empty matcher and three reader extensions.** `*` is documented as the same thing and costs
  no reader a line; §8 F1.
- **Require `gate-guard.js`'s walk from `run-lease.js`.** It returns no git dir and refuses a
  detached `HEAD`, both wrong for a session key; a fresh `resolveRepo` costs twenty lines and
  leaves a landed hook and its 124-assertion suite untouched; §8 F2.
- **Read the knob through the driver.** `--liveness` is unit 2's contract and is being specced
  concurrently; a second reader of one conf line in the hook is the same class `gate-guard.js`
  already carries, and it stays inside the kit.
- **Exit 2 with the reason on stderr.** Documented as a block too, but the JSON shape is the one
  the research measured delivering the reason under `Stop hook feedback:`.
- **Block on a pending background task.** The harness re-invokes the session when it completes;
  a block there spends a turn to arrive where the harness was going.
- **A counter file per session.** The sidecar already holds every block; a second counter is the
  two-answers-to-one-question class.

## 5. Production-readiness checklist

- security — the hook reads the tree, spawns the driver beside itself, and appends to a file under
  the git dir. It runs for every session on the node with this repo open, so the unbound path is
  the one that matters: one directory listing, one small read per build folder, no spawn.
- perf / scale — unbound: milliseconds, 51 record reads in this tree today (PINNED 2026-09-16;
  DERIVED by the scan). Bound: one driver spawn bounded at 60 s, once per stop of one session.
- error / empty / loading states — four outcomes: silent exit 0 when unbound or unparseable; allow
  with a sidecar line; block with a sidecar line and the JSON; allow with a stderr line when the
  liveness, the knob or the sidecar cannot be read. A broken hook never blocks a stop.
- observability — every bound stop is a line naming the decision, its class, the phase, the
  verdict and the count; the reason text names the slug, the count and the two verbs to run.
- risks — a run whose stop is blocked N times and still cannot proceed spends N turns; the bound is
  the cost ceiling and `--abort` is the documented exit. A `Stop` hook blocking a session the owner
  is driving by hand: bound only through a `session:` fact, which the owner's session carries only
  if it preflighted or resumed the run. A stale `session:` after process death: the pid is dead and
  the new session has another id, so the old id binds nothing until unit 1's re-record.
- testing — the pass observes each arm by feeding the copied hook a payload against the stub
  driver, in milliseconds, and one arm against the real driver on a git fixture; the suite re-runs
  the same payloads at the close.
- migration — additive: a new event key in the settings file, a new optional conf key with a
  default, a new module nothing else requires yet. An adopter on kit 1.24 keeps working.
- user docs — none here; unit 6 owns every prose carrier (§3).

## 6. Acceptance criteria

`KIT`, `FIX` and `P` are the §4 fixture paragraph's; `HOOK` is the copied hook under `KIT`. Each
observation is one payload fed to the hook, or one direct checker, in seconds. The suite is not an
observation here: it runs at the close.

- **AC1** — When `P` carries a `session_id` no record under `FIX` names, `printf '%s' "$P" |
  node "$HOOK"; echo "rc=$?"` prints `rc=0`, stdout is empty, and no file exists under the
  fixture's git dir at the sidecar path. Observed RED before the hook file exists, where `node`
  reports the module missing and the code is not 0.
  Red when: a record at BUILDING with `session: absent` binds, or a sidecar file appears.
- **AC2** — When `FIX`'s record carries `session:` equal to `P`'s and the stub's liveness file
  holds `phase: BUILDING` and `verdict: LIVE`, the same invocation prints `rc=0`, stdout is one
  JSON object with `decision` equal to `block` and a `reason` naming the slug, `block 1/12` and
  `--plan`, and the sidecar holds one line whose `decision` is `block` and `blocks` is 1, parsed
  with `python -c 'import json,sys;…'`, never by grep over the raw bytes; the reason reads
  `block 1/6`.
  Red when: the hook exits 0 with empty stdout on an open run, or the line is not written.
- **AC3** — When the liveness file holds `verdict: TERMINAL`, the invocation prints `rc=0` with
  empty stdout and the sidecar's new line carries `decision` `allow` and `reason` `terminal`. The
  `FINISHED-UNSTAMPED` verdict is not observed here: its row is provisional at this order and
  `TOOL-aWokenSentinel-8` owns it and its arm.
  Red when: a terminal run is blocked, or the allow writes no line.
- **AC4** — When `P` carries a non-empty `background_tasks` array and the liveness is `LIVE`, the
  invocation allows and the line's `reason` is `background-tasks` with `background_tasks` equal to
  the array's length.
  Red when: the run is blocked while a task is pending.
- **AC5** — When the sidecar is pre-seeded with two block lines for this session and `FIX`'s conf
  declares `STOP_GUARD_BLOCKS="2"`, the invocation allows with `reason` `blocks-exhausted`; with
  one seeded line it blocks with `block 2/2` in the reason. The count is read from the file: a
  seeded line for ANOTHER session is not counted, observed by a third payload.
  Red when: the third stop is blocked, or another session's lines move this session's count.
- **AC6** — When `FIX`'s conf declares no `STOP_GUARD_BLOCKS`, stderr carries `declares no
  STOP_GUARD_BLOCKS` exactly once and the block reason reads `1/6`; when it declares
  `STOP_GUARD_BLOCKS="zero"`, the invocation allows with `reason` `knob-malformed` and `rc=0`.
  figure: 6 is PINNED in the hook as `BLOCKS_DEFAULT`; the criterion reads it from the reason.
  Red when: a malformed knob exits 2, which the harness reads as a block.
- **AC7** — When the stub exits 1, and separately prints no `verdict:` line, the invocation allows
  with `reason` `liveness-unreadable` and `verdict` `unreadable` in the line, and `rc=0`.
  Red when: an unreadable liveness blocks, or the hook exits non-zero.
- **AC8** — When `P` carries `session_crons` as a two-element array of objects and
  `stop_hook_active` true, the sidecar line's `session_crons` deep-equals the payload's under
  `python -c 'import json…'` and the block reason ends with the continuation sentence.
  Red when: the field is summarised, reordered or dropped, or the sentence is absent.
- **AC9** — When `P` carries `agent_id`, and separately `hook_event_name` equal to
  `SubagentStop`, the invocation prints `rc=0`, empty stdout, and writes nothing; and
  `grep -c '"event": "Stop"'` over the fragment prints 1 while `grep -c SubagentStop` prints 0.
  Red when: a sub-agent-shaped payload binds and blocks.
- **AC10** — When `FIX`'s `.git` is a FILE holding `gitdir: <path>` naming a directory, the
  sidecar line lands under that directory's `unattended/` and not beside the file; a `find` over
  the fixture prints exactly one `stop.fx.log`.
  Red when: the line is written under the wrong git dir or twice.
- **AC11** — When the real driver is copied beside the hook in a `git init` fixture whose record
  is at BUILDING with `session:` equal to `P`'s, the invocation blocks and the line's `verdict` is
  what the copied driver's own `--liveness fx` prints on its `verdict:` line, run from the same
  fixture by the arm, never a literal.
  fixture: a `git init` tree seeded by the adopter suite's `seed()`, which commits once from unit
  14 so HEAD is born and the driver's `git log` probe is live, built by the pass under a short
  `%TEMP%` path; the driver needs unit 2's verb, which is landed by order.
  cost: the driver's startup, seconds, once.
  Red when: the spawn fails on the fixture's path spelling, or the parse reads no verdict.
- **AC12** — When `python tools/settings-merge.py --fragment` has run with the stop-guard
  fragment as its argument, `python -c` over `.claude/settings.json` prints one group under `Stop`
  whose `matcher` is `*` and whose one command ends with the hook's basename, and a second run
  leaves the file byte-identical.
  Red when: the merger refuses the fragment, or a second run appends a second entry.
- **AC13** — When `bash tools/check-hook-destinations.sh` runs after the fragment lands, it prints
  its clean line and `rc=0`, and its fragment count is one higher than at base. Observed RED first
  by pointing the fragment's `hook_path` at a basename the kit does not ship.
  cost: 75 s measured on node a 2026-09-15, from the gate ledger.
  figure: the count is DERIVED by the gate; base's value is read from its output, not typed here.
  Red when: the resolvers disagree on `{kit}`, or the destination is not shipped.
- **AC14** — When `bash tools/unattended/adopt-unattended.sh --check` runs in this tree with the
  fragment wired, it prints `hooks: 2 fragment(s) wired` and `in sync`, `rc=0`; with the `Stop`
  group removed from a copy of the settings file declared through `GOV_SETTINGS_JSON`, it prints
  `the stop-guard hook is UNWIRED` with a remedy naming that file, `rc=1`.
  cost: 12 s measured on node a 2026-09-15.
  figure: 2 is DERIVED by the loop and equals the kit's fragment count at this order.
  Red when: the loop reports the gate-guard entry alone as `in sync`.
- **AC15** — When the seeded fixture of the adopter suite is built by its `seed()` and `--check`
  runs inside it, `rc=0` where the same fixture at base printed `gate-guard.fragment.json is
  missing from the kit` with `rc=1`; when every `*.fragment.json` is moved out of the fixture's
  kit dir, `--check` refuses naming the kit dir; when `fx.fragment.json` naming `fx.js` is written
  beside them, `--check` prints `the fx hook is UNWIRED`, and after the merger wires it, `rc=0`;
  with `fx.js` deleted, `--check` refuses naming the missing hook.
  fixture: the suite's own `seed()`, run by hand as one function; the pass runs the suite's arms
  as commands, never the suite.
  Red when: the seeded fixture still refuses at base's line, or a fixture fragment ships unwired.
- **AC16** — When `python tools/codebase-map/gen_map.py --check` runs after the regen,
  `rc=0`; before the regen with the two new files present it prints the drift and `rc=1`, which is
  the RED observed first.
  Red when: the `kit-js` layer does not index the new files, so the check cannot move.
- **AC17** — When `python tools/lexicon/lexicon.py` runs, its `js.function` row reports no new
  offender, every name in the §4 inventory leading with a table verb; `bash
  tools/check-install-prefix.sh` reports `tools/run-gates/selftest-budgets.txt` at its raised
  count and no unlisted literal in the kit dir.
  cost: 6 s and 83 s measured on node a 2026-09-15.
  Red when: a function leads with a verb the table does not hold, or a budget row lands without
  its raise.
- **AC18** — When `grep -c 'stop-guard.test.sh' tools/unattended/kit.toml` runs it prints 1 and 0
  at base — the `project-owned` list — and a `node -e` read of the copied hook's exports prints
  `BLOCKS_DEFAULT` less than or equal to `HARNESS_CONSECUTIVE_CAP` and the latter equal to 8.
  figure: 8 is PINNED from the aReplayedCard record cited in §4; 6 is PINNED as `BLOCKS_DEFAULT`.
  Red when: the suite ships to every `govkit apply` adopter because the descriptor does not
  withhold it; or the default rises above the harness cap, which promises blocks a turn cannot
  deliver.
- **AC19** — When the fixture's sidecar directory `<git-dir>/unattended` is made a FILE, the
  invocation on an open run allows, `rc=0`, stderr carries `sidecar-unwritable`, and nothing is
  written; and when the stub sleeps 3 s under `STOP_GUARD_LIVENESS_BOUND_MS=500`, the invocation
  allows with `reason` `liveness-unreadable` within 2 s, `rc=0`.
  Red when: an unwritable sidecar blocks, which loops a session on a bound the hook cannot
  derive; or a hung liveness blocks every stop for sixty seconds and then some, which is the
  bound not wired.

## 7. Gates

`unattended skill wiring` · `hook destinations (every declared hook path ships)` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `govkit selfcheck` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The pass runs none of these. It verifies with the direct checks §6 names — the copied hook fed
one payload, the merger, the hook-destinations gate, the adopter's `--check`, the map's `--check`
— and the bar runs once at the close.

New arm: tools/unattended/stop-guard.test.sh · a fixture record bound to the payload's session against a stub driver, one arm per §6 payload, the unwritable-sidecar and sleeping-stub arms of AC19, the cap-under-harness arm of AC18, one arm against the real driver on a git fixture; the break is the hook absent, then each row of the §4 table negated · `FLOOR_ASSERTIONS` derived at the suite's first green, none moved

New arm: tools/unattended/adopt-unattended.test.sh · `seed()` copies every fragment and hook; arm 1a's fragment-gone arm reads every fragment gone; the `fx` fixture-fragment arm for UNWIRED, wired, and hook-missing; the break is the adopter at base, whose seeded `--check` exits 1 · no floor exists in this suite

## 8. Open questions

- **F1 — an empty matcher with three readers extended, or the documented `*`.**
  RESOLVED (agent, 2026-09-16, delegated): `*`. The harness documentation's matcher table names
  `"*"`, `""` and omitted as one value, `Match all`, and `Stop` as an event with no matcher
  support; `load_fragment`, the adopter's arm and the hook-destinations resolver each refuse an
  empty string today and accept `*` unchanged. Same acceptance criteria satisfied, zero reader
  changes, and unit 4's `StopFailure` fragment takes the same spelling to record every error
  class. Vetoes clean: no new surface, no governance carrier.
- **F2 — rewire `gate-guard.js` onto `run-lease.js` now, or leave it.**
  RESOLVED (agent, 2026-09-16, delegated): leave it, and file the move at landing. Its walk
  refuses a detached `HEAD` and returns no git dir, so the shared function would be a third shape
  rather than an extraction; the hook is landed with a 124-assertion suite and a build order that
  puts unit 4 next; and no criterion in this build observes the move. The second instance of the
  session-keyed binder is unit 4, which is where this module IS the extraction.
- **F3 — declare `STOP_GUARD_BLOCKS` in the root conf here, or leave it to unit 6.**
  RESOLVED (agent, 2026-09-16, delegated): unit 6. The root conf is a kickoff-manifest watch path
  and every edit owes a re-stamp with a delta line; four knobs land across units 2 to 5 and the
  brief gives their prose to unit 6, so one edit and one stamp there beats four. The hook's
  announced default makes the interim state visible on stderr rather than silent.
  AMENDED at rev-2 (agent, 2026-09-20, delegated): the resolver is `TOOL-aWokenSentinel-10`, not
  unit 6. Units 2 and 5 each declare their own root-conf keys, unit 6 adds rationale only where a
  unit left none (its §4), and the audit found no unit writing this key's line (M7, raw 24) and no
  unit writing its section 8 row (H2, raw 19, 31); unit 10 declares the key in all four carriers
  in one commit with one re-stamp, which is the same one-edit-one-stamp reasoning with the writer
  named.
- **F4 — a malformed knob refuses with exit 2, the driver's rule, or allows.**
  RESOLVED (agent, 2026-09-16, delegated): allows, with `knob-malformed` on the line and one
  stderr sentence. For a `Stop` hook exit 2 is the block, so the driver's refusal shape would make
  a conf typo a session that cannot end its turn; the divergence from `read_bound_key` is stated
  in the hook's header beside the reason.
- **F5 — under a glob loop, how is an absent fragment detected.**
  RESOLVED (agent, 2026-09-16, delegated): it is not, per file, and the arm says so. The
  population floor is the zero guard, the fragment-to-hook join catches the other half of a
  partial copy, and the printed count lets a reader see one where two are expected. A declared
  fragment list would be a second spelling of the glob, which is the class the kit's `**` rule
  exists to avoid.
- **F6 — the memory root from `.memory-tree.conf`, as the brief says, or `.unattended.conf`.**
  RESOLVED (agent, 2026-09-16, delegated): `.unattended.conf`. Both files declare `MEMORY_ROOT`
  in this tree; the kit's own conf is the one `gate-guard.js` reads, the knob lives there, and a
  kit file reading a sibling kit's conf names it by literal.

## 9. Revision log

- rev-2 · 2026-09-20 · S2 · S5 · S6 · §3 · §4 · AC2 · AC3 · AC6 · AC11 · AC18 · AC19 · §7 · §8 ·
  folded spec-audit round 1: M5 (raw 8) — the suite's `project-owned` entry had no criterion, so
  AC18 greps it, and the key's declarations move to unit 10 where AC-read greps live; M7 (raw 24)
  — no unit wrote the root-conf line, so F3 is amended to unit 10; M9 (raw 45) — the default 12
  sat above the harness's 8-consecutive cap, so `BLOCKS_DEFAULT` is 6, `HARNESS_CONSECUTIVE_CAP`
  is pinned with the aReplayedCard record and AC18 asserts the order, §3 states what each bounds;
  L5 (raw 14) — the unwritable-sidecar allow and the liveness bound had no arm, so the bound is
  env-overridable for the fixture and AC19 observes both. Sibling agreement for the promoted
  units: the `FINISHED-UNSTAMPED` row is marked provisional and handed to unit 8 (B1); the knob's
  declarations are handed to unit 10 (H2); AC11's fixture cites unit 14's committed `seed()`
  (H6). Order 3 → 5.
- rev-1 · 2026-09-16 · initial draft, from the spec brief and the research record.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a hook that reads the run-state record bound to the
current session and refuses the turn end"` found no seam for a session-keyed binder: the ranked
candidates are `read_text`, `run` and `read` by name stem, `CensusRefused` in the process-monitor
kit, and the `.unattended.conf` affordance seam; it reports `unscanned layers: .sh`, so the
driver's own functions are invisible to it and were read at source instead. The seam this unit
extends is `tools/unattended/gate-guard.js` — its `resolveRepoRoot`, `readMemoryRoot` and
`resolveRunPhase` are the shape the new module generalises to a session key and a git dir — with
`tools/unattended/gate-guard.fragment.json` and the adopter's sixth artifact as the wiring shape.
The recall query returned `TOOL-aDeferredBar-7` (check-wiring has no arm for this kit's
fragments, OPEN, handed off), `TOOL-dRetiredFork-35` and `TOOL-aReplayedCard-2` on the merger's
fragment-level compare and matcher-group moves, and the aReapedSpinner spec-audit finding that a
hook wired without a fragment is the class this repo refuses. Where the brief and source
disagreed: the brief names `.memory-tree.conf` as the conf, and the seam reads `.unattended.conf`
(§8 F6); the brief says the readers should be extended for an absent matcher, and the documented
`*` makes that unnecessary (§8 F1); the brief cites `adopt-unattended.sh:379-422` and the arm runs
to line 428 at base.

Recall terms used: `hook fragment settings-merge wiring adopter check gate-guard PreToolUse
sidechain marker matcher block reason stop`, with the question "how is a hook fragment wired into
settings and checked by the adopter".
