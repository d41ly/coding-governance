# KICK-dKeptSession-57 — the batch's pass-bound items observed at a pass that runs after them, never at an earlier unit's commit

**Status:** CLOSED · rev-4 · 2026-11-23 · node a · Tier-2 · base 71b22e42 · streams kickoff · order 32 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-57-deviation-571.md](../build/2026-10-26-build-KICK-dKeptSession-57-deviation-571.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-57-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-57-promoted-fix-return.md) | research | KICK-dKeptSession-62 |
| [2026-11-21-build-KICK-dKeptSession-57-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-57-1-acceptance-ledger.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-57-1-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-57-1-spec-writer.md) | journal | KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-57-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-57-promoted-fix-brief.md) | research | KICK-dKeptSession-62 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief.md) | research | KICK-dKeptSession-30 KICK-dKeptSession-32 KICK-dKeptSession-35 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-56 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-57-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-57-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-57-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-57-precheck-brief.md) | research | KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-22-prompt-KICK-dKeptSession-57-1-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-57-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-57-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-57-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-57-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-57-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-57-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-57-spec-audit.md) | spec-audit | KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's twelve round-2 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`)
confirmed finding **id 1 at HIGH**, report item **H1**, which no other id shares.

`KICK-dKeptSession-56` takes order 31, past every unit it amends, yet some of its items bind passes
that run long before it. At its rev-6, two still do. S25 to S27 and S44 say "each unit's pass names
the legs", and AC22 reds when "a guarded leg is missing from a pass's record". S29 makes
`.governance/policy.json` a write of unit 40's pass (order 4) and unit 41's pass (order 29), and AC24
runs `mirror --check` "at each of unit 40's and unit 41's pass commits". Unit 40's pass left that
mirror stale, so AC24 stays red at its commit for good. A builder of 56 cannot change those commits.
This unit re-binds each item to a pass that runs after the work it observes: this unit's own. A third
item, S13 with AC11, now reads unit 5's build commit by its pinned sha, which any later pass can run,
so this unit observes it and supersedes nothing there. It builds one step after unit 56 (order 32).

## 2. Scope (IN)

- **S1** — id 1. The factory row and the tuple member. Met by `KICK-dKeptSession-5`: its build commit
  `6178a65e` writes both the `mailbox-message` row of `tools/memory-tree/build_records.py#KINDS` and
  the member of `tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS` (PINNED 2026-11-23, `git show
  --stat 6178a65e`). `KICK-dKeptSession-56` rev-6 S13 and AC11 read that commit, so no text of theirs
  is superseded. This unit's pass observes both together at its own commit, with `import
  build_records` exiting 0. Observed by AC1.
- **S2** — id 1. The committed mirror. `KICK-dKeptSession-56` S29's "a write of units 40 and 41" and
  the "at each of unit 40's and unit 41's pass commits" of its AC24 are superseded by name. After its
  other commits, this unit's pass runs `python tools/policy/policy.py mirror --write` once. When the
  bytes of `.governance/policy.json` moved, it commits that file alone in a commit of its own, the shape
  `tools/policy/guard.py#check_mirror_render` admits. The mirror is then fresh over every input units
  40 and 41 changed. Observed by AC2.
