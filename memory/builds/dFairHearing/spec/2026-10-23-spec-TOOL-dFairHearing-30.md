# TOOL-dFairHearing-30 — unit 15's with-and-without replay run with one fresh clone per record and arm, so no arm reviews a tree holding the other's report

**Status:** INPROGRESS · rev-6 · 2026-11-03 · node d · Tier-2 · base 3708a705 · streams tooling · order 23 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-30-deviation-301.md](../build/2026-10-23-build-TOOL-dFairHearing-30-deviation-301.md) | deviation | — |
| [2026-10-23-build-TOOL-dFairHearing-30-deviation-309.md](../build/2026-10-23-build-TOOL-dFairHearing-30-deviation-309.md) | deviation | — |
| [2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-departures-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-departures-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-3 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-32 |
| [2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md) | research | TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-31 TOOL-dFairHearing-32 |
| [2026-10-23-prompt-TOOL-dFairHearing-30-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-30-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFairHearing-30-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFairHearing-30-build-brief.md) | research | — |
| [2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief.md) | research | TOOL-dFairHearing-25 TOOL-dFairHearing-35 TOOL-dFairHearing-32 TOOL-dFairHearing-37 TOOL-dFairHearing-40 |
| [2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief.md) | research | TOOL-dFairHearing-25 TOOL-dFairHearing-35 |
| [2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief.md) | research | TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-31 TOOL-dFairHearing-35 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 |
| [2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md) | spec-audit | TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-31 TOOL-dFairHearing-32 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit's finding id 28 (item H2, HIGH,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`) is
closed. `TOOL-dFairHearing-25` runs unit 15's `selected` and `ungated` arms of each record in one
clone, and the harness writes each report under `${repo}/${reviewDir}`
(the `reviewDir` default and the report instruction, `tools/workflows/tier2-review.template.js:400`
and `:2121` at `9c1a2857a`). The first arm's report therefore sits in
the working tree the second arm reviews, and the recall comparison that decides spec 15 S6's product
state can be contaminated. This unit takes that replay from unit 25 and runs each record and arm in
its own freshly made clone, checked clean before its call, so no arm can read another arm's output.
The decision then follows from these runs. The per-arm step, the orchestrating commit, the attempt
rows and the evidence kept for unit 40 are written here, before the runs (unit 25 §8 F2).

## 2. Scope (IN)

- **S1** — One clone per record and arm. Unit 15's eight runs (spec 15 S5, its §4 corpus, arms
  `selected` and `ungated`) each take a fresh clone made by the replay section of
  `tools/workflows/README.md`, as unit 25 S8 leaves it, with S7's per-arm step, at that record's range
  head. A clone is named `f<r><a><n>`: `<r>` the record's position 1 to 4 in
  spec 15 §4's corpus, `<a>` `s` or `u` for the arm, `<n>` the attempt from 1. So the first attempts
  are eight distinct names, `f1s1` to `f4u1`. Observed by AC1.
