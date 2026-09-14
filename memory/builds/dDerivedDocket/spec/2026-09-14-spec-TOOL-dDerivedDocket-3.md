# TOOL-dDerivedDocket-3 — the run's landing path

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

`gates-green` is one boolean over `$GATE_CMD` run in the run's own tree, so it grades the branch and
never the merge that actually lands; a branch green alone can land red once merged onto a tip the
remote moved. And the unattended landing still goes through the primary tree and local main. Wire
the in-place lander into the run: a declared lander mode, a Land step that prepares the merge
before the close, a close whose bar grades that prepared merge, records committed on it, and a
landing that cannot complete ending HELD instead of on local main.

## 2. Scope (IN)

- **S1** `LANDER_MODE`, a closed set `primary|in-place` in `.unattended.conf`, blank reading as
  `primary` and announced as a default. Gov's conf sets `in-place`; the kit's conf example documents
  both. The driver and the kit gate validate it. Observed by AC5 and AC9.
- **S2** Under `in-place`, `--preflight` runs `$LANDER --carry --slug <slug>` once as a liveness
  probe of the declared lander. An exit of 2 refuses preflight, naming `LANDER_MODE`; 0 and 1 are
  both a lander that implements the mode. Observed by AC5.
- **S3** Under `in-place`, `gates-green` refuses, numbered, unless HEAD carries a prepared merge by
  the lander's definition, and otherwise runs `$GATE_CMD` with `GATE_FULL=1` exported, plus
  `GATE_SELFTESTS=1` when the landing range touches a path the new `SELFTESTS_OWED_PATHS` key lists.
  It runs before `--close` writes anything. Observed by AC1, AC2 and AC10.
- **S4** Under `in-place`, `--close` asks `$LANDER --carry --slug <slug>` after the Definition of
  Done evaluates and before any write, and refuses on exit 1 quoting the lander's list. Observed by
  AC6.
- **S5** Under `in-place`, `--close` COMMITS its run-state change on top of the prepared merge with
  the subject `records(<slug>): close — LANDING`, leaving the tree clean, which closes
  TOOL-dUnstalledConvoy-24 for this mode. The push boundary's scoped bar then covers that
  records-only delta, because the full-green stamp at the prepared merge sits in the same git dir.
  Observed by AC3 and AC7.
- **S6** The Skill's Close and Land sections and protocol §6 carry the in-place sequence —
  `{{LANDER}} --prepare`, then `--close`, then `{{LANDER}} --land`, then `--landed` — with reconcile
  only from the remote's default branch onto the run branch, never through local main. A landing the
  lander could not complete pushes the branch and holds, never merges into local main. Observed by
  AC4.
- **S7** Under `primary`, every verb behaves as at BASE. Observed by AC9.
- **S8** Arms in `tools/unattended/unattended.test.sh` and `tools/unattended/check-unattended.test.sh`,
  run once at the unit's end under attribution. Observed by AC11.

## 3. Non-goals (OUT)

- The lander's own flags and the carry predicate. They are the in-place landing merge unit's, and
  this unit calls them rather than re-spelling them.
- Deriving LANDED from the advertised tip, and `--landed` refusing the local-main arm in `in-place`
  mode (KF4). The derived-terminal unit owns both, and receives this unit's committed LANDING record.
- The charter's §1 sentence recording the unattended landing exception (D12-i3). That text is the
  charter-template unit's; this unit writes the rule where D12-i3 says it lives, in the protocol.
- A relaxed or second stamp kind for a landing over inherited reds (KF2). The inherited-red policy
  unit adds `gate-inherited-green`; this unit only ever writes the ordinary stamp, and only green.
- The bound the landing bar runs under. It stays `GATE_BOUND` until the declared-wall unit derives
  it; the risk that a full bar with self-tests outlasts that bound is stated in §5.
