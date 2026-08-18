# TOOL-aPacedTurnstile-2 — the runner's knobs become a declared hardware profile table

**Status:** OPEN · rev-3 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

The runner resolves its pool width from core count alone and looks at memory never, so a
16-core / 8 GB VM gets width 8 and thrashes. Replace the single hardcoded formula with a DECLARED
table that maps detected hardware to a named set of knobs, auto-selects at startup, prints what it
chose, and is overridable.

## 2. Scope (IN)

- **S1** — `tools/run-gates/gate-profiles.txt`: a tab-separated declared table, one row per profile,
  ordered most-capable-first, with a catch-all last row and `#` comments carrying the justification
  for every threshold.
- **S2** — a detection chain in the runner returning cores and RAM as positive integers or zero for
  unknown, using only primitives measured on a real box, every value length-bounded BEFORE any
  arithmetic touches it.
- **S3** — selection and precedence: `GATE_JOBS` wins for width only and keeps its current meaning;
  `GATE_PROFILE` names a row and skips detection; otherwise the first row both thresholds satisfy.
  Test seams for cores, RAM and the table path, mirroring the existing manifest seam.
- **S4** — one visibility line with a stable `gate profile: ` prefix, printed before the first leg
  verdict and copied into the durable summary and failure records, naming the selected row, the
  detected values, the resolved knobs, and a bracketed provenance tag.
- **S5** — knob application: width feeds the EXISTING clamp block unchanged, and an optional per-leg
  timeout wraps the leg exec, shipped as off in every row.
- **S6** — refusal semantics, split: an ABSENT table falls back to the built-in formula and says so;
  a malformed row, an unknown knob key, a profile name that resolves to nothing, or a table that
  matches nothing all exit 2 naming the file and the offending token.
- **S7** — new arms in the canary covering threshold matching, both overrides, the detection-failure
  path, every refusal, the timeout wrap, the built-in fallback, and a PINNED known-knob set.
- **S8** — repair the two claims this falsifies in `AGENTS.md`: the stated width formula, and the
  `335s serial to ~95s at width 8` figure, which the measurements in this build's README show is
  stale by roughly nine times.

## 3. Non-goals (OUT)

- Any knob that could turn a leg into a PASS or a SKIP. See the governing invariant below; the
  pinned knob set is what keeps it true.
- A GPU knob. Cut at kickoff: there is no float math on this bar.
- Making the bar faster on this node. At 16 cores the width is already 8 and the wall clock is
  floored at roughly 660 s by one leg, so what this unit buys here is a RAM guard on the low end and
  one declared place for every future knob to land. Stated plainly rather than dressed up.
- Sharding the heavy legs, which is what would actually move the floor. Separate build.
- Editing `memory/guides/SESSION-KICKOFF.md`. `TOOL-aPacedTurnstile-3` owns that file's gate-command
  block; two units editing three shared lines is the collision this build's reconcile pass caught.
- An exemption row for the table. It lands inside the kit directory, which the kit's own file rule
  already claims, so a row would be a stale exemption the deployer's selfcheck reds on.

## 4. Design

### The governing invariant

**No knob may ever turn a leg into a PASS or a SKIP.** A knob may make the bar slower, and it may
turn an unbounded hang into a bounded RED. It may never make the bar check less. There is therefore
no coverage carve-out in the shipped code, and the canary pins the knob set so the next knob cannot
be added without an author reading the rule.

### Data model

The grammar follows `tools/template-size-limits.txt`, which is this tree's settled answer to "a
declared value with its history beside it": tab-separated, `#` comments carrying the reasoning, read
with `awk -F'\t'`. Fields are name, minimum cores, minimum RAM in MB, and a comma-joined knob list.

Rows are ordered most-capable-first and the FIRST row whose both thresholds are satisfied wins. The
last row is a zero-threshold catch-all, so an unknown-hardware run lands there by ordinary threshold
matching — one selection mechanism, no special case.

