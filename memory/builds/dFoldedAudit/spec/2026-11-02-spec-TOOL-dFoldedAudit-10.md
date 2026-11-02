# TOOL-dFoldedAudit-10 — a chain round joins to the terminal review row and the spec-audit records it claims

**Status:** CLOSED · rev-2 · 2026-11-02 · node d · Tier-2 · base 74274869 · streams tooling · order 110

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dFoldedAudit-10-1-builder-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-10-1-builder-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-10-ledger.md](../build/2026-11-02-build-TOOL-dFoldedAudit-10-ledger.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md) | research | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-3-cross-read-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-3-cross-read-return.md) | journal | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-prompt-TOOL-dFoldedAudit-10-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-10-build-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-10-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-10-spec-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md) | research | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |

<!-- /gen:spec-records -->

## 1. Goal

A chain round grades itself. `--record-round` compares its counts only with its own `--finding` rows
and joins `--audited` to nothing, so a forged zero-count round reads `STOP · reason clean`. The
verdict can also stop clean over a folded spec the next round never read, because `aud` is one set
across all rounds. This unit joins each round in check 2 to the terminal review row of the same
exit and to the tracked `spec-audit` records, and holds a round's promotions and folds to the next
round's own `audited` row. It closes items H2 and M7 of the closing review, and the design it
extends is [chain] and [address].

## 2. Scope (IN)

- **S1** — The count join. Check 2 reads every tracked `-chain-rounds.md` record. A round whose
  subject has a terminal `review · item <subject>` row in any of that build's `RUN*.md` files, a
  rotated one included, reds when that row's blockers or highs exceed the round's distinct BLOCKER
  or HIGH ids. Observed by AC1, AC2, AC3 and AC6.
- **S2** — The first row. Where one subject holds terminal rows in two records, the join reads the
  earliest by timestamp. Observed by AC7.
- **S3** — The attended round. A round with no terminal row is attended, not forged: it is not
  joined, it reds nothing, and the skip is announced. Observed by AC4.
- **S4** — The audited join. Only for a round the count join reached, every id on its `audited` row
  must be named by a tracked `spec-audit` record of that build. Observed by AC5.
- **S5** — The shared reader. `read_spec_audit_ids` in `tools/unattended/lib-unattended.sh` answers
  which ids a build's tracked `spec-audit` binding lines name, and both the `specs-audited` term and
  check 2 call it. Observed by AC10.
- **S6** — The re-audit. `derive_chain_verdict` keeps each round's own `audited` ids, and adds to U
  every live id of P(N-1) and F(N-1) that round N's row lacks, so the verdict stays
  `CONTINUE · reason unreviewed`. Observed by AC8 and AC9.
- **S7** — The census. Both joins feed `rv_bad` and the verdict change adds no refusal, so neither
  file gains a `fail` site. Observed by AC11.

## 3. Non-goals (OUT)

- Enforcing the verdict. `--dispatch`, `--close` and a Definition-of-Done item stay out of this unit,
  because `TOOL-dFoldedAudit-9` holds H1. H2 fixes a record nobody checks and H1 a verdict nobody
  obeys, so neither closes the other.
- A presence term. A counted spec exit row with no chain round reds nothing here, and no `--close`
  term keys on a declared `disposal`, which the report's corrected fix rules out.
- Joining a fold to the spec it names, which `TOOL-dFoldedAudit-11` holds.
- Grading MEDIUM or LOW counts. The report's join reads blockers and highs only, and a round's rows
  need not carry a minor that folded.
- Any change to the chain record's row grammar. The round's counts stay derived from its rows, so no
  field is added and `derive_chain_verdict`'s row test does not move.
- A second copy of the verdict. Check 2 reads no verdict word and computes no set the verdict
  computes, and the verdict stays in the driver alone.
- The verdict's skip list, review item M8. A body row prefixed `# ` reads as it does today.
- A new cutoff. No chain record is tracked today, so no landed record can red.
- Any closing diff review row, message or grading. The join reads rows only through a chain round's
  subject, and a chain subject is `<slug>-spec-set-r<N>`, never the slug.

### Edges

