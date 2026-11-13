# TOOL-aCarriedStop-3 — the closing review's mediums and lows, batched: the count test on the audit route only, the owner-stop arms the suite lacks, the base driver's reading and the usage header's padding

**Status:** CLOSED · rev-1 · 2026-11-13 · node a · Tier-2 · base cfda7001 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-build-TOOL-aCarriedStop-1-agent-ledger.md](../build/2026-11-13-build-TOOL-aCarriedStop-1-agent-ledger.md) | journal | TOOL-aCarriedStop-1 TOOL-aCarriedStop-2 |
| [2026-11-13-build-TOOL-aCarriedStop-2-promotions.md](../build/2026-11-13-build-TOOL-aCarriedStop-2-promotions.md) | research | TOOL-aCarriedStop-2 |
| [2026-11-13-build-TOOL-aCarriedStop-3-1-acceptance-ledger.md](../build/2026-11-13-build-TOOL-aCarriedStop-3-1-acceptance-ledger.md) | journal | — |
| [2026-11-13-prompt-TOOL-aCarriedStop-3-1-builder.md](../prompts/2026-11-13-prompt-TOOL-aCarriedStop-3-1-builder.md) | journal | — |
| [2026-11-13-prompt-TOOL-aCarriedStop-3-build-brief.md](../prompts/2026-11-13-prompt-TOOL-aCarriedStop-3-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review of unit 1 confirmed one behavioural defect below HIGH and seven gaps beside it.
Every successful `--record-round --owner-stop` call prints two shell errors, and passes a count
test on an error status. Four stated behaviours of the owner-stop row have no suite arm, one
observation is on no record, and one usage line lost its alignment. This unit closes them in one
batch, as the build method's rule for a diff review's mediums and lows asks.

The review is
`memory/builds/aCarriedStop/reviews/2026-11-13-review-TOOL-aCarriedStop-1-diff-review-round1.md`.
Its items M1, M2, M3, L1, L2, L3 and L4 hold finding ids 4, 12, 6, 7, 8, 9, 10 and 15.

## 2. Scope (IN)

- **S1** — Ids 4 and 12. In `write_chain_round`, the test that compares the disposed BLOCKER and
  HIGH ids with `--blockers` and `--highs` runs on the audit route only. An owner-stop call prints
  no shell error, and an audit round short of its counts is refused as today. Observed by AC1.
- **S2** — Id 6. The suite arms the mixed-flag refusal for `--audited`, `--blockers`, `--highs`
  and `--sibling`, the four tokens it does not pass today. Observed by AC2.
- **S3** — Id 7. The suite arms the reader's owner-stop branch with a row it must refuse, once
  for the path's class and once for the field count, each on its own record state. Observed by
  AC3.
- **S4** — Id 8. The suite arms two stated behaviours after a stop: the stop's round counts
  toward the ceiling, and the round after a stop carries no fold of the round before it. Each
  takes the review's corrected fix and a control without the stop. Observed by AC4.
- **S5** — Id 9. The suite arms the roster fallback that names a new record when no spec is
  tracked, on a fixture of its own, and the empty `--owner-stop` value. Observed by AC5.
- **S6** — Id 10. The failing case that the suite's `TOOL-aCarriedStop-1` header names is observed
  against the driver of `d646814e`, and this unit's acceptance ledger holds that reading. Observed
  by AC6.
- **S7** — Id 15. The `--chain-verdict` usage line of the driver's header takes back its two
  spaces, so its comment aligns with its neighbours, and no usage fingerprint moves. Observed by
  AC7.
- **S8** — The driver gains no refusal site, no check number and no second copy of the append
  tail. Observed by AC8.
- **S9** — The five arms of §7 land in the suite. NOT OBSERVED by a criterion of this spec: a
  suite is no acceptance observation, so the main loop observes each arm red and then green at the
  close.

## 3. Non-goals (OUT)

- No change to what any call answers on stdout or to any exit status. S1 moves stderr alone.
- No rewording of the suite header that id 10 cites. Its phrase, "observed at the close and not by
  the pass that wrote this", opens eight block headers of the suite (PINNED, 2026-11-13, by
  `grep -c`), seven of them from earlier builds. It names where the observation is made. What id
  10 confirmed is that no record held the reading, and S6 supplies one.