Three rows ship. The capable row requires 8 cores AND about 24 GB, because cores alone are the wrong
question: the runner's own header records that each heavy leg builds its own scratch repo, so width
8 means up to eight scratch git repos and eight interpreters resident at once. The threshold is set
below 32 GB deliberately — the honest distinction is a RAM class, not an exact figure. The middle
row is the owner's 4-core class and is deliberately behaviour-neutral, because the built-in formula
already yields that width there; the table's job on the low end is to stop a high-core, low-RAM box
from selecting the capable row. The catch-all is also the detection-failure row and takes a width of
2 rather than 1, because unknown hardware is slow rather than serial-only.

Every shipped row sets the per-leg timeout to off. Nobody has measured a 660 s leg on a 4-core box,
so shipping a number would be inventing certainty; the mechanism ships proven by a fixture and
turning it on later is a one-field edit.

### Detection

Every source is RUN and its output validated, never probed for existence — the lesson
`tools/lib/resolve-python.sh` records, that being on PATH is not evidence, applies verbatim to
`getconf` and `sysctl`. Cores are read from `nproc`, then `getconf _NPROCESSORS_ONLN`, then the
Windows environment variable. RAM is read from `getconf _PHYS_PAGES` times `PAGESIZE`, then
`/proc/meminfo`, then the macOS `sysctl` key.

The ordering is not a guess. Measured on node `a`: the three core sources all report 16; the page
arithmetic gives 32693 MB and `/proc/meminfo` gives 32692 MB, agreeing within 1 MB; `sysctl` exits
127, which is the case the chain must survive and does.

Every value passes a LENGTH bound before any arithmetic. Both `[ "$v" -gt 0 ]` and `$(( ))` ERROR on
an int64 overflow rather than comparing, which is exactly how a 20-digit width value once span the
dispatch loop forever having executed zero legs. The page arithmetic divides the page size before
multiplying so the product stays small, and guards the truncation-to-zero case rather than silently
reporting no memory.

### Fail-safe direction

Detection failure must reduce SPEED, never COVERAGE, and the two knob classes fail in opposite
directions. A wrong width costs wall clock and nothing else — the runner already says this knob can
never skip a leg, and already clamps garbage to 1 rather than refusing — so failing small is safe:
slow and complete. A coverage knob would make an undetectable box quietly check less, which is the
green-by-absence class every registry here is written against, so no such knob ships.

The timeout sits between the two and is classified honestly: a timeout that fires produces a RED
naming its leg, never a skip and never a green. It converts a hang into a verdict, which is a
coverage improvement — `TOOL-aBoundedVerdict-10` records a leg hanging with zero output at 240 s and
wedging the whole bar at 46 of 65.

| condition | outcome |
|---|---|
| table absent | built-in formula, timeout off, line tagged as the built-in default |
| detection returns unknown | catch-all row by ordinary matching, line tagged with the sources tried |
| row malformed | exit 2, naming file and line number |
| unknown knob key | exit 2, naming the key |
| profile name resolves to no row | exit 2, listing the names that do exist |
| no row matches at all | exit 2 |

An absent table is not a refusal because the runner is becoming a deployable kit and an adopter may
take it without the table. A malformed one IS, because the operator declared something the runner
cannot honor. A silently ignored knob is a knob the operator believes they set.

### Selection and override interaction

The width override does NOT suppress the rest of the profile: the row is still selected and still
supplies the timeout. The implementation is one line sitting directly above code that does not move,
which is the compatibility argument — the int64-overflow fix and its arm keep working because
nothing beneath them changes.

### Visibility

One line with a stable prefix, before the first leg verdict, carrying the selected row, the detected
cores and RAM, the resolved knobs, and a provenance tag distinguishing a detected selection from an
explicit profile, an explicit width, the built-in default, and a detection failure. Any parenthesised
tail on this line follows `TOOL-aPacedTurnstile-1`'s two-space contract.

### Rollout

