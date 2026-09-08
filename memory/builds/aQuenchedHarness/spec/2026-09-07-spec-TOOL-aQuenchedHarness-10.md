# TOOL-aQuenchedHarness-10 — the leg asks git once per question, not once per record

**Status:** CLOSED · rev-5 · 2026-09-07 · node a · Tier-2 · base ab58d1cc · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-07-build-TOOL-aQuenchedHarness-10-git-arity.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-10-git-arity.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`unattended kit gate` is the longest leg on the bar and its wall clock is its PROCESS COUNT: a git
process costs about 130 ms on this platform whatever it is asked, and the leg spawns 1114 of them.
Ask each question once — one batch where there were 290 calls, one graph walk where there were 87 —
and grade the builds that can produce a finding rather than all 102.

The BASELINE THIS UNIT WAS OPENED AGAINST WAS WRONG, and the record says so rather than quietly
using the right one: the leg's recorded 541 s, and every figure this unit quoted before its
closing measurement, were read on a box carrying this session's own orphaned processes. On a
quiet box the unmodified leg is 331 s. The process-count argument above is unaffected — spawn
counts do not care what else is running — but the wall-clock case for the unit was overstated by
roughly 3x for its whole life. §9 rev-5 carries the correction.

## 2. Scope (IN)

- **S1** — The facts that cannot change during a run resolve ONCE: `HEAD`, and whether the tip the
  remote advertises for its default branch is readable here. Measured on this tree, those two were
  re-asked 127 times between them. AC1, AC4.
- **S2** — Existence of every sha-shaped token in every tracked run-state file resolves in ONE
  `cat-file --batch-check`, behind a `check_rev` accessor that falls back to the original single call
  for any key the warm-up did not collect. AC1, AC4.
- **S3** — Ancestry becomes set membership over one `rev-list` per subject: `check_head_reaches` against `HEAD`,
  `check_adv_reaches` against the advertised HEAD. Both keep the original `merge-base` call for an
  abbreviated rev, which a table of full shas cannot answer. AC1, AC4.
- **S4** — `is_published` reads the object TYPE from the field `cat-file --batch-check` actually
  prints it in. The rebuilt warm-up read it one field late, which made every advertised tip look
  unreadable and turned every answer into CANNOT TELL. AC4, AC6.
- **S5** — Check 30 asks the driver about the builds whose specs can produce a `NOT A UNIT` row,
  found by one awk pass over the whole spec corpus, instead of launching `--plan` for all 102.
  AC2, AC3.
- **S6** — That selector's two patterns are asserted against the driver they are copied from, so a
  driver that stops spelling either one REFUSES rather than selecting nothing. AC5.
- **S7** — The leg's stdout is unchanged, byte for byte, against a fixture whose remote is frozen
  and present. AC4.

## 3. Non-goals (OUT)

- **The two `GIT show <rev>:<path>` sites stay** (54 spawns). Batching them needs a binary-safe
  `cat-file --batch` reader that counts bytes rather than lines, which is a mechanism of its own and
  not a change of arity. Follow-up: its own unit, with `dScaffoldedMirror-7`'s batched blob reader as
  the seam to extend.
- **The per-record `git log --follow` stays** (27 spawns). One walk over `memory/builds` would have
  to reconstruct rename chains to reproduce `--follow`, and the site's own header explains that the
  rotation of a run-state file is exactly the rename it exists to see through. Getting that wrong
  changes a graded/ungraded verdict for 4 s of wall clock.
- **`verb_plan`'s own 29 processes per build are not touched.** It is the driver's main verb, used by
  people and by other checks; this unit changes how OFTEN check 30 calls it, not what it costs.
- **No check changes what it ASSERTS**, with one exception stated plainly: check 30's population is
  now a selection rather than the whole corpus. §4 states why that cannot hide a finding.

### Edges

- **consumes-from** `TOOL-aQuenchedHarness-7` — the same leg, rebuilt from 5420 external processes to
  2321. That unit left the wall target MISSED at 435 s against 400 s, and left the leg's git
  interaction untouched; this is the half it did not reach.
- **hands-off** `none`

