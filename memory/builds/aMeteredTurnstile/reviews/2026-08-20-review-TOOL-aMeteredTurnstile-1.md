# Tier-2 review — `56b945cbb0613b1352dd06221d4d39940db33419...HEAD`

**Serves:** diff-review TOOL-aMeteredTurnstile-1


Reviewed range: `56b945cbb0613b1352dd06221d4d39940db33419...HEAD` — the cumulative diff landing on `main`
(5 commits, 18 files, +1198/-5). The whole product surface under review is
`tools/run-gates/profile_bar.py` (new, 379 lines), `tools/run-gates/profile_bar.test.sh` (new),
`tools/run-gates/kit.toml` and `tools/gate-legs.json`; the rest is records.

**Review shape** — raw 21 · confirmed 17 · refuted 4 · unverified 0 · precision 0.81.

**Verdict: 3 BLOCKERS. Do not land.** All three make the profiler publish a confident number that is
wrong, into an append-only record file (`gate-profile.jsonl`) that is advertised as comparable across
months. A wrong measurement is worse than no measurement, and this tool exists to be believed.

## Counting note

The 17 confirmed findings collapse to **9 distinct defects** — three independent lenses landed on the
same three high-severity bugs from different angles. Every id is preserved below against the defect it
reports; nothing was dropped in the merge.

| Band | Defects | Confirmed ids |
|------|---------|---------------|
| BLOCKER | 3 | 1, 3, 5, 6, 7, 8, 11, 15 (6 high + 2 medium restatements) |
| Medium | 3 | 2, 4, 9, 12, 16 |
| Low | 3 | 14, 19, 20 |

Raw severity as returned by the finders: high 6 · medium 7 · low 4.

---

## BLOCKER 1 — the recorded `width` is a guess, and it inverts the verdict

`tools/run-gates/profile_bar.py:265` (with `:218-220`) — ids **5, 8, 15**

`main()` copies the caller's environment (`env = dict(os.environ)`) and sets `env["GATE_JOBS"]` only
when `--width > 0`. The runner reads `JOBS=${GATE_JOBS:-…}` (`run-gates.sh:127`), so an inherited
`GATE_JOBS` wins and the bar runs at that width — while line 265 falls back to `derive_width()`, which
reads nothing but `os.cpu_count()`.

Reproduced in a 4-leg scratch repo, `GATE_JOBS=1` exported, no `--width`: the bar ran serially for
18.7s wall, and the record said `width 8`, `throughput 0.7s`, `bound: floor`. The summary printed
"The bar cannot go below 1.8s at ANY width on ANY hardware" and "Widening the pool and trimming small
legs both buy ZERO" — for a serial run whose only available win was, exactly, widening the pool.

`GATE_JOBS=1` is this repo's own documented serial rollback (AGENTS.md, `run-gates.sh:5`), so the
triggering environment is ordinary. The error is bidirectional: `run-gates.sh:134-135` clamps a
5+ digit width to 64 and a non-numeric or <1 width to 1, and the record reflects neither.

`width` is not cosmetic — it is the divisor in `derive_regime`'s `throughput = work / width`, so
`throughput`, `bound`, `ideal` and `packing` are all wrong together, and the record is appended to
`gate-profile.jsonl` as a durable comparable measurement carrying `w8` in its run id.

**Fix.** Resolve the effective width once, before building `env`, and pin it into the child:

```python
width = args.width if args.width > 0 else clamp(os.environ.get("GATE_JOBS"), derive_width())
env["GATE_JOBS"] = str(width)          # always — record and run cannot then diverge
```

mirroring `run-gates.sh:134-135`'s clamps, and delete the re-derivation at line 265. Deleting
`derive_width()`'s use as a *fallback for an env var that is right there* is the whole fix.

**Left-shift gate.** Add a `profile_bar.test.sh` arm that runs a fixture with `GATE_JOBS=1` exported
and **no** `--width`, and asserts `rec.width == 1`. The existing suite passes `--width` on every arm
(lines 85, 124, 145), so the defaulting branch is unexercised — this is the
`fixture-passes-by-finding-nothing` class, live. Stage the break first and confirm RED (§7).

## BLOCKER 2 — `check_quiet()` returns the affirmative on a platform where it cannot look

`tools/run-gates/profile_bar.py:124-127` — ids **1, 7, 17**

