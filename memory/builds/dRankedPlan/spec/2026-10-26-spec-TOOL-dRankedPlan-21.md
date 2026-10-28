# TOOL-dRankedPlan-21 — a plan row is ratified by the recorded crossing of its build's `plan.exit`, read in any session

**Status:** DEFERRED · rev-3 · 2026-10-28 · node a · Tier-2 · base 0689e7fa · streams tooling · order 6 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-21-deviation-211.md](../build/2026-10-26-build-TOOL-dRankedPlan-21-deviation-211.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-28-build-TOOL-dRankedPlan-21-deviation-212.md](../build/2026-10-28-build-TOOL-dRankedPlan-21-deviation-212.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 TOOL-dRankedPlan-48 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-57 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-64 TOOL-dRankedPlan-67 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 TOOL-dRankedPlan-81 |
| [2026-10-28-prompt-TOOL-dRankedPlan-1-parents-reground.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-reground.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-9 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-22 TOOL-dRankedPlan-24 TOOL-dRankedPlan-29 TOOL-dRankedPlan-31 TOOL-dRankedPlan-37 TOOL-dRankedPlan-45 |
| [2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) | spec-audit | TOOL-dRankedPlan-27 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-22 TOOL-dRankedPlan-20 TOOL-dRankedPlan-19 TOOL-dRankedPlan-28 TOOL-dRankedPlan-23 TOOL-dRankedPlan-29 |

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
  tools/loop/ratify.py <slug> --exited` prints `plan.exit — crossed · <how> · harness <h> · <sha8> ·
  <verdict>`, the verdict `ratifying` when `how` is in S2's `RATIFYING_EXITS` and `not ratifying`
  otherwise (§8 F3), or `plan.exit — not crossed`, exit 0, and exits 2 on an unknown slug. Observed by
  AC1.
- **S2** — The owner acts. `RATIFYING_EXITS = ("witness", "intake-not-installed", "disposition")` in
  `ratify.py` names the `how` values that record the owner's act: the counted witness, and the owner's
  disposition under the fallback and outside it. `before-placement` records a gate that was not held,
  and `unrecorded` a move written before unit 10 landed; neither ratifies a row. Observed by AC2.
- **S3** — The order check re-pointed. `check_ratified_order`'s `ratified` input
  (`tools/memory-tree/gen_build_index.py`, `TOOL-dRankedPlan-2` S3) is the set of rows whose build
  S1's verb answers `ratifying`, read once per build per run by running `<sys.executable> <loop
  kit>/ratify.py <slug> --exited` as a subprocess bounded by a timeout, the loop kit's directory found
  by `backlog.resolve_kit_dir("loop", "ratify.py", …)`, which builds a path and loads nothing. A kit
  imports no sibling kit (PLAY-dOrderedCharter-7 §4), so the generator neither imports `ratify.py` nor
  holds a copy of `RATIFYING_EXITS` (§8 F3). Exit 2, an unknown slug, reads as not crossed; any other
  non-zero exit, a timeout or a line of neither form exits the check 2 naming the build and the cause,
  so a broken reader never reads a row unratified. The check calls `read_plan_ratification`
  nowhere. With no loop kit, no row reads ratified and the run prints one line,
  `plan order — no loop kit resolves; no row reads ratified`. This supersedes unit 2 S3's sentence "A
  row is ratified when TOOL-dRankedPlan-9's `read_plan_ratification` answers a witness for its build",
  §4 "The authority"'s "its build's plan ratification holds (I6)", and §8 F5's option (a) as written.
  Observed by AC2 and AC3.
- **S4** — The plant `drafts-cross-session` joins `gen_build_index.py --ratified-order --plant
  <case>` (`TOOL-dRankedPlan-2` S8): under `planner-drafts-owner-ratifies`, `dA` and `dB` each carry a
  committed `plan.exit` move, `ratification=disposition` and `ratification=witness`, written as session
  S1; the agent commit runs as session S2 with no `.typed` line and puts `dB` before `dA`; `dC`, whose
  move carries `ratification=before-placement`, is reordered in the same plant's second commit. The
  plant reaches the loop kit only as S3 does, by running its CLIs, `loop_transition.py record`
  (`TOOL-dDeclaredLoop-3` S5) for each move among them, and imports no loop-kit module. Observed by
  AC3.
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
- **hands-off** `TOOL-dRankedPlan-37` — `read_exit_ratification`, `RATIFYING_EXITS`, the `drafts-cross-session` plant and AC1's move: that unit adds `read_ratifying_exit`, seeds and forges in the plant, imports the set into `show`, guards S4's run of `ratify.py` and spells the move `--field harness=claude-code` (spec audit of units 19 to 29, ids 1, 3, 11, 16, 35)

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
- `read_slot_mode` (`tools/memory-tree/gen_build_index.py:2283-2306`) finds the policy kit through
  `backlog.resolve_kit_dir` and then loads it in process, `sys.path.insert` and `import budgets`
  (:2293-2296), so it is no precedent here: PLAY-dOrderedCharter-7 §4 (its spec :202-205) has a kit
  reach a sibling only by running its CLI, and `tools/memory-tree/kit.toml:8` declares no
  `requires_if` row for `loop`.

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
- **Importing `ratify.py` into the generator, under a `requires_if` row for `loop`.** S1's verb
  already answers, so a subprocess reaches it with no import, and no row's reason holds (§8 F3).
- **The predicate asked with the session forced.** No session id held by a later run is the owner's,
  so forcing one forges consent, which `TOOL-dPlacedRequest-19` S5 exists to refuse.

## 5. Production-readiness checklist

- security — narrows: an agent commit in any session is now refused for reordering rows the owner
  ratified. The fact read is a commit trailer written only by `write_transition` past
  `check_plan_exit`, so it cannot be typed into a README to fake a ratification.
- perf / scale — one `ratify.py --exited` subprocess, holding one `read_transitions` call, per placed
  build per staged README commit.
- error / empty / loading states — no loop kit prints one line and reads no row ratified; an unknown
  slug exits 2 and reads not crossed; a reader that fails or times out exits the check 2 naming the
  build.
- observability — `ratify.py <slug> --exited` prints how and where each build crossed.
- risks — a build that crossed before unit 10's fields existed reads unratified until its next
  crossing; no build has crossed at base, since the loop kit is unbuilt there.
- testing — S4's plant and the reader's own lines.
- migration — none.
- user docs — `help/plan.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant claude-adapter` has recorded the
  `plan.exit` move (`TOOL-dRankedPlan-10` AC2), `python ratify.py tFix --exited` prints
  `plan.exit — crossed · witness · harness claude-code`, the move's sha8 and `ratifying`; over a build
  with no move it prints `plan.exit — not crossed`.
  Red when: the reader answers from anything but the move's trailer, or names a crossing that did not
  happen.
- **AC2** — When a probe imports `ratify.py` and calls `read_exit_ratification` over planted moves
  carrying each of the four `ratification=` values and one carrying none, the three S2 values are in
  `RATIFYING_EXITS` and `before-placement` and `unrecorded` are not.
  Red when: a crossing no owner act gated reads as ratified.
- **AC3** — When `python3 tools/memory-tree/gen_build_index.py --ratified-order --plant
  drafts-cross-session` runs, the S2 commit putting `dB` before `dA` exits 1 naming both builds and
  `planner-drafts-owner-ratifies`, and the commit reordering `dC` exits 0; `grep -c
  "read_plan_ratification" tools/memory-tree/gen_build_index.py` prints 0, and `grep -cE
  "^\s*(import|from) (ratify|loop_transition)\b" tools/memory-tree/gen_build_index.py` prints 0.
  Red when: a later session reorders rows the owner ratified, the check still asks the predicate, or
  the generator loads a loop-kit module.
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
- **F3 — How does the generator learn that a crossing ratifies?** Options: (a) S1's `--exited` line
  carries the verdict, read from `RATIFYING_EXITS` where it lives; (b) the generator parses `<how>`
  against its own copy of the set; (c) the generator imports `ratify.py` under a `requires_if` row
  for `loop`. RESOLVED (agent, 2026-10-28, delegated): (a), rung 1: PLAY-dOrderedCharter-7 §4 lets a
  kit reach a sibling only through its CLI, which rules out (c) while the verb exists, and (b) types
  one fact twice, against `[one-fact]`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's finding 3 (HIGH, item H2,
  shared with finding 37), repairing `TOOL-dRankedPlan-2`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-37`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-28 · §2 S1, S3, S4 · §3 Edges · §4 Evidence, Alternatives rejected · §5 · §6 AC1, AC3 · §8 F3 · §10 · re-grounded by the cross-check record `build/2026-10-28-build-TOOL-dRankedPlan-1-parents-crosscheck.md`, row 45: the generator runs `ratify.py <slug> --exited` as a subprocess and imports no loop-kit module (PLAY-dOrderedCharter-7 §4), the verb's line carries the ratifying verdict, and `read_slot_mode` is no longer cited as the route.

## 10. Reuse audit

The seams extended are `TOOL-dRankedPlan-10` S5's trailer fields, read through dDeclaredLoop's one
transition reader `read_transitions` (`TOOL-dDeclaredLoop-3` S7), and the memory-tree kit's
`backlog.resolve_kit_dir` (`tools/memory-tree/backlog.py:1758`), which finds the loop kit whose CLI
the generator runs; `read_slot_mode`'s in-process load of its sibling (:2293-2296) is not followed. `python
tools/codebase-map/reuse_lookup.py "read how a gate was passed from the transition record trailer
field"` ranked name stems only (`read`, `read_text`, `records`, `field`); none reads a transition, and
the loop kit is unbuilt at base 0689e7fa, so no existing seam fits the reader beyond the transition
reader it calls. The recall query returned `TOOL-dPlacedRequest-19` S5's consent predicate and the
audit's H2 item, which agree with the specs read.

Recall terms used: `python tools/memory-recall/query.py "how is a session-scoped consent predicate kept out of a commit-time guard" --terms "request-consent typed relayed session predicate commit-time guard pre-commit ratified order cross-session plant"`