## 4. Design

### Data model

Four tables, each filled by one query, each lazily on first use because several checks exit before
reaching a record and a walk nobody asks for is the same waste one process at a time was.

| accessor | table | filled by | replaces |
|---|---|---|---|
| `$HEAD_SHA` | scalar | one `rev-parse HEAD` | 39 identical calls |
| `$ADV_HEAD_OK` | scalar | one `cat-file -e` | 36 identical calls |
| `check_rev` | rev → 0/1 | one `cat-file --batch-check` over every sha-shaped token in the tracked run-state files | 290 calls at six sites |
| `check_head_reaches` | sha → present | one `rev-list HEAD` | 81 calls at two sites |
| `check_adv_reaches` | sha → present | one `rev-list $ADV_HEAD` | 66 calls at two sites |

**Every accessor keeps the call it replaces as a fallback.** A key the warm-up did not collect is
answered by the original single git call and then memoised. Correctness therefore does not depend on
the pre-scan being complete: a miss is slow, never wrong. This is what makes the change safe to make
at fourteen call sites at once.

**The zip is the one subtle part.** `cat-file --batch-check` emits exactly one reply per request, in
order, and its first field is the FULL sha. Keying the table on that field would key it by full sha
and silently miss every abbreviated recorded fact, so the table is keyed by the REQUEST, paired with
its reply by index. A reply count that does not match the request count leaves the table empty and
every call falls back — a short read must not become a wrong answer.

`check_head_reaches` and `check_adv_reaches` rest on `merge-base --is-ancestor A B` being true exactly when A is
reachable from B, which is what `rev-list B` enumerates: same relation, same reflexive case, since
`rev-list` emits B itself and B is its own ancestor. `check_adv_reaches` is a DIFFERENT set from the union
`is_published` holds — reachable-from-any-advertised-tip does not imply reachable-from-ADV_HEAD — so
it gets its own walk rather than reusing one that answers a wider question.

### Check 30's population

The check asks the driver for its own verdict on each build and looks for one shape: a `NOT A UNIT`
row beside the claim that every tracked spec is terminal. Getting the verdict from the driver is
right and is unchanged — deciding it here would be a second implementation rather than a second
opinion. What was wrong was the ARITY. One `--plan` costs 3786 ms and 29 spawned processes, 13 awk
and 9 grep among them, re-reading spec files; over 102 builds that is roughly 390 s, and it is the
largest single item on the bar's longest leg.

`NOT A UNIT` is emitted at exactly two places in the driver, and both are keyed on ONE spec: its
status header did not parse, or its heading id did not. So "some tracked spec of this build fails
one of those two" is a NECESSARY condition for the row. A build with no such spec cannot produce it,
and passing over that build cannot hide a finding. A build WITH one is handed to the driver, which
decides both halves of the conjunction — the selector says nothing whatever about the terminal half,
and over-selecting is free.

The scan is one `git ls-files`, one `grep -v` for the `spec/_*/` scratch dirs the driver also drops,
and one awk over the survivors — chunked through `xargs`, because 551 spec paths are 41 KB of argv
and Windows caps a command line at 32 KB. An unreadable or zero-length spec selects its build without
reaching awk, because that is what the driver does with one: `spec_facts` emits an empty row for a
path it cannot read, and awk's `FNR==1` never fires for a zero-length file, so neither yields an id
or a status. On this tree the scan costs 2074 ms and selects five builds — the same five check 30's
own header records it redding on the day it was written.

**The patterns are the driver's and are asserted against it.** A filter keyed on a predicate spelled
in two places is a filter that stops selecting when one copy moves, and a check whose population
quietly empties reports clean forever. Both literals are `grep -F`'d out of the driver before the
scan runs; either one absent is a refusal.

**Liveness is now two assertions, because the check has two stages.** The scan must have read a spec,
and the driver must have returned a verdict for something it was asked about. Where the scan selects
nothing at all, one build is graded anyway, so the assertion that the driver path answers is never
about an empty ask — that assertion exists because the first cut of this check resolved the driver
path wrongly and walked zero builds.

### Alternatives rejected

