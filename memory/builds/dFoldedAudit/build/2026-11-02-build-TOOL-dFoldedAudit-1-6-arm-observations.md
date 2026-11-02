# dFoldedAudit — the RED-first arm observations

**Serves:** journal TOOL-dFoldedAudit-1

The runnable `New arm:` lines of units 1 to 15 were observed in scratch clones of the run branch at 951f44e43, before the main merge. The driver lives in the session scratchpad and is not tracked. Each run cloned HEAD, staged one break as exact string edits, re-rendered where a template moved, ran its suite under Git bash, and logged to its own file. One unbroken clone ran every suite to observe GREEN.

GREEN at HEAD, `base-green`: every suite exits 0 except `tools/check-spec-tokens.test.sh`, whose two parity arms (`a manifest suite invocation BAR does not match`, `graded 54 + exempt 14 != the manifest's 69 selftests legs`) fail at BASE too. They are attributed INHERITED in `2026-11-02-build-TOOL-dFoldedAudit-16-1-first-bar.md`. The deviation-join plants read `audit-fold` 0, `audit-fold-pass` 0, and `stranger`, `foreign`, `norev` and `closed` 1.

The 58 arms in `tools/unattended/unattended.test.sh` and `check-unattended.test.sh` are not observed here. The owner chose to land without them, as recorded in `prompts/2026-11-02-prompt-TOOL-dFoldedAudit-1-owner-land.md`.

## H1-rows-stub

Break: `deriveDispositionFault` returns empty, in `tools/workflows/unattended-build.template.js`. RED, read from the run's log:

    [rc 0]
    ok   GH28 the head reworded and committed: the leg reds with DRIFT
    FAIL FA3 AC2 specs empty: disposal NOT done -- output lacked 'disposal: NOT done'
    FAIL FA3 AC2 specs empty: an empty roster -- output lacked '"roster":[]'
    FAIL FA3 AC2 specs empty: a DEGRADED note -- output lacked 'DEGRADED'
    FAIL FA3 AC2 specs empty: no record agent ran -- output carried 'agent:record' and must not
    FAIL FA3 AC2 specs empty: the reason -- output lacked 'names no spec'
    FAIL FA3 AC2 unit absent: disposal NOT done -- output lacked 'disposal: NOT done'
    FAIL FA3 AC2 unit absent: an empty roster -- output lacked '"roster":[]'
    FAIL FA3 AC2 unit absent: a DEGRADED note -- output lacked 'DEGRADED'
    FAIL FA3 AC2 unit absent: no record agent ran -- output carried 'agent:record' and must not
    FAIL FA3 AC2 unit absent: the reason -- output lacked 'outside the {id, severity, nature, specs, unit, rev} shape'

## H2-independent

Break: terminal test narrowed to `DONE`, read-rev pinned to 1, bound highs from all HIGHs, chain-record order and the terminal next action removed, in `tools/workflows/unattended-build.template.js`. RED, read from the run's log:

    [rc 0]
    FAIL attended, DONE (FORKED): SKIPPED, not refused -- output lacked 'SKIPPING 1 terminal unit'
    FAIL attended, terminal units: still hands out a roster -- output lacked '"roster":[{'
    FAIL attended: a surviving unit is still IN the ROSTER -- output lacked 'A-tB-2'
    FAIL AC25: units still counts the WHOLE ordered set, not the roster -- output lacked '"units":2'
    FAIL AC25: the skipped unit is still reported in skippedTerminal -- output lacked '"skippedTerminal":["A-tB-1"]'
    ok   GH28 the head reworded and committed: the leg reds with DRIFT
    FAIL FA3 AC1 a local HIGH folds under by-nature -- output lacked 'disposal: done — promoted 0 · folded 1'
    FAIL FA3 AC1 ...beside a non-empty roster -- output lacked '"roster":[{'
    FAIL FA3 AC1 ...and the row counts the fold -- output lacked '--highs 1 --minors 0 --folded 1 --promoted 0 --disposition fold'
    FAIL FA4 AC2 a sibling at DONE (THIN): disposal NOT done -- output lacked 'disposal: NOT done'
    FAIL FA4 AC2 a sibling at DONE (THIN): an empty roster -- output lacked '"roster":[]'

## H3-declared-ending

