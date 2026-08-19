# Spec audit — TOOL-aPacedTurnstile (units 1-7)

**Serves:** spec-audit TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7

**Date:** 2026-08-18 · **Tier:** 2 · **Streams:** tooling · **Base:** `6517579`
**Targets:** the seven specs under `memory/builds/aPacedTurnstile/spec/`, pre-code, against
`memory/builds/aPacedTurnstile/README.md`, `memory/TEMPLATE-SPEC.md` and `BUILD-METHOD.md` M2/M4.
**Question asked:** does this spec set, as written, describe a bar that still refuses a bad merge
once the push boundary stops running every leg?
**Out of scope:** the five owner decisions settled at kickoff, and the defects the design-pass
reconciliation already folded in.

## Verdict: BLOCKED

Forty-four findings survived a default-refute skeptic pass: 5 BLOCKER, 25 HIGH, 13 MEDIUM, 1 LOW.

Five blockers. Three of them sit on the chain the whole build rests on — `TOOL-aPacedTurnstile-5`
writes `gate-full-green`, `TOOL-aPacedTurnstile-7` reads it and scopes the authoritative run on the
strength of it. The precondition that matters most on that record, "the run failed nothing", has no
acceptance criterion in either spec (F3), and nothing on either side requires the recorded green to
have been earned on a clean tree (F5). Separately, `TOOL-aPacedTurnstile-5` S1 moves the per-leg
`.rc` files from a per-run `mktemp -d` to a fixed path, and those files are the dispatch suppressor
and the verdict, not a log (F2). The remaining two blockers are set-level: `-1` and `-4` both claim
ownership of the same `kit.toml` gate-leg row and `-1` lands first (F1), and `TOOL-aPacedTurnstile-6`
has no position in the README's build order at all while it changes the base every guard diffs
against (F4).

The dominant HIGH theme is criteria that cannot fail. Three separate lenses landed on
`TOOL-aPacedTurnstile-2` AC11, whose negative grep already returns zero at `6517579`
(F9, F10, F11); `TOOL-aPacedTurnstile-7` AC7's negative half is vacuous for `AGENTS.md` for the same
line-wrapping reason (F27); `TOOL-aPacedTurnstile-5` AC11 asks `govkit.py selfcheck` to observe two
things it does not read (F20); and three of the five forcing predicates in `-7` are armed only by
"observes `GATE_FULL=1`", which predicate 1 also yields (F28). Against that sit six scope items with
no criterion at all: `-1` S4, `-2` S2, `-3` S2, `-3` S9, `-4` S4 and `-7` S5.

The second theme is joins between siblings that do not resolve. `-3` AC7 and AC8 read a
`<git-dir>/gate-run/header` field no unit writes (F12, F13, F14); `-5` AC12 and `-3` AC11 assert
assertion counts for two harnesses `-1` S11 keeps waived (F21); `-5` S8 and `-6` §4 both own the
`impure` values with different provenance (F41); `-1` S12 claims a map key that `-4` does not create
until four units later (F31).

Two findings are prior-art misses rather than internal contradictions. `-4` AC1/AC2 reintroduce the
interval-intersection arm `TOOL-cSteadyMetronome-1` refuted by name, and `-4` §10 records that the
reuse probe returned no prior runtime-lock record (F18). `-6` S5 adopts a merge-base form whose
local-branch fallback resolves to HEAD, which is the class `TOOL-cFinalBerth-2` already landed (F23).

## Findings

#### F1 · BLOCKER · TOOL-aPacedTurnstile-1 §2 S6 and §4 Files touched — two units write the same fifth gate-leg row

`-1` S6 writes `kit.toml` with five `[[gate_leg]]` rows and §4 Files touched gives
`tools/gate-legs.json` "three new legs". `-4` S10 then registers `run-gates.turnstile.test.sh` "in
the manifest and in the kit's descriptor", and `-4` §4 calls that "the fifth gate-leg row". `-1`
lands first of seven; `-4` lands fifth.

Only four legs exist for this kit at `-1`'s landing: the two repointed rows (`run-gates canary` and
`run-gates evidence`, verified as the only run-gates legs in `tools/gate-legs.json` and the only two
exempt-leg rows in `tools/govkit/registry.toml`) plus S7's adopter e2e and its `--check`.

- **Breaks:** `govkit.py` selfcheck 7h fails with `entry '<id>' declares gate leg '<name>', which is
  in no leg of tools/gate-legs.json`, so five descriptor rows red `-1` AC3 at `-1`'s own landing.
  Adding the manifest leg instead — the unexplained "three new legs" — reds the bar on a script that
  does not exist for four more units.
- **Fix:** `-1` S6 declares four `[[gate_leg]]` rows and §4 says "two new legs". `-4` S10 keeps sole
  ownership of the turnstile row in both carriers and `-4` §4 calls it the fifth.

#### F2 · BLOCKER · TOOL-aPacedTurnstile-5 §4 Design and §2 S1 — a fixed `.rc` path turns a stale file into a false GREEN

Moving the per-leg completion files from the per-run `mktemp -d` to the fixed `<git-dir>/gate-run/`
converts a leftover `.rc` into a green verdict, and §4 never states the "exactly one live writer, and
the clear always succeeds" precondition it depends on.

Verified in `tools/run-gates.sh`: line 84 makes `$WORK` unique per run (`mktemp -d`, hard `exit 2` on
failure), so no leaked writer and no failed cleanup can reach a later run. The `.rc` file is not a
record — line 186 (`{ [ -z "${names[$k]}" ] || [ -f "$WORK/$k.rc" ]; } && continue`) never dispatches
a leg whose `.rc` already exists, and lines 189 and 162-166 report whatever that file holds.

- **Breaks:** at a fixed path a pre-existing `<i>.rc` containing `0` means the leg never runs and the
  bar prints `GATE ok`. Two sibling units create exactly the writers that outlive a run: `-3` S5
  kills live workers at a chunk boundary and `-2` S5 adds a per-leg timeout. S1's "cleared at the
  START of each run" also has no failure branch where the `mktemp` it replaces has one, so a clear
  that partially fails on Windows (open handle, AV lock) inherits the previous run's verdicts. §6 has
  no criterion that a pre-existing `.rc` is refused; AC3 only counts rows after a completed run.
