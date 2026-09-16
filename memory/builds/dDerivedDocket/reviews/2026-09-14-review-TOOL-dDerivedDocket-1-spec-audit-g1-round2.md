**Serves:** spec-audit TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28

# dDerivedDocket — spec audit of topic group G1, kit self-protection, round 2

*Node `d`, 2026-09-14. The second Tier-2 adversarial pass over the eight G1 specs: the suite
baseline, the in-place landing, the landing path, HELD, auto-resume, the derived terminal, the gate
wall and the process ledger. This round was aimed at the text the round-1 fold introduced, using
each spec's §9 rev-2 line as the index, and at whether each round-1 fix actually holds. Four primed
finder lenses were launched and ONE DIED. A skeptic stage prompted to REFUTE each finding ran in five
batches, and all five returned. Then came this synthesis. The sources were the ratified design
record `memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the
owner mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the spec brief's roster and edge tables, and the round-1 record
`memory/builds/dDerivedDocket/reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md`.
Sibling specs outside G1 were read wherever an edge or an interface named them. Every blocker and
every high below was re-checked against source at `abac6d59` before it was written down, and the
sites read are named in each entry.*

**Round: 2.** Range at base `abac6d59`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-1.md@e8b51404cebc1e9b77ecc512f51a3568b4a4841e`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-2.md@9a9f045b2f57f7430c94be78f16d2d4333b3bbeb`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-3.md@f4d2cb5049d73be7771587b888309b1e2bbab085`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-4.md@d18f9dbe289eb7ad33c9a5f2d27ae7bc7052079d`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-5.md@349ccde6146f932bbca97a8cc528bbe6f7e3e295`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-22.md@5842b43cc162bbbc82830e3411441bf22d211916`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-27.md@d1b96509f9b54d980b03250c2dc82728bce19f63`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-28.md@2ec917f842f656db96b75615280fe87711214ae8`

## Verdict: BLOCKED

Two blockers stand, one finding id each. Both sit in unit 22 §2 S4, the rotation that rev-2 wrote
to fix round-1 B2, so **round-1 B2's fix does not hold**. B1: the rotation cannot be built from
BASE's primitives into a correct committed archive. BASE derives the archive name before any write,
and `GIT mv -f` carries the old staged blob. AC6 reads only the working file, so it cannot see
either failure. B2: a rotated in-place archive names a single-parent close commit as its witness.
Unit 19's terminal rule then grades `BASE..C` with no exclusion, and an ordinary owner `may:` grant
on the default branch during the run's window reds check 19 on a frozen archive for good.

One HIGH defect stands, carried by two finding ids. The criterion unit 1 hands to every self-test
unit, "no NEW FAIL", reads a suite that aborted before its first FAIL line as clean. That leaves
round-1 M12's fix stopping at unit 1's own exit code. There are also 13 MEDIUM defects (17 ids) and
8 LOW defects (10 ids).

**This run is INCOMPLETE: one of four lenses died.** Every count on this page is a floor. A HIGH or
BLOCKER may exist in the dead lens's scope and never have reached a skeptic.

Convergence under `memory/guides/BUILD-METHOD.md` M4 reads two ways. By finding id, the blocker count
fell from 4 to 2, which is strictly smaller, so the loop re-arms after the fold. By distinct defect,
it held at 2 and 2, which would end the loop. Either way the next act is the same, because M4
disposes a standing blocker in a document the review read by FOLD. The drop from 4 is also
confounded by the dead lens: a smaller count from a smaller review is not evidence of convergence.
The B2 fold crosses into unit 19 §4, which topic group G3 audits, so it should be folded in both
specs at once. The H1 fold needs one decision first, stated in its entry: whether an R-side DEAD
PROBE fails unit 1's exit.

## Run integrity

- Lenses: 3 of 4 returned, **1 DIED**.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

This run is not complete. The dead lens's findings never reached a skeptic, so the confirmed set is
INCOMPLETE. This synthesis was not told which lens died, so no lens area or subject can be called
covered. Every zero on this page therefore means "not found by three of four lenses", not "absent".
That includes each "no confirmed finding" in the round-1 table below. The pipeline's duplicate
count of 0 comes from its own exact-match dedupe. On reading, six groups each describe one defect
reported by two or three lenses: 2 and 24, 6 and 29, 7 and 35, 9 with 25 and 41, 18 and 37, and 20
and 33, where 33 is the ledger half of 20. Each group is folded into one entry below, and every count
on this page stays per finding id.

## Review shape

Raw 49, confirmed 31, refuted 18, unverified 0, precision 0.63. The 31 confirmed ids collapse to 24
distinct defects.

| Severity | Finding ids | Distinct defects |
|---|---:|---:|
| BLOCKER | 2 | 2 |
| HIGH | 2 | 1 |
| MEDIUM | 17 | 13 |
| LOW | 10 | 8 |

Precision rose from round 1's 0.56 to 0.63, on a round with one lens fewer. Two classes dominate
the confirmed set.

- **`memory/gotchas/fold-text-is-unreviewed-surface.md`.** 29 of the 31 ids, and 22 of the 24
  defects, sit in a section some spec's §9 rev-2 line names, or in the half of a round-1 fix that line
  left standing. The two exceptions are M8 (26), a contradiction between unit 5 and unit 24, and L8
  (47), which is rev-1 text in unit 1.
- **`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`**, the round-1 dominant
  class. It returns in the fold's own new criteria: 13 ids and 10 defects (M7, M10, M11, M12, M13,
  L2, L4, L5, L6, L7). H1 is the same class one level up, since it is a consumer's criterion that
  cannot fail.

## Round-1 fixes: what this round found against them

The round-1 records map onto round-2 entries as follows. "No confirmed finding" means only that the
three surviving lenses confirmed nothing against the fix. It does not certify the fix, because one
lens died.

| Round 1 | Spec | Round-2 reading | Round-2 entries |
|---|---|---|---|
| B1 | 22 | no confirmed finding | none |
| B2 | 22 | does not hold | B1, B2 |
| H1 | 27, 4 | no confirmed finding against the backstop term | none |
| H2 | 4 | holds on the fresh working-phase row only | M5, M7 |
| H3 | 4 | no confirmed finding | none |
| H4 | 22 | no confirmed finding | none |
| H5, H6 | 1, 22 | no confirmed finding | none |
| M1 | 3, 4 | partial: the route and the checkpoint lag the verb | L3, L4 |
| M2 | 27 | the fallback clause is unobserved | L6 |
| M6 | 4 | the idempotent re-preflight now refreshes a lease it does not hold | M6 |
| M9 | 4 | does not hold for five of the table's nine rows | M1 |
| M11 | 1 | the one version move is observed by no criterion | M11 |
| M12 | 1 | holds at unit 1's exit, not at any consumer | H1 |
| M14 | 5 | the probe extension is observed by a criterion that cannot fail | M12 |
| M22 | 3 | the `LANDER_MODE` half holds; the kit-roots half is vacuous | M13 |
| M30 | 28 | `--hold` reaping is still unobserved | L5 |
| L1 | 22, 28, 4 | does not hold: the symptom moves to the absent-lease row | M3, L5 |
| L3 | 2, 3 | holds for `--carry` only | L1, L2 |
| G3 H7, as S17 | 22 | wrong under primary, and silent on rotated records | M4, B2 |

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---|---|
| 40 | BLOCKER | B1 | 22 | §2 S4; §4 The readers, `archive_name_of` row; §6 AC6 |
| 1 | BLOCKER | B2 | 22 | §2 S4, S17; §6 AC6; against unit 19 §4 The cross-run arm |
| 2 | HIGH | H1 | 1 | §1 Goal; §2 S8; §3 Edges |
| 24 | HIGH | H1 | 1 | §1 Goal; §3 Edges; §2 S8 against S3 and S5 |
| 4 | MEDIUM | M1 | 4 | §4 `derived_phase()`; §2 S8; §6 AC8 |
| 5 | MEDIUM | M2 | 4 | §4 The lease, absent row and the Skill's Resume rule; §2 S7; §6 AC19; §5 |
| 6 | MEDIUM | M3 | 22 | §2 S16; §6 AC15; against unit 4 §2 S7 |
| 29 | MEDIUM | M3 | 22 | §2 S16; §6 AC15; against unit 4 §2 S7 and §4 The lease |
| 7 | MEDIUM | M4 | 22 | §2 S17; §6 AC17 |
| 35 | MEDIUM | M4 | 22 | §2 S17; against unit 19 §4 The cross-run arm |
| 27 | MEDIUM | M5 | 4 | §2 S5; §4 The lease, take-over rows |
| 44 | MEDIUM | M6 | 4 | §2 S6, S9; §4 The lease; §6 AC10 |
| 13 | MEDIUM | M7 | 4 | §2 S6; §4 The lease, matching-id row; §8 F6; §6 AC17 |
| 26 | MEDIUM | M8 | 5 | §2 S5; §4 Data model; §6 AC6; against unit 24 §2 S10 |
| 43 | MEDIUM | M9 | 3 | §4 `--close` under `in-place`, step 4; §4 What an incomplete landing does |
| 12 | MEDIUM | M10 | 27 | §2 S5; §6 AC13 |
| 3 | MEDIUM | M11 | 1 | §2 S9 |
| 9 | MEDIUM | M12 | 5 | §6 AC15; §2 S11 |
| 25 | MEDIUM | M12 | 5 | §6 AC15; §2 S11; §4 Rollout |
| 41 | MEDIUM | M12 | 5 | §2 S11; §6 AC15 |
| 11 | MEDIUM | M13 | 3 | §6 AC13; §2 S1 |
| 18 | LOW | L1 | 3 | §2 S3, S2; §4 `gates-green` |
| 37 | LOW | L1 | 3 | §2 S3; §4 `gates-green`; against unit 2 §2 S7, S10 |
| 17 | LOW | L2 | 2 | §2 S7; §6 AC13 |
| 36 | LOW | L3 | 3 | §4 What an incomplete landing does; §2 S6; §6 AC8; against unit 4 §2 S2, S3 |
| 14 | LOW | L4 | 4 | §4 Codes and conditions; §4 The checkpoint; §6 AC15 |
| 20 | LOW | L5 | 28 | §2 S3; §4 Pruning and concurrency; §6 |
| 33 | LOW | L5 | 28 | §4 Pruning and concurrency; against §2 and §6 |
| 21 | LOW | L6 | 27 | §2 S7; §6 AC8 |
| 22 | LOW | L7 | 22 | §2 S9; §6 AC6 |
| 47 | LOW | L8 | 1 | §2 S8; §6 AC7 |

Every spec path below is `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-<n>.md`,
named by its unit number. Every `unattended.sh` line number is at `abac6d59`.

## Blockers

### B1 — the rev-2 rotation cannot produce a committed LANDED archive from BASE's primitives (40)

**Where.** Unit 22 §2 S4; §4 "The readers", the `archive_name_of` row; §6 AC6. S12 is involved too.
It amends protocol §2's rotation paragraph but leaves standing that paragraph's sentence that
`git mv` puts both sides in the index in one operation (`tools/unattended/PROTOCOL.template.md:161`).
That sentence becomes false once the record is edited before the move.

**Defect.** S4 writes `phase: LANDED`, `witness` and `landed-derived` "in one write", then retires the
record "to the name `archive_name_of` derives from those bytes". It also refuses "before any write".
The readers-table row says "S4 writes LANDED before the name is derived". Neither half of that model
is true at BASE, and I re-read both halves in `tools/unattended/unattended.sh`.

- The name is derived in preflight's PRECONDITION half. `archive_name_of` runs at `:2569`, inside
  the `is_terminal` test at `:2568`, and both fail-28 collision tests follow at `:2577-2584`. All of
  this runs on the unedited LANDING bytes and before the write gate at `:2642`.
  `archive_name_of` (`:1602-1607`) builds the name from `fact phase` and
  `GIT hash-object` of the working file.
- The rename is `GIT mv -f` (`:2658`). It moves the index entry together with its old staged blob.
  `stage_or_fail` at `:2764` stages only the fresh `RUN.md`.

The skeptic reproduced the second point in a scratch repo. After a `set_fact`-style edit and
`git mv -f`, `git show :<archive>` reads `phase: LANDING`, the working copy reads LANDED, and status
is `RM`.

**Impact.** The two natural builds fail differently.

- A builder who keeps BASE's order names the archive `RUN.LANDING.<blob8>.md`, contradicting S4 and
  KF15's `RUN.LANDED.` name.
- A builder who moves only the name derivation leaves the LANDED edit unstaged. If the agent then
  commits the staged set, the archive is committed saying LANDING. That is round-1 B2's permanent
  check-4 red, seen on every clone but this one. Here the worktree is left dirty.

AC6 cannot see either outcome. The leg's `phase_of` reads working files
(`tools/unattended/check-unattended.sh:1063-1067`), and AC6 asserts nothing about the index or
porcelain.

**Fix.** State the order in S4, in three steps.

1. In the precondition half, apply the three fact edits to a scratch copy. Derive the name from that
   copy and run both fail-28 tests against it, all before the write gate.
2. After the gate, write the facts to `RUN.md` and stage it, then `GIT mv -f`. Staging the archive
   after the move works equally well.
3. Assert that the archive's staged blob is the one its name's `blob8` encodes.

Correct the readers-table row to "the name derives from the post-write bytes, computed before the
gate". S12 amends the protocol sentence to state the staging precondition. Extend AC6 to read
`git show :<archive>` for `phase: LANDED`, match its `blob8`, and assert no unstaged change to the
archive once preflight has staged.

**Left-shift.** Round 1's class item 2 asked for one helper that every archive-producing arm calls.
That helper must grade the INDEX copy and `git status --porcelain`, never the working file. Stage the
break by removing the pre-move stage and confirm RED. The nearest class record is
`memory/gotchas/spec-names-code-its-base-lacks.md`: a spec that states its base's mechanics from a
model rather than from the code.

### B2 — a rotated in-place archive reds check 19 for good after any owner grant in its window (1)

**Where.** Unit 22 §2 S4 and S17; §6 AC6; against unit 19 §4 "The cross-run arm", its terminal-record
row and §8 F4.

**Defect.** Under in-place, unit 3 S5 commits the close ON TOP of the prepared merge. The landing
commit C is therefore single-parent, and its parent T is the prepared merge, whose first parent is
the advertised default tip. S4 writes `witness: <C>` and `phase: LANDED` into the rotated archive.
Check 19 then grades the archive by unit 19's terminal row: "endpoint its recorded witness,
exclusion the witness's first parent when the witness is a two-parent commit". C has one parent,
so no exclusion applies. Unit 19 justifies that with "the local arm's witness is the run branch's
own tip, whose history since BASE is the run's". That is false under in-place, because `BASE..C`
passes through T into every default-branch commit landed since BASE. S17 does not rescue the case:
it covers a LANDING record deriving LANDED, and a rotated record says LANDED. AC6 runs only checks 4
and 15 over the rotated record, and AC17 grades only an unrotated LANDING record.

**Impact.** An owner commit on the default branch that adds `may:` to any other build's README
between BASE and the landing reds check 19 on the frozen archive for good. That is the hand-typed
grant channel ruling D12-j keeps open. Check 19 is on the repo-subject `unattended kit gate` leg, so
the red lands on every default bar. Unit 19 §8 F4 names this exact outcome as the reason for its
range ("the archived record reds the bar for ever"), and unit 19 AC6's Red-when repeats it. The trigger is
ordinary. Owner grants are how runs are authorized, and gov runs several builds at once.

**Fix.** Give a rotated record carrying `landed-derived` the same range as a derived-LANDED LANDING
record. S17's endpoint is the landing commit C. Its exclusion is the first parent of the prepared
merge C^1, verified as the lander's prepared merge, as M4's fix requires. Either S17 names the
population and unit 19's terminal row routes a record carrying `landed-derived` to S17 before its
two-parent test, or S4 records the exclusion as a third field of `landed-derived` and check 19 reads
it. Fold unit 19 §4 in the same change, because G3 audits that spec.

Extend AC6, or add an AC17 arm. The fixture's default branch gains an owner commit adding `may:` to
another build's README after BASE. The record is rotated through `--preflight`, and the WHOLE leg,
check 19 included, runs over the rotated tree and passes. A `may:` commit made by the run itself in
the same fixture still reds. Stage it RED under unit 19's unamended terminal row.

**Left-shift.** The archive helper from B1 runs the whole leg, not a named subset, over a fixture
whose default branch moved after BASE. The class is
`memory/gotchas/amendment-leaves-its-other-half-standing.md`. S4 changed what a rotated archive
says, and the reader that keys on what an archive says, unit 19's terminal row, kept its old premise.

## High

### H1 — the criterion every self-test unit inherits reads an aborted suite as clean (2, 24)

**Where.** Unit 1 §1 Goal, §2 S8 and §3 Edges, which carry every hands-off payload; against unit 1 S3
and S5.

**Defect.** Round-1 M12's fold made DEAD PROBE and an L-side OVER BUDGET separate verdicts that exit
1 (S3, S5, AC2, AC9, AC10). The criterion unit 1 HANDS OFF is still only "no NEW FAIL". S8 writes it
into `tools/unattended/kit.toml` and both runner headers as "no NEW FAIL against the build's BASE,
and every INHERITED FAIL named by a filed backlog row", with no DEAD term. A DEAD PROBE block prints
no NEW set, so its summary reads `NEW 0 · … · DEAD 1`.

Six consumer criteria read only "reports no NEW failure": unit 3 AC11, unit 4 AC12, unit 5 AC14,
unit 24 AC12, unit 27 AC10 and unit 28 AC10. Each Red-when names an arm that fails, never a suite
that did not run. Unit 2 AC9 and unit 22 AC13 also require named arms to pass, so they are guarded
only for the arms they name.

**Impact.** Take a unit whose own change aborts an unattended suite before its first FAIL line. That
unit meets its Definition of Done. This is the `set -u` abort shape TOOL-aHoistedPass-36 records,
never run to completion and with nothing saying so, and it is the abort design U16's acceptance 2
names as the break. The unattended suites are off the bar, so this once-per-unit run is their only
reader. Neither S5's exit status nor the summary's DEAD count is read by any consumer. S8's second
term, the backlog row per INHERITED FAIL, is checked by no consumer AC either. AC10's Red-when ("a
runner REDS on breach … in the mode this build's self-test units verify with") is voided the same
way, because the consumers read NEW and not the exit.

**Fix.** Define the handed-off criterion ONCE in unit 1, as the runner's verdict and not one field
of it: under `--attribute <BASE>`, NEW 0, no DEAD PROBE at L, and no OVER BUDGET at L. An R-side DEAD
PROBE is inherited and, like an INHERITED FAIL, must be named by a filed backlog row. State it in S8's
compensating-check text, in all four places (see L8). Restate each consumer's final AC as that
criterion, and drop "no NEW failure" from each. Either give the backlog-row term a consumer criterion
or drop it from S8. Extend AC7 so the stated wording must name DEAD PROBE and OVER BUDGET, and
Red-when the wording names NEW alone.

**Decide this first; I read it at synthesis and it was not put to a skeptic.** S5 exits 1 on ANY
DEAD PROBE, the R side included. If some unattended suite is DEAD at BASE, every consumer's
attributed run exits 1 for a cause that consumer did not create. So "exit 0" cannot be the handed-off
criterion unless S5 first exits 0 on an R-only DEAD PROBE and reports it like an inherited failure.
The alternative is a criterion that reads the summary fields rather than the exit.

**Left-shift.** Add a join over the edge lines the build-edge renderer already parses. Every AC in a
spec that declares consumes-from `TOOL-dDerivedDocket-1` must carry the producer's named criterion
token. `tools/check-spec-tokens.py` can print a consumer AC saying "no NEW failure" without that
token as a near-miss. The class is `memory/gotchas/swallowed-delegate-reads-as-clean.md`: the
consumer reads a delegate that never ran as a clean population.

## Medium

### M1 — the structural arm exempts whole functions, so five rows' direct reads pass it (4)

**Where.** Unit 4 §4 `derived_phase()`; §2 S8; §6 AC8.

**Defect.** §4 defines a WRITER as "a function containing a `set_fact <file> phase` site" and exempts
writers from the direct-read red. At BASE, `verb_phase` (`:2233`), `verb_landed` (`:2459`) and
`verb_preflight` (`:2749`) are writers, and `verb_resume` becomes one once S5 returns it to the
held-from phase. The rotation test's direct `is_terminal "$(fact "$rel" phase)"` at `:2568` sits in
`verb_preflight`. Its row says derived, and unit 22 S4 depends on it being derived. Yet it passes the
arm unchanged. AC8's second case expects a red for `verb_resume` calling `recorded_phase`, while §4
reds that only "from a function the table does not list", and `verb_resume` is listed. The skeptic
judged that half weaker, because the recorded-rows allow-list sentence can be read to resolve it.

**Impact.** Five of the nine table rows sit in writer functions, where a direct read can never red.
With the behavioural suites held off the bar, this arm is the on-bar guard for the classification.

**Fix.** Exempt the `set_fact <file> phase` LINE, not the function around it. Every other
`fact … phase` read outside the two readers reds unless the table lists that site, and a
`recorded_phase` call reds unless its function's row says recorded. Add an AC8 driver copy whose
`verb_preflight` rotation test reads the fact directly.

**Left-shift.** Before wiring, run the predicate over BASE's driver and print hits and near-misses, as
charter §7 requires. `:2568` must appear as a hit.

### M2 — the holder of a leaseless live record is refused, then told to take over (5)

**Where.** Unit 4 §4 "The lease", the `working phase · absent` row and the Skill's Resume rule; §2 S7;
§6 AC19; §5 migration.

**Defect.** Every run in flight when unit 4 lands has no lease, and this build's own run is one of
them. `memory/builds/dDerivedDocket/RUN.md` records a working phase with keepalive `00c7d786`, and
no lease directory exists under the git common dir. S6
lets only `--preflight` and a take-over TAKE a lease. The absent row refuses any `--resume` inside the
bound without telling the holder from anyone else, and a run that commits continually is always
inside the bound. The rewritten Resume rule then sends a session that sees no `LEASE` line down the
take-over path: reap the recorded job, which is its own keepalive, reschedule, and resume with the new
id. That resume is refused on commit age again, and `--preflight` refuses the new id (S9).

**Impact.** The slug stalls until the bound passes, which is 7200 s for a record that pins no backstop.
The absent row's refusal names the commit age, not `--keepalive-id`, and prints no status block. That
contradicts the fallback in the parked M7 decision in the same `RUN.md`, which relies on the
refusal printing the phase and witness. §5's claim that existing records read "exactly as before"
does not hold for the lease.

**Fix.** Add a matrix row. A working-phase record with no lease, resumed with the id its `keepalive`
fact records, TAKES the lease as an orientation. The Resume rule checks the `keepalive` fact when no
`LEASE` line exists. The absent row's refusal prints the status block and names `--keepalive-id`. Add
an AC: a leaseless working fixture resumed with its recorded id inside the bound takes the lease and
exits 0.

**Left-shift.** This is class item 4 below, a reacher column on the lease matrix. The holder of a
pre-lease record is the first reacher of the absent row, and the matrix never considered it.

### M3 — removing the lease at in-place `--landed` moves the symptom to the absent-lease row (6, 29)

**Where.** Unit 22 §2 S16 and §6 AC15; against unit 4 §2 S7 and its absent-lease row.

**Defect.** Round-1 L1's fix removes the lease when in-place `--landed` succeeds. A landed record
still reads LANDING whenever `derived_phase` cannot see the tip: the remote does not answer, or this
clone lacks the advertised tip's object (unit 22 §4 "Where the tip comes from"). The second case is
ordinary on an unfetched clone after another node lands. Unit 22 AC5 itself treats such a LANDING
record like a working-phase one. Unit 4's new absent-lease row then derives `presumed-stopped` once
the newest build-folder commit is older than the bound, and offers a take-over.

**Impact.** `--status` prints `presumed-stopped` for a slug that has already landed, and `--resume`
offers to take it over. That is exactly the outcome AC15's Red-when says the removal prevents. The
take-over then refuses later, at re-authorization, on the wrong grounds. AC15 checks only that the
lease file is gone, and a missing lease is the input that produces the break.

**Fix.** Exempt from both `presumed-stopped` rows any LANDING record for which `landing_commit_of`
returns a commit, and print the derivation's reason instead. That is the alternative round-1 L1
named. Alternatively, in-place `--landed` rewrites the lease as `released <iso> landed`, which a
matrix row reads as nothing to resume. Re-point AC15: after in-place `--landed`, make the remote
unreachable, age the fixture's commits past the bound, and assert `--status` prints no
`presumed-stopped`.

**Left-shift.** A fixed symptom is tested at the READER that produced it, never at the fixing verb's
output. AC15's Red-when names the reader, so AC15 has to run it.

### M4 — S17's exclusion is, under primary, the one unit 17 rejected (7, 35)

**Where.** Unit 22 §2 S17 and §6 AC17; against unit 19 §4 "The cross-run arm" and unit 17 §8 F5.

**Defect.** S17's exclusion is "the first parent of the first two-parent commit on that commit's
first-parent chain (unit 2's prepared merge)", and it is stated for every derived-LANDED record. Under
primary there is no prepared merge, and the landing commit sits on the run branch. On a run branch
that plainly merged the default branch after BASE, which is a real pattern (`29a0d0ea`), the first
two-parent commit is that reconcile, and its first parent is a run commit.

**Impact.** The run's commits before the reconcile fall out of check 19's range, so a `may:` line the
run added there goes ungraded. That fail-open half is not in unit 19's stated residual, which covers
only the opposite direction. The default-branch commits the reconcile brought in come into range, so
an owner grant among them reds. Both effects hold for a primary record while it derives LANDED, from
the push until `--landed` records the terminal, after which S17 no longer applies to it. That window
is why this stays MEDIUM rather than joining B2. A primary record rotated without `--landed` leaves
S17's reach and falls to unit 19's terminal row, which is B2's population, and B2's fix covers it.
AC17 runs only an in-place fixture.

**Fix.** Restrict S17 to a landing commit whose parent is the lander's prepared merge, recognized by
the lander's own predicate or its `merge: <slug> — land onto` subject. Otherwise use unit 17's own
exclusion. Add a primary AC17 arm over a branch with a plain mid-run reconcile. Fold this together
with B2's fix, which extends the same S17 to rotated records.

**Left-shift.** The class is item 3 below. A rule written for one mode is stated without a mode, and
only that mode's fixture runs.

### M5 — a take-over with no `--keepalive-id` takes a lease naming no keepalive, and the slug wedges (27)

**Where.** Unit 4 §2 S5; §4 "The lease", the take-over rows.

**Defect.** S5 orders "taking the lease" before "accepting a new `--keepalive-id`", and it requires
every refusal to come before the lease is taken. So no take-over row refuses a missing id. Only the
fresh working-phase row refuses a no-id resume, which is round-1 H2's fold. Two real no-id callers
reach the take-over rows. One is `memory/guides/BUILD-METHOD.md` M7's regrounding step,
`unattended.sh --resume <slug>`. The other is unit 5's scheduled restart `--resume <slug>
--scheduled <held-at>`, as its S6, its filed prompt and AC7 and AC8 spell it. AC8 needs that
take-over to complete.

**Impact.** The lease is written `taken <iso> keepalive <blank>`. The session then schedules its own
keepalive and ticks `--resume --keepalive-id <own>`. That call meets the fresh different-id row and
is refused, and `--replaces` cannot name a blank id. Nobody can drive the slug until the lease goes
stale, which is hours under the backstop bound. That is `memory/gotchas/two-guards-one-question-two-answers.md`:
two rows that jointly leave no legal move. The parked M7 decision in `RUN.md` records option (b) as
"fully functional". It holds only on the fresh row.

**Fix.** Move the `--keepalive-id` requirement into S5's refusal block, after the `still held` exit
and before anything is written. Every take-over row then refuses a missing id with a numbered message
naming `--keepalive-id`, and the lease is taken naming the id. Unit 5's prompt and AC8 pass the
session's own id. Add an AC: a no-id `--resume` on a HELD fixture with a met condition refuses and
leaves the run-state and lease files byte-unchanged.

**Left-shift.** This is item 4 below, a reacher column on the lease matrix. Each of these two callers
is a reacher of the take-over rows.

### M6 — `run_bounded`'s unconditional refresh lets a refused preflight renew a dead session's lease (44)

**Where.** Unit 4 §2 S6 and S9; §4 "The lease", refresh sources; §6 AC10.

**Defect.** S6 lists "the start of `run_bounded`" as a REFRESH source with no condition on who holds
the lease. At BASE, `--preflight`'s precondition block runs `check_wiring || true` (`:2596`), which
reaches `run_bounded $WIRING_CHECK` (`:1116`) because gov declares `WIRING_CHECK`. That happens
before the write gate at `:2642`, whether or not preflight will then refuse. Units 3 and 27 add two
more bounded probes to that block: the `--carry` probe and `GATE_PROFILE_CMD`. Nothing places S9's
HELD and different-id refusals ahead of it.

**Impact.** Suppose a second session runs `--preflight --keepalive-id C` over a dead session's working
record. The refused preflight turns the dead lease fresh. Its `--resume --keepalive-id C` then meets
the "fresh, a different id" row and is refused for the whole bound, about 29400 s once unit 27 lands.
Every retried preflight re-arms the refusal. Over HELD, a `released … held` lease is rewritten as
refreshed. Unit 28 §4 names this hazard in its own words ("`run_bounded`'s lease refresh would write a
lease the verb does not hold"), and AC10 checks only the `keepalive` fact.

**Fix.** Refresh from `run_bounded` only when the lease names the verb's own keepalive, or only after
the verb's own lease decision. State that S9's refusals return before any `run_bounded` call. Add a
lease-file byte-unchanged assertion to AC10's different-id and HELD arms.

**Left-shift.** A refresh source is a WRITE. The lease matrix's AC set should hold every lease write
to the same byte-unchanged-on-refusal assertion AC1, AC6 and AC18 already make.

### M7 — the matching-id refresh that F6's resolution depends on is unobserved (13)

**Where.** Unit 4 §2 S6; §4 "The lease", the matching-id row; §8 F6; §6 AC17.

**Defect.** F6 resolves KF7's keepalive-tick refresh through a `--resume` carrying the lease's own id.
S6 says AC6, AC7, AC17 and AC20 observe it. None of them reads `refreshed` after a matching-id
orientation. AC17 covers preflight, phase, hold and abort. AC20 is the `--replaces` row. AC6 and AC7
are a refusal and a take-over. Unit 28's matching-id arms observe only reaping.

**Impact.** An orientation that skips the refresh passes every criterion. An idle holder's lease then
goes stale after the bound, and a second session takes the slug over while its holder is alive. That
is the defect round-1 H2 asked the refresh to prevent.

**Fix.** Extend AC17: `--resume --keepalive-id <the lease's id>` on a working-phase record advances
`refreshed` and changes nothing else. Stage it RED by dropping the refresh from the orientation row.

