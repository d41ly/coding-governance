**Serves:** spec-audit TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9

# aGraftedHelix — Tier-2 spec audit of the nine-unit set, ROUND 1

*Node `a`, 2026-10-04, ROUND 1. This is the first audit of the nine specs the harness spec stage
authored at `b3a5e2ecf`. Four lenses ran: underspecification, contradiction, unstated assumption and
prior art. Every finding in the body survived a skeptic prompted to REFUTE it. The four findings the
skeptics refuted appear only in the appendix. The author of this report confirmed that each pinned
blob below is the blob at HEAD (`cddacb6fd`), and spot-checked both blocker rows in the tree: the
URL test at `.githooks/pre-push:164-169`, the refusal at `:413-420`, and the absence of
`CLAUDE_CODE_SESSION_ID` from `tools/unattended/resume-tick.sh`. The other rows carry the skeptics'
verified text and were not re-derived here. Each row gives its address inside the spec, the fix
together with the skeptic's verdict on it, and the gate that would catch its class before a reviewer
has to.*

**Reviewed at ROUND 1, each subject pinned at its blob:** `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md`@`d10784b8cd5f1722b0ef7e6b6aa623ed9a18c017`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-2.md`@`e4f8020ffa832a783e9261be23f227e68d4e3bb7`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-3.md`@`ae441e751e9a198278867c98a91082d0f08d0bb8`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-4.md`@`82abd7af65f8c2fe68e4484207cc58d064551011`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-9.md`@`740a9c16ea7ece8207b31cf85d75cd8693f7b077`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-6.md`@`275b25efee313367bf13663051654e744561221c`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-5.md`@`ece112f4fe791e234d0cd8f72e53767c0b849417`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-7.md`@`5ec6b3edd3e530677e180537697bb7d0186430f6`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-8.md`@`d12bcfd09328592cd593b0915fc48ee2344e15c1`.

## Verdict: BLOCKED

Two confirmed findings are graded BLOCKER. Both sit in TOOL-aGraftedHelix-1, both are on the claim
write path, and neither is visible to that unit's own fixtures. B1: the claim is pushed to a URL, and
the tracked pre-push hook refuses every URL push on a node where `GOV_DEFAULT_BRANCH` is unset, as it
is on node `a`. Every `--preflight` then refuses with check 91, while AC4 to AC9 stay green on
`git clone --local` fixtures that run no hook. B2: `--beat` runs from the OS-scheduled tick, which
carries no `CLAUDE_CODE_SESSION_ID`. Its renewal rewrites the claim's session to `absent`, so the
holder reads its own claim as foreign `live` and is forced to `--abort claim-lost`.

Five findings are at HIGH, twenty-eight at MEDIUM and fourteen at LOW. Adjudicated, the forty-nine
confirmed findings form forty-seven items. Two merges were made: unit 7's two hold-bound findings
(ids 33 and 41) are one defect, and the engine-dispatch findings of units 6 and 9 (ids 20 and 27)
are one class. Id 31 is the same mechanism as B1 but carries a binding HIGH grade, so it stays a
separate item; the note beside it gives the reason I would grade it higher.

Disposition: FOLD. Both blockers are defects in the documents this review read, and the mechanism
each needs is inside unit 1's own scope. B1 needs one invocation change and one hook-wired fixture
arm. B2 needs one identity rule for renewals and one tick arm run with the session variable unset.

## Review shape

Intensity full. Raw 53, confirmed 49, refuted 4 (ids 42, 44, 49 and 53), unverified 0 (0 uncertain),
precision 0.92.

The adjudicated tally, counted both ways:

| severity | items | raw confirmed findings |
|---|---|---|
| BLOCKER | 2 | 2 |
| HIGH | 4 | 5 |
| MEDIUM | 27 | 28 |
| LOW | 14 | 14 |
| **total** | **47** | **49** |

By lens, raw then confirmed: underspecification 30 and 30, contradiction 7 and 7, unstated
assumption 4 and 4, prior art 12 and 8.

By unit, counting confirmed findings by the spec each one is anchored on: unit 1 holds 15, unit 2
holds 4, unit 3 holds 5, unit 4 holds 3, unit 5 holds 5, unit 6 holds 4, unit 7 holds 4, unit 8
holds 3 and unit 9 holds 6. Ids 36 and 37 are anchored on unit 9 and name unit 6 too.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and 0
  duplicates were found.
- Fixes on confirmed findings: 40 judged sound, 9 judged UNSOUND, 0 with no fix proposed, and 0 NOT
  JUDGED. An unjudged fix would be the finder's proposal and nothing more; none occurs here.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, so none is bound at the finder's grade
  by default. 4 were RE-GRADED by the skeptic: ids 1, 34 and 45 down one step, and id 35 up one step to
  medium.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

This report does not call the run complete. Every lens and every skeptic batch returned, but no
checklist was swept, no intent was supplied, and every lens ran on the generic brief.

**Intent:** NEITHER `specs` nor `context` was supplied to this review. The lenses graded the nine
specs against themselves, against each other, against the spec brief and against the tree, not
against a stated intent for the build.

**Checklist:** NONE swept — absent. The count of recurring-bug-class findings in this report is
therefore not evidence that the project's recurring classes are absent from these specs. Unit 3 S9
is the change that would hand a spec audit its checklist; until it lands, a round-2 caller should
pass the output of `python tools/memory-tree/gotchas.py --for-paths` over the specs' Files-touched
paths.

## How the findings cluster

A fold that repairs a class repairs every row in it, so the classes are named here before the rows.

| class | ids | where the gate belongs |
|---|---|---|
| A fixture that cannot see the production environment | 38, 31, 39 | the unattended driver suite's fixture builder |
| A decision-table cell with no criterion | 2, 3, 4, 9, 10, 23, 46 | a table-row-to-AC join over spec §6 |
| A criterion that observes presence, not behaviour | 8, 12, 13, 20, 25, 27 | a §10 checklist entry, and a candidate spec lint |
| A red condition the AC's own fixture cannot reach | 1, 26, 30, 21 | a §10 checklist entry |
| A failure or edge branch with no criterion | 5, 6, 7, 11, 14, 15, 16, 17, 18, 19, 22, 24, 28 | arms in the owning suite |
| An example conf whose value nothing checks | 15, 29, 9 | the example-conf arm in `check-memory-hygiene.test.sh` |
| Prose that contradicts the design or a sibling spec | 32, 33, 41, 34, 35, 36, 37, 40 | a §10 checklist entry |
| A prior ruling or reader the spec did not engage | 43, 45, 47, 48, 50, 51, 52 | a §10 checklist entry |

Ids appear in more than one class where the defect has two faces. Each id still sits in exactly one
graded item below.

# BLOCKERS

## B1 · id=38 — claim writes push to a URL, and the tracked pre-push hook refuses every URL push on a node without `GOV_DEFAULT_BRANCH`

- **Address:** TOOL-aGraftedHelix-1 §4 "The remote" and "The outcome of a write"; §3 "The pre-push
  hook"; §6 AC4 to AC9.
- **Defect:** §4 "The remote" sends claim reads and writes to the push URL. When git pushes to a
  URL, the hook receives the URL as `$1`. `resolve_remote_name` (`.githooks/pre-push:164-169`) treats
  anything containing `/`, `\`, `:` or `@` as no name, so the observed default stays empty and falls
  back to `GOV_DEFAULT_BRANCH`. With that variable unset, the hook writes a `default-branch` refusal
  and exits 1 at `:413-420`. That is well before the skip-nondefault exit at `:905`, which §3 says a
  claim push takes.
- **Reproduced by the skeptic:** in a scratch clone with `core.hooksPath` set to the tracked
  `.githooks` and `GOV_DEFAULT_BRANCH` unset, a `--force-with-lease` push of `refs/gov/runs/x` to the
  push URL was refused with "can't determine the default branch". git printed no `!` status line and
  the exit was 1. The same push to the remote NAME, with `origin/HEAD` set, landed as a new
  reference. The URL push with `GOV_DEFAULT_BRANCH=main` also landed.
- **Impact:** node `a` has no `GOV_*` variable in its environment, and its `core.hooksPath` points at
  the tracked `.githooks`; `check-wiring --session` auto-sets that path on every node. So every
  production claim write ends NOT COMPLETED, and every `--preflight` refuses with check 91. No
  unattended run can start. AC4 to AC9 cannot see this: a `git clone --local` fixture inherits no
  `core.hooksPath`, and the driver suite exports `GOV_DEFAULT_BRANCH=main`
  (`tools/unattended/unattended.test.sh:477`). The criteria would go green while every production run
  is refused, which makes the suite a check certifying a write path it never exercised.
- **Fix — the skeptic judged it SOUND:** push the claim to the remote NAME, which `observe_anchor`
  already resolves; check 25 already proves the name and the URL are one endpoint. Alternatively,
  export `GOV_DEFAULT_BRANCH`, set to the branch `default_branch()` resolved, into the claim push's
  environment only. State in §3 which of the two the design relies on. Add an AC whose fixture wires
  `core.hooksPath` to the tracked `.githooks` with `GOV_DEFAULT_BRANCH` unset, and assert that
  `--preflight` writes `refs/gov/runs/<slug>` and that `<git-dir>/pre-push-refusal` is absent
  afterwards.
- **Left-shift gate:** the new AC is the regression arm. The class gate is the fixture builder: the
  unattended suite should wire its fixtures' `core.hooksPath` to the tracked hooks and leave
  `GOV_DEFAULT_BRANCH` unset by default, exporting it only in the arms that test it. A push arm then
  cannot pass on a fixture the production hook never sees. Add a §10 checklist entry: "a fixture made
  by `git clone --local` carries no `core.hooksPath`; every push a spec adds is observed through the
  tracked hook."

## B2 · id=39 — `--beat` from the OS-scheduled tick rewrites the claim's session to `absent`, and the holder then reads its own claim as foreign

- **Address:** TOOL-aGraftedHelix-1 §4 "The claim record", "Renewal" and "The two verbs" (`--beat`);
  §2 S10 and S11; §6 AC12.
- **Defect:** the claim record pins `session: <CLAUDE_CODE_SESSION_ID, else absent>` (spec line 160).
  A renewal writes whenever a field it would set differs. `resume-tick.sh` is launched by the OS
  scheduler and sets no `CLAUDE_CODE_SESSION_ID`; the variable appears nowhere in that file. On a
  LIVE run, `--beat` reads `mine`, because the claim's session equals the record's session fact. Its
  write would set the session to `absent`, so the write is due at once and lands `session: absent`.
- **Impact:** the holder's next `--resume`, `--dispatch` or `--close` sees the keepalive match and
  the session differ, so the claim is not `mine`. The `same session` row needs the claim's session to
  equal a non-absent environment id, which it does not. The claim reads foreign `live`, the call
  refuses with check 90, and the run must `--abort claim-lost`. That happens on every run the tick
  beats, which is the long-Workflow case F5 adds the tick for. AC12 asserts only that `beat-utc`
  moved, and a tick suite launched from a Claude session inherits `CLAUDE_CODE_SESSION_ID`, so it
  would pass. The finder also raised an unverified second exposure: `--dispatch` is run by Workflow
  child agents (`tools/workflows/unattended-unit.js:147`), whose session id was never shown to equal
  the lease's. The corrected fix below closes that exposure too, because a holder renewal on the
  `mine` row no longer takes identity from its environment.
- **Fix — the finder's proposal was REJECTED by the skeptic; the skeptic's corrected fix:**
  `--beat` never takes identity from its environment. On the `mine` row it copies keepalive, session,
  node, host and lease-utc from the claim it read. On the `none` row it takes them from the run's
  lease record (the RUN.md keepalive, session, host and lease-utc facts). In both cases it moves only
  `beat-utc` and status. A holder renewal on the `mine` row likewise copies identity from the claim it
  read. Environment identity is used only by `--preflight`, a take-over and the same-session take.
  Extend AC12 to run the tick's `--beat` with `CLAUDE_CODE_SESSION_ID` unset, once over a seeded
  claim and once with no claim. Each time, assert that the claim names the lease's session and that
  `--resume <slug> --keepalive-id <id>` exits 0 without check 90.
- **Left-shift gate:** the extended AC12 is the regression arm, and it must run under
  `env -u CLAUDE_CODE_SESSION_ID`, because the suite's own parent supplies the variable otherwise.
  Class gate: every verb the OS-scheduled tick runs is exercised in the suite with the session
  variable unset. Add a §10 checklist entry: "identity a verb writes comes from the environment of
  the process that runs it; name that process for every writer, and the tick is not a Claude
  session."

# HIGH

## H1 · id=31 — §3 and the Evidence bullet say a claim push takes the hook's non-default exit; a URL push never reaches it

- **Address:** TOOL-aGraftedHelix-1 §4 "The remote", against §3 "The pre-push hook" and the §4
  Evidence pre-push bullet.
- **Defect:** the contradiction between §4's invocation and §3's claim, by the mechanism B1 states.
  The M12 probe that "passed the pre-push hook" can only have pushed by remote name, because
  `origin/HEAD` resolves and `core.hooksPath` is set on node `a`. Neither `unattended.sh` nor
  `gate-env.sh` exports `GOV_DEFAULT_BRANCH` before the claim push.
- **Impact:** as B1. Every `write_claim` on a hook-wired node with `GOV_DEFAULT_BRANCH` unset reads
  NOT COMPLETED, and `--preflight` and `--close` refuse every run with check 91. The fixtures stay
  green. The failure refuses safely rather than passing silently, but it disables the feature on the
  main path.
- **Grade note:** the binding grade is HIGH and this item keeps it. I would grade it BLOCKER, because
  it is the same mechanism as B1, whose consequence includes a suite certifying a write path it never
  exercised. Folding B1 closes this item; it needs no separate repair beyond the §3 restatement.
- **Fix — the skeptic judged it SOUND:** push the claim by the remote's NAME, which `observe_anchor`
  already holds, so the hook observes `<name>/HEAD`. Alternatively, pass `GOV_DEFAULT_BRANCH` set to
  the anchor's observed default into the claim push's environment. Add a driver-suite arm whose
  fixture sets `core.hooksPath` to the tracked `.githooks`, and observe a create and a CAS update
  through it. Restate in §3 which hook branch a claim push takes, and with which invocation.
- **Left-shift gate:** B1's hook-wired fixture arm. Add a §10 checklist entry: "a spec's claim about
  which hook branch a push takes names the invocation it was measured with."

## H2 · id=2 — the refusing cells of the write table have no criterion

- **Address:** TOOL-aGraftedHelix-1 §6, against §2 S4 and the §4 table "Who may write a claim".
- **Defect:** no AC observes these refusing cells: foreign `held` at preflight (check 89), foreign
  `terminal` at take-over (check 89, "would land it twice"), and `unknown` at preflight and at
  take-over (check 89, the F3 ruling). AC4 covers foreign `live` at preflight, AC5 covers `stale` and
  `landed` at preflight, and AC8 covers `live` and `stale` at take-over. S4 says AC4, AC5, AC7 and AC8
  observe the table, and §7's arm sentence names checks 89, 90 and 91 only in general terms.
- **Impact:** a build that maps any of these cells to `take` passes every AC. It would start a second
  driver on a held slug, which is the double drive the unit exists to stop, or re-take a slug another
  driver landed, or take over a claim whose bytes nobody can parse.
- **Fix — the skeptic judged it SOUND:** extend AC5 with a foreign `held` claim and an `unknown`
  claim, each refused with check 89 and leaving no run-state file. Extend AC8 with a foreign `landed`
  claim and an `unknown` claim, each refused with check 89 and leaving the record byte-unchanged.
- **Left-shift gate:** the table-driven arm of M8 (id=46) covers these cells and the rest of the
  matrix. As a class gate, consider a spec lint that joins every row of a §4 decision table to an AC
  or to an explicit `unreached` mark. Run that predicate over the existing specs before wiring it,
  and print hits and near-misses (charter §7).

## H3 · id=3 — no criterion shows `--beat` declining to write

- **Address:** TOOL-aGraftedHelix-1 §6 AC12, against §2 S10 and §4 "The two verbs".
- **Defect:** `--beat` must write only through the `none` and `mine` rows of the holder column and
  print a skipped line for every other row: another host, a claim not this run's, a beat not yet due.
  AC12 observes only the positive renewal and the dry run. AC7's younger-beat and foreign-live cases
  exercise `--resume`, not `--beat`, and §7's tick arm names only "the LIVE row runs --beat, and
  --dry-run pushes nothing".
- **Impact:** a `--beat` that skips the `mine` test makes a valid CAS on the observed sha and
  overwrites a claim another node took over. For example, the original session wakes after a sleep,
  after the new holder has passed `--close`. The stale run can then pass its own `--close` while the
  new holder lands, which is a double landing on a narrow path.
- **Fix — the skeptic judged it SOUND:** add to AC12: with the fixture claim rewritten to another
  session `live`, the tick's line reads `beat · unattended: beat — <slug> · skipped:` and the ref's
  sha is unchanged. Do the same with a beat younger than a quarter of the bound.
- **Left-shift gate:** the two AC12 cases become suite arms. The table-row join of H2 covers the class.

## H4 · id=20, id=27 — the hygiene engine's dispatch of checks 28 and 27 is observed only by a grep that a comment satisfies

- **Address:** TOOL-aGraftedHelix-6 §6 AC7, against §2 S4 (check 28). TOOL-aGraftedHelix-9 §6
  AC10, against §2 S7 (check 27).
- **Defect:** each unit wires a new check into `tools/memory-tree/check-memory-hygiene.sh` as a
  dispatch block that must set `status=1`, key offenders under its check number and print the mode's
  summary on a green run. Each unit observes the wiring only with `grep -n` for its mode name over the
  engine. A comment or a dead block satisfies that grep. For unit 6, a real block that also carries a
  comment prints two lines and fails AC7. AC5 and AC6 of unit 6 run `row_grammar.py` directly and
  never the engine. Unit 9's AC11 grades the catalog and the README count. Each §7 adds only a
  `row_grammar.py --selftest` arm. The green-run print departs from the check-24 precedent at
  `check-memory-hygiene.sh:1330-1335`, which prints only on failure, so the builder writes new logic
  there. `check-arms.py` counts only `fail <n> "` call sites, so a delegated block that sets
  `status=1` is outside the harness-arms leg as well.