- No table-driven arm for the mixed-flag tokens. The six tokens sit inline in one `for`, and
  hoisting them into a variable for a test to read is a refactor no finding asked for.
- No arm for the usage header's padding. AC7 observes it, and the line is a comment.
- No change to `tools/unattended/check-unattended.sh`, to a document, or to the Skill. No
  user-facing text moves.
- No repair of the census arm, which reads red at the base. It is unit 1's stated inheritance.
- No edit of unit 1's spec or ledger. Both belong to a CLOSED unit.

### Edges

- **consumes-from** `TOOL-aCarriedStop-2` — the driver and the suite as that unit leaves them.
  Both units write `tools/unattended/unattended.sh` and its suite, so this one builds second. S3's
  class arm reds on the `pathre` variable unit 2 gives the reader, and the suite's `_cs_folder`
  holds unit 2's text.
- **consumes-from** external — unit 1's writer, reader and suite block, built at `a5594293`.
- **hands-off** external — the suite's own red and green readings of unit 1's arm
  block and of this unit's arms, which the main loop takes at the close and writes beside AC6's
  line. A pass may run no suite.
- **hands-off** external — the suite arm `FA9 AC15 the driver's census holds`, red before and
  after this unit.

## 4. Design

### Evidence

Read at `cfda7001`. Line citations are blob-pinned to that commit. Every "probed" below is a run
of the probe fixture on 2026-11-13.

| Id | Claim | Where |
|---|---|---|
| 4, 12 | The count test has no route guard | `tools/unattended/unattended.sh@cfda7001:13768` |
| 4, 12 | On the owner-stop route both operands are empty | the mixed-flag refusal, `tools/unattended/unattended.sh@cfda7001:13713` to `:13716` |
| 4, 12 | A successful call prints two `[: : integer expected` lines | probed: stderr held eight `unattended: NOTE - ` lines and those two |
| 4, 12 | The suite's caller drops stderr | `tools/unattended/unattended.test.sh@cfda7001:2811` |
| 6 | The suite passes `--subject` and `--finding` beside the flag, and no other token | `tools/unattended/unattended.test.sh@cfda7001:3379` and `:3386` |
| 7 | The reader's branch tests three fields and the path's class | `tools/unattended/unattended.sh@cfda7001:13858` |
| 8 | The step-0 comment states the ceiling count and the empty carry | `tools/unattended/unattended.sh@cfda7001:13802` to `:13807` |
| 8 | The shipped ceiling is 4 | `tools/unattended/unattended.sh@cfda7001:1173` |
| 9 | A new record is named from the specs, then from the roster | `tools/unattended/unattended.sh@cfda7001:13742` |
| 9 | The no-id arm removes the specs and the roster in one step | `tools/unattended/unattended.test.sh@cfda7001:3389` |
| 10 | The header's claim | `tools/unattended/unattended.test.sh@cfda7001:3343` |
| 15 | The `--chain-verdict` line's comment opens at column 65, its neighbours' at 67 | `tools/unattended/unattended.sh@cfda7001:32` to `:34`, by the `awk` of AC7 |

### S1 — the count test's route

The test at `tools/unattended/unattended.sh@cfda7001:13768` takes a route guard in place:

```bash
if [ -z "$path" ] && { [ "${#b_ids[@]}" -lt "$blockers" ] || [ "${#h_ids[@]}" -lt "$highs" ]; }; then
```

The body, its `check_chain_fault` value and the `return 1` do not move. The guard is the route
test the function already uses at `:13705`, so the owner-stop route skips the comparison on a
branch and no longer on an error status.

Defaulting the operands with `${blockers:-0}` is the review's other sound form. It is not taken:
it keeps the audit route's test running on a route that has no counts, and hides which route a
reader is on.

Applied to a scratch copy of the driver, the owner-stop call left no stderr line outside the
`NOTE` lines, and an audit round with `--highs 1` and no finding row was still refused.

### The review's stderr assertion is corrected