**Left-shift.** Class item 5 below, the skip test.

### M8 — auto-filed asks reset `hold-streak`, so the resume limit never binds for inherited reds (26)

**Where.** Unit 5 §2 S5, §4 Data model (`hold-streak`) and §6 AC6; against unit 24 §2 S10.

**Defect.** `hold-streak` adds 1 only when every path changed since the previous hold is the run-state
file, and any other path resets it to 1. Once `ASKS_CMD` is armed, unit 24 S10 stages an ask, a SEV
row and a KEEP row in the run's `BACKLOG.md` for every INHERITED leg on each `gates-green`. Each ask
gets a fresh id and nothing dedupes. On the hold path the Skill's Close sequence commits those rows
before `--hold`, so every hold of this class changes `BACKLOG.md`.

**Impact.** A hold for an aged or parked inherited red restarts without end. Each probe-gate resume
re-runs the full bar, holds again, owes another one-shot schedule, and files another duplicate HIGH
ask. `RESUME_SCHEDULE_LIMIT` never binds for the one stop class that cannot progress in-run, which
contradicts S5's own purpose.

**Fix.** Exclude the driver-written record paths from the progress test: the run-state file, and the
ask rows the run's own auto-file stages in its `BACKLOG.md`. Alternatively, unit 24's auto-file can
reuse an OPEN ask already filed for the same leg and R. Add an AC6 arm in which each hold auto-files a
row, and expect streak 2 with `none · limit`.