The probe greps `ps` output for the substring `run-gates`. MSYS `ps -W` and `ps ax` print only the
executable path in COMMAND (`/usr/bin/bash`, `C:\Windows\System32\smss.exe`) — never argv. `ps -W`
exits 0, so the `ps ax` fallback at line 119 never even fires.

Reproduced on node `a`: with a real `bash <dir>/run-gates.sh` alive in the background,
`ps -W | grep -c run-gates` returned 0 and `check_quiet()` returned
`('true', 'no other run-gates process visible to ps')`. Every record written on any node in this
repo's registry — all four are Windows — asserts a quiet machine it never verified, and the CAVEAT
block at lines 336-339 is dead code.

The function's own docstring (lines 104-107) names this exact failure and forbids it: "reporting
`true` because it found nothing is exactly the reassuring zero this repo's charter forbids". The code
does the thing the docstring promises it does not.

A second, independent bug in the same three lines: `check_quiet()` is called at line 230, **before**
the runner subprocess is spawned at line 237, so the `len(hits) > 1` self-discount is excluding a
child that does not exist yet. Even on a platform where the substring matched, one genuinely
contaminating foreign bar would be reported as quiet.

**Fix.** Make the probe assert its own liveness before trusting a zero: after the runner is spawned,
re-run `ps` and require the profiler's own known-live child to appear. If the probe cannot see a
process it knows is running, return `"unverified"` with that reason. On Windows the command-line-
bearing source is `Get-CimInstance Win32_Process` / `wmic process get commandline`, not `ps` — use it
or declare the platform unverified. Then count foreign hits as `> 0` after excluding self by pid.

**Left-shift gate.** A selftest arm that spawns a sleeping decoy process whose argv contains
`run-gates`, then asserts `check_quiet()` does **not** return `"true"`. The current test
(`profile_bar.test.sh:105-107`) only asserts `env.quiet ∈ {true,false,unverified}`, which is green
either way — a predicate that cannot fail. Same class as BLOCKER 1's missing arm.

## BLOCKER 3 — durations are read from a shared cache with no freshness check

`tools/run-gates/profile_bar.py:249` and `:285` — ids **3, 6, 11**

`read_timings()` is called after the run and the only trust predicate (lines 254-262) is
`verdict != "skip"` — never freshness. `before_mtime`/`after_mtime` (lines 231, 248) are consulted
**only** in the total-failure refusal at 268-269, which fires solely when *no* leg carried a duration.
`timings_moved` is computed at line 285, written into the record, and read by nothing: it appears
exactly once in the entire repo. `print_summary` branches on `quiet`, `timings_orphans` and
`legs_without_duration`, never on this.

The failure path is real and by design: `run-gates.sh:291` writes the cache with
`cp "$merged" "$TIMINGS" 2>/dev/null || true` — an advisory write that fails silently — and line 290
carries forward every prior row this run did not measure. So the write can fail (locked file on
Windows, read-only or full gitdir) while the bar exits 0.

Reproduced end to end: with `.git/gate-timings.tsv` made read-only and all four fixture legs changed
to `bash -c true`, the profiler reported `total leg work 12.0s`, `floor 3.8s`, and named "The binding
leg is: pb c (3.8s, 57% of wall)" — every second of it carried over from the previous run. The record
held `timings_moved: false`. The summary said nothing.

The comment at line 250 claims only legs this run executed carry a trusted duration. The code checks
executed-vs-skipped. Those are different questions.

**Fix.** Act on the value already collected: if `after_mtime <= before_mtime` and any executed leg
took its duration from the cache, refuse with exit 2 the way the empty-regime path does, or record the
regime as unverified. Add the structural check too — `wall < ideal` is impossible for a real
measurement, so `packing < 1.0` proves stale input and should refuse rather than print. The durable
fix is to stop reading a shared last-write-wins cache at all: have the runner emit per-leg seconds on
stdout, alongside the verdicts the profiler already parses.

**Left-shift gate.** Selftest arm: run a fixture, `chmod -w` the timing cache, run again with legs
whose real cost is near zero, and assert the profiler exits non-zero (or that the summary contains the
stale-cache caveat). Add a cheap invariant assertion that `packing >= 1.0` on every recorded run.

---

## Medium