- **Batching the driver launches** (landed and then measured as worthless on its own). `--plan` now
  takes several slugs in one process, which removes 101 execs — but a launch is ~1.2 s of a 3.8 s
  call, and an A/B over the whole leg could not distinguish the win from noise. It is kept because
  the selection needs a multi-slug call anyway, not because it was the fix.
- **Re-implementing the driver's predicate in the leg** — that is a second implementation, and the
  check's whole value is that it grades the driver's OWN output.
- **A per-tip reachability set for `is_published`** — measured at 8.88 s against 1.31 s for the
  union over the 28 heads this origin advertises. The per-tip shape looks more careful and is
  strictly worse.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/lib-unattended.sh` ·
`tools/unattended/unattended.sh` · `tools/unattended/check-pass-order.sh`

## 5. Production-readiness checklist

- security — N/A. No new input is trusted; every accessor answers the same question from the same
  object database, and the fallback path is the code that was there before.
- perf / scale — this IS the unit. The tables are keyed by sha and bounded by the record and commit
  counts of the repository; `rev-list HEAD` is 2327 entries here at 157 ms.
- error / empty / loading states — a short or failed batch leaves a table empty and every call falls
  back; an absent `ADV_HEAD` leaves `ADV_HEAD_OK` at 0, which is what the guarded sites already
  tested for.
- observability — the argv log used to measure this is instrumentation, not shipped code. The leg's
  own per-leg log under `<git-dir>/gate-logs/` is unchanged.
- risks — fourteen call sites change at once. The mitigation is byte-identity against a frozen
  fixture (AC4), not review alone. The second risk is check 30's population; AC3 stages the break
  that would prove the selector can hide a finding.
- testing — AC3 and AC5 are staged breaks, observed before landing. AC4 is a back-to-back A/B on one
  frozen clone.
- migration — none. No file format, no recorded artifact and no declared value moves.
- user docs — N/A. No user-facing surface; the reasoning lives beside the code it explains.

## 6. Acceptance criteria

- **AC1** — When the leg runs with every git argv logged, its own git spawns fall below 300 from
  777, and no single argv appears more than five times. `GIT_ARGV_LOG` shim, `cut -f2 | uniq -c`.
  Red when: a warm-up marks itself filled while holding nothing, so every call falls back and the
  old per-record counts return unchanged.
  figure: DERIVED — both numbers are counted from the log at observation time.
- **AC2** — When check 30 runs on this tree, the driver is asked about exactly the builds the scan
  selected. Red when: the selection is empty and no canary is added, so `--plan` grades no build and
  the liveness line passes over an empty ask.
- **AC3** — When a tracked spec loses its `**Status:**` header, the scan selects its build where it
  did not before. Observed by removing the header from
  `spec/2026-09-07-spec-TOOL-aQuenchedHarness-9.md` and re-running the scan. Red when: the filter
  keys on something the driver does not, and a build that would red is passed over.
- **AC4** — When the rebuilt leg runs against a fixture clone whose remote is frozen and whose
  objects are all present, its stdout is byte-identical to the same leg before the change. `diff`
  over both captures. Red when: any accessor's answer differs from the call it replaced — which is
  how the `cat-file --batch-check` field offset in S4 was found.
  fixture: a bare frozen origin advertising all 28 heads. A clone with the remote DETACHED does not
  observe this: `$ADV_TIPS` is then empty and the whole published-anchor path never runs, which is
  precisely how the S4 defect survived an earlier A/B.
- **AC5** — When `tools/unattended/unattended.sh` stops spelling either selector pattern, the
  `grep -qF` parity assertion in check 30 REFUSES, naming the driver. Observed against a doctored
  copy of that file, never against the tracked one. Red when: the parity assertion is absent, and the
  selector silently selects nothing forever.
- **AC6** — When `bash tools/unattended/check-unattended.sh` runs standalone, its wall clock timed
  by `date +%s%3N` is under 334 s — the pool bound at width 8, below which the bar is pool-limited
  rather than limited by this leg. Baseline 618 s on the fixture.
  Red when: the process count falls but the wall does not, which would mean the cost was never
  process creation.
  figure: DERIVED — timed at observation.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `bash tools/run-gates/run-gates.sh`

New arm: none. Check 30's parity refusal and its selector are arms of an existing leg, and their
failing cases are staged by AC3 and AC5 rather than by a new suite — this kit's self-tests are held
off the bar by the 2026-08-23 owner ruling and a new one would not run.

## 8. Open questions

None blocking. One parked: the two deferred sites in §3 are 81 spawns of the leg's remaining cost,
and whether they are worth their own unit depends on what the leg measures at after this one.

## 9. Revision log

- rev-5 · 2026-09-08 · CLOSING MEASUREMENT, and a correction to every earlier one. AC6 MET:
  197.0 s under the 8-wide pool against a 334 s target, on a green bar of 203 s wall; standalone
  331.4 s to 169.1 s over four arms in A-B-B-A order. Three earlier readings of AC6 were
  reported before they were checked and all three were contaminated - a fixture clone that is
  not representative for time, then two of this session's own 11-hour spin loops, then four
  subagents running during the BEFORE arm. The fix was not arithmetic: it was a harness that
  samples the box THROUGHOUT each arm and refuses to report an arm it did not observe quiet.
  Nothing in §2 or §3 moved.
- rev-4 · 2026-09-07 · the kit's own self-test suites caught two defects that no fixture in this
  unit could. `cross-component.test.sh` red on three arms because `--plan` decided its output
  FORMAT from the slug COUNT: at one slug it emitted no frames, and check 30 - which reads
  frames - counted zero verdicts and red a healthy tree. Every fixture I built had several
  builds, so the one-slug shape never occurred in one. `--framed` makes the framing a declared
  mode at any arity and the unframed one-slug form is unchanged; the verb doc and its shipped
  template both say so. Separately the canary became a SAMPLE of three rather than one build,
  because a single build refusing for its own reasons must not decide this check's liveness.
  Both are §2 S5's mechanism, not new scope.
- rev-3 · 2026-09-07 · the eight new helpers renamed onto the declared verb table -
  `check_rev`, `check_head_reaches`, `check_adv_reaches` and five `_load_*`/`resolve_*`
  fillers. The `lexicon naming predicates` leg is a RATCHET on verb offenders and my first
  spelling added eight, one per definition: `rev`, `in`, `pub` and `advh` are not verbs. The
  count is back AT its pin with the eight definitions still graded, so nothing was waived. The
  pin's value is not repeated here - `.lexicon.conf` owns it, and its own header says why a
  count typed beside that file does not survive the next commit.
- rev-2 · 2026-09-07 · built and measured. The check-30 rebuild moved two of this leg's own
  fail branches, so `check-unattended.test.sh` gained arms for the selector's liveness and its
  parity refusal and its branch-1 assertion was re-texted; the unguarded `harness arms` leg
  catches exactly that, and did. §3 gained nothing and §2 gained nothing: the scope is as
  specced.
- rev-1 · 2026-09-07 · specced AFTER the code it describes, which is a deviation from the method and is recorded rather than tidied away: the unit began as a measurement of a leg already landed, and what it should build was not knowable until the measurement existed. The measurement: every git argv logged through
  a shim in `GIT()`, which is the only method that follows the driver's child processes — `bash -x`
  does not, and that blind spot is why the first attempt at this leg optimised the wrapper instead of
  the work.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` was not the probe that answered this; memory-recall was, and it
named the seam directly: `TOOL-aThawedCorpus-4` — "hygiene check 23 stops spawning a process per spec
and per record" — is the same technique applied to the memory-tree kit's leg, and
`dScaffoldedMirror-7` is the batched `cat-file --batch` blob reader this unit's §3 defers to. Neither
is importable here: kits are COPY-INSTALLED and carry their shared code inline rather than depending
on `tools/lib/`, so `check-unattended.sh` holds its own accessors by design, and the reuse is of the
technique and its recorded measurements rather than of a file. No existing seam fits as an import.

Recall terms used: gate leg git spawn process count batch cat-file rev-list memoise warm table record
loop.
