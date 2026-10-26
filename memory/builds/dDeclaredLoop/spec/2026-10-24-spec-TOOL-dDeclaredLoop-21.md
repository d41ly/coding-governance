# TOOL-dDeclaredLoop-21 — the review round bounds as policy keys: review.max-rounds, the design rounds and follow-ups, REVIEW_ROUNDS and RUNAWAY_CEILING retired

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 26 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0106@90aa01b6 whole
**Carries:** node:policy-key.review.follow-up
**Carries:** node:policy-key.review.design.rounds
**Carries:** node:policy-key.review.design.round-count
**Carries:** node:policy-key.review.max-rounds

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-readers-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-readers-fix-return.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-21-deviation-211.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-21-deviation-211.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-readers-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-readers-fix-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

Every review loop's bound becomes a policy value the owner sets in one file: `review.max-rounds` bounds
every loop, the closing review's follow-ups included, the design audit's rounds follow
`review.design.rounds` and `review.design.round-count`, and the closing review's follow-ups follow
`review.follow-up`. Today the backstop is a file constant, `RUNAWAY_CEILING="8"`
(`tools/unattended/unattended.sh:774`), the spec bound a conf key, `REVIEW_ROUNDS`
(`tools/unattended/unattended.sh:779`), and the closing review had no bound but the constant (the
stall-and-loop round, P39; v2:1253-1255).

## 2. Scope (IN)

- **S1** — The one reader of the four keys, `read_review_bounds(root, rev=None)` in the new module
  `tools/loop/review_bounds.py`, each key read through dGroundRules-2's `resolve` (I10), with the
  catalogue defaults until a file sets them: `review.max-rounds` 3, `review.design.rounds` `one`,
  `review.design.round-count` 2, `review.follow-up` `after-high`. It derives two bounds: the spec bound,
  1 under `one`, `review.design.round-count` under `fixed-count`, and `review.max-rounds` under each
  `until-*` value; and the closing bound, 1 under `never` and `review.max-rounds` otherwise. Its CLI,
  `python tools/loop/review_bounds.py show [--rev <rev>]`, prints
  `max-rounds=<n> spec-bound=<n> closing-bound=<n> follow-up=<value>` on one line. Observed by AC1, AC3.
- **S2** — The refusal. A `review.design.round-count` above `review.max-rounds` is refused under
  `fixed-count`, naming both keys and both values, and a count equal to it is admitted (v2:1254). Any
  value below 1 or outside a key's catalogued values is refused. The refusal lives in the loop kit, so
  it holds with `unattended.sh` absent: `check_review_bounds` runs as an arm of `loop_lib.py --check`,
  the leg `loop definition` (TOOL-dDeclaredLoop-1 S7), over the tree's policy file, and the module's
  plants run by `python tools/loop/review_bounds.py --fixture`, the leg `loop review bounds fixtures` in
  `tools/gate-legs.json`, declared in `tools/loop/kit.toml`. Observed by AC1 and AC2.
- **S3** — `RUNAWAY_CEILING` retired into `review.max-rounds`. `review_state`
  (`tools/unattended/unattended.sh:12610-12618`) keeps its test order, zero, then non-decrease, then the
  ceiling, then the bound, with the ceiling read as one round past `review.max-rounds`
  (`n + 1 > max-rounds`), dFairHearing-17's `deriveRoundState` order; `verb_review`'s bound
  (:12769) takes the closing bound on the slug subject and the spec bound on every other, and the exit
  sentences (:12857-12858) name the key. **Readers:** by name: `tools/unattended/unattended.sh`
  (:774, :12611, :12615, :12769, :12857), `tools/unattended/check-unattended.sh` (:624, :726-727, :821,
  :876), `tools/unattended/unattended.test.sh` (:7073-7075), `tools/unattended/check-unattended.test.sh`
  (:1097-1100), `tools/unattended/runlog-writer.test.sh` (:396), and `tools/workflows/tier2-review.test.sh`,
  whose parity arm dFairHearing-17 S5 adds slices the constant's line and takes the ceiling as its
  own variable instead · by value: the `ceiling of 8` arms of `tools/unattended/unattended.test.sh`
  (:9310, :9316), each re-pointed to `review.max-rounds`'s default of 3. Observed by AC4.