### M1 — `parse_verdicts` accepts fabricated verdict rows

`tools/run-gates/profile_bar.py:56` (comment at `:47-49`) — id **2**

`parse_verdicts` iterates `stdout.splitlines()`, which breaks on `\v \f \x1c \x1d \x1e` as well as LF.
The runner's failing-leg indenter (`sed 's/^/    /'`, `run-gates.sh:226`) only prefixes after LF. So
leg output can inject rows that the anchored regex then accepts at column 0.

Reproduced through the real subprocess path: a child writing
`'GATE FAIL  real leg  (exit 1)\n    progress 50%\rGATE ok    injected leg\n    tail \x1eGATE ok    sep leg\n'`
yields `parse_verdicts() == [('real leg','FAIL'), ('injected leg','ok'), ('sep leg','ok')]`. Two
fabricated legs enter `rec['legs']` and, given a matching stale `gate-timings.tsv` row, `executed` and
the regime arithmetic. `\x1e` is the runner's own field separator, so this is reachable by accident.

Correcting the finder's attribution, which makes it slightly worse: text-mode universal newlines
already translate a bare CR to `\n` before the parser sees it, so switching to `split("\n")` closes
the `\x1e`/`\v`/`\f` vectors but not a CR one. Either way the comment at lines 48-49 — "only the
runner writes at column 0" — asserts an invariant the code does not provide, which is this repo's own
named bug class.

**Fix.** `for line in stdout.split("\n"): line = line.rstrip("\r")`, and correct the comment to say the
anchor holds only because LF is the sole line break honoured.

**Left-shift gate.** Selftest arm with a fixture leg that prints `\x1e` followed by a well-formed
`GATE ok` string, asserting the fabricated name does not appear in `rec['legs']`.

### M2 — `--scoped` does not clear an inherited `GATE_FULL`

`tools/run-gates/profile_bar.py:221-222` — ids **9, 16**

Line 218 copies the caller's environment and lines 221-222 only ever *set* `GATE_FULL`. Meanwhile
`run-gates.sh:112`'s `changed()` short-circuits to "run everything" whenever `GATE_FULL` is non-empty.

Reproduced: `GATE_FULL=1 python profile_bar.py --width 2 --scoped` appended a record reading
`"full": false` and printed the header `scoped`, for a run in which the child honoured no guard at all.
`.githooks/pre-push` sets `GATE_FULL=1` and an operator who exported it once keeps it for the shell's
life. The arithmetic is unaffected, hence medium — but the envelope is this wrapper's stated reason to
exist ("without that envelope two numbers taken a month apart are not comparable"), and `full` is the
one field the record can lie about.

**Fix.** One line: `env.pop("GATE_FULL", None)` on the `args.scoped` branch, so the flag names the run
in both directions.

**Left-shift gate.** Selftest arm exporting `GATE_FULL=1` with `--scoped`, asserting the fixture's
guarded leg reports `skip`.

### M3 — the runner's exit code is recorded and never shown

`tools/run-gates/profile_bar.py:281` (printed at `:312-355`) — ids **12** (medium), **4** (low)

`proc.returncode` is stored at line 281 and no consumer reads it. `print_summary` surfaces sha, host,
width, full, wall, regime, legs and three env fields — never `exit`, and never the FAIL count within
`rec['legs']` (`ran`, line 314, lumps `ok` and `FAIL` together). The word FAIL appears nowhere in the
output. Because the profiler runs the bar with `capture_output=True` and prints only its own summary
on success, the runner's own `gates RED — n/N legs failed` line (`run-gates.sh:311`) is swallowed too.

Net: an operator profiling a RED bar sees a clean-looking profile with a confident BOUND verdict and
no indication the run failed. The contamination is real — `runleg()` writes `$WORK/$i.sec`
unconditionally after capturing rc, so a leg that fails fast carries its truncated duration, and line
262 excludes only `skip`, so that short duration feeds `work`/`floor`/`throughput` and can flip the
regime classification.

One sub-claim from the raw findings is **refuted** and noted for the record: the runner has no
fail-fast — it dispatches and reaps every leg, incrementing `fails`, and exits 1 only at line 314. So
the bar does not "die early", and `work` is not small for that reason. The defect stands on the
unreported exit and unreported FAIL count alone.

