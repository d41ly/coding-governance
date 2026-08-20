# Tier-2 review — TOOL-aPacedTurnstile-2, the declared hardware profile table

**Range reviewed:** `56b945cbb0613b1352dd06221d4d39940db33419...HEAD` (commits `2d03cb5`, `d37c8a4`).

**Serves:** diff-review TOOL-aPacedTurnstile-2
· **Build:** aPacedTurnstile · **Date:** 2026-08-20 · **Tier:** 2
· **Streams:** tooling
**Contract:** `memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-2.md`, AC1–AC13.
**Governing invariant graded:** no knob may ever turn a leg into a PASS or a SKIP; a knob may cost
speed, and the timeout may convert an unbounded hang into a bounded RED naming its leg.

**Review shape:** raw 19 · confirmed 15 · refuted 4 · unverified 0 · precision 0.79. The 15 confirmed
findings collapse to **8 distinct defects** — four reports named the same stale width formula, two
named the same command-substitution hang, two named the same dropped `GATE_PROFILE`, and three named
the same missing length bound. Counts below are the distinct set: **1 blocker · 0 further highs ·
4 medium · 3 low**. The blocker is the only high-severity finding; it is graded as a blocker rather
than counted twice.

## Verdict: FIX THE BLOCKER BEFORE LANDING

The invariant itself holds everywhere I attacked it. No knob path produces a PASS or a SKIP: the
width clamp only schedules, an unknown knob key refuses, a malformed row refuses, an unmatchable
table refuses, an absent table falls back and still runs every leg, and a timed-out leg is reported
`GATE FAIL` with a RED verdict. Every wrong-value path reproduced below — over-long thresholds, an
over-long `timeout=`, a dropped `GATE_PROFILE` — costs a wrong *width* or a silently inert *timeout*,
never a wrong verdict. That is the load-bearing property and it survived.

What did not survive is the timeout's *upward* half. The knob's whole justification is that it
converts an unbounded hang into a bounded RED, and it does not: the verdict is bounded, the clock is
not. Everything else here is documentation drift or a coverage gap.

## Blocker

### B1 — the per-leg timeout bounds the verdict, not the clock

`tools/run-gates/run-gates.sh:330` (severity **high**, graded **BLOCKER**) · merges raw findings 1
and 10.

`runleg()` runs the timed leg inside a command substitution:

```sh
if [ "$PROF_TIMEOUT" -gt 0 ]; then out=$(timeout "$PROF_TIMEOUT" "${argv[@]}" </dev/null 2>&1); rc=$?
```

`$( )` reads until EOF, and EOF arrives only when the last inherited write end closes. `timeout`
signals the leg's direct process — GNU coreutils 8.32 on node `a` signals the process group, but does
not reach a grandchild reliably under MSYS — so any surviving descendant holds the pipe open and the
worker blocks for the full hang. The pool slot is held, `wait -n` does not return, and the bar wedges
exactly as it did before the knob existed.

Measured against the real runner in a scratch fixture built the way the canary builds its own (two
legs, `sleeper` = `bash fx/sleeper.sh` running a long `sleep`):

| Table row | Wall clock | Verdict |
|---|---|---|
| `tight 0 0 width=2,timeout=1` | 51.4 s (35.5 s and 73.7 s on other runs) | `GATE FAIL  sleeper  (timed out after 1s)`, run RED |
| `off 0 0 width=2,timeout=0` | 50.2 s | GREEN |

Same wall clock. The knob changed the verdict and bought zero time. A four-run set against a 30 s
sleeper with `timeout=3` measured 18.7 / 22.1 / 27.0 / 27.0 s against the declared 3 s bound. The
mechanism reproduces standalone: `out=$(timeout 1 bash -c 'sleep 10; echo done')` returned rc=124
after 13.6 s, and `out=$(bash -c 'sleep 12 & exit 0')` returned after 15 s.