One commit. The rollback is deleting the table file, which the absent-table path already handles by
falling back to today's behaviour — so the rollback is exercised by an arm rather than hoped for.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/gate-profiles.txt` | new — the declared table |
| `tools/run-gates/run-gates.sh` | detection, selection, the visibility line, the timeout wrap |
| `tools/run-gates/run-gates.test.sh` | S7's arms, and a named filter of the new line in the existing equivalence arm |
| `tools/run-gates/kit.toml` | the table declared as a kit seed file |
| `AGENTS.md` | the width formula and the stale timing figure |

### Alternatives rejected

- **Detect and compute a width in code, with no table.** Rejected: the owner asked for something
  extensible to knobs beyond width, and a formula has nowhere for a second knob to live.
- **A conf file in the repo root.** Rejected: the runner is becoming a kit, and a root file would
  need an exemption row that the kit's own file rule makes stale.
- **Ship a non-zero timeout now.** Rejected: unmeasured on the hardware it would protect.

## 5. Production-readiness checklist

- security — the table is read-only data inside the kit; a hostile table can only slow the bar or
  refuse it, never reduce coverage, which is the invariant above.
- perf / scale — detection is at most six short command substitutions, once per run.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English in shell.
- error / empty / loading states — the absent-table and detection-unknown paths ARE the empty
  states; both are tagged in the visibility line and both carry arms.
- observability — S4 is the observability, and it reaches the durable records, not just stdout.
- risks (concurrency, data-loss, rollback hazards) — none new; the knobs schedule work and bound
  failures, and neither writes anything.
- testing + left-shift gates — the pinned knob set left-shifts the invariant: a coverage knob cannot
  be added without an arm going red.
- migration / rollback — deleting the table restores today's behaviour, and an arm proves it.
- user docs — S8, plus the table's own header comments.

## 6. Acceptance criteria

- **AC1** — When the runner starts, it prints one line beginning `gate profile: ` before the first
  `GATE ` line, and `bash tools/run-gates/run-gates.test.sh` asserts that line is present.
- **AC2** — When `GATE_CORES=16` and `GATE_RAM_MB=32000` are set, the canary observes the
  most-capable row selected; when `GATE_CORES=16` and `GATE_RAM_MB=8000` are set, it observes the
  middle row — the RAM guard, which today's formula cannot express, is the assertion.
- **AC3** — When `GATE_CORES=0` and `GATE_RAM_MB=0` are set, the canary observes the catch-all row
  and a provenance tag naming the sources tried.
- **AC4** — When `GATE_PROFILE` names a row that does not exist, the runner exits 2 and lists the
  row names that do — asserted in `tools/run-gates/run-gates.test.sh`.
- **AC5** — When a table row carries an unknown knob key, the runner exits 2 naming that key,
  asserted in `tools/run-gates/run-gates.test.sh`.
- **AC6** — When `GATE_PROFILES` names a path that does not exist, the runner completes normally,
  tags the line as the built-in default, and every leg still runs — the rollback path, asserted.
- **AC7** — When `GATE_JOBS` is set alongside a selected profile, the canary observes the width
  taken from `GATE_JOBS` AND the timeout still taken from the row, proving the override is
  width-only.
- **AC8** — When a fixture row sets a one-second timeout and a fixture leg sleeps past it, the
  runner reports that leg FAILED with a timeout tail and the overall verdict is RED — never a skip
  and never a green, asserted in `tools/run-gates/run-gates.test.sh`.
- **AC9** — When a knob key is added to the table without being added to the canary's pinned set,
  `bash tools/run-gates/run-gates.test.sh` exits non-zero naming the unpinned key.
- **AC10** — When the existing width-1 against width-4 equivalence arm runs, it filters the
  `gate profile: ` line BY NAME and a companion arm asserts the line was present to filter, so the
  filter cannot hide the line disappearing.
- **AC11** — When the charter is read after this lands, a POSITIVE search finds the measured pair —
  873 s wall against the 4018 s leg-sum — in `AGENTS.md`, and finds no surviving `335s` or `95s`
  figure. Stated positively because the negative half alone is already true at this build's base: the
  charter backticks its width formula, so a plain `grep -c` for the bare formula returns zero today
  and would pass unchanged.
