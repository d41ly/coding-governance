# TOOL-cSettledDocket-6 — a standing fixture for the frozen-versus-live class

**Status:** OPEN · rev-1 · 2026-08-16 · node c · Tier-1 · base 1da67d9c · streams tooling

## 1. Goal

cBriefedPilot's closing review found the same root three times: **a predicate joining a FROZEN
historical value to a LIVE present one**. Each instance was found by a human-shaped read, each was
filed separately, and each fix was local.

1. Leg check 8 compared a terminal run's frozen generated region to a build README that keeps moving,
   while check 26 refused the only verb that could re-splice it. A permanent red wedge.
2. Check 17 graded a frozen waiver's handle against today's `DIRECTIVES` set — same wedge, one check
   to the left, found only because the first had just been fixed.
3. `closing-review-recorded` joined a pinned BASE to a needle width the repo does not produce.

Nothing in the suite looks for this shape. This unit adds the fixture that would have caught all
three: **move the world around a terminal record, then assert silence.**

## 2. Scope (IN)

- **S1** — one fixture in `tools/unattended/check-unattended.test.sh` that takes a conforming tree
  with a TERMINAL run-state record and then moves everything around it that a later build legitimately
  moves: the build README's generated region, its roster, the directive set, the phase vocabulary,
  and the tracked review records.
- **S2** — after each move, the leg must be SILENT. A terminal record is a snapshot of what its run
  saw; nothing a later build does to the tree may red it, because no verb can rewrite it.
- **S3** — a paired LIVE control for every move: the same mutation over a non-terminal record must
  still red where it did before. Without the pair, S2 is satisfiable by turning the checks off.
- **S4** — each move goes through `mutate`, so a mutation that silently matches nothing fails rather
  than making the fixture pass by changing no bytes.
- **S5** — the fixture is written so a NEW check that joins a frozen value to a live one reds here
  without anyone adding an arm. That is what makes it standing rather than three more arms.

## 3. Non-goals (OUT)

- **Fixing a fourth instance.** All three known ones are fixed. This unit is the net that catches the
  next.
- **A general property-based harness.** The moves are enumerated from what a build actually does to a
  tree — re-render the index, close a unit, add a directive, add a review. A generator would produce
  states no build produces and refusals nobody should act on.
- **The driver's own terminal guards.** `refuse_if_terminal` covers all five verbs and has its own
  arms. This unit grades the LEG, which has no such single guard and instead exempts per check.
- **Extending the fixture to `check-memory-hygiene.sh`.** The same class may live there — a terminal
  spec graded against a moving corpus — but measuring that is its own row.

## 4. Design

### Why silence is the assertion

Every one of the three instances presented as a refusal nobody could clear. The diagnostic property
is not "the check fires" but "the check fires on something no verb can fix." A terminal record is
exactly that: `refuse_if_terminal` refuses `--phase`, `--landed`, `--abort`, `--preflight` and
`--close` on it, so once a run ends its record is immutable through the kit. Any leg check that can
red on a terminal record is therefore a wedge by construction, whatever it is checking.

That gives the fixture a rule a future check must satisfy rather than a list of past bugs: **if a
tree with a terminal record can be made red by changing something outside that record, the check is
wrong.**

### Why the live control is not optional

S2 alone is satisfiable by exempting every check from terminal records, which would delete the leg's
value for finished runs — and unit 36 already got this half-wrong once, scoping check 8's exemption
so wide that it swallowed the two malformed-marker refusals and left the repo's only marker validator
guarding zero files. The pair is what distinguishes "correctly exempt" from "switched off", and that
distinction has already been got wrong in this codebase inside one unit's lifetime.

### The moves, enumerated from real builds

| Move | Why a real build makes it | Frozen thing it could collide with |
|---|---|---|
| re-render the build index | every unit close does it | the run-state file's copied generated region |
| add a roster row | scope changes on owner instruction | `check_authorization`'s slice compare |
| add a directive to the core set | a later kit version | check 17's handle-membership test |
| add a phase to the vocabulary | a later kit version | check 4's membership test |
| add a tracked review record | the closing review | `closing-review-recorded`'s base join |

Each row is one `mutate` plus a silence assertion plus its live twin.

### Files touched

`tools/unattended/check-unattended.test.sh` only, plus its `FLOOR_ASSERTIONS`.

## 5. Production-readiness checklist

No new dependency and no new leg — it extends a suite already on the bar. It depends on unit 3 only
in ordering: unit 3 moves a `next` in a different gate and both touch `ARMS_FLOORS`, so building them
in sequence avoids two units racing one constant.

## 6. Acceptance criteria

- **AC1** — with a TERMINAL record, each of the five moves leaves `bash tools/unattended/check-unattended.sh`
  silent and exiting 0.
- **AC2** — with a LIVE record, each move that used to red still reds, naming the same `UNATTENDED check <n> FAILED` it named before.
- **AC3** — every move goes through `mutate`, so a fixture edit changing no bytes fails the suite.
- **AC4** — re-introducing unit 36's over-wide exemption in `tools/unattended/check-unattended.sh` —
  skipping the whole check-8 block rather than its equality — makes AC2's malformed-marker control
  FAIL, proving the pair detects an exemption that went too far.
- **AC5** — the suite's `FLOOR_ASSERTIONS` is re-pinned to the new total in the same commit.

## 7. Gates

`bash tools/unattended/check-unattended.test.sh` · `bash tools/unattended/check-unattended.sh` ·
`python tools/memory-tree/check-arms.py` · `bash tools/run-gates.sh`.

## 8. Open questions

none — the design pass had one real decision, whether to enumerate the moves or generate them, and
§3 takes it against producing states no build produces. AC4 is the arm that keeps the fixture honest
about the difference between an exemption and a switch-off.

## 9. Revision log

- rev-1 · 2026-08-16 · authored from `TOOL-cBriefedPilot-38`, the class the M8 review named after
  finding three separate instances of it in one diff.

## 10. Reuse audit

`mutate` (`TOOL-cBriefedPilot-23`) is reused for every move — this is the fixture it was built for,
and S4 makes it mandatory rather than optional. The suite's existing `reset_tree`, `run`, `hit`,
`miss` and `same` are reused unchanged; the `pedit` two-file helper from unit 22 is reused for the
protocol moves so both copies stay in step and the parity leg does not fire instead of the check
under test. `PHASES_TERMINAL` is read from the driver through the leg's existing `core_of`, not
re-declared, so the fixture's idea of "terminal" cannot drift from the kit's. No new helper is
introduced: if this fixture needed one, it would be evidence the moves are not the ones real builds
make.