Break: the declared-disposal ending forced false, in `tools/workflows/unattended-build.template.js`. RED, read from the run's log:

    [rc 0]
    ok   GH28 the head reworded and committed: the leg reds with DRIFT
    FAIL FA12 AC1 the note carries: --record-round tB --subject tB-spec-set-r1 --audited "A-tB-1 A-tB-2" -- output lacked '--record-round tB --subject tB-spec-set-r1 --audited "A-tB-1 A-tB-2"'
    FAIL FA12 AC1 the note carries: --chain-verdict tB -- output lacked '--chain-verdict tB'
    FAIL FA12 AC1 the note carries: --finding <id>/<severity>/<nature>/<spec>[,<spec>]/<unit>/<rev> -- output lacked '--finding <id>/<severity>/<nature>/<spec>[,<spec>]/<unit>/<rev>'
    FAIL FA12 AC1 the note carries: CONTINUE: re-invoke this harness with round: 2 -- output lacked 'CONTINUE: re-invoke this harness with round: 2'
    FAIL FA12 AC1 the note carries: STOP: dispatch every unit -- output lacked 'STOP: dispatch every unit'
    FAIL FA12 AC1 the note carries: HOLD: run the recipe it prints -- output lacked 'HOLD: run the recipe it prints'
    FAIL FA12 AC3 the note orders: commit the disposal's folds and specs -- output lacked 'commit the disposal's folds and specs'
    FAIL FA12 AC3 the note orders: --record-round -- output lacked '--record-round'
    FAIL FA12 AC3 the note orders: commit the chain record it staged -- output lacked 'commit the chain record it staged'
    FAIL FA12 AC3 the note orders: --chain-verdict -- output lacked '--chain-verdict'

## H4-declared-always

Break: the declared-disposal ending forced true, and both by-nature guards removed, in `tools/workflows/unattended-build.template.js`. RED, read from the run's log:

    [rc 0]
    ok   GH28 the head reworded and committed: the leg reds with DRIFT
    FAIL FA3 AC1 a local HIGH folds under by-nature -- output lacked 'disposal: done — promoted 0 · folded 1'
    FAIL FA3 AC1 ...beside a non-empty roster -- output lacked '"roster":[{'
    FAIL FA3 AC1 ...and the row counts the fold -- output lacked '--highs 1 --minors 0 --folded 1 --promoted 0 --disposition fold'
    FAIL FA3 AC2 specs empty: the reason -- output lacked 'names no spec'
    FAIL FA3 AC2 unit absent: the reason -- output lacked 'outside the {id, severity, nature, specs, unit, rev} shape'
    FAIL FA3 AC2 rev not bumped: the reason -- output lacked 'a fold is a rev bump'
    FAIL FA3 AC2 dispositions absent: the reason -- output lacked 'no `dispositions` list'
    FAIL FA3 AC4 one HIGH graded MEDIUM: the reason -- output lacked 'a grade cannot be lowered to hide a HIGH'
    FAIL FA3 AC4 folded 2 beside one entry: the reason -- output lacked 'the integers and the list are one fact'
    FAIL FA3 AC4 one confirmed id unnamed: the reason -- output lacked 'confirmed finding(s) 8 have no `dispositions` entry'

## H5-inverted

Break: `byNature` inverted, in `tools/workflows/unattended-build.template.js`. RED, read from the run's log:

    [rc 0]
    FAIL NON-CONVERGENT handed out no roster, so a terminal verdict cannot land a build
    FAIL CEILING handed out no roster, so a terminal verdict cannot land a build
    FAIL BOUNDED handed out no roster, so a terminal verdict cannot land a build
    FAIL V1 ...and the log says the rule, on CONVERGED too -- output lacked 'disposing by severity, on CONVERGED too'
    FAIL V1 ...and the roster is handed out -- output lacked '"roster":[{'
    FAIL MT promoted 13 into 10 units, by raw id, is ACCEPTED -- output lacked 'disposal: done — promoted 13 · folded 0'
    FAIL MT ...and the roster is handed out -- output lacked '"roster":[{'
    FAIL MT ...and the harness disposes the unverified population -- output lacked 'disposal: done — promoted 48 · folded 0'
    FAIL MT ...and the record counts the 48 promoted UNVERIFIED findings as minors -- output lacked '--blockers 0 --highs 0 --minors 48 --disposition promote'
    FAIL MT20 control: item-typed counts refuse the raw-id disposal, as measured -- output lacked '11 unit(s) where at most 7 fit'
    FAIL MT20 promoted 16 into 11 units, by raw id, is ACCEPTED -- output lacked 'disposal: done — promoted 16 · folded 0'