- **Fix:** keep the per-run uniqueness — write to `<git-dir>/gate-run/<run-id>/` with a fixed
  `<git-dir>/gate-run/current` pointer for the in-flight reader — or make the start-of-run clear a
  hard refusal in the shape of line 84. Add an AC: a planted `<git-dir>/gate-run/3.rc` containing `0`
  must not be reported as that leg's verdict.

#### F3 · BLOCKER · TOOL-aPacedTurnstile-5 §2 S7 and §6 AC7–AC9 — the "failed nothing" precondition on `gate-full-green` is unarmed

`gate-full-green` has four preconditions: failed nothing, skipped nothing, reused nothing, tree
unmoved. Three are armed — skipped by AC8, tree-moved by AC9, reused by `-6` AC11. The first has no
acceptance criterion in either spec.

- **Breaks:** an implementation that writes the file on `skips==0 && reused==0 && !tree_moved` and
  forgets the fails check passes AC7, AC8, AC9 and `-6` AC11 unchanged. `-7` then reads that file,
  finds a fresh ancestor green, and scopes the next landing on the strength of a RED run. This is the
  single fact the push-boundary inversion rests on and it is the only precondition with no negative
  control.
- **Fix:** add to `-5` §6: when a run reds, `<git-dir>/gate-full-green` is neither written nor
  updated, asserted in `tools/run-gates/run-gates.evidence.test.sh` against a pre-existing file from
  an earlier green, so the arm distinguishes not-written from not-updated.

#### F4 · BLOCKER · TOOL-aPacedTurnstile-6 §4 Rollout — the unit has no position in the README's build order

The README's chain `-1 → -2 → -5 → -3 (runner) → -4 → -7 → -3 (manifest reorder)` and its edge table
never mention `-6`. The unit is in the Units table and in the front-matter `ids:`, with no position
and no edge. `-6` §4 Rollout declares its own position ("One commit after `TOOL-aPacedTurnstile-5`"),
which the README's chain does not contain.

- **Breaks:** M2's ordering axis is checked against the README's authored order, so a unit absent from
  it has no sequenced position. `-6` S5 changes the BASE that `changed()` uses, and `-7` — which is
  sequenced — consumes `changed()` and states in its §10 that it is "consumed unchanged". Whether
  `-7` lands on the origin-tip base or the merge-base base is undecidable from the record, and the
  two give different leg sets at the authoritative boundary.
- **Fix:** insert `-6` into the README chain with its forcing edges (`-5 → -6` for the ledger it
  reads, `-6 → -7` for the base `-7` inherits), or state in `-6` §3 that it lands after `-7` and why.

#### F5 · BLOCKER · TOOL-aPacedTurnstile-7 §4 Data model — a full green earned on a dirty tree resets the lag counter

The hook reads "three fields from the run record and nothing else: the sha, that run's leg-manifest
fingerprint, and a schema version". Nothing constrains the working tree the recorded green was proven
against, and `-5` S7's preconditions require only that the tree did not MOVE, never that it was
CLEAN.

`GATE_FULL=1 bash tools/run-gates/run-gates.sh` on a dirty tree is the documented developer action
and is `-7` §7's own last gate. It stamps `head=HEAD` and satisfies every predicate in `-7`'s table
for the next `GATE_FULL_MAX_LAG` commits. `-5` §4 puts a tree fingerprint into `gate-full-green`;
`-7` §4 declines to read it.

- **Breaks:** the replacement property written into `AGENTS.md` — "every leg runs against a tree that
  lands at least once every N commits" — is then false, and the record makes it look measured.
  `tools/push-main.sh` line 45 refuses a dirty tree, so the boundary itself is clean, which is
  exactly why the hole is invisible to the arms.
- **Fix:** add predicate 0 to the forcing table (the recorded `tree_fingerprint` must equal a fresh
  fingerprint of the pushed tip, else `no usable run record`), or have `-5` S7 refuse to write
  `gate-full-green` when `git status --porcelain` is non-empty. Arm it in `.githooks/pre-push.test.sh`.

#### F6 · HIGH · TOOL-aPacedTurnstile-1 §2 S4 — the kit version marker has no criterion and its named gate is vacuous

S4 adds `KIT_RUN_GATES_VERSION` with its same-line `gov:kit` marker, a README carrying the same
marker, and the paired assertion in `tools/check-kit-versions.sh`. It has no acceptance criterion,
and the §7 gate named for it proves nothing.

Verified: `tools/check-kit-versions.sh` is a hand-kept enumeration — one `need` line or one pair
block per kit, spelled literally for memory-tree, codebase-map, agent-cap, settings-merge,
unattended, memory-recall, drift-audit, pytest-parallel-guardrails, govkit and lexicon. It has no
derived population over `tools/*`.

- **Breaks:** the script exits 0 today and exits 0 if S4 is skipped entirely, so `bash
  tools/check-kit-versions.sh` in §7 grades nothing about this kit.
- **Fix:** add an AC — with the run-gates constant deleted or half-bumped,
  `bash tools/check-kit-versions.sh` exits 1 naming `KIT_RUN_GATES_VERSION`, the red-proof the
  memory-tree and agent-cap pairs already carry.

#### F7 · HIGH · TOOL-aPacedTurnstile-1 §4 and §2 S2 — the shipped canary keeps the gov-internal dependency the unit exists to remove

§4's verification enumerates one gov-internal dependency, but S1 ships `run-gates.test.sh` into the
kit and that file sources `$ROOT/tools/lib/resolve-python.sh` at line 7 for its own interpreter.

Verified: `tools/run-gates.test.sh:7-8` is `. "$ROOT/tools/lib/resolve-python.sh"` then
`PYBIN=$(resolve_python) || { echo "canary: no usable python"; exit 2; }` — structurally identical to
the runner's lines 15-16 that §4 dissects. S2 scopes the inline to the runner's source line plus the
canary's scratch-BUILDER copies at lines 68/70, 215/217 and 249/251, which are a different thing.

- **Breaks:** S8's registry surgery deletes the exempt rows, so this file becomes governed kit
  payload. AC1 proves only that `run-gates.sh` runs in a repo with no `tools/lib/`; no AC runs the
  canary there, and the repo-wide ban §4 relies on covers `command -v python3 || python`, not a
  source line. An adopter receives a kit whose own `run-gates canary` leg exits 2.
- **Fix:** paste the marker-delimited resolver block into `run-gates.test.sh` too, which enrols it in
  `resolve-python.test.sh`'s grep-derived parity population. Widen AC1 to run every `*.test.sh` the
  kit ships inside the `tools/lib`-free scratch repo.

