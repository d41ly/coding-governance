# TOOL-dUnstuckLanding-17 — the history legs grade the run's own range, and check 23 a per-build budget

**Status:** CLOSED · rev-4 · 2026-10-04 · node d · Tier-2 · base 98926870 · streams tooling · order 5 · closes TOOL-dUnstuckLanding-7 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-dUnstuckLanding-17-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-17-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |
| [2026-10-04-review-TOOL-dUnstuckLanding-13-implementation-diff-round1.md](../reviews/2026-10-04-review-TOOL-dUnstuckLanding-13-implementation-diff-round1.md) | diff-review | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 TOOL-dUnstuckLanding-25 |
| [2026-10-04-review-TOOL-dUnstuckLanding-27-implementation-diff-round2.md](../reviews/2026-10-04-review-TOOL-dUnstuckLanding-27-implementation-diff-round2.md) | diff-review | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 TOOL-dUnstuckLanding-27 |

<!-- /gen:spec-records -->

## 1. Goal

Three kit legs grade history that is already on the default branch: `pass-order history`,
`brief-recorded` and check 23 of the `unattended kit gate`. A violation landed by anybody, at any
time, reds every later closing run, and in the adopters that class stopped more closes than any
other (design §4, census K1b and K1c). This unit makes each leg grade only the commits the closing
run adds on top of the tip the remote advertises, makes check 23's count a per-build budget instead
of a fleet-wide ceiling, prints the fleet total on a line that never fails a run, and adds a
report-only drift-audit signal, `fleet_over_budget`, that lists the builds over budget.

## 2. Scope (IN)

- **S1 — one advertised-tip reader for the two history legs.** `read_advertised_head` in
  `tools/unattended/lib-unattended.sh` takes the driver's path, reads the three bound constants
  `REMOTE_BOUND`, `REMOTE_CONNECT_BOUND` and `REMOTE_LOWSPEED_BYTES` out of it as data, the way the
  kit gate's `core_of` does, and runs ONE bounded `ls-remote --symref --exit-code <remote> HEAD`
  through the library's pinned `GIT` options. It returns 0 with the global `ADVH_SHA` set, or 1 with
  `ADVH_WHY` set. It refuses, with the reason, when the clone has no remote or more than one, when a
  constant does not read, when `ls-remote --get-url` differs from `remote get-url --push`, when the
  bound fires, when the remote advertises no HEAD, when `GATE_PUSH_BASE` is set and names another
  sha, and when the advertised object is not in this clone. It never reads a local ref, and the one
  environment variable it reads, the one the pre-push hook writes from git's own ref line, can only
  refuse a tip and never supplies one. Beside it, `read_history_range` applies S2's rule once for both legs: it calls the reader
  and sets `HR_MODE`, `HR_EXCL` (the `^<tip>` token, empty in WHOLE mode) and `HR_FIELD`, the summary
  field. Observed by AC1.
- **S2 — the range rule, the same in all three legs.** A leg is in RANGE mode when the advertised
  tip resolves and HEAD carries at least one commit the tip does not. Every commit walk it makes then
  excludes the tip's history. Otherwise it is in WHOLE mode and grades exactly what it grades today.
  WHOLE mode is never silent: the leg's summary line names the mode and, for WHOLE, which of the two
  reasons applies — the tip did not resolve, or HEAD carries nothing the tip lacks. Observed by AC2,
  AC3, AC4 and AC5.
- **S3 — `pass-order history` in RANGE mode.** In `tools/unattended/check-pass-order.sh`, both
  `build_commit` calls take `^<tip>` as an extra range token, so a unit whose build commit is on the
  tip is never graded and lands in the existing `unbuilt-in-range` figure. The summary line gains a
  `range` field. A waiver row naming a unit outside the range is not judged stale in RANGE mode; the
  summary counts such rows on a `waivers not judged` field instead. WHOLE mode judges staleness as
  today. Observed by AC2 and AC5.
- **S4 — `brief-recorded` in RANGE mode.** In `tools/unattended/check-brief-recorded.sh`, every
  `build_commit` call that takes a range takes `^<tip>` as well. The single-commit `<sha>^!` probes
  are unchanged, because they read a commit the ranged search already selected. The summary line
  gains the same `range` field. S3's waiver rule applies here too: in RANGE mode a waiver row naming a
  unit outside the range is not judged stale and is counted on a `waivers not judged` field. Observed
  by AC3.