- **S2** — Clean before the call. Immediately before each arm's harness call, `git -C "$TEMP/<clone>"
  status --porcelain --untracked-files=all`, read as its own call with its exit checked (S7), prints
  nothing, and the call names that clone as its `repo`. A non-empty status refuses the call, and the arm takes a new attempt in a new clone. The
  verdict record keeps each observed status beside its clone. Observed by AC1 and AC2.
- **S3** — No clone is reused. A re-run of a record and arm, for any cause, takes the next attempt
  number and a new clone, and the replay section's stale-directory refusal holds for every name. A
  clone stays on disk until unit 40's pass (S10). Observed by AC2.
- **S4** — Scoring and the decision, on unit 25's stated terms. The manifest declares the two arms one
  variable apart and `dispatched` 4 per arm, in unit 23 S4's terms, and
  `tools/workflows/replay_scorer.py --experiment` checks it. Pairing, the pooled figures and the
  decision are unit 25 S4's and S5's unit-15 half, read as written, and spec 15 S6 lands only when
  `ungated`'s pooled recall is above `selected`'s. Observed by AC3 and AC4.
- **S5** — One verdict record,
  `memory/builds/dFairHearing/build/<date>-build-TOOL-dFairHearing-30-replay-verdict.md`, opening
  `**Serves:** research TOOL-dFairHearing-30 TOOL-dFairHearing-15`. For each record and arm it names
  every attempt's clone, the clone's `HEAD`, the status S2 observed, its outcome and void cause (S9)
  and the report path, beside the orchestrating commit (S8). It names each record's recall under both
  arms, the pooled figures, the decision and the class set the `ungated` arm carried. Observed by AC1
  and AC3.
- **S6** — Supersession. Unit 25's S4, AC4, the unit-15 half of S5, AC6, and the unit-15 lines of S6
  and AC7 (the `ungated` class set) are answered by this unit's S1 to S5 and AC1 to AC4. Unit 25's
  acceptance ledger records them superseded here (`TOOL-dFairHearing-23` §8 F7's form). NOT OBSERVED by
  a criterion of this unit: it is a ledger entry in unit 25's record, read there.
- **S7** — The per-arm step, carried from `TOOL-dFairHearing-37` S8 (id 20 of the round-4 spec audit)
  and S12 (id 34), as `TOOL-dFairHearing-40` S12, S13 and S14 (ids 15, 38 and 22 of the round-5 audit)
  correct them. Before the first run, the replay section of `tools/workflows/README.md` gains the
  per-arm step of §4. It refuses, exit 2 naming the variable, when `SCRATCH` or `ORCH` is empty. It
  builds the clone's parent from `TEMP`, else `TMPDIR`, refusing when both are empty, and folds it to
  forward slashes with `cygpath -m` where `cygpath` exists. It reads the clone's status as its own
  call with its exit checked before the clean test. It reads the orchestrating commit as its own call,
  `git -C "$ORCH" rev-parse --verify HEAD`, its exit checked, and appends `orchestrating <sha> clone
  <path>` to `$SCRATCH/run.log` before the harness call. The README states that `TEMP` is the Windows
  name and `TMPDIR` the POSIX one. Observed by AC5.
- **S8** — The orchestrating commit, carried from `TOOL-dFairHearing-32` S14 (ids 5 and 13 of the
  round-3 spec audit), as unit 25 S7 states it for replay 1. The verdict record quotes the run log's
  `orchestrating` lines, which all name one sha, and names that sha as the orchestrating commit, on a
  line apart from each clone's `HEAD`. Beside it the record names the blob of
  `tools/workflows/README.md`, `tools/workflows/tier2-review.js` and `tools/workflows/replay_scorer.py`
  as the runs read them, each by `git hash-object`. The commit that adds the record has that sha as
  its first parent, each named blob equals that commit's blob at its path, and the sha descends from
  unit 23's build commit. Observed by AC6.
- **S9** — Attempts and the void rule, carried from `TOOL-dFairHearing-32` S20 (id 29) and S21 (id 30)
  for unit 15's replay as `TOOL-dFairHearing-37` S2 (id 2) words their unit-15 half, with the outcome
  of `TOOL-dFairHearing-40` S8 (id 35) and the void cell of its S9 (id 13). The record lists each
  attempt as a row: record, arm, attempt number, clone, outcome, and void cause or `-`. The outcome is
  `refused` (stopped before its call by S2's status, the stale refusal or the exact-commit check),
  `completed` (the call returned a report) or `failed` (the call was made and returned no usable
  report, as when it died or timed out). A void cause is spec 1 §4's, as unit 25 S3 reads it, and one
  citing an outside read quotes `<transcript file>:<line>` and the absolute path read. A void or
  failed attempt is re-run in the next attempt's clone. Which attempt is scored is unit 35 S1's rule,
  written before these runs: an attempt after the second completed one is never read, and a record
  and arm with no eligible attempt that is not void ends the replay with no decision (unit 35 S4).
  Observed by AC2.
- **S10** — The evidence kept, carried from `TOOL-dFairHearing-40` S9 (id 13), whose re-derivation of
  the void column reads it. Every clone, report and transcript the record names stays on disk until
  unit 40's pass; this pass removes none. This replaces S3's "until the verdict record cites it".
  Observed by AC7.

## 3. Non-goals (OUT)

- No replay 1. Its two design-audit runs each already take their own clone (unit 25 S1), so the shared
  tree this finding names does not arise there, and they stay unit 25's.
- No change to the recipe, the manifest grammar, the corpus, the arms or the decision rule. They are
  units 23, 14 and 15's, read here.
- No reading of the record after the runs. The same audit's minors on unit 25 that had to hold
  before the runs are carried: ids 5 and 13 by S8, id 21 by unit 25 S8 and this unit's S1, ids 29 and
  30 by S9 and unit 35, id 31 by unit 25 S8. Their post-run readings and ids 4 and 24 are
  `TOOL-dFairHearing-32`'s, after this unit.
- No product change of spec 15 S6: the decision and its files are unit 35's (AC4).
- No change to where the harness writes its report. A per-arm clone removes the shared tree without a
  product change, and the harness's `reviewDir` contract serves every other caller.
- No help page: `help/` covers neither the review harness nor the scorer factory.

### Edges

- **consumes-from** `TOOL-dFairHearing-25` — the replay section as its S8 and S9 leave it (the recipe with unit 27 S22's envelope, the placement step and the one trap), unit 15's run terms and the decision rule; this unit runs that replay in its place
- **consumes-from** `TOOL-dFairHearing-15` — the `resume:checklist` agent, the corpus, the two arms, the instrument and S6's product change
- **consumes-from** `TOOL-dFairHearing-14` — `check_experiment` and the manifest's `parsed` lines, which AC3 reads literally
- **hands-off** `TOOL-dFairHearing-32` — the minors that read this unit's verdict record after the runs: the behavioural `selected` check after unit 35's decision (id 4), the re-read of the orchestrating commit S8 records (ids 5, 13) and the re-read of the attempts S9 records (ids 29, 30)
- **hands-off** `TOOL-dFairHearing-35` — finding id 32 (item H2) of the round-4 spec audit: the attempt rule that decides which completed attempt is scored, and with it the scoring and the decision; this unit's S4, the figure and decision half of S5 and AC3, AC4's ungated half, spec 15 S6's product files and the selftest arm on the flag are superseded by its S1 to S6 and AC1 to AC4
- **hands-off** `TOOL-dFairHearing-37` — the same audit's minors on this spec that read its record or harden the harness after the runs, ids 1, 5, 12, 26 and 33: this unit's commit read beside unit 35's, the selected half observed by behaviour after the decision, the harness's `repo` fold for every caller, the leg line read, and each scored clone read (its S1, S4, S6, S11 and S18); ids 20 and 34 and id 33's restatement of AC1 are carried here as S7 and AC1
- **hands-off** `TOOL-dFairHearing-40` — the round-5 spec audit's minors that read this unit's verdict record, ids 9, 13, 24 and 29: the void column re-derived from each attempt's report and quoted transcript line, which S10 keeps on disk until that unit's pass, the record's `**Serves:**` line read for `TOOL-dFairHearing-35`, and the `ungated` class set re-derived (its S9, S24, S25 and S30); ids 15, 22 and 38, its corrections of the per-arm step, are carried here as S7


## 4. Design

### Why the replay moves here

Unit 25 runs at order 22 and this unit at 23. Correcting the isolation after unit 25 had run would
mean about 100 agents spent on a comparison the build had already found contaminable, then run
again, the shape unit 25 §8 F1 refused for the same reason. So unit 25 hands this replay over, as
units 1 and 15 handed their replays to unit 25. Replay 1 stays with unit 25.

### The run, per record and arm

```bash
test -n "$SCRATCH" || { echo "SCRATCH is empty"; exit 2; }
test -n "$ORCH" || { echo "ORCH is empty"; exit 2; }
t="${TEMP:-$TMPDIR}"
test -n "$t" || { echo "no temp directory: TEMP and TMPDIR are both empty"; exit 2; }
if command -v cygpath >/dev/null 2>&1; then t=$(cygpath -m "$t"); fi
c="$t/f<r><a><n>"
# the replay section's recipe over "$c" at the record's range head: stale refusal, exact-commit check
s=$(git -C "$c" status --porcelain --untracked-files=all) || { echo "status failed: $c"; exit 2; }
test -z "$s" || { echo "dirty: $c"; exit 2; }
o=$(git -C "$ORCH" rev-parse --verify HEAD) || { echo "orchestrating head unreadable: $ORCH"; exit 2; }
echo "orchestrating $o clone $c" >> "$SCRATCH/run.log"
# the harness call, `repo` set to "$c"; its report lands under "$c/<reviewDir>"
```

`ORCH` is this repository's root. The block is unit 40 §4's, which corrected unit 37 §4's; it lands
in the README before the first run, so no run follows a step a later unit rewrites. Measured on
2026-10-23 (unit 37 §4): `cygpath -m "$TEMP"` printed `C:/Users/DAILY-~1/AppData/Local/Temp` here,
and in a fixture whose `.git/index` was overwritten with seven bytes `git status` exited 128 while
`test -z "$(git status …)"` read the tree as clean.

The status check sits after the clone is made and before the call, so it reads the tree the arm will
review. After the call, that clone's status lists one untracked path, the arm's own report, which is
what AC1 observes after the fact.

### What it does not check

That no agent reads a sibling clone by absolute path. The per-arm clone and the clean-tree check
remove the in-tree path the finding names. A read outside the clone is what spec 1 §4's outside-read
void rule reads, and for these runs S9 records it with the transcript line that shows it.

### Files touched (estimate)

- `tools/workflows/README.md`
- `memory/builds/dFairHearing/build/`

The README's replay section gains the per-arm step (S7) before the first run. Spec 15 S6's product
files, `gotchas.py` and the harness template, are unit 35's.

### Alternatives rejected

- **Keep one clone per record and delete arm 1's report before arm 2.** A cleanup step is one more
  thing a run can skip, and the durability files a resumed run writes sit beside the report. A fresh
  clone has nothing to clean.
- **Write the report outside the clone.** That changes the harness's `reviewDir` contract for every
  caller to serve one comparative run.
- **Run first, and let the later units correct the per-arm step and the record** — unit 25 §8 F2
  option 2.

## 5. Production-readiness checklist

- security — the clones sit under `%TEMP%`, outside the repository, and the replay section's one EXIT
  trap clears its transient ref (unit 25 S9). The lenses keep the diff kind's read-only probe rules.
- perf / scale — eight clones in place of four, each a local fetch of one range head. The agent cost
  is unit 25's, about 100 agents (spec 15 AC8).
- error / empty / loading states — an empty `SCRATCH`, `ORCH` or temp variable, an unreadable
  orchestrating head, a stale clone name, a `HEAD` that is not the range head, a failed status call
  and a dirty tree are each refused before the call, and the arm takes a new attempt.
- observability — the verdict record names every attempt's clone, `HEAD`, status and outcome beside
  the orchestrating commit and its blobs.
- risks — a flaky run costs a new clone per attempt; unit 35 S1's rule, written before these runs,
  reads no attempt after the second completed one, so a further re-run spends agents and moves
  nothing.
- testing — AC1 to AC7. Spec 15's `New arm:` line for `gotchas.py`'s selftest is unit 35's.
- migration — none for adopters: the README's replay section gains a step only a replay runs.
- user docs — `tools/workflows/README.md`'s replay section (S7); no `help/` page.

## 6. Acceptance criteria

- **AC1** — When the verdict record lands, it lists every attempt of the eight record and arm pairs,
  each under its own `f<r><a><n>` clone, no name twice, with its outcome; each `refused` attempt
  carries its reason. For each `completed` or `failed` attempt the observed status is empty and `git -C
  "$TEMP/<clone>" rev-parse HEAD` equals its record's range head, and for each `completed` one `git -C
  "$TEMP/<clone>" status --porcelain --untracked-files=all` lists exactly one path, that arm's own
  report.
  Red when: two attempts share a clone, so one clone lists two reports, a clone dirty before its call
  is reviewed, or a clone at another commit is reviewed.
  fixture: the clones under `%TEMP%`, made by the pass and kept until unit 40's pass.
- **AC2** — When the per-arm block runs into a scratch clone holding one planted untracked file, it
  exits 2 printing `dirty:` and the clone's path before any harness call. A second run into an existing
  clone name exits 2 before any fetch. Every re-run the record lists names a clone whose attempt number
  is higher than the one before, each void or `failed` attempt is followed by the next attempt's row,
  and each void cell citing an outside read holds a `<transcript file>:<line>` and an absolute path.
  Red when: the dirty clone is reviewed, a re-run reuses a clone, or an outside read is recorded
  without the transcript line that shows it.
  fixture: one scratch clone under `%TEMP%/fdirty`, made by the probe.
- **AC3** — When `replay_scorer.py --experiment` runs over this unit's committed manifest, it prints
  `arm ungated: varies checklist from selected`, then `parsed selected: 4 of 4` and `parsed ungated: 4 of
  4` before any figure. The verdict record names each record's recall under both arms, `paired 4 of 4`,
  both pooled figures, the decision and the `ungated` class set.
  Red when: a record one arm did not answer is pooled.
  cost: about 8 review runs, roughly 100 agents.
- **AC4** — When this unit's commit lands, `git diff <this unit's parent> HEAD --
  tools/memory-tree/gotchas.py tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js`
  prints nothing. The decision and spec 15 S6's product files are unit 35's (its AC4), and the
  behavioural check of a `selected` decision is `TOOL-dFairHearing-32` S13's.
  Red when: this unit's commit changes a product file of spec 15 S6 before any decision is taken.
- **AC5** — When `grep -n "cygpath -m" tools/workflows/README.md`, `grep -n "status failed"
  tools/workflows/README.md` and `grep -n "orchestrating head unreadable" tools/workflows/README.md`
  run, each prints a line in the replay section, and that section's fenced bash lines still open
  `trap '` on one line. A scratch run of the per-arm block exits 2 naming the variable with `SCRATCH`
  empty, then `ORCH` empty, then `TEMP` and `TMPDIR` both empty, before any clone path is used. With
  `ORCH` naming a directory that is no repository it exits 2 printing `orchestrating head unreadable`,
  and over a fixture clone whose `.git/index` is overwritten it exits 2 printing `status failed:`, each
  before any harness call. Over a clean fixture clone with every variable set, `grep -c "^orchestrating
  [0-9a-f]\{40\} clone " run.log` prints 1, and that sha equals `git -C "$ORCH" rev-parse HEAD`.
  Red when: a path is built from an unset variable, a failed status reads as clean, or the log line is
  absent, empty or unanchored.
  fixture: clones under `%TEMP%/fpa` and `%TEMP%/fcx`, made by the probe and removed after it.
