# TOOL-aRuledFrontispiece-8 — check 8 stops judging a run it can no longer repair

**Status:** CLOSED · rev-2 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Check 8 of the unattended leg compares a frozen copy against a living source. The moment this build
changes what the build-index renderer emits, both tracked run-state files red permanently, and the
only verb that could refresh them refuses to run on them. Carve the equality refusal out at a
terminal phase, keep the two shape refusals at every phase, and price the escape the carve-out opens.

## 2. Scope (IN)

- **S1** — check 8's equality refusal is skipped when the run-state file's phase is a member of
  `PHASES_TERMINAL`. Membership is decided against the set `core_of` already parses out of the driver
  at `tools/unattended/check-unattended.sh:77`, never against a literal `LANDED` and never against a
  key the project layer can declare.
- **S2** — check 8's two malformed-marker refusals keep running at every phase. Marker shape is a
  property of the file on disk, not of the run that wrote it, and a terminal record with an unpaired
  marker is a defect whoever is asked to read it next.
- **S3** — a new refusal guards the carve-out against widening: `PHASES_TERMINAL` must be non-empty
  and a PROPER subset of `PHASES_CORE`. **The denominator is the CORE set, never the effective one,
  and the two are not interchangeable.** The leg composes `PHASES="$PHASES_CORE $PHASES_EXTRA"` at
  `tools/unattended/check-unattended.sh:82` from the project's `.unattended.conf`, so a proper-subset
  test against the effective vocabulary is satisfied by declaring one extra phase while
  `PHASES_TERMINAL` covers every core phase — the project-defeatable shape §4 rejects for the conf
  key, reached through the denominator instead. It looks equivalent here only because this repo
  declares `PHASES_EXTRA=""`, which is the accident that makes a vacuous arm score green. The
  refusal is ONE branch carrying both conditions, so S5's floor moves by one and not two. Check 2 is
  the other question and keeps the other denominator: it asks whether a run could ever REACH a
  terminal phase, and a run's phase is validated against the effective set at
  `check-unattended.sh:208`, so `check-unattended.sh:121` is right to read `$PHASES`.
  Neither refusal is vacuous, because `PHASES_CORE` and `PHASES_TERMINAL` are declared independently
  at `tools/unattended/unattended.sh:73` and `:74` and neither is composed from the other — the same
  falsifiability argument the comment above check 2 already makes.
- **S4** — both directions are armed in `tools/unattended/check-unattended.test.sh`: the existing
  drift fixture still HITS its message at a non-terminal phase, and MISSES it once the same fixture's
  phase is moved to a terminal one. A one-directional arm here proves the skip fires and proves
  nothing about what survives it.
- **S5** — `ARMS_FLOORS` in `.memory-tree.conf` is re-measured for this gate. The pair is
  `tools/unattended/check-unattended.sh:39:39` today and becomes `40:40` with S3's branch.
- **S6** — `KIT_UNATTENDED_VERSION` moves in both literals, `tools/unattended/unattended.sh:32` and
  `tools/unattended/check-unattended.sh:17`. The two are not at the same line and an earlier revision
  of this item said they were; both read `1.4` today. The kit is copy-installed, so two adopters
  holding the same version string must hold the same refusals.
- **S7** — the reason for the carve-out, and its residual, are written at the branch in
  `check-unattended.sh`. That file's own convention is that an honest limit belongs beside the code
  rather than in a document nobody reads at the same time, and check 13's comment block says so.

## 3. Non-goals (OUT)

- Re-rendering or hand-editing `memory/builds/aSealedCaravan/RUN.md` and
  `memory/builds/aSiftedPlaybook/RUN.md`. Check 8's own message forbids hand-editing them, and the
  repair would be owed again on every future corpus re-render.
- A repair verb, or any relaxation of `refuse_if_terminal` at `tools/unattended/unattended.sh:566`.
  That branch exists because `--close` on a LANDED record re-opened it and let `--landed` re-point the
  witness check 15 judges.
- Comparing the region against the build README at the recorded BASE instead of the worktree. See
  §4's rejected alternatives — it breaks a live run rather than a landed one.
- Adding the roster-region comparison to check 13. The driver's `check_authorization` compares the
  `<!-- roster:units -->` pair across BASE and the leg does not; unit 1 makes that asymmetry live, and
  closing it is a second mechanism with its own write set.
- Any change to checks 9 and 15, both of which already treat LANDED specially and are the two things
  a run pays to claim it.

## 4. Design

### Inventory

Five facts, each read from source at writing time. They are what makes a carve-out the resolution
rather than a re-render.

