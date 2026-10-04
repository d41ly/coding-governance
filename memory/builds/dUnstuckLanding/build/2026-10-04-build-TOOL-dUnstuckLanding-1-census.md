# dUnstuckLanding — the closing-time failure census (research record)

**Serves:** research TOOL-dUnstuckLanding-1 TOOL-dUnstuckLanding-2

## Provenance

This record was read on 2026-10-04 by three read-only historian passes, one per repository, at these
tips:

| Repo | Tip read | Driver | Kit | Stop contract |
|---|---|---|---|---|
| gov | `origin/main` `a587e82d` | `tools/unattended/unattended.sh` | 1.56 | `UNATTENDED-STOPS.md`, with HELD and the inherited-red policy |
| inCMS | `incms/main` `bef832f9e` (the remote is named `incms`) | `scripts/unattended/unattended.sh` | 1.40 | none: no HELD, no inherited-red policy |
| NicoCares (nc) | `origin/main` `3368d475` | `scripts/unattended/unattended.sh` | older than 1.40 | none: no HELD, no inherited-red policy |

The orchestrator then re-verified everything below that this build's design rests on: the abort
counts, the witness-ancestry probe, and the driver lines. Figures are PINNED to those tips and to
this date.

## The headline

**`ABORTED` is the fleet's hand-off verb, and the record is never corrected afterwards.**

- **Aborts.** Across the three repositories, 37 unattended runs aborted: 15 in gov, 13 in nc and
  9 in inCMS.
- **Their work landed anyway.** The work of 36 of the 37 reached the default branch. The 37th,
  gov's `dHonouredPark`, had its record deleted (`994a93b0`), so its outcome cannot be read.
- **Most landed with the owner present.** 29 of those landings were attended merges, made between
  14 minutes and 41 hours after the abort commit. The rest were re-runs or pushes made before the
  abort.
- **The records still say ABORTED.** 28 run-state files read `phase: ABORTED` today: 8 in gov,
  12 in nc and 8 in inCMS.

**The landing is derivable for all of them.**

- **The probe.** For each record, ask whether its witness is an ancestor of the remote's default
  tip, using `git merge-base --is-ancestor`.
- **The result.** All 28 records read ON. So do the two retired records that have successors
  (nc `dCandidLodestar`, inCMS `aRisingCultivar`).
- **Liveness.** The probe was asserted live on two known-unmerged stamps, and both read OFF: nc
  `a7e0eb03` and inCMS `eafbff4f4`.

The same records carry the owner's two named causes:

- **A red the run did not cause**, coded `gate-red-out-of-scope` or `external-prerequisite`.
- **A closing decision the run would not take**, coded `fork-unresolvable`, `scope-approval-needed`
  or `repo-state-out-of-mandate`.

The halt codes over the 37 aborts:

| Code | gov | nc | inCMS | All |
|---|---|---|---|---|
| `gate-red-out-of-scope` | 4 | 2 | 6 | 12 |
| `external-prerequisite` | 1 | 9 | 1 | 11 |
| `fork-unresolvable` | 3 | 1 | 1 | 5 |
| `repo-state-out-of-mandate` | 2 | 1 | 1 | 4 |
| `scope-approval-needed` | 3 | 0 | 0 | 3 |
| before the vocabulary existed | 2 | 0 | 0 | 2 |

**What the abort reasons actually say.** In the abort reasons, the code is followed by a sentence
handing the landing to the owner:

- inCMS `aCharteredWard`: "Owner: land core local main when the bar is green".
- inCMS `aLanternedFoyer`: "the landing is left for the owner".
- nc `dBarredPostern`: "Do you want dPlumbedAtrium's record terminated, or this branch merged by
  hand?"

Six of inCMS's nine aborts do so in so many words (`history-incms` §a.1).

## The runs

### gov: ABORTED today, witness on `origin/main`

