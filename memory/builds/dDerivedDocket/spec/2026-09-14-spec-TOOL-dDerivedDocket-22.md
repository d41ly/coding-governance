# TOOL-dDerivedDocket-22 — LANDED derived from the tip

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 22

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
  for a LANDING record; an unanswered remote leaves the phase LANDING with a stated reason. Observed
  by AC1, AC2 and AC5.
- **S3** `--status` prints the derived phase with its evidence, or the reason it stays LANDING.
  Observed by AC1 and AC5.
- **S4** `--preflight` on a derived-LANDED record ROTATES it (KF15): it writes a `landed-derived`
  fact naming the landing commit and the advertised tip, then retires the record to
  `RUN.LANDED.<blob8>.md`. The recorded `phase: LANDING` line is never rewritten. Observed by AC6.
- **S5** `--resume` on a derived-LANDED record reports nothing to resume and never invokes the
  lander. Observed by AC6.
- **S6** Under `LANDER_MODE=in-place`, `--close` writes `units-at-landing`, and `asks-at-landing`
  wherever that fact applies, beside the LANDING phase in the record it commits. Under `primary` both
  stay at `--landed`. Observed by AC3.
- **S7** Under `LANDER_MODE=in-place`, `--landed` is an OBSERVATION: it prints the derivation and exits
  0 when LANDED derives, writing nothing. It refuses with a new numbered code when the landing commit
  is on local `<def>` and not on the advertised tip (KF4's local arm), and when no LANDING record is
  committed at all. Observed by AC4.
- **S8** Under `primary`, check 34 becomes ANCESTRY: the marker's commit is on the advertised tip,
  and the witness is that commit or an ancestor of it (TOOL-dUnstalledConvoy-38). Observed by AC7.
- **S9** The leg's check 7 exclusion (`tools/unattended/check-unattended.sh:1520`) reads S1's commit
  instead of the witness, and reports the record `derived LANDED`. Observed by AC8.
- **S10** A leg arm for the weak form of TOOL-aBoundedCeiling-11: a LANDED record whose first commit
  is at or after a new `LANDED_FACTS_CUTOFF` carries every fact `--landed` writes on its arm —
  `landed-anchor`, `units-at-landing` and `unpushed-at-landing`. Blank turns it off, announced; gov
  sets the landing date. Observed by AC9.
- **S11** `tools/memory-tree/gen_build_index.py` is not touched: the committed LIVE index renders the
  recorded phase. Observed by AC10.
- **S12** Protocol §6 states the derived terminal in one sentence citing D12-i2, and the rest goes to
  the companion stops guide; the Skill's Land section names the in-place `--landed` as an
  observation. Observed by AC11.
- **S13** The unattended kit version moves once for this build. Observed by AC12.
- **S14** The unattended suites run once at the unit's end under attribution against BASE. Observed by
  AC13.

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
  branch inside the function and relies on its four callers already reading through it.
- **The close commit and the prepared merge.** The landing-path and in-place lander units own both.
- **`asks-at-landing` as a fact.** The asks-disposed unit defines it; this unit moves where it is
  written under in-place, exactly as that unit's hand-off asks.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-3` — the LANDING record committed on the prepared merge under
  `LANDER_MODE=in-place`. Without it the in-place path has no landing commit to find, and `--landed`
  has no in-place mode to be an observation under.
- **consumes-from** `TOOL-dDerivedDocket-4` — `derived_phase()` and its four callers, inside which S2
  goes, the resume row that never re-drives the lander, and the stops companion guide S12 writes
  into.
- **consumes-from** `TOOL-dDerivedDocket-17` — `asks-at-landing`, whose write moves to `--close`
  beside `units-at-landing` under in-place landing.

## 4. Design

### Data model

```
RUN.md facts   units-at-landing: <ids>           written by --close under in-place (S6)
               landed-derived: <landing sha> <advertised tip sha>   written by --preflight only,
                                                  immediately before the rotation (S4)
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

`observe_anchor` (`tools/unattended/unattended.sh:692`), the observation `--landed` and `--close`
already trust, with its integrity checks. It is called only when the recorded phase is LANDING, so
`--status` on every other record stays offline. `fail` sets a global status with no reset in that
file, so in `--status` the call's refusal is captured and printed as the reason the phase stays
LANDING, and never leaks into the verb's exit status.

### The readers

| Reader | Derives? | Why |
|---|---|---|
| `derived_phase()`, hence `refuse_if_terminal`, preflight's rotation test, `--resume`, `--status` | yes | KF5 and KF15 |
| the leg's check 7 exclusion | yes | it already observes the advertised tip (`ADV_HEAD`) |
| the leg's check 15 and S10 | no | they grade what a record SAYS it is, and a derived record says LANDING |
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

Graded on the record's FIRST-commit date, the idiom `LANDED_ANCHOR_CUTOFF` already uses. A new key
and not that one: `memory/builds/dCarriedReceipt/RUN.md` was first committed after 2026-08-21 and
deliberately carries no `unpushed-at-landing`, because the driver measures it at landing time and it
was not reconstructable (TOOL-aBoundedCeiling-11). Reusing the anchor cutoff would red it forever.

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
  preflight of their slug.
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
- **AC3** — When `--close` succeeds under `LANDER_MODE=in-place` in the fixture, the committed record
  carries `units-at-landing`; under `primary` the same close writes no such line.
  Red when: the freeze stays at `--landed`, so the pushed record never carries its roster.
- **AC4** — When `--landed` runs under in-place with the landing commit on the advertised tip, it exits
  0, prints the derivation, and `git status --porcelain` stays empty; with the landing commit merged
  into local main only, it refuses with a numbered message naming the local arm.
  Red when: `--landed` writes `phase: LANDED` after the push, or accepts the local arm.
- **AC5** — When the fixture's `origin` URL names a missing path, `--status` on a LANDING record prints
  the unanswered observation as its reason and exits exactly as it does for LANDING at BASE.
  Red when: an unanswered remote reads as landed, or its refusal leaks into the verb's exit status.
- **AC6** — When `--resume` runs on a derived-LANDED fixture record, it prints nothing to resume and
  the lander stub records no invocation; when `--preflight` then runs, the record is retired to a
  `RUN.LANDED.` name carrying a `landed-derived` fact and its original `phase: LANDING` line.
  Red when: preflight refuses the record as a live run or overwrites it, or the resume re-drives the
  lander.
- **AC7** — When `--landed` runs under `primary` on a `--no-ff` landing whose marker names the merge
  commit and whose witness is that merge's second parent, it succeeds; with a marker naming a commit
  the remote does not advertise, it refuses on check 34.
  Red when: check 34 keeps equality, which no `--no-ff` landing can satisfy.
- **AC8** — When `bash tools/unattended/check-unattended.sh` grades a fixture holding a LANDING record
  whose witness was pushed and whose record commit was not, check 7 counts it live; with the record
  commit pushed too, it prints `derived LANDED` and excludes it.
  Red when: check 7 keeps the witness reading, so the leg and `--status` disagree about one record.
- **AC9** — When the leg grades a fixture LANDED record first committed after `LANDED_FACTS_CUTOFF`
  and missing `units-at-landing`, it reds naming the fact; `memory/builds/dCarriedReceipt/RUN.md` is
  not graded by the arm; a blank cutoff prints that the arm is off.
  Red when: the arm is keyed on `LANDED_ANCHOR_CUTOFF`, which reds a record that cannot be repaired.
- **AC10** — When `git diff abac6d59 -- tools/memory-tree/gen_build_index.py` runs at the unit's build
  commit, it is empty.
  Red when: the generator reads the derivation, and the committed index goes stale on the next
  remote move.
- **AC11** — When `bash tools/unattended/check-unattended.sh` and the skill-wiring check run over the
  rendered tree, the protocol's terminal sentence names the derivation, the companion carries the
  rest, and the Skill's Land section calls in-place `--landed` an observation.
  Red when: the protocol still states a terminal is reached only by a verb while `--status` derives
  one.
- **AC12** — When `bash tools/check-kit-versions.sh` runs, the unattended version constant and every
  rendered marker agree.
  Red when: the constant moves and a render keeps the old marker.
- **AC13** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once at the
  unit's end, it reports no NEW failure.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: the brief lists this unit among those allowed to run the unattended suites (D12-i8).

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `pass-order history` · `memory hygiene` · `kit version markers` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · a pushed and an unpushed LANDING record, a lander killed after its push, and an in-place local-arm landing · none
New arm: tools/unattended/check-unattended.test.sh · a record whose witness was pushed and record was not, and a LANDED record missing a fact after the cutoff · none

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

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR 21.4 U20 with KF4, KF5 and KF15. Departs from DR in
  three places: DR's AC4 (`branch-ref` on a default-branch anchor) is struck per KF4; `--status` does
  not observe the remote at BASE, contrary to KF5's premise, so S2 adds the observation for LANDING
  records only; and in-place `--landed` becomes an observation (F2). One edge the brief's table does
  not list is added: consumes-from unit 17, whose own spec already hands the freeze to this unit.

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