| Fact | Where | Consequence |
|---|---|---|
| check 8 reads the WORKTREE README | `check-unattended.sh:248` derives `rd` from the record's own directory; no `GIT show` on this path | the source moves whenever the corpus is re-rendered |
| both tracked run-state files are LANDED | `aSealedCaravan/RUN.md:19` and `aSiftedPlaybook/RUN.md:24` | the whole live population is terminal |
| LANDED is terminal | `unattended.sh:74` declares `PHASES_TERMINAL="LANDED ABORTED"` | neither record can be moved |
| one call site re-copies the region | `unattended.sh:846` is the sole `splice` over the `run:generated` pair | only `--preflight` refreshes a copy |
| that verb refuses a terminal run | `unattended.sh:804` calls `refuse_if_terminal` before anything is written | there is no driver repair path |

The leg exits 0 today, measured. It reds the first time a unit in this build changes what the
build-index region renders — unit 5's wrap of the status line changes it for every build in the
corpus, and units 2, 3 and 4 each add a region beside it.

### Data model

The carve-out splits check 8's three refusals by what they judge.

| Refusal | Judges | Terminal phase |
|---|---|---|
| run-state markers malformed | the file's own shape | still runs |
| build README markers malformed | the source's shape | still runs |
| region differs from the slice | the copy's freshness | skipped |

Freshness has an owner already, and it is not this leg. `dod_met` at `unattended.sh:977` evaluates
the `records-current` Definition-of-Done item by diffing the same two regions, at `--close`, which is
the last moment the copy is meant to be true. Check 8's equality half is the bar's second opinion on
that item. Held past landing it stops measuring the run's honesty and starts measuring the README's
later movement.

### Migration

None. No committed byte changes in this unit; the two stale copies become legal rather than repaired.

### Alternatives rejected

**Comparing against the README at the recorded BASE.** Stable forever for a landed run, and wrong for
a live one: a run legitimately re-runs `--preflight` after the README has moved, so the region would
drift from the BASE blob mid-run and red the honest case.

**Repairing the two files by hand or by re-render.** The message check 8 prints says to re-run the
driver rather than hand-edit, and the driver refuses. The debt also recurs: every later change to the
generated region re-opens it, for every terminal record the tree will ever hold.

**Keying the skip on a new conf declaration.** `PHASES_EXTRA` and `DOD_EXTRA` are project-layer keys;
a terminal set reachable from the project layer is a carve-out an adopter can widen to everything.
Reading `PHASES_TERMINAL` from the driver keeps the set where the refusals that enforce it live.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.sh` for the version literal only · `.memory-tree.conf` for the floors.

## 5. Production-readiness checklist

- security — the carve-out is keyed on a field the run writes, which is the objection check 9's own
  comment raises against phase-keyed carve-outs generally; see the risks line for the price.
- perf / scale — one string membership test per run-state file, in a loop that already performs one.
- a11y — N/A. No user-facing surface.
- i18n — N/A. Phase tokens are ASCII literals from a closed vocabulary.
- error / empty / loading states — an empty `PHASES_TERMINAL` fails SAFE today (no run is terminal, so
  check 8 runs on everything) and S3 makes it a named refusal rather than luck.
- observability — the skip is silent by design; a leg that prints on a clean tree has no clean tree.
  The reason is at the branch, and the drift fixture in the sibling test is what shows the split.
- risks — a run can write `phase: LANDED` to escape the equality refusal. It then owes check 15 a
  sha-shaped witness that is an ancestor of the anchor observed from the remote, and it forfeits every
  phase-writing verb through `refuse_if_terminal`. What it buys is a stale copy of a generated table
  and the freed slot at check 7. That trade is why the same carve-out was correctly refused at check
  9, where the escape would buy the base pin every mandate assertion hangs on.
- testing + left-shift gates — S4's two-directional arm plus S3's set refusal; both ride
  `tools/unattended/check-unattended.test.sh`, which is a leg rather than a file someone remembers.
- migration / rollback — single-file revert of the leg plus the floor pair; no corpus bytes move.
- user docs — none. `memory/guides/UNATTENDED-PROTOCOL.md` does not state check 8's freshness rule, so
  check 10's parity pair is untouched and adding a sentence there would create the duplication that
  check 10 exists to catch.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` runs over a tree whose build READMEs have
  been re-rendered after both run-state files reached `phase: LANDED`, it exits 0 and prints nothing.
- **AC2** — When the sibling test drives its drift fixture at a non-terminal phase, the run still
  emits `a run-state file's generated region differs from the build README slice it is a COPY of`.