| Slug | Code | Died at | Landed after the abort, by | Evidence |
|---|---|---|---|---|
| `cBriefedPilot` | `fork-unresolvable` | close: would not judge whether 16 of 22 units was a landable build; bar 54/54 green | attended merge `d523861f` | abort `9ad35319` |
| `dClosedLexicon` | `fork-unresolvable` | mid-build: P3 non-convergent | attended merge `c48ccdaa` | abort `63ea7f5c` |
| `aWalkedCorpus` | `gate-red-out-of-scope` | lander: origin/main red on two legs | attended `31d08316` | abort `ae9aac36` |
| `aMeteredTurnstile` | `gate-red-out-of-scope` | lander: host process creation 25x slower | `6e73562c` | abort `4fe1f659` |
| `dScriptedRepeat` | `scope-approval-needed` | close: `build-complete` blocked on two owner forks | `0aa49bc3` | abort `c2b3576b` |
| `dMispairedQuote` | `gate-red-out-of-scope` | close: 85/86, kit check 2 on its own fold | `f0eb3239`, same day | abort `a22834c0` |
| `aHoistedPass` | `repo-state-out-of-mandate` | lander: diverged primary main, two bars killed at 3604 s and 3602 s | `8a36ff4e` | abort `36a90178` |
| `dTieredTribunal` | `repo-state-out-of-mandate` | after the push, killed before the marker; aborted BY ANOTHER run | pushed `b4e1d5be` BEFORE the abort | `d7ba0f67` |

The remaining seven gov aborts:

- **Re-run to LANDED.** Three were re-run to LANDED through a fresh `--preflight`: `aBoundedVerdict`,
  `aGradedDialect` and `aBatchedArm`.
- **Hand-flipped.** Three were hand-flipped to LANDED past check 26, on owner instruction
  (`56b945cb`): `aDeclaredBound`'s re-run, `aFusedCharter` and `aPromptedMandate`.
- **Deleted.** One was deleted (`dHonouredPark`, `994a93b0`).

**Overrides recorded at gov closes.** These have no abort, but the same pressures show in them:

- **`gates-green` 12.** Five of those were explicit owner "skip the bar" instructions.
- **`build-complete` 11.**
- **`specs-audited` 6.**

### nc: 13 aborts, 13 landed attended, 12 still ABORTED

- **The lone exception.** `dCandidLodestar`'s retired record has a LANDED successor run. Nothing
  else changed state.
- **The landings were quick.** Every merge followed its abort by 18 minutes to about 41 hours.
- **Every witness is on `origin/main`**, per the probe above.
- **Node b produced five of them.** Node `b` produced 4 aborts, plus `bGildedVestibule`, which is
  stuck at LANDING. nc's `CLAUDE.md:59` limits unattended landing to nodes `a` and `d`, and nothing
  at `--preflight` refuses a node-`b` run.
- **One record was overruled at merge.** `dPlumbedAtrium`'s own branch closed it to LANDED
  (`f33cce22`, `1f5e00ca`). The integration merge `23be1536` then deliberately kept main's ABORTED,
  because LANDED "would manufacture a state no sequence of verbs produced".

### inCMS: 9 aborts, 9 landed, 8 still ABORTED

- **The lone re-run.** `aRisingCultivar` was the only one re-run (`aba970028`) to LANDED.
- **The fastest landing.** `aTactfulWicket`'s attended merge `f20531108` came 14 minutes after its
  abort, `e97e657c5`.
- **Records short of a terminal.** Five records are stuck non-terminal although their work is on
  `incms/main`:
  - `dSnideCartographer`, `dWardedThreshold` and `dTimedHerald` are at LANDING.
  - `dPlumbedAtrium` is at VERIFYING.
  - `aClearedPortico` is at BUILDING.
- **Stamps that are not published.** Five more records were stamped LANDED on the `local` anchor
  and never pushed.

## Failure classes

Counts are instances per repository. A run can appear in more than one class.

| # | Class | gov | inCMS | nc | Resolved today by |
|---|---|---|---|---|---|
| K1 | a red bar the run did not cause | 14 | 15 | 22 | 9 overrides, 3 aborts, 1 hold-then-absorb and 1 policy landing in gov; abort-then-attended in the adopters |
| K2 | a closing decision deferred to the absent owner | 15 | 17 | 14 | abort or a `build-complete` override, then an owner turn |
| K3 | a terminal or near-terminal record that contradicts git | 8 | 18 | 14 | nothing; hand edits (`56b945cb`), deletion (`994a93b0`) or a re-run |
| K4 | the bar does not return, or returns red under load | 7 | 5 | 0 | overrides, aborts, `host-degraded` holds |
| K5 | lander-marker and `--landed` ordering defects | 5 | 0 | 4 | kit fixes (`dSealedTally-1`), some still open |
| K6 | the run cannot land from this node or this tree | 0 | 15 | 5 | abort `external-prerequisite`, then attended |

K1 counts INSTANCES, so a run can be counted in two sub-shapes. Per repository, the counts come
from each report's section b:

- **gov** — §B1.
- **inCMS** — B1, the shared ceiling (6 instances); B2, the load flake (6); and B5, the history legs
  (3).