The review's fix for ids 4 and 12 asks an arm to assert that the call's stderr is empty. It is
never empty in the suite's fixture: the driver prints one `unattended: NOTE - ` line for each key
the fixture's conf does not declare, eight of them in the probe. The arm and AC1 therefore count
the stderr lines that do not open with `unattended: NOTE - `, and require none. That holds the
class, any shell error on a successful call, and not the one message.

### S2 to S5 — the arms

Each arm is specified by what it runs and what it asserts. All live in the suite's
`TOOL-aCarriedStop-1` block and use its helpers: `write_stop_fixture`, `write_stop_row`,
`write_fixture_round`, `run_chain`, `read_chain_file` and `check_chain_refused`. The suite's
fixture holds seven units whose specs stand at rev-3 with rev-2 logged, so a `--sibling` row at
rev-2 joins there as it does in the probe fixture. That join was probed in the probe fixture and
is UNVERIFIED in the suite's, which no pass may run.

| Arm | Runs | Asserts |
|---|---|---|
| S1, ids 4 and 12 | on a fresh stop fixture, the owner-stop call made as `run_chain` makes it, with stderr sent to a file under the suite's temp folder | exit 0, and no stderr line outside the `NOTE` lines |
| S2, id 6 | four `check_chain_refused` calls beside the `--subject` one at `:3379`, each passing `--owner-stop "$_cs_stop"` and one of `--audited FIX-dFix-1`, `--blockers 0`, `--highs 0` and `--sibling FIX-dFix-1@rev-2` | `$_cs_alone: <flag>` for that flag, and the record's bytes as they stood |
| S3, id 7 | on a fresh stop fixture with the row committed, a malformed row appended to the record, the verdict read, and the record restored from the index; then the same for the second row | each verdict exits 1 and prints the body-row fault naming the row whole |
| S4, id 8, ceiling | on a fresh stop fixture, the three rounds of "The rounds" below with the stop between the second and the third | `round 4 · HOLD · reason ceiling`; and on a second fresh fixture with no stop, `round 3 · CONTINUE · reason open` |
| S4, id 8, carry | on a fresh stop fixture, the three fold rounds below with the stop between the second and the third | `round 4 · STOP · reason clean`; and on a fresh fixture with no stop, `round 3 · CONTINUE · reason unreviewed · audit FIX-dFix-2` |
| S5, id 9 | on a fresh stop fixture of its own, placed after the assertion `CS1 AC4 no refusal left a record`: the spec folder removed with `git rm` and the README left whole, then the owner-stop call; and one call with `--owner-stop ""` | exit 0 and a record whose name ends `-build-FIX-dFix-1-chain-rounds.md`; then exit 1 and check 112 naming `--subject` |

Why each has the shape it has:

- **S3 restores between rows.** The awk exits at the first row outside the grammar, so two bad
  rows in one record exercise the first only. That is the skeptic's condition on id 7.
- **S4's ceiling arm holds three audit rounds, not four.** Round 4 is then at the ceiling only if
  the stop's round is counted. The finder's four-audit form reaches HOLD either way, which is why
  the skeptic rejected it.
- **S4's carry arm folds a unit an earlier round audited.** A promoted unit would be unreviewed by
  the first clause whichever way the reader looks, so only a fold tells the two readers apart.
- **S4's controls are in the arm.** Each control is the same record less the stop, and it answers
  differently, which shows the arm's fixture reaches the behaviour.
- **S5 owns a fixture.** A successful call inside the existing no-id arm leaves a record, so the
  no-id call after it would skip the naming block and two existing assertions would fail. Placed
  after them on a fresh fixture, it changes no existing assertion's start state.
- **S5's empty value is a direct call.** `check_chain_refused` asserts check 118, and an empty
  value takes the audit route's check 112.

### The rounds

`<all>` is the seven ids, `FIX-dFix-1` to `FIX-dFix-7`, separated by one space. Each line is the
tail of `run --record-round dFix`.