**Left-shift.** A no-progress predicate lists every path the machinery itself writes. The same list
can feed both unit 5's streak and unit 24's staging, so one declaration answers "what does the driver
write".

### M9 — a re-close after a re-prepare has nothing to commit, and refuses after paying the bar (43)

**Where.** Unit 3 §4 "`--close` under `in-place`", step 4; §4 "What an incomplete landing does".

**Defect.** Step 4 commits the run-state change unconditionally. At BASE, `verb_close` writes only
`phase LANDING` and stages it (`:3037-3042`). Unit 22 S6 adds `units-at-landing` and
`asks-at-landing`, both derived from unchanged inputs. A re-close over a record that is already
LANDING, with no override, rewrites identical bytes and stages nothing, so `git commit` exits 1. The
spec leads there itself twice. A `red` push is "a fix-and-re-prepare", and a resumed HELD-from-LANDING
run whose remote moved has `--land` refuse naming `--prepare`. Both paths re-run S6's sequence of
`--prepare`, `--close` and `--land`.

**Impact.** The re-close refuses at step 4 as "a failed commit" after `gates-green` has already paid a
full bar. The documented sequence wedges on both re-prepare paths the spec names.

**Fix.** Step 4 commits only when the stage is non-empty. Otherwise it reports that the close record
is already committed and exits 0. Or state that a re-prepared landing goes straight to `--land`. Add
an arm that re-closes a LANDING record after a re-prepare.