- Attributing a red landing bar leg. The red-attribution unit owns that; here a red bar is unmet.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-1` — the "no NEW FAIL" criterion for the unattended suites
  this unit runs once at its end.
- **consumes-from** `TOOL-dDerivedDocket-2` — `--prepare`, `--land` and `--carry`, their refusal
  texts and the definition of a prepared merge that `gates-green` tests for.
- **consumes-from** `TOOL-dDerivedDocket-4` — `derived_phase()` and HELD's refusal of `--close`,
  the `--hold` verb an incomplete landing ends with, and the companion guide the landing text
  overflows into.
- **hands-off** `TOOL-dDerivedDocket-22` — the LANDING record committed on the prepared merge, from
  which that unit derives LANDED once the remote carries it, and the in-place mode `--landed` must
  refuse the local arm under.

## 4. Design

### The sequence under `in-place`

```
{{LANDER}} --prepare --slug <slug>            # merge onto the advertised tip, in this worktree
bash {{KIT_DIR}}/unattended.sh --close <slug> # bar on the prepared merge, carry check, commit
{{LANDER}} --land --slug <slug>               # push HEAD to the default branch through the hook
bash {{KIT_DIR}}/unattended.sh --landed <slug>
```

The order is forced by one fact: the full-green stamp is written only by a clean, unmoved run
(`tools/run-gates/run-gates.sh:1855`), so the bar must run on the prepared merge before the close
writes a byte, and the push must reuse that stamp rather than pay a second full bar. The lab showed
the graded merge, its stamp and the push resolving one git dir from the run's own worktree.

### `gates-green`

| Mode | Precondition | Command |
|---|---|---|
| `primary` | none, as at BASE | `$GATE_CMD` |
| `in-place` | HEAD carries a prepared merge, tested by the three facts the lander defines | `GATE_FULL=1 [GATE_SELFTESTS=1] $GATE_CMD` |

The self-test term is derived, never assumed. The landing range is `<T^1>..HEAD`; when any path it
touches starts with an entry of `SELFTESTS_OWED_PATHS`, the bar gets `GATE_SELFTESTS=1`. Blank means
never, announced, which is the charter's "owed by a DoD only for KIT work" with the kit surface
declared rather than guessed. Gov declares its kit roots. Nothing here runs the unattended kit's
own suites, which live in no manifest; `GATE_SELFTESTS=1` runs only held manifest legs.

A refusal of the precondition is a numbered failure that names `{{LANDER}} --prepare`, never an
unmet item: an unmet `gates-green` invites an override, and an override here would land an ungraded
merge.

### `--close` under `in-place`

1. Every Definition-of-Done item evaluates, `gates-green` among them, with the tree clean.
2. `$LANDER --carry --slug <slug>`, bounded by `run_bounded`. Exit 1 refuses, quoting the list; exit
   2 refuses as a lander that does not implement the mode.
3. The LANDING phase and its facts are written.
4. The run-state change is committed with the subject in S5, bounded, and the commit's own hooks run
   as for any commit. The subject names the slug and no unit id, so `build_commit` never takes it
   for a unit's build commit.

Under `primary`, step 2 does not run and step 4 stays a stage, exactly as at BASE.

### What an incomplete landing does

The lander's `unreachable` and exhausted-race outcomes are not a reason to merge anywhere. The run
pushes its branch, so the prepared merge and the committed close survive the session, then runs
`--hold --code platform-unavailable --until after <now + 30 minutes>` with the lander's last line as
the reason. The lander's `red` outcome is a red push-boundary bar; it holds under the same code only
when the red is the bound firing, and is otherwise a fix-and-re-prepare, because a red the run
caused is the run's work.

### Where the text goes

The protocol stands at 57,815 of its 61,440-byte cap at BASE, and HELD's two rows land first. §6 is
rewritten in place, not appended to: the two-anchor paragraph stays for the derived-terminal unit,
the lander paragraph becomes the four-step sequence, and anything past a net growth of 400 bytes
moves to the companion guide. The Skill's Close section gains the prepare step above its command,
and its Land section carries both modes, because the Skill is one render shared by every adopter
and the mode is a conf value.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/SKILL.template.md` · `tools/unattended/PROTOCOL.template.md` · the companion guide
template · `tools/unattended/.unattended.conf.example` · `.unattended.conf` · the rendered guides
and Skill · the kit version marker.