| Name | Flags |
|---|---|
| `<c1>` | `--subject s1 --audited "FIX-dFix-1 FIX-dFix-2 FIX-dFix-3" --blockers 0 --highs 1 --finding 1/HIGH/new-mechanism/FIX-dFix-1/FIX-dFix-4/1` |
| `<c2>` | `--subject s2 --audited FIX-dFix-4 --blockers 0 --highs 1 --finding 2/HIGH/new-mechanism/FIX-dFix-1/FIX-dFix-5/1` |
| `<c3>` | `--subject s3 --audited "FIX-dFix-5 FIX-dFix-6 FIX-dFix-7" --blockers 0 --highs 1 --finding 3/HIGH/new-mechanism/FIX-dFix-1/FIX-dFix-6/1` |
| `<f1>` | `--subject s1 --audited "<all>" --blockers 0 --highs 0` |
| `<f2>` | `--subject s2 --audited FIX-dFix-1 --blockers 0 --highs 0 --sibling FIX-dFix-2@rev-2` |
| `<f3>` | `--subject s3 --audited FIX-dFix-1 --blockers 0 --highs 0` |
| `<s>` | `--owner-stop <stop>` |

Probed against the driver at `cfda7001`: `<c1>`, `<c2>`, `<s>` and `<c3>` read
`round 4 · HOLD · reason ceiling`, and the same less `<s>` read
`round 3 · CONTINUE · reason open · audit FIX-dFix-6`. `<f1>`, `<f2>`, `<s>` and `<f3>` read
`round 4 · STOP · reason clean`, and the same less `<s>` read
`round 3 · CONTINUE · reason unreviewed · audit FIX-dFix-2`.

### S6 — the base driver's reading

The header says the driver from before unit 1 reds every arm of its block, because `--owner-stop`
is an unknown argument there. The builder observes that directly: the probe fixture, with the
driver and its library taken from `d646814e` by `git show`, answers the owner-stop call with check
14 and leaves no record. The same call with the worktree's driver records the row. Both readings
go on AC6's line of this unit's acceptance ledger, which is the record id 10 found missing.

```bash
git -C "$W" show d646814e:tools/unattended/unattended.sh > u/unattended.sh
git -C "$W" show d646814e:tools/unattended/lib-unattended.sh > u/lib-unattended.sh
```

`$W` is the worktree, and both run from `<fx>` after the fixture is built.

The review's fix runs the suite's shard against both drivers. A pass may not run a suite, so that
reading stays the main loop's (§3, Edges), and this one is the same failing case seen through the
verb.

### S7 — the usage line

`tools/unattended/unattended.sh@cfda7001:33` gains two spaces before its `#`, so the comment opens
at column 67 as the `--owner-stop` line above it and the `--check-commit` line below it do. The
fingerprint of `verb:unattended.sh:--chain-verdict` is `5fdc7c80` at `cfda7001` (PINNED,
2026-11-13, by `python tools/govkit/docs_leg.py --fingerprints`) and reads the verb's shape, so it
does not move.

### The probe fixture

The criteria run the driver in a scratch repository. The builder saves this as `stopfix.sh` in its
scratch directory and runs it as `bash stopfix.sh <worktree> <fx>`. It is unit 2's fixture, byte
for byte.