**Left-shift.** Every documented retry path gets one arm that runs the sequence twice, the second time
over the first run's output.

### M10 — `gates-green`'s attribution arm is observed only on inherited-only records (12)

**Where.** Unit 27 §2 S5; §6 AC13; against unit 24's gates-green criteria.

**Defect.** AC13 covers MET under `land` and the park hold. Unit 24 observes the aged row (AC17) and
the moved row (AC15) in `gates-green`. It observes OWN and MIXED only at the pre-push hook (AC2) and
at override and abort (AC6, AC7), and an override skips `gates-green` entirely. No criterion in
either spec runs `gates-green` over a record holding one INHERITED red and one OWN or MIXED red.

**Impact.** A mapping that tests "any red is INHERITED" instead of "every red is" passes both specs.
The run then commits LANDING over a NEW red, and only the push boundary stops it. Unit 27 rewrites
this table after unit 24 builds it, so the gap sits on the rewriter.

**Fix.** Add an AC13 arm. An attribution record with one INHERITED leg and one MIXED leg, under
`land`, leaves the item UNMET, prints the attribution lines, and prints no `hold ·` line. Stage it RED
with an existential INHERITED test.

**Left-shift.** A quantified predicate is tested with a MIXED population. A fixture that carries only
the passing kind is `memory/gotchas/fixture-passes-by-finding-nothing.md`.