- **S4** — `REVIEW_ROUNDS` retired into `review.design.rounds` and `review.design.round-count`, with
  `REVIEW_ROUNDS_DEFAULT` (:447), its `read_bound_key` call (:779), its strict-below refusal (:783) and
  the NOTE it prints. **Readers:** by name: `tools/unattended/unattended.sh` (:447, :507, :565, :767,
  :779-783, :12599, :12768, :12858), `tools/unattended/check-unattended.sh` (:1850-1876, :1881-1892,
  :2652, :2721-2737), `tools/unattended/kit.toml` (:174, `optional_keys`), `.unattended.conf` (:111),
  `tools/unattended/.unattended.conf.example` (:118), `tools/unattended/lib-unattended.sh` (:222),
  `tools/unattended/README.md` (:359, :367), `tools/unattended/PROTOCOL.template.md` (:487) and its
  render `memory/guides/UNATTENDED-PROTOCOL.md`, `tools/unattended/VERBS.template.md` (:243, :798) and
  its render `memory/guides/UNATTENDED-VERBS.md`, `tools/memory-tree/BUILD-METHOD.template.md` (:144)
  and its render `memory/guides/BUILD-METHOD.md`, and `tools/workflows/unattended-build.template.js`
  (:224, :317) and its render `tools/workflows/unattended-build.js` · by value: the `REVIEW_ROUNDS="7"`
  fixture lines of `tools/unattended/unattended.test.sh` (the `mkconf` default at :243 and its
  seventh-positional caller at :7211, the seven conf heredocs from :10543 to :16542, and the two
  `printf` confs at :17103 and :17241) and `tools/unattended/resume-tick.test.sh` (:166), the default read at
  `tools/unattended/unattended.test.sh:9295-9301`, and the round-bound arms of
  `tools/unattended/check-unattended.test.sh` (:756, :5958-6019), and the copied refusal of
  `tools/unattended/runlog-writer.test.sh` (:388, :396), each re-pointed to a policy file
  setting `review.design.rounds = "fixed-count"` and `review.design.round-count`. Observed by AC5.
- **S5** — `review.follow-up` on the closing review's subject: `never` gives it one round; `after-high`
  re-arms a follow-up only after a round standing on a blocker or a high, read from the count the
  round records, which TOOL-dDeclaredLoop-32 widens to blockers and highs; `while-finding` is admitted
  and bounded by `review.max-rounds` here, its stopping rule TOOL-dDeclaredLoop-32's, as every
  `until-*` value of `review.design.rounds` is. Observed by AC3.
- **S6** — `tools/unattended/check-unattended.sh` re-pointed. Check 2's ceiling (:624) is read from
  `python <prefix>/loop/review_bounds.py show`, an unreadable value refusing as the empty ceiling does
  today (:726-727), and its awk arm (:821, :876) compares each subject's rounds with that subject's
  bound. Check 19 (:2719-2738), the owner-only round bound, is re-pointed and kept: its
  `read_rounds_of` (:1859-1876) reads the spec bound at each commit and each parent through
  `review_bounds.py show --rev`, so a run commit moving the effective bound in `.governance/policy.toml`
  reds as a conf edit does today. Observed by AC6.