```bash
set -eu
W=$1; F=$2; R=${3:-memory}; B=$R/builds/dFix; D="2026-11-02T12:00:00 +0000"
rm -rf "$F"; mkdir -p "$F/u" "$F/$B/spec" "$F/$B/prompts"
cp "$W/tools/unattended/unattended.sh" "$W/tools/unattended/lib-unattended.sh" "$F/u/"
printf 'MEMORY_ROOT=%s\nDISPOSITION_CUTOFF="2000-01-01"\nREVIEW_ROUNDS="1"\nSPEC_FOLD_CUTOFF="2026-11-01"\n' "$R" > "$F/.unattended.conf"
{ printf '# dFix\n\n<!-- roster:units -->\n'; for i in 1 2 3 4 5 6 7; do printf 'FIX-dFix-%s\n' "$i"; done; printf '<!-- /roster:units -->\n'; } > "$F/$B/README.md"
for i in 1 2 3 4 5 6 7; do
  printf '# FIX-dFix-%s — u\n\n**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base 0123abcd\n\n## 2. Scope (IN)\n\n- s\n\n## 6. Acceptance criteria\n\n- AC1 observable.\n\n## 7. Gates\n\n- g\n\n## 8. Open questions\n\nnone\n\n## 9. Revision log\n\n- rev-1 · 2026-11-01 · u.\n- rev-2 · 2026-11-01 · a fold.\n' "$i" > "$F/$B/spec/2026-11-01-spec-FIX-dFix-$i.md"
done
printf '# the owner ends the audit chain\n' > "$F/$B/prompts/2026-10-24-prompt-FIX-dFix-1-owner-review-stop.md"
cd "$F"; git init -q -b main .; git config user.email t@t.test; git config user.name t; git config core.autocrlf false
git add -A >/dev/null; GIT_COMMITTER_DATE="$D" git commit -q -m conf --no-verify
printf '# dFix\n\n## Run facts\nphase: BUILDING\nwitness: abc\nspec-audit: 2026-11-01\nbase: %s\n\n## Parked\n\n' "$(git rev-parse HEAD)" > "$B/RUN.md"
git add -A >/dev/null; GIT_COMMITTER_DATE="$D" git commit -q -m record --no-verify
```

In §6, each criterion starts from a fresh fixture unless it says otherwise, and these names stand:

- `run` is `env -u GOV_REMOTE -u GOV_DEFAULT_BRANCH bash u/unattended.sh "$@" 2>/dev/null`, called
  from `<fx>`.
- `runerr` is `run` with `2>err` where `run` has `2>/dev/null`, so the call's stderr is the file
  `err` in `<fx>`.
- `<b>` is the fixture's build folder under the root `memory`, and `<p>` is `<b>/prompts`.
- `<stop>` is `<p>/2026-10-24-prompt-FIX-dFix-1-owner-review-stop.md`.
- `<rec>` is the one path `git ls-files '*-chain-rounds.md'` prints.
- "commit" is `git add -A && GIT_COMMITTER_DATE="2026-11-02T12:00:00 +0000" git commit -q -m c --no-verify`.
- `<118>` is `UNATTENDED check 118 FAILED — the spec-audit chain record refuses this: `.
- `<alone>` is
  `--owner-stop records the owner's ruling alone, and a round's flag beside it would mix a ruling with an audit: `.
- `<bad>` is
  `a body row is outside the grammar, and the record is append-only, so it was edited by hand: `.
- The rounds `<c1>` to `<c3>`, `<f1>` to `<f3>` and `<s>` are the table's above.

### What it does not check

- Stderr on any route but the owner-stop's successful one. A refusal's stderr and an audit round's
  are not asserted.
- The mixed-flag refusal with two or more flags given at once, beyond what unit 1's arms pass.
- A malformed owner-stop row of any other shape: a missing `record` word, an empty path, or a
  round number that is no positive integer. The two arms hold the branch's two conditions.
- The ceiling at any value but the shipped 4, and the carry for a promotion. The arm folds.
- The roster fallback on a README whose roster pair is malformed, which is another refusal.
- That the suite's block reds against the base driver arm by arm. AC6 observes the verb once, and
  the suite's reading is the main loop's.
- The alignment of any usage line but the three AC7 names.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Assert an empty stderr.** The review's wording, and red on every run for the reason above.
- **Default the count test's operands.** Sound, and it leaves the test on the wrong route.
- **Reword the suite header for id 10.** It would change one of eight like headers and add no
  reading to any record.
- **One arm appending both malformed rows.** The reader stops at the first.
- **The finder's fixes for ids 8 and 9.** Each was judged unsound by its skeptic, for the reasons
  "Why each has the shape it has" repeats.

## 5. Production-readiness checklist

- security — N/A — no input, write path or grammar moves. S1 narrows where one comparison runs,
  and the audit route's count refusal is held by AC1.
- perf / scale — One string test more on each `--record-round` call.
- error / empty / loading states — The empty `--owner-stop` value and the spec-less roster are
  now armed. Neither answer moves.
- observability — A successful owner-stop call stops printing two shell errors, so a caller that
  shows stderr sees the notes alone.