- **Impact:** a block that swallows the mode's exit leaves the `memory hygiene` leg green over a
  duplicated record (check 28) or an unsatisfied near match (check 27). The close's leg runs over a
  clean tree, so it is green either way. Unit 9's rollout says it "lands armed red, so its own close
  bar grades every row", and that would never happen. The bar would certify checks it never runs, and
  every AC of both units would pass. This also breaks the charter §7 rule that a gate's failing case
  must be observed before it lands. The path needs a mis-build, which is why the grade is HIGH and not
  BLOCKER.
- **Fix — the skeptic judged both SOUND:** for unit 6, add an AC: in AC6's scratch clone (the copied
  gotcha), `bash tools/memory-tree/check-memory-hygiene.sh` exits non-zero and prints a `check 28:`
  line, and a clean clone prints the `row-grammar: check 28 graded` summary line on a green run. For
  unit 9, add an AC: in a fixture clone holding a restated row added after its base, the same engine
  run exits non-zero with a `check 27:` line, and a clean range prints the `row-grammar: check 27
  graded` line on green. Add both arms to `check-memory-hygiene.test.sh`.
- **Left-shift gate:** the two engine arms. As a class gate, extend `check-arms.py` to count a
  delegated dispatch block that sets `status=1` as a check needing an engine arm, so a delegated check
  without one reds the harness-arms leg. Add a §10 checklist entry: "`grep -n <word>` over a source
  file is a presence probe, not an observation of behaviour."

# MEDIUM

## M1 · id=1 — the age-alignment rule for `date -u -f -` has no criterion

- **Address:** TOOL-aGraftedHelix-1 §6 AC2, against §2 S2 and §4 "Reading".
- **Defect:** §4 "Reading" pins one `date -u -f -` call, and when the answer count differs from the
  count asked, every age that call should have given reads `unknown` instead of shifting. AC2's
  malformed claim lacks `beat-utc`, so it never reaches `date`; it is the "missing key" row of the
  Verdicts table. Neither the "beat-utc that does not parse" row nor the alignment rule is observed,
  although S2 says AC1 to AC3 observe it.
- **Impact:** a build that pairs `date`'s answers with claims in order lets one stamp-shaped but
  invalid `beat-utc` (for example `2026-02-30T00:00:00Z`) shift every later claim's age. A fresh live
  claim can then read `stale`, and another node's `--preflight` can take it over. The path is narrow,
  because the driver writes every beat through `date`, so such a beat comes only from a hand-edited or
  foreign-written claim. The skeptic re-graded it from high to medium on that ground.
- **Fix — the finder's proposal was REJECTED by the skeptic; the skeptic's corrected fix:** add a
  separate case, not a sixth row in AC2's fixture, because a sixth row would turn AC2's other ages
  `unknown`. Seed a claim whose `beat-utc` is stamp-shaped but invalid (`2026-02-30T00:00:00Z`),
  sorted before a fresh `live` claim. Assert, per §4 "Reading", that every claim whose beat went
  through that `date` call reads `unknown` with age `-`. Red when any claim reads `live` or `stale`,
  or prints an age taken from another claim's beat.
- **Left-shift gate:** the new case is the regression arm. Add a §10 checklist entry: "a malformed
  input that never reaches the parser observes nothing about the parser; a Red-when must be reachable
  from the AC's own fixture."

## M2 · id=4 — the `--replaces` block, the LANDING re-bind and the `same session` row have no criterion

- **Address:** TOOL-aGraftedHelix-1 §6, against §2 S7 and the `same session` row of §4.
- **Defect:** S7 says AC7 and AC8 observe it. Neither exercises the `--replaces` block or the LANDING
  re-bind writing the claim, and no AC exercises the `same session` row. AC7 exercises only a holder
  whose keepalive and session both still match.
- **Impact:** with `CLAUDE_CODE_SESSION_ID` absent, `mine` falls back on the keepalive. A `--replaces`
  that left the claim stale-keyed then reads foreign `live`, the holder gets check 90, and the run
  wedges on its own replacement. A build that treats `same session` as foreign has the same effect.
  With the session id present, the `same session` row answers `take`, and after the re-bind the next
  verb is `--landed`, a status write that only announces. The effect is contained to the run's own
  wedge.
- **Fix — the finder's proposal was REJECTED by the skeptic; the skeptic's corrected fix:** after
  `--resume <slug> --replaces <old> --keepalive-id <new>`, assert that the claim's `keepalive` is
  `<new>`, and that a following `--resume <slug> --keepalive-id <new>` exits 0 with the ref's sha
  unchanged when the beat is not yet due. Run it once with `CLAUDE_CODE_SESSION_ID` unset. For the
  LANDING re-bind, seed the prior session's claim `stale` and assert that the claim then names the
  re-binding session's keepalive. Seed it foreign fresh `live` and assert the `claim not written`
  line with exit 0. Add a holder `--resume` against a claim carrying this `CLAUDE_CODE_SESSION_ID`
  under an older keepalive, and assert it is rewritten with exit 0, not check 90.
- **Left-shift gate:** the cases above become suite arms. The table-row join of H2 covers the
  `same session` row.

## M3 · id=5 — `--close`'s check 91 and `--dispatch`'s holder read have no criterion

- **Address:** TOOL-aGraftedHelix-1 §6 AC10, against §2 S8.
- **Defect:** AC10 covers only `--close` against a foreign `live` claim. Two behaviours have no
  criterion: check 91 when the claim cannot be read, and `--dispatch`'s holder read (check 90 with no
  row written, renewal when due).
- **Impact:** `verb_close` runs `observe_anchor || true` and still grades the non-overridable
  authorization-reachable DoD item, so a remote that answers nothing blocks the close anyway. The
  unprotected case is a remote that answers the anchor read but refuses the `refs/gov/` fetch: a
  `--close` that treats that as a pass lands a run whose claim it never verified. A `--dispatch` that
  skips the read writes pass rows for a run another node now drives, which a correct `--close` later
  refuses. The effect is contained.
- **Fix — the skeptic judged it SOUND:** extend AC10: with the fixture's remote URL broken, `--close`
  exits with `UNATTENDED check 91 FAILED` before any DoD line. Add a `--dispatch` case: with the claim
  rewritten to another session `live`, it exits with check 90 and the run-state file is
  byte-unchanged.
- **Left-shift gate:** the two cases become suite arms. To reach the unprotected case, the broken
  remote should answer the anchor read and refuse only the `refs/gov/` fetch.

## M4 · id=6 — `--preflight`'s check 91, the never-a-lost-race rule, and CAS-before-rotation have no criterion

- **Address:** TOOL-aGraftedHelix-1 §6 AC4 and AC6, against §2 S3 and S5 and §4 "The outcome of a
  write".
- **Defect:** AC3 observes check 91 for `--claims` only. AC4 to AC6 never make the preflight write
  fail without a race, so S5's check 91 and §4's rule that a pre-push refusal, a non-race `!` line or
  an exit 124 is never a lost race have no criterion. AC6 runs on a fresh slug, so it observes the CAS
  coming before `scaffold_runmd` (through the missing run-state file) but not before the rotation.
- **Impact:** a build that misclassifies a refused or timed-out push as LOST sends the run to
  `--abort --code claim-lost` over a network fault, reporting check 90 where 91 is due. A build that
  rotates before the CAS leaves a prior run's record moved by a preflight that then lost. Both are
  contained.
- **Fix — the skeptic judged it SOUND:** add an AC: a `git` shim that makes the push print a non-race
  `!` line, or exit 124, makes `--preflight` exit with check 91 (not 90) and leaves the tree
  byte-unchanged. Run AC6 once on a slug holding a prior terminal record, and assert that the prior
  record is unmoved after the check 90.
- **Left-shift gate:** the shim arm and the AC6 variant. Add a §10 checklist entry: "an ordering claim
  ('before X') observed on a fixture where X is a no-op is unobserved."

## M5 · id=7 — `--landed`'s write of status `landed` has no criterion

- **Address:** TOOL-aGraftedHelix-1 §6 AC9, against §2 S9.
- **Defect:** S9 says AC9 observes the `--landed` write of `landed`, but AC9 sequences `--hold`,
  `--resume` and `--abort` only.
- **Impact:** a landed run whose claim stays `live` ages to `stale` rather than `terminal`. The card
  shows it as stale until the one-day hide, and the take-over column reads "take, announced" where
  `terminal` would refuse. The local record's own terminal refusal (`refuse_if_terminal`) mostly
  closes the re-land path, so the effect is contained.
- **Fix — the skeptic judged it SOUND:** add a separate case: after `--landed`, the claim reads
  `status: landed` and `--claims` prints verdict `terminal`. Take the separate-case form, not an
  append to AC9's sequence: `--landed` after AC9's `--abort` would meet a terminal record.
- **Left-shift gate:** the new case becomes a suite arm.

## M6 · id=8 — the S13 documentation edits have no criterion, and render parity passes on an unedited template

- **Address:** TOOL-aGraftedHelix-1 §6 AC13, against §2 S13.
- **Defect:** AC13 asserts render parity and one `--claims` grep. `adopt-unattended.sh --check` passes
  whenever the template and its render agree, including when the template was never edited. The S13
  edits therefore have no criterion: STOPS §7, the STOPS §8 holder row, the SKILL holder sentence (F7)
  and the `check_single_live` comment.
- **Impact:** the rendered Skill can ship still saying that for the holder `--resume` writes nothing,
  which F7 states becomes false the day this lands. An unattended agent loading the Skill is told the
  opposite of what the driver does.
- **Fix — the finder's proposal was REJECTED by the skeptic; the skeptic's corrected fix:** read the
  files as one line before grepping, because the sentence wraps after "For the holder it" in both
  `tools/unattended/SKILL.template.md` (lines 38-39) and the rendered `.claude/skills/unattended/SKILL.md`.
  `tr '\n' ' ' < .claude/skills/unattended/SKILL.md | grep -c 'For the holder it writes nothing'`
  must print 1 at base `5266d22e` (observe that first) and 0 after the edit. Do the same with the
  template. Scope the STOPS probe to its sections:
  `awk '/^## 7\. /,/^## 9\. /' memory/guides/UNATTENDED-STOPS.md | grep -c claim` must print 0 at
  base and a non-zero count after the edit.
- **Left-shift gate:** the probes become AC13 assertions. Add a §10 checklist entry: "a grep for a
  sentence is observed matching at base before it is trusted to read 0 after; prose wraps."

## M7 · id=32 — the holder column takes a foreign `stale` claim, contradicting §1, S8 and the two-site hand-off

- **Address:** TOOL-aGraftedHelix-1 §4 "Who may write a claim" (holder column, foreign stale row),
  against §1, §2 S4 and S8, and the §3 Edges hand-off to TOOL-aGraftedHelix-8.
- **Defect:** §1 says a run that does not hold its claim cannot close, and S8 says `--close` refuses
  with check 90 then. Yet the holder column answers a foreign `stale` claim with "take, announced",
  and `--close`, `--dispatch` and the `--resume` holder row all run in holder mode. S4 and the unit-8
  hand-off call the stale take-over "a branch of its own at BOTH take-over sites", and the call-sites
  table names only `--preflight` and `run_takeover`. The table takes a stale claim in three columns.
  §5 risks says the displaced session's next claim read refuses it with check 90, which the table
  contradicts once the taker has itself gone stale.
- **Impact:** a displaced holder can re-take its successor's claim and close. CAS still lets at most
  one session close and the re-take is sequential, so the finder's "double drive" framing is
  overstated. What remains real: the text contradicts itself, and a take-over on the holder path falls
  outside the branch where unit 8 S5 sits its `claim-taken-over` event, so the health log misses it.
  AC10 covers only a foreign `live` claim.