- **S3** — id 1. The owed legs. `KICK-dKeptSession-56` S25 to S27 and S44's "each unit's pass names
  the legs" and the "at its pass" of AC22 are superseded by name. This unit's pass runs `python
  tools/check-spec-tokens.py --legs-for` over the paths
  `tools/check-spec-tokens.py#extract_files_touched` reads from each named unit's `### Files touched
  (estimate)`. It records one OBSERVED line per unit, each naming its unit, in this unit's own
  acceptance ledger,
  `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-57-1-acceptance-ledger.md`.
  A line names every leg the query prints on a row not marked `broad`, the legs the guards join owes.
  The lines for units 35, 36 and 42 also name `loop transition record`, the leg that runs
  `tools/loop/loop_transition.py check` at the close; unit 44's line also names `loop position
  fixtures`, as 56 S27 owes. Neither leg carries a `guard` in `tools/gate-legs.json`, so the query
  never names them and counts them among the unguarded legs. Every named unit builds before this one
  and is CLOSED when it builds, so no named unit's ledger is written (F1). Observed by AC3.
- **S4** — id 1. The sibling texts answered. This unit's own acceptance ledger answers
  `KICK-dKeptSession-56` AC11, AC22 and AC24 by this unit's AC1 to AC3, each by name, quoting AC11's
  "the factory row lands without the tuple member", AC22's "a guarded leg is missing from a pass's
  record" and AC24's "at each of unit 40's and unit 41's pass commits". Unit 56 builds at order 31
  and is CLOSED when this unit builds, so neither its spec nor its ledger is written (F1). Observed by
  AC4.

## 3. Non-goals (OUT)

- Renumbering any order. Unit 5's build commit landed the row and the member together, so S1 needs no
  two units to share a pass.
- Rewriting unit 40's pass commit or its ledger's owed mirror answer. Unit 40 is CLOSED, and S2's
  render at this pass is what makes the mirror fresh.
- The six units the batch's S25 and S27 omit: id 2, `KICK-dKeptSession-62`.
- The report's left-shift hygiene arm, that a criterion naming an earlier unit's pass commit reds. It
  is a separate gate, so a separate unit by M2, and no clause of this build names it.

### Edges

- **consumes-from** `KICK-dKeptSession-56` — S13, S25 to S27, S29 and S44 with AC11, AC22 and AC24, which this unit re-binds to its own pass (id 1)
- **hands-off** `KICK-dKeptSession-62` — S3's ledger rule, which the batch's S1 runs for units 49, 50, 52 to 55 (id 2)
- **hands-off** `KICK-dKeptSession-63` — S3's ledger rule, whose population the batch's S9 derives and whose non-success outputs its S17 records (ids 13, 27)

## 4. Design

### Evidence

- spec-56 rev-6: §1 "takes the order past every unit of the build (order 31)"; S13 "Met: unit 5's
  build commit writes its factory row and unit 39's tuple member together"; AC11 "`git show --stat
  6178a65e`, unit 5's build commit"; S25 "each unit's pass names the legs"; S27 "no `loop selftest`
  leg exists"; S29 "a write of units 40 and 41"; AC24 "at each of unit 40's and unit 41's pass
  commits".
- `git show --stat 6178a65e` lists `tools/memory-tree/build_records.py` and
  `tools/memory-tree/tree_lib.py` (PINNED 2026-11-23). Spec-39 rev-6 §3 names both as unit 5's,
  landed.
- Unit 40's acceptance ledger answers its AC4 as owed: `mirror --check` exited 1 naming
  `legacy_blobs`, and "this pass does not write" the mirror. Spec-41 rev-5 S5 renders the mirror in
  its own pass, after its catalogue commit.
- `.governance/policy.json` was last re-rendered by `8b464fb8`, a fix of `KICK-dKeptSession-10`, and
  `python tools/policy/policy.py mirror --check` printed `policy: mirror fresh` at `71b22e42`
  (PINNED 2026-11-23).
- `tools/gate-legs.json` carries no `loop selftest` leg, and `tools/loop/selftest.py` is absent; the
  `loop transition record` and `loop position fixtures` rows carry no `guard` (PINNED 2026-11-23).
- `tools/check-spec-tokens.py#print_legs_for` prints, per path, each tripped leg, marking a broad
  guard's row `broad`, and refuses with exit 2 when no path given is tracked at HEAD.
- The README's generated build order puts unit 40 at step 4, unit 5 at 16, unit 41 at 29, unit 56 at
  31 and this unit at 32; every unit of 30 and 32 to 44 sits below 32 (DERIVED, the specs' `order`
  fields).

### The re-binding

| 56's text | Bound to | Re-bound to |
|---|---|---|
| S13, AC11 | unit 5's build commit, by its pinned sha | observed again at this pass, AC1 |
| S29, AC24 | units 40 and 41's pass commits | this unit's `mirror --write`, AC2 |
| S25 to S27, S44, AC22 | each named unit's pass | one ledger line per unit at this pass, AC3 |

Unit 56's own ledger also carries a line per named unit, derived at its pass. This unit's lines are
the query re-run at this pass over the same Files touched, never a copy of 56's, so the query stays
the one source of both.

### Inventory

No identifier is minted.

### Migration

None: the mirror is re-rendered by the kit's own verb, and this unit's ledger carries the lines.

### Shipped texts and the ceiling

No product code moves, so no shipped text this unit's clauses would make false was found. The guide
step at `help/policy.md`, "first the policy or catalogue change, then `python
tools/policy/policy.py mirror --write`", stays true because S2 follows it. The `[[generated]]` row
of `tools/policy/kit.toml` and the mirror section of `tools/policy/README.md` stay true, since the
render is that row's own verb. No catalogue summary or help anchor is edited. The unit does not edit
`tools/unattended/unattended.sh`, so it adds no `fail`, `exit 1` or `status=1` site, and it adds no
suite plant or arm, so no floor or budget row moves.

### Files touched (estimate)

- `.governance/policy.json`: S2, when its render moved
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-57-1-acceptance-ledger.md`:
  S3's lines and S4's answers beside the criteria observed

### Alternatives rejected

- **Moving S29 and the ledger duties into units 40 and 41's specs.** Unit 40 is CLOSED with its
  mirror answer owed, and a closed unit's spec and records are never written by a later unit.
- **Dropping AC22 and AC24.** The duties they observe stay owed, and nothing would observe them.

## 5. Production-readiness checklist

- security — none: one render by the kit's own verb and ledger lines.
- perf / scale — one `mirror --write` and one `--legs-for` per named unit, once.
- error / empty / loading states — a named unit whose paths are none of them tracked makes the query
  refuse with exit 2; its ledger line records that refusal instead of a leg list.