## T1-tally

Break: the tally's `addressOwed` clause removed, in `tools/workflows/tier2-review.template.js`. RED, read from the run's log:

    [rc 0]
    FAIL address: a diff review's HIGH with no specs counts
    FAIL address: an undeclared spec audit's HIGH with no specs counts
    FAIL executed 355 assertions against a floor of 357 — arms are UNREACHABLE rather than absent; look for a block stranded past an early exit or a die()
    [rc 1]

## T2-owed

Break: `addressOwed` without its disposal test, in `tools/workflows/tier2-review.template.js`. RED, read from the run's log:

    [rc 0]
    FAIL address: an undeclared spec audit's HIGH with no specs counts
    FAIL address: the undeclared prompt carries no **Specs:** line
    FAIL executed 355 assertions against a floor of 357 — arms are UNREACHABLE rather than absent; look for a block stranded past an early exit or a die()
    [rc 1]

## S1-supersede

Break: per-line search, and the supersede waiver exemption removed, in `tools/check-spec-tokens.py`. RED, read from the run's log:

    arm FAIL  parity: a manifest suite invocation BAR does not match:
    arm FAIL  parity: graded 54 + exempt 14 != the manifest's 69 selftests legs — a leg was skipped without being printed
    arm ok    a carry of an id no clause has REDS as [carries] ghost
    arm ok    a chain spec carrying nothing and derived from nothing REDS as [carries] unbound
    arm ok    a pin that is not the view's hash REDS as [carries] stale, naming both hashes
    arm ok    --list reads the waived hit as WAIVED [carries]
    arm ok    two whole carriers of one clause REDS as [carries] ambiguous
    arm ok    two part carriers pinning two hashes REDS as [carries] ambiguous, naming both
    arm ok    parts 1/3 and 3/3 REDS as [carries] parts
    arm ok    a carry of an id the record withdraws at the baseline REDS as [carries] withdrawn
    arm ok    a malformed Carries line REDS as [carries] malformed, and never as unbound
    arm ok    the same second carrier at OPEN REDS as [carries] ambiguous, so the status is what set it apart

## P1-parity

Break: 'derived verdict' removed from M4 in both copies, in `tools/memory-tree/BUILD-METHOD.template.md`. RED, read from the run's log:

    kit-parity: tools/memory-tree/BUILD-METHOD.template.md has no 'derived verdict' in M4, so a spec audit's disposal or a closing review's is no longer stated
    [rc 1]

## P2-precision-ci

Break: a lowercase 'precision' added to M4 in both copies, in `tools/memory-tree/BUILD-METHOD.template.md`. RED, read from the run's log:

    kit-parity: tools/memory-tree/BUILD-METHOD.template.md still holds PRECISION in M4, and precision bounds no chain
    [rc 1]

## PP-protocol

Break: one line appended to the render, in `memory/guides/REVIEW-PROTOCOL.md`. RED, read from the run's log:

    protocol-parity: DRIFT — memory/guides/REVIEW-PROTOCOL.md does not match tools/workflows/REVIEW-PROTOCOL.template.md rendered for this install ('tools/workflows')
    [rc 1]

## CU-check22-26

Break: the SPEC_FOLD_CUTOFF table rows and the --chain-verdict verb entry removed, in `tools/unattended/PROTOCOL.template.md`. RED, read from the run's log:

    UNATTENDED check 22 FAILED — the protocol's binding key table and the declared conf disagree, so a key is either configurable and undocumented or documented and dead. undocumented in the protocol: SPEC_FOLD_CUTOFF  | documented but in no example: none | set by this project and undocumented: SPEC_FOLD_CUTOFF
    UNATTENDED check 26 FAILED — a declared verb has no entry in the verb carrier, so the contract a run is measured against does not describe a verb that run can call: --chain-verdict in /tmp/fa-CU-check22-26/tools/unattended/VERBS.template.md
    [rc 1]

## D1-fold-false

Break: `check_audit_fold` forced False, in `tools/memory-tree/design_lib.py`. RED, read from the run's log:

    plant audit-fold rc 1
    plant audit-fold-pass rc 1
    plant audit-fold-stranger rc 1
    plant audit-fold-foreign rc 1
    plant audit-fold-norev rc 1
    plant audit-fold-closed rc 1
    [rc 0]