### M11 — unit 1 S9's version move is observed by no criterion (3)

**Where.** Unit 1 §2 S9.

**Defect.** S9 says "the `kit version markers` leg grades it". `tools/check-kit-versions.sh` checks
only that each constant is present and well formed, and that each marker/constant pair agrees. If
the move is skipped, the pairs agree at BASE's values, 1.6 and 1.19, and the leg stays green.

**Impact.** The fold made S9 the build's one move for both kits. Units 5, 22, 27 and 28 now defer to
it, and units 27 and 28 lost their own check-kit-versions criteria. No criterion anywhere in the
build grades the move. TOOL-dMuffledSentinel-3 is the precedent (`2df329ac`). Gov's leg missed
exactly this, and an adopter's leg refused the pull.

**Fix.** Add an AC. At unit 1's build commit, `KIT_RUN_GATES_VERSION` and `KIT_UNATTENDED_VERSION`
each read higher than at `abac6d59`, compared with `git show abac6d59:<file>`. Red when: the move is
skipped and the markers still agree.

**Left-shift.** A monotone check in `tools/check-kit-versions.sh`: a kit whose shipped bytes changed
since the recorded base carries a higher constant. Memory-tree's verdict-epoch gate is the pattern.

### M12 — unit 5 AC15 cannot fail (9, 25, 41)