- **S7** — The upgrade step (I25). An `[[upgrade]]` row `unattended/review-rounds-to-policy` in
  `tools/unattended/kit.toml`, its program `tools/govkit/steps/review_rounds.py`, on dSafePassage-1's
  step kind: up reads an adopter's effective `REVIEW_ROUNDS`, writes nothing for 1, which is the
  catalogue default `one`, and for N above 1 writes `review.design.rounds = "fixed-count"` and
  `review.design.round-count = N`, adding `review.max-rounds = N` when N exceeds 3 so the adopter's
  bound reads the same; then it deletes the conf line. Down restores both files byte-identical.
  Observed by AC7.
  **Readers:** by name: in an adopter's tree the line is read only by its installed copy of this kit,
  the same files S4 re-points in this unit, so the release that ships the step ships no reader of it:
  `tools/unattended/unattended.sh` (:779, its `read_bound_key` call), `tools/unattended/check-unattended.sh`
  (:1859-1876, `read_rounds_of`), `tools/unattended/kit.toml` (:174, `optional_keys`) and
  `tools/unattended/.unattended.conf.example` (:118); S4 carries the full list, and gov's own line,
  `.unattended.conf` (:111), is S9's · by value: the adopter's N, read today by `verb_review`'s bound
  in `tools/unattended/unattended.sh` (:12769) and by check 19 through `read_rounds_of` in
  `tools/unattended/check-unattended.sh`, each reading `review.design.round-count` after S4 and S6, the
  key the step writes N into.
- **S8** — The shared step, extracted at this second instance (I25): the move of one conf key into
  policy keys and back, `tools/govkit/steps/conf_to_policy.py`, which dSafePassage-1 S6's
  `tools/govkit/steps/fanout_cap.py` and S7's program both call, re-pointed in this unit with their
  bytes out unchanged. Observed by AC8.
- **S9** — Gov migrated first: S7's up runs on gov's own tree in this unit's commit, and gov's
  `REVIEW_ROUNDS="1"` (`.unattended.conf:111`) maps to the default, so the line goes and no policy key is
  written. Observed by AC7.
- **S10** — The page `help/loop.md` (TOOL-dDeclaredLoop-1 S7) gains a section on the review bounds:
  the four keys, the two derived bounds, and that a count equal to `review.max-rounds` is admitted and
  raising any of them is the owner's. Observed by AC9.

## 3. Non-goals (OUT)

- No stopping rule for an `until-*` or `while-*` value, no blocker-and-high count, and no promotion of
  a NON-CONVERGENT or CEILING round's findings: TOOL-dDeclaredLoop-32's convergence routing, which also
  passes `review.max-rounds` to dFairHearing-17's harness as `roundLimit`.
- No `review.trigger` refusal and no disposal: TOOL-dDeclaredLoop-20's items read the bound.
- No catalogue row: dGroundRules-1 S3 writes one per v2 row, and dGroundRules-11 gives the loop bounds
  `direction = "raise-loosens"`, which makes raising each the owner's.
- No write to `.governance/policy.toml` by an agent: gov's own value maps to the default, so the step
  writes none here, and an adopter's step runs under govkit's update.
- No run of the unattended kit's own suites at the close: README rule 8 waives them for this landing,
  so the by-value fixture edits are made and their clean reading is owed with PLAY-dClosedLoop-13.
- No `help/` page on the unattended conf: none exists, and the loop page carries the keys.

### Edges

- **hands-off** `TOOL-dDeclaredLoop-32` — `review.max-rounds`, with the spec and closing bounds, which the convergence routing stops `until-*` and `while-*` loops against and passes as `roundLimit`
- **hands-off** `TOOL-dDeclaredLoop-20` — `review.max-rounds`, the bound `review.trigger` refuses another round past
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 9, 39, 44, 63, each a scope item of that unit

## 4. Design

### The bounds

| Subject | Bound | Ceiling (`CEILING` past it) |
|---|---|---|
| the closing review (the build slug) | 1 under `never`, else `review.max-rounds` | `review.max-rounds` |
| a spec audit (any other subject) | 1, `review.design.round-count` or `review.max-rounds`, by `review.design.rounds` | `review.max-rounds` |