### Alternatives rejected

- Grading the branch tip and trusting the push boundary to grade the merge. The hook's scoped bar
  would then be the only grader of the merge, and it is scoped by a guard, which is the i28 and i29
  aborts' shape: two green changes that fail together surfacing after the run has closed.
- Re-implementing the carry predicate in the driver. Two spellings of one predicate disagree, and
  the lander is where the landing happens.
- A second full bar at the push (KF2 rules it out); the stamp in the run's git dir makes it
  unnecessary.

## 5. Production-readiness checklist

- security — no new authority: the run still lands only through the lander and the hook, and the
  mandate rules are untouched. The commit at close is the run's own record on the run's own branch.
- perf / scale — one full bar per landing, as F7 rules; the push reuses its stamp. The one extra
  cost is the carry probe, a pair of bounded `rev-list` calls.
- error / empty / loading states — an undeclared mode reads `primary`, announced; a lander that does
  not implement the mode refuses at preflight rather than at landing; a missing prepared merge,
  a foreign carry and a failed commit each refuse with a number and write nothing further.
- observability — `--status` names the mode; the close prints the bar's env, the carry verdict and
  the commit it made.
- risks — until the declared-wall unit lands, the landing bar runs under `GATE_BOUND`, and gov's
  full bar with self-tests may outlast it; the bound's own message then names the kill rather than a
  leg. The derived term `SELFTESTS_OWED_PATHS` can under-declare a kit root; the kit gate reds a
  declared path that resolves to nothing, not one that is missing.
- testing — driver and kit-gate arms over a scratch repository with a bare remote, each staged RED,
  run once at the unit's end under attribution.
- migration — adopters stay `primary` until their own deployer builds adopt the in-place lander.
- user docs — the Skill's Close and Land sections, protocol §6 and the conf example's two keys.

## 6. Acceptance criteria

- **AC1** — When a fixture branch passes its gate alone and the advertised tip has moved by a commit
  that makes the merged tree fail the same `GATE_CMD`, `--close` under `in-place` reports
  `gates-green` unmet after `--prepare`.
  Red when: the bar grades the bare branch tip, which is green.
- **AC2** — When `--close` runs under `in-place` with HEAD on an unprepared branch tip, it refuses
  with a numbered message naming `--prepare` and writes nothing.
  Red when: the missing merge is reported as an unmet item, which an override can then pass.
- **AC3** — When the fixture closes under `in-place` and then lands with `--land`, the push prints
  the hook's `scoped gate` line naming the prepared merge as the full green one commit back.
  Red when: the stamp is written outside the run's git dir, so the hook prints `FULL gate`.
  fixture: a scratch repository with a bare remote, a linked worktree and a two-leg manifest.
  permission: observed by hand in that fixture, per D12-h's method for lander breaks.
- **AC4** — When `bash tools/unattended/check-unattended.sh` grades a Skill render whose Land
  section lacks `--prepare` or `--land`, or names local main as a merge target, it reds; the shipped
  render passes, and the skill-wiring check reds a render that drifted from its template.
  Red when: the arm reads a section the render never emits, so it passes over nothing.
- **AC5** — When `--preflight` runs under `in-place` with a lander stub that exits 2 on `--carry`, it
  refuses naming `LANDER_MODE`; with a stub exiting 1 it proceeds.
  Red when: preflight trusts the declaration, and the first refusal arrives at landing time.
- **AC6** — When the lander stub's `--carry` exits 1 listing a sha, `--close` under `in-place`
  refuses, quotes that sha, and leaves the run-state file unchanged.
  Red when: the carry probe runs after the phase write, leaving a LANDING record that cannot land.
- **AC7** — When `--close` succeeds under `in-place`, `git status --porcelain` is empty, the newest
  commit's subject is `records(<slug>): close — LANDING`, and `build_commit` in
  `tools/unattended/lib-unattended.sh` returns the same commit per unit as before the close.
  Red when: the close stages without committing, which is TOOL-dUnstalledConvoy-24's defect.
