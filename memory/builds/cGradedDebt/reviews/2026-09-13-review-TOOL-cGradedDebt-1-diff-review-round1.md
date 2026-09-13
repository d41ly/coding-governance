**Serves:** diff-review TOOL-cGradedDebt-1 TOOL-cGradedDebt-2

# cGradedDebt — Tier-2 diff review, round 1

*Node `c`, 2026-09-13. Subject: the curation-debt registry stops DROPPING listed files from checks 6,
7 and 8 and starts GRADING them, plus the backlog-token cleanup that lands beside it. Four finder
lenses, five skeptic batches. Every `file:line` below was re-opened in this worktree before it was
written down, and every claim that could be settled by running something carries that run's output
inside the finding.*

**Range reviewed: `09a22d2bf5c3fc51bdc3ccee8c727b0793664106...c642c23f`** — one commit, 22 files,
+582/-30. **Round: 1.**

## Verdict: BLOCKED

Four blockers, and all four are gates that are RED at the landing commit — none of them is a
judgement call about the design. Three legs (`harness arms`, `kit/dogfood doc parity`,
`drift-audit records`) carry no guard or are guarded on files this very commit touches, so they run
on an ordinary bar: this commit cannot be pushed as it stands. The fourth is the kit's own self-test,
which this build's Definition of Done owes with `GATE_SELFTESTS=1` because it is kit work.

The engine itself is sound. `split_debt`'s path extraction fails in the safe direction by
construction, the `DEBT_EARNED` subshell discipline holds, the `#rows` sentinel sums and strips
correctly, and the gate exits 0 over this repo with no stale row and the four report lines the spec
predicts. Every blocker is a one-to-three-line repair in a test, a template or a status header. What
is actually wrong here is that the bar was not run before the commit landed — three of the four
blockers announce themselves in under two seconds each.

Nine distinct defects (4 blocker, 0 high, 1 medium, 4 low) out of 14 confirmed findings: three
clusters were the same defect reached by different lenses, and are merged below with their source
ids cited.

## Review shape

Raw 19 · confirmed 14 · refuted 5 · unverified 0 · precision 0.74.

**Run integrity.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every count is zero, so
this run is complete and a zero finding count in the hunted areas below is positive evidence rather
than an absence of coverage.

Co-reporting was heavy on the two test defects: three lenses independently reached the unarmed
branch (ids 5, 10, 13) and three reached the block-extractor swallow (ids 4, 9, 14), which is what
drags raw precision down to 0.74 without a single one of those reports being wrong.

## Findings

| # | Sev | File:line | Defect |
|---|-----|-----------|--------|
| B1 | blocker | `tools/memory-tree/check-memory-hygiene.test.sh:1472` | The new arm greps a PREFIX of the fail message, so `check-arms.py` reads the branch as unarmed and the `harness arms` leg exits 1 |
| B2 | blocker | `tools/memory-tree/check-memory-hygiene.test.sh:1479` | The check-6 block extractor never closes before the new per-row report, so the negative assertion matches the REPORT and fires a false FAIL |
| B3 | blocker | `tools/memory-tree/HYGIENE.template.md:98` | The unit's prose landed only in the rendered `memory/HYGIENE.md`; the template it renders FROM got the version bump alone, so `kit/dogfood doc parity` is RED |
| B4 | blocker | `memory/guides/SESSION-KICKOFF.md:253` | A product source cites `TOOL-cGradedDebt-1`, whose spec is still SPECCED, pushing a shrink-only drift signal from its pin of 2 to 3 |
| M1 | medium | `tools/memory-tree/check-memory-hygiene.sh:1814` | The per-row report's denominator is the literal `6 7 8` rather than the checks the path is actually in, overstating the waiver width of 3 of the 4 live rows |
| L1 | low | `tools/memory-tree/check-memory-hygiene.sh:1808` | The stale-entry guard gates on the INDEX while earning is decided against the WORKTREE, so a tracked-but-deleted file reds with the remedy "delete the row" |
| L2 | low | `memory/builds/cGradedDebt/spec/2026-09-12-spec-TOOL-cGradedDebt-1.md:171` | AC4 pins the graded-row count at 499 and the landing commit's own run prints 500 |
| L3 | low | `memory/backlog/TOOL.md:6` | The new `TOOL-cGradedDebt-3` row states `check-arms.py` counts 31 armed; it counts 30 |
| L4 | low | `tools/memory-tree/check-memory-hygiene.sh:1803` | The new FAIL arm is held under `--staged` and announces nothing, unlike the two sibling holds in the same run |

