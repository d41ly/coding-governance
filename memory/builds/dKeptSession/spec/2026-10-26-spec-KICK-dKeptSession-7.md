# KICK-dKeptSession-7 — dependency coordination: `deps.coordination` switching the dependency gate by the parent's lease, `deps.early-build` admitting Build, and the `confirmed`, `changed` and `landed` notices

**Status:** DEFERRED · rev-3 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 24 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0145@b38efe3e whole
**Carries:** node:policy-key.deps.coordination
**Carries:** node:policy-key.deps.early-build

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-26 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-7-deviation-71.md](../build/2026-10-26-build-KICK-dKeptSession-7-deviation-71.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-7-deviation-72.md](../build/2026-10-26-build-KICK-dKeptSession-7-deviation-72.md) | deviation | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-5 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-25 KICK-dKeptSession-36 KICK-dKeptSession-44 KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-7-1-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-7-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

A dependent build coordinates with the builds its `parents:` names before it waits on them: a parent
is reachable while its build lease is live; at Design's exit a build posts its frozen interfaces to
each dependent as `confirmed`; a dependent's units enter Build once those interfaces are confirmed, as
`deps.early-build` admits; a later change posts `changed` and the landing posts `landed`; and a
dependent whose parent is unreachable enters Build only after the parent lands, as
`deps.coordination` says (coordination item 8, FI-2, FI-5). Each key is seen on strict's value,
`wait-for-landing` and `design-only` (the whole-design audit's C2-F11). At base the position engine's
dependency gate is specced as one rule, any unlanded parent blocks the build
(TOOL-dDeclaredLoop-7 S4), so strict and standard behave alike and no build reaches another
(gap-flow-06).

## 2. Scope (IN)

- **S1** — Reachability, `derive_parent_reach(repo, parent)` in `tools/loop/position.py`: `landed`
  when the parent has landed on the default branch, TOOL-dDeclaredLoop-7 S4's test; else `reachable`
  when the parent's build lease `refs/gov/leases/<parent>/build` reads `live` or `held` in the
  driver's `--claims` rows (TOOL-dPlacedRequest-1 S2, S6; the verdicts of TOOL-dPlacedRequest-17 S3);
  else `unreachable`, for `stale`, `terminal`, `unknown` or no lease. The rows are read by running
  `bash <kit>/unattended.sh --claims` as a subprocess through `resolve_kit_dir`, never by parsing a
  lease ref here. There is no other timeout (coordination `[interpretations]` 1). Observed by AC1,
  AC2 and AC3.
- **S2** — `deps.coordination` (`message-then-progress`, `wait-for-landing`, `order-only`; default
  `message-then-progress`) switches TOOL-dDeclaredLoop-7 S4's dependency gate, per parent not
  `landed`. `wait-for-landing`: the gate holds every Build-step item and after, and Design items run
  (§8 F1). `message-then-progress`: an `unreachable` parent holds as `wait-for-landing` does; a
  `reachable` one holds as `deps.early-build` says (S3). `order-only`: the gate holds nothing. A held
  item makes the engine answer `blocked` with the reason
  `dependency — <parent> · <reach> · <cause> (deps.coordination: <value>)`; an unheld parent prints the
  same line as an `interrupt —` and the answer is unchanged. Observed by AC1, AC2 and AC3.
- **S3** — `deps.early-build` (`confirmed-interfaces`, `design-only`, `anything-coordinated`; default
  `confirmed-interfaces`), read for a `reachable` parent under `message-then-progress`.
  `confirmed-interfaces`: a Build-step item runs once `KICK-dKeptSession-27`'s
  `check_interface_notice <slug> "interfaces <parent>" <file>` exits 0, a `confirmed` or `changed` row
  from the parent whose `content-key` equals the key recomputed over `<file>`, never chosen by arrival
  order. `<file>` is the dependent's view of the parent's interface: the listing
  `git ls-tree -r <w> -- <memory root>/builds/<parent>/spec/` at `<w>`, the `witness` field of the
  parent's build lease record (TOOL-dPlacedRequest-1 S2, field 15 of `CLAIM_ROWS`), the commit that
  records the parent's newest transition on the channel `transitions.record` makes the source (its
  S8), fetched from the remote when absent. `--claims` prints fields 1 to 5 only (its §4 "The rows";
  `print_claims`, `tools/unattended/unattended.sh:2204`), so the field is read through the driver
  verb §8 F5 asks for. Exit 1, a lease with no witness, or a listing that cannot be derived, holds
  with the cause `awaiting confirmed`. `design-only`: Build
  waits for the parent's landing.
  `anything-coordinated`: Build runs while the parent is reachable. Every unit of the dependent counts
  as consuming the parent's interfaces (§8 F2). Observed by AC4, AC5 and AC6.