#### F8 · HIGH · TOOL-aPacedTurnstile-2 §2 S2 — the detection chain and its length bound are never observed

AC1 asserts only that the profile line is present; AC2 and AC3 drive `GATE_CORES` and `GATE_RAM_MB`,
the seams that bypass detection entirely.

§4 names the prior failure the length bound exists for — a 20-digit width value once spun the
dispatch loop forever having executed zero legs — and both `[ -gt ]` and `$(( ))` error rather than
compare on int64 overflow. Nothing in §6 feeds an oversized or non-numeric value at the bound, and
nothing exercises `nproc`, `getconf`, `_PHYS_PAGES`, `/proc/meminfo` or `sysctl`.

- **Breaks:** the whole of S2 can ship broken with §6 green.
- **Fix:** add two ACs — a seam value of 20 digits and one non-numeric are rejected at the length
  bound and the run still completes at a clamped width; and a fixture `PATH` shim making the first
  core or RAM source exit non-zero still yields a resolved profile with its sources-tried provenance
  tag.

#### F9 · HIGH · TOOL-aPacedTurnstile-2 §6 AC11 — the negative grep already returns zero at base

AC11's negative half, `grep -c 'width min(8, nproc)' AGENTS.md` returns zero, is satisfied at
`6517579` before any code is written. Verified: `AGENTS.md:85` writes it as ``width `min(8, nproc)` ``
with a backtick between `width ` and `min`, so the unbackticked literal never matched. Measured today:
the pattern returns 0 and exits 1, while `grep -c 'min(8, nproc)' AGENTS.md` returns 1.

- **Breaks:** the criterion cannot fail whether or not S8 lands, which is the retired-arm class this
  build's own `-3` §8 refuses.
- **Fix:** grep the string that is in the file (`min(8, nproc)`), and pair it with a positive grep for
  the replacement sentence, in the shape `-7` AC7 uses.

#### F10 · HIGH · TOOL-aPacedTurnstile-2 §6 AC11 against §2 S8 — the stale-figure half of S8 has no observable at all