- **nc** — B2, cross-repo (5 instances); B3, the foreign record (4); B4, build tenure (6); and B5, the
  history legs (7).

K6 is the node-b class in nc (B1). In inCMS it is the shared primary tree (B3: 1 abort and 9 parked
landings) together with submodule drift (B4, 5).

Every instance is cited in the per-repo detail below.

### K1 — a red bar the run did not cause

Five sub-shapes. They are distinct because each is cured by a different mechanism:

- **K1a — the leg is red on the default branch already.** Instances:
  - gov `aWalkedCorpus`: lexicon 450 against a pin of 417, plus the govkit selftest red at `43eb6b1`.
  - gov `aPrimedKeepalive`: five legs.
  - gov `aHonedRuleset` and `dTracedLattice`: the drift-audit pins.
  - gov `dAlignedCarrier`: the memory-recall selftest. It landed under policy, as
    `gates-inherited: 87c245b3`, and is the only policy landing on record.
  - gov `aSightedSkeptic`: the canary and the merge-rows replay, asks `TOOL-aSightedSkeptic-11` and
    `-12`.

  Duplicated effort is recorded too: `94a41505`, "two nodes fixed the same two red legs".
- **K1b — a FLEET counter the run's own bar grades over other builds' state.**
  - **The counters.** Three kinds:
    - The undeclared-write ceiling: inCMS check 23. `dSnideCartographer`'s never-closed record alone
      held 18 of 20 slots, which redded `aRenewedTether`, `dTuckedKebab` and `aTactfulWicket`.
    - Build tenure: nc, 6 midnight rollovers. Each was cleared by an owner pin raise, 0→2, 0→1,
      1→2 and 2→4 (nc `DECISIONS.md:234,245,303,370`).
    - The single-live-run check 7: nc ×4, and gov `aBoundedVerdict`.
  - **Gov has narrowed its own.** Check 23 now excludes generated renders and derived-LANDED records,
    and `UNDECLARED_WRITE_CEILING` is `0` (`.unattended.conf:342`). The single-live rule was retired
    at kit level (protocol §3). The adopters run older kits and carry neither fix.
- **K1c — a leg anchored in pushed history.**
  - **The legs.** `brief-recorded`, check 23 and `pass-order`.
  - **The instances.** nc ×7 and inCMS ×3.
  - **The trap.** The red can only be cured by rewriting history, which runs refuse as forgery
    (inCMS `dRelayedLatch/RUN.md:117`), or by moving a shrink-only knob. inCMS moved
    `BRIEF_RECORDED_CUTOFF` twice. nc moved it three times and raised `UNDECLARED_WRITE_CEILING`
    2→6→13. Once pushed, the red is inherited by the next build: nc `dSealedHandoff`,
    `.unattended.conf:147-153`.
- **K1d — load and environment flakes at the push-boundary bar.**
  - **The instances.** In inCMS: `aLanternedFoyer`, `aDeputedApothecary` and `aCharteredWard`
    aborted; `aBoxedCipher` overrode `gates-green`; `aRestoredTollbooth` hit two load reds. Gov
    `aMeteredTurnstile` aborted on a host-speed collapse.
  - **The signature.** `alembic upgrade head` subprocesses exit `0xC000070A`. The failing test
    differs each run, and every failing file passes alone.
  - **Never left-shifted.** No gotcha, ask or build in inCMS names the class.
- **K1e — the prerequisite is in another repository.** nc ×5: `aTiledEstuary`, `aBoxedCipher`,
  `aCharteredWard`, `aTactfulWicket` and `aGildedQuiver`.
  - **Why.** nc's gate 8 needs a core carrying the floor. Landing core is outside nc's authorization:
    "my unattended authorization is nc's build folder, not core's" (nc `aTiledEstuary/RUN.md:43`).
  - **The chain.** In three of the five, core's own run had already aborted on a red bar, so the
    reds chain across repositories.

### K2 — a closing decision deferred to the absent owner

The decisions, by kind. Each row cites one or two instances, and the per-repo reports list every
one:

| Kind | Example, with its stated reason |
|---|---|
| land a PARTIAL build | gov `cBriefedPilot`: "whether 16 of 22 units is a landable build. That is a scope decision". Gov `dScriptedRepeat`: an override of `build-complete` "would be the run authorizing itself past it" |
| move a shrink-only pin or cutoff | inCMS `aRisingCultivar`: "governance-carrier pin that may only fall (veto 2)". nc `aClearedPortico`: "Every past raise of this pin was owner-authorized" |
| act on ANOTHER run's record | nc `dBarredPostern` refused to "terminate another run's record to unblock my own". inCMS `aRenewedTether`: stamp `dSnideCartographer`, or not |
| publish another session's commits | inCMS `aMendedTollgate`: local main "carries EIGHT commits from at least three other sessions". Gov `aHoistedPass`: "would publish 13 commits whose own run chose not to publish them" |
| land in a dependency order | nc `aGildedQuiver`: "core cannot land unattended in this run" |
| choose a fix shape where every option touches a carrier | gov `dMispairedQuote`: "I refused to decide between them rather than pick the one that lands". Gov `aBatchedArm` |
| a question main had ALREADY answered | nc `dGuardedThreshold` parked a question that `74b010b4` had fixed on `origin/main` four hours earlier, because a run "pins its BASE at preflight and never fetches again" (nc gotcha `a-parked-decision-whose-answer-already-landed-on-main.md`) |

**The root cause sits in the build method.** BUILD-METHOD M3 makes park-not-pick the rule for every
veto-2 survivor: "No survivors → park, never the least-bad option" (`BUILD-METHOD.md:96`). At the
close, a park has only one terminal it can turn into, and that terminal is ABORTED. Gov widened the
delegation to "FULL delegation inside the build's stated goal" (`dUnstalledConvoy/README.md:117-125`),
but veto 2 still binds. The aborts that followed are `dMispairedQuote`, `aGradedDialect` and
`aBatchedArm`.

### K3 — the record contradicts git

- **The 28 ABORTED-but-landed records above.**
- **Ten LANDING records whose stamp never reached main.**
  - Under `primary`, the `--landed` stamp is a commit made AFTER the push, so it needs a second merge
    and push. nc merges that exist only to carry it: `c598108e`, `e2b7da36`, `3368d475`, `20d56100`
    and `cb458de3`. nc `dSpacedPlacard`'s `a7e0eb03` and inCMS `dTimedHerald`'s `eafbff4f4` were
    never merged.
  - Gov's in-place mode derives LANDED instead (`UNATTENDED-STOPS.md` §12), which closes this for
    gov only.
- **Records abandoned non-terminal.**
  - Gov `aClosedDocket` and `aUnblockedFleet` have sat at BUILDING since 2026-08-31. Both are
    announced as concurrent runs at every `--preflight`, this run's included.
  - inCMS `aClearedPortico` (BUILDING) and `dPlumbedAtrium` (VERIFYING).

**Why nothing repairs them.**

- **The terminal set is closed to writes.** `PHASES_TERMINAL="LANDED ABORTED"`
  (`unattended.sh:647`), and `refuse_if_terminal` (`:2675-2690`, fail 26) guards every writing verb.
- **Derivation covers LANDING only.** The derived terminal reads only a LANDING record
  (`read_derived_phase`, `:1160-1164`).
- **Rotation starts over.** The only exit is a fresh `--preflight` that rotates the record. That
  starts a NEW run, whose BASE post-dates the build's own closing review, so it costs a
  `closing-review-recorded` override every time (inCMS `aRisingCultivar/RUN.md:41`).

**Aborting is also rewarded in the adopters.** inCMS check 23 stops counting an ABORTED record
(`check-unattended.sh:2376`). `aRenewedTether`'s option (c) said so outright: "land attended now,
since this run is ABORTED and aborted records are excluded from check 23".

### K4 to K6, briefly

- **K4.**
  - Gov: `aHoistedPass` (3604 s and 3602 s against a 3600 s bound), `aThawedCorpus` (turnstile
    starvation) and `aSurfacedLexicon` (pass-order 4438 s against 900).
  - inCMS: the K1d load class.
  - Gov's backstop and `host-degraded` holds now cover the "did not return" half (protocol, Close).
  - **Root cause.** Several bars ran at once on one host, and the queue shares a single bound with the
    work. A bar that is killed or red under load reads the same as a failing leg (`history-gov` §B6,
    `history-incms` §B2).
- **K5.** Gov:
  - `--landed` wrote LANDED before check 34 could refuse, fixed by `dSealedTally-1`.
  - The marker shared across worktrees, `TOOL-aUnblockedFleet-7`.
  - `--close` staging LANDING with nothing to commit it, `TOOL-dUnstalledConvoy-24`.

  nc: a stale marker after a hook-bypassing push, `bGildedVestibule/RUN.md:54`.
  - **Root cause.** A post-push fact, the marker or the stamp, is written by a different act than the
    push. Each kill or bypass between the two acts leaves them disagreeing.