- **Fix — the skeptic judged it SOUND:** make the holder column's foreign `stale` cell check 90 with
  the claim-lost remedy. A holder whose claim another session took has lost it, and the
  `same session` row already covers the holder's own restart. That makes S4's "both sites" and S8
  true. The `--replaces` path compares the claim against the record's own facts, so it stays `mine`.
  If re-taking is intended instead, amend §1 and S8, have S4 and Edges name three sites, and add an AC
  for `--close` over a foreign `stale` claim.
- **Left-shift gate:** an AC for `--close` and `--dispatch` over a foreign `stale` claim. Add a §10
  checklist entry: "a site count in prose ('both sites') equals the take branches in the decision
  table."

## M8 · id=46 — about twenty cells of the 8 × 4 write matrix have no criterion

- **Address:** TOOL-aGraftedHelix-1 §4 "Who may write a claim" and "Call sites"; §6.
- **Defect:** the matrix has eight claim-read rows and four modes. AC4 to AC12 observe only eleven
  cells. Unobserved cells include take-over × terminal (check 89, the spec's own guard against
  landing one slug twice), preflight × unknown and take-over × unknown (F3's "refuses like live"),
  preflight × held, the holder's `held`, `terminal` and `unknown` rows, the same-session rewrite and
  take, and status writes of `stale` and `unknown`. §7 lists "the verdicts, checks 89, 90 and 91" but
  promises no per-cell coverage. The OPEN ask TOOL-dDerivedDocket-40 recorded the same class for the
  resume matrix.
- **Impact:** any wrongly implemented cell ships with every arm green, the take-over × terminal guard
  included. H2 is the subset of these cells whose consequence is a double drive.
- **Fix — the finder's proposal was REJECTED by the skeptic; the skeptic's corrected fix:** add a
  table-driven arm to `tools/unattended/unattended.test.sh`. It seeds each claim state with real
  `gov-claim` messages over a bare remote, drives each of the four modes, and asserts each cell's
  outcome from §4. Give the matrix a reacher per cell, and mark a cell no path reaches as such. Cite
  TOOL-dDerivedDocket-40 in §10 as prior art, without a header verb: its subject is the resume matrix
  of TOOL-dDerivedDocket-4, which per-cell arms here do not move.
- **Left-shift gate:** the table-driven arm is itself the gate, provided it derives its cell list
  from the §4 table rather than from a second typed copy. The table-row join of H2 is the class gate.

## M9 · id=47 — claims ship always-on in every adopter, with no off switch and no ruling

- **Address:** TOOL-aGraftedHelix-1 §3 "A new conf key"; §4 Rollout.
- **Defect:** unit 1 is Tier-2, and §3 says no conf key turns claims off. Charter §1 requires Tier-2
  to land dark behind a default-OFF flag or as inert data; Rollout's "dark for every run preflighted
  before this lands" is not that. The last time a kit behaviour shipped ON, TOOL-dDerivedDocket-5
  recorded an owner ruling row plus an opt-out (`RESUME_SCHEDULE="off"`). Here no DECISIONS row of
  that shape records the choice, and the tick's `--beat` adds a remote push by standing configuration.
  The run mandate's ruling that claim-ref pushes need no ask covers the push authority, not shipping
  always-on.
- **Impact:** an adopter whose remote refuses `refs/gov/*`, or whose policy forbids refs outside
  branches, has every `--preflight` refused with check 91 after a kit update. Downgrading the kit is
  the only recourse.
- **Fix — the skeptic judged it SOUND:** add a claims switch, off in
  `tools/unattended/.unattended.conf.example` and on in gov's `.unattended.conf`. Alternatively, record
  a TOOL-dDerivedDocket-5-style ruling row naming the always-on choice and its opt-out, and scope the
  tick's `--beat` push explicitly. The skeptic adds one condition: the switch must read OFF when the
  key is absent, or adopters with an existing conf stay exposed until they add it.
- **Left-shift gate:** an arm asserting that a conf without the key never writes `refs/gov/`. Add a
  §10 checklist entry: "a Tier-2 spec that ships kit behaviour on names its default-OFF key or cites
  the ruling row that waives charter §1's dark landing."

## M10 · id=10 — the card's row cap, `… <m> more` row and verdict-first order have no criterion

- **Address:** TOOL-aGraftedHelix-2 §6 AC1, against §2 S6.
- **Defect:** S6 says AC1, AC4 and AC5 observe it. AC1 prints 5 rows, under the cap of 8, and asserts
  which rows appear but not their order. AC4 and AC5 are skip forms.
- **Impact:** S6 orders by verdict "so a busy remote cannot push a live claim off the card". A build
  that sorts by slug passes AC1 and drops a live claim past the cap on a remote with nine or more
  shown claims. The driver's own preflight still refuses, so the effect is contained to the card.
- **Fix — the skeptic judged it SOUND:** add an AC with ten kept claims whose live one sorts last by
  slug. Assert exactly 8 rows, the live claim on the first row, and a `… 2 more` row. Red when the
  live claim is missing, or the rows are in slug order.
- **Left-shift gate:** the new AC becomes a `manifest-check` suite arm.

## M11 · id=51 — the narrowing row records the network contact but not the card budget, and its wording is open

- **Address:** TOOL-aGraftedHelix-2 §2 S7; §5 perf / scale.
- **Defect:** S7 says a DECISIONS row records the read, "narrowing the no-fetch clause
  KICK-aReplayedCard-1 S8 set", and pins no wording. KICK-aReplayedCard-1 §5 also budgets the card at
  about 1.6 s quiet with no network. Unit 2 adds a driver start (1.89 s measured) plus a fetch under a
  15 s bound, and records the new walls only in its acceptance ledger. Unit 4's P1 grammar tags a
  record only on a `supersede`-family verb followed by the id, with `'s` or `for` marking the edge
  partial. A row that says "narrows" is invisible to it.
- **Impact:** recall keeps serving KICK-aReplayedCard-1's "no fetch" and its 1.6 s budget with no
  label, and a later change to the card reasons from a superseded ruling. That is the failure unit 4
  exists to fix, here on this build's own first narrowing.
- **Fix — the skeptic judged it SOUND:** pin the row text in S7 as
  `SUPERSEDES KICK-aReplayedCard-1's no-fetch clause and its card budget: ...`, with the new budget
  taken from AC10's measured figure. That form matches P1 under the partial rule, so unit 4 tags the
  record "partly superseded".
- **Left-shift gate:** at the close, run unit 4's `extract_supersessions` over the new DECISIONS row
  and assert a partial edge to KICK-aReplayedCard-1. Add a §10 checklist entry: "a row that narrows a
  ruling uses the `SUPERSEDES <id>'s` form, so recall labels it."

## M12 · id=12 — RUN INTEGRITY's by-design source is observed by a source grep

- **Address:** TOOL-aGraftedHelix-3 §6 AC7, against §2 S8.
- **Defect:** AC7 observes "RUN INTEGRITY states the by-design source" with `grep -c "By design:"`
  over the rendered harness. At base the string is absent (the harness has only the uppercase
  `BY DESIGN` at `tier2-review.js:741`), so the grep can fail. But any comment or dead literal the
  build adds satisfies it, including the header and `byDesign` comment S11 rewrites. AC6 observes only
  the prelude's log lines, which never reach the synthesis prompt.
- **Impact:** RUN INTEGRITY can omit or misstate the by-design source while every criterion passes,
  and a review record then cannot show which source its skeptics were primed with.
- **Fix — the skeptic judged it SOUND:** move the observation into AC6: the probe's emitted RUN
  INTEGRITY text carries `By design: <n> invariant(s) from the checklist's by-design block`, and the
  caller's-byDesign wording when `byDesign: 'x'` is given. Drop the source grep. The suite already
  observes RUN INTEGRITY by slicing the synthesis prompt (`tier2-review.test.sh:534`, `:631`, `:762`).
- **Left-shift gate:** the moved AC6 assertion, as a slice of the synthesis prompt. The presence-probe
  checklist entry of H4 covers the class.

## M13 · id=13 — the resolver's new instruction is replaced by a stub, and caller precedence is unobserved

- **Address:** TOOL-aGraftedHelix-3 §6 AC8, against §2 S9.
- **Defect:** S9's substance is the resolver agent's new instruction: collect the Files-touched paths,
  run `--for-paths`, and return the stdout verbatim plus `checklistPaths`. AC8 replaces that agent with
  a stub that already returns `checklist`. Nothing observes that the rendered prompt carries the
  instruction (`unattended-build.template.js:778-787`). §4's rule that a caller-supplied `checklist`
  wins over the resolver's is a new argument, and no criterion observes it either.
- **Impact:** if the prompt edit is missing or wrong, every real spec audit logs `WARNING:` and runs
  without a checklist, which is the gap S9 exists to close, while AC8 stays green. The failure is
  announced rather than silent, so the effect is contained.
- **Fix — the skeptic judged it SOUND:** add to AC8: the rendered `tools/workflows/unattended-build.js`
  resolver prompt names `gotchas.py --for-paths` through the `{{MEMORY_TREE_DIR}}`-rendered path and
  `### Files touched`. Given a caller `checklist` argument alongside a resolver one, the audit receives
  the caller's.
- **Left-shift gate:** the two AC8 assertions. Add a §10 checklist entry: "a stub that replaces the
  component under change observes nothing about that component."

## M14 · id=14 — no arm for an invariant whose every anchor is append-only

- **Address:** TOOL-aGraftedHelix-3 §6 AC2, against §2 S3 and the §4 grading table row "not inert".
- **Defect:** S3 and the grading table require invariant anchors that reach more than the append-only
  tree (`inert_only()`), and S3 says AC2 observes it. AC2's explicit arm list holds an unanchored and a
  universal invariant, but no inert-only one. The existing "check 19 catches INERT anchors" arm covers
  `kind: class` only, because `cmd_check`'s loop skips every non-class record (`gotchas.py:275`), so
  the invariant branch is new code.
- **Impact:** an invariant anchored only on `memory/DECISIONS.md` passes check 19. It then reaches
  every review that touches the decision log and none that touches the code it describes. The effect
  is a by-design line that is dead on code reviews.
- **Fix — the skeptic judged it SOUND:** add to AC2's arm list: an invariant whose only anchor resolves
  to an append-only path is a check 19 finding, observed FAIL with `inert_only()` disabled.
- **Left-shift gate:** the new `gotchas.py` self-test arm, observed RED with the predicate disabled.

## M15 · id=50 — a caller's `byDesign` replaces the invariant block, though the two are different inputs

- **Address:** TOOL-aGraftedHelix-3 §2 S8; §4 "The harness — reading I4 out of checklist" step 5.
- **Defect:** the block becomes `byDesign` only when `args.byDesign` is absent, so a caller's value
  replaces the invariants wholesale. The harness's args contract defines `byDesign` as
  "known/tracked issues reviewers must NOT re-report" (`tier2-review.template.js:76`), and charter §8
  feeds reviewers tracked issues through it. Tracked issues and intended behaviour are different
  inputs. §5's "a block cannot override an explicit instruction" does not justify replacing, because
  concatenating overrides nothing.
- **Impact:** any run whose caller passes its tracked-issue list (the spec measured 14 of 464 records)
  loses every invariant its diff selected. Reviewers then re-report intended behaviour, and a skeptic
  can confirm a "fix" that breaks a ruling. The loss is logged but the invariants are not delivered.
- **Fix — the skeptic judged it SOUND:** concatenate the two: the caller's `byDesign` first, then the
  block's entries, each labelled. Keep the header-count check, log both sources and their counts, and
  carry both in the RUN INTEGRITY `By design:` clause. AC6's `byDesign: 'x'` case must then assert that
  both sources appear.
- **Left-shift gate:** the amended AC6 case. Add a §10 checklist entry: "an argument with a defined
  contract is not a free slot; read the args contract before giving it a second meaning."

## M16 · id=16 — the supersession order step has no fixture

- **Address:** TOOL-aGraftedHelix-4 §6 AC7, against §2 S5 and S10.
- **Defect:** S10 promises self-test arms for "the order step" and cites AC7 and AC9. AC7 enumerates
  extraction and map cases only, and AC9 is the version check. AC3 is one live case with one
  successor. S5's rules for two successors (land after the lowest-ranked one), a successor ranked
  above (no move, since the step moves only down) and preserved relative order have no fixture. AC4
  does observe a partial hit keeping its rank.
- **Impact:** a mis-ordering separates a label from its successor. §4 notes that the P3 headers name
  several successors, for example TOOL-aClosedDocket-4 with three. The effect is contained.
- **Fix — the skeptic judged it SOUND:** add an AC7-style fixture probe of
  `derive_supersession_order` over synthetic hit lists. Cover a successor below (moves to directly
  after it), a successor above (keeps rank), a successor absent (keeps rank), two successors (lands
  after the lower one) and a partial edge (keeps rank). Assert that the other hits keep their relative
  order.
- **Left-shift gate:** the fixture probe becomes `selftest.py` arms.

## M17 · id=18 — two of S1's three `unknown` conditions have no criterion

- **Address:** TOOL-aGraftedHelix-5 §6 AC3, against §2 S1.
- **Defect:** S1 names three `unknown` conditions and claims AC1 to AC3 observe them. AC3's stub only
  exits 1. A header with no PID or PPID column, and a snapshot with no row for the runner itself (§4
  step 5), have no AC and no §7 staged break.
- **Impact:** these are the cases where the census cannot see what it measures. A build that returns
  `0` there stamps every reading `foreign 0`, which is admitted as faithful, so contended readings
  argue ceilings on exactly the hosts where the census is blind. Ceilings only rise, so the harm is
  inflated evidence, the status quo before this unit.
- **Fix — the skeptic judged it SOUND:** extend AC3 with two `ps` stubs: one printing a header without
  PID or PPID columns, and one printing a valid table that omits the runner's pid. Each must make every
  `.leg` row's `foreign` field read `unknown`.
- **Left-shift gate:** the two stubs become run-gates suite arms. The charter §7 rule "a probe that
  cannot move says so" is the class; this is its fixture.

## M18 · id=35 — the first census sample is promised before dispatch but placed in a detached subshell

- **Address:** TOOL-aGraftedHelix-5 §2 S2, against §4 "The sampler".
- **Defect:** S2 puts the census file's truncation and its first sample inside the detached sampler.
  §4 claims the first sample is taken before the first leg dispatches, "so every leg has one inside
  its window". A backgrounded subshell gives no such ordering. The `ts_tick_start` shape it copies
  (`run-gates.sh:849-869`) does all its work after `&` with its stdio on `/dev/null`, so S2's
  `run-gates: NOTE` line for a first sample reading `unknown`, which AC3 requires, also cannot come
  from inside it.
- **Impact:** first-wave legs shorter than one loaded `ps -ef` (0.4 s to 3.2 s, per §4) can end before
  any sample lands, read `unknown` and be set aside as uncensused. A fast first leg on a reused run id
  can read the stale samples the truncation exists to discard. A reading can only be set aside, never
  admitted, so the effect is contained. The skeptic re-graded this from low to medium.
- **Fix — the skeptic judged it SOUND:** in `arm_census`, do the truncation and the first sample
  synchronously (about 52 ms) before returning to the dispatch loop, and detach only the periodic loop.
  Alternatively, drop the §4 claim and add an AC with a sub-second first-wave leg.
- **Left-shift gate:** an AC with a sub-second first-wave leg whose row carries a census count. Add a
  §10 checklist entry: "a detached subshell gives no ordering against its parent."

## M19 · id=43 — the `--observed` path bypasses the census filter, and a ratified ruling says it must stay admissible

- **Address:** TOOL-aGraftedHelix-5 §2 S5 and S6; §3.
- **Defect:** unit 5 filters only `read_runs`. `derive-ceilings.py --write --observed '<leg>=<seconds>'
  --how ...` (lines 469-494) writes an evidence row directly, never goes through `read_runs`, and
  carries no census. Its docstring (line 26) and `DECISIONS.md:198` record TOOL-cMendedVintage-17:
  a reading taken outside the runner is admissible, and has to be. The spec never names this path.
- **Impact:** the unit's goal, that the evidence tool argues only from readings whose census found
  none, stays false on the one manual path. The docstring, README and evidence-header text S6 writes
  would claim more than the code enforces. A builder who instead closes the path reverses a ratified
  decision with no record.
- **Fix — the skeptic judged it SOUND:** name TOOL-cMendedVintage-17 in §3 or §4 and decide the path
  explicitly. One option: keep `--observed` admissible as a declared exception whose `--how` text must
  state the load it was taken under, and say so in the docstring, the README and the evidence header
  S6 renders.
- **Left-shift gate:** an arm asserting that `--observed` without a load statement in `--how` is
  refused, if that option is taken. Add a §10 checklist entry: "a filter claimed to cover every
  reading enumerates every writer of the filtered table."

## M20 · id=21 — the cross-document identity exemption is not observed under `snapshot` rotation

- **Address:** TOOL-aGraftedHelix-6 §6 AC3, against §2 S3.
- **Defect:** S3 exempts a key held under one identity across documents, a `snapshot` carry-forward
  being that by design. AC3's "one id twice with one text" does not place the copies in different
  documents, so a build keyed on (path, id) passes it. This repository declares `ROTATION_MODE="cut"`
  (`.memory-tree.conf:483`), so AC5's real-tree run never sees a carry-forward. The shipped example
  declares `snapshot` (`.memory-tree.conf.example:240`), and `scan_records` takes the index and its
  archives.
- **Impact:** a mis-keyed build reds every carried-forward row in a default adopter, on every hygiene
  run, and passes AC1 to AC9 here. The red is loud and contained.
- **Fix — the skeptic judged it SOUND:** make AC3's same-id fixture a decision index and an archive
  under `ROTATION_MODE=snapshot`, both holding one id with one text. Assert no `check 28:` line.
- **Left-shift gate:** the amended fixture becomes a `row_grammar.py --selftest` arm.

## M21 · id=48 — check 28 grades landed append-only rows in every adopter, with no pin and no conf key

- **Address:** TOOL-aGraftedHelix-6 §3 "A shrink-only pin or a waiver registry"; §4 Rollout.
- **Defect:** check 28 grades the whole corpus: the decision index, its frozen archives and the
  gotchas. It ships in the memory-tree kit with no pin, waiver or conf key, justified only by gov's own
  census of 0. Landed decision rows may never be edited or removed (charter §6), and
  TOOL-cSpliceWarden-4 repairs archives only by supersession. Check 20 needed `ROW_DUPLICATE_PIN` and
  `--emit-pin` (`.memory-tree.conf.example:268-271`) for the same adopter case, TOOL-cSpliceWarden-3
  kept check 20 off files nobody may edit, and sibling unit 9 ships its key blank because a floor
  measured on gov's corpus is not a floor for another.
- **Impact:** an adopter whose landed decision rows already share a normalized key goes red on the
  memory-hygiene leg at kit update and stays red. The spec's remedy, "fold the two into one", is
  illegal for landed append-only rows, and superseding one adds a row without removing the duplicate.
- **Fix — the skeptic judged it SOUND:** grade only records added since the mainline merge-base, as
  check 27 does. Alternatively, ship a shrink-only content-duplicate pin, or ship the check dark in
  the kit's example conf. In either case, state the adopter path in §3.
- **Left-shift gate:** an arm over a fixture holding two landed duplicate rows below the merge-base,
  asserting no red. Add a §10 checklist entry: "a whole-corpus check shipped to adopters is argued on
  a corpus other than gov's, or ships dark; gov's census of 0 is not evidence about another corpus."

## M22 · id=33, id=41 — the hold bound is tested only at the next leg completion, so S4, §4, §5, F1 and AC6 misstate it

- **Address:** TOOL-aGraftedHelix-7 §2 S4; §4 "The decision" (rule 5, and "each episode releases one
  leg per MEMPAUSE_HOLD"); §5 perf / scale; §8 F1; §6 AC6 Red when.
- **Defect:** S4 says a hold ends `bound` once the episode has held `MEMPAUSE_HOLD` seconds. §4, §5
  and F1(a) state the same bound three more ways. But §4 also says a decision happens when a leg
  completes and nothing polls: a hold leaves the inner loop and blocks on `wait -n` with no timeout
  (`run-gates.sh:3080`). The bound is therefore tested only at the first completion after it expires.
  Traced through AC6 with `HOLD=2`: B ends at 1 s and D is held; C ends at 4 s, releasing D `bound`
  after 3 s while A and C ran; E is held from about 4 s until A ends at 8 s, closing `drained`. AC6's
  expected `drained` row can arise only by violating its own Red-when, "a held dispatch waits past the
  bound while legs still run".
- **Impact:** a hold can last as long as the longest running leg, which the charter's bar notes
  measure at 1565 s; unit 5 F2 counts 46 legs of 60 s or more. The stated bound and the F1 worst-case
  reasoning are wrong, though F1's conclusion holds because at least one leg always runs. AC6 as
  written either reds a faithful build or pushes the builder into the polling §4 rejects.
- **Fix — the skeptic judged both SOUND:** restate the bound in S4, rule 5, §5's risk row and F1's
  worst case as "released at the first leg completion after MEMPAUSE_HOLD seconds; a hold lasts at
  most until then". Rewrite AC6's Red-when to that semantics: a held dispatch survives a completion
  that occurs after the bound while legs still run. If a hard wall-clock bound is actually wanted,
  specify the wake mechanism, show it takes no pool slot, and price it.
- **Left-shift gate:** the rewritten AC6 is the regression arm. Add a §10 checklist entry: "a bound in
  a non-polling loop is checked at the next event, not at expiry; trace the AC's own fixture under the
  stated bound before writing its Red-when."

## M23 · id=40 — the runner's forced-progress branch is a second dispatch site with no pause decision

- **Address:** TOOL-aGraftedHelix-7 §4 "The decision" (the call site, and "only the wall's break can
  leave" an episode open); §2 S4 and S5.
- **Defect:** §4 assumes every dispatch passes through the inner-loop call site.
  `run-gates.sh:3086-3091` runs `runleg $k &` with no per-leg hook, not even `arm_wall`, when nothing
  is live, legs remain and the inner pass dispatched nothing (`di == di_before`). A hold steps `di`
  back, which leaves `di == di_before`, and the decision's running count is captured from the inner
  condition rather than re-asked. If the running legs finish between that capture and the outer
  `$(live) -gt 0` test, the held leg is force-dispatched there and its episode is never closed
  `drained`. The runner's own comment (6 of 30 legs) measures this window as common.
- **Impact:** a later decision closes the episode `fell` or `bound` with held seconds that include
  time when nothing was paused. When the forced leg is the last one, the episode survives the loop and
  is closed `wall` although no wall fired, contradicting §4. S7's overlap join then sets aside, as
  `paused`, readings of legs that ran while nothing was held. The effect is limited to the summary
  line, the verdict's `paused_s` and the set-aside counts.
- **Fix — the skeptic judged it SOUND:** name the forced-progress branch in §4 and route it through
  `check_dispatch_pause` with `running=0`, so rule 4 closes the episode `drained` and dispatches.
  Alternatively, call `write_pause_row drained` there. Add an arm that stages the race: a held decision
  with one running leg that exits before the outer liveness test, asserting a `drained` row and no
  `wall` close.
- **Left-shift gate:** the staged-race arm. Add a §10 checklist entry: "before hooking 'the' dispatch
  site, enumerate every `runleg … &` in the runner."

## M24 · id=24 — the Python appender's never-raises contract has no criterion

- **Address:** TOOL-aGraftedHelix-8 §6 AC1 and AC2, against §2 S1 and §4 "The shared block".
- **Defect:** §4 pins the contract for both languages: one `health: NOTE -` line, nothing written, and
  for Python, returns None and never raises. AC1 drives the empty-path, refused-token and
  missing-directory branches through the bash copy only. AC2 and the S2 behaviour arm call the Python
  copy on the happy path only.
- **Impact:** §5 names a real empty-path case: `reap.py` run from a root outside any repository. A
  Python copy that raises there turns a completed kill into a traceback and a non-zero exit, which the
  gate runner's teardown and the driver's orphan reap read as a failed reap. The effect is contained to
  the reaper's exit status.
- **Fix — the skeptic judged it SOUND:** add to AC2: `reap.add_health_event('', 'reap',
  'tree-killed', 'x')`, the same call with event `Bad`, and a path inside a missing directory each
  return None, print one `health: NOTE -` line on stderr, and raise nothing.
- **Left-shift gate:** the three calls become arms in the Python copy's self-test. Add a §10 checklist
  entry: "a contract pinned for two language copies is observed on the failure paths of both."

## M25 · id=25 — AC5 proves call presence, not that each call sits in its branch

- **Address:** TOOL-aGraftedHelix-8 §6 AC5, against §2 S3, S5 and S6.
- **Defect:** AC5 is a `git grep` for presence, and its Red-when checks placement only for
  `tree-killed`. S3 claims AC4 and AC5 observe `merge-driver-set`, but AC4 exercises only the hooks
  arm. §7 has no behaviour arm for `merge-driver-set`, `turnstile-expired`, `scratch-swept` or
  `ticket-swept`. At base, `check-wiring.sh:1089-1100` shows the merge arm's FIXED branch beside an
  `ok` branch. `run-resumed` is covered by §7's resume-tick arm.
- **Impact:** a merge-arm call placed on the `ok` branch writes `merge-driver-set` on every
  SessionStart. The card then reports a self-heal in every session and its count stops meaning
  anything, while AC5 stays green.
- **Fix — the skeptic judged it SOUND:** extend AC4 to the merge arm: with `merge.rows.driver` unset,
  the first `--session` appends one `merge-driver-set` line and a second run appends none. Note in AC5
  that it proves presence only, and name the §7 arm that proves placement for each other site.
- **Left-shift gate:** the extended AC4 arm. The presence-probe checklist entry of H4 covers the class.

## M26 · id=28 — the no-argument base derivation has no criterion, though the production caller uses it

- **Address:** TOOL-aGraftedHelix-9 §6, against §2 S2.
- **Defect:** S2's no-argument derivation, reimplemented in Python as `derive_relation_base`, takes the
  merge-base of `origin/<branch>` and HEAD, falls back to `<branch>`, and reads `<branch>` from
  `GOV_DEFAULT_BRANCH`. AC1 to AC4 and AC12 pass an explicit base, AC8 and AC9 pass `5266d22e`, and
  AC7 observes only the no-base refusal and base equal to HEAD. The hygiene dispatch, which is the
  production caller, passes no argument.
- **Impact:** a derivation that takes the branch tip, prefers a stale local `main`, or ignores
  `GOV_DEFAULT_BRANCH` grades the wrong added set. Records another node already landed get findings
  their author cannot change, or a branch's own records go ungraded. The effect is wrong findings on
  one range.
- **Fix — the skeptic judged it SOUND:** add a `--selftest` arm: a fixture with `origin/main` behind a
  local `main`, and a branch adding one restated row. `--check-relations` with no argument names the
  merge-base as `<base8>` and grades exactly that row. With `GOV_DEFAULT_BRANCH=trunk` and only
  `trunk` present, it resolves `trunk`.
- **Left-shift gate:** the new self-test arm.

## M27 · id=29 — nothing observes that the kit's example conf ships `NEAR_MATCH_GATE` blank

- **Address:** TOOL-aGraftedHelix-9 §6, against §2 S5.
- **Defect:** S5 says the kit's example conf declares `NEAR_MATCH_GATE` blank, "because a floor
  measured on gov's corpus is not a floor for another corpus". S5 cites AC1, AC4, AC5 and AC6, none of
  which reads `tools/memory-tree/.memory-tree.conf.example`. The existing example-conf arm
  (`check-memory-hygiene.test.sh:2411-2428`) derives its keys from the shell engine's validation loop
  and checks only that a key is declared, never its value; this key is read by `row_grammar.py`. The
  "too old" recall-kit refusal is also unobserved, since AC6 seeds only an absent `bench.py`.
- **Impact:** an example conf shipped with `red:0.125` arms check 27 red in every new adopter at a
  floor never measured on its corpus, which is the outcome S5's own reason rules out.
- **Fix — the skeptic judged it SOUND:** add to AC11: `grep -n '^NEAR_MATCH_GATE=""'
  tools/memory-tree/.memory-tree.conf.example` prints one line, and
  `grep -n 'NEAR_MATCH_GATE="red:0.125"' .memory-tree.conf` prints one line. This leaves the "too old"
  refusal unobserved, which is outside the impact the finding names; a fold may add an arm for it.
- **Left-shift gate:** extend the example-conf arm in `check-memory-hygiene.test.sh` to assert the
  VALUE of every key a kit declares must ship blank, including keys read by `row_grammar.py` rather
  than the shell engine. That one arm also covers L4 (id=15).

# LOW

## L1 · id=9 — AC11 lists only `live` and `landed`, and the HALT_FLOOR rise has no criterion

- **Address:** TOOL-aGraftedHelix-1 §6 AC11 and AC7, against §2 S6 and S12.
- **Defect:** AC11 seeds only a `live` claim and a `landed` one, so the listing of `held`, `stale` and
  `unknown` claims of other slugs is unobserved. S12 raises `HALT_FLOOR` from 7 to 8 in both conf
  files and says AC7 observes it, but AC7 observes only that `--abort --code claim-lost` is accepted.
  `check-unattended.sh` compares `nhalt -ge HALT_FLOOR`, so a floor left at 7 passes.
- **Impact:** the announcement can omit stale, held or malformed claims of other slugs, and the floor
  can stay at 7, so `claim-lost` can later be dropped silently. Neither changes behaviour today.
- **Fix — the finder's proposal was REJECTED by the skeptic; the skeptic's corrected fix:** seed
  AC11's remote with one claim of another slug per verdict: `live`, `stale`, `held`, `unknown` and
  `terminal`. Assert four are listed and the terminal one is absent. Add
  `grep -c '^HALT_FLOOR="8"$' .unattended.conf tools/unattended/.unattended.conf.example`, which must
  report 1 for each file. Both files spell the key quoted (`.unattended.conf:313`,
  `.unattended.conf.example:346`).
- **Left-shift gate:** the seeded AC11 and the quoted-form grep. Consider whether the floor should be
  derived from the declared halt codes, so a new code cannot be added without the floor moving.

## L2 · id=11 — the no-driver form, the no-`timeout -k` skip and the stdin redirect have no criterion

- **Address:** TOOL-aGraftedHelix-2 §6, against §2 S3 and S4.
- **Defect:** S3 says AC7 observes the `claims — skipped: no unattended driver resolves in this tree`
  form, but AC7 runs only the install-prefix leg. The no-working-`timeout -k` skip that "runs no read",
  and stdin redirected from `/dev/null`, are also unobserved. The resolvers check `-f`, so a deleted
  driver reaches the untested branch.
- **Impact:** with a conf but no driver, the cell can print a bash error or run `bash ''`. Without
  `timeout -k`, the read can run unbounded inside the SessionStart hook. Without the stdin redirect,
  the hook's never-closing pipe holds the read until the bound fires on every card write. The effect is
  limited to the card cell and the hook's time, which the harness bounds.
- **Fix — the finder's proposal was REJECTED by the skeptic; the skeptic's corrected fix:** add two
  cases: a deleted driver gives the no-driver form, and a failing `timeout -k` shim gives the skip
  with a stub driver's marker file absent. Add a stdin case: replace the driver with a stub that runs
  `cat >/dev/null` and then prints `claims: none`. Write the card as
  `sleep 30 | bash skills/session-kickoff/manifest-check.sh --card --write --session t2` with
  `CARD_CLAIMS_BOUND=2`, and assert the cell reads `claims — none on the remote`. A build that lets the
  hook's pipe reach the driver's stdin fires the bound and prints the skipped form.
- **Left-shift gate:** the three cases become `manifest-check` suite arms.

## L3 · id=52 — §5 says nothing reads the driver's run log, and the runlog kit does

- **Address:** TOOL-aGraftedHelix-2 §5 risks.
- **Defect:** §5 says the card's `--claims` call adds START and END lines to a run log "which nothing
  reads back". `runlog_lib.PRODUCER_FILES` maps `driver` to `driver.log`
  (`tools/runlog/runlog_lib.py:40`). The driver journals every verb except `--version` and `--plan`
  (`unattended.sh:10405-10412`), and unit 1 does not add `--claims` to that list.
- **Impact:** every session start in an adopting tree adds a slug-less invocation pair to the journal
  the runlog CLI and Skill answer run questions from. The risk is assessed against a reader that does
  exist; the effect is noise.
- **Fix — the skeptic judged it SOUND:** run the card's driver call with `GOV_RUNLOG=0`, the driver's
  documented switch that writes no line (`unattended.sh:10406`). Otherwise, state the added journal
  noise in §5.
- **Left-shift gate:** an arm asserting that a card write appends nothing to `driver.log`. Add a §10
  checklist entry: "a 'nothing reads it' claim is grepped against every reader first."

## L4 · id=15 — three failure forms in unit 3 have no criterion

- **Address:** TOOL-aGraftedHelix-3 §6, against §2 S6 and §4 "Grading".
- **Defect:** a set `LEG_MANIFEST` naming an unreadable file must be a named HYGIENE failure, never a
  traceback. The second announcement, when the id grammar's kit is absent, is specified. S6 says the
  shipped `.memory-tree.conf.example` declares `LEG_MANIFEST` blank and cites AC2 and AC3, but neither
  reads that file. AC2 has only the blank-key announcement.
- **Impact:** an adopter whose example conf ships `tools/gate-legs.json`, a file it lacks, or whose tree
  lacks the id-grammar kit, can get a traceback or a red hygiene leg where the spec promises an
  announcement. Only adopter-only paths are affected.
- **Fix — the skeptic judged it SOUND:** add arms to AC2: `LEG_MANIFEST` naming a missing file prints a
  HYGIENE line and no traceback, and the grammar kit absent prints `NOT resolved` and exits 0. Add
  `grep -n '^LEG_MANIFEST=""' tools/memory-tree/.memory-tree.conf.example` to AC11.
- **Left-shift gate:** the AC2 arms, and the example-conf value arm proposed under M27.

## L5 · id=17 — the `emit(full=True)` tag and the multi-id tag form have no criterion

- **Address:** TOOL-aGraftedHelix-4 §6, against §2 S6.
- **Defect:** S6 requires the tag in `render()` and in `emit(full=True)`, plus the form
  `[superseded by <id>, <id>]`. AC3 and AC4 run the default render with one successor each, and AC7
  checks the two-id P3 case only at map level. The full branch is not user-facing: `query.py:823` says
  `full=True` is not a CLI flag and exists only for byte measurement.
- **Impact:** a record with two successors can show one. That is cosmetic.
- **Fix — the finder's proposal was REJECTED by the skeptic; the skeptic's corrected fix:** add a
  `selftest.py` arm that calls `QRY.emit(hits, q, budget, full=True)` directly, as `selftest.py:2124`
  already does, over a hit list carrying a whole-superseded hit, and assert the header carries
  `[superseded by <id>]`. Add a `render()` arm over a hit annotated with two whole successors, and
  assert both ids appear in one `[superseded by <id>, <id>]` tag.
- **Left-shift gate:** the two `selftest.py` arms.

## L6 · id=34 — unit 4's hand-off to unit 9 names an interface unit 9 explicitly rejects

- **Address:** TOOL-aGraftedHelix-4 §3 Edges (hands off TOOL-aGraftedHelix-9), against unit 9 §2 S4
  and §4 "The predicate" step 5 and "Alternatives rejected".
- **Defect:** unit 4's hand-off says unit 9 queries this index and sees the supersession map in the
  cache manifest and each hit's supersession fields. Unit 9 builds its own in-memory
  `bench.build_index`, refuses to read `manifest.json` or the served query cache, and calls
  `extract_supersessions` and `derive_supersession_map` directly. Unit 4 also says a record declaring a
  supersedes relation becomes a P1 edge, but P1 needs an id after the verb, and unit 9 step 5 accepts a
  bare `supersedes`.
- **Impact:** the contradiction sits only in the hand-off text. Unit 4's own S4 to S6 already require
  the manifest key and the per-hit fields for its own render, and a bare token not reaching the map is
  unit 9's deliberate choice. Built as written, nothing behaves differently. The skeptic re-graded this
  from medium to low.
- **Fix — the skeptic judged it SOUND:** rewrite the edge to the interface unit 9 actually consumes:
  `extract_supersessions` and `derive_supersession_map` called directly, with no manifest or hit
  fields. Drop the P1-edge sentence, or state that only `supersedes <id>` reaches recall. Optionally,
  have unit 9's finding remedy text suggest `supersedes <id>`, so the declared relation also reaches
  the map.
- **Left-shift gate:** add a §10 checklist entry for spec audits: "each Edges hand-off is read against
  the receiving spec's own interface section."

## L7 · id=19 — `.retry.leg` rows' eighth field and the positive-beats-unknown precedence have no criterion

- **Address:** TOOL-aGraftedHelix-5 §6, against §2 S3.
- **Defect:** S3 says `.retry.leg` rows gain the eighth field too, and `derive-ceilings.py`'s glob
  `gate-run/*/*.leg` (line 209) reads them as evidence. No AC runs a deferred serial retry. S3's rule
  that the largest positive count beats an `unknown` sample in the same window is unobserved too,
  because AC1, AC3 and AC5 each produce a uniform window.
- **Impact:** retry readings, the least contended a bar takes, can be written with seven fields and
  set aside as `uncensused`. A mixed window can read `unknown` instead of `contended`. The effect is
  lost evidence or a different set-aside reason, never a wrong ceiling.
- **Fix — the skeptic judged it SOUND:** add an AC with a leg that times out and passes on the serial
  retry, asserting that the `.retry.leg` row has eight fields. Add a census fixture holding `unknown`
  and `2` inside one leg's window, asserting `foreign` reads 2.
- **Left-shift gate:** the two cases become run-gates suite arms.

## L8 · id=45 — unit 5's header does not advance the OPEN ask it answers

- **Address:** TOOL-aGraftedHelix-5 status header; §10.
- **Defect:** TOOL-aSurfacedLexicon-22 is OPEN (`memory/backlog/TOOL.md:264`). It records a ceiling
  row written twice from contended readings and asks the runner to report pool width and neighbour
  count beside a kill. Unit 5's mechanism answers it, yet §10 cites it only as a recall hit and the
  header carries no `advances` or `closes`, although `BACKLOG_MODE` is `builds`
  (`.memory-tree.conf:636`) and unit 1 uses `advances` for its own ask.
- **Impact:** the generated asks index keeps showing the ask OPEN with no linked spec. Product
  behaviour does not move, which is why the skeptic re-graded this from medium to low.
- **Fix — the skeptic judged it SOUND:** add `advances TOOL-aSurfacedLexicon-22` to the status header,
  or `closes` if the stamped kill row discharges it, and say in §4 which of the ask's candidates the
  `foreign` field answers.
- **Left-shift gate:** add a §10 checklist entry: "every OPEN ask a spec's §10 cites is either named
  `advances` or `closes` in the header, or ruled unrelated in one line."

## L9 · id=22 — the empty-key branch and three-holder keys have no fixture

- **Address:** TOOL-aGraftedHelix-6 §6, against §2 S3.
- **Defect:** S3's "an empty key is not graded and is counted" is a distinct branch, and S5 requires a
  fixture arm for every new branch. AC4's empty population is a different case. Three or more holders
  of one key are unobserved too.
- **Impact:** two front-matter-only gotchas, or two rows whose summary normalizes to nothing, can red
  each other, and a three-holder finding can name two. The real tree measured 0 empty keys, so both
  paths are rare.
- **Fix — the skeptic judged it SOUND:** add a `--selftest` arm with two records whose keys normalize
  to empty, asserting no `check 28:` line and `<e>` of 2 in the summary. Add one arm with three holders
  of one key, asserting that the finding names all three.
- **Left-shift gate:** the two self-test arms.

## L10 · id=23 — the `unread` and `wall` end reasons, and the wall-stopped summary, have no criterion

- **Address:** TOOL-aGraftedHelix-7 §6, against §2 S4 and S5.
- **Defect:** S4 lists five end reasons and cites AC5 and AC6. AC5 produces only `fell`, and AC6
  produces `bound` and `drained`. No criterion produces `unread` (rule 2 of the decision) or `wall`.
  S5's "in all three of its writers" is observed only on AC5's normal verdict path, and §4's claim that
  a wall-stopped run still prints the summary line is unobserved.
- **Impact:** an unreadable meminfo mid-hold can hold until the bound instead of releasing, and a
  wall-stopped run can omit its open episode from `pauses` and its verdict keys. Both stay inside one
  bar's record.
- **Fix — the skeptic judged it SOUND:** add an AC5 variant whose leg A deletes the `GATE_MEMINFO` file
  instead of rewriting it, asserting a row ending `unread`. Add a `GATE_WALL` fixture that fires during
  a hold, asserting a `wall` row, the verdict's `paused` keys and one `memory:` line.
- **Left-shift gate:** the two variants become run-gates suite arms.

## L11 · id=26 — AC2's "fires at 499" red condition cannot occur with a 500-line fixture

- **Address:** TOOL-aGraftedHelix-8 §6 AC2, Red when.
- **Defect:** AC2 seeds exactly 500 lines. A trim at 500 or more and an off-by-one trim at 499 or more
  both fire on 500 lines and leave 251, so the 499 condition is unobservable.
- **Impact:** an off-by-one cap passes. The effect is one line of log length.
- **Fix — the skeptic judged it SOUND:** add a second fixture of 499 lines and assert that the file
  holds 500 lines after one append, with no trim.
- **Left-shift gate:** the 499-line arm. Add a §10 checklist entry: "a threshold is fixtured on both
  sides of its boundary."

## L12 · id=30 — AC9 states an equality and checks only non-zero

- **Address:** TOOL-aGraftedHelix-9 §6 AC9.
- **Defect:** AC9 states that the graded count equals the rows and gotchas added since `5266d22e`, but
  its Red-when fires only when the count is 0 while a gotcha file was added. It never derives the
  expected count.
- **Impact:** a miscounted added set, such as dropped rows or a missed archive, passes as long as the
  count is non-zero.
- **Fix — the finder's proposal was REJECTED by the skeptic; the skeptic's corrected fix:** derive the
  expected count as an identity set difference. Count the gotcha stems listed by
  `git ls-tree --name-only HEAD memory/gotchas/` that are absent from the same listing at `5266d22e`,
  excluding `INDEX.md`; equivalently, use `git diff --no-renames --name-only --diff-filter=A`. Add the
  keyed ids present across the decision index and its archives at HEAD and absent from them at
  `5266d22e`. Red when the summary's graded count differs from that figure.
- **Left-shift gate:** the derived equality. Add a §10 checklist entry: "an added-set count uses
  `--no-renames` and an identity set difference, never added diff lines."

## L13 · id=36 — §7 says no pass runs the `--selftest` its own ACs observe with

- **Address:** TOOL-aGraftedHelix-9 §7 Gates (closing sentence), against §6 AC1 to AC7 and AC12. The
  identical sentence sits in TOOL-aGraftedHelix-6 §7 over its AC1 to AC4.
- **Defect:** §7 lists `row-grammar selftest`, whose argv is
  `python3 {prefix}/memory-tree/row_grammar.py --selftest` (`tools/gate-legs.json:442-447`), and then
  says "The close runs these; no pass does". AC1 to AC7 and AC12 name that same command as their
  observation, and brief invariant 11 lets a pass verify with a `--selftest` arm.
- **Impact:** a pass that obeys §7 cannot observe its own criteria, or see each new arm RED on a staged
  break. The ACs and invariant 11 make the intent recoverable, so shipped behaviour is unaffected.
- **Fix — the skeptic judged it SOUND:** in both specs, state that the pass runs
  `row_grammar.py --selftest` as its direct check, staged break included, and that the close runs the
  listed bar legs.
- **Left-shift gate:** add a §10 checklist entry: "a spec's §7 'no pass runs these' list excludes every
  command its §6 criteria name as the observation."

## L14 · id=37 — units 9 and 6 move `BUILD-METHOD.md` line 1 without citing unit 3's ruling

- **Address:** TOOL-aGraftedHelix-9 §2 S9 and §4 Files touched (and TOOL-aGraftedHelix-6 S6), against
  the spec brief's shared invariant 10.
- **Defect:** line 1 of `memory/guides/BUILD-METHOD.md` is `<!-- gov:kit memory-tree@2.118 -->`, a
  carrier the memory-tree bump re-renders. Brief invariant 10 says no unit edits that file. Unit 3
  resolves exactly this in its §8 F1 (Option A), with AC12 checking that only line 1 changed. Units 9
  and 6 bump memory-tree "in every carrier" but neither cites that ruling, lists the file, nor observes
  a line-1-only diff.
- **Impact:** the shipped change is the same marker line unit 3 already accepted. The defect is
  traceability: two units move a carrier the brief forbids with no record and no check.
- **Fix — the skeptic judged it SOUND:** add a §8 line to units 9 and 6 citing unit 3 F1. List
  `memory/guides/BUILD-METHOD.md` (line 1 only) under Files touched, and add a line-1-only diff check
  like unit 3 AC12.
- **Left-shift gate:** the line-1-only diff check. As a class gate, consider a spec-tokens join: a spec
  that bumps a kit version lists every carrier `tools/check-kit-versions.sh` pairs for that kit.

## What a fold should do first

1. Unit 1, the claim write path. Fold B1 and H1 together: push by remote name (or export the observed
   default into the push only), restate §3, and add the hook-wired fixture arm with
   `GOV_DEFAULT_BRANCH` unset. Then fold B2: renewals copy identity from the claim or the lease, and
   the tick arm runs with `CLAUDE_CODE_SESSION_ID` unset.
2. Unit 1, the write matrix. One table-driven arm (M8) covers H2, H3 and the `same session` row of M2. Decide the
   holder's foreign-`stale` cell (M7) before writing it, because the arm asserts it. Decide the claims
   switch (M9) in the same fold.
3. Units 6 and 9, the engine arms (H4). They are the two places where the bar would certify a check it
   never runs.
4. Unit 7, the hold bound (M22). Restate it once, in the four places it appears, and rewrite AC6's
   Red-when before any builder reads it.
5. The rest are single-AC additions inside their own units, and can fold in any order.

A round-2 audit should run after the fold, with a checklist swept and an intent supplied. This round
had neither.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 6 AC2 (against section 2 S2 and section 4 'Reading') | high | medium | confirmed | Spec 1 section 4 'Reading' pins the rule: one `date -u -f -` call, and when the answer count differs from the count asked, every age that call should have given reads `unknown` instead of shifting. AC2's malformed claim LACKS `beat-utc`, so it is never sent to `date`. That makes it the 'missing key' row of the Verdicts table. Neither the 'beat-utc that does not parse' row nor the alignment rule is observed, although S2 says AC1 to AC3 observe it. The gap is real. The path is narrow, though. The driver writes every beat through `date`, so a stamp-shaped but invalid beat comes only from a hand-edited or foreign-written claim. A wrong build also has to coincide with such a claim. That makes the effect contained, so medium rather than high. FIX: unsound. It asserts that the live claim after the invalid one 'still reads live with an age under the bound'. Section 4 'Reading' says the opposite: on a short answer count, every age the call should have given reads `unknown`. The fix would therefore red a build that follows the design. | unsound |
| 2 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 6 (against section 2 S4 and the section 4 table 'Who may write a claim') | high | high | confirmed | In spec 1, AC4 covers foreign `live` at preflight. AC5 covers `stale` and `landed` at preflight, both `take`. AC8 covers `live` and `stale` at take-over. No AC observes these refusing cells of the section 4 table: foreign `held` at preflight, foreign `terminal` at take-over, and `unknown` at preflight and at take-over. S4 says AC4, AC5, AC7 and AC8 observe the table. Section 7's arm sentence lists 'checks 89, 90 and 91' only in general terms. A build that maps any of these cells to `take` passes every AC. It would start a second driver on a held slug, which is the double drive the unit exists to stop, or re-take a slug another driver landed. That is a wrong result on a narrow path. | sound |
| 3 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 6 AC12 (against section 2 S10 and section 4 'The two verbs') | high | high | confirmed | Section 4 'The two verbs' says `--beat` writes only through the `none` and `mine` rows of the holder column, and every other row is a skipped line. AC12 observes only the positive renewal and the dry run. AC7's younger-beat and foreign-live cases exercise `--resume`, not `--beat`, and section 7's tick arm names only 'the LIVE row runs --beat, and --dry-run pushes nothing'. So no criterion shows `--beat` declining to write. A `--beat` that skips the `mine` test makes a valid CAS on the observed sha and overwrites a claim another node took over. One example: the original session wakes after a sleep, after the new holder has passed `--close`. The stale run can then pass its own `--close` while the new holder lands, which is a double landing on a narrow path. | sound |
| 4 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 6 (against section 2 S7 and the `same session` row of section 4) | medium | medium | confirmed | S7 says AC7 and AC8 observe it. Neither exercises the `--replaces` block or the LANDING re-bind writing the claim, and no AC exercises the `same session` row. The finder overstates the impact. With `CLAUDE_CODE_SESSION_ID` present, a `--replaces` that left the claim stale-keyed is caught by the `same session` row, which the holder column answers with `take`. After the re-bind the next verb is `--landed`, a status write that only announces. The wedge the finder describes does occur when the session id is absent: `mine` then falls back on the keepalive, the claim reads foreign `live`, and the holder gets check 90. A build that treats `same session` as foreign has the same effect. The effect is contained to the run's own wedge. FIX: unsound. The re-bind half asserts that after the LANDING re-bind the claim's keepalive equals the record's new keepalive, without fixing the claim's state. The re-bind serves a session the record does not name (fail 55), so the claim it reads is normally the prior session's fresh, foreign `live` one. The call-site table runs the re-bind in 'status write' mode, which answers that cell with 'announce' and does not write. A correct build would fail the fix's assertion. 'The following holder --resume exits 0' is also vacuous after a re-bind, because that resume prints 'nothing to resume' and exits 0 whatever the claim holds. | unsound |
| 5 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 6 AC10 (against section 2 S8) | medium | medium | confirmed | S8 says AC10 observes it, but AC10 covers only `--close` against a foreign `live` claim. Two behaviours have no criterion: check 91 on an unreadable claim, and `--dispatch`'s holder read (check 90 with no row written). The impact is narrower than stated. `verb_close` runs `observe_anchor \|\| true` and still grades the non-overridable authorization-reachable DoD item. A remote that answers nothing therefore blocks the close anyway. The unprotected case is a remote that answers the anchor read but refuses the `refs/gov/` fetch. A `--dispatch` that skips the read writes pass rows that a correct `--close` later refuses. The effect is contained. | sound |
| 6 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 6 AC4/AC6 (against section 2 S3, S5 and section 4 'The outcome of a write') | medium | medium | confirmed | AC3 observes check 91 for `--claims` only. AC4 to AC6 never make the preflight write fail without a race, so S5's check 91 and section 4's rule that a pre-push refusal or an exit 124 is never a lost race have no criterion. AC6 runs on a fresh slug, so it observes that the CAS comes before `scaffold_runmd`, through the missing run-state file, but not that it comes before the rotation. A build that rotates first leaves a prior record moved by a preflight that then lost. A build that misclassifies a network fault reports check 90 where 91 is due. Both are contained. | sound |
| 7 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 6 AC9 (against section 2 S9) | medium | medium | confirmed | S9 says AC9 observes the `--landed` write of `landed`, but AC9 sequences `--hold`, `--resume` and `--abort` only. A landed run whose claim stays `live` ages to `stale`. The card then shows it as stale until the one-day hide, and the take-over column reads 'take, announced' where `terminal` would refuse. The re-land path is mostly closed by the local record's own terminal refusal (`refuse_if_terminal`), so the effect is contained. Take the fix's separate-case form. Appending `--landed` after AC9's `--abort` would meet a terminal record. | sound |
| 8 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 6 AC13 (against section 2 S13) | medium | medium | confirmed | AC13 asserts render parity and one `--claims` grep. `adopt-unattended.sh --check` passes whenever the template and its render agree, including when the template was never edited. So the S13 edits have no criterion: STOPS section 7, the section 8 holder row, the SKILL holder sentence (F7) and the `check_single_live` comment. The rendered Skill can keep a false sentence about what `--resume` writes for the holder. An unattended agent loads that Skill. FIX: unsound. In both `tools/unattended/SKILL.template.md` (lines 38-39) and the rendered `.claude/skills/unattended/SKILL.md`, the sentence breaks across a line, after 'For the holder it'. `grep -c 'For the holder it writes nothing'` therefore prints 0 today, before any edit, so the proposed assertion cannot fail. `grep -n 'claim' memory/guides/UNATTENDED-STOPS.md` already hits two lines, in section 6 and section 10, so it also needs scoping to sections 7 and 8. | unsound |
| 9 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 6 AC11 and AC7 (against section 2 S6 and S12) | low | low | confirmed | S6 says AC11 observes it, but AC11 seeds only a `live` claim and a `landed` one, so the `held`, `stale` and `unknown` listings are unobserved. S12 says AC7 observes the HALT_FLOOR rise, but AC7 observes only that `--abort --code claim-lost` is accepted. `check-unattended.sh` compares `nhalt -ge HALT_FLOOR`, so a floor left at 7 passes silently. Both gaps are real. One affects an informational announcement. The other is a ratchet not tightened, which changes no behaviour today. FIX: unsound. Both conf files spell the key quoted, `HALT_FLOOR="7"` (`.unattended.conf:313`, `.unattended.conf.example:346`). The proposed `grep -n '^HALT_FLOOR=8'` never matches the quoted form, so it reds a correct build. | unsound |
| 10 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-2.md:section 6 AC1 (against section 2 S6) | medium | medium | confirmed | S6 of spec 2 says AC1, AC4 and AC5 observe it. AC1 prints 5 rows, under the cap of 8, and asserts which rows appear but not their order. AC4 and AC5 are skip forms. So the cap, the `… <m> more` row and the verdict-first ordering have no criterion. A build sorting by slug drops a live claim past the cap on a busy remote. That is the stated reason for the order. The card is informational, and the driver's own preflight still refuses, so the effect is contained. | sound |
| 11 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-2.md:section 6 (against section 2 S3 and S4) | low | low | confirmed | S3 says AC7 observes the no-driver form, but AC7 runs only the install-prefix leg. The no-working-`timeout -k` skip in S4 and the stdin redirect from /dev/null are also unobserved. The resolvers check `-f`, so a deleted driver reaches the no-driver branch, which nothing tests. The effect is limited to the card cell and the SessionStart hook's time, which the harness bounds. FIX: unsound. The finding names three unobserved behaviours, and the fix adds criteria for two. The stdin redirect from /dev/null stays unobserved. Dropping it is a defect, because a SessionStart hook's never-closing pipe would then hold the read until the bound fires on every card write. | unsound |
| 12 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-3.md:section 6 AC7 (against section 2 S8) | medium | medium | confirmed | Spec 3 S8 says RUN INTEGRITY states the by-design source. AC6 observes only the log lines from a probe of the prelude, which never reaches the synthesis prompt. AC7's observation is `grep -c "By design:"` over the rendered source. At base the string is absent (the harness has only the uppercase `BY DESIGN` at tier2-review.js:741), so the grep can fail at all. But any comment or dead literal the build adds satisfies it, and the §7 tier2-review arm covers extraction only. The suite already observes RUN INTEGRITY the cheap way, by slicing the synthesis prompt (tier2-review.test.sh:534, 631, 762). The clause can therefore be missing or misstated while every criterion passes. The effect is limited to what a review record says about its priming. | sound |
| 13 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-3.md:section 6 AC8 (against section 2 S9) | medium | medium | confirmed | AC8 swaps the resolver agent for a stub that already returns `checklist`, so the substance of S9 goes unobserved. That substance is the new instruction in the resolver prompt at unattended-build.template.js:778-787. The §7 arm stages only 'the resolver's checklist not forwarded'. The caller-precedence rule in §4 ('A caller-supplied `checklist` argument wins over the resolver's') is a new argument, since the template accepts no `checklist` today, and no criterion observes it. A missing prompt edit would degrade every real audit to the WARNING path while AC8 stays green. That failure is announced rather than silent, so the effect is contained. | sound |
| 14 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-3.md:section 6 AC2 (against section 2 S3 and the section 4 grading table 'not inert') | medium | medium | confirmed | S3 and the 'not inert' row of the grading table require check 19's inert arm for invariants, and S3 says it is 'Observed by AC2'. AC2's explicit arm list holds an unanchored and a universal invariant but no inert-only one. The existing 'check 19 catches INERT anchors' self-test arm covers `kind: class` only: cmd_check's loop skips every non-class record (gotchas.py:275), so the invariant branch is new code. §7's 'each invariant predicate disabled' line implies the arm, but the observed criterion does not demand it. An invariant anchored only on the decision log could then pass check 19 unnoticed. The effect is a by-design line that is dead on code reviews, which is contained. | sound |
| 15 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-3.md:section 6 (against section 2 S6 and section 4 'Grading') | low | low | confirmed | Three behaviours in spec 3 have no criterion. §4 states that a set LEG_MANIFEST naming an unreadable file is a named HYGIENE failure, never a traceback. It also states the second announcement, for an absent id grammar. S6 says the example conf declares LEG_MANIFEST blank and claims 'Observed by AC2 and AC3', but neither criterion reads tools/memory-tree/.memory-tree.conf.example. AC2 has only 'the blank-key announcement'. The behaviours are specified, so only a mis-build on adopter-only paths is left uncaught. | sound |
| 16 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-4.md:section 6 AC7 (against section 2 S5 and S10) | medium | medium | confirmed | S10 promises self-test arms for 'the order step' and says 'Observed by AC7 and AC9'. AC7 enumerates extraction and map cases only, and AC9 is the version check. So the order step's rules from S5 have no fixture: two successors (land after the lowest-ranked one), successor above (no move, since the step moves only down), and relative order preserved. AC3 is a single live case with one successor. Some of the finder's impact is overstated. AC4 does observe a partial hit keeping its rank. A move-to-end build would fail AC3's 'sits directly below it' unless the successor is last. The multi-successor and successor-above rules are still unobserved, and §4 notes the P3 headers name several successors, for example TOOL-aClosedDocket-4 with three. A mis-ordering there separates the label from its successor, which is contained. | sound |
| 17 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-4.md:section 6 (against section 2 S6) | low | low | confirmed | S6 requires the tag in `render()` and in `emit(full=True)`, plus the multi-id form `[superseded by <id>, <id>]`. AC3 and AC4 each go through the default render with one successor, and AC7 checks the two-id P3 case only at map level. The full branch is not user-facing: query.py:823 says `full=True` 'is not a CLI flag' and exists only for byte measurement. Only the two-id tag affects a reader, and the risk there is a label showing one successor of several. That is cosmetic. | unsound |
| 18 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-5.md:section 6 AC3 (against section 2 S1) | medium | medium | confirmed | S1 names three `unknown` conditions and claims 'Observed by AC1, AC2 and AC3'. AC3's stub only exits 1. The other two conditions are a header with no PID or PPID column and a snapshot with no row for `$$` (§4 step 5). No AC covers them, and no §7 staged break does either: the listed breaks are the ancestor walk, the window reach, the undisowned sampler and the ledger read. A build returning 0 there would stamp readings faithful on exactly the hosts where the census is blind. The finder's second impact, a count taken without exclusions, is already covered by AC2. Ceilings only rise, so the harm is contained to inflated evidence, the status quo before this unit. | sound |
| 19 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-5.md:section 6 (against section 2 S3) | low | low | confirmed | S3 says the eighth field is written to `.retry.leg` rows too, and derive-ceilings.py's glob `gate-run/*/*.leg` (line 209) reads those rows as evidence. No AC runs a deferred serial retry, so a seven-field retry row would quietly read `uncensused` and be set aside. The rule that 'largest positive count' beats an `unknown` in the same window is also unobserved, because AC1, AC3 and AC5 each produce a uniform window. The effect is lost evidence or a different set-aside reason, never a wrong ceiling. | sound |
| 20 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-6.md:section 6 AC7 (against section 2 S4) | high | high | confirmed | S4's dispatch block must set `status=1`, key offenders under 28, and print the mode's output on a green run, and it claims 'Observed by AC7 and AC8'. AC7 is `grep -n 'check-content'` expecting one line, which a comment alone satisfies (a real block that also carries a comment would print two lines and fail it). AC5 and AC6 run row_grammar.py directly and never the engine. §7's only new arm is in row_grammar.py --selftest. The close's `memory hygiene` leg runs over a clean tree, so it is green whether or not the block propagates the exit. Precedent agrees: check 24's block at check-memory-hygiene.sh:1330 has no engine arm either. A broken dispatch would leave the bar certifying 'no duplicate' while never grading one. That needs a mis-build, so it is a narrow path. | sound |
| 21 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-6.md:section 6 AC3 (against section 2 S3) | medium | medium | confirmed | S3 exempts a key held under one identity across documents and names a `snapshot` carry-forward as such. AC3's 'one id twice with one text' does not place the copies in different documents. A (path, id) identity build therefore passes it: a same-document pair is one (path, id) anyway. This repo declares ROTATION_MODE="cut" (.memory-tree.conf:483), so AC5's real tree never holds a cross-document same-id pair. The shipped example declares `snapshot` (.memory-tree.conf.example:240), and scan_records takes the index and its archives. A mis-keyed build would therefore red every carried-forward row in a default adopter. That red is loud and contained. | sound |
| 22 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-6.md:section 6 (against section 2 S3) | low | low | confirmed | S3's 'an empty key is not graded and is counted' is a distinct branch, and S5 requires a fixture arm for every new branch. Neither the AC list nor §7's arm list holds an empty-key fixture: AC4 is an empty population, which is a different case. Three holders are unobserved too. Built wrong, two empty-bodied records would red each other, or a finding would name two of three holders. Both paths are rare, because the real tree measured 0 empty keys, and the effect is small. | sound |
| 23 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-7.md:section 6 (against section 2 S4 and S5) | low | low | confirmed | Unit 7 S4 lists five end reasons, fell, bound, drained, unread and wall, and says they are 'Observed by AC5 and AC6'. AC5 produces only `fell`, and AC6 produces only `bound` and `drained`. No criterion produces `unread`, which is rule 2 of the decision, or `wall`, which closes an episode after the loop. S5's 'all three of its writers' is observed only on AC5's normal verdict path. The §4 Recording claim that a wall-stopped run still prints the summary line is not observed either. The effect stays inside one bar's record. | sound |
| 24 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-8.md:section 6 AC1/AC2 (against section 2 S1 and section 4 'The shared block') | medium | medium | confirmed | Unit 8 §4 'The shared block' pins the contract for both languages: one `health: NOTE -` line, nothing written, and Python 'returns None, never raises'. AC1 drives the empty-path, refused-token and missing-directory branches through the bash copy only. AC2 and the S2 behaviour arm call the Python copy on the happy path only. §5 risks names the empty-path case as real: reap.py run from a root outside any repository. A Python copy that raises there would turn a completed kill into a traceback and a non-zero exit, and no criterion would see it. The effect is contained to the reaper's exit status. | sound |
| 25 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-8.md:section 6 AC5 (against section 2 S3, S5 and S6) | medium | medium | confirmed | Unit 8 AC5 is a `git grep` for presence, and its red-when checks placement only for `tree-killed`. S3 claims merge-driver-set is 'Observed by AC4 and AC5', but AC4 exercises only the hooks arm. §7 has no behaviour arm for merge-driver-set; the same is true of turnstile-expired, scratch-swept and ticket-swept. At base, check-wiring.sh:1089-1100 shows the merge arm's FIXED branch (DO_FIX=1 under --session, line 206) beside an `ok` branch. A call placed on the `ok` branch would log a self-heal on every SessionStart, and AC5 would stay green. run-resumed is covered by §7's resume-tick arm ('stage the call moved above the pid check'), which the fix's AC5 note acknowledges. | sound |
| 26 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-8.md:section 6 AC2 'Red when' | low | low | confirmed | Unit 8 AC2 seeds exactly 500 lines. A trim at 'holds 500 or more' and an off-by-one trim at '499 or more' both fire on 500 lines and leave 251, so the 'fires at 499' red condition cannot be observed with this fixture. Only the 501 case is distinguishable, because 500 lines with no trim become 501. A 499-line fixture separates the two: 500 lines after the append under the spec, 251 under the off-by-one. The effect is one line of log length. | sound |
| 27 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-9.md:section 6 AC10 (against section 2 S7) | high | high | confirmed | Unit 9 S7 says the wiring is observed by AC10 and AC11. AC10 is only `grep -n 'check-relations'` over check-memory-hygiene.sh, which a comment or a dead block satisfies. AC11 grades the catalog and the README count. Nothing observes that the dispatch reddens the `memory hygiene` leg, keys offenders under 27, or prints the summary on a green run. The green-run print departs from the check-24 precedent at check-memory-hygiene.sh:1330-1335, which prints only on failure, so the builder has to write new logic there. check-arms.py counts only `fail <n> "` call sites, so this delegated block, which sets status=1, is outside the harness-arms leg too. §7's only new arm is row_grammar --selftest. A dispatch that swallows the exit would therefore leave the leg green over an unsatisfied near match while AC1 to AC13 pass. That is a check certifying what it does not check, reached by a narrow but undetected build error. It also breaks AGENTS §7's rule that a gate's failing case must be observed before it lands. | sound |
| 28 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-9.md:section 6 (against section 2 S2) | medium | medium | confirmed | S2's no-argument derivation is reimplemented in Python as `derive_relation_base`. It takes the merge-base of origin/<branch> and HEAD first, falls back to <branch>, and reads <branch> from GOV_DEFAULT_BRANCH. AC1 to AC4 and AC12 all pass an explicit base. AC8 and AC9 pass 5266d22e. AC7 observes only the no-base refusal and base equal to HEAD. The hygiene dispatch is the production caller, and it uses the derived base. A derivation that takes the wrong ref or ignores the variable would grade the wrong added set, and no criterion would catch it. The effect is wrong findings on one range. | sound |
| 29 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-9.md:section 6 (against section 2 S5) | medium | medium | confirmed | S5 says the kit's example conf declares NEAR_MATCH_GATE blank, and gives the reason. S5 cites AC1, AC4, AC5 and AC6, none of which reads tools/memory-tree/.memory-tree.conf.example. The existing example-conf arm in check-memory-hygiene.test.sh:2411-2428 derives its keys from the shell engine's validation loop. It checks only that a key is declared, never its value, and this key is read by row_grammar.py. 'Too old' is a refusal S5 names, and AC6 seeds only an absent bench.py. An example shipped as red:0.125 would arm red in every adopter at an unmeasured floor. The fix's `KEY=""` spelling matches the example's other blank keys. It leaves the 'too old' refusal unobserved, but that is not the impact the finding names. | sound |
| 30 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-9.md:section 6 AC9 | low | low | confirmed | Unit 9 AC9 states an equality: a graded count equal to the rows and gotchas added since 5266d22e. Its red-when fires only on a count of 0 while a gotcha file was added, so a miscount such as a missed archive or dropped rows passes when it is non-zero. The fix is unsound. `git diff --diff-filter=A` keeps rename detection on by default, so a gotcha renamed in the range shows as R and is left out, while S2 counts it as added under its new name. Counting keyed ids off the decision documents' added diff lines also counts rows that a rotation moved into an archive, and S2's identity test does not count those. On either event the fix would red a correct build. | unsound |
| 31 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 4 'The remote' against section 3 'The pre-push hook' and the section 4 Evidence pre-push bullet | high | high | confirmed | Unit 1 §4 'The remote' says reads and writes both use the push URL. At base, .githooks/pre-push:164 `resolve_remote_name` returns an empty REMOTE_NAME for any $1 containing / : or @. A push to a URL hands the hook the URL as both arguments, so `obs` stays empty and `def` falls to GOV_DEFAULT_BRANCH. With that variable unset, the hook exits 1 at lines 413-420 ('the push names a URL ... and GOV_DEFAULT_BRANCH unset') before stdin is read, so it never reaches the skip-nondefault exit at 905. No earlier exit covers a non-branch ref. On node a, core.hooksPath is C:/projects/coding-governance/.githooks and GOV_DEFAULT_BRANCH is unset, and neither unattended.sh nor gate-env.sh exports it before this point. Per §4 'The outcome of a write', a pre-push refusal is NOT COMPLETED, so every --preflight refuses with check 91. §3's and the Evidence bullet's 'non-default exit' claim is therefore false for the specified invocation. The AC fixtures are `git clone --local` copies, which carry no core.hooksPath, so the suites pass while the production write path is dead. The failure refuses safely rather than passing silently, but it disables the feature on the main path. | sound |
| 32 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 4 'Who may write a claim' (holder column, foreign stale row) against section 1, section 2 S4 and S8, and the section 3 Edges hand-off to TOOL-aGraftedHelix-8 | medium | medium | confirmed | Unit 1's table takes a foreign `stale` claim ('take, announced') in the preflight, take-over and holder columns. The holder column covers the --resume holder row and --replaces, --dispatch and --close. S4 and the Edges hand-off to unit 8 call the stale take-over 'a branch of its own at BOTH take-over sites', and the call-sites table names only --preflight and run_takeover as take-over sites. Unit 8 S5 sits claim-taken-over on that branch, so holder-path take-overs would go unlogged. S8 and §1 say --close refuses when the run does not hold its claim, yet over a foreign stale claim it takes the claim and closes, and AC10 covers only foreign `live`. §5 risks says the displaced session's 'next claim read refuses it with check 90', which the table contradicts once the taker has itself gone stale. The finder's 'double drive' framing is overstated: CAS still lets at most one session close, and the re-take is sequential. The text contradiction and the missed health event are real, and their effect is contained. The fix is sound. The --replaces path compares the claim against the record's own facts, so it stays `mine`. A displaced holder aborts with claim-lost, and the slug stays recoverable through preflight's or run_takeover's stale take. | sound |
| 33 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-7.md:section 2 S4 and section 4 'The decision' against section 6 AC6 (also section 5 perf / scale and section 8 F1) | medium | medium | confirmed | Unit 7 §4 says a hold leaves the inner loop and blocks on `wait -n`, and that 'a decision happens when a leg completes; nothing polls'. The bound is therefore tested only at the next completion after it expires. A hold lasts until that completion, not MEMPAUSE_HOLD, so 'each episode releases one leg per MEMPAUSE_HOLD' in §4, '…at most MEMPAUSE_HOLD' in F1(a) and §5's 'at most one MEMPAUSE_HOLD per released leg' are all false. Traced through AC6 with HOLD=2: B ends at 1 s and D's episode opens. C ends at 4 s, which closes D's episode `bound` after 3 s. E's episode then opens with A, which runs 8 s, still running. D finishes instantly and E is still held. A ends at 8 s and E closes `drained` after about 4 s, past the 2 s bound while A ran. The expected `drained` row can arise only by violating AC6's own red-when. F1's worst-case conclusion still holds, since at least one leg always runs, so the effect is contained: misstated bounds and a self-contradicting AC. The fix's restated red-when fits this trace: D is released at the first completion after the bound, and no completion follows E's bound while legs run. | sound |
| 34 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-4.md:section 3 Edges (hands-off TOOL-aGraftedHelix-9) against unit 9 section 2 S4 and section 4 'The predicate' step 5 / 'Alternatives rejected' | medium | low | confirmed | Unit 4 section 3 Edges says unit 9 'queries this index, so it sees the supersession map in the cache manifest and each hit's supersession fields'. Unit 9 section 4 'Alternatives rejected' explicitly refuses to read the map from manifest.json and from query.py's fusion, and it calls extract_supersessions and derive_supersession_map directly. Unit 4's P1 needs an ID after the verb, while unit 9 step 5 accepts a bare `supersedes`, so 'a record that declares a supersedes relation becomes one of this map's P1 edges' is false for the bare token. The contradiction is real, but it sits only in the hand-off text. Unit 4's own S4, S5 and S6 already require the manifest key and the per-hit fields for its own render. A bare token not reaching the map is unit 9's deliberate choice (its 'Alternatives rejected' bare-token line). Built as written, nothing behaves differently. | sound |
| 35 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-5.md:section 2 S2 against section 4 'The sampler' | low | medium | confirmed | S2 puts the truncation and the first sample inside the detached sampler ('It truncates ... appends one sample at once'). Section 4 claims the first sample lands 'before the first leg dispatches, so every leg has one inside its window'. A backgrounded subshell gives no such ordering. The ts_tick_start shape it copies (run-gates.sh:849-869) does all its work after `&`, and its stdio goes to /dev/null. So S2's 'first sample reading unknown prints one run-gates: NOTE line on stderr' (required by AC3) also cannot come from inside that subshell. A first-wave leg whose runleg reads `census` before the sampler's first append gets `unknown` and is set aside as uncensused. That is a real behavioural defect, but its effect is contained: it can only set a reading aside, never admit one. | sound |
| 36 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-9.md:section 7 Gates (closing sentence) against section 6 AC1-AC7 and AC12 | low | low | confirmed | Unit 9 section 7 lists `row-grammar selftest`, whose manifest argv is `python3 {prefix}/memory-tree/row_grammar.py --selftest` (tools/gate-legs.json:442-447), and then says 'The close runs these; no pass does'. AC1-AC7 and AC12 name that same command as their observation. Brief invariant 11 explicitly lets a pass verify with 'a `--selftest` arm'. Unit 6 section 7 carries the identical sentence over its own --selftest-observed AC1-AC4. The text contradicts itself, but the ACs and invariant 11 make the intent recoverable, so shipped behaviour is unaffected. | sound |
| 37 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-9.md:section 2 S9 and section 4 Files touched against the spec brief's shared invariant 10 | low | low | confirmed | Line 1 of memory/guides/BUILD-METHOD.md is `<!-- gov:kit memory-tree@2.118 -->`, a carrier the memory-tree bump re-renders. Brief invariant 10 says no unit edits that file. Unit 3 resolves exactly this tension in its section 8 F1 (Option A), with AC12 checking that only line 1 changed. Unit 9 S9 and unit 6 S6 bump memory-tree 'in every carrier' but neither cites that ruling, lists the file, nor observes a line-1-only diff. The shipped change is the same marker line unit 3 already accepted, so the defect is in traceability: those two units carry no record or check that only line 1 moved. | sound |
| 38 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 4 "The remote" and "The outcome of a write"; section 3 "The pre-push hook"; section 6 AC4-AC9 | blocker | blocker | confirmed | Reproduced. In a scratch clone with core.hooksPath set to the tracked .githooks and GOV_DEFAULT_BRANCH unset, `git push --porcelain --force-with-lease=refs/gov/runs/x: <push url> <sha>:refs/gov/runs/x` was refused. The hook printed 'can't determine the default branch (the push names a URL, so no remote HEAD is observable and GOV_DEFAULT_BRANCH unset)', git reported 'failed to push some refs' with no `!` status line, and the exit was 1. The same push to the remote NAME, with origin/HEAD set, landed `[new reference]`. The URL push with GOV_DEFAULT_BRANCH=main also landed. resolve_remote_name (.githooks/pre-push:164-169) rejects anything containing / : or @, and the refusal at :414-420 comes before the skip-nondefault exit at :905. Section 4 'The remote' sends both reads and writes to the push URL. Node a's environment has no GOV_* variable, and the tree exports GOV_DEFAULT_BRANCH only in test suites (unattended.test.sh:477). So every production claim write ends NOT COMPLETED and every --preflight refuses with check 91. The fixture ACs, which run with no hook or with the variable exported, would stay green. Section 3's claim that 'a claim push takes its non-default exit today' is false for a URL push. | sound |
| 39 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 4 "The claim record", "Renewal" and "The two verbs" (--beat); section 2 S10/S11; section 6 AC12 | blocker | blocker | confirmed | The claim record pins `session: <CLAUDE_CODE_SESSION_ID, else absent>`. Renewal writes when 'a field the write would set differs'. resume-tick.sh is launched by the OS scheduler, sets no CLAUDE_CODE_SESSION_ID, and only launches `claude -p --resume` itself (resume-tick.sh:14, :345). On a LIVE run, --beat reads `mine`, because the claim's session equals the record's session fact. Its write would set session to absent, so it is due at once and writes `session: absent`. The holder's next --resume, --dispatch or --close then sees the keepalive match and the session differ, so the claim is not `mine`. The same-session row needs the claim's session to equal the non-absent env id, which it does not, so the claim reads foreign `live` and the call refuses with check 90. That forces --abort claim-lost on every run the tick beats, which is the case F5 adds the tick for. AC12 asserts only that beat-utc moved, and a tick suite launched from a Claude session inherits CLAUDE_CODE_SESSION_ID, so it would pass. | unsound |
| 40 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-7.md:section 4 "The decision" (call site and the 'only the wall's break can leave' sentence); section 2 S4/S5 | medium | medium | confirmed | run-gates.sh:3086-3091 is a second dispatch site. When nothing is live, legs remain and the inner pass dispatched nothing (di == di_before), it runs `runleg $k &` with no per-leg hook, not even arm_wall. A hold steps di back, which leaves di == di_before, and the decision's running count is captured from the inner condition rather than re-asked. So if the running legs finish between that capture and the outer `$(live) -gt 0`, the held leg is force-dispatched and its episode is never closed as `drained`. The runner's own comment (6 of 30 legs) measures this window as common. When the forced leg is the last one, the episode survives the loop and section 4 closes it as `wall`, contradicting 'only the wall's break can leave' it open. S7's overlap join then sets aside readings that ran while nothing was held. The effect is limited to the summary line, the verdict's paused_s and the set-aside counts. | sound |
| 41 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-7.md:section 4 "The decision" (rule 5 and 'each episode releases one leg per MEMPAUSE_HOLD'); section 2 S4; section 6 AC6 Red when | medium | medium | confirmed | S4 says 'A decision happens when a leg completes; nothing polls', and section 4 rejects polling. Rule 5 is therefore checked only at the next completion or report, because the reader blocks on `wait -n` (run-gates.sh:3080). A hold lasts until the first completion after MEMPAUSE_HOLD, so 'each episode releases one leg per MEMPAUSE_HOLD' is false. Tracing AC6 under that design: B rewrites the fixture to 95% and ends at t=1, so D is held. C ends at t=4, so D is released as `bound` after 3 s against a 2 s bound while A and C ran. E is then held from about t=4 until A ends at t=8 (`drained`). That trips AC6's 'Red when: a held dispatch waits past the bound while legs still run' on a faithful build. A builder must either fail the criterion or add the polling section 4 rejects. | sound |
| 42 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-8.md:section 4 Data model and Alternatives rejected; section 3 last bullet; section 10 | high | - | refuted | Unit 8's file and format are not invented. The spec brief's I3 pins `<git-common-dir>/health.log` as one TAB-separated line of utc (ISO-8601 with offset), source, event and detail, owned by unit 8, and section 4 opens 'I3, as the brief pins it'. The cited ruling is scoped to run logs: TOOL-dLoggedFlight-1's goal names three producers' journals, S2 puts them at `<common-dir>/runlog/{driver,gates,pushes}.log`, and the README is titled 'one line grammar for run logs'. The finder itself scopes it to journals 'under <common-dir>/runlog/', and health.log is not there. Neither the ruling nor the README's three-producer statement becomes false. The double-recording example is also wrong: the tick's `run-resumed` follows its launch of `claude -p --resume <session>` (resume-tick.sh:14, :345), not the driver's --resume verb that driver.log journals. And the runlog CLI not reading heals is an explicit section 3 non-goal. What remains is a request to mention runlog in 'Alternatives rejected', which is a detail, not a defect that makes the spec wrong. | unsound |
| 43 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-5.md:section 2 S5 and S6; section 3 | medium | medium | confirmed | derive-ceilings.py's `--write --observed '<leg>=<seconds>' --how ...` path (lines 469-494) writes an evidence row directly. It never goes through read_runs and carries no census. Its docstring (line 26) states the ruling 'A READING TAKEN OUTSIDE THE RUNNER IS ADMISSIBLE, AND HAS TO BE (TOOL-cMendedVintage-17)', and DECISIONS.md:198 records it. Unit 5 filters only read_runs (S5) and never names this path. Its goal ('makes the evidence tool argue only from readings whose census found none') and the docstring, README and evidence-header text S6 writes would claim more than the code enforces, and an uncensused out-of-band reading still raises a ceiling. A builder who instead closes that path would reverse a ratified decision with no record. The effect is contained to that one manual path and its documentation. | sound |
| 44 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-5.md:section 3 first bullet; section 8 F1 | medium | - | refuted | Section 3's wording echoes the brief, which itself calls TOOL-dDerivedDocket-26 inside-the-bar handling. The spawn-floor probe (run-gates.sh:1919-1990, dDerivedDocket-26 S5) answers a different question: whether a leg that times out AGAIN, run alone after the pool drains, is HOST-limited. It is measured at calibration and in the serial retry, never per leg reading. Sampled during a pooled run, a spawn-cost ratio reads the bar's own process creation, so as F1 candidate (d) it loses on the same condition that eliminated (b), and the decision stands. The claimed impact, a reading under non-gate host load stamped `foreign 0`, is exactly section 3's second non-goal ('Load that is not shaped like this repository's gate work'), which the runner's census header is required to state. What remains is an incomplete one-line description of a landed ruling, with no effect on the design. | sound |
| 45 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-5.md:Status header; section 10 | medium | low | confirmed | Unit 5's status header carries no `closes` or `advances`, and BACKLOG_MODE is `builds` (.memory-tree.conf:636). TOOL-aSurfacedLexicon-22 is OPEN (memory/backlog/TOOL.md:264) and its stated finding is that the ceiling row was written twice from contended readings. Unit 5's whole mechanism answers that: contended readings stop arguing a ceiling. §10 names the ask only as a recall hit. TEMPLATE-SPEC defines `advances` as a unit that moves an ask without finishing it, so the verb fits, and unit 1 uses it. The omission is real, but it only changes the derived status in the generated asks index, which reads OPEN with no linked spec. Product behaviour does not move, so the grade is low and not medium. One part of the finding is overstated: the mandate's 'do not backlog' rule covers new discoveries, not an ask that already exists. | sound |
| 46 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 4 'Who may write a claim' and 'Call sites'; section 6 | medium | medium | confirmed | The §4 write matrix has 8 claim-read rows and 4 modes. AC4 to AC12 observe only these cells: preflight×none, preflight×foreign live, preflight×stale, preflight×terminal, take-over×live, take-over×stale, holder×mine, holder×foreign live, the --close holder×live, status-write×mine and status-write×foreign live. Cells that nothing observes include take-over×terminal (check 89, the spec's own guard against landing a slug twice), preflight×unknown and take-over×unknown (F3's 'refuses like live'), and preflight×held. The §7 arm lists 'the verdicts, checks 89, 90 and 91' but promises no per-cell coverage. A wrong cell therefore ships with every arm green. TOOL-dDerivedDocket-40 is OPEN and records this exact class for the resume matrix. The fix is unsound in one part. TOOL-dDerivedDocket-40's subject is the resume matrix of TOOL-dDerivedDocket-4, and its candidates are a Reacher column in that guide and a leg joining that guide's rows to arms. Per-cell arms in unit 1's claim matrix move neither, so marking that ask `advances` would show it SPECCED while nothing of its subject moved. | unsound |
| 47 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 3 'A new conf key'; section 4 Rollout | medium | medium | confirmed | Unit 1 is Tier-2. §3 says 'No conf key turns claims off; a host that refuses the namespace refuses `--preflight` with check 91', so on such a host every new run is refused after the kit update, and downgrading the kit is the only way out. Charter §1 requires Tier-2 to land dark behind a default-OFF flag or as inert data, and Rollout's 'dark for runs preflighted before this lands' is not that. The run mandate reads 'Waive §1 explicit ask' as covering the explicit ask only, and says outright that it does not rewrite the charter's other §1 rules. The mandate's ruling that claim-ref pushes need no ask covers the push authority, so the finding overstates there. It does not cover shipping always-on, and no DECISIONS row of the TOOL-dDerivedDocket-5 shape (decision at memory/DECISIONS.md:118) records an opt-out. On the fix: either alternative gives an adopter an off switch, which removes the downgrade-only outcome. The claims switch must read OFF when the key is absent, or adopters with an existing conf are still exposed until they add it. | sound |
| 48 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-6.md:section 3 'A shrink-only pin or a waiver registry'; section 4 Rollout | medium | medium | confirmed | Check 28 grades the whole corpus: the decision index, its archives and the gotchas. It ships in the memory-tree kit with no pin and no conf key (§3, §5 migration 'No conf key, no pin'). Its only justification is gov's own census of 0. Check 20 handles the same adopter case with ROW_DUPLICATE_PIN and `--emit-pin` (.memory-tree.conf.example:268-271). Sibling unit 9 grades only records added since the merge-base, and ships its key blank because a floor measured on gov is not a floor elsewhere. An adopter whose landed append-only decision rows already share a key goes red on the memory-hygiene leg. The spec's remedy, 'fold the two into one', is illegal under charter §6's append-only rule for landed rows. | sound |
| 49 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-3.md:section 2 S2; section 4 'Grading' table, 'guard resolves' arm | medium | - | refuted | Two premises fail. First, check 18 applies `declares()` only to `kind == "class"` records (gotchas.py:276-280). S2 grades invariants by a separate arm, so the gate never runs both predicates on one record and cannot disagree with itself. Second, the arm answers a different question: does the first line of `## Guarded by` name tokens that RESOLVE to a tracked path or a leg. `declares()` matches a phrase anywhere in the body and resolves nothing, so routing the invariant through it would be weaker, not a duplicate. The only claimed symptom is `gotchas.py --declares` printing `no` for an invariant. `git grep -- --declares` finds no consumer outside the module's own self-test, so no reader sees that answer. The fix is unsound for two reasons. Extending DECLARES_RE to match the `## Guarded by` form would make every invariant declare by its heading alone, which makes the predicate vacuous for that kind. Routing through `declares()` would also admit a `gated by`- or `documented check`-shaped first line, which S2's resolution rule deliberately refuses. | unsound |
| 50 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-3.md:section 2 S8; section 4 'The harness — reading I4 out of checklist' step 5 | medium | medium | confirmed | S8 and §4 step 5 set `byDesign = a.byDesign` when the caller supplies one, and use the extracted invariant block only otherwise. The harness's args contract defines `byDesign` as 'known/tracked issues reviewers must NOT re-report' (tier2-review.template.js:76), and charter §8 feeds reviewers tracked issues through it. So any run whose caller passes its tracked-issue list loses every invariant its diff selected. Those are the records written because reviewers mistake the behaviour for a bug. A skeptic without them can then confirm a 'fix' that breaks a ruling. The loss is logged but not delivered. §5's 'a block cannot override an explicit instruction' does not justify replacing over concatenating, because concatenation overrides nothing. The fix's AC6 consequence: the `byDesign: 'x'` case must then assert both sources appear. | sound |
| 51 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-2.md:section 2 S7; section 5 perf / scale | medium | medium | confirmed | S7 says only that a DECISIONS row records the read, 'narrowing the no-fetch clause KICK-aReplayedCard-1 S8 set'. It pins no wording. Unit 4's P1 (spec-4 §4 line 91) tags a record only on a `supersede`-family verb followed by the id, with `'s` or `for` making the edge partial. A row that says 'narrows' therefore leaves KICK-aReplayedCard-1 (DECISIONS:15, 'no fetch') unlabelled in recall. That is the failure unit 4 exists to fix, here on this build's own first narrowing. KICK-aReplayedCard-1 §5 also budgets the card at ~1.6 s quiet with no network. Unit 2 adds a driver start (1.89 s) plus a fetch under a 15 s bound, and records the new walls only in its acceptance ledger. The pinned `SUPERSEDES KICK-aReplayedCard-1's ...` form matches P1 with the PARTIAL rule, so the fix produces the 'partly superseded' tag. | sound |
| 52 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-2.md:section 5 risks | low | low | confirmed | Unit 2 §5 risks says the `--claims` call's START and END lines go to a run log 'which nothing reads back'. That is false. runlog_lib.PRODUCER_FILES maps `driver` to `driver.log` (tools/runlog/runlog_lib.py:40). The driver journals every verb except --version and --plan (unattended.sh:10405-10412), and unit 1 does not add --claims to that list. Every card write therefore adds a slug-less invocation pair to the journal the runlog CLI and Skill read. The effect is noise in a read journal, which is minor. GOV_RUNLOG=0 is the environment switch that turns every line off (unattended.sh:10406), so the fix works. | sound |
| 53 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md:section 4 'The claim record'; section 8 F2 | low | - | refuted | F2 does weigh the registry-tag option, and rejects it for a stated reason: the tag needs the governing doc's registry, which the unattended kit can reach only through a path it does not own or a new conf key. The precedents the finding cites both read `$ROOT/AGENTS.md` directly (run-selftests.sh:286). The unattended driver reads no charter today; `grep AGENTS.md tools/unattended/unattended.sh` finds nothing. F2 also notes that the registry's Machine/user column keys a node by the OS user, so `daily-agent` maps to `a`. What remains is a display difference between the card's node line and the claim rows, in a field that only display and messages read. That is a choice with recorded reasons, not a defect. The fix is unsound. Its first option makes a shipped kit read the charter at a path it does not own, which is the exact cost F2 rejected. Its second option swaps in `host`, a machine name that is no closer to the tag `a` and so does not cure the mismatch it targets. | unsound |