Three carriers now record a bound that is not enforced: the comment at `run-gates.sh:328` ("an
unbounded hang wedges the whole bar and names nothing"), `tools/run-gates/gate-profiles.txt:13` and
`:21` ("turn an unbounded hang into a bounded RED", "converts a hang into a verdict"), and
`memory/map/features/run-gates.md:70`. Latent today only because all three shipped rows set
`timeout=0` — the first operator to raise it is the one who discovers it, and the shipped canary
already raises it in a fixture.

**Fix.** Stop capturing the timed leg through a pipe. Redirect to a file and read it after `timeout`
returns, and add `-k` so a child that ignores SIGTERM still dies:

```sh
if [ "$PROF_TIMEOUT" -gt 0 ]; then timeout -k 5s "$PROF_TIMEOUT" "${argv[@]}" </dev/null >"$WORK/$i.raw" 2>&1; rc=$?
else "${argv[@]}" </dev/null >"$WORK/$i.raw" 2>&1; rc=$?; fi
out=$(cat "$WORK/$i.raw")
```

Measured on the same case: 2.4 s and 3.9 s, i.e. actually bounded. If the orphans themselves must die
— they hold the leg's `mktemp -d` scratch repo — run the leg under `setsid` and signal the group
rather than trusting `timeout` alone.

**Left-shift gate.** Arm 4h (`tools/run-gates/run-gates.test.sh:596-610`) is the
fixture-passes-by-finding-nothing instance this build named as a hunted class: it asserts the message
string and the RED verdict and never measures elapsed time, so the property the knob exists for is
unobserved by its own gate. Wrap the `runp` call in `date +%s` and fail if the run outlived, say, 4x
the declared timeout. AC8 as written is satisfied by the broken code; the elapsed assertion is what
makes AC8 grade the claim rather than the message.

## Medium

### M1 — `min(8, nproc)` survives in the two files closest to the change, and the shipped README never mentions the table

`tools/run-gates/run-gates.sh:4` and `tools/run-gates/README.md:30` · merges raw findings 3, 7, 15,
16.

AC11b stripped the backticked width formula from `AGENTS.md` and armed gov canary G5
(`run-gates.gov.test.sh:182`) to keep it out — but G5 greps `"$ROOT/AGENTS.md"` only, and
`git grep 'min(8'` returns two live tracked hits outside the build records, both inside the kit the
sentence describes:

- `run-gates.sh:4` — the usage header reads "legs run CONCURRENTLY, width min(8, nproc)". It is the
  first thing any reader of the changed file sees, and it names neither `gate-profiles.txt` nor
  `GATE_PROFILE` / `GATE_PROFILES` nor the RAM threshold.
- `README.md:30` — the `run-gates.sh` row of the adopter-facing piece table repeats the same formula
  and says `GATE_JOBS` overrides it.

Worse than reported: `grep -in 'profile\|GATE_RAM\|GATE_CORES' tools/run-gates/README.md` returns
**zero hits**. The kit's own "The pieces" table lists seven files and has no row for
`gate-profiles.txt`, which `kit.toml:114` declares as a shipped LF-pinned file. The formula now
describes only the absent-table fallback (`run-gates.sh:235`), so every adopter receives a README
telling them the width comes from core count and is never pointed at the file that owns it. This is
the two-answers-to-one-question class the unit set out to remove, relocated from the charter into the
kit rather than removed.

**Fix.** Rewrite `run-gates.sh:4` to name the source — "legs run CONCURRENTLY, at the width
`<prefix>/run-gates/gate-profiles.txt` declares" — and add a usage line for `GATE_PROFILE=<row>` and
`GATE_PROFILES=<path>` beside the existing `GATE_JOBS` line. Fix the README row the same way and add
a `gate-profiles.txt` row to the pieces table.

**Left-shift gate.** Move the pair into the SHIPPED canary. Both files travel, so the arm is true in
any tree and does not belong in `run-gates.gov.test.sh`. Assert both halves, so a deleted row cannot
satisfy the negative alone: `grep -qF 'min(8, nproc)'` over `"$KITREL/run-gates.sh"` and over
`"$KITREL/README.md"` must both return non-zero, AND `grep -qF 'gate-profiles.txt'` over both must
return zero. That gates the CLASS instead of the one AGENTS.md instance.

### M2 — the canary's timeout arms assert unconditionally on a host where the runner declares the knob INERT

`tools/run-gates/run-gates.test.sh:590` (arms 4g and 4h).

The runner deliberately degrades when `timeout` does not run (`run-gates.sh:238-242`), printing that
the profile asks for a per-leg timeout "but timeout does not run here — the knob is INERT this run".
Reproduced with a PATH shim making `timeout` exit 127: the runner prints the INERT line, then
`gate profile: tight (... timeout off ...)`, then `gates GREEN — 2/2 legs passed`. Three assertions
then fail and every message names the wrong defect:

- 4g's `*'timeout 9s'*` case prints "GATE_JOBS suppressed the row's OTHER knob — the override is not
  width-only". False; the override is fine.
- 4h prints "a leg that outlived the per-leg timeout was not reported FAILED with a timeout tail".
- 4h prints "a timed-out leg did not make the run RED — a timeout must never read as a skip or a
  pass".

This canary ships as a merge-bar leg, so an adopter on a macOS/BSD base install or a minimal image
gets a red bar blaming the runner's override and timeout logic for a host capability the runner
explicitly supports. Symmetrically, `INERT` appears only in `run-gates.sh` — no arm in
`run-gates.test.sh`, `.gov.test.sh` or `.evidence.test.sh` drives that branch.

**Fix.** Probe once and use this file's own convention for the case, a loud counted SKIP (arms 4b and
4e both do it): `if timeout 1 true >/dev/null 2>&1; then <4g/4h as written>; else echo "canary: SKIP
arms 4g/4h — no working timeout on this host; the runner's INERT branch is what runs here"; fi`, with
the `n=$((n+1))` increments outside the branch so the executed total does not move with host
capability.