- **AC8** — When the lander stub reports `unreachable`, the Skill's documented next act is a branch
  push and `--hold` under `platform-unavailable`, and no rendered sentence in the Land section
  directs a merge into local main.
  Red when: the fallback text survives from the primary path, which lands through local main.
- **AC9** — When `LANDER_MODE` is blank, `--close` and `gates-green` over the fixture produce the
  BASE driver's output and exit, including no commit and no carry probe.
  Red when: an in-place branch runs in primary mode.
- **AC10** — When the landing range touches a path under a declared `SELFTESTS_OWED_PATHS` entry, a
  fixture `GATE_CMD` that prints its environment shows `GATE_SELFTESTS=1`; when it touches none, it
  does not.
  Red when: the term is exported unconditionally or never.
- **AC11** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once at the
  unit's end, it reports no NEW failure.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: the brief lists this unit among those allowed to run the unattended suites.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `pass-order history` · `memory hygiene` · `kit version markers` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a fixture branch green alone and red once merged onto a moved tip, and a lander stub whose carry probe exits 1 · none
New arm: `tools/unattended/check-unattended.test.sh` · a Skill render missing `--prepare`, and an invalid `LANDER_MODE` · none

## 8. Open questions

- **F1 — how does the driver know the DoD owes the self-tests?** Options: always export
  `GATE_SELFTESTS=1`; never; derive it from the landing range against a declared path list. The
  first charges every records-only landing a self-test bar; the second lands kit work unverified.
  RESOLVED (agent, 2026-09-14, delegated): derive it, over `SELFTESTS_OWED_PATHS`.
- **F2 — the design's criterion that a Skill missing either flag reds check 26.** Check 26 grades
  the driver's verbs, not a lander's flags, and the unit that teaches it flags is sequenced after
  this one, so the criterion would rest on work this unit does not build.
  RESOLVED (agent, 2026-09-14, delegated): this unit adds its own kit-gate arm for the Land section
  (AC4) and does not cite check 26.
- **F3 — order against the HELD unit.** This unit consumes that unit's refusals and verb, while the
  brief's roster numbers put it first; the §3 order join refuses a consumer ordered before its
  producer. RESOLVED (agent, 2026-09-14, delegated): this unit takes `order 4`, the HELD unit
  `order 3`; no other edge in the roster involves either value.
- **F4 — the landing shape and the charter exception.** RESOLVED (owner, 2026-09-13): D12-i1 in
  place; D12-i3 keeps the charter's attended rule and puts the unattended exception's rule in the
  protocol.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Takes `order 4` rather than the roster's 3 (F3). Adds one edge
  the brief's table does not list, consumes-from unit 1, inside this spec's own group. Replaces the
  design's check-26 criterion with its own arm (F2).

## 10. Reuse audit

- The seams are the driver's `gates-green` item and its `run_bounded` wrapper, the close path's
  existing write gate, and the lander's own `--carry`, which exists so this unit asks rather than
  re-derives. The Skill's `{{LANDER}}` token is reused for all three lander calls, so
  `landed-via-lander` keeps grading the same spelling. The probe `reuse_lookup.py "land a merge onto
  the remote default branch tip and push it"` returned name-stem matches only, and its coverage line
  reads `unscanned layers: .sh`; the driver, the lander and the hook are all shell, so the lookup is
  blind here and the seams were found by reading `tools/unattended/unattended.sh` at BASE. Recall
  returned TOOL-dUnstalledConvoy-38 and TOOL-aPacedTurnstile-15 beside the aHoistedPass landing
  record. Where the design record and the source disagree: its line citations for `gates-green` sit
  within a few lines of BASE's, and its check-26 criterion names a check that grades verbs (F2).
- M12 was not reached: the owner ratified the mechanism and the lab measured it.
- Recall terms used: `push-main lander in-place landing merge remote-tip carry-set foreign-commit
  pre-push marker full-green-stamp reconcile local-main`
