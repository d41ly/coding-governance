# TOOL-dPlacedRequest-56 — the round-4 promotions' minors: fresh race attempts, failures staged so they take, one oracle contract, and criteria that read the places they name

**Status:** DEFERRED · rev-5 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 29 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 |
| [2026-10-25-build-TOOL-dPlacedRequest-56-deviation-561.md](../build/2026-10-25-build-TOOL-dPlacedRequest-56-deviation-561.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-56-deviation-562.md](../build/2026-10-25-build-TOOL-dPlacedRequest-56-deviation-562.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 |
| [2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-4 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md`)
exited CONVERGED with 25 confirmed findings. Its three highs are units 53, 54 and 55. This unit is
the batch BUILD-METHOD M4 makes of the rest: 12 MEDIUM and 10 LOW findings by raw id, one scope item
per id, each naming its finding and, in brackets, the review item holding it (M1 to M9, L1 to L7).
Six review items hold two ids each (M1: 7 and 18; M2: 2 and 23; M5: 9 and 25; L1: 4 and 20; L2: 5
and 10; L3: 6 and 11), and M1 restates H1's defect, which unit 53 closes at HIGH. Each id still gets
its own item and its own observation. The minors land on eight units, so this unit repairs none in
particular and sits above every unit of the build, at order 29, after units 53 to 55 at 28.
Criterion ACn observes item Sn.

| Item | Finding | Severity | Lands on |
|---|---|---|---|
| S1, S2 | 7, 18 (M1) | MEDIUM | unit 52 |
| S3, S4 | 2, 23 (M2) | MEDIUM | unit 52 |
| S5 | 3 (M3) | MEDIUM | units 48, 50 |
| S6 | 8 (M4) | MEDIUM | units 44, 52 |
| S7, S8 | 9, 25 (M5) | MEDIUM | unit 52 |
| S9 | 12 (M6) | MEDIUM | units 45, 51, 52 |
| S10 | 13 (M7) | MEDIUM | units 43, 44 |
| S11 | 19 (M8) | MEDIUM | unit 52 |
| S12 | 24 (M9) | MEDIUM | unit 51 |
| S13, S14 | 4, 20 (L1) | LOW | unit 51 |
| S15, S16 | 5, 10 (L2) | LOW | unit 51 |
| S17, S18 | 6, 11 (L3) | LOW | units 50, 52 |
| S19 | 14 (L4) | LOW | units 44, 52 |
| S20 | 15 (L5) | LOW | units 47, 50, 52 |
| S21 | 21 (L6) | LOW | unit 51 |
| S22 | 26 (L7) | LOW | unit 52 |

## 2. Scope (IN)

Every edit to another unit's spec is in place, one rev bump per spec with its §9 line naming this
unit and the items it carries.

- **S1** — finding 7 (M1). 52's "named in two places" criteria observe each place. AC1 extracts 48's
  S2 paragraph and its §3 Edges, AC6 48's S1 paragraph and its §5 risks line, and AC9 43's S22
  paragraph and its AC22 bullet, each by the `awk` paragraph form 52 S15 uses, and each extract must
  name the pattern (`S25`, `43 S30`, `48128`). Unit 53's occurrence counts stay beside them. Observed
  by AC1.
- **S2** — finding 18 (M1). Under 52 §6's `flat` definition, one sentence: `grep -c` over `flat`
  answers present or absent only, and a count of 2 or more is `grep -o '<pat>' | wc -l`. Observed by
  AC2.
- **S3** — finding 2 (M2). Each attempt of 52's placed race runs on a fresh fixture, a new unit-19
  clone and bare remote, so no stored `requests/<key>.md`, `.typed` line or remote record an earlier
  attempt wrote is met. 52 S4 and its §4 sketch state it. Observed by AC3.
- **S4** — finding 23 (M2). The rest of the per-attempt reset. The arm records the health log's line
  count when `$h/held` appears and reads only lines past it for `node-lock-broken`. "Never placed"
  fails the arm at once, as 48 S3 says. An A still running at its bound is killed and waited for
  before the next attempt. 52 S3, S4 and the §4 sketch state it. Observed by AC4.
- **S5** — finding 3 (M3). 50 §4 Files touched and 48 §4 Files touched each say that the other unit
  writes `tools/unattended/unattended.test.sh` at order 25, so the two passes run in sequence.
  Observed by AC5.
- **S6** — finding 8 (M4). The oracle's `rev-list --count` ends its revisions with `--`, and `n` is
  checked numeric before use: `case $n in ''|*[!0-9]*) echo 'version oracle: rev-list failed'; exit
  2;; esac`. Written into 44 §4 and 52's §4 sketch; 52 §4 Evidence names the deep-path failure.
  Observed by AC6.
- **S7** — finding 9 (M5). 52 AC19 and its §7 arm line stage the scratch-directory skip with a file
  where the directory should be: `: > "$s/f"; CARD_DIR="$s/f/sub"`. The built case in
  `skills/session-kickoff/manifest-check.test.sh` stages it so, and neither text says "unwritable".
  Observed by AC7.
- **S8** — finding 25 (M5). Before it judges the cell, that case asserts its stage took effect:
  `mkdir -p "$CARD_DIR"` fails, else the case fails naming the stage. Observed by AC8.
- **S9** — finding 12 (M6). One fixture description. 51 S2 is rewritten so 45 AC2 cites
  `TOOL-dPlacedRequest-44` §6's fixture by its count, two branch commits and `· 2 commits`, and runs
  each row's command on it; 45 AC2 is restated to that citation and holds no second description of
  the fixture. 52 S14's "as 51 S2 writes it" points at the citation, and 52 AC14 checks that 45 AC2
  names `TOOL-dPlacedRequest-44` and holds no `--no-ff`. Observed by AC9.
- **S10** — finding 13 (M7), the skeptic's corrected fix, its 44 §8 half being S19's. 44 is restated
  to the oracle units 52, 54 and 55 leave: S2 and the §5 error line read exit 2 on an empty walk; §5
  risks names the fact-1 derivation with the own-merge test, a missing or foreign merge exiting 2;
  the §4 Evidence observations and the Alternatives bullet name the same derivation; and AC3 runs on
  52 AC13's `git commit-tree -p <tip> -p <base>` merge carrying the lander's subject. 43 AC24 reads
  "header line, exit 0, no `KIT_` line". Observed by AC10.
- **S11** — finding 19 (M8). 52 §4 Evidence measures unit 34 with every pending edit applied (52
  S11's AC59 text as `TOOL-dPlacedRequest-54` S3 cuts it, the §9 lines of 49, 52 and 54) after a
  `gen_build_index.py --write` render, and records the figure, its date and the margin under 48128.
  Observed by AC11.
- **S12** — finding 24 (M9). 51 AC1 gains the absence of 45 rev-2's row: `grep -cE 'git log
  --first-parent <base>\.\.HEAD` *\|'` over the record prints 0, its red observed by planting that
  row in a scratch copy. 51 AC2 also runs the `--name-status` form and expects `M
  tools/unattended/unattended.sh` under the merge. A record that still holds the rev-2 row is
  corrected in place. Observed by AC12.
- **S13** — finding 4 (L1). 51 S1's second row reads "`git log --first-parent -p <base>..HEAD`, or
  `--name-status`", the spelling of 51 §4 and AC1. Observed by AC13.
- **S14** — finding 20 (L1). One spelling, observed: the string AC1 greps for appears in 51's S1
  paragraph, its §4 table and its AC1 bullet alike. Observed by AC14.
- **S15** — finding 5 (L2). Every `grep -cF` in 51 AC1 passes its pattern through `-e`. Observed by
  AC15.
- **S16** — finding 10 (L2). Each command 51 AC1 spells is run once, as written, over the record at
  this unit's pass; 51 §4 Evidence records that each exited 0 or 1. Observed by AC16.
- **S17** — finding 6 (L3). 50 §4 Evidence cites 47 by label, S1 and AC1 to AC3, with no line
  numbers. Observed by AC17.
- **S18** — finding 11 (L3). The same shape in the other round-4 promotion that has it: 52 AC15's
  "43's `:168`" names 43's §3 hands-off edge to 48 by label. Observed by AC18.
- **S19** — finding 14 (L4). 44 §8 F1 is amended in place to (a'), the lander's fact-1 derivation
  with the own-merge test, refusing with exit 2, "superseded by `TOOL-dPlacedRequest-52` F1 and
  `TOOL-dPlacedRequest-54` F1"; 52 F1 names 44 F1 as the decision it supersedes. Observed by AC19.
- **S20** — finding 15 (L5). The torn stamp joins its siblings. 47 AC4 gains a third row, a middle
  commit whose `seen-utc` is `2026-10-2`, expected `live`, in 47's arm; 52 AC21's second clause
  points at that row instead of planting its own chain. 52's Edges gain a consumes-from
  `TOOL-dPlacedRequest-50`, mirrored by a hands-off in 50. Observed by AC20.
- **S21** — finding 21 (L6). 51 §5 observability reads "none: the description line `gotchas.py`
  prints is unchanged; the pair is named in the record body". Observed by AC21.
- **S22** — finding 26 (L7). 52 S26 states that the first `renews:` line of a commit wins, as
  `read_claims` keeps the first occurrence of every key (`tools/unattended/unattended.sh:2171`).
  52 AC26 gains the row of §4, and the built walk reads the first line. Observed by AC22.

## 3. Non-goals (OUT)

- No second mechanism for a high: units 53, 54 and 55 own findings 1, 16 and 22. S1 and S2 sit beside
  unit 53's counts, and S6, S10 and S19 restate the oracle as units 54 and 55 leave it.
- No renumbering of any order: S5 records the sequence line for a pair of order-25 passes in text,
  and the dispatch's recorded write sets are what sequence them (BUILD-METHOD M6).
- No new gate leg, no lint over spec criteria and no new bug-class record: each arm joins an existing
  suite, and the closing review's left-shift decides any record (BUILD-METHOD M8).
- No edit to `TOOL-dPlacedRequest-34`: S11 measures it after unit 54's cut.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-52` — §6's `flat` note and AC1, AC6, AC9, AC14, AC15, AC19, AC21 and AC26, S3, S4, S14, S26, §4's sketches and Evidence, Edges and F1, which S1 to S4, S6 to S9, S11, S18 to S20 and S22 amend
- **consumes-from** `TOOL-dPlacedRequest-44` — S2, §4, §5, AC3 and §8 F1, which S6, S10 and S19 restate to one oracle contract
- **consumes-from** `TOOL-dPlacedRequest-43` — AC24, which S10 restates to the oracle's header line and exit 0
- **consumes-from** `TOOL-dPlacedRequest-45` — AC2, which S9 makes cite 44's fixture by count
- **consumes-from** `TOOL-dPlacedRequest-47` — AC4's rows and its arm, which S20 extends with the torn-stamp row
- **consumes-from** `TOOL-dPlacedRequest-48` — §4 Files touched, which S5 gives its sequence line
- **consumes-from** `TOOL-dPlacedRequest-50` — §4 Files touched, Evidence and Edges, which S5, S17 and S20 amend
- **consumes-from** `TOOL-dPlacedRequest-51` — S1, S2, §4 Evidence, §5, AC1 and AC2, which S9 and S12 to S16 and S21 amend
- **consumes-from** `TOOL-dPlacedRequest-53` — 52's occurrence counts, beside which S1 and S2 observe each place and note what `grep -c` answers
- **consumes-from** `TOOL-dPlacedRequest-54` — the own-merge test and 34 AC59's one-line cut, which S10 and S19 restate in 44 and S11 measures unit 34 after
- **consumes-from** `TOOL-dPlacedRequest-55` — the oracle's captured walk, after which S6 guards the count line
- **consumes-from** `TOOL-dPlacedRequest-57` — 34 AC59 without its base, after which S11 measures unit 34; that unit's pass runs first at this order
- **hands-off** `TOOL-dPlacedRequest-58` — S3, §4's per-attempt sketch, AC3 and the race arm, which that unit gives the handshake reset; AC3 is read again at that unit's pass
- **hands-off** `TOOL-dPlacedRequest-59` — S4, S11, S19, S22, §3, §4, §5, §10 and AC5, which that unit's minors amend; a unit 34 over 48128 at this pass, and AC10 and AC19 while 44 F1's options keep the phrases they count, are read at that unit's pass
- **hands-off** `TOOL-dPlacedRequest-61` — §1, the consumes-from edge to 57, the header order and AC5 as unit 59 restates it, which that unit's items for findings 3 and 10 amend
- **hands-off** `TOOL-dPlacedRequest-63` — §3's renumbering bullet, which that unit's item for finding 18 restates

## 4. Design

### The placed race, per attempt (S3, S4)

```
attempt 1..3:
  fresh unit-19 clone and bare remote; m = lines in the health log
  A in background; wait for $h/held (30 s bound), else fail "request race never placed"
  stamp th; B to its end; stamp tb
  touch $h/release; wait for A (bound), else kill A and wait
  tb - th <= NODE_LOCK_BOUND and no node-lock-broken past line m -> judge AC1's asserts, stop
  else -> discard this attempt
every attempt overran -> fail "request race placed past the lock bound"
```

### The duplicate-key row (S22)

```
commit    renews lines           seen-utc                expect
tip       renews: no             a minute ago
middle    renews: no, renews: -  a minute ago
start     renews: no             1,000 hours ago         stale  (first line wins)
red copy  the walk keeps the last renews: line           live
```

### Evidence

- `skills/session-kickoff/manifest-check.sh:653-654` skips only when `mkdir -p "$CARD_DIR" && mktemp
  -d "$CARD_DIR/.claims.XXXXXX"` fails; the review's skeptic measured `chmod 555` leaving `mktemp -d`
  working under Git Bash on NTFS, and a file in the directory's place failing `mkdir -p` with "Not a
  directory".
- `tools/unattended/unattended.sh:2171` keeps a key only when `!(k in v)`, the first occurrence.
- `tools/memory-tree/gotchas.py:276-279` takes `description` from the front matter and no body text.
- 52 AC15 cites 43 at `:168`, which today is 43's hands-off edge to 48; 50 §4 Evidence cites 47 at
  `:33-35` and `:111-120`, where 47 now holds S1 at :34 and AC1 to AC3 at :114, :118 and :121. Read
  2026-10-25.
- Unit 34 measured 47490 bytes at rev-7 and 47782 at rev-8, after this round's edge line to unit 54,
  on 2026-10-25: 346 under 48128 before any edit S11 names. PINNED at that date.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/`: the specs of units 43, 44, 45, 47, 48, 50, 51 and 52, each
  edit a rev bump with its §9 line
- `tools/unattended/unattended.test.sh`: S3, S4, S20 and S22 in their arms
- `tools/unattended/unattended.sh`: S22's first-line read, where the built walk reads another line
- `skills/session-kickoff/manifest-check.test.sh`: S7 and S8
- `memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md`: S12, where 51's pass left the
  rev-2 row

### Alternatives rejected

- **Two batches.** S9 and S12 to S16 and S21 land on unit 51 and write only 51, 45 and the record, a
  write set disjoint from the rest. Split off, that half repairs unit 51 and takes order 27 while this
  half takes 29, so the two never build concurrently, which is the only reason M4 admits a second
  batch.
- **Reset the race's files in place (S3).** It needs every path an attempt writes named and kept
  current; a fresh clone and remote reset all of them, the unnamed ones included, for at most two
  more fixture builds.
- **Counts alone for the two places (S1).** Two mentions inside one paragraph reach 2 and pass a
  criterion that names two places.

## 5. Production-readiness checklist

- security — S22 makes a duplicate `renews` key read as the strict reader reads it, so a `-` line
  cannot turn a stale take-over check `live`.
- perf / scale — S3 builds at most three fixtures per arm run; the oracle gains one `case`.
- error / empty / loading states — S4 fails an unplaced race at once; S6 and S8 name their failures.
- observability — S4's health-log read names only its own attempt's event.
- risks — S7's staging relies on `mkdir -p` refusing a path under a file, measured on Git Bash.
- testing — the probes of §6 and the arms of §7.
- migration — none: every surface is new in this build.
- user docs — none beyond the specs and one class record.

## 6. Acceptance criteria

`flat <file>` is `TOOL-dPlacedRequest-52` §6's. The fixtures are the named units': unit 19's clones for
the race, unit 26's chains for the walk, and unit 52's oracle fixture under `%TEMP%`, each
`RUN_CLAIMS=on` unless stated.

- **AC1** — When 52's AC1, AC6 and AC9 extractions run over the built 48 and 43, 48's S2 and its Edges
  each name `S25`, 48's S1 and its §5 risks line each name `43 S30`, and 43's S22 and AC22 each name
  `48128`. Red when: two mentions in one paragraph satisfy a criterion that names two places.
- **AC2** — When 52 §6 is read, the sentence under `flat` names `grep -o` and "present or absent".
  Red when: a reader takes `grep -c` over `flat` for a count.
- **AC3** — When 52's placed-race arm runs with B delayed 11 s on attempt 1 only, the arm prints two
  distinct clone paths, and attempt 2's A exits 0 with `.typed` holding s1 alone and one remote
  record. Red when: attempt 2 meets attempt 1's stored copy and reads `never placed` or `collision`.
- **AC4** — When that run ends it passes, naming `node-lock-broken` for attempt 1 alone; with a
  pass-through `cp`, it fails `request race never placed` on attempt 1; after either, `ps` lists no
  `--request` process of the arm. Red when: an earlier attempt's event marks a later one, or A
  outlives the arm.
- **AC5** — When `grep -n 'in sequence' 2026-10-25-spec-TOOL-dPlacedRequest-48.md 2026-10-25-spec-TOOL-dPlacedRequest-50.md | grep -F tools/unattended/unattended.test.sh`
  runs, it prints one line from each spec, each naming the other unit. Red when: two passes of one
  order write one suite file with no sequence line.
- **AC6** — When the oracle runs on 52's fixture from a working directory more than 180 characters
  deep, its header ends `· 2 commits`; with a stub `git` whose `rev-list --count` alone prints
  nothing, it prints `rev-list failed` and exits 2. Red when: a deep path reads as an empty walk.
  fixture: built by the probe under `%TEMP%`; the deep path reproduces on Windows only.
- **AC7** — When the manifest-check case stages `CARD_DIR="$s/f/sub"` under a file `$s/f`,
  `derive_claims_line` prints `claims — skipped: no scratch directory under`, and `grep -c chmod`
  over that case prints 0. Red when: the stage leaves the directory creatable and the skip never runs.
- **AC8** — When the case's stage is swapped for `chmod 555` on a directory under Git Bash, the case
  fails naming its stage and judges no cell. Red when: a stage that did not take is judged as a pass.
- **AC9** — When 45's AC2 bullet is read, it names `TOOL-dPlacedRequest-44` and `· 2 commits` and holds
  no `--no-ff`, and 52 AC14 checks both. Red when: 45 describes the shared fixture a second time.
- **AC10** — When `flat 2026-10-25-spec-TOOL-dPlacedRequest-44.md | grep -oE 'merge-base (form|origin)' | wc -l`
  runs it prints 0, `grep -oE 'walked no commit[^.]*exits 1'` over the same prints nothing, 43 AC24
  names `exit 0`, and on 44 AC3's `commit-tree` merge the oracle prints `walked no commit of the build`
  and exits 2. Red when: a reader of 44 meets two exit contracts for one oracle.
- **AC11** — When `gen_build_index.py --write` has rendered after every edit S11 names, `wc -c` of
  unit 34's spec prints at most 48128, and 52 §4 Evidence states that figure with its date.
  Red when: the ceiling is set without measuring the file it bounds.
  figure: DERIVED at observation.
- **AC12** — When `grep -cE 'git log --first-parent <base>\.\.HEAD` *\|'` runs over the record, it
  prints 0, and over a scratch copy with 45 rev-2's row planted it prints 1; 51 AC2's `--name-status`
  run prints `M tools/unattended/unattended.sh` under the merge. Red when: a stale row stands beside
  its correction.
- **AC13** — When 51's S1 paragraph is extracted by the `awk` form of 52 S15 and squeezed, it holds
  `git log --first-parent -p <base>..HEAD`. Red when: S1 spells the row another way.
- **AC14** — When `grep -cF -e 'git log --first-parent -p <base>..HEAD'` runs over 51's S1 extract, its
  §4 table and its AC1 bullet, each prints at least 1. Red when: one grepped string has two spellings.
- **AC15** — When `grep -n 'grep -cF'` runs over 51, every hit passes its pattern after `-e`.
  Red when: a pattern beginning `--` parses as an option.
- **AC16** — When each command 51 AC1 spells runs as written over the record, each exits 0 or 1 and
  none prints `unknown option`. Red when: a criterion errors before it measures.
- **AC17** — When ``grep -nE '\(`:[0-9]' 2026-10-25-spec-TOOL-dPlacedRequest-50.md`` runs, it prints
  nothing, and 50 §4 Evidence names 47's S1 and AC1 to AC3. Red when: evidence cites a sibling's
  moved lines.
- **AC18** — When 52's AC15 bullet is read, it names 43's §3 hands-off edge to 48 and holds no `:168`.
  Red when: a criterion cites a sibling spec by a line that moves.
- **AC19** — When `flat 2026-10-25-spec-TOOL-dPlacedRequest-44.md | grep -o 'merge-base form elsewhere' | wc -l`
  runs, it prints 0, 44 F1 names `TOOL-dPlacedRequest-52`, and 52 F1 names 44 F1. Red when: 44 keeps
  a live resolution for a form no oracle runs.
- **AC20** — When 47's arm runs AC4's three rows over the built walk, the unset, `-` and `2026-10-2`
  rows each print `live`, and the `2026-10-2` row prints `stale` on a scratch copy without 52 S21's
  shape test; 52's and 50's Edges carry the paired edge. Red when: the torn-stamp chain is planted
  twice.
- **AC21** — When `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh`
  runs, the record's line is its front-matter description, and 51 §5 says so. Red when: §5 claims an
  effect the command does not show.
- **AC22** — When the §4 duplicate-key row runs, `--claims` prints `stale`; the red copy prints
  `live`. Red when: a duplicate `renews` key resolves otherwise than `read_claims` reads it.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC3 AC4 AC20 AC22 · the race's fresh attempts, the torn-stamp row and the duplicate-key row, each staged against the arm or walk as unit 52 leaves it · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC7 AC8 · a file in `CARD_DIR`'s parent place, staged against a `chmod` stage that does not take · none

## 8. Open questions

- **F1 — How does each race attempt start clean (S3)?** (a) A fresh unit-19 clone and bare remote
  per attempt; (b) the stored copy, `.typed` and the remote's request ref reset in place. (b) must
  name every write an attempt makes and stay current with it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's first fix judged sound. widens: none · relaxes: none
- **F2 — How are the named places observed (S1)?** (a) One extract per named place beside unit 53's
  counts; (b) the counts alone. (b) passes two mentions in one paragraph. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the review's second fix judged sound. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-4 promotions' 12
  MEDIUM and 10 LOW findings.
- rev-2 · 2026-10-25 · AC5 observes the two specs by one grep pipeline, the shared suite file a
  `grep -F` argument rather than a token of its own, so the criterion reads as a grep over specs and
  never as a suite run (the promoted fix brief's [bar] hit); the suite stays on §7's `New arm:` line.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the consumes-from edge to `TOOL-dPlacedRequest-57` and the hands-off edges to `TOOL-dPlacedRequest-58` and `TOOL-dPlacedRequest-59`, mirroring theirs.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edge to `TOOL-dPlacedRequest-61`, mirroring its consumes-from.
- rev-5 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edge to `TOOL-dPlacedRequest-63`, mirroring its consumes-from.

## 10. Reuse audit

Each item extends the unit its finding names, and the new code reuses four seams: unit 19's fixture
builder for S3, the `awk` paragraph extraction 52 S15 uses for S1 and S13, the first-occurrence rule
of `read_claims` (`tools/unattended/unattended.sh:2171`) for S22, and the scratch-directory skip of
`derive_claims_line` (`skills/session-kickoff/manifest-check.sh:653-654`) for S7.
`python tools/codebase-map/reuse_lookup.py "reset every piece of state a retried test attempt wrote
before the next attempt"` ranked `before`, `plan_state` and `resolve_state_dir`, name stems only,
none a retry reset: no existing seam fits beyond unit 19's fixture. `python
tools/memory-recall/query.py "how is a spec audit's minor findings batch promoted into one unit that
amends several specs"` returned TOOL-aDistilledCharter-7, `TOOL-dPlacedRequest-52`,
TOOL-aGraftedHelix-32 and `TOOL-dPlacedRequest-49`, batches of the same kind; none disagrees with
source.

Recall terms used: minors batch promote medium low spec audit round finding item amend in place edge mirror