- **S5 — check 23 in RANGE mode, against a per-build budget.** In
  `tools/unattended/check-unattended.sh`, a dispatched pass whose pass commit is an ancestor of the
  advertised tip is not graded against the budget, through the leg's existing `check_adv_reaches`.
  The over-declared passes that remain are counted PER RUN RECORD, and a record whose count exceeds
  `UNDECLARED_WRITE_BUDGET` fails check 23 naming that record and its passes. RANGE mode reads the
  leg's existing `ADV_HEAD` and `ADV_HEAD_OK`; this leg does not call S1's reader. Observed by AC4.
- **S6 — the fleet line.** Check 23 still walks its whole population exactly as today, and prints one
  line on the default channel whenever that population holds at least one record with dispatch rows:
  `unattended: check 23 fleet — <n> undeclared write(s) over <g> graded pass(es) in <r> record(s) ·
  budget <b> per build · over <slug>=<n>…|none · range <tip8>..<head8>|whole (<why>) · at <head8>`.
  It never fails the leg. The header's exception TWO names it beside check 23's two existing
  notices, so the "exit 0 and no output" contract still describes the code. Observed by AC4 and AC9.
- **S7 — the budget key.** `UNDECLARED_WRITE_BUDGET` is declared in the leg's initialiser, in the
  closed conf allow-list between the `gov:conf-allow-begin` and `gov:conf-allow-end` sentinels, in the kit example conf, in gov's `.unattended.conf` at `"0"`, and
  in PROTOCOL §8's key table. It is MANDATORY: undeclared or not a single integer is a numbered
  refusal, as the ceiling was. The liveness branch stays: a budget above zero over a fleet that graded
  no pass at all is a refusal, because a count of zero there is a dead probe. Observed by AC6.
- **S8 — the ceiling key is retired, by name.** `UNDECLARED_WRITE_CEILING` leaves every carrier S7
  names. A conf that still declares it is refused with a message naming `UNDECLARED_WRITE_BUDGET`,
  detected by the leg's existing text scan of declared names, so the retired key is never imported.
  The shrink-only comparison and its "below the ceiling, lower the pin" report leave with it, because
  a budget is a policy and not a measurement. Observed by AC6 and AC7.
  **Readers:**
  by name: `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh`,
  `tools/unattended/cross-component.test.sh`, `tools/unattended/.unattended.conf.example`,
  `.unattended.conf`, `tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md`
  and `tools/unattended/README.md` each spell `UNDECLARED_WRITE_CEILING`.
  by value: check 23's comparison in `tools/unattended/check-unattended.sh` is the only reader of the
  value; its replacement reads `UNDECLARED_WRITE_BUDGET`. Adopters' confs are carried by ask
  `TOOL-dUnstuckLanding-11`, and the named refusal is what they meet on upgrade.
- **S9 — the measuring flag is retired.** `--emit-ceiling` printed a measured value for the retired
  pin. Its argv branch becomes a refusal that exits 2 before any check runs, naming the fleet line as
  where the count now appears. Its header block, its two output sites and its README line go.
  Observed by AC8.
  **Readers:**
  by name: `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh` and
  `tools/unattended/README.md` spell `--emit-ceiling`.
  by value: NO VALUE READERS — its one output was a conf line a person pasted by hand; no program
  read it.
- **S10 — the drift signal.** `measure_fleet_over_budget` in `tools/drift-audit/drift_report.py`,
  registered in `SIGNALS` beside `build_nonterminal_merged_runs`. It reads the newest run record
  under the git dir's `gate-run` directory, through the `_RUN_RECORD_DIR` constant
  `measure_legs_retried_after_timeout` already uses, whose leg output carries a fleet line. Its value
  is the number of builds over budget, its `of` is the record count the line states, and its detail
  lists each build with its count and the line's `at` sha, noting when HEAD has moved past it. It is
  REPORT-ONLY. It reads NOT ASKED where the repo carries no `.unattended.conf`, and DEAD PROBE where it
  does and no run record carries a fleet line, or where the newest line's `over` field holds anything
  but `none` or `<slug>=<n>` tokens, as `over unjudged` does when no budget is declared. Its row joins the signal table in
  `tools/drift-audit/README.md`. Observed by AC9 and AC10.