- **K6.**
  - nc node `b` cannot land (5 runs). nc's dependence on core is K1e, not K6.
  - inCMS lands from a shared primary tree whose local `main` carries other sessions' unpushed
    commits: 1 abort and 9 parked landings (`history-incms` §B3), plus submodule pointer drift
    (5 instances).
  - **Root cause.** The ability to land belongs to the NODE and the TREE, and nothing checks it at
    `--preflight`. So the run finds out at the lander, after every unit has been built.

## Why an inherited red is not resolved in-run

This answers the owner's question. Each mechanism below is cited at the gov tip unless the line says
otherwise.

1. **The adopters have no attribution at all.**
   - **No classifier.** Neither inCMS nor nc ships an inherited-red classifier. inCMS's
     `push-main.sh:183-187` sorts a gate verdict only as `gate-red`.
   - **The landing rule.** Both landing rules demand a fully green bar through the lander: inCMS
     `CLAUDE.md:243-250` and nc `CLAUDE.md:58`.
   - **The override buys nothing.** A `gates-green` override at `--close` lets the record reach
     LANDING, and then the lander's pre-push bar re-runs and refuses. nc `dBarredPostern`: "an
     override records a fact, it does not satisfy the condition". inCMS `dSnideCartographer`:
     "a --close override records a judgement about the Definition of Done, it does not turn a red
     leg green".
2. **The kit default PARKS.**
   - **The default.** Under `park`, every inherited red ends in the hold
     `hold · inherited-red · until probe gate` (`UNATTENDED-STOPS.md` §13).
   - **The release.** That hold's release, `probe gate`, re-runs the bar, which is red again until
     somebody ELSE fixes main.
   - **Gov's own policy.** Gov runs `INHERITED_RED=land` with `INHERITED_RED_MAX_AGE=10`
     (`.githooks/gate-env.sh:92-93`). A red older than 10 landings still parks.
   - **Usage so far.** No `inherited-red` hold has ever been taken in gov (`git log -S'hold-code:
     inherited-red'` is empty). The policy has landed exactly once, for `dAlignedCarrier`.
3. **One non-inherited leg blocks every exit.** `check_inherited_override` (`unattended.sh:7115`,
   fail 83 at `:7148`) refuses both `--override gates-green` and `--abort --code
   gate-red-out-of-scope` unless EVERY red leg reads INHERITED, on a clean tree that has not moved.
4. **Attribution is conservative on purpose.** Two runner rules (`run-gates.sh:2385-2400`) push a
   red to OWN:
   - KF3 forces OWN when the diff touches the runner.
   - Rule 3 makes a red OWN when the diff touches the leg's COMPARATOR.

   The runner's header gives the reason: "Five recorded stops were a run deciding, with nobody to
   ask, that a red 'was not mine', and at least two of those claims were wrong" (`:2373-2375`). Gov
   `aSightedSkeptic`'s canary was "proven inherited at base but read OWN because unit 9 touched its
   comparator".
5. **ABSORB is narrow.** STOPS §13 admits an absorb only with no M3 veto tripped and KF3 not
   triggered. Veto 2 excludes every governance carrier, and that includes the shrink-only pins,
   which "never rise". In practice runs absorb only the mechanical reds: clone-ratchet, lexicon and
   hygiene (inCMS `aRisingCultivar` `57e40fffa`, `aLatchedVestibule`). The one gov absorb,
   `68d6c009`, came only after an owner turn.
6. **The fix lives somewhere the run may not write.** Four places, each ruled out by its own rule:
   - another run's record;
   - another session's dirty primary tree;
   - pushed history, which K1c covers;
   - another repository, which K1e covers.
7. **The red is found late.**
   - **One bar per session.** The bar runs once per session, at the close (`DECISIONS.md:112`), and
     the kit self-tests are off the bar by owner ruling 2026-08-23.
   - **Nobody tells the run sooner.** Nothing tells a run at START which reds it will inherit. The
     close is the first time anyone sees them, and by then the only owner turn is spent.
8. **The run never looks again.**
   - **A frozen BASE.** BASE is pinned at `--preflight`, and nothing re-fetches before a park or an
     abort. A red that main already fixed is reported as a blocker (nc `dGuardedThreshold`).
   - **The in-place exception.** Gov's in-place `--prepare` re-merges the advertised tip before the
     bar, so this gap is closed for gov's bar. It is not closed for its parks, and it is not closed
     in `primary` mode.

## Sources

The three historian reports this record condenses were written to the session scratchpad and are
not tracked. Every claim above carries the citation they gave, and the orchestrator re-ran the
witness probe and the driver line reads.