- **AC12** — When a hardware seam is given a twenty-digit value or a non-numeric one, the length
  bound rejects it, the run still completes, and every leg still runs at a clamped width — asserted
  in `tools/run-gates/run-gates.test.sh`, because that bound is the guard against the int64-overflow
  hang and nothing else observes it.
- **AC13** — When a fixture `PATH` shim makes the FIRST core source and the FIRST RAM source exit
  non-zero, the runner still resolves a profile and tags the line with the sources it tried —
  asserted in `tools/run-gates/run-gates.test.sh`. The seams that bypass detection cannot prove the
  detection chain works, which is what AC2 and AC3 alone were doing.

## 7. Gates

`bash tools/run-gates/run-gates.test.sh` · `bash tools/run-gates/run-gates.evidence.test.sh` ·
`bash tools/check-testsuite-counts.sh` · `bash tools/check-playbook-parity.sh` ·
`python tools/govkit/govkit.py selfcheck` · `python tools/codebase-map/test_codebase_map.py` ·
`bash tools/memory-tree/check-memory-hygiene.sh` · `python tools/drift-audit/drift_report.py --check`.

## 8. Open questions

none — the forks below are RESOLVED. Every pick is the M3 ratification of the fork's own
recommendation; the reason each survived the veto order is recorded with it.

- **Whether the middle row should differ from the built-in formula at all.** It is behaviour-neutral
  as specced, which makes it easy to review and easy to call pointless. Recommendation: keep it
  neutral. Its purpose is the RAM threshold that stops a high-core, low-RAM box selecting the
  capable row, and changing the 4-core width at the same time would confound the one measurement
  that matters.
  RESOLVED (agent, 2026-08-18, delegated): keep it behaviour-neutral. Moving the 4-core width in
  the same unit would confound the RAM-threshold measurement that is the row's whole purpose,
  and a knob whose first landing is also its first behaviour change has no control.
- **Whether the per-leg timeout ships in this unit or waits for a measurement.** Recommendation:
  ship the mechanism with every row at off, proven by a fixture. `TOOL-aBoundedVerdict-10` is an
  observed hang that wedged a whole bar, so the mechanism has a recorded motivating failure even
  though the value does not yet have a measurement.
  RESOLVED (agent, 2026-08-18, delegated): ship the mechanism now, every row's value OFF, proven
  by a fixture. This is the more feature-rich option under M3 - it satisfies the stated
  acceptance criteria and leaves no follow-up open - and it survives every veto, because an
  off-by-default knob widens no surface. `TOOL-aBoundedVerdict-10` is the recorded hang that
  motivates the mechanism; the VALUE still waits for a measurement, which is what off means.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the spec audit: AC11 restated positively, since its negative half was
  already satisfied at this build's base (F9, F10, F11); AC12 and AC13 added, because the detection
  chain and its length bound were specified and never observed — both existing criteria drove the
  bypass seams instead (F8).
- rev-3 · 2026-08-18 · swept section 8 under the standing mandate: every fork RESOLVED in
  place per M3, and the section's first non-blank line made machine-legal so the classifier
  reads this unit as READY instead of FORKED.

## 10. Reuse audit

The seam this extends is `tools/template-size-limits.txt` — a declared, tab-separated value table
with its justification in `#` comments, read with `awk -F'\t'`, and outranking the environment. This
unit copies that grammar rather than inventing a second one. The width clamp in
`tools/run-gates/run-gates.sh` is consumed unchanged, with the profile value supplied as its default
so the int64-overflow fix beneath it does not move. The test seams mirror the existing `GATE_LEGS`
manifest seam, which is already the canary's way of driving the runner without re-entering the real
bar. Detection reuses no seam: nothing in this tree reads hardware today, and that absence was
verified by grepping for the candidate primitives across `tools/`.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL, guard, skip. The probe returned `TOOL-aTimedTurnstile-3` (the
floor is the longest leg under load, which is why this unit does not claim a speedup) and
`TOOL-aBoundedVerdict-10` (the observed hang that motivates the timeout knob).