- **S11 — the two history legs declare `impure`.** Their verdict now depends on the remote, so their
  entries in `tools/gate-legs.json` carry an `impure` reason, which keeps the runner from reusing a
  cached verdict after the remote moved. Observed by AC11.
- **S12 — the protocol render does not grow.** The PROTOCOL §8 row for `UNDECLARED_WRITE_BUDGET` is
  shorter than the row it takes the place of, and the render is re-copied by
  `bash tools/unattended/adopt-unattended.sh` in the same pass. Observed by AC12.
- **S13 — the kickoff manifest is re-stamped**, because `.unattended.conf` and `tools/gate-legs.json`
  are in its `watch:` list. Observed by AC13.

## 3. Non-goals (OUT)

- **The kit version moves.** Both the unattended and the drift-audit versions move once, at
  VERIFYING, by the orchestrator, per the build's brief. No pass here touches a version marker.
- **The adopter tenure legs.** nc's and inCMS's build-tenure legs live in their own repositories and
  ride ask `TOOL-dUnstuckLanding-11`'s carriage.
- **Routing check 23 or the driver through S1's reader.** The kit gate keeps its own observation,
  because its source-level no-write arm is per file, and the driver keeps `read_advertised_tip`.
  Three bounded observations of one advertisement is a known residual, stated here rather than left
  to be found. Converging them is a follow-up, filed by whoever next touches either observation.
- **Making the fleet total bind.** It binds nowhere. The leg prints it and the signal lists it; no
  bar, CI job or hook fails on it. This is said plainly because the design's rev-1 named a binding
  site that never ran the leg (review M10).
- **Grading a landed violation again.** A violation already on the default branch was graded when it
  landed, or was landed past a bypass the charter names. RANGE mode does not re-grade it, and WHOLE
  mode, which remote CI runs after every landing because its HEAD is the tip, still does.
- **The 103-byte headroom of the protocol render.** S12 keeps this unit net-negative there. Other
  units' growth is theirs to fit.

### Edges

- **hands-off** `TOOL-dUnstuckLanding-18` — the close-decision table's "move a shrink-only pin" row,
  which this unit's range grading dissolves for the kit's three legs.
- **hands-off** external — the adopters' build-tenure legs, carried by ask `TOOL-dUnstuckLanding-11`.

## 4. Design

### Evidence

Read at base `98926870`. Line numbers are PINNED to that reading; the builder locates each by the
quoted text.

| Site | Where | What it does today |
|---|---|---|
| check 23's record loop | `check-unattended.sh:3641-3690` | every RUN.md not recorded LANDED or ABORTED, not derived LANDED, with dispatch rows |
| check 23's ratchet | `check-unattended.sh:3850-3868` | the fleet count against `UNDECLARED_WRITE_CEILING`, plus `--emit-ceiling`'s print |
| `--emit-ceiling` | `check-unattended.sh:141-154` | argv branch and its EXIT trap |
| the conf allow-list | `check-unattended.sh:282-290` | the closed key set between the two sentinels |
| `ADV_HEAD`, `ADV_HEAD_OK` | `check-unattended.sh:1062-1228` | the leg's own bounded observation of the remote |
| `check_adv_reaches` | `check-unattended.sh:418` | ancestry against `ADV_HEAD` |
| `build_commit` | `lib-unattended.sh:720` | takes its range as `$1`, expanded UNQUOTED into `rev-list`, so a second token passes through |
| pass-order's calls | `check-pass-order.sh:380`, `:397` | `base..HEAD` and the pre-anchor `base` |
| brief-recorded's calls | `check-brief-recorded.sh:384`, `:410`, `:462` | `base..HEAD`, `<sha>^!` and the pre-anchor `base` |
| the driver's reader | `unattended.sh:1187` | `read_advertised_tip`, driver-only, through the driver's `observe_remote` |
| the run record | `<git-dir>/gate-run/<id>/<i>.out` | each leg's stdout per bar run, beside a `<i>.leg` row naming the leg |