**Left-shift gate.** Add the missing arm for the degradation itself using arm 4k's PATH-shim pattern
(the AC13 mechanism): a `$P/shim/timeout` exiting 127, a row asking for `timeout=1`, and assertions
that the run states the knob is INERT and still completes GREEN with every leg run.

### M3 — `GATE_PROFILE` is silently dropped when the table is absent

`tools/run-gates/run-gates.sh:225-236` (the else branch; reported at `:233` and `:234`) · merges raw
findings 5 and 12.

The fallback branch calls `det_cores` / `det_ram`, computes the built-in width, and hardcodes
`PROF_TAG="built-in default"` without ever reading `GATE_PROFILE` — the variable is consulted only
inside the `[ -f "$PROFILES" ]` branch. Reproduced:

```
$ GATE_PROFILES=fx/nope.txt GATE_PROFILE=capable bash tools/run-gates/run-gates.sh
gate profile: built-in  (cores 16 via nproc, ram 32692 MB via getconf; width 8, timeout off; built-in default)
… exit 0
```

The operator pinned a profile, got a different width, and nothing on stderr or in the durable
visibility line says the pin was dropped. The identical operator error is *fatal* in the other state:
`GATE_PROFILE=nosuch` against a present table exits 2 with `names no row. Declared rows: …`. So one
typo in `GATE_PROFILES`, or an exported `GATE_PROFILE` surviving the documented table-deletion
rollback, turns a refusal into an invisible no-op. It contradicts this same block's stated rule at
`:194` ("A silently ignored knob is a knob the operator believes they set, so an unknown key
REFUSES") and the rule five lines later at `:238` ("A knob the operator set and the host cannot
honour is worse than no knob: say so rather than run inert"). The visibility line already discloses
the sibling override — `PROF_TAG` appends `, GATE_JOBS` at `:262` — so the omission also breaks a
convention inside the same block.

**Fix.** Warn rather than refuse; refusing would block the documented rollback for anyone with
`GATE_PROFILE` in their environment. After `PROF_TAG="built-in default"`:

```sh
[ -n "${GATE_PROFILE:-}" ] && { echo "run-gates: GATE_PROFILE='${GATE_PROFILE}' is set but no profile table exists at $PROFILES — the built-in formula is in force and the request is IGNORED" >&2; PROF_TAG="$PROF_TAG, GATE_PROFILE ignored"; }
```

so the dropped request appears on stderr *and* on the durable line.

**Left-shift gate.** Arm it beside 4f, which already drives this branch for AC6: run
`GATE_PROFILE=any GATE_PROFILES=definitely/absent/…` and assert the run still completes GREEN with
every leg AND that the visibility line carries the `GATE_PROFILE ignored` tag. AC6 as written grades
only that the fallback runs, so it passes today.

### M4 — declared thresholds and knob values get a digits check with no length bound

`tools/run-gates/run-gates.sh:193` and `:199` · merges raw findings 6, 14, 17.

`num_ok` (`:139`) carries a 15-digit bound and its own header argues the reason: `[ "$v" -gt 0 ]` and
`$(( ))` ERROR on an int64 overflow instead of comparing, "which is how a 20-digit width value once
span the dispatch loop forever having executed ZERO legs". AC12 arms that bound on the `GATE_CORES` /
`GATE_RAM_MB` seams, and `JOBS` gets its own `?????*` clamp — but the row validator two functions
below is digits-only, so the DECLARED half of the same comparison is unbounded. Both halves reproduce
against the real runner:

- A row declaring `timeout=99999999999999999999` produces `run-gates.sh: line 239: [:
  99999999999999999999: integer expected`, again at `:266`, and once per leg at `:330`; the
  visibility line reports `timeout off` and the run exits 0 GREEN. The declared knob is silently
  dropped — the exact failure mode this block refuses by name for an unknown key — and the INERT
  warning at `:239` is itself disabled by the same failing test, so nothing announces it. The
  operator sees bash internals instead of the runner's own `$PROFILES:$ln:` refusal.
- A row declaring a twenty-digit core threshold errors at `:205`, silently fails to match, and drops
  the run to the catch-all with no refusal.

`width` escapes only by accident, because the pre-existing `?????*` clamp catches it downstream. No
verdict is wrong in either case, which is why this is medium and not high — but the visibility line
gives a *wrong* answer (`timeout off` beside a table that declares a timeout) rather than a missing
one, and a pinned timeout silently becoming `off` is exactly the state B1's fix is supposed to make
meaningful. One sub-claim from the raw report does not hold and is dropped here: the bash diagnostics
are **not** persisted into `<git-dir>/gate-logs/` or `gate-last-summary.txt` — the leg log holds only
the header and the leg's own output, and the noise goes to the runner's stderr.

**Fix.** Reuse the bound that already exists. At `:193` add
`{ [ ${#pcores} -le 15 ] && [ ${#pram} -le 15 ]; } || prof_die "$PROFILES:$ln: threshold too long to
compare (max 15 digits): '$pcores', '$pram'"`, and at `:199` add the same `[ ${#v} -le 15 ]` test to
the knob value before accepting it. `timeout=0` must stay legal.

**Left-shift gate.** Two fixture rows in arm 4i, which already owns the malformed / unknown-knob /
no-catch-all refusal set: a twenty-digit `timeout=` and a twenty-digit threshold, each asserting exit
2 with the `file:line` refusal. The fixture is load-bearing — against the shipped table both cases are
unreachable, so an arm driving the real table would pass by finding nothing, the class AC12c already
records for the catch-all case.

### M5 — `det_ram` reads host memory, never the cgroup limit, so the RAM guard cannot fire in a container

`tools/run-gates/run-gates.sh:157-175`.

The whole chain is `getconf _PHYS_PAGES * PAGESIZE`, then `/proc/meminfo MemTotal`, then
`sysctl hw.memsize`. All three report host physical memory inside a cgroup v1 or v2 memory-capped
container; the enforced limit lives at `/sys/fs/cgroup/memory.max` (v2) or
`/sys/fs/cgroup/memory/memory.limit_in_bytes` (v1) and nothing reads either.

The RAM threshold is the table's entire reason to exist — `gate-profiles.txt:124` states the
motivating case as "a 16-core / 8 GB VM used to select width 8 and thrash", and arm 4b calls it "the
whole reason this table exists". A CI runner pinned to 4 GB on a 64-core / 512 GB host, where `nproc`
commonly still reports the host count absent a cpuset, reads as 64 cores / 512 GB, selects `capable`,
and runs eight concurrent scratch-repo legs in 4 GB. That is the exact thrash the guard was written
for, in the environment the bar is scheduled to move to (`AGENTS.md` records CI wiring as a follow-up)
and in the most likely shape of an adopter's tree — the kit ships this detection chain, `kit.toml`
takes `include="**"` and LF-pins `{kit}/gate-profiles.txt`.

Nothing in the tree declares containers out of scope: a grep for `cgroup|container|docker` across
`tools/` and this build folder returns zero relevant hits, and the spec's Detection section (lines
83-92) enumerates exactly those three sources with no limitation noted. The failure is silent in the
worst way — the visibility line prints a confident `ram <host> MB via getconf` rather than the UNKNOWN
state the same function already produces one branch earlier for its page-truncation case.
`GATE_RAM_MB` and `GATE_PROFILE` are workarounds but appear in neither `gate-profiles.txt`'s OVERRIDES
block nor the README, so an operator cannot find them.