- risks — Unit 2 lands first in the same two files, so this unit's line citations are to
  `cfda7001` and the builder re-reads each site. The census arm is red at the base.
- testing — AC1 to AC6 are driver runs in the probe fixture, and AC7 and AC8 read the driver. The
  arms add about 35 driver launches and nine fixtures. At the roughly 1.2 s a launch that unit 1's
  spec pins, which this spec did not re-measure, that is under a minute of suite wall.
- migration — None.
- user docs — N/A — no verb, flag, refusal text or printed line moves.

## 6. Acceptance criteria

The names of §4, "The probe fixture" and "The rounds", stand.

- **AC1** — When `runerr --record-round dFix <s>` runs in a fresh fixture, it exits 0 and
  `grep -vc '^unattended: NOTE - ' err` prints 0. Then
  `run --record-round dFix --subject s9 --audited FIX-dFix-1 --blockers 0 --highs 1` exits 1 and
  prints `<118>` followed by
  `the rows dispose 0 BLOCKER and 0 HIGH id(s) where the review counted 0 and 1`.
  Red when: the count test runs on the owner-stop route, which at `cfda7001` prints 2 for the two
  `integer expected` lines; or the guard also skips the audit route.
- **AC2** — When `run --record-round dFix --owner-stop <stop>` runs in a fresh fixture with each
  of `--audited FIX-dFix-1`, `--blockers 0`, `--highs 0` and `--sibling FIX-dFix-1@rev-2` after
  it, one per call, each exits 1 and prints `<118>`, then `<alone>`, then that flag's name. Then
  `git ls-files '*-chain-rounds.md'` prints nothing.
  Red when: a token left the writer's loop, so its flag is taken beside the ruling, and for
  `--sibling` a fold row is appended to the stop's round.
- **AC3** — When `run --record-round dFix <s>` and a commit run in a fresh fixture, and
  `printf 'round 2 · owner-stop · record <p>/a b.md\n' >> <rec>` runs, `run --chain-verdict dFix`
  exits 1 and prints `<118>`, `<bad>` and that row. And when `git checkout -- <rec>` and then
  `printf 'round 2 · owner-stop · record <stop> · extra\n' >> <rec>` run, it exits 1 and prints
  `<118>`, `<bad>` and that row.
  Red when: the reader's class admits a space, its pattern lost an anchor, or its field count
  reads "at least three".
- **AC4** — When `run --record-round dFix` runs with `<c1>`, `<c2>`, `<s>` and `<c3>` in that
  order in a fresh fixture, `run --chain-verdict dFix` prints a first line of
  `unattended: chain dFix · round 4 · HOLD · reason ceiling`; and with `<c1>`, `<c2>` and `<c3>`
  in another, it prints `unattended: chain dFix · round 3 · CONTINUE · reason open · audit FIX-dFix-6`.
  When it runs with `<f1>`, `<f2>`, `<s>` and `<f3>` in a third, the verdict prints
  `unattended: chain dFix · round 4 · STOP · reason clean`; and with `<f1>`, `<f2>` and `<f3>` in
  a fourth, it prints `unattended: chain dFix · round 3 · CONTINUE · reason unreviewed · audit FIX-dFix-2`.
  Red when: the stop's round is left out of the ceiling count, so the first reads CONTINUE; or the
  reader looks behind the stop for a fold, so the third names `FIX-dFix-2` as unreviewed.
  figure: the ceiling of 4 is PINNED, 2026-11-13, from `SPEC_AUDIT_CHAIN_CEILING_DEFAULT`.
- **AC5** — When `git rm -q -r <b>/spec` and then `run --record-round dFix <s>` run in a fresh
  fixture, the second exits 0 and `git ls-files '*-chain-rounds.md'` prints one path whose name
  ends `-build-FIX-dFix-1-chain-rounds.md`. And when `run --record-round dFix --owner-stop ""`
  runs in another, it exits 1, prints a line opening
  `UNATTENDED check 112 FAILED — --record-round requires --subject`, and the same listing prints
  nothing.
  Red when: the roster fallback is gone, so a build with a roster and no tracked spec is refused
  as yielding no id; or an empty value is read as a path.