---

### B1 — blocker — the new fail branch is UNARMED, and the arms leg reds on every bar

`tools/memory-tree/check-memory-hygiene.test.sh:1472` (confirms ids 5, 10, 13)

The assertion greps only `curation-debt.txt lists paths that now pass checks 6, 7 and 8 unwaived`.
`check-arms.py`'s `signature()` takes the longest interpolation-free run of the fail message — here
the whole first line up to the trailing colon — and `classify()` arms a branch only when that whole
signature is a substring of one assertion line. The prefix is about 62 characters of it, so the
substring test cannot match.

Reproduced at `c642c23f`:

```
$ python tools/memory-tree/check-arms.py --check
HYGIENE check-arms: tools/memory-tree/check-memory-hygiene.sh:1810 check 6 branch 3 has no POSITIVE
assertion naming its own failure text ('curation-debt.txt lists paths that now pass checks 6, 7 and 8
unwaived, so the row hides nothing and the registry has stopped shrinking — delete the row rather
than re-justifying it') and is not pinned in memory/project/unarmed-branches.txt
```

`--report` prints `branches 31 (floor 27) armed 30 (floor 27)` for this file. The branch is not in
`unarmed-branches.txt` (which holds only three `tools/unattended/unattended.sh` rows). The leg
`harness arms (fail branches armed or pinned)` carries NO guard key at all and is `chunk:
declarations`, so it runs on every bar including the pre-push one — the push is blocked. Spec AC5 is
RED at the commit that claims it.

**Fix.** Widen the grep at `:1472` to the branch's full signature on one line, keeping the U+2014 em
dash byte: `grep -qF 'curation-debt.txt lists paths that now pass checks 6, 7 and 8 unwaived, so the
row hides nothing and the registry has stopped shrinking — delete the row rather than re-justifying
it' <<<"$outsr"`. Shell test files are not subjects of `tools/line-length-limits.txt`, so the length
is fine. The line to paste is exactly the row `check-arms.py --report` prints.

**Left-shift.** The class is already gated, and the gate already caught it — nothing new is owed
except running the bar. The one cheap improvement that would stop this recurring: have
`check-arms.py` print the paste-ready `grep -qF '<signature>'` line beside each unarmed branch, so
quoting a prefix stops being the path of least resistance.

---

### B2 — blocker — the negative assertion matches the new REPORT line, so the self-test is red

`tools/memory-tree/check-memory-hygiene.test.sh:1479` (confirms ids 4, 9, 14)

`fail 6` for the stale rows at `check-memory-hygiene.sh:1810` is immediately followed, inside the
same `if`, by the per-row report loop at `:1812-1816`. The test's block extractor — `cblock()` at
`test.sh:985`, re-spelled inline at `:1478` and `:1479` — only closes a block on a line whose
index-1 prefix is `HYGIENE check`, and `memory-hygiene: …` is not that. `fail()` at
`check-memory-hygiene.sh:218` is the only emitter of that prefix, and in this fixture the stale
`fail 6` is the LAST one (check 23 is silent with a blank `ACCEPTANCE_LEDGER_CUTOFF`, and the
`POP_MISSING` block prints `HYGIENE FAILED`, not `HYGIENE check`). So the window stays open to EOF
and swallows the report lines.

The report line for the earning fixture row contains `memory/builds/tRunBig/RUN.md`, which is
precisely the path the negative assertion at `:1480` greps for. It matches, and the suite prints
`FAIL the stale-ENTRY guard named a row that is still earning its listing` with `st=1`. No fixture
state avoids it: `:1473` requires the stale fail and `:1485` requires the report line, and the script
emits the second immediately after the first. The arm is also unfalsifiable in the other direction —
it cannot distinguish a guard finding from a report, so its positive sibling grades a wider window
than it claims.