**Fix.** Add a cgroup source at the head of the chain, before `getconf`: read
`/sys/fs/cgroup/memory.max` then `/sys/fs/cgroup/memory/memory.limit_in_bytes`, treat the literal
`max` and any value failing `num_ok` as unknown, convert to MB, and take the **minimum** of it and the
host reading rather than replacing it — a v1 sentinel of 9223372036854771712 must not win. Name it in
`RAM_SRC` like the others so the line still reports the chain walked.

**Left-shift gate.** Drive it with a fixture file through a shimmed root path, the way AC13's PATH
shim drives the detection chain: a fixture `memory.max` holding a small value against a host reading
of 32 GB must select the low-RAM row, and a fixture holding `max` must fall through to the host
reading. Without a seam the source is untestable and will rot.

## Low

### L1 — the unit edited a file its own spec lists as a non-goal and another open unit claims

`memory/guides/SESSION-KICKOFF.md:77`.

`git diff HEAD~2..HEAD -- memory/guides/SESSION-KICKOFF.md` shows this unit rewrote line 77 — the
`bash tools/run-gates/run-gates.sh` line inside the "### Gate commands (the merge bar)" fence — plus
both the `last-audit` and `last-body-change` stamps. Spec-2 §3 (lines 46-47, still present at rev-5,
which this same commit set edited) reads verbatim: "Editing `memory/guides/SESSION-KICKOFF.md`.
`TOOL-aPacedTurnstile-3` owns that file's gate-command block; two units editing three shared lines is
the collision this build's reconcile pass caught." Spec-3 is still OPEN (rev-7) and its S9 at line 57
claims "This unit owns that BLOCK for this build", enumerating the file's editors as exactly `-3`,
`-1` and `-7`, and closing with "TOOL-aPacedTurnstile-2 §3's non-goal already used this narrower
wording".