- **AC6** — When, in a fresh fixture, the two `git show` commands of §4's S6 put the driver of
  `d646814e` in place, `run --record-round dFix <s>` exits 1, prints a line
  opening `UNATTENDED check 14 FAILED — unknown argument`, and
  `git ls-files '*-chain-rounds.md'` prints nothing. In another fresh fixture, with the worktree's
  driver, the same call exits 0. This criterion's ledger line states both readings.
  Red when: the base driver knows the flag, so the header's failing case is not one; or the ledger
  line carries one reading.
- **AC7** — When
  `awk '/^#   unattended[.]sh --(record-round <slug> --owner-stop|chain-verdict|check-commit) /{print index($0," # ")}' tools/unattended/unattended.sh | sort -u`
  runs it prints the one line `67`, and `python tools/govkit/docs_leg.py --fingerprints` prints a
  row for `verb:unattended.sh:--chain-verdict` carrying `5fdc7c80`, which
  `grep -c 'verb:unattended.sh:--chain-verdict 5fdc7c80 -->' help/spec-audit.md` finds once.
  Red when: the line keeps its comment at column 65, which at `cfda7001` prints `65` and `67`; or
  the edit reached the verb's shape and moved the anchor.
  figure: 67 and `5fdc7c80` are PINNED, 2026-11-13, from the driver at `cfda7001`.
- **AC8** — When `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh` runs it
  prints 319, `grep -c 'check_verb_flag --record-round' tools/unattended/unattended.sh` prints 4,
  and `grep -c 'chain round recorded' tools/unattended/unattended.sh` prints 1.
  Red when: a refusal took a new site, the route guard was built from a fifth required-flag call,
  or the owner-stop route was split off with its own append tail.
  figure: the three counts are PINNED, 2026-11-13, from the driver at `cfda7001`.

## 7. Gates

`unattended kit gate` · `docs` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `scratch-guard self-test` · `tier2-review self-test`

The first four grade this unit's change, and the last two are owed by a guard a path of the
estimate trips. The main loop runs the merge bar once, at the close, with the self-test tier that
holds the driver's suite. No leg is added.

The first arm is red against the driver as unit 2 leaves it. The other four hold behaviour that is
correct today, so each one's red is staged by the named edit to a scratch copy of the driver, and
its green is the driver as built.

New arm: tools/unattended/unattended.test.sh · covers AC1 · the driver as unit 2 leaves it, whose owner-stop call prints two `integer expected` lines · none
New arm: tools/unattended/unattended.test.sh · covers AC2 · the writer's loop with one of the four tokens deleted, once per token · none
New arm: tools/unattended/unattended.test.sh · covers AC3 · the reader's branch with `pathre` left unanchored for the first row, and with its field count read as at least three for the second · none
New arm: tools/unattended/unattended.test.sh · covers AC4 · the reader's last round taken over subject rows only for the ceiling, and its previous-round sets taken from the last round that is no stop for the carry · none
New arm: tools/unattended/unattended.test.sh · covers AC5 · the roster fallback deleted from the naming block for the first call, and the empty value read as a path for the second · none

What these arms do not check is §4's list. They add no floor, and the census arm's figure is not
theirs.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 10. Reuse audit

The seam is unit 1's own code and suite block: `write_chain_round` takes one route guard on a test
it has, and the suite's `TOOL-aCarriedStop-1` block takes five arms through the helpers it already
defines, `write_stop_fixture`, `write_stop_row`, `write_fixture_round`, `run_chain`,
`read_chain_file` and `check_chain_refused`. No helper is added. The probe,
`tools/codebase-map/reuse_lookup.py` run with the sentence "suite arm for a chain round refusal
and a verdict over a hand-edited record row", ranked name stems only and named no closer seam. For
the stderr arm, the suite's `run_switch_probe` is the precedent for sending a driver call's stderr
to a file under its temp folder.

Recall terms used: owner-stop record-round chain-verdict suite arm stderr ceiling carry-forward
roster fallback mixed-flag usage header