Corroborated independently: this worktree carries an uncommitted rewrite of exactly these two
assertions, replacing the inline awk with a `stale_list()` whose extractor closes on
`/^HYGIENE/||/^memory-hygiene:/`. Someone is already fixing this swallow; it is simply not in the
commit under review.

**Fix.** Fix it once in the shared helper rather than in the inline copies: add
`index($0, "memory-hygiene: ") == 1 { g = 0 }` to `cblock()` at `:985-988` — all 15 call sites route
through it and all carry the same leak — then replace the two re-spelled inline awks at `:1478` and
`:1479` with `cblock "$outsr" 6`. The in-flight `stale_list()` fixes the two call sites but leaves
the shared helper leaking for the other thirteen.

**Left-shift.** Ban the re-spelling. A one-line arm in the suite's own meta-checks that greps
`check-memory-hygiene.test.sh` for the `index($0,"HYGIENE check " n " FAILED")==1{g=1}` awk shape
outside `cblock()`'s own definition and fails on any hit. Every inline copy of a block extractor is a
future copy of this bug; there is one correct extractor and it should be the only one.

---

### B3 — blocker — the kit template did not receive the prose its rendered copy did

`tools/memory-tree/HYGIENE.template.md:98`, and `:166` for the second block (confirms ids 11, 15)

Reproduced at `c642c23f`:

```
$ bash tools/memory-tree/kit-dogfood-parity.test.sh
kit-parity: DRIFT — memory/HYGIENE.md does not match tools/memory-tree/HYGIENE.template.md rendered
for this install ('tools/memory-tree')
    99,102c99      (the curation-debt ratchet bullet)
    170,171d166    (check 8's graded-row sentence)
    fix: bash tools/memory-tree/kit-dogfood-parity.test.sh --render
```

`git show c642c23f -- tools/memory-tree/HYGIENE.template.md` shows the only change to the template is
`gov:kit memory-tree@2.69` → `@2.70`. The leg `kit/dogfood doc parity` is `subject: repo`, `chunk:
declarations`, guarded on both `memory/HYGIENE.md` and `tools/memory-tree/` — both in this commit's
file list — so it is not held and reds an ordinary bar.

Two things make this worse than an ordinary parity red. First, the remedy the failure PRINTS is
destructive in this state: `--render` writes TEMPLATE → LIVE (`kit-dogfood-parity.test.sh:30-31`),
so running it as printed silently deletes both new paragraphs. Second, an adopting repo installs a
`HYGIENE.md` that still says the registry only fails "if a listed path is gone", describing a guard
the 2.70 engine no longer has — the kit-versus-dogfood divergence the parity test exists to prevent.

**Fix.** Move both passages into `tools/memory-tree/HYGIENE.template.md` (the registry bullet at
`:98-99`, the check-8 item at `:166`), then run `bash tools/memory-tree/kit-dogfood-parity.test.sh
--render` and commit both files together.

**Left-shift.** A pre-commit fast-leg rule: staging `memory/HYGIENE.md` without
`tools/memory-tree/HYGIENE.template.md` in the same commit is refused. The full parity leg already
catches this at the bar; the cheap version catches it at the keystroke where the hand-edit happens,
and the direction rule ("edit the template, then re-render — never hand-edit the live copy") is
already written in the test's own header.

---

### B4 — blocker — a product source cites a spec that is still SPECCED

`memory/guides/SESSION-KICKOFF.md:253`, spec header at
`memory/builds/cGradedDebt/spec/2026-09-12-spec-TOOL-cGradedDebt-1.md:3` (confirms id 16)

Reproduced at `c642c23f`:

```
$ python tools/drift-audit/drift_report.py --check
drift-report: non_terminal_specs_cited_by_product_source = 3 (pin 2) — this list is shrink-only
  non_terminal_specs_cited_by_product_source             3     30  OVER PIN 2 — gateable
exit 1
```

The third row is the new one: `{'file': 'memory/builds/cGradedDebt/spec/2026-09-12-spec-TOOL-
cGradedDebt-1.md', 'id': 'TOOL-cGradedDebt-1', 'status': 'SPECCED', 'cited_in':
['memory/guides/SESSION-KICKOFF.md']}`. The spec header still reads `**Status:** SPECCED` at the
commit that lands the whole implementation, which is what makes the citation non-terminal. The leg
`drift-audit records` has no guard, so it runs on every bar and blocks the push.