The two history legs read the driver only as data, which is why S1 takes the driver's path and not
its functions. Neither leg observes the remote at base.

### Data model

The fleet line is the one contract between two kits, and it is spelled once in each:

```
unattended: check 23 fleet — 3 undeclared write(s) over 41 graded pass(es) in 6 record(s) · budget 0 per build · over aClosedDocket=2 dPlumbedAtrium=1 · range 0a66eacb..5f1e2d3c · at 5f1e2d3c
```

`measure_fleet_over_budget` anchors on the head `unattended: check 23 fleet — `, splits the tail on
` · `, and reads the `over` and `at` fields by their leading word. A line that does not parse is
detail, never a count. The values above are illustrative.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `read_advertised_head` | shell function | `sh.function`; `python tools/lexicon/lexicon.py --suggest read_advertised_head --as sh.function` answered OK |
| `ADVH_SHA`, `ADVH_WHY` | shell globals | not graded |
| `read_history_range` | shell function | `sh.function`; the lexicon answered OK |
| `HR_MODE`, `HR_EXCL`, `HR_FIELD` | shell globals | not graded |
| `measure_fleet_over_budget` | python function | `py.function`; the lexicon answered OK |
| `fleet_over_budget` | drift signal name | none |
| `UNDECLARED_WRITE_BUDGET` | conf key | none |
| `check 23 fleet` | default-channel message head | none |

### Rollout

1. Write S1, then S3 and S4, then S5 to S9, then S10 and S11, then the carriers, then re-copy the
   renders with `bash tools/unattended/adopt-unattended.sh`.
