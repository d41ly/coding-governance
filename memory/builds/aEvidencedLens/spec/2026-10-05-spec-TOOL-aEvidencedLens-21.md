# TOOL-aEvidencedLens-21 — the closing diff review's batched minors, round 1

**Status:** CLOSED · rev-1 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-aEvidencedLens-21-1-ab-replay.md](../build/2026-10-05-build-TOOL-aEvidencedLens-21-1-ab-replay.md) | journal | — |
| [2026-10-05-build-TOOL-aEvidencedLens-21-2-acceptance-ledger.md](../build/2026-10-05-build-TOOL-aEvidencedLens-21-2-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-aEvidencedLens-21-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-21-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build
(`reviews/2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md`) exited CONVERGED
at round 1 with nine confirmed findings: four MEDIUM and five LOW, no blocker and no high. BUILD-METHOD
M4 promotes them all, and because nothing above MEDIUM stood they form ONE batched unit, the one
exception M2's one-mechanism rule admits. This is that unit. It folds nothing into a landed spec. One
unit, not two: the build is driven by one main loop, so a second unit over a disjoint write set
would buy no concurrency.

It closes the record's seven items:

- **M1 (MEDIUM, id 2)** — the scratch-under-repo refusal skips silently on a relative or
  MSYS-spelled `repo`. Closed by S1.
- **M2 (MEDIUM, id 5)** — the disposal unit floor counts raw ids while the prompt counts merged
  items. Closed by S2.
- **M3 (MEDIUM, id 7)** — the hostile-value matrix's `--review` row passes by refusing for an
  unrelated reason. Closed by S3.
- **M4 (MEDIUM, id 10)** — the mandate's replay half is unrecorded. Closed by S4, which also fixes
  the two replay-only defects it finds still live (S5, and S1's dot-dot and MSYS arms).
- **L1 (LOW, ids 1, 4, 6)** — check 19's round-bound clause: decoy masking, zero-padding and skip
  wording. Closed by S6.
- **L2 (LOW, id 8)** — the move check's NOT-MOVED classification has no arm. Closed by S7.
- **L3 (LOW, id 11)** — the README's parked decisions say nothing is open while `RUN.md` parks the
  generation bound. Closed by S8.

## 2. Scope (IN)

- **S1 — M1, and the live half of replay id 38.** On the spec kind, `tier2-review.js` refuses a
  `repo` that is not absolute, by the same shape test `scratch` already takes: a relative `repo`
  such as `"."` cannot be compared in a runtime with no filesystem, so the refusal that skipped it
  silently now refuses by name. Before comparing, both values fold a leading `/<letter>/` to
  `<letter>:/` after the existing slash, case and trailing-slash fold, so `/c/p/x/t` is under
  `C:/p/x`. A `scratch` or `repo` carrying a `..` segment is refused, because the comparison is
  textual and `/tmp/q/../r/x` resolves under `/tmp/r`. The args doc at the `scratch:` line and the
  comment above `scratchRule` state all three, and that an 8.3 short name or a link aliasing `repo`
  is still not seen. The prelude of `unattended-build.js`, which copies the comparison so it
  refuses before any stage spends work, takes the same three changes and keeps one answer. The
  diff kind does not move: it never reads `scratch`, and its `repo` stays as accepted today.
  Observed by AC1 and AC2.
- **S2 — M2.** The disposal floor and the disposal prompt agree on RAW ids. The prompt states
  that each BLOCKER or HIGH id is its own unit even where the report merged several ids into one
  item, because the floor, the driver's owed count and check 2 all count raw ids; ids sharing an
  item each take a unit, and each unit's spec names its id and the item it shares. The floor's
  refusal reason says `one unit per RAW blocker and high id, merged items included`, keeping its
  leading clause `<k> unit(s) for <b> blocker(s), <h> high(s) and <m> minor(s), below the floor of
  <n>` byte-identical so the arms that read it still read it. No count changes basis. Observed by
  AC3.
- **S3 — M3, and its class.** The matrix helper's `review)` line passes `--highs 0 --minors 0`, so
  the one-line hostile form reaches `park()` again. The record verbs' liveness shape is added for
  `--review`: on the one-line form the run-state file carries ONE row holding
  `review · item yes\nphase: LANDED · reason verdict CLEAN · blockers 0 · CONVERGED · highs 0 · minors 0`.
  The class: the matrix records each verb's exit status on the one-line form, and a verb that
  refused it reds the matrix, naming the verb, unless a declared exemption list in the same block
  names that verb with the reason it refuses the value itself. An exemption naming a verb that
  ACCEPTED the form also reds, so the list cannot go stale. The list's members are measured by the
  pass against the fixed helper and recorded in the acceptance ledger; this spec does not know them.
  Observed by AC4.
- **S4 — M4, the replay record.** This unit writes
  `memory/builds/aEvidencedLens/build/2026-10-05-build-TOOL-aEvidencedLens-21-1-ab-replay.md`,
  carrying `**Serves:** journal TOOL-aEvidencedLens-21`. It holds:
  - both `review_replay.py` outputs whole, the forward run (round-1 record as known, the replay
    report as candidate) and the reverse run (the two swapped);
  - the two per-lens tables, round 1's four lenses and the replay's five, each lens's raw,
    confirmed, refuted and precision;
  - an old-versus-new table: raw, confirmed, refuted, precision, items by severity and raw findings
    by severity, for the round-1 record against the replay;
  - the ceiling the tool states: a spec-mode match is the same file and the same SECTION, so one
    candidate in a spec's §2 matches every known finding in that §2, a MATCHED pair is not the same
    defect, and both recall figures are upper bounds at that granularity;
  - a liveness row for every replay-only HIGH or MEDIUM finding, and for the two HIGH items that
    matched only at section level: its id, its defect in one line, `live` or `not live` at this
    unit's base commit, and the probe that decided it;
  - the provenance: the replay ran the improved harness over the same eleven round-1 spec blobs in
    a frozen clone at `4d0d64688`, and the report stayed in the session scratch. It is not copied
    under `reviews/`, where its `**Serves:** spec-audit` line would read as a second audit of
    those specs.
  Observed by AC5.
- **S5 — replay id 37, live.** `PROBE_RULES` in `tier2-review.js` gains one constant rule, the
  skeptic's corrected fix: "Write temporary files only under a subdirectory of the scratch
  directory named for your own role, <lens key> for a finder or verify-<batch> for a skeptic,
  created on first use." The rule interpolates nothing, so it joins the input print, and the
  `find:` and `verify:` PROBE POLICY slices stay byte-identical to each other. Concurrent lenses
  then no longer overwrite one another's same-named probe files. Observed by AC6.
- **S6 — L1.** Three changes to check 19's round-bound clause in `check-unattended.sh`.
  - Finding 4: `read_rounds_of` strips leading zeros from an all-digit value AFTER its default
    fallback, an all-zero value printing `0`, so `01` and `1` are one bound and `00` never reads as
    absent.
  - Finding 1, the skeptic's corrected fix: a blob carrying more than one `REVIEW_ROUNDS=`
    assignment line prints `rounds=multi:<v1>,<v2>…`, each value normalised, in file order. Its
    string differs from any single-line parent's, so `scan_round_writes` reports the commit as a
    round write, fail-closed and without executing the blob. A parent carrying the same lines
    compares equal and reports nothing. The NOT-CHECKED header names the masked shape, an
    assignment masked by a later one inside a dead block, a function body or a heredoc, and says it
    is read fail-closed. No conf in this repository's history carries two assignment lines.
  - Finding 6: the two skip reports read `check 19 SKIPPED the grant-write and round-bound arms for
    $f`, and the local-ref report and the empty-range note each name the round-bound arm beside the
    grant-write arm, matching the fallback that already names both scans.
  Observed by AC7 and AC8.
- **S7 — L2.** A `tier2-review.test.sh` arm feeds a probe `blobs` row whose 40-hex `now` begins with
  the pinned blob, `abc1234` followed by 33 zeros, for subject `m.md` beside a moved subject, and a
  second case where `m.md` is the only subject. It asserts no `m.md MOVED` WARNING is logged, the
  SUBJECT line reads `  - m.md  blob abc1234` with no MOVED suffix, and in the sole-subject case
  RUN INTEGRITY carries `no checked subject moved`. The arm is observed red once against a copy of
  the render whose predicate is always MOVED. Observed by AC9.
- **S8 — L3.** The build README's `## Parked decisions` slot names the one parked question: the
  spec-audit promotion-chain generation bound, parked in `RUN.md` at 2026-10-04T23:32:23Z and
  re-parked at 2026-10-05T03:59:40Z when the run stopped the chain after round 4. It names the
  options those rows record and that `specs-audited` is overridden at the close naming the park.
  The slot body stays within its 1800-byte ceiling in
  `tools/memory-tree/build-readme-slot-limits.txt`. Observed by AC10.
- **S9 — the suites.** The arms S1, S2, S3, S6 and S7 name are written into the suites that pin
  each file, and each suite's floor moves by the assertions added. NOT OBSERVED inside the pass: a
  pass runs no suite (M6), and each arm is declared under `New arm:` in §7; the main loop runs the
  suites once at VERIFYING.

## 3. Non-goals (OUT)

- The skeptic's cross-batch duplicate gap, the root of M2's two raw HIGH ids for one defect
  (`tier2-review.js`'s spec skeptic refutes a duplicate only within its batch). M2's defect is the
  disagreement between prompt and floor, and S2 closes it.
- A shared path-containment helper inlined into both workflow scripts with a parity check. Mirrored
  arms in both suites carry the one answer for now.
- The BUILD-METHOD wrap-up checklist line M4's record proposes as its left-shift. The method is a
  governance carrier and a watched file of the kickoff manifest, and a run may not change it (M3
  veto 2). Handed off below.
- The hygiene check L3's record proposes, reding a README whose parked slot reads "None yet." beside
  a `RUN.md` decision row. It is a new check in the memory-tree kit; the class is the universal
  `two-answers-to-one-question` entry the checklist already selects on every closing round. Handed
  off below.
- Any replay-only finding found NOT live at base. S4 records it and changes nothing.
- A kit version bump. The main loop bumps once at the close.
- The README's roster row for this unit. The main loop's `--rescope` added the unit, and its row is
  the main loop's.

### Edges

- **consumes-from** `TOOL-aEvidencedLens-2` — the spec-kind `scratch` refusal and `PROBE_RULES` that
  S1 and S5 amend. Without them there is no refusal to extend and no policy to add a rule to.
- **consumes-from** `TOOL-aEvidencedLens-5` — the build harness's prelude copy of that refusal, which
  S1 amends so the two scripts keep one answer.
- **consumes-from** `TOOL-aEvidencedLens-8` — the disposal unit floor and its prompt, which S2 makes
  agree.
- **consumes-from** `TOOL-aEvidencedLens-7` — the `--review` counts requirement that made the matrix
  row refuse, which S3's helper now satisfies.
- **consumes-from** `TOOL-aEvidencedLens-9` — `read_rounds_of`, `scan_round_writes` and the clause's
  NOT-CHECKED header, which S6 amends.
- **consumes-from** `TOOL-aEvidencedLens-14` — the shared walk that put the round scan behind the
  grant arm's skip reports, which S6 rewords.
- **consumes-from** `TOOL-aEvidencedLens-4` — the move check's predicate, which S7's arm pins.
- **consumes-from** `TOOL-aEvidencedLens-10` — `review_replay.py`'s spec mode, which S4 runs both
  ways.
- **hands-off** external — the BUILD-METHOD wrap-up line for a mandate deliverable handed to the
  main loop as a non-goal, and the README-versus-`RUN.md` parked-decisions hygiene check. Both are
  owner turns: one changes a governance carrier, the other adds a kit check.

## 4. Design

### Evidence

Read at `11a0965e7` on 2026-10-05. The run branch past base touches `tools/` only through this
build's own units, and every line below is in a file those units wrote.

- `tools/workflows/tier2-review.template.js:265` runs the scratch comparison only when `repo` matches
  `/^(\/|[A-Za-z]:[\\/])/`, and folds slashes, case and a trailing slash at `:263-264`, with no
  `/<letter>/` fold and no `..` handling. `:120` refuses an ABSENT `repo`, so the `|| '.'` default
  at `:134` is unreachable; the defect stands for an explicit relative `repo`, which the review's
  skeptic also confirmed.
- A probe of the render's prelude, extracted as the suite extracts it, with
  `{kind: 'spec-audit', scratch, repo}` printed: `repo "."` beside `C:/projects/x/tmp` proceeds;
  `C:/projects/x` beside `/c/projects/x/tmp` proceeds; `/c/projects/x` beside `C:/projects/x/tmp`
  proceeds; `/tmp/r` beside `/tmp/q/../r/x` proceeds. `/tmp/r` beside `/tmp/rs` proceeds, which is
  correct and must stay so.
- `tools/workflows/unattended-build.template.js:236-239` copies the same comparison under the same
  absolute-shape condition, with the same two gaps; `:206` refuses an absent `repo` only.
- The suites pass `repo: '/tmp/r'` and `"repo":"/tmp/r"` everywhere, and the one Windows arm passes
  `c:/r`, so refusing a relative `repo` on the spec kind reds no existing arm.
- `tools/workflows/unattended-build.template.js:1490` sets `unitFloor = au.blockers + au.highs + …`
  from the review's RAW counts, and `tools/workflows/tier2-review.template.js:1592-1594` derives
  `blockers` and `highs` from `perRaw`. The prompt at `unattended-build.template.js:1344-1347` says a
  merged finding "still counts once, by its own id" and never says one unit per raw id.
- `tools/unattended/check-unattended.sh:739-747` reads `highs` and `minors` from the review row and
  owes one unit per blocker and high from them, and `tools/unattended/unattended.sh:10230` computes
  the same `owe`. Both are raw, because `--highs` is the raw count the harness records.
- `tools/unattended/unattended.test.sh:2786` drives `run --review tRun --subject "$2" --verdict CLEAN
  --blockers 0` with no counts, and `tools/unattended/unattended.sh:10222-10223` refuses a terminal
  exit with no `--highs` and `--minors`, before `park()`.
- `read_rounds_of`, extracted from `tools/unattended/check-unattended.sh:1685-1700` and sourced,
  printed `rounds=01` for `REVIEW_ROUNDS=01` and `rounds=1` for `REVIEW_ROUNDS=4` followed by an
  `if false` block holding `REVIEW_ROUNDS=1`. `tools/unattended/lib-unattended.sh:184-189` accepts
  `01`.
- The two skip reports sit at `check-unattended.sh:2477` and `:2479`, the local-ref report at
  `:2471`, the empty-range note at `:2496`, the both-scans fallback at `:2490`, and the NOT-CHECKED
  header from `:2511`.
- `tools/workflows/tier2-review.template.js:771` classifies MOVED by `now.indexOf(String(x.blob)) !==
  0`; the suite's only 40-hex `now` is `MOVED40` at `tools/workflows/tier2-review.test.sh:1351`,
  which does not begin with the pin.
- `tools/workflows/tier2-review.template.js:441-450` holds `PROBE_RULES`, whose temp-file rule names
  the one shared scratch directory and no per-role subdirectory.
- `memory/builds/aEvidencedLens/README.md:47-49` reads "None yet."; `memory/builds/aEvidencedLens/RUN.md`
  carries the two decision rows at 2026-10-04T23:32:23Z and 2026-10-05T03:59:40Z.

### The replay, as measured

PINNED, measured 2026-10-05 by the main loop and re-derived by S4's two runs. Forward, with the
round-1 spec-audit record as known and the replay report as candidate: `replay: recall 31/45 = 0.69`,
fourteen candidate-only rows. Reverse, the two swapped: `replay: recall 25/38 = 0.66`, fifteen
candidate-only rows. The replay report: raw 42, confirmed 39, refuted 3, precision 0.93, 2 HIGH
items over 4 raw findings. The round-1 record: raw 49, confirmed 46, refuted 3, precision 0.94, 3 HIGH.

The forward run's replay-only HIGH or MEDIUM findings, each probed at `11a0965e7`:

| Replay id | Defect | At base | Probe |
|---|---|---|---|
| 3 | spec 11 AC6 cannot pass on a correct build | not live | spec 11 rev-3 at `fd063e749` excludes the history gotchas |
| 12 | spec 10's pins are read from the opening line | not live | `review_replay.py:127-137` reads every line before the first `## ` |
| 14, 28 | spec 7's refusal sentences carry no arm duty | not live | `check-arms.py --check` exits 0 |
| 23 | spec 1 misses the summed-kind arm `uvp.length` | not live | `tier2-review.test.sh:936` reads `uvp.length === 10` |
| 24, 25 | specs 6 and 10 omit `symbols.json` | not live | the map's symbol inventory carries every function units 6 and 10 minted |
| 26 | spec 11 omits the kickoff manifest re-stamp | not live | `manifest-check.sh` exits 0 on the kickoff manifest |
| 37 | one scratch directory for every probing agent | LIVE | no per-role rule in `PROBE_RULES`; fixed by S5 |
| 38 | the scratch test is textual: MSYS and `..` unfolded | LIVE in part | the probe above; fixed by S1. Its prefix-sibling case is fixed |

The two HIGH items matched round-1 findings only at section level. Replay H1, the moved-text read
resolving `<path>` outside `repo`, is not live: the acquire sentence hands `git -C ${repo} diff
<blob> -- <path>` at `tier2-review.template.js:892`. Replay H2, the terminal walk keyed on the grant
scan alone, is not live: `check-unattended.sh` walks on `[ -n "$maywr$mayrw" ]`, unit 14's fix.

### Inventory

No function is defined and no file is created under `tools/`, so the map's generated symbol
inventory does not move and no lexicon cell grades a new name. One returned prose string per
refusal moves, and one array entry joins `PROBE_RULES`.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/unattended.test.sh`
- `memory/builds/aEvidencedLens/README.md`
- `memory/builds/aEvidencedLens/build/2026-10-05-build-TOOL-aEvidencedLens-21-1-ab-replay.md`
- `memory/builds/aEvidencedLens/build/2026-10-05-build-TOOL-aEvidencedLens-21-2-acceptance-ledger.md`

Both `.js` renders are written by `bash tools/workflows/check-protocol-parity.test.sh --render`, in
the commit that edits their templates, and never by hand. This spec's status header and generated
regions, and the README's generated regions, are rewritten by `gen_build_index.py --write`.
`memory/LIVE.md` and the month's ledger shard are declared at dispatch if and only if the derived
build status with this unit CLOSED differs from the rendered one, as unit 20's S3 derived it.

### Alternatives rejected

- **The skeptic's corrected M2 fix: return `perItem` from the review and floor on items.**
  `check-unattended.sh:739-747` owes one unit per blocker and high from the row's raw `highs`, and
  the driver's `owe` is the same sum. A disposal the harness accepted at the item floor would red
  check 2 at the close, so the defect would move from the harness to the bar. Writing the item count
  into `--highs` instead changes what that flag means in the driver, both carriers and check 2, and
  leaves two raw BLOCKER ids in one item broken, since blockers drive convergence and stay raw.
- **The finder's M2 fix, items everywhere.** Rejected by the skeptic: `confirmedMinors` is raw minus
  raw by `TOOL-dMergedTally-1`, and one basis on both sides is that ruling.
- **Evaluating the committed conf to read the effective bound (finding 1's first option).** It runs
  the commits the clause distrusts inside the bar. Rejected by the skeptic.
- **A WARNING instead of a refusal for a relative `repo`.** A warning beside an accepted scratch
  still lets a lens write the tree; the refusal costs a caller one absolute path.

## 5. Production-readiness checklist

- security — S1 narrows accepted input on the one argument a probing lens writes under, and
  closes two evasions of the read-only rule's guard. S5 narrows where each lens writes. Nothing
  widens.
- perf / scale — a few regex replacements per invocation, one awk counter per conf blob, and one
  exit status per matrix verb.
- error / empty / loading states — every new refusal names its argument and value. A conf with no
  assignment still falls to the driver's default before the zero strip, so `00` prints `0` and an
  empty value prints the default.
- observability — the skip reports name both arms; the multi-assignment bound prints every value it
  saw, in order, in the fail line.
- risks — the multi-assignment rule is fail-closed and can red a run commit that merely repeats one
  value. No history commit carries two assignment lines, so it reds nothing landed. The S3 exemption
  list is measured, not known, so the pass may find more refusing verbs than expected; each takes a
  reason.
- testing — each new arm is observed red once on a staged break before it lands: AC1, AC2, AC4, AC7
  and AC9 name the break.
- migration — none: no record is rewritten, and an archived run's single-assignment conf reads as
  before.
- user docs — the args doc in `tier2-review.js`'s header and the NOT-CHECKED header are the docs.

## 6. Acceptance criteria

Every stub run below copies a suite's own runner shape into a scratch script under the session
scratch directory and runs it there, never the suite: `armScratch`'s prelude extraction and
`runReview` with `buildStubs` from the tier2-review suite, and `run_wf` from the unattended-build
suite. A staged break is a scratch copy of the render with one named edit, never an edit to the tree.

- **AC1** — When `u21-m1.js` evaluates the prelude of `tools/workflows/tier2-review.js` on the spec
  kind, each of `repo "."` beside an absolute scratch, `C:/p/x` beside `/c/p/x/t`, `/c/p/x` beside
  `C:/p/x/t`, and `/tmp/r` beside `/tmp/q/../r/x` throws a message starting `tier2-review:` and
  naming `repo` or `scratch`. `C:/t/s` beside `C:/p/x` and `/tmp/rs` beside `/tmp/r` proceed, and a
  diff-kind call with `repo "."` proceeds. The same four over the base render proceed.
  Red when: any of the four proceeds, or either control or the diff-kind call is refused.
- **AC2** — When `run_wf` runs `tools/workflows/unattended-build.js` with each of AC1's four
  (`repo`, `scratch`) pairs, each prints `THROW unattended-build:` naming `repo` or `scratch`, and
  the `/tmp/r` beside `/tmp/s` control reaches `agent:spec:`.
  Red when: a pair reaches a stage, or the two scripts answer one pair differently.
- **AC3** — When `run_wf` runs the unattended-build render with `review_out 0 2 2` and `rec
  CONVERGED`, the `prompt:dispose:` line contains `even where the report merged several ids into
  one item`. A dispose double promoting both into ONE unit is refused with `below the floor of 2`
  and `one unit per RAW blocker and high id, merged items included`, and the RESULT carries
  `"roster":[]`. Two units log `disposal: done`, and the record line carries `--highs 2 --minors 0`.
  Red when: the prompt still lets one unit stand for two raw HIGH ids, or a count changed basis.
- **AC4** — When the hostile-value matrix block is run as a slice, prologue plus that block in a
  scratch copy named `u21-matrix.sh` inside the unattended kit directory and deleted after, it
  prints no `FAIL` line and the run-state file after the one-line form carries
  `review · item yes\nphase: LANDED · reason verdict CLEAN · blockers 0 · CONVERGED · highs 0 · minors 0`.
  With `--highs 0 --minors 0` taken back out of the `review)` helper line, the slice prints a `FAIL`
  naming `--review`. With `--bogus` appended to the `rescope)` line it prints a `FAIL` naming
  `--rescope`, and with a verb that accepts the form added to the exemption list it prints a
  `FAIL` naming that verb. The ledger records the exemption list as measured.
  Red when: a verb whose every hostile form is refused passes the matrix, or a stale exemption does.
  cost: the slice builds several run fixtures, about a minute on node `a`.
- **AC5** — When `2026-10-05-build-TOOL-aEvidencedLens-21-1-ab-replay.md` under the build's `build/`
  folder is read, it carries `**Serves:** journal TOOL-aEvidencedLens-21`, a forward
  `replay: recall` line and a reverse one each with its `per-lens:` and `per-lens known:` lines, the
  two per-lens tables, the old-versus-new table, the section-level ceiling sentence, and a liveness
  row for replay ids 3, 12, 14, 23, 24, 25, 26, 28, 37 and 38 and for the two section-matched HIGH
  items, each naming its probe. No file under `reviews/` names the replay report.
  Red when: an id has no row, a row has no probe, or a recall line was typed rather than pasted
  from a run.
  figure: both recall lines are DERIVED by re-running `review_replay.py` both ways against the
  report in the session scratch; §4's figures are PINNED from the main loop's run on 2026-10-05.
  fixture: needs the replay report at the session scratch path; a lost scratch means the record
  pastes the main loop's saved forward output and says the reverse could not be re-derived.
- **AC6** — When `runReview` stubs a spec-audit run of the render, every `find:` and every `verify:`
  prompt carries `named for your own role, <lens key> for a finder or verify-<batch> for a skeptic`,
  the two PROBE POLICY slices are byte-identical, and no diff-kind prompt carries it. The base
  render's prompts carry none of it.
  Red when: a probing prompt lacks the rule, or the rule interpolates a value and splits the slices.
- **AC7** — When `read_rounds_of`, extracted by `sed -n '/^read_rounds_of() {/,/^}/p'` from
  `tools/unattended/check-unattended.sh` into a scratch file and sourced with `DRIVER` naming
  `tools/unattended/unattended.sh`, reads `REVIEW_ROUNDS=01` it
  prints `rounds=1`, reads `REVIEW_ROUNDS=00` it prints `rounds=0`, reads the decoy blob (`4`, then
  `1` inside `if false`) it prints `rounds=multi:4,1`, and reads an empty blob it prints the
  driver's default. Over the base file the first prints `rounds=01` and the decoy `rounds=1`.
  Red when: the zero-pad still reads as a change, the decoy reads as one bound, or `00` reads as
  absent.
- **AC8** — When `grep -c 'SKIPPED the grant-write arm for' tools/unattended/check-unattended.sh`
  runs it prints 0, and `grep -c 'SKIPPED the grant-write and round-bound arms for'` prints 2. The
  local-ref report and the empty-range note each contain `round-bound`, and
  `grep -c 'inside a dead block, a function body or a heredoc'` prints 1. Over the base file the
  first prints 2.
  Red when: a skip report names one arm while skipping two.
- **AC9** — When `runReview` stubs the render with a probe `blobs` row of `abc1234` and 33 zeros for
  `m.md`, no log line contains `m.md MOVED`, every `find:` prompt carries `  - m.md  blob abc1234`
  followed by a newline, and with `m.md` the only subject the synth prompt carries
  `no checked subject moved`. Over a scratch copy whose `now.indexOf(String(x.blob)) !== 0` reads
  `true`, all three red. `grep -c 'no checked subject moved' tools/workflows/tier2-review.test.sh`
  prints at least 1; over the base file it prints 0.
  Red when: an unchanged subject is reported MOVED, or the suite carries no arm for it.
- **AC10** — When `sed -n '/^## Parked decisions/,/^<!-- roster:units -->/p'` reads
  `memory/builds/aEvidencedLens/README.md`, it does not contain `None yet.` and does contain
  `2026-10-04T23:32:23Z`, `2026-10-05T03:59:40Z` and `generation bound`. Its body is at most 1800
  bytes by `wc -c`.
  Red when: the slot still says nothing is open, or it exceeds its ceiling.
- **AC11** — When `2026-10-05-build-TOOL-aEvidencedLens-21-2-acceptance-ledger.md` under the build's
  `build/` folder is read, it carries `**Serves:** journal TOOL-aEvidencedLens-21` and an
  `**Evidences:** TOOL-aEvidencedLens-21` block with one line per criterion AC1 to AC10.
  Red when: an observation lives only in the transcript, or a criterion has no line.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `unattended kit gate` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · `armScratch` rows for a relative `repo`, both MSYS spellings and a `..` segment, each observed proceeding on the base render · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/tier2-review.test.sh · an unmoved subject whose `now` begins with the pin, red on an always-MOVED render copy · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/tier2-review.test.sh · the per-role scratch rule in every `find:` and `verify:` prompt, absent from the base render · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/unattended-build.test.sh · the prelude refusing AC1's four pairs, and two raw HIGH ids in one item over the dispose prompt and floor · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/unattended/unattended.test.sh · the `--review` liveness row and the per-verb one-line exit status, red with the counts removed · the floor of the shard holding the matrix, raised by the assertions added
New arm: tools/unattended/check-unattended.test.sh · a run commit writing the decoy conf names a round write, `1` to `01` names none, and the four reports name both arms · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, the minors batch promoted from the closing diff review's round
  1 (`reviews/2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md`), items M1 to M4
  and L1 to L3, ids 2, 5, 7 and 10 (MEDIUM) and 1, 4, 6, 8 and 11 (LOW), with the replay comparison
  M4's record asks for and the two replay-only defects it found live.

## 10. Reuse audit

Every change extends a seam this build already touched: the spec-kind prelude of
`tools/workflows/tier2-review.template.js` and its copy in `unattended-build.template.js`, the
DISPOSAL prompt and floor, `PROBE_RULES`, check 19's round-bound functions, and the hostile-value
matrix. The replay record reuses `tools/workflows/review_replay.py` as built by unit 10, both ways,
and builds no scorer. `python tools/codebase-map/reuse_lookup.py "refuse a scratch path equal to or
under the repository path"` returned name-stem neighbours only (`CensusRefused`, `attribute_paths`,
`deriveSidecarPath`) and printed `unscanned layers: .sh`, so no existing seam fits a path-containment
fold beyond the two copies S1 amends; a shared helper is a §3 non-goal. The recall probe's top hits
were `TOOL-aBatchedMinors-6`, the precedent this spec follows, `TOOL-aEvidencedLens-8`, whose floor
S2 aligns, `TOOL-aBatchedMinors-5`, the ruling that promotes every closing-review finding, and
this unit's own `RUN.md` rescope row.

Recall terms used: `python tools/memory-recall/query.py "how should the closing diff review's medium and low findings be batched and what binds the scratch refusal, the unit floor and the round bound read" --terms "closing diff review batched minors promote scratch refusal unit floor perItem REVIEW_ROUNDS hostile matrix replay"`