The engineering edit is defensible — the old "(width min(8,nproc))" text is falsified by this very
unit, and the runner is on the manifest's `watch:` list so the stamp move is forced by the ratchet.
What is wrong is that the record was not reconciled: rev-5 was appended in the same commit about a
different design decision. Two false records now survive inside the build folder the merge bar
validates, and unit 3 will rebase onto a rewritten line 77 plus moved stamps.

**Fix.** Rev spec-2 to move the gate-command line out of §3's non-goals (it is charter-mandated once
the width claim went stale), correct spec-3's three-editor map, and record the hand-off in
`memory/builds/aPacedTurnstile/README.md`. Alternatively revert line 77 and keep only the `last-audit`
re-stamp, leaving unit 3 owning the block it declared.

**Left-shift gate.** No new gate; this is the documented-check half of §7. The reusable rule for this
build's remaining units: when a fix falsifies a literal, grep the changed literal across the spec set
before committing, rather than re-reading only the finding's own carrier list — the same sweep the
round-4 review of unit 1 recommended for exactly this residue pattern.

### L2 — the runner and its own canary disagree about what a comment line is

`tools/run-gates/run-gates.sh:189` against `tools/run-gates/run-gates.test.sh:562`.

The runner skips only `''|'#'*`, i.e. `#` at column 0. Arm 4e strips `^[[:space:]]*(#|$)`. On the same
two-line table the canary's expression cleanly strips an indented `# an indented note` while the
runner exits 2 with `gate-profiles.txt:2: malformed profile row (expected name, min cores, min RAM MB,
knobs)`; a line of three spaces produces the identical refusal. So the whole merge bar dies on a table
edit the shipped file's own header invites ("Comments carry the justification for a threshold and
every movement of it"), and the refusal message never says the word column or indentation,
misdirecting whoever hits it toward the field count. Arm 4e is the one arm whose subject IS that
file's content, and it and the parser disagree about which lines are even rows.