`review_state` then reads, for round `r = n + 1`: `CONVERGED` at count 0; `NON-CONVERGENT` when the
count did not fall; `CEILING` when `r > max-rounds`; `BOUNDED` when `r >= bound`; `CONVERGING`
otherwise. A bound equal to the ceiling is reached as `BOUNDED`, the equality S2 admits; today the
ceiling's `>=` test fired first, which is why `:783` refused equality.

### How the shell reads it

`verb_review` and `--preflight` call `"$py" "<prefix>/loop/review_bounds.py" show`, the python from
the driver's inlined `resolve_python` (`tools/unattended/unattended.sh:392-422`), and split the one
line on spaces into `MAX_ROUNDS`, `SPEC_BOUND`, `CLOSING_BOUND` and `FOLLOW_UP`; nothing is sourced, and
no shell copy of the policy parse is added (I10). A refusal's stderr is passed through and the verb
fails 37. The load-time refusal at `:783` moves into these two callers, so a driver verb that reads no
review bound starts no python.

### Migration

The upgrade step of S7, run by govkit's update over an adopter. A conf line left after the step is
an unknown key once `kit.toml` drops it from `optional_keys`, which govkit's conf check names.

### Rollout

Live at landing. Gov's spec bound stays 1; the closing review's backstop moves from 8 rounds to 3,
v2:1255's default, and a round past 3 now reads `CEILING`.

### Files touched (estimate)