**Where.** Unit 5 §2 S11, §6 AC15 and §4 Rollout.

**Defect.** The shipped example already carries `KEEPALIVE_CREATE="<your-schedule-create-tool>"`
(`tools/unattended/.unattended.conf.example:43`), along with the matching `KEEPALIVE_DELETE` and
`KEEPALIVE_INTERVAL` placeholders at `:44` and `:49`. The discharge probe is
`! grep -qE '^KEEPALIVE_(CREATE|DELETE|INTERVAL)="<.*>"'` (`tools/unattended/kit.toml:196`), and it
already exits non-zero on a verbatim copy, with or without S11's extension. It is a quiet grep and
prints no line, so "exits non-zero on the `RESUME_SCHEDULE_CREATE` line" cannot be observed. Gov's
filled conf exits 0 either way.

**Impact.** A probe that never gains the RESUME keys passes AC15, which is round-1 M14's defect again.
The population the extension exists for has no fixture: an adopter who filled the keepalive keys and
kept the example's resume placeholders. Rollout's "a fresh adopter who copies the example verbatim is
caught by the extended probe" names the wrong population.

**Fix.** Build AC15's fixture from the example with the three KEEPALIVE lines filled and only
`RESUME_SCHEDULE_(CREATE|DELETE)` left verbatim, and expect a non-zero exit. Fill those two as well and
expect 0. Stage it RED by reverting the probe to the KEEPALIVE-only alternation. Correct the Rollout
sentence.