- **S4** — The `confirmed` notice at Design's exit. When `loop_transition.py record`
  (TOOL-dDeclaredLoop-3 S5) has committed a move from `designing` to `building`, it posts, through
  `KICK-dKeptSession-5`'s `--mail post` run as a subprocess, one message per dependent, every build
  whose README front matter's `parents:` names this slug: kind `confirmed`, to `build:<dependent>`,
  subject `interfaces <slug>`, and `--interface <file>`, unit 27's option, `<file>` the same listing
  S3 derives, taken at the transition commit `write_transition` has just made, the commit the driver
  next records as the lease's `witness` (TOOL-dPlacedRequest-1 S8, §8 F3), so the post carries its
  `content-key`. Where `transitions.record` selects `micro-format` alone the writer makes no commit and
  no commit witnesses (TOOL-dPlacedRequest-1 §4 "The witness under `progress`"), so the listing is
  taken at `HEAD`, and a dependent recomputing at the lease's older `witness` admits Build only where
  the parent's `spec/` listing has not moved since. Where this
  build already posted a `confirmed` to that dependent, the post is `changed`, carrying the new key. A dependent's
  `confirm-request` is answered the same way, a `confirmed` whose `answers` names the request.
  Observed by AC7.
- **S5** — The `landed` notice. `verb_landed` (`tools/unattended/unattended.sh:6316`), on its success
  exit, posts one `landed` message per dependent, subject `landing <slug>`, its body the landed sha. A
  post that fails prints its line and never fails the verb. Observed by AC8.
- **S6** — The keys, each read by running `<sys.executable> <prefix>/policy/policy.py get
  deps.coordination` and `… get deps.early-build` as a subprocess (TOOL-dGroundRules-2 S7's verb),
  `policy.py` found through `loop_lib.py`'s inline `resolve_kit_dir` block (TOOL-dDeclaredLoop-12 S4),
  since a kit imports no sibling kit (TOOL-dGroundRules-1 §4 Evidence). A refusal, or no policy kit
  found, reads the catalogue default with one NOTE naming the key. A policy file naming `preset = "strict"` with no override reads
  `wait-for-landing` and `design-only`, strict's cells in I1 (`tools/policy/presets.toml`, v2:1490-1491),
  through the reader's preset step. Observed by AC9.
- **S7** — The page `help/loop.md` gains the dependency gate's values, the reach words and the three
  notices. Observed by AC10.

## 3. Non-goals (OUT)

- No re-entry on `changed`: the cross-build interface-change re-entry is dIndexedDesign's
  `design.reentry`, which a `changed` message triggers (coordination.md:142-143).
- No landing order and no held landing: `landing.order` and `deps.landing` are dShippedRelease's.
- No `deps.on-parent-withdrawn`: dDeclaredLoop's.
- No lease, verb or verdict: TOOL-dPlacedRequest-1's and -17's; this unit reads `--claims`, and the
  lease's `witness` through the verb §8 F5 asks for.
- No mailbox, kind or post path: `KICK-dKeptSession-5`'s; no content key or supersession rule:
  `KICK-dKeptSession-27`'s.
- No per-unit interface declaration (§8 F2).
- No catalogue rows: dGroundRules-1 S3 writes both keys' rows, owner dKeptSession.

### Edges

- **consumes-from** `KICK-dKeptSession-1` — `presets.toml`, whose strict cells `wait-for-landing` and `design-only` each key is seen on
- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox` and the `--mail post` writer, through which the notices are posted and the confirmations read
- **consumes-from** `KICK-dKeptSession-27` — `content-key`, its `--interface` option and `check_interface_notice`, the recomputed key that decides which confirmation is current, never arrival order
- **consumes-from** external — TOOL-dDeclaredLoop-7's dependency gate and answer precedence, TOOL-dDeclaredLoop-3's writer, TOOL-dPlacedRequest-1's build lease, `--claims` rows and lease `witness`, and dGroundRules' `policy.py get` with its preset step, run as a subprocess
- **hands-off** external — dIndexedDesign's `design.reentry` re-enters a dependent's consuming units on a `changed` message
- **hands-off** `KICK-dKeptSession-35` — `write_dependency_notices` and `verb_landed`'s notice, which that unit gives a pass and a visible refusal line (id 4)
- **hands-off** `KICK-dKeptSession-42` — the notices and S3's listing, which that unit's transition writer reads to acknowledge what the dependent consumed (id 55)
- **hands-off** `KICK-dKeptSession-44` — `derive_parent_reach`, the listing's bytes and `read_dependents`, the batch's S17 and S20 (ids 24, 35)

## 4. Design

### Evidence

- Coordination item 8 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md:130-137`)
  and its interpretations 1 and 2 (:187-191): reachable while the build lease is live, no separate
  timeout; Design's exit posts the frozen interfaces, which is how a frozen design confirms them.
