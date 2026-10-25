# TOOL-dWitnessedBar-91 — unit 90 AC2 counts the quoted `sha)` arm, not every `rec_sha="`, so a correct build passes and the reader's resets stay

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 48 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-92 |
| [2026-10-25-build-TOOL-dWitnessedBar-91-round13-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-91-round13-fix-return.md) | research | TOOL-dWitnessedBar-92 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-91-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-91-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-91-round13-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-91-round13-fix-brief.md) | research | TOOL-dWitnessedBar-92 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of unit 90
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-90-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**. Id 6 is the same defect found by the
grounding lens at MEDIUM, item M1. The two items share one fix. This unit makes that fix, and
`TOOL-dWitnessedBar-92` S1 takes id 6 and adds the baseline observation its fix names.

`TOOL-dWitnessedBar-90` AC2 requires `grep -c 'rec_sha="'` over each of its two scratch clones'
`.githooks/pre-push` to print 1. The hook already holds two `rec_sha=""` initialisers, and
`TOOL-dWitnessedBar-69` S1 keeps them. Each clone adds one quoted `sha)` arm, so a correct build
prints 3 and reds AC2. A builder chasing the 1 would delete the resets, which ships a reader that
keeps stale values for an unreadable record.

This unit replaces that count with one anchored on the `sha)` arm, adds the check that the arm is the
reader's only `sha)` arm, and holds the resets at the count the unedited built hook carries. It
repairs `TOOL-dWitnessedBar-90` and builds one step after it (order 48).

## 2. Scope (IN)

- **S1** — 90 AC2's count, anchored on the arm. In each of the two scratch clones 90 AC2 makes, the
  main loop observes three counts over the clone's `.githooks/pre-push`, in place of 90 AC2's
  `grep -c 'rec_sha="'` clause, which this unit supersedes:
  - `grep -c 'sha)[[:space:]]*rec_sha="'` prints 1, so the clone carries exactly one quoted arm;
  - `awk '/^read_green_file\(\)/,/^}/'` piped to `grep -o 'sha)' | wc -l` prints 1, so the edited arm
    is the reader's only `sha)` arm;
  - `grep -c 'rec_sha=""'` prints the same number over the clone as over the unedited built hook, so
    both initialisers still stand when the other two counts pass.

  90 AC2's other clauses stand: no line holding `variant changed 0 lines` and none holding `visited`.
  Observed by AC1.
- **S2** — Unit 90 answered. Unit 90's acceptance ledger records S1's three counts for each clone as a
  note under its `- AC2` answer. The note is a continuation line, two spaces in, never a line opening
  `- AC2`. It opens with the label `TOOL-dWitnessedBar-91 S2` and carries the backticked
  `sha)[[:space:]]*rec_sha="` token on that one physical line, with prose wrapped after it.
  Observed by AC2.

## 3. Non-goals (OUT)

- The baseline that the anchored count prints 0 over the unedited built hook, whose arm unit 69
  spells unquoted. That is id 6's half of the shared fix, and `TOOL-dWitnessedBar-92` S1 takes it.
- Rewording the spec text of unit 90. Its AC2 is answered in its ledger by name, as
  `TOOL-dWitnessedBar-90` §3 does for units 87 and 89.
- The two `rec_sha=""` initialisers themselves. Unit 69 owns `read_green_file`, and no spec of this
  build touches the top-level reset.
- The report's left-shift text, a spec-lint rule re-deriving every exact `grep -c` count against the
  current tree at spec time. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-90` — AC2's two quoted-arm clones and its `rec_sha="` count, which S1 supersedes with the anchored count and S2 answers in that unit's ledger (id 1)
- **consumes-from** `TOOL-dWitnessedBar-69` — S1's `read_green_file`, whose `sha)` arm the clones quote and whose two resets S1 holds at the unedited count (id 1)
- **hands-off** `TOOL-dWitnessedBar-92` — the anchored count's baseline over the unedited built hook, id 6 of the same audit, the medium-graded half of the shared fix

## 4. Design

### Evidence

- `.githooks/pre-push`, read on 2026-10-25: `:1350` is the top-level
  `rec_sha=""; rec_fp=""; ...` initialiser, and `:1352` is the same reset inside `read_green_file`,
  which opens at `:1351`. `grep -c 'rec_sha="'` prints 2 and `grep -c 'sha)[[:space:]]*rec_sha="'`
  prints 0. PINNED on 2026-10-25; S1 reads both counts against the built hook at the close.
- `grep -n 'sha)'` over the whole hook prints `:1427`, `sha) bg_sha=$v ;;`, which is outside
  `read_green_file`. So the only-arm check cuts the reader first, as `TOOL-dWitnessedBar-88` AC10
  cuts it with `awk '/^read_green_file\(\)/,/^}/'`.
