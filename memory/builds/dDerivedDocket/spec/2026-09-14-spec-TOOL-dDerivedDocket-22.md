# TOOL-dDerivedDocket-22 — LANDED derived from the tip

**Status:** SPECCED · rev-2 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 22

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md) | spec-audit | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |

<!-- /gen:spec-records -->

## 1. Goal

A landing becomes terminal only when `--landed` runs after the push and finds a lander marker
naming exactly the commit it validated. Every gap between the push and that verb leaves a record
stuck at LANDING: a kill after the push and before the marker (i150, `dTieredTribunal/RUN.md:55`), a
marker naming the `--no-ff` merge rather than the witness (TOOL-dUnstalledConvoy-38), a marker
another landing overwrote (TOOL-aUnblockedFleet-7). And when `--landed` does write LANDED, that write
follows the push, so no bar ever grades it (TOOL-aBoundedCeiling-9). By owner ruling D12-i2, LANDED
is DERIVED instead: a LANDING record whose own commit is reachable from the tip the remote advertises
is landed. Only `--status`, the phase readers and the leg compute it (KF5); no committed file does.

## 2. Scope (IN)

- **S1** `landing_commit_of <run-state file>` in `tools/unattended/lib-unattended.sh`, shared by the
  driver and the leg: the commit that last changed the run-state file, provided the file is unchanged
  from HEAD's copy and that copy reads `phase: LANDING`; otherwise nothing. Observed by AC1 and AC8.
- **S2** `derived_phase()` returns LANDED when the recorded phase is LANDING and that commit is an
  ancestor of the advertised default tip, and the recorded phase otherwise. The tip is observed only
  for a LANDING record; an unanswered remote leaves the phase LANDING with a stated reason. It
  observes through a quiet helper that returns a code, never through `fail`, so no caller inherits
  the observation's refusal. Observed by AC1, AC2 and AC5.
- **S3** `--status` prints the derived phase with its evidence, or the reason it stays LANDING.
  Observed by AC1 and AC5.
- **S4** `--preflight` on a derived-LANDED record ROTATES it (KF15). In one write it sets
  `phase: LANDED`, `witness: <C>` and `landed-derived: <C> <advertised tip>`, C being the landing
  commit. It then retires the record to the name `archive_name_of` derives from those bytes,
  `RUN.LANDED.<blob8>.md`. No record is edited after it is retired. Before any write, the rotation
  refuses with a number when the record lacks a fact that the landed fact-set arm (S10) would
  require of the retired copy, and it names `--landed` under `primary`, so a rotation never freezes a
  record the leg reds. The predicate is one function in `tools/unattended/lib-unattended.sh`, shared
  with S10. Observed by AC6 and AC12.
- **S5** `--resume` on a derived-LANDED record reports nothing to resume and never invokes the
  lander. Observed by AC6.
- **S6** Under `LANDER_MODE=in-place`, `--close` writes `units-at-landing`, and `asks-at-landing`
  wherever that fact applies, beside the LANDING phase in the record it commits. Under `primary` both
  stay at `--landed`. Observed by AC3.