**Fix.** Move the unit-1 spec status off SPECCED in the same commit that lands its code, then re-run
`--check`. Do not raise the pin — the list is declared shrink-only, and raising it would be the
exact move the shrink-only declaration exists to refuse.

**Left-shift.** Already gated, and the gate is correct. The process fix is the one that matters: a
unit's status header moves in the commit that moves its code, which is `BUILD-METHOD.md`'s pass loop
doing its job. No new gate is owed.

---

### M1 — medium — the report denominator is a constant, so it overstates 3 of the 4 live rows

`tools/memory-tree/check-memory-hygiene.sh:1814` (confirms id 12)

The report prints `of the 6 7 8 it is waived from` as a literal, regardless of which checks the path
is actually a population member of. Measured on this repo at `c642c23f` (clean run, gate exit 0):

```
memory-hygiene: curation-debt.txt — memory/builds/aBoundedVerdict/README.md earns check(s) 6 7 of the 6 7 8 it is waived from
memory-hygiene: curation-debt.txt — memory/builds/cBriefedPilot/README.md earns check(s) 6 of the 6 7 8 it is waived from
memory-hygiene: curation-debt.txt — memory/builds/aUnmannedHelm/README.md earns check(s) 7 of the 6 7 8 it is waived from
memory-hygiene: curation-debt.txt — memory/backlog/TOOL.md earns check(s) 6 7 of the 6 7 8 it is waived from
```