Low because it fails loud, names `file:line`, and no verdict can be wrong.

**Fix.** Make the runner match the canary, which is the looser and safer of the two: strip leading
blanks before the case, or `case "${pname#"${pname%%[! ]*}"}" in ''|'#'*) continue ;; esac`.

**Left-shift gate.** A fixture row in arm 4i proving an INDENTED comment and a whitespace-only line
are skipped rather than refused, which joins the two readers so they cannot drift apart again.

### L3 — recorded for the fold: three more carriers of B1's false claim

`tools/run-gates/run-gates.sh:326-329`, `tools/run-gates/gate-profiles.txt:13` and `:21`,
`memory/map/features/run-gates.md:70`.

Not an independent defect — it is B1's prose surface, listed separately so the fold sweeps all four
carriers rather than only the code. If B1 is fixed, all four become true and need no edit. If B1 is
deferred, all four must be softened to what the code actually delivers: "a leg that outlives the
budget is reported RED naming itself" is true, "converts an unbounded hang into a bounded RED" is not.
The map dossier is the carrier most likely to be missed.

## Against the contract

Every AC1–AC13 arm exists and passes. Four of them pass on code that does not deliver the claim:

- **AC8** is satisfied by B1's broken code — it grades the message and the verdict, never the clock.
  It needs the elapsed-time half.
- **AC11b** is satisfied while two live copies of the retired formula ship inside the kit (M1). The
  criterion scoped itself to the charter and the arm followed it; the class needed the kit dir.
- **AC12** is satisfied while the declared half of the same comparison is unbounded (M4). The
  criterion names the hardware seams only.
- **AC6** is satisfied while `GATE_PROFILE` is silently dropped on that same path (M3).

## The three hunted classes

- **fixture-passes-by-finding-nothing** — found, twice. Arm 4h asserts the timeout's message and not
  its bound (B1), and AC12's length-bound arm covers the seams but not the declared values (M4). The
  build was already alert to this class — AC12c calls its fixture "load-bearing" for exactly this
  reason — and it recurred one level over, in the arms that shipped with the same commit.
- **two-answers-to-one-question** — found, in M1 (`min(8, nproc)` in the runner header and the shipped
  README against the table that now owns the width), in L2 (two definitions of a comment line), and
  pending in L3 (four carriers of one timeout claim).
- **heredoc-escape-reaches-the-regex** — hunted, not found. The new canary arms write their fixture
  tables with `printf` and single-quoted format strings, and the heredocs in arm 4h and its successor
  use quoted delimiters, so no expansion reaches a pattern. Reported as a clean scan of a small
  surface, not as coverage.

## Landing order

1. Fix B1 and re-run arm 4h with the elapsed assertion added. Nothing else in this list blocks.
2. Fold M1–M5 with their gates; M1 and M3 are a one-line edit plus one arm each.
3. Reconcile the spec-2 non-goal and the spec-3 editor map (L1) before unit 3 rebases onto line 77.