- **S7** Under `LANDER_MODE=in-place`, `--landed` tests terminality on the RECORDED phase through
  `refuse_if_terminal --recorded`, and only then reads `derived_phase`. A derived LANDED prints the
  derivation and exits 0, writing nothing to the tree. It refuses with a new numbered code when the
  landing commit is on local `<def>` and not on the advertised tip (KF4's local arm), and when no
  LANDING record is committed at all. Observed by AC4.
- **S8** Under `primary`, check 34 becomes ANCESTRY: the marker's commit is on the advertised tip,
  and the witness is that commit or an ancestor of it (TOOL-dUnstalledConvoy-38). `--landed` tests
  the recorded phase here too. A record whose committed LANDING has already reached the advertised
  tip, which is the state `--close`'s own instruction to commit before landing produces, therefore
  proceeds to the ancestry test and writes its facts. It is not refused as finished. Observed by AC7.
- **S9** The leg. Check 7's exclusion (`tools/unattended/check-unattended.sh:1520`) reads S1's
  commit instead of the witness, and reports the record `derived LANDED`. Check 4 needs no change,
  because a rotated record says LANDED (S4). Check 15 reads a `landed-derived` fact as the anchor
  evidence of a LANDED record that carries one: no `landed-anchor` is required, since no in-place
  verb writes it, and the landing commit the fact names must be an ancestor of the advertised tip.
  Check 15's `LANDED_ANCHOR_CUTOFF` grandfathering dates a record by
  `git log --follow --diff-filter=A`, as `DISPOSITION_CUTOFF` does, so a rotation does not re-date a
  pre-cutoff record into the graded set. The driver's twin of that exclusion, `check_single_live`
  (`tools/unattended/unattended.sh:1260-1306`), reads the same S1 commit, so preflight and the leg
  agree about one record. Observed by AC6, AC8 and AC9.
- **S10** A leg arm for the weak form of TOOL-aBoundedCeiling-11, graded BY MODE. Every record is
  dated by its first commit, read with `git log --follow --diff-filter=A`, against a new
  `LANDED_FACTS_CUTOFF`: blank turns the arm off, announced, and gov sets the landing date. There are
  three graded populations. (i) A recorded LANDED record without `landed-derived` carries every fact
  `--landed` writes on its arm: `landed-anchor`, `units-at-landing` and `unpushed-at-landing`. (ii) A
  recorded LANDED record carrying `landed-derived`, which only S4's rotation writes, carries
  `units-at-landing` and `landed-derived`. (iii) While the conf's `LANDER_MODE` is `in-place`, a
  committed LANDING record, one S1's `landing_commit_of` finds, carries `units-at-landing`, which S6
  writes at close. Under `primary`, a committed LANDING record the leg derives LANDED is REPORTED
  naming `--landed <slug>` and is never graded, because `--landed` is the verb that completes it.
  `asks-at-landing` is left to the freeze-presence arm (S15). The arm prints its graded count per
  population on one line, and a count of 0 announces itself. The predicate is one function in
  `tools/unattended/lib-unattended.sh`, shared with S4's rotation refusal. Observed by AC9, AC12 and
  AC16.
- **S11** `tools/memory-tree/gen_build_index.py` is not touched: the committed LIVE index renders the
  recorded phase. Observed by AC10.
- **S12** Protocol §6 states the derived terminal in one sentence citing D12-i2, and the rest goes to
  the companion stops guide; the Skill's Land section names the in-place `--landed` as an
  observation. Protocol §2's rotation paragraph states that a derived-LANDED record is written
  LANDED with its evidence before it is retired. It keeps the rule that no retired record is edited,
  and the rule that an archived non-terminal phase reds. Observed by AC11.
- **S13** No unattended version constant moves here: this unit's bytes ride the move
  `TOOL-dDerivedDocket-1` S9 makes once for the build. NOT OBSERVED by a criterion here:
  `kit version markers` grades the final tree's constant-marker agreement.
- **S14** The unattended suites run once at the unit's end under attribution against BASE. Observed by
  AC13.
- **S15** Under `LANDER_MODE=in-place` the freeze is written at `--close` (S6). So the
  freeze-presence arm, `TOOL-dDerivedDocket-18` S4 reporting under check 15, also grades every
  committed LANDING record that carries an `asks:` fact, a committed record being one S1's
  `landing_commit_of` finds. It does so in the same commit that moves the freeze. Under `primary` the
  arm keeps grading recorded LANDED only. A record S4 rotated says LANDED and is graded as before.
  Observed by AC14.
- **S16** Under `in-place`, `--landed`'s successful observation removes the slug's lease file. It
  lives under the git common dir, so the tree stays clean. The process-ledger unit removes its
  ledger at the same point. Observed by AC15.
- **S17** For a LANDING record whose landing commit (S1) is an ancestor of the advertised tip, the
  run's-own-commits function (unit 17) takes that landing commit as its endpoint and, as its
  exclusion, the first parent of the first two-parent commit on that commit's first-parent chain
  (unit 2's prepared merge). Unit 19's cross-run arm and unit 17's T4 read it. Observed by AC17.

## 3. Non-goals (OUT)

- **Deriving LANDED in the LIVE generator or any committed file** (KF5). LIVE is freshness-gated,
  so a derivation there would red check 9 after every landing, because the remote tip moves while
  the committed index does not.
- **Pinning `branch-ref` on a default-branch anchor.** DR 21.4 U20 listed it; KF4 struck it.
- **D12-i2's option (b)**, append-only `pending|landed` marker lines and a numbered second landing.
- **Re-keying the shared lander marker** (TOOL-aUnblockedFleet-7's candidate). The in-place path
  reads no marker; the primary path keeps the shared one, whose race still fails closed.
- **ABORTED records' fact set.** TOOL-aBoundedCeiling-11 is about LANDED, and so is S10.
- **`derived_phase()` itself, HELD and the lease.** They are the HELD unit's; this unit adds one
  branch inside the function and relies on the call sites the HELD unit classifies, including
  `refuse_if_terminal --recorded` for `--landed`.
- **The close commit and the prepared merge.** The landing-path and in-place lander units own both.
- **`asks-at-landing` as a fact.** The asks-disposed unit defines it; this unit moves where it is
  written under in-place, exactly as that unit's hand-off asks.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-3` — the LANDING record committed on the prepared merge under
  `LANDER_MODE=in-place`. Without it the in-place path has no landing commit to find, and `--landed`
  has no in-place mode to be an observation under.
- **consumes-from** `TOOL-dDerivedDocket-4` — `derived_phase`, `recorded_phase` and the call-site
  table that classifies every phase read, inside which S2 goes, the resume row that never re-drives
  the lander, and the stops companion guide S12 writes into.
- **consumes-from** `TOOL-dDerivedDocket-17` — `asks-at-landing`, whose write moves to `--close`
  beside `units-at-landing` under in-place landing, and the run's-own-commits function S17 extends.
- **consumes-from** `TOOL-dDerivedDocket-1` — the "no NEW FAIL" reading of the unattended suites
  under `--attribute` against BASE, which this unit's final criterion (AC13) uses.
- **consumes-from** `TOOL-dDerivedDocket-18` — the freeze-presence arm (S4 there), whose population
  S15 extends to a committed in-place LANDING record.
- **consumes-from** `TOOL-dDerivedDocket-19` — the cross-run arm whose derived-LANDED endpoint S17
  supplies, and the unattended-suite arms that unit added, which this unit's AC13 run executes
  first.
- **consumes-from** `TOOL-dDerivedDocket-20` — the unattended-suite arms that unit added, which this
  unit's AC13 run executes first.
- **hands-off** `TOOL-dDerivedDocket-28` — the in-place removal point, `--landed`'s successful
  observation, where that unit removes its ledger.

## 4. Design

### Data model

```
RUN.md facts   units-at-landing: <ids>           written by --close under in-place (S6)
               landed-derived: <landing sha> <advertised tip sha>   written by --preflight only,
                                                  with phase LANDED and witness <landing sha>, in
                                                  the one write before the rotation (S4)
--status       unattended: <slug> · phase LANDED (derived: <C8> on <aref> at <tip8>) · ...
               unattended: <slug> · phase LANDING (not on the remote: <why>) · ...
.unattended.conf  LANDED_FACTS_CUTOFF="<landing date>"   blank = the S10 arm is off, announced
```

### Finding the landing commit

```
git diff --quiet HEAD -- <rel> || return          # the record must be the committed one
[ "$(git show "HEAD:<rel>" | sed -n 's/^phase: //p' | head -1)" = LANDING ] || return
git log -1 --format=%H HEAD -- <rel>              # the commit that produced this content
```

By CONTENT, not by subject: the in-place close commits with a fixed subject, but a primary-mode
close is committed by the agent under a subject of its own, so a subject key would find one mode's
records. And never by walking the file's history back to the newest LANDING copy: the run-state
path is reused after a rotation, so that walk passes a staged, uncommitted LANDING and finds an
EARLIER run's landing commit, which is on the remote and would derive the new run landed. A staged
LANDING has no landing commit and cannot derive, which is right: that record never reached any
history a remote could carry.

### Where the tip comes from

`derived_phase` observes the advertised tip through a QUIET helper that returns a code and prints
nothing, in the shape of `branch_tip_quiet` (`tools/unattended/unattended.sh:821`). It never goes
through `observe_anchor`'s `fail`, which prints to stdout and sets the global `status` with no
reset. It observes only for a LANDING record, so `--status` on every other record stays offline. An
unanswered remote, or an advertised tip whose object this clone lacks, leaves the phase LANDING with
its reason in the second global. Every caller then reads LANDING, the writing verbs
`refuse_if_terminal` guards among them, and none inherits a refusal.

### The readers

| Reader | Derives? | Why |
|---|---|---|
| `derived_phase()`, hence `refuse_if_terminal`, preflight's rotation test, `--resume`, `--status` | yes | KF5 and KF15 |
| `--landed`'s terminal guard | no, recorded | its own postcondition is the terminal; a derived guard refuses it after every good landing |
| the leg's check 7 exclusion | yes | it already observes the advertised tip (`ADV_HEAD`) |
| `check_single_live`, the driver's twin of check 7's exclusion | yes, through `landing_commit_of` | preflight and the leg must agree about one record |
| the leg's check 4 | no, recorded | unchanged; a rotated record is terminal by its own bytes |
| the leg's check 15 | reads `landed-derived` | a rotated derived record says LANDED and names its landing commit (S4, S9) |
| the freeze-presence arm (check 15) | committed LANDING under in-place, plus recorded LANDED | the freeze is due at close under in-place (S15) |
| the leg's S10 fact-set arm | by mode: recorded LANDED, rotated derived LANDED, and committed LANDING under in-place | the facts are due at close under in-place and at `--landed` under primary |
| `archive_name_of` | no, recorded | S4 writes LANDED before the name is derived, so the recorded phase is the terminal |
| the leg's check 19 cross-run arm (unit 19) | yes | a landed record's range must end at its landing commit, or the owner's default-branch grant reds it |
| `gen_build_index.py` and `memory/LIVE.md` | no | KF5: committed and freshness-gated |

### In-place `--landed`

It stays in the Skill's four-step sequence because it is the one step that confirms the push carried
the record. It writes nothing, so no LANDED commit follows the push and TOOL-aBoundedCeiling-9's
mechanism has no instance. The two refusals are one new code, allocated at build time as the next
integer above the driver's highest, because other units of this build allocate codes concurrently.

### Check 34 under `primary`

`push-main.sh` writes `landed <def> at <sha> by push-main`, and that sha is the merge the lander
pushed. The check becomes: the marker names a sha M; `git merge-base --is-ancestor M <advertised tip>`;
and the witness is M or `git merge-base --is-ancestor <witness> M`. The equality test it replaces
could never pass on a `--no-ff` landing, which is the shape the charter mandates.

### The fact-set arm

Graded on the record's FIRST-commit date, read with `git log --follow --diff-filter=A` exactly as
`DISPOSITION_CUTOFF` reads it. Without `--follow` a rotation re-dates the record to the rotation
commit: aPacedTurnstile's `RUN.LANDED.a1fd98d8.md` reads 2026-08-20 without it and 2026-08-18 with
it. The fix lands at check 15's `LANDED_ANCHOR_CUTOFF` site in the same change. The arm's header
states what `--follow` does NOT do: it takes the oldest add along the followed history, and a reused
`RUN.md` path can date a later run's archive to an earlier run's first commit, which errs toward
grandfathering and never toward a frozen red.

In gov's in-place mode no post-cutoff record says LANDED until a rotation, so rev-1's arm graded an
empty population. Population (iii) is where gov's landed records are, and (ii) is where they go once
rotated. A hand-committed, pushed `phase: LANDING` with none of the close's facts is exactly (iii)'s
red, which is the hand-reached terminal TOOL-aBoundedCeiling-11 records. A new key, not the anchor
cutoff: `memory/builds/dCarriedReceipt/RUN.md` was first committed after 2026-08-21 and deliberately
carries no `unpushed-at-landing`, because the driver measures it at landing time and it was not
reconstructable (TOOL-aBoundedCeiling-11). Reusing the anchor cutoff would red it forever.

### Files touched (estimate)

`tools/unattended/lib-unattended.sh` · `tools/unattended/unattended.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.test.sh` · `tools/unattended/PROTOCOL.template.md` · the stops
companion template · `tools/unattended/SKILL.template.md` · `tools/unattended/.unattended.conf.example`
· `.unattended.conf` · the rendered guides and Skill · `memory/map/features/unattended.md`.

### Alternatives rejected

- **Finding the landing commit by the close commit's subject.** Tested against the two modes: only
  the in-place close has a fixed subject, so every primary-mode record would never derive.
- **Deriving from the witness, as check 7's exclusion does at BASE.** It answers whether the WORK is
  on the remote, not the RECORD. A primary-mode run that pushed before committing its LANDING record
  has its witness on the remote and a record nobody pushed; a witness reading calls that landed.
- **A `landed` fact written at `--close`** (D12-i2 option c). The owner rejected it: a refused push
  would leave a false LANDED on the branch.

## 5. Production-readiness checklist

- security — the derivation adds no authority: it reads refs and the observation `--landed`
  already trusts. A run cannot make a record derive LANDED without its record commit reaching the
  remote's advertised tip, which the pre-push hook gates.
- perf / scale — one `git log` over one file's history and one ancestry test, plus a remote
  observation only for a LANDING record.
- error / empty / loading states — an unanswered remote keeps LANDING with the reason; an
  uncommitted LANDING has no landing commit and says so; an unreadable committed copy is skipped as
  not LANDING, never read as one.
- observability — the derived line in `--status` names the landing commit, the ref and the tip.
- risks — a stale-by-design LIVE index: LIVE shows LANDING for a landed build until the next
  preflight rotates it. That is KF5's stated price. Clone-local refs can lag the remote, so the leg
  and `--status` read the advertisement, never `refs/remotes`.
- testing — arms in `tools/unattended/unattended.test.sh` over a scratch repository with a bare
  remote, and in `tools/unattended/check-unattended.test.sh` for S9 and S10, each staged RED.
- migration — additive. Every record at BASE is either terminal already or LANDING; the corpus's
  stuck LANDING records with pushed work derive LANDED on the next `--status` and rotate on the next
  preflight of their slug. A stuck LANDING record derives LANDED only in a clone that holds the
  advertised tip's object, and on an unfetched clone the reason line says to fetch.
- user docs — protocol §6's sentence, the companion guide's paragraph and the Skill's Land section.

## 6. Acceptance criteria

- **AC1** — When a fixture's committed LANDING record is pushed to its bare remote's default branch,
  `--status` prints `phase LANDED (derived:` naming that commit; with the same commit merged into
  local main only, it prints `phase LANDING (not on the remote:`; and with an earlier run's LANDING
  commit of the same path on the remote and the current LANDING only staged, it prints LANDING.
  Red when: the derivation reads local `<def>`, or walks the path's history back to an earlier run's
  landing commit, so an unpushed record derives LANDED.
- **AC2** — When the fixture's lander stub pushes and is killed before writing its marker, `--status`
  still derives LANDED.
  Red when: the derivation requires the lander marker, which is the i150 window left open.
- **AC3** — When `--close` succeeds under `LANDER_MODE=in-place` in a mandated fixture, the committed
  record carries both `units-at-landing` and `asks-at-landing`. With the fixture's `ASKS_CMD` witness
  failing, `--close` refuses before any write. Under `primary` the same close writes neither line.
  Red when: the freeze stays at `--landed`, so the pushed record never carries its roster or its
  asks.
- **AC4** — When `--landed` runs under in-place with the landing commit on the advertised tip, it exits
  0, prints the derivation, and `git status --porcelain` stays empty; with the landing commit merged
  into local main only, it refuses with a numbered message naming the local arm; and with the record
  commit already on the advertised tip before `--landed` runs, it is not refused on check 26.
  Red when: `--landed` writes `phase: LANDED` after the push, or accepts the local arm; or the guard
  reads the derived phase, so `--landed` refuses the run as finished after every good landing.
- **AC5** — When the fixture's `origin` URL names a missing path, `--status` on a LANDING record prints
  the unanswered observation as its reason and exits exactly as it does for LANDING at BASE; and
  `--hold` and `--abort` on that LANDING record, with the same unanswered remote, exit exactly as they
  do on a working-phase record, and their stdout carries no `UNATTENDED check` line.
  Red when: an unanswered remote reads as landed, or its refusal leaks into the verb's exit status;
  or `--hold` or `--abort` inherits the observation's refusal through the global status, so a correct
  write exits 1.
- **AC6** — When `--resume` runs on a derived-LANDED fixture record, it prints nothing to resume and
  the lander stub records no invocation. When `--preflight` then runs, the record is retired to a
  `RUN.LANDED.` name whose `phase:` reads LANDED and which carries `witness` and `landed-derived`
  naming the landing commit. `bash tools/unattended/check-unattended.sh` over the rotated tree then
  reports no check 4 or check 15 failure for it.
  Red when: the archive keeps `phase: LANDING`, so check 4 reds a frozen record forever; or preflight
  refuses the record as a live run or overwrites it; or the resume re-drives the lander.
- **AC7** — When `--landed` runs under `primary` on a `--no-ff` landing whose record commit is already
  on the advertised tip, whose marker names the merge commit, and whose witness is that merge's second
  parent, it succeeds and writes `phase: LANDED`. With a marker naming a commit the remote does not
  advertise, it refuses on check 34.
  Red when: check 34 keeps equality, which no `--no-ff` landing can satisfy; or the terminal guard
  reads the derived phase and refuses before check 34 runs.
- **AC8** — When `bash tools/unattended/check-unattended.sh` grades a fixture holding a LANDING record
  whose witness was pushed and whose record commit was not, check 7 counts it live; with the record
  commit pushed too, it prints `derived LANDED` and excludes it; and `--preflight` of another slug
  over the same fixture announces the record live in the first case and finished in the second.
  Red when: check 7 keeps the witness reading, so the leg and `--status` disagree about one record;
  or `check_single_live` keeps the witness reading, which moves the disagreement into the driver.
- **AC9** — When the leg grades a fixture LANDED record that was first committed after
  `LANDED_FACTS_CUTOFF` and is missing `units-at-landing`, it reds naming the fact.
  `memory/builds/dCarriedReceipt/RUN.md` is not graded by the arm. Neither is a pre-cutoff LANDED
  record rotated to a `RUN.LANDED.` name after the cutoff, and check 15 does not red that rotated,
  anchorless, pre-cutoff record for naming no anchor kind. A blank cutoff prints that the arm is off.
  Red when: the arm is keyed on `LANDED_ANCHOR_CUTOFF`, which reds a record that cannot be
  repaired; or either site dates a record without `--follow`, so a rotation re-dates a pre-cutoff
  record into the graded set.
- **AC10** — When this grep runs at the unit's build commit, it prints 0:
  `grep -cE 'ls-remote|landing_commit_of|derived_phase|is-ancestor' tools/memory-tree/gen_build_index.py`
  Red when: the generator reads the advertised tip, or runs an ancestry test against it, so the
  committed index goes stale on the next remote move.
- **AC11** — When `bash tools/unattended/check-unattended.sh` and the skill-wiring check run over the
  rendered tree, the protocol's terminal sentence names the derivation, the companion carries the
  rest, and the Skill's Land section calls in-place `--landed` an observation.
  Red when: the protocol still states a terminal is reached only by a verb while `--status` derives
  one.
- **AC12** — When `--preflight` runs under `primary` on a derived-LANDED fixture record that was first
  committed after `LANDED_FACTS_CUTOFF` and lacks `units-at-landing`, it refuses with a numbered
  message naming `--landed`, and the record is neither edited nor moved. The same record first
  committed before the cutoff rotates.
  Red when: the rotation retires a record that the fact-set arm then reds, and no verb can repair it
  once it is archived.
- **AC13** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once at the
  unit's end, it reports no NEW failure, and every arm units 19 and 20 added to the unattended suites
  passes; a NEW failure in one of those arms names its owning unit, whose fix lands before this unit
  closes.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: the brief lists this unit among those allowed to run the unattended suites (D12-i8).
- **AC14** — When the leg grades a fixture under `LANDER_MODE=in-place` holding a committed LANDING
  record that carries `asks:` and no `asks-at-landing:`, check 15 reds naming the record. The same
  record under `primary` does not red, and with the fact present it passes.
  Red when: the arm grades only records whose recorded phase is LANDED, which in gov's mode are none
  until a rotation, so the second opinion never fires.
- **AC15** — When `--landed` observes a derived LANDED under `in-place` in the fixture, the slug's
  lease file is gone and `git status --porcelain` is empty.
  Red when: no verb removes the lease after an in-place landing, so an unanswered remote later reads
  a landed run as `presumed-stopped` and offers a take-over.
- **AC16** — When the leg runs over a fixture whose conf declares `LANDER_MODE=in-place`, holding a
  hand-committed LANDING record that was first committed after `LANDED_FACTS_CUTOFF` and carries no
  `units-at-landing`, it reds naming the fact and prints the arm's graded count per population. Over
  a fixture with no graded record, it prints a count of 0. Under `primary`, the same record derived
  LANDED is reported naming `--landed` and does not red.
  Red when: the arm grades only records that SAY LANDED, so in gov's own mode its population is
  empty and it passes on nothing.
- **AC17** — When check 19's cross-run arm grades a derived-LANDED in-place fixture record while an
  unpushed owner commit on the default branch adds `may:` to a build README, it does not red; a
  `may:` line added by that run's own commit reds.
  Red when: the arm reads the derived-LANDED record as live, so its range becomes whatever the
  graded tree has not pushed and the owner's push is blocked.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `pass-order history` · `memory hygiene` · `kit version markers` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · a pushed and an unpushed LANDING record, a lander killed after its push, an in-place local-arm landing, and `--landed` in each mode with the record commit already on the advertised tip · none
New arm: tools/unattended/check-unattended.test.sh · a record whose witness was pushed and record was not, and a LANDED record missing a fact after the cutoff · none
New arm: tools/unattended/check-unattended.test.sh · a derived-LANDED record rotated through --preflight, then graded by the leg through one helper every archive-producing arm calls · none
New arm: tools/unattended/check-unattended.test.sh · a pre-cutoff LANDED record, anchorless and without the landing facts, rotated after the cutoff · none
New arm: tools/unattended/check-unattended.sh self-scan · a `--diff-filter=A` first-commit date without `--follow` under `tools/unattended/`, the predicate run over the tree with hits and near-misses printed before it is wired (charter §7); `check-unattended.sh:1276` is a live hit at BASE · none

## 8. Open questions

- **F1 — how does a landing become terminal?** RESOLVED (owner, 2026-09-13): D12-i2, DERIVED from
  the advertised tip, computed only by `--status` and the leg (KF5).
- **F2 — what does `--landed` do under in-place?** Options: (a) an observation that writes nothing;
  (b) refuse outright; (c) write LANDED as today. (c) is TOOL-aBoundedCeiling-9's mechanism, and (b)
  breaks the landing path's four-step sequence. RESOLVED (agent, 2026-09-14, delegated): (a).
- **F3 — how is the landing commit found?** Options: the close subject, a recorded fact, or the
  record's committed content. A fact cannot name its own commit, and a subject exists in one mode.
  RESOLVED (agent, 2026-09-14, delegated): content, per §4.
- **F4 — which cutoff grandfathers the fact-set arm?** RESOLVED (agent, 2026-09-14, delegated): a new
  `LANDED_FACTS_CUTOFF`, because the existing anchor cutoff would red a record that cannot be
  repaired (§4).
- **F5 — how does rotation retire a derived-LANDED record?** Options: (a) write `phase: LANDED`,
  `witness` and `landed-derived` before retiring, so the archive says what the derivation found; (b)
  keep `phase: LANDING`, and teach checks 4, 7 and 15 to accept an archived LANDING whose
  `landed-derived` commit is on the advertised tip. Under (b), check 4 depends on the remote for every
  archived in-place record, each recorded-phase reader learns a second rule, and `archive_name_of`
  names the file `RUN.LANDING.` rather than KF15's `RUN.LANDED.`. RESOLVED (agent, 2026-09-14,
  delegated): (a). The LANDED line is written only after `--preflight` has derived it from the
  advertised tip, so it records D12-i2's derivation. It is not D12-i2's rejected option (c).
- **F6 — which unit extends the freeze-presence arm to the in-place population?** Options: (a) the
  leg second-opinions unit, at its own order; (b) this unit, in the commit that moves the freeze to
  `--close`. Under (a) the grader's population precedes its producer by four units. RESOLVED (agent,
  2026-09-14, delegated): (b), which that unit's §3 already anticipated.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR 21.4 U20 with KF4, KF5 and KF15. Departs from DR in
  three places: DR's AC4 (`branch-ref` on a default-branch anchor) is struck per KF4; `--status` does
  not observe the remote at BASE, contrary to KF5's premise, so S2 adds the observation for LANDING
  records only; and in-place `--landed` becomes an observation (F2). One edge the brief's table does
  not list is added: consumes-from unit 17, whose own spec already hands the freeze to this unit.
- rev-2 · 2026-09-14 · §2 S2 S4 S7 S8 S9 S10 S12 S13 S15 S16 S17 · §3 · §4 · §5 · §6 AC3 to AC10,
  AC12 to AC17 · §7 · §8 F5 F6 · round-1 spec-audit fold (G1 B1, B2, H4, H6, M4, M5, M9, M11, M16,
  L1, L2, L5; G3 H7, H8, M5). `--landed` guards on the recorded phase, so a good landing is no
  longer refused as finished (AC4, AC7). Rotation writes `phase: LANDED`, `witness` and `landed-derived` before
  retiring a derived-LANDED record, replacing rev-1's keep-LANDING rule (F5, AC6), and refuses to
  freeze a record the fact-set arm would red (AC12). Check 15 reads `landed-derived`, and both
  first-commit cutoffs date with `--follow`. The fact-set arm is graded by mode over three
  populations with a liveness count (AC9, AC16); this states DR U20's fact set per mode rather than
  narrowing it. AC10 is a grep, not a BASE diff. `derived_phase` observes through a quiet helper.
  S15 extends the leg second-opinions unit's freeze arm to the in-place LANDING population (F6,
  AC14). S16 removes the lease at in-place `--landed` (AC15). `check_single_live` joins the
  derivation. S13 rides the held-suite baseline unit's version move. G3 H7: S17 supplies the
  derived-LANDED endpoint of unit 17's run's-own-commits function, and the readers table gains the
  cross-run arm (AC17). G3 M5: AC13's run is the first execution of units 19's and 20's
  unattended-suite arms. Adds consumes-from units 1, 18, 19 and 20, and a hands-off edge to unit 28.