Check 8's population is built at `:763` from `$M/backlog/[^/]+\.md` plus
`$M/builds/[^/]+/STATUS\.md`, so the three build READMEs are structurally outside it and their
waiver buys nothing there. `aBoundedVerdict/README.md` reads as one check over-wide when its waiver
is exactly as wide as its fault; `aUnmannedHelm/README.md` reads as two over-wide when it is one. A
`RUN.md` is outside check 7 as well (`ex7` at `:703`), so the self-test's own subject prints `earns
check(s) 6 of the 6 7 8` for a row with exactly one applicable check.

This is not cosmetic. S4 and AC3 exist to make an over-wide waiver VISIBLE, the registry header this
commit adds tells readers that where the derived report and the hand-written blast-radius notes
disagree "the run is right", and the hand-written note for `aUnmannedHelm` is the one that is
correct. The spec's own §4 Rollout table writes `n/a` in the check-8 column for exactly these three
rows; the emission does not carry that distinction.

**Fix.** Report the applicable set instead of the constant. `sel6`, `sel7` and `files8` are all still
in scope at `:1812` — either test membership in the report loop, or record the applicable set
alongside `DEBT_EARNED` in the same one-line filters that already build those three lists, then print
`earns check(s) X of the <applicable> it is waived from`. A row whose earned set equals its
applicable set then reads as exactly-wide, which is the signal the unit is selling.

**Left-shift.** One self-test arm over a fixture `RUN.md` — applicable to check 6 alone — asserting
the emitted line reads `earns check(s) 6 of the 6 `. Today that arm would fail; once the denominator
is derived, it pins it. The current arms only ever assert the EARNED half, which is why the
denominator shipped wrong.

---

### L1 — low — the stale-entry guard reads the index while "earning" is decided against the worktree

`tools/memory-tree/check-memory-hygiene.sh:1808` (confirms id 1)

`TRACKED_SET` is filled from `git ls-files` at `:1785`, and the stale-entry guard skips a listed path
only when it is absent from that set. But `DEBT_EARNED` is filled only from files that survive
`[ -f "$f" ]` — `index_set` ends with `while IFS= read -r f; do [ -f "$f" ] && echo "$f"; done` at
`:612`, and `files8` carries the same filter. So a path that is still in the index but gone from the
working tree is in the stale-entry population and records nothing, and reads as stale.

Reproduced at `c642c23f`: `rm memory/builds/aUnmannedHelm/README.md` without `git rm` makes the gate
print `HYGIENE check 6 FAILED — curation-debt.txt lists paths that now pass checks 6, 7 and 8
unwaived … delete the row rather than re-justifying it: memory/builds/aUnmannedHelm/README.md`, while
the sibling stale-LINE guard stays silent because the path is still tracked. A developer who follows
the printed remedy drains a waiver row that is still load-bearing — that path earns check 7 in the
clean run — and checks 6, 7 and 8 silently widen over the file once it is restored.

Severity is low because the tree is already inconsistent in that state and the run is loud for other
reasons in this repro. Neither of those other signals names the registry, and neither is guaranteed
for a file with no inbound link.

**Fix.** One existence test beside the `TRACKED_SET` test at `:1808`: `[ -f "$p" ] || continue`.
Absence is the sibling guard's question in spirit, and a path that is in no population never had a
chance to earn anything.

**Left-shift.** A self-test arm that deletes a listed fixture file from the worktree without
`git rm` and asserts the stale-ENTRY guard stays silent while the stale-LINE guard also stays silent.
That arm is the only thing that distinguishes "the row hides nothing" from "the file is not there to
hide anything", which is the whole distinction this guard rests on.

---

### L2 — low — AC4 pins 499 and the landing run prints 500

`memory/builds/cGradedDebt/spec/2026-09-12-spec-TOOL-cGradedDebt-1.md:171` (confirms id 3)

Measured at `c642c23f`: `memory-hygiene: check 8 graded 500 backlog row(s) across 4 shard(s)`. The
build itself added the `TOOL-cGradedDebt-3` row to `memory/backlog/TOOL.md`, which is the 500th; the
commit's diff to that file is 7 insertions / 6 deletions, net one row. AC4 reads "When that same
run's stdout is read … the number is 499", and "that same run" is AC2's run at the landing commit,
not the base. Its `figure: DERIVED` line does name `09a22d2b` as the corpus the 499 comes from, which
is the only reason this is low rather than medium — a careful reader can reconstruct the intent.

A literal grader cannot. Whoever writes the check-23 acceptance ledger — which requires every AC of a
CLOSED Tier-2 unit to be evidenced — reads this as RED on a unit that is correct. This is the
number-typed-beside-a-population-it-does-not-derive class, inside the criterion written to observe it.

**Fix.** Drop the literal and keep the `figure: DERIVED` line, or restate as "500 at the landing
commit, 499 at base `09a22d2b` — the build adds one backlog row".

**Left-shift.** A hygiene arm over spec acceptance criteria: a criterion carrying a `figure:
DERIVED` line may not also carry a bare integer in its assertion sentence. It is a narrow rule and it
is exactly the shape both L2 and L3 take.

---

### L3 — low — the backlog row that justifies the floor states a figure that is false at the commit shipping it

`memory/backlog/TOOL.md:6` (confirms id 17)

The new `TOOL-cGradedDebt-3` row asserts `check-arms.py --report` "counts 31 branches and 31 armed".
Measured at `c642c23f`, for `tools/memory-tree/check-memory-hygiene.sh`: `branches 31 (floor 27)
armed 30 (floor 27)`. The row is the record that justifies leaving `ARMS_FLOORS` at `27:27`, and its
measured premise is false — this is also why B1 went unnoticed. A future session reading this row
believes the arms gate is green and the only open question is the floor. Nothing dates or qualifies
the figure (it says only "Measured at TOOL-cGradedDebt-1", which is this commit), so no
pinned-versus-derived convention covers it.

**Fix.** After arming the branch (B1), re-run `--report` and restate the measured pair, or drop the
figure and point at the command. The row's advice to raise the floor on a quiet tree is the only part
that cannot be derived, and it is the part worth keeping.

**Left-shift.** Same arm as L2, applied to backlog rows: a row quoting a tool's output names the
command rather than the number. Realistically this one is a review check, not a gate — the class is
"one fact in one place" and the project already names it.

---

### L4 — low — a hold that announces nothing

`tools/memory-tree/check-memory-hygiene.sh:1803` (confirms id 19)

The block is `if [ "$STAGED" = 0 ] && [ -n "$DEBT" ]` and emits nothing on the held path. Measured:
`bash tools/memory-tree/check-memory-hygiene.sh --staged` on this tree prints exactly three lines —
the `PROJECT_REGISTRY_EXTRA` line, the §3 edge-JOINS hold at `:1646`, and `check 23 HELD under
--staged` at `:1866` — and says nothing at all about the registry. Two sibling holds in the same run
announce themselves; this new one does not.

`.githooks/pre-commit:48-50` runs exactly this mode whenever anything under `memory/**` is staged, so
a pre-commit run is indistinguishable from one that graded the registry and found every row earning
its listing. That is §7's "a skip must announce itself", and it is the same could-not-fail shape this
unit exists to remove one level up. The verdict itself is correct — nothing fires wrongly or is
suppressed wrongly under `--staged`.

**Fix.** One line inside the held path, beside the existing hold announcements: `memory-hygiene: the
curation-debt stale-ENTRY guard and its per-row report are HELD under --staged — the selection is the
staged set, so an unstaged listed file would record nothing and read as stale. The push-boundary run
is where the registry binds.`

**Left-shift.** An arm asserting that a `--staged` run emits one `HELD under --staged` line for every
block guarded on `[ "$STAGED" = 0 ]` in the script. The count is derivable by grep from the source, so
the arm cannot rot as holds are added — which is the property that makes it worth writing rather than
listing today's three holds in a test.

---

## Hunted and found clean

All four lenses and all five skeptic batches returned, so a zero here is evidence rather than a gap.

**1. `split_debt` path extraction (priority 1) — clean, and safe by construction.**
`_p=${_l%%[ :]*}` at `:243`. A path containing a space or colon extracts SHORT, matches no registry
key, and therefore stays in `_UNWAIVED` — the finding fails loudly rather than being silently waived.
Same for any continuation line that does not lead with a path. No mis-key that fails OPEN was found in
any of the three finding formats, and the direction is structural rather than a property of a corpus
that happens to hold no such path. The source comment at `:239-242` says exactly this and it is
correct.

**2. Subshell semantics (priority 2) — clean.** All three `split_debt` calls (`:670`, `:747`, `:800`)
are at top level in the main shell, so no `DEBT_EARNED` write is lost. The reads at `:1809` and
`:1813` sit inside `$( )` and pipeline subshells, which inherit a populated copy — reads from a
subshell are fine and only writes would be discarded. The hazard is documented at `:229-231`.

**3. The `#rows` sentinel (priority 4) — clean.** `#rows <rows> <shards>` is emitted by the awk END
block at `:795`, summed across xargs invocations at `:796-797`, and stripped at `:798` before `bad8`
is read. No real check-8 finding can lead with that prefix: findings lead with a path, and `#` is not
a legal leading character for a path in the `$M/` populations. The reported figure matched the graded
population on a clean run — `check 8 graded 500 backlog row(s) across 4 shard(s)`, four shards being
the whole of `memory/backlog/`.

**4. `--staged` behaviour (priority 5) — correct except for the announcement.** The hold is complete
and correctly placed: both the stale arm and the report loop sit inside the one `STAGED = 0` guard,
and nothing else in the new code changes what `--staged` does. The gap is L4 and only L4.

**5. Verdict changes elsewhere (priority 6) — none found.** `pop_guard 6`'s count, check 7's `ex7`
exclusion and check 8's `pop_guard` all read populations built before `split_debt` runs, so removing
the `in_debt` filters widened the FINDING set without moving any population guard. The clean run over
this repo exits 0 with the four expected report lines and no stale row, which is AC2 and AC3 holding.
Unit 2's four `WITHDRAWN` → `WONTDO` rewrites and its two pipe-quoting rewordings are in the check-8
vocabulary at `:772-773` and produce no findings.

**6. Unit 2 (Tier-1) — clean.** Additive, verified by the same green check 8, no further comment.

## What a fixed commit owes

`bash tools/memory-tree/kit-dogfood-parity.test.sh` · `python tools/memory-tree/check-arms.py
--check` · `python tools/drift-audit/drift_report.py --check` · `GATE_SELFTESTS=1 bash
tools/run-gates/run-gates.sh` for the `memory-hygiene self-test` leg, which this kit work's
Definition of Done owes and which B2 currently reds.