**Fix.** Print the runner exit in the summary header (it is already in the record) and emit a CAVEAT
block when it is non-zero, in the same shape as the quiet caveat: say the bar was RED, name how many
legs carry a `FAIL` verdict, and say the regime is derived from a run that did not complete.

**Left-shift gate.** Selftest arm with a deliberately failing fixture leg, asserting the summary text
contains both the non-zero exit and a caveat line.

---

## Low

### L1 — the `classify` → `derive_regime` rename reached operator-facing prose

`tools/run-gates/profile_bar.py:191` and `:269` — id **14**

`--help` prints "Measure a run-gates bar run and derive_regime its regime." The stderr refusal prints
"Refusing to derive_regime." Both read as a half-applied sed, and the second is the message someone
reads while diagnosing a dead timing cache — i.e. exactly when clear English matters.

**Fix.** Line 191: "…bar run and derive its regime." Line 269: "…Refusing to derive a regime."

**Left-shift gate.** Cheap and general: a grep leg asserting no user-facing string literal in
`tools/run-gates/*.py` contains an underscore-joined identifier. Worth it only if this class recurs —
otherwise record it as a documented check in the rename ritual.

### L2 — `kit.toml`'s "FOUR gate legs" comment sits above five rows

`tools/run-gates/kit.toml:49` — id **19**

The comment reads "# FOUR gate legs, and four is the RULE rather than a census" and is immediately
followed by five `[[gate_leg]]` rows (lines 55, 63, 71, 76, 81). The withheld gov-only harness cannot
account for it — line 31 of the same file says that one is "deliberately NOT a `[[gate_leg]]` below".
The paragraph also predicts the fifth row will be the turnstile unit's "turnstile suite"; the row this
diff actually adds is `profile-bar selftest`. So the descriptor's own rationale block hands the next
reader a wrong count and a wrong name.

§7 bans this outright: "NO count of a derived population is written in prose."