- **AC3** — When that same fixture's `phase:` is moved to a member of `PHASES_TERMINAL`, the run no
  longer emits that message, and the fixture differs from the green case in `phase:` alone.
- **AC4** — When a terminal run-state file's `<!-- /run:generated -->` marker is deleted, the run
  still fails naming that file, so the carve-out did not take the shape refusals with it.
- **AC5** — When a fixture sets the driver's `PHASES_TERMINAL` to the whole of `PHASES_CORE` AND
  declares a `PHASES_EXTRA` phase in `.unattended.conf`, `bash tools/unattended/check-unattended.sh`
  fails rather than passing a tree it no longer compares. That combination is the arm that
  discriminates the two denominators: the terminal set is then a proper subset of the effective
  vocabulary and equal to the core one, so an implementation reading `$PHASES` passes a tree in which
  every reachable run is terminal. A second fixture setting `PHASES_TERMINAL=""` fails on the same
  branch.
- **AC6** — When `python tools/memory-tree/check-arms.py --check` runs at this unit's tip, it is clean
  with `ARMS_FLOORS` reading `tools/unattended/check-unattended.sh:40:40`.
- **AC7** — When `bash tools/check-kit-versions.sh` runs, it is clean, and `KIT_UNATTENDED_VERSION`
  differs from `1.4` in both `tools/unattended/unattended.sh` and `check-unattended.sh`.

## 7. Gates

`bash tools/unattended/check-unattended.sh` · `bash tools/unattended/check-unattended.test.sh` ·
`bash tools/unattended/unattended.test.sh`, because the driver's version literal moves ·
`python tools/memory-tree/check-arms.py --check` for the re-measured floor pair ·
`bash tools/check-kit-versions.sh` for the paired constant ·
`bash tools/unattended/adopt-unattended.test.sh` and `bash tools/unattended/adopt-unattended.sh
--check`, both guarded on `tools/unattended/` and therefore in scope for this diff.

## 8. Open questions

none — fork 7 at the build README resolved the two LANDED run-state files to a terminal-phase
carve-out in this check, and §4's rejected alternatives record the two options it beat rather than
re-opening them.

The one park this unit raised is now closed. **P5 at the build README — `KIT_UNATTENDED_VERSION`
moves although no gate compels it.** RESOLVED (owner, 2026-08-16): the bump stands as S6 writes it.
The owner accepted the author's reason rather than the cheapness of the reversal — the kit is
copy-installed, so without the bump two adopters can hold one version string over different
refusals, and nothing on the bar can tell them apart. `tools/check-kit-versions.sh` asserts only that
the driver's literal and the leg's literal agree with each other; it cannot assert that a given
version means one set of behaviours, which is exactly what an adopter reads it as.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.
- rev-2 · 2026-08-16 · folded the M4 spec audit. The MEDIUM row "S3's denominator and AC5's differ":
  S3 now names ONE denominator, `PHASES_CORE`, states why the effective set is project-defeatable
  through `PHASES_EXTRA` and therefore falls to §4's own rejection, and records that the two look
  equivalent here only because this repo declares no extra phases. AC5 gains the `PHASES_EXTRA` leg
  that actually discriminates the two readings. The LOW row "S6 cites the driver's line 17": the
  literal is at `tools/unattended/unattended.sh:32`, re-measured. P5 is marked RESOLVED (owner,
  2026-08-16) in §8 with the reason the owner accepted.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `unattended run-state
terminal phase carve-out generated region copy freshness landed witness anchor arms floor shrink-only`.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| read the kit's terminal phase set | `core_of PHASES_TERMINAL` at `check-unattended.sh:77` | REUSE unchanged — already parsed, already used by checks 2 and 7 |
| test membership in that set | the `case " $PHASES_TERMINAL " in` form at `check-unattended.sh:210` | REUSE THE SHAPE — same guard, one loop body later |
| judge the copy's freshness at the honest moment | `dod_met` `records-current` at `unattended.sh:977` | REUSE unchanged — it already owns this question at `--close` |
| refuse a set that has gone vacuous | the terminal-phase-outside-the-vocabulary refusal at `check-unattended.sh:119` | EXTEND — the same anti-vacuity idiom from the other side |
| pin a shrink-only branch/arm pair | `ARMS_FLOORS` in `.memory-tree.conf` | REUSE unchanged — re-measured, not re-shaped |

The map probe for "skip a gate check for a record in a terminal phase" returned the `.unattended.conf`
affordance seam and a spread of generic `check`/`record` symbols, and no seam for a phase-conditional
gate branch outside this kit. Every claim above about existing code was verified against source at
writing time, including the measurement that the leg exits 0 on the tree as it stands.