**Left-shift.** A staged-RED arm asserts WHICH rule reds, never merely that something did. A
quiet-grep probe cannot say which, so its fixture must isolate the rule under test.

### M13 — unit 3 AC13's `SELFTESTS_OWED_PATHS` half passes on an empty declaration (11)

**Where.** Unit 3 §6 AC13; §2 S1; §4 `gates-green`.

**Defect.** §4 says "Blank means never, announced" and "Gov declares its kit roots". AC13 asks only
that every entry resolves to a tracked directory under `tools/`, which is vacuously true for a blank
value. Its Red-when names only a blank `LANDER_MODE`. The fix round-1 M22 asked for was entries that
resolve to the `tools/` kit roots, and this wording dropped that requirement.

**Impact.** Gov can ship the key blank with AC13 green. Every in-place landing of kit work in gov then
runs without `GATE_SELFTESTS=1`, the kit DoD `AGENTS.md` states.

**Fix.** Require AC13's printed list to be non-empty and to cover every kit root a landing range can
touch, compared against the derived set of kit directories under `tools/` that carry a `kit.toml`.
Add a Red-when for a blank declaration.

**Left-shift.** `memory/gotchas/vacuous-selector-empty-population.md`. A criterion over "every entry"
asserts a non-empty population first.

## Low

### L1 — `gates-green` reads `--prepared` only as zero or non-zero (18, 37)

**Where.** Unit 3 §2 S3 and S2; §4 `gates-green`, the precondition refusal; against unit 2 §2 S7 and
S10.

**Defect.** Unit 2 S7 gives every new flag exit 2 for an argument refusal and exit 3 for an
observation failure. Round-1 L3's fold maps those apart for `--carry` only (unit 3 S2). For
`--prepared`, the query that same fold introduced, `gates-green` treats any non-zero exit as an
unprepared HEAD and names `{{LANDER}} --prepare`. Preflight probes `--carry` only.

**Impact.** During a remote outage, `--close` tells the run to re-prepare, and `--prepare` then fails
the same way. That is L3's wrong diagnosis again. The route to a `platform-unavailable` hold starts
only at `--land`.

**Fix.** Map `--prepared`'s exits as step 2 maps `--carry`'s: 1 names `--prepare`, 2 names a lander
that does not implement the mode, and 3 names the observation failure. Probe both flags at preflight.
Add an AC arm with a stub whose `--prepared` exits 3.

**Left-shift.** Class item 3 below. A fold that fixes one member of a set lists the set.

### L2 — exit 3 is observed only for an undeterminable default branch (17)

**Where.** Unit 2 §2 S7; §6 AC13.

**Defect.** S7 gives exit 3 three members: not a repository, an undeterminable default branch, and a
failed `ls-remote` or fetch. AC13 exercises only an unset `origin/HEAD`. Its own Red-when names the
network-fault misreport, which that fixture cannot produce. At BASE a failed fetch exits 2
(`tools/push-main.sh:78`).

**Impact.** A new flag that reuses the fetch path passes AC13 and AC6. Unit 3's preflight would then
report an outage as a `LANDER_MODE` misdeclaration.

**Fix.** Add an AC13 arm with the fixture's `origin` pointing at a missing path, and require both
`--carry` and `--prepared` to exit 3. Unit 4 AC15 already builds that fixture.

**Left-shift.** Gate the class, not the instance: one arm per member of a closed exit-code set.

### L3 — the incomplete-landing route omits `--reaped`, which `--hold` requires (36)

**Where.** Unit 3 §4 "What an incomplete landing does", §2 S6 and §6 AC8; against unit 4 §2 S2 and S3,
and unit 27 §2 S7.

**Defect.** Unit 4 S3 and AC14 refuse a hold whose keepalive is neither named by `--reaped` nor
recorded unreachable, and unit 4 S2's synopsis omits both flags. Unit 3's route spells
`--hold --code platform-unavailable --until after <now + 30 minutes>` with a reason and no
`--reaped`. Unit 27 S7 spells `--reaped <id>` for the same verb.

**Impact.** A run following the Land section's documented act is refused at its only ending, and two
routes to one verb disagree about its arguments. That is
`memory/gotchas/two-answers-to-one-question.md`. The refusal is numbered and recoverable, which keeps
this LOW.

**Fix.** The route and the rendered Land section name `--reaped <recorded id>`, the keepalive the
close's attestation already reaped, and AC8 greps for it. Unit 4 S2's synopsis lists `--reaped` and
`--keepalive-unreachable`.

**Left-shift.** The skill-wiring check already parses the Skill's verb invocations. It can compare
each spelled `--hold` against the driver's required-flag set.

### L4 — the checkpoint format has no `hold-unpushed` field (14)

**Where.** Unit 4 §4 "Codes and conditions"; §4 "The checkpoint"; §6 AC15.

**Defect.** §4 says `--status` prints the unpublished tip on the checkpoint line, and that a take-over
prints the push as its first act. §5 names this signal as the mitigation for relaxing design §21.7.
The normative checkpoint block lists witness, next, last bar and parked, and no `hold-unpushed`
field. No criterion observes either behaviour, and AC15 reads only the fact.

**Impact.** An implementation that follows the format block hides the one signal that held work
exists only on this node.

**Fix.** Add `unpushed <sha8>` to the checkpoint format. Extend AC15: `--status` shows the field, and a
take-over over such a hold prints the branch push as its first act.

**Left-shift.** Class item 5 below.

### L5 — `--hold` reaping and the ledger's removal are unobserved (20, 33)

**Where.** Unit 28 §2 S3, §4 "Pruning and concurrency" and §6; against unit 22 §2 S16 and AC15.

**Defect.** S3 lists `--hold` as a reaping verb, but AC11 observes only `gates-green` and `--preflight`,
and AC6 runs `--hold` under a live driver, where nothing is an orphan. Round-1 M30 named `--hold`
among the unobserved sites. The ledger's removal at a terminal and at in-place `--landed` appears
only in §4 prose and the rev-2 line. No S-item scopes it and no AC observes it. Unit 22 S16 says "The
process-ledger unit removes its ledger at the same point. Observed by AC15". AC15 checks only the
lease file and porcelain, and porcelain cannot see a file under the git common dir.

**Impact.** A build that never reaps at `--hold`, or never removes the ledger, passes every criterion
in both units. A leftover ledger is pruned by the next reaping verb, which keeps this LOW.