- **consumes-from** external — the record `write_chain_round` writes and the sets `derive_chain_verdict` reads, both shipped by a closed unit; a change to either row's spelling reds the arms that write a round through the real verb
- **hands-off** `TOOL-dFoldedAudit-15` — the first verdict test in M4 of `memory/guides/BUILD-METHOD.md` still names only a spec no round audited when this unit lands, so CONTINUE `unreviewed` has a case M4 does not state until that unit's batch writes it. This unit writes no carrier

## 4. Design

Every line cited here was read at `f055a11b`, the branch tip, because units 1 to 8 moved them past
the header's base.

### The count join

A new block in check 2 sits after the record loop's `done`
(`tools/unattended/check-unattended.sh:987`) and before the `fail 2` line (`:988`), inside the branch
where `rv_bad` is live. It adds no `fail` site, so `_disp_ok`'s announced skip covers it too.

```bash
for rv_cr in $(GIT ls-files ":(glob)$M/builds/*/build/*-chain-rounds.md" 2>/dev/null); do
  [ -f "$rv_cr" ] || continue
  # the build's tracked RUN*.md files that exist, then one awk over the record and those files
done
```

One awk reads the record and then each `RUN*.md`, told apart by `FILENAME`, so the sets are built
once.

| Input | Reads |
|---|---|
| a `round <N> · subject <s> · audited <ids>` row | subject and `audited` ids per round |
| a `round <N> · finding <id> · BLOCKER` or `HIGH` row | one distinct id per round and severity, the test `write_chain_round` makes through `b_ids` and `h_ids` (`tools/unattended/unattended.sh:13529`) |
| a `review · item <s> · reason ...` row with an exit token | that subject's first row by timestamp, with its blockers and highs |

The review row takes check 2's own reading: the row regex at
`tools/unattended/check-unattended.sh:845`, the exit tokens at `:878`, the blockers match at `:853`
and the highs match at `:863`. A row with no `highs` field is an older shape, so only its blockers
compare. The round's counts are distinct ids because a multi-spec fold writes two rows for one id
(`tools/unattended/unattended.test.sh:2689`), and a count of rows would pass a HIGH that stood
twice over. A round holding more ids than the row is legal, because an UNVERIFIED finding the
disposal adjudicated adds a row above the count. That is why the test is "exceeds", the same
direction as the verb's "fewer" at `tools/unattended/unattended.sh:13535`.

An honest round cannot red here. `renderChainRecord` passes the `au.blockers` and `au.highs` that
`writeRound` passes to `--review` (`tools/workflows/unattended-build.template.js:2303`), under the
one `subject` at `:369`, and the verb already refuses fewer rows than those two counts.

The fault line is one entry of `rv_bad`, in this shape:

```
<record> (round <N>, subject <s>: its first terminal review row counts <b> blocker(s) and <h> high(s), and the round disposes <rb> and <rh>, so a confirmed finding reached no row the chain verdict reads)
```

### The first row

`--review` refuses a second terminal row per subject by reading the live record alone
(`tools/unattended/unattended.sh:12914`), so a later run can write another after a rotation.
`--record-round` refuses that subject as a replay (`:13523`), so the later row has no round to answer
for. The round was written after the first row, and reading any later row would put a permanent red
on two append-only records, which is the class of review item H6. Timestamps compare as strings
because the row's stamp is ISO UTC.

### The attended round

A round whose subject has no terminal row is left alone, because `writeRound` makes no driver call in
attended mode, so no row exists there to join. A non-terminal row does not join either. After each
record, check 2 prints one line on stdout when any round was left alone, outside `report()` as the
blank-cutoff announcements are (`tools/unattended/check-unattended.sh:725`):

```
unattended: check 2 read <n> chain round(s) in <record> with no terminal review row and took each as attended, so nothing grades their counts or their audited ids
```

The awk prints that count on its first line and each fault after it, so one capture feeds both.

### The audited join

`read_spec_audit_ids` is read once per record, its output joined with spaces and handed to the awk as
one `-v` value, the way `live` reaches `derive_chain_verdict` (`tools/unattended/unattended.sh:13569`).
The awk builds a set and tests each id as a whole key, so `FIX-tFix-31` does not satisfy
`FIX-tFix-3`. Only a round with a terminal row is joined. The fault line reads:

```
<record> (round <N>, subject <s>: audited <ids> named by no tracked spec-audit record, so the round claims an audit that left no evidence)
```

Both routes that write a round leave such a record. A report's binding line names every subject
(`tools/workflows/tier2-review.template.js:318`), and a clean round's line names every id of
`auditedIds` (`tools/workflows/unattended-build.template.js:2991`), which is the join `audited` is
rendered from (`:2731`).

### The shared reader

The loop at `tools/unattended/unattended.sh:12032-12041` moves to `tools/unattended/lib-unattended.sh`
beside `expand_id_runs`, and the `specs-audited` term calls it. Check 2 is the kind's second
instance, and check-unattended already sources the library.

```bash
read_spec_audit_ids() { # build folder -> stdout: ids its tracked spec-audit binding lines name, one per line
  local f
  for f in $(GIT grep --cached -l -E '^\*\*Serves:\*\*[[:space:]]*spec-audit([[:space:]]|$)' -- "$1/*.md" 2>/dev/null); do
    GIT show ":$f" 2>/dev/null | awk '<the term's twelve-line awk, unchanged>'
  done | expand_id_runs
}
```

The `git grep` narrows the walk and decides nothing: the twelve-line window and the fence test stay
the awk's, so a record quoting another's binding line still names nothing. It exists because check 2
runs on every bar, where the term runs once at `--close`, and today's loop spawns two processes per
`.md` file of the build. Measured on 2026-11-02 at `f055a11b` over `dMindYourWords`, `dTrueNorth`,
`aEvidencedLens`, `aProbedUnit`, `aGradedMandate` and `dFoldedAudit`: PINNED, the sorted id list of
both forms hashed identically on all six, and the narrowed form took 60 to 190 ms a build.

### The re-audit

`aud` at `tools/unattended/unattended.sh:13601` stays cumulative, because a spec round 1 audited stays
reviewed. Beside it, the same branch keeps `audn[r]`, that round's own ids. In `END`, once `prior` is
set at `:13617`, the loop at `:13619` adds a live id to U on either test:

| Test | Reads |
|---|---|
| not in `aud` and not in P(N) | today's step 1 |
| in `prior` and not in round N's own ids | a promotion or fold round N skipped |

The loop walks `live`, which holds no CLOSED or WONTDO id, so a frozen or retired spec holds nothing
open. Round 0 and round 1 have an empty `prior`. The other four steps do not move, and step 1 still
prints U with P(N) and F(N). The comment at `:13553-13562` states the second test.

Every existing verdict arm in `tools/unattended/unattended.test.sh` already re-audits `prior` in its
next round, so none moves. This unit's own fixture rows claim rev 2 or 3, which is where
`TOOL-dFoldedAudit-11` leaves the suite's fixture specs.

### What the joins do not check

The block's header comment says each of these:

- A round with no terminal row, whether attended or a run that skipped `--review`.
- That the terminal row itself is true. The row and the round are two acts of one run, so a run
  forging both passes, and the closing review reads that diff.
- That the audit read the spec at its current rev. Like `specs-audited`, the join is a `has ever
  named` lower bound, so a re-audit round's ids pass on round 1's record.
- MEDIUM and LOW counts.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `read_spec_audit_ids` | `sh.function` | `lexicon.py --suggest` answered OK on 2026-11-02 |

### Rollout

Live at landing, and it reads nothing until a chain record is tracked. `git ls-files '*-chain-rounds.md'`
printed nothing at `f055a11b` (PINNED), so the real tree gives the join an empty population and the
arms below are its only coverage.

### Files touched (estimate)