## 10. Reuse audit

- **Probe result.** `reuse_lookup.py` over "derive a landed phase from the commit the remote
  advertises" returned name-stem matches only (`derive_scope`, `derive_lf`, `derive_carried`) and
  reports `.sh` unscanned, so it is blind to the driver. Reading source found the seams: the
  remote-arm ancestry test in `verb_landed` (`tools/unattended/unattended.sh:2342`),
  `observe_anchor`, `archive_name_of` and the rotation half in `verb_preflight`, the `set_fact`
  freeze of `units-at-landing` (`tools/unattended/unattended.sh:2435`), and check 7's advertised-tip
  exclusion in the leg, which is the derivation's precedent — it already treats a pushed LANDING as
  finished and only calls it "not counted".
- **DR against BASE.** KF5 says `--status` already observes the advertised tip; `verb_status`
  (`tools/unattended/unattended.sh:2790`) reads local facts only. DR's check-34 and freeze citations
  hold at BASE, because `unattended.sh` did not move between `09a22d2b` and `abac6d59`.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: LANDED LANDING landed-anchor lander-marker check-34 advertised-tip ADV_HEAD
  derived witness units-at-landing rotation no-ff — passed as `--terms` with the question "how does
  an unattended run become terminal once its landing is on the remote, and why does the lander
  marker fail". Top hits: TOOL-dUnstalledConvoy-38, the dSealedTally acceptance ledger,
  TOOL-dScaffoldedMirror-22, TOOL-aUnblockedFleet-7 and TOOL-aBoundedCeiling-11.