- FI-2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md:78-82`):
  "progress to the best of their ability, otherwise build waits for parent's landing (if they cannot
  communicate)". FI-5 (:109-111) and its settled text (:127-130): a dependent designs at any time and
  enters Build once the interfaces it consumes are confirmed.
- v2:1165-1166 give the values and defaults; strict sets `wait-for-landing` and `design-only`
  (v2:1490-1491).
- The engine's gate today: "dependency gates (a build the README's `parents:` names that has not
  landed on the default branch)", answer `blocked` at precedence 5 (TOOL-dDeclaredLoop-7 S4, S5).
- `verb_landed` is the driver's landing record (`tools/unattended/unattended.sh:6316`).

### The gate, per parent not landed

| `deps.coordination` | reach | `deps.early-build` | Design items | Build items |
|---|---|---|---|---|
| `wait-for-landing` | any | not read | run | held: `not landed` |
| `message-then-progress` | `unreachable` | not read | run | held: `unreachable` |
| `message-then-progress` | `reachable` | `confirmed-interfaces` | run | run once a current confirmation holds, else held: `awaiting confirmed` |
| `message-then-progress` | `reachable` | `design-only` | run | held: `not landed` |
| `message-then-progress` | `reachable` | `anything-coordinated` | run | run |
| `order-only` | any | not read | run | run |

A held item answers `blocked`; the engine's precedence is otherwise untouched.

### The notices

```
confirmed · to build:<dependent> · subject interfaces <slug> · content-key <12 hex>   first Design exit
changed   · to build:<dependent> · subject interfaces <slug> · content-key <12 hex>   every later Design exit
landed    · to build:<dependent> · subject landing <slug>    · body <landed sha>       verb_landed's success
```

The dependents are read from every `memory/builds/*/README.md` front matter's `parents:`, the same
key the engine reads for the build's own parents.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_parent_reach`, `derive_dependency_hold`, `read_dependents` | Python functions, `tools/loop/position.py` | `py.function`, verb-first |
| `write_dependency_notices` | Python function, `tools/loop/loop_transition.py` | `py.function`, verb-first |
| `landed`, `reachable`, `unreachable` | reach words on the engine's lines | none |
| `deps-wait`, `deps-unreachable`, `deps-order`, `deps-confirmed`, `deps-design-only`, `deps-anything`, `deps-strict` | `--plant` cases of `position.py --fixture` | none |

### Migration

None: no confirmation exists before this unit; a dependent with a reachable parent and no
confirmation holds its Build items under the default, exactly the clause's rule.

### Rollout

Live with the engine and the mailbox. The notices post only where a README's `parents:` names the
moving build, so a build no other build depends on posts nothing.

### Files touched (estimate)

- `tools/loop/position.py`: the reach, the switched gate, seven plants
- `tools/loop/loop_transition.py`: the Design-exit notices
- `tools/unattended/unattended.sh`: the `landed` notice in `verb_landed`, `KIT_UNATTENDED_VERSION` moved
- `tools/unattended/unattended.test.sh`: the landed-notice arm
- `help/loop.md`: the gate's values and the notices
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`

### Alternatives rejected

- **A reply timeout as the reach test.** FI-6's settlement was revised to the lease (coordination
  `[interpretations]` 1, RC-5): no timeout applies.
- **The gate holding Design too under `wait-for-landing`.** FI-2 offered "Design waits too" and the
  owner did not pick it; the value set has no such member.
- **The engine parsing lease refs itself.** A second reader of the lease record beside `read_claims`.

## 5. Production-readiness checklist

- security — the notices pass through unit 5's post path and its body check; the engine's reads are
  subprocesses with fixed argv.
- perf / scale — one `--claims` and one `--mail read` per engine call that meets an unlanded parent;
  one post per dependent per Design exit and per landing.
- error / empty / loading states — an unreadable `--claims` reads `unreachable`, which holds Build and
  never admits it; an unreadable or absent lease `witness` holds Build as `awaiting confirmed`; a
  failed notice prints its line and fails no transition or landing.
- observability — every held item names its parent, reach, cause and value; every notice is a mail
  message the dependent's interrupt lists.
- risks — under the default, a dependent with a live parent that never confirms waits for the
  landing, which is the clause's fallback; a parent spec revised during Build moves the listing and
  holds its dependents until its next Design exit posts `changed` or it lands, which fails closed.
- testing — the plants and the arm of §6 and §7.
- migration — none.
- user docs — `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python position.py --fixture --plant deps-wait` runs with
  `deps.coordination = "wait-for-landing"`, a parent unlanded and its lease `live`, a next item of the
  Design step answers `act` with the `interrupt — dependency` line, and a next item of the Build step
  answers `blocked` naming the parent, `not landed` and the value.
  Red when: Design is held, or Build runs before the landing.
- **AC2** — When `--plant deps-unreachable` runs under `message-then-progress` with the parent's lease
  planted `stale`, the Build item answers `blocked` naming `unreachable`; with the lease `live` and a
  current confirmation, it answers `act`.
  Red when: an unreachable parent admits Build, or a reachable confirmed one holds it.
- **AC3** — When `--plant deps-order` runs with `deps.coordination = "order-only"` and the parent
  unlanded and unreachable, the Build item answers `act` and prints the dependency interrupt.
  Red when: `order-only` holds anything.
- **AC4** — When `--plant deps-confirmed` runs under the defaults with the parent reachable, the Build
  item answers `blocked` naming `awaiting confirmed` while no confirmation is in the mailbox, `act`
  once a `confirmed` whose `content-key` recomputes is, and `blocked` again when the newest
  confirmation's key does not recompute.
  Red when: Build runs on no confirmation, or on one whose key is stale.
- **AC5** — When `--plant deps-design-only` runs with `deps.early-build = "design-only"` and the parent
  reachable, the Design item answers `act` and the Build item `blocked` naming `not landed`.
  Red when: `design-only` admits Build before the landing.
- **AC6** — When `--plant deps-anything` runs with `deps.early-build = "anything-coordinated"`, the
  parent reachable and no confirmation, the Build item answers `act`; with the lease `stale` it is
  `blocked` naming `unreachable`.
  Red when: `anything-coordinated` holds a reachable parent's dependent, or admits an unreachable one.
- **AC7** — When `python loop_transition.py record` moves a fixture parent from `designing` to
  `building` with one dependent README naming it in `parents:`, one `confirmed` message to
  `build:<dependent>` with subject `interfaces <parent>` and a 12-hex `content-key` is in the mailbox,
  the key recomputed over the parent's `spec/` listing at the move's transition commit, with
  `--witness` planted at an older ancestor whose listing differs; a second move out of Design posts
  `changed` with a different key and no second `confirmed`.
  Red when: Design's exit posts nothing, a later exit posts `confirmed` again, or the key is taken at
  `--witness`.
  fixture: a scratch repository with two builds, a bare origin under `%TEMP%` and `RUN_CLAIMS=on`.
- **AC8** — When `bash tools/unattended/unattended.sh --landed <parent>` succeeds in that fixture, one
  `landed` message to `build:<dependent>` carrying the landed sha is in the mailbox; with the post
  planted to fail, the verb still exits 0 and prints the post's line.
  Red when: a landing posts no notice, or a failed notice fails the landing.
- **AC9** — When `--plant deps-strict` runs with a policy file naming `preset = "strict"` and no
  override of either key, it gives AC1's answers and AC5's, the keys reading `wait-for-landing` and
  `design-only` with the source `preset`. This is each key seen on strict's value.
  Red when: a strict-named file behaves as standard, C2-F11's consequence.
- **AC10** — When `grep -n 'deps.coordination\|deps.early-build\|unreachable\|landed'` runs over
  `loop.md`, the loop kit's help page, each is found in its dependency section.
  Red when: the gate's values are undocumented.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/loop/position.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC9 · the seven `--plant` cases, `deps-wait` staged red by the gate read without its value · none
New arm: tools/loop/selftest.py · covers AC7 · the Design-exit notices over a two-build fixture, red with the notice call left out · none
New arm: tools/unattended/unattended.test.sh · covers AC8 · the landed notice, staged by a post planted to fail · `FLOOR_ASSERTIONS` and its shard floor rise by the arm's count, counted off the diff

## 8. Open questions

- **F1 — Which items does the dependency gate hold?** Options: (a) the Build step's items and every
  later step's, Design items running, as FI-2's answer and FI-5's settled text say a dependent designs
  at any time; (b) every item, TOOL-dDeclaredLoop-7 S4's single rule, which is "Design waits too", an
  option FI-2 offered and the owner did not take. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1,
  FI-2 and FI-5. widens: none · relaxes: none
- **F2 — Which of a dependent's units consume a parent's interfaces?** Options: (a) every unit of the
  dependent, since no record declares per-unit consumption and holding a unit that consumes nothing
  costs only waiting; (b) a new per-unit declaration, a surface no clause names. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — What interface text does a `confirmed` carry the key of?** Options: (a) the listing
  `git ls-tree -r` of the build's `spec/` folder at the transition commit that leaves Design, the
  record of its frozen feature design, which the dependent recomputes at the parent lease's `witness`,
  so any spec change since the confirmation holds the dependent until a `changed` names it; (b) a
  declared interfaces section, a record kind no build has landed.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, re-resolved on TOOL-dPlacedRequest-1 S8 at
  rev-5, whose lease `witness` is a commit recording a transition of the build, not the `--witness`
  ancestor TOOL-dDeclaredLoop-3 §4 step 3 resolves, so the key is taken at the transition commit, and
  at `HEAD` where `micro-format` alone makes none; first resolved on rung 3, coordination
  `[interpretations]` 2's "Design's exit posts each frozen feature's declared interfaces".
  widens: none · relaxes: none
- **F4 — How is a later change told additive from breaking?** Options: (a) not here: every later
  Design exit posts `changed` with the new key, and dIndexedDesign's `design.reentry` judges the
  change; (b) a classifier in this unit, which no record defines. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F5 — How does S3 read the parent lease's `witness`, when `--claims` prints fields 1 to 5 and
  `witness` is field 15?** TOOL-dPlacedRequest-1 §4 "The rows" keeps `print_claims` at five fields,
  the shape TOOL-dDeclaredLoop-8 S7 extends, and its S5 offers no verb printing one lease's fields.
  Options: (a) an ask to dPlacedRequest for a read verb printing one lease's `witness`, run as a
  subprocess through `resolve_kit_dir` as S1 runs `--claims`; (b) an ask that `--claims` print
  `witness` as a sixth field, which moves a row shape another reader parses; (c) parsing the lease
  ref's commit here, a second lease parser beside `read_claims`, which §4's rejected alternative
  refuses. (a) keeps `read_claims` the one parser and the five-field row unchanged; its cost is a
  wait, since until it lands S3 reads no witness and `confirmed-interfaces` holds every reachable
  parent's dependents as `awaiting confirmed`, the landing fallback, and AC4's admitting half runs on
  a stub driver only. Recommendation (a). Open for the owner: the ask the build run files is
  "TOOL-dPlacedRequest-1: a verb `unattended.sh --lease show build <slug>` prints the lease's `witness`
  field from `CLAIM_ROWS`, or `-` where it holds none".

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 7, scout C row 1, Shared interfaces I1,
  I8, I19, I20 and I22, coordination item 8 and its interpretations, FI-2, FI-5, v2:1165-1166 and
  v2:1490-1491.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-35`, `KICK-dKeptSession-42`,
  `KICK-dKeptSession-44` mirrored, the other ends of the edges the round-1 spec audit's promoted
  units declare; no other section moved.
- rev-3 · 2026-10-26 · §2 S3, S4, S6 · §3 Non-goals, Edges · §5 · §6 AC7 · §8 F3, F5 · re-grounded on
  dPlacedRequest at `2740f0a3d` and dDeclaredLoop at `783f1ad3a` by the cross-check record
  `build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md`, rows 23, 24 and 26: the lease
  `witness` is read through the verb F5 asks for, the listing is taken at the transition commit, and
  the keys are read by `policy.py get` as a subprocess.

## 10. Reuse audit

The seam extended is TOOL-dDeclaredLoop-7 S4's dependency gate in `tools/loop/position.py`, its one
"not landed" test kept as the `landed` reach word; the reach reads TOOL-dPlacedRequest-1's build lease
through the driver's `--claims` rows, the one lease reader, and the notices post through unit 5's
writer. `tools/loop/` is absent at base, so the engine and the transition writer are parents' spec
sections, read at `origin/main`; `verb_landed` is verified at `tools/unattended/unattended.sh:6316`.
`python tools/codebase-map/reuse_lookup.py "a dependency gate switched by policy and parent
reachability"` ranked `load_policy`, `check_gate_wall`, `parse_gate_profile` and `read_gate_policy`,
name stems only; none is a dependency gate. `python tools/memory-recall/query.py "how does a dependent
build coordinate with its parent"` returned this build's brief, scout C's row 1 and C2-F11 in the
walk return; scout C's note that the parent spec names dWellOiledMachine for the mailbox holds and is
`KICK-dKeptSession-10`'s ask, not this unit's.

Recall terms used: deps.coordination deps.early-build confirmed changed landed parent lease reachable wait-for-landing dependency gate