`tools/unattended/lib-unattended.sh` · `tools/unattended/unattended.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **The join inside `--record-round`.** That verb names no run-state file, so an attended run takes
  the same route, and a hand call could still skip the row. A gate reading tracked records is the
  independent reader H2 asks for.
- **A `--close` term keyed on a declared `disposal`.** The report's skeptic rejected it, because the
  value is the caller's copy and an attended run never reaches `--close`.
- **Treating a round with no row as forged.** Every attended chain would red.
- **Counts on the `round` row.** That moves the row grammar `derive_chain_verdict` reads for the same
  numbers the rows already give.
- **Replacing `aud` with the per-round set.** A spec audited in round 1 and not in round 3 would read
  unreviewed, so the chain could not end.
- **A second copy of the `spec-audit` loop in check 2.** It is the second instance of one reader, and
  [reuse] extracts it.

## 5. Production-readiness checklist

- security: no write path, and no shell string is composed from a record's text, because the awk takes
  the files as data. The join is a read by a gate, so a round cannot widen it.
- perf / scale: per tracked chain record, one `git ls-files`, one `read_spec_audit_ids` and one awk.
  The pinned figure in §4 prices the reader, and the population is zero today.
- error / empty / loading states: no record reads nothing and prints nothing, a tracked record gone
  from the worktree is skipped as check 2's record loop skips one, and `--chain-verdict` refuses that
  state by name. An `audited` id with no record at all takes the fault line.
- observability: each fault names the record, round and subject, and the attended skip prints a count.
- risks:
  - A run forging both rows passes, as §4 states.
  - A caller that keeps departing from the printed `audit` ids stays on step 1 and never reaches the
    ceiling, because step 1 is read first. Each such round's `audited` row shows the departure.
  - A row and a chain round written in different builds join to nothing, so only a same-build subject
    grades.
- testing: fixtures per §6, no gate, with the arms on `New arm:` lines in §7. The join's rows are
  written by the real verb, so a drift in the record's grammar reds an arm.
- migration: none. No tracked record changes reading, and no chain record is tracked.
- user docs: N/A. `help/` documents neither the chain nor check 2, which a grep over it confirmed on
  2026-11-02.

## 6. Acceptance criteria

Fixture J is a scratch git repository at `%TEMP%/fa10j` on branch `main` with no remote, holding a
copy of `tools/unattended/` whole, a `.unattended.conf` carrying `MEMORY_ROOT=memory`,
`DISPOSITION_CUTOFF="2000-01-01"`, `REVIEW_ROUNDS="1"` and `SPEC_FOLD_CUTOFF="2026-11-01"`, and a build
`memory/builds/tFix/` whose `RUN.md` is built as the suites' `mkdisp` builds it, first committed at
`2026-11-02T12:00:00 +0000`. `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` are cleared. `$D` and `$G` are
`bash "$F/tools/unattended/unattended.sh"` and `bash "$F/tools/unattended/check-unattended.sh"`, the
fixture's own copies, run with the fixture as the working directory. A round is written by
`$D --record-round` and committed. Every `--finding` row here is `new-mechanism`, because the round's
counts do not read nature and a `local` row owes a spec once `TOOL-dFoldedAudit-11` lands. `ROW1` is a
committed row `2026-11-02T01:00:00Z review · item S1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 0 · folded 1 · promoted 0 · disposition fold`,
and `ROW0` is the same row with zero counts and no disposition. `REC` is a tracked record under the
build's `reviews/` folder whose first line is `**Serves:** spec-audit FIX-tFix-1@rev-1 FIX-tFix-2@rev-1`.

Fixture C is a scratch git repository at `%TEMP%/fa10c` holding copies of
`tools/unattended/unattended.sh` and `tools/unattended/lib-unattended.sh` under `u/`, a
`.unattended.conf` carrying `MEMORY_ROOT=memory` and `SPEC_FOLD_CUTOFF="2000-01-01"`, because
`TOOL-dFoldedAudit-13` refuses a `local` row under a blank cutoff, and a build `dFix` whose README's
roster region names
`FIX-dFix-1` to `FIX-dFix-7`, each with a tracked OPEN spec at rev-3 whose Revision log holds rev-1 to
rev-3, and no `RUN.md`. `$V` is `bash "$F/u/unattended.sh"`, run from the fixture root with `GOV_REMOTE`
and `GOV_DEFAULT_BRANCH` cleared. `ALL` is the seven ids.

- **AC1** — When fixture J commits `ROW1`, `REC` and the round from `$D --record-round tFix --subject S1 --audited "FIX-tFix-1 FIX-tFix-2" --blockers 0 --highs 0`,
  `$G` prints `UNATTENDED check 2 FAILED` and `counts 0 blocker(s) and 1 high(s), and the round disposes 0 and 0`.
  Red when: the join reads only the round's own rows, so a forged clean round stands.
- **AC2** — When a committed row reads `blockers 2 · BOUNDED · highs 0 · minors 0 · folded 2 · promoted 0 · disposition fold`
  and the round carries `--blockers 1 --finding 5/BLOCKER/new-mechanism/FIX-tFix-1/FIX-tFix-4/1`, `$G`
  prints `counts 2 blocker(s) and 0 high(s), and the round disposes 1 and 0`. When a row counts
  `highs 2` and the round carries one HIGH id on two rows, `$G` prints `counts 0 blocker(s) and 2 high(s), and the round disposes 0 and 1`.
  Red when: the blockers half is unread, or the round counts rows rather than distinct ids.
- **AC3** — When fixture J commits `ROW1`, `REC` and a round with `--highs 1 --finding 4/HIGH/new-mechanism/FIX-tFix-1/FIX-tFix-4/1`,
  `$G` prints no `UNATTENDED check 2 FAILED` line. It prints none with a second HIGH id on the round
  beside the row's count of one.
  Red when: the test is "differs" and not "exceeds", so an adjudicated UNVERIFIED finding reds an
  append-only record.
  fixture: this is the green control beside AC1, so neither passes by finding nothing.
- **AC4** — When fixture J commits a zero-count round for `S1` with no terminal row and no `REC`, `$G`
  prints no `UNATTENDED check 2 FAILED` line and prints `took each as attended`. It prints the same
  with a mid-loop `blockers 1 · CONVERGING` row for `S1`.
  Red when: a round with no row reds, or the skip prints nothing.
- **AC5** — When fixture J commits `ROW0`, `REC` and a round with `--audited "FIX-tFix-1 FIX-tFix-3"`,
  `$G` prints `audited FIX-tFix-3 named by no tracked spec-audit record`. It prints that with `REC`
  also naming `FIX-tFix-31`, and with a binding line naming `FIX-tFix-3` on line 13. It prints no check 2
  line when `REC` names `FIX-tFix-1..3`. With no `REC` and no terminal row, no id is joined.
  Red when: the test matches a substring, reads past the twelve-line window, or joins an attended
  round.
- **AC6** — When AC1's `ROW1` sits in a tracked archive `RUN.LANDED.0bd0bd00.md` beside a `RUN.md`
  holding no review row, `$G` prints AC1's sentence.
  Red when: the join reads only the live record, so a rotation hides a forged round.
- **AC7** — When an archive holds `ROW1` dated `2026-11-02T01:00:00Z`, a later `RUN.md` row for `S1` dated
  `2026-11-20T01:00:00Z` counts `highs 3 · minors 0 · folded 3 · promoted 0 · disposition fold`, and the
  round carries one HIGH id, `$G` prints no `UNATTENDED check 2 FAILED` line. Swapping the two dates
  prints `counts 0 blocker(s) and 3 high(s), and the round disposes 0 and 1`.
  Red when: the join reads any row, which reds a chain no verb can repair.
- **AC8** — When fixture C records `$V --record-round dFix --subject s1 --audited "$ALL" --blockers 0 --highs 1 --finding 1/HIGH/local/FIX-dFix-2/FIX-dFix-2/2`
  and then `--subject s2 --audited FIX-dFix-3 --blockers 0 --highs 0`, `$V --chain-verdict dFix` prints
  `round 2 · CONTINUE · reason unreviewed · audit FIX-dFix-2` and exits 0. With `--audited FIX-dFix-2`
  on round 2 it prints `round 2 · STOP · reason clean`.
  Red when: `aud` alone decides step 1, so a run scopes itself out of the re-audit.
- **AC9** — When round 1 audits `ALL` and folds a HIGH into `FIX-dFix-2`, round 2 audits `FIX-dFix-2` and
  folds a HIGH on `FIX-dFix-3` into it, and round 3 audits `FIX-dFix-2` and folds a HIGH on `FIX-dFix-3`
  into it again, `$V --chain-verdict dFix` prints `round 3 · CONTINUE · reason unreviewed · audit FIX-dFix-3`. With
  round 3 auditing `FIX-dFix-3` it prints `round 3 · STOP · reason own-work`. With `FIX-dFix-3` at
  CLOSED and round 3 auditing `FIX-dFix-2`, it prints `round 3 · STOP · reason own-work`.
  Red when: the test reads terminal ids, so a frozen spec holds the chain open, or `own-work` answers
  over a fold nobody re-read.
- **AC10** — When `grep -c 'read_spec_audit_ids "' tools/unattended/unattended.sh tools/unattended/check-unattended.sh`
  runs, each file prints 1, and `grep -c 'for _sa_f in' tools/unattended/unattended.sh` prints 0. A scratch
  script holding the term's loop as it reads at `f055a11b` prints the same sorted ids as `read_spec_audit_ids`
  for the six builds §4 names.
  Red when: a second copy of the reader stays, or the narrowing loses a record.
  figure: DERIVED, both sides computed at the observation.
- **AC11** — When `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh tools/unattended/check-unattended.sh`
  runs before and after the pass, it prints the same two figures.
  Red when: a join adds a `fail` site, which passes the file's `check-arms` ceiling.
  figure: DERIVED. They read 318 and 264 at `f055a11b`, the ceilings only the owner moves.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `routed-commits selftest` · `shell hygiene (a fork spent on builtin work)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit version markers`

New arm: tools/unattended/check-unattended.test.sh · covers AC1 AC2 AC3 · a forged zero-count round written by the real verb beside a terminal row carrying a HIGH, with its green control, staged with the join's exceeds test forced false, which greens the forged round · none
New arm: tools/unattended/check-unattended.test.sh · covers AC4 · a round with no terminal row, staged with the attended count forced to 0, which leaves the skip silent · none
New arm: tools/unattended/check-unattended.test.sh · covers AC5 · ids a record names, a substring of one and a line past the window, staged with the whole-key test turned into `index`, which lets `FIX-tFix-31` satisfy `FIX-tFix-3` · none
New arm: tools/unattended/check-unattended.test.sh · covers AC6 AC7 · a rotated folder and two rows of one subject, staged with the join's file list narrowed to the live `RUN.md`, which hides the archived row · none
New arm: tools/unattended/unattended.test.sh · covers AC8 AC9 · the re-audit and its terminal exclusion, staged with the second test cut from the U loop, which turns AC8 back to `STOP · reason clean` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the closing review's items H2 and M7, the promotion notes,
  and the design's [chain] and [address].
- rev-2 · 2026-11-02 · §3 · §6 · §7 · Fixture C's conf declares `SPEC_FOLD_CUTOFF="2000-01-01"`, because
  `TOOL-dFoldedAudit-13` ships first and refuses a `local` row under a blank cutoff. §7 gains
  `routed-commits selftest`, whose guard §4's `tools/unattended/lib-unattended.sh` trips. M2's
  cross-read: the M4 edge read as outside this run while `TOOL-dFoldedAudit-15` writes that sentence,
  so it is a `hands-off` to that unit.

## 10. Reuse audit

`reuse_lookup.py` on "join a recorded round to a terminal review row and spec-audit records" ranked
name-stem symbols and no chain reader, so the seams are found in source. This unit extends check 2's
review-row reading (`tools/unattended/check-unattended.sh:845-872`) and its `rv_bad` channel, the
`specs-audited` loop (`tools/unattended/unattended.sh:12032-12041`) over `expand_id_runs`
(`tools/unattended/lib-unattended.sh:2235`), and `derive_chain_verdict`
(`tools/unattended/unattended.sh:13567`). `check_audit_fold` and `read_spec_revisions` in
`tools/memory-tree/design_lib.py` were ranked and do not fit, because this kit copy-installs without
the memory-tree kit. `tools/memory-tree/gotchas.py --for-paths` selected
`fixture-passes-by-finding-nothing`, which AC3 and AC4 answer beside the red arms,
`id-matched-as-a-substring`, which AC5 answers, `assertion-between-two-derived-values`, which the two
separate writers answer, and `a-helper-extraction-blinds-a-per-function-rule`, which a grep for
`_sa_f` and `_sa_named` over `tools/` cleared: no source rule reads that loop. The review's cites were re-read at
`f055a11b` and held. The recall hits were the report itself and the verbs entry, and neither disagreed
with source.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit chain round joined to the review row and a fold joined to the spec revision" --terms "spec-audit chain round record-round terminal review row fold rev revision log forged"`