- **AC6** — When the verdict record lands, every `orchestrating` line it quotes from the run log names
  one sha, the orchestrating commit it records. `git log --diff-filter=A --format=%P -1 -- <record>`
  prints a first parent equal to that commit, `git merge-base --is-ancestor <unit 23's commit> <that
  commit>` exits 0, and each blob the record names equals `git rev-parse <the adding commit>:<path>`.
  Each clone's `HEAD` stands on a line of its own.
  Red when: the record's commit is one the writer picked, the runs straddle two orchestrating commits,
  a procedure file changed between the runs and the commit, or a clone's `HEAD` stands in for the
  orchestrating commit.
- **AC7** — When this unit's commit lands, `test -e` exits 0 for every clone directory, report and
  transcript file the verdict record names.
  Red when: the pass removes a clone, report or transcript the record cites, which unit 40 S9 then
  cannot re-derive.

## 7. Gates

`review-replay selftest` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `gotchas selftest` · `recall floor` · `recall floor arms` · `review-protocol parity (kit vs dogfood)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `policy fixtures`

No new arm: the per-arm step is README prose that AC5's scratch run observes, and spec 15's `New arm:` line for `gotchas.py`'s selftest moved with the decision to `TOOL-dFairHearing-35`, whose §7 carries it.

## 8. Open questions

- **F1 — Does unit 25 still run unit 15's replay at its own order?** Options: (a) it runs it as written,
  and this unit re-runs it in isolated clones and reverses any verdict that moves; (b) unit 25 hands
  the replay to this unit, each superseded criterion named in its hands-off bullet, and the runs
  happen once, here. (a) spends about 100 agents on a comparison already found contaminable and can
  land spec 15 S6 only to take it out again. (b) closes the finding with one run per arm and leaves
  unit 25 replay 1. RESOLVED (agent, 2026-10-23, delegated): (b), rung 3, unit 25 §8 F1's form.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 28 (item H2, HIGH) of the round-3 spec
  audit of specs 4, 14, 25, 26 and 27.
- rev-2 · 2026-10-23 · §3 · the round-4 spec audit's disposal: hands-off edges to TOOL-dFairHearing-35 (the attempt rule,
  the scoring and the decision, finding id 32) and TOOL-dFairHearing-37 (seven minors).
- rev-3 · 2026-10-23 · §3 · the round-5 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-40 (four minors that read the verdict record).
- rev-4 · 2026-11-03 · §7 · the leg line adds `policy fixtures`, whose guard §4's
  `tools/memory-tree/gotchas.py` trips (fix brief 2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief, item 1).
- rev-4 · 2026-11-03 · §1 · §10 · the harness's `reviewDir` default and report instruction re-cited at
  `9c1a2857a`, :297 and :1749 having moved to :400 and :2121 (fix brief 2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief, item 2).
- rev-5 · 2026-11-03 · header · §4 · §8 · the header's order 21 to 23, after unit 25 at 22 and
  `TOOL-dFairHearing-27` at 21; §4 and §8 re-word the two units' positions to match (fix brief
  2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief, items 2 and 3).
- rev-6 · 2026-11-03 · §1 · S1 · S2 · S3 · S5 · S7 · S8 · S9 · S10 · §3 · §4 · §5 · §7 · AC1 · AC2 ·
  AC4 · AC5 · AC6 · AC7 · the replays' pre-run corrections folded in (fix brief
  2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief, item 2; unit 25 §8 F2). S7 carries unit 37
  S8's per-arm clone, forward-slash path and run-log line (id 20) and S12's checked status (id 34), as
  unit 40 S12, S13 and S14 correct them (ids 15, 38 and 22), and AC5 carries unit 37 AC8 and unit 40
  AC7; S8 carries unit 32 S14's orchestrating-commit binding (ids 5 and 13); S9 carries unit 32 S20
  and S21's unit-15 half as unit 37 S2 words it (ids 29, 30 and 2), with unit 40 S8's `failed`
  outcome (id 35) and S9's quoted void cell (id 13); S10 carries unit 40 S9's reports and transcripts
  kept on disk (id 13); AC1 carries unit 37 S11's restatement over every attempt (id 33); AC4 carries
  unit 37 S4's correction of its `selected` half (id 5), which now reads no count, and §7 drops the
  `New arm:` line unit 35 already carries. S1, S3, §4 and §10 point at the README's replay section in
  place of unit 25 §4's block, which unit 25 S8 retired.

## 10. Reuse audit

No new mechanism: the clone procedure is the replay section of `tools/workflows/README.md` (unit 23's
recipe, unit 27 S22's envelope, unit 25 S8's placement), which S7 extends with the per-arm step, and
the scorer is unit 14's `check_experiment`. `python
tools/codebase-map/reuse_lookup.py "give each comparative review run its own clean working tree"`
ranked the generic `tree`, `run`, `run_arms` and `run_git` stems, none a per-run clone. The
report-path seam was read at `tools/workflows/tier2-review.template.js:400` (the `reviewDir`
default) and `:2121` (the report written under `${repo}/${reviewDir}`), both at `9c1a2857a`. The recall query returned
the audit's H2 item, spec 15's brief row for the replay and `TOOL-aEvidencedLens-10`, the replay
scorer's origin, and no prior per-arm isolation rule. §8 F1 follows unit 25 §8 F1's hand-off form,
read from that spec.

Recall terms used: `python tools/memory-recall/query.py "two arms of a comparative replay share one clone so the second reads the first report" --terms "replay arm clone isolation reviewDir report working tree selected ungated porcelain fresh attempt contamination"`