**Fix.** Rewrite the paragraph without the literal — state the rule ("a row here must name a leg the
target's manifest can carry") and delete the census.

**Left-shift gate.** The kit selfcheck already compares descriptor rows against the manifest; extend it
to reject a number-word (`ONE|TWO|THREE|FOUR|FIVE`) in a comment adjacent to a repeated table. Cheaper
alternative if that predicate reds innocent files: derive the count in the selfcheck output instead.

### L3 — `FLOOR_ASSERTIONS=14` while the suite runs 15

`tools/run-gates/profile_bar.test.sh:17` — id **20**

`bash tools/run-gates/profile_bar.test.sh` prints `PASS (15 assertions)`. Counting `chk` calls agrees:
8 in arm 1, 4 in arm 2, 3 in arm 3. The comparison at line 163 is `-lt` and its failure text is "arms
went missing", so the pin's stated job is catching a vanished arm — and at one below the real count,
the first arm deleted or short-circuited passes silently. An off-by-one against the guard's own
purpose.

**Fix.** `FLOOR_ASSERTIONS=15`, re-stamped in the same commit as any arm added or removed. Note that
the three BLOCKER left-shift arms above will move this again.

---

## §10 recurring-bug-class checklist

`python tools/memory-tree/gotchas.py --for-diff 56b945cbb0613b1352dd06221d4d39940db33419..HEAD`
selected 0 anchored classes and 3 universal ones. All three fired.

- **`fixture-passes-by-finding-nothing`** — HIT, three times. `profile_bar.test.sh` passes `--width`
  on every arm (BLOCKER 1's branch unexercised), asserts `env.quiet ∈ {true,false,unverified}` which
  no outcome can fail (BLOCKER 2), and never varies the timing cache (BLOCKER 3). The suite is green
  and covers none of the three blockers.
- **`two-answers-to-one-question`** — HIT, twice. The pool width is decided in `run-gates.sh:127` and
  mirrored in `derive_width()`, and the copies disagree silently (BLOCKER 1). The gate-leg count is
  stated in `kit.toml:49` prose and owned by the row list beneath it (L2).
- **`heredoc-escape-reaches-the-regex`** — no instance found. `profile_bar.test.sh` writes its
  fixtures through heredocs, but the escapes that reach `VERDICT` are the runner's own output, and M1
  is a `splitlines` semantics bug rather than a quoting one. Reported as a clean arm, not a skipped
  one.

## Left-shift summary

Every confirmed defect above has a named gate or a documented check. The single highest-value item is
not any one of them: it is that **`profile_bar.test.sh` currently exercises only the happy path**, and
all three blockers live in branches no arm reaches. Adding the four arms named above (default width,
decoy process, frozen cache, failing leg) closes the three blockers and M3 together, and would have
caught them before review. Stage each break and confirm RED before wiring it (§7).

## Refuted, recorded

4 of 21 raw findings were refuted by the skeptic pass and are not restated here. One sub-claim inside a
confirmed finding was also refuted and is noted inline at M3: the runner does not fail fast.

---

## Fold-in — every blocker fixed, every fix ARMED

Recorded 2026-08-20 by the run that received this review. The verdict above stands as written; this
section records what changed and, for each fix, the evidence that its arm can actually fail. An arm
only ever seen pass is an assertion about nothing, so each defect below was reintroduced on its own
and the suite required to go RED.

| Finding | Fix | Arm | Observed RED against the reintroduced defect |
|---|---|---|---|
| BLOCKER 1 — width guessed | `derive_width(explicit, env)` resolves from `--width`, else the inherited `GATE_JOBS` with the runner's own clamps mirrored, and `GATE_JOBS` is then PINNED into the child so record and run cannot diverge. `width_source` is recorded. | arm 3 | yes |
| BLOCKER 2 — `check_quiet` blind | rewritten onto `Get-CimInstance Win32_Process`, filtered to `bash.exe` plus our own pid, with a LIVENESS assertion that the query can read THIS process's own command line before any zero is trusted | arm 9 | yes |
| BLOCKER 3 — stale durations | the freshness value is now ACTED ON: a cache that did not move is a refusal, not a record | arm 6 | yes |
| BLOCKER 3b — no structural check | `check_packing(wall, ideal)` extracted so the refusal is reachable without manufacturing stale data | arm 10 | yes |
| M1 — verdict injection | `split("\n")` plus `rstrip("\r")`; the comment now states the anchor holds only because LF is the sole break honoured | arm 5 | yes |
| M2 — `--scoped` leak | `env.pop("GATE_FULL", None)` on the scoped branch | arm 4 | yes |
| M3 — exit unreported | runner exit in the summary header, `failed_legs` recorded, and a RED caveat block | arm 7 | yes |
| L1 — rename leak | `--help` and the stderr refusal read as English again | none | n/a |
| L2 — `kit.toml` census | the "FOUR gate legs" paragraph rewritten without the literal | none | n/a |
| L3 — floor vs actual | `FLOOR_ASSERTIONS` moved 14 -> 33 against 35 real assertions | self | n/a |

### Two further defects the NEW arms caught, which this review could not have

Both were introduced by the fixes themselves and found before landing:

- **The probe crashed instead of reporting.** PowerShell writes in the console code page, so an
  undecodable byte (0xfa) raised inside `subprocess`'s reader thread, leaving `stdout` as `None` and
  taking the whole measurement down with it. A probe now decodes with `errors="replace"` and treats
  ANY exception as `unverified` — it reports that it could not look, and never raises into its caller.
- **The first floor fixture was itself load-graded.** It used a 4s dominant leg against 0.5s legs at
  width 2, and flipped to throughput-bound once per-leg overhead reached ~1.5s on this node. Rebuilt
  at width equal to the leg count, where throughput is the MEAN and floor the MAX, so a per-leg
  constant is added to both and cancels exactly. This is the same class the header disavows, committed
  in the file that disavows it.

### A false negative worth knowing about

The first arming pass reported the quiet arm as NOT ARMED. It is armed; the run had imported a stale
`tools/run-gates/__pycache__`. The directory is gitignored and untracked, so nothing ships to an
adopter, but an arming check that rewrites a module between runs can read yesterday's bytecode and
report a green that means nothing. Confirmed by hand afterwards: with the liveness assertion disabled
the probe returns `('true', ...)` and the arm fails, naming it.

### What was NOT done

No re-review of the whole diff. M8 asks for a re-review of the FIX rather than the diff, and the
arming table above is that: each fix is covered by an arm that was observed failing without it. The
pre-code spec audit M4 requires is parked on the run record — it cannot be performed after the code
without dating a pre-code pass after the code.