- `tools/loop/review_bounds.py` (new)
- `tools/loop/loop_lib.py`: `--check` calling `check_review_bounds`
- `tools/loop/kit.toml`: the module and the leg declared
- `tools/gate-legs.json`: the leg `loop review bounds fixtures`
- `help/loop.md`: the section of S10
- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/kit.toml`
- `tools/unattended/.unattended.conf.example`
- `.unattended.conf`
- `tools/unattended/lib-unattended.sh`: the comment at :222
- `tools/unattended/README.md`
- `tools/unattended/PROTOCOL.template.md` and its render `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/unattended/VERBS.template.md` and its render `memory/guides/UNATTENDED-VERBS.md`
- `tools/memory-tree/BUILD-METHOD.template.md` and its render `memory/guides/BUILD-METHOD.md`
- `tools/workflows/unattended-build.template.js` and its render `tools/workflows/unattended-build.js`
- `tools/govkit/steps/conf_to_policy.py` (new), `tools/govkit/steps/review_rounds.py` (new),
  `tools/govkit/steps/fanout_cap.py`
- `tools/unattended/unattended.test.sh`, `tools/unattended/check-unattended.test.sh`,
  `tools/unattended/resume-tick.test.sh`, `tools/unattended/runlog-writer.test.sh`
- `tools/workflows/tier2-review.test.sh`: dFairHearing-17's parity arm

### Alternatives rejected

- **Keep the equality refusal.** v2:1254 holds the count "at or below" the ceiling, and the clause asks
  a count equal to it admitted.
- **Map `REVIEW_ROUNDS` straight onto `review.design.round-count`.** The count is read only under
  `fixed-count` (v2:1254), so a moved value under the default `one` would change nothing an adopter set.
- **A third copied step program.** dSafePassage-1 S6 and S7 already move conf files into policy keys;
  the [reuse] rule extracts the shared step here.

## 5. Production-readiness checklist

- security — the policy file is read, never written by an agent; raising any bound stays the owner's
  under dGroundRules-6's guard and dGroundRules-11's direction.
- perf / scale — one python start per `--review` and per preflight.
- error / empty / loading states — an unreadable or out-of-range value refuses by key; an absent file
  reads the catalogue defaults.
- observability — `show` prints every derived bound; the exit sentences name the key they stopped at.
- risks — a closing review that ran past 3 rounds before now stops at `CEILING` sooner; v2 chose 3.
- testing — direct probes of `review_bounds.py`, the driver and the leg in scratch repositories; the
  suite arms in §7, the unattended ones waived for this landing.
- migration — the step of S7; gov's own value maps to the default.
- user docs — `help/loop.md` gains the bounds' section; the unattended README, protocol and verbs
  reference are re-worded.

## 6. Acceptance criteria

- **AC1** — When `python review_bounds.py show --rev HEAD` runs in a scratch repository whose committed
  policy file sets `review.design.rounds = "fixed-count"`, `review.design.round-count = 4` and
  `review.max-rounds = 3`, it exits 2 naming `review.design.round-count`, 4 and 3; with the count set to
  3 it exits 0 and prints `spec-bound=3`.
  Red when: the comparison keeps the driver's strict-below form, so a count equal to the ceiling is
  refused.
- **AC2** — When the same planted policy file is committed in a scratch clone of the tree from which
  `tools/unattended/unattended.sh` has been deleted, `python review_bounds.py show --rev HEAD`, run in the
  clone's loop kit, still exits 2 naming `review.design.round-count`.
  Red when: the bound is read out of the driver, so deleting it silences the refusal.
  fixture: the clone sits under `%TEMP%/rbclone`, a short path, since the scratch path is too long for
  a clone on Windows.
- **AC3** — When `python review_bounds.py show --rev HEAD` reads policy files setting each of
  `review.follow-up` = `never`, `after-high` and `while-finding`, it prints `closing-bound=1`, `3` and
  `3`; and with no policy file it prints `max-rounds=3 spec-bound=1 closing-bound=3 follow-up=after-high`.
  Red when: `never` reads the ceiling, so a closing review the owner set to one round runs follow-ups.
- **AC4** — When `review_state` is sliced out of `tools/unattended/unattended.sh` and called with
  `MAX_ROUNDS=3` over prior counts `5 4` and a count of `3` with bound 3, it prints `BOUNDED`, and over
  `5 4 3` and `2` it prints `CEILING`; `grep -c RUNAWAY_CEILING tools/unattended/unattended.sh` prints 0.
  Red when: the ceiling is tested as `r >= max-rounds`, so the bound equal to it reads `CEILING`.
- **AC5** — When `git grep -n REVIEW_ROUNDS -- tools .unattended.conf` runs at this unit's commit, it
  prints only the upgrade step's program and its row in `tools/unattended/kit.toml`, the one place the
  retired key's name is still read.
  Red when: a by-value fixture still writes `REVIEW_ROUNDS="7"`, so a suite arm grades a key no reader
  reads.
- **AC6** — When `bash tools/unattended/check-unattended.sh` runs in a scratch repository whose run's
  own commit raises `review.design.round-count` in the policy file, it fails check 19 naming the
  commit; and with `review_bounds.py` absent from the scratch tree it fails check 2 naming the unread
  ceiling.
  Red when: check 19 still reads `.unattended.conf`, so the raise in the policy file passes.
- **AC7** — When `python review_rounds.py up` runs over three scratch targets whose conf holds
  `REVIEW_ROUNDS="1"`, `"2"` and `"5"`, the first gains no policy key, the second gains
  `review.design.rounds = "fixed-count"` and `review.design.round-count = 2`, the third those with 5
  and `review.max-rounds = 5`, each conf losing the line; `down` restores each pair byte-identical.
  Red when: N above 3 is written without raising `review.max-rounds`, so the adopter's own bound is
  refused after the step.
- **AC8** — When `python fanout_cap.py up` runs over dSafePassage-1 S6's scratch target before and after
  the extraction, the files it writes are byte-identical, and the program imports `conf_to_policy`.
  Red when: the shared step is copied into the new program and the first keeps its own.
- **AC9** — When `grep -n "review.max-rounds" loop.md` runs over the help page at this unit's commit, it
  finds the section naming the four keys and the admitted equality.
  Red when: the keys move into the policy file and no page says where an owner sets the bound.

## 7. Gates

`unattended kit gate` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `routed-commits selftest` · `build-method size` · `unattended protocol size` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/review_bounds.py · covers AC1 AC2 AC3 · the `loop review bounds fixtures` leg's plants, its failing case staged by a count above the ceiling read with the strict-below form · none
New arm: tools/govkit/selftest.py · covers AC7 AC8 · a step tree with no `review_rounds.py` and with `fanout_cap.py` unextracted · none
New arm: tools/unattended/unattended.test.sh and tools/unattended/check-unattended.test.sh · covers AC4 AC6 · the base driver's `RUNAWAY_CEILING` and conf-keyed check 19 · waived for this build's landing by README rule 8, so their clean reading is owed with PLAY-dClosedLoop-13

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation,
  2026-10-24: `DRAFT` is not in the tuple. Liveness: the tuple would list it if the vocabulary admitted
  it. RESOLVED (agent, 2026-10-24, delegated): `OPEN`.
- **F2 — Where does the round-count refusal live, so it holds with `unattended.sh` deleted?** Options:
  (a) the loop kit's `review_bounds.py`, called by the driver and run as an arm of the loop kit's
  check; (b) `check-unattended.sh`, reading the policy file; (c) a new catalogue field in dGroundRules'
  schema. (b) cannot run without the driver it reads fifteen sets from; (c) re-specs a parent's
  contract. RESOLVED (agent, 2026-10-24, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F3 — What does an `until-*` or `while-*` value bound here?** Options: (a) `review.max-rounds`, its
  stopping rule TOOL-dDeclaredLoop-32's; (b) refuse those values until that unit lands. Both units build
  in one run, and v2:1255 bounds every loop by the key. RESOLVED (agent, 2026-10-24, delegated): (a),
  by rung 1.
- **F4 — Editing `tools/memory-tree/BUILD-METHOD.template.md` M4 and the unattended protocol's conf
  table changes governance carriers; does the build's grant cover it?** The clause retires
  `REVIEW_ROUNDS` with its readers derived and each re-pointed, and both carriers read it by name.
  RESOLVED (agent, 2026-10-24, delegated): covered, rung 3.
  grants: PLAY-dClosedLoop-3 the REVIEW_ROUNDS mentions in tools/memory-tree/BUILD-METHOD.template.md, tools/unattended/PROTOCOL.template.md and their renders re-worded to the policy keys

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 21, v2:1236 and :1253-1255, scout C's
  row and conflicts 1 to 5, dSafePassage-1 S6 and S7 and dFairHearing-17, read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.

## 10. Reuse audit

The seams extended are the driver's round predicate `review_state`
(`tools/unattended/unattended.sh:12610-12618`) and its caller (:12769), the leg's ceiling read (`core_of`
at `tools/unattended/check-unattended.sh:624`) and check 19's `read_rounds_of` (:1859-1876), and
dSafePassage-1's step kind with its first conf-to-policy program, whose shared part S8 extracts.
`python tools/codebase-map/reuse_lookup.py "move a conf round bound into a policy key with an upgrade step"`
ranked name stems (`key`, `load_conf`, `parse_conf`, `step` in `tools/govkit/govkit.py`) and found no
upgrade-step code, since `tools/govkit/upgrade_steps.py` is specced and unbuilt. `python
tools/memory-recall/query.py` returned scout C's row, the packet's clause and aWokenSentinel's
measurement that `REVIEW_ROUNDS` bounds one subject while promotions mint fresh ones
(`memory/builds/aWokenSentinel/BACKLOG.md:5`), the cascade TOOL-dDeclaredLoop-30's budget closes. Scout
C's line numbers agree with source at base, and its eleven by-value fixtures are the ten lines of the
driver's suite, the `mkconf` default and two `printf` confs among them, and one in the resume suite,
which S4 lists by line.

Recall terms used: REVIEW_ROUNDS RUNAWAY_CEILING review.max-rounds round bound BOUNDED CEILING review_state upgrade step policy key