- observability — each ledger line names the legs it read.
- risks — a pass that moves a mirror input without rendering leaves the mirror stale until the next
  render; `policy-mirror.js` reads it STALE and its reads fall through to the shim
  (`KICK-dKeptSession-49` §5), never to a wrong value.
- testing — the criteria of §6; no arm is added.
- migration — none.
- user docs — none: no owner-facing behaviour changes.

## 6. Acceptance criteria

Each criterion reads this unit's own pass commit, `<this pass>`.

- **AC1** — When `git grep -n "mailbox-message" <this pass> -- tools/memory-tree/tree_lib.py
  tools/memory-tree/build_records.py` runs, it prints the tuple member and the factory row, and
  `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import build_records"` exits 0 at
  that commit.
  Red when: either half is absent, or the import refuses.
- **AC2** — When `python tools/policy/policy.py mirror --check` runs at `<this pass>`, it exits 0 and
  prints `policy: mirror fresh`; any commit of this pass touching `.governance/policy.json` touches
  no other file.
  Red when: the committed mirror is stale against the inputs units 40 and 41 changed, or it was
  committed beside another file.
- **AC3** — When this unit's ledger is read at `<this pass>`, it carries one OBSERVED line for each
  of units 30 and 32 to 44. Each names every leg `check-spec-tokens.py --legs-for` prints on a row not
  marked `broad` over that unit's Files touched at `<this pass>`. The lines for units 35, 36 and 42
  name `loop transition record`, and unit 44's names `loop position fixtures`.
  Red when: a named unit has no line, or a printed leg is missing from its line.
  figure: the legs are DERIVED by the query at observation time.
- **AC4** — `tr -s ' \r\n' ' '` over this unit's acceptance ledger piped into `grep -c` prints `1`
  for each of "the factory row lands without the tuple member", "a guarded leg is missing from a
  pass's record" and "at each of unit 40's and unit 41's pass commits"; and `git diff --name-only
  <pass base> HEAD -- memory/builds/dKeptSession/build/` lists no acceptance ledger but this unit's
  own.
  Red when: an answer or a line lands in unit 56's ledger or a named unit's, or this unit's ledger
  leaves one of unit 56's criteria unquoted.

## 7. Gates

`build-index selftest` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The bar's preflight runs the policy kit's `[[generated]]` check, `mirror --check`, before its first
leg (`tools/policy/kit.toml`).

## 8. Open questions

- **F1 — Where are S3's lines and S4's answers recorded?** Units 30 and 32 to 44 and unit 56 build
  before this unit, so each is CLOSED when it builds, and their ledgers are in neither this unit's
  Files touched nor its write set. (a) Each named unit's acceptance ledger, a record of a closed unit
  written by a later one; (b) this unit's own acceptance ledger, one line per named unit and unit
  56's criteria quoted. Recommendation (b). RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a
  CLOSED unit's records are never written by a later unit, as KICK-dKeptSession-49 rev-6 ruled.
  Rejected: (a), writing the other unit's ledger. The main loop's ruling, in
  `2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-2 promotions' audit, H1 (id 1).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared
- rev-3 · 2026-11-21 · §1 · S3 · S4 · §4 · AC3 · AC4 · §8 · S3's lines and S4's answers move from
  the named units' and unit 56's ledgers to this unit's own acceptance ledger, which joins Files
  touched, F1 resolved (b) and AC4 observing the quoted criteria, under the brief
  `2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief`; the class KICK-dKeptSession-49 rev-6
  first resolved. §1 re-reads unit 56 at rev-4, whose S25 to S27 and S44 record in its own ledger.
  The ledger's path trips the two `recall floor` legs, already on §7's leg line.
- rev-4 · 2026-11-23 · §1 · S1 to S3 · §3 · §4 · §5 · AC2 · AC3 · §7 · §10 · re-grounded on
  `71b22e42` by `2026-11-22-prompt-KICK-dKeptSession-57-reground-brief`, unit 56 read at rev-6: S1
  reduced to its observation, unit 5's build commit `6178a65e` having landed the row and the member
  and 56's AC11 reading it; S2 grounded on unit 40's owed mirror and unit 41 rev-5 S5's render, the
  mirror committed alone; S3's absent `loop selftest` replaced by `loop transition record`, with
  unit 44's `loop position fixtures` and the broad rows excluded; §4 gains the shipped texts and the
  ceiling, none moved.

## 10. Reuse audit

The seams reused are `policy.py mirror --write` and `--check`, dGroundRules' one mirror renderer, and
`check-spec-tokens.py --legs-for` (`tools/check-spec-tokens.py#print_legs_for`) over the paths
`tools/check-spec-tokens.py#extract_files_touched` reads, the derivation 56's S25 already names;
nothing is minted. `python tools/codebase-map/reuse_lookup.py "re-bind a pass commit criterion to a
later pass"` and `"legs a spec's files touched trip"` returned name-stem candidates only, so no
existing seam in the tree fits beyond those verbs.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted unit placed when it
repairs an earlier unit's pass" --terms "promoted order pass commit ledger superseded batch minors
hands-off consumes-from parity mirror"`
