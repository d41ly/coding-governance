# The stray-job probe, designed against three refuted candidates

**Serves:** research TOOL-aQuenchedHarness-11

Node `a`, 2026-09-08. The report that precedes the spec. Produced by a four-lens survey, three
independent designs and one adversarial verdict per design; ALL THREE scored 3/10 from their own
reviewers, which is the useful result rather than a failed one. Two design-killing facts were
re-verified directly on this box rather than taken on the survey's word:

- MSYS and Windows keep different pid spaces. One live process is msys `2543011` and Windows
  `31208`; `kill -0` succeeds on the first and fails on the second. Every candidate design put a
  Windows pid in its kill path.
- `/proc` is instance-scoped here: 12 directories against 41 `ps -ef` rows. An environment tag is
  therefore unreadable for most processes, which the tool must report rather than paper over.

What follows is the synthesis verbatim.

---

# `gate-strays` — the tagged-descendant reader

**Spec, implementable. Node `a`, 2026-09-08. Every figure below was measured in this worktree today
unless marked ACCEPTED-UNMEASURED.**

One line: a ~2 s reader that lists the gate-family processes and fixture roots THIS msys runtime can
attribute, prices each against its own age, refuses by name every process it cannot attribute, and
kills nothing unless a human types `--reap`.

---

## 0. What this synthesis takes, and from where

The three candidates scored 3/3/3 and each died on the same three rocks. The synthesis is the
smaller tool the watchdog's own reviewer named at the end of that verdict, plus the two mechanisms
the other two got right.

| Taken | From | Why |
|---|---|---|
| Stay in the **MSYS pid space** for the forest and the kill; CIM is a CPU **lookup table only**, joined on winpid, and a failed join is LOUD | watchdog's verdict, verbatim recommendation | I reproduced the killer bug: `kill -0 35272` (winpid) → `No such process`; `kill -0 2536258` (msys) → OK, same live process. All three designs held winpids in the kill path. |
| The **run-id chain in the environment** as the attribution key | reaper | It is the only key that survives reparenting AND exec-replacement, which is exactly what the orphan class destroys. argv does not attribute (all 101 legs carry repo-root-relative argv), cwd does not attribute (every heavy leg `cd`s into its own `mktemp -d`). |
| The chain is a **chain, not a scalar**, and stray-ness is decided by its **ROOT** | reaper's verdict | A scalar `GOV_REAP_CLAIM` is overwritten by the nested `run-selftests.sh`, so a dead parent's tree launders into a live child's claim and the class-5 "never kill a live claim" rule shields class 2 forever. |
| **No kill while the owner lives**; the only kill condition is *the owner is dead* | watchdog | Correct central safety property. Kept, and narrowed further: the probe never kills automatically at all. |
| **Never print a negative about a process**; no stall signal exists | auditor | Kept as a rule, and made structural — see §3, the delta is gone entirely, so a class-5 false positive is unreachable rather than debounced. |
| **Exact basename match against a declared set**, never substring | auditor | `msedge.exe` matches `/sed/`. |
| **`not_asked` as a third state**, keyed per program | reaper's verdict + drift-audit | `live: false` alone prints DEAD PROBE for an adopter who simply has not wired a wrapper. |
| **The contended-run field** — label the measurement, which is the damage the owner actually named | watchdog's verdict, its closing paragraph | "add the one ledger field that labels a contended run, because that is the damage the owner named and it is one column, not a new script plus a held self-test." |
| **HELD** — a fixture root that refuses deletion is proof of a live holder | reaper | Kept, and demoted to what it is: a Windows-only signal, absent on POSIX. |

### What is dropped, and the cost accepted for each

Nothing here is silently dropped; each line is a decision with a price.

- **The detached watchdog process.** Dropped whole. Cost: an orphaned tree lives until someone runs
  the probe (next SessionStart, ~one working session) instead of one poll interval. Bought: no
  blind window, no detached-child lifetime problem, no `--disarm`/`cleanup` trap hazard, no
  self-orphaning probe, no 120-poll duty cycle, no `GATE_RUN_ID` export. The watchdog's entire
  weakness list except its class-1/class-4 refusals evaporates with this one deletion.
