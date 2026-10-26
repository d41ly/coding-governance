# TOOL-dRankedPlan-21 — a plan row is ratified by the recorded crossing of its build's `plan.exit`, read in any session

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 6 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-21-deviation-211.md](../build/2026-10-26-build-TOOL-dRankedPlan-21-deviation-211.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`) confirmed
**finding 3 at HIGH**. It shares item **H2**, "unit 2 judges row ratification through a session-scoped
predicate, so other sessions can reorder ratified rows", with finding 37, which
`TOOL-dRankedPlan-22` closes. `TOOL-dRankedPlan-2` S3 counts a row as ratified only while
`TOOL-dRankedPlan-9`'s `read_plan_ratification` answers a witness, and its S4 hook asks at commit
time. Under the default `plan.ratification: request` that witness exists only in the session whose id
is a line of the request's `.typed` file, and under `TOOL-dRankedPlan-10`'s fallback, the only live
path until dWellOiledMachine lands, the owner ratifies by a disposition record the predicate never
reads. In any later session every row reads unratified, and an agent commit reorders rows the owner
ratified. This unit makes "ratified" a durable fact: the `ratification=` field `TOOL-dRankedPlan-10`
S5 already writes on a build's `plan.exit` move, read back by one reader, which `check_ratified_order`
asks in place of the predicate.

## 2. Scope (IN)

- **S1** — The reader. `read_exit_ratification(repo, slug)` in `tools/loop/ratify.py` reads the
  build's transitions through `read_transitions(build, repo)` (`TOOL-dDeclaredLoop-3` S7) and returns
  `(how, harness, sha)` for the newest move whose `item` is `item.plan.exit`: `how` its `ratification`
  field and `harness` its `harness` field (`TOOL-dRankedPlan-10` S5), each `unrecorded` where the move
  carries none, and `sha` the move's commit; `None` where no such move exists. `python
  tools/loop/ratify.py <slug> --exited` prints `plan.exit — crossed · <how> · harness <h> · <sha8>` or
  `plan.exit — not crossed`, exit 0, and exits 2 on an unknown slug. Observed by AC1.
- **S2** — The owner acts. `RATIFYING_EXITS = ("witness", "intake-not-installed", "disposition")` in
  `ratify.py` names the `how` values that record the owner's act: the counted witness, and the owner's
  disposition under the fallback and outside it. `before-placement` records a gate that was not held,
  and `unrecorded` a move written before unit 10 landed; neither ratifies a row. Observed by AC2.
- **S3** — The order check re-pointed. `check_ratified_order`'s `ratified` input
  (`tools/memory-tree/gen_build_index.py`, `TOOL-dRankedPlan-2` S3) is the set of rows whose build
  `read_exit_ratification` answers with a `how` in S2's set, read once per build per run, the loop kit
  found by `backlog.resolve_kit_dir` as `read_slot_mode` finds the policy kit
  (`tools/memory-tree/gen_build_index.py:2283-2306`). The check calls `read_plan_ratification`
  nowhere. With no loop kit, no row reads ratified and the run prints one line,
  `plan order — no loop kit resolves; no row reads ratified`. This supersedes unit 2 S3's sentence "A
  row is ratified when TOOL-dRankedPlan-9's `read_plan_ratification` answers a witness for its build",
  §4 "The authority"'s "its build's plan ratification holds (I6)", and §8 F5's option (a) as written.
  Observed by AC2 and AC3.
- **S4** — The plant `drafts-cross-session` joins `gen_build_index.py --ratified-order --plant
  <case>` (`TOOL-dRankedPlan-2` S8): under `planner-drafts-owner-ratifies`, `dA` and `dB` each carry a
  committed `plan.exit` move, `ratification=disposition` and `ratification=witness`, written as session
  S1; the agent commit runs as session S2 with no `.typed` line and puts `dB` before `dA`; `dC`, whose
  move carries `ratification=before-placement`, is reordered in the same plant's second commit.
  Observed by AC3.
- **S5** — `help/plan.md`'s section "The planner and the plan's order" (`TOOL-dRankedPlan-2` S7) says
  a row is ratified once its build has crossed `plan.exit` on an owner's act, whichever session reads
  it, and names `ratify.py <slug> --exited`. Observed by AC4.

## 3. Non-goals (OUT)

- The session-scoped predicate itself: `TOOL-dRankedPlan-9`'s `read_plan_ratification` stays the
  answer at the act of crossing, which `TOOL-dRankedPlan-10` asks. Holding every other caller to the
  crossing record is `TOOL-dRankedPlan-22`'s gate.
- The pre-commit block's shape, its terminal proof and its trigger: `TOOL-dRankedPlan-2` S4, unchanged.
- A row's ratification revoked by a plan revision. A build moved back to `planning` by
  `TOOL-dRankedPlan-15` keeps its row ratified by the earlier crossing; the revision re-ratifies the
  plan's content, not the build's place.

### Edges

- **consumes-from** `TOOL-dRankedPlan-2` — `check_ratified_order` and its `--ratified-order` plants, whose `ratified` input S3 re-points; without it there is no order to hold
- **consumes-from** `TOOL-dRankedPlan-10` — S5's `ratification` and `harness` fields on the `plan.exit` move, the durable record S1 reads; without them no crossing says how it was ratified
- **hands-off** `TOOL-dRankedPlan-23` — `read_exit_ratification`, which that unit's `show` reads for the re-entering move instead of re-asking the predicate

## 4. Design

### Evidence

- `TOOL-dRankedPlan-2` S3 (spec lines 56-57) and §8 F5 pick the predicate; its S4 hook evaluates it at
  commit time.
- `TOOL-dRankedPlan-9` S2: under `request` the plan is ratified only when `--request-consent <key>`
  exits 0, which `TOOL-dPlacedRequest-19` S5 grants only when this session's id is a line of
  `requests/<key>.typed`; under the three other values its witnesses are durable records, but
  `request` is the default.
- `TOOL-dRankedPlan-10` §4 "The record" lists the four `ratification=` values and what admitted each,
  and S5 adds `ratification` and `harness` to `TRANSITION_FIELDS`, so every crossing after unit 10
  carries them.
- `read_slot_mode` (`tools/memory-tree/gen_build_index.py:2283-2306`) is the generator's existing
  route to a sibling kit through `backlog.resolve_kit_dir`, asked once per run.

### The reading

| The build's newest `plan.exit` move | Row |
|---|---|
| none | unratified |
| `ratification=witness`, `intake-not-installed` or `disposition` | ratified |
| `ratification=before-placement` | unratified: no owner act gated it |
| no `ratification` field | unratified: written before unit 10's field existed |

The answer is the same in every session and on every node that holds the commits, because it reads
commits and never the session's `.typed` lines.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_exit_ratification` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest read_exit_ratification --as py.function` answered OK |
| `RATIFYING_EXITS` | constant, `ratify.py` | none declared |
| `--exited` | flag of `ratify.py` | none |
| `drafts-cross-session` | `--ratified-order` plant | none |

### Rollout

Live at landing. A repository whose builds have crossed no `plan.exit` sees every row unratified, as
it does at base under any session other than the typing one.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2
- `tools/memory-tree/gen_build_index.py`: S3, S4
- `help/plan.md`: S5's sentences

### Alternatives rejected

- **A ratification record written once while the witness holds.** `TOOL-dRankedPlan-10` S5 already
  writes that record, on the move itself; a second record kind would be a second home for one fact.
- **Every row at HEAD ratified.** `TOOL-dRankedPlan-2` §8 F5 rejected it: it refuses the planner's own
  drafted order before the owner has seen it.
- **The predicate asked with the session forced.** No session id held by a later run is the owner's,
  so forcing one forges consent, which `TOOL-dPlacedRequest-19` S5 exists to refuse.

## 5. Production-readiness checklist

- security — narrows: an agent commit in any session is now refused for reordering rows the owner
  ratified. The fact read is a commit trailer written only by `write_transition` past
  `check_plan_exit`, so it cannot be typed into a README to fake a ratification.
- perf / scale — one `read_transitions` call per placed build per staged README commit.
- error / empty / loading states — no loop kit prints one line and reads no row ratified; an unknown
  slug exits 2.
- observability — `ratify.py <slug> --exited` prints how and where each build crossed.
- risks — a build that crossed before unit 10's fields existed reads unratified until its next
  crossing; no build has crossed at base, since the loop kit is unbuilt there.
- testing — S4's plant and the reader's own lines.
- migration — none.
- user docs — `help/plan.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant claude-adapter` has recorded the
  `plan.exit` move (`TOOL-dRankedPlan-10` AC2), `python ratify.py tFix --exited` prints
  `plan.exit — crossed · witness · harness claude-code` and the move's sha8; over a build with no move
  it prints `plan.exit — not crossed`.
  Red when: the reader answers from anything but the move's trailer, or names a crossing that did not
  happen.
- **AC2** — When a probe imports `ratify.py` and calls `read_exit_ratification` over planted moves
  carrying each of the four `ratification=` values and one carrying none, the three S2 values are in
  `RATIFYING_EXITS` and `before-placement` and `unrecorded` are not.
  Red when: a crossing no owner act gated reads as ratified.
- **AC3** — When `python3 tools/memory-tree/gen_build_index.py --ratified-order --plant
  drafts-cross-session` runs, the S2 commit putting `dB` before `dA` exits 1 naming both builds and
  `planner-drafts-owner-ratifies`, and the commit reordering `dC` exits 0; `grep -c
  "read_plan_ratification" tools/memory-tree/gen_build_index.py` prints 0.
  Red when: a later session reorders rows the owner ratified, or the check still asks the predicate.
- **AC4** — When `grep -n "\-\-exited" plan.md` runs over the help page, it finds S5's sentence in
  the section "The planner and the plan's order".
  Red when: the page still says ratification is asked of the session.

## 7. Gates

`build-index selftest` · `tier2-review self-test` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/memory-tree/gen_build_index.py · covers AC3 · the `drafts-cross-session` plant in `--selftest`, staged by a `check_ratified_order` that asks `read_plan_ratification` · none

New arm: tools/loop/ratify.py · covers AC1 AC2 · the `--exited` reader over planted `plan.exit` moves, staged by a reader that counts `before-placement` · none

## 8. Open questions

- **F1 — Does a crossing the owner gate did not hold ratify its row?** Options: (a) only `witness`,
  `intake-not-installed` and `disposition`; (b) every recorded crossing. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 1: R2.4's default is "drafted by the planner and binding once the owner
  ratifies it" (`TOOL-dRankedPlan-2` §1), and a `before-placement` crossing records no owner act.
  widens: none · relaxes: none
- **F2 — What does the check read with no loop kit?** Options: (a) no row ratified, one printed line;
  (b) exit 2, refusing every README commit. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3:
  without the loop kit no `plan.exit` move can exist, so (a) states the fact, while (b) refuses an
  adopter every README commit for a kit it never installed. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's finding 3 (HIGH, item H2,
  shared with finding 37), repairing `TOOL-dRankedPlan-2`.

## 10. Reuse audit

The seams extended are `TOOL-dRankedPlan-10` S5's trailer fields, read through dDeclaredLoop's one
transition reader `read_transitions` (`TOOL-dDeclaredLoop-3` S7), and the generator's sibling-kit
route of `read_slot_mode` (`tools/memory-tree/gen_build_index.py:2283-2306`). `python
tools/codebase-map/reuse_lookup.py "read how a gate was passed from the transition record trailer
field"` ranked name stems only (`read`, `read_text`, `records`, `field`); none reads a transition, and
the loop kit is unbuilt at base 0689e7fa, so no existing seam fits the reader beyond the transition
reader it calls. The recall query returned `TOOL-dPlacedRequest-19` S5's consent predicate and the
audit's H2 item, which agree with the specs read.

Recall terms used: `python tools/memory-recall/query.py "how is a session-scoped consent predicate kept out of a commit-time guard" --terms "request-consent typed relayed session predicate commit-time guard pre-commit ratified order cross-session plant"`