**Fix.** Add an AC11 clause: an orphan left by a killed driver is reaped by `--hold`, which then
proceeds. Add an S-item and an AC for removal. After in-place `--landed` and after `--abort`, with no
recorded process alive, `<slug>.procs` is gone. With one alive, the file stays and the line says so.
Correct unit 22 S16's observed-by claim.

**Left-shift.** A hands-off payload is an S-item in the receiving spec. The edge join in class item 2
can check that each hands-off names one.

### L6 — unit 27 S7's `platform-unavailable` fallback is unobserved (21)

**Where.** Unit 27 §2 S7; §6 AC8.

**Defect.** S7's second clause holds under `platform-unavailable` when the branch push fails because
the remote does not answer. S7 says AC8 observes it. AC8 checks only the order of commit, push and
`--hold`, and the absence of `--override`. Unit 3 AC8 covers the same clause for the Land section only.

**Impact.** The Close section can omit the fallback and pass.

**Fix.** Extend AC8: the rendered Close section names `platform-unavailable` as the hold when the
branch push fails because the remote does not answer.

**Left-shift.** Class item 5 below.

### L7 — check 15's `landed-derived` ancestry test has no reject arm (22)

**Where.** Unit 22 §2 S9; §6 AC6.

**Defect.** S9 requires the landing commit a `landed-derived` fact names to be an ancestor of the
advertised tip. AC6 and AC9 are accept-side, and AC8 grades check 7. No criterion or §7 arm plants a
`landed-derived` commit off the tip.

**Impact.** A check 15 that accepts any `landed-derived` line as anchor evidence passes every
criterion, so a hand-written archive meets the anchor rule without ever having landed.

**Fix.** Add an arm: a `RUN.LANDED.` fixture whose `landed-derived` names a commit the bare remote
lacks reds check 15.

**Left-shift.** Every acceptance rule pairs one accept arm with one reject arm.

### L8 — a fourth place states the GREEN-verdict DoD (47)

**Where.** Unit 1 §2 S8; §6 AC7.

**Defect.** S8 moves the compensating check's wording "in the three places that state it". A fourth
exists at BASE. `.githooks/gate-env.sh:23-28` says "the DoD for work touching a kit is a GREEN verdict
pasted into the landing report" and names both runners. No other dDerivedDocket spec touches that
wording, and unit 24 edits the file only to add keys.

**Impact.** After S8, gov carries two answers to one question, which is AC7's own Red-when, and AC7
reads only `tools/unattended/kit.toml` and the two runner headers.

**Fix.** Add the comment in `.githooks/gate-env.sh` to S8's carriers and to AC7's read set, or replace
it with a pointer to the kit.toml block. H1's restated criterion then lands in all four places.

**Left-shift.** AC7's read set is a grep for the phrase across the tracked tree, not a list of three
files. An unwatched fourth copy is the class `memory/gotchas/two-answers-to-one-question.md` records.

## Left-shift, by class

1. **An archive-producing arm grades the working copy and a subset of the leg** (B1, B2). This
   extends round-1 item 2. The shared helper asserts `git status --porcelain` is empty, reads the
   archive through `git show :<archive>`, and runs the WHOLE leg, check 19 included, over a fixture
   whose default branch gained an owner `may:` commit after BASE. Stage each RED by removing the
   pre-move stage and by restoring unit 19's terminal row.
2. **A handed-off criterion is one field of the producer's output, not its verdict** (H1, L5, L8).
   Add a join over edge lines: every AC in a spec that consumes from a producer carries the
   producer's named criterion token, and every hands-off payload is an S-item in the receiving spec.
   `tools/check-spec-tokens.py` prints the misses as near-misses for the auditor, never as a red.
3. **A fold fixes one member of a set and leaves its siblings** (L1, L2, L3, L6, M4, M10, M3, B2). This
   is `memory/gotchas/amendment-leaves-its-other-half-standing.md` in its fold-time form. It is a
   documented check for whoever folds. When a fix names one flag, route, row or mode, the fold line
   lists the set's other members and gives each a criterion or a reason. Round 1's fold fixed
   `--carry` and left `--prepared`, fixed one hold route and left the other, and fixed the lease at
   one row and moved its symptom to the next.
4. **A lease-matrix row with no analysis of who reaches it** (M2, M3, M5, M6, M7). Add a Reacher
   column to unit 4's matrix naming who arrives first: the holder, a second session, the scheduler, M7's
   no-id regrounding, a preflight, or a pre-lease run. Add one driver arm per row and reacher. The
   mechanical half is a self-scan in `tools/unattended/check-unattended.test.sh` that counts matrix
   rows against arms, printing hits and near-misses before it is wired.
5. **An S-item whose "Observed by" criteria survive its deletion** (M7, M10, M11, M12, M13, L2, L4,
   L5, L6, L7). This is round-1 item 5 again, and the fold reintroduced it in its own new criteria:
   10 of the 24 defects. The skip test has to run on the FOLD, by the folder, before the next round.
   For each new or changed S-item, name the mutation that deletes it and the AC that reds.
6. **An exemption at the wrong grain** (M1). A structural arm exempts the writing LINE, never the
   function that contains it. Run the predicate over BASE's driver first. `unattended.sh:2568` is a
   live hit.

## Outside the confirmed set

One observation came from reading unit 1 at synthesis and was not put to a skeptic, so it is not
counted above. Unit 1 S5 exits 1 on any DEAD PROBE, the R side included. If any unattended suite is
DEAD at BASE, every consumer's attributed run exits 1 for a cause that consumer did not make, which
is the problem unit 1 exists to remove. It constrains H1's fix, and the H1 entry states it there. A
fold should settle it before any consumer criterion is rewritten against the exit status.

## What this round did not cover

- **The dead lens's whole scope.** Which lens died was not reported to this synthesis, so no subject
  and no lens area can be claimed covered. Round-1 fixes marked "no confirmed finding" above, B1, H3,
  H4, H5 and H6 among them, were examined by at most three lenses.
- **Units outside G1**, read only where an edge or an interface named them. B2 and M4 require a fold
  in unit 19 (G3), and M8 and M10 name unit 24 (G4), so those groups' own audits should pick up the
  other half. Nothing here clears units 6 to 21, 23 to 26 or 29 to 36, PLAY-dDerivedDocket-1 or
  DEPL-dDerivedDocket-1.
- **The design record's measured figures**, which were not independently re-derived. The 29400 s
  backstop is taken as unit 27 and round 1 computed it.
- **The 18 refuted findings**, which are not reproduced here. They were refuted, not lost, as the
  run-integrity counters show.