- **The two-sample CPU delta**, the three-poll debounce, the `NO PROGRESS` line and the
  `NOT proof of death` parenthetical. Dropped. Replaced by ONE cumulative CPU reading against the
  process's own age — a duty cycle. This prices the incident's spin loop exactly (46221 CPU-s over
  11.4 h = 1.13 cores) with one sample and no gap, and it removes the only signal in any of the
  three designs that could fire on a healthy quiet process. Cost: the probe can never say "advancing
  right now". It never needed to — CPU is never an input to any decision it makes.
- **The claim-file registry** (`gate-claims/`, `watchdog.claimed`, `<i>.pid` copies). Dropped. The
  run id already carries its own pid: `RUNID="${GATE_RUN_ID:-$(date -u +%Y%m%dT%H%M%SZ)-$$}"`
  (`run-gates.sh:997`). Liveness of a run is `kill -0` on the pid parsed out of its id. Cost: none
  found. Bought: no trap edits (`run-gates.sh:953` `cleanup` is untouched — the hazard its own
  comment warns about never arises), no `GATE_RUN_KEEP` interaction, no nameable `<i>.pid`
  suppressor-adjacent file, no `verdict`-absence coupling.
- **The bar leg.** Dropped. Both reviewers showed it either grades nothing while shipping a green
  row named after the process table (§7's "a structural check reads as a semantic one … and the
  resulting false confidence is worse than the gap") or reds non-reproducibly on a developer's box.
  Cost: nothing mechanically forces anyone to look. Mitigated by the SessionStart call site, which
  is a habit, and stated as such.
- **`--kill-untagged` and `reap-policy.txt`.** Dropped. Cost: incident classes 1 and 4 are out of
  reach — see §8, where they are refused explicitly rather than half-covered.
- **macOS.** Declared dark. ACCEPTED-UNMEASURED, no host available.

---

## 1. Files

Four things change. Three are one line each.

**New — `tools/run-gates/gate-strays.sh`** (LF, bash + awk, no python, no new dependency). The whole
tool. Verbs, exactly four:

```
bash tools/run-gates/gate-strays.sh              # report (default)
bash tools/run-gates/gate-strays.sh --count-foreign   # print ONE integer, nothing else
bash tools/run-gates/gate-strays.sh --reap       # act; human-typed only
bash tools/run-gates/gate-strays.sh --json       # the same report, machine shape
```

**New — `tools/run-gates/gate-strays.test.sh`** (held). `tools/run-gates/kit.toml` already withholds
this kit's suites by claiming the destination with `role = "project-owned"`; add the new filename to
that existing `[[files]] include` array — one array element, no new mechanism. It owes a
`selftest-budgets.txt` row and is **not** on the bar (2026-08-23 ruling).

**Edit — three wrappers, one `export` each.** No traps, no cleanup edits, no sourcing.

- `tools/run-gates/run-gates.sh`, immediately after `RUNID=` is assigned (:997):
  ```sh
  export GOV_GATE_CHAIN="${GOV_GATE_CHAIN:+$GOV_GATE_CHAIN:}$RUNID"
  ```
- `tools/run-gates/run-selftests.sh` and `tools/unattended/run-unattended-gates.sh`, after `ROOT=`
  is resolved (:26 and :34 respectively — both verified to have **no** existing `trap`):
  ```sh
  export GOV_GATE_CHAIN="${GOV_GATE_CHAIN:+$GOV_GATE_CHAIN:}$(date -u +%Y%m%dT%H%M%SZ)-$$"
  ```

  The variable is `GOV_GATE_CHAIN` and deliberately **not** `GATE_RUN_ID`. `GATE_RUN_ID` is an
  *override the runner reads*; exporting it makes four bar legs that drive `run-gates` as a
  subprocess share a run directory and a reap glob with their parent. The reaper's reviewer found
  a literal `GATE_RUN_ID=PINNED` already pinned at `run-gates.evidence.test.sh:386`. A separate
  name the runner never reads closes that class by construction.

**Edit — `tools/lib/lib-selftest.sh:81`**, one line:
```sh
SELFTEST_ROOT=$(mktemp -d -t "gate-${GOV_GATE_CHAIN%%:*}-XXXXXXXX" 2>/dev/null || mktemp -d) || { ... }
```
`${GOV_GATE_CHAIN%%:*}` is the chain ROOT. Unset chain falls through to the plain `mktemp -d` and
the root is simply untagged, which the probe reports as untagged rather than guessing.

**Edit — `tools/run-gates/run-gates.sh` header block (:1204-1244), two `printf` rows.** This is the
one that addresses the damage the owner named. Inside the existing header writer, in its existing
`key<TAB>value` grammar:
```sh
printf 'foreign_gate_procs\t%s\n' "$(bash "$KITREL/gate-strays.sh" --count-foreign 2>/dev/null || echo '?')"
printf 'foreign_gate_procs_from\tgate-strays --count-foreign\n'
```
A run measured alongside other gate work now says so in its own record, and `?` (the probe could
not answer) is distinguishable from `0` (it answered zero). Additive rows in an existing key/value
file; no reader of `gate-ledger.tsv` moves.

---

## 2. Attribution — the rule that keeps it off other sessions and other checkouts

**One key: the chain root, read from the process's own environment. There is no argv match, no
image-name match, no cwd match and no age heuristic anywhere in the kill path.**

```
chain      GOV_GATE_CHAIN = <root-id>[:<child-id>[:...]]
root       ${chain%%:*}  →  <utc>-<msys-pid>
alive?     the pid parsed from the root
```

A run named by a chain root is **DEAD** iff **both** independent readers agree it is gone:
`kill -0 <root-pid>` fails **AND** that pid is absent from the `ps -ef` snapshot. Two readers,
because `kill -0` also fails with EPERM — a present-but-unsignalable pid is LIVE and prints
`REFUSED`. It is also DEAD if the pid answers but its start time disagrees with the id's own UTC
stamp by more than 120 s (pid reuse). **If the start time cannot be read, the run is LIVE.** Every
ambiguity resolves toward "do not touch it".

Scope is by construction, not by predicate:

- **Other checkouts of this repo, and other repositories.** A chain root is only *resolvable* here
  if its pid is in this box's process table; it is only *actionable* if the process also sits in
  this msys runtime's `/proc`. Two clones cannot share a root pid without sharing a machine, and on
  one machine the pid IS the identity. No path, worktree or git-dir comparison is needed or made.
- **Other sessions on this machine.** Their processes are in `ps -ef` but their `/proc/<pid>/environ`
  is unreadable from here — **measured: 9 `/proc` dirs against 41 `ps -ef` rows in one instant.**
  An unreadable environ is never "not ours"; it is `REFUSED`, counted, and reported in the coverage
  ratio. The probe therefore cannot attribute another session's orphans on Windows **and says so
  every run.** This is the honest scope, and it is the right one: the incident's stated consequence
  was contention from *the session's own orphans*.
- **Other users.** uid from `ps -ef` field 1 must be ours, checked before anything else.

Two hazards handled explicitly because both were reproduced:

1. **`ps -ef` continuation rows are real and I hit them today.** Sampling eight `$2` values returned
   six argv fragments — `(for`, `-ef`, `-d`, `"ps`, `"---`, `e=no` — from a multi-line `bash -c`.
   Every awk over the snapshot carries the guard `$2 ~ /^[0-9]+$/ && $3 ~ /^[0-9]+$/`, the same
   guard `run-gates.sh:429-441` earned, and the **parse ratio is printed** (§3). A snapshot the
   walker mostly could not parse must never render as a clean board.
2. **`scan_descendants` is reused unchanged, over `ps -ef` only.** It is moved verbatim from
   `run-gates.sh:428-473` into `tools/run-gates/lib-proc.sh` and sourced by both callers. It is
   never fed CIM columns — the watchdog's plan to reuse it "verbatim" against
   `pid ppid cpu created` would have passed both of its numeric guards while reading ppid-as-pid.

`ppid == 1` is **not** an orphan test. It condemns two healthy populations here: Claude Code's own
Bash-tool shells, and the turnstile's deliberately `disown`ed ticker.

---

## 3. Signals

Everything is derived at emission. No count of a derived population is written in this spec or in
the script.

| Signal | Source | Cost |
|---|---|---|
| forest | one `ps -ef`, msys pid space — the space `kill` speaks | 0.070 s (41 rows) to ~0.8 s under load |
| chain | `tr '\0' '\n' < /proc/<pid>/environ \| grep -m1 '^GOV_GATE_CHAIN='`, over `/proc` pids only | 0.494 s for the whole `/proc` set |
| winpid | `awk 'FNR==1{split(FILENAME,a,"/"); print a[3], $0}' /proc/[0-9]*/winpid` — batched, one process | 0.404 s, 16 rows |
| cpu + age | ONE `pwsh` CIM read, joined on winpid: `SELECT ProcessId,CreationDate,KernelModeTime,UserModeTime FROM Win32_Process`, `(Kernel+User)/10000` ms | 0.880 s, 330 rows |
| duty | `cpu_ms / age_ms` — a cumulative reading against the process's own age. No second sample, no gap. | free |
| litter | `ls -d /tmp/gate-*-* /tmp/tmp.* 2>/dev/null` | 0.05 s |

`Get-Process` is refused as a CPU source (null CPU on a third of rows, silently). `tasklist /V` is
refused on cost (17.5 s, measured by two readers). A per-pid `cat /proc/<pid>/stat` loop is refused
(3409 ms for 14 pids). A host-wide process count is refused — it was already built, measured and
deleted at `lib-selftest.sh:90-96` for reporting the box's load instead of this run's cost.

**There is no progress signal, no output-freshness signal and no fixture-mtime signal.** Each was
measured condemning a healthy process, and none of them is needed: nothing the probe decides takes
CPU as an input, in either direction.

---

## 4. Verdict vocabulary

Every line is a bare markdown list item per §16 R1. All lines go to **stderr** except `--json` and
`--count-foreign`, whose stdout is machine-read. One example of every line the tool can print:

**Header — always, first, one line, every figure derived at emission:**

- `strays — snapshot 41/47 parsed · tags 9/41 readable · cpu via cim · self ok · chains 2 live 1 dead`

**Per-row:**

- `STRAY — 2536912 · run-selftests.sh · root 20260907T084852Z-796422 DEAD (pid gone, absent from snapshot) · age 27043s · cpu 26981s (1.00 cores) · winpid 41208`
- `LIVE — 2537110 · run-gates.sh · root 20260908T061200Z-2536001 live · age 412s · cpu 39s (0.09 cores)`
- `REFUSED — 2315342 · environ unreadable, not in this msys runtime · age 221690s · cpu unavailable`
- `REFUSED — 2536700 · root 20260908T0530Z-PINNED unparseable — treated as live`
- `REFUSED — 2537400 · kill -0 says no but the snapshot still lists it (EPERM?) — treated as live`
- `UNTAGGED — 2530118 · bash · age 41022s · cpu 2s (0.00 cores) · no chain, no claim, not mine to judge`

**Fixtures:**

- `LITTER — /tmp/gate-20260907T084852Z-796422-hK3nQ8vA · root DEAD · age 27043s`
- `HELD — /tmp/gate-20260907T084852Z-796422-hK3nQ8vA · refused to delete, so a live holder still has it open`
- `UNTAGGED FIXTURES — 20 tmp.* roots in a directory holding 67030 entries · oldest 512440s · counted, never touched`

**Closing:**

- `strays — CLEAN · 0 stray · 0 litter · 32 REFUSED (unreadable) · 1 untagged`
- `strays — FOUND · 3 stray · 1 litter · 32 REFUSED · --reap to act`
- `strays — REAPED · 3 killed · 1 survived · 2 fixture roots removed`
- `SURVIVED — 2536912 · still alive after SIGKILL · winpid 41208 · run: taskkill //PID 41208 //T //F`
- `strays — NOT ASKED · no process in this tree carries GOV_GATE_CHAIN; no wrapper here is wired`
- `strays — DEAD PROBE · could not read my own environ through /proc; no attribution is possible this run · exit 3`

Copyable kill lines print **msys pids**, and only msys pids. `taskkill //PID <winpid> //T //F` is
printed **only** on the `SURVIVED` line and is never run by the tool: a mis-resolved join across
that boundary is unrecoverable, so the last step across it stays with a human. `taskkill` is present
at `/c/Windows/system32/taskkill`.

---

## 5. The probe's own liveness assertion

**It grades the JOIN and the CLAIM RESOLUTION, not "did the snapshot tool run".** That was the
common defect: all three designs asserted `rows > 0`, which passes on an arm that sees 4% of the box.

Four checks, each with a reachable red branch, evaluated before any row is printed:

1. **Self-attribution.** The probe exports its own `GOV_GATE_CHAIN` before scanning, then must find
   its own pid in the snapshot **and read that chain back out of `/proc/self/environ`**. This is the
   one environ read that always succeeds — so it is deliberately *not* the whole assertion, only its
   floor. Its failure means `/proc` is not exposed at all → `DEAD PROBE`, exit 3.
2. **Foreign-read coverage.** `tags <readable>/<candidates>` is printed and is an **assertion, not a
   display**: `readable == 0` while `candidates > 0` is `DEAD PROBE`, exit 3. This is the check that
   catches the state I measured (9 of 41) degrading to zero, which no candidate design could see.
3. **Snapshot parse ratio.** `snapshot <parsed>/<rows>`. Below 0.5 → `DEAD PROBE`, exit 3. I
   reproduced 6 unparseable rows in an 8-row sample; a snapshot the walker mostly cannot parse is
   not a clean board.
4. **Self CPU.** The probe's own winpid must resolve in the CIM table and read `cpu > 0`. It has
   just enumerated hundreds of processes, so zero means the counter is broken. Failure does **not**
   kill the run — it disarms the CPU column wholesale, every row prints `cpu unavailable`, and the
   header reads `cpu via none (self reading was 0)`. CPU is informational; losing it must not lose
   the attribution.

The rejected alternative, named because it is the shape this repo's doctrine exists against: *"did
anything at all advance globally?"* returns 12–37 movers even at a zero gap, because the enumeration
itself burns ~100 ms. It is near-unfailable, and it would have reported a healthy probe through the
entire incident.

**Three states, not two.** No process carrying `GOV_GATE_CHAIN` and no `gate-*` fixture root is
`NOT ASKED` — the wrappers are unwired, or this is an adopter tree that copy-installed the kit. It
is never `CLEAN`. `not_asked` is keyed **per program**, so a tree where `run-gates` is wired and
`run-selftests` is not says exactly that.

---

## 6. Reaping policy

**Default is report. `--reap` is typed by a human. No leg, no hook and no wrapper ever sets it.**

`--reap` kills a process iff **all** of:

1. its uid is ours;
2. its `GOV_GATE_CHAIN` was read from `/proc/<pid>/environ` by this run of the probe;
3. the **root** of that chain is DEAD by the two-reader rule in §2;
4. it is still alive at the moment of the kill (`kill -0` re-checked per pid);
5. the msys pid is the pid the snapshot named — descendants are walked from the ONE snapshot taken
   before any kill, because killing a parent reparents its children.

Mechanics: descendants deepest-first, root last. `kill -TERM`, re-check at 2 s, `kill -KILL`,
re-walk the original snapshot and print `SURVIVED` with the winpid and the `taskkill` line for
anything still answering. That survivor re-walk is `remove_descendants`' own liveness assertion and
the reason its `rm -f "$snap"` sits *after* the loop (`run-gates.sh:456-472`).

Fixtures: `rm -rf` only on `/tmp/gate-<root>-*` where `<root>` is a chain root this run proved DEAD.
Never `/tmp/tmp.*`, never an mtime rule, never "older than the oldest live claim" — that predicate
degenerates to `rm -rf /tmp/tmp.*` whenever the caller's own claim is the only live one, over a
directory measured here holding 67,030 entries. A root that refuses deletion prints `HELD` and is
left alone (Windows only; on POSIX an open file does not block unlink, so `HELD` is structurally
unreachable there and the POSIX header says so).

**It refuses, always, in every mode:**

- any process whose chain root is LIVE — whatever it is doing, however quiet, however long;
- any process whose chain is unreadable (another session, another runtime) — `REFUSED`, counted;
- any process with no chain at all — `UNTAGGED`, counted, priced, never judged;
- any process whose chain root id does not parse to a pid (`GATE_RUN_ID` pinned to a literal);
- any process whose start time cannot be read, and any root that answers `kill -0` with EPERM;
- any process owned by another uid;
- **everything, when any liveness check in §5 fails.** A probe that cannot see does not act on a
  partial view.

---

## 7. Portability

Selected by **running** the candidate, never by `uname` and never by `command -v` — the repo's own
resolver doctrine, because the MS-Store `python3` stub answers `command -v` and exits 9009.

- **MSYS / Cygwin (nodes a–d, the whole registry).** `ps -ef` for the forest, `/proc/<pid>/environ`
  for the chain, `/proc/<pid>/winpid` for the join, one `pwsh -NoProfile -NonInteractive` CIM read
  for cpu+age, falling back to `powershell` 5.1, falling back to `cpu unavailable` on every row.
  Losing the CPU arm costs the price column and nothing else.
- **POSIX adopter (Linux — the reference second arm).** Simpler and cheaper, and it is the arm where
  the whole tool is *complete*:
  - forest: same `ps -ef`, same numeric guards (harmless there, mandatory here);
  - chain: `/proc/<pid>/environ` — same read, and on Linux it covers **every** process of our uid,
    so the coverage ratio that reads 9/41 here reads N/N there, and tier `REFUSED` empties;
  - cpu + age: one awk sweep, no second process —
    `awk '{i=index($0,") "); split(substr($0,i+2),f," "); print $1, f[2], (f[12]+f[13])*1000/CLK, f[20]}' CLK=$(getconf CLK_TCK) /proc/[0-9]*/stat`
    with age from field 22 against `/proc/uptime`. **`CLK_TCK` is read, never typed** — it is 100 on
    Linux and **measured 1000 under this MSYS**. The `index($0,") ")` idiom is mandatory: a comm
    containing a space shifts every positional field and a live process reports zero CPU.
  - no winpid join, no pwsh, no CIM, no `HELD` (unlink of an open file succeeds), and the header
    says `cpu via procfs · held detector unavailable on this platform`.
- **macOS.** Declared **dark**: `strays — NOT ASKED · platform Darwin is declared dark`, exit 3, no
  rows, no reaper. There is no `/proc`, so both the chain key and the CPU source lose their reader.
  ACCEPTED-UNMEASURED — no host was available, and a guessed arm on the platform where the key is
  absent is worse than a named refusal. An adopter on macOS gets an honest dead probe.

LF via the existing `.gitattributes` `*.sh` rule. **No `.ps1` file ships** — the CIM query contains
no slash, so MSYS path-mangling has nothing to chew, and a tracked `.ps1` would owe the repo's
PowerShell BOM/case-collision scan for no gain. No python, so `resolve-python.sh` is not in the path.

---

## 8. Cost

Measured, node `a`, 16 cores, non-elevated:

| | Windows | POSIX |
|---|---|---|
| `ps -ef` | 0.070 s idle, ~0.8 s loaded | same |
| chain reads over `/proc` | 0.494 s | ~0.02 s |
| winpid join (batched, 1 awk) | 0.404 s | n/a |
| cpu + age (1 `pwsh`, 1 CIM query, 330 rows) | 0.880 s | ~0.01 s, no process |
| **report total** | **≈ 1.9 s, 3 external processes** (`ps`, awk, `pwsh`) | **≈ 0.1 s, 2 processes** |
| `--count-foreign` (no CPU arm) | ≈ 0.6 s, 2 processes | ≈ 0.1 s |

Call sites and what each pays:

- **SessionStart hook**, beside `tools/check-wiring.sh --session`, report mode. ≈ 1.9 s per session
  start. It always prints its header line, so a dead probe is never mistaken for a clean box.
  It never exits non-zero into the hook and never blocks a session.
- **`run-gates.sh` header**, `--count-foreign` only. ≈ 0.6 s once per bar, against a bar with a
  measured 26-minute floor.
- **By hand**, when a session suspects it left something behind.

No wall-clock is added to any leg. The probe holds no beacon, takes no turnstile ticket, and writes
nothing anywhere — a probe that writes into `<git-dir>` during a bar becomes a participant in the
contention it exists to measure.

---

## 9. What this does NOT check

```
# WHAT THIS TOOL DOES NOT CHECK. It does not grade the machine. It reports only what THIS msys
# runtime can attribute through a process's own environment, and on Windows that was measured at 9
# readable processes out of 41 in the table — so it is blind to another session's orphans by
# construction, prints that ratio every run, and REFUSES the rest by name rather than calling them
# absent. It does not decide whether any process is doing useful work: CPU is priced against age and
# is never an input to any verdict, in either direction, because a healthy bar legitimately prints
# nothing for an hour and a stale 61-hour monitor burns 0.03% of a core. It does not detect a stall,
# a hang, or a slow leg — the per-leg ceiling and the whole-run wall remain the only killers, and
# this tool replaces neither, nor the turnstile. It does not see a process nobody declared: a spin
# loop or a monitor spawned by a harness tool call carries no chain and can never carry one, so
# incident classes 1 and 4 are OUT OF REACH and are reported as UNTAGGED with an age and a price and
# no judgement. It does not verify that a killed tree released its file handles. It does not check
# any other repository, any other checkout, or any other user. It cannot reach a native Windows
# grandchild from bash at any pid — measured, `kill -0` fails on both the winpid and the synthesized
# msys pid — so it prints the taskkill line and stops. It is not a gate: no leg on the merge bar
# depends on it, deliberately, because a check that reds on the state of a developer's box is not
# reproducible on another node and a green row named after the process table manufactures exactly
# the false confidence §7 forbids.
```

---

## 10. Class coverage, honest

| Class | Verdict |
|---|---|
| **1 — spin loop** (11.4 h, 12.8 core-hours) | **NOT COVERED.** Harness-spawned, no chain, never killable by this tool. Reported as `UNTAGGED` with `age 41022s · cpu 46221s (1.13 cores)`, which is the number that tells an operator this one is expensive. Accepted: reaching it needs argv heuristics pointed at `kill -9`, which is the class that killed all three candidates. |
| **2 — orphaned tree** | **COVERED, and it is why the tool exists.** The wrapper dies, the chain survives in every descendant's environment through reparenting and exec, its root pid answers nothing, and the row is `STRAY`. Zero time dimension: one snapshot. Detected in report mode, killed only by `--reap`. Conditional on the descendants being in this msys runtime's `/proc`, which they are when the probe runs in the session that spawned them — and when they are not, the row is `REFUSED`, never `CLEAN`. |
| **3 — duplicate runs** | **COVERED AS A CONSEQUENCE, not directly.** Nine concurrent suites were orphans from earlier runs; reap the orphans and they stop accumulating. No cardinality signal is built: it needs argv counting, argv does not attribute across checkouts, and the continuation rows I reproduced today bias such a count in *both* directions (a measured 2× overcount, and unparseable rows biasing down). The incident's "nine" is probably not nine. |
| **4 — stale monitors** (52–61 h) | **NOT COVERED.** Harness-spawned, no chain. Also invisible to CPU by construction (~67 CPU-s over 61 h), which is why "CPU advancing = healthy" is not a rule here. Reported as `UNTAGGED` with an age. Accepted. |
| **5 — silent-but-alive** | **PROTECTED STRUCTURALLY.** There is no output-freshness signal, no fixture-mtime signal, and no CPU delta. A live chain root is never touched. The tool owns no predicate that can fire on a quiet healthy process — this is stronger than the debounce all three designs used, because the false positive is unreachable rather than delayed. |
| **6 — fixture litter** | **COVERED FOR WHAT IT OWNS, counted for what it does not.** The one-line `mktemp -d -t` change makes every suite scratch root attributable to a chain root for the first time. `--reap` removes only `/tmp/gate-<dead-root>-*`. Untagged `tmp.*` roots are counted **against the total entry count of the directory** — reporting "20 stale roots" in a directory holding 67,030 entries is the reassuring-number shape one level up, so both figures print or neither does. |
| **the stated damage** | **ADDRESSED.** `foreign_gate_procs` in the run header labels a measurement taken alongside other gate work, and `?` (could not answer) is distinguishable from `0`. None of the three candidates touched this. |

---

## 11. Residual weaknesses, stated

1. **Windows coverage of another session's orphans is ~20% and that is a property of cygwin `/proc`,
   not of this design.** Every unreadable process is `REFUSED` and counted, and zero readable
   candidates is `DEAD PROBE` — so the tool can never report clean while blind. It still cannot
   *see* what it cannot read.
2. **Latency is "until someone runs it".** No detached watcher, so an orphan lives to the next
   SessionStart. Traded deliberately for the entire watchdog weakness list.
3. **A chain root pinned to a literal** (`GATE_RUN_ID=PINNED`) makes its whole subtree permanently
   `REFUSED — unparseable, treated as live`. Fail-safe direction; a fixture that pins the id gets no
   reaping.
4. **The pid-reuse guard is 120 s wide**, from a `date -u` stamp against a process start time.
   Windows recycles pids aggressively; a reuse inside that window defeats it. The failure direction
   is a wrong kill, which is why it is only ever reached under a human-typed `--reap` and behind
   three other ANDed conditions.
5. **The mtime/format hazard on `ps` STIME is sidestepped, not solved**: start times come from CIM
   `CreationDate` (100 ns ticks) or `/proc/stat` field 22, never from `ps` STIME, which the auditor
   measured switching format past 24 hours — precisely on the multi-hour processes that matter.
6. **`HELD` is Windows-only.** On POSIX it is structurally unreachable and the header says so
   instead of implying a detector that cannot fire.
7. **Nothing forces anyone to look.** No leg, by design. The SessionStart line is a habit.
8. **macOS is dark and unmeasured.**

---

## 12. Failing cases that must be OBSERVED before it lands

§7: a gate you have only ever seen pass is an assertion about nothing. Each arm below stages the
break, confirms RED, unstages. All live in `gate-strays.test.sh` (held, `subject = kit`,
`chunk = selftests`, one `selftest-budgets.txt` row, not on the bar).

1. **STRAY fires.** Spawn `bash -c 'export GOV_GATE_CHAIN=<utc>-<pid-of-a-doomed-shell>; sleep 300' &`
   under a wrapper shell, `kill -9` the wrapper, run the probe. Assert one `STRAY` row naming the
   sleeper's **msys** pid, and that `--reap` then kills it and `kill -0` on that pid fails after.
   *This is the class-2 arm and the reason the tool exists.*
2. **STRAY does NOT fire on a live root.** Same tree, wrapper left alive. Assert zero `STRAY` rows
   and one `LIVE` row, and that `--reap` kills nothing. *The class-5 arm.*
3. **The kill lands in the right pid space.** Assert every pid on a `STRAY` row and every pid in a
   printed kill line answers `kill -0` from bash **before** the reap. This is the assertion that
   would have caught all three candidate designs; it must be a first-class arm, not an implication.
4. **DEAD PROBE on zero foreign readability.** Seam `GATE_STRAYS_PROC=/nonexistent` so no
   `/proc/<pid>/environ` resolves while candidates exist. Assert `DEAD PROBE`, exit 3, **zero** rows
   printed and **zero** kills attempted under `--reap`.
5. **DEAD PROBE on an unparseable snapshot.** Seam a `ps` stub returning mostly continuation rows.
   Assert the parse ratio prints, that it is below 0.5, and that the verdict is `DEAD PROBE` and not
   `CLEAN`.
6. **CPU disarms without disarming attribution.** Seam `GATE_STRAYS_CPU=/bin/false`. Assert every
   row reads `cpu unavailable`, the header names the reason, and the `STRAY` verdict from arm 1 is
   **unchanged**.
7. **NOT ASKED is distinguishable from CLEAN.** Run in a tree with no `GOV_GATE_CHAIN` anywhere.
   Assert `NOT ASKED`, and assert the string `CLEAN` does not appear.
8. **REFUSED, not silently absent.** Stage a process of ours whose environ read fails. Assert a
   `REFUSED` row exists and that the header's `tags <readable>/<candidates>` denominator counts it.
9. **EPERM does not read as death.** Stub the `kill -0` seam to fail while the snapshot still lists
   the pid. Assert `REFUSED — … treated as live` and no kill.
10. **Fixture reap is exact.** Create `/tmp/gate-<dead-root>-AAA`, `/tmp/gate-<live-root>-BBB` and
    `/tmp/tmp.CCC`. Assert `--reap` removes exactly the first, and that the run's own untagged count
    prints both the stale count and the directory's total entry count.
11. **The wrapper edits do not break the runner.** Run the existing `run-gates.test.sh`,
    `run-gates.turnstile.test.sh` and `run-gates.evidence.test.sh` unchanged after the `export` and
    header-row edits, and assert `GATE_RUN_ID` is still **not** exported by any of them
    (`bash -c 'run-gates …; env | grep -c "^GATE_RUN_ID="'` reads 0).
12. **The lexicon leg.** Run `python3 tools/lexicon/lexicon.py --suggest` over every function name
    in both new files before the first landing attempt; it grades nested helpers, and a records-only
    branch bar skips it as unchanged-vs-main, so it only reds at the lander.

Landing also owes: the `kit.toml` `project-owned` array element for the new test, the
`selftest-budgets.txt` row, and a claim for the new keys in `memory/map/features/run-gates.md`
(the codebase-map coverage leg reds otherwise).