Second lens on AC11. Beyond the vacuous pattern, S8's other half — the stale `335s serial to ~95s at
width 8` figure at `AGENTS.md:91` — has no mechanical observable; AC11's second clause is prose with
no backticked token.

- **Breaks:** S8 can land half-done with AC11 green. This is the same defect `-7` AC7 was rewritten to
  avoid, and the sibling that fixed it did not check this one.
- **Fix:** assert `grep -c 'min(8, nproc)' AGENTS.md` returns 0 AND `grep -c '335s serial' AGENTS.md`
  returns 0, plus a positive grep for the replacement sentence naming the table file and the measured
  873 s / 4018 s pair.

#### F11 · HIGH · TOOL-aPacedTurnstile-2 §6 AC11 — the criterion leads with its vacuous half

Third lens on AC11, stated as the general defect: the acceptance criterion is satisfied by the tree
as it stands, so the charter edit could be skipped entirely and AC11 stays green. Overlaps F9 and
F10; kept because it names the correct division — the second clause ("the charter states the measured
873 s wall against the 4018 s leg-sum") is a positive assertion and does carry weight, while the
negative half the criterion leads with carries none.

- **Breaks:** a reader grading S8 against AC11 sees one green criterion covering two claims, one of
  which is unobservable.
- **Fix:** fix the pattern to the text that exists and pair it with the positive grep, so a rewording
  that is still false cannot satisfy it.

#### F12 · HIGH · TOOL-aPacedTurnstile-3 §6 AC7 and AC8 — both criteria read a header field no unit writes

Both assert dispatch order "against the dispatch order `<git-dir>/gate-run/header` carries". `-5` §2
S2 enumerates the header's keys — schema version, run id, start time, head, base and how it resolved,
tree fingerprint, manifest path and blob hash, full-run flag, resolved width, leg count, worktree
path — and dispatch order is not among them. `-3`'s own S1–S9 add nothing to the header.

- **Breaks:** the two criteria that prove chunk-major dispatch and the pole escape — the unit's core
  mechanism — name an observation that cannot be made. Neither spec owns the field, so each will
  assume the other adds it.
- **Fix:** add a scope item to `-3` writing the resolved dispatch order into
  `<git-dir>/gate-run/header` (or into the chunk roll-up S7 already owns), and add the key to `-5` §2
  S2's list so the record's key set stays single-sourced.

#### F13 · HIGH · TOOL-aPacedTurnstile-3 §6 AC7 and AC8 — `-5` owns the header and lands first, so the field must be a `-5` rev

Second lens on the same join, from the `-5` side. `-3` §2 adds no header field and `-3` §4 Files
touched does not list a `-5` record change, so no unit in the set writes what AC7 and AC8 read.
Overlaps F12.

- **Breaks:** both criteria are unobservable as written, and they are the only two that grade
  chunk-major dispatch and the pole escape, which is `-3`'s actual mechanism in S4.
- **Fix:** add `dispatch_order` to `-5` S2's key list as a rev bump on `-5`, which already writes the
  header before dispatch where `ORDER` is in scope, or restate AC7/AC8 against an observable `-3`
  owns.

#### F14 · HIGH · TOOL-aPacedTurnstile-3 §6 AC7 and AC8 — the build-time resolution is silent either way

Third lens on the same join, naming the failure mode at build time rather than the missing key. The
builder either adds an undeclared header key, so `-5`'s pinned grammar and its arms no longer
describe the file, or silently re-anchors the arms to a stdout ordering that `-3` §3 already forbids
from carrying timing. Overlaps F12 and F13.

- **Breaks:** AC7 and AC8 then pass without dispatch order having been observed at all. `-6` §8
  claims the reconcile pass checked every record field's join in both directions; this one is missing
  in both.
- **Fix:** name the field identically in `-3` and `-5`, and add it to `-5`'s header arms.

#### F15 · HIGH · TOOL-aPacedTurnstile-3 §2 S2 and §8 — "all 70 legs get an explicit chunk" has no criterion, and §8's substitute reasoning is false

§8 argues that "the contiguity arm makes an unclaimed leg visible". Per S1 a leg with no key falls
into a DEFAULT chunk. A single unclaimed leg forms a one-member default chunk, which is trivially
contiguous; two adjacent unclaimed legs likewise. AC6 passes in both cases.

- **Breaks:** a leg that silently drops out of its intended chunk loses its place in the halt ordering
  and the roll-up, and is invisible to every criterion in §6.
- **Fix:** add an AC asserting every leg in `tools/gate-legs.json` carries a `chunk` key whose value
  is in the declared six, and correct §8's reasoning to cite that arm rather than contiguity.

#### F16 · HIGH · TOOL-aPacedTurnstile-3 §4 Halting — killing the pool job does not terminate the leg

§4 states that "live workers are killed and reaped BEFORE the scratch cleanup runs". The runner has no
job control, so there is no process group to signal and the leg process and its children survive.

Verified: `tools/run-gates.sh:187` dispatches `runleg "$k" &`; line 140 runs the leg inside a command
substitution (`out=$("${argv[@]}" </dev/null 2>&1)`) within that background subshell. The script never
enables `set -m`, so every background job shares the runner's own process group — `kill -- -$$` would
kill the runner, and `kill $(jobs -p)` reaches only the `runleg` subshell, not the
`bash tools/<x>.test.sh` it is blocked on nor that script's own children.

- **Breaks:** §4's stated remedy does not fix the Windows partial-delete it is written against,
  because the handles are held by processes the kill never reached. Those orphans also keep writing
  into the now-fixed `<git-dir>/gate-run/` of F2, and `-4` AC9 ("the beacon is released after a halted
  run") would pass while the halted run's legs are still executing.
- **Fix:** record each leg's real pid from inside `runleg` before the command substitution, or via
  `exec` in a wrapper, and kill the recorded set; or enable per-job process groups with `set -m` and
  signal the group. Add an AC that no descendant of a halted run survives the halt — AC3 today asserts
  only the printed lines and the exit code.

#### F17 · HIGH · TOOL-aPacedTurnstile-4 §2 S4 — the heartbeat refresh has no criterion and no negative control

S4 refreshes the heartbeat at two existing call sites and has no acceptance criterion. Every reap AC
proves reaping HAPPENS (AC3 dead PID, AC4 stale heartbeat); none proves it does not happen to a live
run.

- **Breaks:** §4 spends a subsection establishing that a 659.9 s leg bounds the refresh gap, and the
  failure it guards against — a waiter reaping a live holder and running a second 873 s bar — is the
  unit's worst outcome. A refresh site that is wired but never fires, or fires only in the reader loop
  while workers are quiet, satisfies every existing AC.
- **Fix:** add an AC — a holder whose legs run longer than the TTL is still held at the end of the
  run, and a waiter polling across that window never claims, driven at a scaled-down TTL against a
  fixture leg.

#### F18 · HIGH · TOOL-aPacedTurnstile-4 §6 AC1 and AC2, §10 Reuse audit — interval intersection was refuted by name in `TOOL-cSteadyMetronome-1`

AC1 and AC2 assert mutual exclusion as interval intersection over leg execution windows.
`memory/builds/cSteadyMetronome/spec/2026-08-14-spec-cSteadyMetronome-1.md` §4 "Why a rendezvous and
not interval intersection" rejects that form: intersection is immune to per-leg slowdown but depends
entirely on the skew between start instants, which is almost pure process-spawn cost. The DECISIONS
row is landed: a gate asserts what the SUBJECT does, never what the NODE does. The replacement
mechanism ships at `tools/run-gates.test.sh:75-101` (`.up` announce plus `.peak`) with its negative
control at line 168.

- **Breaks:** AC2 is the load-sensitive half — it requires two unqueued runners to actually overlap,
  which a busy node can refuse, reproducing the three blocked pushes that build was written for. `-4`
  §10 records that "the probe returned no prior runtime-lock record"; a probe with `-4`'s own declared
  terms returns `TOOL-cSteadyMetronome-1` as hit 1.
- **Fix:** reuse the rendezvous preamble instead of timestamps — assert peak concurrent holders equals
  1 across the queued pair and is greater than 1 with the turnstile disabled, both written by the legs
  themselves. Cite `TOOL-cSteadyMetronome-1` in §10 and correct the "no prior record" line.

#### F19 · HIGH · TOOL-aPacedTurnstile-4 §6 AC4, §2 S5, §5 testing — the TTL arm tests a mutant, not the shipped code

AC4 arms the TTL reap branch "with the PID branch disabled". S5 specifies the shipped semantics as "a
heartbeat older than the TTL reaps regardless of PID", and §5 claims each reap branch is armed in
isolation.

- **Breaks:** the defect the TTL branch exists for is the wedged-but-alive holder
  (`TOOL-aBoundedVerdict-10`): PID live, heartbeat stale. If the shipped code nests the TTL check
  under a dead-PID branch — the most likely implementation slip — AC4 still passes with the PID branch
  disabled, AC3 still passes, and the beacon is held forever by the exact case §4 argues the second
  signal is mandatory for. The isolation the spec claims is bought by editing the implementation.
- **Fix:** restate AC4 against the unmodified runner — a holder whose PID is live and answering, with
  a heartbeat forced older than the TTL, is reaped and the recorded reap reason is the TTL rather than
  the PID. Keep the PID-disabled variant only as a supplementary arm.

#### F20 · HIGH · TOOL-aPacedTurnstile-5 §6 AC11 — `govkit.py selfcheck` observes neither thing AC11 asserts

AC11 reads: when `python tools/govkit/govkit.py selfcheck` runs, the `impure` key is accepted by the
manifest reader and the declared legs are the measured ones.

Verified: `govkit.py` reads `tools/gate-legs.json` in exactly two places, checks 7c and 7h, and
consumes only `name` and `guard`; nothing in the file mentions `impure`. "The declared legs are the
measured ones" is a fact about `-6`'s measurement pass that no program holds.

- **Breaks:** the criterion cannot fail, leaving S8 — the declaration that gates every reuse decision
  — with only AC10's pinned-key-set arm behind it.
- **Fix:** drop the govkit half. Assert instead that the runner's parser carries `impure` through to
  the reuse decision, as an arm in `run-gates.test.sh`, and record the measured leg set in the build
  ledger rather than as a gate observation.

#### F21 · HIGH · TOOL-aPacedTurnstile-5 §6 AC12 and TOOL-aPacedTurnstile-3 §6 AC11 against TOOL-aPacedTurnstile-1 §2 S11 — the assertion-count criteria contradict the waiver rows

`-5` AC12 asserts both moved harnesses report their executed assertion counts at or above their
floors; `-3` AC11 asserts the same for the canary. `-1` S11 keeps them waived — "the two repointed
rows in `memory/project/testsuite-count-waivers.txt`".

Verified: `tools/run-gates.test.sh` and `tools/run-gates.evidence.test.sh` are both rows in that
waiver file today (lines 20 and 21), meaning they print no count and pin no floor. Neither `-3` §2 nor
`-5` §2 has a scope item adding a counter to either harness.

- **Breaks:** both ACs are false as written, and making them true without deleting the rows reds the
  gate the other way — `tools/check-testsuite-counts.sh` fails with "a testsuite-count waiver names a
  suite that now complies".
- **Fix:** either drop AC12 and AC11 to "exits 0 with the repointed waiver rows intact", or put the
  counters in as a scope item in whichever unit adds them, plus deletion of the two waiver rows in the
  same commit.

#### F22 · HIGH · TOOL-aPacedTurnstile-6 §2 S5 and §3 Non-goals against TOOL-aPacedTurnstile-7 §10 — the base change is disowned by the unit that owns the boundary

`-6` §3 puts "The push boundary. `TOOL-aPacedTurnstile-7` owns it" OUT, while S5 replaces the base
`changed()` diffs against — the single input that decides which legs a scoped push-boundary run
executes. `-7` §10 states `changed()` is "consumed unchanged". Neither spec names which ref the
merge-base is taken against.

Source: `BASE=$(git rev-parse --verify -q "${GATE_BASE:-origin/${DEFBR:-main}}")` and `changed()`
diffs `$BASE`. `-6` §4 argues the change only for a diverged worktree branch and never considers HEAD
ON the default branch, which is exactly the case `.githooks/pre-push` gates — it refuses unless
`main_local` equals `HEAD`.

- **Breaks:** if the merge-base is taken against `refs/heads/<def>`, then at the push boundary
  merge-base equals HEAD, every guard's diff is empty, and all 42 guarded legs skip on the run `-7`
  just made scoped. Against `origin/<def>` it is a no-op there. The spec set does not say which.
- **Fix:** name the ref in `-6` S5 (`git merge-base HEAD "origin/$DEFBR"`), add the
  HEAD-is-the-default-branch case to §4 with the degenerate merge-base called out, and add an AC that
  a default-branch run still resolves a base behind HEAD. Or move the base change into `-7`.

#### F23 · HIGH · TOOL-aPacedTurnstile-6 §2 S5 and §4 The base — the adopted merge-base form inherits a local-branch fallback that resolves to HEAD

`tools/memory-tree/check-verdict-epoch.sh:77` is
`git merge-base "origin/$DEF" HEAD || git merge-base "$DEF" HEAD`. On the primary tree the §3 branch
guard keeps HEAD on the default branch, so when `origin/<def>` is absent — a fresh clone, or
`git init` plus `remote add`, the shape `.githooks/pre-push.test.sh` itself builds — the fallback
yields `merge-base(main, main) = HEAD`.

`tools/run-gates.sh:59-60` today leaves BASE empty in that case and `changed()` returns 0, running
every leg.

- **Breaks:** under S5 the base is resolvable and equals HEAD, so a clean tree diffs to nothing and
  every guarded leg skips. S5's "an unresolvable base still fails safe" never fires because nothing is
  unresolvable. `TOOL-cFinalBerth-2` is the landed record of this class, and `TOOL-cFinalBerth-4`
  records that the no-`origin/HEAD` silent-skip refusals scoped for it never landed. With `-7` scoping
  the push boundary this is a wrong merge verdict, not a late signal.
- **Fix:** refuse a base that equals HEAD and fall back to running everything, matching today's
  direction; take the merge-base only against a remote-observed default and never against a local
  branch. Cite `TOOL-cFinalBerth-2` and `TOOL-cFinalBerth-4` in §10, and add the arm to S6 beside the
  diverged-branch case.

#### F24 · HIGH · TOOL-aPacedTurnstile-6 §2 S8 and §6 AC10 — the impure-detection matcher is unpinned and finds nothing on the real population

The structural arm reds when a leg's script "directly calls out to the network" and carries no
`impure` declaration. Nothing in S8 or AC10 pins the matcher against the known population.

Verified: both remote-calling scripts route through a wrapper —
`tools/unattended/check-unattended.sh:32` defines `GIT() { git -c … "$@"; }` and line 228 calls
`GIT_TERMINAL_PROMPT=0 GIT ls-remote`.

- **Breaks:** a case-sensitive `git ls-remote` matcher finds zero call sites in the very files `-6` §4
  and `-7` §4 cite as motivating evidence, so the arm ships green having detected nothing, forever.
  This is `memory/gotchas/fixture-passes-by-finding-nothing.md`, and it is the one arm §5 offers as
  the bound on the mis-declared-impure risk. AC10 arms only the firing direction, on a fixture the
  author writes to match their own regex.
- **Fix:** add an anti-vacuity assertion in the shape the lexicon and playbook-parity gates use — the
  scan over the real manifest must resolve the known network-calling legs by name and print
  `DEAD PROBE` when its match set is empty. Wrapper-aware matching (`GIT` and `git`) is the concrete
  case to cover.

#### F25 · HIGH · TOOL-aPacedTurnstile-7 §2 S5 — the durable half of the forcing reason has no mechanism and contradicts §3

S5 says "the decision and its reason are printed on one line and written to the run record". There is
no mechanism and no AC, and it contradicts §3, which disowns "the run record's format, location and
writer" and says this unit "states only what it reads". `-5` §2 S2's header key set has no decision or
reason field.

- **Breaks:** the hook runs BEFORE the runner, and `-5` §2 S1 clears `<git-dir>/gate-run/` at the start
  of each run, so anything the hook writes there is deleted by the run it describes. AC2 and AC3
  observe only the printed reason, so the durable half ships unbuilt and unnoticed — and it is the
  half that makes the replacement property measurable, which is §4's whole safety argument.
- **Fix:** either pass the reason to the runner in the environment and add a `full_run_reason` key to
  `-5` §2 S2's header list, or cut the durable half from S5 and say the reason is stdout-only. Add an
  AC that reads it back from the record.

#### F26 · HIGH · TOOL-aPacedTurnstile-7 §2 S6 and §4 The decision — the cited `GOV_DEFAULT_BRANCH` shape does not exist, and the implied one is fail-OPEN

`GATE_FULL_MAX_LAG` is specced as "the shape `GOV_DEFAULT_BRANCH` already uses".
`.githooks/pre-push:27-33` does not default `GOV_DEFAULT_BRANCH`; it reads
`env_def=${GOV_DEFAULT_BRANCH:-}` and uses it only as a cross-check that can refuse, never select —
the landed decision that a classifier taking the NAME of the thing it classifies from the environment
is a fail-OPEN, not an override.

- **Breaks:** a hook-defaulted `${GATE_FULL_MAX_LAG:-10}` inverts that: the environment then decides
  coverage, and `GATE_FULL_MAX_LAG=99999` scopes every landing forever. It is also a `test`-based
  numeric comparison on env input with no clamp — the left-shift gate filed OPEN as
  `TOOL-aTimedTurnstile-8` — so a non-numeric value makes predicate 4 return non-zero and NOT force
  full, contradicting §4's "Every predicate fails toward FULL".
- **Fix:** make the lag a source constant the environment cannot supply, or validate it as a decimal
  integer and force full with reason `unusable lag` on anything else. Add the arm alongside AC5, and
  cite `TOOL-aStandingWrit-4` and `TOOL-aTimedTurnstile-8` instead of the `GOV_DEFAULT_BRANCH` shape.

#### F27 · HIGH · TOOL-aPacedTurnstile-7 §6 AC7 — the negative half is vacuous for `AGENTS.md`

Measured: `grep -rc 'only ever scope a NON-authoritative run' AGENTS.md tools/run-gates.sh` gives
`AGENTS.md:0` and `tools/run-gates.sh:1`. `AGENTS.md` hard-wraps the sentence across lines 81-82
("…can only ever scope a" / "NON-authoritative run, …") and grep is line-oriented.

- **Breaks:** half of the strengthened criterion is already satisfied at base. rev-2 added AC7's
  positive half precisely because the negative was weak; for `AGENTS.md` the negative is not weak, it
  is vacuous.
- **Fix:** match a single-line substring that survives the wrap (`NON-authoritative run`), or grep with
  the file joined. The positive half stays as written.

#### F28 · HIGH · TOOL-aPacedTurnstile-7 §6 AC4, AC5, AC6 — three forcing predicates are armed only by an observation predicate 1 also yields

AC2 and AC3 assert their reason strings (`no usable run record`, `the leg manifest is in this diff`).
AC4 (non-ancestor), AC5 (lag exceeded) and AC6 (fingerprint mismatch) assert only that
`.githooks/pre-push.test.sh` observes `GATE_FULL=1`.

- **Breaks:** predicate 1 also yields `GATE_FULL=1`. Any of these three fixtures that fails to build a
  record the hook can parse — the likely outcome, since each needs a synthetic `gate-full-green` with
  a valid schema, sha and fingerprint — falls through to `no usable run record` and the arm passes
  green having exercised none of predicates 2, 3 or 4. Three of the five forcing predicates would ship
  unarmed while §5 records the forcing table itself as the left-shift.
- **Fix:** give AC4, AC5 and AC6 their table reason strings verbatim, as AC2 and AC3 do, and add one
  arm asserting each fixture's record parses before the predicate under test is triggered.

#### F29 · HIGH · TOOL-aPacedTurnstile-7 §8 Open questions and §4 The decision — the push-main retry stops being full exactly on the merge commit

"The retry re-runs the same decision" is false once S2 lands: attempt 1's own full-green record makes
attempt 2 SCOPED, so the reconcile merge commit — the only commit in the flow whose content nobody has
ever gated — is the one that stops getting a full bar.

`tools/push-main.sh` lines 49-90 loop: fetch, `git merge --no-ff "$remote/$def"` when origin advanced,
then `git push`, which re-invokes `.githooks/pre-push` and re-runs the gate. Attempt 1 runs full on a
cold start, goes green, and `-5` S7 writes `gate-full-green` at HEAD_1. Attempt 2's tip is
`merge(HEAD_1, origin/def)`, so predicate 3 (`--is-ancestor`) passes, predicate 4's lag is origin's new
commits plus one merge — normally well under the shipped `GATE_FULL_MAX_LAG=10` — and predicates 2 and
5 are unaffected.

- **Breaks:** the run goes scoped, and its guards diff against BASE = `merge-base(HEAD_2, origin/def)`
  = `origin/def` after `-6` S5, so origin's newly landed commits sit on the base side and are invisible
  to every guard. The one tree that has never existed anywhere before is graded by the narrowest run in
  the build.
- **Fix:** force full on any push-main attempt greater than 1 (one exported line in the retry loop), or
  add a predicate forcing full when the pushed tip is a merge whose second parent is not an ancestor of
  the recorded green. Add the arm to `.githooks/pre-push.test.sh` and rewrite the §8 answer with the
  feedback loop stated.

#### F30 · HIGH · TOOL-aPacedTurnstile-7 §4 Data model — the hook never joins the recorded tree fingerprint to the pushed tip

The hook reads three fields and nothing else, so it never checks the recorded tree fingerprint against
the pushed tip. Overlaps F5, which states the same hole from the dirty-tree side; kept because the fix
here is a field join rather than a write-time precondition.

- **Breaks:** `-5` S7's four preconditions are green, nothing skipped, nothing reused, and tree did not
  move DURING the run. None requires a clean tree, and `-5` §4 explicitly puts the tree fingerprint
  into `gate-full-green` where `-7` §4 declines to read it. A full green stamped on a dirty tree
  satisfies every predicate in the table for the next ten commits.
- **Fix:** add predicate 0 — force full unless the record's `tree_fingerprint` equals a fresh
  fingerprint of the pushed tip, or unless the record asserts a clean tree at that sha. Add the AC.

#### F31 · MEDIUM · TOOL-aPacedTurnstile-1 §2 S12 and §6 AC10 against TOOL-aPacedTurnstile-4 §3 — the dossier claims a key that does not exist for four more units

`-1` S12 authors `memory/map/features/run-gates.md` "claiming the `kits` key and this build's new
gate-leg keys", and `-4` §3 relies on it. `-1` lands first; `-4`'s leg key does not exist until four
units later.

- **Breaks:** `tools/codebase-map/test_codebase_map.py` reds on "STALE CLAIMS (a dossier names a key
  that no longer exists)" as well as on unclaimed ones, so a dossier naming `run-gates turnstile`
  before `-4` registers it fails `-1` AC10 at `-1`'s own landing.
- **Fix:** `-1` S12 claims only the keys existing at its landing; `-4` S10 adds its leg's claim line to
  the same dossier, so `-4` §3's one-dossier non-goal survives, and `-4` §7 keeps
  `test_codebase_map.py`.

#### F32 · MEDIUM · TOOL-aPacedTurnstile-2 §2 S4 — the durable half of the profile line is never read back

S4 scopes the visibility line to be "copied into the durable summary and failure records"; AC1
observes stdout only. No criterion reads it back from `<git-dir>/gate-last-summary.txt` or
`gate-last-failure.txt`.

- **Breaks:** §5 observability says S4 reaches the durable records, not just stdout — that is the half
  that survives a run nobody watched, and it is the half with no observation. A stdout-only
  implementation satisfies every AC in §6.
- **Fix:** extend AC1, or add an AC — after a red run, `<git-dir>/gate-last-failure.txt` carries the
  same `gate profile: ` line, byte-equal to the one on stdout.

#### F33 · MEDIUM · TOOL-aPacedTurnstile-3 §2 S9 — the `SESSION-KICKOFF.md` edit has no criterion

S9 adds the chunk contract and the halt note to `memory/guides/SESSION-KICKOFF.md`'s gate-command
block. It has no acceptance criterion, and no gate in §7 reads that file's content. Confirmed the file
is in drift-audit's `PRODUCT_GLOBS` but no signal grades its gate-command prose.

- **Breaks:** its two siblings both arm their doc edits — `-1` AC12 via `drift_report`'s hand-kept
  signal, `-2` AC11 via grep. `SESSION-KICKOFF.md` is the file `/session-kickoff` loads, so an operator
  told nothing about the halt will read a truncated verdict list as a complete one.
- **Fix:** add an AC in the shape `-2` AC11 uses — a grep for the halt sentence and the chunk-contract
  sentence in `memory/guides/SESSION-KICKOFF.md` returns non-zero counts.

#### F34 · MEDIUM · TOOL-aPacedTurnstile-3 §4 Data model and §4 Inventory — the pole set is two legs, not one

§4 states "the total is 4018 s at width 8, so the threshold is 502 s and the pole set is exactly
`unattended driver selftest` at 659.9 s. It starts at time zero; the other seven workers run
chunk-major." The inventory table two paragraphs below gives `selftests` a measured max of 634.6 s,
which also exceeds the 502 s threshold.

- **Breaks:** the pole set is at least two legs and at most six workers run chunk-major. The singleton
  claim is load-bearing twice: it underpins "head-of-line blocking is bounded by the slowest leg IN A
  CHUNK" — the `selftests` chunk still contains a 634.6 s leg, so its verdict lands at roughly 635 s
  regardless of the pole escape — and AC8's arm will be written against whatever the spec says the pole
  set is.
- **Fix:** reconcile the two figures. State the pole set as derived rather than enumerated, name both
  legs, and re-derive the predicted per-chunk verdict times with `selftests` closing at roughly 635 s.

#### F35 · MEDIUM · TOOL-aPacedTurnstile-3 §4 with TOOL-aPacedTurnstile-5 §2 S6 — the cold-ledger run is slower than today's bar

`-5` S6 replaces `<git-dir>/gate-timings.tsv` with `<git-dir>/gate-ledger.tsv` and specifies no
migration, so the first run after `-5` lands has no durations. `-3` S4's pole escape is derived from
cached durations, so with a cold ledger the pole set is empty and the order is pure chunk-major — and
§4's own inventory puts the 659.9 s `unattended driver selftest` in `e2e`, the sixth and last chunk.

- **Breaks:** chunk-major dispatch starts that leg only after roughly the other 3358 s of leg-sum has
  been dispatched at width 8, about 420 s, pushing wall clock toward roughly 1080 s against the
  measured 873 s. The README records eleven live worktrees on node `a`, each with its own git dir and
  so its own cold first run. The observability win survives; the wall-clock claim does not.
- **Fix:** have `-5` S6 seed the ledger from an existing `gate-timings.tsv` on first read, or give `-3`
  a declared fallback pole — a `pole` boolean in the manifest, or dispatching the last chunk's members
  first when the ledger is empty. Note the cold-run cost in `-3`'s rollout either way.

#### F36 · MEDIUM · TOOL-aPacedTurnstile-3 §6 AC6 and §2 S2 — the contiguity arm is conditional on the thing it should enforce

AC6 reads "When chunks are declared, `run-gates.test.sh` asserts they are contiguous in
`tools/gate-legs.json`." S2 requires all 70 legs to carry an explicit chunk, and §8 resolves that
`rest` is not legal in gov's manifest. Overlaps F15; kept because it names the conditional clause
rather than §8's substitute reasoning.

- **Breaks:** strip or lose the chunk keys — plausible, since the manifest reorder is the build's last
  commit and rewrites every row of a file four units also edit — and all 70 legs fall into the default
  chunk, which is trivially contiguous. The arm passes, the run stays green, and the per-chunk
  reporting collapses to one verdict at the end.
- **Fix:** assert that every leg carries a `chunk` from a pinned six-name set and that the distinct
  chunk count equals that set's size, so AC6's contiguity assertion becomes unconditional.

#### F37 · MEDIUM · TOOL-aPacedTurnstile-4 §2 S8 and §6 AC7 — the queue wait bound is undeclared and only its expiry is armed

S8 specifies "a bounded wait that fails OPEN: on expiry, print loudly, drop the ticket, and run
unqueued". No value is given and no relation to any measurement is stated, while §4 anchors the TTL to
a measurement.

- **Breaks:** any bound below one full bar makes every genuinely queued run fail open and run
  concurrently — the turnstile becomes a no-op under exactly the contention it was built for, with
  three waiters needing 2×873 s. AC7 arms the expiry path, so the criterion set's only observation of
  the bound is the one that passes precisely when the unit has stopped working.
- **Fix:** declare the bound with the 873 s measurement beside it, as the TTL constant is declared, and
  add a criterion that a waiter behind a full-length holder acquires rather than expiring.

#### F38 · MEDIUM · TOOL-aPacedTurnstile-5 §4 Design and §4 Rollout against TOOL-aPacedTurnstile-4 §4 — dropping the trap leaks `$WORK` and falsifies `-4`'s premise

`-5` says the emitter is "retarget the directory, drop the trap, add a header before dispatch and a
verdict after", and its rollback is "restoring the trap". `-4`, landing two units later, says "The
existing trap is EXIT only, so terminate and hangup already leak the scratch dir today" and hangs
beacon release on widening it.

`WORK=$(mktemp -d); trap 'rm -rf "$WORK"' EXIT` still guards more than the per-leg files after `-5`:
`$WORK/timings.new` and `$WORK/timings.merged` are written there at the end of every run.

- **Breaks:** dropping the trap leaks a `mktemp` dir per run and leaves `-4` widening a trap that is no
  longer in the file, so `-4` §4's premise about existing behaviour is false the moment `-5` lands.
- **Fix:** `-5` S1 should say the trap stops covering `<git-dir>/gate-run/` and keeps covering `$WORK`.
  State the same in §4 and in the Rollout line.

#### F39 · MEDIUM · TOOL-aPacedTurnstile-5 §2 S1 and §5 — the retargeted `<i>.out` is an unredacted durable copy of every leg's output

`tools/run-gates.sh:135-142` writes two copies: the durable log goes through `redact` and
`chmod 600` (`TOOL-dNomadicAtlas-1`, with the reason in place), while
`printf '%s\n' "$out" > "$WORK/$i.out"` is the raw copy, safe today only because `WORK` is `mktemp -d`
under `trap 'rm -rf "$WORK"' EXIT` at lines 84-85.

- **Breaks:** S1 moves that raw file into the git dir and removes the trap. §5 says "the new files
  carry no command output", which is false for `<i>.out`, and no mode is stated for `gate-run/` where
  `LOGDIR` gets 700.
- **Fix:** keep `<i>.out` in the scratch dir and make durable only the TSV row, header and verdict —
  the reader already has the redacted log to point at — or route `<i>.out` through `redact`,
  `chmod 600` it and `chmod 700` the directory. Correct the §5 security line either way.

#### F40 · MEDIUM · TOOL-aPacedTurnstile-5 §6 AC11 — AC11 is an unrelated green gate

Second lens on AC11, naming the TEMPLATE-SPEC §6 rule it breaks rather than the two missing
observations. Overlaps F20.

- **Breaks:** selfcheck exits 0 today and will exit 0 whether `impure` parses or not, and `-6` §4
  states plainly that whether the self-tests reach the network is "NOT yet verified", so no gate can
  assert the declared legs are the measured ones. S10 and AC10's pinned key set is already the correct
  owner of the first clause.
- **Fix:** delete AC11 or replace it with an observation of the actual reader — a manifest carrying
  `impure` parses and the runner reports every leg, asserted in
  `tools/run-gates/run-gates.test.sh`. Move the "declared legs are the measured ones" clause into `-6`
  as a build-time measurement recorded in the ledger.

#### F41 · MEDIUM · TOOL-aPacedTurnstile-6 §4 Which legs are impure and §4 Files touched against TOOL-aPacedTurnstile-5 §2 S8 — two units write the same manifest key with different provenance

`-5` S8 puts the `impure` values in, "seeded from MEASUREMENT rather than guess". `-6` §4 says whether
the three self-tests reach those paths "is NOT yet verified, so the build measures before declaring.
Until measured, declare all four", and `-6` §4 Files touched lists `tools/gate-legs.json` with "the
measured `impure` values".

- **Breaks:** `-5` lands first, so `-6`'s "measure before declaring" is measuring values already
  committed. On M2's scope axis, `-6` §3 puts "Writing the record. That is `TOOL-aPacedTurnstile-5`"
  OUT, yet takes the declaration back in §4. Whichever lands second silently overwrites the other's
  set, and neither spec says which is authoritative.
- **Fix:** `-5` S8 seeds the four over-declared values and says so; `-6` §4 either narrows them after
  its measurement as an explicit scope item with its own AC, or drops the `tools/gate-legs.json` row
  from Files touched.

#### F42 · MEDIUM · TOOL-aPacedTurnstile-7 §2 S9 — the shipped playbook template carries the retired claim with no criterion

S9 names three carriers of the retired safety property and §4's files-touched lists all three, but AC7
greps only two: `AGENTS.md` and `tools/run-gates/run-gates.sh`.
`parallel-coding-governance.template.md` has no criterion.

Verified: the template's line 53 states "After each merge run a diff-scoped gate …; the FULL bar runs
ONCE, at the push boundary", which this unit falsifies, and the template contains no occurrence of
`GATE_FULL` or of AC7's search string, so AC7 could not cover it even if the file were added to the
grep. `check-playbook-parity.sh` is structural and its own header says a fluent paraphrase that is
subtly wrong still passes.

- **Breaks:** the template is the shipped product, so the stale claim reaches every adopter.
- **Fix:** add an AC naming `parallel-coding-governance.template.md` specifically — the old
  full-bar-once sentence is gone and the replacement names the bounded obligation. It needs its own
  string, not AC7's.

#### F43 · MEDIUM · TOOL-aPacedTurnstile-7 §7 Gates — the gate commands name pre-move paths

§7 names `bash tools/run-gates.test.sh` and `GATE_FULL=1 bash tools/run-gates.sh`, while §4 Files
touched names `tools/run-gates/run-gates.sh` and AC9 names `bash tools/run-gates/run-gates.test.sh`.
`-7` is rev-2, so post-reconciliation, and lands sixth, well after `-1` S1 moves all three files.

- **Breaks:** `-7` is the only spec in the set still carrying the old spelling — `-1` through `-6` all
  use `tools/run-gates/`. A §7 gate list is what the build runs at DoD, so the unit's own gate command
  does not exist by the time the unit lands, and §4 and §7 of one document disagree on the same file.
- **Fix:** repoint both §7 entries to `tools/run-gates/run-gates.test.sh` and
  `GATE_FULL=1 bash tools/run-gates/run-gates.sh`, and log it in §9 as a rev-3 line.

#### F44 · LOW · TOOL-aPacedTurnstile-7 §5 testing and §5 user docs — two checklist lines cite scope items that do not carry the claim

§5 reads "testing + left-shift gates — S7's arms." and "user docs — S8." S7 is the no-halt export and
declares no arms; the arms are S8. S8 is the test file and is not user docs; the docs rewrite is S9.

- **Breaks:** both checklist lines are answered by a citation that does not resolve, which is the class
  this audit is hunting one size down.
- **Fix:** S7's arms becomes S8's arms; user docs becomes S9.

## Unverified findings

None. Every finding above returned a verdict and survived a default-refute skeptic pass.