- `TOOL-dWitnessedBar-69` S1 (spec-69 lines 38-49) replaces the reader's seven `$(awk ...)` reads with
  one loop and a `case` on the key, and says "An unreadable file leaves all seven empty, as today".
  Spec-69 line 74 spells the built arm `sha) rec_sha=$_rg_v`, unquoted. The reader's seven keys, read
  from its awk reads at `:1354` to `:1368`, are `sha`, `fingerprint`, `manifest_blob`, `manifest`,
  `selftests`, `reused` and `reused_cache`, so only one of them closes as `sha)`. Over today's hook
  the cut piped to `grep -o 'sha)' | wc -l` prints 0.
- `memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md` records that a ledger grep reads
  one physical line.

### Inventory

Minted: nothing in code. The ledger note of S2, labelled `TOOL-dWitnessedBar-91 S2`. No function,
constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

At the close, after every unit is terminal. The unit takes order 48, one above unit 90's 47, beside
`TOOL-dWitnessedBar-92`. Its counts run in 90 AC2's clones, and its note is written at the close.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/`

### Alternatives rejected

- **Cut `read_green_file` and count `sha) *rec_sha="` inside the cut, the report's second way.** It
  drops the top-level reset from the count but leaves the reader's own reset in it, so it still
  prints 2 on a correct clone. The anchored arm count needs no cut.
- **Expect 3 in place of 1.** A pinned 3 counts the resets with the arm, so a clone that deletes one
  reset and doubles the arm passes. S1 counts the arm and the resets apart.

## 5. Production-readiness checklist

- security — no new write path. The scratch clones are 90 AC2's, under `%TEMP%`.
- perf / scale — three greps per clone, once, at the close.
- error / empty / loading states — an empty cut of `read_green_file` prints 0 for the only-arm count,
  which reds.
- observability — the note quotes each count with its clone, so a reader can rerun it.
- risks — a builder who quotes the arm on a line apart from its `sha)` label passes the only-arm count
  and fails the anchored one; unit 69's arm keeps the label and the assignment on one line
  (spec-69 line 74).
- testing — AC1 by scratch clone and AC2 by ledger, both at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In each of 90 AC2's two scratch clones, one spelling the `sha)` arm `rec_sha="$_rg_v"`
  and one `rec_sha="${_rg_v}"`, `grep -c 'sha)[[:space:]]*rec_sha="' .githooks/pre-push` prints 1,
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push | grep -o 'sha)' | wc -l` prints 1, and
  `grep -c 'rec_sha=""' .githooks/pre-push` prints the number it prints over the unedited built hook.
  Red when: a correct clone reds because the count includes the resets, or a clone passes with a
  reset deleted or a second `sha)` arm in the reader.
  fixture: 90 AC2's scratch clones under `%TEMP%/<short-name>`.
  figure: the reset count is DERIVED at observation time from the unedited built hook; it reads 2 today.
  permission: the clones are the main loop's, at the close.
- **AC2** — When
  `awk '/^\*\*Evidences:\*\*|^#/{o=""} /^- /{o=$0} /TOOL-dWitnessedBar-91 S2([^0-9]|$)/{print o}' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-90*acceptance-ledger*`
  runs at the close, it prints exactly one line, and that line opens `- AC2 `. The note line itself
  holds `sha)[[:space:]]*rec_sha="`.
  Red when: unit 90 AC2 is recorded against the unanchored count, or the note opens its own `- AC2`
  line and doubles 90's answer.
  permission: the ledger is written at the close.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` are owed for the ledgers under `memory/`. AC1 reads 90 AC2's
clones at the close; this unit adds no arm and moves none, so it declares no `New arm:` line, and
`TOOL-dWitnessedBar-88` S6's derivation still names unit 90 the floor's owner.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 90 is itself
  derived and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-90` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which unit takes id 6, the medium-graded item of the same defect?** Options: (a) this unit,
  so the shared fix lands once; (b) the minors batch, as M4 places every MEDIUM. The task's disposal
  rule puts every MEDIUM in the batch, so (a) fails it; veto 1 discards it. Under (b) this unit makes
  the fix and the batch adds id 6's baseline half, so nothing is fixed twice. RESOLVED (agent,
  2026-10-25, delegated): (b), rung 3, the one survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of unit 90, id 1 (HIGH,
  item H1; id 6 is its medium-graded item M1, batched into TOOL-dWitnessedBar-92).

## 10. Reuse audit

The seam is 90 AC2's own clones and the reader cut `TOOL-dWitnessedBar-88` AC10 already uses,
`awk '/^read_green_file\(\)/,/^}/'`; the ledger note uses the acceptance ledger of
`memory/HYGIENE.md` "Acceptance ledger".
`python tools/codebase-map/reuse_lookup.py "count one case arm assignment in a shell hook without counting the variable initialisers"`
ranked `counts`, `arm`, `armed` and `run_arms`, none a counter of one case arm apart from a variable's
resets, so no existing seam fits beyond the cut and the ledger named above.

Recall terms used: `python tools/memory-recall/query.py "how does a grep count criterion pass on a correct build when the file already holds the token" --terms "grep count criterion baseline initialiser rec_sha case arm anchored selector clone pre-push quoted"`