2. Observe each acceptance criterion directly, in the scratch fixtures and slices it names.
3. Re-stamp the manifest and commit once, with the unit id in the subject.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-pass-order.sh`
- `tools/unattended/check-pass-order.test.sh`
- `tools/unattended/check-brief-recorded.sh`
- `tools/unattended/check-brief-recorded.test.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/cross-component.test.sh`
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/README.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `.unattended.conf`
- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

Each was rejected by a test, and §8 carries the fork it decided.

- **The drift signal re-implements check 23 in Python.** Rejected by reading what it would copy:
  `check-unattended.sh:3641-3870` holds the pass-commit join, the generated-render skip, the ABSORB
  classification and the brief exclusion, about 230 lines a second copy would have to agree with.
  That is the `two-answers-to-one-question` class.
- **The drift signal runs the kit gate.** Rejected by its cost: `<git-dir>/gate-ledger.tsv` on node d
  records the `unattended kit gate` leg at 623.656 s against 26.372 s for `drift-audit records`, both
  PINNED to the last full bar before 2026-10-04. The drift report's contract is seconds.
- **The history legs read `GATE_PUSH_BASE` or a remote-tracking ref.** Both are values the run
  controls, and a range the run names is a range the run can empty. The protocol records both
  channels as reproduced bypasses of an observed BASE.
- **An unavailable tip grades nothing.** That is a probe reading zero, which M3's counter-rule
  refuses, and it would also make remote CI's bar, whose HEAD is the tip, grade nothing at all.

## 5. Production-readiness checklist

- security — the range narrows what is graded, so its one input is observed from the remote and
  never read from a ref, a file or the environment the run controls. Every failure to observe widens
  to WHOLE mode, never to an empty range.
- perf / scale — RANGE mode walks only the run's commits, where today both history legs walk every
  build's whole range. The ledger records 189.827 s for `pass-order history` and 114.314 s for
  `brief-recorded` under a full bar (PINNED, node d, before 2026-10-04); the drop is UNVERIFIED until
  the close's bar measures it. Each history leg gains one bounded remote call.
- error / empty / loading states — an unreachable remote, an absent object and an empty range each
  select WHOLE mode with the reason on the summary line; a budget above zero over an ungraded fleet
  stays a refusal.
- observability — the summary lines name the mode and the tip, the fleet line names every build
  over budget, and the drift signal names the bar run it read.
- risks — every suite arm that asserts a summary line byte-for-byte moves with the new `range`
  field; the builder updates those arms in the same pass. A fixture with no remote now reads WHOLE,
  which is today's behaviour, so the existing arms keep their verdicts.
- testing — the new arms named under §7, each observed through a scratch slice.
- migration — gov's conf moves from the ceiling key to the budget key at `"0"`. An adopter that
  upgrades without moving its key is refused by name.
- user docs — the kit README's leg list loses `--emit-ceiling`, PROTOCOL §8 gains the budget row,
  and the drift-audit README gains the signal row.

## 6. Acceptance criteria

- **AC1** — When a scratch script sources `tools/unattended/lib-unattended.sh` in a fixture clone at
  `%TEMP%/ul17a` with a bare origin and calls `read_advertised_head` with the driver's path, it
  returns 0 and `ADVH_SHA` equals the HEAD sha `git ls-remote origin HEAD` prints. After a second
  clone pushes a new commit to that origin, a second call in a fresh shell returns the new sha. With
  the remote removed it returns 1 and `ADVH_WHY` names the missing remote. With the fetch URL pointed
  at another bare clone while the push URL stays, and with `GATE_PUSH_BASE` naming another sha, it
  returns 1 naming the split, and each history leg reads `range whole` with that reason.
  Red when: the helper reads `refs/remotes/origin/HEAD`, which is stale after the second clone's
  push, so the second call returns the old sha.
  fixture: built under `%TEMP%`, never the scratchpad, because a clone under the scratchpad path
  fails with Filename too long.
- **AC2** — When a scratch slice of the pass-order suite runs the new range arm, a fixture whose
  origin tip carries a unit built before its spec, and whose unpushed run adds one conforming unit,
  makes `check-pass-order.sh` exit 0 with a summary line carrying `range ` and the tip's 8 hex. The
  same fixture with a second, unpushed, built-before-specced unit exits 1 naming that unit and not
  the pushed one.
  Red when: the `^<tip>` token is staged out of the `build_commit` call at `check-pass-order.sh:380`,
  so the pushed unit reds the first run.
- **AC3** — When a scratch slice of the brief-recorded suite runs the new range arm, a fixture whose
  origin tip carries a CLOSED unit with no brief row, and whose unpushed run adds a CLOSED unit with
  one, makes `check-brief-recorded.sh` exit 0 with `range ` on its summary line. Adding an unpushed
  CLOSED unit with no row exits 1 naming that unit only.
  Red when: the `^<tip>` token is staged out of the call at `check-brief-recorded.sh:384`.
- **AC4** — When a scratch slice of the kit-gate suite runs the new check 23 arm, a fixture whose
  live record carries one pushed pass with an undeclared write and one unpushed clean pass prints a
  `check 23 fleet` line reading `1 undeclared write(s)` and no `check 23 FAILED`. Adding an undeclared
  write to the unpushed pass prints `check 23 FAILED` naming the unpushed pass and not the pushed one.
  Red when: the `check_adv_reaches` test is staged out of the budget count, so the pushed write reds
  the first run.
- **AC5** — When the AC2 fixture's origin HEAD symref is pointed at `refs/heads/nothing-here`, the
  pass-order summary line reads `range whole` with the unresolved-tip reason, and the pushed unit
  reds as it does today. With HEAD reset to the tip, the line reads `range whole` with the
  nothing-unpushed reason.
  Red when: an unresolved tip is read as an empty range, so the pushed unit is never graded and the
  leg exits 0.
- **AC6** — When `sed -n '/gov:conf-allow-begin/,/gov:conf-allow-end/p' tools/unattended/check-unattended.sh`,
  `tools/unattended/.unattended.conf.example` and `tools/unattended/PROTOCOL.template.md` are each
  grepped for `UNDECLARED_WRITE_BUDGET`, all three match, and `grep -n '^UNDECLARED_WRITE_BUDGET="0"' .unattended.conf`
  prints one line. `git grep -n UNDECLARED_WRITE_CEILING -- tools .unattended.conf memory/guides`
  prints only the refusal text in the leg and its arm.
  Red when: any one of the three carriers lacks the new key, which is the join check 22 makes.
- **AC7** — When a scratch slice of the kit-gate suite runs the arm that adds
  `UNDECLARED_WRITE_CEILING="0"` back to the fixture conf, the output carries the refusal naming
  `UNDECLARED_WRITE_BUDGET`.
  Red when: the name scan is staged out, so the retired key is silently ignored and the leg passes.
- **AC8** — When `bash tools/unattended/check-unattended.sh --emit-ceiling` runs in this tree, it
  exits 2 within a second and prints the retirement message naming the fleet line.
  Red when: the branch still sets the skip-28 scope, so the run starts checks and does not exit at
  once.
- **AC9** — When `python tools/drift-audit/drift_report.py --json` runs in a scratch clone at
  `%TEMP%/ul17d` whose git dir holds no run record, `fleet_over_budget` reads `live` false. After a
  scratch file `<git-dir>/gate-run/fx/0.out` carrying one fleet line with `over aFixture=2` is
  written, it reads value 1, `gateable` false, and its detail names `aFixture`. The same file
  reading `over unjudged` reads `live` false, naming it. Deleting the file returns it to `live` false.
  Red when: the signal reports `live` true with value 0 after the file is deleted.
  cost: about 30 s per report run.
- **AC10** — When `grep -c 'check 23 fleet — '` runs over `tools/unattended/check-unattended.sh`
  and `tools/drift-audit/drift_report.py`, each prints at least 1.
  Red when: one kit spells the head differently, so the signal parses nothing the leg prints.
- **AC11** — When `git diff HEAD~1 HEAD -- tools/gate-legs.json` runs at the pass's commit, it
  shows an `impure` key added to the `pass-order history` entry and to the `brief-recorded` entry,
  and no other entry changed.
  Red when: either history leg lacks an `impure` reason, or the diff moves another leg.
- **AC12** — When `wc -c memory/guides/UNATTENDED-PROTOCOL.md` runs at the pass's commit and at its
  parent, the commit's figure is not larger, and `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md`
  exits 0.
  Red when: the budget row outgrows the ceiling row, or the render was not re-copied.
  figure: both byte counts are DERIVED at observation time.
- **AC13** — When `git diff HEAD~1 HEAD -- memory/guides/SESSION-KICKOFF.md` runs at the pass's
  commit, it shows the `last-audit:` line moved.
  Red when: `.unattended.conf` or `tools/gate-legs.json` moved in the commit and the stamp did not.

## 7. Gates

`unattended kit gate` · `pass-order history` · `brief-recorded` · `unattended protocol size` · `unattended skill wiring` · `drift-audit records` · `drift-audit wiring` · `drift-audit selftest` · `run-gates canary` · `run-gates gov canary` · `harness arms (fail branches armed or pinned)` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/unattended/check-pass-order.test.sh · a pushed built-before-specced unit beside a clean unpushed run, then a second unpushed violation; the unresolved-tip and nothing-unpushed WHOLE arms; a waiver row naming the pushed unit, not judged · none
New arm: tools/unattended/check-brief-recorded.test.sh · a pushed CLOSED unit with no brief row beside a clean unpushed run, then an unpushed one; the unresolved-tip WHOLE arm; a waiver row naming the pushed unit, not judged · none
New arm: tools/unattended/check-unattended.test.sh · a pushed live record with an undeclared write beside a clean unpushed pass, then an unpushed undeclared write; the retired ceiling key; the budget's three refusals replacing the ceiling's; `--emit-ceiling`'s refusal · none
New arm: tools/drift-audit/selftest.py · `test_fleet_over_budget`, a fixture run record carrying a fleet line, then none · CHECK_FLOOR rises by the arm's checks

The suites themselves are held from the bar by the 2026-08-23 owner ruling. The close runs them
once, under `TOOL-dUnstuckLanding-24`.

## 8. Open questions

- **F1 — Where does `fleet_over_budget` get its counts?** (a) A Python copy of check 23. (b) Run the
  kit gate. (c) Read the fleet line from the newest run record the bar persisted. (a) is the
  two-answers class over about 230 lines; (b) costs 623 s against a report measured in seconds;
  (c) reads one file, through a constant the engine already holds, and its liveness is a record
  carrying the line. Recommendation (c).
  RESOLVED (agent, 2026-10-04, delegated): (c).
- **F2 — How do the two history legs learn the advertised tip?** (a) A library reader with its own
  bounded observation, its bounds read from the driver. (b) The same, with the kit gate and the
  driver moved onto it. (c) `GATE_PUSH_BASE`. (d) The local remote-tracking ref. (c) and (d) are
  values the run controls, so veto 3 discards them. (b) moves two other mechanisms and their
  source-level arms, which this unit's tier did not price. Recommendation (a).
  RESOLVED (agent, 2026-10-04, delegated): (a).
- **F3 — What does a leg grade when there is no range?** (a) The whole history, as today, announced.
  (b) Nothing, announced. (b) decides by reading zero, which M3's counter-rule refuses, and blinds
  remote CI. Recommendation (a).
  RESOLVED (agent, 2026-10-04, delegated): (a).
- **F4 — Is `fleet_over_budget` gateable?** (a) Report-only. (b) Gateable with a pin. Under (b) the
  `drift-audit records` leg, which runs on the bar, would fail a closing run on the fleet total, and
  the ask says the total never does. Recommendation (a).
  RESOLVED (agent, 2026-10-04, delegated): (a).
- **F5 — What happens to `--emit-ceiling`?** (a) Retire it with a numbered refusal. (b) Keep it,
  printing the budget. A budget is declared, not measured, so (b) prints a value nobody should
  paste. Recommendation (a).
  RESOLVED (agent, 2026-10-04, delegated): (a).
- **F6 — Do the two history legs declare `impure`?** (a) Yes, in `tools/gate-legs.json`. (b) No.
  Under (b) a reused cached green survives a remote rewind that widens the range, which is the
  fail-open direction. The manifest is data the bar reads, not one of the method's governance
  carriers, so veto 2 does not reach it. Recommendation (a).
  RESOLVED (agent, 2026-10-04, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief, design §4 at rev-2 and review items M7 and
  M10, with the three legs, the kit library, the driver's tip reader and the drift engine read at
  base `98926870`.
- rev-2 · 2026-10-04 · the builder, before the code. S4 gains S3's waiver rule: gov's own
  `brief-recorded` registry waives two units already on the default branch, so RANGE mode would have
  judged both rows stale and redded every closing run. S1 names `read_history_range`, the one
  spelling of S2's rule both history legs call. AC4 grades two passes of one live record rather than
  two records, because a second live record in the kit-gate fixture moves checks the arm does not
  assert; the `check_adv_reaches` exclusion it observes is the same.
- rev-3 · 2026-10-04 · S10 AC9 · folded implementation review round 1 M10 and L7 (ids 15, 19, 29):
  `_parse_fleet_line` returns an `over` field holding anything but `none` or `<slug>=<n>` as
  unjudged, and `measure_fleet_over_budget` reads it DEAD naming it, never a live zero.
- rev-4 · 2026-10-04 · S1 AC1 · folded implementation review round 1 M6 (id 4) and M13 (id 20):
  `read_advertised_head` refuses a fetch URL that is not the push URL and a tip `GATE_PUSH_BASE`
  contradicts, both widening to WHOLE, and its header states the relay residual; the pass-order
  suite arms every refusal, each RED against a library copy with that refusal removed. M1 (id 26),
  the intent lens's duplicate of H1, is closed by `TOOL-dUnstuckLanding-27`, whose pre-anchor
  exemption probe carries no range exclusion.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade only the commits a closing run adds since the advertised default-branch tip"`
ranked name-stem neighbours only and printed `unscanned layers: .sh`, so it cannot see the shell
seams. Its one relevant hit was `build_nonterminal_merged_runs` in
`tools/drift-audit/drift_report.py`, which S10's signal sits beside. The seams were read directly
instead, and this unit extends them: `build_commit` and `read_run_commits` in
`tools/unattended/lib-unattended.sh`, `check_adv_reaches` and `ADV_HEAD` in
`tools/unattended/check-unattended.sh`, the driver's `read_advertised_tip` as the shape S1 copies,
and `measure_legs_retried_after_timeout`'s run-record read in the drift engine. The recall probe
returned this build's ask and design, review item M7, the `TOOL-aSightedSkeptic-13` spec that made
check 23 exclude derived-LANDED records, and two asks recording `pass-order history` breaching its
ceiling under a full bar. None records a reason to keep grading landed history.

Recall terms used: check 23 undeclared-write ceiling pass-order brief-recorded history leg advertised tip fleet shrink-only range

The question passed with them: "why do the history legs and check 23 grade landed history on every
closing run".