## D2-fold-true

Break: `check_audit_fold` forced True, in `tools/memory-tree/design_lib.py`. RED, read from the run's log:

    plant audit-fold rc 0
    plant audit-fold-pass rc 0
    plant audit-fold-stranger rc 0
    plant audit-fold-foreign rc 0
    plant audit-fold-norev rc 0
    plant audit-fold-closed rc 1
    [rc 0]

## D3-status

Break: the terminal-status test removed, in `tools/memory-tree/deviation_join.py`. RED, read from the run's log:

    plant audit-fold rc 0
    plant audit-fold-pass rc 0
    plant audit-fold-stranger rc 1
    plant audit-fold-foreign rc 1
    plant audit-fold-norev rc 1
    plant audit-fold-closed rc 0
    [rc 0]

## G1-index

Break: the past-pin range capped at one revision, in `tools/memory-tree/gen_build_index.py`. RED, read from the run's log:

    arm FAIL  TOOL-dFoldedAudit-6 AC7 — one revision past the pin citing nothing keeps the unit, named at the pin — expected to see: Ids whose spec moved past its audited revision: ARCH-tOne-1@rev-1.
    arm ok    TOOL-dTrueNorth-6 AC8 — and --check exits 1 listing the view under build-index DRIFT, at its first differing line and naming the clause that cites no record
    arm ok    TOOL-dTrueNorth-8 S3 — and --check exits 1 listing the stale view under build-index DRIFT, with no as-built VERDICT
    arm ok    TOOL-dTrueNorth-17 S3 — a kit path staged alone over a committed record the view does not count: --check --staged exits 1 listing the stale view under build-index DRIFT
    arm ok    TOOL-dTrueNorth-20 AC34 — a staged git rm of a record the view counts: --check --staged renders and exits 1 listing the view under build-index DRIFT
    FAIL — 1 arm(s) failed
    [rc 1]

## G2-reviews-path

Break: the `/reviews/` path test removed, in `tools/memory-tree/gen_build_index.py`. RED, read from the run's log:

    arm FAIL  TOOL-dFoldedAudit-15 AC28 — a cited record outside reviews/ clears nothing, and its pin still counts — expected to see: ['ARCH-tOne-1@rev-1']
    arm ok    TOOL-dTrueNorth-6 AC8 — and --check exits 1 listing the view under build-index DRIFT, at its first differing line and naming the clause that cites no record
    arm ok    TOOL-dTrueNorth-8 S3 — and --check exits 1 listing the stale view under build-index DRIFT, with no as-built VERDICT
    arm ok    TOOL-dTrueNorth-17 S3 — a kit path staged alone over a committed record the view does not count: --check --staged exits 1 listing the stale view under build-index DRIFT
    arm ok    TOOL-dTrueNorth-20 AC34 — a staged git rm of a record the view counts: --check --staged renders and exits 1 listing the view under build-index DRIFT
    FAIL — 1 arm(s) failed
    [rc 1]

## G3-view

Break: the as-built view restored to its pre-fold blob, in `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`. RED, read from the run's log:

    [rc 0]
    build-index DRIFT — run: python tools/memory-tree/gen_build_index.py --write
        memory/builds/dDeclaredLoop/README.md (stale — differs from a fresh render)
    [rc 1]

## M1-revlog

Break: the rev-3 revision-log line deleted, in `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md`. RED, read from the run's log:

    HYGIENE check 12 FAILED — spec files dated >= 2026-07-15 not conforming to memory/TEMPLATE-SPEC.md:
    [rc 1]

## K1-carries

Break: the carries pin restored to the stale 166df103, in `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md`. RED, read from the run's log:

    spec-tokens: memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md [carries] `carries <- stale:cl-dClosedLoop-0117` — pins cl-dClosedLoop-0117@166df103, and the clause's text in the view hashes afb50a20 (a stale pin)
    [rc 1]

## R1-roles

Break: the old one-driver-verb sentence restored in both copies, in `tools/roles/SKILL.template.md`. RED, read from the run's log:

    FAIL arm 18 the render's ATTENDED bullet names the chain's two verbs
    FAIL (1 of 63)
    [rc 1]

